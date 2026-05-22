Now I'll write the consolidated review.

## Summary

The paper introduces Content-Aware Mamba (CAM) for learned image compression (LIC), addressing two fundamental limitations of standard Mamba when applied to images: its content-agnostic raster scan order and its strict causality. Two mechanisms are proposed: (1) **Content-Adaptive Token Permutation (CTP)** — a codebook-based clustering strategy that reorders latent tokens by feature similarity rather than spatial adjacency, enabling Mamba's SSM to scan semantically-related tokens contiguously; and (2) **Global-Prior Prompting (GPP)** — injecting sample-specific global priors (derived from clustering centroids) into the SSM's output projection to mitigate strict causality without multi-directional scanning. The resulting model **CMiC** achieves strong rate-distortion performance (BD-rate savings of −15.91%, −21.34%, −17.58% against VTM-21.0 on Kodak, Tecnick, and CLIC) with moderate complexity (69M params, 2.39 TFLOPs), and substantially outperforms prior Mamba-based LIC models in both RD performance and efficiency.

## Strengths

1. **Well-motivated, clearly articulated problem** — The paper identifies two genuine and previously underexplored limitations of Mamba for compression: (a) the fixed raster scan ignores feature-space proximity, and (b) strict causality prevents tokens from accessing later context. Both limitations are demonstrated concretely through Figure 9's ERF visualizations, which show that a vanilla Mamba layer's ERF stops exactly at the anchor token under a causal scan.

2. **Content-Adaptive Token Permutation is empirically effective and practical** — The codebook-based clustering with EMA updates avoids the instability of per-sample K-Means while being efficient (5% training overhead). Table 2 shows CTP alone yields 1.8–2.4% BD-rate gains across datasets. Figure 10 confirms the clustering captures semantically meaningful groupings (edges, red regions, smooth backgrounds), and Table 5 shows the number of activated clusters adapts to image content (mean 23.27, variance 90.91 on Kodak).

3. **Global-Prior Prompting demonstrably relaxes strict causality** — Figure 9(c) provides direct ERF evidence: with GPP enabled, non-zero activations appear beyond the causal scan cutoff, confirming that the prompt allows the model to "see beyond" preceding tokens. Combined with CTP, the complementary gain is 2.7–3.6% (Table 2).

4. **Thorough ablation study isolating each component** — Tables 2–6 systematically ablate CTP, GPP, network architecture (Conv/2D Mamba/Attention/CAM), and cluster count K. The ablations convincingly support the design choices: both components are necessary and complementary, CAM blocks outperform alternatives at comparable parameter counts, and K=64 is a saturation point.

5. **Competitive or state-of-the-art RD performance with strong efficiency** — CMiC achieves the best reported BD-rate on Tecnick (−21.34%) and CLIC (−17.58%) and is within 0.25% of the best reported Kodak result (MLICv2: −16.16%, CMiC: −15.91%). It uses 69M params and 2.39 TFLOPs, compared to MambaIC's 157M and 5.56 TFLOPs, while outperforming MambaIC by 2–6% BD-rate. Throughput is 22.05 samples/s, 2.4× faster than MambaIC and 3.4× faster than MambaVC (Table 3).

6. **ERF analysis provides compelling visual evidence** — Figures 7–8 show that CMiC achieves substantially larger and content-adaptive receptive fields than CNN-, Transformer-, and prior Mamba-based LIC models. Per-image ERFs (Figure 8) align with semantic structures (hair, feathers, shoreline), directly supporting the claim that the model captures long-range redundancy in a content-dependent way.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **"State-of-the-art" claim is imprecise** — The abstract and introduction claim "state-of-the-art rate-distortion performance." However, Table 1 shows that MLICv2 achieves a better BD-rate on Kodak (−16.16% vs. CMiC's −15.91%). CMiC is SOTA on Tecnick and CLIC, and overall the best across the aggregate of datasets, but the Kodak-specific claim should be qualified. This is a presentation issue, not a methodological flaw.

2. **Architecture comparison (Table 4) would be strengthened by compute-matched baselines** — The Conv block variant (66.47M, 2.18 TFLOPs) and 2D Mamba variant (71.44M, 2.54 TFLOPs) differ by approximately 2–5% in params and 7–16% in FLOPs from the CAM block (69.11M, 2.39 TFLOPs). While these differences are modest and the conclusion (CAM is best) is robust, a controlled experiment that normalizes compute (e.g., widening the Conv block to match FLOPs) would eliminate any residual concern about capacity-driven advantages.

3. **No statistical significance or variance reported** — BD-rate values are reported as single numbers without confidence intervals or variance across runs. Many recent LIC papers now report run-to-run variance. This is a standard limitation common in the field but worth noting.

4. **Entropy model component is under-described** — The Enhanced SCTX entropy model is described only briefly (Section 3.2, Figure 3). The paper notes that "adding CAM to the entropy model yields negligible gain" (Section 4.5) but does not analyze why. Given that the entropy model contributes to overall RD performance, a brief discussion or reference to the (stripped) appendix would help.

### Trivial

1. **Missing hyperparameter details** — Algorithm 1 does not specify the EMA decay λ, nor whether centroid updates are performed per-image or per-batch. The number of training steps and learning rate schedule are not fully specified (only optimizer and initial lr are given).

2. **Minor overstatement about multi-directional scans** — The paper states that multi-directional scanning "quadruples computational complexity." This is technically correct (four directional scans, each linear), though total complexity remains linear with a larger constant factor, and the scans can be parallelized. The phrasing could be misinterpreted as suggesting a change in asymptotic complexity.

## Nice-to-Haves

- An ablation comparing the proposed codebook-based cosine clustering against simpler alternatives (random permutation, spatial grid-based grouping, K-Means without codebook) would further isolate the benefit of semantic grouping.
- Reporting absolute bpp and PSNR values alongside BD-rate would aid reproducibility and allow readers to reconstruct the RD points.
- A brief analysis of why CAM does not help the entropy model would be useful, as it could reveal interesting properties about the interaction between token permutation and causal context modeling.

## Removed Points

The following points from the inputs were removed with justification:

- **"Misleading framing of mitigating strict causality"** (harsh critic point #2) — REMOVED. The paper consistently uses "mitigates" and "alleviates," not "breaks" or "eliminates." Figure 9(c) directly shows non-zero ERF beyond the causal cutoff, providing empirical evidence for the claim. The SSM remains formally causal in the recurrent update, but the prompt introduces non-causal global information — the paper accurately describes this mechanism.
- **"Unfair comparison with Mamba baselines / speculation about suboptimal training"** (harsh critic point #1, part 2) — REMOVED. CMiC outperforms both a smaller baseline (MambaVC: 48M params) and a much larger one (MambaIC: 157M params). This is evidence of effectiveness, not a weakness. The speculation that baselines were "suboptimally trained" has no basis in the paper and is not verifiable.
- **"Multi-directional scanning complexity claim is misleading"** — REMOVED. Four directional scans do quadruple FLOPs, which is a straightforward claim. Parallelization does not reduce total compute.
- **Generic strength-finder strengths** (e.g., "the paper addresses an important problem") — REMOVED per filtering rules. Only concrete, evidence-backed strengths were retained.
- **Missing appendix content / proofs** — REMOVED per hard rules (parser strips appendices).

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Qualify the SOTA claim** — Replace "state-of-the-art rate-distortion performance" with "competitive or state-of-the-art rate-distortion performance" and acknowledge MLICv2's edge on Kodak in the text while noting that CMiC achieves the best aggregate results across all three datasets.

2. **Add a compute-matched variant in Table 4** — A simple control experiment normalizing FLOPs (e.g., slightly widening the Conv block) would remove any doubt about capacity-driven advantages in the architecture ablation.

3. **Release the Appendix A.3.2 entropy model details** — The entropy model is a significant contributor to overall RD performance. A brief analysis of why CAM does not help the entropy model would be informative and could point to future improvements.

4. **Disclose the EMA decay λ** — This is a minor but useful reproducibility detail.

5. **Add variance intervals to BD-rate results** — Even a single additional run with a different seed would increase confidence in the results.

## Score and Decision

**Calibration anchors (all from the human-review corpus):**

| Path | Avg Score | Comparison to this paper |
|------|-----------|------------------------|
| `KgJwbsfN7G` (MambaVC) | 4.80 | First SSM compression paper but lacks task-specific design. This paper has substantially more novelty (CTP, GPP) and stronger empirical support. |
| `iDe1mtxqK5` (Spatial-Mamba) | 7.00 | Both address Mamba's vision limitations. Comparable contribution level; Spatial-Mamba has theoretical analysis, while this paper has deeper empirical validation for the compression setting. |
| `CxXGvKRDnL` (Progressive Compression) | 8.00 | Theoretically deeper and more novel framing. This paper is more applied/engineering but has thorough ablations and strong results. |
| `HKGQDDTuvZ` (FAT) | 6.00 | Both are LIC papers with SOTA claims. This paper has more extensive ablations and a clearer decomposition of contributions. |
| `RmmrHEH6Nx` (GroupMamba) | 3.00 | This paper has significantly more novelty and stronger empirical validation. |
| `AL1fq05o7H` (Mamba) | 6.25 | Foundational SSM paper. The current paper builds application-specific contributions on top of the SSM framework. |
| `0A6f1b66pE` | 4.60 | Vision-language Mamba application; limited relevance. This paper has more coherent contributions. |
| `KgJwbsfN7G` (MambaVC, medium band) | 4.80 | See above. |
| `gIrVoQEDQv` (NCA Compression) | 3.40 | Significantly weaker than this paper in both novelty and results. |

The paper identifies a genuine limitation of Mamba for image compression, proposes two effective and well-validated solutions, and demonstrates competitive results with thorough ablations. There are no fatal or major weaknesses. The minor issues (imprecise SOTA claim and compute-matched ablations) do not threaten the core contributions. Positioned against the anchors, the paper is stronger than MambaVC (4.80), on par with or slightly above Spatial-Mamba (7.00), and below Progressive Compression (8.00) in theoretical depth. It merits acceptance.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>