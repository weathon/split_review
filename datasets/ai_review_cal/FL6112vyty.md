- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5, 5
I have all the information I need. Let me now produce the consolidated review.

---

## Summary

DirectTriGS proposes a triplane representation for Gaussian Splatting (GS) to enable direct 3D generation without 2D-lifting. The pipeline consists of: (1) encoding objects into triplanes via a differentiable TriRenderer that decodes triplanes to GS point clouds with only 2D supervision, (2) compressing triplanes through a VAE, (3) two-stage latent diffusion for text-to-3D generation, and (4) an optional SDS refiner. The core idea — representing the irregular, multi-channel GS point cloud as a continuous image-like triplane field — is well-motivated and addresses a genuine challenge in 3D GS generation.

---

## Strengths

- **Novel triplane encoding for GS that is interpretable and learnable**: The paper visualizes triplane channels (Fig. 4), showing clear object shapes from three orthogonal views, providing direct evidence that the representation captures geometry and appearance in a continuous field suitable for convolution-based processing. The separate encoding of geometry and GS attribute channels (line 42) is a reasonable design for convergence.

- **Fully differentiable TriRenderer trained with 2D supervision only**: The TriRenderer (Sec. 4.2) combines a deformable SDF geometry branch, FlexiCubes mesh extraction, surface sampling, and a GS attribute branch into an end-to-end differentiable pipeline. Joint training with rendering losses (Eq. 3–8) and a two-stage training strategy (small batch to train the shared renderer, then frozen renderer for all objects) enables scaling to large datasets without per-object GS pretraining — a practical advance.

- **Concrete efficiency advantage over SDS-based methods**: The paper reports inference time (Table 4) and notes direct generation completes in under a minute versus SDS methods taking 10+ minutes (Sec. 4). This is a tangible practical strength for deployment.

- **Qualitative results show sharp geometry and rendering**: The generated samples in Fig. 6 and Fig. 7 demonstrate visually plausible objects with better sharpness than the NeRF-based baselines (Shap-E, Direct3D), supporting the value of the GS representation.

---

## Weaknesses

### Fatal
None.

### Major

- **Incomplete quantitative comparison with the closest competitor (GaussianCube)**: GaussianCube (Zhang et al., 2024) is the most directly related prior work on direct 3D GS generation, yet the paper explicitly limits this to a "qualitative comparison" (line 164: "Additionally, we provide a qualitative comparison with GaussianCube"). The quantitative results (Tables 1, 2) compare against Shap-E and Direct3D — both NeRF-based and arguably weaker baselines for GS generation. Since the paper's core claim is producing high-quality GS generation, the lack of a multi-metric quantitative comparison (CLIP scores, user study, rendering metrics) against the state-of-the-art method in the same representation class is a significant evidential gap. This weakens the claim that DirectTriGS "outperforms" or is "competitive" with existing direct GS generators.

- **Ablation study does not isolate the paper's own design choices**: The ablation section (Sec. 5.4) tests (1) 3D diffusion on voxel-based GS and (2) direct triplane diffusion without VAE. Both fail, which the paper presents as evidence for the pipeline. However, these are tests of completely different approaches, not ablations of the *proposed method's components*. Genuinely informative ablations would include: (a) training the TriRenderer without the geometry branch (decoding GS attributes directly from triplane), (b) single-stage vs. two-stage diffusion on the latent, (c) varying triplane resolution or channel count, (d) allowing free (non-surface-bound) GS points. Without these, the contribution of each component — deformable SDF, surface sampling, decoupled geometry/appearance branches, two-stage generation — is unsubstantiated.

- **Surface-binding of GS points is a strong assumption left unanalyzed**: The method binds every splat to be flat (s₃ fixed to near-zero), axis-aligned to its associated mesh triangle, and located on the surface (Sec. 4.2). This is a significant departure from standard 3D GS, where Gaussians can be arbitrarily oriented, elongated, and positioned anywhere in the volume. The paper provides no analysis of how this restriction affects expressiveness — e.g., whether it prevents capturing fine geometric details, semi-transparency, glossy reflections, or volumetric effects that benefit from off-surface or non-flat splats. A comparison against a version with free GS points (e.g., predicting offsets from the surface) is needed to validate this design choice.

### Minor

- **Scalability cost of the preprocessing pipeline is not discussed**: Fitting triplanes for 200K objects at ~30 seconds each (line 150) translates to >1,600 GPU-hours of preprocessing before any generative model is trained. The paper presents this as a fixed cost but provides no comparison with the preprocessing or training costs of alternatives (e.g., GaussianCube, feed-forward predictors). For a framework aiming to make GS generation practical, this overhead deserves acknowledgment and justification.

- **No analysis of failure cases or generation diversity**: The paper shows only successful samples and does not discuss typical failure modes (e.g., thin structures, texture blur, geometric artifacts). It also shows only single samples per prompt, with no analysis of generation diversity or mode coverage (e.g., whether the model memorizes training examples).

- **No confidence intervals or statistical significance for quantitative results**: The user study scores (Tables 1, 3) and CLIP scores (Table 2) are reported as single numbers with no variance or significance tests. The tables are embedded as images so the precise formatting cannot be verified, but the text describes only "average results" (line 168), making it impossible to assess whether differences between methods are statistically meaningful.

- **View-dependent surface sampling during training is not fully reconciled with a view-independent representation**: The TriRenderer samples "only faces oriented toward the camera" (line 60) during training to reduce computation. However, the triplane is intended to be a view-independent 3D representation. The paper does not explain how the view-dependent sampling at training time affects the final triplane encoding or how this is resolved at generation time when a complete 3D asset must be produced.

### Trivial
- Minor formatting issues (e.g., garbled caption in Fig. 6 at line 164: "Zhang et al.3" truncation) are parser artifacts and not author errors.

---

## Nice-to-Haves
- A quantitative reconstruction metric (PSNR, SSIM, LPIPS) for the triplane fitting and VAE reconstruction steps would help quantify information loss in the pipeline.
- A comparison of single-stage vs. two-stage latent diffusion would validate the claimed benefit of staged generation.
- Reporting the number of GS points per object and how the surface sampling density is determined would help understand the method's behavior.
- Geometry-only metrics (Chamfer distance, F-score) on Objaverse ground truth meshes would help separate geometry quality from appearance quality in the evaluation.

---

## Removed Points

These points from the reviewers are flagged for removal:
- **"Garbled numbers in user study"** — The tables are embedded as images that the PDF parser could not extract. The original submission contains properly formatted tables; this is a parsing artifact, not an author error.
- **"Missing appendix/reproducibility details"** — Architecture specifications, diffusion schedules, and other implementation details are presumed present in the original appendix, which the parser strips from all papers.
- **"How does CLIP score or user preference compare to a single-stage diffusion?"** — This is a fair experimental question but framed as an absolute weakness; it belongs in nice-to-haves, not in weaknesses.
- **"Why use a mesh at all?"** — The paper explains that surface sampling is designed to produce GS points bound to the surface (line 52: "GS pointcloud is generally gathered on the surface of objects"). This is a stated design choice, not an omission.
- **"Related work description of GaussianCube is too brief"** — This is a scope opinion; the paper covers the key distinction (optimal transport vs. triplane) adequately for context.
- **Generic formatting/style nitpicks** about capitalization, whitespace, line breaks — these are parser errors, not author errors.

---

## Novel Insights

None beyond the paper's own contributions. The reviews largely restate and critique what is already present in the paper rather than uncovering unexpected patterns or observations.

---

## Suggestions

1. **Add a direct, multi-metric quantitative comparison with GaussianCube** on a common subset of Objaverse. Report CLIP scores, user study results, and rendering metrics (e.g., FID of rendered views if available). If GaussianCube's code or outputs are not available for your evaluation setup, state this limitation explicitly and frame your claims accordingly.

2. **Replace the current "ablation" section with true component-level ablations** that isolate your own design choices. At minimum: (a) remove the geometry branch and decode GS attributes directly from triplane, (b) replace two-stage diffusion with joint diffusion on full latents, (c) vary triplane resolution, (d) compare surface-bound GS points against a version allowing free GS points with predicted offsets.

3. **Analyze the surface-binding assumption** by quantifying its impact on rendering quality for objects with challenging properties (thin structures, reflective surfaces, volumetric effects). If it causes no degradation, show this; if it does, document the trade-off.

4. **Report confidence intervals or standard deviations** for all quantitative metrics and state the number of independent trials or seeds used.

5. **Include a failure case analysis** to establish the method's limitations and inform future work.

---
