## Summary

This paper proposes PlanSearch, an algorithm for code generation that searches over natural-language plans rather than directly over code. PlanSearch generates observations about a problem, combinatorially combines them into plan sketches, then translates plans through pseudocode into final code. The authors demonstrate that searching in idea space produces more diverse outputs than standard repeated sampling, achieving 77.0% pass@200 on LiveCodeBench with Claude 3.5 Sonnet versus 60.6% for repeated sampling. The paper also introduces a diversity metric and shows it correlates with search gains across models and methods.

## Strengths

- **Backtranslation experiment provides causal evidence for the core hypothesis.** Section 3.2 (Figure 3a) shows that supplying a model with a correct natural-language sketch (backtranslated from a passing solution) significantly improves accuracy — even a sketch as short as 10 tokens helps. This cleanly isolates the bottleneck: if a correct sketch is available, the model can reliably produce correct code.

- **Conditioning-on-idea experiment demonstrates that sketch quality explains most of the variance in solve rates.** Section 3.3 (Figure 3b) shows that when a model generates its own sketch before implementing, the per-sketch solve rates polarize toward 0% or 100%, versus a broad distribution for unconditional sampling. This is a clean empirical argument that idea correctness, rather than implementation details, is the dominant factor — directly motivating searching over plans.

- **PlanSearch outperforms baselines across all evaluated models and benchmarks.** Table 1 shows consistent improvements over repeated sampling and IdeaSearch for GPT-4o-mini, GPT-4o, DeepSeek-Coder-V2, and Claude 3.5 Sonnet on LiveCodeBench, HumanEval+, and MBPP+. PlanSearch on GPT-4o-mini surpasses the pass@1 of larger models (e.g., Claude 3.5 Sonnet at 41.4%) with only ~4 attempts, demonstrating practical value.

- **The combinatorial observation-subset generation (Section 4.3) is a principled mechanism for exhaustive idea-space exploration.** Generating all subsets of observations (up to size 2) at two depths provides a systematic way to force diverse combinations of ideas, clearly distinct from prior work searching over tokens, lines, or entire programs.

## Weaknesses

### Major

- **The headline comparison (pass@200) compares methods at unequal inference budgets, and the compute-normalized results are referenced but not concretely reported.** PlanSearch generates observations, combinatorial subsets, second-order observations, plans, revised plans, pseudocode, and code — spending substantially more inference compute per code output than repeated sampling, which generates code directly. The paper acknowledges this (PlanSearch "usually ranging on the order of 300 to 400" codes vs. exactly 200) and references a compute-normalized figure (Fig.~\ref{fig:compute_normalized_plansearch}), stating findings are "highly similar." However, no concrete numbers from that figure appear in the text, and the 77.0% vs. 60.6% comparison is presented in the abstract and introduction without qualification about the compute gap. This is the central evidential issue: the reader cannot assess from the written text alone whether PlanSearch's advantage is due to better search or simply more search. Reporting the compute-normalized numbers (tokens or FLOPs) prominently is essential.

### Minor

- **The pass@k estimator's independence assumption is acknowledged as violated but not analyzed.** The paper's footnote honestly states that PlanSearch generations "may not be independent" because many outputs share the same observations and plans. When samples are positively correlated, the pass@k estimator can be biased. The paper provides no analysis, correction, or sensitivity study. While this alone may not invalidate the results, it is a meaningful evidential gap that should be addressed — for example via bootstrap confidence intervals or by sampling a fixed number of independent paths through the tree.

- **The diversity–performance correlation claim lacks quantitative evidence.** The paper asserts that diversity "accounts for much of the variance" in relative improvement and that "we can accurately predict performance gains" (abstract), but no correlation coefficient, R², or other quantitative measure is reported. The claim rests entirely on visual inspection of a scatter plot (Figure 6). The diversity metric itself (Equation 1) is reasonable, but the central claim about its predictive power needs numerical backing.

- **The conditioning-on-idea experiment's claim "most of the variance is captured by whether the sketch is correct" (line 50) is stated more strongly than the evidence supports.** The experiment uses only 75 LiveCodeBench problems and 375 sketches from a single model (GPT-4o-mini), with problems filtered to remove those solved 0% or 100% of the time. The polarization shown is suggestive, but the paper does not report the original problem count before filtering, nor does it quantify "most of the variance" — no variance decomposition or explained-variance metric is provided.

- **The number of LiveCodeBench problems used in the main evaluation is not stated.** The paper says it uses problems "between May 2024 and September 2024" but does not report how many problems this yields. For a benchmark where the pool size is typically ~50–80 problems, knowing the exact count is important for assessing the reliability of the 77.0% result.

- **Backtranslation experiment lacks error bars or significance testing.** The observation that "even only after 10 tokens of backtranslated solution significantly helps" (Section 3.2) is interesting but not accompanied by any variance estimate. Given the small number of problems used for this experiment, it is unclear whether the observed improvements are statistically robust.

### Trivial

- A few LaTeX artifacts remain (e.g., `\todolater{fix}` on line 162), suggesting incomplete cleanup before submission.

## Nice-to-Haves

- **Ablation study of PlanSearch components.** The method has several design choices (subset size S=2, tree depth L=2, generating a revised plan by "supposing the idea is wrong"). An ablation isolating which components drive the gains would deepen the analysis without broadening scope.
- **Error bars / confidence intervals for pass@k.** While point estimates are the norm in code generation papers, given the moderate size of the LiveCodeBench pool, confidence intervals would help assess whether smaller differences (e.g., o1-mini: 90.8→91.3) are meaningful.

## Removed Points

Points removed from the harsh critic that were not included in the main review (treat with caution):

- **"The backtranslation experiment is somewhat tautological"** — Removed. The experiment is designed to test whether a correct sketch is sufficient for correct code, which is a meaningful causal test, not a tautology. The critic misreads the purpose of the experiment.
- **"The o1-mini result puts an upper bound on the method's added value"** — Removed. This is an observation about the method's scope, not a weakness. The paper already notes that "since o1-mini already uses inference-time compute, the gap is much smaller." This is honestly discussed, not a flaw.
- **"Public test filtering claim about tenfold reduction is uncontrolled"** — Removed. The comparison (pass@20 with filtering vs. pass@200 without) is clearly described and the filtering is a standard technique. The paper does not claim this comparison is controlled; it reports an empirical observation.
- **"The diversity judge using GPT-4o-mini creates circularity"** — Partially removed. The paper uses GPT-4o-mini as a judge across all methods, not just to evaluate itself. The critic overstates this as a circularity concern; it is a reasonable choice of judge.
- **"No error bars or variance estimates"** — Moved to Nice-to-Have, as point-estimate reporting is standard practice in this field.

## Novel Insights

None beyond the paper's own contributions. The two key insights — (1) that sketch correctness polarizes solve rates (Section 3.3) and (2) that combinatorial observation-subset generation in natural language space produces more diverse code outputs — are well-articulated by the authors themselves.

## Suggestions

1. **Report the compute-normalized numbers in the text** — either as a second column in Table 1 or as explicit numbers (e.g., "at equal inference cost of X tokens, PlanSearch achieves Y% vs. Z% for repeated sampling"). This is the single most impactful fix for the paper's credibility.
2. **Quantify the diversity-performance correlation** — report the Pearson/Spearman correlation coefficient and R² for the relationship shown in Figure 6.
3. **Address the independence violation for pass@k** — either by providing bootstrap CIs showing bias is small, or by sampling a fixed number of independent search paths per problem.
4. **State the total LiveCodeBench problem count** explicitly alongside the date range.
5. **Clean up remaining LaTeX artifacts** (`\todolater{fix}`).

## Score and Decision

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>