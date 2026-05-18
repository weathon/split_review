Now I have a thorough understanding of the paper and all the reviewer claims. Let me produce the consolidated review.

---

## Summary

This paper proposes a two-step test-time adaptation (TTA) method for graph neural networks that operates on batch normalization layers. In the first step (BNSA), BN statistics (mean/variance) are adapted via data-driven weighting derived from Jensen-Shannon divergence between training and test activation distributions, with a learnable mask matrix (trained via Gumbel-Max trick and contrastive loss) that selectively adjusts which dimensions are adapted. In the second step (BNPA), BN parameters (scale/shift) are fine-tuned using a joint energy-based model with entropy-based and confidence-based pseudo-label filtering. Experiments across 7 datasets and 3 GNN backbones show consistent improvements over 7 baselines.

## Strengths

1. **Principled two-step design that decouples statistic adaptation from parameter adaptation, supported by ablation evidence.** The paper separates BN statistic adaptation (BNSA) from BN parameter adaptation (BNPA), and the ablation study (Table 2, described in text) shows that using either component alone degrades performance compared to the full method. This design explicitly addresses the model collapse problem that entropy-minimization-only methods suffer during prolonged adaptation (as cited from Press et al. 2024).

2. **Data-driven weighting (JS divergence) and learnable mask for dimension-wise statistic interpolation.** Instead of tuning α via grid search (common in prior BN-statistic methods like a-BN, DUA), the paper computes α from the Jensen-Shannon divergence between non-parametric density estimates of training and test activations (Eq. 3–4), and introduces a learnable mask M via the Gumbel-Max trick (Eq. 5–6) for selective adjustment per BN dimension. Ablations in the text confirm that removing either the learned α or the mask matrix M decreases performance.

3. **Consistent strong results across a broad evaluation.** The method achieves the best or second-best accuracy on 20 out of 21 dataset-backbone combinations in Table 1, with notable gains on Cora (GCN: +2.84%), Elliptic (GraphSAGE: +2.60%), and Elliptic (GAT: +1.60%) over the next-best competitor. The evaluation covers both synthetic and natural distribution shifts, 7 diverse datasets, and 3 GNN architectures.

4. **Regularization strategy that preserves training knowledge without requiring training data access.** The BNSA loss combines InfoNCE contrastive loss with KL divergence between original and adapted model predictions (Eq. 7–8), preventing drastic forgetting. The method stores only a small histogram from the final training epoch, qualifying as a practical TTA approach.

## Weaknesses

### Fatal
None.

### Major

1. **Unaddressed computational cost of the JS-divergence-based weight α.** Equation 4 computes α as the average Jensen-Shannon divergence over all pairs of training and test instances: O(|D_tr| × |D_te|) per BN dimension. For large graphs like OGB-Products (~2.4M nodes), this pairwise computation is prohibitive. The paper acknowledges storing "only the information from the last few training epochs" and using "non-parametric density estimation," but neither addresses the quadratic pairwise cost. No wall-clock time or memory analysis is provided. The paper asserts that α is computed once before adaptation, but even a single O(|D_tr|×|D_te|) pass at the scale of OGB datasets is a serious practical concern that must be addressed.

### Minor

2. **Ambiguity in when the mask M / Bernoulli matrix B is learned.** The description in Section 3.1 (lines 117–118) uses the phrase "In the training process" to describe the optimization of B, which is ambiguous — it could mean during the original model training or during the TTA optimization loop. The surrounding context ("statistics of BN layers are not updated during the training process") and the use of contrastive learning "for training at test-time adaptation" (line 125) suggest B is optimized during TTA, but the language is not precise enough. Given that this is a core component of the method, the paper should clearly state whether B is learned offline (during original training) or online during TTA, and if online, how the contrastive learning is sufficiently sample-efficient on test batches.

3. **Marginal accuracy contribution of BNPA relative to its complexity.** The paper's own ablation description (lines 253–256) characterizes the gains from BNPA components as "minor but consistent." Meanwhile, BNPA introduces multiple hyperparameters (τ_e, τ_c¹, τ_c²), the SGLD sampling loop, and the EBM formulation — substantially increasing method complexity. The paper claims improved calibration from BNPA but the extracted text does not contain quantitative calibration metrics (ECE or reliability diagrams), though section 4.4 may have been present in the original submission but stripped by the parser. The paper's own admission of marginal accuracy gains from this component, combined with its complexity, weakens the argument for including the full BNPA pipeline.

4. **The non-parametric density estimation implementation is underspecified.** The paper mentions using "non-parametric density estimation" to estimate activation distributions P_m and P_n, and refers to a "small histogram matrix" (line 29), but does not specify the number of bins, bin width selection strategy, or how densities are estimated from activations. This makes the computation of the JS divergence (which requires density functions, not samples) difficult to reproduce.

5. **The JS-divergence weight α is computed once and kept fixed during adaptation.** The paper computes α from the initial activation distributions of the pre-adapted model and does not update it as the model's activations change during adaptation. Since the BN statistics shift over the course of adaptation, a static α may become suboptimal. An adaptive update would better align with the "test-time" nature of the method.

6. **No guidance for setting the per-class pseudo-label thresholds τ_c¹ and τ_c².** These thresholds control the confidence-based filtering in BNPA (Eq. 15–16) and are defined per class. The paper does not provide any heuristic, ablation, or sensitivity analysis to guide their setting, making it difficult for practitioners to apply the method to new datasets.

### Trivial
None.

## Nice-to-Haves

- **Analysis of how the decay steps k affects accuracy.** The paper shows a plot of mean/variance difference over k but does not study how k affects classification accuracy. A sensitivity study would help justify the claim that "small k suffices."
- **Extension to graph-level tasks.** The paper is scoped to node classification; applying the method to graph classification would broaden the contribution but is not required.
- **The KL regularization in BNSA (Eq. 8) and the pseudo-label approach in BNPA both serve to prevent forgetting of training knowledge.** The paper could clarify the distinct role each plays and why both are needed.

## Removed Points

- **"Many of these (e.g., MEMO, GTRANS) are not GNN-focused TTA methods."** Removed — GTRANS is listed under "Input augmentation" and is a graph-specific method. Using general TTA methods (TENT, SAR, MEMO) as baselines is standard practice in the TTA literature. This criticism is factually incorrect.
- **"Evaluated only on node classification."** Moved to Nice-to-Haves. The paper explicitly states it evaluates on node classification, which is a standard task for GNN evaluation.
- **"No calibration metrics provided."** The extracted text references section 4.4 which appears to discuss calibration but is missing from the parser output. Calibration metrics may have been present in the original submission.
- **"Incomplete comparison" / missing more baselines.** The paper compares against 7 baselines across 3 categories; this is a reasonable baseline zoo for a TTA paper. The demand for additional graph-specific baselines ignores that GTRANS is already included.
- **Strength Finder claims about specific numerical ablation values (e.g., "Cora: 56.53 → 55.04").** These cannot be verified against text since Table 2 is embedded as an image; they are kept as directional but not cited as verified facts.

## Novel Insights

The key tension surfaced across the reviews is between the paper's design ambition and its practical justification. The two-step approach (statistic adaptation → parameter adaptation) is well-motivated by the BN mechanics, but the paper piles on heavy machinery (JS-divergence pairwise computation, Gumbel-Max-learned masks, SGLD-based EBM sampling, dual pseudo-label filtering thresholds) without adequate computational analysis or ablation evidence that each added component earns its keep. The core insight — that adapting BN statistics via distributional divergence is more principled than grid-searched α — is a genuinely useful contribution. But it is buried under a complex pipeline where the later stages (BNPA with its EBM) add disproportionate complexity for apparently marginal returns. A lesson for similar work: a simpler method with thorough justification often beats a complicated one where each new component must be individually justified.

## Suggestions

1. **Address the computational cost of Eq. 4 explicitly.** Report wall-clock time for α computation on the largest datasets and propose an approximation (e.g., mini-batch subsampling, or computing JS divergence only on a random sample of pairs) to make the method practical.
2. **Clarify the training procedure for the mask M.** State unambiguously whether the Bernoulli variable matrix B is learned during the original training phase, during TTA, or both. If learned during TTA, discuss how the contrastive loss receives enough data from test batches.
3. **Provide calibration metrics (ECE or reliability diagrams)** for the full method vs. BNSA-only vs. BNPA-only variants, to substantiate the claim that the EBM improves calibration.
4. **Reduce hyperparameter burden or show robustness.** Conduct a sensitivity study for at least τ_e (entropy threshold) and λ (KL weight) across datasets, or tie τ_c¹/τ_c² to global quantiles rather than class-specific values.
5. **Specify the histogram binning strategy** used for non-parametric density estimation, including number of bins and how the boundaries are determined.

## Score and Decision

The paper makes a genuine contribution to GNN test-time adaptation with a well-motivated two-step BN adaptation framework, extensive empirical evaluation, and consistent improvements over existing methods. The weaknesses are substantive but not fatal — they concern missing implementation details, unaddressed computational costs, and a complex second component (BNPA) whose marginal benefits need stronger justification. These issues are addressable in a major revision.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>