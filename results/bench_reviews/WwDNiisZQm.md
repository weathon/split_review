Now I have sufficient calibration material. Let me synthesize the review.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses
### Fatal
### Major
- weakness 1 — why it matters
### Minor
- weakness 1 — why it matters
### Trivial

## Nice-to-Haves
- suggestion that would improve but is not a core flaw

## Removed Points

## Novel Insights

## Suggestions

## Score and Decision

Let me now write the consolidated review.

---

**Verification of Harsh Critic Claims:**

1. **MLICv2 outperforms CMIC on Kodak** — Verified. Table 1: MLICv2 -16.16%, CMIC -15.91%. The paper says "Our CMIC model achieves superior performance" and "consistently outperforms leading methods." This is factually correct but needs qualification. **KEEP as Major weakness.**

2. **Core technical novelty limited** — The paper uses VQ-VAE-style clustering (acknowledged in Section 3.3: "draw inspiration from VQ-VAE") and MambaIRv2's attentive state-space equation (acknowledged in Section 3.4: "following the Attentive State-Space equation in MambaIRv2"). However, the combination and application to compression is novel, and the paper clearly differentiates from MambaIRv2 in Appendix A.13. The criticism is valid but the paper does acknowledge sources. **KEEP as Minor weakness** — the paper is transparent about its influences, and the application to compression is still a valid contribution.

3. **Entropy model choice weakens global modeling claim** — The paper states in Section 4.5: "For the entropy model, adding CAM yields negligible performance gains while increasing latency, indicating a limitation of CAM in enhancing entropy modeling." Appendix A.3.2 provides full details. The paper is transparent about this limitation. **WEAKEN** — the paper already acknowledges this. Move to Minor or Nice-to-Have.

4. **Non-differentiable clustering** — The paper discusses training stability in Appendix A.8 with test loss curves (Figure 18) across random seeds. The criticism about biased gradients is technically valid but the paper provides empirical evidence of stability. **KEEP but weaken** to a minor observation.

5. **No confidence intervals** — This is standard practice in LIC. **MOVE to Nice-to-Have.**

6. **Missing multi-directional scanning baseline** — This is a reasonable suggestion. **KEEP as Nice-to-Have.**

7. **ERF analysis on SSM layer, not final reconstruction** — The paper explicitly states this is done "to analyze the proposed non-causal mechanism and to isolate the effects of our two main components." This is by design. The per-image ERF (Figure 8) does show effects on the final reconstruction. **REMOVE** — the paper's analysis is appropriate for what it's trying to demonstrate.

8. **Modest gains from CTP+GPP (2.7-3.6%)** — This is insightful. The paper proposes specific components (CTP and GPP) and attributes specific gains to them. The claim is that these components improve the model, not that they constitute the entirety of the gain. The 2.7-3.6% BD-rate improvement is meaningful in compression. However, it's a fair observation that the base architecture does most of the heavy lifting. **KEEP as Minor weakness** — it's a valid observation but doesn't invalidate the contribution.

9. **Gradient flow delay from non-differentiable centroids** — The paper acknowledges the centroids are updated via non-gradient K-Means while the mapping A(·) is differentiable (Section 3.4: "whereas the centroid codebook is updated via non-gradient K-Means, the mapping A(·) is differentiable and trained end-to-end"). The paper provides empirical stability evidence. **WEAKEN to a minor point.**

Let me now also check the Strength Finder. It says:
- "Novel content-adaptive scanning mechanism" — supported by Table 2 (CTP alone gives 1.8-2.4% improvements). Genuine strength.
- "Global-prior prompting effectively mitigates Mamba's causality" — supported by Figure 9. Genuine strength.
- "SOTA performance with lower complexity" — Table 1 shows this clearly. Genuine strength.
- "Comprehensive ablation analysis" — Yes, very thorough. Genuine strength.
- "Interpretable content-adaptive behavior" — Figure 10 is compelling. Genuine strength.

All of these are genuine. I'll keep them.

Now, the human finder - I don't see any human finder output in the provided context. Let me check... The user only provided "Harsh Critic" and "Strength Finder" inputs, no "Human Finder." So I don't need to process that.## Summary

This paper introduces Content-Aware Mamba (CAM) for learned image compression, addressing two fundamental misalignments between Mamba's sequential scanning and image structure: (1) the content-agnostic raster scan that separates semantically similar but spatially distant tokens, and (2) Mamba's strict causality that prevents tokens from accessing global context. CAM proposes Content-Adaptive Token Permutation (CTP), which uses codebook-based K-Means clustering to reorder tokens by feature similarity, and Global-Prior Prompting (GPP), which injects cluster-derived global priors into the SSM's output matrix to relax causality. The resulting model (CMIC) achieves BD-rate reductions of 15.91%, 21.34%, and 17.58% over VTM-21.0 on Kodak, Tecnick, and CLIC respectively, while using 56% fewer parameters and 57% fewer FLOPs than MambaIC.

## Strengths

1. **Well-motivated and clearly articulated problem.** The paper identifies two concrete limitations of Mamba for image compression (rigid raster scan and strict causality) and designs targeted mechanisms to address each. The ERF visualizations in Figures 7–9 convincingly illustrate these limitations and how CAM alleviates them.

2. **Content-adaptive scanning demonstrably improves compression.** Table 2 shows that CTP alone yields BD-rate reductions of 1.8–2.4% across datasets, and cluster visualizations (Figure 10) confirm that the clustering captures semantically meaningful groupings (edges, textured regions, smooth backgrounds). This provides direct evidence that reordering by feature similarity helps eliminate redundancy.

3. **Substantial efficiency gains over prior Mamba-based LIC models.** CMIC achieves 69M params / 0.405s decode latency vs. MambaIC's 157M / 0.669s — a 56% parameter reduction, 57% FLOP reduction, and 78% peak memory reduction — while outperforming MambaIC by 2.17–6.48% BD-rate across datasets. This favorable efficiency-performance trade-off is directly attributed to CAM's single selective scan versus multi-directional scanning.

4. **Comprehensive and well-structured ablation study.** The paper systematically ablates CTP, GPP, cluster number (Table 6), network structure variants (Table 4), and entropy model choices (Appendix A.3.2), and measures throughput overhead (Table 3). The experiments isolate each component's contribution and confirm they are complementary.

5. **Interpretable content-adaptivity validated through multiple visualizations.** The cluster visualization (Figure 10) shows semantically consistent cluster assignments across images, the per-image ERFs (Figure 8) align with semantic structures (hair, feathers, shorelines), and the non-causality analysis (Figure 9) provides direct evidence that GPP enables the SSM to "see beyond" the causal scan boundary.

## Weaknesses

### Fatal
None.

### Major

1. **State-of-the-art claim is partially overstated.** Table 1 shows MLICv2 achieves -16.16% BD-rate on Kodak while CMIC achieves -15.91%. The paper's abstract, introduction, and Section 4.3 state "superior performance" and "consistently outperforms leading methods" without qualification. While CMIC outperforms MLICv2 on Tecnick (-21.34% vs -20.13%) and CLIC (-17.58% vs -15.79%) with significantly better efficiency, the Kodak result contradicts the unqualified "state-of-the-art" framing. The paper should acknowledge this and clarify that CMIC is competitive with (not uniformly better than) top Transformer-based methods on the Kodak benchmark, with the key advantage being efficiency.

### Minor

2. **Proposed components contribute a modest fraction of total gain.** Table 2 shows that CTP+GPP together yield a 2.7–3.6% BD-rate improvement over the baseline single-scan Mamba, while the overall model improves 15.91–21.34% over VTM-21.0. This means the majority of the performance comes from the base Mamba + SCCTX architecture rather than the paper's novel components. This does not invalidate the contribution, but a more measured framing would strengthen the paper.

3. **Technical novelty is moderate.** CTP adapts codebook-based K-Means clustering from VQ-VAE (Van Den Oord et al., 2017), and GPP adapts the Attentive State-Space equation from MambaIRv2 (Guo et al., 2024a) while changing the prompt source from a standalone learnable matrix to a projection of centroids. The paper acknowledges these sources (Section 3.3, Section 3.4, Appendix A.13) and clearly differentiates its redundancy-aware design from MambaIRv2. However, the contribution is primarily an engineering combination of known techniques applied to a new domain, rather than a conceptual breakthrough.

4. **Entropy model does not benefit from CAM's global modeling.** As the paper transparently reports (Section 4.5, Appendix A.3.2), applying CAM to the entropy model yields negligible gains while increasing latency by ~16%. This means the "global redundancy elimination" narrative applies only to the transform networks, not the full compression pipeline. The paper acknowledges this limitation, but it narrows the scope of the claimed benefit.

5. **Non-differentiable clustering may introduce biased gradients.** The token permutation and assignment are discrete operations. The paper relies on EMA-based codebook updates (Algorithm 1) for stability and provides test-loss curves across random seeds (Figure 18) as empirical evidence of stable convergence. A formal analysis or gradient-norm comparison with a differentiable alternative (e.g., Gumbel-Softmax) would strengthen the argument.

### Trivial
None.

## Nice-to-Haves

- **Report BD-rate with confidence intervals or multiple seeds.** While single-run evaluation is standard in LIC, confidence intervals would strengthen the claimed improvements, especially given the small margin with MLICv2 on Kodak.
- **Include a multi-directional scanning baseline.** The paper argues multi-directional scanning quadruples complexity, but does not include an ablation where the same architecture uses four-direction scans instead of CTP+GPP. This would directly quantify the benefit of the proposed approach over a simpler alternative.
- **Show a failure case** where the clustering groups tokens incorrectly, to provide a balanced view of the method's limitations.
- **Evaluate on a larger training set** (e.g., CLIC train + ImageNet) to test whether the gains from content-adaptive scanning scale with more data.

## Removed Points

- **"ERF analysis performed on SSM layer not final reconstruction"** — The paper explicitly states this is done "to isolate the effects of our two main components" (Section 4.5), and the per-image ERF (Figure 8) does analyze the full model's effect on reconstruction. The analysis is appropriate for its stated purpose.
- **"No confidence intervals"** — This is standard practice in the LIC field and is more appropriately a nice-to-have than a weakness.
- **"Entropy model choice weakens global modeling claim"** — The paper already transparently acknowledges this limitation and discusses it in detail (Section 4.5, Appendix A.3.2).

## Novel Insights

None beyond the paper's own contributions. The reviews primarily converge on the paper's own stated findings: that content-adaptive token permutation and global-prior prompting improve Mamba-based compression, with thorough ablation evidence. The key tension revealed by the reviews is between the paper's strong empirical execution (comprehensive ablations, efficiency gains, interpretable visualizations) and the moderate technical novelty of its components (adaptations of VQ-VAE clustering and MambaIRv2 prompting). This is a common pattern for solid applied papers that stop short of being conceptual breakthroughs.

## Suggestions

1. **Qualify the SOTA claim.** Explicitly acknowledge that MLICv2 achieves a slightly better BD-rate (-16.16% vs -15.91%) on Kodak, and reframe the contribution around CMIC's superior efficiency-performance trade-off rather than unqualified dominance on all metrics.
2. **Add a multi-directional scanning ablation.** Compare the same architecture using four-direction scans (as in VMamba/MambaIC) vs. the proposed CTP+GPP at matched complexity, to directly quantify the benefit of content-adaptive scanning over a simpler alternative.
3. **Add gradient health analysis.** Include a plot comparing gradient norms or loss curves with and without the clustering component, to address the discrete-gradient concern beyond the already-provided seed-averaged loss curves.

## Score and Decision

**Calibration anchors:**

| Paper | Avg Score | Comparison to CMIC |
|-------|-----------|-------------------|
| MambaSIC (0dHrYUd17W) — Mamba-based stereo image compression | 4.00 (Withdrawn) | Weaker novelty (direct application of Mamba to stereo), similar criticism of incremental contribution. CMIC has more novel mechanisms and better evaluation. |
| GMamba/GSSM (96p1eBUVaN) — Global perception in SSMs | 5.50 (Accept Poster) | Stronger theoretical framing (mathematical definition of global perception) but weaker empirical validation on compression. CMIC has cleaner execution for its domain. |
| Hierarchical Image Coding (lO6I66lweK) — Spectral regularization for LIC | 5.50 (Accept Poster) | More fundamental contribution (spectral analysis of training dynamics) but some methodological ambiguities. CMIC has comparable empirical rigor with clearer ablation structure. |
| Human Aligned Compression (AuzSDvSUzg) — Compression as adversarial defense | 2.00 (Withdrawn) | Much weaker paper — lacks novelty and empirical depth. CMIC is substantially stronger. |
| SF-Mamba (X4KsowemNB) — Rethinking SSM scanning for vision | 4.50 (Reject) | Similar motivation (fixing Mamba's scanning limitations) but less thorough evaluation. CMIC has stronger empirical support. |

CMIC sits between the MambaSIC (4.00) and the Hierarchical Coding paper (5.50). It has stronger empirical validation and better efficiency analysis than the lower-scoring anchor, but its technical novelty is less fundamental than the higher-scoring anchor's spectral analysis contribution. The overclaimed SOTA statement and moderate component-level novelty prevent a higher score, while the thorough evaluation and clear efficiency gains prevent a lower one.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>