Now I have a thorough understanding of the paper and the reviewer claims. Let me construct the final consolidated review.

## Summary

This paper proposes ComPC, a test-time point cloud completion framework that uses 2D diffusion priors (Zero 1-to-3) via 3D Gaussian Splatting (GS) rendering. Unlike existing test-time methods (SDS-Complete) that require manual text prompts, ComPC renders a reference image from the partial point cloud itself to condition the diffusion model. The pipeline consists of Partial Gaussian Initialization (PGI), Zero-shot Fractal Completion (ZFC), and Point Cloud Extraction (PCE). The method requires no training on point cloud datasets and achieves completion in ~15 minutes per point cloud (vs. up to 1,950 minutes for SDS-Complete).

## Strengths

- **Eliminates dependence on manual text prompts.** Unlike SDS-Complete (Kasten et al., 2024), which requires a hand-crafted text description for each partial point cloud, ComPC renders a reference image from the partial input itself and uses it to condition Zero 1-to-3 (Section 2.2, Section 3.1). This is a genuinely practical improvement for real-world deployment.

- **Substantial speedup over the only prior test-time method.** The paper reports ~15 minutes per point cloud on an RTX A6000 (Section 5), compared to up to 1,950 minutes for SDS-Complete — a >100× speedup. This is enabled by efficient GS rendering versus the VolSDF-based rendering used by SDS-Complete.

- **Strong quantitative results on real-world scans.** On the Redwood dataset out-domain split (Table 2), ComPC achieves CD 6.37 and EMD 6.60, substantially outperforming all baselines including SDS-Complete (CD 11.96, EMD 12.02) and supervised methods. The advantage on in-domain scans is also clear (CD 3.54 vs. next best 7.45).

- **Novel technical adaptations for GS-based completion.** The binarized opacity (Eq. 2, Fig. 3) forces Gaussian centers to cluster near surfaces, and the shared scalar scaling maintains isotropic point-like Gaussians (Section 3.2). The Preservation Constraint (Eq. 6) and Grid Pulling module (Section 3.3) are cleanly motivated and ablated.

- **Ablations isolate each component's contribution.** Tables 3–4 and Figs. 7–8 systematically evaluate colorization strategies, the Preservation Constraint, Gaussian Surface Extraction, and Grid Pulling, showing the contribution of each module.

## Weaknesses

### Fatal
None.

### Major

- **SDS-Complete is omitted from the synthetic benchmark (Table 1).** The paper's central positioning is against SDS-Complete as the only prior test-time method, yet Table 1 compares only against supervised methods (PointAttN, PoinTr, etc.). The authors state (Section 4) that SDS-Complete "only provide codes for the processing of Redwood," but this explains rather than excuses the gap: the claim of superiority over the test-time baseline on synthetic data cannot be assessed from the presented evidence. The Redwood comparison (Table 2) does include SDS-Complete and is encouraging, but the synthetic comparison remains incomplete.

### Minor

- **Synthetic test data is underspecified.** The paper does not state how many objects are used, which categories are represented, how partial views are generated from the cited sources (Krishnamurthy & Levoy 1996; DeCarlo et al. 2003; Praun et al. 2000; Lipman et al. 2008), or the number of test samples (Section 4). While test-time methods reasonably use smaller test sets than supervised benchmarks, this lack of detail prevents reproducibility assessment.

- **Key hyperparameters not reported.** The weighting factors \(w_0\) (Eq. 1), \(w_1\) (Eq. 5), \(w_2\) (Eq. 6), \(w_3\) (Eq. 10), and the noise scale \(\sigma_n\) for initializing \(G_m\) (Section 3.2) are mentioned but never given numerical values. Only \(\delta=0.01\) is reported. This makes re-implementation unnecessarily difficult.

- **No sensitivity analysis for the reference viewpoint estimation.** The estimation searches over 5,000 candidate camera poses (Section 3.1) with a weighting factor \(w_0\). The paper does not analyze how the number of candidates or the value of \(w_0\) affects downstream completion quality. Since the entire pipeline conditions on this reference view, its sensitivity should be characterized.

- **No computational cost breakdown.** The paper reports ~15 minutes total but does not break this down into PGI (viewpoint estimation + rendering), ZFC (optimization), and PCE (surface extraction + Grid Pulling). A breakdown would help identify bottlenecks.

### Trivial

- The filter \(h(G_{in}, V_n)\) identifying "frontmost" Gaussians (Section 3.1, Algorithm 1) is not defined quantitatively (e.g., depth-sorting vs. z-buffer). While the intent is clear, a precise definition would improve clarity.

- Results are averaged over three runs (Section 4) without reporting variance. This is common for test-time methods but noting standard deviations would strengthen confidence.

## Nice-to-Haves

- **Details of the SDF network used in Grid Pulling** (architecture, learning rate, iterations, batch size). These may appear in the supplementary material (Section 5 references ".4" for additional details), but including them in the main paper would improve self-containedness.

- **A direct comparison of binarized vs. continuous opacity** in the ablation study would quantitatively validate the motivation for the binarization (Fig. 3), beyond the conceptual illustration.

- **Failure case discussion in the main paper.** The paper references supplementary material for failure cases (Section 5). Given the method's reliance on a good reference viewpoint and the diffusion model's priors, a brief discussion of when the method fails (e.g., objects with deep concavities, inaccurate reference views) in the main paper would strengthen the presentation.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"The paper does not clarify that Zero 1-to-3 requires the reference image as a condition"** — The paper explicitly states this: "Zero 1-to-3...explicitly conditioned on the reference image and camera transformation" (Section 2.1, line 33).

- **"The assumption that a single reference viewpoint provides a nearly complete view is stated only implicitly"** — The paper states: "methods concentrate mainly on point clouds incomplete due to self-occlusion, which means that these point clouds often appear nearly complete from at least one viewpoint" (Fig. 1 caption, line 17).

- **"Failure cases are not discussed"** — The paper references supplementary material for failure cases (line 230: ".4 for failure cases of our method"). The parser strips supplementary content; this exists in the original submission.

- **Criticism that SDS-Complete results were "re-optimized and normalized" without explanation** — Normalizing coordinates to a standard range (here −0.5 to 0.5) is standard practice for fair metric computation in point cloud completion and does not alter method behavior.

- **"The paper provides no evidence that the Gaussian center drift is problematic or that binarized opacity fixes it"** — Figure 3 provides a clear conceptual illustration of the issue and the fix. While a dedicated quantitative ablation would strengthen this, the critic's claim of "no evidence" is too strong.

## Novel Insights

None beyond the paper's own contributions. The reviewer analyses consistently affirm the core novelty (image-conditioned test-time completion via GS, replacing text prompts) while disagreeing on the severity of evaluation gaps. The most useful signal from the meta-review is that the paper's central claim is incompletely tested on synthetic data against its primary baseline, but the real-scans comparison provides strong support.

## Suggestions

1. **Add SDS-Complete results to the synthetic benchmark (Table 1).** This is the single most impactful fix. Even if it requires re-implementation, providing this comparison would directly validate the paper's core claim on both benchmarks.

2. **Report all hyperparameter values in a single table** (w₀, w₁, w₂, w₃, σₙ, δ, number of candidate poses, N). This is straightforward and would substantially improve reproducibility.

3. **Specify the synthetic test set composition** (number of objects, categories, partial-view generation protocol).

4. **Add a brief failure-case paragraph to the main paper** noting when the reference-viewpoint assumption breaks and how the diffusion model can hallucinate.

5. **Include a per-phase runtime breakdown** (PGI / ZFC / PCE) and a sensitivity analysis of the viewpoint estimation parameters.

## Score and Decision

The paper proposes a genuinely novel test-time framework with clear practical advantages (no text prompts, >100× speedup, strong real-world results). The main technical components are well-motivated and ablated. The most significant weakness is the omission of SDS-Complete from the synthetic benchmark, which undermines a clean quantitative case on that split. However, the Redwood comparison (Table 2) does include SDS-Complete and shows a decisive advantage. The other weaknesses (missing hyperparameters, underspecified synthetic data) are addressable in revision. The contribution is real and the paper is above the bar.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>