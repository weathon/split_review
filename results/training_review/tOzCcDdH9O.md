Now I have all the information needed. Let me compose the final review.

## Summary

The paper introduces Matryoshka Diffusion Models (MDM), a family of diffusion models that perform joint denoising at multiple resolutions via a NestedUNet architecture with parameter sharing across scales. MDM enables end-to-end pixel-space training at up to 1024×1024 resolution without cascaded or latent stages, using a progressive training schedule that starts from low resolutions. Experiments cover class-conditional ImageNet generation, text-to-image on CC12M (up to 1024²), and text-to-video on WebVid-10M.

## Strengths

- **Multi-resolution loss with progressive training demonstrably accelerates convergence.** Section 4.2 shows that MDM converges faster and reaches better FID than a standard single-resolution UNet (Simple DM) on ImageNet 256×256, and progressive training further improves both speed and final quality. The ablation in Section 4.3 (referenced as Fig. "imagenet_fid_ablation") quantifies that more low-resolution pretraining iterations directly benefit high-resolution FID.

- **NestedUNet enables parameter-efficient multi-scale processing.** Section 3.2 describes how low-resolution features and parameters are nested within the high-resolution model, allowing most computation (attention layers) to be concentrated at low resolution. The comparison in Section 4.2 shows MDM has fewer combined parameters than the Cascaded DM baseline yet outperforms it, demonstrating architectural efficiency.

- **Single pixel-space model trained on a modest dataset (CC12M, 12M images) produces 1024×1024 samples.** The paper demonstrates high-resolution text-to-image generation using only publicly available data, in contrast to prior work relying on proprietary datasets orders of magnitude larger. The deliberate choice of CC12M as a reproducible benchmark is a positive community contribution.

- **Generality demonstrated across three tasks with a single framework.** The same training pipeline is applied to class-conditional image, text-to-image, and text-to-video generation, confirming the method's versatility.

## Weaknesses

### Fatal
None.

### Major

- **Video generation lacks any quantitative evaluation.** The text-to-video experiments on WebVid-10M are supported only by qualitative samples (Fig. 4/6). No standard metrics (e.g., FVD, IS, CLIP score) are reported. Given that video generation is presented as a key demonstration of generality, the absence of any metric-based evaluation makes it impossible to assess the method's actual performance on this task.

- **Cascaded DM comparison is confounded by the under-trained low-resolution model, and the paper acknowledges this.** The Cascaded DM baseline starts from a 64×64 model trained for only 200K iterations (line 153), which the paper itself admits was "not aggressively trained" (line 154). Because MDM's progressive training continues to improve the low-resolution components (via parameter sharing) while Cascaded DM's upsampler conditions on a fixed weak model, the comparison conflates the benefit of continued low-resolution training with the architectural advantage. The paper's own hypothesis for Cascaded DM's inferior performance ("large gap between training and inference wrt the conditioning inputs") confirms this confound. While this does not invalidate MDM—progressively improving low-resolution representations is indeed a benefit of the approach—the experiment as designed does not cleanly isolate the architectural contribution.

### Minor

- **The LDM baseline uses a pretrained autoencoder from Rombach et al. (likely trained on a larger dataset), making the comparison less controlled.** The paper explicitly acknowledges this on line 154 ("a less direct control as LDM is indeed more efficient"). The comparison is not invalid—it shows MDM is competitive despite operating in more challenging pixel space—but the confound limits what can be concluded.

- **The text summarizing main results is vague.** Section 4.2 states only that MDM "provides comparable results to prior works" (line 175) without reporting specific FID/CLIP numbers in prose. While the actual numerical results are in tables and figures (which exist in the original submission), the text would benefit from citing key numbers to make the core claims immediately evaluable.

### Trivial

- Some implementation details (e.g., the exact progressive training schedule beyond what is described, the noise schedule shift details) are deferred to an appendix section that was stripped by the parser.

## Nice-to-Haves

- Reporting FVD or similar video metrics on WebVid-10M or a held-out benchmark to substantiate the video claim.
- A controlled experiment where the low-resolution model for Cascaded DM is trained to convergence (same loss/FID as MDM's low-res component) before comparing, to isolate the architectural advantage.
- Ablation of the multi-resolution loss weighting scheme (currently inverse-proportional to resolution size) versus alternatives.

## Removed Points

- **Point about core results being "absent" from the paper**: The tables and figures containing FID-50K, zero-shot FID-30K, and ablation curves exist in the original submission but were stripped by the parser. The paper does contain these numbers. The criticism that results are "not reproduced or summarized in the text" is a presentation issue, not an evidential gap. (Kept as Minor: the text summary is indeed vague.)

- **Point that "no human evaluation or perceptual metrics"**: Scope creep — FID and CLIP are the standard evaluation metrics in this field. Demanding human evaluation for an algorithmic contribution is not standard practice.

- **Point about CLIP score ~31 being a "misprint"**: CLIP scores are unitless, and the paper is citing Imagen's reported CLIP score in Figure A.11 of Saharia et al. This is accurate, not a misprint.

- **Point about missing pseudocode, missing iteration counts, missing hyperparameters**: These are deferred to the appendix (parser-stripped) or are standard implementation details. Per the rules, these are parser artifacts or minor reproducibility nitpicks.

- **Point that the 64×64 model "not aggressively trained" invalidates the paper's claims**: The paper acknowledges this limitation explicitly. The comparison still demonstrates a real advantage of MDM (parameter sharing allows continued improvement), but the confound is real. Moved to Major rather than Fatal.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a new perspective not already present in the paper's discussion of its limitations and design rationale.

## Suggestions

1. Add quantitative video evaluation (e.g., FVD, CLIP score) on WebVid-10M or a standard video benchmark to substantiate the video generation claims.
2. In the cascaded comparison, either (a) train the low-resolution model to convergence before comparing, or (b) explicitly frame the experiment as "MDM with progressive training vs. cascaded from the same initialization" and discuss the confound more directly.
3. Include key numerical results (ImageNet FID-50K, COCO zero-shot FID-30K) in the main text rather than relying solely on tables, so the core claims are immediately verifiable.

## Score and Decision

The paper introduces a well-motivated framework with a clean conceptual contribution (joint multi-resolution denoising with nested architectures) and demonstrates clear benefits over a standard single-resolution UNet. The progressive training schedule is practical and supported by ablation. The main weaknesses are: (1) the video results lack any metric, (2) the cascaded comparison is confounded in a way the authors partially acknowledge but do not fully address, and (3) the main numerical results are not cited in the text (though they exist in tables). These are addressable weaknesses, not fatal flaws. The core methodological contribution is solid, the experiments on image generation are reasonable, and the community benefit of a reproducible CC12M-based benchmark is real. The paper would benefit from revisions to address the video evaluation gap and better-controlled baselines.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>