Now I have sufficient information from the paper to verify claims. Let me construct the consolidated review.

## Summary

This paper empirically challenges the prevailing belief that spectral augmentations are necessary for contrast-based graph self-supervised learning (CG-SSL). It argues that simple edge perturbation (edge dropping for node-level tasks, edge adding for graph-level tasks) consistently matches or outperforms spectral augmentation methods like SPAN, while being orders of magnitude cheaper computationally. The paper provides evidence through (1) comprehensive experiments across 7 node-level and 5 graph-level datasets under 4 CG-SSL frameworks, (2) a spectral degeneration analysis showing that edge perturbation collapses the spectral distinguishability of graphs, and (3) a Spectral Perturbation Augmentor (SPA) experiment designed to destroy spectral information while preserving topology.

## Strengths

- **Well-motivated paradox that raises a genuinely important question.** The paper clearly identifies a contradiction in the spectral augmentation literature: SpCo/GASSER argue for preserving specific spectral components, while SPAN maximizes spectral change — yet all claim performance gains. This paradox is stated crisply in the Introduction and provides strong motivation for questioning whether spectral information is the actual driver of performance.

- **Comprehensive empirical evaluation across diverse setups.** The paper compares edge perturbation against spectral augmentations under 4 CG-SSL frameworks (MVGRL, GRACE, BGRL, G-BT) on 7 node-level and 5 graph-level datasets (Tables 2, 3). This breadth makes the negative finding (spectral augmentations are not necessary) more credible than if tested on only one framework.

- **The SPA experiment is a clever causal probe.** The idea of destroying spectral information while preserving topological proximity (Section 7.2) is the paper's most novel contribution. If the spectral distances were verified, this experiment would directly show that SPAN's performance does not depend on spectral cues — a strong causal claim that goes beyond correlation.

- **Clear efficiency advantage demonstrated.** Table 1 quantifies the time and space complexity gap between spectral operations (O(n³) eigenvalue decomposition) and linear-time edge perturbation, with empirical runtime on PUBMED. This gives the paper a practical impact dimension beyond accuracy comparisons.

- **Ablation on GNN encoder types (GAT, GPS) shows the result is not GCN-specific.** Section 6.3 extends the main results beyond GCN to GAT and GPS encoders, strengthening the generality of the findings.

## Weaknesses

### Fatal
None.

### Major

- **Undocumented hyperparameter tuning procedure for spectral baselines.** The paper's central quantitative claim depends on a fair head-to-head comparison between edge perturbation (DROPEDGE/ADDEDGE) and SPAN. The paper states that "best parameters" are used (Section 7.1) but does not describe how hyperparameters were selected for each method within each framework/dataset. Edge perturbation has a single drop/add rate; SPAN has multiple knobs (perturbation budget, spectral norm weight). If SPAN hyperparameters were taken from defaults while edge perturbation rates were grid-searched, the comparison is structurally unfair. Section 6.1 mentions "fair comparisons" but provides no search ranges, tuning budgets, or procedure. This undermines the reliability of Tables 2 and 3 as support for the claim that edge perturbation is "optimal."

- **SPA experiment lacks quantitative verification of spectral destruction.** Section 7.2 introduces SPA to "eliminate" spectral information, but the paper does not report actual spectral distances (L2 norms of eigenvalue differences) between original and SPA-perturbed graphs for any dataset. The claim that "spectral information is destroyed" is supported only by a reference to "properly chosen hyperparameters" and Fig. 3 (which only shows performance, not spectral change). Without numerical evidence that the spectral manipulation was effective, the experiment cannot support the paper's strongest causal claim. Additionally, SPA's effect on other topological properties beyond spectral information is not assessed, leaving open alternative explanations for why performance is maintained.

### Minor

- **The argument that shallow GNNs "cannot capture spectral information" is overstated.** Section 4 argues that 1–2 layer GNNs have limited receptive fields and therefore cannot leverage spectral information. This conflates expressive power with learnability: even a 2-layer GCN can approximate polynomial spectral filters of degree 2 (ChebNet-like behavior), and spectral augmentations that modify local structure can affect training dynamics even without the encoder "seeing" the full Laplacian spectrum. The empirical evidence (Fig. 1) shows shallow encoders work best, which is consistent with the paper's argument but does not *prove* that spectral information is inaccessible. The conclusion does not depend solely on this argument, but it weakens the theoretical scaffolding.

- **Statistical significance is not reported for most results.** In Table 2, only a few cells show standard deviations; the majority do not. Table 3 (graph classification) reports no variance at all. For a paper making a strong negative claim that challenges established methods, the absence of uncertainty quantification makes it impossible to assess whether the reported advantages of edge perturbation are reliable or within noise. This is particularly important for small-dataset graph classification where variance can be high.

- **The evidence primarily targets one spectral method (SPAN).** SpCo is included only for its original setting (GRACE on a subset of datasets), and GASSER results are adopted from prior work without confirmation of identical experimental setups (Section 6.1). The paper acknowledges this limitation but does not discuss how it constrains the generalizability of the conclusion that "spectral augmentations" broadly are unnecessary, rather than SPAN specifically.

- **Degeneration analysis (Section 7.1) is qualitative only.** The claim that edge perturbation makes graph spectra "highly overlapped" is supported by visual histograms (Fig. 2) but no numerical measures (e.g., pairwise KL divergence, L2 distances between average spectra) are reported. This weakens the strength of the claim that "GNN encoders can hardly learn spectral information."

### Trivial
None (confirmed formatting issues appear to be parser artifacts).

## Nice-to-Haves

- **"No augmentation" baseline.** The paper does not compare edge perturbation against the trivial baseline of using the same view twice (no augmentation). This would help establish the absolute benefit of any augmentation and contextualize the advantage.
- **Hyperparameter sensitivity analysis.** An analysis of how performance varies with drop/add rate for edge perturbation (and perturbation budget for SPAN) on at least one representative dataset per task would demonstrate robustness and rule out cherry-picking.
- **Code release.** The paper promises future release; providing the code at time of publication would strengthen reproducibility.
- **Scope note on downstream tasks.** The experiments cover only classification tasks; noting explicitly whether the findings extend to link prediction, anomaly detection, or regression would manage expectations.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Criticism that the paper doesn't compare against methods outside its stated scope (e.g., "missing related works"):** Removed per hard rules — I cannot verify existence of missing references.
- **"The paper should cover other downstream tasks (link prediction, anomaly detection, regression)":** Removed as scope creep. The paper is focused on classification tasks, which is standard for this literature and a coherent scope.
- **Pure formatting/style nitpicks and claims about missing appendix/proofs:** Removed per hard rules — parser artifacts.
- **Criticism about "the authors should add Y domain / Z additional tasks":** Removed as scope creep — the paper's claim is about CG-SSL on standard benchmarks, which it covers adequately.

## Novel Insights

The reviews surface one genuinely novel insight beyond the paper's own contributions: the SPA experiment (Section 7.2) implicitly reveals that the spectral augmentation methods' generative processes are constrained to a specific family of graphs, and that counterexamples exist within the same topological neighborhood. This insight — that spectral augmentation methods define a generative process that does not model the true graph distribution, and that their success is attributable to properties other than spectral cues — is interesting in its own right and could be developed further. The reviews also highlight that the paper's framing as challenging "spectral augmentations" broadly, when the evidence is mostly against SPAN, points to a useful reframing opportunity: the paper might be better positioned as a systematic evaluation of whether SPAN's specific design choices matter, rather than a blanket rejection of spectral methods.

## Suggestions

1. **Document the hyperparameter tuning protocol explicitly.** For each augmentation method (DROPEDGE, ADDEDGE, SPAN) and each framework-dataset pair, report the search range, search strategy (e.g., grid search on drop rate), and the selected optimal value. Even a summary table in the appendix would largely address the fairness concern.
2. **Report spectral distances for the SPA experiment.** For each dataset, provide the L2 distance between original and SPA-perturbed spectra alongside the performance comparison. Consider also reporting a topological proximity measure (e.g., edge overlap ratio) to verify that SPA preserves structure as claimed.
3. **Add standard deviations to all experimental results.** Without uncertainty estimates, the reader cannot assess whether the reported advantage of edge perturbation over SPAN is statistically meaningful.
4. **Add a "no augmentation" baseline.** Include the performance of training with identical views (no topological augmentation) for at least one representative framework and dataset to calibrate the absolute benefit of any augmentation.
5. **Soften the theoretical claim about shallow GNNs.** Replace "cannot capture spectral information" with "have limited capacity to capture spectral information" and note that the primary evidence for the paper's conclusion is empirical, not theoretical.

## Score and Decision

Based on the above analysis: the paper tackles an important and timely question with a well-designed set of experiments that, despite their gaps, represent a meaningful contribution to the field. The weaknesses are real but addressable — primarily requiring better documentation of tuning procedures, quantitative verification of the SPA experiment, and uncertainty quantification — rather than fundamental methodological flaws. The paper does not propose a new method, and it should not be judged on that rubric; as an empirical study challenging a prevailing assumption, its value is in the clarity and rigor of its evidence. The main claims (that simple edge perturbation is competitive with spectral augmentations and that spectral cues may not be the driver of performance) are reasonably supported, though the scope should be narrowed from "spectral augmentations" to "SPAN-like spectral augmentations."

**Score:** 6.0 / 10 (weak accept: has genuine contributions but needs substantial revision to close evidential gaps before the claims are fully convincing)

**Decision:** Accept

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>