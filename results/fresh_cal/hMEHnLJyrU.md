Now I have all the information I need. Let me produce the consolidated review.

## Summary

This paper proposes a novel methodology for evaluating LLM generation diversity by leveraging code as a domain where semantics are executable. The authors create a dataset of 21 open-ended program synthesis tasks, define semantic diversity by comparing program outputs on test cases, and conduct an extensive empirical study across multiple model families, sizes, and prompting strategies. The central finding is that instruction tuning—especially preference tuning—*increases* semantic diversity while decreasing lexical and syntactic diversity, challenging prior claims that alignment uniformly reduces diversity. The paper also demonstrates that neural diversity metrics (CodeBERTScore, ICE-Score) fail to reflect execution-based semantic diversity.

## Strengths

- **Novel methodology for automatic semantic diversity evaluation.** The paper constructs an open-ended program synthesis dataset (Section 3, Figure 2) and defines semantic diversity by comparing programs' execution outputs on fixed test cases (Section 4). This enables objective, scalable diversity measurement without human evaluation, directly attacking a core bottleneck in diversity research. The pairwise-averaging metric (Equation 2) is validated to be sample-size-invariant (Figure 3), a necessary technical step often overlooked.

- **Counterintuitive and nuanced empirical finding.** Table 1 reports that for preference-tuned models (LLAMA-3, LLAMA3.1, QWEN-CODER-2.5), semantic diversity significantly increases (large to huge Cohen's d effect sizes) while lexical/syntactic diversity decrease. This contradicts the narrative that alignment uniformly suppresses diversity and is the paper's central empirical contribution. The finding that SFT-only models show more modest effects (and often non-significant) adds useful granularity to the result.

- **Demonstration that neural diversity metrics fail on code.** Figure 4 shows negative Spearman/Kendall correlations between neural metrics (CODEBERTSCORE, ICE-SCORE) and execution-based semantic diversity. Figure 5 provides concrete failure cases where CODEBERTSCORE gives nearly maximal similarity to semantically distinct programs. This evidence supports the paper's claim that existing metrics are insufficient for measuring semantic diversity in code.

- **Systematic and broad experimental scope.** Across model families (LLAMA-3, LLAMA3.1, CODELLAMA, QWEN-CODER-2.5, commercial models), sizes (7B–70B), prompting strategies (zero-shot, few-shot), and instruction-tuning methods (SFT, PPO, DPO, rejection sampling), the paper provides a comprehensive survey. The use of paired Wilcoxon tests and Cohen's d throughout is methodologically sound.

## Weaknesses

### Fatal

None.

### Major

- **The main results conflate coherence with semantic diversity, weakening the headline claim.** The semantic diversity metric in Tables 1 and 2 is computed over **all** 100 generations per problem, including those with syntax errors, runtime errors, or missing function definitions. Since error outputs are all recorded as failures (and different errors of the same type count as semantically similar), a base model that produces mostly incoherent code will have artificially depressed semantic diversity—not because it lacks the capacity for diverse solutions, but because it cannot reliably produce valid ones. The paper acknowledges this concern and states that it analyzes semantic diversity among only well-formed programs in the appendix (Section 4, footnote 3). However, the **primary evidence** for the paper's central finding—Tables 1 and 2—does not present this controlled analysis. The "BEST COH." row selects the prompt that maximizes coherence for each model but still aggregates over all generations, including incoherent ones. Until the coherence-controlled analysis is presented as primary evidence, the headline result that "instruction tuning increases semantic diversity" remains vulnerable to the simpler explanation that instruction-tuned models simply generate *more valid programs*, not necessarily a more diverse set of valid solutions. This does not invalidate the paper—the authors state they have performed the controlled analysis—but it means the main presentation undersupports its strongest claim.

- **Small problem set with limited characterization.** The dataset comprises only 21 competitive programming problems adapted from CodeNet. While generating 100 samples per problem is reasonable, 21 problems is a thin basis for the broad claims the paper makes about diversity. The paper does not report per-problem variance, problem selection criteria, or the diversity of algorithmic approaches required across problems. The conclusion acknowledges this limitation, but the gap between the scope of the claims ("cooking recipes, essays, unit tests" in the introduction) and the empirical foundation (21 CP problems) is noticeable.

### Minor

- **No multiple-testing correction across many comparisons.** Tables 1, 2, and 3 report many paired Wilcoxon tests (p-values) without any adjustment (Bonferroni, Benjamini-Hochberg, etc.). Given the number of comparisons, some correction would be standard practice.

- **Test case coverage and selection are not discussed.** Semantic diversity is defined relative to a fixed set of test cases per problem. The paper mentions these come from AlphaCode but does not report how many test cases per problem, how they were selected, or how exhaustive they are. If test cases are sparse, the semantic diversity metric could systematically undercount diversity for all models, and it is unclear whether this interacts with model type.

### Trivial

None.

## Nice-to-Haves

- Present the well-formed-only semantic diversity analysis (currently in the appendix) as a primary result in the main text. This would directly address the coherence confound and substantially strengthen the paper's central claim.
- Include per-problem breakdowns of semantic diversity (e.g., box plots or standard deviations) to show that results are not driven by a few outlier problems.
- Add a brief discussion of test case coverage per problem so readers can assess the granularity of the semantic equivalence definition.
- Distinguish more consistently between SFT and preference-tuning claims throughout the paper, since the effects differ substantially between these two categories.

## Removed Points

These points are flagged to be removed, treat them with caution:

1. **Claim that the paper "never presents" the well-formed-only analysis.** The paper explicitly states (Section 4, line 83) that it analyzes semantic diversity among only well-formed programs. This analysis resides in the appendix, which was stripped by the PDF parser. The criticism is that it is not in the main text—this is a presentation choice, not an omission.

2. **Criticism that speculative claims about "voice" and RL dynamics are unsupported.** The paper frames these as speculation ("We speculate that...", "We hypothesize that...") in the Discussion section. Speculation in a discussion section is standard and appropriate.

3. **Claim that CoT was "not used in most experiments" without explanation.** The paper states it created three prompts (zero-shot, two-shot, two-shot+CoT). BEST COH./BEST SEM. rows in Table 1 select the best prompt for each model, which could include CoT. The main focus on zero-shot vs. two-shot is a reasonable experimental design choice.

4. **Criticism that the comparison is "unfair" to base models.** The asymmetry (base models struggle on instruction-following tasks) is inherent to studying instruction tuning—comparing models with and without instruction-following capability necessarily involves a task that requires instruction following. The paper acknowledges this and attempts to control for it.

5. **The "open-endedness" criticism.** The paper explicitly scopes itself to code generation with open-ended prompts (the task description is abstracted to allow multiple valid solutions). Competitive programming problems are a reasonable starting point for this investigation, and the paper acknowledges the limitation.

## Novel Insights

None beyond the paper's own contributions. The reviewers did not surface a synthetic insight that goes deeper than what the paper itself articulates.

## Suggestions

1. **Foreground the coherence-controlled analysis.** Move the analysis of semantic diversity among only well-formed (or only correct) programs from the appendix into the main results tables. This single change would neutralize the paper's most significant vulnerability.

2. **Report per-problem variance.** Add standard deviations, confidence intervals, or per-problem box plots for the semantic diversity metric across the 21 problems to demonstrate that results are consistent rather than driven by a few tasks.

3. **Add multiple-testing correction.** Apply Benjamini-Hochberg or a similar correction to the p-values reported across Tables 1–3, or at minimum acknowledge the multiple comparisons and note which results survive correction.

4. **Discuss test case coverage.** Briefly characterize how many test cases are used per problem and how they were selected from the AlphaCode test suites, so readers can assess the granularity of the semantic equivalence relation.

5. **Tighten the scope-language match.** The introduction invokes cooking recipes and essays, but the evaluation is purely on competitive programming code. The conclusion already acknowledges this gap; a sentence in the introduction scoping the claims could better calibrate expectations.

## Score and Decision

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>