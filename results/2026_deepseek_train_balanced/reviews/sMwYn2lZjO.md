## Summary

This paper presents a benchmark study examining how MoE-specific structural properties (expert usage frequency, attention-vs-FFNN role, block depth, shared experts) can guide mixed-precision post-training quantization. Evaluated on Mixtral-8x7B and DeepSeek-MoE-16B-base across six tasks, the study finds that attention layers, early MoE blocks, and shared experts benefit from higher-precision allocation. Two lightweight methods are introduced—a column-wise outlier scorer for linear layers and a trained predictor for block importance—and are shown to outperform random allocation in several settings.

## Strengths

- **Systematic empirical study of MoE-specific quantization heuristics.** The paper investigates four structurally motivated heuristics (Q1–Q4) across two architecturally distinct MoE models and six tasks, providing the first dedicated benchmark for MoE quantization. The finding that attention layers consistently yield higher returns on additional bits than FFNN layers (Q2, Figure 2) is cleanly demonstrated, with 4–8 bit attention allocations improving performance by >5% over equivalent FFNN allocations. The shared-expert result (Q4, Figure 3) is similarly well-motivated and validated.

- **Linear weight outlier scorer shows meaningful gains on DeepSeek-MoE.** The proposed `outlier-score` metric (Eq. 5) identifies FFNN linear layers with large column-wise weight outliers and allocates them higher precision. On DeepSeek-MoE-16B-base (Table 5), it achieves 62.43% average accuracy versus random's 59.61% at the same 2.54-bit budget—a ~2.8% improvement. This is an architecture-aware metric that leverages the observation that MoE FFNN weights contain narrow-ranged values interspersed with outliers.

- **First-vs-last block comparison (Q3) yields a clear, actionable finding.** Allocating higher bits to the first k MoE blocks consistently outperforms allocating to the last k blocks on both models and at both k=4 and k=8 (Table 2). The margin is substantial (e.g., 58.16% vs 47.36% for Mixtral at k=8), making this a practically useful design rule.

## Weaknesses

### Fatal
None.

### Major

- **Statistical comparison is asymmetric and undermines significance claims.** Throughout Tables 5 and 6, random baselines are reported with means and standard deviations over 3 trials, but the proposed methods are reported as single numbers with no variance. This makes it impossible to assess whether the reported improvements are statistically significant. The problem is acute in several settings:
  - Table 5 (Mixtral): Ours (56.20) vs Random (55.25 ± 0.95) — the proposed method's reported average is within one standard deviation of the random baseline.
  - Table 6 (k=8): Predicted (60.58) vs Random (60.49 ± 0.56) — a 0.09% difference, far smaller than the random baseline's own standard deviation. The claim that the predictor "shows superiority" is unsupported for this setting.
  
  Without variance estimates or multiple trials for the proposed methods, the reader cannot distinguish genuine improvement from noise. This is a first-order methodological issue for a benchmark paper.

- **The activation quantization study (Section 5.1) does not support the conclusion drawn from it.** Table 4 reports weight+activation quantization where average accuracies are ~38–40% across all settings—far below the weight-only results (~50–65%) and near floor level for several tasks. The paper claims this "demonstrates that our conclusions regarding weight quantization are robust and can be reliably extended to various activation quantization scenarios" (line 232). This does not follow: when overall model quality is severely degraded, performance differences collapse and the absence of a meaningful gradient cannot be interpreted as evidence of robustness. The correct interpretation is that the aggressive 2/4-bit weight quantization dominates the degradation. The study either needs a design where weight and activation quantization are both moderate enough for their interaction to be measurable, or the robustness claim should be dropped.

- **Block importance predictor is only evaluated on DeepSeek, not Mixtral.** The predictor is introduced as a general method but is only tested on one model (Table 6). Its generality is unestablished, and the paper does not explain why Mixtral was excluded. Additionally, training a separate two-layer predictor per MoE block (potentially 32 predictors for DeepSeek) has a computational cost that is never quantified or discussed, making the "lightweight" claim unverifiable.

### Minor

- **Proposed methods are only compared against random allocation, not against simple non-random alternatives.** For the outlier scorer (Table 5), the baseline is "random 25% of linear layers." Stronger baselines are needed: e.g., selecting layers by total weight magnitude, column-wise variance, or maximum absolute weight. Similarly, for the block predictor (Table 6), the "First k" baseline is reasonable but comparing against "blocks with lowest actual cosine similarity" would directly test whether the trained predictor adds value over the proxy it is trained to predict. Without such comparisons, the reader cannot assess whether the proposed metrics are genuinely better than obvious heuristics.

- **The outlier scorer's advantage on Mixtral is weak.** On Mixtral (Table 5), the proposed method (56.20%) is within 1σ of random (55.25 ± 0.95%) and actually underperforms random on HellaSwag and MMLU. The claim of "consistently outperforming" (line 288) overstates the evidence for this model.

- **Deployment cost is never reported.** The paper recommends specific mixed-precision schemes but never translates bit-widths into actual memory footprints (GB). Average bit-width is an intermediate quantity—the practical utility of the findings would be clearer with memory savings reported.

### Trivial

- **Equation (2) contains a notational error.** The sum runs `\sum_{i=1}^{l}` where `l` is already used as the MoE block index; the intended upper bound is the number of experts per block.
- **Task count inconsistency (line 114).** The text says "six popular LLM tasks" but lists only five (WinoGrande, COPA, OBQA, HellaSwag, MMLU); PIQA is present in every table but omitted from this sentence.

## Nice-to-Haves
- Run multiple trials for proposed methods and report variance, enabling proper statistical comparison.
- Compare the outlier scorer against simple magnitude-based baselines (e.g., selecting layers with largest weight norms or column variances).
- For the block predictor, compare against using the actual cosine similarity directly (which the predictor approximates) to isolate the predictor's value-add.
- Report actual memory footprint (GB) for the recommended mixed-precision schemes.
- For the activation quantization study, use less aggressive weight quantization (e.g., 4-bit uniform) so that the effect of activation precision is measurable.

## Removed Points
- **QMoE citation gap (Harsh Critic, point 1).** The critic argues the "first benchmark" claim is undermined by missing engagement with QMoE. Per the review guidelines, I cannot mention missing related works without external sources to verify their relevance. Removed.
- **Q1 results overstated (Harsh Critic, Section-by-section notes).** The critic claims the paper "slightly overstates" the expert-usage results. The paper's characterization—"fairly good" and "corroborates its effectiveness"—is appropriate given the data. Table 1 shows the trend consistently favoring usage frequency over random across almost all configurations. Removed.
- **Block predictor contradictions with Q3 (Harsh Critic, Section-by-section notes).** The critic claims the finding that "last two blocks are also crucial" contradicts Q3 (first > last). This is a misreading: Q3 says first blocks are more important than last blocks on average, which is compatible with both ends being more important than the middle. Figure 6 confirms this pattern. Removed.
- **"Rigorous comparison" strength (Strength Finder, point 6).** The strength finder praises "rigorous comparison against random baselines with multiple trials and standard deviations" as a strength, but this conflicts with the verified weakness that the proposed methods themselves lack variance estimates. The asymmetry makes the comparison less rigorous, not more. Removed.
- **Activation quantization strength (Strength Finder, point 4).** The strength finder claims the activation quantization study "demonstrates that the MoE quantization principles generalize." This conflicts with the verified weakness that the results (38-40% accuracy) are too degraded to support this claim. Removed.

## Novel Insights
The harsh critic's most incisive observation is that the proposed methods' improvements are evaluated against the weakest possible baselines (random selection), while the variance asymmetry between baseline and method prevents meaningful significance testing. This joint problem—weak comparator + missing variance—means the reader cannot determine whether either the outlier scorer or the block predictor is genuinely better than any reasonable heuristic, let alone an optimal one. This is a structural flaw in how the paper's claimed contributions (item 3 in the introduction) are validated, distinct from the more defensible benchmarking contributions (items 1 and 2). Separately, the strength finder's observation that the shared-expert finding is "well-motivated and validated" correctly identifies a clean empirical result that strengthens the benchmarking contribution.

## Suggestions
1. Report all proposed method results with variance over multiple trials, or at a minimum run 3 trials as is done for the random baselines.
2. For the activation quantization study, either (a) redesign with less aggressive weight quantization so that the effect of activation precision is measurable, or (b) drop the robustness claim and present the results as a preliminary exploration.
3. Add simple non-random baselines for both proposed methods (magnitude-based layer selection for the outlier scorer; actual cosine similarity for the block predictor).
4. Reframe the "first benchmark" claim more carefully, or explicitly situate the work relative to prior MoE-specific quantization efforts.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>