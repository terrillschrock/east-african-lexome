# Ethics Statement

The East African Lexome (EALex) is committed to building research infrastructure that serves the languages and communities of East Africa, not just the scholars who study them. This document articulates the ethical principles guiding the project at its current stage and the directions it intends to grow.

## Foundational acknowledgement

The languages documented in EALex belong to their speakers and communities. EALex aggregates and structures data drawn from published linguistic sources; it does not lay claim to the languages themselves, the cultural knowledge they encode, or the communities they belong to. The project exists to make existing scholarly documentation more discoverable, comparable, and useful — not to substitute for the relationships and rights that connect languages to the people who speak them.

## Current stage: aggregation and direct contribution

In its present phase, EALex's data comes from two streams. The primary stream is **published linguistic sources** — dictionaries, grammars, wordlists, and survey reports — whose authors have already navigated the ethics of working with the speech communities involved. The secondary stream is **direct contributions from linguists**, who may submit unpublished lexical data from their own fieldwork or research, with their consent and under the project's contributor terms.

Each stream carries a different ethical profile, and EALex commits to handling both responsibly.

For data drawn from published sources, EALex commits to:

- **Full source attribution.** Every form in the dataset is linked to its bibliographic source. The provenance of every datum is preserved and transparent.
- **No aggregation of culturally restricted material.** Where sources mark vocabulary as sacred, secret, restricted to particular contexts, or otherwise sensitive, EALex excludes that material from aggregation. This commitment applies with particular force to language-specific vocabulary — ethnobiological terminology, ritual roles and practices, kinship and age-set categories, and other meanings that East African languages lexicalize in culturally embedded ways. EALex's data model accommodates such vocabulary as first-class data, which raises rather than lowers the standard of vigilance: the same model that lets the project document a community's distinctive lexicon also imposes responsibility for not aggregating material the community considers restricted.
- **Honest representation.** Data is presented with appropriate caveats about uncertainty. Speculative or doubtful forms are noted in the Comment field rather than presented as confirmed, and source attribution is preserved so that downstream users can independently assess the reliability of any datum. EALex does not over-represent the certainty of sources whose own data was preliminary.
- **Documentation of methodological choices.** Decisions about classification, inclusion, and reconciliation are documented openly — including cases where the project diverges from standard references like Glottolog or Ethnologue.

For data contributed directly by linguists, EALex additionally commits to:

- **Contributor warranty of right to share.** Contributors are asked to confirm that they have the right to share the data — that it was collected with appropriate consent, that no community-imposed restrictions are being violated, and that no third-party rights are infringed.
- **Clear attribution to the contributing linguist.** Direct contributions are credited to the linguist who collected and contributed the data, alongside any speech-community acknowledgements the contributor wishes to record.
- **Distinction between data streams.** The dataset records whether each form was extracted from a published source or contributed directly, so that downstream researchers can trace data lineage.
- **Responsibility for unpublished material.** Because direct contributions involve previously unpublished data, EALex takes special care to honor takedown and correction requests promptly, recognizing that the relationships between contributing linguists and the communities they work with are ongoing.

## AI involvement in data work

EALex is being assembled with substantive assistance from a large language model (Anthropic's Claude) acting as a sustained collaborator. The model's role goes beyond drafting documentation and includes participation in data-level work: helping organize and structure source bibliographies, assisting with the semantic domain tagging of incoming forms during imports, generating candidate analyses of citation forms into roots for maintainer review, and stress-testing methodological decisions through dialogue. This is a more substantive AI involvement than is typical in linguistic dataset projects, and EALex acknowledges it explicitly here rather than letting it sit unremarked.

Three commitments govern how AI involvement is handled:

- **Maintainer review of all AI-generated data.** Any data-level annotation produced or suggested by the AI — domain tags, root analyses, sense disambiguation, normalization decisions — passes through review by the project maintainer before being committed to the dataset. The AI generates candidates; the maintainer accepts, modifies, or overrides them. No AI output enters the dataset without that review.
- **Recoverability of AI-assisted decisions.** Where AI assistance has shaped specific data — e.g., domain tags suggested by an AI tool and accepted by the maintainer — that provenance is recoverable. The methodology is documented in the project's accompanying notes, and the patterns of AI involvement are described in release notes for each version.
- **Bias acknowledgment.** AI models trained on globally-distributed text data have known biases toward overrepresented languages and concepts. For East African languages — many of which are underrepresented in the training data of any large language model — AI suggestions are particularly likely to be wrong in specific, language-specific ways (folk-taxonomic categories that don't fit Indo-European-shaped expectations, ritual or pastoralist vocabulary outside the model's distribution, tonal and morphological structures that diverge from common patterns). This is one reason maintainer review is non-negotiable. The bias is acknowledged, not solved.

This disclosure complements the more general note on AI collaboration in the project README. ETHICS.md is the place where the disclosure carries weight, because data-level AI involvement is a methodological matter with ethical implications, not a stylistic choice about documentation drafting.

## Correction and takedown process

Communities, scholars, and custodians of linguistic knowledge can request correction or removal of specific data at any time. The process is intentionally low-friction:

1. Email the project lead at **terrill.schrock@gmail.com** with a description of the data in question and the requested action (correction, removal, additional context).
2. The project lead will respond within **two weeks** to acknowledge the request and discuss next steps.
3. Where requested removals are warranted, the data will be removed from the master dataset within **one month** and reflected in the next public release of EALex.
4. Removal requests are honored without requiring justification beyond a credible claim of standing — the project errs on the side of community concerns.

This process applies to individual entries, broader categories of data, or whole-language data as appropriate. The project is small enough at this stage that requests can be handled personally and responsively.

## Aspirational alignment

EALex aspires to align its practices with the **CARE Principles for Indigenous Data Governance** (Collective Benefit, Authority to Control, Responsibility, Ethics), the leading framework for ethical handling of indigenous data in research. Full operational implementation of these principles requires resources, governance structures, and community engagement that exceed what a single-maintainer project in its infrastructure-building phase can provide. EALex commits to deepening this alignment as the project matures, including:

- Establishing a community advisory structure as the project grows
- Pursuing partnerships with regional research institutions and language communities
- Developing language-specific consultation protocols for any future primary data collection
- Periodically revisiting and revising this ethics statement as the project evolves

## Future directions

EALex's current scope is the aggregation of existing published linguistic data and the curation of direct contributions from linguists. Should the project's resources and identified needs eventually permit primary fieldwork — whether to fill documented gaps, support communities seeking documentation of their own languages, or address scholarly questions that existing sources cannot answer — such work will be conducted in genuine partnership with the relevant speech communities, with explicit attention to consent, benefit-sharing, data sovereignty, and the priorities of the communities themselves. Any such expansion will be accompanied by a substantive revision of this ethics statement.

## A note on this statement

This ethics statement is a living document. It reflects the project's commitments at its current stage and is expected to evolve as the project matures, as community engagement deepens, and as norms in research ethics continue to develop. Suggestions for improvement are welcomed through the email contact above or via the project's GitHub Issues.

The statement is offered in the spirit of methodological transparency and good-faith commitment — not as a claim of perfection, but as a public articulation of where the project stands and where it intends to go.

---

*Last updated: May 2026*
