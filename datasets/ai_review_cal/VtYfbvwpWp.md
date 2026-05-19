- Decision: Accept
- Avg Score: 5.60
- Scores: 8, 3, 5, 6, 6
Now I have all the verification I need. Here is the final consolidated review.

---

## Summary

This paper introduces GoodDrag, which improves diffusion-based drag editing through two key practices: (1) Alternating Drag and Denoising (AlDD), a framework that interleaves drag operations with denoising steps to prevent perturbation accumulation, and (2) Information-Preserving Motion Supervision (IP), which anchors handle-point features to the original image to mitigate feature drifting during editing. The paper also contributes the Drag100 benchmark dataset with labeled masks and control points, plus two evaluation metrics (DAI for drag accuracy and GScore using Gemini for perceptual quality). Experiments show consistent improvements over DragDiffusion and SDE-Drag across DAI, GScore, user-study preference, and extensive qualitative comparisons.

## Strengths

1. **AlDD framework is well motivated and demonstrated.** The toy experiment (Fig. 3) directly shows that distributing perturbations across multiple diffusion timesteps preserves content far better than adding them all at once. The qualitative ablation (Fig. 8) confirms that AlDD restores fidelity that degrades without it, while reducing drag steps alone sacrifices drag success. The paper also notes (Sec. 3.3) that AlDD reorders computations rather than adding new ones, incurring no extra computational overhead — a practically valuable property.

2. **Information-preserving motion supervision is supported by quantitative feature analysis.** Fig. 9(b) plots the feature distance between the handle point and the original point over drag steps, showing that IP produces a substantially smaller distance (blue curve) than the baseline (orange curve). Fig. 9(a) further shows that the feature-distance heatmap becomes more concentrated (higher standard deviation) with IP, enabling more precise point tracking. These are concrete, measurement-based validations of the claimed mechanism.

3. **GScore shows meaningful alignment with human perception.** Table 3 reports a Spearman correlation of ρ=0.708 with human judgments, far exceeding existing NR-IQA methods (TReS 0.250, MUSIQ −0.125, TOPIQ 0.083). This is a useful contribution to benchmarking drag editing quality.

4. **Drag100 dataset addresses a genuine need.** The dataset provides 100 images with labeled masks and control points, covering diverse categories and task types (relocation, rotation, rescaling, content removal, content creation). This enables controlled comparisons that previous datasets lacked due to unconstrained mask choices.

5. **Strong and consistent quantitative dominance.** Table 1 shows GoodDrag achieves roughly half the DAI error of the best baseline (0.0696 vs. 0.1189 at γ=1) across all patch radii. The advantage holds even when DragDiffusion is given 210 drag operations (matching GoodDrag's motion supervision steps), establishing that the gain is not simply due to more optimization steps — a well-controlled comparison.

## Weaknesses

### Fatal
None.

### Major

1. **No quantitative ablation (DAI/GScore tables) for AlDD and IP components.** The paper's two core contributions are demonstrated only through qualitative visual comparisons (Figs. 8, 10) and a feature-distance plot (Fig. 9). There are no ablation tables reporting DAI or GScore for variants "w/o AlDD" or "w/o IP" on the Drag100 benchmark. Since DAI and GScore are the paper's own evaluation metrics introduced for rigorous comparison, their absence in ablations is a significant gap. Without this, it is impossible to determine how much each component contributes quantitatively to the final performance, or whether one dominates. The paper strongly implies that both are "good practices," but the ablation evidence is incomplete.

### Minor

2. **The notation `z_t^0` in the IP loss (Eq. 6) is not fully explained.** The loss references `z_t^0` as the "unedited image" at timestep t, but the paper does not explicitly describe how this quantity is obtained for each t during the AlDD process. It can be inferred (by running DDIM inversion from z₀ to each timestep t), but a brief clarifying statement is needed for reproducibility.

3. **GScore validation rests on a modest sample.** The correlation ρ=0.708 is computed from 12 images × 3 methods = 36 data points. The paper is transparent about the setup, but the sample is small enough that the reported correlation could be unstable. The paper should explicitly note this limitation.

4. **Task-type distribution in Drag100 is not numerically reported.** The paper shows category counts (58 animals, 16 landscapes, etc.) and lists task types (relocation, rotation, etc.) in Fig. 5, but only the category counts are given numerically. The number of images per task type is missing, which makes it harder to assess whether certain tasks dominate the benchmark.

### Trivial
None.

## Nice-to-Haves

- Reporting DAI/GScore for component ablations (w/o AlDD, w/o IP) would turn a current major weakness into a strength and is the single highest-impact addition the authors could make.
- An independent drag-accuracy metric (e.g., manually labeled point displacement) would complement DAI and further strengthen the evaluation, though the qualitative evidence and user study already support the conclusions.
- Reporting numerical counts per task type for Drag100.

## Removed Points

These points were flagged by reviewers but are removed from the main review for the following reasons:

1. **Metric circularity (DAI ∼ IP loss inflates results).** The harsh critic claimed the IP loss "directly minimizes the same quantity DAI evaluates." This is factually incorrect. DAI (Eq. 4) computes pixel-space MSE between a patch at the *original* handle point p_i and a patch at the *target* point q_i in the final edited output. The IP loss (Eq. 6) aligns *feature-space* representations at the *intermediate* advanced position (p_i^k+β·d_i^k) with the reference at position p_i^0, within the same diffusion timestep t. These are different quantities in different domains (pixel vs. feature), at different positions (original-vs-target vs. intermediate-vs-original), and at different stages (final vs. during optimization). The IP loss could reasonably produce outputs that score better on DAI, but that is a property of a working method, not a circularity. No evidence suggests the comparison is unfair to baselines.

2. **Toy experiment uses Gaussian noise, not structured perturbations.** The paper presents this as an intuitive analogy, not a formal proof. The harsh critic explicitly acknowledges "this is not a flaw."

3. **References to missing appendix sections / proofs.** The parser strips appendix content from all submissions; these exist in the original paper.

## Novel Insights

None beyond the paper's own contributions. The review surfaces a clear pattern: the paper's external validation (comparisons with baselines) is thorough and well-controlled, but its internal validation (ablation of its own components) is qualitatively presented only. This asymmetry is the paper's main structural weakness.

## Suggestions

- Add a quantitative ablation table reporting DAI and GScore for: (a) full GoodDrag, (b) w/o AlDD (single timestep), (c) w/o IP (standard motion supervision), and ideally (d) w/o both. This single addition would substantially strengthen the paper.
- Explicitly clarify how z_t^0 is obtained for each timestep t in the AlDD process (a brief algorithmic note or formula).
- Report the numerical counts per task type (relocation, rotation, etc.) for Drag100.
- Note the limited sample size for the GScore correlation study as an explicit caveat.
