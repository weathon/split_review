Now I have all the calibration data I need. Let me synthesize the final review.

## Summary

This paper introduces Content-Aware Mamba (CAM), a state-space model designed for learned image compression. It addresses two fundamental limitations of standard Mamba for images: (1) rigid, content-agnostic raster scanning that separates semantically related tokens, and (2) strict causality that prevents tokens from accessing global context. The two proposed mechanisms — Content-Adaptive Token Permutation (CTP), which clusters and reorders tokens by feature similarity, and Global-Prior Prompting (GPP), which injects sample-specific global priors via a centroid-conditioned prompt dictionary — are well-motivated and cleanly integrated. The resulting CMIC model achieves SOTA rate-distortion performance (BD-rate reductions of 15.91%, 21.34%, and 17.58% on Kodak, Tecnick, and CLIC over VTM-21.0) with lower complexity than prior Mamba-based LIC methods.

## Strengths

- **Clear problem decomposition and motivated design.** The paper crisply identifies two orthogonal Mamba limitations for image compression — fixed scanning and strict causality — and proposes targeted, mechanistic solutions for each. The connection between the limitations and the proposed mechanisms is logically tight and well-articulated (Section 1, Section 3.3–3.4).

- **Strong empirical results with genuine SOTA performance.** Table 1 demonstrates CMIC outperforms all listed learned methods, including recent strong baselines (MLICv2, HPCM, DCAE, LALIC) and the prior Mamba-based MambaVC and MambaIC. The margins are consistent across all three datasets and bitrates (Figs. 4–6). The complexity profile (69M params, 2.39 TFLOPs, 0.405s latency, 4.44 GB memory) is substantially leaner than MambaIC (157M/5.56 TFLOPs/0.669s/20.32 GB) while delivering better RD performance.

- **Thorough and revealing ablations.** Table 2 cleanly isolates CTP and GPP contributions (2.0–2.4% from CTP alone, 0.5–1.4% from GPP alone, with complementary gains when combined). Table 4 validates CAM against Conv, 2D-Mamba, attention-only, and CAM-only variants. Table 6 shows K=64 is near-optimal. The ERF visualizations (Figs. 7–9) provide causal evidence for the method's claims — Fig. 9 in particular is a compelling demonstration of how GPP introduces non-causality (activations beyond the scan line) and CTP reshapes the receptive field toward semantic regions.

- **Effective use of visual evidence.** The cluster visualizations (Fig. 10) directly show semantically coherent grouping (doors, clouds, feathers), and the per-image ERF maps (Fig. 8) illustrate content-adaptive influence patterns. The quantitative cluster activation statistics (Table 5: mean 23–26 active centroids out of 64, high variance) support the adaptivity claim.

## Weaknesses

### Fatal

None.

### Major

None. The core claims are well-supported by the evidence presented. The SOTA performance is verified across three standard datasets with thorough comparisons, the contributions of CTP and GPP are individually ablated, and the ERF analysis provides mechanistic evidence for the claimed non-causal and content-adaptive behavior.

### Minor

- **Missing controls for the clustering mechanism.** The paper does not include a baseline that replaces the learned clustering-based permutation with a content-agnostic reordering of comparable cost (e.g., a fixed segment-based reorder or a random permutation). This makes it harder to attribute the gains specifically to *content-awareness* of the clustering rather than to the general benefit of any non-raster scan that brings distant tokens into proximity. The ERF evidence in Fig. 9(d–e) partially addresses this by showing the pattern changes qualitatively, but a quantitative ablation would strengthen the claim that the learned content-adaptive grouping, specifically, drives the improvement.

- **The centroid-conditioned prompt is not isolated from simpler alternatives.** The prompt dictionary is explicitly tied to cluster centroids via a learned linear projection. The paper does not compare against a standard fully learnable prompt pool (as in MambaIRv2) indexed by cluster assignment, which would isolate whether the centroid grounding actually helps or whether the same gains could be obtained from a freely learned dictionary. This is not a fatal gap — the ablation in Table 2 already shows GPP helps — but it leaves one design choice unvalidated.

- **Limited analysis of clustering failure modes.** Figure 10 shows three clean, semantically coherent clustering examples, and Table 5 provides aggregate activation statistics. However, there is no discussion of failure cases (images where clustering may be uninformative or collapse to few clusters), and no quantitative measure of cluster quality (e.g., cluster purity) across the full dataset. This limits confidence in the robustness of the clustering mechanism.

### Trivial

- The order of tokens *within* each cluster after permutation is not explicitly specified (presumably retaining original spatial order, but this affects SSM scan behavior).
- The EMA decay parameter λ for the centroid update is not given in the main text (may be in the appendix).
- The paper does not include an explicit limitations section.

## Nice-to-Haves

- A "random reorder" or fixed-pattern permutation baseline to isolate the benefit of content-adaptive clustering specifically.
- A comparison against a freely learnable prompt pool (not tied to centroids) to isolate the centroid-conditioning benefit.
- A direct controlled comparison that clones the MambaIC pipeline and replaces only the transform blocks with CAM, to more precisely attribute the BD-rate gap.
- Expanded MS-SSIM RD curves beyond the single Kodak PSNR–MS-SSIM plot (Fig. 6) — e.g., for Tecnick or CLIC.

## Removed Points

These points are flagged to be removed — treat them with caution:

- **"Entropy model detail missing from main text"**: The appendix, which contains these details (referenced as Appendix A.3), is stripped by the parser. The paper explicitly cites where the full description lives.
- **"Encoding latency absent from main text"**: The paper states encoding latency is provided in Appendix A.14; the parser strips appendices.
- **"Training stability discussion missing"**: The paper references Appendix A.8–A.10 for clustering stability details. The main text does mention that the EMA update "ensures training stability and robustness to initialization" (Sec. 3.3), which is a reasonable summary.
- **"MS-SSIM curves not shown"**: Fig. 6 shows Kodak PSNR–MS-SSIM, and the text reports MS-SSIM BD-rate improvements over TCM-L and FTIC. The paper could include more curves, but this is not a missing element.
- **"Clustering mechanism decoupling from end-to-end training is a risk"**: The harsh critic acknowledges the method works and Fig. 10 shows semantic clustering. The "risk of drift" is speculative — the paper demonstrates effective training in practice, and the EMA update scheme is a standard technique from VQ-VAE known to be stable. This is a theoretical concern not borne out by the evidence.
- **"Fig. 9 uses soft clustering without definition"**: The ERF computation for Fig. 9 uses soft clustering as a differentiable proxy for the hard clustering used in the actual model, which is a standard technique for gradient-based ERF analysis. The caption clarifies this is for analysis purposes.
- **"Comparison against MambaVC/MambaIC not under identical training conditions"**: Table 4 provides a controlled within-architecture comparison (CAM vs. 2D Mamba), which is the appropriate way to isolate architectural contributions. External comparisons across different codebases inherently differ in training recipes; the paper provides both external and internal comparisons, which is the correct approach.
- **"The statement about capturing dependencies between semantically related regions is an overgeneralisation"**: This is a phrasing preference, not a substantive weakness. The paper's mechanisms demonstrably group semantically related tokens (Fig. 10), and the claim is properly scoped to feature-space proximity.

## Novel Insights

The paper's most genuinely novel contribution is the identification that Mamba's two problems for image compression — fixed scanning order and strict causality — can be disentangled and addressed orthogonally. The clustering-based permutation (CTP) solves the scanning problem by reorganizing tokens in feature space rather than Euclidean space, while the prompt mechanism (GPP) solves the causality problem by injecting global statistics without requiring multi-directional scans. This decomposition is clean, and the ERF visualization methodology (particularly Fig. 9) provides a rare direct window into *why* each component works: GPP literally makes the model "see beyond" the scan line, and CTP literally reshapes the receptive field to follow semantic boundaries. This kind of mechanistic evidence is uncommon in LIC papers and represents a methodological contribution beyond the architecture itself.

## Suggestions

- Add a control experiment with a content-agnostic reordering (e.g., fixed spatially-grouped blocks, or random-but-valid permutation) to isolate the benefit of *learned content-aware* clustering specifically.
- Compare the centroid-tied prompt dictionary against a freely learnable prompt pool indexed by cluster ID, to validate the centroid-conditioning design choice.
- Include at least one failure case or challenging clustering example in the qualitative analysis, and consider reporting a quantitative cluster quality metric.
- Specify the EMA decay λ and intra-cluster token ordering explicitly in the main text.
- Add an explicit limitations paragraph to the conclusion.

## Score and Decision

### Calibration Anchors

| Anchor Paper | Path | Avg Score | Round | Comparison to CMIC |
|---|---|---|---|---|
| MambaVC | KgJwbsfN7G | 4.80 | R1 (low-mid) | CMIC is substantially stronger: more novel contributions (CTP+GPP vs. straightforward VSS block application), far more comprehensive evaluation, SOTA comparisons, and genuine architectural innovation rather than adaptation. |
| FTIC | HKGQDDTuvZ | 6.00 | R2 (narrow) | Both are strong LIC papers accepted at ICLR. CMIC's problem framing is sharper, its solutions are more innovative, and its evaluation (ERF analysis, complexity breakdown, per-component ablations) is more thorough. CMIC's BD-rate numbers are also higher. |
| RECOMBINER | VkWbxFrCC8 | 6.67 | R2 (narrow) | Different paradigm (INR-based). CMIC's results are more competitive against SOTA and its contribution is more impactful within its paradigm. |
| Spatial-Mamba | iDe1mtxqK5 | 7.00 | R1 (mid) | Closest comparator. Both address Mamba's limitations for 2D data with well-motivated mechanisms. CMIC's contributions (CTP+GPP) are more tailored to the compression problem and arguably more innovative than adding dilated convs to state space. CMIC's evaluation is more comprehensive. |
| LongMamba | fMbLszVO1H | 6.75 | R2 (narrow) | Addresses Mamba's limited receptive field for language. Different domain, but similar quality level. CMIC's empirical validation is more thorough. |
| Demystifying Token Dynamics | qtTIP5Gjc5 | 7.50 | R2 (narrow) | Theoretical analysis paper, very different type. Not directly comparable in format, but represents the high-quality end of Mamba-analysis papers. CMIC is empirical rather than theoretical but makes a comparably strong contribution. |

**Round 1 Bracket**: [6.0, 8.0] — clearly above MambaVC (4.80), plausibly above FTIC (6.00), and comparable to Spatial-Mamba (7.00).

**Round 2 Narrowing**: CMIC is stronger than FTIC (6.00) and RECOMBINER (6.67), comparable to or slightly above Spatial-Mamba (7.00), and not quite at the level of the 7.50 theoretical papers which offer fundamentally new understanding. Score: **7.5**.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>