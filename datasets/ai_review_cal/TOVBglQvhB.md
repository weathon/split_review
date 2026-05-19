- Decision: Reject
- Avg Score: 4.75
- Scores: 3, 5, 6, 5
Now I have all the information I need. Let me compose the final consolidated review.

## Summary

This paper proposes a low-bit quantization method for raw-based low-light image enhancement (LLIE) using U-Net architectures. It introduces two main components: (1) a Distribution-Separative Asymmetric Quantizer (DSAQ) that separately quantizes encoder and decoder features before skip-connection concatenation and uses an asymmetric quantizer with learnable scale/offset for right-skewed activations from LeakyReLU, and (2) a uniform feature distillation (UFD) technique that uses a feature uniform module (FUM) to bridge the representation gap between low-bit and full-precision features. Experiments on SID and MCR datasets show the 4-bit quantized model achieves results close to full-precision performance while reducing model size by 87.5% and FLOPs by 86.6%.

## Strengths

- **The distribution-separative quantization is well-motivated and empirically validated.** Figure 3 demonstrates that upsampled decoder features have a larger value range than encoder features, and the ablation in Table 2 shows that adding DSQ alone yields a 0.28 dB gain at 3-bit over the symmetric baseline on SID-Sony, directly confirming the core observation.

- **The asymmetric activation quantizer is supported by both analysis and ablation.** Figure 2 measures activation skewness across layers and illustrates wasted quantization bins. Table 2 (row Asym) shows a 0.47 dB improvement at 2-bit over the symmetric baseline, providing concrete evidence that handling LeakyReLU-induced asymmetry is beneficial.

- **Ablation studies systematically isolate each component's contribution.** Table 2 adds Asym, DSQ, and UFD incrementally, showing consistent PSNR improvements (e.g., 27.53 → 28.01 dB at 4-bit on SID-Sony). Table 3 further shows UFD outperforms the PAMS-style normalized feature distillation by 0.90 dB at 3-bit and 3.49 dB at 2-bit. This controlled breakdown provides clear evidence for each design choice.

- **The method achieves state-of-the-art results among compared quantizers on two raw LLIE datasets.** On both SID and MCR, the proposed method outperforms all compared quantization methods (DoReFa, PACT, PAMS, LSQ, LLT, QuantSR) at every bit-width (2–4 bits), with meaningful margins (e.g., outperforming LSQ by 0.39–0.98 dB on MCR).

- **Practical efficiency gains are large and clearly reported.** The 4-bit model reduces model size by 87.5% and FLOPs by 86.6%. On a Snapdragon 8 Gen 3 NPU, the 4w/8a quantized model runs 2.2× faster than a 16-bit floating-point model on the same NPU, demonstrating real-world acceleration.

## Weaknesses

### Fatal
None.

### Major

- **Feature Uniform Module (FUM) architecture is not specified.** The paper introduces FUM as a core component of UFD (Section 3.3) — "we introduce a full-precision feature uniform module (FUM) to process features from the quantized network" — but never describes its architectural design. Is it a 1×1 convolution, a small MLP, a residual block? Does it use batch normalization or activation functions? Since FUM is claimed to be discardable at inference, its design is central to understanding whether UFD's improvement comes from the distillation scheme itself or from the capacity of an arbitrary auxiliary network. Without this detail, the method is underspecified and the ablation in Table 3 cannot be fully interpreted. This is a significant reproducibility gap.

- **Comparison fairness with baseline quantizers is insufficiently documented.** The paper compares against DoReFa, PACT, PAMS, LSQ, LLT, and QuantSR (Section 4.2) but provides no description of how these methods were adapted to the U-Net structure for LLIE. Critical questions are left unanswered: Were all baselines trained with the same training schedule (300 epochs, Adam, cosine annealing, learning rate 10⁻⁴)? Were they all initialized from the same pretrained full-precision U-Net? Were quantization settings (signed vs. unsigned, handling of first/last layers) matched fairly? Without this information, the reported performance gaps — often less than 0.5 dB — could partially reflect hyperparameter differences rather than methodological superiority. This weakens the central comparative claims.

### Minor

- **The 33× speed-up claim conflates hardware platform with quantization benefit.** Table 4 reports the 4w/8a quantized model as "33× faster than the 32-bit floating-point model running on GPU." This compares quantized inference on NPU against full-precision inference on GPU, mixing both precision and hardware platform. The 2.2× same-platform comparison (quantized 4w/8a vs. 16-bit float, both on NPU) is clean and informative; the 33× figure should be presented with a clear caveat that it reflects combined gains from quantization and platform differences.

- **The abstract overstates results.** The abstract claims the 4-bit model achieves "comparable or superior results to full-precision counterparts." The text in Section 4.2 more accurately says "maintaining comparable enhancement results." If the 4-bit PSNR is consistently slightly below full-precision (as the critic suggests: 29.04 vs. 29.51 on SID; 31.87 vs. 32.27 on MCR), then "superior" is inaccurate. The claim should be restricted to "comparable."

- **The distillation loss weight λ₂ = 100 is not justified.** Given λ₁ = 1, this is a two-order-of-magnitude imbalance. No sensitivity analysis is provided, so it is unclear whether the performance is robust to this choice or whether it was tuned on the test set.

- **Choice of distillation layer is not ablated.** The paper uses features from "the convolution block of the last decoder" (Section 3.3) without comparing against alternatives (e.g., earlier decoder blocks, encoder features). A brief ablation would strengthen the design choice.

- **No variance or statistical significance is reported.** All quantitative results appear to be single runs. Given that the key comparisons involve small PSNR differences (often < 0.5 dB), reporting standard deviations across multiple seeds would bolster confidence that the improvements are systematic.

- **The 2-bit limitation is acknowledged but discussed too briefly.** The paper notes (Table 2, Section 4.3) that UFD "hurts performance" at 2-bit and is excluded, stating "the low capacity of 2-bit model limits knowledge transfer." This is an honest admission but deserves deeper analysis: does the FUM overfit? Is the distillation signal fundamentally mismatched at very low bit-widths? This is a genuine limitation that constrains the method's applicability.

- **Two minor experimental documentation gaps:** (i) The amplification ratio *r* used for input scaling is mentioned (Section 3.1) but its value is never specified. (ii) The computational overhead of the second set of quantization parameters in DSAQ is mentioned qualitatively but not quantified in FLOPs or runtime.

### Trivial
None.

## Nice-to-Haves

- A sensitivity analysis of the distillation weight λ₂ and a comparison of different FUM architectures (e.g., 1×1 conv vs. small MLP).
- Ablation on which decoder layer is used for distillation features.
- Quantized versions of lightweight LLIE architectures (LLPack, RRT) as additional baselines, to isolate quantization gains from architectural differences.
- Reporting results with standard deviations across multiple runs.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"The paper does not mention how the low-light raw images are packed (the standard 2×2 Bayer packing)."** — Factually incorrect. Section 3.1 explicitly states: "we pack each 2×2 pattern into four channels to ensure each channel represents the same color." This describes the standard Bayer packing. [Removed: factually wrong]

- **"The paper does not discuss the computational overhead of the second set of quantization parameters."** — The paper does acknowledge this in Section 3.2: "Compared with channel-wise quantizers ... our DSAQ is a more efficient approach as only one additional set of quantization parameters is introduced." While not quantified in FLOPs, the overhead is discussed. [Removed: partially addressed by the paper; downgraded to minor point above]

- **"The paper does not mention code release."** — Not a substantive weakness; many papers do not release code and this is not a requirement for evaluation. [Removed: not a valid weakness per guidelines]

- **"No statistical significance or variance is reported"** — This is retained as a Minor weakness rather than removed, since the PSNR differences are small and variance reporting would be appropriate for this community. However, the harsh critic's framing as a "missing parts" concern is softened.

- **Criticisms framed as speculative gaps** (e.g., "assuming Y is the case...", "if the normalization were X...") — No such speculative-fatal claims were present in the harsh critic's input; all major criticisms are grounded in what is and isn't on the page.

## Novel Insights

None beyond the paper's own contributions. The harsh critic correctly identifies the key tension: the method's core ideas are well-motivated and empirically supported, but the evaluation is weakened by incomplete documentation of both the FUM architecture and the baseline adaptation protocol. This is a common pattern in quantization papers — the design decisions are sensible, but the reproducibility and comparative rigor lag behind.

## Suggestions

1. **Specify the FUM architecture explicitly** — even a simple design (e.g., a 1×1 convolution followed by batch normalization and ReLU) would resolve the reproducibility gap. Alternatively, clarify if FUM is simply a learnable linear projection.
2. **Document baseline adaptation protocols** — state clearly whether all quantization baselines used the same training schedule, loss functions, teacher model, and hyperparameter search. A table showing the shared training configuration would suffice.
3. **Reframe the inference speed comparison** — present the 2.2× same-platform speedup (quantized vs. 16-bit float on NPU) as the primary efficiency claim, and clearly label the 33× figure as combining quantization + platform gains.
4. **Add standard deviations** across multiple seeds (e.g., 3 runs) to all quantitative results, especially given the small PSNR differences being compared.
5. **Fix the abstract** to say "comparable" rather than "comparable or superior" unless specific settings show statistically significant superiority.
6. **Add a sensitivity study** for the distillation weight λ₂ and the choice of distillation layer.
