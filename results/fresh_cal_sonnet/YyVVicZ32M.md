Now let me run the calibration search (Round 1 — bracketing) while I continue reading:Now let me do Round 2 narrowing calibration:Now let me read two more anchors to nail down the score:Now I have sufficient information to write the final review. Let me verify the key claims about Algorithm 1 once more before proceeding:Now I have everything I need to write the final authoritative review.

---

## Summary

This paper introduces the Permute-and-Flip (PF) decoder as a replacement for softmax sampling in LLM text generation. The method, adapted from McKenna & Sheldon (2020)'s differentially private selection mechanism, is proven to share the same $(2/T)$-stability as softmax sampling while achieving provably better expected utility at the same temperature. Building on the Report-Noisy-Max equivalence of PF sampling, the authors design the PF watermark — an original analog of Aaronson's Gumbel watermark — with a tractable null distribution that admits exact false-positive-rate control. Experiments on Llama-2-7B and TinyLlama validate both the quality improvement and watermark detectability.

---

## Strengths

1. **Clean Pareto-optimality proof (Theorem 3.1, item 5).** The paper proves that PF decoding is never dominated by any equally $(2/T)$-stable decoder: for any competitor that achieves higher expected utility at some logit configuration, there must exist another logit configuration where the competitor is worse. This is a genuine and non-trivial guarantee; Example 3.2 + Figure 1 quantify the up-to-2× advantage concretely in the binary-logit case.

2. **Novel, tractable watermarking design with exact FPR control.** Theorem 4.3 (statement 2) establishes that under the null, and given unique m-grams, the test score follows exactly Gamma(n-m, 1). This gives a closed-form threshold guaranteeing FPR = α. Figure 4 validates this empirically across multiple datasets and keys, with empirical FPR tracking the theoretical α values across settings.

3. **Honest framing of prior-work dependencies.** The paper explicitly states that Theorem 3.1 "follows directly from McKenna & Sheldon (2020)" and that "our contribution is in applying this method to LLM decoding and connecting these known theoretical results to the broader ML audience." This transparency is admirable and allows the reader to correctly attribute the genuine novel content (PF watermark and its analysis) versus the exposition of known results.

4. **Robustness of the PF watermark.** The paper demonstrates (Appendices C.1.1 and C.2.2) that the PF watermark remains detectable after paraphrasing attacks and even with only 30 tokens, supporting practical deployability.

---

## Weaknesses

### Fatal
None.

### Major

- **The FPR-control "key strength" claim is not exclusive to PF watermark.** Section 5 presents "its ability to precisely control the false positive rate" as the *key* distinguishing strength of PF watermark. However, the Gumbel watermark test score under the null is $\sum_{t} -\log(1-r_t(y_t))$, where $r_t(y_t) \sim \text{Uniform}([0,1])$ when text is independent of the key. Since $-\log(1-U) \sim \text{Exp}(1)$, the Gumbel null distribution is also $\text{Gamma}(n-m, 1)$ under the same unique-m-gram assumption — identical to PF watermark's null. Consequently, the Gumbel watermark admits the same exact threshold rule with the same FPR guarantee. The paper never establishes this comparison, leaving the "key strength" characterization misleading with respect to Gumbel. (The claim may hold meaningfully against KGW, whose binomial-based test score depends on correlated tokens and does not admit the same clean closed form.) At minimum, the FPR control presentation should clarify which baseline(s) it distinguishes from.

### Minor

- **The empirical quality comparison is mathematically predetermined at fixed temperature.** Table 2 runs PF and softmax at the same temperature $T$. Because Theorem 3.1 item 3 proves $\mathbb{E}_{y \sim \text{PF}}[u(y)] \geq \mathbb{E}_{y \sim \text{Softmax}}[u(y)]$ for any logit configuration, the reported perplexity advantage is a logical consequence of the theorem rather than an empirical discovery. The genuinely informative comparison — matching the diversity or entropy of both methods and then measuring quality — is done analytically for the two-token case in Figure 2b but is absent from the experiments. This gap means the paper cannot claim from its experimental section that PF offers a *practical* advantage over softmax at the same diversity level; it only confirms in-distribution that the theoretical guarantee holds.

- **Detection comparison saturates, limiting its informativeness.** The paper itself notes "all watermarking methods achieved near-perfect detection accuracy on the C4 dataset" (Section 5). In this saturated-TPR regime, a claim of "best balance of the highest detection accuracy and lowest perplexity" is not well-supported, since detection accuracy has no meaningful room to vary. The more revealing regime (shorter texts, lower entropy) is treated in the appendix but not the main results.

- **Theorem 4.3 statement 2 uniqueness condition under-discussed.** The exact $\text{Gamma}(n-m, 1)$ null distribution requires that all m-grams in $y_{1:n}$ are unique. For short texts or texts with repeated phrases, this condition is violated and the FPR guarantee becomes approximate. The paper does not discuss the magnitude of degradation in practice, and Figure 4's validation does not include cases where m-gram uniqueness is violated.

### Trivial

- The "up to 2x better" language in the abstract and title is correct (Theorem 3.1 item 4 is an existence claim), but a brief clarification that this bound is achieved in a specific degenerate configuration (Example 3.2) rather than uniformly across all logit regimes would avoid over-reading.

---

## Nice-to-Haves

- **An entropy-matched empirical comparison.** Choose temperatures $T_\text{PF}$ and $T_\text{Softmax}$ such that the two decoders produce distributions with the same average entropy per token; then compare perplexity, repetitiveness, and detection power. Figure 2b provides the exact analytic template for this comparison — running it on actual LLM outputs would be the paper's most compelling empirical result and would directly test whether the Pareto-optimality proof (Theorem 3.1 item 5) translates to practice.

- **Clarify FPR control across all three watermarks.** A short side-by-side derivation showing that PF and Gumbel share the same Gamma null distribution (and hence identical FPR control), while KGW's binomial-based test relies on approximate normality, would make the FPR claim sharper and more honest.

- **Detection comparison outside the TPR ceiling.** Running the watermark comparison on shorter texts (where TPR is not near 1) in the main body (not appendix) would make the detection results more informative and support the "best balance" claim more directly.

---

## Removed Points

*These points are flagged for removal; treat them with caution.*

- **Algorithm 1 fallback concern (harsh critic).** *Removed — factually incorrect.* For the maximum-logit token $y^*$, the Bernoulli probability in line 7 of Algorithm 1 equals $\exp((u_t(y^*) - u_t^*)/T) = \exp(0) = 1$. The inner loop always terminates when the permutation reaches $y^*$, which it must since $y^* \in \tilde{\mathcal{V}}$. The algorithm is fully specified.

- **Top-p/Top-k omitted from experiments (harsh critic).** *Weakened/removed.* The paper's focus is on stable decoders. Table 1 lists Top-p and Top-k as "not stable"; if true, they fall outside the paper's stated scope. Criticizing the absence of methods outside scope is scope creep.

- **"Up to 2x better" headline misrepresents (harsh critic).** *Removed.* Theorem 3.1 item 4 is stated as an existence claim ("there exists logits..."), and "up to" in the abstract correctly conveys a worst-case bound. This is not a misrepresentation.

- **Section 3 inconsistency with Section 4 experimental framing (harsh critic).** *Weakened/merged into Minor.* The distinction between fixed-temperature and fair (diversity-matched) comparison is acknowledged in the paper (Figure 2a caption explicitly says the same-temperature comparison is unfair to Gumbel). The inconsistency with the experiments is real but falls under the Minor weakness about the predetermined nature of the empirical comparison.

- **Generic strength about "important problem" (strength finder).** *Removed* — generic strength without paper-specific grounding.

- **Strength about demonstrating highest TPR among baselines (strength finder).** *Partially removed.* The TPR advantage in Figure 3b is real but occurs in a saturated regime; this is noted in the Minor weaknesses and the strength is only kept narrowly.

---

## Novel Insights

The paper's most intellectually interesting observation is that the PF watermark's advantage derives not from direct detectability superiority at fixed temperature, but from the freedom to *increase* temperature for PF (because PF is more greedy at any given temperature), thereby simultaneously recovering any detectability gap and preserving — or even improving — the stability parameter. This "compensate-by-raising-temperature" mechanism (Figure 2b) is a clean example of how a decoder's quality-diversity tradeoff directly determines the design space available to a watermarking scheme layered on top of it. The idea that coupling the decoding algorithm with its watermarking scheme via this temperature-compensation argument could yield a jointly optimal design is a perspective that could inform future work on distortion-free watermarking for other non-softmax decoders.

---

## Suggestions

1. Run an entropy-matched comparison as outlined in Nice-to-Haves — choose $T_\text{PF}$ and $T_\text{Softmax}$ to produce equal average per-token entropy, then report PPL, MAUVE, seq-rep-5, and TPR@1%FPR.
2. Add a paragraph or small table in Section 4/5 comparing the null distributions of PF watermark, Gumbel watermark, and KGW watermark side-by-side, making explicit which baseline(s) the FPR control claim distinguishes from.
3. Move the detection comparison under non-saturated TPR (shorter texts, currently in appendix) into the main body, as this is where the tradeoff actually manifests.
4. In Theorem 4.3, add a brief empirical study or analytical bound on how much the FPR degrades when m-gram uniqueness is violated (e.g., for texts with phrase repetition).

---

## Score and Decision

**Calibration Summary**

| Paper | Avg Score | Round | Comparison |
|---|---|---|---|
| jbfDg4DgAk (Sparse Watermarking LLMs) | 3.0 | R1 | Clearly weaker — incremental method, no principled analysis |
| V4Xs283LHH (FlashSampling) | 2.5 | R1 | Much weaker — efficiency trick only, limited novelty |
| hTUrBJqECJ (Low-entropy Unbiased Watermark) | 5.5 | R1/R2 | Comparable scope but murkier contribution hierarchy and weaker experiments |
| LdIlnsePNt (SEAL Watermarking) | 6.0 | R1/R2 | Comparable; PF paper has fewer proof issues but less ambitious theoretical claims |
| 0koPj0cJV6 (Black-box Watermark) | 4.6 | R1/R2 | Weaker — missing baselines, evaluation design gaps; PF paper is better |
| 6p8lpe4MNf (Semantic Invariant Watermark) | 5.5 | R1/R2 | Comparable scope, similar contribution size; PF paper's theory is cleaner |
| 0KHW6yXdiZ (End-to-end Logits Watermark) | 5.25 | R2 | Weaker — end-to-end optimization without principled theory |
| FBkpCyujtS (Min-p Sampling) | 8.5 | R1 | Significantly stronger — human evals, practical adoption, broader evaluation |
| tyEyYT267x (SAR diffusion LM) | 8.0 | R1 | Different area; significantly stronger experimental scope |

**Round 1 bracket:** 5–7.

**Round 2 narrowing:** The paper compares favorably against the 5.0–5.5 anchors (hTUrBJqECJ, 6p8lpe4MNf, 0KHW6yXdiZ) due to cleaner theoretical structure, honest attribution, and genuine novelty in the PF watermark. It is roughly on par with LdIlnsePNt (6.0), which has more ambitious theoretical claims but serious proof issues; the PF paper's analysis is correct but less ambitious. The major weakness (FPR claim vs. Gumbel) and the minor weakness (temperature-matched comparison absent from experiments) hold the paper below 7. The paper does not approach the experimental scope or practical impact of the 8+ papers.

**Assessment by axis:**
- *Originality:* Moderate. The decoding method is borrowed from DP literature; the watermark design and its analysis are novel.
- *Importance:* Good. Stable, watermarkable, quality-improving decoding is a practically relevant contribution.
- *Claims supported:* Partially. Core theoretical claims are sound (from prior work or correctly proved). The FPR control distinction vs. Gumbel is overstated. The empirical perplexity advantage is mathematically predetermined at the tested conditions.
- *Soundness of experiments:* Adequate. Real models, two datasets, relevant metrics, but the key comparison (entropy-matched) is not run.
- *Clarity of writing:* Good — clear exposition, transparent about prior work.
- *Value to community:* Solid. Introduces a useful technique to the LLM decoding community with the right theoretical framing.

**Final score: 6.0** — comparable to the LdIlnsePNt anchor (6.0), slightly above hTUrBJqECJ/6p8lpe4MNf (5.5), and well below the 8+ anchors. The paper is publishable: its genuine novelty (PF watermark, Pareto-optimality framing applied to LLMs) outweighs its real but manageable weaknesses.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>