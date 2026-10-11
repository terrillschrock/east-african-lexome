# Column reference (October 2026)

Supplements `SCHEMA.md` with the columns added since it was written. All appear in `cldf/`.

| Table | Column | Meaning |
|---|---|---|
| forms.csv | Parameter_ID | Meaning the form expresses (master column `Meaning_ID`; links to `parameters.csv`) |
| | Morphological_Analysis | Decomposition of the citation form (e.g. `root-NOM`) |
| | Root | Root of the form; final hyphen marks a bound root |
| | Segments | Space-separated segmentation of Root (not of Form) |
| | Plural_Form / Source_Plural | Recorded plural in IPA / as spelled in the source |
| | Part_Of_Speech, Source_Gloss | Category and the source's own gloss |
| | LoanSource_Form_ID | Donor form in this table, when attested (empty until donor data is imported) |
| parameters.csv | Broader_ID | More general meaning (general/specific hierarchy) |
| | Source_Language, Concepticon_Mapping_Notes | Language of a non-English source gloss; mapping notes |
| sources.bib | `note` | Now includes License where recorded |

**Form IDs** are `form-` plus eight digits, assigned in sheet order at first publication and never reused or renumbered. Forms added later receive the next number; deleted forms leave gaps.

**Ik conventions.** Form, Root, Plural_Form and Segments are in IPA with mid pitch written as low (it is low before high); only `Source_Form` and `Source_Plural` keep Schrock (2017) spelling. Segments come from Root.
