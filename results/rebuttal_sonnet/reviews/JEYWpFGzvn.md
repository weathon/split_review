Now I have read the full paper and can evaluate the rebuttal carefully. Let me produce the updated review.

---

## Summary

INFOTok proposes an information-theoretically grounded framework for adaptive discrete video tokenization. Building on top of Cosmos Discrete Video Tokenizer, it adds an ELBO-based router that allocates token budgets proportional to per-video information complexity, and a transformer-based adaptive compressor that selects the highest-information tokens. The paper proves that uniform adaptive routing is biased, and demonstrates empirically that INFOTok substantially outperforms ElasticTok across all compression rates, datasets, and metrics, while requiring only 1× (vs. 11×) additional NFEs at inference.

---

## Rebuttal Assessment

---

**Weakness: 50% vs. 20% token savings inconsistency**
- **Author's response:** Partially address
- **Assessment:** Partially convincing — The authors correctly explain that the two figures compare against *different* baselines: 20% savings vs. Cosmos-DV (BPP₁₆ = 1.00 → 0.81 at matched PSNR 30.08 vs. 30.01 and FVD 49 vs. 49, confirmed in Table 1), and 50% savings vs. Open-MAGVIT2 (BPP₁₆ = 1.12 → 0.56, where INFOTok *surpasses*, not merely matches, Open-MAGVIT2 quality per Table 1). The factual defense is defensible in a narrow sense — INFOTok at 0.56 BPP₁₆ does objectively outperform Open-MAGVIT2 at 1.12 BPP₁₆ on all metrics. However, the introduction's phrase "without loss of reconstruction quality compared to state-of-the-art fixed-length tokenizers" still attributes "state-of-the-art" status to Open-MAGVIT2, which Table 1 clearly contradicts (Cosmos-DV dominates Open-MAGVIT2 on every metric). The rebuttal promises a revision but the paper, as submitted, remains misleading. The defense confirms the data is factually consistent only if the reader knows which baseline to apply to which claim — something the introduction does not make clear.
- **Score impact:** Weakness downgraded (from a clear contradiction to an acknowledged framing problem), but not removed — the paper as submitted still presents the 50% figure misleadingly.

---

**Weakness: Practical router drops the KL term without formal justification**
- **Author's response:** Partially address
- **Assessment:** Partially convincing — The rebuttal adds a new argument not in the paper: since FSQ is deterministic quantization, the posterior q_φ(z|x) is effectively a delta function, making the KL term approximately constant across videos. This is a plausible argument but it exists only in the rebuttal, not in Section 3.1. The paper's text (verified at lines 156) simply states: *"using the reconstruction error itself (without the KL term) to derive r_β(N_x|x) is sufficient, as the KL term is approximately proportional to the reconstruction error, and the ratio is similar"* — a bare assertion with no evidence. The rebuttal promises to add a scatter plot in revision; this does not count. Theorem 3.1 still applies to the full ELBO, not the reconstruction-only surrogate.
- **Score impact:** Weakness unchanged — the paper provides no empirical or theoretical evidence for the proportionality claim.

---

**Weakness: Table 2 shows INFOTok-Flex sometimes exceeds "Optimal" upper bound**
- **Author's response:** Partially address
- **Assessment:** Partially convincing — The rebuttal's explanation (FVD's high variance causes sampling noise; the bound is strict *in expectation* but stochastic evaluation introduces variance) is reasonable and consistent with the data: PSNR consistently respects ordering (Optimal ≥ INFOTok-Flex in all six PSNR rows, confirmed in Table 2), and the FVD reversals are 3–10 units in magnitude, plausible as noise given FVD's known instability. The rebuttal promises to soften the "strict upper bound" language; this correction is not in the paper as submitted. The internal framing inconsistency (calling it "a strict upper bound" while showing reversals) remains.
- **Score impact:** Weakness downgraded (the explanation is plausible and PSNR ordering is consistent) but not removed — the paper's framing is still internally inconsistent.

---

**Weakness: Missing ablation — fixed-rate Cosmos-DV at lower BPP**
- **Author's response:** Acknowledge
- **Assessment:** Unconvincing — The authors explicitly acknowledge the confound is not resolved and would require retraining the base tokenizer, which they did not do. The Table 3 (Right) ablation confirms ELBO routing helps regardless of architecture but does not separate adaptive routing benefit from additional model capacity (both routing strategies in the ablation share the added transformer). The weakness stands.
- **Score impact:** Weakness unchanged.

---

**Weakness: Evaluation restricted to 256×256; no downstream task evidence**
- **Author's response:** Acknowledge
- **Assessment:** Unconvincing as a defense — The rebuttal accurately points to Section 4 and Section 6's Limitations, where the paper acknowledges the constraint. But acknowledging a limitation is not the same as addressing it. The lack of downstream evidence remains a gap.
- **Score impact:** Weakness unchanged.

---

**Weakness: Theorem 3.1 upper bound explanation lacks transparency (Trivial)**
- **Author's response:** Partially address
- **Assessment:** Partially convincing — The paper does state (lines 154–155): *"Notice that β ≥ −E[ELBO(x)] ≥ E[−log p(x)]... providing a strong theoretical guarantee when β is selected appropriately,"* which partially conveys the slack interpretation. The rebuttal promises to add a one-sentence clarification in revision. Not yet in the paper but this was already classified as Trivial.
- **Score impact:** Weakness unchanged (trivial; no impact on score).

---

## Strengths
- **Large, consistent empirical gain over ElasticTok:** At BPP₁₆ = 0.56, FVD drops from 194→70 (TokenBench) and 930→540 (DAVIS); PSNR improves ~2 dB; LPIPS improves 25–40% (Table 1, Figure 4). Unambiguous margins consistent across both datasets and all metrics.
- **ELBO router near-oracle quality (Table 2):** PSNR gap of ≤0.1 dB and FVD gap of ≤10% versus the optimal search-based strategy at all tested BPP₁₆ levels, with PSNR ordering universally respected. This is clean validation of the ELBO proxy's informativeness.
- **Architecture-agnostic ablation (Table 3, Right):** ELBO routing on both the Cosmos backbone (PSNR 29.30 vs. 27.35, FVD 71 vs. 152) and ViT backbone (PSNR 28.64 vs. 27.21, FVD 114 vs. 198) consistently outperforms uniform routing. This separates routing gains from model architecture.
- **11× inference efficiency over ElasticTok:** One additional decoder pass for ELBO vs. log₂(4096)−1=11 NFEs for binary search (Figure 4g, Section 4.2). A concrete, practically significant advantage.
- **INFOTok-Flex single-model multi-rate capability:** Training with mixture of β values achieves on-par performance with separately trained single-rate models across all compression levels (Figure 4, Table 1).

---

## Weaknesses

### Fatal
None.

### Major

- **Introduction's "50% token savings" remains misleadingly attributed to "state-of-the-art":** The rebuttal's defense confirms the 50% figure requires comparing against Open-MAGVIT2, not Cosmos-DV. But the introduction says "without loss of reconstruction quality compared to *state-of-the-art* fixed-length tokenizers" — and Table 1 shows Cosmos-DV dominates Open-MAGVIT2 on every metric. The rebuttal acknowledges the need for revision but does not fix it in the submitted paper. The abstract correctly says "20% tokens saved"; the introduction contradicts this. This remains a substantive overclaiming issue.

### Minor

- **Practical router drops KL term without in-paper justification:** The rebuttal's explanation (FSQ determinism makes KL approximately constant) is plausible but appears only in the rebuttal, not the paper. Theorem 3.1 applies to the full ELBO; the implemented router is a surrogate with no formal guarantee stated in the paper.
- **Table 2 "strict upper bound" framing inconsistent with observed FVD reversals:** Three cells show INFOTok-Flex outperforming "Optimal" in FVD (by 3–20 units). The rebuttal's noise explanation is reasonable (PSNR ordering holds universally), but the paper does not acknowledge this and uses "strict" language inconsistently. A revision is promised but not present.
- **Missing fixed-rate Cosmos-DV baseline at lower BPP:** The confound between adaptive routing benefit and additional transformer capacity is not resolved. The Table 3 ablation provides a partial answer but does not cleanly isolate the capacity effect.
- **Evaluation restricted to 256×256 reconstruction; no downstream task evidence:** Explicitly acknowledged as a limitation in Sections 4 and 6, but acknowledged limitations are still limitations.

### Trivial

- **Theorem 3.1 slack interpretation (β − H(p)) not explained in paper text.** Minor pedagogical gap; revision promised.

---

## Nice-to-Haves
- A scatter plot of per-video KL vs. reconstruction error (promised in revision) to validate the proportionality claim.
- Softened "strict upper bound" language in Table 2 caption with a note about FVD variance (promised in revision).
- Surface wall-clock inference time comparison from Appendix D into the main body given its prominence as a headline claim.
- One downstream experiment (retrieval, linear probing, or generation perplexity) to validate token efficiency translates to representational benefit.

---

## Novel Insights

The most genuinely novel contribution is the demonstration that ELBO-based per-sample token allocation closely approximates the exhaustive oracle at all tested compression levels (Table 2: ≤0.1 dB PSNR gap, ~5% FVD gap, with PSNR ordering universally respected). This empirically validates the information-theoretic claim that ELBO is a reliable proxy for log-likelihood complexity ordering in well-trained tokenizers — a result with potential applicability beyond video to any VAE-style modality. The formal proof that uniform-router training is *arbitrarily* biased relative to the entropy lower bound (Theorem 2.2) is also a clean theoretical contribution with practical implications.

---

## Suggestions

1. **Correct the introduction's 50% claim** to specify the comparison baseline explicitly: "50% fewer tokens than Open-MAGVIT2 with superior quality, and 20% fewer tokens than Cosmos-DV at matched quality." Remove "state-of-the-art" from the description of the 50% comparison since Cosmos-DV clearly outperforms Open-MAGVIT2.
2. **Add in-paper justification for dropping the KL term** — either a scatter plot of per-video KL vs. reconstruction error, or a formal argument using FSQ determinism to show the KL is approximately constant (the rebuttal's argument is plausible; it should be in the paper, not the rebuttal).
3. **Soften "strict upper bound" language** in Table 2 and acknowledge that FVD reversals at this magnitude are within evaluation noise.
4. **Add a fixed-rate lower-BPP Cosmos-DV baseline** or quantify the compressor parameter count relative to Cosmos-DV to bound the capacity confound.

---

## Score and Decision

**Rebuttal impact summary:**
- The major weakness (50%→20% inconsistency) is downgraded from "clear contradiction" to "acknowledged framing problem that requires revision" — but the revision is not in the submitted paper. The defense is partially convincing (the data does support a 50% claim if you read it narrowly) but the attribution to "state-of-the-art" remains factually wrong relative to Table 1.
- The KL proportionality weakness is unchanged — the rebuttal's explanation is new reasoning not in the paper.
- The Table 2 inconsistency is downgraded slightly (the noise explanation is plausible given that PSNR ordering universally holds).
- The missing ablation and downstream evaluation weaknesses are explicitly acknowledged with no resolution.

The rebuttal is honest, competent, and does not reveal new problems. It provides plausible reasoning for some issues but does not resolve them in the submitted paper. The score should remain at **6.5**: the paper's core contributions (ELBO routing, near-oracle allocation, 11× efficiency) are well-validated and genuinely useful; the major overclaiming issue and minor theoretical gap are correctable but not yet corrected.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>