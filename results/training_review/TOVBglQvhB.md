Now I have all the information I need. Let me write the consolidated review.

## Summary

This paper tackles low-bit quantization (2–4 bits) for raw-based low-light image enhancement (LLIE) models that use U-Net architectures. It identifies two obstacles: (1) distribution mismatch between encoder and decoder features in skip connections, and (2) the representation-capability gap between low-bit and full-precision features. To address these, the authors propose Distribution-Separative Asymmetric Quantization (DSAQ), which applies separate quantization parameters to encoder and decoder features before concatenation, plus an asymmetric activation quantizer with learnable offset. They further introduce Uniform Feature Distillation (UFD) with a trainable Feature Uniform Module (FUM) to bridge the capacity gap. Experiments on SID and MCR datasets show that the method outperforms six prior quantization approaches at 3–4 bits, with a 4-bit model approaching full-precision performance while reducing model size by 87.5% and FLOPs by 86.6%.

## Strengths

1. **Well-motivated analysis of U-Net quantization obstacles.** The paper provides empirical evidence (Figure 3's histogram analysis) that encoder and decoder features in U-Net skip connections have substantially different value ranges, and that LeakyReLU activations exhibit skewed distributions (Figure 2). These observations genuinely motivate the proposed DSAQ design, and the problem framing is clear and specific to the U-Net structure common in LLIE.

2. **DSAQ is a simple, principled, and effective modification for U-Net quantization.** The idea of applying separate quantization parameters to encoder and decoder features before concatenation is intuitive and directly addresses the identified problem. The ablation study (Table 2) confirms that distribution-separative quantization alone improves PSNR across all bit-widths (e.g., from 24.10 to 24.57 at 2-bit with the asymmetric component). The asymmetric activation quantizer also shows clear benefit, especially at lower bit-widths.

3. **Strong 4-bit and competitive 3-bit results with meaningful compression.** The 4-bit quantized model achieves near full-precision performance on both SID and MCR datasets (Table 1), while delivering 87.5% size reduction and 86.6% FLOPs reduction. The method consistently outperforms six prior quantization methods (Dorefa, PACT, PAMS, LSQ, LLT, QuantSR) across 2/3/4-bit settings on both datasets, providing solid evidence of practical value.

4. **Uniform Feature Distillation outperforms vanilla distillation.** The ablation (Table 3) shows that UFD with the FUM module improves over the vanilla PAMS distillation baseline (e.g., 25.79 vs. 25.69 at 4-bit and 24.96 vs. 24.88 at 3-bit), validating the claim that projecting low-bit features into the teacher's feature space via a trainable module reduces representation disparity.

5. **Real-device latency measurement.** The paper measures inference speed on a Qualcomm Snapdragon 8 Gen 3 NPU, showing 2.2× speedup over 16-bit float on NPU and 33× over 32-bit float on GPU (Table 4). This provides concrete deployment evidence, even though the hardware configuration (4w/8a) does not fully match the paper's target regime.

## Weaknesses

### Fatal
None.

### Major

1. **Missing experimental comparison with channel-wise quantization (DAQ).** The paper motivates DSAQ by the distribution mismatch in skip connections and explicitly claims that DSAQ is "more efficient" than channel-wise quantizers (DAQ, Hong et al., 2022) because it adds only two sets of parameters per skip connection rather than C sets. However, DAQ is never compared experimentally. Since a channel-wise quantizer also handles per-group distribution differences, it is the most directly relevant baseline for assessing whether DSAQ's grouped approach is genuinely advantageous or merely a minor variant. Without this comparison, the claimed advantage over channel-wise quantization is unsubstantiated, and the core novelty is partially unverified.

2. **The method does not adequately handle 2-bit quantization, which the paper's scope claims to address.** The paper frames its contribution as covering "2–4 bits" (title, abstract, introduction), but the method performs poorly at 2-bit, with large PSNR/SSIM drops from full-precision. Critically, the authors explicitly exclude their own distillation technique at 2-bit because "the low capacity of 2-bit model limits knowledge transfer even with the feature uniformity module." This admission means the proposed UFD component — one of the two main contributions — cannot operate at the most challenging bit-width the paper sets out to address. While the 2-bit limitation is acknowledged, the title and framing ("Low-bit Quantization for Seeing in the Dark" without qualification) are misleading, as the evidence primarily supports 4-bit and, to a lesser extent, 3-bit.

3. **The architecture of the Feature Uniform Module (FUM) is not specified, harming reproducibility.** The paper describes FUM only as a "full-precision feature uniform module" that "projects the low-precision feature to a uniform space" and is "excluded during inference," but never states whether it is a single convolution layer, an MLP, a sequence of blocks, or something else. Without this detail, readers cannot reproduce the method, and it is unclear whether the observed improvement stems from principled feature alignment or simply added network capacity. Given that FUM operates in full-precision during training, it could be absorbing distribution differences through brute force rather than through the claimed alignment mechanism.

### Minor

1. **Hardware evaluation does not validate the full low-bit regime advocated by the paper.** Table 4 measures latency on a Snapdragon NPU using 4w/8a quantization (activations remain 8-bit), not the 2–4 bit full quantization (weights + activations) that the paper's contributions target. The compression ratios (86.6% FLOPs reduction for 4-bit) are computed via a theoretical bit-ops model, not measured on hardware that uses low-bit activations. The paper acknowledges this ("most devices currently do not support 3-bit or 2-bit"), but this limitation means the practical motivation — accelerating models on resource-limited devices with full low-bit quantization — is not actually validated. The claimed benefits of the asymmetric activation quantizer and UFD are not reflected in the hardware numbers.

2. **No statistical significance or variance reported.** The results in Table 1 do not report standard deviations or whether multiple runs were performed. Given the small differences between methods at 4-bit (e.g., 28.76 vs. 28.50 PSNR on SID Sony), it is unclear whether the reported improvements are statistically meaningful. This is a standard expectation for reproducibility that should be addressed.

3. **The paper does not analyze why distillation fails at 2-bit.** The authors exclude UFD for 2-bit with a brief statement about "low capacity" limiting knowledge transfer, but provide no analysis or ablation that explains the failure. Understanding whether the issue lies in the FUM's capacity, the quantization granularity, or some other factor would clarify the method's limits and guide future work.

4. **The comparison with lightweight full-precision LLIE models (LLPack, RRT) is tangential.** These are alternative efficiency strategies, not quantization baselines, and comparing against them adds limited insight beyond showing that quantization can outperform lightweight architectures — which is already well established in the quantization literature. This space could be better used for the missing DAQ comparison.

### Trivial
None.

## Nice-to-Haves

- **Post-quantization distribution visualization.** Showing histograms of quantized activations under DSAQ vs. symmetric/channel-wise quantization would visually confirm that DSAQ better preserves both encoder and decoder distributions, strengthening the motivation.
- **Sensitivity analysis of DSAQ grouping granularity.** How would results change with different numbers of groups (e.g., 2 groups vs. 4 groups vs. per-channel)? Understanding this trade-off would strengthen the contribution by showing that the encoder/decoder grouping is optimal.
- **Simulation-based latency estimates for full 4-bit (w4a4) quantization.** Even if hardware doesn't support it, simulating the latency impact of full low-bit activations would help validate the claimed efficiency benefits.

## Removed Points

- **Criticism that "the phrase 'comparable or superior results to full-precision counterparts' only holds for 4-bit" is presented as an over-generalization.** The paper's abstract specifically says "Our 4-bit quantized model can achieve comparable or superior results to full-precision counterparts" — this claim is explicitly qualified to 4-bit. The critic misreads this as an unqualified claim about all low-bit settings.
- **Criticism that comparing with lightweight models is "odd."** The paper presents this as an *additional* comparison (not a primary one) to show that quantization can outperform dedicated lightweight architectures. This is a valid extra data point, not a weakness. While tangential, it does not harm the paper.
- **Criticism about "missing experiments on other low-level vision tasks" (denoising, HDR).** The paper's scope is explicitly raw-based LLIE. Extending to other tasks is future work, not a core weakness.
- **Criticism about "no comparison to attention transfer, contrastive distillation" for UFD.** The paper compares against the most directly relevant baseline (PAMS vanilla feature distillation). Requesting a broad survey of distillation methods is scope creep.
- **Generic strength from Strength Finder about "comprehensive evaluation against multiple quantization baselines"** — this is properly a strength, but the Strength Finder's wording is generic. Kept in spirit but reworded.

## Novel Insights

The most interesting observation emerging across the reviews is the asymmetric behavior of the method across different bit-widths: DSAQ helps at all bit-widths (the distribution-separative strategy is architecture-agnostic), while UFD works at 3–4 bits but *hurts* at 2 bits to the point where it must be excluded. This suggests that the FUM module may itself require a minimum level of feature fidelity to learn a meaningful projection — at 2 bits, the quantization noise may be so severe that any learned mapping from student to teacher space is ineffective or even damaging. This differential efficacy across bit-widths is worth investigating further, as it implies that 2-bit quantization may require fundamentally different strategies (e.g., novel architecture designs, mixed-precision allocation) rather than distillation-based remedies.

Additionally, the reviewers converge on the observation that DSAQ's advantage over a straightforward channel-wise quantizer remains unverified, which is the single most consequential gap in the paper's evaluation. If DSAQ's grouped approach proves superior to per-channel quantization *without* requiring significantly more parameters, that would be a genuinely useful finding for the broader U-Net quantization community.

## Suggestions

1. **Add an experimental comparison with DAQ (channel-wise quantization) as the primary missing baseline.** This is essential to substantiate the claim that DSAQ is a better or more efficient approach than per-channel quantization for handling distribution mismatches in skip connections. Report both accuracy and parameter count.

2. **Narrow the framing to reflect what the method actually achieves.** Either (a) change the title and abstract to focus on "3–4 bit quantization" and acknowledge 2-bit as a limitation, or (b) include an analysis of why 2-bit fails and a clear path toward improvement, and keep the current scope only if the method is shown to work at 2-bit with UFD.

3. **Specify the FUM architecture explicitly** (e.g., "a single 1×1 convolution with ReLU" or "a 3-layer MLP with hidden dimension 256"). Provide enough detail for exact reproducibility. If the FUM is a standard component, cite its origin clearly.

4. **Report variance** (at least 3 runs with mean and std) for the main results in Table 1, especially for the 4-bit setting where differences between methods are small.

5. **Add measured or simulated latency for full 4w4a quantization** to validate that the proposed components (especially the asymmetric activation quantizer) actually translate to speed on hardware. If no hardware supports it, use an established cycle-accurate simulator.

## Score and Decision

The paper addresses a relevant problem (efficient deployment of LLIE models) and proposes two sensible, well-motivated components (DSAQ and UFD) that are validated through ablation studies. The 4-bit results are strong and the method consistently outperforms existing quantization approaches on two datasets. However, the evaluation has significant gaps — most critically, the missing comparison with channel-wise quantization (DAQ) undermines the claimed novelty of DSAQ, and the hardware validation does not match the paper's stated low-bit regime. The method also does not adequately handle 2-bit quantization, despite the broad scope implied by the title. These issues are addressable in a revision but weaken the contribution in its current form.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>