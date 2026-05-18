Now I have a thorough understanding of the paper. Let me write the consolidated review.

## Summary

This paper introduces Video Active Perception (VAP), a training-free method for long-form video QA that uses a text-conditioned video diffusion model (CogVideoX) as a prior to guide frame selection. The core idea is to generate expected video latents from initial frames + question text, encode all real frames into the same latent space via a 3D VAE, and select the real frames that diverge most from the generated expectations (the "most surprising" frames) for VLM inference. VAP achieves strong zero-shot results on EgoSchema (68.1%), NExT-QA (81.4%), ActivityNet-QA (64.6%), and CLEVRER (40.5%), and is shown to work across GPT-4o, Gemini 1.5, and LLaVA-OV families. The efficiency claim (up to 5.6×) is measured in terms of frames per question fed to the VLM.

## Strengths

- **Novel framing of frame selection as active perception.** The paper draws a clean connection between active perception theory (Bajcsy et al.) and frame selection for VLMs, treating the video diffusion model as a prior world knowledge model and selecting frames that maximally diverge from expectations. This provides a principled, well-motivated alternative to heuristic-based selection.

- **Strong empirical results across multiple benchmarks and VLM families.** VAP achieves the best reported zero-shot accuracy on EgoSchema (68.1%), NExT-QA (81.4%), and CLEVRER (40.5%), and competitive results on ActivityNet-QA (64.6%). The gains are consistent across three VLM families (GPT-4o, Gemini 1.5, LLaVA-OV), demonstrating VLM-agnostic applicability. The comparison against standard VLMs at their default sampling rates (e.g., 180 frames on EgoSchema) shows that VAP's 32 selected frames yield better accuracy — a concrete benefit.

- **Clear advantage over caption-based methods on visual reasoning tasks.** On CLEVRER's explanatory and counterfactual subtasks, VAP achieves 154.0% and 71.43% relative gains over VideoTree. This is attributed to using visual frames directly rather than captions, which is a genuine methodological advantage validated by the results.

- **Ablation studies on frame counts.** Tables 2 and 3 systematically explore sensitivity to both the number of selected frames (6 to 48) and initial frames (6 to 90), showing that performance plateaus at 32 frames. This provides practical guidance and suggests that VAP is not overly sensitive to hyperparameter choice.

## Weaknesses

### Fatal

None.

### Major

- **No equal-frame-budget comparison against simple baselines (random/uniform selection).** The paper compares VAP (32 frames) against standard VLMs using many more frames (180, 44, 90), which confounds selection strategy with frame count. The central claim that VAP's selection strategy is responsible for the gains requires a controlled experiment: given the same budget of 32 frames, how does VAP compare against uniform sampling of 32 frames, random selection of 32 frames, or simple heuristics (e.g., motion-based selection)? The paper mentions Figure 3 comparing against other frame-selection methods at matched counts, but the most basic baselines (uniform/random at the same budget) are absent. Without this, one cannot attribute the improvement to the selection mechanism rather than simply to using fewer frames (which may reduce noise).

- **Efficiency claim lacks total compute accounting.** The efficiency metric ("frames per question") is well-defined and repeatedly qualified, but the paper's framing in the title ("Efficient Inference-Time"), abstract, and introduction creates the impression of end-to-end efficiency gains. In reality, VAP must: (a) encode all T real frames through the 3D VAE encoder, (b) run 50 diffusion denoising steps on initial latents, and (c) run RIFE interpolation — all before the VLM sees a single frame. Algorithm 1 shows that Step 3 encodes *all* real frames \(h_{1:T}\). For a 3-minute video at 30 fps, that's 5,400 frames through a neural encoder. No wall-clock time, FLOPs, or API cost comparison is provided. The comparison against standard VLMs also preprocesses all frames (via 1 fps uniform sampling and frame extraction), so the question is the *relative overhead*, but the paper does not quantify this. The efficiency contribution would be much stronger with a total-cost comparison.

- **No validation of the generation model's output quality.** The method's core mechanism assumes that the text-conditioned diffusion model (CogVideoX) generates meaningful latents for unseen frames, such that the cosine-similarity between real and generated latents is a useful signal for frame relevance. The paper provides no evidence for this: no reconstruction metrics, no comparison between generated and ground-truth latents, no human evaluation. The qualitative examples in Figure 4 are illustrative but post-hoc. If the generated latents are poor (or nearly uniform), the cosine-similarity signal could be arbitrary, even if the end-to-end results happen to work. A simple diagnostic (e.g., do generated latents of held-out frames correlate with real latents?) would significantly strengthen the paper.

### Minor

- **"Lightweight" characterization of CogVideoX is misleading.** The paper repeatedly calls the generation model "lightweight" (abstract, Section 2, Section 4) but simultaneously describes CogVideoX as a "large-scale diffusion transformer" (Section 2.1, line 47). CogVideoX has billions of parameters and requires substantial GPU memory. The RIFE interpolation step is separately called "light-weighted," but the generation model overall is not lightweight by any standard definition. This inconsistency undercuts the efficiency narrative.

- **SOTA claims would benefit from direct leaderboard comparisons.** The paper claims "state-of-the-art zero-shot results" on EgoSchema (68.1%) but does not cite specific numbers from the EgoSchema leaderboard for comparison. Similarly, the claim about ActivityNet-QA ("state-of-the-art VideoTree results of 64.6%") is ambiguous — is VAP SOTA among zero-shot methods, or just better than VideoTree? Providing concrete numbers from comparable methods would make the claim self-contained.

- **Inconsistent VLM backbones across baselines.** The paper evaluates VAP on GPT-4o, Gemini, and LLaVA-OV, but baseline methods (VideoAgent, VideoTree, IG-VLM, LVNet) use their own backbones. For example, VideoTree was only re-implemented on CLEVRER (line 117). This means cross-method comparisons in Table 1 may partly reflect the choice of VLM rather than the frame-selection strategy. Holding the VLM backbone constant in at least one comparison would strengthen the evidence.

- **Generation quality is not ablated.** The paper does not test what happens when CogVideoX is replaced with a simpler interpolant (e.g., direct latent interpolation without the diffusion model) or when the diffusion-generated latents are replaced with random noise. Such ablations would help determine whether the specific generative prior matters, or whether any differentiable distance metric would suffice.

### Trivial

- Line 12 has a garbled LaTeX rendering issue ("S2,000...") — this is a parser artifact, not the authors' fault, but worth noting for the camera-ready version.
- Line 70: "surprsing" → "surprising."
- Line 228: "successfull" → "successful."

## Nice-to-Haves

- Provide a wall-clock time comparison (or FLOP estimate) for VAP's full pipeline vs. standard VLM inference at comparable accuracy levels.
- Test VAP with a simpler selection baseline (e.g., any 32 frames, or frames with highest motion magnitude) to isolate the benefit of the generative prior.
- Validate generation quality with a quantitative metric (e.g., PSNR/SSIM between generated and held-out real latents on a subset).

## Removed Points

These points were removed from consideration:

1. **"The cited cost estimate ($2,000 for 100 hours of video) is extreme"** — Removed. The estimate is reasonable given GPT-4's token pricing and presented only as motivational context. The paper also evaluates open-source models, and the estimate is not central to any claim.

2. **"Figure 1 is referenced but not provided"** — Removed. The figure is an image in the PDF; the parser stripped it. This is not a paper flaw.

3. **"The paper only implements VideoTree on CLEVRER" (framed as selective reporting)** — Partially removed from weakness categorization. The paper is transparent about this (line 117 explicitly states "We implemented VideoTree on the CLEVRER dataset"). Other baseline results are cited from original papers. This is standard practice; the limitation is already covered by the VLM-backbone inconsistency point above.

4. **"No comparison against simple frame selection baselines"** (in the Strengthening section) — This is already covered as a Major weakness above. Duplicated entries from the harsh critic's "Strengthening the Paper" section are merged into the Nice-to-Haves.

5. **Criticisms framed as speculation** (e.g., "if the generation is poor," "could the metric be measuring a proxy") without specific evidence from the paper — Removed. The validated core concern (no generation quality validation) is retained as a weakness above.

## Novel Insights

The harsh critic's critique usefully identifies that the paper's central weakness is a missing controlled experiment: VAP's selection strategy is never compared against simpler alternatives (uniform/random) at the same frame budget, making it impossible to attribute performance gains to the active-perception selection mechanism rather than merely the effect of using fewer frames. The strength finder correctly highlights that the paper's VLM-agnostic evaluation across three model families and the ablation on frame counts are genuine empirical strengths. The most insightful observation from the reviews is the tension between the paper's "lightweight" framing and the actual computational profile of the method — VAP processes all frames through a VAE and runs a diffusion model, which is not obviously lightweight. A clean resolution would be to provide total compute accounting, which would either validate or bound the efficiency claim transparently.

## Suggestions

- **Add an equal-budget baseline.** Compare VAP (32 frames) against uniform sampling of 32 frames and random selection of 32 frames on EgoSchema and NExT-QA. This is the single most impactful addition.
- **Report end-to-end latency.** Provide a wall-clock time breakdown (VAE encoding, diffusion denoising, RIFE interpolation, VLM inference) for a representative video. This would either substantiate or bound the efficiency claim.
- **Validate generation quality.** Compute the correlation between cosine-similarity scores (real vs. generated latents) and human-annotated frame importance, or compare generated latents to ground-truth latents on a held-out subset.
- **Tone down the "lightweight" characterization** of CogVideoX, or clarify what "lightweight" means relative to the VLM being accelerated.
- **Provide explicit SOTA context.** Cite specific numbers from the EgoSchema leaderboard or other benchmarks to make the SOTA claim fully self-contained.

## Score and Decision

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>