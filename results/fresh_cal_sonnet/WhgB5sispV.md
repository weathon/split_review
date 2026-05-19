Now let me run the calibration search for scoring anchors.Let me read some middle-range anchors to calibrate more precisely.Now let me do the narrowing round with more targeted queries.Now I have enough context to write the complete final review. Let me compile all findings.Now I have all the information needed to write the complete review.

---

## Summary

This paper proposes 4D Gaussian Splatting (4DGS), a method that represents dynamic scenes as a collection of 4D Gaussian primitives whose full 4D covariance matrix—parameterized by two quaternions for 4D rotation and a diagonal scaling matrix—treats space and time symmetrically. A conditional 3D Gaussian at any timestamp is derived analytically, enabling use of an adapted tile-based rasterizer. The paper also introduces 4D Spherindrical Harmonics (4DSH), which extends spherical harmonics with Fourier time-basis functions to model time-varying view-dependent appearance. On the Plenoptic Video and D-NeRF benchmarks, the method achieves state-of-the-art quality metrics while rendering at ~915 FPS, far exceeding all prior methods in speed.

---

## Strengths

- **Principled 4D primitive with clean mathematical derivation.** The full 4D covariance $\Sigma = RSS^TR^T$ with a 4D rotation parameterized by two quaternions is a well-grounded extension of 3DGS. The analytic conditional mean $\mu_{xyz|t} = \mu_{1:3} + \Sigma_{1:3,4}\Sigma_{4,4}^{-1}(t - \mu_t)$ and covariance $\Sigma_{xyz|t}$ follow directly from multivariate Gaussian identities, enabling reuse of the splatting pipeline. This is not a heuristic extension but a mathematically coherent generalization.

- **Exceptional rendering speed at SOTA quality.** On the Plenoptic Video dataset the method achieves PSNR/SSIM/LPIPS scores topping all prior methods while rendering at 915 FPS—roughly 600× faster than the next-fastest real-time-capable method (HexPlane at 1.54 FPS). This dual achievement (quality and speed) is the paper's central empirical result and it is directly supported by Table 1.

- **4D Spherindrical Harmonics as a principled appearance model.** The product basis $Z_{nl}^m(t,\theta,\phi) = \cos(2\pi n t/T) Y_l^m(\theta,\phi)$ is a mathematically valid orthonormal system. The ablation in Table 3 confirms a measurable quality drop when 4DSH is removed, directly supporting the claim that time-evolving appearance modeling is beneficial.

- **Spacetime densification strategy verified by ablation.** Incorporating $\mu_t$ gradients as a density-control indicator and performing joint spatial-temporal position sampling during splitting is a meaningful adaptation of the 3DGS densification heuristic to 4D. The last two rows of Table 3 confirm its effectiveness.

- **Works across multi-view and monocular settings without topology priors.** Unlike deformable-GS methods that assume a fixed canonical set and topological invariance, 4DGS is applied to both Plenoptic Video (multi-view) and D-NeRF (monocular synthetic) with state-of-the-art results in both, demonstrating genuine versatility.

---

## Weaknesses

### Fatal
None.

### Major

- **Ablation study covers only two of the six Plenoptic Video scenes.** Section 4.4 explicitly states "we conduct experiments on two representative scenes" for all four ablation variants (No-4DRot, No-4DSH, two densification variants). The central novelty—unconstrained 4D rotation—is therefore validated over only a third of the available benchmark data. Since the advantage of 4D rotation is expected to scale with scene motion complexity, restricting the ablation to hand-picked representative scenes means the generalization of this benefit is not demonstrated. Extending ablations to all benchmark scenes would substantially strengthen the paper's core claim.

- **4D Spherindrical Harmonics hyperparameters not reported.** Equation (6) defines the basis but the paper never states how many Fourier terms $n$ are used in practice, what SH degree $l$ is set to, or how the period $T$ is determined relative to scene duration. These parameters directly control model capacity and computational cost, yet they are absent from both the method section and Section 4.2 (Implementation Details), which only notes "we adopted the settings of Kerbl et al." These are core hyperparameters of a claimed contribution, not trivial implementation details.

### Minor

- **The "first-ever" priority claim is imprecise.** The introduction states without qualification: "This approach marks the first-ever model supporting end-to-end training and real-time rendering of high-resolution, photorealistic novel views in complex dynamic scenes with volumetric effects and varying lighting conditions." The conclusion is more carefully phrased ("To the best of our knowledge…"). The uncaveated version in the introduction is an overclaim, since Dynamic 3D Gaussians (Luiten et al. 2023) also achieves real-time rendering for dynamic scenes (and is cited in the same paper). The distinction being drawn—that this method handles volumetric effects and varying lighting—is not directly demonstrated by a comparison against Luiten et al. on those specific characteristics.

- **The linear motion trajectory limitation is not discussed.** From the conditional mean formula, each Gaussian's trajectory in space is affine in $t$: $\mu_{xyz|t} = \mu_{1:3} + c \cdot (t - \mu_t)$ where $c$ is a constant. Non-linear or multi-modal motion paths must therefore be approximated by many Gaussians with narrow temporal extents. The paper presents the 4D rotation as enabling "motion capture" but does not discuss this structural linearity constraint, which bears on claims of flexibility and scalability.

- **Motion capture demonstrated only qualitatively.** Section 4.4 presents optical flow rendered from $\mu_{xyz|t}$ displacements (Figure 5) as evidence that 4D rotation captures scene dynamics. The paper itself acknowledges the captured motion is "coarse." No quantitative comparison to optical flow estimates is provided. This is acceptable for a paper whose primary objective is rendering quality, but the repeated framing of motion capture as a key interpretive strength is not backed by rigorous evidence.

- **Initialization ambiguity for D-NeRF.** Section 4.1 states "set their initial mean as the scene's time duration," which is ambiguous—it presumably means all Gaussians are initialized with $\mu_t$ equal to the scene midpoint, but this is not stated explicitly. For the monocular reconstruction setting where temporal initialization affects optimization dynamics, the vagueness is unhelpful.

### Trivial

None.

---

## Nice-to-Haves

- **Extend ablations to all benchmark scenes.** Running the four ablation conditions over all six Plenoptic Video scenes and reporting per-scene breakdowns would directly address the evidential gap in the core 4D-rotation claim and reveal whether gains concentrate in high-motion scenes.
- **Report training time.** The paper emphasizes rendering speed (915 FPS) but does not report training wall-clock time. Practitioners need both to evaluate practicality.
- **Clarify the linear trajectory approximation.** A brief discussion of how the affine-in-time trajectory interacts with scene complexity (e.g., a plot of Gaussian count vs. motion complexity) would sharpen the scalability claim.
- **Add a quantitative motion evaluation.** Even end-point error against sparse optical flow annotations for one scene would convert the motion-capture claim from qualitative to quantitative.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Missing deformable 3DGS baselines (Yang et al. 2023, Wu et al. 2023) in quantitative tables** — The harsh critic raises this, but the comparison tables are embedded via `\input{}` commands that are not present in the extracted text; I cannot verify whether these methods are or are not included. Moreover, the paper explicitly discusses why its approach differs from deformable methods (no topological invariance assumption) and demonstrates broader generality. Given the uncertainty, this cannot be confirmed as a genuine omission from available text. *Removed: unverifiable from paper as submitted.*

- **"Training time not reported" as unfair efficiency claim** — The paper does not claim efficiency of training, only of rendering. Omitting training time is mildly informative but does not impugn the paper's stated claims. Moved to Nice-to-Haves.

- **Gaussian count vs. scene length scaling plot** — Framed by the harsh critic as needed to anchor "highly scalable" claims. The paper does not make a quantitative scalability claim tied to Gaussian count, so demanding this plot is scope creep. Moved to Nice-to-Haves.

- **Strength: "first end-to-end real-time dynamic scene rendering"** — As discussed under the Minor weakness above, the "first-ever" framing is imprecise. Removed as a listed strength; the real achievement (SOTA quality + ~600× speed improvement) is acknowledged under verified strengths.

- **Generic strength about "important problem"** — Any framing of the research question as important without specific grounding was not included in the final strengths list.

---

## Novel Insights

The most genuinely novel intellectual contribution is the observation that treating space and time as fully symmetric dimensions within a single Gaussian covariance—rather than attaching time as an independent modulator—implicitly encodes rigid-body-like linear motion through the off-diagonal cross-terms $\Sigma_{1:3,4}$. This is elegant: motion is not learned as an explicit output but emerges as a geometric property of the 4D ellipsoid's orientation. The companion insight that the product of a spherical harmonic basis and a Fourier temporal basis forms a valid orthonormal system (Spherindrical Harmonics) is a natural extension with a clean name. Together, these two ideas—4D covariance for geometry/motion and 4DSH for time-varying appearance—constitute a coherent, parsimonious generalization of 3DGS to the dynamic setting.

---

## Suggestions

1. **Specify 4DSH hyperparameters explicitly** (number of Fourier terms $n$, SH degree $l$, period $T$ relative to scene duration) in Section 4.2.
2. **Run the full ablation on all benchmark scenes** rather than two representative scenes.
3. **Qualify the "first-ever" claim** in the introduction to match the more careful language already present in the conclusion.
4. **Clarify the initialization sentence** in Section 4.1: "set their initial mean as the scene's time duration" should say explicitly that all Gaussians are initialized with $\mu_t$ equal to the midpoint of the scene's time range.

---

## Score and Decision

**Calibration anchors retrieved:**

| Path | Avg Score | Round | Comparison |
|---|---|---|---|
| mYo9r0CwUf.md (NeDDF NeRF) | 2.33 | R1 (low) | Clearly weaker; incremental NeRF improvement, rejected |
| NLRo4qhg6t.md (HIWE NeRF) | 3.00 | R1 (low) | Weaker; grid-encoding NeRF speed improvement |
| uqYjAQ5diD.md (FMapping) | 3.00 | R1 (low) | Weaker; RGB-only NeRF reconstruction |
| xPxHQHDH2u.md (Ref-Gaussian) | 6.50 | R1 (mid) | Weaker; incremental reflective extension of 3DGS |
| dkrEoT68by.md (GS Lucas-Kanade) | 6.00 | R1 (mid) | Weaker; analytical velocity for deformable GS |
| tMG6btjBfd.md (SplineGS) | 6.00 | R1 (mid) | Weaker; NURBS trajectory extension of deformable GS |
| L3WnnnBRdu.md (Hi-Gaussian) | 5.75 | R1 (mid) | Weaker; single-view 3D reconstruction |
| c1RhJVTPwT.md (Swift4D) | 6.50 | R2 | Weaker; divide-and-conquer static/dynamic GS, soundness concerns |
| PbheqxnO1e.md (Lightweight Pred. GS) | 7.00 | R2 | Comparable scope; GS compression, solid but narrower problem |
| LuGHbK8qTa.md (DG-Mesh) | 7.00 | R2 | Comparable; mesh+Gaussian for monocular dynamic, similar fundamental contribution |
| P4o9akekdf.md (NoPoSplat) | 8.00 | R1/R2 | Stronger; clean, complete contribution with no major gaps |
| rzF0R6GOd4.md (Neural SDF Flow) | 8.00 | R1/R2 | Stronger; perfect reviewer consensus, no significant weaknesses |
| QQ6RgKYiQq.md (MovingParts) | 8.00 | R1/R2 | Stronger; rigorous motion discovery with quantitative evaluation |
| qxRoo7ULCo.md (4K4DGen) | 7.00 | R2 | Comparable; 4D generation paper, different task |
| Cjz9Xhm7sI.md (STC-GS weather) | 8.00 | R1 (high) | Different domain; less directly comparable |

**Round 1 bracket:** 6–8.

**Round 2 narrowing:** The paper sits clearly above the 6.0–6.5 cluster (SplineGS, Swift4D, Ref-Gaussian), which all represent incremental or engineering-focused extensions of GS. The 4DGS contribution is more fundamental: a new primitive type with a clean mathematical derivation, enabling simultaneous quality-and-speed breakthroughs. Comparing to the 7.0 anchors: DG-Mesh (7.0) proposes a dual-representation framework for mesh reconstruction, a contribution of comparable depth; the current paper's evidential gaps (ablation restricted to 2 scenes, missing 4DSH hyperparameters) are roughly comparable in severity to DG-Mesh's missing quantitative ablations. The 8.0 anchors (NoPoSplat, Neural SDF Flow, MovingParts) are distinguished by reviewer consensus reflecting no significant unresolved weaknesses; 4DGS falls short of this bar due to the ablation coverage and underspecified 4DSH hyperparameters. The paper lands between 7.0 and 8.0, closer to 7.5: its contribution is larger than the 7.0 papers (the real-time breakthrough is more impactful than mesh reconstruction or GS compression), but the evidential thin spots prevent a clean 8.0.

**Final score: 7.5 — Accept.**

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>