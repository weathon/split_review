Now I have a thorough understanding of the paper and can verify each claim. Let me produce the final consolidated review.

---

## Summary

This paper introduces Content-Aware Mamba (CAM), a state-space model variant for learned image compression that addresses two key limitations of standard Mamba: its content-agnostic raster-scan order and its strict causal processing. The authors propose Content-Adaptive Token Permutation (CTP), which clusters latent tokens by feature similarity and reorders the scan sequence to group content-correlated tokens, and Global-Prior Prompting (GPP), which injects sample-specific global priors into the state-space equations to relax causality. The resulting CMIC model achieves state-of-the-art rate-distortion performance on Kodak, Tecnick, and CLIC datasets (e.g., -15.91%, -21.34%, -17.58% BD-rate over VTM-21.0) while maintaining competitive efficiency.

## Strengths

- **State-of-the-art rate-distortion performance across three datasets.** Table 1 reports BD-rate savings over VTM-21.0 of -15.91% (Kodak), -21.34% (Tecnick), and -17.58% (CLIC), surpassing all prior learned methods including recent Mamba-based models (MambaVC, MambaIC). The RD curves in Figures 4–6 show consistent gains across all bitrates.

- **Favorable complexity-performance trade-off compared to prior Mamba compressors.** As shown in Table 1, CMIC (69.11M params, 2.39 TFLOPs, 0.405s latency, 4.44 GB peak memory) substantially outperforms MambaIC in BD-rate while using 56% fewer parameters, 57% fewer FLOPs, and 78% less memory — a direct result of the single-scan design avoiding multi-directional overhead.

- **Individual contributions of CTP and GPP are cleanly ablated.** Table 2 quantifies that CTP alone yields 1.8–2.4% BD-rate savings over the vanilla Mamba baseline, GPP alone yields 0.5–1.4%, and the combination yields 2.7–3.6%, providing clear evidence that both components contribute meaningfully.

- **ERF visualizations provide strong mechanistic insight.** Figure 9 isolates the per-layer effects of CTP and GPP: (b) shows the strictly causal raster-scan ERF of vanilla Mamba; (c) shows GPP introducing non-causal activations beyond the scan boundary; (d) shows CTP replacing the raster pattern with activations spread over semantically related regions. Figures 7–8 further demonstrate that CMIC produces larger and more content-adaptive receptive fields than competing models.

- **Clustering visualizations confirm semantically meaningful grouping.** Figure 10 shows that clusters consistently group visually/semantically similar content (red doors, sky, parrot feathers). The paper also provides evidence that centroids learn semantically consistent visual patterns (e.g., centroid #10 responds to edges, #33 to smooth blue/green backgrounds) and that different images activate different numbers of centroids (Table 5), supporting the adaptivity claim.

- **Negligible inference overhead from proposed modules.** Table 3 shows only a ~5% training throughput reduction (23.19 → 22.05 samples/s) and a 4% decoding latency increase (0.387s → 0.405s), confirming the practical efficiency of the CTP+GPP mechanisms.

## Weaknesses

### Fatal
None.

### Major

1. **Missing control for non-content-adaptive permutation.** The paper's central claim is that content-adaptive grouping drives the RD improvement. However, the ablation in Table 2 only compares CTP against the vanilla raster-scan baseline — there is no comparison against a *non-content-adaptive* permutation (e.g., random permutation, luminance-sorted order, or a fixed shuffled order). The improvement from CTP could partially come from simply breaking the rigid raster-scan grid rather than from content-awareness per se. While the ERF visualizations (Figure 9(d)) and cluster visualizations (Figure 10) provide supporting evidence that the permutation is indeed content-adaptive, without this control the paper cannot fully isolate content-adaptivity as the mechanism behind the BD-rate gains. This is the most significant gap in the evaluation and should be addressed before acceptance.

2. **Gradient flow through hard clustering assignments is not addressed.** The token-to-centroid assignment uses hard argmax (Algorithm 1), and centroids are updated via EMA — explicitly described as a "non-gradient update process" (lines 129, 186). The permutation is a discrete function of these assignments. The paper never discusses how gradients flow through this discrete operation. While the SSM and the prompt projection 𝒜 are differentiable, and gradient signals can reach the token features through the permutation gathering operation, the centroids themselves receive no gradient signal from the RD loss. This is a material methodological gap: the paper draws inspiration from VQ-VAE but does not mention whether a straight-through estimator, commitment loss, or any other gradient approximation is employed. The paper should clarify the gradient path and justify why the two-optimizer setup (gradient for features, EMA for centroids) is sufficient for the RD objective.

### Minor

1. **Quantitative clustering quality metrics are absent.** Figure 10 provides compelling qualitative evidence for semantic clustering (red doors grouped together, sky grouped together, etc.), and Table 5 shows that activation counts vary per image. However, the paper does not report any quantitative clustering metrics (e.g., NMI or ARI against segmentation labels, silhouette scores). Adding such measures would strengthen the claim that clusters capture meaningful visual semantics beyond the qualitative examples shown.

2. **No comparison to a simple bidirectional (forward+backward) Mamba variant.** The paper compares against 2D Mamba (full four-directional scanning) in Table 4, showing CAM outperforms it. However, a simpler 2-pass (forward+backward) Mamba without CTP or GPP would provide a cleaner baseline for isolating the benefit of GPP's non-causal prompting mechanism versus simply running the scan in two directions. This is not a critical omission but would strengthen the analysis.

### Trivial
None.

## Nice-to-Haves

- Compare CTP against random permutation, luminance-sorted permutation, and fixed shuffled-order permutation baselines in BD-rate.
- Report NMI or ARI between cluster assignments and ground-truth segmentation masks (e.g., from ADE20K or COCO-Stuff) on a held-out set of images.
- Provide a failure case where clustering splits a coherent region across multiple clusters, with discussion of how the model compensates.
- Statistically correlate per-image activation counts (Table 5) with image complexity measures (e.g., texture entropy) to strengthen the adaptivity claim.
- Compare against a simple 2-pass forward+backward Mamba without CTP/GPP to isolate GPP's non-causal benefit.

## Removed Points

These points from the inputs were removed with justification:

- *Missing permutation baseline labeled as "fatal" / "structural flaw."* — The critic characterized this as fatal, but the paper provides multiple complementary forms of evidence supporting content-adaptivity (ERF visualizations in Figure 9 showing semantic spreading; cluster visualizations in Figure 10 showing semantic grouping; per-image adaptivity in Table 5). A missing control weakens, but does not invalidate, the core claim. Downgraded to **Major**.

- *Critic's claim that the gradient issue "means the clustering is not optimized for the rate-distortion loss... there is no guarantee and no analysis."* — The paper shows tokens receive gradient signals through the differentiable SSM path, and centroids are updated via EMA over many batches, which is standard practice in VQ-inspired architectures. The issue is the lack of explicit discussion, not a complete absence of gradient flow. Kept as **Major** with adjusted framing.

- *Critic's "Insufficient quantitative evidence for clustering semantics" characterized as a significant issue.* — The qualitative evidence (Figure 10) is strong and the paper's contribution is not about clustering quality per se. This is a **Minor** weakness — nice to have but not critical.

- *Various generic or speculative points from "Missing Parts" section* (e.g., asking for wall-clock ablation for 5% overhead claim, suggesting the gradient issue requires a "toy experiment") — these are either already addressed, scope creep, or minor improvement suggestions. Moved to **Nice-to-Haves** or removed.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Add a non-content-adaptive permutation baseline** (random permutation, luminance-sorted, or fixed shuffled order) to Table 2. If the content-adaptive version significantly outperforms random permutation, this directly validates the paper's central mechanism claim.
2. **Explicitly discuss the gradient path** through the clustering and permutation operations. Clarify whether a straight-through estimator, relaxed assignment, or other technique is used, and explain how the two-optimizer setup (gradient descent for features, EMA for centroids) is justified.
3. **Add quantitative clustering metrics** (e.g., NMI or ARI against segmentation labels) to complement Figure 10.

## Score and Decision

This paper presents a novel and well-motivated architecture for learned image compression, achieves clean SOTA results across three benchmarks with favorable complexity, and provides extensive visual analysis (ERF, clustering) that gives insight into model behavior. The weaknesses are real but addressable: the missing permutation baseline weakens the mechanism claim without invalidating the overall contribution, and the gradient analysis gap requires explicit discussion but does not collapse the method. The paper is otherwise thorough in its ablations, comparisons, and analysis.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>