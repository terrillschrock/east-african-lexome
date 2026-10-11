# Scripts

## `regenerate_cldf.py`

Exports the master spreadsheet to the CLDF files in `cldf/` (the master is the source of truth; `cldf/` is generated).

    pip install openpyxl
    python3 regenerate_cldf.py /path/to/EALex_Master.xlsx /path/to/east-african-lexome/cldf

What it does:

- Exports every named column of `LanguageTable`, `MeaningTable` (as `parameters.csv`), `FormTable` (`Meaning_ID` becomes `Parameter_ID`), `CognateTable`, `CognatesetTable` and `OrthoRegistry`, in sheet order. Internal bookkeeping columns (`Citation_Policy_Notes`, `Sources_acquired`, `Data_extracted`, `Lexemes_collected`, `Link_count`) are left out.
- Writes `sources.bib` from `SourceTable` (multiple authors separated by `;` become BibTeX `and`).
- Gives any FormTable row with a blank ID the next free `form-NNNNNNNN`. Existing IDs are never changed. The master itself is not modified, so paste the printed IDs back into the master when you publish.
- Reads cached formula values: open and save the master in Excel/LibreOffice first.

`cldf/Wordlist-metadata.json` is not regenerated. When you add a column to a sheet, add it to the matching table in that file too, then check with `pip install pycldf` and `cldf validate cldf/Wordlist-metadata.json`.

After running: review the diff, commit, push.
