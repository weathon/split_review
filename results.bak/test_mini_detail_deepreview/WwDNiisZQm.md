Now I have all the information I need. Let me write the final consolidated review.

## Summary
2-3 sentence summary of the paper's contribution.

The paper introduces Content-Aware Mamba (CAM), a state-space model block for learned image compression that addresses two core limitations of standard Mamba: content-agnostic raster-scan order and strict causality. It proposes Content-Adaptive Token Permutation (CTP), which clusters tokens by feature similarity and reorders them for better redundancy removal, and Global-Prior Prompting (GPP), which injects sample-specific global priors to relax causality. The resulting model (CMIC) achieves SOTA rate-distortion performance on Kodak, Tecnick, and CLIC, surpassing prior Mamba-based models by 2–6% BD-rate while reducing parameters by 56% and memory by 78% relative to MambaIC.

## Strengths

- **Clear problem identification backed by causal evidence**: The paper identifies two specific, fundamental limitations of Mamba for image compression (content-agnostic scan order and strict causality) and proves them directly via ERF visualization in Fig. 9. The single-layer ablation (columns b–e) convincingly decomposes how each proposed component addresses each limitation: GPP introduces non-causality beyond the scan position, and CTP reshapes ERF toward semantically related regions.

- **State-of-the-art rate-distortion performance**: CMIC achieves superior BD-rate savings over VTM-21.0 on all three datasets (Table 1: –15.91% Kodak, –21.34% Tecnick, –17.58% CLIC), outperforming all prior methods including the best prior Mamba-based model MambaIC (by 2.36–6.48%) and Transformer-based models like FTIC (by ~2–3%). RD curves (Figs. 4–6) consistently place CMIC at the top across the full bitrate range.

- **Favorable efficiency–performance trade-off**: Compared to MambaIC, CMIC reduces parameters by 56% (69.11M vs. 157.09M), FLOPs by 57% (2.39T vs. 5.56T), decoding latency by 39% (0.405s vs. 0.669s), and peak memory by 78% (4.44GB vs. 20.32GB) as shown in Table 1. Throughput ablation (Table 3) shows that CTP and GPP add only minimal overhead (22.05 vs. 23.19 samples/s), while competing Mamba models are substantially slower (MambaVC at 6.55, MambaIC at 9.35).

- **Comprehensive and well-controlled ablations**: Table 2 isolates the individual contributions of CTP and GPP, showing combined BD-rate gains of 2.7–3.6% over baseline. Table 4 demonstrates that CAM outperforms alternative structures (Conv, 2D Mamba, Attention-only, CAM-only) under comparable parameter counts. Table 6 ablates cluster number K with diminishing returns beyond 64. The variance in activated clusters per image (Table 5: mean 23.27, variance 90.91 on Kodak) provides quantitative evidence of content-adaptivity.

- **Empirical demonstration of content-adaptivity and global receptive fields**: Figure 10 visualizes clustering results where tokens with similar visual attributes (red doors, sky, feathers) are consistently grouped, confirming that token permutation prioritizes feature-space proximity. Figures 7–8 show that CMIC achieves significantly larger and more content-aware ERFs compared to all competing models, with high-influence regions aligning with semantic structures.

## Weaknesses

### Fatal
None.

### Major

- **Undisclosed gradient handling for the clustering-and-permutation pipeline.** The core of CTP involves hard assignment of tokens to clusters via argmax over cosine similarities (§3.3, Algorithm 1), which is non-differentiable. The centroid codebook is updated via EMA (non-gradient). The one-hot assignment matrix Γ used for prompt generation (§3.4) is also non-differentiable. The paper explicitly states the codebook uses "non-gradient K-Means" but never explains how gradients from the rate-distortion loss are routed back through these discrete operations to update the feature encoder or the projection A. The paper claims "end-to-end" learning (contributions list) and draws inspiration from VQ-VAE, but unlike VQ-VAE's standard straight-through estimator, no gradient approximation mechanism is described. Without clarification, the claim that the model *learns* content-adaptive scanning in an end-to-end fashion is incompletely supported. The features do receive gradients through the permutation (which is differentiable as reordering), but the argmax assignments themselves cannot guide the encoder toward better clustering without a differentiable relaxation or straight-through estimator. This is a significant methodological gap that the authors must address in rebuttal.

### Minor

- **GPP mechanism is adapted from MambaIRv2 with incremental novelty.** The core conditioning operation O_i = (C + P)h_i + Dx_i (§3.4) is identical to the Attentive State-Space equation in MambaIRv2 (Guo et al., 2024a). The paper acknowledges this and describes the difference: their prompt dictionary is tied to clustering centroids rather than being a standalone learnable matrix. This is a reasonable extension, but the core conditioning innovation is inherited from prior work. The novelty lies primarily in CTP, with GPP providing complementary gains (0.7–1.2% in Table 2 ablation).

- **Missing random-permutation baseline.** The ablation in Table 2 shows clear additive gains for CTP, but it does not isolate whether the improvement stems from content-aware grouping or simply from breaking the fixed raster order. A baseline where tokens are permuted randomly (or by a content-agnostic heuristic such as sorting by norm) would cleanly separate these effects. This is important because random permutation alone might already improve over the raster baseline, and the paper should quantify the added value of clustering-specific grouping.

- **Encoding latency is not reported in the main paper.** The paper states in §4.2 that "detailed encoding latency on A100 and RTX3090 GPUs [is] provided in Appendix A.14," but this appendix is absent from the submission. For practical compression, encoding time is equally important as decoding time. The authors should include this in the main paper.

### Trivial

- The paper uses "CMIC" in most places but "CMiC" in the abstract, Figure 1 caption, and Section 1. This inconsistency should be harmonized.

## Nice-to-Haves

- Comparison with content-adaptive LIC baselines (SegPIC, Zhang et al. 2024b), which are cited in §2.3 but not experimentally evaluated. Adding these under a common evaluation protocol would directly benchmark the Mamba-based approach against existing CNN-based cluster-and-convolve methods.
- Ablation of K-Means iterations T and EMA decay rate λ (both are unspecified in the main text). Showing sensitivity would improve reproducibility.
- Ablation isolating the entropy model contribution: the current entropy model (Fig. 3) uses depthwise conv + gated MLP, which is non-standard. A control experiment with a baseline entropy model (e.g., ELIC's SCTX) would cleanly separate transform improvements from entropy model improvements.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Harsh critic's claim about MambaIC's peak memory at 20.32 GB being "unusually high" and needing verification** — This is a baseline number cited from the original MambaIC paper, not fabricated by the authors. Questioning reported baseline numbers without evidence is inappropriate.

- **Harsh critic's claim that gradients cannot flow into A through the assignment stage** — This is factually incorrect. The projection A is applied directly to centroids (U = A([c_1; ...; c_K])), producing the prompt dictionary. Gradients flow from P = ΓU back to U, and from U back to A, via the differentiable Mamba equation. The one-hot Γ acts as an indexing selector, which does not block gradients to U or A. The gradient concern is about the encoder features and centroids, not about A.

- **Strength Finder's generic strengths about "importance of the problem"** — these are superficial and not specific to this paper's contributions.

- **Criticism about missing related works comparison** — removed per policy.

## Novel Insights

Both the Harsh Critic and the Strength Finder focus on different aspects of the same two-component design (CTP + GPP), but neither fully articulates the key insight that the combination of *feature-space proximity ordering* (CTP) and *global conditioning* (GPP) addresses two distinct failure modes of SSMs for images in a complementary way. The ERF ablation (Fig. 9) reveals this cleanly: GPP alone adds non-causality but retains a raster-like activation pattern, CTP alone breaks the raster pattern but retains causal constraints, and together they produce a global, semantically-structured ERF. This decomposition into complementary mechanisms is the paper's strongest conceptual contribution, and it is well-supported by the experimental design.

## Suggestions

1. **Clarify gradient handling explicitly**: State whether a straight-through estimator, Gumbel-softmax, or other relaxation is used for the argmax in clustering and the one-hot assignment matrix. If no relaxation is used, justify why the current design still enables the encoder to learn useful features for compression (e.g., gradients flow through the permutation step to the features, even though the assignments themselves are non-differentiable).
2. **Add a random-permutation baseline** to Table 2 to quantify the gain from content-awareness specifically (vs. just breaking raster order).
3. **Include encoding latency** (or make it clearer that it is in the appendix) for practical relevance.
4. **Consider a soft clustering alternative** (e.g., weighted permutation or differentiable sorting) to allow true end-to-end optimization of the clustering objective through the rate-distortion loss.
5. **Harmonize the "CMIC"/"CMiC" naming** throughout the paper.

## Score and Decision

**Round 1 (Bracketing):** I queried three bands with similar Mamba/compression queries. Weak anchors (avg 3.00–3.40) were papers with limited novelty or different problem settings — clearly below this paper. Middle anchors included MambaVC (avg 4.80, Reject), which simply applied VSS blocks to compression and was criticized for lack of compression-specific design — our paper is substantially more novel. FAT (avg 6.00, Accept) achieved SOTA with frequency decomposition and comparable experimental rigor. Strong anchors (avg 7.50–8.00) included papers with deeper theoretical contributions (diffusion model reformulation, training acceleration paradigm) — our paper does not reach this tier. **Initial bracket: 5.5–7.0.**

**Round 2 (Narrowing):** I queried inside (5.5–7.0) and (6.0–7.5). Anchors included FAT (6.00, Accept) — a direct LIC competitor with comparable innovation level and SOTA results, but weaker ablations and no efficiency advantages. RECOMBINER (6.67, Accept) — a specialized INR compression method. Compared to FAT, CMIC has better efficiency, more comprehensive ablations (structural comparisons, K ablations, per-image cluster analysis), and ERF visualizations that directly evidence the claimed mechanisms. However, the gradient handling gap in CMIC is a real weakness that FAT does not have. Compared to RECOMBINER (6.67), CMIC is on firmer experimental ground but addresses a less underserved problem. **Final placement: CMIC sits between FAT (6.00) and the 6.5–7.0 papers — slightly above FAT due to stronger ablations and efficiency evidence, but held below 7.0 by the gradient handling omission and GPP's limited novelty. Score: 6.0.**

**Anchors retrieved:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| KgJwbsfN7G (MambaVC) | 4.80 | R1 | Much weaker — just applies VSS block to compression; our paper has compression-specific design and better results |
| HKGQDDTuvZ (FAT) | 6.00 | R1, R2 | Comparable innovation level; FAT has worse ablations and no efficiency advantage; CMIC has gradient gap not present in FAT |
| CxXGvKRDnL (Progressive Comp.) | 8.00 | R1 | Stronger theoretical contribution (diffusion + compression reformulation); CMIC is more conventional architecture work |
| GRMfXcAAFh (Oscillatory SSM) | 8.00 | R1 | Different problem (sequence modeling theory); not directly comparable |
| U67J0QNtzo (Disentangled Training) | 7.50 | R2 | Opens a new research direction (training acceleration); CMIC is in a more established paradigm |
| Tv36j85SqR (Lattice Transform) | 7.20 | R2 | Deeper theoretical contribution to compression theory |
| VkWbxFrCC8 (RECOMBINER) | 6.67 | R2 | Specialized INR compression; CMIC addresses a broader LIC architecture question |
| PQpvhUrA1C (Auto. Pretrain Mamba) | 5.75 | R2 | Different task (image classification with Mamba); not LIC-specific |

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>