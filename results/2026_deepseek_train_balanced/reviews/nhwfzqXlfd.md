Now I have all the information needed to write the final consolidated review.

---

## Summary

This paper proposes LAST, a 3D human reconstruction framework that integrates a VAE-based Image-to-Point (I2P) model with 3D Gaussian Splatting (3DGS). The core idea is to learn a dependency matrix over latent factors (pose, clothing, lighting) from images and use it to guide 3DGS optimization — replacing pixel-level supervision with latent-factor-level supervision to avoid spurious correlations between visual features. The paper reports state-of-the-art PSNR, SSIM, and LPIPS on ZJU-MoCap and MonoCap datasets.

## Strengths

- **Clear formulation of the spurious correlation problem in 3DGS human reconstruction.** The paper identifies a genuine limitation of pixel-level supervision: image-level gradients entangle visual features that have no causal relationship (e.g., wrinkled clothing co-occurring with body occlusions in athletic poses). This diagnosis is concrete, well-motivated, and goes beyond the standard criticisms in prior 3DGS human reconstruction work.

- **The I2P VAE with latent structure learning is reasonably well-specified.** The VAE framework with exogenous-to-endogenous factor propagation (Eq. 6–7), the dependency matrix A trained with reconstruction, disentanglement (MI), and DAG regularization objectives (Eq. 8–11) — this component of the pipeline is described with sufficient formal detail to be understood and reproduced.

- **State-of-the-art quantitative results on standard benchmarks.** Table 1 reports that LAST outperforms six baselines (NeuralBody, InstantAvatar, AnimatableNeRF, GauHuman, 3DGS-Avatar, HuGS) across all three metrics (PSNR, SSIM, LPIPS) on both ZJU-MoCap and MonoCap datasets. Qualitative results (Figures 2–3) show improved preservation of fine details in challenging cases.

## Weaknesses

### Major

1. **The interface between the I2P model and 3DGS optimization is critically underspecified.** This is the paper's central claimed contribution — using learned latent factors to guide 3DGS optimization — yet the actual mechanism by which this occurs is never concretely explained. The paper states that the decoder's point cloud output "preserves a mapping relationship with 3DGS" (line 146) and that identified regions can be "translate[d] into key Gaussian points of each latent factor" (line 146), but no algorithm, network, or heuristic for this translation is provided. The I2P decoder outputs a point cloud; 3DGS operates on Gaussian primitives with positions, covariances, opacities, and spherical harmonics — these are different representations with different optimization dynamics. The paper does not specify (a) how individual Gaussian primitives are associated with specific latent factors, (b) how the point-cloud comparison identifies factor-specific Gaussian subsets, or (c) how optimizing abstract latent vectors z_p and z_s (Eq. 9–11) translates into concrete updates of Gaussian attributes during 3DGS rendering. Without this specification, the core innovation connecting the I2P model to the 3DGS pipeline is not a method — it is a sketch.

2. **Inconsistent problem framing: "Monocular" title vs. "Multiocular" abstract and multi-view evaluation.** The title reads "Monocular Human Videos," but the abstract opens with "Multiocular human reconstruction aims to create a high-quality 3D human representation from sparse video data." The word "monocular" does not appear in the body text. The evaluation uses ZJU-MoCap and DNA-Rendering, which are multi-view datasets (typically 10–23 cameras). The paper never clarifies how many views are used per subject during evaluation, whether a single view or multiple views are employed, or how this relates to the title's monocular framing. This ambiguity makes it impossible to assess the difficulty of the evaluation setting or compare against methods that specify their input protocol.

3. **No empirical evidence that spurious correlations are actually mitigated.** The paper's entire motivation (lines 12–13) rests on a causal claim: pixel-level supervision causes 3DGS to learn spurious correlations (e.g., body occlusion depending on wrinkled clothing), and LAST fixes this. But the paper provides no diagnostic experiment to demonstrate that: (a) baseline methods actually exhibit this specific spurious correlation, or (b) LAST reduces or eliminates it. The ablation study (Table 2) is referenced in a single sentence (line 207) with no discussion of which components were ablated or what the results showed. All quantitative comparisons are against entire baselines, which conflate many differences. A controlled experiment — e.g., a synthetic case where the spurious correlation is known to exist — would be needed to support the causal framing.

4. **Training data and supervision for the I2P pre-training are not specified.** The paper states the I2P model is "pre-trained on a large human reconstruction dataset" (line 108) but does not name the dataset, specify how ground truth point clouds are obtained (laser scan? SMPL fit? depth sensor?), or report resolution, number of identities, or poses. Without this information, the reader cannot evaluate whether the I2P model's point cloud generation capability generalizes to the evaluation datasets, or whether the dependency matrix learned during pre-training is meaningful.

5. **The LPIPS* values are misinterpreted, undermining confidence in quantitative reporting.** The paper says InstantAvatar "fails on ZJU-Mocap with 68.41 LPIPS*" (line 196). Since LPIPS* = 1000×LPIPS (as defined in line 198), 68.41 corresponds to LPIPS ≈ 0.0684, which is a good perceptual similarity score — not a failure. If this is an error in interpretation, it casts doubt on how the reported metrics are understood and compared. If the comparison is fair, the paper should clarify what constitutes "failure" relative to typical LPIPS ranges for this task.

### Minor

- **No standard deviations or confidence intervals reported.** Most 3DGS-based human reconstruction papers report variance. Table 1 gives only point estimates, making it impossible to assess whether the reported improvements are statistically significant or driven by a few sequences.

- **Ablation study not discussed.** Table 2 is presented as an embedded image without any analysis. The reader cannot assess which components contributed to performance or what was learned from the 377-sequence study. This reduces the ablation to a placeholder rather than evidence.

- **Progressive update strategy's operationalization is ambiguous.** The paper proposes updating parent then child latent factors (Eq. 9–11) with a threshold λ, but it does not specify how this sequential optimization is implemented within the 3DGS rendering loop — e.g., how gradients with respect to "z_p" are backpropagated through the renderer to update only a subset of Gaussian primitives. In standard 3DGS, the rendered image is a function of all Gaussians simultaneously; the paper does not explain how per-factor isolation is achieved.

### Trivial

- The paper uses "multiocular" (line 4) where "multi-view" or "multi-camera" is standard terminology.

## Nice-to-Haves

- Show the learned dependency matrix A for a concrete example and analyze whether the discovered dependencies align with actual physical relationships (e.g., pose→clothing wrinkles). This would directly support the causal framing.
- Report per-sequence results or error bars to establish that improvements are consistent rather than driven by outliers.
- Report training/rendering runtime to show whether the added VAE overhead is practical.
- Clarify whether the method uses monocular or multi-view input during evaluation, and if multi-view, specify how many views and the selection protocol.

## Removed Points

- The Harsh Critic's claim that the progressive update strategy "cannot work as described" because "the rendered image is a function of **all** Gaussian primitives simultaneously" is overstated. In block coordinate descent, one can freeze a subset of parameters while updating others; this is not an architectural impossibility. The real issue is that the paper does not specify *how* factor-specific subsets of Gaussians are identified and isolated, which is already captured in Major weakness #1 and #6. The "cannot work" framing is too strong given what is on the page.
- Criticisms about the absence of theoretical proofs or causal intervention/counterfactual reasoning (e.g., "the dependency matrix is never used for actual causal reasoning") demand scope expansion. The paper claims to be *inspired by* causal structure learning, not to perform formal causal inference. This is a reasonable design choice that does not invalidate the method.
- Strength Finder's claim about the "ablation study on 377 sequences" is removed because it conflicts with the verified weakness that the ablation is not discussed — an unreferenced embedded image does not constitute evidence.
- Strength Finder's claim about "mitigation of spurious correlations" is partially retained in Strengths but the "mitigation" aspect is not treated as a demonstrated strength given the lack of diagnostic evidence (covered in Major weakness #3).
- Criticisms about missing implementation details (number of latent factors, decoder architecture, mask mechanism specifics) are treated as underspecification in Major weakness #1 rather than standalone points.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a clear pattern: the paper has a well-motivated diagnosis of a real problem (spurious correlations in pixel-level 3DGS supervision) and a plausible high-level solution architecture (learn factor dependencies → guide optimization), but falls short in specifying the concrete mechanism connecting the two. The component that makes the core claim operational — the interface between latent factors and Gaussian primitives — is missing from the paper.

## Suggestions

1. Specify concretely how the I2P decoder's point cloud output maps to 3DGS Gaussian primitives. Is there a learned projection? A correspondence by spatial position? A per-factor parameter group? Without this, the method is incomplete.
2. Resolve the monocular vs. multiocular inconsistency. Clarify how many views are used during evaluation and at training time.
3. Add a controlled diagnostic experiment demonstrating the claimed spurious correlation and its mitigation (e.g., a synthetic co-occurrence bias between two unrelated factors).
4. Name the pre-training dataset, describe how ground truth point clouds are obtained, and provide implementation details sufficient for reproducibility.
5. Correct or clarify the LPIPS* interpretation. If 68.41 is a "failure," justify that claim with typical LPIPS ranges for this task.
6. Report standard deviations and discuss the ablation study with numerical results.

## Score and Decision

Based on the above assessment, the paper proposes a well-motivated direction but has a critical gap: the core mechanism connecting the I2P model to 3DGS optimization is not specified, the problem framing is inconsistent, and the causal claims lack empirical support. These are major issues that prevent acceptance in current form. A score reflecting this assessment:

MY FINAL SCORE: <score>3.5</score>
MY FINAL DECISION: <decision>Reject</decision>