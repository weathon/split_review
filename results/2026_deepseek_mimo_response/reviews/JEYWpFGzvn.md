Now I have enough calibration data. Let me finalize the review.

**Round 1 bracket:** 6.5–8.0 (clearly above ElasticTok at 6.0, likely below UQDM at 8.0)

**Round 2 narrowing:** 
- LTC (7.20): Comparable theoretical rigor (proves suboptimality of existing methods), similar practical scope. INFOTOK's ablation validation (Table 2) is arguably cleaner.
- ClusterMIM (7.00): Similar theoretical+empirical structure. ClusterMIM had weaker experiments (ImageNet-100 only) while INFOTOK has more extensive evaluation, but INFOTOK lacks downstream task evaluation.
- RECOMBINER (6.67): Less directly relevant but confirms the 6.5–7.5 range for compression papers with variational/ELBO-based methods.

INFOTOK sits between ClusterMIM (7.00) and LTC (7.20) — comparable theoretical contribution with cleaner ablation validation, but the downstream evaluation gap keeps it from scoring higher. Final score: **7.0**.

## Summary
INFOTOK proposes an adaptive discrete video tokenization framework grounded in Shannon's information theory. It introduces an ELBO-based router that determines per-video token counts proportional to information complexity, and a transformer-based adaptive compressor that selects which tokens to retain based on per-token ELBO values. The paper provides formal proofs that fixed-rate and data-agnostic adaptive tokenizers are suboptimal, and demonstrates empirically that its router achieves near-optimal routing (Table 2) while outperforming ElasticTok and matching fixed-rate Cosmos at ~20% fewer tokens.

## Strengths
- **Rigorous information-theoretic foundation (Theorems 2.1, 2.2, 3.1):** The paper formally proves that uniform routing is arbitrarily suboptimal (Theorem 2.2: E[N_x] ≥ κ·H_C(D) for any κ>1) and that the proposed ELBO-based router approaches theoretical optimality (Theorem 3.1). This elevates the contribution beyond heuristic design to principled foundations that prior adaptive tokenizers (e.g., ElasticTok) lack.
- **ELBO router empirically matches exhaustive optimal routing (Table 2):** The ablation comparing INFOTOK-Flex against brute-force optimal routing shows nearly identical performance — within ~0.1 dB PSNR across all compression rates and both datasets. This directly validates the core theoretical claim.
- **Substantial improvements over ElasticTok (Table 1, Figure 4):** At matched BPP₁₆=0.81, INFOTOK reduces FVD by ~60%, LPIPS by ~25%, and improves PSNR by ~1.6 dB over ElasticTok on TokenBench. INFOTOK at BPP₁₆=0.56 outperforms ElasticTok at BPP₁₆=0.81 (PSNR 29.27 vs 27.34).
- **11× inference efficiency improvement (Figure 4g):** INFOTOK requires one additional decoder forward pass vs. ElasticTok's 11-pass binary search per 4096-token block.
- **Architecture-agnostic design validated (Table 3 Right):** The ELBO-based mechanism consistently outperforms uniform routing across both Cosmos (3D-CNN) and pure ViT backbones, demonstrating the contribution is not tied to a specific architecture.
- **Single-model multi-rate flexibility (INFOTOK-Flex):** Training one model with mixed β values performs comparably to separately trained models at each rate (Figure 4, blue vs. green lines).

## Weaknesses

### Fatal
None

### Major
- **No downstream task evaluation limits the significance claim.** The paper's motivation (lines 13, 28) frames the work around enabling downstream video understanding/generation with LLMs, yet all experiments evaluate only reconstruction metrics (PSNR, SSIM, LPIPS, FVD). The paper acknowledges this in Section 6 ("beyond our current scope"), but the gap between the stated value proposition and validated claim is substantial. The binary mask auxiliary structure, variable-length token sequences, and ELBO-based token selection (which may discard "rare" but semantically important content) could interact with downstream models in ways reconstruction metrics don't capture. Even a small-scale downstream experiment (e.g., autoregressive video prediction) would substantially close this gap.

### Minor
- **The binary mask introduces non-standard auxiliary structure.** The binary mask m (Section 3.2, line 162) is stored alongside the discrete token sequence with ~5% overhead. This means INFOTOK's output is not a pure sequence of discrete tokens — it has auxiliary structure that downstream architectures must handle specially. The paper does not discuss how this mask would be represented or integrated in practice.
- **KL-term approximation not directly validated.** The router uses reconstruction error alone (without KL) because "the KL term is approximately proportional to the reconstruction error, and the ratio is similar" (line 156). Table 2 provides indirect validation (ELBO router ≈ optimal), but a direct scatter plot of per-video KL vs. reconstruction error would more explicitly confirm this assumption.
- **Evaluation limited to 256×256 square crops.** The main results use only 256×256 crops on two datasets (line 172), explained by ElasticTok's input requirements. While the paper claims generalization in Appendix D, the main results are narrow for a video tokenizer paper.

### Trivial
None

## Nice-to-Haves
- Quantify the computational overhead (parameter count, training time) of the 8-layer transformer adaptive compressor compared to the base Cosmos tokenizer.
- Provide a concrete proposal for how downstream models would consume the variable-length token sequences plus binary mask.
- Include at least one higher resolution (e.g., 512×512) in the main results.

## Removed Points
These points are flagged to be removed, treat them with caution.
- **"Per-token ELBO computation may not be truly free" (from harsh critic):** This concern misunderstands the paper. Line 138 explains that the initial decoder pass produces a full reconstruction from which per-token errors are computed, and line 162 correctly states this doesn't require extra network evaluations. The decoder output is spatially/temporally localized, enabling standard per-token error decomposition.
- **"FVD as a reconstruction metric is unusual":** FVD is standard in video tokenizer evaluation (used by Cosmos, ElasticTok, and other baselines in Table 1).
- **"2.3× claim represents best-case operating points":** The paper explicitly states this from specific points on Figure 4 (line 221), and the curves show consistent superiority across ALL operating points, not just selected ones.
- **Formatting/typos/grammar:** Parser artifacts only.

## Novel Insights
The paper's key insight is that the information-theoretic framework not only motivates adaptive tokenization in principle (via Shannon's theorem) but produces a concrete, provably near-optimal algorithm (ELBO-based routing) that is empirically validated to match exhaustive optimal search within 0.1 dB. The formal demonstration that uniform routing (Theorem 2.2) is arbitrarily suboptimal — not just suboptimal by a constant factor — is a strong negative result that should redirect the field away from data-agnostic adaptive approaches.

## Suggestions
- Add at least one small-scale downstream experiment (e.g., autoregressive video prediction or captioning) to validate that compression gains translate to downstream tasks.
- Include a direct empirical validation of the KL-proportionality assumption (scatter plot of per-video KL vs. reconstruction error).
- Propose a concrete scheme for how downstream models consume the mask + token representation.

## Calibration Report

**Anchors retrieved:**
| Paper | Path | Avg Score | Round | Comparison |
|-------|------|-----------|-------|------------|
| VQ-VAE+Diffusion tokenization | IqGVIU4rvM | 2.50 | 1 | Weak; heuristic, no theory. INFOTOK much stronger. |
| TextEconomizer | DsMxVELk3K | 3.00 | 1 | Weak; text compression, limited scope. INFOTOK much stronger. |
| VideoDiT | lvgsPjRtLM | 2.50 | 1 | Weak; video generation, not tokenization. INFOTOK much stronger. |
| DM-Codec | UFwefiypla | 3.00 | 1 | Weak; speech tokenization, different domain. INFOTOK much stronger. |
| ElasticTok | tFV5GrWOGm | 6.00 | 1 | Direct baseline; INFOTOK formally proves it suboptimal and achieves substantially better results. INFOTOK stronger. |
| How many tokens | mb2ryuZ3wz | 5.75 | 1 | Variable-length image tokenization without theoretical grounding; lacked optimality analysis that INFOTOK provides. INFOTOK stronger. |
| BSQ | yGnsH3gQ6U | 5.75 | 1 | Video tokenizer with BSQ; good engineering but no adaptive theory. INFOTOK stronger theoretically. |
| BPE tokenizer | 3TnLGGHhNx | 6.00 | 1 | Image tokenizer for MLLMs; different contribution type. Comparable quality. |
| Progressive Compression UQDM | CxXGvKRDnL | 8.00 | 1 | Progressive diffusion compression; universal 8s, cleaner single insight. INFOTOK slightly below due to downstream gap. |
| ViT Registers | 2dnO3LLiJ1 | 8.00 | 1 | Different domain (ViT artifacts). Not directly comparable. |
| LTC | Tv36j85SqR | 7.20 | 2 | Proves suboptimality of scalar quantization; similar theoretical rigor. INFOTOK comparable but LTC's contribution is more fundamental. |
| ClusterMIM | WNLAkjUm19 | 7.00 | 2 | Theory of discrete tokenization for MIM; limited experiments (IN-100). INFOTOK has stronger experiments. |
| RECOMBINER | VkWbxFrCC8 | 6.67 | 2 | Variational compression; less directly comparable. |
| TokenFlow | lKK50q2MtV | 7.00 | 2 | Video editing with diffusion features; different contribution. |
| MotionAura | bW9fGYo44s | 7.33 | 2 | Video generation with discrete diffusion; different focus. |

**Round 1 bracket:** 6.5–8.0 (clearly above ElasticTok at 6.0; below UQDM at 8.0)
**Round 2 narrowing:** Between ClusterMIM (7.00) and LTC (7.20). INFOTOK has a stronger ablation validation than ClusterMIM but a downstream evaluation gap. Comparable theoretical rigor to LTC. Final score: **7.0**.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>