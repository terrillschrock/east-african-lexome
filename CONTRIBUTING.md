# Contributing to EALex

Thank you for considering a contribution to the East African Lexome. This document describes how contributions to the project work in practice. For the ethical principles that govern data handling, see [ETHICS.md](ETHICS.md). For the data model details, see [SCHEMA.md](SCHEMA.md).

EALex is currently maintained as a **curated dataset** by the project lead. Contributions are welcome, with the workflow varying by what you'd like to contribute.

## Kinds of contributions

EALex welcomes contributions in several forms:

- **Lexical data** for languages in scope — wordlists, dictionaries, or fieldnote data for one of the 422 East African languages
- **Source identification** — pointing the project to a published source it doesn't yet have catalogued
- **Corrections** — fixing errors in existing data, metadata, or documentation
- **New language proposals** — suggesting languages or speech varieties that should be added to the scope
- **Methodological feedback** — pushing back on schema decisions, suggesting refinements, or raising issues with how the project is structured
- **Infrastructure contributions** — code, documentation improvements, or tooling

The contribution workflow differs depending on which of these applies. The sections below describe each.

## Contributing lexical data

This is the contribution path most directly relevant to EALex's mission. Linguists with wordlists, dictionaries, or fieldnote data for any of the languages in scope are encouraged to contribute.

### Workflow

During the current project phase, lexical data contributions are handled by **email** rather than through GitHub directly. This keeps the process accessible to linguists who may not be familiar with version control workflows, and lets the maintainer review contributions in context before they enter the master dataset.

1. **Initial contact.** Email **terrill.schrock@gmail.com** with a brief description: the language(s) involved, the approximate size and nature of the data (number of forms, what dictionary or fieldwork it draws on), and whether the data is published, unpublished, or a mix.

2. **Template provision.** The maintainer will respond with a contributor template — a spreadsheet aligned with EALex's FormTable schema, with the columns you'll need to populate and the conventions explained. The template will be tailored to the data type you're contributing (full dictionary import, focused wordlist, supplementary additions to existing data, etc.).

3. **Data preparation.** Fill out the template per the conventions in the accompanying notes. The level of completeness expected depends on what's available: at minimum, citation form, English gloss, and source attribution; ideally also root analysis, broad IPA transcription, semantic domain, and part of speech. Don't let perfect be the enemy of contribution — partial data is welcome and can be augmented later.

4. **Submission.** Email the completed spreadsheet back. Include in the message: confirmation that you have the right to share the data (per [ETHICS.md](ETHICS.md)), any community-imposed restrictions on the material, and how you'd like to be attributed.

5. **Integration.** The maintainer reviews, normalizes against EALex conventions, and integrates into the master dataset. Contributions are acknowledged in release notes and, for substantial contributions, with named-contributor anchor tags in the data itself (e.g., `direct_contribution_<your_name>_<year>` on relevant rows).

### Data quality expectations

EALex aims to capture lexical material at the granularity of **roots, stems, and admitted compounds** — not full dictionary entries with all inflected forms and idiomatic phrases. See the "Lexome scope" section of [SCHEMA.md](SCHEMA.md) for full detail on what's admitted.

For most contributions, this means:

- One row per lexical entry (root, stem, or admitted compound)
- Citation form as the language conventionally cites it
- English gloss for the meaning, following the conventions in SCHEMA.md
- Source attribution: either bibliographic reference for published data, or "[your name], [year]" for unpublished fieldwork
- Optional but valuable: root analysis when it differs from the citation form, broad IPA, semantic domain ID (RWC hierarchy)

The maintainer will help with any of the more technical fields if you're uncertain.

### Languages that especially need contributions

Researchers working on poorly-documented languages in scope of EALex — particularly in **Sudan, South Sudan, and the smaller Kordofanian and Surmic groups** — are especially encouraged to reach out. The SourceTable already documents where the documentation gaps are most acute, and EALex aims not just to be a data repository but a research roadmap.

If you're considering contributing data for a language you're not sure is in scope, just ask.

## Contributing source identification

If you know of a published source EALex doesn't have catalogued — a dictionary, grammar, wordlist, comparative study, or survey report — please share the citation. This can be done by:

- **Email** to terrill.schrock@gmail.com with the bibliographic details and, if possible, where the source can be accessed
- **Opening an issue** on GitHub with the source citation, tagged as a source-addition request

Sources don't need to be in your possession to be valuable; pointing the project at sources it should pursue is genuinely useful.

## Contributing corrections

Corrections to existing data, metadata, or documentation are welcome through any of these channels:

- **GitHub Issues** — for structured reports with clear before/after, suitable for individual data points or specific bugs
- **Email** — for corrections that require explanation, involve multiple related issues, or come with broader context
- **Takedown requests** — for material that should be removed for ethical or rights-based reasons, handled per the process in [ETHICS.md](ETHICS.md)

Please include source citations or other evidence for the correction where possible, so the maintainer can verify before changing the data.

## Proposing new languages

EALex's scope is built on Glottolog 5.2 with project-specific reconciliation. If you believe a language is missing from scope — particularly a cross-border variety, a recently recognized community, or a language without current Glottolog representation — open an issue or email with:

- The language's name(s) and any alternative names
- Geographic distribution and approximate speaker population
- Any known Glottolog code, ISO 639-3 code, or other standard identifiers (or note that none exist)
- Bibliographic sources documenting the language, if any
- A brief rationale for inclusion

EALex has a precedent for including languages on independent ethnolinguistic grounds when standard identifiers are unavailable (e.g., Ketebo/Mening), so absence from Glottolog isn't a blocker, but it does require positive justification.

## Methodological feedback

EALex's architectural decisions — the lexome model, the root-centric FormTable, the etic scaffolding framing for comparative anchors and semantic domains, the decision to extend CLDF — are made deliberately but not infallibly. Substantive feedback is welcome, particularly from linguists with experience in:

- Computational comparative linguistics and CLDF-ecosystem tooling
- Documentary linguistics and language archive infrastructure
- Specific East African language families where EALex's general conventions may strain against language-particular realities
- Ethnographic and anthropological-linguistic perspectives on the etic/emic distinctions in EALex's design

This kind of contribution is best made by **email** in the first instance, since the conversations tend to be substantive and benefit from back-and-forth before any concrete change is proposed.

## Infrastructure contributions

For contributions to the project's code, schema, or documentation infrastructure (the `regenerate_cldf.py` script, the spreadsheet structure, the markdown documentation), the standard GitHub workflow applies:

1. **Open an issue** describing the change you'd like to propose, before doing the work. This avoids duplicated effort and lets the maintainer flag any constraints upfront.
2. **Fork the repository**, make your changes on a branch, and open a pull request referencing the issue.
3. **Pull requests** are reviewed by the maintainer. For schema or methodological changes, expect some discussion before merge.

EALex doesn't currently have automated tests or CI, so contributions should include clear descriptions of what was changed and why, and where appropriate, before/after examples.

## A note on attribution

EALex aims to preserve attribution in the data itself, not just in release notes. For lexical data contributions, the contributor's name is associated with the contributed rows via either the `Source` field (for published material the contributor authored) or `Sense_Origin` and contributor-specific anchor tags (for direct unpublished contributions). For substantial methodological contributions to the schema or documentation, acknowledgement is made in the relevant document and in release notes.

Contributors who would prefer not to be named publicly should indicate this in their initial contact, and the project will arrange attribution accordingly (institutional attribution, pseudonymous attribution, or omission as preferred).

## Questions

For anything not covered above, email **terrill.schrock@gmail.com**. The contribution process is intentionally informal at the current project stage and the maintainer is generally responsive.
