Now I have sufficient calibration data. Let me construct the final review.

## Summary

This paper proposes BiEnhancer, a plug-in module for low-light image enhancement targeting high-level vision tasks (object detection, face detection, semantic segmentation). The module extracts multi-scale features via a Feature Aggregation Module, enhances high-level features, fuses them via an attentional bi-level feature fusion mechanism, and refines the representation through iterative estimation. The method is trained end-to-end using only the downstream task loss, without requiring paired low-light/normal data. Experiments on ExDark, Dark Face, and ACDC datasets show consistent but small improvements over prior methods.

---

## Strengths

1. **Consistent improvements across multiple tasks and backbones**: BiEnhancer is evaluated on three different low-light vision tasks (dark object detection, face detection, nighttime semantic segmentation) using four different backbones (RetinaNet, Sparse R-CNN, DeepLab-V3, SegFormer). On ExDark with Sparse R-CNN, it achieves 78.9 AP50 and 49.3 mAP; on Dark Face with Sparse R-CNN, 60.0 AP50 and 25.5 mAP; on ACDC with DeepLab-V3, 53.1 mIoU. All metrics are above the prior best (Tables 2–4).

2. **Ablation evidence for each architectural component**: Table 5 systematically removes FAM, HFEM, BFFM, and IEM individually, showing that each component contributes positively to the final performance on both ExDark (mAP) and ACDC (mIoU). The full model achieves the best results in both settings.

3. **End-to-end training without LIE loss or synthetic paired data**: Following the spirit of FeatEnhancer, BiEnhancer is trained using only the high-level task loss and does not rely on synthetic paired datasets for pre-training. This design choice addresses a practical generalization concern for real-world low-light deployment.

---

## Weaknesses

### Fatal
None.

### Major

1. **Marginal improvements over the direct predecessor (FeatEnhancer) with no statistical significance assessment**: The headline gains over FeatEnhancer are consistently small: +0.5 mAP on ExDark (Table 2), +0.9 mAP on Dark Face (Table 3), +0.3 mIoU on ACDC (Table 4), and +0.5 FPS on ExDark. These numbers are reported from single runs with no error bars, confidence intervals, or statistical significance tests. Given that FeatEnhancer shares the same design philosophy (plug-in, no LIE loss, end-to-end), the claimed advantages are within a range that could be explained by random seed variation or small differences in training configuration. The paper does not establish that BiEnhancer is meaningfully different from its closest competitor.

2. **Method description is confusing and under-specified in key parts**: Several aspects of the architecture are difficult to understand and would impede faithful reproduction.
   - **BFFM tensor notation (Section 3.3)**: Features are cast into a non-standard 5D shape $\mathbb{R}^{H \times W \times 1 \times 1 \times C/N}$ with underspecified operations (multiplication of differently-shaped tensors, summation along an unnamed dimension $T$). The constraint $C/N = 3$ (necessitating $C=24, N=8$) appears to be an artifact of the concatenation logic rather than a principled design choice, and its motivation is not explained.
   - **Iterative estimation (Section 3.4)**: Equation (4) $I_{n+1} = I_n(1 + \bar{F}_{2n-1} + \bar{F}_{2n} I_n)$ is a nonstandard multiplicative update. The mapping from $F_n$ to $\bar{F}_n$ is never specified, and the claimed inspiration from DDPM is not justified—DDPM uses learned additive noise schedules, not pixel-wise multiplicative transforms. The stability of this iteration is not discussed.
   - **HFEM channel dimensions (Section 3.2)**: The module is described as converting "low-channel features $f_h$ into high-channel features" and then reducing channels back to $C$, but the actual intermediate channel counts are not given.

3. **Naming inconsistency in Table 4**: The method is labeled "FFNet(Ours)" in Table 4 (ACDC semantic segmentation results), while the paper title and all other sections use "BiEnhancer." This appears to be an artifact of an incomplete rename and undermines the presentation quality.

### Minor

- **"Inspired by cross attention" claim (Section 1) not reflected in the design**: The BFFM module concatenates features, performs element-wise multiplication and summation, and applies softmax—this is closer to a channel-wise gating mechanism than to the query-key-value formulation of cross-attention. No connection is made to standard attention formulations, making the claim misleading.

- **"Decompose" terminology is imprecise**: The paper states that BiEnhancer "decomposes low-light images into low-level and high-level components" (Abstract, Section 1), but the method performs standard multi-scale feature extraction through downsampling and convolution, not intrinsic image decomposition (e.g., reflectance vs. illumination).

- **No parameter count or FLOPs comparison**: The paper claims speed advantages but does not report the number of parameters or multiply-accumulate operations for BiEnhancer relative to baselines. Given that the FPS gain over FeatEnhancer is only 0.5 FPS (on a ~40 FPS baseline, Table 2), a computational cost analysis is needed to determine whether the marginal accuracy gain comes from added model capacity.

- **No error bars on any experimental result**: All tables report single-run values without variance. While this is common practice in some LIE papers, the small-margin setting (<1% on several metrics) makes the absence of variance information a genuine concern for evaluating robustness.

### Trivial
- The figure captions (Figures 2, 4, 5) contain duplicated text from the image alt-text, a parser artifact of the submission format.

---

## Nice-to-Haves

- A controlled comparison replacing BFFM with FeatEnhancer's fusion mechanism (or vice versa) to isolate the specific contribution of the new fusion design beyond the overall architecture.
- Feature-space analysis (e.g., feature separability or t-SNE) to substantiate the claim of improved "machine readability."
- Testing on additional backbones (e.g., YOLOv8, Mask R-CNN) to strengthen the "versatile plug-in" claim.
- Discussion of failure cases or conditions under which BiEnhancer does not improve performance.

---

## Removed Points

These points are flagged to be removed — treat them with caution.

- **Criticism that "the distinction between machine vision and human vision is not operationalized"** (Harsh Critic, Sec 1): The paper operationalizes this by using the task loss directly (rather than a visual-quality loss), which is a standard approach in the field. The core distinction is that the module optimizes for task accuracy, not perceptual quality.
- **Criticism that Figure 1 (Zero-DCE end-to-end vs non-end-to-end comparison) is not novel because FeatEnhancer already made the point** (Harsh Critic, Sec 1): Independent verification of prior findings is standard practice and does not constitute a weakness.
- **Criticism that Figures 4 and 5 (visual comparisons) undermine the paper's own motivation** (Harsh Critic, Experiments): Showing visual results alongside task metrics is standard practice even when the primary goal is machine readability. The two are not contradictory.
- **Accusation that "the paper does not discuss any task-specific methods beyond those cited"** (Harsh Critic, Related Work): Generic and lacks a concrete anchor.
- **FAM notation inconsistency claim** (Harsh Critic, Sec 3.2): The text describes FAM generating both low-level (F_l) and high-level (f_h) features, which is consistent. The critic's confusion appears to stem from a misreading.

---

## Novel Insights

None beyond the paper's own contributions. The reviews did not generate a genuinely novel observation about the method or the problem that the paper itself does not already surface.

---

## Suggestions

1. Clarify the BFFM tensor operations with standard dimension notation and provide a pseudocode or PyTorch-style implementation sketch in the supplement.
2. Report results with standard deviations over multiple seeds (at least 3) to demonstrate that the observed gains over FeatEnhancer are statistically reliable.
3. Fix the naming inconsistency in Table 4 to use "BiEnhancer" throughout.
4. Provide a parameter count and FLOPs comparison against FeatEnhancer and other baselines to establish that the marginal accuracy gain is not simply from added capacity.
5. Remove or better justify the "inspired by DDPM" and "inspired by cross attention" claims if the architectural connection remains as loose as it currently is.

---

## Calibration

**Round 1 bracket**: Papers from the same topic area were retrieved in three bands — low (avg <3.5), middle (3.5–7.5), and high (>7.5). The paper clearly falls below accepted papers (typically 6+) and above very weak rejects (1–3). Initial bracket: **3.5–6.0**.

**Round 2 narrowing**: Anchors inside this bracket were retrieved:

| Anchor Paper | Avg Score | Round | Comparison to BiEnhancer |
|---|---|---|---|
| SEE (event-based low-light) | 4.00 | R2 | Comparable — SEE had a larger dataset but quality issues; BiEnhancer has consistent experiments but smaller contribution and confusing description |
| LALNet (unified lighting adaptation) | 5.00 | R2 | Weaker — LALNet showed larger performance margins and clearer motivation, despite some reviewer concerns about baseline fairness |
| Flare Removal | 4.00 | R2 | Comparable — both have limited novelty with reasonable experiments |
| LIME-Eval (low-light evaluation framework) | 6.25 | R2 | Weaker — LIME-Eval addresses a more novel problem (evaluation methodology), though it was ultimately rejected |
| Exposure Bracketing | 6.00 | R2 | Weaker — accepted poster with clearer contribution and solid experiments |

The paper is weaker than LALNet (5.0) and LIME-Eval (6.25), and comparable to SEE (4.0). The marginal gains, confusing method description, and naming inconsistency place it below the acceptance threshold.

**Final score**: 4.0 — a weak reject. The paper shows consistent but small improvements and has a reasonable experimental scope, but the contribution over the direct predecessor is not convincingly demonstrated, the method is under-specified, and the presentation has clear errors.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>