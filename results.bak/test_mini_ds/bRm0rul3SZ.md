## Summary

This paper introduces the first dedicated approach for unpaired panoramic image-to-image translation (Pano-I2I), tackling the task of translating daytime panoramas into night/rainy/twilight styles using readily available pinhole images as the target domain. The method combines deformable convolutions with spherical offsets, spherical positional embeddings, distortion-free discrimination (projecting random panorama regions to pinhole views for the discriminator), rotation augmentation/ensemble, and two-stage training. Results on StreetLearn → INIT and Dark Zurich show substantial improvements over existing I2I methods (CUT, FSeSim, MGUIT, InstaFormer) in both quantitative metrics and user studies.

## Strengths

1. **Distortion-free discrimination is a well-motivated and effective technical contribution.** The idea of converting random panorama regions to pinhole-like views before feeding them to the discriminator directly addresses the core challenge: the discriminator otherwise tries to separate style from geometric distortion, which it cannot do. Ablation Table 3 confirms this component's importance (FID improves from 33.4 to 29.1, SSIM from 0.539 to 0.613).

2. **Spherical positional embedding and ERP-aware deformable convolution are principled adaptations for panoramic geometry.** The spherical PE (Eq. 4) provides cyclic spatial guidance that encourages boundary continuity, while the deformable convolution with fixed ERP offsets (Eq. 1) enables a shared encoder to process both panoramas and pinhole images. Ablation confirms both contribute meaningfully (removing both: SSIM drops from 0.613 to 0.578).

3. **Two-stage training strategy is well justified and supported by ablation.** Stage I (self-reconstruction on panoramas) followed by Stage II (I2I with pinhole targets) is a sensible approach given the large domain gap and limited panorama data. Ablation shows two-stage training improves FID from 35.8 to 29.1 and SSIM from 0.576 to 0.613 compared to single-stage.

4. **User study provides independent validation.** Results from 60 users across 10 images per task (Fig. 5) show Pano-I2I ranking highest in overall quality, content preservation, and style relevance for both day→night and day→rainy, corroborating the quantitative findings with human perception.

## Weaknesses

### Fatal

None.

### Major

1. **Baseline comparison fairness is not adequately demonstrated.** The quantitative gaps are extreme — e.g., FID of 18.68 vs. 161.54 for night and SSIM of 0.654 vs. 0.052 (Table 1). An SSIM of 0.052 indicates the baseline output is nearly uncorrelated with the input, which strongly suggests training collapse rather than a reasonable-but-inferior translation. The paper reports that baselines were trained on the same datasets but provides no evidence of hyperparameter tuning for this novel setting, no learning curves, no monitoring for training divergence, and no analysis of whether the baselines received a fair configuration. While the core claim that existing methods struggle on this task is likely true (supported qualitatively by Fig. 4), the quantitative evidence as presented does not convincingly rule out that baselines were set up to underperform. This does not invalidate the method's contribution but weakens the quantitative superiority claim.

### Minor

2. **The FID metric on random pinhole projections captures only local style consistency.** The paper computes FID by projecting a random 90°-FoV crop of the translated panorama and comparing it to real pinhole images. While this is a reasonable adaptation for the pinhole target domain, it only evaluates a single narrow crop, not the global style coherence across the full 360° panorama. A method that transfers style correctly in only one region could potentially score well. The SSIM metric (full panorama) and user study partially mitigate this, but the paper does not discuss this limitation of the primary style metric.

3. **MGUIT and InstaFormer are disadvantaged by noisy bounding box pseudo-labels.** These methods require instance annotations, so the paper uses YOLOv5 to generate pseudo-labels. The paper acknowledges this but does not discuss the potential degradation this may cause for these baselines. A simple experiment comparing pseudo-label quality or showing results with ground-truth labels on a subset would clarify this.

4. **Reproducibility details are partially incomplete.** The paper does not specify the FoV or resolution of the pinhole crop used in distortion-free discrimination during training (only the evaluation metric specifies 90° FoV), nor the sampling frequency of random viewpoints. Baseline hyperparameters (learning rates, iterations, batch sizes) are not reported, making it difficult to assess whether baselines were configured fairly. These are addressable but missing.

### Trivial

None.

## Nice-to-Haves

- Providing training curves or loss trajectories for baselines would directly address the baseline fairness concern.
- Adding a simple baseline that projects panoramas to multiple pinhole views, applies an existing I2I method, and stitches them back would establish a nontrivial lower bound.
- A whole-panorama style metric (e.g., average FID across multiple fixed-angle pinhole projections, or per-patch style variance) would strengthen the evaluation.
- Error bars or confidence intervals on the main results would improve confidence, though the large gaps make this less critical.

## Removed Points

- **"No discussion of inference speed / compute cost"** — This is a nice-to-have, not a weakness, as the paper does not claim efficiency.
- **"First time claim should be softened"** — Pure phrasing nitpick; the paper already says "to the best of our knowledge."
- **"Missing related works"** — Cannot be verified without external sources. Removed per instructions.
- **"Baselines such as FSeSim and CUT are known to work on pinhole-to-pinhole"** — True but irrelevant to the novel setting; this is a general observation, not a specific weakness of the paper.
- **"The ablation shows distortion-free discrimination gives the biggest gain"** — Not a weakness; this supports the contribution. This was listed in the harsh critic's "Strengthening the Paper on Its Own Terms" section as a positive.
- **Generic strengths from Strength Finder about problem importance** — Dropped as generic/superficial.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface an angle or implication that the authors themselves missed.

## Suggestions

1. **Address the baseline fairness concern directly.** Show learning curves for all methods (training loss, validation metrics over time) to demonstrate that baselines did not diverge. Report any hyperparameter tuning performed. If the baselines truly collapse due to architectural limitations, provide evidence of this (e.g., training dynamics, loss curves showing failure to improve). Even a brief analysis of why CUT/FSeSim produce SSIM < 0.1 would significantly strengthen the paper.

2. **Add an additional global style evaluation.** Compute FID on a set of fixed-angle projections (e.g., 4 or 8 equally spaced horizontal angles) averaged together, or report the variance of patch-wise style features across the panorama. This would address the concern that the current metric only evaluates local style consistency.

3. **Expand implementation details for reproducibility.** Specify the pinhole crop dimensions/FoV used in df-GAN during training, the frequency of random viewpoint sampling, and the hyperparameters used for each baseline method (learning rate, iterations, batch size, optimizer, scheduler).

## Score and Decision

### Calibration Report

**Round 1 (Bracketing):** Three queries on low (0–3), middle (4–7), and high (8+) bands.

- **Low-band anchors:** Papers scoring 2.00–3.00 (Reject). All substantially weaker — poorly motivated, flawed methodology, or insufficient evaluation.
- **Middle-band anchors:** 4K4DGen (7.00, Accept) — stronger panoramic generation paper with compelling results but narrower scope; VideoPanda (4.75, Reject) — panoramic video generation with overfitting concerns and no ablation; UniHDA (4.80, Reject) — domain adaptation with overstated claims.
- **High-band anchors:** Papers scoring 8.00–10.00 (Accept). All significantly stronger — technically deeper, more comprehensive evaluation, no major fairness concerns.

**Bracket: 4.5 – 6.5**

**Round 2 (Narrowing):** Queries inside [4.5, 6.0] and [5.5, 7.5].

- StochSync (6.00, Accept): Zero-shot panoramic diffusion. Stronger evaluation, no baseline fairness concerns. Our paper is **weaker** — the baseline comparison issue brings it below StochSync.
- UIP2P (5.67, Reject): Instruction-based image editing. Had fundamental backpropagation concerns. Our paper is **stronger** — better ablation, clearer contributions, user study.
- AnyView (5.50, Reject): View transfer with diffusion. Had limited innovation and evaluation concerns. Our paper is **similar or slightly stronger** — more novel problem, better ablation.
- Disentangled Representation Learning (5.50, Accept): Had strong theory but experimental limitations. Our paper is **comparable** — different type of contribution but similar evidence strength.
- Towards Identifiable UDT (6.25, Accept): Domain translation theory. Stronger theory, similar experimental concerns. Our paper is **weaker** — less rigorous fundamental analysis.

**Final score:** 5.5 — The paper has genuine novelty (first panoramic I2I) and technically sound components with ablation support. However, the baseline comparison weakness is significant enough to prevent a higher score. The paper is comparable to AnyView (5.50) and weaker than StochSync (6.00) but stronger than VideoPanda (4.75) and UIP2P (5.67) in terms of overall evidence quality and contribution clarity.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>