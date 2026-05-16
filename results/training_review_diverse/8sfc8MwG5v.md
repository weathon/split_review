Now I have all the information needed. Let me synthesize the final review.

## Summary

The paper proposes CONDA, a test-time adaptation framework for Concept Bottleneck Models (CBMs) built on foundation models. It first formalizes a taxonomy of distribution shifts (low-level vs. concept-level) and identifies three failure modes of CBM pipelines. CONDA then addresses these via three components: Concept-Score Alignment (CSA), Linear Probing Adaptation (LPA), and Residual Concept Bottleneck (RCB). Experiments across five datasets with different shift types, multiple FM backbones (CLIP ViT-L/14, BioMedCLIP), and three CBM construction methods show accuracy improvements of up to 28%.

## Strengths

1. **Principled framework where each component targets a formalized failure mode.** The paper provides the first formal taxonomy of distribution shifts for CBMs (Section 2.2) and maps three failure modes (non-robust concept bottleneck, non-robust classifier, incomplete concept set) directly to the three CONDA components (CSA, LPA, RCB). This design rationale is validated by the ablation analysis in Figure 3, which shows CSA dominates under low-level shifts while LPA/RCB dominate under concept-level shifts — confirming the connection between theory and method.

2. **Strong empirical results across diverse settings.** CONDA improves test-time accuracy by up to 28% across low-level shifts (CIFAR-10/100-C), concept-level shifts (Waterbirds, Metashift), and natural shifts (Camelyon17), using three different CBM construction approaches (post-hoc, unsupervised, GPT-generated) and multiple FM backbones. Performance matches or exceeds non-interpretable baselines (zero-shot, linear probing) on worst-group accuracy, showing that interpretability does not come at a cost.

3. **Component-wise ablation that validates the failure-mode analysis.** The paper explicitly tests each component in isolation (Figure 3) and finds that CSA alone excels under low-level shifts while LPA/RCB are critical for concept-level shifts. This empirically confirms the connection between the failure-mode taxonomy and the adaptation design, and the paper transparently reports that individual components can match the full pipeline on "pure" shift types.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **No comparison against generic TTA methods applied to the CBM pipeline.** The paper claims to be the first TTA approach for CBMs, but does not compare against straightforward applications of generic TTA methods (e.g., TENT — entropy minimization on the CBM predictor, or on the full backbone+pipeline). The central claim that specialized CSA/LPA/RCB components are necessary would be strengthened by showing that a simple entropy-minimization baseline does not achieve comparable gains. Without this, the value of the specialized design over off-the-shelf TTA is partially unclear.

2. **No statistical variance or significance reported.** All results in Table 1 and Figure 3 are single numbers without standard deviations, confidence intervals, or multiple seeds. The paper states it "randomly split" test data into batches, introducing randomness from batch order, yet no variance is reported. For a method claiming up to 28% improvement, uncertainty estimates are needed to assess reliability.

3. **Pseudo-label quality is unexamined.** The pseudo-labeling strategy combines zero-shot and linear probing predictors. The paper does not report pseudo-label accuracy on test data, nor analyze sensitivity to labeling errors — a well-known failure mode in TTA (confirmation bias). Understanding whether the method is robust to moderate labeling noise or depends on high-quality pseudolabels would strengthen the analysis.

4. **No hyperparameter sensitivity analysis.** The method introduces four regularization weights (λ_frob, λ_sparse, λ_sim, λ_coh) and the number of residual concepts r, but provides no analysis of how performance varies with these choices. For a method intended for deployment without labels, users need guidance on default settings.

5. **No analysis of computational cost.** CONDA involves three separate optimization steps per batch plus pseudo-label generation from an ensemble. A wall-clock comparison to the unadapted CBM (and a simple TTA baseline) would help practitioners understand practical overhead.

### Trivial

- **Mahalanobis Gaussian assumption unchecked.** CSA models class-conditional concept scores as Gaussians and uses Mahalanobis distance. The paper does not check whether this assumption holds or discuss robustness to its violation — a minor technical caveat standard in this literature.
- **Top-k parameter for RCB coherency not specified.** The coherency regularization (Eqn. 13) uses top-k nearest neighbors but does not state how k is chosen.
- **Interpretability analysis is qualitative.** The claim that three residual concepts correspond to "feathers, wings, and beak" relies on manual inspection without quantitative validation of semantic alignment. This is standard for interpretability analysis but should be caveated as qualitative.

## Nice-to-Haves

- Adding TENT (or another simple TTA baseline) applied to the CBM predictor as a comparison would directly test whether the specialized components are necessary.
- Reporting pseudo-label accuracy on each test set, broken down by domain, would clarify the method's robustness to labeling noise.
- A brief analysis of performance variance across different random batch orders would address concerns about online adaptation stability.
- Running 3–5 random seeds for the main results would provide variance estimates.
- A standard CLIP backbone (non-FARE2) on CIFAR as a control would isolate the effect of the concept bottleneck from backbone robustness.

## Removed Points

- **Criticism about FARE2 backbone choice (Section 4.1):** The reviewer claimed using an adversarially robust CLIP variant "biases the backbone toward robustness, possibly making the CBM's lack of robustness less attributable to the concept bottleneck." This is removed because (a) the paper uses standard CLIP for Waterbirds and Metashift, not just FARE2, so there is a control; (b) using a robust backbone makes the CBM *failure more striking* (the bottleneck is the weak point even with a robust backbone), not less; and (c) the paper explicitly justifies the choice.
- **Criticism about low-level shift definition vs. CSA need (Section 2.2):** The reviewer noted confusion about why CSA is needed if low-level shifts don't change concept scores. This is addressed in the paper: Failure Mode 1 (non-robust concept bottleneck) is precisely the case where the concept mapping *does* change under low-level shifts, violating the idealized definition. The taxonomy and failure modes are clearly separated.
- **Criticism about component interference being a "structural weakness":** The paper directly acknowledges that CSA alone can beat the full method on low-level shifts and LPA alone on concept-level shifts, and explains this through the lens of Lee et al. (2023)'s framework about fine-tuning subsets of layers. The paper provides clear characterization of when each component is most useful. A gating mechanism would be a nice extension but its absence is not a structural flaw.
- **Criticism about theoretical grounding of CSA loss:** The claim that the loss is "a heuristic, not a proper divergence" — the paper explicitly says it is "motivated by" CAFA and describes it as a heuristic alignment loss, not claiming it as a proper statistical divergence. This is standard in the feature alignment literature.

## Novel Insights

Beyond the paper's own contributions, the most interesting insight from the review process is the tension between the paper's component-wise design and the empirical finding that components can interfere: CSA alone beats the full CONDA on low-level shifts. The paper's explanation (citing Lee et al. 2023 — different layers handle different shift types) is plausible but suggests an unresolved design question: should a CBM-TTA framework automate component selection, or is the current "apply all three" sufficient as a general strategy where performance is never catastrophically worse? The paper shows the full method is competitive overall, but this question is worth exploring in future work.

## Suggestions

1. **Add TENT as a baseline.** Apply entropy minimization to the CBM's linear predictor (and optionally to the full backbone+pipeline). This directly tests whether the specialized CSA/LPA/RCB design is needed or whether generic TTA already recovers most of the improvement.
2. **Report variance across at least 3 random seeds** for the main results (Table 1). Also report performance across different random batch orders.
3. **Include a brief pseudo-label quality analysis** showing test-set accuracy of the pseudo-labels per domain, and ideally a robustness analysis to label noise.
4. **Add a hyperparameter sensitivity study** for the key parameters (at minimum λ_frob, λ_sparse, λ_sim, λ_coh, and r).

## Score and Decision

The paper addresses a timely and well-motivated problem, provides a principled framework with clear design rationale, and demonstrates consistent improvements across diverse settings. The weaknesses are real but fall short of being structural or fatal — they are gaps in the evaluation (missing baselines, no variance estimates, unexamined pseudo-labels) rather than flaws in the method or its motivation. The paper's core contributions (the failure-mode taxonomy, the CONDA framework, and the empirical demonstration) are solid. With the suggested additions, the paper would be significantly stronger.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>