- Decision: Reject
- Avg Score: 4.75
- Scores: 3, 5, 6, 5
Now I have thoroughly verified every claim against the paper. Let me construct the final consolidated review.

---

## Summary

This paper introduces RULES (referred to as BIND in the abstract), a benchmark for programmatically evaluating whether LLMs follow natural-language rules provided in a prompt. The benchmark consists of 15 text scenarios inspired by computer security properties and children's games, each with a concise regex/string-matching evaluation program. Through extensive red-teaming, the authors identify 6 attack strategy categories and construct both a manual test suite (870 cases) and a systematic test suite (862 cases) covering those strategies. Evaluating 13 proprietary and open models, the paper finds that even the best model (GPT-4) passes only 73.9% of systematic test cases, and open models score as low as 26.1%. The paper also tests GCG adversarial suffix attacks and examines models' ability to detect rule violations.

## Strengths

- **Systematic taxonomy of 6 attack strategies from red-teaming.** The paper identifies and categorizes strategies (Just Ask, Indirection, Legalese, Obfuscation, Rule Change, Simulation) from retrospective analysis of successful rule-breaking attempts (Section 3.3, Table 2). This provides a structured basis for constructing the test suite and for future defense research.

- **Programmatic evaluation enabling scalable benchmarking.** Each scenario includes a concise evaluation program (a few lines of regex/string matching) that can automatically detect rule violations without human judgment or heavy model inference (Section 2.3). This design makes the benchmark reproducible, low-cost, and easy to extend.

- **Demonstration that all current models fail significantly.** The paper evaluates 13 models on both test suites. The finding that GPT-4, the best model, passes only 73.9% of systematic test cases, and Llama2-7B only 26.1% (Figure 2, Table 1), provides clear empirical evidence that rule-following under simple, verifiable constraints is a challenging unsolved capability.

- **Adversarial suffix experiments (GCG).** Section 3.6 evaluates GCG adversarial suffixes against 7B open models, showing pass rates can be driven to near zero across multiple scenarios (Table 5), demonstrating that automated attacks compound the difficulty revealed by human-written test cases.

- **Error detection analysis.** Section 3.5 tests whether models can *detect* rule violations as a zero-shot binary classification task (1098 sampled outputs). The finding that even GPT-4 achieves only 82.1% accuracy (Table 4) adds depth by showing that not only rule-following but also rule-violation detection remains unsolved.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Naming inconsistency between abstract and body (BIND vs. RULES).** The abstract introduces "the Benchmark for Identifying Non-compliant Decisions (BIND)" (line 5), while the body from Section 1 onward uses "Rule-following Language Evaluation Scenarios (RULES)" (line 23). These are clearly the same benchmark, but the two names are never reconciled. This creates confusion for anyone reading a skimmable preview and then diving into the body, and it introduces an avoidable signal of carelessness. The fix is trivial but must be done before final publication.

- **Per-strategy test case counts not reported.** The paper gives overall counts (355 negative, 507 affirmative, line 117) and reports per-strategy results in Table 9 (appendix), but does not state how many test cases fall into each of the 6 strategy categories. Without this breakdown, the reader cannot assess whether the test suite is balanced across strategies or whether certain strategies dominate. A reader examining per-strategy results in Table 9 also lacks context about the base rates.

- **Human validation of evaluation programs not formally quantified.** The paper acknowledges (line 72) that evaluation programs "are unable to exactly reproduce human judgment in edge cases" and asserts that "in practice the vast majority of rule-breaking outputs from models are unambiguous." However, no formal agreement study (e.g., Cohen's kappa on a stratified sample of model outputs) is provided. This is a real gap, though it is substantially mitigated by the nature of the benchmark: the rules are designed to be objectively checkable (e.g., whether a specific string appears in the output), and edge cases are acknowledged to be a small minority. A human agreement study would strengthen confidence in the benchmark's diagnostic accuracy, especially for any future work using it as a ground-truth evaluation tool.

### Trivial
None.

## Nice-to-Haves

- **Per-strategy performance breakdown in the main paper.** The paper mentions Table 9 (in the appendix) for per-strategy breakdowns. Including a summary in the main body would help readers immediately see which strategies are most effective against which models.
- **A brief external-validity discussion for the specific 15 scenarios.** The scenarios are drawn from computer security properties and children's games. A short paragraph connecting these abstract scenarios to concrete real-world rule-following demands (e.g., legal compliance, content policy) would strengthen the motivation for readers who may not immediately see the connection.
- **A small correlational comparison with an existing red-teaming benchmark (e.g., HackAPrompt or TensorTrust).** The paper distinguishes itself conceptually from these benchmarks (fixed universal rules vs. customizable user-specified rules), but a brief empirical comparison showing divergence in model rankings across benchmarks would make the case for distinctiveness even stronger.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"No validation of evaluation programs" treated as fatal.** The harsh critic elevated this to the paper's single most important structural weakness. I verified: the evaluation programs check objective properties (string presence/absence, regex patterns) on rules designed to be programmatically checkable. The paper acknowledges edge cases. This is a reasonable limitation, not a fatal flaw. Demoted to Minor.
- **"Underspecified novelty" / calls for systematic comparison with Gandalf/TensorTrust/HackAPrompt.** The paper clearly positions itself (line 27) as complementing benchmarks focused on fixed universal rules. The distinction is stated; a systematic comparison is beyond the paper's scope. Moved to Nice-to-Have.
- **"Statistical tests not used for model-to-model comparisons."** The paper explicitly states McNemar's test is used (line 143) and applies it in tables. The criticism is factually incorrect.
- **"Table 9 / appendix details not described."** Stripped by PDF extraction; not an author error.
- **"Reproducibility details about seeds."** Nitpick; the paper specifies temperature=0 and notes API non-determinism is minimal (variance ≤1.1/39 cases, Table 3).
- **"Scenario realism" discussion requested.** The paper already discusses the scenarios' origins (security properties, children's games) in Sections 1-2. A deeper external-validity discussion would be a Nice-to-Have.
- **Strongth Finder items removed as generic/superficial/sycophancy:** None. All 5 identified strengths are concrete, specific, and evidence-grounded.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a novel observation about the paper's approach or results that the authors themselves did not articulate.

## Suggestions

1. **Resolve the BIND/RULES naming inconsistency.** Pick one name and use it consistently throughout the abstract, body, and figures. This is a trivial change with disproportionate impact on clarity.
2. **Report per-strategy test case counts.** Add a simple table or inline sentence specifying how many test cases belong to each of the 6 strategy categories (Just Ask, Indirection, etc.) in the systematic test suite. This takes minimal space and significantly aids interpretability of existing results (Table 9).
3. **Consider adding a human agreement study on a stratified sample.** Even 200-300 example outputs, annotated by 2-3 raters with a reported kappa statistic, would go a long way toward eliminating the remaining uncertainty about the evaluation programs' accuracy.
