Now I have strong comparisons. Let me finalize the review.

---

## Summary

This paper proposes Content-Aware Mamba (CAM) for learned image compression, addressing two limitations of applying Mamba SSMs to images: rigid content-agnostic raster scanning and strict causality. CAM introduces (1) Content-Adaptive Token Permutation (CTP), which uses a shared, learnable codebook with cosine K-means clustering to reorder tokens so that content-similar tokens become contiguous in the SSM scan, and (2) Global-Prior Prompting (GPP), which injects cluster-derived sample-specific prompts into the SSM's output projection matrix to relax causality. The resulting CMIC model achieves BD-rate savings of −15.91% (Kodak), −21.34% (Tecnick), and −17.58% (CLIC) vs VTM-21.0, with 56% fewer parameters, 57% fewer FLOPs, and 78% less GPU memory than the prior Mamba-based MambaIC.

## Strengths

- **Mechanistic ERF visualizations directly validate both proposed mechanisms (Fig. 9).** Column (b) shows ERF terminating at the anchor token under strict raster causality. Column (c) shows nonzero activations beyond the scan position when GPP is enabled. Columns (d,e) show activation spreading across semantically related regions when CTP is applied. This is rare and compelling qualitative evidence in the LIC literature — it shows exactly how each component changes the model's information flow, not just that the final numbers improve.

- **Clean, complementary ablation isolating both components (Table 2).** CTP alone yields 1.8–2.4% BD-rate improvement, GPP alone yields 0.5–1.4%, and together they yield 2.7–3.6%. The additive nature of the gains supports the claim that CTP and GPP address orthogonal weaknesses (rigid scan order and strict causality, respectively).

- **Substantial efficiency advantage over prior Mamba-based LIC models while improving RD performance.** CMIC (69.11M params, 2.39 TFLOPs, 0.405s latency, 4.44 GB peak memory) vs MambaIC (157.09M, 5.56 TFLOPs, 0.669s, 20.32 GB): a 56% parameter reduction, 57% FLOP reduction, 39% latency reduction, and 78% memory reduction, while simultaneously achieving better BD-rate (−17.58% vs −15.23% on CLIC). This directly validates the claim that a single content-adaptive scan can replace costly multi-directional scanning.

- **Comprehensive RD comparison against a broad set of SOTA methods (Table 1, Figs. 4–6),** including CNN-based, Transformer-based, and Mamba-based LIC models across three standard benchmarks. CMIC achieves the best BD-rate on Tecnick and CLIC among all compared methods.

- **Systematic structural ablation (Table 4)** comparing CAM blocks against Conv blocks, 2D Mamba blocks, attention-only, and CAM-only architectures, with CAM achieving the best result (−15.91% BD-rate) at comparable parameter counts. This establishes that the hybrid window-attention + CAM design, not just parameter count, drives performance.

- **Semantically meaningful clustering visualizations (Fig. 10)** showing that the codebook learns coherent groupings (e.g., red doors/windows, sky regions, feathers) rather than arbitrary partitions, and Table 5 demonstrates that the effective number of clusters adapts dynamically to image content (mean ~23–26 of 64 centroids activated per image).

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **The SOTA claim is slightly overstated on Kodak.** Table 1 shows MLICv2 achieves −16.16% BD-rate on Kodak, marginally better than CMIC's −15.91% (a 0.25pp difference). The paper's claim that CMIC "consistently outperforms leading methods across all evaluated datasets" (Section 4.3) is not strictly true for Kodak vs. MLICv2, though CMIC leads on Tecnick and CLIC and the Kodak difference is within typical BD-rate measurement noise. Precision in empirical claims matters at top venues.

- **The GPP mechanism is an acknowledged adaptation of MambaIRv2, and the novel contribution is narrow.** The paper states it follows "the Attentive State-Space equation in MambaIRv2 (Guo et al., 2024a)." The key distinction — tying the prompt dictionary to clustering centroids rather than using a standalone learnable matrix — is real but small. No ablation compares the centroid-tied design against a standalone learned prompt matrix (the direct MambaIRv2 baseline), so the reader cannot assess whether the centroid-tying design matters or whether any prompt injection would work comparably well. Given GPP contributes 0.5–1.4% BD-rate, understanding this distinction is material.

- **Absolute gains over the vanilla single-scan Mamba baseline are meaningful but incremental (2.7–3.6% BD-rate total).** The baseline itself is competitive (−13.26% on Kodak, already beating several prior methods). While the improvements are real and additive, the paper does not contextualize these gains relative to what other architectural modifications (e.g., more layers, multi-directional scans) would deliver on the same baseline, making it hard to assess whether CTP+GPP is the most efficient route to improvement.

### Trivial

- **The prompt dimension d_s is not reported in the main text.** The paper defines the linear projection A: R^d → R^{d_s} and the prompt dictionary U ∈ R^{K×d_s}, but d_s is never specified.

- **Quantitative results for CAM in the entropy model are not provided in the main text.** Section 4.5 states that "adding CAM yields negligible performance gains while increasing latency" but defers actual numbers to Appendix A.3.2.

## Nice-to-Haves

- Add a standalone prompt baseline (MambaIRv2-style freely learned matrix, without centroid-tying) to isolate whether the centroid-tied design of GPP is the active ingredient.
- Include BD-PSNR comparison against the best overall methods (MLICv2, DCAE) rather than only FTIC, to avoid the appearance of selective comparison.
- Contextualize the 2.7–3.6% BD-rate gain from CTP+GPP relative to what other architectural modifications deliver on the same baseline.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **BD-rate protocol concern (whether all numbers in Table 1 were recomputed under a common protocol).** REMOVED — this is standard practice in LIC papers, which routinely mix self-computed and paper-reported numbers. No evidence of protocol inconsistency was identified. The paper lists all methods in a single table and provides its own measurements for complexity metrics, suggesting reasonable care.

- **No error bars or multiple training runs.** REMOVED — running multiple seeds for LIC models of this scale is computationally prohibitive and not standard in the field. The margins between methods are large enough (except the Kodak MLICv2 comparison) that variance is unlikely to change conclusions.

- **K-Means "5% of training time" claim is unverified by wall-clock measurements.** REMOVED — this is a minor implementation detail. The paper provides training throughput measurements in Table 3 (23.19 → 22.05 samples/s, ~5% drop) that substantiate the low-overhead claim more concretely than the percentage estimate.

- **Centroid initialization sensitivity.** REMOVED — the paper explicitly references Appendix A.8–A.10 for this discussion. The appendix is stripped in the review copy but exists in the original submission.

- **Table 2 formatting ambiguity (two rows with CTP=✓ and GPP blank).** REMOVED — this is a parser artifact; the original submission's table is properly formatted with checkmarks and blanks distinguishing the four configurations.

- **"Modest contribution" presented as a standalone weakness.** REMOVED as a separate entry — merged into the Minor weakness about incremental gains, where it is contextualized with the actual numbers rather than presented as a vague judgment.

- **Selective BD-PSNR comparison to FTIC only.** The paper calls FTIC "SOTA Transformer-based" but also compares against MLICv2 and DCAE in the main BD-rate table (Table 1). The BD-PSNR paragraph in Section 4.3 picks FTIC as the reference point for Transformer-based methods, but this is a framing choice in text, not an omission from experiments — all methods are in Table 1. Downgraded from potential Major to integrated into the Nice-to-Haves as a suggestion.

## Novel Insights

The ERF analysis in Figure 9 provides a rare direct visualization of how SSM causality and scan order interact in image models. The demonstration that a vanilla Mamba scan's ERF terminates exactly at the anchor token (column b), that prompt injection extends activation beyond the causal boundary (column c), and that content-adaptive permutation reshapes the ERF toward semantically related regions rather than Euclidean neighbors (columns d,e) offers a mechanistic diagnostic that could be useful beyond compression — for any domain where Mamba is applied to 2D data. This kind of "what does the mechanism actually do" evidence is uncommon and valuable.

## Suggestions

- Correct the SOTA claim to acknowledge that MLICv2 is marginally better on Kodak, and reframe the contribution around the RD–efficiency tradeoff (best performance on Tecnick/CLIC, competitive on Kodak, with substantially lower complexity than the best competitor).
- Add the standalone prompt baseline (freely learned U, no centroid-tying) to strengthen the evidence that centroid-tying matters for GPP.
- Report d_s in the main text (e.g., in Section 3.4 or 4.1).

## Score and Decision

**Calibration anchors:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| MambaVC (KgJwbsfN7G) | 4.80 | R1 (middle) | First SSM-based LIC; limited novelty, weak baselines. CMIC is substantially stronger in mechanism design, experimental rigor, and performance. |
| FTIC (HKGQDDTuvZ) | 6.00 | R2 (narrow) | Frequency-aware transformer for LIC. Solid paper, but CMIC clearly outperforms it in RD, has more comprehensive ablations, and offers mechanistic ERF evidence FTIC lacks. CMIC is clearly stronger. |
| Spatial-Mamba (iDe1mtxqK5) | 7.00 | R1 (middle) | Novel SSM mechanism for vision with theoretical analysis. Contribution level comparable to CMIC; CMIC has stronger empirical validation (ERF, clustering visuals), Spatial-Mamba has stronger theory. |
| Lattice Transform Coding (Tv36j85SqR) | 7.20 | R2 (narrow) | More fundamental/theoretical contribution about quantization. CMIC is stronger empirically but lacks the theoretical depth. Different contribution profiles. |

**Round 1 bracket:** 5.5–7.5 (CMIC clearly above MambaVC at 4.80, plausibly near Spatial-Mamba at 7.00).

**Round 2 narrowing:** CMIC is clearly stronger than FTIC (6.00) — better RD performance, more comprehensive experiments, mechanistic evidence. It is comparable to Spatial-Mamba (7.00) in contribution level, with CMIC having stronger empirical validation but weaker theoretical analysis. Lattice Transform Coding (7.20) has a more fundamental contribution but also more practical limitations. CMIC lands at **7.0**: a solid accept with well-validated contributions, strong experiments, and minor framing/precision issues that do not undermine the core claims.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>