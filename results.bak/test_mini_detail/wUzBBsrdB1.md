Now I have a comprehensive calibration picture. Let me write the final consolidated review.

---

## Summary

This paper studies how the L0 hyperparameter (average number of active features per token) in sparse autoencoders (SAEs) affects feature quality. Using toy models with known ground-truth features and validating on Gemma-2-2b and Llama-3.2-1b, the paper shows that if L0 is set too low, SAEs mix correlated features to improve reconstruction at the cost of monosemanticity — and that if L0 is too high, degenerate solutions also emerge. The authors propose decoder pairwise cosine similarity (c_dec) as a diagnostic to identify problematic L0 values, and show that its "elbow" aligns with peak sparse probing performance. A central finding is that sparsity-reconstruction tradeoff plots are misleading because a corrupted SAE can outperform a ground-truth SAE on reconstruction at low L0.

## Strengths

1. **Clean toy model demonstration of the core failure mode (Section 3.1–3.3).** The paper shows concretely that at low L0, SAE decoder latents mix positive components of positively-correlated features and negative components of negatively-correlated features (Figures 2, 3). This provides direct, visualizable evidence for why low L0 corrupts monosemanticity — a point previously obscured by aggregate sparsity-reconstruction plots.

2. **MSE loss actively incentivizes wrong features (Section 3.3).** The paper constructs a ground-truth SAE (with correct features) and shows it achieves MSE 4.88, while a trained SAE with mixed features achieves MSE 2.73 at the same L0=5. This is concrete proof that the loss function pushes away from correct features at low L0 — a genuinely non-obvious and important result.

3. **Sparsity-reconstruction tradeoff plots are shown to be actively misleading (Section 3.4, Figure 4).** The trained SAE outperforms the ground-truth SAE on variance explained across all L0 values below the true L0. This is a direct critique of standard evaluation methodology: the metric would reject a perfect SAE in favor of a corrupted one.

4. **c_dec is a simple, well-motivated diagnostic that works in toy models and correlates with probing in LLMs (Sections 3.5, 4).** The metric is minimized at the true L0 in toy models (Figure 6), and its "elbow" aligns with peak sparse probing F1 in both Gemma-2-2b and Llama-3.2-1b (Figure 8). This provides a practical tool for practitioners to detect problematic L0 values.

5. **Validation across two LLMs, two SAE architectures, and multiple layers (Section 4).** The paper tests on Gemma-2-2b and Llama-3.2-1b with both BatchTopK and JumpReLU SAEs, demonstrating that the c_dec pattern and its relation to probing performance generalizes beyond a single setting.

## Weaknesses

### Fatal
None.

### Major

1. **The "correct L0" concept is well-defined in toy models but its meaning in real LLMs is ambiguous, and the paper's LLM validation rests on a single proxy (sparse probing) without direct feature-quality validation.** In toy models, ground-truth features and their firing distribution are known, so the "correct L0" is unambiguous. In real LLMs, the paper relies on sparse probing (Kantamneni et al., 2025) as a proxy for feature correctness and shows the c_dec elbow aligns with peak probing F1. This is reasonable but circumstantial: peak probing performance could arise from more active features providing more signal even if those features are not perfectly monosemantic. The paper does not directly validate that features at the c_dec-elbow L0 are more monosemantic (e.g., via human evaluation or automated interpretability scores). The paper acknowledges this limitation in Section 6 ("we do not view this as a perfect guide"), which is good, but the central framing — that c_dec identifies the "correct" L0 in LLMs — is stronger than the evidence directly supports. This is an evidential gap that limits confidence in the strongest claims about LLMs, though it does not invalidate the contribution.

2. **The claim that "most commonly used SAEs have an L0 that is too low" is an extrapolation not directly supported by the paper's experiments.** The paper observes that many open-source SAEs on Neuronpedia have L0 < 100 and shows that in their own trained SAEs, L0 < ~200 yields degraded c_dec and probing performance. However, the paper does not compute c_dec or probing performance on any existing third-party SAE from Neuronpedia. The extrapolation is plausible, but the claim (stated in the abstract and Section 6) would be stronger if tested directly. As written, it overstates what the experiments directly demonstrate.

### Minor

3. **The c_dec-probing alignment in LLMs is qualitative, not quantified.** Section 4 notes that "the elbow just before c_dec jumps due to low L0 is around L0 200, and this also corresponds to peak sparse probing performance" (Figure 8), but no quantitative measure is provided — e.g., a table comparing the elbow L0 to the peak probing L0 for each layer/model, or a correlation coefficient. Given that the alignment between c_dec and probing is the central methodological claim for LLMs, a simple quantitative summary would substantially strengthen the paper.

4. **The theoretical grounding for c_dec assumes orthogonal ground-truth features, but real LLM features are only approximately orthogonal.** The paper states that LRH posits "nearly orthogonal" features (Section 3) and its toy model uses strictly orthogonal features. The c_dec metric's validity at nonzero feature correlations is not formally analyzed (the appendix reference for formal justification is in the stripped portion). The LLM c_dec values of 0.02–0.03 (not zero) are consistent with near-orthogonality, and the metric still works empirically, but a brief ablation with near-orthogonal features in the toy model would strengthen the theoretical connection.

5. **LLM probing results show mean F1 across 3 seeds without error bars or significance tests.** Given the small seed count, the variance matters. The paper should at minimum state whether the observed differences are meaningful (e.g., standard deviations or confidence intervals).

### Trivial
None.

## Nice-to-Haves

- A quantitative table comparing the c_dec elbow L0 vs. peak probing L0 for each layer and model in Section 4.
- A brief toy-model experiment with near-orthogonal (rather than strictly orthogonal) features to test whether c_dec remains a reliable indicator under more realistic conditions.
- Evaluation of c_dec on a few representative existing SAEs from Neuronpedia to directly support the claim about commonly used SAEs having too low L0.

## Removed Points

- **Criticism about missing theoretical justification for c_dec in non-orthogonal settings being a "structural concern":** The paper does provide theoretical justification (Appendix A.6, referenced in Section 3.5) and the empirical patterns across two LLMs and two SAE architectures are consistent with the metric working despite approximate orthogonality. Downgraded from "Critical Issue" to Minor weakness #4 above.
- **Criticism about "sparsity-reconstruction tradeoff claim being potentially overstated":** The paper's toy model demonstration (Section 3.4, Figure 4) directly supports this claim. The harsh critic's counterargument about practitioners comparing Pareto fronts misses the paper's actual claim: that at a *fixed* low L0, better reconstruction does not imply better features. Removed as factually incorrect.
- **Strength about "provides theoretical justification for c_dec":** This is a generic strength that overlaps with the paper's own description. Merged into core strengths.
- **Strength about "validates findings across multiple LLMs and SAE architectures":** This is adequately captured already.

## Novel Insights

The harsh critic and strength finder together surface one genuinely novel synthesis: the paper's central finding that *low L0 is not merely a neutral sparsity tradeoff but actively corrupts features* is convincingly proven in toy models and opens a new line of practical questions for the SAE community. The insight that MSE loss *rewards* incorrect features at low L0 (Section 3.3) is particularly crisp: it means practitioners cannot trust reconstruction metrics to select among SAEs at different L0 values. The JumpReLU result (Section 3.6) — that the training method "sticks" near the correct L0 — is underexplored and hints that training dynamics themselves may encode information about the underlying feature distribution.

## Suggestions

1. **Add a quantitative table** comparing c_dec elbow L0 vs. peak probing L0 for each layer and model combination in Section 4. This would turn a qualitative observation into a measurable claim and is a simple addition.
2. **Quality the claim about existing SAEs** in the abstract and Section 6 from "most commonly used SAEs have an L0 that is too low" to something like "our results suggest that many commonly used SAEs may have an L0 that is too low, as evidenced by..." — unless the authors can directly test a few existing SAEs.
3. **Include error bars or standard deviations** in the LLM probing plots (Figure 8, 9) or explicitly state the variance across seeds in the text.
4. **Explicitly discuss the ambiguity of "correct L0" in real LLMs** as a limitation — the paper acknowledges limitations generally but does not address this specific point directly.

## Score and Decision

**Calibration procedure (summary):**

**Round 1 (Bracketing):** Searched three score bands for papers on SAE L0, feature quality, and interpretability.
- Weak band (<3.5): papers scoring 1.67–3.00 — mostly withdrawn/rejected papers on unrelated SAE topics. This paper clearly outranks all of them.
- Middle band (3.5–7.5): key anchors include "Towards Principled Evaluations" (avg 7.0, Accept Poster), "Adaptive Sparse Allocation" (avg 5.5, Reject), "Compute Optimal Inference" (avg 4.67, Withdrawn), "SAGE" (avg 4.0, Withdrawn).
- Strong band (>7.5): "Scaling and evaluating SAEs" (avg 8.2, Oral) — a landmark paper on SAE scaling laws far exceeding this paper's scope.

Initial bracket: 5.5–7.5.

**Round 2 (Narrowing):** Queried for papers in (4.5, 6.5) and (5.5, 7.5) on related topics. Read in full:
- "Rethinking Evaluation of SAEs through Polysemous Words" (avg 5.75, Accept Poster): similar scope (new evaluation method for SAEs), but had conceptual concerns and limited validation. **This paper is stronger** — its toy model evidence is more direct, and its findings have clearer practical implications.
- "Residual Stream Analysis with Multi-Layer SAEs" (avg 6.5, Accept Poster): novel method, limited validation, fewer insights. **This paper is comparable** — both make solid contributions with some scope limitations.
- "Efficient Dictionary Learning with Switch SAEs" (avg 7.0, Accept Poster): strong practical contribution but limited to one model. **This paper is slightly weaker** — the LLM validation is less definitive than Switch SAE's Pareto improvement demonstration.
- "Towards Principled Evaluations" (avg 7.0, Accept Poster): rigorous evaluation framework but limited to one task. **This paper is broadly comparable** — both have strong toy-model-style validation and honest limitations.

The paper's core toy-model findings are genuinely strong and its LLM validation, while not definitive, is extensive. The evidential gaps (weaknesses 1–3 above) are real but addressable and do not undermine the central contribution. The paper is stronger than the 5.75 and 5.5 anchors and sits between 6.5 and 7.0 anchors — closer to 6.5 given the LLM validation limitations.

**Final score: 6.5. Decision: Accept.**

All anchor papers retrieved (across all rounds):

| Paper Path | Avg Score | Round | Comparison |
|---|---|---|---|
| /home/wg25r/review_agent/human_reviews/WxqWuG431g.md | 2.60 | R1 | Much weaker — unrelated topic, withdrawn |
| /home/wg25r/review_agent/human_reviews/bIb1xhSCVY.md | 3.00 | R1 | Much weaker — narrower scope, withdrawn |
| /home/wg25r/review_agent/human_reviews/UbLvSPMvMA.md | 1.67 | R1 | Much weaker — different SAE topic, withdrawn |
| /home/wg25r/review_agent/human_reviews/zgHamUBuuO.md | 3.00 | R1 | Much weaker — not about SAE for LLMs |
| /home/wg25r/review_agent/human_reviews/1Njl73JKjB.md | 7.00 | R1/R2 | Slightly stronger — more rigorous eval framework but limited to one task |
| /home/wg25r/review_agent/human_reviews/ghH6YYDs15.md | 4.67 | R1/R2 | Weaker — theory paper with limited empirical validation |
| /home/wg25r/review_agent/human_reviews/TIjBKgLyPN.md | 5.50 | R1/R2 | Weaker — incremental architecture contribution, rejected |
| /home/wg25r/review_agent/human_reviews/sknUS8X9q0.md | 4.00 | R1/R2 | Weaker — poorly presented evaluation framework, withdrawn |
| /home/wg25r/review_agent/human_reviews/tcsZt9ZNKD.md | 8.20 | R1 | Much stronger — landmark SAE scaling paper, Oral |
| /home/wg25r/review_agent/human_reviews/I4e82CIDxv.md | 8.00 | R1 | Much stronger — broader scope, Oral |
| /home/wg25r/review_agent/human_reviews/WCRQFlji2q.md | 9.00 | R1 | Much stronger — different topic, Oral |
| /home/wg25r/review_agent/human_reviews/5Ca9sSzuDp.md | 8.00 | R1 | Much stronger — different model/topic, Oral |
| /home/wg25r/review_agent/human_reviews/HpUs2EXjOl.md | 5.75 | R2 | Weaker — conceptual concerns, limited validation |
| /home/wg25r/review_agent/human_reviews/XAjfjizaKs.md | 6.50 | R2 | Comparable — both have solid contributions with scope limits |
| /home/wg25r/review_agent/human_reviews/k2ZVAzVeMP.md | 7.00 | R2 | Slightly stronger — clearer Pareto improvement demonstration |
| /home/wg25r/review_agent/human_reviews/Pa1vr1Prww.md | 5.00 | R2 | Weaker — applied SAE paper, rejected |
| /home/wg25r/review_agent/human_reviews/ZLAQ6Pjf9y.md | 5.60 | R2 | Weaker — applied domain (radiology), rejected |

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>