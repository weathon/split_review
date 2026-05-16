Now I have a thorough understanding of the paper and can verify the reviewer claims against the actual content. Let me compile my final consolidated review.

## Summary

NeRM introduces a two-stage generative framework for human motion synthesis that first learns variational implicit neural representations (INRs) of motion clips at their native framerates, then trains a diffusion model on the resulting latent codes. The key insight is to represent motion as a continuous function over temporal coordinates, decoupling the representation from discrete framerate and duration. This enables training on mixed-framerate datasets (e.g., 20–250 fps in HumanML3D) without downsampling or discarding data, and supports high-framerate motion generation without prohibitive memory cost.

## Strengths

1. **Training on native-framerate data demonstrably improves generation quality.** The paper directly validates its central claim: NeRM trained on native framerates achieves FID 0.024 on HumanML3D text-to-motion, substantially outperforming its own fixed-framerate variant (FID 0.034) and the best baseline MLD (FID 0.40). The "Fairness discussion" (lines 151) cleanly separates the benefit of raw data usage from the benefit of the architecture itself. This is the paper's strongest piece of evidence.

2. **High-framerate motion synthesis without interpolation artifacts.** Table 2 shows NeRM achieving clip-FID of 0.025 (50 fps), 0.031 (100 fps), and 0.048 (250 fps) on HumanML3D, while interpolation-based baselines degrade sharply (MLD: 0.128, 0.361, 0.594). Figure 4b provides qualitative corroboration: NeRM's high-framerate output avoids the foot-sliding artifacts that appear when baselines upsample via spherical linear interpolation.

3. **Variational INR formulation creates a smooth latent space for diffusion.** Unlike prior INR-based motion models (NeMF) that overfit deterministic codes, NeRM treats each latent as a normal distribution (Section 3.1). The benefit is empirically validated in unconditional generation (Figure 5): NeRM achieves FID 0.044 and Diversity 9.765 on AMASS versus NeMF's FID 0.7 and Diversity 8.860.

4. **Codebook-Coordinate Attention (CCA) enriches coordinate embeddings.** The fixed-framerate variant of NeRM (FID 0.034) outperforms all baselines including MLD (FID 0.40), suggesting that CCA and the latent diffusion framework contribute beyond the multi-framerate advantage. The paper motivates CCA by noting Fourier features alone are empirically insufficient (Section 3.1).

## Weaknesses

### Fatal
None.

### Major

1. **Missing ablations for core design choices.** Three key components are introduced without independent justification:
   - **Variational vs. deterministic latents**: The paper argues variational formulation enables smooth latent interpolation, but provides no experiment showing this matters for generation quality or diversity.
   - **Codebook-Coordinate Attention (CCA)**: No ablation compares "decoder with Fourier features only" vs. "decoder with CCA" (or a simpler alternative). The fixed-framerate NeRM outperforms MLD, but this conflates CCA with other differences (latent diffusion, transformer architecture). A direct CCA vs. no-CCA comparison is needed to attribute the improvement.
   - **Progressive training**: The two-phase training (fixed framerate first, then multi-framerate) is described (lines 102) without any analysis showing it outperforms multi-framerate training from scratch.
   
   These are standard expectations for a method paper. Their absence makes it unclear which design choices drive performance.

### Minor

2. **The "arbitrary framerate" claim is overstated given the evidence.** The paper uses "arbitrary framerate" and "any-framerate" in the abstract and introduction, but evaluation in Table 2 only tests framerates within the training distribution (50, 100, 250 fps, all within the 20–250 fps training range). The paper would be strengthened by testing extrapolation to unseen framerates (e.g., 500 fps or intermediate values like 75 fps). The method's continuous formulation *should* support this, but no evidence is provided.

3. **clip-FID is underspecified and unvalidated.** As the metric central to the high-framerate evaluation (Table 2), clip-FID is described in only ~4 sentences (lines 145). Key details are missing: (a) what feature extractor is used for FID computation on motion clips; (b) the clip size *m* and number of sampled clips; (c) whether the metric correlates with human perception of detail quality. A simple sanity check—computing clip-FID between real motions at different framerates to establish a reference range—would help calibrate the numbers in Table 2.

4. **Efficiency and memory claims are asserted without measurement.** The abstract claims NeRM is "memory-friendly" and "highly efficient even when generating high-framerate motions." No runtime, GPU memory, throughput, or parameter count numbers are reported. The conceptual argument (INRs decouple memory from resolution) is reasonable, but the paper makes specific empirical claims without supporting data.

5. **Implementation details are insufficient for reproduction.** The decoder *f_θ* architecture (number of layers, hidden dimension, activation functions) is not described. Latent code dimensionality is not given. Codebook size *N* and dimension *d* are named but not specified, nor is the pretraining procedure for the codebook. These details may exist in a supplementary appendix (which the parser strips), but the main text alone is not self-contained.

### Trivial
None.

## Nice-to-Haves

- **Root trajectory handling at high framerates**: The paper does not discuss how root velocity accumulation is handled when generating at high framerates, where drift could be a concern. A discussion or simple evaluation would help.
- **Long-sequence generation**: The model generates clips of fixed size *m*; how full sequences beyond this size are produced (stitching, sliding window, or direct full-sequence decoding) is not addressed.
- **Confidence intervals on unconditional results**: Figure 5 (bar chart) would benefit from error bars for the unconditional generation metrics.

## Removed Points

These points were raised by reviewers but are removed per guidelines:

1. **Criticism about missing newer baselines (MotionGPT, ReMoDiffuse, LODGE).** Per instruction: missing related works should not be mentioned as a weakness since external verification is unavailable.

2. **Complaint that Figure 2 is "not explained in the text."** The paper explicitly references Figure 2 in lines 40 and 46 with a caption explaining the two-stage pipeline. This is standard for a method figure.

3. **The claim that certain test framerates (30, 60, 120, 240 fps) are evaluated.** The actual tested framerates from the paper's discussion are 50, 100, 250 fps. The reviewer's specific numbers are inaccurate, though the broader point (all tested framerates are within training distribution) stands.

4. **Complaint about "long sequences beyond clip size" not being addressed.** The continuous motion field formulation inherently supports querying at arbitrary time points; the clip-based training is a training strategy, not a constraint on inference.

## Novel Insights

The reviews surface one tension not fully explored in the paper: the method's strongest result (native-framerate training beating fixed-framerate training in Table 1) cleanly validates the core thesis, but the mechanism behind this improvement is underspecified. Is the improvement driven by (a) simply having more training data (frames not discarded), (b) the continuous inductive bias of INRs, or (c) the specific architecture choices (CCA, variational latents)? The fixed vs. native comparison supports (a) + (b), but without ablations the paper cannot separate them or attribute to (c). The reviews correctly identify this as the paper's central methodological gap.

## Suggestions

1. **Add three targeted ablations**: (i) variational vs. deterministic latents on the unconditional generation task; (ii) decoder with Fourier features only vs. decoder with CCA; (iii) progressive training vs. multi-framerate training from scratch. Report FID for each.

2. **Report efficiency numbers**: GPU memory (peak training and inference) and inference time (ms per frame) for NeRM vs. at least MLD at 20, 100, and 250 fps.

3. **Validate clip-FID**: Specify the feature extractor, clip size, and sampling procedure. Compute clip-FID between real motions at different framerates (e.g., real 20 fps vs. real 120 fps) to establish the metric's behavior.

4. **Test framerate extrapolation**: Generate motions at one unseen framerate above the training range (e.g., 500 fps on HumanML3D) and report clip-FID with qualitative inspection.

5. **Provide architecture details** (decoder layers/hidden dims, latent dimension, codebook N/d, pretraining objective) either in main text or an appendix that will not be stripped.

## Score and Decision

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>