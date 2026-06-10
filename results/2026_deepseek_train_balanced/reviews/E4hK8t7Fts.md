## Summary

This paper investigates three fine-tuning strategies on the MATH dataset using PaLM 2 models: (1) supervised step-by-step solution fine-tuning (SSFT), (2) solution-cluster re-ranking (SCR), which re-ranks only the top-K majority-voting clusters rather than all candidate solutions, and (3) multi-task sequential fine-tuning, where a model is fine-tuned as generator → evaluator → generator in sequence. The main empirical contributions are a cluster-based re-ranking strategy that improves both accuracy and efficiency, a comprehensive comparison of six re-ranking strategies with cost analysis, and an analysis of cross-model generalization for solution evaluators.

## Strengths

- **Solution-cluster re-ranking (RR.Top-8) simultaneously improves accuracy and efficiency over full re-ranking.** The paper shows that re-ranking only the top-8 majority-voting clusters (rather than all 64 candidates) achieves better accuracy while requiring fewer evaluator calls (Table 2, Tab:rerank). PaLM 2-L with margin loss reaches 58.8% (RR.Top-8) vs. 57.0% (RR.All), establishing a practical and well-supported improvement.

- **Controlled comparison isolating solution-style effects on fine-tuning vs. few-shot.** The paper demonstrates that PRM800K (fine-grained, GPT-4-generated) solutions substantially outperform MATH (abstract, human-written) solutions when used for fine-tuning (Table 1: Maj1@64 54.2% vs. 49.2% for PaLM 2-L), but that few-shot performance is largely invariant to the same style difference (Table 4: 47.2% vs. 47.6%). This rules out a trivial prompt-side explanation and cleanly isolates the effect to the fine-tuning process.

- **Comprehensive head-to-head comparison of six re-ranking strategies with cost analysis.** Table 6 (Tab:rerank-compare) reports all six strategies (RR.All, RR.MajK, W.RR, W.RR.MajK, Maj1, Maj1.TopN) with optimistic hyper-parameter configurations, and Figure 1 adds computational cost. The best variant (W.RR.MajK, 61.2%) is identified transparently rather than cherry-picked, and the cost-efficiency trade-offs are quantified.

- **Cross-model generalization of the solution evaluator.** Table 5 (Tab:rerank-analysis) shows the PaLM 2-L evaluator re-ranks solutions from a different generator (PaLM 2-S*) at 46.4% RR.Top-8, confirming the evaluator is not simply overfitting to its own generator's output distribution. Conversely, the PaLM 2-S* evaluator fails to improve PaLM 2-L solutions, providing a clean scaling result: solution evaluation requires sufficiently large models.

## Weaknesses

### Major

- **The non-standard test split undermines comparability of absolute accuracy numbers.** The paper uses only 500 examples from the MATH test set for evaluation (line 217: "5K original test examples are used for training and validation, and the remaining 500 test examples are used for model evaluation"). The abstract claims "approximately 58.8% accuracy on the MATH dataset" without qualification. Since every published result a reader would compare against (GPT-4: 42.5%, PaLM 2 few-shot: 33.4%) is reported on the full 5,000-example test, the paper's absolute numbers are incommensurable with prior work. The internal comparisons between methods are valid, but the paper does not prominently flag this deviation from standard practice.

- **No variance estimates for any reported result.** All accuracy numbers in every table are point estimates with no standard deviations, confidence intervals, or indication of the number of runs/seeds. On a 500-example test set, the binomial standard error for values around 50–58% is approximately ±2.2 percentage points. Several claimed improvements are in the 0.6–2.0 percentage point range (e.g., Table 5: 36.2% vs. 35.6%; Table 4: 57.0% vs. 56.8%), making it impossible to assess whether these reflect real effects or sampling noise. This directly affects the reliability of comparative conclusions drawn at this granularity.

- **The multi-task sequential fine-tuning result has an uncontrolled confound.** The sequential method (Section 3.3) proceeds as: (1) fine-tune as generator (SSFT), (2) fine-tune as evaluator (SCR), (3) fine-tune as generator again. The baseline is SSFT only. Step (3) adds *additional* training on the generation objective that the baseline never receives. The improvement could simply come from training the generator for more steps/epochs, not from the intermediate evaluation step. The paper does not run the obvious control: SSFT → more SSFT (continued generator training for the same number of additional steps). Without this control, the core claim of Section 5 — that "the training objective of the solution evaluation task can provide useful supervision signals to the solution generation model" — is not adequately supported.

### Minor

- **The improvements from multi-task sequential fine-tuning are modest and inconsistent.** Even taken at face value, the sequential method's improvements over the SSFT baseline are +2.0 points (margin loss) and +0.6 points (cross-entropy loss) on Pass@1, and +2.0 and +1.4 points on Maj1@64. Pass@64 actually decreases slightly (Table 5). The paper frames this as a clear success, but the effect sizes are small and inconsistent across metrics.

- **The "quality and style" attribution for solution data sources is undersupported.** Section 5.1 shows PRM800K (GPT-4 generated) solutions outperform MATH (human-written) solutions for fine-tuning. The paper attributes this to the PRM800K solutions being "more fine-grained and detailed." However, the two sets differ in source model, correctness coverage, vocabulary, and reasoning patterns — confounds the paper does not control for. The observation that the effect is specific to fine-tuning (vs. few-shot) is valuable, but the causal mechanism is not identified.

- **Missing details on how the 500-example test subset was selected.** The paper does not describe whether the 500-example subset was randomly sampled, stratified by difficulty, or selected by some other procedure. This matters for reproducibility and for calibrating how representative the results are.

- **The selection of the 10 training examples for margin loss is underspecified.** Line 285 states that "10 training examples" are constructed per problem from the 64 candidates for the margin loss, but does not explain how these 10 are selected or whether pairs are balanced. This affects reproducibility.

### Trivial

None.

## Nice-to-Haves

- Add the obvious control experiment for the sequential method: continue training the SSFT baseline on the generation objective for the same number of additional steps as the sequential method's third phase, and compare. This would cleanly isolate whether the evaluation objective contributes anything beyond additional training.
- Add variance information (multiple seeds or bootstrapped confidence intervals) to the main result tables.
- Explicitly state in the abstract and conclusion that the 58.8% figure is on a 500-example subset of the MATH test set, not the full 5,000-example test.
- Show that the re-ranking improvements hold across different values of N (number of candidate solutions), not just N=64.

## Removed Points

*The following points were flagged by reviewers but are removed from the main review after verification:*

- *Criticism about the PRM800K test set (512 examples) being listed but "never used for evaluation."* — The paper clearly uses PRM800K only for training solutions; including the full dataset statistics is informative and standard practice. Not a weakness.
- *Criticism that "models are very close to their fine-tuning ceiling already, or there is substantial overlap/leakage between training and test data."* — The paper uses a non-standard split (test examples used for training), which is already addressed as a MAJOR weakness about comparability. The speculation about "leakage" goes beyond what the evidence supports.
- *Strength about "multi-task sequential fine-tuning demonstrably improves generation via evaluation" from Strength Finder.* — This conflicts with the verified MAJOR weakness about the uncontrolled confound. The improvement is observed but the attribution to the evaluation objective is not adequately supported. Moved here because the strength is not justified given the verified weakness.
- *Complaints about missing related work.* — I cannot verify the existence of external works not cited.
- *Formatting/style nitpicks.* — These are parser artifacts, not author errors.
- *Reproducibility nitpicks about undisclosed hyperparameters in the standard sense.* — The paper reports the key hyperparameters used.

## Novel Insights

The most insightful cross-review observation is that the paper's strongest contribution (cluster-based re-ranking) is well-supported empirically and stands independently of the weaker sequential method, yet the paper packages both with equal emphasis. The cluster re-ranking work is novel, practical, and properly controlled — it genuinely advances the state of practice for combining majority voting with verifier-based re-ranking. The sequential method, while interesting, is experimentally under-supported due to the confounding of additional training steps, and its effect sizes are small enough that variance information is necessary to assess reliability. Separating these two contributions in the paper's framing would give appropriate weight to the stronger result.

## Suggestions

1. Add the control experiment for the sequential method (SSFT → more SSFT) to isolate the effect of the evaluation objective.
2. Report confidence intervals or bootstrap estimates for all main tables.
3. Qualify the headline "58.8% on the MATH dataset" by explicitly noting the 500-example subset.
4. Describe how the 500-example test subset was selected and how the 10 margin-loss training examples per problem were chosen.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>