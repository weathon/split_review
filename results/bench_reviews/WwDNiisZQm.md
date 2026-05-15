Now I have all the information needed. Here is my consolidated final review.

## Summary

This paper introduces Content-Aware Mamba (CAM) for learned image compression, addressing two fundamental limitations of standard Mamba SSMs: the content-agnostic raster-scan order and strict causality. It proposes Content-Adaptive Token Permutation (CTP), which clusters latent tokens by cosine similarity and reorders the scan sequence to group semantically similar tokens, and Global-Prior Prompting (GPP), which injects sample-specific prompts derived from cluster centroids to relax causality. The resulting model, CMIC, achieves state-of-the-art BD-rate savings of 15.91%, 21.34%, and 17.58% over VTM-21.0 on Kodak, Tecnick, and CLIC respectively, with moderate complexity and notably lower memory footprint than prior Mamba-based compression models.

## Strengths

- **State-of-the-art rate-distortion performance**: CMIC outperforms all prior learned methods including MambaVC (by 7.51% BD-rate on Kodak) and MambaIC (by 2.36%), as well as Transformer-based models like FTIC and TCM-L, across three standard benchmarks (Table 1). The gains are consistent across PSNR, MS-SSIM, and multiple bitrate levels (Figs. 4-6).

- **Clean ablation validates both components**: Table 2 shows CTP alone yields 1.8-2.4% BD-rate improvement, GPP alone yields 0.5-1.4%, and their combination gives 2.7-3.6% total, cleanly demonstrating that both components are individually effective and complementary. Table 4 further shows CAM blocks outperform 2D Mamba and attention-only alternatives.

- **Favorable complexity-efficiency trade-off**: CMIC (69.11M params, 2.39 TFLOPs, 4.44 GB peak memory) achieves better RD than much larger models (MambaIC: 157M params, 20.32 GB memory; MLIC++: 116M params), and the CTP/GPP overhead is minimal (throughput drops from 23.19 to 22.05 samples/s, decoding latency increases from 0.387s to 0.405s) (Tables 1, 3).

- **Compelling qualitative analysis**: ERF visualizations (Figs. 7-9) show that CTP and GPP jointly produce a substantially broader, content-adaptive receptive field that aligns with semantic structures. Cluster visualizations (Fig. 10) confirm that the codebook-based grouping captures semantically meaningful tokens (e.g., red doors, clouds, feathers). Table 5 demonstrates dynamic adaptivity: only 23-26 of 64 centroids activate per image, varying across content.

## Weaknesses

### Fatal
None.

### Major

1. **Missing control for random permutation in CTP ablation.** The paper attributes CTP's ~2% BD-rate gain to content-aware grouping, but does not compare against a simple random permutation baseline. Any reordering that breaks the raster-scan order—whether content-aware or not—exposes the SSM to non-local tokens and could improve global awareness. Without this control, the paper cannot fully separate the effect of *content-awareness* from the effect of *order-breaking*. The ERF visualizations (Fig. 9) and cluster visualizations (Fig. 10) provide qualitative support for the mechanism, but a quantitative random-permutation ablation is needed to substantiate the central claim that feature-space proximity, not merely the disruption of spatial locality, drives the improvement.

2. **Missing ablation of prompt dictionary design.** The paper distinguishes GPP from MambaIRv2's prompt pool by tying prompts to cluster centroids via a learnable projection A. However, no experiment compares this design against (a) a directly learned prompt pool (as in MambaIRv2) or (b) a fixed random projection from centroids. Without this ablation, it is unclear whether the centroid-tie provides any benefit, or whether the performance gain of GPP simply comes from adding a learnable conditioning signal. This is not a fatal issue—the method works as demonstrated—but it weakens the claim about the specific design choice.

### Minor

1. **Clustering stability and hyperparameter sensitivity are not analyzed.** The clustering is central to both CTP and GPP, yet the paper does not report variance in cluster assignments across training seeds, sensitivity to the EMA decay parameter λ, or quantitative clustering quality metrics (e.g., intra-cluster similarity, silhouette score). While the provided cluster visualizations (Fig. 10) are informative, they cover only three images from one stage. Given that the entire content-adaptivity chain depends on clustering quality, some quantitative stability analysis would be valuable.

2. **The paper does not evaluate whether CTP/GPP transfer to prior Mamba-based LIC architectures.** The ablation adds CTP/GPP to the authors' own strong baseline, which already includes window attention and a custom entropy model. Demonstrating on MambaVC or MambaIC would strengthen claims about generalizability of the CAM mechanism. (Table 4 substitutes CAM with 2D Mamba within the same architecture, which partially addresses this, but does not establish transfer to existing Mamba LIC implementations.)

3. **Throughput overhead characterization.** The paper describes the ~5% throughput drop (23.19 to 22.05 samples/s) as "negligible," but the 5% figure combines both CTP and GPP overhead. A breakdown of which component costs what would be helpful. This is a very minor presentation issue; the absolute overhead remains small.

### Trivial
None.

## Nice-to-Haves

- Apply CAM to other modalities or tasks (video compression, super-resolution) to demonstrate generality.
- Analyze why CAM provides negligible gains when applied to the entropy model (mentioned in Section 4.5 but not explained).
- Report whether the number of codebooks (one per CAM block, likely 7 blocks) contributes meaningfully to the parameter count.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **Criticism that tokens are not normalized before cosine similarity (Critic Claim 3, part):** The critic states "it is not stated whether tokens are also normalized before distance computation (lines 3-4 of Algorithm 1 imply they are not)." This is incorrect. Algorithm 1, line 3 explicitly computes `(x_i^T c_j^*) / (||x_i||_2 ||c_j^*||_2)`, which normalizes both the token and the centroid. The paper is clear on this point.

- **Criticism that the baseline is "already strong" and this confounds claims (Critic Claim 2):** This is a strawman. The paper claims the *full CMIC model* achieves SOTA, not that CTP/GPP alone are responsible for all gains. The ablation (Table 2) cleanly shows marginal contributions of each component added to a fixed baseline, which is standard methodological practice. The critic's suggestion to start from a reimplementation of prior Mamba LIC methods is a nice additional experiment but not a requirement for validity.

- **Criticism about missing appendix content (Appendix A.2 comparisons with Zhang et al. 2024b):** The appendix is stripped by the PDF parser. The paper references it; its absence in the parsed text is a tool artifact, not an author error.

- **"5% throughput drop is small but not negligible":** 5% training throughput reduction for two new mechanisms is negligible by any standard in this field. This is a nitpick.

- **Various missing related work suggestions:** Per policy, I cannot verify whether suggested missing references exist or are relevant, so these are removed.

- **Formatting/style nitpicks and typo-related complaints:** These are parser artifacts.

## Novel Insights

The reviews surface an interesting tension in evaluating "content-adaptive" mechanisms: distinguishing genuine content-awareness from the general benefit of breaking structural priors (raster order, spatial locality). The paper's ERF visualization (Fig. 9) is a creative approach to this problem—showing that CTP reshapes the ERF toward semantically relevant regions rather than spreading activation uniformly—but the missing random-permutation baseline means the evidence for content-awareness is qualitative (ERF shape, cluster visualizations) rather than quantitative. This is a methodological challenge that extends beyond this paper to any work claiming content-adaptive token reordering: the reviewer community expects a control that isolates adaptivity from order-disruption. The paper's clustering design (codebook-based, EMA-updated) is well-motivated to avoid K-Means instability, but the lack of quantitative clustering metrics leaves a gap between the qualitative visual evidence and the strong claims about clustering quality.

## Suggestions

1. **Add a random-permutation baseline to Table 2:** Replace the CTP grouping with a fixed random permutation (shared across all images) and report the resulting BD-rate. If random permutation yields significantly less improvement than CTP, the content-awareness claim is strongly supported. If random permutation gives comparable gains, the paper should reframe its contribution accordingly.

2. **Add an ablation comparing prompt designs:** Compare centroid-tied prompts (current GPP) against (a) a directly learned prompt pool of the same size, and (b) a fixed (non-learned) projection from centroids. This would clarify whether the centroid tie itself, the learnable projection A, or simply adding a conditioning signal is the source of GPP's gain.

3. **Report clustering stability across 3 training seeds** (mean, variance of cluster assignments and BD-rate). This is inexpensive and would substantially strengthen the robustness claims.

## Score and Decision

### Calibration Anchors

| Path | Avg Score | Comparison |
|------|-----------|-----------|
| `/home/wg25r/review_agent/human_reviews_2026/0dHrYUd17W.md` (MambaSIC) | 4.00 | Mamba-based SIC with limited novelty; CMIC has more novel components (CTP, GPP) and stronger validation |
| `/home/wg25r/review_agent/human_reviews_2026/42gPoLZLQB.md` (S3Mamba) | 4.50 | SSM-based super-resolution criticized as "module replacement"; CMIC has more fundamental architectural innovation |
| `/home/wg25r/review_agent/human_reviews_2026/FXu4G5T5QZ.md` (ARPC) | 5.00 | Accepted poster at similar tier; CMIC has more thorough evaluation and cleaner ablations |
| `/home/wg25r/review_agent/human_reviews_2026/lO6I66lweK.md` (Taming Hierarchical) | 5.50 | Accepted poster with strong spectral analysis; CMIC has comparable empirical performance but higher methodological novelty |
| `/home/wg25r/review_agent/human_reviews_2026/YDRoTtmXu1.md` (CoTAM) | 6.00 | Accepted poster; CMIC's novelty and evaluation thoroughness are comparable |
| `/home/wg25r/review_agent/human_reviews_2026/R5xBLfD9Dv.md` (SSMs for Neural Repr.) | 5.00 | Accepted poster; different topic, similar clarity and evaluation depth |
| `/home/wg25r/review_agent/human_reviews_2026/AuzSDvSUzg.md` (Human Aligned Compression) | 2.00 | Low-scoring anchor; CMIC is dramatically more rigorous and substantial |
| `/home/wg25r/review_agent/human_reviews_2026/XpvgGoTrza.md` (CSA-LIC) | 3.33 | Withdrawn/reject; CMIC is far stronger in methodology, evaluation, and results |

The paper is solid and makes genuine contributions. The missing random-permutation baseline is the most significant weakness, but it does not invalidate the core results—the paper still demonstrates SOTA performance with moderate complexity and provides compelling qualitative evidence for the claimed mechanism. Relative to the calibration anchors, CMIC sits above the 5-5.5 range (papers accepted with moderate enthusiasm) but below the 7+ range (exceptionally strong papers where every claim is fully controlled). The paper's contributions are well-motivated, the experiments are thorough, and the writing is clear.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>