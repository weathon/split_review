- Decision: Reject
- Avg Score: 3.67
- Scores: 3, 3, 5
Now I have all the information I need. Let me produce the consolidated review.

## Summary

This paper proposes RDNet, a multi-column reversible encoder with a transmission-rate-aware prompt generator for single-image reflection removal. The architecture uses reversible inter-column connections intended to preserve information across scales, combined with an adaptive prompt that estimates per-channel transmission/reflection ratios. The method achieves state-of-the-art results on five benchmark datasets, outperforming prior methods by ~0.9–1.2 dB PSNR on average.

## Strengths

- **State-of-the-art quantitative results across multiple benchmarks.** In both training data settings (with/without Nature data), RDNet achieves the highest average PSNR (25.95 and 26.65 dB) across Real20, Objects, Postcard, and Wild datasets, surpassing DSRNet by 0.55–0.90 dB. On the Nature dataset it also achieves best PSNR (26.21 dB). These gains are consistent across four out of five datasets.

- **Systematic ablation studies support each design choice.** Table 2 separately ablates the prompt generator (1.13 dB drop, Setting A vs. Ours), the reflection loss (0.66 dB drop, Setting E), and the reversible connections (2.6 dB drop when replaced with U-Net connections, Setting F). The reversible-connection ablation is particularly informative because the alternative (U-Net) has *more* parameters, isolating the benefit of reversibility.

- **The transmission-rate-aware prompt module is validated with a clear stand-alone test.** The estimated α, β parameters, used as a simple linear preprocessing, achieve 24.34 dB PSNR — a result that confirms the parameters encode meaningful information about the transmission-reflection relationship.

- **Qualitative results on in-the-wild captures demonstrate real-world generalization.** Figure 4 shows challenging cases (e.g., dense reflection on a car window) where competing methods largely fail while RDNet produces nearly clean transmission estimates.

## Weaknesses

### Fatal
None.

### Major

- **The reversibility claim for inter-column connections is imprecisely formalized.** Equation (3)–(4) states that given forward features \(F_j^i\), one can recover \(F_j^{i-1}\) via \(F_j^{i-1} = \gamma^{-1}[F_j^i - \omega(\theta(F_{j-1}^i) + \delta(F_{j+1}^{i-1}))]\). The right-hand side depends on \(F_{j-1}^i\) (same column, lower level) and \(F_{j+1}^{i-1}\) (previous column, higher level). While a bottom-up, column-sequential processing order would make the reverse well-defined (since forward features \(F_{j-1}^i\) are available from the forward pass and \(F_{j+1}^{i-1}\) comes from the already-reversed previous column), the paper never specifies this order, nor does it explain whether the reverse is actually used during training (e.g., for activation checkpointing). The term "learnable reversible channel-wise scaling" for \(\gamma\) also lacks detail on how invertibility is enforced (e.g., is \(\gamma\) constrained away from zero?). This is a formalization gap around the paper's central conceptual claim. However, it does not invalidate the empirical results: the Setting F ablation (replacing reversible connections with non-reversible U-Net connections causing a 2.6 dB drop) provides strong empirical support for the design, independent of the mathematical precision of the reversibility claim.

### Minor

- **The comparison of the prompt generator alone against Dong et al. (24.34 vs. 24.21 dB) is not like-with-like.** The prompt generator's estimated parameters are applied as a simple per-channel linear rescaling of the input, while Dong et al. produces a full transmission image via a learned network. Reporting this as "surpassing the previous state-of-the-art method by Dong et al." could be misinterpreted. The result is useful as a sanity check on the parameter estimation quality, but the framing should be adjusted, and an explicit baseline such as the input image itself or an identity mapping should be included for context.

- **The number of columns \(N\) is never specified.** The text says \(i \in \{1, 2, ..., N\}\) (line 105) but \(N\) is never given. Similarly, the "learnable reversible channel-wise scaling" for \(\gamma\) is not described (e.g., how is it parameterized? how is invertibility guaranteed?).

- **No discussion of limitations, failure cases, or computational cost.** The conclusion (Section 5) reads as a summary with no acknowledgment of limitations. Inference time, parameter count, and memory footprint are not reported despite the multi-column architecture being plausibly heavier than single-stream competitors.

- **Typographical error in the loss coefficients.** Line 140 writes "\(c_3=0.6\)" but the content loss equation (Eq. 9) defines only \(c_0, c_1, c_2\); this should be \(c_2\).

### Trivial
- The \(c_3\) typo noted above.

## Nice-to-Haves
- An ablation replacing the reversible inter-column connection with a non-reversible but otherwise identical additive connection (rather than the full U-Net replacement in Setting F, which changes many architectural details at once) would more precisely isolate the benefit of invertibility.
- Reporting variance or confidence intervals for the main quantitative results, though not standard in this benchmark literature, would strengthen reproducibility.
- A discussion of when the method fails (e.g., heavy ghosting, extreme overexposure) would be more informative than the current qualitative selection.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **DSRNet inconsistency (harsh critic Critical Issue #3):** The critic flags DSRNet's Real20 PSNR dropping from 24.23 (w/o Nat.) to 23.91 (w Nat.) as suspicious. Real20 has only 20 images; a ~0.3 dB shift is well within sampling noise. The average across all four datasets (25.40 → 25.75) shows the expected improvement with more data. The critic's speculation about "different training configurations" is unsupported by evidence presented. **REMOVED — not a substantive weakness.**

2. **GLOM connection not operationalized:** The critic's observation that GLOM's column structure is used differently (different weights per column in RDNet vs. shared weights in GLOM) is a design choice, not a flaw. Inspiration does not require faithful replication. **REMOVED — not a weakness.**

3. **Ablation table confusion:** The critic claims the Ours row appearing in both sub-tables of Table 2 with the same average PSNR (26.65) is confusing. It is the same full model viewed from two different angles (left: prompt/preprocessing; right: dual-stream/loss/invertibility). This is standard table design for ablations that vary different parameters. **REMOVED — not a valid criticism.**

4. **Missing single-column ablation:** The critic asks for a single-column variant without multi-column structure. The dual-stream ablation (Setting D) is a single-column design (two streams within one column), which partially addresses this. While a pure single-column non-dual-stream variant could be informative, the absence is not a significant gap given the other ablations. **DEMOTED from what the harsh critic implied — addressed adequately by Setting D.**

5. **Missing statistical significance / confidence intervals:** Not standard practice in this benchmark literature, where PSNR/SSIM comparisons on fixed datasets are the norm. **REMOVED — not a field-standard requirement.**

6. **Table formatting complaints:** Parser-related style issues. **REMOVED — formatting/style.**

## Novel Insights

No genuinely novel insight emerges from these reviews beyond the paper's own contributions. The harsh critic's technical concern about the reversibility formalization is a valid clarity gap, but it does not reveal a hidden flaw in the empirical results. The strengths in terms of SOTA gains and clean ablation evidence remain intact.

## Suggestions

1. **Clarify the reversibility claim.** Specify (a) the computation order for the reverse of the inter-column connection, (b) whether the reverse is actually used during training, and (c) how \(\gamma\) (learnable channel-wise scaling) is constrained to be invertible (e.g., strictly positive scaling factors). If the reverse is never used in practice, clarify that the benefit is architectural rather than operational invertibility.
2. **Rephrase the prompt-generator comparison (24.34 dB vs. Dong et al.)** as a sanity check on parameter estimation quality rather than a direct method comparison, and include the input image PSNR as a baseline for context.
3. **Report the number of columns \(N\), total parameter count, and inference time** to allow practical assessment of the method's cost.
4. **Discuss limitations and failure cases** in the conclusion.
