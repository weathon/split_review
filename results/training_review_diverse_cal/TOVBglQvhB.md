Now I have all the information needed. Let me compose the consolidated review.

---

## Summary

This paper proposes a low-bit quantization method tailored for U-Net-based raw low-light image enhancement (LLIE). It introduces two components: (1) a Distribution-Separative Asymmetric Quantizer (DSAQ) that separately determines quantization intervals for encoder and decoder features before skip-connection concatenation, and (2) a Uniform Feature Distillation (UFD) scheme that projects low-bit student features through a Feature Uniform Module (FUM) to narrow the representation gap with a full-precision teacher. Experiments on SID and MCR datasets show the method outperforms several existing quantization approaches (Dorefa, PACT, PAMS, LSQ, LLT, QuantSR) at 2–4 bit widths while achieving substantial model compression (87.5% size reduction at 4-bit).

## Strengths

1. **Distribution-separative quantization is well-motivated and empirically validated.** The paper identifies a genuine problem specific to U-Net architectures in LLIE — that encoder and decoder features concatenated via skip connections have markedly different value ranges (Figure 3). The DSAQ solution is simple and principled: separate scaling factors for each branch before concatenation. The ablation (Table 2) confirms that this design choice consistently improves PSNR (e.g., +0.34 dB at 4-bit on SID-Sony), directly supporting the core claim.

2. **Uniform feature distillation shows clear gains over vanilla distillation.** Table 3 demonstrates that UFD outperforms the structured knowledge transfer from PAMS by 0.75 dB (3-bit) and 0.54 dB (4-bit) on SID-Sony. This provides concrete evidence that projecting low-bit features through the FUM before computing the distillation loss is more effective than directly aligning normalized features.

3. **State-of-the-art results among compared quantization methods on raw LLIE.** On both SID and MCR datasets across 2-, 3-, and 4-bit settings, the proposed method achieves the highest PSNR/SSIM among all compared quantizers (Dorefa, PACT, PAMS, LSQ, LLT, QuantSR), while reducing model size by up to 93.7% and FLOPs by up to 95.5% (Table 1). The improvements over LSQ on MCR are quantified in-text (e.g., +0.98 dB at 4-bit).

4. **Systematic ablation study.** Table 2 disentangles the contributions of each component (distribution-separative quantization, asymmetric activation quantizer, uniform feature distillation) across bit-widths, revealing nuanced trade-offs: the asymmetric quantizer helps more at 2-bit, while distribution-separative strategy is more impactful when more quantization bins are available.

5. **Real-device latency benchmarking.** Table 4 reports a 2.2× speedup on a Snapdragon 8 Gen 3 NPU relative to 16-bit floating-point, demonstrating practical deployability on edge hardware.

## Weaknesses

### Fatal
None.

### Major

1. **The Feature Uniform Module (FUM) architecture is never specified.** The paper describes FUM as a "full-precision feature uniform module" that "projects the low-precision feature to a uniform space" and is "removable at inference time" (Section 3.3), but never states what the module actually is — a single linear layer, a 1×1 convolution, a residual block, an MLP? The reader is given the loss function involving FUM but cannot reproduce the method or assess whether the reported gains come from the proposed alignment mechanism or from an ad-hoc transformation that could introduce confounding capacity. This is a structural omission that directly impacts reproducibility and verifiability of a claimed core contribution.

2. **Missing comparison against channel-wise quantization (DAQ) despite directly claiming superiority.** In Section 3.2, the paper states: "Compared with channel-wise quantizers Hong et al. (2022) that learn parameters for each channel of the activations, our DSAQ is a more efficient approach as only one additional set of quantization parameters is introduced." This is a direct claim that DSAQ is more efficient than channel-wise methods like DAQ. Yet DAQ is not included in any experiment (Table 1). Since DSAQ's main selling point is efficiently handling U-Net's distribution mismatch, the most relevant competitor is a method that learns per-channel quantization parameters. Without this comparison, the reader cannot tell whether DSAQ's advantage comes from its distribution-separative design or from other factors (asymmetric quantization, distillation), nor whether the efficiency claim holds.

### Minor

1. **Overstated "comparable to full-precision" claim.** The abstract and conclusion claim that the "4-bit quantized model can achieve comparable or superior results to full-precision counterparts." While the paper demonstrates strong results, the actual PSNR gap (not directly stated in text but implied by the comparison methods table) is non-trivial. A more precise characterization — e.g., "competitive for deployment" or acknowledging the gap while explaining when it is acceptable — would better serve readers than the current phrasing, which risks overstating the results.

2. **Distillation component fails at 2-bit, limiting scope of the claimed unified solution.** The paper acknowledges (Section 4.3) that "the low capacity of 2-bit model limits knowledge transfer even with the feature uniformity module" and that distillation is excluded at 2-bit. However, the abstract and contributions present the method as a unified 2–4 bit solution. Since UFD is listed as a main contribution and the 2-bit setting is where compression is most aggressive (and arguably most important), this limitation deserves more prominent qualification — e.g., explicitly noting in the abstract or introduction that the distillation technique is applicable for 3–4 bit settings.

3. **Adaptation details for comparison methods are not provided.** The paper compares against six prior quantization methods (Dorefa, PACT, PAMS, LSQ, LLT, QuantSR) but does not explain how each was adapted to the U-Net backbone. Whether these were taken from official implementations, re-implemented, or modified affects confidence in the relative rankings. Adding a brief implementation note (or citing specific code repositories) would improve reproducibility.

### Trivial
None.

## Nice-to-Haves

- **Clarify weight quantization details**: the paper says weights use a symmetric quantizer (Eq. 1) but does not specify whether per-layer or per-channel scaling is used.
- **Distillation at multiple decoder stages**: the paper only distills the last decoder feature. An ablation on whether earlier decoder features also benefit from distillation would be informative but is not required to validate the core contribution.
- **Justification for spatial mapping before distillation**: the paper sums squared feature maps across channels before computing the distillation loss, collapsing the channel dimension. A brief justification for this design choice (vs. per-pixel cross-channel loss) would be helpful.
- **Latency numbers for the actual 2–4 bit targets**: the paper acknowledges this limitation but it would strengthen deployment claims.

## Removed Points

- **"Garbled figure captions"** — Removed per hard rules: pure formatting artifacts are parser errors, not author errors.
- **"Latency evaluation uses 4w/8a not 2–4 bit"** — The paper explicitly acknowledges this limitation ("most devices currently do not support 3-bit or 2-bit") and frames the experiment appropriately. This is a practical constraint, not a methodological flaw.
- **"Distillation at multiple decoder stages" / "pixel-distillation vs feature-distillation" / "weight quantization details"** — These are suggestions for additional experiments, not weaknesses. They ask the authors to expand the paper's scope beyond what is needed to validate the core claims.

## Novel Insights

The most novel observation from this review is the tension between the claimed generality of the distillation component and the empirical finding that it actively harms performance at 2-bit. This reveals that the "capacity gap" between student and teacher is not monotonic in bit-width — there is a qualitative regime change below 3 bits where alignment-based distillation becomes counterproductive, likely because the student's representational capacity is too constrained to even coarsely match the teacher's feature space. This suggests that future work on extremely low-bit quantization (≤2 bits) for LLIE may need fundamentally different knowledge transfer mechanisms (e.g., targeting intermediate representations or using task-level losses) rather than feature-space alignment. A second insight is that the paper's main contribution (DSAQ) is actually the more robust and general component — it helps across all bit-widths — while UFD is narrower in applicability. The paper could be strengthened by foregrounding this asymmetry.

## Suggestions

1. **Specify the FUM architecture** with enough detail to replicate it (e.g., "a single 1×1 convolutional layer with batch normalization and ReLU, outputting C channels" or similar). This is the most impactful single fix.
2. **Add a comparison against DAQ (or a re-implemented channel-wise quantizer)** on the same backbone at 4-bit (or across bit-widths). This would directly validate the claim that DSAQ's efficiency-vs-performance trade-off beats per-channel quantization.
3. **Re-calibrate the "comparable to full-precision" language** to honestly reflect the measured PSNR/SSIM gaps, and discuss under what deployment constraints those gaps are acceptable.
4. **Qualify the 2-bit scope in the abstract**: note that UFD is applied at 3–4 bits, while DSAQ alone handles the 2-bit setting.
5. **Add a brief implementation note** for how each comparison method was adapted to the U-Net backbone, ideally with repository references.

## Score and Decision

**Originality:** Solid — the distribution-separative idea is simple but well-targeted to the U-Net + LLIE setting, and the paper identifies a genuine underexplored problem (quantization for raw-based LLIE).

**Importance:** High — deploying LLIE on edge devices (cameras, smartphones) is practically relevant, and the paper addresses a real obstacle (U-Net distribution mismatch) that generic quantizers don't handle.

**Claims support:** Mixed — the core empirical claims (DSAQ + UFD beats other quantizers) are well-supported. However, the claim of efficiency over channel-wise quantization is unvalidated, and the "comparable to full-precision" characterization is somewhat overstated.

**Soundness:** Generally sound experiments with proper ablations and two datasets, but undermined by the unspecified FUM architecture (affecting verifiability) and the missing DAQ baseline.

**Clarity:** Generally clear, though the FUM omission is a significant gap.

**Value:** The paper offers a practical recipe for quantizing U-Net LLIE models that demonstrably works. Once the architectural specification and missing baseline are addressed, the contribution is solid and actionable.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>