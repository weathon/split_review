Now I have a solid calibration. Let me now produce the final consolidated review.

---

## Summary

This paper identifies a spatial imbalance problem in sparse-view 3D Gaussian Splatting — overfitting in near-field regions and underfitting in far-field regions — and proposes D²GS to address it. The framework has two components: a Depth-and-Density Guided Dropout (DD-Drop) that adaptively prunes redundant Gaussians based on local density and camera distance, and a Distance-Aware Fidelity Enhancement (DAFE) module that applies stronger supervision to distant areas via monocular depth masks. Experiments on LLFF and MipNeRF360 show consistent PSNR gains of 0.5–0.9 dB over prior per-scene optimization methods.

## Strengths

- **Well-motivated problem analysis with concrete evidence.** Section 3.1 and Figure 1 go beyond qualitative claims by reporting actual Gaussian counts: near-field regions under sparse views produce 11,450 Gaussians vs. 6,112 in dense views (overfitting), while far-field regions produce only 3,082 vs. 5,224 (underfitting). This empirical grounding clearly differentiates the paper's motivation from prior work (e.g., DropGaussian's uniform dropout).

- **Component-wise ablation confirms each module contributes.** Table 4 shows monotonic PSNR improvements from 19.22 (baseline) to 21.35 (full model) as density score, depth score, depth-based layering, and DAFE are added sequentially. The IMR also improves consistently from 3.162 to 3.039. This demonstrates that the modules work as designed and are complementary.

- **Consistent quantitative gains across benchmarks.** On LLFF (3-view, 1/8 res.), D²GS achieves 21.35 PSNR / 0.746 SSIM / 0.179 LPIPS, surpassing DropGaussian by 0.59 dB and LoopSparseGS by 0.50 dB (Table 1). On MipNeRF360, it improves over DropGaussian by 0.35 dB (Table 2). These gains are modest but consistent, lending credibility to the method.

- **Systematic parameter robustness analysis.** Table 5 explores dropout rates, score weights, depth threshold, and DAFE loss weight over reasonable ranges; the best PSNR varies only between 21.16 and 21.35, showing the method is not overly sensitive to hyperparameter choices.

## Weaknesses

### Major

- **The ablation does not cleanly isolate improvement from uniform dropout to adaptive dropout.** The baseline row in Table 4 achieves 19.22 PSNR — which corresponds to vanilla 3DGS, not DropGaussian (which achieves 20.76 in Table 1). Since the paper's core thesis is that uniform dropout (DropGaussian's approach) is suboptimal and adaptive dropout is better, the ablation should include a row replicating DropGaussian's uniform dropout under the same codebase. Without this, the reader cannot tell how much of the 21.35 final PSNR comes from replacing uniform dropout with adaptive dropout vs. from other factors. The paper does compare against DropGaussian in Table 1 as a separate method, but the ablation table itself lacks this critical contrast.

- **The IMR metric is introduced as a contribution but is not validated against any interpretable quantity.** The metric measures distribution-level consistency across training runs, and D²GS achieves a lower IMR than baselines (Table 3). However, the paper never shows that IMR correlates with anything meaningful — e.g., the standard deviation of PSNR across runs, per-view rendering variance, or any downstream task. The metric could be omitted from the paper without changing the core claims about rendering quality. Figure 3 (left) shows PSNR instability across runs, yet IMR is never plotted against PSNR variance. Validation would require at minimum one plot linking IMR to an existing, interpretable measure of robustness.

- **No error bars or variance reporting for the main image metrics.** The paper extensively discusses instability (Figure 3, left) and runs 10 independent models for IMR, yet Tables 1, 2, 4, 5, and 6 report only point estimates with no standard deviations or confidence intervals. Given the paper's emphasis on robustness and stability, this is a significant omission — the reader cannot assess whether the reported PSNR gains are statistically meaningful across runs.

### Minor

- **State-of-the-art claim needs scope qualification.** The abstract and introduction state that D²GS achieves "state-of-the-art novel view synthesis" without qualification. The experiments compare only against per-scene optimization methods (NeRF and 3DGS variants). The related work section discusses feed-forward methods (PixelSplat, MVSplat, HiSplat) that follow a different paradigm for the same task, but these are not included in the comparison. The claim should be explicitly scoped to per-scene optimization methods.

- **Table 2 (MipNeRF360) does not specify the number of input views.** Table 1 clearly states "3-view" and "6-view" in its header; Table 2 should do the same for consistency and completeness. The experimental setup section says "following the same data splits and downsampling as prior work," but the specific view count should be stated in the table caption.

- **IMR is only evaluated on LLFF, not MipNeRF360.** If IMR is intended as a general evaluation tool for 3DGS robustness, it should be demonstrated on at least a second dataset. As presented, it is only shown on one dataset (Table 3), making its generality unclear.

- **The DAFE improvements across different depth estimators are very small (0.14 dB).** Table 6 shows PSNR ranging from 21.21 (MiDas) to 21.35 (DepthAnything V2). While this demonstrates compatibility, the absolute variation is small enough to raise questions about whether the depth estimator choice matters much in practice.

### Trivial

- The dropout rate schedule in Equation (3) is described as "progressively increasing," but it is simply a linear function min(t,T)/T. This is not a problem with the method, but the description is slightly inflated.

## Nice-to-Haves

- A computational cost analysis (training time added by density estimation, per-Gaussian scoring, and Sinkhorn computation for IMR) would help practitioners assess the method's practical overhead.
- A limitations paragraph discussing the reliance on monocular depth quality, the fixed threshold τ, and the increased training complexity would strengthen the paper's credibility.
- Validating IMR by plotting it against PSNR variance across training runs (as suggested by the critic) would turn the metric from an unsubstantiated construct into a demonstrably useful tool.

## Removed Points

- **"The IMR metric is a solution in search of a proven problem"** — Kept but demoted from a critical/fatal issue to Major. The metric's lack of validation is a real weakness, but the paper's core method contributions (DD-Drop, DAFE) are independent of IMR. The paper would still be publishable without the metric.

- **"Feed-forward methods omission is misleading"** — Weakened from a Critical Issue to Minor. The paper clearly scopes to per-scene optimization methods; feed-forward methods are a different paradigm. The SOTA claim should be qualified but the omission is not an evidential flaw.

- **"The description of Equation 2 as 'locally continuous and globally discrete' is inflated"** — Removed. This is a style judgment, not a substantive criticism. The description is a reasonable characterization of the design.

- **"Stratified importance sampling for IMR may introduce bias — impact not analyzed"** — Removed. This is a reasonable practical choice for tractability; the paper acknowledges it. Demanding bias analysis for a secondary metric is scope creep.

- **"Table 3 has no error bars for IMR despite 10 runs"** — Merged into the broader "no error bars" weakness above. Already covered.

- **"No discussion of the fixed threshold τ as a limitation"** — Moved to Nice-to-Haves as a suggestions-type point.

- **Strength Finder strengths about "novel robustness metric with clear empirical advantage"** — Weakened. The metric is novel but its empirical advantage is not validated against interpretable quantities. Changed to acknowledge the metric exists and D²GS scores lower on it, without claiming it constitutes a validated strength. (The component ablation and quantitative gains are kept as strengths.)

- **Strength Finder statement about "the single most convincing evidence is LLFF performance"** — This is a subjective framing, not a strength. Removed.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Add a DropGaussian (uniform dropout) ablation row to Table 4.** This is the single most impactful addition: it would directly demonstrate whether the improvement comes from adaptive dropout, depth-based layering, or both. Currently, the reader must cross-reference Tables 1 and 4 to approximate this comparison.

2. **Validate IMR with one concrete experiment.** The simplest approach: compute the standard deviation of PSNR across the 10 runs used for IMR, then plot IMR vs. PSNR std-dev across methods. If IMR correlates with PSNR variance, its utility as a robustness metric is immediately clear.

3. **Add standard deviations (±) to Tables 1, 2, and 4.** Run each configuration at least 3–5 times and report mean ± std. Given the paper's emphasis on training instability, this directly supports the robustness narrative.

4. **Qualify the "state-of-the-art" claim** to explicitly reference per-scene optimization methods.

5. **Specify the number of input views** in the MipNeRF360 table and in the experimental setup description.

## Score and Decision

**Round 1 (bracketing):** Searched three bands for sparse-view 3DGS papers. Low band (<3.5) contained weak/withdrawn papers (scores 2.5–3.4). Middle band (3.5–7.5) contained anchors including DepthSplat (5.0), MVGS (4.75), studentSplat (4.25), and Ref-Gaussian (6.5). High band (>7.5) contained top papers (NoPoSplat 8.0, DreamGaussian 8.5). Initial bracket: **4.5–6.5**.

**Round 2 (narrowing):** Searched within (4.0, 6.0) and (5.5, 7.0) bands. Retrieved SHARE (5.5), 3DGS-Det (5.25), Well-NeRF (5.2), NVS-Solver (6.0), and HQGS (6.5, accepted poster). 

Comparing against anchors:
- **SHARE (5.5)**: Pose-free GS with a novel formulation but missing key baselines. D²GS has a narrower but more clearly validated core contribution. Comparable quality.
- **Well-NeRF (5.2)**: Simple regularization idea for sparse-view NeRF, with limited comparisons. D²GS has more thorough experiments and clearer ablations. **D²GS is slightly stronger.**
- **HQGS (6.5, accepted poster)**: Strong problem motivation, thorough evaluation, well-written. D²GS has comparable problem analysis but weaker evaluation (no error bars, unvalidated IMR). **D²GS is weaker than HQGS.**

The paper has real contributions (DD-Drop and DAFE are cleanly motivated, the ablation shows each helps, and the gains are consistent). However, the evaluation gaps — the missing uniform-dropout ablation row, unvalidated IMR metric, and absence of error bars — prevent it from reaching the level of a clear accept. These are addressable in revision.

**Final score: 5.5** — a solid paper with a well-motivated method and consistent gains, held back by evaluation gaps that can be resolved.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>