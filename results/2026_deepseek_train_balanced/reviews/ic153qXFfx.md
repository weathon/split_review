## Summary

Proposes MMMT-IF, a benchmark for multimodal multi-turn instruction following built on top of the MMDU dataset by inserting cross-turn formatting constraints across 6 categories. Introduces programmatic metrics (PIF, PIF-N-K) evaluated via code execution rather than LLM judges, with evaluations of Gemini 1.5 Pro, GPT-4o, and Claude 3.5 Sonnet showing degradation over turns and limited robustness.

## Strengths

- **PIF-to-human validation is concrete and empirically grounded.** The 0.60 correlation between the automatic PIF metric and human instruction-following ratings (per-model: 0.44, 0.68, 0.63) provides real evidence that the programmatic metric aligns with human judgment — a direct validation of the paper's core evaluation approach.

- **PIF-N-K reveals robustness failures invisible in average PIF.** Even Sonnet 3.5, with average PIF = 0.771, achieves PIF-4-4 (all 4 samples perfect) only 28% of the time, while Gemini and GPT-4o score just 11%. This is a genuine contribution over mean-only metrics and highlights a qualitatively different failure mode.

- **Stochastic-dominance analysis using empirical CDFs is more informative than mean-only reporting.** The distribution-level comparison is methodologically sound, even though the prose description has a direction error that needs correction.

- **Documentation of LLM-as-judge bias supports the motivation for objective metrics.** The observation that GPT-4o as a judge ranks GPT-4o's instruction following above Sonnet's (reversing the true ordering established by PIF) directly motivates the paper's emphasis on programmatic evaluation.

## Weaknesses

### Fatal
None.

### Major

1. **Confounded ablation undermines the retrieval-vs-following claim (Contribution 4).** The experiment adds all given instructions at the end of the input context *in addition to* their original positions (line 260: "In addition to having instructions throughout the input context, we add all given instructions at the end of the input model context"). This confounds position/recency with repetition — the model sees each instruction twice. The measured 22.3-point PIF improvement could partly reflect the benefit of repetition rather than easier retrieval. A clean test would compare (A) instructions only at original positions vs. (B) instructions only at the end *without duplication*. The paper's headline finding — that the bottleneck is retrieval, not following — rests on an experimental design that cannot separate these factors.

2. **No comparison to existing instruction-following benchmarks.** The paper cites IFEval and CFBench (line 25) as single-turn predecessors but never evaluates the same models on those benchmarks to contextualize MMMT-IF's difficulty or measure what new information it provides. For a benchmark paper, this is a significant omission: readers cannot assess whether MMMT-IF is genuinely harder or measuring a different dimension.

3. **Stochastic dominance direction is reversed in the prose (appears twice, lines 35 and 241).** The paper states "the empirical CDF for Sonnet 3.5 is stochastically dominated by the empirical CDF for Gemini 1.5 Pro" but then gives the inequality P(PIF\_Sonnet > x) ≥ P(PIF\_Gemini ≥ x) for all x — which is the definition of *Sonnet* dominating *Gemini*. The prose says the opposite of what the mathematics shows. While the rest of the paper's data consistently shows Sonnet > Gemini, this error appears in both the introduction and results sections with identical wording and undermines confidence in the analysis.

### Minor

4. **Correlation type between PIF and human ratings is unspecified** (Table corr\_pif\_human, lines 305–311). The paper does not state whether this is Pearson, Spearman, or another measure. Given that PIF scores are discrete {0, 0.5, 1} and human ratings are 1–10, Pearson assumptions are not met. The model-specific variation (0.44 for Gemini vs. 0.68 for GPT-4o) is reported but not discussed — this range suggests the metric aligns differently across models, which merits explanation.

5. **Evidence for LLM-as-judge bias is thin.** Table autorater\_comparison shows GPT-4o as judge rates GPT-4o's instruction following at 9.06 vs. Sonnet's 9.01 (Δ=0.05), and Gemini as judge rates Gemini at 7.61 vs. Sonnet's 7.81 (Δ=-0.20). These differences are small on a 10-point scale and not tested for significance. The claim in the abstract that "LLM based judges are biased towards answers from the same model" is not convincingly supported by these numbers alone.

6. **The weighted combination of PIF and LLM scores (20:1) is arbitrary and yields low alignment.** The composite score achieves only 16% correlation with human preference, which is substantially worse than the PIF-only correlation of 60%. The paper does not justify the weighting or discuss this degradation.

7. **Programmatic checker implementation details are not provided.** The benchmark's reliability depends on code-based checking of instructions (sentence boundary detection, case-sensitivity, handling of code blocks or lists), but no pseudocode or logic description is given. This hinders reproducibility.

### Trivial

- Temperature dependency of PIF-N-K (uniformly default=1 for all models) is not discussed.
- The paper lacks a dedicated limitations section acknowledging the formatting-constraint-only scope and the 27.5% chat filtering rate.

## Nice-to-Haves

- A properly controlled ablation comparing instructions at original positions only vs. instructions at end only (no duplication), to cleanly separate retrieval from following.
- Evaluation of the same models on IFEval or CFBench (or citation of published results for the same model versions) to contextualize MMMT-IF's difficulty.
- Specification of correlation type — Spearman would be more appropriate given the discrete nature of PIF scores — and per-turn correlations.
- Adding a limitations section.

## Removed Points

Points from the input reviews that were filtered out as speculative, factually incorrect, scope-creep, or already addressed:

- *"The benchmark covers an extremely narrow slice of instruction following"* — The paper is scoped to programmatically verifiable formatting constraints; demanding content/reasoning/retrieval constraints that cannot be automatically checked is scope creep. Weakened from a structural criticism to a scope limitation in the trivia.
- *"Human vs. model PIF comparison is misleading"* — Removed. The paper acknowledges raters had the instruction list separately (line 314), and the specific comparison it makes (human 0.94 vs. Sonnet 0.97 with instructions at end) controls for retrieval burden on both sides.
- *"28% filtering may introduce selection bias"* — Speculative; no evidence of actual bias provided. Removed.
- *"Null hypothesis oddly phrased"* — H0: P(PIF\_Gemini > PIF\_Sonnet) ≥ 0.5 is a standard stochastic superiority formulation for the Wilcoxon signed-rank test. Not a weakness.
- *"Missing dataset construction details (probability threshold)"* — The mechanism is adequately described at lines 29–30 and 96. Removed as the critic's reading was incomplete.
- *Strength: "Clean ablation isolating retrieval from following"* — Dropped because it directly conflicts with Major weakness #1 (the ablation is confounded, so it cannot be described as "clean" or "isolating").
- *Strength: "Stochastic-dominance analysis"* — Retained but qualified; the methodology is valid but the prose error undermines the presentation.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Fix the ablation**: compare instructions at original positions only vs. instructions at end only (no duplication). If the improvement persists, the retrieval claim is strongly supported.
2. **Correct the stochastic dominance prose** at lines 35 and 241 to match the supplied inequality (Sonnet dominates, not Gemini).
3. **Specify correlation type** (recommend Spearman) and report per-turn correlations.
4. **Add benchmark comparisons** — evaluate models on IFEval/CFBench or cite published results for the same model versions.
5. **Add a limitations section** covering the formatting-constraint scope, the ablation confound, and the missing benchmark comparison.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>