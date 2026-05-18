Now I have full clarity on all the claims. Let me write the consolidated review.

## Summary

Know2BIO is a large, multi-source biomedical knowledge graph benchmark that integrates data from 30 sources across 11 biomedical categories (~219K nodes, ~6.2M edges, 108 edge types). The paper's key structural contributions are a dual-view design (instance + ontology views connected by bridge nodes), multi-modal node features (text descriptions, sequences, structures), and extensive benchmarking of 13 KG representation learning models across three view configurations.

## Strengths

1. **Substantially broader coverage than existing biomedical KG benchmarks.** Table 1 shows Know2BIO has 30 source databases (the highest among compared KGs) and 108 edge types—more than triple the next closest benchmark (OpenBioLink with 30). It covers 11 biomedical categories including under-represented ones like anatomy-specific gene expression and transcription factor regulation, which are absent from prior benchmarks (Section 3).

2. **Dual-view architecture with explicit instance/ontology separation.** Section 3.2 and Figure 1 define separate ontology and instance views connected by bridge nodes. The paper benchmarks all three views (ontology, instance, whole) separately across 13 models, providing a concrete evaluation framework for multi-view learning methods. No other biomedical KG in Table 1 offers this distinction.

3. **Provision of multi-modal node features.** Section 3 reports node features including text descriptors (~208,500 nodes), amino acid sequences (~21,000 proteins), SMILES (~7,200 compounds), protein structures (~21,000 proteins), and DNA sequences (~22,000 genes). This is a qualitative advance over most benchmarks (e.g., Hetionet, DRKG, OGB-biokg) that provide only structural triples.

4. **Rigorous multi-model benchmarking with hyperparameter tuning.** Section 4.2 details a beam-search hyperparameter optimization over batch size, learning rate, and negative sampling ratio with early stopping. Results are reported across three view splits (Tables 4–11) for 13 models spanning Euclidean, complex, and hyperbolic spaces, providing thorough baselines for future work.

## Weaknesses

### Fatal

None.

### Major

None. The paper's core contribution—a comprehensive, multi-source biomedical KG with dual-view structure and extensive benchmarking—is well-supported. The issues below are addressable limitations, not structural flaws.

### Minor

1. **The "automatically updatable" claim is asserted without concrete demonstration.** The paper lists this as a core contribution (bullet point 2) and uses it to distinguish Know2BIO from benchmarks like OpenBioLink that "have not been continually updated." However, the only description of the update mechanism (line 152) is that "users must create free accounts… and then manually download two files into the input folder. After that, all scripts can be run." This describes a re-runnable build pipeline, not an automated update system with change detection or version tracking. There is no demonstration (e.g., a comparison of version 1 vs. version 2 node/edge counts, a description of how changes propagate from source databases into the KG). The limitations section (line 368) acknowledges that "incomplete knowledge… can bias the data, resulting in different results over time" but does not leverage or demonstrate the claimed update capability. For a benchmark paper, this does not invalidate the dataset, but the claim is oversold relative to what is shown.

2. **The "dual view" is acknowledged to partly arise from unresolved entity alignment.** The paper is transparent about this (lines 150–151): compound nodes have two types because "an incomplete amount of such identifiers could be aligned"; pathways have three types because they "could not be aligned—even by loose definitions"; anatomy and disease have two types for similar reasons. The paper then frames these as an intentional dual-view design. The transparency is commendable, but it means the boundary between instance and ontology views is blurrier than a cleanly designed multi-view benchmark would ideally have. Users interpreting results from the two views should be aware that some separation is driven by alignment pragmatics rather than semantic design. This does not invalidate the dataset's value but moderates the claimed contribution.

3. **Confidence thresholds for STRING and DisGeNET are not reported.** The construction section (line 112) notes that these sources provide confidence scores and that "threshold scores … were chosen for each source based on evidence-backed reasons," and the limitations section (line 369) acknowledges "some arbitrariness." However, the specific threshold values are never reported. Since these sources contribute a large fraction of edges (protein-protein and gene-disease associations), the threshold choice directly affects graph density and noise. Reporting the values and rationale would improve reproducibility and help users who may want to adjust thresholds for their own use.

4. **Best hyperparameter configurations per model are not reported.** The paper describes the beam search space (batch size, learning rate, negative sampling ratio) but does not report which configuration was selected for each of the 13 models. Since hyperparameter choice can significantly affect rankings (as the paper itself notes, citing Bonner et al.), omitting these values makes it harder for others to reproduce exact results or assess whether some models were disadvantaged by the search range.

5. **Multi-modal node features are provided but not evaluated in any experiment.** The paper lists multi-modal features as a contribution (bullet point 3) and the abstract frames it as "enabling … multi-modal data integration strategies." Yet the entire evaluation (Section 4) uses only KG triples for link prediction with structural models; no experiment uses text descriptions, sequences, or structures. For a dataset paper, providing features as a resource is itself a valid contribution, and it is reasonable to focus the benchmark on structure-based methods. However, the framing as an "enabling" contribution would be strengthened by even a simple proof-of-concept (e.g., a bag-of-words text feature baseline on one view). As written, there is a mismatch between the claimed significance and what is demonstrated.

### Trivial

None.

## Nice-to-Haves

- A brief comparison of Know2BIO version 1 vs. a hypothetical re-built version to substantiate the "evolving" claim.
- An analysis of alignment completeness (e.g., percentage of identifiers successfully mapped per source) to help users understand where duplication exists.
- Reporting of edge-type counts for source databases in Table 1 (e.g., noting OGB:biokg is derived from a single source rather than leaving the cell as "/").

## Removed Points

- **"Table 1 omits edge types for CKG, iBKH, OGB:biokg, OpenBioLink, PharmKG"** — Factually wrong. All entries in the #Edge types column have filled values (CKG=47, iBKH=18, OGB:biokg=6, OpenBioLink=30, PharmKG=29). The "/" appears in the #Source databases column for OGB:biokg, not in the edge types column. This criticism is removed as incorrect.

## Novel Insights

None beyond the paper's own contributions. The reviews surface that the dual-view structure is partially driven by alignment pragmatics rather than pure design, and that the "evolving" claim lacks demonstration—but these are observations about gaps in the paper's presentation, not novel insights about the subject matter.

## Suggestions

1. Either demonstrate the update mechanism with a concrete example (e.g., number of new nodes/edges between two builds) or downgrade the "evolving" claim from a headline contribution to a design goal described in future work.
2. Report the specific confidence thresholds used for STRING and DisGeNET in the construction section, with a brief rationale for each.
3. Report the best hyperparameter configuration found per model (can be in supplementary material).
4. Add one simple experiment using node features (e.g., DistMult + bag-of-words text descriptors vs. feature-less DistMult on one view) to substantiate the multimodal claim. Even a small-scale demonstration would significantly strengthen the paper.
5. Clarify the filtered ranking procedure: the current description ("filtered by edge types' respective node types") is ambiguous about whether it follows the standard "filtered" setting (removing all other valid triples from the candidate list).

## Score and Decision

This is a solid benchmark/dataset paper. The core contribution—a comprehensive, multi-source biomedical KG with dual-view structure, multi-modal features, and extensive baselines—is genuine and well-supported. The weaknesses are addressable: some claims (particularly "automatically updatable") are somewhat oversold, and several construction details (confidence thresholds, hyperparameter configurations) are under-specified. None of these issues threaten the dataset's value or the validity of the benchmarking results. The paper is clearly within the acceptance threshold for a benchmark/dataset contribution.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>