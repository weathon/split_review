## Summary

This paper presents a systematic robustness analysis of latent diffusion models (LDMs) for image editing, going beyond prior encoder-focused attacks to evaluate eight distinct internal modules (encoder, quantization, ResNet, self-attention, cross-attention, feed-forward, post-quantization, decoder) under white-box and black-box (transfer) settings. The authors also introduce automatic dataset construction pipelines yielding 500 image-prompt pairs and 500 image-prompt-mask triplets. Key findings include: (1) the denoising process (especially the ResNet block) is the most vulnerable component; (2) adversarial examples transfer across prompts and models, with an asymmetric pattern where SD-v1 examples transfer effectively to SD-v2 but not vice versa; (3) Instruct-pix2pix is more robust than standard Stable Diffusion models.

## Strengths

- **First systematic module-level vulnerability analysis of latent diffusion models.** Prior work attacked only the encoder (Zhuang et al.) or output image (Salman et al.). This paper evaluates eight modules individually (Table 1) and identifies the denoising process (ResNet) as the most vulnerable — ResNet attack drops CLIP to 29.89 vs. benign 34.74, and SSIM to 0.076. This is a genuinely new finding that moves beyond encoder-focused attacks.

- **First demonstration of two black-box transfer regimes for LDMs.** The paper introduces and evaluates both prompt-transfer (adversarial examples transfer across different prompts for the same model, Table 4: CLIP 28.27 for Unet, nearly matching white-box 29.89) and model-transfer (Table 5: SD-v1-5 adversarial examples transfer to SD-v2-1 with CLIP 28.48 vs. SD-v2-1's own white-box 27.98). The asymmetric transfer finding — SD-v1→SD-v2 works but SD-v2→SD-v1 does not — is a novel empirical result.

- **Automatic dataset construction pipelines with reusable outputs.** The two pipelines (COCO → CLIP filtering → ChatGPT prompt generation → segmentation-based masking) are well-described and produce a usable benchmark (500 pairs + 500 triplets). The use of CLIP score for quality filtering is sensible, and the code/dataset release commitment (line 25) supports reproducibility.

- **Systematic comparison across model versions and architectures.** Table 3 compares four models (SD-v1-4, SD-v1-5, SD-v2-1, Instruct-pix2pix) under identical settings, revealing that Instruct-pix2pix is more robust (Unet attack CLIP 31.65 vs. SD-v1-5's 29.89) — an architectural insight not previously reported.

## Weaknesses

### Major
None. The paper's core findings are supported by evidence, and no single issue invalidates the central claims.

### Minor

- **Cross-module vulnerability comparison is confounded by feature-scale differences.** The paper compares vulnerability across modules (ResNet, self-attention, cross-attention, FF) using the same input perturbation budget (ε=0.1), but different modules may have different feature-space sensitivities. A fixed input budget could cause larger feature distortions in one module than another for reasons unrelated to "vulnerability." The paper does not normalize for this, making the ranking (e.g., "ResNet is the most vulnerable") less precise than claimed. The paper's actual finding is: with a fixed input budget, disrupting ResNet features causes the most output degradation — which is interesting but not the same as ResNet being inherently the most vulnerable component.

- **Model-transfer conclusions are stronger than the evidence supports.** The asymmetric transfer finding (SD-v1→SD-v2 works, SD-v2→SD-v1 does not) is real and visible in Table 5. However, the paper's causal conclusion — "SD-v2 is more vulnerable, and defects inside SD-v1 are inherited by SD-v2" — overinterprets the evidence. Alternatives not ruled out include: different feature-space scales between model versions, different gradient alignments, or the attack parameters (ε=0.1) being relatively smaller for SD-v2. A random-noise baseline (to show the transfer is adversarial rather than just noise amplification) and tests across multiple attack budgets would substantially strengthen this claim. Without these, the "defect inheritance" narrative is speculative.

- **Dataset quality control is weak for a stated contribution.** The human evaluation step uses a single volunteer with no details on background, instructions, or quality checks (line 122). For a dataset intended as a community benchmark, single-annotator curation is insufficient. The CLIP-based prompt filtering using SD-v1-5 also introduces model-specific bias. The dataset is still useful as an experimental resource, but its value as a rigorous benchmark is limited.

- **FID computation is not sufficiently specified.** The benign FID of 167.9 (Table 1) is unusually high, and the paper does not state what reference dataset/distribution is used for FID calculation, nor how many images contribute to the FID estimate. While the high FID may be explained by the image-variation task (edited images naturally differ from the original COCO distribution), the lack of specification makes the FID numbers difficult to interpret or reproduce. The paper should clarify the reference distribution and the sample size used.

- **No variance or confidence intervals reported.** All experiments use a fixed random seed (line 178), so no standard deviations or error bars are provided. Given the stochasticity in diffusion models (sampling noise), single-run results make it impossible to assess the reliability of the reported numbers or the significance of differences between modules.

- **Prompt-transfer experiment underspecified.** The paper states (line 348) that adversarial examples are crafted on one prompt and transferred to "other prompts," but does not specify how many prompts were tested, how they were selected, or whether they are semantically similar to the original. Without this, the generality of the prompt-transfer claim is unknown.

### Trivial

- The "Gaussian" row in Table 1 (non-adversarial noise baseline) and the "Gaussian" defense in Table 6 serve different roles but share the same label. Clarifying this distinction would help readers.
- The paper does not discuss potential overlap or interaction between modules (e.g., ResNet and self-attention computational paths may overlap), which could affect interpretation of the independent module attacks.

## Nice-to-Haves

- **Adaptive defenses or defense-aware attacks.** The defense evaluation (Table 6) tests three defenses against unadapted attacks. Testing whether the attack can be made robust to R&P by including random transformations in the attack loop would better characterize the practical threat. However, since defense is not the paper's main contribution, this is non-critical.
- **Experimental comparison with prior attack methods (Salman et al., Zhuang et al.)** on a subset of metrics would help situate the contribution. The paper cites these works but does not benchmark against them directly.
- **Random noise baselines** in the transfer experiments (equal l∞ budget, random direction) would strengthen the claim that the transfer effect is genuinely adversarial.
- **Cross-module interaction analysis** — the paper attacks modules independently; analyzing whether attacking multiple modules jointly yields compounding effects would be informative.

## Removed Points

The following criticisms from reviewers were evaluated against the paper and removed:

1. **"Attack objective is not aligned with evaluation metrics — foundational gap"** — Removed. The paper's feature-level attack (maximizing l2 distance of intermediate representations) and output-level evaluation (CLIP, PSNR, SSIM) are different by design: the attack is the mechanism, the metrics measure the outcome. This is standard practice in adversarial robustness. The paper's assumption that feature disruption leads to output degradation is empirically validated by the results in Table 1 (all attack CLIP scores are well below benign). The methodology is internally consistent.

2. **"Defense analysis is too brief and superficial"** — Moved to Nice-to-Haves. The defense section is a supporting experiment testing whether adversarial examples survive practical preprocessing defenses, not a main contribution. The paper's conclusion ("geometry transformation can largely mitigate" and "adversarial examples can still mislead under several defenses") is accurately supported by the data. Requesting adaptive attacks is appropriate for a defense paper, not for an attack analysis paper whose defense section is auxiliary.

3. **"Missing comparison with prior attack methods"** — Moved to Nice-to-Haves. The paper cites and discusses Salman et al. and Zhuang et al. (line 72). Experimental comparison is a reasonable suggestion but not a required standard, as the attack targets (different modules) and settings differ substantively.

## Novel Insights

The main novel insight that emerges from this review is that the paper's most interesting finding — asymmetric model transfer where SD-v1 attacks transfer to SD-v2 but not vice versa — is empirically robust in the data (Table 5 clearly shows the pattern) but the paper's causal interpretation ("defect inheritance") outstrips what the experiment can support. This asymmetry could equally reflect that SD-v2's feature representations are simply more distant from SD-v1's in a way that makes v2→v1 gradient alignment poor. The paper would benefit from reframing this finding as an empirical observation with several plausible explanations rather than a definitive statement about model evolution. Conversely, the core finding that the denoising process (especially ResNet) is the most attack-vulnerable component is well-supported and genuinely novel — no prior work had systematically compared modules inside the Unet.

## Suggestions

1. Clarify the FID computation: state the reference dataset/distribution and the number of samples used. If FID is computed between the 100 human-filtered edited images and the full COCO validation set, acknowledge that this measures distribution shift from editing, not generation quality in the usual sense.

2. Add a random-noise baseline to the transfer experiments: craft perturbations of equal l∞ budget with random directions from both source models and measure the resulting CLIP scores on target models. This distinguishes adversarial transfer from noise-amplification effects.

3. For the cross-module ranking (Table 1), either normalize the feature-space sensitivity or reframe the claim: instead of "ResNet is the most vulnerable," report it as "attacking the input to disrupt ResNet features causes the largest output degradation under a fixed input budget."

4. Report key results with variance estimates (e.g., over 3 random seeds or bootstrapped subsets of the dataset) to enable meaningful comparison of the reported differences.

5. Expand dataset quality control: use at least 3 annotators and report inter-annotator agreement. Even a small-scale multi-annotator study on a subset would substantially strengthen the dataset contribution.

6. Tone down the causal language in the model-transfer conclusion to match the evidence level, or add the controls needed to support the stronger claim.

## Score and Decision

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>