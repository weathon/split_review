Now I have all the information I need. Let me construct the final review.

## Summary

The paper proposes HOMIL (Higher-Order Multi-Instance Learning), a framework for whole-slide image classification that augments standard attention-based MIL (first-order moment) with a second-order moment (covariance matrix of cluster features). DBSCAN clustering is used to group locally similar patches, improving computational efficiency. Experiments on CAMELYON16 and TCGA-NSCLC show consistent improvements over nine baselines, along with substantial runtime reductions.

## Strengths

- **Novel application of second-order statistics in MIL for WSIs.** The paper makes a conceptually clean connection between MIL aggregation and statistical moments, and extending to the covariance matrix is well-motivated by the observation that first-order (mean) aggregation discards feature variability and correlation structure. This framing is a genuine addition to the WSI-MIL toolbox.

- **Substantial and well-documented computational efficiency gains.** The DBSCAN clustering reduces per-slide patches to ~16–18% of the original count, resulting in a 5-fold runtime of 310s on CAMELYON16 — faster than ABMIL (455s), CLAM (640–1115s), and orders of magnitude faster than Transformer/SSM-based methods (TransMIL 5175s, MambaMIL 7200s). On TCGA-NSCLC the same pattern holds (3685s vs. 32400s+). This is a practically meaningful engineering contribution.

- **Unified and fair baseline comparison.** All nine baselines are implemented in a shared codebase with identical input specifications and patient-level 5-fold CV, reducing implementation-driven variance. The baseline performances are competitive with or above typical literature values, suggesting the comparisons are not artificially favorable.

## Weaknesses

### Major

- **Performance gains are modest, particularly on the more challenging dataset, and no statistical significance is reported.** On TCGA-NSCLC, HOMIL's ACC is 93.24±2.47 vs. HMIL's 92.89±1.45 — a 0.35% difference far smaller than either standard error. The AUC improvement over the strongest competitor (MambaMIL's 96.68 vs. HOMIL's 97.41) is more notable but still without confidence measures. On CAMELYON16 the gains over ABMIL are larger (ACC: +2.26%, F1: +2.94%), but here too the reported standard errors overlap substantially. The paper claims "significantly improves the state-of-the-art" without any statistical test (paired t-test, signed-rank, or bootstrapped intervals). Given that 5-fold CV produces paired observations, a per-fold paired test would be straightforward to compute and would meaningfully strengthen the evidence. Without it, the reader cannot distinguish signal from noise.

- **Ablation study does not conclusively attribute gains to the proposed components.** In Table 3, the differences between the full model and its ablated variants (w/o CM: −1.26% ACC; w/o SOM: −1.00% ACC) are all within overlapping standard errors (e.g., full model 96.98±2.43 vs. w/o SOM 95.98±2.68). The removal of SOM on AUC actually increases the gap from ABMIL's baseline (98.88) rather than shrinking it. While a consistent degradation trend is visible across three metrics, the lack of error-bar separation or paired testing weakens the claim that each component is essential. This is especially problematic because the fusion weight analysis (Figure 2b) shows the model increasingly relies on first-order information over training, raising the question of how much the second-order stream actually contributes after convergence.

### Minor

- **"Attention-weighted covariance" terminology is imprecise.** The paper describes the covariance matrix as "attention-weighted" (Section 4.3.3), but the formula C = Σ \~g_k \~g_k^T contains no attention weights — only the centering uses the attention-weighted mean v^(1) = Σ a_k g_k. A properly weighted covariance would be Σ a_k (g_k − v^(1))(g_k − v^(1))^T. The centering is indeed attention-informed, but calling the matrix itself "weighted" overstates what the equation implements. This is a terminology issue, not a methodological flaw, but it should be corrected.

- **No qualitative or quantitative validation of the claimed adaptive clustering behavior.** The paper asserts that DBSCAN forms "small clusters for rare pathological regions and large clusters for abundant normal tissues" (Section 4.2), which is a central motivation for using DBSCAN. Yet no visualization of cluster assignments on actual WSIs, no cluster-size distribution analysis, and no comparison of cluster granularity across diagnostic classes is provided. The clustering's adaptive behavior is assumed but not demonstrated.

- **Covariance vectorization via Conv1D+max-pooling lacks ablation or motivation.** The paper compresses the d×d covariance matrix to a d-dimensional vector using 1D convolution with four kernels followed by hierarchical max-pooling. This specific design is not compared with simpler alternatives (flatten+linear, eigenvalue extraction, or bilinear pooling), making it unclear whether the vectorization itself contributes to performance or is merely a dimensionality reduction step.

- **Fusion weight analysis raises an unanswered question.** Figure 2b shows the first-order fusion weight α^(1) stabilizing at ~0.6 and the second-order weight α^(2) at ~0.4. The paper interprets this as the model "retaining" second-order information, but it also shows the second-order contribution diminishing during training. Combined with the overlapping ablation error bars, this pattern makes the marginal value of the second-order stream ambiguous rather than complementary.

### Trivial

- None that are not parser artifacts.

## Nice-to-Haves

- Reporting paired statistical tests (per-fold) for the main comparisons and ablations would substantially strengthen the empirical claims.
- A qualitative figure showing DBSCAN cluster assignments overlaid on a WSI, with cluster sizes labeled, would validate the adaptive granularity claim.
- An ablation comparing the Conv1D vectorization against a simple flatten+linear baseline would clarify whether the vectorization design matters.
- Adding a baseline that directly computes a flattened patch-level covariance (without clustering) and concatenates it with ABMIL features would cleanly isolate the contribution of the clustering vs. the covariance.

## Removed Points

These points were raised by reviewers but removed or demoted for the following reasons:

- **"The covariance formula inconsistency is a fatal structural flaw"** (Harsh Critic) — Demoted to Minor. The centering uses the attention-weighted mean v^(1), so the covariance is attention-informed even if the outer product sum lacks explicit a_k weights. Calling it "attention-weighted" is imprecise but not structurally invalid; the method as implemented is clear from the equations.
- **"The paper does not discuss prior second-order work like bilinear CNNs"** — Removed. The paper is focused on MIL for WSIs, not general covariance pooling in vision. The relevant prior work on MIL is adequately covered. Criticizing the omission of a tangentially related sub-field is scope creep.
- **"Baseline hyperparameter tuning may bias comparisons"** — Weakened from concern to non-issue. The unified codebase and competitive baseline numbers (ABMIL at 94.72% ACC on CAMELYON16 is at or above typical literature values) suggest the baselines are reasonably tuned.
- **"The claim of SOTA improvement is not supported"** — Retained but reframed: the evidence is suggestive but not conclusive due to missing significance tests. The claim itself is standard and the data directionally supports it; the weakness is in the strength of the evidence, not the claim's validity.
- **Strength Finder's claim that "ablation study isolates contribution of second-order moments"** — Weakened. The ablation shows consistent degradation but the differences are within overlapping standard errors, making the isolation less clean than claimed.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

- Add a statistical significance test (paired across the 5 folds) comparing HOMIL against ABMIL and the next-best baseline for each metric. Report p-values or denote which comparisons pass standard thresholds.
- Clarify the covariance terminology: either rename it "covariance centered by the attention-weighted mean" or introduce explicit weights a_k in the outer product sum to genuinely implement a weighted covariance.
- Include a visual or quantitative analysis of DBSCAN cluster sizes (e.g., histogram of cluster sizes, or a side-by-side WSI patch with cluster labels color-coded) to validate the adaptive granularity claim.
- Add a simple ablation comparing the Conv1D vectorization against flatten+linear to confirm the vectorization design is not arbitrary.

## Score and Decision

**Round 1 bracket (initial):** Between 4.0 and 6.0. The paper is substantially stronger than the weak-anchor papers at 2.5–3.25 (Mamba-HMIL, Pg-GAT) which had serious novelty/writing issues, but clearly below the 8.0 anchors which represent top-tier contributions.

**Round 2 narrowing:** Compared against three anchors in the 4.5–6.0 range:
- SMIL (4.50, rejected): HOMIL has clearer motivation and a more concrete contribution, placing it above 4.50.
- MI-PLL (5.00, rejected): HOMIL's presentation is cleaner, though MI-PLL had substantial theory. Comparable quality but different genres.
- MFC (6.00, accepted): HOMIL is less ambitious and has weaker experimental validation (no significance tests, smaller gains), placing it below 6.00.

The paper provides a well-motivated and clearly described method with a novel (in the WSI-MIL context) idea, fair baselines, and genuine efficiency gains. However, the experimental evidence for the core claim — that second-order moments improve accuracy — is weakened by modest effect sizes, overlapping error bars, and the absence of statistical significance testing. The ablation does not cleanly attribute gains to the proposed components.

**Final score: 5.0**

**Decision: Reject** — The core idea has merit and the paper is clearly written, but the experimental validation does not meet the standard required to confidently support the claimed improvements. The weaknesses are evidential rather than structural: with rigorous significance testing, corrected terminology, and validation of the clustering behavior, the paper could become publishable. A major revision is warranted.

### All calibration anchors consulted

| Anchor ID | Avg Score | Round | Comparison |
|-----------|-----------|-------|------------|
| 0yVP49SDg0 (Mamba-HMIL) | 3.25 | 1 (weak) | Weaker: less clear contribution, major novelty concerns |
| i4ouG6Kc8M (Dual-Metric SSL) | 2.50 | 1 (weak) | Weaker: different topic, lower quality |
| MOCEoNsjEx (Pg-GAT) | 3.00 | 1 (weak) | Weaker: unclear methodology |
| jHdsZCOouv (SHAP-CAT) | 3.40 | 1 (weak) | Weaker: different topic (multimodal), lower quality |
| 6xrDPHhwD3 (MFC) | 6.00 | 1 (middle), 2 | Stronger: more ambitious, more comprehensive validation |
| trj2Jq8riA (VLSA) | 5.67 | 1 (middle), 2 | Slightly stronger: clearer novelty, more thorough experiments |
| AZW3qlCGTe (Set-Level Labels) | 5.67 | 1 (middle), 2 | Similar quality but different topic |
| lo9HMoGNwQ (SMIL) | 4.50 | 1 (middle), 2 | Weaker: unclear clinical motivation, limited novelty |
| xriGRsoAza (Inherently Interpretable TSC) | 8.00 | 1 (strong) | Much stronger: not directly comparable (time series) |
| 3b9SKkRAKw (LeFusion) | 8.00 | 1 (strong) | Much stronger: not comparable (diffusion models) |
| oZdaEiDBpF (MI-PLL) | 5.00 | 2 | Slightly weaker: poor presentation, but strong theory |

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>