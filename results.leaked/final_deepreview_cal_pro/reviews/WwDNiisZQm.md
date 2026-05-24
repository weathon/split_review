Now I have a solid calibration picture. Let me synthesize the final review.

**Calibration anchors:**

| Anchor | Avg Score | Decision | Round | Comparison vs CMiC |
|---|---|---|---|---|
| MambaVC (KgJwbsfN7G) | 4.80 | Reject | R1 (middle) | CMiC much stronger: genuine novelty, thorough ablations, comprehensive comparisons |
| FTIC (HKGQDDTuvZ) | 6.00 | Accept | R1 (middle) / R2 | CMiC comparable or better: more ablations, two complementary innovations, better BD-rates |
| Lossy Compression w/ Diffusion (raUnLe0Z04) | 5.50 | Accept | R2 | CMiC more technically substantive with novel mechanisms |
| Progressive Compression w/ Diffusion (CxXGvKRDnL) | 8.00 | Accept | R1 (high) | Different domain; CMiC not at this tier |

**Bracket from Round 1:** 5.0–7.5. After Round 2 narrowing: CMiC sits above FTIC (6.00) and well above the diffusion compression paper (5.50), but below the 8.0 diffusion model papers. **Final score: 6.5.**

---

## Summary

This paper proposes CMiC, a learned image compression method that adapts Mamba-style state-space models to be content-aware through two mechanisms: (1) Content-Adaptive Token Permutation (CTP), which reorders the 1D scan sequence via codebook-based clustering so that feature-similar tokens are processed consecutively, and (2) Global-Prior Prompting (GPP), which injects sample-specific global priors from a learnable prompt dictionary into the SSM output to relax the strict causality of sequential scanning. The model is integrated into a VAE-based compression framework and achieves near-state-of-the-art rate–distortion performance across Kodak, Tecnick, and CLIC datasets while maintaining lower complexity than prior Mamba-based LIC models.

## Strengths

- **CTP is a well-motivated and effective innovation.** The codebook-based clustering with EMA-updated centroids is a principled solution to the problem of rigid raster-scan ordering in Mamba. Ablation results (Table 2) show CTP alone contributes 1.8–2.4% BD-rate improvement, and removing it from the full model loses 1.6–2.2%. The clustering visualizations (Fig. 10) convincingly demonstrate that semantically coherent regions (red doors, clouds, feathers) are grouped together, directly supporting the claim that the permutation follows feature-space proximity.

- **GPP provides genuine global context with minimal overhead.** The prompt-conditioned output O_i = (C+P)h_i + Dx_i effectively injects image-level statistics into the per-token readout. ERF analysis (Fig. 9) shows that GPP creates non-zero activations beyond the causal scan position, and the ablation (Table 2) confirms 0.5–1.4% BD-rate improvement. The throughput reduction is negligible (~5% at training, 4% at inference).

- **Strong empirical validation with favorable complexity trade-off.** CMiC achieves BD-rate reductions of 15.91% (Kodak), 21.34% (Tecnick), and 17.58% (CLIC) against VTM-21.0, while using 56% fewer parameters, 57% fewer FLOPs, and 78% less GPU memory than MambaIC. The comparison against MambaVC and MambaIC (Table 1, Fig. 1c) shows consistent and substantial gains over prior Mamba-based LIC approaches. The structure replacement study (Table 4) and throughput ablation (Table 3) further validate that the CAM block, not the surrounding architecture, drives the improvements.

- **Thorough and varied ablations and visualizations.** Beyond component ablations, the paper includes cluster-number sensitivity (Table 6), adaptivity statistics (Table 5), throughput comparisons, ERF analysis on full networks (Fig. 7) and single layers (Fig. 9), per-image content-adaptive ERF (Fig. 8), and clustering visualizations (Fig. 10). This body of evidence collectively strengthens the central claims.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **Overclaim about consistent outperformance.** The paper states that CMiC "consistently outperforms leading methods across all evaluated datasets" (Section 4.3). However, Table 1 shows MLICv2 achieves a better BD-rate on Kodak (−16.16% vs. CMiC's −15.91%). The difference is small (0.25 percentage points) and CMiC wins on the other two datasets, but the blanket claim is inaccurate as written. The framing should be adjusted — e.g., "is competitive with or outperforms most leading methods." A brief acknowledgment of where CMiC trails MLICv2 would give a more honest picture.

- **Table 2 formatting is confusing.** The ablation table shows two rows with CTP checked and GPP unchecked, and the baseline row (no CTP, no GPP) appears absent or misaligned with its checkmark. The relationship between the percentage deltas in the prose and the tabulated BD-rate values requires the reader to reconstruct the baseline. A clearly labeled four-row table (baseline, CTP-only, GPP-only, full) with consistent delta reporting would improve evidential clarity.

### Trivial

- The "relaxing strict causality" phrasing in the abstract and Section 3.4 is slightly loose. GPP modulates the output readout (C+P) but does not alter the causal state update h_i = Āh_{i-1} + B̄x_i. The paper is clear about the actual mechanism, so this is a wording preference rather than a conceptual error — but a more precise framing (e.g., "augments the causal output with global priors") would forestall pedantic objections.

## Nice-to-Haves

- A controlled analysis quantifying how information from distant-but-similar tokens decays under raster scan vs. the content-adaptive permutation would directly support the central motivation for CTP.
- Explicitly reporting how much of the total BD-rate gain over MambaIC remains when both are placed in the same backbone (same entropy model, same window-attention blocks) would isolate the CAM block's contribution more cleanly than the current structure-replacement study.
- A brief note on out-of-distribution behavior of the clustering codebook (e.g., on medical or satellite imagery) would acknowledge a natural limitation.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Harsh Critic: "Complexity-measurement protocol needs to be stated."** The paper already specifies that FLOPs, peak memory, and decoding latency are "measured on 2K-resolution images" (Table 1 footnote), and states all experiments run on NVIDIA A100 GPUs (Section 4.1). While a more detailed protocol statement would be nice, the harsh critic's framing as a significant missing detail is overstated — this level of reporting is standard in the LIC field.

- **Harsh Critic: "Comparison with MLICv2 on Kodak should be acknowledged."** This is already captured as a Minor weakness above. The harsh critic framed it as part of the overclaim issue, which is correct but does not need separate listing.

- **Harsh Critic: "Reproducibility details absent from main text."** The paper reports optimizer (Adam), initial learning rate (10⁻⁴), hardware (A100), channel dimensions, block depths, cluster count, window size, and K-Means iteration count — all in the main text (Section 4.1). Batch size and training steps are presumably in the appendix. This is standard practice; the criticism is a nitpick that does not rise to a weakness.

- **Strength Finder: "CTP and GPP yield synergistic gain exceeding sum of individual improvements."** This claim does not hold on all datasets. On Kodak, CTP-only gain is 1.95%, GPP-only is 1.01%, sum = 2.96%, but combined gain is 2.65% (lower). On CLIC the sum does hold (1.80 + 0.47 = 2.27 vs. combined 2.71). The paper itself only claims complementarity, not super-additivity. The strength is adjusted accordingly.

- **Strength Finder: "CMiC achieves state-of-the-art RD performance"** — qualified above due to the MLICv2 result on Kodak. The claim is mostly true (CMiC is clearly among the top methods) but the unqualified "SOTA" label is slightly imprecise.

## Novel Insights

Beyond the paper's own contributions, a notable insight emerging from the review process is that the ERF visualization in Fig. 9 provides a clean decomposition of the two mechanisms' effects: GPP alone (column c) extends the receptive field beyond the causal scan position while preserving the raster-scan structure in the ERF pattern, whereas CTP alone (column d) breaks the raster-scan pattern entirely by reordering tokens, causing activation to spread to semantically related regions. The fact that these effects are visually separable and combine to produce a global, content-aligned receptive field (column e) is a compelling piece of evidence that the two mechanisms address genuinely distinct limitations of standard Mamba, rather than being two variants of the same idea.

## Suggestions

- Revise the "consistently outperforms leading methods" claim to reflect that CMiC is competitive with or outperforms most methods, and briefly note that MLICv2 edges ahead on Kodak.
- Fix Table 2 to include a clearly labeled baseline row and ensure the checkmark columns align with the described configurations.
- Consider replacing "relaxes the strict causality" with "augments the causal output with global priors" or similar phrasing that more precisely describes the GPP mechanism.
- The cluster visualization (Fig. 10) and adaptivity analysis (Table 5, Table 6) are strong — consider moving these observations earlier to strengthen the motivation for K=64 as an upper bound rather than a fixed cluster count.

## Score and Decision

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>