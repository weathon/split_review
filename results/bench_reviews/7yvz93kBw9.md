## Summary

This paper addresses spatial imbalance in sparse-view 3D Gaussian Splatting, where near-field regions overfit with excessive Gaussians while far-field regions underfit. The authors propose D²GS, consisting of: (1) DD-Drop, a depth-and-density guided probabilistic dropout that selectively regularizes near-field over-reconstruction while protecting underfitted far-field regions; and (2) DAFE, a distance-aware fidelity enhancement module that boosts supervision in distant regions using monocular depth priors. The paper also introduces IMR, an inter-model robustness metric measuring consistency across independently trained runs. Experiments on LLFF, MipNeRF360, and DTU show consistent improvements over optimization-based sparse-view baselines.

---

## Strengths

1. **Clear problem diagnosis with quantitative evidence**: Figure 1 concretely demonstrates the spatial imbalance — sparse-view training produces 11,450 Gaussians in near-field (vs. 6,112 for dense views) and only 3,082 in far-field (vs. 5,224 for dense views). This goes beyond anecdotal observation and grounds the method in a measurable failure mode.

2. **Consistent quantitative gains across multiple datasets and settings**: On LLFF 1/8 resolution, D²GS outperforms DropGaussian by 0.59 dB PSNR and CoR-GS by 0.9 dB. On DTU (Table 9), the gains are even larger (21.25 vs. 20.29 PSNR for 3-view). The improvements hold across 3-view and 6-view settings, and on all three standard benchmarks. The ablation (Table 4) shows each component contributes cumulatively, with the full model gaining +2.13 dB over the baseline.

3. **DAFE module is well-designed and robust to depth estimator choice**: Table 6 shows DAFE improves performance with MiDaS, DPT, and DepthAnything V2, with consistent gains across all three. This demonstrates the module's practical utility beyond dependence on a single depth estimator.

4. **Reasonable training overhead**: Table 7 reports D²GS training takes 82s vs. DropGaussian's 56s on LLFF — a modest increase considering the consistent improvement, and far faster than FSGS (425s) or CoR-GS (223s).

---

## Weaknesses

### Fatal
None.

### Major
1. **No error bars or variance reported on quantitative results**: All main tables (Tables 1, 2, 8, 9) report single point estimates with no standard deviations or confidence intervals. Given that the paper's own motivation (Section 3.4, Figure 3) highlights the significant variance across training runs in sparse-view 3DGS, the absence of any variance reporting is a significant omission. The claimed margins of 0.59 dB or 0.35 dB PSNR could easily fall within run-to-run noise. This must be addressed to establish statistical significance.

2. **DropGaussian baseline reproducibility issue is insufficiently surfaced**: The paper discloses in Appendix E that "we found it difficult to reproduce the results reported in their paper, and thus, we report the results obtained from our training." This is a critical detail — the primary baseline numbers in the main text may not correspond to the officially reported DropGaussian performance. This disclosure belongs in the main paper alongside the quantitative tables, not buried in an appendix. While the authors are transparent about this, burying it undermines reader trust in the comparisons.

### Minor
1. **DD-Drop design rationale could be clearer, not fundamentally contradictory**: The local dropout score (Eq. 1) increases with depth (penalizing far-field Gaussians), while the global layering (Eq. 2) then protects far-field Gaussians via λ_far=0.3. The critic calls this a "contradiction," but it is better described as a two-stage design where the local score identifies all potentially problematic Gaussians (based on density and depth) and the global modulation then selectively attenuates regularization in regions known to be underfitted. This is functionally coherent — near-field dense Gaussians get high local scores and no attenuation, while far-field dense Gaussians get high local scores but are attenuated — but the exposition in Section 3.2 could explain this logic more directly rather than relying on the reader to piece it together.

2. **IMR metric lacks explicit validation**: While IMR is a reasonable measure (lower variance across runs = more robust), and Table 4 shows it correlates with PSNR improvements in the ablation study, the paper does not explicitly validate IMR against human judgments, downstream tasks, or demonstrate that it captures information beyond what PSNR/SSIM already tell us. The metric adds value as a secondary diagnostic but is presented as a standalone contribution without the supporting evidence one would expect for a new evaluation metric.

3. **Missing comparison against feed-forward methods**: PixelSplat, MVSplat, and HiSplat are discussed in Related Work but not compared in experiments. While these operate under a different paradigm (generalizable feed-forward vs. per-scene optimization) and have different data requirements, a discussion of how D²GS relates to or complements these approaches would strengthen the positioning. This is scope-appropriate — the paper's baselines (DropGaussian, CoR-GS, FSGS, etc.) are the correct optimization-based comparisons — but acknowledging the gap is warranted.

4. **No explicit failure case analysis or visualization**: The paper shows only successful results. Discussing or visualizing cases where D²GS still struggles (e.g., thin structures, large depth discontinuities, scenes where the depth estimator fails) would provide a more balanced assessment.

### Trivial
- The MipNeRF360 main table (Table 2) only lists 3DGS and FSGS, while CoR-GS and DropGaussian results are relegated to Appendix Table 8. The full set of baselines should appear in the main table for completeness.

---

## Nice-to-Haves

- An analysis of how the depth threshold τ and DAFE weight λ_DAFE interact with scene properties (e.g., indoor vs. outdoor depth ranges).
- A visualization of how the depth-stratified importance sampling works in practice for IMR computation — how are the 10,000 sampled Gaussians distributed across depth?
- An adaptive or learned version of the hand-tuned hyperparameters (D_near, D_middle, λ_far, λ_middle), which the paper itself acknowledges as a limitation in Appendix D.

---

## Removed Points

- **"The IMR metric is not validated as a meaningful measure"** — This is weakened and moved to Minor. The paper does show IMR correlates with PSNR in Table 4 (lower IMR → higher PSNR as components are added), so the concern is better framed as "insufficiently validated" rather than "unvalidated." The critic's claim that "lower IMR could mean always converging to the same bad local minimum" is directly contradicted by Table 4.
- **"The 1/4 resolution results are suspicious because the gap increases with resolution"** — The critic claims larger gap at higher resolution is "counterintuitive." This is incorrect: 1/4 resolution images are *larger* (more detail) than 1/8, and spatial imbalance problems scale with available detail. Larger gains at higher resolution are precisely what one would expect from a method that addresses spatial imbalance.
- **"The analysis in Figure 1 compares 55-view vs 3-view — trivially different"** — The comparison is explicitly designed to characterize the failure mode. Dense-vs-sparse is the relevant comparison and the quantitative counts it produces are informative.
- **Formatting/style nitpicks** (AVGE definition parsed twice, "training details mention 10k iterations but no batch size" — standard 3DGS practice is known).
- **"Missing related works"** — Cannot verify without external sources; the paper cites relevant works including PixelSplat, MVSplat, HiSplat in its related work section.
- **"DD-Drop has a fundamental design contradiction"** — Weakened to Minor. The design is functionally coherent; the exposition is what needs improvement.
- **General reproducibility gripes** about undisclosed hyperparameters — the paper provides substantial implementation details in Appendix B.

---

## Novel Insights

The most interesting observation across the reviews is the tension between the local (depth-penalizing) and global (depth-protecting) mechanisms in DD-Drop. While the reviewer interprets this as a contradiction, it actually reflects a genuine design challenge in sparse-view 3DGS: the same signal (depth) plays opposite roles depending on context — near-field depth correlates with overfitting (too many Gaussians), while far-field depth correlates with underfitting (too few Gaussians). A more carefully controlled experiment that isolates the contribution of each design choice (e.g., removing the depth term from the local score entirely) would not only clarify the paper's claims but would provide a principled understanding of how to design spatially adaptive regularization more broadly.

---

## Suggestions

1. **Report means and standard deviations over 3–5 runs** for all quantitative results. This is essential given the acknowledged instability of sparse-view 3DGS training.

2. **Move the DropGaussian reproducibility disclosure from Appendix E to the main paper**, alongside the quantitative tables where DropGaussian comparisons appear.

3. **Expire the IMR validation** with at least one experiment showing that IMR tracks something not already captured by PSNR/SSIM — for instance, showing that two methods with matched PSNR but different IMR have different behavior (e.g., sensitivity to input perturbations, or quality under small camera pose jitter).

4. **Clarify the DD-Drop design logic** in Section 3.2: explicitly state that the local score identifies *all* high-density Gaussians (regardless of depth), and the global modulation ensures only *near-field* high-density regions are aggressively regularized. Show an ablation removing the depth term from the local score to verify it is the interaction, not redundancy, that drives improvement.

5. **Add a failure case analysis** showing scenes where D²GS does not improve (or degrades) relative to baselines.

---

## Score and Decision

**Anchors consulted:**
- **Path Matters** (avg 5.20, Accept Poster): Similar sparse-view 3DGS paper; our paper shows clearer and larger quantitative gains across more baselines, but lacks variance reporting which Path Matters also lacked. Comparable quality.
- **A Step to Decouple Optimization in 3DGS** (avg 6.00, Accept Poster): Strong optimization-focused 3DGS paper. Our paper has a clearer practical contribution (addressing spatial imbalance) but less analytical depth.
- **Layer-Based 3DGS for CT** (avg 5.50, Reject): Similar structure (problem analysis → method → evaluation). Our paper evaluates on standard NVS benchmarks and has clearer comparisons, making it stronger.
- **Pi3DGS** (avg 5.00, Withdrawn/Reject): Our paper's contributions are more clearly delineated (specific dropout design, depth supervision) compared to Pi3DGS's more incremental combination of existing components.
- **OGGSplat** (avg 3.00, Reject): Much weaker paper with limited evaluation. Our paper is substantially stronger.
- **How to evaluate MDE** (avg 4.50, Reject): Different topic, but the severity of the reviewer concerns (unvalidated new metric) is comparable to concerns about IMR in our paper, though our core contributions do not depend on IMR.

**Calibration**: This paper sits around the 5.0–6.0 range, comparable to "Path Matters" (5.20, accepted) and "Decouple Optimization in 3DGS" (6.00, accepted). The core methodological contributions (DD-Drop + DAFE) are sound and supported by consistent empirical results. The main weaknesses — missing error bars and the insufficiently surfaced DropGaussian reproducibility issue — are addressable but significant. The paper's contributions do not depend on the IMR metric, which is the most controversial element. Relative to the field, this is a solid incremental contribution that addresses a well-motivated problem with a reasonable solution and adequate empirical support, though the presentation and rigor need improvement.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>