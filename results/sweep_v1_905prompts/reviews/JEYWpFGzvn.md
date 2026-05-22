Now I have all the information needed. Let me produce the final consolidated review.

## Summary

InfoTok introduces an information-theoretic framework for adaptive discrete video tokenization. It proves that fixed-rate and uniform-adaptive routers are suboptimal (Theorem 2.2), proposes an ELBO-based router that achieves near-optimal token allocation (Theorem 3.1), and implements a transformer-based adaptive compressor that selects tokens by per-token information content. Empirically, InfoTok saves ~20% tokens over Cosmos-DV at equivalent reconstruction quality and outperforms ElasticTok by substantial margins (e.g., +1.8 dB PSNR, −62% FVD at matching compression) while requiring only 1 additional NFE versus ElasticTok's 11.

## Strengths

- **Theoretical grounding for adaptive tokenization (Theorem 2.2, Theorem 3.1).** The paper provides two rigorous theorems: one proving that data-agnostic uniform routers can produce arbitrarily suboptimal expected token lengths, and another showing that the proposed ELBO-based router achieves near-optimal compression (bounded additive gap) when the tokenizer is well-trained. This goes beyond the purely heuristic approaches of prior work like ElasticTok.

- **Strong empirical validation with clean ablations.** Table 1 shows InfoTok at BPP₁₆=0.81 achieves PSNR 30.08 vs. Cosmos-DV's 30.01 at BPP₁₆=1.00 (~19% fewer tokens for the same quality), and outperforms ElasticTok by 1.0–2.0 dB PSNR at matching compression. The ablation in Table 2 shows the ELBO-based router matches an exhaustive optimal search within <0.1 dB PSNR. Table 3 (left) isolates the compressor contribution, showing ELBO-based masking substantially outperforms R2L and Jump schemes. The consistency across both TokenBench and DAVIS datasets strengthens the results.

- **Inference efficiency advantage.** InfoTok requires only 1 additional decoder pass (for ELBO computation) compared to ElasticTok's 11 NFEs for binary search over token lengths (Figure 4g). This is a practical advantage validated by the paper.

- **Clean, modular framework.** The approach is built on top of existing fixed-length tokenizers (Cosmos-DV), making it compatible with future advances in base tokenizer architectures. The separation of the router and adaptive compressor is conceptually clean.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **Per-token ELBO computation is underspecified.** The adaptive compressor (§3.2) selects tokens based on "per-token log-likelihood, which is also approximated via the ELBO values." However, the ELBO in Equation 3 is defined as a single scalar over the entire video. The paper does not explain how per-token values are derived from this global quantity — whether from per-patch reconstruction error aggregated over each token's spatial-temporal footprint (natural given Cosmos's 3D CNN structure with 4×8×8 downsampling), per-token KL terms, or some other decomposition. While the ablation results confirm the approach works, this omission affects reproducibility. The authors should specify the aggregation procedure.

- **Token length rounding from the continuous router is not specified.** Equation 4 defines the router as r_β(N_x|x) = δ(β·ELBO(x)/E[ELBO(x)]), but the right-hand side is a continuous value while N_x must be a positive integer. The paper does not state whether flooring, rounding, or another discretization is used. The same issue applies at inference: β is computed as N_max·(BPP₁₆ − 1/16), but how this maps to an integer token count is implicit. This should be stated explicitly.

- **The theoretical optimality guarantee (Theorem 3.1) is stated under an idealized optimality condition** ("if the tokenizer manages to minimize the reconstruction loss") that no neural tokenizer can fully achieve. The paper's rhetoric ("near-optimal compression," "optimal up to the approximation error") somewhat overstates the practical certificate that the theorem provides. While this is standard for information-theoretic analysis, the framing could be more carefully qualified to distinguish the conceptual justification from the empirical claim.

- **No variance or confidence intervals reported.** Table 1 and Figure 4 report single-point metrics. Given that BPP₁₆ values for adaptive methods are per-dataset averages, reporting standard deviations or confidence intervals would help assess the statistical significance of the reported improvements.

- **Comparison to adaptive baselines is limited to ElasticTok.** Other adaptive methods mentioned in §5 (ALIT, CAT, FlexTok) are not benchmarked, even as image-only comparisons. Since the method applies to images (footnote 1), a brief image-domain comparison would strengthen the "state-of-the-art" positioning.

### Trivial

- The EMA momentum hyperparameter for the normalization term E[ELBO(x)] is not specified.
- The transformer hidden dimension in the adaptive compressor is not stated (only the number of layers, 8, is given).

## Nice-to-Haves

- Reporting wall-clock inference latency on representative hardware would strengthen the efficiency claim beyond the NFE proxy.
- A brief description of how the binary mask is serialized into the token sequence (to justify the "~5% overhead" claim) would improve clarity.

## Removed Points

- **Weakness about ElasticTok comparison fairness (different backbones):** The paper already provides the critical controlled comparison in Table 3 (Right), which compares both mechanisms on the same Cosmos architecture. The cross-paper comparison in Table 1 is supplemental.
- **Weakness about BPP averaging not being stated explicitly:** The paper reports average BPP₁₆ values and this is clear from context. The phrase "average compression rate" is used in §4.2.
- **Weakness about "optimal" baseline being unfair:** The paper explicitly calls it a "strict upper bound" in Table 2's caption.
- **Weakness about theorem proofs being in the appendix:** This is standard practice; the appendix is present in the original submission.
- **Strength about "addressing an important problem":** Generic; not specific to this paper's contribution.
- **Strength about inference efficiency:** Already captured in the main strengths above.
- **Strength about ablation showing ELBO masking outperforms alternatives:** Already captured in the main strengths.

## Novel Insights

Beyond the paper's own contributions, the most noteworthy observation coming out of the review process is the clean convergence of the empirical ablations with the theory: the ELBO-based router matches an oracle that exhaustively searches over all compression rates (Table 2, within <0.1 dB PSNR), and the ELBO-based masking scheme substantially outperforms heuristic alternatives (Table 3 left). This provides unusually direct evidence that the theoretical principle is being realized in practice, rather than the theory and empirics operating at arm's length.

## Suggestions

1. **Specify the per-token ELBO computation.** Clarify whether it uses per-patch reconstruction error, per-token KL, or a combination, and describe the spatial-temporal mapping from tokens to pixels.
2. **State the discretization method** for mapping the continuous router output to integer token lengths (floor, round, or otherwise).
3. **Add variance information** (std. dev. or IQR) to the main results tables.
4. **Qualify Theorem 3.1's scope** more explicitly: "Under the idealized assumption of a globally optimal tokenizer, the expected token length is bounded within an additive gap… This provides a principled justification for the ELBO-based router, though in practice the gap also depends on approximation quality."

## Score and Decision

**Anchor papers considered (all rounds):**

| Anchor | Avg Score | Round | Comparison to InfoTok |
|---|---|---|---|
| ElasticTok (tFV5GrWOGm) | 6.00 | R1/R2 | Direct baseline; InfoTok has stronger theory, better results, better efficiency |
| ALIT: "How many tokens" (mb2ryuZ3wz) | 5.75 | R1/R2 | Image-only, weaker results, no theory; InfoTok is stronger |
| BSQ-ViT (yGnsH3gQ6U) | 5.75 | R1/R2 | Different contribution (quantization); InfoTok addresses a different problem |
| "Role of Discrete Tokenization" (WNLAkjUm19) | 7.00 | R1 | Different topic (SSL/MIM theory); comparable theoretical depth |
| LARP (Wr3UuEx72f) | 7.50 | R2 | Different focus (generation); stronger empirically in downstream tasks but InfoTok has better theory |
| BPE Visual Tokenizer (3TnLGGHhNx) | 6.00 | R2 | Different approach; InfoTok is stronger |
| VideoDiT (lvgsPjRtLM) | 2.50 | R1 | Weak paper; not comparable |

**Round 1 bracket:** Plausible score range [5.5, 7.5]. The paper is clearly above the weak anchors (2.5–3.0) and in the same topic space as ElasticTok (6.0) and ALIT (5.75), but with stronger theory and results.

**Round 2 narrowing:** Comparing directly against ElasticTok (6.0), InfoTok has provably better adaptive routing theory, 1.0–2.0 dB higher PSNR at matching compression, and 1 vs. 11 NFEs. All ElasticTok reviewers scored it 6. InfoTok is clearly stronger, placing it above 6.0. However, compared to LARP (7.5), InfoTok has a narrower evaluation scope (reconstruction only, no downstream generation) and some minor presentation gaps, which prevent it from reaching that tier.

**Final score: 6.5** — a strong paper with principled theory and convincing empirics that clearly advances the state of the art in adaptive video tokenization.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>