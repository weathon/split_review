## Summary

This paper investigates how the temperature parameter in InfoNCE contrastive loss affects text embeddings, showing that higher temperatures produce lower intrinsic dimensionality (measured via PCA variance explained), which in turn enables substantially better quality retention under post-training compression (truncation and binarization). The paper proposes temperature aggregation methods (TempAgg, TempAggMRL, TempSpecMRL) that achieve a Pareto improvement: matching the retrieval performance of the best single-temperature model while maintaining ~99% quality retention under 32× compression via binarization with re-ranking.

## Strengths

- **Clear demonstration of the temperature → intrinsic dimensionality relationship (Figure 4):** Using PCA-based analysis, the paper shows that the number of principal components needed to explain 95% of the variance decreases from ~896 (random baseline) to much lower values as τ increases. This is a concrete measurement, not just a qualitative claim, and goes beyond prior work that only studied temperature effects in vision.
- **Quantifies a strong, consistent correlation between larger τ and higher quality retention under compression (Figures 5, 6):** Retention after truncation to 256 dimensions rises from ~93% at τ=0.04 to ~99% at τ=0.4. The same trend holds for binarization, and the paper verifies this across two different compression methods (random feature selection and binarization), ruling out method-specific artifacts.
- **Temperature aggregation methods (TempAgg, TempAggMRL, TempSpecMRL) achieve a concrete Pareto improvement (Table 2):** TempSpecMRL matches the retrieval NDCG@10 of the best single-τ model (τ=0.04) while achieving ~99% quality retention under 32× compression via binarization with re-ranking. This directly addresses the core trade-off identified in the paper.
- **Ablates the interplay between MRL training and temperature effects (Table 1):** MRL training further reduces intrinsic dimensionality across all τ values and improves compression retention, especially at small τ (binarization retention from 95.3% to 96.1% for τ=0.04). This strengthens the causal story by showing additive effects between a known intrinsic-dimensionality reducer and temperature.
- **Temperature specialization (TempSpecMRL) exploits a directional dependency in MRL training:** Using small τ at lower dimensions (256:0.03) for strong retrieval at truncated sizes and larger τ at full dimension (1024:0.1) for low intrinsic dimensionality is a novel architectural insight that leverages the fact that loss at larger dimensions affects lower dimensions but not vice versa.

## Weaknesses

### Major

- **Single architecture evaluation limits generalizability of the central claim.** All experiments use the CodeSage architecture (356M params, 1024 dims). The paper claims a general property of contrastive learning (temperature → intrinsic dimensionality → compression quality), but this is never validated on a different architecture, embedding dimension, or training data configuration. For an empirical study whose central thesis is about a general property of contrastive training, the single-point evaluation is a significant evidential gap. (Architecture and setup described in Section 3.1, lines 83-85.)
- **No empirical comparison against the most natural prior-art baseline: temperature schedules.** Kukleva et al. (2023) proposed varying the temperature during training (a schedule from 0.07 to 1.0) to address the instance-vs-group-wise discrimination trade-off. The paper states TempAgg is "simpler than temperature schedules" (line 171) but never directly compares against this existing approach. Without this comparison, it is unclear whether the aggregation methods offer any advantage over a known proposed solution to a closely related problem. This substantially weakens the claimed contribution of the methodological component.

### Minor

- **No variance or statistical significance reporting.** Every result appears to come from a single training run. Several comparisons involve small numerical differences (e.g., binarization retention improving from 95.3% to 96.1% with MRL at τ=0.04). Without run-to-run variance or confidence intervals, the reader cannot assess whether these differences are meaningful or within training noise. While the main monotonic trends are clear (and unlikely to be overturned by variance), the specific comparative claims lack statistical grounding.
- **Missing conclusion/discussion section.** The paper ends abruptly at Section 6 (Future Work). While the abstract and the summary in Section 4 (lines 157-161) partially compensate, a proper conclusion section that synthesizes findings, acknowledges limitations (e.g., single architecture), and discusses broader implications would significantly improve the paper's completeness as an empirical study.
- **Clustering improvements for aggregation methods not quantified in text.** The text states that TempAgg and TempAggMRL "improve on clustering by a large margin" (line 203) but does not report the actual numerical clustering scores. Table 2 includes a clustering column, but the key values should be called out explicitly in the text to support this claim.
- **TempSpecMRL temperature choices may risk overfitting to validation sets.** The specific temperature assignments (256:0.03, 512:0.06, 1024:0.1) appear to be selected based on the earlier experimental sweep. The paper does not clarify whether these values were chosen a priori or after observing MTEB validation results.

### Trivial

None beyond the minor issues noted above.

## Nice-to-Haves

- Validating the core findings on at least one additional architecture (e.g., a BERT- or T5-based encoder with a different embedding dimension) would substantially strengthen the paper's central claim about general properties of contrastive learning.
- Adding a temperature-schedule baseline (following Kukleva et al., 2023) would demonstrate whether TempAgg offers advantages beyond what schedules already provide.
- Reporting confidence intervals from multiple seeds (at minimum 2-3) for key comparisons would improve statistical grounding.

## Removed Points

These points were flagged in reviewer inputs but are removed or substantially weakened after cross-checking against the paper:

- **Harsh Critic #4 (re-ranking ambiguity):** The paper states "binarizing both with re-ranking (bin re-rnk) and without" in the Table 2 caption (line 187), which clearly indicates re-ranking was applied uniformly to all compared models. The text's phrasing "In this last set of experiments, we also add re-ranking" (line 201) is mildly ambiguous in isolation, but the table caption resolves it. This is not a genuine weakness.
- **Criticism that the monotonicity claim at line 96 is only supported by figures:** Figures are standard forms of evidence in ML papers; numerical values can be read from them. This is not a weakness.
- **Criticism of the "no instructions" decision:** The paper explicitly justifies this design choice (line 89) as avoiding MTEB overfitting and follows prior work (Neelakantan et al., 2022). This is a legitimate methodological choice, not a weakness.
- **Criticism that the paper says "It is difficult to assess where our results fit" (line 162):** This is honest contextualization of results relative to a heterogeneous body of prior work, not a weakness.

## Novel Insights

Beyond the paper's own contributions, the most notable insight from the reviews is that the temperature specialization approach (TempSpecMRL) exploits a directional dependency in MRL training — the loss at larger dimensions affects lower dimensions but not vice versa — to simultaneously optimize for retrieval quality (via small τ at truncated sizes) and compression friendliness (via larger τ at full dimension). This asymmetry is a clever architectural insight that could generalize to other multi-resolution training setups beyond temperature control.

## Suggestions

1. **Compare TempAgg/TempSpecMRL against a temperature-schedule baseline** (Kukleva et al., 2023) using the same architecture and data. This is essential to substantiate the claimed advantage of aggregation over schedules.
2. **Validate on at least one additional architecture** (e.g., a BERT-based encoder with a different embedding dimension) to demonstrate that the temperature → intrinsic dimensionality → compression relationship is a general property, not an artifact of the CodeSage model.
3. **Report numerical clustering scores for TempAgg and TempAggMRL** in the text (not only in the table image) to substantiate the claim of large clustering improvements.
4. **Add a brief conclusion/discussion section** that synthesizes findings and explicitly acknowledges limitations (single architecture, lack of variance reporting).
5. **Clarify whether TempSpecMRL temperature values were chosen a priori or based on validation** to help readers calibrate confidence in those results.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>