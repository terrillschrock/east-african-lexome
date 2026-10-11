# EALex Data Model

This document describes the conceptual data model of the East African Lexome (EALex). It is the authoritative reference for what the data represents, how the parts relate, and what conventions govern each field.

EALex is currently encoded as a multi-sheet spreadsheet with a CLDF (Cross-Linguistic Data Format) export, but the conceptual model is intentionally portable across encodings. This document describes the model first, then notes how the current encoding implements it. When EALex eventually migrates to a database-backed architecture, this document is the specification for the new schema.

---

## Overview

EALex is a registry of lexicalized meanings and the forms that express them across the languages of East Africa. The data model has three core entities:

- **Meanings** — semantic nodes that one or more languages have lexicalized
- **Forms** — lexical roots, stems, and admitted compounds drawn from each language's lexicon
- **Languages** — the speech varieties in scope, with their geographic, genealogical, and sociolinguistic metadata

Supporting entities:

- **Sources** — the publications, datasets, and direct contributions from which forms are extracted
- **MeaningRelations** — explicit semantic relationships between meanings
- **Cognates / Cognate Sets** — historical relationships between forms
- **OrthoRegistry** — orthographic systems referenced by forms

The data model is **root-centric**: forms exist primarily to record the etymologically interesting roots and stems of each language. Spontaneously inflected forms (a plural derived from a singular citation, a past tense of a present citation), transparent derivations, and multi-word expressions are excluded by design — see "Lexome scope" below. The Root_IPA field carries the broad IPA transcription of the root, not the citation form. Morphological analysis describes how the citation form decomposes into the root plus any inflectional or derivational material.

The data model is also **concept-centric at the meaning layer**: meanings represent semantic content abstracted from grammatical category. The same meaning can be expressed by a noun in one language, a verb in another, and a complex predicate in a third; all three forms link to the same meaning. This abstraction is from grammatical category, not from cultural specificity: language-specific meanings (those lexicalized by only one or a few languages and reflecting culturally specific referents) are first-class citizens of the registry.

---

## Lexome scope

The lexome contains the building blocks from which each language's lexicon is generated, not every form the language has ever produced. Specifically:

### Admitted

- **Lexical roots** — the morphological units that bear etymological identity, recorded in the form the language's tradition supports (a bare root where the language allows it, or an abstract bound root where the language requires affixation for all surface forms). Bound roots are marked with the language's conventional marker (often a trailing hyphen).
- **Stems** — root plus derivational morphology, where the stem rather than the root is the language's standard citation form. The choice between root and stem is per-language and documented in each language's citation policy.
- **Citation forms with conventional inflection** — many languages cite nouns and verbs with obligatory inflectional morphology: Ik nouns in the singular nominative, Bantu nouns with their noun-class prefix, Semitic verbs in a 3sg perfect, and so on. The citation form is admitted as the lexome entry shape per the language's citation policy; the Root field captures the underlying morphological identity, and Morphological_Analysis records the decomposition.
- **Compounds with stable lexical identity** — admitted when the compound has acquired meaning or distribution that isn't fully predictable from its components.
- **Lexicalized derivatives** — admitted when the meaning of the derivative has specialized beyond what the derivational process predicts.
- **Bound lexical morphemes** — admitted when they carry lexical content, regardless of restricted distribution. Includes cranberry morphs, fossilized roots, and similar.
- **Loanwords** — admitted as lexome material in the borrowing language, with the source language recorded where known.

### Excluded

- **Spontaneously inflected forms beyond the citation convention** — once a citation form is established for a language, derived inflections (a plural from a singular citation, a past tense from a present citation, an accusative from a nominative citation) are not separate entries. They reflect predictable application of the grammar to lexome material, not lexome material themselves.
- **Transparent derivational outputs** — *developer* and *development* are not separate entries when they derive predictably from *develop*. The root suffices.
- **Bound grammatical morphemes** — affixes marking case, tense, aspect, mood, agreement, valency, etc. (These appear in Morphological_Analysis fields when decomposing citation forms, but they don't get their own FormTable rows.)
- **Multi-word expressions** — idioms, fixed phrases, light-verb constructions, serial verb constructions, and similar combinations of lexome material.

---

## Meanings

### What a meaning represents

A meaning is a semantic node — a concept that one or more languages have lexicalized. Meanings are abstracted from grammatical category: HUNGER is one meaning regardless of whether a language expresses it as a noun, a verb, a stative predicate, or otherwise. Meanings are not abstracted from cultural specificity, however. A meaning like "clear liquid in the stomach of a slaughtered elephant" is highly language-specific in its conceptualization and may be attested in only one language; it remains a legitimate row in the registry because some language has lexicalized it.

Meanings are not curated comparative concepts in the lexibank sense, though a curated subset (the comparative-anchor layer) provides interoperability with that tradition. Most meanings will enter the database through extraction from language-specific sources, capturing meanings that any in-scope language has found worth lexicalizing.

### The core-to-satellite continuum

Meanings vary in attestation density. Some are densely attested across most languages in scope (BODY, WATER, EAT, NUMBERS); these are at the core end of the continuum. Some are attested in only one or a handful of languages (CLEAR LIQUID IN THE STOMACH OF A SLAUGHTERED ELEPHANT, specific ritual roles, specific ethnobotanical categories); these are at the satellite end.

The continuum is observed rather than imposed. A meaning's position is a function of how many forms attest it across the imported corpus, and shifts as the corpus grows. The classification is computed (currently by hit count) rather than assigned.

### Comparative anchors

A subset of meanings carry one or more **comparative anchor** tags indicating their provenance from established comparative concept lists. These anchors enable interoperability with the lexibank tradition and serve as a curated comparative-wordlist backbone.

Anchor values (pipe-separated, multi-value):

- `CAWL` — SIL Comparative African Wordlist
- `LJ100` — Leipzig-Jakarta 100-item list
- `Swadesh100` — Swadesh 100-item list
- `Swadesh207` — Swadesh 207-item list
- `RVN_<contributor>_<year>` — contributions from community calls to the Rift Valley Network mailing list, with named contributors and year
- `EALEX_<year>` — maintainer's curated additions
- `imported_from_<dataset_id>` — organic growth from imported datasets keyed to Concepticon

A meaning may carry multiple anchors (a CAWL item that is also on LJ100 is tagged both). Meanings without any comparative anchor are language-specific senses extracted during import. The anchor layer is annotation, not gatekeeping; meanings are admitted to the registry regardless of anchor status.

### Sense origin

Each meaning records how it entered the registry:

- `seed` — present in the initial CAWL/Swadesh/LJ-derived seed layer
- `direct_contribution` — contributed by a named linguist via call or correspondence
- `maintainer_curation` — added by the project maintainer based on independent knowledge
- `extracted` — created during import to host a form whose meaning didn't match any existing entry

### Concepticon mapping

Meanings that correspond to entries in the Concepticon catalog carry a `Concepticon_ID` referencing the Concepticon Set ID. This is a partial overlay — populated for most comparative-anchor meanings and almost no language-specific meanings — and provides stable cross-dataset identifiers for the meanings where it applies.

A `Concepticon_Mapping_Notes` field records non-obvious mapping decisions.

### Semantic field

Meanings carry one or more semantic domain identifiers from the SIL Rapid Word Collection (RWC) domain hierarchy. The `Semantic_Field` field holds pipe-separated RWC domain IDs (e.g., `1.6.1.2|6.3.4` for a meaning belonging to both BIRD and ANIMAL_HUSBANDRY domains).

The RWC hierarchy is used as an organizational tool for finding and browsing meanings, not as a claim about indigenous semantic structure. Domain assignment is part of the import workflow; for sources without pre-existing tags, an AI-assisted suggestion tool generates candidates that the maintainer reviews.

### Glosses

Each meaning has two display fields:

- **Gloss** — natural-language form, in English, used for human display, search, and AI processing. Conventions: verbs without "to" (`walk`, not `to walk`); modifiers in natural English position (`dwarf mongoose`); articles dropped; lowercase except proper nouns; numerals as digits when part of quantities (`20-liter`); parenthetical disambiguators for sense ambiguity or argument-structure splits (`light (adj, pale)`, `walk (vi)`).
- **Sort_Key** — head-first comma-separated form for dictionary-style sorting (`mongoose, dwarf`; `jerrycan, 20-liter`). Identical to Gloss when the gloss is already a single word or starts with its semantic head.

The two fields exist because they do different work: Gloss optimizes for natural-language display and tool compatibility; Sort_Key optimizes for sorted browsing by semantic head.

### Etic scaffolding

Meaning-level apparatus — comparative anchors, RWC domain tags, Concepticon IDs — is etic scaffolding. It organizes the data for cross-linguistic comparison and retrieval. It does not claim to represent indigenous semantic structure. Emic observations about how specific languages organize meaning live in the MeaningRelations table.

---

## Forms

### What a form represents

A form is a lexical entry in a specific language, linked to a meaning. Forms are the empirical data of the lexome — what the languages actually use to express each meaning.

A single meaning typically has multiple forms attesting it across languages (one per language that lexicalizes the meaning). A single language may have multiple forms linked to the same meaning when grammatical packagings differ (e.g., a noun and a verb both meaning "hunger") or when synonymy/dialectal variation produces multiple lexicalizations.

### Citation form, source form, and root

Three representations of the form, with distinct jobs:

- **Source_Form** — the form as it appeared in the source, in whatever script and convention the source used. Non-Roman scripts (Ge'ez for Ethiopian Semitic, Arabic for some Sudanese languages, etc.) live in this field. Source_Form is the provenance anchor: it preserves the source's representation faithfully and enables reproducibility.
- **Form** — the citation form in a Roman-alphabet representation. Form serves two purposes. First, it provides a Roman-script counterpart when Source_Form is in a non-Roman script, so EALex's data is uniformly readable across languages. Second, it provides the natural-language citation shape — what a reader of the language would recognize as the word, in EALex's normalized conventions. The specific orthography or transliteration scheme used is recorded in the `Orthography` field, a foreign key to OrthoRegistry. When EALex adopts the source's Roman-script representation directly, Form and Source_Form are identical.
- **Root** — the lexical root underlying the citation form, recovered by stripping the conventional inflectional or morphological material that the citation form carries. Root is the comparative-analytical surface of FormTable: this is where etymological work happens, where cognate candidates are identified, and what phonological similarity is computed against (via Root_IPA). For languages where citation form equals root (no morphological stripping required), Root is populated with the same value as Form. For languages where they differ (Ik, Bantu, Cushitic, Semitic, and many others), Root captures the etymologically interesting unit.

The three fields move from provenance (Source_Form) through human-readable citation (Form) to comparative-analytical identity (Root). Source_Form and Form together represent the citation form at two levels of provenance — what the source said versus what EALex says the language uses. Root is conceptually distinct, the analytical recovery underneath both. Source_Form and Form are means; Root is the goal.

### Root-centric analysis

The phonological and morphological analysis apparatus describes the root, not the citation form:

- **Root_IPA** — broad IPA transcription of the root. Phonemic-level by default, with whatever finer phonetic detail is confidently recoverable. For languages with morphologically dynamic tone, tonal marking is included where the underlying tone is confidently determined; omitted otherwise. The Root_IPA field's level of detail varies by analytical confidence, which is acknowledged rather than hidden.
- **Source_IPA** — the source's IPA transcription of the *citation form*, when one was provided. Preserves source-provided phonetic data for cases where the citation form's phonology is independently interesting (narrow transcription work, suprasegmental detail). Most rows will be empty since most sources do not provide IPA.

Segmentation for cognate detection (tokenized phonological units) is derived from Root_IPA at export time and is not stored as a separate field in the source spreadsheet.

### Form type

Each form is classified as one of:

- `simplex_root` — a root not further decomposable
- `simplex_stem` — a stem (root plus derivational morphology) functioning as a single lexical unit
- `compound` — a compound with stable lexical identity
- `bound_root` — a root with restricted distribution (e.g., only in compounds)
- `lexicalized_derivative` — a derived form with specialized meaning

### Morphological analysis

The `Morphological_Analysis` field records how the citation form decomposes into the root plus its inflectional, derivational, or compositional material. For an Ik noun with citation form `kɔna` and root `kɔn-`, the analysis records the decomposition: `kɔn- + -a (nominative)`. For an Ik verb with citation form `atson` and root `ats-`, the analysis records: `ats- + -on (intransitive infinitive)`.

This field is populated whenever the relationship between Form and Root requires explanation. For languages like Ik, Bantu languages, Semitic languages, and others where citation forms carry conventional inflection or class markers, this field is populated for most or all forms. For languages where Form equals Root, the field is typically blank or contains only a note about the form's compound or derivative status.

For compounds and lexicalized derivatives, the analysis decomposes the form into its components (e.g., `blackbird` as `black + bird`, with a note that the compound has acquired non-compositional meaning).

### Part of speech

The `Part_Of_Speech` field records the form's grammatical category in its language. This is a property of the form, not the meaning — the same meaning can have noun-typed forms in one language and verb-typed forms in another. Controlled vocabulary is language-typological-aware: N, V, Adj, Adv, Num, Pron, Interj, Conj, Prep are the broad categories, with language-specific subcategorization (e.g., transitive vs. intransitive) carried where relevant.

### Provenance

Each form records:

- **Source** — foreign key to SourceTable, identifying the publication or dataset the form was extracted from
- **Source_Page** — page reference within the source
- **Data_Source_Type** — `published`, `direct_contribution`, or other origin category
- **Collector** — the person who originally elicited or collected the form, when this differs from the source's author (preserves attribution for fieldworkers and research assistants whose work was published under others' names)
- **Collection_Date** — date of collection, when this differs meaningfully from the source's publication date
- **Elicitation_Context** — for primary-fieldwork data, the elicitation method used

### Cognate fields

`Cognate_ID` and `Cognate_Set_ID` link forms into cognate sets via the CognateTable and CognatesetTable. Populated incrementally as cognate work proceeds; not required for form entry.

### Loan tracking

`Loan` is a true/false flag (typically marked with `x` or left blank in the spreadsheet) indicating that the form is borrowed from another language. `LoanSource_Language` records the source language of the borrowing when identifiable, using the EALex language ID format where the source language is itself in scope, or a free-text language name otherwise.

---

## Languages

### Identification

Each language has:

- **ID** — an EALex-specific identifier in the format `lexome_<short>-<country>` (e.g., `lexome_ikkk-ug` for Ik in Uganda). The short code is typically a 4-character abbreviation; the country suffix is a 2-character lowercase ISO 3166 code indicating the language's primary country of distribution.
- **Name** — the canonical name used by EALex
- **Glottocode** — Glottolog identifier when one exists; blank when no Glottolog entry covers the language
- **ISO639P3code** — ISO 639-3 code when one exists; blank when none assigned

The blank-code convention applies when EALex includes a language on independent ethnolinguistic grounds despite no current Glottolog or ISO entry (e.g., Ketebo). The absence is a known finding, not a data error.

### Geographic and genealogical metadata

- **Latitude, Longitude** — point coordinates, typically the geographic center of the speech community or the location of the largest population concentration
- **Country** — the primary country of the language's distribution. For cross-border languages, this is the country with the largest population concentration or strongest historical center
- **EA_Countries** — pipe-separated ISO 3166 codes for all East African countries where the language is spoken (e.g., `KE|SS|UG`)
- **Family** — the broad language family (Nilotic, Atlantic-Congo, Afro-Asiatic, etc.)
- **Subfamily** — finer-grained subfamily classification

### Sociolinguistic metadata

- **Speaker_Population** — estimated number of speakers, when known
- **Endangerment** — AES (Agglomerated Endangerment Scale) status: `not_endangered`, `threatened`, `shifting`, `moribund`, `nearly_extinct`. Visualized via row-color fill in the spreadsheet encoding

### Citation policy

The `Citation_Policy_Notes` field documents per-language conventions for what counts as a lexome entry — whether forms are recorded as roots, stems, or full citation forms; what morphological stripping is applied; what conventions mark bound roots. Most languages share patterns; each gets its own brief note as it's imported.

### Progress tracking

Three columns track the project's progress per language:

- **Sources_acquired** — non-empty when sources for the language have been obtained
- **Data_extracted** — non-empty when lexical data has been extracted from sources
- **Lexemes_collected** — count of forms entered for this language

These columns feed the project Dashboard's aggregate counts.

---

## Sources

The SourceTable is the project's bibliography. Each source represents a publication, dataset, or direct contribution from which forms are extracted. Sources are tiered by coverage:

- Pan-regional comparative wordlists and surveys
- Family-level comparative studies
- Language-specific dictionaries, grammars, and field notes
- Direct contributions from named linguists

Source records include standard bibliographic fields (author, year, title, publisher, etc.) plus EALex-specific provenance metadata.

---

## MeaningRelations

A table of explicit semantic relationships between meanings. Each row records a directed or undirected relation between two meanings, with a relation type:

- `synonym` — fully equivalent meanings in some context
- `near_synonym` — partially overlapping meanings
- `colexified` — meanings that some language expresses with a single form
- `taxonomic_sibling`, `taxonomic_parent`, `taxonomic_child` — hierarchical relationships
- `attested_shift` — meanings between which documented semantic shift has occurred
- `meronym_holonym` — part-whole relationships

MeaningRelations is the natural home for **emic observations** about how specific languages organize semantic space. A row recording that Ik colexifies HORNBILL and WOODPECKER is a language-specific claim about Ik's semantic structure, distinct from the etic organizational scaffolding (RWC domains, Concepticon IDs) that the meaning-level fields carry.

The table is populated opportunistically as imports and analysis surface relationships, not as a systematic pass.

---

## Cognates

CognateTable and CognatesetTable handle historical-comparative cognate identification:

- A cognate set groups forms that descend from a common etymon
- Each form's `Cognate_ID` links it to a cognate row, which in turn links to a cognate set
- Cognate evidence (sound correspondences, scholarly references) is recorded on the cognate rows

Cognate work is downstream of phonological analysis (which requires Root_IPA to be populated) and is performed incrementally rather than systematically.

---

## OrthoRegistry

A registry of orthographic systems used across the languages. Each orthography record describes a writing system (modern standard, historical/missionary, linguist-specific notation, etc.) with provenance and conventions. Forms reference the registry via the `Orthography` field, identifying which writing system the form's `Form` field uses.

---

## Derived outputs

The EALex master spreadsheet is the source of truth. A regeneration script produces derived outputs:

### Top-level CLDF dataset

The full lexome encoded in CLDF, with `MeaningTable` containing all meanings (comparative-anchored and language-specific) and `FormTable` containing all forms. This is the comprehensive view of EALex.

### Nested comparative wordlist

A CLDF-conformant Wordlist nested in `cldf/comparative/`, filtered to comparative-anchored meanings. This provides lexibank-style interoperability for researchers running comparative analyses. The comparative wordlist is a fully CLDF-conformant Wordlist in its own right, with its own metadata file declaring conformance.

### Segmentation

`Root_Segments` (tokenized Root_IPA for cognate-detection tools) is derived at output time from `Root_IPA`. The source spreadsheet stores only Root_IPA; segmentation is generated when downstream tools need it.

---

## Encoding notes

The current encoding is a multi-sheet Excel workbook with one sheet per entity. The regeneration script reads the workbook and emits CLDF CSVs.

This encoding is a pragmatic medium-term choice. The conceptual model described above is what migrates when EALex eventually adopts a database-backed architecture (PostgreSQL or similar). At that point:

- Meanings, Forms, Languages, Sources, MeaningRelations, Cognates become database tables with proper indexing and foreign key constraints.
- A separate Media table joins to Forms via Form_ID for audio, video, and image references (deferred from the current schema; will be added when multimedia work begins).
- The web frontend, API, and any community contribution tooling sits on top of the database.
- CLDF remains an export format produced from the database, alongside other export formats (JSON-LD, GraphQL, etc.) as needed.

The conceptual model described in this document is the specification for that eventual migration.

---

## Versioning

EALex follows semantic versioning at the dataset level:

- **MAJOR** version bumps for breaking schema changes (renaming tables, changing foreign keys, removing fields)
- **MINOR** version bumps for additive changes (new languages, new columns, new rows)
- **PATCH** version bumps for corrections (typos, coordinate adjustments, gloss fixes)

The version number is recorded in the CLDF metadata and in repository tags.
