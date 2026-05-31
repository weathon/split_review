I have thoroughly read and analyzed the paper and all reviewer claims. Let me now produce the consolidated review.

---

## Summary

This paper introduces Matryoshka Diffusion Models (MDM), an end-to-end framework for high-resolution image and video synthesis. The key idea is to perform joint denoising across multiple resolutions using a NestedUNet architecture where low-resolution computation is nested within higher-resolution processing, together with a progressive training schedule that transitions from lower to higher resolutions. The method is evaluated on class-conditional ImageNet generation, text-to-image on CC12M (up to 1024×1024), and text-to-video on WebVid-10M, all using publicly available datasets.

## Strengths

- **End-to-end high-resolution generation without multi-stage pipelines.** MDM demonstrates a single pixel-space model operating at up to 1024×1024 resolution, eliminating the need for separately trained super-resolution models (cascaded) or autoencoders (latent). This is a clean and well-motivated design. Evidence: Abstract ("single pixel-space model at resolutions of up to 1024×1024 pixels"), Section 3 (joint diffusion process over multiple resolutions), and the comparison to Simple DM / Cascaded DM baselines in Section 4.2.

- **Multi-resolution loss and progressive training accelerate convergence.** The controlled comparisons show that MDM with the joint denoising objective converges faster and achieves better final quality than a standard UNet baseline (Simple DM), and that progressive training further improves both speed and final performance. Evidence: Section 4.2 ("Comparing simple DM to MDM, we see that MDM clearly has faster convergence, and reaches better performance in the end"), Section 4.3 ablation on progressive training ("more low resolution training clearly benefits that of the high-resolution FID curves").

- **NestedUNet enables efficient parameter allocation.** The architecture concentrates most parameters and computation at the lowest resolution, achieving better scalability than standard UNets that dedicate uniform compute across scales. Evidence: Section 3.2 ("our early exploration found that MDM achieved much better scalability when allocating most of the parameters & computation in the lowest resolution"), the architecture description, and the comparison noting Cascaded DM has more parameters yet underperforms MDM.

- **Strong zero-shot results from a modestly-sized, public dataset.** Trained on CC12M (12M images), MDM achieves CLIP scores on COCO zero-shot evaluation that are described as comparable to models trained on much larger datasets. This is notable because it demonstrates the method's data efficiency and enables reproducible research with accessible compute/data. Evidence: Section 4.3 CLIP-FID trade-off discussion ("MDM is trained on a significantly smaller training set compared to other models... it still demonstrates strong CLIP score"), and the overall experimental design using only public datasets.

## Weaknesses

### Fatal

None.

### Major

- **The controlled cascaded comparison is undermined by an undertrained base model, weakening the claim of superiority over cascaded methods.** The paper explicitly states: "We hypothesize that the inferior performance of Cascaded DM is largely due to the fact that our 64x64 is not aggressively trained, which causes a large gap between training and inference wrt the conditioning inputs" (Section 4.2). This means the Cascaded DM baseline was handicapped by design — the low-resolution model was not trained to convergence before the upsampler was added. Yet the paper still presents this as evidence that MDM outperforms cascaded generation ("As a direct comparison, we see that the Cascaded DM baseline significantly under performs MDM"). The comparison is therefore not a fair test of cascaded models at their best; it only shows MDM is more robust to an undertrained base model. To support the broader claim that MDM is superior to cascaded generation, the 64×64 model should be trained to convergence (or a standard protocol should be used) before comparing.

- **No quantitative video evaluation metrics are provided.** The paper presents text-to-video results on WebVid-10M as evidence of generality, but only shows qualitative samples. No video-specific metrics (e.g., FVD, IS for video) are reported. The paper claims MDMs show "strong zero-shot capabilities of generating high-resolution images and videos" (Section 4.2, Qualitative Results), yet for video this claim rests entirely on subjective samples. Given that the paper presents MDM as a general framework for both image *and* video, the absence of any quantitative video evaluation is a significant omission that weakens the claim of generality.

### Minor

- **Mixed-resolution training is described but never ablated or evaluated.** Section 3.3 mentions that "we can incorporate mixed-resolution training, a technique that involves the concurrent training of samples with varying final resolutions within a single batch" (line 105), but no experiment isolates or measures its effect. This is a missed opportunity to validate an aspect of the training pipeline.

### Trivial

None.

## Nice-to-Haves

- Adding a quantitative video metric (e.g., FVD on a standard subset of WebVid or UCF-101) would substantially strengthen the claim of generality to video.
- Providing the noise schedule shift formula or key parameters in the main text (rather than only citing gu2022f) would improve self-containedness, though the current citation is standard practice.

## Removed Points

1. **"Quantitative evidence absent from prose"** (Harsh Critic Point 2) — Removed because the actual numbers reside in the tables and figures that exist in the original submission (the parser strips \input{tables/...} and figures). It is standard practice to report numbers in tables and summarize qualitatively in prose. The prose describes the qualitative trends visible in those tables/figures.

2. **"Method specification incomplete (noise schedule, pseudo-code)"** (Harsh Critic Point 4) — Removed because the pseudo-code is in an \input{} file that exists in the original submission (stripped by parser). Referencing gu2022f for the noise schedule shift is standard citation practice.

3. **"Missing statistical significance / confidence intervals"** — Removed because single-run evaluation on standard benchmarks is the norm in this field.

4. **Criticisms that are pure formatting/style nitpicks or speculative concerns** — Removed per the filtering guidelines.

5. **Strength Finder strengths that conflict with verified weaknesses** — The Strength Finder's claim about the controlled comparison being the "single most important piece of evidence" is partially weakened by the cascaded baseline issue noted above. The retained strength about end-to-end generation without multi-stage pipelines is retained but calibrated accordingly.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a novel synthesis that meaningfully extends the paper's own framing.

## Suggestions

1. **Fix the cascaded baseline comparison:** Either train the 64×64 model to convergence before adding the upsampler, or remove/narrow the claim about MDM outperforming cascaded models and focus on the more solid comparisons (vs. Simple DM and the progressive training ablation).
2. **Add a quantitative video metric** (e.g., FVD) to support the generality claim for video generation.
3. **Ablate the mixed-resolution training** technique to either validate or remove this aspect of the pipeline.
4. **Report key numbers (FID, CLIP) for MDM and baselines explicitly in a table** — while the tables exist, a few anchoring numbers in the prose would help readers immediately assess the magnitude of the reported improvements.

## Score and Decision

The paper presents a genuinely novel method (joint multi-resolution diffusion with NestedUNet and progressive training) that is well-motivated and shows clear advantages in convergence speed and end-to-end simplicity. The core technical contributions are supported by controlled comparisons and ablation studies. However, two significant weaknesses — the fairness of the cascaded comparison and the lack of quantitative video metrics — prevent the paper from fully substantiating its broader claims. These issues are fixable and do not invalidate the core contribution.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>