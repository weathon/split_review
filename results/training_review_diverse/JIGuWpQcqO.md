I've thoroughly verified the paper content against the reviewer claims. Let me now produce the consolidated review.

## Summary

This paper proposes RDNet, a reversible decoupling network for single-image reflection removal (SIRR). The architecture has two main innovations: (1) a multi-column reversible encoder (MCRE) that uses intra- and inter-level reversible connections to preserve hierarchical semantic information during feature propagation, avoiding information bottleneck issues in prior dual-stream networks; and (2) a transmission-rate-aware prompt generator (TAPG) that learns per-channel α,β parameters and uses them to modulate features dynamically via learned prompts. The method achieves state-of-the-art results on five benchmark datasets, with notable gains on challenging cases (e.g., +1.67 dB PSNR over the next best on Real20 with Nature data).

## Strengths

1. **Consistent SOTA results across all benchmarks.** RDNet achieves new records on all five datasets under both training settings (with and without Nature data). On the four-dataset average with Nature data, RDNet reaches 26.65 dB PSNR vs. 25.75 dB for DSRNet (the next best), a gain of 0.90 dB (Table 1). On Real20 specifically, the gain is 1.67 dB over the second-best method. These gains are substantial for this well-populated benchmark.

2. **Ablation study validates the reversible design empirically.** Replacing the reversible connections with standard U-Net connections (Setting F, Table 4) causes a 2.6 dB drop in average PSNR. This is a large delta that directly confirms the necessity of the invertibility design for reflection removal.

3. **Prompt generator ablation shows clear contribution.** Removing all transmission-rate-aware techniques (Setting A) drops performance by 1.13 dB, while the prompt-only variant (Ours, Setting C→B comparison) shows that the prompt mechanism outperforms simple input-side adjustment (0.47 dB gain over no-prompt, and 0.62 dB over direct input adjustment).

4. **Qualitative results demonstrate genuine practical robustness.** Figures 4–5 show RDNet removing strong, dense reflections that competing methods leave largely intact, including in-the-wild examples captured by the authors (car windows, etc.), supporting the claim of real-world generalization beyond benchmark datasets.

## Weaknesses

### Fatal
None.

### Major

1. **The claimed 24.34 dB PSNR from the prompt generator alone is insufficiently supported.** Section 3.2 (line 124) states that using the six estimated parameters from the prompt generator achieves 24.34 dB average PSNR across four datasets, *"surpassing the previous state-of-the-art method by Dong et al."* (which achieves 24.21 dB with a full network). This claim is remarkable — a simple per-channel linear adjustment outperforming a trained neural network — but the paper provides no experimental protocol. It does not specify exactly how the six parameters produce an output image (presumably (I−β)/α per channel), whether clipping is applied, whether the comparison is fair (Dong et al.'s 24.21 dB is the "w Nat." setting, but the prompt generator was also trained on Nature data in stage 1), or even that this was computed on the same test sets under the same conditions. The claim appears in the methodology section and is never revisited in the experiments. This undermines credibility and should either be moved to the experiments with full protocol details or removed.

### Minor

2. **The "information lossless" claim slightly overstates what is demonstrated.** Equations 4–5 define a reversible connection where F_j^{i-1} can be retrieved given F_j^i, F_{j-1}^i, F_{j+1}^{i-1}, ω, θ, δ, and the invertibility of γ. The paper claims this connection is "information lossless" (line 110). However: (a) the invertibility of γ (implemented as "learnable reversible channel-wise scaling") is not verified — if any learned scale factor is zero, γ is not invertible; (b) no empirical reconstruction error is shown to verify losslessness in practice. The strong ablation result (2.6 dB drop in Setting F) convincingly shows that the reversible design is *beneficial for information retention*, which is sufficient. The paper should rephrase the claim to "information-preserving" or "reversible-by-construction" and either verify γ's invertibility or note the non-zero assumption.

3. **The ablation study does not state which data setting it uses.** The ablation table (Table 4) reports "Ours" at 26.65 dB, which matches the "w Nat." setting in Table 1, but the text (Section 4.3) never explicitly states this. Readers comparing against the "w/o Nat." setting (25.95 dB) could be confused about the baseline. The paper should state clearly that ablations use the additional Nature data.

4. **The dual-stream ablation (Setting D) drops only 0.28 dB — the paper should discuss significance.** The paper interprets this as confirming "the superiority of our decoupling design," but a 0.28 dB difference across four datasets could fall within evaluation noise, especially since Setting D uses "double computation." A brief discussion of variance or statistical significance would strengthen this claim.

5. **The Nature dataset result (Table 2) shows best PSNR but second-best SSIM.** The paper acknowledges this (line 206) but offers no explanation for why the method trades a small amount of structural fidelity (0.004 SSIM below Zhu et al.) for pixel-level accuracy. A brief comment would be helpful.

6. **The Pretrained Hierarchy Extractor (PHE) is under-described in the methodology.** The PHE is described functionally (line 88) but its architecture is only revealed in the implementation details ("initialized by a pretrained FocalNet," line 159). The methodology section should specify what features at what resolutions are extracted and how they feed into the first column.

### Trivial
None.

## Nice-to-Haves

- A single-column RDNet ablation (removing the multi-column ensemble but maintaining the reversible design) would directly isolate the benefit of the column ensemble beyond what Setting D (dual-stream) tests.
- A brief sensitivity analysis of the perceptual loss weight (w=0.01) would strengthen the experimental section.
- The paper could report whether the learned γ scaling factors are empirically bounded away from zero, to support the invertibility claim.

## Removed Points

- **Criticism about "not stored" features for reverse operation (Critical Issue 2, part 1):** The critic claimed that F_{j-1}^i and F_{j+1}^{i-1} "are not stored unless special mechanisms are used." In the sequential column processing (column 1→N, levels bottom-up within each column), these features are computed before F_j^i in the forward pass and are available for a reverse computation without special storage. This part of the critique is incorrect. *However, the valid concern about γ's invertibility (the rest of Issue 2) is kept in Minor above.*
- **Request to verify against InvDN-style methods:** The critic suggests verifying the "first reversible architecture for reflection removal" claim against InvDN-style methods. The paper already cites several reversible networks for other low-level tasks (line 81) and notes that these apply reversible networks as generative encoders, while reflection removal requires decoupling. The claim is properly scoped ("to the best of our knowledge...specifically for reflection removal"). This is not a concrete weakness.

## Novel Insights

The most interesting observation from the reviews that goes beyond the paper's own claims is that the prompt generator's design reveals an underexplored middle ground in SIRR: between explicit physics-based parameter estimation (α, β per channel) and implicit learning-based decomposition. The paper estimates physical parameters but then uses them only as input to learned feature modulation rather than directly applying them. The 0.28 dB gap between the dual-stream and decoupling designs, while small, suggests that the decoupling formulation itself may matter less than the reversible information flow — a finding that would benefit from further analysis beyond what this paper provides.

## Suggestions

1. **Clarify or remove the 24.34 dB claim.** Move it to the experiments section with full protocol: exactly how the six parameters transform the input, whether clipping is applied, which datasets (the same four as in Table 1?), and a direct comparison table row showing this as a baseline. If the numbers cannot be fully substantiated, remove the sentence.
2. **Rephrase "information lossless" to "information-preserving" or "reversible-by-construction"** to match what is actually demonstrated. Add a note about the non-zero scaling factor condition for γ.
3. **Explicitly state the data setting (w/ Nature) in the ablation section** and consider repeating the key ablation on the w/o Nat. setting for consistency.
4. **Add a brief discussion of the 0.28 dB drop in Setting D** — acknowledge it is small and may be within variance.

## Score and Decision

The paper presents a well-motivated architecture with consistently strong experimental results across five benchmarks, thorough ablation studies, and convincing qualitative examples. The weaknesses are presentation-level issues (an under-supported claim, a slightly over-reaching phrasing, and missing experimental details) that are straightforward to fix in a revision. The core technical contributions — the reversible multi-column encoder and the learned prompt-based feature modulation — are validated empirically and advance the state of the art in SIRR.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>