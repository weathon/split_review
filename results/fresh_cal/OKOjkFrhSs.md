Now I have a thorough understanding of the paper. Let me compose the final review.

## Summary

This paper proposes Prompt-guided Dynamic Network (PDN) for single image super-resolution, which uses CLIP-encoded multi-modal prompts (text captions or images) to condition both a spatial attention mask and a dynamic convolution. The core technical innovation is the Dynamic Correlation Module (DCM), consisting of a Spatially Multi-Modal Attention Module that generates pixel-wise cross-modal attention masks and a Prompt-Guided Dynamic Convolution Module that generates convolutional kernel weights from the prompt embedding. DCM is designed as a plug-and-play module that can be inserted into existing SR backbones (EDSR, RDN, RCAN).

## Strengths

- **First use of CLIP prompt embeddings for dynamic convolution kernel generation in SR.** The paper formulates a mechanism where prompt embeddings (via CLIP) generate attention weights over a kernel bank, replacing the conventional image-feature-based dynamic weighting. This design is clearly motivated (Section 3.3, Remark) and distinguished from both CondConv and prior guided SR methods like TGSR. The contrast between conventional and prompt-guided dynamic convolution is explicitly diagrammed (Figure 2).

- **Plug-and-play integration consistently improves multiple SR backbones.** Table 3 shows that inserting DCM into EDSR, RDN, and RCAN yields consistent PSNR gains of 0.11–0.51 dB and SSIM gains of 0.009–0.02 on the COCO ×4 benchmark. This is the strongest evidence in the paper: it demonstrates that DCM is a broadly applicable add-on, not a method that only works with one specific architecture.

- **Ablation confirms both sub-modules contribute.** Table 4 shows that removing either the attention module or the dynamic convolution module from EDSR+ degrades PSNR from 26.84 dB to 26.69 dB and 26.72 dB respectively, validating that both components are functional.

- **Qualitative attention maps show prompt responsiveness.** Figures 4 and 5 visualize attention masks that shift to semantically meaningful regions when different text captions are provided (e.g., "cats" vs. "television" highlighting different image regions), providing intuitive evidence that the spatial attention is driven by prompt content.

## Weaknesses

### Fatal
None.

### Major

- **Missing ablation: prompt-based vs. image-feature-based dynamic convolution is not compared.** The paper's key technical novelty claim (Section 3.3, Remark) is that using *prompt embeddings* to generate dynamic kernel weights is superior to conventional *image-feature-based* dynamic convolution (e.g., CondConv). The Remark argues this is because prompt embeddings have "high variance and sparse distributions" while image features are "averaged." However, the ablation study (Table 4) only removes the dynamic convolution entirely (replacing it with standard convolution) or removes the attention module. It never replaces the *prompt-based* weight generation with an *image-feature-based* one of comparable capacity. Without this control, the observed improvements could come from any dynamic weighting mechanism or simply from added parameters, rather than from the specific use of prompt embeddings. The paper's core technical distinction from prior work is left untested.

- **The PDN architecture in the main comparison (Table 1) is underspecified.** The paper says "We adopt the residual in residual (RIR) block... as the basic residual block" (Section 3.2), which is the building block of RCAN. But it never states explicitly: "PDN uses RCAN as its backbone" or provides the baseline performance of that same backbone *without* DCM in Table 1. The main quantitative comparison pits "PDN" against RCAN, RDN, EDSR, and GAN-based methods — but the reader cannot determine how much of PDN's gain comes from DCM vs. from architectural differences in the backbone itself. Table 3 (EDSR+/RDN+/RCAN+) mitigates this by showing modular gains, but Table 1 remains the headline comparison and its interpretation is ambiguous.

### Minor

- **Evaluation mixes PSNR-oriented and GAN-based methods in the same table.** Table 1 includes SRGAN, ESRGAN, and SPSR (trained with adversarial/GAN objectives to optimize perceptual quality at the cost of PSNR) alongside L1-trained methods (EDSR, RDN, RCAN) and PDN (also L1-trained). Comparing PSNR/SSIM across these two categories is uninformative because GAN-based methods are expected to have lower PSNR by design. The presence of GAN baselines inflates the apparent gap. The PSNR-oriented and GAN-based methods should be reported in separate tables, and perceptual metrics (LPIPS, FID) should be included for the GAN comparison.

- **Multi-modal framing is partially overstated given the experimental setup.** The paper emphasizes "multi-modal prompts (texts or images)" as a core contribution, but the quantitative results on FFHQ (×8, ×16 in Table 1) and the visual comparison on Urban100 (Figure 3) rely on horizontally flipped versions of the *same LR image* processed through CLIP's image encoder — this is a single-modality, within-image conditioning signal, not a cross-modal prompt. The paper is transparent about this (Section 4.1), but the framing ("powerful multi-modal representations," "rich semantic information from prompts") extends beyond what these experiments demonstrate. The truly multi-modal evidence is limited to the COCO experiments where text captions are used.

- **No quantitative prompt sensitivity analysis.** Section 4.5 shows attention masks varying with different captions (qualitative), but the paper does not quantify how prompt quality affects SR performance (e.g., correct vs. mismatched vs. random captions). Without this, it is unclear whether the prompt's semantic content matters or the module simply learns a fixed conditioning signal.

### Trivial
- The text references "From Figure 1" when describing visual results, but the visual comparison is in Figure 3 (Section 4.2, line 148).

## Nice-to-Haves
- Report results on standard benchmarks (Set5, Set14, Urban100) for the integrated models (EDSR+, RDN+, RCAN+) to allow direct comparison with the literature. If those datasets lack text captions, the paper should be explicit that the multi-modal setting applies only to datasets with annotations.
- Replace the flipped-image prompt baseline on non-annotated datasets with a control that uses the same additional compute (e.g., an extra convolution block of similar parameter count) to isolate the effect of the prompt mechanism.
- Add a control where the prompt is replaced by a fixed/random vector to test whether the specific semantic content of the prompt matters, or whether the module simply benefits from extra capacity.

## Removed Points

These points were raised by reviewers but are removed after verification:

- **"The dynamic convolution uses a global embedding so cannot handle spatial variants"** — Removed because the paper attributes spatial variation handling to the *combined* DCM (attention mask handles pixel-level variation, dynamic convolution handles image-level variation). The claim is about the full system, not the convolution alone.
- **"TGSR already used text prompts, novelty overclaimed"** — Removed because the paper acknowledges TGSR and explicitly claims novelty in *kernel estimation from prompts*, not merely using prompts. The claim is scoped to "convolutional kernel estimation."
- **"ζ initialized to 50 without discussion"** — Removed because the paper does discuss this: "considering that the values of both prompt embedding and image feature are suppressed by L2 normalization, we scale the mask by a learnable factor ζ to keep a relatively large variance" (Section 3.3).
- **"Reproducibility concerns with TGSR reimplementation"** — Removed because the paper states TGSR code was not released; reimplementation is the only available option and the paper is transparent about this.
- **"No error bars / statistical significance"** — Removed because single-run evaluation is standard practice in SR benchmarking; this is not a weakness specific to this paper.
- **"Missing related works"** — Removed because I cannot verify the existence of missing references without external sources.
- **"Parser issues / formatting"** — Removed as these are PDF extraction artifacts, not author errors.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Add the critical ablation.** Compare PDN's prompt-guided dynamic convolution against an otherwise identical model that uses conventional image-feature-based dynamic convolution (e.g., global average pooling of the feature map fed into the same MLP → attention weights over the kernel bank). This directly tests the paper's central technical claim.

2. **Clarify the PDN backbone.** State explicitly which backbone PDN is built upon in Table 1 (appears to be RCAN via RIR blocks). Better yet, add a row showing the backbone without DCM in Table 1 so readers can directly see the gain.

3. **Restructure the evaluation tables.** Separate PSNR-oriented comparisons (against EDSR, RDN, RCAN) from GAN-based comparisons (against SRGAN, ESRGAN, SPSR). Include perceptual metrics (LPIPS, FID) for the latter.

4. **Add quantitative prompt sensitivity experiments.** Measure PSNR when using correct captions vs. mismatched captions vs. random text vs. no prompt, to demonstrate that the semantic content of the prompt drives the improvement.

5. **Report quantitative results on standard benchmarks.** Even though Set5/Set14/Urban100 lack text captions (requiring flipped-image prompts), reporting these results would allow the community to compare against standard SR literature.

## Score and Decision

**Originality:** The idea of using CLIP embeddings to condition both spatial attention and dynamic convolution weights in SR is novel and well-motivated. The paper correctly identifies the limitation of conventional dynamic convolution (averaged weights) and proposes a plausible alternative.

**Quality of claims and support:** The central claim — DCM improves SR — is partially supported by Table 3 (consistent gains across backbones). However, the more specific claim that prompt-based dynamic convolution is superior to image-feature-based dynamic convolution is not tested, which is a significant evidential gap. The headline comparison (Table 1) is difficult to interpret due to an underspecified backbone and mixed baseline types.

**Soundness:** The method is clearly described and the design decisions (CLIP encoder, L1 loss, RIR blocks) are reasonable. The main experimental weakness is the missing ablation for the core novelty.

**Clarity:** The paper is generally well-written. The method description in Section 3 is clear, the figures are helpful, and the motivation is sound.

**Significance:** If validated, the DCM module could be a useful plug-and-play addition to SR networks, especially in settings where text descriptions are available. The broader idea of conditioning low-level vision tasks on CLIP embeddings is timely.

**Overall:** The paper presents a genuinely interesting idea and the plug-and-play integration results (Table 3) provide meaningful evidence. However, the missing ablation for the core technical novelty (prompt-based vs. image-feature-based dynamic convolution), the underspecified main comparison, and the evaluation design issues collectively prevent full validation of the paper's claims. The contribution is real but the evidence is incomplete.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>