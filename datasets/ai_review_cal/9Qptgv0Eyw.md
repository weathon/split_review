- Decision: Reject
- Avg Score: 3.40
- Scores: 5, 1, 3, 5, 3
Now I have all the information needed for a thorough verification. Let me compose the final consolidated review.

---

## Summary

This paper presents PtychoFormer, a hierarchical transformer-based model for ptychographic phase retrieval. The key ideas are: (1) an input scheme that groups multiple overlapping diffraction patterns into separate channels preserving their spatial relationships, (2) a Mix Transformer (MiT) encoder adapted from SegFormer with a convolutional decoder, (3) a feathering-based stitching algorithm to eliminate grid artifacts, and (4) a hybrid approach (ePF) that initializes ePIE with PtychoFormer's output for iterative refinement. The paper demonstrates improvements over older CNN-based methods (PtychoNN, PtychoNet) and over ePIE in terms of speed (2100–3600× faster), robustness to sparse scans, and reduction of global phase shift (via ePF).

## Strengths

- **Spatially-aware multi-pattern input scheme.** The paper devises an input scheme (Section 4, Fig. 3a) that groups up to nine overlapping diffraction patterns into separate channels ordered by their relative scan coordinates, explicitly preserving spatial relationships between patterns. This directly addresses a core limitation of prior DL methods (PtychoNN, PtychoNet) that process each pattern independently. Figure 4 shows PtychoFormer eliminates grid artifacts that plague single-pattern methods.

- **Well-motivated MiT encoder with domain-specific justification.** The paper identifies three specific limitations of standard ViT for ptychography — single-resolution features, quadratic self-attention cost, and resolution-sensitive fixed positional encoding — and adopts a MiT encoder with Spatial Reduction Attention, overlapping patch merging, and zero-padded Mix-FFN to address each (Section 4). This architectural reasoning is grounded in the task requirements (multi-resolution inputs from different scan configurations, need for positional information without fixed PE).

- **Quantified speed advantage.** PtychoFormer completes reconstruction in 0.14 seconds versus 5–8.5 minutes for ePIE on 18×18 diffraction patterns, a speedup of 2100–3600× (Section 5.2). This is a tangible practical advance that could enable real-time ptychographic imaging.

- **Hybrid ePF improves both quality and global phase shift.** ePF combines PtychoFormer's single-shot prediction as initialization for ePIE, achieving 73.59% and 47.30% NRMSE reduction for amplitude and phase over standalone ePIE (abstract). Figure 1 shows ePF nearly matches the ground truth phase profile while ePIE exhibits substantial global shift. Figure 7 documents consistent improvement across all lateral offsets.

- **Demonstrated robustness to sparse scan patterns across a wide overlap range (68.7% down to 14.9%).** The paper tests with lateral offsets from 20 to 60 pixels (Figs. 6, 7). PtychoFormer preserves structural integrity even at 14.9% overlap where ePIE produces severe artifacts, supporting practical reduction in data collection requirements.

- **Generalization demonstrated via zero-shot transfer and low-data fine-tuning.** Zero-shot testing on Flower102 and Caltech101 achieves NRMSE of 0.18/0.51 (amplitude/phase) and 0.28/0.97 respectively (Section 5.2). The model fine-tuned on only 2,000 samples for new probe functions and scan patterns shows little performance degradation, suggesting the encoder learns transferable ptychographic features.

## Weaknesses

### Fatal
None.

### Major

- **Missing experimental comparison against the most relevant transformer-based baseline (PtychoDV).** The paper explicitly cites PtychoDV (gan2024) in Related Work (line 81–82) as addressing the same limitation — that prior CNNs fail to capture spatial relationships between diffraction patterns — and even uses the same NRMSE metric formulation (line 166). Nevertheless, no experimental comparison against PtychoDV is conducted. The abstract claims "state-of-the-art phase retrieval in ptychography," but the evaluation omits the closest existing transformer-based method. Without this comparison, the paper cannot substantiate its strongest claim of being state-of-the-art, and readers cannot assess whether the claimed improvements are relative to only older CNN methods or represent genuine progress over the closest prior art.

- **No ablation studies isolating architectural contributions.** The method has several distinct design choices — MiT encoder (vs. a CNN encoder with the same decoder), the choice of nine input channels/patterns per group, the feathering algorithm, and the hierarchical multi-resolution encoder — none of which are disentangled. The paper uses "ablation study" (line 159) to refer to testing different scan scenarios (offsets, probes, datasets), not to architectural component analysis. Consequently, the reported performance gains cannot be reliably attributed to any specific design choice. For example, it is unknown whether the transformer encoder, the multi-pattern input scheme, or simply the stronger decoder drives the improvement over baselines.

### Minor

- **No error bars or statistical reporting on primary quantitative results.** Figure 4 (main DL comparison) and Figures 6–7 (comparison with ePIE across offsets) report only single-point averages over 3100 test samples, with no standard deviations, confidence intervals, or significance tests. The only variance reporting appears in the generalization results (§5.2, line 197) where mean ± std is given. Without error bars, the reader cannot assess whether the reported improvements over baselines are statistically meaningful or within noise.

- **Global phase shift advantage relies on training with absolute phase labels, which is not available in real-world ptychography.** The paper claims that PtychoFormer mitigates global phase shift because it is trained on ground-truth absolute phase (Section 4, line 226). However, real ptychographic data never has absolute phase ground truth. The Discussion acknowledges this challenge and suggests using calibrated measurements (line 248), but this creates a tension: the paper's central advantage over ePIE hinges on a training condition that cannot be replicated in practice without external calibration data. This significantly bounds the practical applicability of the claimed advantage.

- **Critical training and architectural details are missing.** The paper does not specify: which MiT variant was used (B0/B1/B2 from SegFormer?), the training hyperparameters (learning rate, optimizer, scheduler, number of epochs), the model parameter count, the depth and channel sizes of the convolutional decoder, or the spatial reduction ratios. The decoder is described only as upsampling multi-level features and refining resolution (line 103, 117–119). These details are essential for reproducibility and meaningful comparison.

- **Low-data generalization experiments lack baseline comparisons.** Section 5.2 reports that PtychoFormer fine-tuned on 2,000 samples shows "little to no degradation" on new scan patterns and probes, but no baselines (PtychoNN, PtychoNet, or PtychoDV) are fine-tuned under the same conditions. Without this comparison, the reader cannot determine whether the generalization property is specific to the transformer architecture or simply a consequence of fine-tuning a larger model from a good initialization.

- **Quantitative results for non-grid scan patterns are not reported.** The paper claims the input scheme has been tested on various scan patterns and with different numbers of diffraction patterns (line 98, referencing Fig. 3b which shows scan patterns). However, quantitative metrics broken down by individual scan pattern type are never presented. The claim of strong transfer learning across scan patterns rests only on a qualitative statement, not on supporting numbers.

- **The quality gap between single-shot PtychoFormer and ePF/ePIE on dense scans is acknowledged but not quantified.** The paper states "speed comes at the expense of quality" (line 254), and Figure 6 shows PtychoFormer's reconstructions have notably higher NRMSE (0.6–0.8) compared to ePF and ePIE (0.1–0.2) on dense scans. This gap is not discussed quantitatively, leaving the reader without a clear picture of the quality-speed tradeoff.

### Trivial

- It is unclear whether ePF refines the probe function in addition to the sample estimate, or relies on a fixed known probe — this should be clarified for real-world applicability.
- The speedup factor (2100–3600×) uses ePIE's convergence range of 800–1500 iterations; the paper would benefit from reporting median/mean runtime rather than just the extreme range.

## Nice-to-Haves

- **Run a controlled ablation replacing the MiT encoder with a ResNet or similar CNN encoder** (same input scheme, same decoder) to isolate whether the transformer or the multi-pattern input scheme drives the improvement.
- **Ablate the number of input channels** (e.g., 1, 3, 5, 9 patterns per group) to motivate the fixed choice of nine.
- **Quantitatively evaluate the feathering effect** by reporting metrics with and without it on the same test set (currently only qualitative, Fig. 3c).
- **Report runtimes of all methods on the same hardware** with consistent implementation details for a fairer speed comparison.
- **Provide training compute estimates** (GPU hours, model size, inference time breakdown) to help practitioners assess practical deployment costs.

## Removed Points

The following points from the harsh critic were removed or substantially weakened after cross-referencing with the paper:

1. **"The paper does not report whether baselines were trained to convergence"** — The paper states (line 186): "PtychoNN and PtychoNet are trained to convergence on the pre-training set." This criticism is factually incorrect.

2. **"Probe functions are simpler than real probes"** — This is speculative and not tied to a specific claim in the paper. The paper tests multiple probe shapes including unseen ones. Removed as unsupported speculation.

3. **"The 'tested on various scan patterns' near Figure 3(a) is a dangling claim"** — The reference is actually to Fig. 3b (the dataset figure showing scan patterns), and the fine-tuning experiments do test on new scan patterns. Weakened to a minor point about missing quantitative breakdown by pattern type rather than a "dangling claim."

4. **"Pure formatting/style nitpicks"** and **"typos/spelling/grammar"** — None present in the paper; any such artifacts are parser-induced.

5. **"The paper does not report performance at each offset individually for DL baselines"** — This is true but is a minor reporting preference, not a weakness that threatens the paper's claims.

## Novel Insights

The most interesting observation emerging from the reviews is the tension between the paper's two central framing devices. On one hand, the paper claims that transformers are uniquely suited for ptychography because they capture long-range spatial dependencies that CNNs miss. On the other hand, the multi-pattern input scheme (grouping nine patterns into nine channels) may itself be responsible for most of the improvement, independent of the transformer backbone — a CNN with the same 9-channel input could potentially achieve comparable results. The absence of an ablation to disentangle these two factors means we cannot evaluate the paper's core architectural claim. A second noteworthy tension is between the paper's practical motivation (real-time imaging of real samples) and its evaluation setting (simulated data with ground-truth absolute phase). The global phase shift advantage — arguably the paper's most impactful claimed improvement — is demonstrated only in the simulation regime where absolute phase is available for training. The paper is transparent about this limitation, but it significantly constrains the direct applicability of the claimed result.

## Suggestions

1. **Add a systematic experimental comparison against PtychoDV** using the same training/testing protocols. This is the single most important addition needed to substantiate the "state-of-the-art" claim.
2. **Perform ablations isolating the MiT encoder (vs. a CNN encoder), the number of input channels (1, 3, 5, 9), and the feathering module** to allow readers to attribute the performance gains to specific design choices.
3. **Report standard deviations or confidence intervals for all main metrics** — especially Figure 4 and Figures 6–7. With 3100 test samples, computing error bars is straightforward.
4. **Add training hyperparameters** (learning rate, optimizer, scheduler, epochs, model parameter count) to the Training Details section for reproducibility.
5. **Explicitly discuss the gap between single-shot PtychoFormer and ePF** (quantified visually in Figure 6) in the quantitative results to frame the quality-speed tradeoff clearly.
