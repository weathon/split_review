Now I have a thorough understanding of the paper and can verify each reviewer claim against the actual text. Let me write the final consolidated review.

---

## Summary

This paper proposes Variational Bayes Gaussian Splatting (VBGS), a method that frames Gaussian splatting as variational inference over the parameters of a generative mixture model. By leveraging conjugate priors (Normal-Inverse-Wishart for spatial parameters, Dirichlet for mixture weights), the authors derive closed-form coordinate-ascent variational updates that are order-invariant, enabling continual learning from streamed 2D and 3D data without replay buffers. The method is evaluated on Tiny ImageNet (2D images), Blender objects (3D), and Habitat rooms (3D), comparing against a gradient-based optimization baseline.

## Strengths

1. **Principled variational formulation with closed-form updates** — The paper derives analytical update rules (Equations 7–8) by exploiting the conjugate relationship between NIW/Dirichlet priors and multivariate-Normal/categorical likelihoods. This is technically sound and genuinely enables parameter estimation in a single step per observation, unlike gradient-based methods that require many iterations.

2. **Demonstrated continual learning without replay buffers** — The 2D image experiments (Figure 2b) cleanly show that VBGS maintains consistent reconstruction quality across sequentially observed patches while gradient-based optimization catastrophically forgets. The theoretical justification (Section 3.3) correctly explains that the iterative update is order-invariant and equivalent to batch processing. This is the paper's strongest and most distinctive contribution.

3. **Reasonable static performance when fairly compared** — Under data initialization, VBGS achieves PSNR values comparable to the gradient baseline (Table 1), despite using only a single variational update step. This demonstrates that the variational approach does not sacrifice reconstruction quality for the continual-learning benefit when both methods operate under similar conditions.

## Weaknesses

### Fatal
None.

### Major

1. **"State-of-the-art" claim is unsupported.** The abstract claims VBGS "matches state-of-the-art performance on static datasets." However, the only comparison is against a gradient baseline that is explicitly stripped down: no spherical harmonics beyond degree 0, no adaptive density control, no opacity learning. The gradient baseline itself achieves PSNR values in the 19–25 dB range on Blender (Table 1), whereas the actual 3DGS pipeline (Kerbl et al.) typically achieves >30 dB on the same dataset. Comparing against this simplified baseline and calling the result "state-of-the-art" is misleading. The paper's actual experiments fairly compare VBGS against a matched simplified gradient baseline, and the conclusions should be reframed to reflect this. (Section 4's "Gradient" description confirms the simplifications on lines 248–249.)

2. **The 3D rendering pipeline is critically underspecified.** The paper states (line 158): "For 3D rendering, we use the renderer from [Kerbl et al.], where the spatial component is first projected onto the image plane using the camera parameters, and the estimated depth is used to deal with occlusion." The VBGS generative model (Figure 1) does not include an opacity parameter — a required input for the 3DGS renderer's alpha-blending pipeline. The paper does not specify how the VBGS posterior parameters (NIW over spatial parameters, Normal over color mean with fixed covariance) are mapped to the renderer's expected inputs (opacity, anisotropic covariance, color). Without this specification, the 3D reconstruction results (Table 1, Figures 4–6) are unverifiable. This gap must be resolved for the 3D experiments to be interpretable.

### Minor

1. **Continual learning comparisons lack practical baselines.** The gradient baseline in the continual setting (100 gradient steps per frame, no replay buffer) demonstrates catastrophic forgetting, which is well-understood behavior. While this is an appropriate baseline for showing VBGS's order-invariance property, the paper positions the continual learning results as a practical advantage (abstract: "drastically improving performance in this setting"). Adding a gradient-based method with a replay buffer of reasonable size would provide a more informative comparison and strengthen the practical claims. The paper cites SplaTAM and related work that uses replay buffers (line 43) but does not compare against them.

2. **No analysis of the component-reassignment heuristic.** Section 3.4 describes a heuristic that replaces unused components' means with data points sampled proportional to negative ELBO, using a 5% fraction parameter. This heuristic substantially improves Habitat room results (Figure 6b), but the paper provides no ablation: no sensitivity analysis on the fraction parameter, no comparison against simpler alternatives (e.g., k-means initialization or periodic reassignment), and no variant without reassignment on the Blender dataset. Given its apparent importance, this deserves more scrutiny.

3. **Fixed-assignment design choice is not discussed.** Assignments are computed once against the initial posterior and never updated (line 203). This guarantees order-invariance but may limit final model quality. The paper does not compare against an alternative where assignments are recomputed periodically, which might improve quality while still largely avoiding forgetting. The trade-off is not discussed.

4. **Limited expressiveness relative to full 3DGS is inadequately acknowledged.** The VBGS color model is a fixed-covariance isotropic Gaussian with no view-dependence and no opacity. The conclusion briefly mentions that 3DGS "dynamically adjusts the model size" (line 373) but does not discuss the opacity or view-dependence limitations. While the gradient baseline shares the same limitations (no spherical harmonics), the paper's title and framing position VBGS as an alternative to 3DGS, making this gap worth more explicit discussion.

### Trivial
- The continual 3D learning results (line 332) report an "average reconstruction error" of 11.19 dB for VBGS vs. 21.26 dB for Gradient. If these are PSNR values, the interpretation contradicts the text ("the same properties from the 2D experiment hold"). If they are MSE values in dB where lower is better, this should be clarified to avoid ambiguity.

## Nice-to-Haves
- **Uncertainty visualization**: The paper claims a variational posterior over parameters as an advantage but never visualizes or uses this uncertainty (e.g., confidence intervals on renders, active learning). A simple demonstration would strengthen the motivation.
- **Per-component quality analysis**: The paper uses 100K components throughout — analyzing how many are actually active after training would help understand model efficiency.

## Removed Points

These points were raised by reviewers but removed or downgraded after verification against the paper:

- **"Time comparison conflates steps"** (removed): The reviewer claimed the wall-clock comparison (0.03s vs 0.05s) conflates steps, but the paper explicitly states it measures "the wall-clock time required for the Gradient approach to reach the performance level of VBGS after a single update step" (line 271). This is a time-to-target-quality comparison, not a per-step comparison, and is appropriately framed.
- **"Straw-man continual baseline"** (downgraded to Minor): The gradient baseline without replay is the correct baseline to demonstrate VBGS's order-invariance property. The paper's claim is specifically about not *needing* replay buffers; comparing against gradient-without-replay is the appropriate experiment. However, the paper would be stronger with a replay-buffer comparison, hence this remains as Minor point #1.
- **"Catastrophic forgetting is inevitable"** (removed): This is an editorial comment rather than a verifiable weakness about the paper.
- **"Missing related works"** (removed per instructions): Not verifiable without external sources.

## Novel Insights

The most interesting observation that emerges from the reviews is that VBGS's fixed-assignment design (computing assignments once against the initial posterior and never updating them) is simultaneously its greatest strength and most significant limitation. It guarantees order-invariance and enables the continual learning property, but it also means assignments cannot benefit from improved component estimates over time. The paper treats this as a design given without analyzing the trade-off. An interesting extension would be to compare periodic full-batch recomputation of assignments (which would still avoid forgetting since it uses all data) against the current fixed-assignment strategy. This could reveal whether the cost of order-invariance is meaningful in practice.

## Suggestions

1. **Reframe the contribution honestly.** Replace "matches state-of-the-art" in the abstract and throughout with something like "achieves competitive performance against a matched gradient baseline" or focus the claims on the continual learning contribution. The paper's real strength is the variational framework for streaming updates, not static SOTA parity.

2. **Specify the rendering pipeline completely.** Describe exactly how VBGS posterior parameters are converted to the 3DGS renderer's expected inputs (opacity, covariance, color). If opacity is omitted or set to a constant value, state this explicitly. Without this, the 3D results are unverifiable.

3. **Add a replay-buffer baseline** for the continual 3D experiments. Even a simple buffer of 10–20 recent frames with the gradient method would substantially strengthen the practical claims.

4. **Run an ablation of the reassignment heuristic.** Show performance with and without reassignment across all datasets, and analyze sensitivity to the fraction parameter and the "unused component" criterion.

## Score and Decision

The paper's core idea — variational inference with conjugate priors for Gaussian splatting with closed-form, order-invariant updates — is principled and addresses a real limitation of gradient-based methods. The 2D continual learning experiments are clean and compelling. However, the paper has two significant issues that must be addressed: (1) the unsupported "state-of-the-art" overclaim in the abstract, and (2) the critically underspecified 3D rendering pipeline (the opacity gap makes the 3D results unverifiable in their current form). The latter is the more serious problem because it affects the core 3D evaluation that constitutes a substantial portion of the experimental results.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>