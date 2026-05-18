Now I have a thorough understanding of both the paper and the reviews. Let me synthesize the final consolidated review.

---

## Summary

This paper proposes ACDC (Autoregressive Coherent multimodal generation with Diffusion Correction), a zero-shot inference-time method that combines pre-trained autoregressive models (ARMs) and diffusion models (DMs) via SDEdit, augmented by an LLM-based memory module that summarizes past prompts to preserve global context. ACDC is architecture-agnostic and requires no fine-tuning. It is evaluated on coherent multi-frame story generation (using Show-o and Unified-IO-2 as ARMs, Stable Diffusion as DM) and autoregressive video generation (using LWM as ARM, AnimateDiff as DM), showing consistent improvements in frame consistency, CLIP similarity, subject/background consistency, and aesthetic quality.

## Strengths

1. **Zero-shot, architecture-agnostic combination of ARMs and DMs without fine-tuning.** ACDC is the first method to pair pre-trained ARMs and DMs at inference time with no additional training or architectural modifications. This is validated across three distinct ARM designs (Show-o's discrete diffusion, Unified-IO-2's raster-scan, LWM's causal generation) and two DM types (image DM and video DM), with the paper explicitly noting other DM choices (e.g., DeepFloyd IF) are compatible "without any modifications to the algorithm" (Sec. 4.1). This contrasts with prior work like SEED-X, Pandora, or Mini-Gemini that require modality-specific fine-tuning or architectural adapters.

2. **Consistent and substantial quantitative improvements across multiple metrics.** In story generation (Table 1), Show-o + ACDC improves frame consistency by +10.4%, CLIP similarity by +7.16%, ImageReward by +0.574, and FID by –7.34%. Unified-IO-2 + ACDC reduces FID by –16.1%. In video generation (Table 3), LWM + ACDC improves subject consistency by +3.43%, background consistency by +1.45%, aesthetic quality by +7.33%, and motion smoothness by +0.23%, all while maintaining dynamic degree. Critically, the improvements on non-FID metrics (frame consistency, CLIP similarity, ImageReward, subject consistency, background consistency, aesthetic quality) are all methodologically sound and independently support the paper's claims.

3. **The LLM memory module is shown to be critical for preserving global context.** The ablation study (Table 2) demonstrates that removing the LLM memory module causes frame consistency to drop from 0.853 to 0.835 and CLIP similarity to fall from 30.85 to 29.43, while FID degrades. A compelling visual example (Fig. 3) shows that without memory, the DM loses track of the character's identity ("His" → "Benny, the golden retriever"). This directly validates the design choice of using an LLM to distill global context into the DM's local conditioning.

4. **Demonstrated reduction of error propagation through ablation on corrected frame count.** Table 2's ablation (ACDC #2, #4, #6) shows that applying correction to more frames monotonically improves CLIP similarity (28.58 → 28.79 → 30.85) and FID (109.6 → 107.6 → 101.4), directly supporting the claim that correction reduces error accumulation over sequence length rather than merely providing a uniform uplift.

5. **Incorporation of additional user-specified physical constraints as an extension.** The paper demonstrates that ACDC's framework naturally extends to correcting physical implausibilities (e.g., three-eared rabbits, multiple moons) via DM-based inpainting (Fig. 5), showcasing the versatility of the approach beyond artifact correction.

## Weaknesses

### Fatal
None.

### Major

1. **The FID metric in story generation uses SDXL-lightning generations as pseudo-ground truth, not real images.** Section 4.1 states: "To compute FID against in-distribution images, we generate pseudo-ground truth images using SDXL-lightning with 6 NFE." FID is designed to measure distributional distance to a real data distribution; substituting another generative model's output conflates distributional fidelity with stylistic similarity to a particular reference model. The paper acknowledges this ("Although the FID score lags behind SD v1.5, this can be partly attributed to the fact that we consider SDXL-generated images as ground truth") but does not mitigate it. **Why this matters:** While the relative comparison between baselines using the same reference is internally consistent, the absolute FID values cannot be interpreted as quality relative to real data, and the metric introduces an uncontrolled bias toward outputs stylistically similar to SDXL-lightning. **However, this does not undermine the paper's core claims** because the other three metrics (frame consistency, CLIP similarity, ImageReward) are methodologically sound and all show consistent improvements. The paper should either replace or supplement this FID evaluation with a metric that does not depend on a reference generative model (e.g., human evaluation, real-image FID from a curated in-distribution dataset, or a perceptual metric like LPIPS comparing ACDC output to original ARM output to measure improvement direction).

### Minor

1. **The video experiment tests the pipeline as a whole but does not isolate whether the improvement comes from the specific diffusion correction mechanism versus simply having better conditioning input.** The experiment (Sec. 4.2) compares LWM generating all 32 frames directly against LWM generating 16 frames + ACDC correction + generating remaining 16 frames. The baseline LWM (all 32 frames) receives no equivalent conditioning improvement. While the paper's claim is about the complete pipeline — which is legitimately tested as-is — an ablation that conditions LWM on frames enhanced by a non-diffusion process (e.g., sharpening, denoising) would strengthen confidence that the diffusion correction specifically drives the improvement and not merely better conditioning.

2. **The claim about mitigating exponential error accumulation would benefit from direct per-frame degradation measurement over sequence length.** The paper argues that ACDC reduces error accumulation, and the strongest evidence for this is the ablation on the number of corrected frames (Table 2) and qualitative results (Fig. 6). However, plotting a per-frame metric (e.g., frame consistency or CLIP similarity as a function of frame index) for ACDC vs. baseline would more directly demonstrate the reduction in error *growth* with sequence length, as opposed to merely a uniform quality uplift. The current aggregated metrics could partially reflect the latter.

3. **The system/user prompt for the LLM memory module is not disclosed.** The paper mentions "the system/user prompt ρ for the memory module" (Sec. 3) but does not provide its content. This is a reproducibility concern, as the prompt design may significantly influence the module's behavior.

4. **The ablation study for the memory module is conducted on 100 test stories.** While the results are informative and the trends are clear, conducting the ablation at a larger scale would increase statistical confidence in the observed margins.

### Trivial

- The paper's use of "Theorem 1" (line 114) is referenced but stated to be in the appendix; this is standard practice and not a flaw in the submitted paper (the appendix exists in the original submission).
- The physical constraints section (inpainting) is purely qualitative. This is acceptable for an additional capability demonstration, and the paper does not present it as a core contribution.

## Nice-to-Haves

- A sensitivity analysis for the SDEdit noise level \(t'\) (reported as 0.4–0.6 range) showing the trade-off between content preservation and artifact removal across different tasks.
- A discussion of computational cost / runtime, since the pipeline runs an ARM, a DM, and an LLM sequentially.
- A stronger evaluation of the error-accumulation reduction claim via per-frame metric plots over sequence index.

## Removed Points
These points are flagged to be removed; treat them with caution.

- **Criticism about Theorem 1 missing from the main text:** The paper states the theorem is in the appendix. The instructions confirm the appendix exists in the original submission. Per policy, this criticism is removed.
- **Criticism that the video experiment "conflates two things" and cannot attribute improvement to ACDC:** The experiment tests the complete ACDC pipeline as claimed — the paper never claims to isolate a sub-mechanism. The test is valid for the pipeline-level claim. The more precise concern (lack of a non-diffusion conditioning control) is preserved in Minor #1 above as a reasonable suggestion, not a structural flaw.
- **Strength Finder item about physical constraints being a core strength:** This is a minor additional capability, not a core contribution. Downgraded to a supporting strength.
- **Generic Strength Finder statement about "addressing an important problem":** This is too generic and lacks specific content. Removed.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface an insight that the paper itself does not already articulate.

## Suggestions

1. **Replace or supplement the FID metric** in story generation with a metric that does not depend on a reference generative model. A human evaluation study (e.g., pairwise preference between ARM output and ACDC output) or a perceptual metric like LPIPS measured against the original ARM output would be credible alternatives. As a lower-effort fix, or if a real-image FID from a curated in-distribution dataset is feasible, that would be even stronger.

2. **Add a per-frame degradation plot** for the video experiment (and ideally for story generation as well) showing metric values as a function of frame index for baseline vs. ACDC. This would directly demonstrate whether the *growth* of errors with sequence length is reduced, which is the paper's central mechanistic claim.

3. **Disclose the LLM memory module's system/user prompt** in the main text, appendix, or supplementary material for full reproducibility.

4. **Add a conditioning control ablation** in the video experiment (e.g., applying a non-diffusion enhancement to the first 16 frames before passing them to the ARM) to help isolate the specific benefit of the diffusion correction mechanism.

## Score and Decision

The paper presents a genuinely useful, practical method for combining pre-trained ARMs and DMs in a zero-shot manner, supported by consistent improvements across multiple sound metrics and two distinct tasks. The primary weakness — the FID metric's reliance on pseudo-ground truth from another generative model — is acknowledged by the authors and does not affect the other three metrics in story generation, all of which independently support the conclusion. The minor concerns about per-frame analysis and prompt disclosure are addressable. Overall, the contribution is solid and the evaluation is largely sound.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>