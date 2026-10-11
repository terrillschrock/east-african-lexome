"""
EALex CLDF Regeneration Script (v2, October 2026)
==================================================
Reads the master spreadsheet and writes CLDF-format files to the cldf/ folder.

USAGE
-----
    python3 regenerate_cldf.py MASTER.xlsx PATH/TO/REPO/cldf

(or edit the two defaults below and run with no arguments).

Export rules
------------
* Every column with a header in a master sheet is exported, in sheet order,
  except those listed in EXCLUDE (internal bookkeeping).
* Master names that differ from CLDF names are mapped in RENAME
  (MeaningTable -> parameters.csv; FormTable.Meaning_ID -> Parameter_ID).
* FormTable rows with a blank ID get the next free number (form-00000NNN).
  IDs already present are never changed. Because the master is not modified,
  paste the printed new IDs back into the master once you publish, so that
  they stay fixed.
* Cached formula values are exported (open and save the master in Excel or
  LibreOffice first, so the values are current).
"""
import csv, os, re, sys

try:
    from openpyxl import load_workbook
except ImportError:
    sys.exit("openpyxl missing: pip install openpyxl")

SPREADSHEET = os.path.expanduser("~/Documents/Linguistics/East African Lexome/EALex_Master.xlsx")
REPO_CLDF_FOLDER = os.path.expanduser("~/Documents/GitHub/east-african-lexome/cldf")
if len(sys.argv) >= 3:
    SPREADSHEET, REPO_CLDF_FOLDER = sys.argv[1], sys.argv[2]

# sheet -> (output file, columns to leave out, {master name: CLDF name})
TABLES = [
    ("LanguageTable",   "languages.csv",     {"Citation_Policy_Notes", "Sources_acquired", "Data_extracted", "Lexemes_collected"}, {}),
    ("MeaningTable",    "parameters.csv",    {"Link_count"}, {}),
    ("FormTable",       "forms.csv",         set(), {"Meaning_ID": "Parameter_ID"}),
    ("CognateTable",    "cognates.csv",      set(), {}),
    ("CognatesetTable", "cognatesets.csv",   set(), {}),
    ("OrthoRegistry",   "orthographies.csv", set(), {}),
]
ID_RE = re.compile(r"^form-(\d+)$")

if not os.path.exists(SPREADSHEET): sys.exit(f"Spreadsheet not found: {SPREADSHEET}")
if not os.path.isdir(REPO_CLDF_FOLDER): sys.exit(f"cldf folder not found: {REPO_CLDF_FOLDER}")
print(f"Reading: {SPREADSHEET}\nWriting: {REPO_CLDF_FOLDER}\n")
wb = load_workbook(SPREADSHEET, data_only=True, read_only=True)

def read_sheet(name):
    rows = wb[name].iter_rows(values_only=True)
    header = next(rows)
    keep = [i for i, h in enumerate(header) if h not in (None, "")]
    names = [str(header[i]).strip() for i in keep]
    out = []
    for r in rows:
        d = {n: ("" if i >= len(r) or r[i] is None else str(r[i]).strip()) for n, i in zip(names, keep)}
        if any(d.values()): out.append(d)
    return names, out

def clean(v):  # whole numbers read back as '12.0' from float cells
    return v[:-2] if re.fullmatch(r"-?\d+\.0", v) else v

for sheet, fname, exclude, rename in TABLES:
    names, rows = read_sheet(sheet)
    cols = [c for c in names if c not in exclude]
    if sheet == "FormTable":
        used = [int(m.group(1)) for r in rows if (m := ID_RE.match(r["ID"]))]
        nxt, new_ids = (max(used) if used else 0) + 1, []
        for r in rows:
            if not r["ID"]:
                r["ID"] = f"form-{nxt:08d}"; new_ids.append(r["ID"]); nxt += 1
        if new_ids: print(f"  [{len(new_ids)} FormTable rows had no ID: assigned {new_ids[0]} .. {new_ids[-1]}]")
        ids = [r["ID"] for r in rows]
        assert len(ids) == len(set(ids)), "duplicate FormTable IDs"
    if sheet == "LanguageTable" and "Macroarea" not in cols:
        cols.insert(cols.index("Family"), "Macroarea")
        for r in rows: r["Macroarea"] = "Africa"
    with open(os.path.join(REPO_CLDF_FOLDER, fname), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow([rename.get(c, c) for c in cols])
        for r in rows: w.writerow([clean(r.get(c, "")) for c in cols])
    print(f"  {fname:<18}{len(rows):>6} rows")

# ── sources.bib ───────────────────────────────────────────────────────────────
_, sources = read_sheet("SourceTable")
esc = lambda s: s.replace("{", "\\{").replace("}", "\\}").replace("&", "\\&")
bib = []
for r in sources:
    if not r.get("ID"): continue
    if r.get("Author"): r["Author"] = re.sub(r"\s*;\s*", " and ", r["Author"])  # BibTeX name separator
    fields = [f"  {b} = {{{esc(r[a])}}}" for a, b in [
        ("Author","author"),("Year","year"),("Title","title"),("Publisher","publisher"),
        ("Place","address"),("Journal","journal"),("Volume","volume"),("Pages","pages"),("URL","url")] if r.get(a)]
    note = [f"{k}: {r[k]}" for k in ("Language_Covered","Region_Covered","Source_Type","License","Comment") if r.get(k)]
    if note: fields.append(f"  note = {{{esc(' | '.join(note))}}}")
    bib.append(f"@{r.get('Type') or 'misc'}{{{r['ID']},\n" + ",\n".join(fields) + "\n}\n")
with open(os.path.join(REPO_CLDF_FOLDER, "sources.bib"), "w", encoding="utf-8") as f:
    f.write("\n".join(bib))
print(f"  sources.bib       {len(bib):>6} entries\n\nDone. Review the diff, then commit and push.")
