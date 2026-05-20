I now have sufficient context. Let me write the final consolidated review.

**Summary of key verifications from the paper:**

1. **"Attention-weighted covariance" claim**: The paper says "attention-weighted covariance matrix" at lines 95, 112, 151, but the formula at line 156 is C = Σ \tilde{g}_k \tilde{g}_k^⊤ — no attention weights a_k in the summation. The centering uses v^(1) = Σ a_k g_k, so centering IS attention-weighted, but the outer product is uniform. The naming is inconsistent with the formula.

2. **Statistical significance**: The paper uses 5-fold CV and reports mean±SE but performs no significance tests. For CAMELYON16, HOMIL ACC 96.98±2.43 vs MambaMIL 96.48±1.37. Standard errors overlap substantially.

3. **DBSCAN**: Line 126 says "non-core points form single-element clusters" — this is indeed a modification of standard DBSCAN (which assigns border points to core clusters and labels unreachable points as noise). No mention of noise handling.

4. **Figure 1**: The caption describes Conv1D layers on instance features producing v^(1) and v^(2), but the text describes cluster features going through parallel streams. This is an inconsistency.

5. **Ablation**: "w/o SOM" (line 282) is ACC 95.98 vs full 96.98 — this IS the correct control (same clustering+attention, without second-order). The comparison is valid.

---

## Summary

This paper proposes HOMIL, a multi-instance learning framework for whole-slide image classification that computes both first-order (attention-weighted mean) and second-order (covariance) moments of patch/cluster features, combined with DBSCAN-based adaptive clustering for efficiency. The core idea — that first-order aggregation discards variability information that a covariance could capture — is well-motivated and practically relevant. On CAMELYON16 and TCGA-NSCLC, HOMIL achieves the highest ACC, AUC, and F1 across ten methods while maintaining competitive runtime.

## Strengths

- **Consistent empirical improvement across all metrics and datasets**: HOMIL achieves the best ACC, AUC, and F1 on both CAMELYON16 (96.98%, 99.23%, 96.54%) and TCGA-NSCLC (93.24%, 97.41%, 92.93%) against nine baselines, all evaluated in a unified codebase with shared feature extractors and data splits.

- **Clean ablation isolating both components**: Table 3 shows that removing the clustering module ("w/o CM") degrades all metrics and increases runtime by 71%, while removing the second-order moment ("w/o SOM") drops ACC by 1.00% and F1 by 1.60%. The comparison "w/o SOM" vs. full model directly isolates the contribution of second-order statistics under the same clustering and attention scheme.

- **Large computational efficiency gains over complex baselines**: HOMIL runs in 310s (CAMELYON16) vs. TransMIL 5175s, MambaMIL 7200s, and HMIL 10800s, making the framework practical for large-scale deployment.

- **Well-motivated statistical reinterpretation of MIL**: Framing ABMIL as first-order moment estimation and motivating the use of covariance to capture inter-feature variability is conceptually clear and provides a principled lens for extending MIL.

## Weaknesses

### Major

1. **The "attention-weighted covariance" claim is inconsistent with the implemented formula.** The paper repeatedly describes the second-order representation as an "attention-weighted covariance matrix" (Sections 4.1, 4.3.3, Figure 1 caption). However, the formula in Section 4.3.3 is **C = Σ_{k=1}^K \tilde{g}_k \tilde{g}_k^⊤**, which contains no attention weight a_k in the summation. While the centering uses v^(1) = Σ a_k g_k (attention-weighted mean), the outer product accumulation is uniformly weighted. A genuinely attention-weighted covariance would be **Σ_{k=1}^K a_k (g_k - v^(1))(g_k - v^(1))^⊤**. This discrepancy matters: the paper motivates the method as a principled extension of ABMIL's moment framework, but the actual implementation computes a hybrid — attention-centered, uniformly-summed covariance — whose statistical interpretation differs from what is claimed. This undermines the central conceptual contribution.

2. **Reported improvements are small and lack statistical support.** On CAMELYON16, HOMIL's ACC improvement over the best baseline is +0.50% (96.98 vs 96.48), and AUC improvement is +0.21% (99.23 vs 99.02). Standard errors overlap substantially: HOMIL's ACC 96.98±2.43 and MambaMIL's 96.48±1.37 give overlapping two-SE intervals. On TCGA-NSCLC, improvements are similarly marginal (+0.35% ACC, +0.73% AUC). The paper uses 5-fold cross-validation but performs no paired significance tests, confidence intervals on differences, or bootstrap analyses. The abstract's claim of "significantly improves the state-of-the-art performance" is not supported by the evidence presented.

### Minor

3. **DBSCAN description deviates from the standard algorithm without discussion.** Section 4.2 states that "non-core points form single-element clusters." In standard DBSCAN, border points (non-core points within ε of a core point) belong to that core's cluster, and points unreachable from any core point are labeled noise (not assigned to any cluster). The paper's version effectively disables the noise label and alters cluster assignments. The paper does not describe this modification, justify it, or analyze its impact on the density-adaptive clustering claim.

4. **Figure 1 does not match the text description.** The figure caption describes Conv1D layers processing instance features to produce first- and second-order features, but Section 4.1 states that cluster features {g_k} are processed through two parallel streams (attention-weighted sum for first-order, covariance for second-order). This discrepancy makes the architecture difficult to follow.

5. **Covariance compression via Conv1D is not ablated or justified.** The covariance matrix C ∈ ℝ^{512×512} is compressed to ℝ^{512} using row-wise 1D convolution (m=64, T=4 kernels) with double max-pooling — a highly aggressive reduction from 262k to 512 values. No alternatives (e.g., flatten + linear, eigenvalue decomposition, Cholesky features) are compared. The paper does not analyze what information is preserved or lost.

6. **Evaluation uses only one feature extractor (CONCH).** All experiments rely on CONCH features, making it unclear whether the benefit of second-order moments generalizes to other histopathology encoders (e.g., UNI, ResNet-50, CTransPath).

### Trivial

7. **Covariance rank and estimation stability are not analyzed.** When the number of clusters K < 512 (which can occur for slides with rare pathology), the per-slide covariance matrix is singular and the estimate is high-variance. The paper does not report the distribution of K or discuss regularization.

## Nice-to-Haves

- Implement the genuinely attention-weighted covariance (with a_k in the outer product) and compare to the current uniform-weighted variant.
- Add significance tests or bootstrapped confidence intervals on the difference between HOMIL and the best baseline.
- Show results with at least one additional feature extractor (e.g., UNI, ResNet-50) to demonstrate generalization.
- Visualize example clusters and their attention weights to support the density-adaptive clustering claim.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Second-order moment requires correct weighting"** (from Harsh Critic's Missing Experiments #1): The reviewer demands the attention-weighted covariance as a missing experiment. While the naming issue is real, the paper already implements a valid method (uniform covariance on attention-centered features). This is a suggested improvement, not a demonstration that the current method is wrong.

- **"Ablation should compare ABMIL+clustering vs full"** (from Harsh Critic's Missing Experiments #3): The paper already does this — "w/o SOM" is exactly ABMIL+clustering (first-order only). The reviewer initially says the paper doesn't report it, then acknowledges "w/o SOM" is this variant. The comparison is valid.

- **"Time comparison is skewed"** (from Harsh Critic): The paper transparently reports times including clustering. The efficiency benefit comes from the overall framework, and the paper never claims the second-order moments specifically reduce computation — the ablation shows they increase it (310s vs 217s w/o SOM).

- **"Discussion of fusion weights is speculation"** (from Harsh Critic): This is a typical level of analysis for learning curves; demanding strict hypothesis testing for every figure is disproportionate.

- **Strengths from Strength Finder that are generic or conflict with verified weaknesses** (filtered as per instructions).

## Novel Insights

None beyond the paper's own contributions. The reviews surface a genuine tension: the paper's core conceptual framing (attention-weighted moments) does not perfectly match its implementation, which weakens the claimed theoretical contribution. The empirical results show consistent but marginal improvements that lack statistical support — a pattern common to incremental MIL papers where SOTA gains are measured in fractions of a percent without significance testing.

## Suggestions

1. **Fix the covariance naming inconsistency**: Either rename it to "covariance of attention-centered features" (accurate) or add the missing a_k weights to the outer product to match the "attention-weighted" claim.
2. **Add statistical significance testing**: Bootstrap the difference between HOMIL and the best baseline over folds or slides, and report p-values or confidence intervals on the improvement.
3. **Ablate the Conv1D compression**: Compare to simpler alternatives (flatten + linear, eigenvalue-based features) to justify the design choice.
4. **Expand evaluation**: Add results with at least one other feature extractor and report the distribution of K across slides.
5. **Clarify DBSCAN handling**: Describe the border/noise modifications and justify their impact.
6. **Harmonize Figure 1 with the text**: Ensure the figure accurately reflects the method described in Section 4.1.

## Score and Decision

**Calibration anchors** (from /home/wg25r/review_agent/human_reviews_2026/):

| Path | Avg Score | Comparison |
|------|-----------|------------|
| CYmjrbQRyM (ASMIL) | 6.00 | Stronger WSI MIL paper; cleaner motivation, comparable scope, accepted. HOMIL has a weaker central claim due to the naming inconsistency. |
| S5Io33pc78 (MAMMOTH) | 6.50 | Much more thorough (19 tasks, 8 MIL methods); accepted. HOMIL's evaluation is less rigorous. |
| EAmn2k52T8 (PackMIL) | 3.50 | Similar tier — interesting idea but execution issues; withdrawn/rejected. HOMIL has a clearer idea but similar presentation problems. |
| Sz2kL7UiEG (CLS-Tuned) | 2.50 | Weaker — minimal novelty, no cross-validation; rejected. HOMIL has more substance. |
| MniooZbsKw (SpecMIL) | 3.50 | Similar — marginal improvements, insufficient statistical rigor; withdrawn/rejected. |
| VaS6xcDrTb | 8.50 | Not directly comparable (rotation estimation). |
| I6LUSZMJLa | 5.50 | Not directly comparable (human-centric MLLM evaluation). |

The paper has a reasonable core idea (using covariance to enrich MIL aggregation) and shows consistent improvements across all metrics on two datasets. However, the central claim about "attention-weighted covariance" does not match the implemented formula, the empirical gains are small without statistical validation, and several design choices are under-explained or unablated. Compared to accepted WSI MIL papers at ICLR (ASMIL at 6.0, MAMMOTH at 6.5), this paper falls short in rigor and clarity. Compared to rejected papers at similar scores, the issues are substantive enough to warrant rejection in the current form.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>