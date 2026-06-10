## Summary

This paper introduces Normalized Space Alignment (NSA), a differentiable representation-space discrepancy metric with O(N²D) complexity. NSA normalizes pairwise distances by the maximum distance from the origin and averages the absolute differences between two point clouds. The authors validate NSA as a loss function for autoencoders (NSA-AE), as a tool for analyzing GNN representations across training and initializations, and for uncovering structural vulnerabilities under adversarial attacks. The core value proposition is a metric that is simultaneously differentiable (unlike CKA) and computationally cheaper than RTD (avoiding cubic-complexity barcode computations).

## Strengths

- **Differentiable metric with quadratic complexity fills a concrete gap.** The paper correctly identifies that CKA is efficient but not differentiable (and not a pseudometric), while RTD is differentiable but incurs cubic complexity from barcode computations. NSA achieves O(N²D) with differentiability, enabling its use as a loss function. The running-time advantage over RTD-AE is reported (Table 3, line 76), and the practical impact is demonstrated by NSA-AE supporting larger batch sizes.

- **Link prediction results provide clean, independent evidence of structure preservation.** Table 2 shows that NSA-AE latent embeddings achieve higher ROC-AUC scores than both a vanilla autoencoder and RTD-AE across all datasets and all latent dimensions. Because ROC-AUC is a task-specific metric unrelated to NSA, this is the strongest non-circular evidence that NSA minimization preserves semantically meaningful structure.

- **Adversarial vulnerability analysis is genuinely insightful.** Section 6 demonstrates that NSA detects anomalously high structural discrepancy in SVD-GCN under evasion attacks that misclassification rate alone does not surface—tracing this to a surge in boundary nodes and confidence decline. This diagnostic capability goes beyond what standard accuracy analysis provides and connects to known catastrophic failures under adaptive attacks (Mujkanovic et al., 2022).

- **Quantile-based normalization addresses a practical robustness concern.** Section 3.5 proposes normalizing by a quantile (e.g., 0.98) instead of the max distance from origin, mitigating outlier sensitivity. This is a concrete, principled modification that shows attention to deployment concerns not addressed by CKA or RTD.

## Weaknesses

### Major

- **Strong, unsupported claims are made without evidence.** The paper states NSA is "currently the only metric that manages to" combine computational efficiency with reflecting global structural discrepancies in mini-batching (line 18). No proof or systematic comparison against a broad set of alternatives (distance correlation, Procrustes analysis, non-parametric CCA variants, etc.) is provided to substantiate uniqueness. Furthermore, the contribution list asserts "the calculation of NSA over a subset of the data is shown to be representative of the global NSA value" (line 20), but no experiment or theoretical argument supporting mini-batch representativeness appears in the visible paper body. These claims are central to the paper's positioning and should either be demonstrated or tempered.

- **Sanity test comparison between NSA and RTD uses substantially different sample sizes.** Line 142 states NSA is computed on 4000–9000 data points while RTD uses the recommended 400 points. The claim that "NSA shows a stronger layer-wise correlation" (Figure 2 caption) is therefore confounded by a 10–20× sample-size advantage. Without controlling for this variable, the comparison does not distinguish between genuine metric superiority and more stable estimation from larger samples.

- **Datasets used in key experiments are not named in the main text.** The autoencoder experiments (line 97: "four real world datasets") and link prediction experiments (line 111: "four distinct graph datasets") do not identify the datasets. Only the Amazon Computers dataset is named in Section 5. For a methods paper whose empirical claims hinge on these results, this is a significant reproducibility gap. Table captions and figure labels also omit dataset names.

### Minor

- **NSA is not translation-invariant, and this limitation is unacknowledged.** The normalization factor is max distance from the coordinate origin (Eq. 1). If point clouds are translated (e.g., through bias parameters in neural network layers), the normalization factor changes, altering NSA even when pairwise geometry within each cloud is preserved. By contrast, linear CKA achieves translation invariance through mean-centering. The paper lists invariance properties (isotropic scaling, orthogonal transformation) in Section 3.3 but does not discuss this limitation. This does not invalidate the metric—the origin may be meaningful in some settings—but it should be acknowledged.

- **NSA is used as both training objective and evaluation metric for NSA-AE in Table 1.** While the paper acknowledges that RTD-AE wins on RTD (since RTD-AE minimizes RTD), the same logic applies to NSA-AE on NSA. The more informative metrics are the ones not minimized by any method (linear correlation of pairwise distances, triplet ranking accuracy), where NSA-AE does indeed perform well. The issue inflates the perceived strength of the evidence rather than undermining it, but the framing should be cleaned up.

- **Quantile normalization's impact on theoretical properties is not discussed.** The quantile-based variant (Section 3.5) is presented as an empirical improvement, but the paper does not address whether the pseudometric axioms, scale invariance, or similarity-metric conditions still hold under this modification.

- **Convergence analysis (Section 5.2) reports NSA's behavior in isolation without comparative baselines.** The finding that NSA convergence correlates with test accuracy convergence is plausible, but CKA and RTD have been shown to exhibit similar trends in prior work. Without comparing against these alternatives on the same task, it is unclear whether NSA provides information that existing metrics do not.

### Trivial

- None beyond those already listed as Minor.

## Nice-to-Haves

- Add a quantitative correlation metric (e.g., Spearman correlation) between NSA and misclassification rate across perturbation levels in the adversarial analysis (Section 6), strengthening the currently qualitative conclusions.
- Evaluate NSA on the same 400-point sample used for RTD in the sanity test to determine whether its advantage persists under equal sample sizes.
- Provide a simple experiment showing that NSA computed on random subsets converges to the full-dataset value as batch size increases, supporting the mini-batch representativeness claim.
- Report variance or error bars on Tables 1 and 2.

## Removed Points

These points were identified in the source reviews but are removed from the final assessment for the following reasons:

- *Missing proofs in Section 3.2 (NSA as a Pseudometric):* The section heading is present with no visible content, but this is likely a parser artifact that stripped the actual content. Per policy, weaknesses about content that may have been stripped by the parser are removed.
- *Concerns about NSA being insufficiently novel or not comparing against enough prior metrics:* The harsh critic's suggestion that the paper should compare against Mantel test, Procrustes analysis, or distance correlation is a scope-expansion request. The paper defines itself against CKA and RTD, the two most directly relevant metrics in the representation-learning space, which is a defensible scope choice.
- *Generic criticisms about lack of confidence intervals or theoretical proofs:* These are demands for practices not standard across all settings in this field. The paper operates within its community's norms.

## Novel Insights

The most interesting observation to emerge from the review process is that the paper's strongest evidence lives in an unexpected place. The autoencoder results (Table 1) appear to be the main exhibit, but they are muddied by the circularity of NSA being both objective and evaluation metric. The link prediction results (Table 2), framed as a "downstream task analysis," actually provide cleaner evidence because ROC-AUC is independent of NSA. And the adversarial analysis (Section 6)—the furthest from the paper's core framing of NSA as a representation-similarity metric—is where the most novel contribution lies: using per-point NSA to diagnose structural vulnerabilities that accuracy metrics miss. If the authors reframe their contribution around NSA's diagnostic capabilities rather than its competitive performance as an autoencoder loss, the paper would make a sharper, more defensible case.

## Suggestions

1. **Temper the "only metric" and mini-batch representativeness claims** unless accompanied by rigorous proof or systematic experimentation. These overstatements will undermine reviewer trust.
2. **Name all datasets in the main text** and add dataset statistics/descriptions.
3. **Clean up Table 1** by either dropping NSA from the evaluation metrics or clearly separating training-objective metrics from independent evaluation metrics.
4. **Acknowledge the translation-dependence of the normalization** and either justify it (the origin is meaningful given bias initialization) or propose a centered variant.
5. **Re-run the sanity test comparison** using equal sample sizes for NSA and RTD to isolate the metric-level advantage from the sample-size confound.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>