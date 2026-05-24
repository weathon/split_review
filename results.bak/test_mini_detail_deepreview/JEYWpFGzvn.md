Now I have a thorough understanding of the paper and the anchors. Let me write the final review.

## Verification of Reviewer Claims

**Claim 1 (Theoretical mismatch: lossless vs lossy):** Verified. The paper frames Theorem 2.1 as an "idealized scenario where the tokenizer T can perfectly reconstruct" (Section 2.2, line 69), and the Shannon Source Coding Theorem is for lossless compression. However, the abstract claims to "rigorously prove" optimality and "approach theoretical optimality" — this is overclaimed given the lossy setting. The bound in Theorem 3.1 uses H_C(D), which is the entropy of the data distribution, not the rate-distortion function. **Keeping this as Major.**

**Claim 2 (Downstream utility):** The paper explicitly says "video generation is an important downstream application, training a video generative model is extremely resource-consuming and is beyond our scope" (Section 4, line 179). This is a legitimate scope choice for a tokenizer paper. **Demoting to Minor/Nice-to-have.**

**Claim 3 (Baseline fairness):** The paper does not specify ElasticTok's base architecture in Table 1, but Table 3 (right) provides controlled comparisons on the same Cosmos and ViT backbones where InfoTok still wins. **Demoting to Minor.**

**Claim 4 (Section notes about missing rate-distortion):** The paper acknowledges the lossless framing is an "idealized scenario." The ELBO-based router is described as a surrogate. The critic's point about the four-data example being not directly applicable is accurate but the example is illustrative. **Keeping relevant parts.**

Now let me also filter the Strength Finder's output. Strength 1 claims "rigorous theoretical proof" — this should be kept but tempered. I'll keep all core strengths since they are supported by evidence, but note the theoretical ones have caveats.

---

## Final Review

## Summary

This paper proposes InfoTok, an adaptive discrete video tokenizer that uses an ELBO-based router to allocate token budgets proportionally to each video's information complexity, and a transformer-based adaptive compressor to realize variable-length token sequences. Built on top of the Cosmos-DV fixed-length tokenizer, InfoTok achieves state-of-the-art results: 20% token savings with no reconstruction loss, 2.3× better compression than the prior adaptive method ElasticTok at matched quality, and 11× fewer forward passes during inference due to avoiding the binary search needed by ElasticTok.

---

## Strengths

- **Strong empirical SOTA against both fixed-length and adaptive baselines.** Table 1 shows InfoTok at BPP₁₆=0.81 matches Cosmos-DV at BPP₁₆=1.00 on PSNR (30.08 vs 30.01) and FVD (49 vs 49), saving 20% tokens. At BPP₁₆=0.56, InfoTok outperforms ElasticTok on all four metrics on TokenBench (PSNR 29.30 vs 27.34, LPIPS 0.179 vs 0.276, FVD 71 vs 194). These margins are substantial for the tokenization task.

- **Dramatic inference-efficiency advantage.** Figure 4g shows InfoTok requires 1 additional network forward pass per video versus 11 for ElasticTok's binary search. This is a concrete practical advantage that makes adaptive tokenization computationally viable.

- **Oracle ablation validates the ELBO-based router.** Table 2 compares InfoTok's ELBO-based allocation to an exhaustive-search "Optimal" strategy across three compression levels. The two are nearly identical (e.g., PSNR 29.86 vs 29.92 at BPP₁₆=0.81), confirming that the ELBO router closely approximates the best possible allocation without brute-force search.

- **Principled information-theoretic framing for adaptive tokenization.** Theorem 2.2 formally proves that data-agnostic (uniform) routers are suboptimal — expected token length can be arbitrarily larger than the information-theoretic optimum. This provides a rigorous justification for moving beyond heuristic approaches like ElasticTok's random masking.

- **Generalizability across architectures.** Table 3 (right) shows InfoTok's ELBO-based mechanism outperforms ElasticTok's uniform masking on both the Cosmos backbone and a pure Vision Transformer backbone (PSNR 29.30 vs 27.35 on Cosmos, 28.64 vs 27.21 on ViT), demonstrating the framework is not tied to a specific architecture.

- **Ablation confirms the ELBO-based token selection in the compressor matters.** Table 3 (left) shows that masking the N_x lowest-ELBO tokens outperforms both simple right-to-left masking (PSNR 29.30 vs 27.43) and a jump-masking strategy (29.30 vs 28.07), justifying the adaptive compressor design.

---

## Weaknesses

### Fatal
None.

### Major
- **Theoretical overclaim: The optimality theorems assume lossless compression but are applied to a lossy setting.** The paper's theoretical framework (Theorems 2.1, 2.2, 3.1) builds on Shannon's Source Coding Theorem for lossless compression, where the relevant lower bound is the entropy H_C(D). However, video tokenization is fundamentally lossy (minimizing MSE reconstruction loss). The paper frames Theorem 2.1 as an "idealized scenario" (Section 2.2) but then in the abstract claims to "rigorously prove that existing data-agnostic training methods are suboptimal" and that the method "approaches theoretical optimality." Theorem 3.1's bound uses H_C(D) and log p(x), which are not the correct information-theoretic quantities for the lossy case (the rate-distortion function R(D) would be). This overclaiming undermines the rigor of the theoretical narrative. The ELBO-based router is a well-motivated heuristic — and the empirical oracle comparison (Table 2) strongly supports its effectiveness — but the theory as presented does not deliver the tight optimality guarantee that the language suggests. **The authors should reframe the theoretical claims to accurately reflect the lossy nature of the problem, acknowledge the gap, and characterize the ELBO-based router as a principled approximation rather than a proven optimal solution.**

### Minor
- **No downstream task evaluation.** The paper evaluates only reconstruction metrics (PSNR, SSIM, LPIPS, FVD). While this is standard for tokenizer papers and the authors explicitly scope out generative training due to resource constraints (Section 4), the stated motivation mentions downstream benefits. A small-scale generation experiment (e.g., training a simple video diffusion model on low-resolution data with InfoTok tokens) would substantially increase the paper's impact and validate that adaptive tokens transfer beyond reconstruction.

- **ElasticTok's base architecture is not specified in the main comparison (Table 1).** The headline table compares InfoTok (built on Cosmos-DV) with the officially released ElasticTok, but ElasticTok's base tokenizer architecture is not stated. The controlled ablation in Table 3 (right) partially addresses this by comparing both methods on the same Cosmos and ViT backbones, confirming InfoTok wins regardless. Still, the main table would benefit from stating ElasticTok's base architecture explicitly.

- **Mask storage overhead is not analyzed for extreme compression ratios.** The paper states the binary mask adds ~5% overhead in token length. However, when N_x is very small relative to N_max (e.g., 10%), the mask overhead becomes proportionally larger. An analysis of how this overhead scales would strengthen the practical characterization.

- **Results reported without confidence intervals or standard deviations.** The main results (Table 1) and ablation studies (Tables 2, 3) report single numbers. Given variability in video content, showing variance across runs or across dataset splits would strengthen the evidence, especially for the near-tie between InfoTok-Flex and the "Optimal" oracle in Table 2.

### Trivial
- The "Limitations" section (Section 6) acknowledges the downstream evaluation gap and the decoder-pass overhead, but does not address the lossy/lossless theoretical gap identified above.

---

## Nice-to-Haves
- **Replace or supplement the lossless entropy framing with a rate-distortion argument.** Even a heuristic justification backed by the strong oracle comparison (Table 2) would be more honest and no less compelling than the current theoretical overclaim.
- **Add confidence intervals or standard deviations** to the main tables.
- **Include a small-scale downstream generation experiment** (e.g., VideoGPT or latent diffusion on 64×64 or 128×128 video) to validate that token savings translate to generation efficiency.
- **Analyze mask overhead more thoroughly** when compression ratios are extreme.

---

## Removed Points
- **"The four-data distribution example is not directly applicable to real video":** The example is explicitly presented as intuition for Theorem 2.2. It is a standard pedagogical device and the paper never claims it directly applies to real video. Removed.
- **"The paper does not address how overhead scales when token lengths are small":** This is a valid point but is more of a nice-to-have analysis; it does not weaken the paper's claims. Moved to Minor (already covered above).
- **"Section 3.1: step from lossless to lossy is not justified":** The paper does frame Theorem 2.1 as an idealized scenario and uses ELBO as a surrogate. The issue is about overclaiming, not lack of justification. Merged into the Major weakness above.
- **"BPP_16 may confuse readers":** The metric is clearly explained (Section 4.1, "For instance, if the number of tokens is c·T·H·W..."). This is a parser-level presentation concern. Removed.
- **"Limitation on video resolution":** The paper notes in Section 4.1 that InfoTok can generalize to other resolutions with results in Appendix D, and the evaluation at 256px is standard when comparing against ElasticTok which only handles 256px. Removed.
- **Strength Finder claim about "rigorous theoretical proof" being a pure strength:** The theory papers over the lossy/lossless gap, so this strength is tempered by the major weakness above. It is still a strength (the suboptimality of uniform routers is proven in the idealized setting) but the weakness modifies how it should be interpreted.

---

## Novel Insights

The harsh critic's observation about the lossy/lossless mismatch in the theoretical framework is insightful and goes beyond surface-level concerns — it identifies a genuine gap between what the theorems formally establish (bounds in terms of H_C(D) under perfect reconstruction) and what the paper claims ("approaches theoretical optimality" for a lossy tokenizer). This is a nuanced point that the Strength Finder entirely missed because it accepted the theoretical framing at face value. However, the critic overstates the severity: the paper *does* characterize Theorem 2.1 as an idealized scenario, and the empirical oracle comparison (Table 2) independently validates the method's effectiveness. The novelty is that the ELBO-based router works well empirically *and* has a plausible connection to information theory, even if the connection is not as tight as claimed.

---

## Suggestions
1. **Reframe the theoretical sections.** Acknowledge explicitly that Theorems 2.1–3.1 use lossless compression as a motivating framework, and that the ELBO-based router is a principled approximation for the lossy setting, supported by the strong empirical comparison with the exhaustive-search optimal (Table 2). Remove or qualify claims of "rigorous proof of optimality" from the abstract and introduction.
2. **Add a sentence in Table 1's caption or in Section 4.1 clarifying ElasticTok's base architecture**, so readers can interpret the comparison correctly.
3. **Report standard deviations** across at least 3 runs for the main benchmark comparisons to improve statistical rigor.

---

## Score and Decision

### Calibration Process

**Round 1 — Bracketing:**
- Weak band (≤3.5): Papers like "VideoDiT" (2.50), "Balancing Token Efficiency" (2.50), "VideoGPT+" (3.40). InfoTok is clearly much stronger — it has a novel method, solid theory, and strong empirical results.
- Middle band (3.5–7.5): ElasticTok (6.00), "How many tokens is an image worth?" (5.75), BSQ-ViT (5.75), "From Pixels to Tokens" (6.00). All are accept papers in related areas.
- Strong band (≥7.5): LARP (7.50), "Vision Transformers Need Registers" (8.00).

**Initial bracket:** 6.0–8.0.

**Round 2 — Narrowing:**
- ElasticTok (6.00): The prior adaptive video tokenization work. InfoTok clearly outperforms it on all metrics (1-2 PSNR, 40-60% FVD, 11× fewer forward passes) *and* provides a principled theoretical framework. InfoTok is a substantially stronger paper.
- "How many tokens is an image worth?" (5.75): Adaptive image tokenization via recurrent processing. Limited to images and lacks the strong empirical SOTA that InfoTok demonstrates. InfoTok is stronger.
- LARP (7.50): Video tokenizer focused on downstream generation with holistic queries and AR prior. Different contribution type (generation-oriented), but comparable in overall quality. LARP achieved SOTA on UCF-101 generation; InfoTok achieves SOTA on reconstruction efficiency. InfoTok has a stronger theoretical framework but a weaker downstream validation.

**Final score:** 7.0. InfoTok is clearly above the ElasticTok/BSQ-ViT cluster at 5.75–6.0 — it has better empirical results, a more principled approach, and stronger ablations. It is comparable to LARP (7.5) but with a different contribution profile. The theoretical overclaim is a real weakness that prevents a higher score, but the empirical contributions are strong enough to place it in the upper-accept range.

### Anchors Used

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| tFV5GrWOGm.md (ElasticTok) | 6.00 | R1, R2 | InfoTok outperforms on all metrics, adds theoretical grounding, 11× fewer NFEs. Clearly stronger. |
| mb2ryuZ3wz.md (How many tokens) | 5.75 | R1, R2 | Image-only, weaker empirical results, less principled. InfoTok is stronger. |
| yGnsH3gQ6U.md (BSQ-ViT) | 5.75 | R1, R2 | Different contribution (quantization method), comparable in quality. InfoTok has stronger empirical wins. |
| 3TnLGGHhNx.md (BPE tokenizer) | 6.00 | R1 | About BPE tokenization for MLLMs, different area. |
| IqGVIU4rvM.md (Balancing tokens) | 2.50 | R1 | Reject paper, much weaker. |
| lvgsPjRtLM.md (VideoDiT) | 2.50 | R1 | Reject paper, much weaker. |
| YGWxpOI6Y0.md (VideoGPT+) | 3.40 | R1 | Reject paper, much weaker. |
| 6j0GH40mFt.md (Window attention) | 3.40 | R1 | Image compression, much weaker. |
| Wr3UuEx72f.md (LARP) | 7.50 | R2 | Video tokenizer for generation. Different focus but comparable quality. InfoTok has stronger theory but weaker downstream. |
| WNLAkjUm19.md (Discrete tokenization role) | 7.00 | R2 | Theory paper about MIM tokenization. Different topic, comparable score. |
| lKK50q2MtV.md (TokenFlow) | 7.00 | R2 | Video editing, different area. |
| pTeOOKnjGM.md (TEASER) | 7.00 | R2 | 3D face reconstruction, different area. |

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>