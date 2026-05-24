Now I have a thorough understanding of the paper and the calibration landscape. Let me write the final review.

## Summary

This paper studies the effect of the L0 hyperparameter (average number of active latents per token) on Sparse Autoencoder (SAE) quality. Using toy models with known ground-truth features, it demonstrates that when L0 is set too low, SAEs mix correlated features together to improve reconstruction — a form of "feature hedging" — and that standard sparsity-reconstruction tradeoff plots actually reward this incorrect behavior. The paper proposes a diagnostic metric (decoder pairwise cosine similarity, c_dec) that is minimized at the correct L0 in toy models and roughly aligns with peak sparse probing performance in LLM SAEs. The findings are validated across BatchTopK and JumpReLU architectures and two LLM families (Gemma-2-2b, Llama-3.2-1b).

## Strengths

1. **Clean toy model experiments demonstrate the mechanism directly.** Figures 2 and 3 (Section 3.1) show that when SAE L0 < true L0, decoder latents systematically contain positive (or negative) components of correlated (or anti-correlated) features, while no such mixing occurs when L0 matches the true L0. The effect is shown for both positive and negative correlations, confirming the mechanism works both ways.

2. **The paper shows that sparsity-reconstruction tradeoff plots are fundamentally misleading.** Section 3.4 (Figures 4 and 5) gives a concrete counterexample: a trained SAE with low L0 achieves higher variance explained than a ground-truth SAE with correct features at the same L0. This proves that better reconstruction at a given sparsity need not imply a better SAE — a direct challenge to standard evaluation practice in the field.

3. **The c_dec metric is well-motivated and validated across settings.** The metric (Eq. 4, Section 3.5) is minimized at the correct L0 in toy models (Figure 6, across 5 seeds) and its "elbow" before the low-L0 jump aligns with peak k=16 sparse probing F1 scores in LLM SAEs (Figure 8). Validation extends to JumpReLU SAEs (Section 3.6, Figure 7) and BatchTopK across two LLM families (Section 4, Figures 8-9), demonstrating robustness.

4. **The paper provides a mechanistic explanation for why low L0 harms SAEs.** Section 3.3 quantifies the gradient pressure: MSE loss directly incentivizes feature mixing (trained SAE MSE=2.73 vs ground-truth SAE MSE=4.88 at L0=5). This goes beyond prior qualitative discussions of feature hedging.

## Weaknesses

### Fatal
None.

### Major

1. **The claim that "most commonly used SAEs have an L0 that is too low" is insufficiently supported.** This assertion appears in the abstract, introduction (line 41), and discussion (line 298). The only evidence cited is a "cursory search of open source SAEs on Neuronpedia" showing "L0 less than 100 is very common" (referenced to Appendix A.13, stripped by parser). No quantitative analysis, systematic survey, or even a single number appears in the main text. The paper's core contribution does not depend on this claim — the core finding is that *if* L0 is set incorrectly, features become corrupted — but the overclaim weakens the paper's credibility. It should be removed from the abstract and either softened substantially or supported with proper evidence elsewhere.

2. **The LLM experiments are thin relative to the paper's scope.** Only two models (Gemma-2-2b, Llama-3.2-1b) and three layers total (Gemma layers 5 and 12, Llama layer 7) are evaluated. The c_dec metric is shown to align with sparse probing performance in these cases, but this is a small sample. While the toy model analysis is thorough, the LLM validation covers a narrow slice that limits confidence in the generality of the findings.

### Minor

3. **The toy model assumes perfectly orthogonal ground-truth features without discussing the implications of this assumption.** Section 3 states "All features are orthogonal," consistent with the idealized Linear Representation Hypothesis. However, the paper does not discuss what happens when features are only approximately orthogonal (as the LRH itself posits features are "nearly" orthogonal). If underlying features naturally have nonzero cosine similarity, the c_dec baseline itself would shift, and the distinction between "feature mixing" and "natural feature non-orthogonality" would become harder to draw. This is a known limitation that should be explicitly acknowledged and, ideally, tested with small deviations from orthogonality.

4. **The c_dec metric has practical utility limitations that are acknowledged but not addressed.** As the paper notes (Section 6), c_dec can remain "nearly flat for a wide range of L0" (e.g., Gemma-2-2b layer 5 in Figure 8). The paper provides no heuristic or automated rule for identifying the elbow, so the metric currently serves as a diagnostic rather than a practical optimization tool. The reference to Appendix A.11 (stripped) for "steps towards automatic optimization" does not help readers of the main text.

5. **The LLM probing results lack error bars and significance tests.** Figure 8 reports 3 seeds per L0 for probing F1 scores, but the main plots show no error bars or confidence intervals. It is unclear whether the observed differences between nearby L0 values are meaningful, particularly in flat regions of the c_dec curve. The c_dec plots do show shaded standard deviation, which is good.

6. **It is not stated explicitly whether decoder vectors are normalized before computing cosine similarity.** The c_dec formula (Eq. 4) computes |cos(·,·)|, but the paper does not clarify whether decoder columns are constrained to unit norm during training (as is standard in some SAE implementations) or whether cosine similarity is computed on raw decoder weights. This affects interpretation of the metric's baseline and should be stated.

### Trivial
None.

## Nice-to-Haves
- Testing c_dec on SAEs with non-orthogonal ground-truth features (e.g., pairwise cosine similarity up to 0.3) would strengthen real-world relevance.
- A simple heuristic for elbow detection (e.g., "choose smallest L0 where c_dec is within X% of its minimum") would increase the metric's practical value.
- Reporting a systematic comparison of L0 values across a small set of open-source SAEs from Neuronpedia would substantiate the claim about "most SAEs having too low L0."

## Removed Points

- **SAE width ablation (h=32768 fixed):** The harsh critic asked whether wider SAEs could compensate for low L0. This is scope creep — the paper is scoped to L0, not width. The paper's contribution is about L0's effect, not about architecture design.
- **"sparsity-reconstruction tradeoff is not a sound method" as separate weakness:** This is not a weakness of the paper but a central finding. It belongs in the strengths.
- **Related works / missing citations:** Cannot be evaluated without external sources.
- **Missing appendix content:** The parser stripped appendix sections; they exist in the original submission.

## Novel Insights

Beyond the paper's own contributions, the key novel observation that emerges from comparing the harsh critic and strength finder is that the paper's *strongest* evidence (toy models) and *weakest* evidence (the sweeping claim about "most SAEs") sit in tension. The strength of the toy model analysis is that it establishes the mechanism cleanly and rigorously. The weakness of the "most SAEs" claim is that it tries to extend this insight to the entire field without systematic evidence. This tension mirrors a broader pattern in the SAE critique literature: papers that identify fundamental limitations of SAEs often find it tempting to overgeneralize from clean toy demonstrations to sweeping field-wide conclusions. The paper would be more effective if it leaned into the *conditional* finding ("if L0 is wrong, features are wrong") as its main result, and treated the observation about existing SAEs as a speculation.

## Suggestions

1. **Remove or heavily qualify** the claim about "most commonly used SAEs" from the abstract. Replace with a statement about the *conditional* finding: "We show that if L0 is set incorrectly, SAEs produce corrupted features."
2. **Add a discussion** of the orthogonal features assumption and its implications in Section 3 or Section 6.
3. **Run c_dec + sparse probing on at least 2–3 more (layer, model) pairs** to strengthen confidence. Even a single additional layer per model would help.
4. **Add a simple elbow-detection rule** so the c_dec metric can be applied without manual inspection.
5. **Clarify decoder normalization** status in the experimental setup.

## Score and Decision

**Round 1 bracketing:** The paper is clearly stronger than the 4.67 ("Compute Optimal Inference" — weak real-model validation) and 5.25 ("Applying SAEs to Unlearn Knowledge") anchors, but weaker than the 7.00 anchors ("Canonical Units of Analysis," "Principled Evaluations") which have more comprehensive experiments and sharper novelty claims. The bracket is **[4.67, 7.00]** .

**Round 2 narrowing:** Compared to "Incidental Polysemanticity" (5.67, Reject), the paper under review has cleaner real-model validation and more practical relevance, placing it above. Compared to the 7.00 anchors, it has thinner LLM evaluation and an overclaiming issue, placing it below. The paper sits closest to the gap between the 5.67 and 7.00 anchors — clearly above the former, clearly below the latter.

**Calibration anchors used:**

- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/9ca9eHNrdH.md` (7.00, Round 1&2) — "Sparse Autoencoders Do Not Find Canonical Units of Analysis." Stronger paper with more comprehensive experiments (stitching, meta-SAEs, BatchTopK contribution). The paper under review has cleaner toy experiments but less thorough real-model analysis. Weaker.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/1Njl73JKjB.md` (7.00, Round 2) — "Towards Principled Evaluations of Sparse Autoencoders." Strong framework with supervised dictionaries. The paper under review has a narrower focus. Weaker.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/OeHSkJ58TG.md` (5.67, Round 2) — "Incidental Polysemanticity." Toy model theory with limited real-model connection. The paper under review has better real-model validation. Stronger.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/ghH6YYDs15.md` (4.67, Round 1&2) — "Compute Optimal Inference..." Theoretical result but very weak experiments. The paper under review is substantially stronger.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/ZtvRqm6oBu.md` (5.25, Round 2) — "Applying SAEs to Unlearn Knowledge." Competent experiments on a narrower application. The paper under review has cleaner mechanistic analysis and broader relevance. Stronger.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/F76bwRSLeK.md` (4.80, Round 1) — The original Cunningham et al. SAE paper. Different genre (foundational methods). Not directly comparable.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/tcsZt9ZNKD.md` (8.20, Round 1) — "Scaling and evaluating sparse autoencoders." Major-scale paper from OpenAI. The paper under review is not at this level of scale or contribution.

The paper makes a genuine, well-argued contribution with clean toy experiments and a useful diagnostic metric. The overclaim about "most commonly used SAEs" and the thin LLM evaluation prevent it from reaching the 7.0 level of the stronger accept anchors. It clearly exceeds the 4.67–5.67 reject-range papers.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>