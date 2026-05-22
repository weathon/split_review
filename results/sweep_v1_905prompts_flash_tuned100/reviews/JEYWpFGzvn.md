Now I have a thorough understanding of the paper and the relevant calibration anchors. Let me write the final consolidated review.

## Summary

This paper proposes InfoTok, an adaptive discrete video tokenizer that uses an ELBO-based router to dynamically determine token lengths per video based on information complexity, and a transformer-based adaptive compressor that discards the lowest-information tokens. The paper provides theoretical grounding via Shannon's source coding theorem (proving data-agnostic routers are provably suboptimal) and empirical validation showing that InfoTok matches or exceeds fixed-rate tokenizers while saving ~20% tokens, and outperforms the heuristic adaptive method ElasticTok with 11× fewer network evaluations.

---

## Strengths

**1. Principled theoretical framework with a provably biased baseline (Theorem 2.2).** The paper proves that uniform/data-agnostic routers can make the expected token length arbitrarily larger than the information-theoretic optimum (Theorem 2.2), while InfoTok's ELBO-based router achieves a bounded expected length relative to the optimal (Theorem 3.1). This moves adaptive tokenization from heuristic masking toward a principled information-theoretic approach.

**2. Controlled empirical validation shows clear improvement over ElasticTok on the same backbone (Table 3 right).** When both InfoTok and ElasticTok's masking strategy use the *same* Cosmos encoder/decoder backbone, InfoTok achieves PSNR 29.30 vs 27.35 at BPP 0.56 — a 1.95 dB gain with FVD reduced from 152 to 71. This controlled comparison cleanly isolates the benefit of InfoTok's adaptive mechanism.

**3. ELBO-based router matches an oracle optimal allocation (Table 2).** InfoTok-Flex's per-video token allocation performs within 0.1 dB PSNR of an exhaustive search-based optimal allocation on both TokenBench and DAVIS. This directly validates that the ELBO approximation is sufficient for near-optimal routing without brute-force search.

**4. Dramatic inference efficiency advantage (Figure 4g).** InfoTok requires only 1 additional network forward evaluation per video (to compute the ELBO), compared to ElasticTok's 11 NFEs from binary search. This is a concrete, well-documented efficiency gain.

**5. Generalization across architectures (Table 3 right).** InfoTok's adaptive mechanism improves over the ElasticTok baseline on both the Cosmos backbone (PSNR: 29.30 vs 27.35) and a Vision Transformer backbone (PSNR: 28.64 vs 27.21), demonstrating the method is not tied to a specific encoder/decoder design.

---

## Weaknesses

### Major

**1. The adaptive compressor ablation (Table 3 left) does not fully isolate the masking strategy from the learned compressor.** The paper compares three "compressor strategies": R2L (right-to-left masking), Jump (mask every fourth token), and Ours (ELBO-based masking). However, the paper does not specify whether R2L and Jump use the same learned Transformer compressor architecture (8-layer transformer with block-causal attention) as Ours, or whether they are simple masking operations applied to the base encoder output. Given that R2L achieves PSNR 27.43 (close to the "Cosmos+Uniform" result of 27.35 from Table 3 right, which is ElasticTok-style masking without a learned compressor), this strongly suggests the comparison may conflate the presence of the learned compressor with the masking criterion. An ablation including "R2L + Learned Compressor" is needed to separate these factors.

### Minor

**2. ElasticTok's backbone in Table 1 is not explicitly stated.** The paper compares InfoTok (built on Cosmos-DV) against ElasticTok in the main benchmark table without specifying what backbone ElasticTok uses. While the nearly identical numbers between "ElasticTok at BPP 0.56" in Table 1 (PSNR 27.34) and "Cosmos+Uniform(ElasticTok)" in Table 3 right (PSNR 27.35) strongly suggest the same Cosmos backbone, this should be stated explicitly. The controlled comparison in Table 3 right already provides the cleaner evaluation, but the main table's lack of clarity could mislead readers.

**3. No error bars or confidence intervals.** All metrics (PSNR, SSIM, LPIPS, FVD) are reported as single point estimates. For FVD in particular, variance can be substantial across evaluation seeds or dataset splits. Standard deviations or confidence intervals would help assess the reliability of the reported improvements.

**4. BPP alignment procedure for ElasticTok is not described.** The paper states "we align our methods with their settings" to match ElasticTok at BPP 0.81 and 0.56, but does not explain how ElasticTok's loss thresholds were calibrated to produce these exact BPP values. If thresholds were tuned on the test set, this would constitute a form of data leakage. The procedure should be clarified.

**5. Theorem 3.1's practical force depends on ELBO approximation quality.** The bound says the expected token length does not exceed $H_C(\mathbb{D}) + (\beta - \mathbb{E}[-\log p(\mathbf{x})])$. This is meaningful as a formal bound, but the overhead term depends on both the gap between $\beta$ and the true entropy, and the assumption that the reconstruction loss is actually minimized. The paper acknowledges the ELBO approximation gap, and the empirical validation (Table 2) compensates, but the theoretical claim of "near-optimal" is softer than it might appear at first reading.

### Trivial

None.

---

## Nice-to-Haves

- Include a "R2L + Learned Compressor" variant in Table 3 left to cleanly separate the effect of the masking criterion from the presence of the learned Transformer compressor.
- Add standard deviations to all tables and error bands to Figure 4's rate-distortion curves.
- Report wall-clock inference latency (the paper mentions this is in Appendix D, which is stripped — if it exists in the submission, it addresses the critic's concern about computational cost).
- The 2.3× compression factor referenced in the abstract and Figure 4 should be more precisely defined (e.g., "at the median operating point" or "when PSNR ≈ 28 on TokenBench").

---

## Removed Points

These are removed from the main weakness list, with justification:

- **"Theorem 3.1 is tautological"** (Harsh Critic point): Removed. The bound $H_C(\mathbb{D}) \leq \mathbb{E}[N_x] \leq H_C(\mathbb{D}) + (\beta - \mathbb{E}[-\log p(\mathbf{x})])$ is not tautological — it bounds the achieved expected length relative to the Shannon lower bound with an overhead term that depends on a controllable parameter $\beta$ and the entropy. This is a meaningful formal statement. The empirical validation in Table 2 corroborates the practical force. Downgraded to the Minor weakness (#5 above) about the assumption-dependence of the bound.

- **"Unfair comparison in Table 1 is uninterpretable"**: Removed. The numbers strongly indicate ElasticTok in Table 1 uses the Cosmos backbone (PSNR 27.34 vs Cosmos+Uniform 27.35 at BPP 0.56). The controlled comparison in Table 3 right confirms the advantage on an identical backbone. The reporting clarity issue is kept as Minor weakness #2.

- **"KL term not included in ELBO approximation"**: Removed. The paper explicitly states (Section 3.1, line 167) that they found the KL term approximately proportional, so using reconstruction error alone is sufficient. This is a reasonable engineering choice acknowledged in the paper. The critic's suggestion of a sensitivity analysis is a nice-to-have, not a weakness.

- **"Wall-clock time not reported"**: Removed. The paper states "More details regarding wall-clock inference latency comparison can be found in Appendix D" — the appendix is simply stripped from the parser output and exists in the original submission.

- **"ELBO computation adds a decoder pass"**: This is listed as a limitation by the authors themselves and is a reasonable design trade-off (1 pass vs ElasticTok's 11). Not a weakness.

- **"2.3× compression factor is imprecisely defined"**: Downgraded to nice-to-have. The visual evidence in Figure 4 supports the claim, and the text ("e.g., PSNR on TokenBench, FVD on DAVIS") provides context. A precise specification would improve the paper but is not a core flaw.

---

## Novel Insights

Beyond the paper's own contributions, the reviews surface a useful tension: the paper's main appeal (Table 1) presents cross-backbone comparisons that look impressive, but the true strength of the method is best seen in the controlled ablation (Table 3 right), where the margin against ElasticTok's strategy on the *same* backbone is ~2 dB rather than the larger spreads in Table 1. A more honest framing would elevate that controlled comparison as the headline result, with the cross-backbone context as a supplementary view. Additionally, the ambiguity in the compressor ablation (Table 3 left) reveals a common pattern in tokenization papers: when the "method" includes both a component (learned compressor) and a strategy (masking criterion), ablations often conflate the two, and the field would benefit from more disciplined isolation of these factors.

---

## Suggestions

1. **Clarify the compressor ablation.** Add a row in Table 3 left labeled "R2L + Learned Compressor" so readers can compare ELBO-based masking to R2L masking *with the same Transformer architecture*. This would cleanly separate the masking criterion from the compressor architecture.
2. **Explicitly state the backbone for ElasticTok in Table 1** (e.g., in a footnote: "ElasticTok results are on the Cosmos encoder/decoder backbone, matching the controlled setting in Table 3 right").
3. **Describe the BPP alignment procedure** — how was ElasticTok's loss threshold calibrated to produce BPP 0.81 and 0.56, and was any tuning done on the evaluation set?
4. **Add standard deviations** to all tables and error bars to Figure 4 (at minimum for FVD, which is known to have high variance).

---

## Score and Decision

**Bracket (Round 1):** The paper is clearly above the weak-band anchors (avg 2.5–3.4). The most directly comparable anchors are ElasticTok (6.0) and "How many tokens is an image worth?" (5.75). The paper is at least as strong as these — it has theoretical grounding ElasticTok lacks, better efficiency, and controlled empirical validation. The bracket is [5.5, 6.5].

**Narrowing (Round 2):** Comparing within the bracket:
- vs ElasticTok (6.0): InfoTok is stronger on theoretical grounding, inference efficiency (1 vs 11 NFEs), and principled ELBO-based routing. The presentation clarity issues (backbone ambiguity, ablation concern) bring it back slightly, placing it comparably.
- vs BSQ-ViT (5.75): Different contribution type (adaptive allocation vs quantization quality), but InfoTok's contribution is more novel and the empirical validation is similarly solid.
- vs "How many tokens is an image worth?" (5.75): InfoTok has stronger theoretical grounding and clearer evidence of improvement; its weaknesses are more about presentation than core methodology.

**Final score:** The paper has a well-motivated core idea, a principled theoretical framework, and generally solid empirical validation. The weaknesses are real but addressable — the most significant (ablation confounding) is fixable with additional clarification/reporting rather than indicating a fundamental flaw. The paper is comparable to ElasticTok (6.0) but with a more principled approach, justifying a slightly stronger position for its contribution while the presentation issues prevent a higher score.

**Anchors consulted across all rounds:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| IqGVIU4rvM | 2.50 | R1 | Much weaker — limited contribution, unclear methodology |
| lvgsPjRtLM | 2.50 | R1 | Much weaker — different problem, limited validation |
| 6j0GH40mFt | 3.40 | R1 | Weaker — image compression, not adaptive video tokenization |
| DsMxVELk3K | 3.00 | R1 | Weaker — text compression, not visual tokenization |
| tFV5GrWOGm (ElasticTok) | 6.00 | R1, R2 | Direct competitor; InfoTok is stronger on theory and efficiency, similar on empirical validation |
| mb2ryuZ3wz | 5.75 | R1, R2 | Similar topic but images only; InfoTok has stronger theory and clearer gains |
| yGnsH3gQ6U (BSQ-ViT) | 5.75 | R2 | Different contribution; both solid but InfoTok's adaptive framing is more novel |
| 3TnLGGHhNx | 6.00 | R2 | Different topic (BPE for visual tokens); less directly comparable |
| B5iOSxM2I0 | 6.50 | R2 | Different topic (NLP tokenization theory); not comparable |
| f4gF6AIHRy | 8.00 | R1 | Much stronger overall but unrelated topic |
| CxXGvKRDnL | 8.00 | R1 | Unrelated topic (diffusion compression) |
| vf5aUZT0Fz | 8.00 | R1 | Unrelated topic (language model pre-training) |
| E4Fk3YuG56 | 8.50 | R1 | Unrelated topic (LLM loss computation) |

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>