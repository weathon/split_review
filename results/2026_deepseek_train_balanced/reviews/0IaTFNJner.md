Below is my consolidated review after cross-checking all claims against the paper text.

---

## Summary

This paper identifies and analyzes the "embedding collapse" phenomenon — embedding matrices in recommendation models occupying a low-dimensional subspace — as the root cause of poor scalability when increasing embedding size. Through empirical and theoretical analysis, the authors demonstrate a two-sided effect: feature interaction causes collapse (limiting scalability) but simultaneously prevents overfitting (making naive solutions fail). Based on this diagnosis, they propose "multi-embedding," which scales the number of independent embedding sets (each with its own interaction module) rather than embedding dimension. Experiments across six architectures and two datasets show consistent scalability improvements, with deployment at Tencent providing real-world validation.

## Strengths

1. **Well-defined and quantified diagnostic metric.** The Information Abundance (IA) metric (Def. 1, Eq. 79: $\|\boldsymbol{\sigma}\|_1/\|\boldsymbol{\sigma}\|_\infty$) cleanly captures embedding collapse without the saturation problem of matrix rank. Figure 2 concretely shows learned embeddings have IA far below randomly initialized counterparts.

2. **Gradient-decomposition analysis provides mechanistic understanding of collapse.** Equations (145–153) derive that for FM-style interaction, the gradient for an embedding decomposes into field-specific terms weighted by the singular values of interacting matrices — when those matrices have low IA, gradients become imbalanced and all rows degenerate similarly. The toy experiment (Figure 3) validates this causal link.

3. **Two-sided effect is a genuinely insightful finding.** Evidence III (orthogonality regularization on DCNv2, Figure 5) and Evidence IV (DNN without explicit interaction, Figure 6) together show that suppressing collapse without addressing interaction causes overfitting — higher IA is insufficient for scalability and can even hurt. This reframes the problem beyond a simple "collapse is bad" narrative.

4. **Consistent and well-documented empirical evidence across diverse architectures.** Table 1 shows that across 6 models × 2 datasets = 12 configurations, multi-embedding achieves its best AUC at the largest (10×) scale in every single case, while single-embedding plateaus or degrades in most. The pattern is remarkably consistent.

5. **Mechanistic ablation traces causality from design to outcome.** Figures 7a–d show that (a) multi-embedding produces lower principal-angle similarity between embedding sets, (b) separate interaction modules learn distinct patterns, and (c) shared-interaction and diversity-regularized variants degrade both diversity and scalability — confirming the causal chain from separated interaction modules → diversity → collapse mitigation.

6. **Real-world deployment at scale.** Online A/B testing at Tencent's WeChat Moments platform yielded a 3.9% GMV lift (hundreds of millions of dollars/year), validating the approach beyond offline benchmarks.

## Weaknesses

### Fatal

None.

### Major

1. **Parameter-count fairness between SE and ME is not established.** The paper states (line 260) that it "add[s] a non-linear projection after interaction for the models with linear interaction modules and reduce[s] one MLP layer for postprocessing module $F$ to achieve a fair comparison," but **no total parameter counts are ever reported**. Multi-embedding at scaling factor $M$ adds $M-1$ complete interaction modules; for models like DCNv2 (cross network with $O(N^2)$ transformation matrices per layer) the parameter difference can be substantial. Without knowing whether SE at 10× (embedding dimension $10K$) and ME at 10× ($M=10$ sets of dimension $K$) have comparable total parameters, the reader cannot determine how much of the observed improvement comes from the architectural innovation versus brute-force parameter increase. The shared-interaction ablation (Figure 7c,d) partially mitigates this — it controls for interaction parameters and still shows worse results than ME — but this does not fully resolve the SE-vs-ME comparison in Table 1. A simple table reporting "#Params (SE) | #Params (ME)" alongside each AUC would settle this.

2. **No statistical significance reported for main results.** The paper reports averaging 3 runs (line 292) but provides no standard deviations, confidence intervals, or variance estimates for the AUC values in Table 1. Given that the claimed average improvement is 0.00110 AUC — a small absolute value even if practically meaningful per the cited prior work — the absence of variance information makes it impossible to assess the reliability of individual comparisons. The footnote citing prior work that treats 0.001 AUC as significant does not substitute for reporting uncertainty.

### Minor

3. **Theoretical analysis is substantially narrower than the claims built on it.** The gradient decomposition (Eqs. 145–153) is derived only for FM-style pairwise interaction ($h = \sum_i\sum_j \mathbf{v}_i^\top\mathbf{v}_j$). The paper's central Finding 1 ("feature interaction is the primary catalyst for collapse") is presented as a general theory for all recommendation models, but the formal derivation does not cover cross networks, CIN, Hadamard products, or MLP-based interactions used in DCNv2, xDeepFM, IPNN, and FinalMLP — most of the models evaluated later. The paper acknowledges this gap indirectly through empirical Evidence I (sub-embedding analysis on DCNv2) and the toy experiment, but the gap between the narrow theoretical apparatus and the broad claimed mechanism is not clearly delineated. This does not invalidate the empirical observations, which stand on their own, but it overstates the theoretical grounding.

4. **Computational cost of multi-embedding is unquantified.** The paper claims ME works "without introducing significant computational resources" (line 329) but provides no FLOPs, training-time, or throughput measurements. ME with $M=10$ adds 9 additional interaction modules — this is not obviously cost-free, especially for expensive interaction mechanisms like DCNv2's cross network or xDeepFM's CIN. Practitioners evaluating the trade-off have no data to assess this.

5. **Base embedding size $K$ for the main experiments is never explicitly stated.** The introduction mentions "size of 10" as typical (line 14), and Table 2 (data-amount analysis) shows embedding sizes 5–40, hinting that $K=10$ is the base. But the experimental setup paragraph (lines 264–265) does not confirm this value, leaving readers to infer it indirectly.

6. **Data-amount analysis (Section 5.4) is thin and the interpretation feels post-hoc.** Table 2 provides raw IA values under varying data fractions but without confidence intervals or a clear criterion for distinguishing "data-limited" from "interaction-limited" regimes. The interpretation ("only for experiments with 10%–100% data and embedding size 5... can we observe the collapse is caused by limited data") is asserted without statistical backing. This section does not materially strengthen the paper's core argument.

### Trivial

None.

## Nice-to-Haves

- Report total parameter counts for each SE and ME configuration in Table 1 to resolve the fairness question.
- Add standard deviations or confidence intervals for the AUC results (3 runs per cell).
- Provide runtime or FLOPs comparison for at least one model (e.g., DCNv2) to substantiate the "no significant computational overhead" claim.
- Plot IA vs. data fraction with error bars in Section 5.4 for a more systematic analysis.

## Removed Points

- **Missing "base" comparison for ME (Harsh Critic Point 3):** ME at 1× is architecturally identical to SE at base (one embedding set, one interaction module). Requesting this column is requesting redundant information; the absence is natural.
- **IA metric limitations (Harsh Critic Point 4):** The critic claims the paper does not discuss that higher IA can indicate noise. However, the entire Section 4.2 (two-sided effect) is built around Evidence III and IV, which explicitly demonstrate this tension — higher IA from suppressed interaction leads to overfitting. The paper's narrative already acknowledges this ambiguity.
- **Several formatting/style nitpicks from the Harsh Critic's section notes** (e.g., "the framing against foundation models is somewhat overdone") — these are subjective opinions without factual grounding.

## Novel Insights

The most interesting observation from the combined reviews is the structural asymmetry between the paper's diagnostic and proposed-solution contributions. The embedding collapse diagnosis and the two-sided effect are well-supported by multiple convergent forms of evidence (spectral analysis, sub-embedding visualization, gradient decomposition, controlled ablations). The multi-embedding solution, while empirically effective, rests on a less secure empirical foundation because the SE-vs-ME parameter fairness question has not been closed — the ablation studies address *mechanism* (separated interaction matters) but not *fairness* (do SE and ME have comparable total capacity?). This asymmetry is worth noting because it means the diagnostic contribution is the stronger, more defensible part of the paper, while the solution's evaluation needs tightening.

## Suggestions

1. **Add a parameter-count table** comparing SE and ME at each scaling factor for each architecture. This is the single highest-leverage improvement and directly addresses the most significant concern.
2. **Report standard deviations** for the 3-run averaged AUC results in Table 1.
3. **Clearly state the base embedding size $K$** used across all experiments in the setup paragraph.
4. **Delineate the scope of the theoretical analysis** more carefully — explicitly note that Eqs. 145–153 apply to FM-style interaction and that the empirical evidence (Evidence I) extends the analysis to more complex models.
5. **Add a brief runtime comparison** for at least one model to substantiate the computational cost claim, or remove the claim.

## Score and Decision

This paper identifies a real, practically important problem, provides a well-structured diagnosis with convergent evidence, and proposes a simple, empirically effective solution with real-world deployment validation. The main weaknesses — unquantified parameter fairness, missing statistical significance, and theoretical scope gap — are addressable and do not undermine the core contributions. The diagnostic finding (embedding collapse + two-sided effect) is independently valuable and well-supported.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>