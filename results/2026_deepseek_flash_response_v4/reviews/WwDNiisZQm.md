Now I have all the calibration data. Let me write the final consolidated review.

## Summary

The paper introduces Content-Aware Mamba (CAM) for learned image compression, with two mechanisms: Content-Adaptive Token Permutation (CTP) that reorders tokens by feature similarity, and Global-Prior Prompting (GPP) that injects sample-specific global priors into the SSM to relax strict causality. The full model (CMIC) achieves strong BD-rate savings over VTM-21.0 (15.91%, 21.34%, 17.58%) with moderate complexity (69.11M params, 2.39 TFLOPs).

## Strengths

1. **Clean, controlled ablation isolating each component's contribution (Table 2).** The paper reports that CTP alone provides 2.0%/2.4%/1.8% BD-rate reduction on Kodak/Tecnick/CLIC, GPP alone provides 0.5%-1.4%, and the combined gain is 2.7%-3.6%. This is a well-structured decomposition that directly supports the claim that both mechanisms are complementary.

2. **ERF visualizations provide mechanistic evidence for both claims.** Figure 9 directly shows that a single Mamba layer without CTP/GPP has zero ERF beyond the raster-scan center position, GPP introduces non-zero activations after the scanned sequence, and CTP reshapes activation toward semantically related regions. This connects the architectural changes to their intended effects at the mechanism level, not just in end-to-end metrics.

3. **State-of-the-art or competitive RD performance with substantially lower compute than prior Mamba-based LIC.** CMIC (69.11M, 2.39 TFLOPs) outperforms MambaIC (157.09M, 5.56 TFLOPs) by 2.36%–6.48% BD-rate while reducing parameters by 56%, FLOPs by 57%, and memory by 78%. The efficiency claim is well-supported.

4. **Clustering visualizations (Figure 10) confirm semantic grouping.** Binary cluster masks align with interpretable visual content (e.g., Centroid #10 activates on high-gradient edges, #26 on red/yellow textured regions), and Table 5 shows dynamic activation counts (mean 23.27 of 64 clusters on Kodak, variance 90.91), supporting content-adaptivity.

## Weaknesses

### Major

- **The comparison with MambaIC is confounded by architectural differences beyond CTP/GPP.** CMIC outperforms MambaIC by 2.36% BD-rate on Kodak. However, the controlled ablation (Table 4) shows that replacing CAM blocks with 2D Mamba blocks at similar scale yields only ~0.55% difference on Kodak (−14.13% vs. −14.68%). The remaining ~1.8% gap between CMIC and MambaIC must come from other architectural choices (different channel dimensions, block depths, window attention modules, entropy model design) rather than from CTP+GPP alone. The paper does not disentangle these factors, making it difficult for readers to assess how much of the reported advantage is attributable specifically to the proposed mechanisms. This does not invalidate the results — CMIC as a full system is clearly strong — but it weakens the claim that CTP and GPP are primarily responsible for the gain over MambaIC.

### Minor

- **Dimensional underspecification of the prompt injection operation (Section 3.4).** The paper states O_i = (C + P)h_i + Dx_i, where P ∈ ℝ^{N × d_s}. In standard Mamba, C ∈ ℝ^{d × d_h}. It is not specified how dimensions are reconciled (e.g., whether P is indexed per-token, whether d_s = d is assumed, or whether broadcasting/reshaping is applied). The paper references MambaIRv2 for the "Attentive State-Space equation," but the description here is not self-contained.

- **MS-SSIM results are poorly presented.** The paper states CMIC outperforms TCM-L and FTIC by −7.34% and −3.87% in MS-SSIM BD-rate, referencing "Fig. 6" — but the figure caption for Figure 6 describes PSNR vs. bpp curves, not MS-SSIM. No dedicated MS-SSIM table or figure is provided. These numbers should be properly contextualized.

- **Naming inconsistency.** Table 1 lists "MambaC" while the text refers to "MambaIC (Zeng et al., 2025)." These should be harmonized.

### Trivial

- **Table 2 baseline interpretation.** The baseline (−13.26% on Kodak) corresponds to the full CMIC architecture with vanilla Mamba blocks, not a standalone lightweight Mamba. The paper explains this ("equivalent to a vanilla single-scan Mamba block") but a reader could initially misinterpret the baseline's strength.

## Nice-to-Haves

- A direct comparison that isolates CTP+GPP's contribution vs. MambaIC by ablating at matched architecture — e.g., replacing MambaIC's blocks with CAM blocks, or matching CMIC's architecture to MambaIC's scale.

## Removed Points

- **Strict causality overstatement (Harsh Critic).** The ERF evidence (Figure 9) directly supports the paper's claim that GPP introduces non-causality. The improvement from GPP is modest on top of CTP (0.7–1.2%) but this is accurately reported; the claim that GPP "effectively mitigates strict causality" is supported by the data. Removed as not a genuine weakness.
- **Missing training datasets for baselines.** Scope creep — the paper states its own training data (Flickr2W) and baselines are cited works whose training setups are standard.
- **Missing EMA decay parameter / K-Means iteration count values.** Per hard rules, these are trivial implementation details and/or appendix content stripped by the parser.
- **Missing related works.** Per hard rules, cannot be confirmed.

## Novel Insights

The ERF visualization methodology used here (Figure 9) — isolating individual Mamba-layer ERF under different component configurations — provides a template for diagnosing content-adaptivity in SSM-based vision models that goes beyond standard benchmark comparisons. The finding that GPP allows non-zero ERF values beyond the raster-scan boundary in a single layer is a clean, visual demonstration that prompt-based conditioning can break SSM causality at the architectural level.

## Suggestions

1. Clarify the dimensional compatibility of the C+P operation in Section 3.4. Specify whether P_i (the i-th row of P) replaces or broadcasts to match C's dimensions, or state the assumption d_s = d.

2. Acknowledge the architectural confound in the MambaIC comparison explicitly. A brief sentence such as "CMIC's advantage over MambaIC combines the benefits of CTP/GPP with architectural improvements in channel sizing, block depth, and attention modules; the ablation in Table 4 isolates the CAM-specific gain" would resolve the issue.

3. Add a dedicated MS-SSIM BD-rate table, or at minimum ensure that the figure reference for MS-SSIM results points to the correct figure.

4. Harmonize the naming: use "MambaC" or "MambaIC" consistently in both Table 1 and the body text.

## Score and Decision

**Calibration report:**

All anchors retrieved across rounds:

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| GroupMamba | RmmrHEH6Nx | 3.00 | R1 | Much weaker (SSM vision but not compression, serious flaws) |
| MambaVC | KgJwbsfN7G | 4.80 | R1 | Direct competitor; our paper is stronger (two novel mechanisms vs. straightforward VSS application) |
| Spatial-Mamba | iDe1mtxqK5 | 7.00 | R1 | Stronger (cleaner story, no confounds, broader vision benchmark) |
| V2M | FowFLhUTgO | 5.50 | R1 | Weaker (moderate novelty concerns, missing efficiency analysis) |
| Autoreg. Pretrain Mamba | PQpvhUrA1C | 5.75 | R1 | Comparable (similar level of contribution) |
| Frequency-Aware Transformer | HKGQDDTuvZ | 6.00 | R2 | Comparable LIC paper (similar structure: two modules + ablation; our ERF evidence is stronger, but FAT has fewer confound issues) |
| Test-time Adaptation | bsnRUkVn63 | 6.00 | R2 | Comparable LIC paper |
| 2D State Space Layer | BGkqypmGvm | 6.00 | R2 | Comparable SSM paper |
| LLM Lossless Compress | dcG17rjJF9 | 5.67 | R2 | Slightly weaker (split reviews, lower consensus) |
| Lattice Transform Coding | Tv36j85SqR | 7.20 | R2 | Stronger (theoretical contribution, higher scores) |

**Round 1 bracket:** 5.0 – 6.5. The paper is clearly above MambaVC (4.80) and below Spatial-Mamba (7.00).

**Round 2 narrowing:** The paper aligns with the ~6.0 cluster — comparable to Frequency-Aware Transformer (6.00) and Test-time Adaptation (6.00), which are accepted LIC papers. The paper has cleaner ablation than FAT but a more substantive confound issue in the MambaIC comparison. Score calibrated to 6.0.

The paper makes a clear, well-motivated contribution with good experimental evidence (clean ablation, ERF visualizations, competitive RD results). The main weakness — the confounded MambaIC comparison — is real but does not undermine the paper's core contribution, as the controlled ablation (Table 4) and ERF evidence independently demonstrate CTP and GPP's value. The dimensional underspecification and MS-SSIM presentation are addressable.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>