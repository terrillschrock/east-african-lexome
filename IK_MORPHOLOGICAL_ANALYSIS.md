# FormTable: Morphological_Analysis Column Spec (Ik)

## Scope

- Applies to **Form** and **Source_Form**, which are assumed to differ only orthographically. One value covers both.
- Does **not** apply to Root, which is unanalyzable by definition.
- If a row shows a morphological (not just orthographic) difference between Form and Source_Form, flag it in the comment field rather than splitting the column.

## Format

- The cell is a closed-vocabulary string of labels, with no free text.
- `root` (lowercase) is the placeholder for the unanalyzable base. The lexical meaning is carried by the Meaning link.
- All other labels are UPPERCASE.
- `-` separates affixes, in surface order. The cell always begins with `root`.
- `+` separates compound members.
- `.` joins two categories fused in a single morpheme (Leipzig convention).
- Explanations go in a separate comment field, never in this cell.

## Label inventory

| Label | Meaning |
|---|---|
| `root` | unanalyzable base |
| `NOM` | nominative case suffix (replacive: replaces the final vowel of the morpheme it attaches to; the suffix segment surfaces full, devoiced, or deleted) |
| `PAT` | patientive nominalizer (attaches to verb roots, derives a noun) |
| `ABST` | abstractive nominalizer |
| `SGV` | singulative suffix (nouns) |
| `INF.TR` | transitive infinitive suffix |
| `INF.INTR` | intransitive infinitive suffix |
| `AND` | andative |
| `VEN` | venitive |
| `INCH` | inchoative |
| `COMPL` | completive |
| `STAT` | stative |
| `PHYS1` | physical attribute 1 |
| `PHYS2` | physical attribute 2 |
| `PASS` | passive |
| `MID` | middle voice |
| `PLUR` | pluractional (follows the Ik grammar; distinct from `PL`, plural, which is not used in this column) |

Add labels here before using them in data. Candidates still to be decided: further case values (only needed if non-citation forms are entered), causative, and others.

## Rules by category

| Category | Pattern | Example |
|---|---|---|
| Noun, citation form | `root-NOM` | `root-NOM` |
| Deverbal noun (patientive), citation form | `root-[extensions]-PAT-NOM` | `root-PAT-NOM`, `root-PLUR-PAT-NOM` |
| Noun with singulative, citation form | `root-SGV-NOM` | `root-SGV-NOM` |
| Verb, citation form | `root-[extensions]-INF.TR-NOM` or `root-[extensions]-INF.INTR-NOM` | `root-PLUR-VEN-INF.INTR-NOM` |
| Verb stem, stative | `root-STAT-INF.INTR-NOM` | `root-STAT-INF.INTR-NOM` |
| Verb stem, physical attribute | `root-PHYS1-INF.INTR-NOM` or `root-PHYS2-INF.INTR-NOM` | `root-PHYS1-INF.INTR-NOM` |
| Verb stem, passive | `root-PASS-NOM` | `root-PASS-NOM` |
| Verb stem, middle inchoative | `root-MID-INCH-INF.INTR-NOM` | `root-MID-INCH-INF.INTR-NOM` |
| Verb stem, pluractional | `root-PLUR-INF.TR-NOM` | `root-PLUR-INF.TR-NOM` |
| Verb stem, extension (`AND`, `COMPL`, `INCH`, or `VEN`) before the infinitive | `root-[ext]-INF.TR-NOM` or `root-[ext]-INF.INTR-NOM` | `root-VEN-INF.TR-NOM` |
| Verb stem, extension (`AND`, `COMPL`, `INCH`, or `VEN`) after the infinitive | `root-INF.TR-[ext]-NOM` or `root-INF.INTR-[ext]-NOM` | `root-INF.INTR-COMPL-NOM` |
| Verb stem, no identified extension | `root-INF.TR-NOM` or `root-INF.INTR-NOM` | `root-INF.INTR-NOM` |
| Compound | `[analysis]+[analysis]` | `root-NOM+root-NOM` |
| Unanalyzable form (including unanalyzable loans) | `root` | `root` |

## Conventions

1. **Nominative.** Citation-form nouns are always `root-NOM`, whether the suffix is full, devoiced, or deleted on the surface. The analysis is underlying, not surface. `NOM` is replacive: it replaces the final vowel of every morpheme it attaches to (the root, `PAT`, `SGV`, etc.), so the Form lacks a vowel that the underlying stem has. The same is true of the instrumental, which is not expected in this database and is therefore not in the inventory.
2. **Infinitive.** Record the suffix actually present (`INF.TR` vs. `INF.INTR`). Do not infer it from the POS or transitivity columns, because extensions can change valence.
3. **Order and co-occurrence.** `NOM` is always the last suffix, on nouns and verbs alike. `SGV` and `PAT` never co-occur on one noun.
4. **Extension order.** Mirror the surface order of the extensions in the form. Extensions may occur between the root and `PAT`.
5. **Segmentation.** Forms carry no hyphens. Users cannot recover the morpheme breaks by comparing Form to Root: because `NOM` replaces the final vowel of the preceding morpheme (in nouns and verbs alike), the Form is not Root + suffix, and a devoiced or deleted `NOM` may have no clear surface string. If boundary marking is wanted later, add an optional `Segmentation` column, filled only where boundaries are clear, with a convention for the replaced vowel. Keep `Morphological_Analysis` a pure label string.
6. **Validation.** Check every cell against the inventory. Reject unknown labels. For plain `root-NOM` nouns, also check that the Form matches the Root minus its final vowel (allowing for orthography); flag mismatches for review. This check does not apply to `PAT` or `SGV` nouns, whose Form includes the suffix. For those, a check of Root + extensions + suffix, minus the final vowel, becomes possible once the surface shapes of the suffixes and extensions are recorded.

## Open points

- Is the verb citation form always the infinitive?
- Should surface realization of NOM (full / devoiced / deleted) be kept in a separate `NOM_Realization` column?
- What convention should the optional `Segmentation` column use for the replaced root-final vowel, if it is kept for nouns?
- Are `SGV` and `PAT` the same morpheme? They never co-occur, and `PAT` attaches to verb roots while `SGV` attaches to noun roots. Until this is settled they stay as separate labels, which can be merged later with a find-and-replace.
- Remaining labels beyond those listed above.
