- Decision: Accept
- Avg Score: 6.67
- Scores: 6, 8, 6
Now I have all the information I need. Let me compose the consolidated review.

## Summary

This paper proposes GeoSyn, a 3D-aware blur synthesizer for data augmentation. The core idea is to decompose 3D camera motion into a parametric 2D rigid component (reducing ill-posedness) and a non-parametric 3D residual component (capturing depth-dependent effects), both estimated from a single blur image. This enables 3D-aware blur synthesis without requiring depth maps or video frame sequences. The synthesizer uses an amplitude-phase representation to allow controllable modification of blur magnitude and direction. The method is evaluated across four network architectures (MIMO-UNet+, Restormer, NAFNet, FFTformer) on three datasets (GoPro, RealBlur, RSBlur), showing consistent PSNR improvements (e.g., +1.06 dB on RealBlur-J with FFTformer, +0.55 dB on RealBlur-J with NAFNet).

## Strengths

- **3D-aware decomposition without depth maps (Section 3.2, Eq. 4-5, Table 4):** The decomposition of 3D rigid transformation into a 2D parametric component and a 3D residual component, combined via amplitude-phase integration, enables 3D-aware blur synthesis without requiring per-pixel depth. Table 4 shows that the proposed combination (P+NP 3D, 33.10 dB) outperforms both 2D-only parametric (32.65 dB) and 3D parametric with actual depth (32.47 dB), validating the design.

- **Consistent, systematic improvements across diverse architectures and datasets (Table 1):** GeoSyn improves PSNR on all four tested networks and on all three datasets. Examples: NAFNet on RealBlur-J goes from 32.87 to 33.42 dB; Restormer on RealBlur-J from 33.41 to 33.97 dB; FFTformer on RealBlur-J from 32.62 to 33.68 dB. The breadth and consistency of gains is strong evidence that the augmentation generalizes and is not overfitted to a single architecture.

- **Data-agnostic and compatible design (Table 2, Section 4.3):** Unlike ID-Blau (Wu et al., 2024), which requires ground-truth video frames and cannot be trained on RealBlur or RSBlur, GeoSyn works on any blur-sharp pair. It is also compatible with ID-Blau: combining ID-Blau pre-training with GeoSyn augmentation yields 33.09 dB, the best result, showing the method adds orthogonal value.

- **Controllable augmentation via amplitude-phase representation (Section 3.4, Fig. 1):** The polar-coordinate representation of the displacement field enables independent control of blur magnitude and direction. This is used during training to generate millions of distinct blur patterns, and the resulting performance gains confirm the practical value of this controllability.

- **Efficiency gains (Table 5):** A smaller NAFNet-16 (3.13 GMac) trained with GeoSyn outperforms a larger NAFNet-32 (6.43 GMac) trained without it on RealBlur-J (32.97 vs. 32.87 dB), demonstrating that the augmentation can reduce computational cost at deployment.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **ID-Blau comparison in Table 2 (lower) has a confounded training domain.** ID-Blau is trained on GoPro and evaluated on RealBlur-J, while GeoSyn is trained on RealBlur-J. As the authors note, ID-Blau *cannot* be trained on RealBlur-J because it requires video frames — this is a genuine limitation of ID-Blau and an advantage of GeoSyn. However, the current presentation (32.99 vs. 32.70 dB) conflates two effects: synthesis quality and domain adaptivity. Adding a "GeoSyn (trained on GoPro)" row evaluated on RealBlur-J would isolate the synthesis quality difference. The GoPro-trained GeoSyn results are reported in the upper part of Table 2 against kernel-based methods, but not against ID-Blau on RealBlur-J.

- **The "3D-aware" claim lacks direct validation that the non-parametric field captures 3D geometry vs. general 2D non-uniformity.** The decomposition in Eq. 4-5 is algebraically valid for a 3D rigid transformation, and Table 4 shows the combined model outperforms alternatives. But there is no controlled experiment (e.g., rendering blur from a 3D scene with known camera trajectory and comparing recovered vector fields to ground-truth projected motion) that would directly confirm the non-parametric residual ε_τ corresponds to depth-dependent 3D effects. This does not invalidate the practical contribution — the method works well — but it weakens the precision of the "3D-aware" claim.

- **The 3D parametric + depth ablation (32.47 dB) underperforms the simpler 2D parametric variant (32.65 dB).** The paper acknowledges this as "sub-optimal" (line 259) but the explanation is truncated by a figure boundary in the extracted text. Since the proposed P+NP 3D method (33.10 dB) clearly outperforms both, this does not threaten the main contribution, but the result is counterintuitive (adding more information degrades performance) and warrants a clear explanation.

- **No error bars or multiple-run statistics are reported.** This is standard practice in the deblurring literature, but given that the per-dataset/architecture gains are modest (+0.2 to +1.06 dB), reporting variance would increase confidence that the improvements are statistically reliable rather than run-to-run noise.

- **Missing limitations paragraph.** The paper would benefit from explicitly acknowledging limitations: (a) the assumption that camera motion dominates (multiple independently moving objects may not be well-captured by a single global field), (b) the learned residual field is not guaranteed to correspond to true 3D geometry, (c) the synthesizer requires separate training per dataset.

### Trivial

- The amplitude-phase composition function $\mathcal{C}$ (line 95) is described in the text — "δ_τ = C(ΔT_τ, ε_τ) = |ΔT_τ| · |ε_τ| L(ϕ(ΔT_τ) + ϕ(ε_τ))" — but the definition of L (the mapping from polar to Cartesian) is implicit. Adding a brief clarification of L would improve reproducibility.

## Nice-to-Haves

- **Quantitative evaluation of controllability:** The paper shows qualitative examples of varying amplitude/phase (Fig. 1) but does not evaluate how different levels of randomization affect downstream deblurring performance. An ablation that trains deblurring models with different amplitude/phase ranges would strengthen the claim of "controllable" augmentation.

- **Synthetic 3D trajectory experiment:** Generating blur from a 3D scene with known ground-truth camera motion and comparing the recovered vector fields to the true projected motion would directly validate the "3D-aware" claim. This is not required for the practical contribution but would substantially strengthen the paper.

## Removed Points

These points were raised by reviewers but are excluded from the main evaluation for the reasons given:

- *"Composition function C is described only verbally and with an incomplete equation."* — **Removed.** The formula IS provided on line 95: "δ_τ = C(ΔT_τ, ε_τ) = |ΔT_τ| · |ε_τ|L(ϕ(ΔT_τ) + ϕ(ε_τ))". The magnitude-multiplication, phase-addition scheme in polar coordinates is clearly stated and sufficient for reproducibility.
- *"The compensation network h_ξ may compensate for motion-model failures rather than photometric variation."* — **Removed.** This is speculative. The paper states h_ξ addresses "photometric variations between blur and sharp images, arising from different image sensors, lenses, and color drifts" (line 107), which is a standard and well-motivated design choice.
- *"The claim that '3D residual component is directly estimated via a neural network' should be stated with caveat."* — **Removed.** The paper's phrasing is appropriate for describing the method's design. The claim is about how the method works (network estimates it directly), not a theoretical guarantee.
- *"Invertible geometric regularization lacks numerical validation of inversion."* — **Removed.** The regularization is conceptually sound for small displacements with Laplacian smoothing, and Fig. 6 shows visual validation. A numerical check would be overkill for this component.
- *"Training dataset not explicitly listed in Table 1."* — **Removed.** The main text (Section 4.2) clearly explains the training setup for each column. The table is an embedded image that likely contains column labels in the original PDF.
- *"Blur region analysis / mixed blur limitation."* — **Removed.** The paper scopes itself to global camera/predominant object motion; segmenting per-object flows is outside the stated scope.

## Novel Insights

The harsh and strength-focused reviews agree on the paper's overall quality but from different perspectives. The most interesting tension is around the "3D-aware" claim: the harsh critic correctly notes that the non-parametric field's ability to capture 3D geometry is asserted rather than directly verified, while the strength finder correctly notes that the combined parametric+non-parametric model empirically outperforms all alternatives — including a 3D parametric approach that uses actual depth. This tension reveals what is actually the paper's most creative contribution: the algebraic decomposition in Eq. 4-5 is not a theorem about recoverable 3D structure, but rather a *design pattern* that uses a structured parametric backbone to reduce ill-posedness while giving the network enough degrees of freedom (via the non-parametric residual) to approximate depth-dependent effects. The paper succeeds because this design pattern is effective in practice, regardless of whether the residual map literally corresponds to interpretable 3D geometry.

## Suggestions

1. **Add a GoPro-trained GeoSyn row in Table 2** evaluated on RealBlur-J alongside ID-Blau to clarify whether the advantage comes from synthesis quality or domain adaptivity (or both).
2. **Add error bars** (or at minimum report results across 2-3 seeds) for the main comparisons to establish statistical reliability of the reported gains.
3. **Include a brief limitations paragraph** acknowledging that the method assumes a dominant global motion and that the non-parametric residual is an approximation of 3D effects rather than a reconstruction.
4. **Clarify the definition of L** in the composition function — it maps (magnitude, angle) back to Cartesian and is the inverse of the polar decomposition already described.
