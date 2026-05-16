Now I have a thorough understanding of the paper. Let me compose the final consolidated review.

## Summary

This paper proposes a low-bit quantization method for raw-based low-light image enhancement (LLIE) using U-Net architectures. The core contribution — Distribution-Separative Asymmetric Quantizer (DSAQ) — is a simple, well-motivated idea: applying separate quantizers to encoder and decoder features before skip-connection concatenation, since these features have distinctly different value ranges. A secondary contribution is Uniform Feature Distillation (UFD), which uses a Feature Uniform Module (FUM) to help the low-bit student model mimic full-precision features. Experiments on SID and MCR datasets show consistent improvements over several quantization baselines, with real-device latency measurements on a Qualcomm Snapdragon NPU.

## Strengths

- **Distribution-separative quantizer solves a concrete U-Net quantization problem**: The paper identifies that encoder and decoder features have different value ranges before skip-connection concatenation (Figure 3), and proposes separate quantizers for each. This is simple, well-motivated, and validated by the ablation study (Table 2) where the separation consistently improves PSNR across 2–4 bit settings.

- **Asymmetric activation quantizer is empirically motivated by LeakyReLU-induced skewness**: The paper measures activation skewness (~1.5–3.0, Figure 2a) compared to near-symmetric weights, and the ablation confirms the asymmetric quantizer helps especially at lower bit-widths (Table 2).

- **Consistent SOTA comparisons on two raw-LLIE datasets**: Evaluated against six recent quantizers (Dorefa, PACT, PAMS, LSQ, LLT, QuantSR) across 2–4 bits on SID and MCR. The method achieves the highest PSNR/SSIM in every setting (Table 1), with margins over LSQ reaching 0.98 dB / 0.0233 on MCR at 4-bit.

- **Ablation systematically disentangles component contributions**: Table 2 separately ablates distribution-separative quantization, asymmetric quantizer, and UFD across three bit-widths. The honest reporting that UFD harms 2-bit performance is a valuable empirical finding.

## Weaknesses

### Fatal
None.

### Major
None. The paper's core claims are supported by evidence; no structural flaw invalidates the main contribution.

### Minor

- **The hardware latency experiment (Table 4) uses a different quantization regime than the main experiments**: The paper evaluates 4w/8a (4-bit weights, 8-bit activations) on the NPU, while the main results (Table 1) use equal bit-widths (2w/2a, 3w/3a, 4w/4a). The paper acknowledges that "most devices currently do not support 3-bit or 2-bit," which is fair, but the efficiency benefit of the paper's aggressive *activation* quantization is not directly demonstrated on hardware. The speedup shown (2.2× vs FP16) primarily reflects weight quantization, which is not the technically challenging part of the contribution.

- **The Feature Uniform Module (FUM) architecture is underspecified**: Section 3.3 describes FUM only as "a full-precision feature uniform module" that "can be excluded during inference" but provides no architectural details — number of layers, type of layers (conv/MLP), input/output dimensions, or training procedure. While FUM is not needed at inference (so the main DSAQ method is reproducible), the distillation results in Table 3 depend on it. Without specification, others cannot reproduce the UFD contribution independently.

- **The improvement from Uniform Feature Distillation is modest and not statistically justified**: Table 3 shows that adding UFD to DSAQ yields gains of only 0.09 dB (4-bit) and 0.07 dB (3-bit) on SID-Sony. No multiple runs or confidence intervals are reported. However, it is worth noting that UFD outperforms the vanilla PAMS distillation by a more substantial 0.40 dB (4-bit) and 0.68 dB (3-bit), so the primary value of UFD may be as a superior distillation scheme relative to prior work rather than a large absolute improvement.

- **Slight overclaim in the abstract**: The claim that "our 4-bit quantized model can achieve comparable or superior results to full-precision counterparts" is not fully supported — on SID-Sony (28.64 vs 28.24) and MCR (27.28 vs 27.15), the full-precision model still leads. "Comparable" is reasonable but "superior" is not supported by the data.

- **The asymmetric quantizer itself is a standard component** (learnable scale/offset affine quantizer, similar to PACT/LSQ). The novelty of DSAQ lies in the *grouping strategy* (separate quantizers for encoder/decoder features), not in the asymmetric quantizer formulation. The paper should be clearer about what is novel vs. adopted from prior work.

### Trivial
- Model size and FLOPs are reported only as percentages in text; a dedicated table with absolute numbers (full-precision size, 4-bit size, FLOPs) would improve readability.
- No sensitivity analysis for the loss weighting hyperparameters (λ₁=1, λ₂=100).
- The soft gradient transformation function is cited to QuantSR but not described; a brief explanation would help self-containedness.

## Nice-to-Haves
- A direct empirical comparison with channel-wise quantizers (e.g., DAQ) would strengthen the claim that DSAQ is more efficient. Currently, DAQ is only discussed in Related Work.
- Testing on another U-Net-based LLIE architecture (e.g., from MCR or DNF) would demonstrate generality beyond the SID U-Net.
- A visual analysis of the learned scale factors for encoder vs. decoder features would deepen the central observation.

## Removed Points
These points are flagged to be removed — treat them with caution:
- *"The paper should also cover other architectures / domains"* — scope creep; the paper is about quantizing a specific U-Net for raw LLIE.
- *"The asymmetric quantizer is not new"* — this is recast as a minor clarity issue (the paper adopts prior ideas), not a structural weakness. The grouping strategy is the novelty.
- *"Baseline quantizers may not have been re-optimized"* — unfalsifiable speculation without evidence that baselines were disadvantaged.
- *"Missing related works"* — cannot be verified without external sources.

## Novel Insights
None beyond the paper's own contributions. The reviews surface that DSAQ's key insight — that the U-Net skip-connection concatenation creates a distribution mismatch that a single quantizer cannot handle — is simple and practically effective. The reviews also highlight that the UFD component, while directionally correct, provides modest absolute gains and would benefit from stronger empirical support.

## Suggestions
1. Specify the FUM architecture in full (layers, dimensions, training procedure) in a brief paragraph or appendix.
2. Align the hardware experiment with the quantization regime studied in the main tables, or add a discussion of estimated BOPs savings to bridge the gap.
3. Add multiple-seed runs with standard deviations for the key distillation ablation (Table 3) to establish statistical significance of the UFD improvement.
4. Temper the "comparable or superior" claim to "comparable" throughout.
5. Add a table of absolute model sizes and FLOPs alongside the compression percentages.

## Score and Decision

The paper presents a solid, well-motivated core contribution (DSAQ) that is consistently validated across datasets and bit-widths. The weaknesses are real but minor — none undermine the central claim that distribution-separative quantization improves low-bit U-Net quantization for raw LLIE. The UFD contribution is weaker but still shows improvement over prior distillation methods. The paper is acceptable with minor revisions.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>