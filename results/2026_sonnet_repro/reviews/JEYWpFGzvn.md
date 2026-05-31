Now let me read the calibration anchors for scoring.Let me read two key anchors and then do Round 2 narrowing.Now let me do Round 2 calibration to narrow within my bracket of 5.5–7.0.Now I have sufficient calibration data. Let me read one more anchor for the 7.0 range.Now I have sufficient calibration data to write my final review.

**Calibration summary:**
- **Round 1 bracket:** The direct baseline ElasticTok scored 6.0; comparable adaptive tokenization papers (BSQ, ALIT) scored 5.75. Strong anchors are at 7.5–8.0 but are not thematically close. Initial bracket: **5.5–7.0**.
- **Round 2 anchors:** "On the Role of Discrete Tokenization" (7.00) has comparable theoretical depth but smaller experimental scope; ElasticTok (6.00) is INFOTok's direct baseline; BSQ/ALIT (5.75) are clearly below INFOTok. INFOTok is clearly above 6.0 (beats ElasticTok on every metric with principled theory and 11× inference efficiency), but the overclaiming, absent downstream tasks, and dropped KL term keep it below 7.0. **Final score: 6.5**.

---

## Summary

INFOTok proposes an information-theoretically grounded framework for adaptive discrete video tokenization. Building on top of an existing fixed-rate tokenizer (Cosmos Discrete Video Tokenizer), it adds an ELBO-based router that allocates token budgets proportional to per-video information complexity, and a transformer-based adaptive compressor that selects the highest-information tokens to retain. The paper proves theoretically that uniform adaptive routing is biased, and demonstrates empirically that INFOTok substantially outperforms ElasticTok across all compression rates, datasets, and metrics while requiring only 1× (vs. 11×) the number of function evaluations at inference.

---

## Strengths

- **Large, consistent empirical gain over ElasticTok across all metrics:** At BPP₁₆ = 0.56, FVD drops from 194→71 (TokenBench) and 930→581 (DAVIS); PSNR improves by ~2 dB; LPIPS improves by 25–40% (Table 1, Figure 4). These margins are unambiguous and consistent across both datasets.
- **ELBO router approaches an exhaustive oracle (Table 2):** The near-oracle comparison validates the core mechanism without brute-force search: PSNR gap of ≤0.1 dB and FVD gap of ≤10% versus the optimal search-based strategy at all tested BPP levels. This is the cleanest evidence that the ELBO proxy is informative.
- **Architecture-agnostic ablation (Table 3, Right):** Applying the ELBO routing on top of the ElasticTok backbone and a ViT backbone both show consistent gains of ~1.5 dB PSNR and ~40% FVD improvement over uniform routing in the same framework. This distinguishes the gain from the routing mechanism versus model architecture.
- **11× inference efficiency improvement:** INFOTok requires only one additional decoder pass to compute ELBO and assign token length; ElasticTok requires log₂(4096)−1 = 11 NFEs for binary search (Section 4.2, Figure 4g). This is a concrete, practically important advantage.
- **Flexible multi-rate tokenizer (INFOTok-Flex):** Training a single model with a mixture of β values achieves on-par performance with separately trained single-rate models across all compression levels (Figure 4), with PSNR matching and FVD within 10% on TokenBench.

---

## Weaknesses

### Fatal
None.

### Major

- **Inconsistency between the introduction's "50% token savings" and the actual result of "20%":** The introduction states: *"INFOTOK can save approximately 50% tokens without loss of reconstruction quality compared to state-of-the-art fixed-length tokenizers"* (Section 1, page 3). However, Section 4.2 explicitly states: *"INFOTOK performs similarly to Cosmos-DV with 20% tokens saved."* And Table 1 confirms: Cosmos-DV (the actual SOTA) runs at BPP₁₆ = 1.00, while INFOTok at BPP₁₆ = 0.81 achieves equivalent quality — approximately 19% token savings. The 50% figure derives from comparing INFOTok at 0.56 BPP₁₆ against Open-MAGVIT2 at 1.12 BPP₁₆, but Open-MAGVIT2 is clearly not state-of-the-art by the paper's own evidence (Cosmos-DV dominates it on every metric in Table 1). This is not a framing nuance — the introduction's claim directly contradicts the experimental section's claim while inflating the headline result by 2.5×. The claim must be corrected to match what the data shows against Cosmos-DV.

### Minor

- **Practical router departs from the stated theoretical framework without formal justification:** Section 3.1 describes the ELBO-based router, which formally requires both the reconstruction term and the KL divergence. But the same section states: *"using the reconstruction error itself (without the KL term) to derive r_β(N_x|x) is sufficient, as the KL term is approximately proportional to the reconstruction error."* This assertion is made without any empirical evidence or theoretical argument. The KL term is neither measured nor bounded. The empirical results may still hold, but the theoretical guarantee in Theorem 3.1 applies to the full ELBO, not to the reconstruction-error-only proxy. The paper should either provide evidence for the proportionality claim or acknowledge that the implemented router is a surrogate for the theoretical one.

- **Table 2 shows INFOTok-Flex sometimes exceeds the "Optimal" upper bound without acknowledgment:** At BPP₁₆ = 0.56 on TokenBench, INFOTok-Flex achieves FVD = 71 versus Optimal = 74; at BPP₁₆ = 0.31 on TokenBench, FVD = 155 vs. 165; at BPP₁₆ = 0.56 on DAVIS, FVD = 581 vs. 601. The paper labels "Optimal" as *"a strict upper bound"*, yet in several cells INFOTok-Flex outperforms it. This is almost certainly noise given FVD's variance, but the paper does not comment on it, leaving the framing of "Optimal" as a strict upper bound inconsistent with the observed data.

- **Missing ablation: fixed-rate Cosmos-DV at lower BPP:** The key confound is whether INFOTok's gains over Cosmos-DV (saving 20% tokens) reflect the benefit of *adaptive* token allocation or simply additional model capacity (the 8-layer transformer compressor and decompressor). The Table 3 (Right) ablation shows ELBO routing vs. uniform routing in the same framework — a meaningful partial answer — but a Cosmos-DV variant trained from scratch at lower fixed rate (e.g., at 4×10×10 or similar spatial downsampling) would resolve the question more cleanly. Without it, the "adaptive vs. lower-capacity fixed-rate" tradeoff remains open.

- **Evaluation restricted to 256×256 reconstruction only; no downstream task evidence:** All experiments are on 256×256 crops to match ElasticTok's constraint. While the paper notes generalization to other resolutions in Appendix D, the central motivation for token efficiency is downstream model scalability (generation, understanding). The paper acknowledges this limitation and scopes it out explicitly, but a single downstream experiment (even retrieval quality or VLM probing) would substantially strengthen the motivation.

### Trivial

- **Theorem 3.1 upper bound explanation could be made more transparent:** The bound E[N_x] ≤ H_C(𝔻) + β − E[−log p(x)] can be interpreted as the slack being β − H(p), which is small when β is chosen close to the true entropy. This interpretation is not explained in the paper, making the theorem harder to unpack for readers.

---

## Nice-to-Haves

- A plot of token allocation (from the ELBO router) as a function of video complexity (e.g., motion magnitude or scene variance) would give intuitive validation that the router behaves as information theory predicts, complementing the aggregate Table 2.
- Wall-clock inference time comparison (mentioned as being in Appendix D) should be surfaced in the main body given that inference efficiency is a headline claim.
- A per-video breakdown in Table 2 comparing ELBO allocation versus Optimal allocation per video complexity bin would show whether harder videos receive proportionally more tokens as theory predicts.
- One downstream experiment (e.g., linear probing or generation perplexity on the tokenized sequences) would validate that the token savings translate to downstream benefits.

---

## Removed Points

*These points are flagged as removed; treat with caution.*

- **Harsh critic: "Theorem 3.1's bound may be vacuous in practice."** The critic claims the bound simplifies to just β. This is mathematically incorrect. The bound is E[N_x] ≤ H_C(𝔻) + β − H(p), where the slack is β − H(p). This is non-trivial when β is chosen close to H(p); the bound is only β if H_C(𝔻) = 0, which is never the case. The critic's algebraic step is wrong, so this specific form of the objection is removed. The narrower concern about the KL term being dropped is retained above as a Minor weakness.

- **Harsh critic: "Sign conventions in Eq. (4) should be made explicit."** The router r_β(N_x|x) = δ(β · ELBO(x)/E[ELBO(x)]) is well-defined through the ratio: since both ELBO(x) and E[ELBO(x)] are negative, their ratio is positive. A video with a more negative ELBO than average has ratio > 1 and receives more tokens. The sign handling is implicit but algebraically consistent. Removed as a factual misunderstanding.

- **Strength finder: "Theorem 3.1 proves near-optimal token allocation."** While the theorem is a genuine contribution, it applies to the full ELBO router and the practical implementation drops the KL term. The strength as stated conflicts with the verified Minor weakness about the theoretical gap, so it is retained in weakened form (the theory provides useful grounding but does not fully cover the implemented system).

- **Harsh critic: "Inference efficiency at 1× NFEs is overstated."** INFOTok requires one *additional* decoder pass to compute ELBO, as stated in Section 4.2. This is accurately described. Not removed—but "1× additional NFE" is correctly measured relative to the standard pipeline, as Figure 4g makes clear.

- **Harsh critic: "Comparison against FlexTok, One-D-Piece, and ALIT is absent."** All three are mentioned in related work; ElasticTok is the only video-level adaptive method. The paper's stated reason (ElasticTok's 256px constraint applies to all methods), combined with the focus on video (not image) tokenization, is a reasonable scoping decision. Removed as scope creep.

---

## Novel Insights

The most genuinely novel insight is the demonstration that ELBO-based per-sample token allocation very closely approximates the exhaustive oracle optimal allocation (Table 2), achieving within 0.1 dB PSNR and ~5% FVD, without any brute-force search. This empirically validates the information-theoretic claim that ELBO is a tight proxy for the true negative log-likelihood for well-trained tokenizers—a result with implications beyond video tokenization for any modality where ELBO-based complexity estimation could drive adaptive representation.

---

## Suggestions

1. **Correct the 50% → 20% inconsistency** in the introduction to match the abstract and Section 4.2. The introduction's claim should reference Open-MAGVIT2 explicitly if the 50% figure is to be retained, but should not label Open-MAGVIT2 as SOTA when Cosmos-DV clearly outperforms it.
2. **Provide evidence for the KL ∝ reconstruction claim** in Section 3.1: a scatter plot of per-video KL vs. reconstruction error on a validation set would either validate the assertion or reveal cases where it breaks down.
3. **Add a fixed-rate Cosmos-DV baseline** at BPP₁₆ ≈ 0.81 to isolate adaptive allocation benefit from additional model capacity. If not feasible, quantify the compressor parameter count relative to Cosmos-DV to bound the capacity confound.
4. **Acknowledge and explain** the Table 2 cases where INFOTok-Flex outperforms "Optimal" — likely FVD noise, but framing "Optimal" as a strict upper bound while showing reversals is internally inconsistent.

---

## Score and Decision

**Anchors retrieved across all rounds:**

| Path | Avg Score | Round | Comparison |
|---|---|---|---|
| tFV5GrWOGm.md (ElasticTok) | 6.00 | 1 & 2 | INFOTok's direct baseline; INFOTok clearly outperforms on all metrics with principled theory and 11× efficiency gain |
| yGnsH3gQ6U.md (BSQ Video Tokenizer) | 5.75 | 1 & 2 | Fixed-rate, weaker scope; INFOTok is more principled and addresses adaptive compression |
| mb2ryuZ3wz.md (ALIT, adaptive image tokens) | 5.75 | 1 & 2 | Image-only, heuristic approach; INFOTok is stronger in video and has theoretical backing |
| 3TnLGGHhNx.md (BPE visual tokens) | 6.00 | 1 & 2 | Different focus (LLM integration); not directly comparable |
| WNLAkjUm19.md (Discrete Tokenization Theory) | 7.00 | 2 | Strong theoretical paper, smaller experimental scope; INFOTok has broader experiments but more practical gaps |
| n64NYyc6rQ.md (SeTok) | 6.20 | 2 | Adaptive visual tokenizer for MLLMs; comparable quality |
| FlvtjAB0gl.md (Dynamic discrete visual tokenization) | 6.25 | 2 | Adaptive tokenizer; comparable scope |
| IqGVIU4rvM.md (VQ-VAE + diffusion) | 2.50 | 1 | Clearly below |
| 6j0GH40mFt.md (Learned Image Compression) | 3.40 | 1 | Clearly below |

**Round 1 bracket:** 5.5–7.0  
**Round 2 narrowing:** INFOTok is clearly above the 6.0 cluster (ElasticTok) due to substantially better empirical results, principled information-theoretic grounding, and inference efficiency. It is below the 7.0 anchor (theoretical tokenization paper) due to the major overclaiming issue, absent downstream evaluation, and the practical-vs-theoretical gap in the router. INFOTok sits between 6.0 and 7.0, closer to 6.5: better than ElasticTok in every measurable dimension, but the headline claim inconsistency and limited scope prevent it from reaching 7.0.

**Final score: 6.5 — Accept**

The paper makes a real and well-supported contribution — principled ELBO-based adaptive routing substantially outperforms heuristic random masking, and the improvement is consistent, large, and validated against an oracle. The major issue (the 50%→20% inconsistency) is a correctable overclaim rather than a methodological failure, and the core empirical and theoretical results hold up under scrutiny.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>