Here is my consolidated review.

---

## Summary

This paper introduces Matryoshka Diffusion Models (MDM), a family of diffusion models that perform joint denoising at multiple resolutions simultaneously using a NestedUNet architecture. By treating low-resolution signals as part of the high-resolution generation process and sharing parameters across resolutions, MDM enables end-to-end high-resolution image and video synthesis without cascaded stages or latent autoencoders. The model is demonstrated on class-conditional ImageNet generation, text-to-image on CC12M (up to 1024×1024), and text-to-video on WebVid-10M, using publicly available datasets and moderate compute.

## Strengths

- **Novel and well-motivated multi-resolution diffusion framework.** The paper defines a diffusion process over an extended space of multiple resolutions (Eq. 2) with a corresponding multi-resolution denoising objective (Eq. 3). The idea of treating lower-resolution signals as part of the high-resolution reverse process (rather than as separate cascaded stages) is conceptually clean and principled. Controlled comparisons described in §4.2 show MDM converging faster and reaching better performance than a standard UNet baseline and a Cascaded DM baseline.

- **NestedUNet architecture with parameter sharing outperforms cascaded models despite fewer parameters.** The paper reports that the Cascaded DM baseline "significantly under performs MDM, while both starting from the same 64×64 model," and notes that "Cascaded DM has more combined parameters than MDM (because MDM has extensive parameter sharing across resolutions), and uses twice as many inference steps." This is a compelling efficiency argument.

- **End-to-end pixel-space generation at 1024×1024 from modest data.** Training a single pixel-space model at 1024×1024 resolution on CC12M (only 12M images) and demonstrating zero-shot capability on COCO is a noteworthy result that supports the method's practical value. The paper's deliberate choice to use only publicly available datasets (CC12M, WebVid-10M) with 2–5 day training on 4–8 GPU nodes strengthens reproducibility.

- **General applicability across tasks.** MDM is applied to class-conditional generation, text-to-image, and text-to-video without task-specific modifications, with qualitative samples from all three domains provided.

- **Ablation studies validate key design choices.** The paper describes ablations over the number of nested resolution levels and the amount of low-resolution pre-training, showing both design choices consistently improve results.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **No inline numerical results in the running text.** The paper reports FID-50K (ImageNet 256×256) and zero-shot FID-30K (COCO) in tables (`\input{tables/comparison_sota}`, etc.) that exist in the original PDF, but the running text contains zero actual numbers. Key claims — "MDM clearly has faster convergence, and reaches better performance in the end," "MDM provides comparable results to prior works," "more low resolution training clearly benefits FID curves" — are made without a single inline FID or CLIP value. While the tables address this at a format level, most papers in this area report at least headline numbers inline (e.g., "MDM achieves FID X vs. baseline Y"). Adding 3–5 key numbers to the text would substantially strengthen the paper's argument without requiring any additional experiments.

2. **Broken description of the third baseline (lines 143–144).** The third numbered baseline reads only: "3 and subsequently train diffusion models that match the dimensions of the {\model} UNet." This sentence is incomplete and the baseline cannot be identified or evaluated. This appears to be a genuine manuscript flaw rather than a parser artifact.

3. **Progressive training schedule is described only conceptually.** The paper states it "divide[s] up the training into R phases, where we progressively add higher resolution" but gives no concrete iteration counts, resolution transition points, or phase durations for MDM. (The 200K iterations mentioned on line 153 refer to the *Cascaded DM* baseline's pretraining, not MDM's progressive schedule.) The ablation for progressive training also references a figure (`fig:imagenet_fid_ablation`) without numeric axes or iteration counts in the text. Specific schedules would significantly aid reproducibility.

4. **NestedUNet architecture description, while conceptually clear, lacks implementation precision.** The paper describes the nesting concept — "low resolution latents will be fed progressively along with standard down-sampling" — and references a pseudo-code snippet and architecture figure that exist in the original submission. However, the text alone does not specify exactly how low-resolution features are reused within the high-resolution computation path, how parameters are shared across resolution levels, or how the model produces R separate outputs from a single forward pass. The pseudo-code would help, but even a brief textual description of the nesting mechanism (e.g., "low-resolution feature maps are concatenated with downsampled high-resolution features at the corresponding spatial level of the UNet") would make the paper more self-contained.

### Trivial

- The paper uses the shifted noise schedule from Gu et al. (2022) but does not ablate or evaluate this choice against a fixed schedule. This is a minor omission.
- No inference-cost analysis (parameters per resolution level, FLOPs, wall-clock inference time) is provided for the efficiency claims, though these are stated qualitatively.

## Nice-to-Haves

- Adding an inference-cost comparison (total parameters, FLOPs, inference time) against the Cascaded DM baseline would make the efficiency argument more concrete.
- Reporting the specific noise schedule parameters used per resolution level would aid reproducibility.
- The claim that CLIP score is "similar to Imagen" (line 189) would benefit from the actual MDM CLIP number being reported inline, since the reader otherwise has to cross-reference a different paper's appendix.

## Removed Points

- **"Quantitative results are entirely absent / unverifiable" — downgraded.** The three tables (`comparison_sota`, `comparison_learning`, `comparison_ablation`) and the pseudo-code snippet are included via `\input` commands and exist in the original submission but are stripped by the text extraction process. The paper does have quantitative evidence in its original PDF. I have kept the remaining concern about the *absence of inline numbers in the running text* as Minor weakness #1 above, which is a separate and valid issue.
- **"NestedUNet architecture is insufficiently described for reproducibility" — downgraded.** The pseudo-code (`\input{sections/pseudo}`) and architecture figure (Fig. 2) that the reviewer faults as missing are present in the original submission. I have kept the text-description gaps as Minor weakness #4.
- **"CC12M choice is questionable" — removed.** The paper extensively motivates this choice (lines 122–124) and it is a defensible scope decision.
- **"No human evaluation" — removed.** This is a standard benchmarking paper; human evaluation is not required for this paper class.
- **"Should compare with more baselines" — removed.** The paper includes Simple DM, Cascaded DM, and LDM as controlled baselines plus literature comparisons. This is adequate for a new-method paper.

## Novel Insights

None beyond the paper's own contributions. The reviews identify real presentation gaps but do not surface a limitation or implication of the method that the authors themselves missed.

## Suggestions

1. **Add 3–5 key numbers inline.** Report the headline FID-50K on ImageNet 256×256, zero-shot FID-30K on COCO, and CLIP scores on CC12M directly in the running text of §4.2, even if the full tables remain.
2. **Fix the broken baseline description** at lines 143–144 of the source.
3. **Provide a minimal textual specification of the nesting mechanism** so the architecture can be understood without the pseudo-code or figure. A single sentence describing how low-resolution feature maps are combined with high-resolution features at each UNet level would suffice.
4. **Report the progressive training schedule concretely** — e.g., "200K iterations at 64² followed by 100K iterations jointly on {64², 256²}."
5. **Consider adding an inference-cost table** (parameters per resolution block, inference FLOPs relative to Cascaded DM) to substantiate the efficiency claims.

## Score and Decision

Based on the provided content, the paper presents a novel, well-motivated method with a clean conceptual contribution, demonstrated across multiple tasks and settings. The primary weaknesses are presentation issues — no inline numerical results, a broken sentence, and under-specified architecture/training details — none of which undermine the core claims or invalidate the contribution (the tables and pseudo-code exist in the original submission). These are addressable in a revision.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>