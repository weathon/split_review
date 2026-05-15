Here is my consolidated review:

---

## Summary

This paper proposes Finite Scalar Quantization (FSQ), a drop-in replacement for vector quantization (VQ) in VQ-VAEs. Instead of learning a parameterized codebook and using nearest-neighbor lookup, FSQ projects the encoder output to a low-dimensional space (typically d ≤ 10), bounds each dimension with a tanh non-linearity, and rounds to a fixed set of values to obtain discrete codes. The resulting implicit codebook requires no auxiliary losses, no EMA, no codebook splitting, and no entropy penalties. The method is validated on MaskGIT for ImageNet class-conditional generation and on UViM for depth estimation, panoptic segmentation, and colorization, achieving competitive performance with significantly simpler training.

## Strengths

1. **FSQ matches VQ performance across diverse tasks with drastically simpler design.** The paper demonstrates this in two different architectural families (convolutional VQ-GAN + masked transformer for MaskGIT; transformer VAE + encoder-decoder transformer for UViM) across four tasks. The MaskGIT experiment on ImageNet 256×256 uses a well-tuned VQ baseline (codebook 1024, entropy loss, 81% usage) and yields nearly identical FID curves across CFG weights (Sampling FID 4.509 for VQ vs. 4.534 for FSQ). The UViM results show small degradations (≤3%) that are acceptable given the simplification gain.

2. **FSQ achieves near-100% codebook utilization without any codebook management tricks.** This is the paper's most compelling evidence: in the MaskGIT trade-off study (Fig. 2c), FSQ maintains ≥99% usage for codebook sizes up to 2¹⁴, while VQ drops below 50% beyond 2¹¹. For UViM depth estimation, VQ without codebook splitting achieves only 0.78% usage, whereas FSQ attains 99% with no splitting at all. The direct comparison of VQ with vs. without codebook splitting (RMSE 0.468 vs. 0.490, usage 99% vs. 0.78%) cleanly demonstrates that VQ's performance relies on an expensive trick that FSQ renders unnecessary.

3. **Clear, simple method with practical design guidance.** FSQ is easy to implement (a rounding operation with STE). Table 1 provides actionable recommendations for L-set configurations across common codebook sizes. The compression cost analysis (Fig. 2d) offers a principled explanation for why sampling FID saturates as codebook size grows, helping practitioners understand the method's limitations.

4. **Parameter reduction without degradation.** FSQ eliminates the parameterized codebook (e.g., 2M parameters for a 2¹²-size, 512-dim VQ codebook) and uses much smaller encoder/decoder projections. The paper explicitly tests adding capacity back and finds no gains, confirming that the removed parameters were unnecessary.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **The trade-off study (Figure 2) uses an undertuned VQ baseline for large codebooks.** The paper states (lines 245-246) that for VQ, "we only sweep the codebook size" while keeping the entropy loss weight and other hyperparameters fixed. VQ's behavior with large codebooks is known to be sensitive to the entropy loss strength, commitment loss weight, and EMA decay. Extending from codebook 2¹⁰ (standard MaskGIT size) to 2¹⁴ or 2¹⁶ without retuning these knobs likely penalizes VQ. This weakens the specific claim that FSQ *outperforms* VQ for large codebooks — what the study more reliably shows is that under a *fixed* training protocol, FSQ is more robust. The paper is transparent about the protocol, but the headline language ("VQ is actually worse for large codebooks") would benefit from a caveat. This does not undermine the paper's core contribution (FSQ as a simpler alternative that works competitively), because the well-tuned MaskGIT and UViM baselines already validate comparable performance in realistic settings.

2. **The comparison confounds quantization method with latent dimensionality.** FSQ uses d ≪ 10 latent dimensions while VQ uses d ≥ 512, leading to different encoder/decoder architectures. The paper acknowledges this (lines 83-84, 211-212) and reports exploring additional dense layers to compensate, finding no gains. However, no systematic controlled experiment is provided (e.g., a VQ with comparably small d, or an FSQ with larger d). It remains unclear whether FSQ's advantages stem from the fixed grid, the low dimensionality, or both. This does not invalidate the results but limits mechanistic understanding.

3. **Missing ablation for the Lᵢ ≥ 5 heuristic.** The paper asserts that "Lᵢ < 5 leads to subpar performance" (line 404) but provides no quantitative ablation to support this claim. Table 1 recommends specific configurations but does not report results for alternatives (e.g., [4,4,4] for 2⁶, or [3,3,3,3]). If the method is sensitive to this choice, the "simplicity" advantage diminishes because users must still search over L-set configurations. A sensitivity analysis for at least one task would substantially strengthen the paper.

4. **UViM results show a small but consistent degradation.** Across all three UViM tasks, FSQ is marginally worse: depth RMSE 0.473 vs. 0.468, panoptic PQ 43.2 vs. 43.4, colorization FID-5k 17.55 vs. 16.90. The paper accurately describes this as "competitive but marginally worse" (Table 2 caption), which is honest — but the consistency of the degradation (always lower-performing, never better) should temper claims about being a "drop-in replacement that works as well as VQ." In practice the differences are small enough to be acceptable, but they are not zero.

5. **No explanation for the precision-recall shift.** The paper observes that FSQ yields higher recall and lower precision than VQ in MaskGIT (Section 4.3) and introduces CFG to compensate. The paper does not explain *why* FSQ produces this shift. Understanding this could help users anticipate when CFG is needed and how to adapt the approach to new tasks.

### Trivial

- The term "drop-in replacement" (abstract, line 34, line 75) is slightly overstated: switching from VQ to FSQ requires changing the encoder's output dimension from ~512 to ≤10, which is not literally a drop-in change. The paper acknowledges this (line 176: "after appropriately adapting the output and input dimension"), so this is a clarity issue, not a factual error.

## Nice-to-Haves

- A controlled experiment with matched latent dimensionality (e.g., VQ with d=5 or FSQ with d=512) would help disentangle the effect of dimensionality from the quantization mechanism.
- A sensitivity analysis for different L-set configurations (as noted in weakness 3) would justify the heuristic.
- Visualizations (t-SNE/PCA) comparing how FSQ's implicit grid partitions the latent space vs. VQ's learned codebook could reveal whether FSQ codes are semantically organized.

## Removed Points

1. **"UViM results undermine the conclusion that FSQ works as well as VQ"** — Removed because the paper's own language ("competitive but marginally worse," "competitive performance") is appropriately hedged. The critic's characterization overstates the paper's claim.
2. **"FSQ has not been used outside of compression" claim from Strength Finder** — This is accurate and not a weakness; it was only raised as context by the harsh critic, not as a criticism.
3. **Several of the harsh critic's "Missing Experiments" and "Deeper Analysis Needed" suggestions** — These are aspirational rather than evaluative criticisms. Many (e.g., "test with ViT-VQGAN," "study d vs. L in more detail") go beyond the paper's stated scope and are better framed as future work suggestions than as weaknesses.

## Novel Insights

None beyond the paper's own contributions. The reviews surface no contradiction or unexpected pattern that the authors themselves did not identify.

## Suggestions

1. Add a controlled ablation for the Lᵢ ≥ 5 heuristic. Report results for at least one task with sub-5 configurations to substantiate the claim.
2. Conduct one controlled experiment holding latent dimensionality approximately constant (e.g., a VQ with d=5-10 and a learned codebook) to separate the effect of quantization mechanism from dimensionality. Even if this VQ collapses, the result would cleanly support the paper's mechanistic claims.
3. Add a brief discussion of why FSQ yields higher recall/lower precision in the MaskGIT setting — this would help practitioners anticipate when CFG adjustments are needed.
4. In the trade-off study discussion, add an explicit caveat that VQ hyperparameters were not tuned per codebook size, so the quantitative gap for large codebooks may be reduced with per-size tuning. This would preempt the most common criticism.

## Score and Decision

The paper makes a solid contribution: FSQ is a genuinely simpler alternative to VQ that achieves competitive performance across multiple vision tasks without auxiliary losses or codebook management tricks. The central evidence — that FSQ avoids codebook collapse, maintains high codebook utilization, and matches well-tuned VQ baselines — is convincing. The weaknesses are evidential gaps (undertuned VQ in the trade-off study, missing Lᵢ ablation, confounded dimensionality) rather than structural flaws, and they can be addressed in a camera-ready version. The paper is clearly written, the experiments are broad, and the practical utility is high.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>