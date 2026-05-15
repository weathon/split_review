Now I have all the information needed. Let me produce the consolidated review.

## Summary

This paper introduces MHPP (Mostly Hard Python Problems), a manually curated benchmark of 210 function-level Python programming problems designed to be more challenging and less contaminated than HumanEval and MBPP. The benchmark is structured around seven challenge types (Distraction, Redefinition, Shortcut, Commonsense, Cornercase, Complexity, Codesense) derived from error analysis of three LLMs on HumanEval. The authors evaluate 26 LLMs and show that MHPP reveals larger performance gaps between models than existing benchmarks, and that even top models (e.g., GPT-4o at 70.0% pass@1) struggle substantially.

## Strengths

- **Rigorous contamination control with concrete evidence**: The paper documents a 65.4% contamination rate in MBPP using a leakage detector, and implements a two-phase QA process (manual Internet search + automated detector) achieving 0% contamination in MHPP after excluding 6 problems. This is a measurable improvement over the existing benchmarks it targets.

- **Systematic error analysis grounding the benchmark design**: The seven challenge types are not arbitrary — they emerge from manual inspection of errors made by GPT-4, GPT-3.5, and DeepSeekCoder on HumanEval (Figure 2), and each category comes with explicit annotation guidelines (Section 3.1). This gives the benchmark a principled foundation rooted in observed model failures rather than intuition alone.

- **Demonstrated discriminative power**: MHPP reveals performance separations that are compressed on HumanEval. For example, GPT-4o achieves 70.0 pass@1 vs. DeepSeek-V2.5's 42.1 (Table 2), whereas on HumanEval many open-source models nearly match GPT-4o. The correlation analysis (Section 4.3) further shows that scaling benefits differ across models on MHPP vs. HumanEval, suggesting MHPP detects overfitting to existing benchmarks.

- **Comprehensive evaluation scale**: 26 LLMs spanning proprietary (GPT-4o, GPT-4-turbo, Claude 3.5 Sonnet) and open-source families (DeepSeek, Llama 3.1, Gemma, Mixtral, Phi-3) are evaluated, providing a broad picture of current capabilities in function-level code generation.

- **Concrete case studies linking failures to challenge categories**: Figure 8 demonstrates that GPT-4's failures on specific MHPP problems align with the intended challenge type (e.g., misunderstanding spatial orientation in the Commonsense category, index errors under multiple constraints in the Complex category), providing at least anecdotal validation of the taxonomy.

## Weaknesses

### Fatal
None.

### Major

- **The challenge categorization lacks rigorous validation.** The seven types are derived from error analysis of only three models on HumanEval, with no inter-annotator agreement reported for the manual coding. While the annotation guidelines (Section 3.1) are clearly specified, there is no evidence that (a) the categories are orthogonal (a model could fail on a problem for reasons unrelated to the intended challenge), (b) they are exhaustive, or (c) the categorization generalizes beyond the original three models. Only two case studies (Section 5.2) attempt to validate that failures stem from the intended challenge. With only 30 problems per category and no statistical evidence that failures within a category share a common cause, the per-category results (Figure 3) must be interpreted with caution. This weakens the paper's central analytical framework, not just a peripheral claim.

- **Per-category reliability is undermined by the small category size and mis-targeted confidence interval analysis.** With only 30 problems per category, the 95% confidence interval for a per-category pass rate near 50% is roughly ±18 percentage points. The paper's CI analysis (Section 5.1) measures sampling variance in *model outputs* (subsampling 50 of 100 generations across 10 trials) — it shows that pass@k estimates are stable across repeated evaluations, which is useful but addresses a different question. What is missing is an analysis of the *benchmark as a measuring instrument*: bootstrap confidence intervals over the 210 problems (or 30 per category) are not reported, so the reader cannot assess how stable the per-category model rankings or scores are with respect to the choice of problems. This limits the granular conclusions that can be drawn from Figure 3.

### Minor

- **High correlation with HumanEval raises questions about what MHPP adds beyond difficulty.** The correlation plot (Figure 7) shows a Pearson correlation of approximately r≈0.95 between HumanEval and MHPP pass@1 scores. The authors argue MHPP is "more challenging and representative," but a correlation this high means the two benchmarks largely rank models similarly. The paper does not report rank correlation (Kendall's τ or Spearman's ρ), which would clarify whether MHPP changes the ordering of models, nor does it provide a statistical test showing that models indistinguishable on HumanEval become separable on MHPP. The added value would be clearer if the paper quantified *which* models change rank and why.

- **No experimental comparison to other hard code generation benchmarks.** The paper cites APPS, CodeContests, and LeetCodeHard in Related Work but does not evaluate any model on them. While these benchmarks target competition-level (full program) generation rather than function-level generation — so the format mismatch is real — the paper's claim that MHPP reveals "previously undiscovered limitations" (Abstract) is hard to evaluate without knowing whether similar limitations are already surfaced by these existing hard benchmarks. This is a missed opportunity to position MHPP's contribution relative to the broader landscape.

### Trivial
None.

## Nice-to-Haves

- **Bootstrap confidence intervals over benchmark problems** (per-category and overall) would strengthen claims about benchmark reliability. This is not yet standard practice for all benchmark papers, so it is a nice-to-have rather than a required analysis.
- **Inter-annotator agreement** for the original error categorization on HumanEval would strengthen the foundation of the taxonomy.
- **A human expert baseline** on MHPP would calibrate what "hard" means relative to human performance.
- **A heatmap or matrix of all 26 models × 7 categories** (rather than just 4 models in Figure 3) would enable richer analysis of model-specific failure patterns.

## Removed Points

These points are flagged to be removed, treat them with caution:

1. *"The detection tool is not named in the text (only referenced as LiContan2023)."* — The tool is cited; providing a citation rather than a full description is standard practice in papers. Not a valid weakness.

2. *"The CI analysis is about sampling variance in model outputs — not about the variability of the benchmark as a measuring instrument."* — This is a valid observation, but the harsh critic overstated its severity. The paper's CI analysis correctly measures evaluation stability (whether repeated trials give consistent results). The missing analysis (bootstrap over problems) is a separate, additional analysis. I have elevated the core concern to the Major tier above but removed the framing that the existing analysis is "mis-targeted" since it is correctly executed for what it measures.

3. *"The paper overstates the problem: HumanEval has 164 problems and MBPP has ~974; contamination concerns are real, but many recent works already use filtered or updated versions."* — This is speculative about the state of "many recent works" without evidence. The paper's concrete contamination finding (65.4% in MBPP) is a real contribution.

4. *"The introduction positions MHPP as uniquely addressing '7 challenges' but does not argue why these particular challenges are important or missing from existing hard benchmarks."* — The introduction (lines 18-25) does argue this, connecting the challenges to specific observed model failures and to gaps in HumanEval/MBPP coverage. This is presented in abbreviated form but not absent.

5. *"Missing appendix, missing proofs in appendix"* — The parser strips appendix sections. These exist in the original submission.

6. *Reproducibility nitpicks about undisclosed hyperparameters* — The paper describes the evaluation setup (temperature 0.7, greedy search + sampling, unbiased pass@k). This is standard and sufficient.

## Novel Insights

Beyond the paper's own contributions, the reviews surface an interesting tension: the paper simultaneously claims (a) that MHPP is "largely correlated with HumanEval" (r≈0.95) and (b) that it reveals "previously undiscovered limitations." If the correlation is indeed that high, then either MHPP is measuring largely the same ability but at a harder level (in which case the "previously undiscovered" claim is about degree, not kind), or the correlation is being driven by a few outlier models while the middle of the pack changes rank — a distinction the paper does not explore. This tension suggests that future benchmark design should pre-specify whether the goal is to shift the difficulty distribution, change the latent ability being measured, or both, and then provide evidence tailored to each claim.

## Suggestions

1. **Validate the categorization more rigorously**: Either report inter-annotator agreement on the original HumanEval error coding, or run an experiment where models' per-category errors are shown to correlate with specific problem features (e.g., description length for Distraction, number of reasoning hops for Complex) rather than being confounded with general difficulty. Even a controlled ablation — where a model's failure on one category is shown to be mitigated by a targeted intervention — would strengthen the case.

2. **Add a comparison (even limited) to one hard benchmark**: Evaluate a subset of representative models (e.g., GPT-4o, GPT-3.5, an open-source model) on APPS or CodeContests, and compare per-model rankings, correlation, and discriminative power with MHPP. This would directly address whether MHPP provides information that existing hard benchmarks do not.

3. **Report bootstrap CIs over problems**: For overall and per-category pass rates, compute 95% bootstrap confidence intervals by resampling the 210 (or 30) problems with replacement. This would quantify benchmark-as-instrument reliability and allow readers to assess the stability of the per-category analysis in Figure 3.

4. **Temper the "previously undiscovered limitations" framing**: Given the high correlation with HumanEval, it is more accurate to say MHPP *amplifies* known limitations or measures the same ability at a harder difficulty level. The stronger claim requires evidence that is not currently in the paper.

5. **Replace Figure 3 (4 models) with a full 26-model × 7-category heatmap**: This would be a compact, information-dense visualization that supports the paper's claims about differential model weaknesses across challenge types.

## Score and Decision

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>