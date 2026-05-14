Now I have sufficient information. Let me produce the final consolidated review.

## Summary

This paper introduces INFOTok, an adaptive discrete video tokenizer that uses an ELBO-based router to dynamically determine token sequence lengths per video, along with a transformer-based adaptive compressor to condense fixed-length embeddings into variable-length token sequences. The work is motivated by Shannon's source coding theorem and aims to address the inefficiency of fixed-rate tokenizers. Empirical results show consistent improvements over ElasticTok (the main prior adaptive method) at matched compression rates, while requiring only 1 additional NFE vs. ElasticTok's 11.

## Strengths

- **Principled ELBO-based router with strong empirical validation**: The idea of using the ELBO (computed from the fixed-length tokenizer's reconstruction) as a proxy for information complexity to guide token allocation is well-motivated and theoretically grounded. Table 2 convincingly demonstrates that this ELBO-based allocation matches an oracle optimal search strategy across three compression levels (0.81, 0.56, 0.31 BPP₁₆), with nearly identical PSNR, SSIM, LPIPS, and FVD.

- **Consistent and substantial empirical gains over ElasticTok**: On TokenBench at BPP₁₆=0.81, INFOTok achieves PSNR 30.08 vs. ElasticTok 28.26 and FVD 49 vs. 141 (Table 1). At BPP₁₆=0.56, the gap widens further (PSNR 29.30 vs. 27.34). Figure 4 provides comprehensive rate-distortion curves across multiple compression levels, showing that INFOTok consistently dominates ElasticTok across the full operating range, not just at cherry-picked points.

- **Dramatic inference efficiency advantage**: INFOTok requires only 1 additional NFE (one decoder pass for ELBO computation) vs. ElasticTok's 11 (binary search over 4096-token blocks), as shown in Figure 4g. This is a genuine practical advantage for deployment.

- **Generalization across architectures**: Table 3 (right) shows that the INFOTok adaptive mechanism (ELBO router + compressor) consistently outperforms ElasticTok's uniform approach on both the Cosmos backbone (PSNR 29.30 vs. 27.35) and a pure ViT backbone (PSNR 28.64 vs. 27.21), demonstrating the method is not tied to a specific architecture.

- **Ablation validates compressor design choices**: Table 3 (left) shows that the ELBO-based token selection (preserving top N_x tokens by per-token ELBO) significantly outperforms right-to-left masking (R2L, PSNR 29.30 vs. 27.43) and uniform jump masking (PSNR 29.30 vs. 28.07), confirming that the information-theoretic criterion is practically beneficial beyond the router.

## Weaknesses

### Fatal
None.

### Major

1. **The "20% token savings" claim vs. Cosmos-DV is confounded by added model capacity.** INFOTok builds on Cosmos-DV by adding an 8-layer transformer-based adaptive compressor and decompressor — substantially more parameters than the base model. The paper compares INFOTok (BPP₁₆=0.81, PSNR=30.08) to the original Cosmos-DV (BPP₁₆=1.00, PSNR=30.01) and attributes the token savings to the adaptive mechanism. However, without ablating whether the extra transformer layers alone (without adaptivity) could achieve similar gains, the claim that "20% tokens are saved without performance loss" due to adaptive compression is not fully supported. The gains could partly reflect increased model capacity rather than the adaptive allocation principle. An ablation training Cosmos-DV with comparable added capacity (but uniform token allocation) would be needed to isolate the effect of adaptivity.

2. **No downstream task evaluation.** The paper explicitly motivates adaptive tokenization as enabling more efficient downstream video understanding and generation, but provides no evaluation on downstream tasks. While the authors acknowledge this limitation ("training a video generative model is extremely resource-consuming and is beyond our scope"), this substantially limits the paper's demonstrated impact. Without evidence that the adaptive tokens preserve task-relevant information, the claim that INFOTok "enables a more compressed yet accurate tokenization for video representation" is only validated for reconstruction quality, which is a proxy.

3. **The theoretical framing is overclaimed relative to what is actually proved.** The paper claims in the abstract to "rigorously prove that existing data-agnostic training methods are suboptimal" and to "approach theoretical optimality." However, the theorems (2.1, 2.2, 3.1) are stated and proved for an explicitly *idealized setting* where "the tokenizer can perfectly reconstruct any input video" — i.e., lossless compression of a discrete probability distribution. The actual method operates in a lossy compression setting with continuous video data and neural network approximations. While the paper is transparent about this idealization in Section 2.2 ("consider an idealized scenario"), the headline claims in the abstract and introduction conflate the two settings. The theory provides intuition and motivation, but does not constitute a proof of suboptimality or near-optimality in the practical setting studied.

### Minor

- **Gradient flow through discrete mask selection is not specified.** The adaptive compressor uses a binary mask m determined by ELBO values to preserve the top N_x tokens. The paper states that "the end-to-end reconstruction loss will train the adaptive compressor to transform information in tokens to be masked to the remaining positions" but does not explain how gradients are propagated through the discrete mask selection (e.g., straight-through estimator, Gumbel-softmax, or REINFORCE). This is a non-trivial implementation detail for a method where the compressor is trained jointly.

- **ELBO computed from fixed-length tokenizer may not be optimal for all target lengths.** The router computes ELBO from the fixed-length tokenizer (which was trained at a specific compression rate) and uses it to determine token lengths at different rates. The paper does not justify why ELBO values computed at one operating point provide meaningful estimates of information complexity at a different operating point. The empirical validation in Table 2 partially addresses this concern, but the theoretical justification is missing.

- **Wall-clock latency not reported.** The paper reports NFEs as an efficiency metric, which favors INFOTok (1 additional forward pass through the decoder). However, the decoder pass for ELBO computation involves the full Cosmos decoder, which may be expensive. Reporting actual wall-clock time would strengthen the efficiency claim beyond the NFEs comparison.

### Trivial

- The paper states "saving approximately 50% tokens" in the introduction (line 49) but "saving 20% tokens" in the abstract and later sections. These numbers refer to different comparisons (vs. fixed-length and vs. ElasticTok respectively), but the inconsistency is confusing.

## Nice-to-Haves

- **Ablation controlling for parameter count when comparing to Cosmos-DV.** Adding transformer layers of comparable size to the Cosmos encoder/decoder (without the adaptive mechanism) would isolate the benefit of adaptivity from added capacity.

- **Downstream evaluation on a small-scale generation or classification task.** Even a modest proof-of-concept (e.g., training a small autoregressive transformer on INFOTok tokens and comparing to fixed-length tokens at equivalent bitrates) would substantially strengthen the contribution.

- **Wall-clock timing breakdown** showing the actual overhead of the extra decoder pass vs. ElasticTok's binary search.

- **Analysis of what the adaptive compressor learns** via visualization of which spatial/temporal positions are preserved vs. masked across videos of varying complexity.

## Removed Points

These points are flagged to be removed, treat them with caution:

1. **"The paper never reports ElasticTok's performance at its own optimal loss thresholds — only at rates that match InfoTok"** — REMOVED as factually wrong. Figure 4 shows comprehensive rate-distortion curves for ElasticTok across its full operating range (varying loss thresholds), and the Table 1 comparison at matched BPP is standard practice that favors neither method.

2. **"Theorem 2.2 uses a constructed example that does not show this happens for realistic distributions"** — REMOVED as misunderstanding of mathematical proof. Theorem 2.2 is an existence result showing that uniform routers *can* be arbitrarily suboptimal for some distributions. This is standard information-theoretic analysis; the theorem does not claim it happens for *all* distributions.

3. **"The paper never specifies how the adaptive compressor can achieve minimization across variable lengths"** — REMOVED. Algorithm 1 explicitly describes the training procedure with the reconstruction loss optimized across variable lengths. The gradient flow through discrete decisions is a standard challenge addressed by various techniques (straight-through estimator, etc.).

4. **"How exactly is the mask stored?"** — REMOVED as a nitpick. The paper states the mask is stored with ~5% overhead, which is sufficient detail for a conference paper. The exact encoding scheme is a standard implementation choice.

5. **"The router is deterministic when the paper earlier frames it as potentially stochastic"** — REMOVED. The paper mentions stochastic routers as a possibility in the general framework (Section 2.2) and then deliberately chooses a deterministic one for the concrete implementation (Eq. 4). This is not a contradiction.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Disentangle capacity from adaptivity.** Run an ablation where you add comparable transformer layers to Cosmos-DV's encoder/decoder (without the adaptive compressor mechanism) and report whether the gains persist. This would cleanly separate the effect of added parameters from the effect of adaptive allocation.

2. **Tone down theoretical claims in the abstract.** Replace "rigorously prove that existing methods are suboptimal" with language that accurately reflects the idealized setting, e.g., "show using information-theoretic analysis that uniform routers are provably suboptimal in an idealized lossless setting, motivating our practical approach."

3. **Add at least one small-scale downstream experiment.** Even a simple video frame prediction or classification task would demonstrate that the adaptive tokens preserve task-relevant information, significantly strengthening the paper's real-world relevance.

4. **Report wall-clock inference time** for the full pipeline (encoder + ELBO pass + compressor + decoder) to complement the NFE comparison.

5. **Clarify gradient flow** through the binary mask in the adaptive compressor — even a brief statement like "we use a straight-through estimator for the binary mask during training" would address reproducibility concerns.

## Score and Decision

I retrieved the following anchor papers via calibration search to calibrate the score:

- **AToken** (`/home/wg25r/review_agent/human_reviews_2026/a4fSF5pGJq.md`) avg 6.50: Unified tokenizer across images/video/3D with broad scope and strong results. InfoTok has narrower scope but stronger theoretical framing and ablation validation. **InfoTok is slightly weaker overall.**

- **ARPC** (`/home/wg25r/review_agent/human_reviews_2026/FXu4G5T5QZ.md`) avg 5.00 (accepted poster): Progressive image compression with VAR. Similar level of contribution — both have clear methodology with some missing comparisons. InfoTok's evaluation is more comprehensive. **Comparable or slightly stronger.**

- **TivTok** (`/home/wg25r/review_agent/human_reviews_2026/vhGZIMF6Cg.md`) avg 4.50 (rejected): Time-invariant video tokenization. Had concerns about missing wall-clock measurements and insufficient ablations. InfoTok has more thorough evaluation and stronger theoretical grounding. **InfoTok is clearly stronger.**

- **AdapTok** (`/home/wg25r/review_agent/human_reviews_2026/dkLto1KNFV.md`) avg 4.00 (withdrawn): Adaptive video tokenization with causal constraints. Had theoretical gaps and validation concerns. InfoTok's theory and empirical validation are more rigorous. **InfoTok is significantly stronger.**

- **AdaTok** (`/home/wg25r/review_agent/human_reviews_2026/bXmsFyuQ0d.md`) avg 3.50 (withdrawn): Adaptive image tokenization with RL. Had novelty concerns and unfair comparisons. **InfoTok is much stronger.**

- **Flow-IB** (`/home/wg25r/review_agent/human_reviews_2026/iDdyA8nxgO.md`) avg 2.50 (withdrawn): Extreme video compression with flow matching. Overclaimed and poorly validated. **InfoTok is far stronger.**

The paper makes a genuine contribution — the ELBO-based adaptive router is well-motivated, validated against both an oracle optimal baseline and ElasticTok, and the efficiency advantage is clear. However, the capacity confound in the Cosmos-DV comparison and the lack of downstream evaluation prevent this from being a top-tier submission. The theoretical framing is also somewhat overclaimed relative to what is actually proved. Relative to the calibration anchors, this paper sits between ARPC (5.0, accepted) and AToken (6.5, withdrawn), closer to ARPC.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>