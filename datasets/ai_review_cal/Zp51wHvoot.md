- Decision: Reject
- Avg Score: 4.25
- Scores: 6, 3, 3, 5
Good — confirmed no confidence intervals or significance tests, and no limitations section. I now have all the evidence needed to produce the final review.

---

## Summary

ACDC is a zero-shot, training-free framework that combines pre-trained autoregressive models (ARMs) and diffusion models (DMs) at inference time. The ARM generates the full multimodal sequence; at each frame, the DM corrects visual artifacts via SDEdit, and an LLM-based memory module summarizes previous prompts to condition the correction with global context. Experiments on story generation (Show-o, UIO-2 + SD v1.5) and autoregressive video generation (LWM + AnimateDiff) show consistent improvements over raw ARM outputs.

## Strengths

- **Genuine zero-shot combination of ARMs and DMs without fine-tuning**: ACDC works with three different ARMs (Show-o, UIO-2, LWM) and two different DMs (SD v1.5, AnimateDiff) using only inference-time operations. No architectural changes or additional training are required. This is demonstrated across Tables 1 and 3 and Section 3.

- **Clear reduction of error accumulation in long sequences**: The most compelling quantitative evidence is the 10.4% improvement in frame consistency for Show-o+ACDC (Table 1: 0.8211 → 0.9062) and the 3.43% improvement in subject consistency for LWM+ACDC (Table 3: 0.7369 → 0.7622). The video experiment design (correcting first 16 frames, measuring impact on uncorrected later frames) directly tests the error-propagation hypothesis, and the results support it.

- **LLM memory module ablation confirms its value**: The ablation (Table 2) shows clear degradation without the memory component across CLIP similarity (29.43 → 30.85 with memory) and frame consistency (0.835 → 0.853). The qualitative example in Figure 3 illustrates concretely why local text conditions are insufficient without global summarization.

- **Architecture-agnostic design is demonstrated across two different tasks**: The same ACDC recipe is applied to multi-frame story generation (image-level correction) and autoregressive video generation (clip-level correction with a T2V DM), with consistent improvements in both settings.

## Weaknesses

### Fatal

None.

### Major

- **FID is computed against SDXL-generated pseudo-ground-truth, not a natural image distribution.** The paper explicitly states (line 190): "To compute FID against in-distribution images, we generate pseudo-ground truth images using SDXL-lightning." This means FID primarily measures proximity to another diffusion model's outputs — not to real images. The authors acknowledge this (line 192: "this can be partly attributed to the fact that we consider SDXL-generated images as ground truth") but do not provide any alternative evaluation (e.g., FID on a standard dataset like COCO or a user study) to shore up the image quality claim. While the relative comparisons (Show-o vs Show-o+ACDC: 60.50 → 56.36) still indicate improvement within this flawed setup, the metric as implemented does not support claims about real-world image quality.

### Minor

- **The story generation benchmark is entirely synthetic and self-generated.** The paper creates 1,000 six-frame stories using GPT-4o-mini with 10 hand-crafted examples, because existing benchmarks are "not in-distribution" (line 184-186). While the rationale is understandable, the absence of any evaluation on an established story-generation benchmark (e.g., StorySalon, Pororo-SV, or even VBench-style prompts adapted for stories) means the quantitative results rest solely on a dataset the authors control. This limits the generalizability claims the paper can make.

- **Video experiments compare only against the raw ARM, with no dedicated T2V baseline.** Table 3 compares LWM+ACDC only against LWM. The improvement is consistent, but it is impossible to calibrate whether ACDC produces videos competitive with, e.g., direct AnimateDiff generation from text. Adding such a baseline (or a FIFO-Diffusion baseline) would contextualize the contribution and is necessary if the paper claims a "general multimodal generation framework." As is, the video experiment only shows that ACDC helps LWM, not where it stands relative to the broader field.

- **The re-encoding step (corrected images → VQGAN tokens → continued ARM sampling) is not analyzed.** Lines 106 and 132-136 describe re-encoding corrected frames back into discrete tokens for continued ARM sampling. VQGAN encoders are lossy, and it is plausible that re-encoding introduces drift that degrades subsequent frames. No reconstruction fidelity analysis (e.g., LPIPS or PSNR between the corrected image and its re-encoded/re-decoded version) is provided to rule this out.

- **The LLM used for the memory module is not specified.** The method section (line 108) refers to "an LLM parametrized with φ" without naming the model, size, or prompt template. GPT-4o-mini is used for dataset generation (line 185), but it is unclear whether the same model is used for the memory module or a smaller, cheaper one. This is a straightforward missing detail for reproducibility.

- **No confidence intervals or significance tests are reported.** The video results include small improvements (e.g., motion smoothness +0.23%, imaging quality +0.72%). Without uncertainty quantification, it is unclear whether these gains are reliable or within the noise of the evaluation.

- **The ablation (Table 2) uses only 100 stories, and an unexplained reversal is noted but not discussed.** ACDC#2 (correcting only the first 2 frames) achieves higher frame consistency (0.888) than ACDC#6 (correcting all 6 frames, 0.853). The paper mentions this (line 235) but does not explain it. This is a non-obvious result — correcting more frames should not hurt consistency — and readers would benefit from a brief analysis (e.g., does the DM over-smooth individual frames, breaking cross-frame coherence?).

### Trivial

None.

## Nice-to-Haves

- A human evaluation study (pairwise preference or Likert ratings) for story coherence and image quality would substantially strengthen the evidential base, especially given the FID issue.  
- An additional T2V baseline for the video experiment (e.g., direct AnimateDiff generation from text, or FIFO-Diffusion) would calibrate the practical value of the results.  
- Statistical significance testing or bootstrapped confidence intervals for the main quantitative results.  
- A brief analysis of the re-encoding reconstruction fidelity (LPIPS/PSNR).  
- A limitations section discussing computational cost, t' sensitivity, and failure cases.

## Removed Points

*These points were identified by the reviewers but are excluded from the main review for the reasons stated below.*

- *"Theorem 1 is referenced but not provided in the main paper"* — The parser strips the appendix from all papers. The theorem likely exists in the original submission. Do not penalize for formatting artifacts.  
- *"CFG settings differ between first and remaining frames; unclear if baseline uses same setting"* — The paper explicitly states "For both pipelines" (line 268), meaning both LWM and LWM+ACDC use identical CFG settings. The concern is factually wrong.  
- *"ACDC's novelty is limited because SDEdit is a known method"* — The paper does not claim to invent SDEdit; it claims a *novel combination* of ARM + DM + LLM memory at inference. This is not a weakness.  
- *"Missing related works"* — Per policy, the reviewer cannot confirm the existence of missing citations without external sources.  
- *"Reproducibility: undisclosed hyperparameters"* — The paper states (line 178): "For the hyperparameters of the base ARM sampling, we use the default settings advised in the original work." This is adequate for a zero-shot method.  
- *Various formatting/style nitpicks, typos, and grammar issues* — These are parser artifacts, not author errors.  
- *"The paper should discuss SDEdit more explicitly"* — The paper does discuss SDEdit clearly in Section 3 (Eq. 2 and surrounding text).  
- *"The model is not yet released"* — This is not a valid weakness; the paper cites a project page.

## Novel Insights

The most interesting observation that emerges from synthesizing the reviews is the tension between ACDC's core technical strength and its evidential fragility. The idea of using a DM as a zero-shot corrector for ARM errors — with an LLM distilling global context into local prompts — is clean, well-motivated, and demonstrably effective across two tasks and three ARM backends. Yet the evaluation relies on a synthetic benchmark for story generation and a circular FID metric, and the video experiments lack baselines that would situate the results in the broader literature. The paper would be considerably more persuasive if the evidence matched the ambition of the framework; the method itself is sound.

## Suggestions

1. **Fix the FID evaluation.** Either compute FID against a standard natural-image dataset (e.g., COCO validation set, generating one image per prompt from each story) or replace the metric entirely with a human evaluation or a reference-free quality metric that does not depend on another DM's output.
2. **Add at least one established benchmark for story generation** (e.g., StorySalon or the StoryGAN dataset), even if it means a smaller evaluation, to demonstrate generalizability beyond the self-generated dataset.
3. **Include a T2V baseline for the video experiments** (e.g., direct AnimateDiff from text, or FIFO-Diffusion) to contextualize the magnitude of the improvement.
4. **Provide a brief reconstruction-fidelity analysis** (LPIPS between corrected image and re-encoded/re-decoded version) to rule out drift from the re-encoding step.
5. **Specify the LLM used for the memory module** (model name, size, prompt template) to improve reproducibility.
