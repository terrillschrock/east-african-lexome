# Release notes

## v0.2.0 (draft, October 2026): first Ik release

The first version of EALex that contains lexical data. The dataset is published in CLDF; see [README.md](README.md) and [SCHEMA.md](SCHEMA.md).

### What's in it

| | |
|---|---|
| Languages | 446 (Glottolog CLDF v5.3, with documented divergences) |
| Forms | 5,391, all Ik, from Schrock (2017), *The Ik Language: Dictionary and Grammar Sketch* (Language Science Press). Nouns 2,247, verbs 3,023, other categories 121 |
| Meanings | 5,550, of which 4,263 are linked to at least one Ik form; the rest are seed meanings awaiting data from other languages |
| Sources | 475 bibliographic entries |
| Orthographies | 20 |

Ik forms are given in IPA, with Schrock (2017) spellings kept in `Source_Form` and `Source_Plural`. Each form records its root, morphological analysis, plural where recorded, and segmentation of the root.

### Changes since v0.1.0 (April 2026)

- Language inventory reconciled and expanded from 420 to 446 languages
- New forms columns: `Morphological_Analysis`, `Root`, `Plural_Form`, `Source_Plural`, `Part_Of_Speech`, `Source_Gloss`, `LoanSource_Form_ID`
- New parameters columns: `Broader_ID` (general/specific hierarchy), `Source_Language`, `Concepticon_Mapping_Notes`
- Form IDs are now fixed: `form-00000001` onward, never renumbered
- Rewritten export script (`scripts/regenerate_cldf.py`) and updated schema file
- Added `FIELDS.md`

### Known limitations

- Only one language has forms so far. This is a first release of the infrastructure plus Ik, not a comparative resource yet.
- `cognates.csv` and `cognatesets.csv` are empty.
- A form links to one meaning (CLDF's `Parameter_ID` takes a single value). Very specific Ik meanings are connected to general ones through `Broader_ID` on the meaning, and how best to link specific lexemes with no general term is still an open design question.
- The `MeaningRelations` table and the nested comparative wordlist described in SCHEMA.md are not yet exported.
- Loan sources are recorded as language names; `LoanSource_Form_ID` is empty until donor-language data is imported.

### Credit and licensing

Data: CC BY 4.0. Ik data: Terrill Schrock. See `CITATION.cff` for how to cite. DOI: *to be added after the Zenodo release.*
