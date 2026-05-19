- Decision: Accept
- Avg Score: 7.50
- Scores: 8, 8, 6, 8
Now I have all the information I need. Let me compose the final consolidated review.

## Summary

This paper presents LARP, a video tokenizer for autoregressive (AR) generative models. The key ideas are: (1) a holistic tokenization scheme using learned queries that decouples discrete tokens from individual video patches—eliminating the flattening-order problem inherent in patchwise tokenizers, and (2) a lightweight 21.7M-parameter AR transformer trained jointly with the tokenizer as a "prior" that shapes the discrete latent space for downstream AR generation, then discarded at inference. LARP achieves an FVD of 57 on UCF-101 class-conditional generation, surpassing prior published models. The ablation study shows removing the AR prior degrades gFVD from 107→190 despite improving reconstruction, cleanly validating the core thesis.

## Strengths

- **Novel holistic tokenization via learned queries.** Section 3.2 describes a clean architectural innovation: learned query tokens are concatenated with patch embeddings, and only the query latents are quantized. This breaks the rigid patch→token correspondence of prior video tokenizers (VQ-VAE, MAGVIT-v2, OmniTokenizer), enabling each token to represent any spatiotemporal region and supporting a flexible number of tokens.

- **Co-trained AR prior with convincing ablation evidence.** Table 2 provides the paper's strongest evidence: removing the AR prior increases gFVD from 107 to 190 (a 78% relative degradation) while rFVD actually improves (31→23). This cleanly demonstrates the prior specifically aligns the latent space for generation, not reconstruction. Scheduled sampling ablation (107→142 without it) further confirms robustness.

- **State-of-the-art FVD results.** On UCF-101 class-conditional generation, LARP-L-Long (632M generator) achieves gFVD 57, surpassing MAGVIT-v2-MLM (58), HPDM (66), and all AR methods by large margins (e.g., MAGVIT-v2-AR 109, OmniTokenizer 191). On K600 frame prediction, LARP achieves 5.1 gFVD, also best among AR methods.

- **Flexible token count demonstrated.** Section 4.2 and Figure 2(b) show scaling from 1024 to 256 tokens with graceful degradation, with gFVD degrading more slowly than rFVD—a practical advantage over fixed-token-count patchwise tokenizers.

- **Clean ablation isolating each component's contribution.** Table 2 systematically ablates the AR prior, scheduled sampling, deterministic quantization, prior loss weight, and CFG, allowing readers to attribute improvements precisely.

## Weaknesses

### Fatal
None.

### Major

- **The "state-of-the-art among all published video generative models" claim rests on a 1-point FVD margin (57 vs. 58) with no uncertainty quantification.** The paper reports no confidence intervals, standard deviations, or multiple-seed evaluations. Given that FVD is computed on finite generated samples, typical variance can easily exceed 1 point. The reader cannot distinguish a genuine improvement from chance variation. This overclaim is material because the paper uses the phrase "state-of-the-art among all published video generative models, including proprietary and closed-source approaches" (line 51) and repeats it in the abstract and conclusion. (The concurrent Yu et al. 2024 holistic image tokenizer is not compared, but this does not affect the UCF-101 SOTA claim since Yu et al. 2024 is on images.)

- **The mechanism by which the AR prior improves generation is claimed but not analyzed.** The paper states the prior "automatically determines an order for latent discrete tokens" and pushes them toward "an optimal configuration" (lines 10, 48–49, 379). Yet it provides zero analysis of what this learned order looks like, whether it corresponds to any meaningful spatiotemporal or semantic structure, or whether a random query ordering would yield different results. Without this analysis, the mechanism remains a black box. The empirical result (prior helps) is solid, but the paper's specific claims about "optimal token order" are unsupported. The improvement could stem from regularization effects of the NLL loss rather than from learning any structured order.

### Minor

- **The SOTA result depends on using a 632M generator, not just the tokenizer.** LARP-L with a comparable-sized generator (343M) achieves only gFVD 102–107 on UCF-101, which is worse than MAGVIT-v2-MLM (58) using a 307M generator. Only with the 632M generator does LARP achieve 57. The paper should more clearly separate the tokenizer's contribution from the generator's scaling, and include a controlled comparison at matched generator size.

- **Evaluation is limited to two benchmarks at 128×128, 16 frames.** While UCF-101 and K600 are standard, the paper's forward-looking claims about "potential for MLLMs" and "broad applicability" (abstract, conclusion) would benefit from evidence on more complex motion (e.g., Something-Something), longer videos, or higher resolution. This is acknowledged as a limitation only implicitly.

- **No visual comparison of generated videos with other methods.** Figure 3 shows reconstruction comparison with OmniTokenizer, but generated videos are shown only for LARP itself (Figures 4, 5). Qualitative comparison of generations with MAGVIT-v2 or OmniTokenizer would strengthen the perceptual claims.

- **Insufficient ablation of key hyperparameters.** The temperature (0.03) in the softmax normalization and the scheduled sampling peak rate (0.5) were not ablated. While α=0.03 vs. 0.06 is ablated, the temperature hyperparameter is known to significantly affect VQ training dynamics.

### Trivial

- The paper uses the term "state-of-the-art" more broadly than the evidence supports (marginal 1-point lead on one benchmark without uncertainty quantification).

## Nice-to-Haves

- Analysis of the learned token ordering: visualize which query tokens attend to which spatiotemporal regions; measure whether the AR prior's NLL is lower for particular orderings; compare with random orderings.
- Multiple evaluation seeds with mean and standard deviation for FVD.
- Ablation of the number of learned queries (n=1024 fixed in all experiments; the claim of "arbitrary token count" would be stronger with explicit variation).

## Removed Points

- **"No comparison with Yu et al. 2024 on image reconstruction"** — Yu et al. 2024 is a concurrent image tokenizer; the paper is about video tokenization. Not a required comparison and outside stated scope.
- **"Prior and codebook co-adaptation may cause instability/mode collapse (not discussed)"** — Speculative concern with no evidence of actual instability in the paper.
- **"No analysis of computational cost (training time, inference speed, memory)"** — Not standard for a tokenizer paper of this type; would be nice-to-have but is not a weakness.
- **"No evaluation on longer videos/higher resolution because ViT quadratic cost not discussed"** — Speculative; the paper operates at standard benchmarks for the field.
- **"AR prior model capacity (21.7M) may limit learning; no scaling study of the prior"** — Speculative, not supported by evidence in the paper.
- **Various formatting/presentation nitpicks and claims about "arbitrarily chosen" hyperparameters** — Most hyperparameters in papers are selected by validation; the paper ablates the key ones.
- **Strength Finder items about "best FVD among AR methods on K600"** — Kept as valid. **Strength Finder items about "Scheduled sampling" and "continuous AR prior architecture"** — Kept as valid. Generic strengths about "important problem" and similar are dropped.

## Novel Insights

None beyond the paper's own contributions. The two reviews mostly converge on the core strengths and weaknesses; the main novel insight from synthesis is that the paper's strongest evidence (the ablation showing AR prior's critical role) coexists with its weakest-supported claim (that the prior works via learning an "optimal token order"). This gap between clean empirical demonstration and speculative mechanistic explanation is the paper's most salient unresolved tension.

## Suggestions

1. Provide FVD with confidence intervals from multiple evaluation seeds, and temper the "state-of-the-art among all published models" claim to reflect the marginal margin and the dependence on a larger generator.
2. Analyze the learned query order—even a simple visualization of which query tokens attend to which spatiotemporal regions—to support the claim that the AR prior determines a meaningful token ordering.
3. Include a controlled comparison at matched generator size (e.g., LARP-L 343M vs. MAGVIT-v2 with comparable generator) to isolate the tokenizer's contribution.
4. Add qualitative comparisons of generated videos with other methods.
