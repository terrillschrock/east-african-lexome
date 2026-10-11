# East African Lexome (EALex)

A comprehensive, machine-readable lexical database for the languages of East Africa — designed as research infrastructure for African historical linguistics in the era of computational and quantitative methods.

EALex aims to bring "lexomics" to a region whose linguistic richness has long been studied through patchwork sources rather than as an integrated whole. The project is structured as a **lexome**: a registry of the lexical roots, stems, and admitted compounds from which each language's lexicon is generated, rather than a catalog of every form each language has ever produced. The goal is to document the etymologically heritable substrate of East African languages, organized for both cross-linguistic comparison and language-specific lexicography.

## Scope

EALex covers **422 languages** spoken across **ten East African nations**: Burundi, Eritrea, Ethiopia, Kenya, Rwanda, Somalia, South Sudan, Sudan, Tanzania, and Uganda. The languoid inventory is built on Glottolog 5.2 with project-specific reconciliation decisions (documented per-language in the dataset) where Ethnologue, regional expertise, or geographic considerations warranted divergence. A small number of languages without current Glottolog entries are included on independent ethnolinguistic grounds, with the absence of standard identifiers documented in the data.

The languages span four major language families plus several isolates:

- **Atlantic-Congo** (largely Bantu) — 183 languages
- **Nilo-Saharan** (Nilotic, Central Sudanic, Surmic, Koman, Kordofanian, and others) — combined majority
- **Afro-Asiatic** (Cushitic, Omotic, Ethiosemitic, Berber-Beja) — 67 languages
- **Isolates** — 10 languages, including Hadza, Sandawe, Kunama, Nara, Berta, Ongota, and Shabo

Over half of the languages in scope are classified as threatened, shifting, moribund, or nearly extinct under Glottolog's Agglomerated Endangerment Status (AES) ratings — making documentation efforts time-sensitive.

## What's in the lexome

EALex's data model has three core entities:

- **Forms** — lexical roots, stems, and admitted compounds drawn from each language's lexicon. The data model is *root-centric*: broad IPA transcription and cognate identification target the root, since that's where etymological comparison happens. Morphological analysis describes how the citation form decomposes into the root plus any inflectional or derivational material. Spontaneously inflected forms, transparent derivations, and multi-word expressions are excluded by design.
- **Meanings** — semantic nodes that one or more languages have lexicalized. The registry contains both densely-attested comparative concepts (drawn from SIL CAWL, Leipzig-Jakarta, Swadesh, and community contributions) and sparsely-attested language-specific senses surfaced during import. A meaning's position on the core-to-satellite continuum is observed from attestation density, not assigned a priori.
- **Languages** — the 422 East African speech varieties in scope, with geographic, genealogical, sociolinguistic, and per-language citation-policy metadata.

A separate `MeaningRelations` table records explicit semantic relationships between meanings — synonymy, colexification, taxonomic siblings, attested semantic shifts — providing a home for emic observations about how specific languages organize semantic space.

For the full data model, see [SCHEMA.md](SCHEMA.md).

## Goal

The project's working target is **one million attested lexical roots and stems** — an average of roughly 2,400 entries per language, though some languages will contribute many more (an established dictionary like the project lead's own Ik dictionary contributes around 4,000 noun and verb roots alone) and others far fewer.

## Data format

EALex is published in [CLDF (Cross-Linguistic Data Format)](https://cldf.clld.org/) at the top level, with extensions documented in SCHEMA.md to support EALex's lexome model. The top-level CLDF dataset describes the full lexome including language-specific senses; a nested comparative wordlist provides lexibank-style interoperability for researchers using comparative concepts as the unit of analysis.

The `cldf/` folder contains:

| File | Contents |
|---|---|
| `languages.csv` | The 422 languages with Glottocodes, ISO codes, coordinates, family/subfamily classifications, country assignments, AES endangerment ratings, and per-language citation policy notes |
| `meanings.csv` | The full meaning registry — comparative anchors and language-specific senses, tagged with provenance, RWC semantic domains, and Concepticon IDs where applicable |
| `forms.csv` | Attested lexical forms with their roots, morphological analysis, IPA transcriptions, and source provenance |
| `meaning_relations.csv` | Explicit semantic relationships between meanings |
| `cognates.csv` / `cognatesets.csv` | Cognate codings (populated incrementally as comparative work proceeds) |
| `orthographies.csv` | A registry of orthographic systems and transliteration conventions used in source materials and EALex's normalizations |
| `sources.bib` | A bibliographic register of 468+ sources organized in three tiers: pan-regional reference works, family-level comparative works, and language-specific descriptive sources |
| `Wordlist-metadata.json` | The CLDF schema describing the dataset structure |
| `cldf/comparative/` | Nested CLDF-conformant Wordlist, filtered to comparative-anchored meanings, for lexibank-compatible tooling |

Semantic domain tagging uses the SIL Rapid Word Collection (RWC) hierarchy under CC BY-SA 4.0. RWC domain IDs serve as etic organizational scaffolding rather than claims about indigenous semantic structure.

## Project status

EALex is in the **infrastructure-building phase**, with the schema redesign and seed data complete and inaugural data imports beginning.

Active work:

1. Inaugural data import from the project lead's Ik dictionary (~4,000 noun and verb roots from FLEx, with SIL semantic domain tags)
2. Concepticon mapping pass for the comparative-anchor layer
3. AI-assisted domain suggestion tool for subsequent imports lacking pre-tagged data
4. Systematic source acquisition and lexical data harvesting, language by language

## Contributing

EALex is currently maintained as a **curated dataset** by the project lead, with a view toward opening more broadly to trusted collaborators as the project matures.

### Lexical data contributions

During the current phase, lexical data is collected by **email** rather than through GitHub directly. This keeps the contribution process accessible to linguists and area specialists who may not be familiar with version control workflows.

To contribute:

1. Email **terrill.schrock@gmail.com** with a brief description of what you'd like to contribute (e.g., "wordlist for [language]" or "regional concept additions in domain X")
2. The project lead will respond with the appropriate template spreadsheet
3. Complete the spreadsheet and email it back
4. Contributions are integrated into the master dataset and acknowledged in the project's release notes, with named-contributor anchor tags preserving attribution in the data itself

Researchers working on poorly-documented languages in scope of EALex (particularly in Sudan, South Sudan, and the smaller Kordofanian and Surmic groups) are especially encouraged to reach out — the SourceTable already documents where the documentation gaps are most acute, and EALex aims not just to be a data repository but a research roadmap.

All contributors are asked to review the project's [Ethics Statement](ETHICS.md) and the [Contributing Guide](CONTRIBUTING.md), which describe how published-source data and direct contributions are handled, the takedown and correction process, and EALex's broader ethical commitments.

### Issue reports

For data corrections, new language proposals, source additions, and general questions, please use the [Issues](../../issues/new/choose) tab to submit a structured report.

## Citation

> Schrock, Terrill (2026). *East African Lexome (EALex): A Lexical Database for East African Languages.* https://github.com/terrillschrock/east-african-lexome

## License

The EALex dataset is released under the [Creative Commons Attribution 4.0 International License (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/), matching the licensing of Glottolog and the broader open comparative linguistics ecosystem.

EALex's semantic domain tagging draws on the SIL Rapid Word Collection domain hierarchy, which is licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). EALex uses RWC domain IDs as reference annotations; any extensions to the hierarchy developed within EALex will be published as separately-licensed CC BY-SA artifacts. See [LICENSE.txt](LICENSE.txt) for full licensing details.

## Maintainer

EALex is maintained by **Terrill Schrock**, a linguist with eight years of fieldwork on Ik, one of three remaining Kuliak languages of northeastern Uganda. Author of *A Grammar of Ik* (LOT, 2014) and *The Ik Language: Dictionary and Grammar Sketch* (Language Science Press, 2017).

## A note on AI collaboration

EALex is being built with the assistance of Anthropic's Claude as a sustained thinking partner and drafting tool. The AI plays a substantial role in compiling and organizing the source bibliography, drafting and refining documentation, structuring the data model, stress-testing methodological decisions through dialogue, and — looking ahead — assisting with semantic domain tagging at scale during import. The AI's outputs are reviewed, edited, and verified by the maintainer at every stage. Decisions about scholarly substance — the scope of the language inventory, the lexome model and root-centric architecture, the reconciliation of Glottolog and Ethnologue, override decisions for individual languages, and the project's overall methodological framing — remain the maintainer's. EALex is offered in the spirit of methodological transparency about how the project is being assembled.

## Acknowledgements

EALex builds on the open scholarly infrastructure of [Glottolog](https://glottolog.org), [Concepticon](https://concepticon.clld.org), [CLDF](https://cldf.clld.org), [SIL International](https://www.sil.org), and the SIL [Rapid Word Collection](https://www.rapidwords.net) semantic domain hierarchy, as well as the descriptive labor of generations of Africanist linguists whose work fills the SourceTable. The project also draws on the network and community of the [Rift Valley Network](https://www.riftvalley.net).
