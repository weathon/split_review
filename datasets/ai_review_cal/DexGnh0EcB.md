- Decision: Reject
- Avg Score: 4.20
- Scores: 3, 6, 6, 3, 3
Now I have all the information I need. Let me synthesize the final consolidated review.

## Summary

MathEval is a benchmark resource paper that assembles 22 math datasets (English and Chinese), defines a prompt adaptation framework tailored to different model types and dataset formats, and uses an LLM-based (GPT-4) answer extraction and comparison pipeline validated against human annotations (Fleiss' Kappa 0.8871). It evaluates 52 models across these datasets and releases a fine-tuned DeepSeek-7B answer comparison model as an open alternative. The core contribution is a unified, human-validated evaluation infrastructure for mathematical reasoning in LLMs.

## Strengths

- **Human-validated LLM-based evaluation pipeline.** The paper develops a two-stage GPT-4 answer extraction and comparison method and validates it via large-scale human annotation (Fleiss' Kappa 0.8871). The absolute difference between GPT-4 judgments and human evaluations is 0–0.1 across multiple models (Section 3.2, Figure 5). This provides a principled alternative to fragile rule-based extraction, addressing the "inconsistency" problem the paper identifies. The fine-tuned DeepSeek-7B comparison model offers a reasonable open alternative for researchers without GPT-4 access.

- **Extensive dataset coverage with new additions.** MathEval integrates 22 datasets spanning English and Chinese, arithmetic and math word problems, and primary through high school levels. It includes five datasets not previously used in other benchmarks (Arith3K, GAOKAO-2023, GAOKAO-2024, TAL-SCQ5K-EN, TAL-SCQ5K-CN), addressing the "incomprehensiveness" concern in prior evaluations (Abstract, Section 2.1, Figure 2).

- **Large-scale evaluation across diverse models.** The benchmark evaluates 52 models (open-source, closed-source, and math-domain fine-tuned) under multiple prompt settings, providing a broad empirical picture. The analysis of open-source vs. closed-source capability gaps and the relationship between parameter size and math performance yields descriptive but useful observations (Section 3.3–3.4).

## Weaknesses

### Fatal
None.

### Major

- **Unsubstantiated contamination detection claim.** The abstract states that MathEval "introduces a method to identify potential data contamination within pre-training datasets" and describes a hypothesis about correlated-dataset improvements signaling contamination. The contributions list claims "a strategy of using a dynamically updated dataset" for this purpose. However, the paper never implements, tests, or evaluates any contamination detection method — no experiment applies the stated hypothesis, no analysis flags suspected contamination, and no validation shows the Gaokao datasets are immune to contamination. The only concrete action is including Gaokao-2023/2024 as evaluation datasets, which is standard practice for freshness, not a detection method. This is a central claim in the abstract and contributions that the paper does not deliver on. The authors should either remove this claim entirely or present an actual experiment.

### Minor

- **Dataset count inconsistency.** The abstract says "19 datasets" while the introduction, Figure 2, and Section 2.1 consistently say "22 datasets." This appears to be a copy-editing error (the abstract was likely written when the collection was smaller and not updated), but it undermines reader confidence in the paper's precision.

- **"First comprehensive benchmark" overclaim.** The paper claims to be "the first comprehensive benchmark specifically designed to evaluate the mathematical capabilities of LLMs holistically" (Section 1, Section 5). Lila (Mishra et al., 2023) aggregates multiple math datasets with task instructions, and evaluation suites like OpenCompass already cover many of the same datasets. While MathEval offers unique features (the LLM-based evaluation pipeline and prompt adaptation framework), the novelty lies in the evaluation methodology rather than the dataset collection itself. The "first" claim should be scoped more carefully.

- **Unweighted average as the primary metric without discussion.** The paper computes the arithmetic mean accuracy across 22 datasets of widely varying sizes (Section 3.3). Equal weighting gives small datasets influence disproportionate to their sample count. The paper does not discuss this choice, compare with sample-weighted averages, or report variance/confidence intervals. Adding a per-dataset breakdown or weighted metric would strengthen the analysis.

- **No statistical rigor for comparative claims.** The paper states that Claude-3.5-Sonnet "surpasses GPT-4 by a significant margin" (Section 3.3) and that the "dataset-level higher" setting "contributes to the robustness and fairness of the evaluation" (Section 3.4), but neither claim is accompanied by any measure of variance, statistical test, or error bar. For a benchmark paper that makes comparative claims, this is a notable omission.

- **Limited validation of prompt adaptation choices.** The prompt template system is described in detail (Section 2.2), but the paper provides no ablation or validation showing that the tailored prompts are fair or systematically beneficial over simpler baselines. For example, the paper acknowledges that base models are "not proficient in zero-shot scenarios" yet evaluates them under zero-shot anyway (relying on a post-hoc "dataset-level higher" selection to compensate). Whether this selection procedure favors certain model families is not discussed.

### Trivial

- **The "dataset-level higher" setting for few-shot/zero-shot** (taking the better of two settings per dataset) is reported as improving "robustness and fairness" (Section 3.4), but this post-hoc selection mechanically inflates scores by construction and could differentially benefit models with inconsistent behavior across settings. The paper acknowledges this is its chosen approach but does not discuss the potential bias. This is a methodological detail that warrants a brief caveat.

## Nice-to-Haves

- Provide basic statistics (problem count, difficulty distribution, answer types) for the five newly introduced datasets (Arith3K, GAOKAO-2023/2024, TAL-SCQ5K-EN/CN) to help readers understand what new challenges they introduce.
- Compare MathEval's evaluation framework against existing pipelines (e.g., OpenCompass, HELM) on a common set of models to substantiate the claimed advantages.
- Report cost estimates for running the GPT-4-based pipeline to help researchers assess reproducibility constraints.

## Removed Points

- **Missing code/repository URLs.** The paper says results are "publicly accessible" and the comparison model "will also be made publicly available" but provides no URLs. While a public repository at submission time would strengthen a benchmark paper, the paper's statements about availability are future promises, not false claims about cited entities. The hard rules prohibit penalizing papers based on speculation about release status. I treat this as a minor point the authors should address, not a substantive weakness.
- **Criticism about missing appendix content and proofs.** The parser strips these sections; they exist in the original submission.
- **Various formatting/typography nitpicks about garbled text in the PDF extraction.** These are parser artifacts, not author errors.
- **Criticism that Lila is dismissed "too quickly."** The paper explicitly discusses Lila and explains the differentiation (Lila focuses on task instructions and Python solutions; MathEval focuses on evaluation methodology). The harsh critic's framing that this dismissal is inadequate is a subjective judgment, not a verifiable flaw.
- **Strength Finder's claim about "dynamically refreshed dataset for contamination detection" as a core strength.** This conflicts with the verified weakness that the contamination detection method is unsubstantiated. Per the rules, when a strength and weakness disagree, the weakness wins. The inclusion of Gaokao datasets is a positive aspect of coverage/freshness, but framing it as a "contamination detection" strength is not supportable.
- **Generic strengths from Strength Finder** that lack specific citation or concrete content (e.g., "this paper addressed an important problem").
- **Strength Finder's claim about "Prompt adaptation" as a core strength.** The template system is described but not validated, so calling it a strong contribution is premature.

## Novel Insights

The harsh critic's central observation — that the contamination detection claim is advertised as a contribution but never executed — is the most actionable finding. Beyond the paper's own contributions, the reviews surface a recurring pattern in benchmark papers: engineering contributions (unified pipeline, prompt templates, LLM-based evaluation) are genuine and useful, but are weakened when packaged with inflated novelty claims. The real value here is the validated GPT-4 evaluation pipeline combined with broad model coverage; the paper would be stronger if scoped around that rather than unfulfilled promises about contamination analysis.

## Suggestions

1. **Remove or implement the contamination detection claim.** If it cannot be supported with experiments, delete it from the abstract, contributions, and introduction. Re-scope the contribution as a unified evaluation pipeline with a dynamically updated dataset component, not a contamination detection method.
2. **Fix the dataset count inconsistency** (19 in abstract, 22 everywhere else).
3. **Soften the "first comprehensive benchmark" framing** — acknowledge Lila and OpenCompass explicitly and explain specifically what MathEval adds beyond them.
4. **Add per-dataset results** (a supplementary table of all 52 models × 22 datasets) so readers can compute their own aggregates and inspect variability. This would mitigate the unweighted-average concern.
5. **Provide a brief ablation** comparing the tailored prompt templates against a generic prompt on a subset of models, to validate that the template engineering effort is justified.
6. **Add error bars or statistical comparisons** for the key comparative claims (Claude vs. GPT-4, open-source vs. closed-source gaps).
