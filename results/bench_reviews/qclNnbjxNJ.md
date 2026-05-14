Now I have all the information needed. Let me write the final consolidated review.

---

## Summary

This paper identifies and formalizes a genuinely underexplored problem in interventional causal discovery: post-treatment selection bias, where samples are selectively retained after interventions (e.g., quality control filtering in gene perturbation studies). The authors show that existing interventional frameworks conflate true causal relations with selection-induced dependencies, propose a new formulation using augmented DAGs with an explicit selection variable, define a refined equivalence class (FI-Markov equivalence) with a corresponding graphical representation (F-PAG), and develop a provably sound and complete algorithm (F-FCI) that leverages intervention-based CI patterns to distinguish causation from selection. Experiments on synthetic and real-world single-cell perturbation data demonstrate improved recovery of causal relations compared to standard interventional discovery baselines.

## Strengths

- **Novel problem formulation with clear motivation**: The paper demonstrates through Figure 1 and Lemma 1 that existing interventional causal discovery frameworks cannot distinguish direct causation from post-treatment selection because both produce the same invariance/variation pattern (variant marginal, invariant conditional). This gap is well-articulated and genuinely not addressed by prior work.

- **Coherent theoretical framework**: The introduction of FI-Markov equivalence (Definition 2) and the F-PAG graphical representation (Definition 5) provides a principled, finer-grained characterization of causal structures under post-treatment selection. Lemmas 2–4 and Theorem 2 give explicit graphical criteria linking inducing paths and intervention-induced CI patterns to edge marks (tail, arrowhead, square), enabling distinctions that standard PAGs cannot capture.

- **Algorithm with formal guarantees**: The F-FCI algorithm (Algorithm 1) is novel in its use of hard interventions on Type I inducing nodes (Step 2.3) to break selection-induced ambiguity. Theorems 3 and 4 establish soundness and completeness, providing theoretical grounding for the approach.

- **Empirical validation**: Figure 6 shows consistent improvements in Precision (+5% on average) and lower SHD over six baseline methods (GIES, IGSP, UT-IGSP, JCI-GSP, FCI-interven, CDIS) across varying graph sizes, sample sizes, and intervention types. The real-world application to Norman et al. single-cell perturbation data demonstrates practical relevance.

## Weaknesses

### Fatal
None.

### Major
- **Evaluation metric mismatch**: The paper reports DAG Precision and DAG SHD against a ground-truth DAG, but the algorithm outputs an F-PAG—a partial ancestral graph with circles, squares, and special edge marks representing equivalence-class uncertainty. There is no description of how partial orientations (e.g., circles, squares) are mapped to deterministic DAG edges for metric computation. This inflates reported performance and makes it impossible to assess whether the method is genuinely recovering the DAG or producing a coarse equivalence class that happens to align with the ground truth. The field-standard approach would evaluate edge-mark recovery or orientation accuracy within the equivalence class.

- **Incomplete experimental comparison**: All baseline methods (GIES, IGSP, UT-IGSP, JCI-GSP, FCI-interven, CDIS) assume no selection bias. While demonstrating their failure under selection is informative, the paper does not compare against any method that explicitly models selection bias (e.g., FCI variants with selection bias, or MAG-based approaches that treat S as a hidden selection node). Without such a comparison, we cannot assess whether the improvement comes from modeling selection bias in general, or specifically from the proposed post-treatment selection formulation. This weakens the evidence for the paper's central claim of uniquely disambiguating causation from post-treatment selection.

### Minor
- **Simulation details incomplete**: The description of how intervention targets are selected is missing from Section 5.1 (only the graph generation and selection mechanism are described). Since the method's key innovation (Step 2.3) depends on having hard interventions on Type I inducing nodes, the distribution of intervention targets directly affects performance. The experimental results cannot be fully interpreted without this information. (The accompanying code repository partially mitigates this.)

- **Algorithm pseudocode rendering**: Step 2.2 in Algorithm 1 shows all CI condition tuples as "(⟂, ⟂, ⟂, ⟂)", which is a PDF-parsing artifact—the original submission presumably had distinct ✓/✗ patterns mapping to Figure 4(i). This makes the core orientation logic unreadable from the current text and harms reproducibility, though the GitHub repository provides a reference implementation.

- **Real-world evaluation lacks causal ground truth**: The gene regulatory network evaluation uses Enrichr (a gene-set enrichment tool) as prior knowledge, which tests for statistical enrichment rather than validating causal regulatory relationships. This makes the real-world results suggestive but not confirmatory.

### Trivial
None.

## Nice-to-Haves
- An ablation study varying the fraction of Type I inducing nodes that receive hard interventions, to quantify how the method degrades when the intervention coverage is incomplete. The authors already acknowledge this dependence as a limitation in Section 6; quantifying it would strengthen the contribution.
- Clarification of whether the approach can be extended to soft interventions on inducing nodes, since the current formulation requires hard interventions for Step 2.3.
- A detailed walkthrough example (e.g., one graph from Figure 4) showing CI test outputs and the resulting F-PAG, to make the algorithm's behavior transparent.

## Removed Points

These points were flagged by one reviewer but are removed from the main review after verification against the paper.

- **"S is unobserved and cannot be conditioned on in CI tests, invalidating the entire framework"**: The paper explicitly states (line 95) that S is not measurable. The CI patterns in Figure 4(i) that include S are d-separation characterizations in the augmented DAG, which map directly to testable CIs in the selected data without S. Specifically, under faithfulness in the selected subpopulation, X_A ⟂_d X_B | X_C, S in the DAG ⇔ X_A ⟂ X_B | X_C in p(X|S=1). The algorithm (Step 2.1) correctly tests CIs without S. This is the standard approach in causal discovery with selection bias (cf. Spirtes et al., 2000; Zhang, 2008b) and does not invalidate the framework.

- **"Lemma 3–4 make false assumptions about invariance holding under selection"**: The lemmas characterize when interventions alter marginal or conditional distributions in terms of the augmented DAG with S. Since all data is conditional on S=1, the d-separation relations in the augmented DAG correctly imply the corresponding (in)variances. The reviewer's concern about invariance "disappearing in the selected sample" conflates the theoretical characterization (d-separation in the DAG) with the empirical test (CI in the selected data), which are linked by Theorem 1.

- **"Figure 1(c)–(d) argument is not compelling because the same skeleton can arise from latent common causes"**: The paper acknowledges this and resolves it later through additional hard interventions on X₃ (Section 3.2, Figure 4 discussion). The introduction's role is to motivate the problem, not to provide the full solution at that point.

- **"Missing appendix, missing proofs"**: The parser strips appendices from all papers; the original submission contains them. Per review guidelines, this is not a valid criticism.

- **"Algorithm Step 2.2 has garbled/duplicate conditions"**: The identical "(⟂, ⟂, ⟂, ⟂)" patterns across all six orientation rules are PDF-parsing artifacts. The original submission uses distinct ✓/✗ symbols from Figure 4(i). This is a formatting issue, not an author error.

- **Various typos/spelling/grammar/formatting criticisms**: These are parser artifacts (the paper uses LaTeX symbols that don't survive extraction) and per the guidelines are not substantive weaknesses.

- **Strength Finder claim about "strong empirical performance" without qualification**: This strength is retained but contextualized—the performance improvement over baselines is genuine, though the metric mismatch tempers the interpretation.

## Novel Insights

The paper's key insight—that standard interventional invariance patterns (variant marginal, invariant conditional) are shared by both direct causation and post-treatment selection, but that additional hard interventions on intermediate nodes along inducing paths can break this symmetry—is genuinely novel. This observation goes beyond the established FCI/selection-bias literature, which typically treats selection as a global phenomenon to be marginalized out, rather than as a structural feature whose differential response to interventions can be exploited for finer-grained identification. The square edge mark and the Type I/Type II inducing node taxonomy are useful conceptual contributions that extend the graphical vocabulary of causal discovery.

## Suggestions
- Describe the mapping from F-PAG output to the DAG-level Precision/SHD metrics used in evaluation, or switch to edge-mark recovery metrics standard for partial ancestral graphs.
- Include at least one baseline that handles selection bias (e.g., FCI with selection bias) to isolate the contribution of the post-treatment formulation.
- Report the distribution of intervention targets and Type I inducing node coverage in the simulation setup to contextualize the performance results.
- Restore the CI pattern symbols in Algorithm 1 Step 2.2, as these are critical for readers to understand the orientation logic.

## Score and Decision

### Anchor comparison:
- **mA78uXqcnl** (avg 7.00, Accept Oral): Stronger theoretical polish and cleaner experiments. The paper under review is less polished but comparably novel in problem scope.
- **s0nYSwlV3I** (avg 5.00, Accept Poster): Comparable in contribution quality—both have novel theory, algorithms, and room for improvement in evaluation. Our paper's problem is arguably more novel; s0nYSwlV3I's evaluation is clearer.
- **wnFbqvUJ6D** (avg 5.00, Reject): Similar quality of theoretical contribution, but our paper has a more clearly motivated problem and better experimental breadth. The divergent reviewer scores on wnFbqvUJ6D reflect polarizing assumptions; our paper's assumptions are more standard in the causal discovery community.
- **V7pT2ZRoTB** (avg 4.50, Accept Poster): Narrower scope (FNR concentration bounds for one score function) but cleanly executed. Our paper is broader and more ambitious, with correspondingly more loose ends.
- **lYearSsgXj** (avg 4.50, Reject): Both tackle coupled bias problems. lYearSsgXj has strong assumptions that reviewers deemed impractical. Our paper's assumptions (Type I inducing nodes) are explicitly acknowledged as limitations and are more plausible in the interventional settings considered.
- **HfiRzzmFt8** (avg 4.00, Reject): Major clarity and motivation issues. Our paper is substantially clearer and better motivated.
- **r4TvgVFo9L** (avg 3.50, Reject): Missing baselines and unclear presentation. Our paper has stronger experiments and a more coherent theoretical framework.

This paper makes a genuine contribution to a novel problem in interventional causal discovery, with a coherent theoretical framework and a working algorithm backed by soundness/completeness proofs. The evaluation has real issues (metric mismatch, incomplete baselines) that prevent a higher score but do not fundamentally undermine the core claims. These issues are addressable in a rebuttal or revision. Placed among the anchors, it sits comfortably at the Accept (Poster) level.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>