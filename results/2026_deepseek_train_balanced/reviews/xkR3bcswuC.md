## Summary

This paper presents a systematic empirical investigation of whether generative models across three major families (GANs, autoregressive models, and diffusion models) encode intrinsic scene properties—depth, surface normals, albedo, and shading. Using LoRA adapters attached to the pre-trained generators with the same output head, the authors demonstrate that these intrinsics can be recovered with remarkably few additional parameters (as low as 0.04% of model weights at rank 2) and little labeled data (as few as 250 samples). The paper also reports a positive correlation between generator quality (measured by FID) and intrinsic recovery accuracy, supported by a control experiment showing that a randomly initialized model fails to recover useful intrinsics.

## Strengths

- **First unified study across GAN, autoregressive, and diffusion models using a single recovery method.** Prior work was model-specific (StyleGAN-only in Bhattad et al. 2023; diffusion-only in Chen et al. 2023). Table 1 provides a systematic comparison across VQGAN, StyleGAN-v2, StyleGAN-XL, and Stable Diffusion, covering both qualitative and quantitative evaluation for four intrinsic modalities. This cross-architecture evidence is the paper's strongest contribution.

- **Control experiment (randomly initialized SD UNet) isolates the role of pre-training.** Training LoRA on a randomly initialized UNet under the same protocol yields poor results (Section 4.3), directly demonstrating that the recovered intrinsic information originates from the pre-trained generator's learned representations rather than from the LoRA mechanism itself. This is a clean and informative ablation.

- **Parameter and label efficiency is convincingly demonstrated.** Rank 2 LoRA (0.4M parameters, 0.04% of SD weights) still produces good performance, and credible predictions emerge from as few as 250 labeled samples. These are the paper's most concrete and replicable findings.

- **Positive FID–intrinsic accuracy correlation within controlled comparisons.** The trend across Stable Diffusion versions (v1.1 → v1.2 → v1.5), which controls architecture, genuinely suggests that better generation quality yields better intrinsic recovery.

## Weaknesses

### Major

- **The framing overclaims specificity to generative models, and the DINO finding is not reconciled with the core thesis.** The paper's title, narrative, and contribution statements center on what *generative* models "know." However, Section 4 reports that DINOv2 (a non-generative, self-supervised ViT) achieves "quantitative results comparable to those from Stable Diffusion" using the same LoRA protocol. This is treated as an extension, but it directly challenges whether the phenomenon is specific to generative models or is instead a general property of strong visual representations. If a non-generative model yields comparable numbers, the claim that "generative models encode intrinsics" (though not false) is misleading without a clear articulation of what distinguishes the generative case. The paper needs either (a) a controlled comparison against a standard vision encoder (e.g., ImageNet-pretrained ViT) with LoRA to test whether generative models are distinctively better, or (b) an honest reframing that situates the contribution as: *strong visual representations, including but not limited to those from generative models, serve as effective feature spaces for intrinsic prediction with lightweight adaptation.* This is the single most significant gap between the paper's framing and its evidence.

### Minor

- **The "surpasses the source models" claim on DIODE needs more transparency.** Line 181 states that LoRA adapters surpass Omnidata and ZoeDepth on median error for normals and RMSE for depth—the very models that provided the training signal. This is a striking result, but the actual numbers are only in parser-stripped tables. The paper should present explicit metric values and clarify that the same evaluation protocol (data split, metric computation, resolution) was used across all methods. Without this, the claim is difficult to assess.

- **The cross-model FID correlation (VQGAN, SG-v2, SG-XL on FFHQ) is confounded.** Different architectures have different inductive biases, and the FID values (9.6, 3.62, 2.19) are cited from separate papers without stating whether they were measured under the same evaluation protocol. This weakens the correlation claim relative to the within-SD comparison (v1.1/v1.2/v1.5), which is cleaner but less architecturally diverse. The paper already has the within-SD evidence; the cross-model comparison should be presented with its limitations caveated.

- **No statistical variance or error bars reported.** For a paper whose primary contribution is empirical, quantitative claims of superiority ("surpasses," "outperforms," "peak performance") are not accompanied by confidence intervals, error bars, or multiple-run statistics. This is a significant omission for a venue where reproducibility and rigor are expected, particularly for the baseline comparisons in the low-data regime (250–16000 samples) where sampling variability could be large.

- **The linear probing baseline is overly restricted.** Following Chen et al. (2023), linear probes are applied per layer independently. The paper itself notes that "intrinsic information is distributed throughout the network" (line 30–31) as a rationale for LoRA, so the baseline is structurally disadvantaged by design. A multi-layer linear probe (concatenating features from multiple layers) would be a fairer comparison to isolate the benefit of LoRA's cross-layer information aggregation from the benefit of low-rank parameterization.

- **The "good/medium/bad" qualitative scale in Table 1 lacks clear thresholds.** While defined as "high quality" / "not high quality" / "cannot be recovered," the criteria for these categories are authors' judgment without quantitative tie-breaking rules. For a paper that also reports quantitative metrics, these categories should be anchored to the metric ranges or inter-rater verification.

### Trivial

- The phrase "first to study generative models of all types" (line 24) mentions GigaGAN and CM3leon in the motivation but does not include them in experiments; the actual coverage is three model families, which is broad but not exhaustive.

## Nice-to-Haves

- A comparison against a standard vision encoder (e.g., ImageNet-pretrained ViT-L or ConvNeXt-L) with the same LoRA protocol on DIODE would cleanly resolve whether the observed performance is generative-specific or a general property of strong visual representations. The DINO result already points in the latter direction; a controlled test would settle the question.
- Ablation of the FID-intrinsic correlation across more than one data domain (e.g., LSUN Bedrooms with SD versions) would strengthen the claim that the effect is about generator quality rather than dataset-specific properties.

## Removed Points

*These points were raised in the reviews but are removed after cross-checking against the paper. Treat them with caution.*

- **Training signal circularity:** The critic argued that training and evaluating on pseudo-ground-truth creates circular evidence. However, the paper explicitly evaluates on DIODE (lines 179–181) using real ground truth for depth and normals, and acknowledges (line 174) that generated-image evaluations must be interpreted in context. The core quantitative claims are not circular.
- **Missing non-generative baseline:** The paper already includes DINO (a non-generative, self-supervised model) as a comparison (lines 183–185). Requesting a ResNet/ViT baseline in addition is a reasonable suggestion but not a missing essential experiment—the DINO comparison already provides the relevant boundary test.
- **FID values not sourced:** The FID values are attributed to specific papers via citations (line 202). This is standard practice.
- **LoRA rank not explained per model:** The paper states (line 171) "We use LoRA with Rank 8 as default for all generative models if not otherwise mentioned," which is sufficient.
- **Criticisms that full fine-tuning may need different hyperparameters:** Speculative and not grounded in any evidence from the paper. The paper states all methods converged.
- **Random init experiment doesn't show generative-specificity:** The paper claims "pre-trained generative capabilities are crucial," not that ONLY generative pre-training works. This is accurately stated.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a legitimate framing tension (DINO result vs. generative-specificity claim) but do not produce a novel unifying insight beyond what the paper already reports.

## Suggestions

1. **Reframe the paper's contribution** to honestly situate it as: strong visual representations (including but not limited to generative models) serve as effective feature spaces for intrinsic prediction under lightweight LoRA adaptation. The generative model study is the main case; DINO and other encoders are the boundary test.
2. **Report variance** (error bars, multiple runs) for the key quantitative claims, especially the low-data-regime comparisons (250–16000 samples) where sampling variability is non-trivial.
3. **Present the explicit DIODE numbers** for the "surpasses the source" claim in the main text, with protocol details.
4. **Replace or supplement the per-layer linear probe baseline** with a multi-layer linear probe to provide a fairer comparison for LoRA.

## Score and Decision

MY FINAL SCORE: <score>7</score>
MY FINAL DECISION: <decision>Accept</decision>