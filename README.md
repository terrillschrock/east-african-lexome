# East African Lexome (EALex)

A comprehensive, machine-readable comparative lexical database for the languages of East Africa.

EALex is research infrastructure for African historical linguistics in the era of computational and quantitative methods. The project aims to bring "lexomics" — the science of large-scale historical lexical data — to a region whose linguistic richness has long been studied through patchwork sources rather than as an integrated whole.

## Scope

EALex covers **420 languages** spoken across **ten East African nations**: Burundi, Eritrea, Ethiopia, Kenya, Rwanda, Somalia, South Sudan, Sudan, Tanzania, and Uganda. The languoid inventory is built on Glottolog 5.2 with project-specific reconciliation decisions (documented per-language in the dataset) where Ethnologue, regional expertise, or geographic considerations warranted divergence from Glottolog's classification.

The languages span four major language families plus several isolates:

- **Atlantic-Congo** (largely Bantu) — 183 languages
- **Nilo-Saharan** (Nilotic, Central Sudanic, Surmic, Koman, Kordofanian, and others) — combined majority
- **Afro-Asiatic** (Cushitic, Omotic, Ethiosemitic, Berber-Beja) — 67 languages
- **Isolates** — 10 languages, including Hadza, Sandawe, Kunama, Nara, Berta, Ongota, and Shabo

Over half of the languages in scope are classified as threatened, shifting, moribund, or nearly extinct under Glottolog's Agglomerated Endangerment Status (AES) ratings — making documentation efforts time-sensitive.

## Goal

The project's working target is **one million attested lexical forms** — an average of roughly 2,381 words per language, though some languages will contribute many more (an established dictionary like the project lead's own Ik dictionary contributes around 4,000 verb and noun roots alone) and others far fewer.

## Data format

EALex is published in [CLDF (Cross-Linguistic Data Format)](https://cldf.clld.org/), the standard format for comparative linguistic datasets. CLDF makes the data interoperable with the wider computational linguistics ecosystem (Glottolog, Concepticon, lexibank, and tools like `pycldf`).

The `cldf/` folder contains:

| File | Contents |
|---|---|
| `languages.csv` | The 420 languages with Glottocodes, ISO codes, coordinates, family/subfamily classifications, country assignments, and AES endangerment ratings |
| `parameters.csv` | The core concept list — 1,737 concepts built on SIL's Comparative African Wordlist (SILCAWL, 1,700 items), supplemented with non-overlapping Leipzig-Jakarta and Swadesh items |
| `forms.csv` | Attested lexical forms (will grow as data is harvested) |
| `cognates.csv` / `cognatesets.csv` | Cognate codings (deferred to a later project phase) |
| `orthographies.csv` | A custom registry of 18 orthographic systems (colonial, modern national, indigenous scripts) used in source materials, supporting eventual mass IPA conversion |
| `sources.bib` | A bibliographic register of 468+ sources organized in three tiers: pan-regional reference works, family-level comparative works, and language-specific descriptive sources |
| `Wordlist-metadata.json` | The CLDF schema describing the dataset structure |

## Project status

EALex is in the **infrastructure-building phase**. The languoid list, concept list, source bibliography, and folder/data architecture are in place. Active work is now turning to:

1. Expanding the core concept list with regionally relevant vocabulary (a public call for contributions has been issued through the Rift Valley Network)
2. Mapping the concept list to Concepticon
3. Inaugural data import from the project lead's Ik dictionary
4. Systematic source acquisition and lexical data harvesting, language by language

## Contributing

EALex is currently maintained as a **curated dataset** by the project lead, with a view toward opening more broadly to trusted collaborators as the project matures.

### Lexical data and concept contributions

During the current phase, lexical data and concept-list additions are being collected by **email** rather than through GitHub directly. This keeps the contribution process accessible to linguists and area specialists who may not be familiar with version control workflows.

To contribute:

1. Email **terrill.schrock@gmail.com** with a brief description of what you'd like to contribute (e.g. "wordlist for [language]" or "regional concept additions in domain X")
2. The project lead will respond with the appropriate template spreadsheet
3. Complete the spreadsheet and email it back
4. Contributions are integrated into the master dataset and acknowledged in the project's release notes

Researchers working on poorly-documented languages in scope of EALex (particularly in Sudan, South Sudan, and the smaller Kordofanian and Surmic groups) are especially encouraged to reach out — the SourceTable already documents where the documentation gaps are most acute, and EALex aims not just to be a data repository but a research roadmap.

All contributors are asked to review the project's [Ethics Statement](ETHICS.md), which describes how published-source data and direct contributions are handled, the takedown and correction process, and EALex's broader ethical commitments.

### Issue reports

For data corrections, new language proposals, source additions, and general questions, please use the [Issues](../../issues/new/choose) tab to submit a structured report.

## Citation

> Schrock, Terrill (2026). *East African Lexome (EALex): A Comparative Lexical Database for East African Languages.* https://github.com/terrillschrock/east-african-lexome

## License

The dataset is released under the [Creative Commons Attribution 4.0 International License (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/), matching the licensing of Glottolog and the broader open comparative linguistics ecosystem.

## Maintainer

EALex is maintained by **Terrill Schrock**, a linguist with eight years of fieldwork on Ik, one of three remaining Kuliak languages of northeastern Uganda. Author of *A Grammar of Ik* (LOT, 2014) and *The Ik Language: Dictionary and Grammar Sketch* (Language Science Press, 2017).

## A note on AI collaboration

EALex is being built with the assistance of Anthropic's Claude as a sustained thinking partner and drafting tool. The AI plays a substantial role in compiling and organizing the source bibliography, drafting and refining documentation, structuring the CLDF schema, and helping stress-test methodological decisions through dialogue. The AI's outputs are reviewed, edited, and verified by the maintainer at every stage. Decisions about scholarly substance — the scope of the language inventory, the reconciliation of Glottolog and Ethnologue, the choice of CAWL as the concept-list backbone, override decisions for individual languages, and the project's overall methodological framing — remain the maintainer's. EALex is offered in the spirit of methodological transparency about how the project is being assembled.

## Acknowledgements

EALex builds on the open scholarly infrastructure of [Glottolog](https://glottolog.org), [Concepticon](https://concepticon.clld.org), [CLDF](https://cldf.clld.org), and [SIL International](https://www.sil.org), as well as the descriptive labor of generations of Africanist linguists whose work fills the SourceTable. The project also draws on the network and community of the [Rift Valley Network](https://www.riftvalley.net).
