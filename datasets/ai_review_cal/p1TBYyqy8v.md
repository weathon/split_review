- Decision: Accept
- Avg Score: 6.60
- Scores: 8, 6, 8, 6, 5
Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper introduces "spreading OOD detection," a new benchmark task where OOD nodes propagate through a graph via epidemic models (SI/SIS), capturing the realistic phenomenon that anomalous samples spread through their connections. The authors construct the Spreading COVID-19 dataset to instantiate this scenario and propose EDBD (Energy Distribution-Based Detector), which uses energy scores as OOD indicators and controls aggregation at both the edge level (via an energy similarity matrix) and node level (via an energy consistency matrix) to prevent harmful mixing of ID and OOD energies. Experiments across seven datasets show consistent gains over existing graph-based OOD detectors in both the spreading and conventional label-leave-out settings.

## Strengths

1. **Well-motivated and formally defined new problem.** The paper identifies a genuine blind spot in node-level OOD detection — prior work evaluates on randomly selected OOD nodes that ignore propagation dynamics. The formulation using SI/SIS epidemic models as a Markov process (Eq. 1–2, Section 3.3) is mathematically precise and reproducible. The contrast between random assignment and realistic spreading is compelling.

2. **EDBD's two-component aggregation with clear ablation evidence.** The energy similarity matrix (Section 4.3) and energy consistency matrix (Section 4.4) are novel mechanisms with a clear design rationale: prevent ID→OOD and OOD→ID energy mixing. Table 4 shows that ablating either component degrades performance across six settings, directly proving both components contribute to the method's effectiveness.

3. **State-of-the-art results across both spreading and conventional evaluations.** EDBD achieves the best metrics on essentially all dataset–model combinations in Tables 1, 2, and 3. The improvement is consistent — not just on one dataset or one metric — and holds for both single-seed and multi-seed settings, demonstrating that the approach generalizes beyond any one configuration.

4. **Carefully constructed Spreading COVID-19 dataset.** The dataset uses 23 symptom-based features grounded in published medical sources (Appendix A), a graph structure from LastFM Asia with justification via comparison to a real human contact network (Figure 5), and epidemic parameters grounded in COVID-19 literature. This provides a realistic evaluation instantiation that partially compensates for the artificiality of the benchmark datasets.

## Weaknesses

### Fatal
None.

### Major

- **The Bernoulli(0.1) OOD features on Cora and LastFM create near-trivial feature-level separation, weakening the interpretation of the main benchmark results (Table 3).** The paper states (line 178) that OOD node features for these datasets are sampled from a Bernoulli(0.1) distribution — essentially uniform binary noise — while ID features are real citation-network bag-of-words (Cora) or social-media features (LastFM). This creates a near-perfect feature-level distinction, meaning any method that can exploit sharp distributional mismatch will succeed. The Energy baseline (i.i.d., no graph information) achieves >99% AUROC-T on Cora SI per Table 3, confirming the feature-level task is nearly solved. The paper uses the COVID-19 dataset (Table 2) to demonstrate realism, but that dataset is used for only one experimental block. The claim that the benchmark provides a "robust basis for comparing methods" (line 26) would be better supported with more challenging OOD feature distributions (e.g., near-OOD from similar domains, perturbations of ID features). As it stands, Table 3 primarily tests structural dynamics under easy feature conditions, and method rankings there may not transfer to harder feature regimes.

### Minor

- **No hyperparameter sensitivity analysis for the four method parameters.** EDBD has at least four free parameters (α, β, ε, K). The paper states hyperparameters are tuned on validation sets but provides no analysis of how performance varies with these choices, whether they are stable across datasets, or how they were selected. This leaves uncertainty about the method's robustness and practical tuning difficulty.

- **The time-averaged metrics (FPR95-T, AUROC-T, AUPR-T) weight early and late stages equally, obscuring practically important early-detection performance.** In epidemic monitoring or network intrusion, detecting the first few infected nodes (small OOD fraction) is critical. The current averaging over all t∈{1,…,T} means a method that only performs well after many nodes are infected (when the OOD fraction is high and the task is easier) could receive the same score as one that detects seeds early. Reporting per-step curves or early-stage aggregated metrics (e.g., for t ≤ 5) would substantially increase practical informativeness.

- **No analysis of failure modes when initial energies are poorly calibrated.** The energy similarity and consistency matrices are constructed from the initial MLP energies (E⁰). If these initial energies are not discriminative (e.g., due to poor training, limited ID data, or label noise), the aggregation could amplify errors rather than correct them. The paper does not examine this boundary case or provide synthetic experiments where initial energies are deliberately corrupted.

- **No runtime or computational cost comparison.** The matrix operations involve constructing similarity and consistency matrices per graph snapshot, which scales with O(N·d̄). For LastFM (7,624 nodes), this could be non-negligible, but the paper provides no runtime comparison to baselines.

- **The similarity function design (Eq. 5) is presented without justification.** The function sin(Eᵢ, Eⱼ) = (ε·(max−min) + (1−ε)·|Eᵢ−Eⱼ|)⁻¹ is reasonable but ad-hoc. Why this particular form rather than an RBF, a cosine-based similarity, or a learnable function? A brief rationale or a comparison with alternative forms would strengthen the presentation.

### Trivial

- **Table 4's baseline label is unclear.** The text states "The first rows of the tables in Table 4, where both S and C [are excluded], correspond to the performance of GNNSAFE." This is ambiguous on first reading — clarifying that the row with neither S nor C equals uniform aggregation (GNNSAFE) would improve readability.

## Nice-to-Haves

- Releasing the full simulation pipeline code (episode generation, baseline runners) alongside the dataset would aid reproducibility.
- A brief analysis of the energy consistency matrix at cluster boundaries (e.g., what happens when a node has exactly one neighbor of each type and variance is moderate rather than high).

## Removed Points

These points are flagged to be removed; treat them with caution.

- *"GNNSAFE results are dramatically worse than plain Energy (Table 3) — could there be an implementation issue?"* — **Removed: speculative.** The paper explicitly explains this as "aggregating without consideration of energy distribution results in a performance drop" (line 204), which is the thesis of the paper. There is no evidence of an implementation error. The degradation is expected under the paper's own reasoning.
- *"Code and data release — authors should release the full simulation code."* — **Moved to Nice-to-Have.** The paper already provides the Spreading COVID-19 dataset in supplementary material. Requesting additional code is reasonable but not a weakness of the paper as submitted.
- *"The similarity function is ad-hoc and not well justified; why not use RBF, cosine, or a learned function?"* — **Demoted to Minor** (merged with the minor point above). The criticism is valid but the function is clearly stated and works; the issue is lack of rationale, not that the function is wrong.

## Novel Insights

The harsh critic's framing that EDBD's primary benefit may be "not breaking a good baseline" rather than fundamentally improving detection is an insightful lens. The ablation (Table 4) shows that raw Energy on Cora label-leave-out already achieves ~95% AUROC, and the main gain from EDBD's aggregation (to ~96.4%) is modest in absolute terms. This suggests EDBD's value proposition is more about robustness to structural mixing than about large absolute gains in easy settings. The spreading OOD benchmark reveals this clearly: GNNSAFE craters under spreading because its uniform aggregation mixes ID/OOD scores, while EDBD preserves the strong baseline. This interpretation clarifies that EDBD's real contribution is *preventing degradation* under structural pressure, which is valuable but different from a claim of fundamental detection improvement.

None beyond the paper's own contributions.

## Suggestions

1. Replace the Bernoulli(0.1) OOD features with more challenging synthetic alternatives (e.g., held-out classes from the same dataset, structured perturbations of ID features, or near-OOD from semantically similar domains) and report whether EDBD's advantage holds under harder feature conditions.
2. Add a hyperparameter sensitivity study (plots of performance vs. α, β, ε, K) to demonstrate robustness.
3. Report per-step metrics or early-stage aggregated metrics (t ≤ 5 or the first quartile of the episode) to complement the time-averaged numbers.
4. Include a synthetic experiment where initial energies are deliberately corrupted (e.g., by reducing training epochs or adding label noise) to test whether EDBD still helps or amplifies errors.
