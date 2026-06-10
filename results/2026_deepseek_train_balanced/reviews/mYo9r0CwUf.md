Now let me write the final consolidated review.

## Summary

The paper proposes continuous volumetric rendering for Neural Density-Distance Fields (NeDDF). It makes three main contributions: (i) deriving analytic lower and upper bounds on transmittance between sample points using only the Eikonal gradient constraint (||∇D|| ≤ 1), enabling rendering without assuming piecewise-constant density; (ii) a bisection sampling strategy that recursively splits intervals at an analytically chosen point to equalize color-weight upper bounds; and (iii) a frequency-separated Multi-resolution Hash Encoding adapted to distance fields, where features from different grid resolutions are masked and scaled to respect gradient constraints. The method also extends distance-field rendering to unbounded 360° scenes via contract coordinate scaling. Experiments on synthetic and real datasets show improved PSNR over prior distance-field methods (NeuS, NeDDF) and, for the first time, enable distance-field rendering on unmasked 360° scenes at performance comparable to iNGP.

## Strengths

- **Principled derivation of transmittance bounds from Eikonal constraints.** The paper derives lower and upper bounds on transmittance between any two sampled points (Section 3.2, Eqs. 94–116) using only the property ||∇D|| ≤ 1. This is a genuine theoretical advance over the standard piecewise-constant density assumption used in NeRF-family discretization (Eq. 5), and Section 4.2 and Figure 7 empirically verify that the true transmittance always falls within the derived bounds across 1024 test rays.

- **Bisection sampling with an analytic split point.** The sampling method (Section 3.2) recursively divides intervals at t_c = ½(t₁ + t₂ + d₁ − d₂), chosen to equalize the maximum color-weight upper bounds on both sub-intervals. This is a novel application of the bound structure to guide sampling without relying on a separate coarse network or occupancy grid.

- **Frequency-separated hash encoding adapted to distance-field constraints.** The paper identifies the core incompatibility between grid-based encodings and distance fields: high-resolution grids produce gradients too large for the Eikonal constraint (Section 2.2). It addresses this by masking the upper-triangular elements of the weight matrix to keep Nyquist frequencies per grid level separate, and scaling each grid's features by 1/N_i so gradient norms remain bounded (Section 3.3, Figure 6). This is a thoughtful architectural adaptation.

- **First distance-field method to handle unmasked 360° scenes.** The paper introduces a distance-field scaling under contract coordinates (Eq. 164–165), enabling distance-field-based methods to handle unbounded scenes for the first time. As reported in Section 4.1, NeuS, NeuS2, and NeDDF "did not converge for the unmasked 360 scenes," whereas the proposed method achieves results comparable to iNGP on the Mip-NeRF 360 benchmark.

- **Honest limitation discussion.** Section 5 openly acknowledges that the method is slightly inferior to iNGP in accuracy, converges ≈2× slower, and struggles with FP16/ReLU due to the need for smooth first-order derivatives. This candor helps practitioners understand the real trade-offs.

## Weaknesses

### Major

- **No ablation studies isolating the contributions.** The paper proposes three distinct components: (i) transmittance bounds with bisection sampling, (ii) tighter bounds with a second-derivative assumption for rendering termination, and (iii) frequency-separated hash encoding with per-frequency scaling. There is no experiment that isolates any of these components. Since the method builds NeDDF on top of iNGP's hash grid architecture, the most basic question — "How much of the improvement comes from the grid-based backbone vs. the proposed sampling/rendering?" — is unanswered. A minimal comparison between (a) NeDDF with vanilla hash encoding and default NeDDF sampling, (b) NeDDF with frequency-separated encoding but default sampling, and (c) the full method would directly measure the value of each claimed innovation. Without this, readers cannot attribute the reported gains.

- **No quantitative comparison of sampling efficiency.** The central methodological claim is that the bisection sampling is *efficient*. Yet Section 4.2 only validates that the bounds correctly contain the true transmittance (on 1024 rays from a single Lego scene). It does **not** compare the number of samples per ray, rendering time, or convergence speed against any baseline strategy (e.g., NeDDF's default coarse-to-fine sampling, or iNGP's occupancy-grid sampling). Figure 9 plots "number of samplings satisfying the resolution" without any baseline for comparison. The abstract states the method "minimizes the maximum of the bound range," but no experiment demonstrates that this translates into a practical advantage.

### Minor

- **Only PSNR reported on the synthetic dataset; SSIM and LPIPS are absent.** NeRF-family papers universally report SSIM and LPIPS alongside PSNR. Their omission is problematic because the paper specifically claims improvements in "thin shapes," "fine holes," and "specular reflections" — details that SSIM and LPIPS are better at measuring. Without these metrics, the qualitative claims about detail recovery are not quantitatively supported.

- **No evaluation of reconstructed geometry.** A key advantage of distance fields over density fields is that they enable surface extraction via Marching Cubes. The paper never evaluates whether the improved rendering quality yields better geometry (e.g., Chamfer distance, normal consistency, or F-score). This would substantially strengthen the distance-field narrative and is a natural extension of the evaluation.

- **No wall-clock time measurements.** The paper states convergence takes "about twice as long" as iNGP (Section 5) but provides no actual timing data. For a paper claiming efficiency improvements, the absence of training or inference wall-clock times is a significant omission.

- **Unclear when the tighter bound assumption holds.** The "tighter bound" (Section 3.2) requires that the second derivative of D not cross zero in the interval. The paper acknowledges this assumption "is not satisfied in the initial segmentation" but claims convergence still works — this claim is supported only on 1024 rays from one scene. No analysis of when this assumption fails or how robust the method is to such failures is provided.

- **Overstated "continuous" rendering in the framing.** The title and contributions claim "continuous volumetric rendering" that "does not require discretization of the density." In practice, the method evaluates the distance and color fields at discrete sample points. The continuity is in the *bounding* of transmittance between samples, but the final rendering uses "the trajectory with the maximum transmittance" (line 141), which is an approximation. This is a useful error-bounding approach, but not a truly continuous rendering integral.

- **Reproducibility details missing for the hash encoding.** The frequency-separated encoding description (Section 3.3) omits key architectural parameters: the specific grid resolutions N₁,...,N_L, the feature dimension F, and the hash table size T. The scaling argument (1/N_i) is justified with a 1D example but the behavior in 3D is more complex. The claim that "a single network can stably handle the distance and color fields" is not supported by any analysis of training stability.

### Trivial

- None beyond what is addressed above.

## Nice-to-Haves

- Add ablation experiments isolating each of the three claimed contributions.
- Compare sampling cost quantitatively (samples per ray, rendering time at equivalent PSNR) against NeDDF's default sampling and iNGP's occupancy grid.
- Report SSIM and LPIPS on the synthetic benchmark to support the detail-recovery claims.
- Evaluate surface reconstruction quality (Chamfer distance, normal consistency) to demonstrate the distance-field advantage.
- Provide wall-clock training and inference times.

## Removed Points

The following points from the reviewer inputs were removed after verification against the paper:

1. **"Suspicious Equation (100) is dimensionally inconsistent."** — The equation as parsed ($\exp(A) = \exp(B) + C$) is indeed mathematically suspicious, but this is likely a formatting artifact from multi-line equation parsing in the PDF extraction, not an error in the original submission. The instructions require treating such artifacts as parser errors.

2. **"Notation $h(t)$ satisfies $|\nabla D|^2 = \sqrt{h^2 + g^2}$ is mathematically wrong."** — This is a formatting artifact (missing/extra symbols from parsing), not an author error.

3. **"The tables are unreadable (embedded as images)."** — Formatting artifact from PDF extraction; the original submission contains proper tables.

4. **"Missing more recent baselines like Neuralangelo."** — The instructions prohibit raising missing related works as weaknesses.

5. **Generic clarity complaints** ("the derivation is dense and several steps are unclear") — Too vague to constitute a concrete weakness.

6. **"The 360-dataset results do not compare against distance-field baselines"** — The paper transparently explains that NeuS and NeDDF did not converge on unmasked 360 scenes. This is not a weakness of the paper but a statement of fact about prior methods.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add a controlled ablation: compare (i) NeDDF + vanilla iNGP hash encoding (no frequency separation, default sampling), (ii) NeDDF + frequency-separated encoding (default sampling), (iii) full method. This will directly measure the value of each claimed component.

2. Add SSIM and LPIPS metrics to Table 1 to support the qualitative claims about fine details.

3. Report wall-clock training times and average samples-per-ray counts against baselines to substantiate the efficiency claims.

4. Clarify the derivation in Section 3.2: ensure all equations are self-consistent and clearly labeled, and specify the exact grid parameters (N₁,...,N_L, F, T) used in experiments.

5. Add geometry evaluation (Chamfer distance, normal consistency via Marching Cubes) to demonstrate the distance-field advantage beyond rendering quality.

## Score and Decision

The paper tackles a real problem — distance-field neural rendering lags behind density-field methods — and proposes genuinely novel solutions: principled transmittance bounds from Eikonal constraints, bisection sampling guided by those bounds, and a frequency-separated hash encoding adapted to distance fields. The core ideas are sound and the method demonstrably improves over prior distance-field approaches.

However, the evaluation is substantially incomplete. The lack of ablation studies makes it impossible to attribute improvements to specific contributions. The absence of sampling efficiency comparisons leaves a central claim unvalidated. Missing metrics (SSIM, LPIPS), geometry evaluation, and wall-clock timing data further weaken the empirical support. For a top conference like ICLR, the evidence does not yet meet the bar for acceptance, though the contributions are promising and worth pursuing with a more thorough evaluation.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>