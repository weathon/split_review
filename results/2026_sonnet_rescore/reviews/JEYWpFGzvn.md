Now I have read the full paper. Let me write the final consolidated review.

---

## Summary

INFOTok proposes an information-theoretically grounded adaptive video tokenization framework. It augments a fixed-rate video tokenizer (Cosmos DV) with an ELBO-based router that allocates token budgets per video proportional to each video's information complexity, and a transformer-based adaptive compressor that selects and retains the highest-ELBO tokens. The framework is backed by theoretical proofs showing fixed-rate and data-agnostic adaptive routers are suboptimal, and achieves substantially better quality-compression tradeoffs than the heuristic ElasticTok baseline.

---

## Strengths

- **Strong empirical advantage over ElasticTok**: At matched BPP₁₆ = 0.56, INFOTok-Flex achieves FVD 71 vs. 194 on TokenBench and 581 vs. 930 on DAVIS — a 60% and 38% FVD reduction respectively — while also improving PSNR by ~2 dB and LPIPS by 25–40% (Table 1). Figure 4 confirms this advantage is consistent across the full compression rate range.

- **ELBO router closely tracks the oracle allocation**: Table 2 shows INFOTok-Flex (PSNR 29.86, FVD 54 at BPP 0.81 on TokenBench) performing nearly identically to the exhaustive per-video length search "Optimal" (PSNR 29.92, FVD 54), validating the core theoretical claim that ELBO routing approximates the information-optimal allocation without brute-force search.

- **Architecture-agnostic ELBO routing ablation**: Table 3 (Right) shows that replacing the uniform (ElasticTok) router with an ELBO router on both the Cosmos backbone and a plain ViT backbone yields substantial consistent gains (PSNR: 29.30 vs. 27.35; FVD: 71 vs. 152 on Cosmos; PSNR: 28.64 vs. 27.21 on ViT). This isolates the routing mechanism rather than attributing gains to the system as a whole.

- **Inference efficiency**: INFOTok requires only one additional decoder pass to compute ELBO, vs. the 11 additional NFEs required by ElasticTok's binary search (Figure 4g), a practical advantage that compounds with the compression gains.

- **Adaptive compressor design matters**: Table 3 (Left) shows that ELBO-based token selection (PSNR 29.30, FVD 71) clearly outperforms right-to-left masking (R2L, PSNR 27.43, FVD 137) and spatially-dispersed masking (Jump, PSNR 28.07, FVD 84).

---

## Weaknesses

### Fatal
None.

### Major

- **Inconsistent headline claim between introduction and results**: The introduction (Section 1, final paragraph before contributions) states "INFOTOK can save approximately 50% tokens without loss of reconstruction quality compared to state-of-the-art fixed-length tokenizers." However, Section 4.2 states "INFOTOK performs similarly to Cosmos-DV with 20% tokens saved," which is consistent with Table 1 (INFOTok at 0.81 BPP₁₆ ≈ Cosmos-DV at 1.00 BPP₁₆). The 50% figure is derived by comparing INFOTok at 0.56 BPP₁₆ against Open-MAGVIT2 at 1.12 BPP₁₆, which is not SOTA — Cosmos-DV dominates Open-MAGVIT2 on every metric in Table 1. This inconsistency between the abstract's accurate 20% claim and the introduction's inflated 50% claim against an older weaker baseline misrepresents the strength of the result and should be corrected.

- **Missing fixed-rate Cosmos-DV baseline at lower compression**: INFOTok adds an 8-layer transformer compressor and 8-layer decompressor on top of the Cosmos encoder/decoder, plus additional training. The key comparison that would isolate the contribution of adaptive routing from the additional model capacity is: Cosmos-DV fine-tuned at a lower fixed compression rate (e.g., targeting BPP₁₆ = 0.81 or 0.56). Without this control, it is unclear whether the gains over ElasticTok stem from the ELBO routing mechanism itself or from the additional transformer capacity and training compute. Table 3 (Right) partially addresses this by comparing ELBO vs. uniform routing within the same architecture, showing a consistent 2 dB PSNR improvement — which does support the routing mechanism. But the cleanest missing comparison is INFOTok vs. a well-trained fixed-rate Cosmos variant at the same BPP.

### Minor

- **Theory-practice gap: KL term dropped from ELBO router**: Section 3.1 establishes the ELBO-based router (Eq. 3) with both reconstruction and KL terms, and Theorem 3.1 is proved in terms of this ELBO. However, Section 3.1 also states: "we find that using the reconstruction error itself (without the KL term) to derive r_β(N_x|x) is sufficient, as the KL term is approximately proportional to the reconstruction error." No evidence is provided for this proportionality claim. The practical router thus computes a proxy for ELBO, not ELBO itself. The empirical results are unaffected — the method clearly works — but the gap between the stated theoretical framework and the actual implementation weakens the theoretical justification.

- **Table 2 "Optimal" bound is not strict in practice**: In several cells, INFOTok-Flex achieves better metrics than the "Optimal" strategy (e.g., FVD 71 vs. 74 at BPP 0.56 on TokenBench; FVD 155 vs. 165 at BPP 0.31 on TokenBench; FVD 581 vs. 601 at BPP 0.56 on DAVIS). The paper describes "Optimal" as an exhaustive per-video search combined with dataset-level optimization — a strict upper bound. The paper does not comment on these reversals. This is likely due to FVD variance or the discrete grid of candidate lengths in the "Optimal" search, but it should be acknowledged to prevent the framing from being misleading.

### Trivial

- **Sign conventions in Eq. (4) are implicit**: ELBO is typically a large negative number; the normalization by E[ELBO(x)] (also negative) yields a positive ratio. Complex videos have more negative ELBO, so |ELBO(x)| > |E[ELBO(x)]| gives ratio > 1, hence N_x > β. This is correct directionally, but the paper does not make the sign relationship explicit. A brief clarification would prevent reader confusion.

---

## Nice-to-Haves

- Even one downstream experiment (e.g., video generation quality using the adaptive tokens, or retrieval/action recognition) would substantially strengthen the motivation, since the paper's core rationale is that token efficiency matters for downstream scalability.
- Quantifying the gap between the ELBO-estimated token count and the true per-video information complexity as a function of video complexity would turn the theoretical claim into an empirically verifiable one, rather than relying solely on average-performance proxies.
- Reporting wall-clock latency comparisons more prominently (currently in Appendix D) would complement the NFE comparison in Figure 4g.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh Critic: Theorem 3.1 bound is "vacuous" (E[N_x] ≤ β)**: The critic observes the bound simplifies to β. While technically correct (β = H_C(D) + (β − H_C(D))), the theorem's substantive content is the comparison to the ELBO approximation error, and the proof strategy is non-trivial. Demoted to Minor (theory-practice gap) rather than treated as fatal.
- **Harsh Critic: FlexTok/One-D-Piece/ALIT absent from experiments**: The paper explains that only 256×256 videos are evaluated to match ElasticTok's constraint, and all methods under the same constraint would be excluded equally. This is a scope limitation, not a fairness problem. Removed.
- **Harsh Critic: Theorem 2.2 as a worst-case existence proof only**: This is an accurate description but not a criticism; existence proofs are standard and the theorem's main contribution is the formal demonstration of suboptimality, not a characterization of typical-case performance. Removed.
- **Strength Finder: "Theorem 3.1 is rigorous"**: Retained only partially — the theorem is valid but the practical router drops the KL term, creating a verified theory-practice gap. The claim of full rigor is weakened accordingly.

---

## Novel Insights

The most genuinely novel finding in this paper — beyond its own stated contributions — is that ELBO-based adaptive routing performs nearly identically to exhaustive optimal search (Table 2) while requiring only one decoder pass. This is a non-trivial empirical finding: it suggests that reconstruction error from the base tokenizer (essentially negative ELBO) is already a near-sufficient statistic for difficulty-aware token allocation, reducing the search problem to a single forward pass. The architecture-agnostic ablation in Table 3 (Right) further shows this is not an artifact of the Cosmos architecture. Together, these findings suggest that difficulty-aware routing may be broadly adoptable as a cheap add-on to any existing fixed-rate tokenizer with minimal overhead.

---

## Suggestions

1. **Fix the 50% vs. 20% inconsistency**: Revise the introduction's "50% savings vs. state-of-the-art" claim to either correctly identify Open-MAGVIT2 as a non-SOTA baseline (with Cosmos-DV as SOTA) or replace it with the honest "20% savings vs. Cosmos-DV with equivalent quality."
2. **Add KL evidence or revise theory**: Either provide empirical evidence that KL ≈ c · reconstruction error (e.g., a scatter plot of per-sample KL vs. reconstruction error), or explicitly acknowledge the router as a practical approximation of ELBO and bound the resulting performance gap.
3. **Address Table 2 anomalies in text**: Add a brief note acknowledging that INFOTok-Flex occasionally exceeds "Optimal" in FVD (likely due to FVD variance and discrete grid approximation in the brute-force search), so readers do not question the upper-bound framing.
4. **Add Cosmos-DV low-rate comparison**: Even approximate results (e.g., fine-tuning Cosmos at 4×12×12 spatial-temporal downsampling to target BPP ~0.70) would cleanly answer the capacity vs. routing question.

---

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>3</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>4</soundness>
<clarity>4</clarity>
<community_value>4</community_value>
</subscores>