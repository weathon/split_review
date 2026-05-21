## Summary

This paper introduces PCE (Planner-Composer-Evaluator), a framework that extracts the implicit environmental assumptions embedded in LLM reasoning traces, structures them into a decision tree, and scores each root-to-leaf path by scenario likelihood, goal-directed gain, and execution cost. This enables embodied agents to select actions under partial observability with dramatically reduced communication. Across two benchmarks (C-WAH, TDW-MAT) and three LLM backbones (GPT-4o mini, GPT-OSS:20B, Gemma3:4B), PCE consistently achieves the best task performance while reducing communication by roughly an order of magnitude. A user study additionally shows human partners perceive PCE's communication patterns as more efficient and trustworthy.

## Strengths

1. **Novel and well-motivated approach to a real problem.** The core insight — that LLM planners already generate implicit assumptions about uncertain environmental states in their reasoning traces, but handle them only locally rather than aggregating them — is genuinely interesting and correctly identifies a limitation of existing LLM-based planners. PCE's design of extracting these assumptions into a structured decision tree and scoring paths by likelihood, gain, and cost is a principled departure from communication-heavy alternatives.

2. **Consistent performance gains across all conditions.** PCE achieves the best or second-best performance on the primary task metric (Total Steps in C-WAH, Total/Food/Stuff transport rates in TDW-MAT) for every one of the 3 LLM backbones × 2 environments = 6 settings. These gains are not marginal: e.g., in TDW-MAT with GPT-4o mini, PCE's 87.50% Total transport rate substantially exceeds the next best (REVECA at 81.25%). The consistency across model families (commercial, open-source reasoning, small open-source) is a genuine strength.

3. **Dramatic reduction in communication while maintaining or improving token efficiency.** Comm counts in Table 1 drop from 6–10 (baselines) to ~2 for PCE; in Table 2, from 13–109 down to 3–14. Token usage (Usages) is often competitive or better than baselines. This demonstrates the framework's core thesis — structured reasoning over assumptions can substitute for costly dialogue.

4. **Component ablation confirms each module's necessity.** Table 3 shows that removing the Planner, Composer, or Evaluator individually degrades Total Steps from 42.76 to 56.46, 46.82, and 47.34 respectively, supporting the claim that all three modules contribute to performance. The LLM scaling ablation (Figure 3) further shows that PCE's gains are additive to scaling model capacity or reasoning depth, confirming the mechanism provides something that scale alone does not.

5. **User study provides human-centered evidence.** While small (n=12), the user study showing that humans perceive PCE's communication as more appropriate, useful, efficient, and trustworthy (Figure 4) goes beyond typical automated evaluation and speaks to the practical motivation of the work.

## Weaknesses

### Fatal
None.

### Major

1. **No variance or statistical significance reported for any result.** Tables 1–3 report only point estimates. C-WAH uses only 10 episodes per condition (line 180). With such small sample sizes, observed differences could stem from noise. For example, on C-WAH GPT-4o mini, PCE's 42.76 steps vs. REVECA's 46.80 is a ~9% improvement, but without standard deviations or confidence intervals, it is impossible to assess whether this difference is reliable. This is a systematic evidential weakness: the conclusions may be correct, but the evidence as presented in the main paper is insufficient to judge robustness. Reporting standard deviations or using paired bootstrap tests across episodes is standard practice in this area, and their absence weakens the paper's quantitative claims.

2. **Core LLM-based likelihood and gain estimates are not validated in the main paper.** The Evaluator's action selection depends critically on the accuracy of $\mathcal{L}(\mathcal{S})$ (scenario likelihood) and $\mathcal{G}(a)$ (conditional gain), both estimated by additional LLM calls. The paper provides no evidence that these estimates are accurate, calibrated, or directionally correct. If the LLM systematically overestimates plausible-sounding assumptions or underestimates unlikely ones, the entire scoring mechanism reflects LLM biases rather than a principled uncertainty treatment. The paper mentions "reliability assessments of the Composer and Evaluator based on human-expert correlation studies" in Appendix A.10 and A.11, but no results from these assessments appear in the main text. Since the validity of the core mechanism depends on this, some representative validation (even a scatter plot of estimated vs. empirical frequencies in a held-out set of states) should be in the main paper.

3. **The "comparable token usage" claim in the abstract and conclusion is misleading for certain conditions.** In TDW-MAT with GPT-4o mini (Table 2), PCE uses 197,807 tokens vs. CoELA's 113,059 — a 75% increase. While PCE is more token-efficient than some baselines (CaPo, CoTS) in this condition, the gap to the most token-efficient baseline is substantial. The abstract's blanket claim of "comparable token usage" is imprecise and should be qualified: PCE improves task performance while token usage is in many cases competitive and in some cases moderately higher. The paper's own discussion (Section 5.1, lines 230–231) acknowledges the per-step cost tradeoff more accurately than the abstract.

### Minor

1. **Limited detail on whether baseline hyperparameters were tuned for these environments.** The paper states baselines are "run under identical environmental and communication settings" (line 186) and defers to Appendix A.2 for details. It does not state whether each baseline's hyperparameters (e.g., MCTS budget for CoTS, debate rounds for CaPo, memory lengths for CoELA) were tuned or validated for the specific environments. Given the large performance gaps (e.g., PCE at 81.25% vs. CoTS at 59.17% on TDW-MAT with GPT-OSS:20B), the possibility of suboptimal baseline configurations is a fairness concern.

2. **User study has limited statistical rigor.** With 12 participants and no reported inferential statistics (significance tests, confidence intervals, or inter-rater reliability), the user study results (Figure 4) are indicative but not conclusive. The paper does not overclaim on this front, but the results should be described as preliminary rather than as firm evidence.

3. **C-WAH's small benchmark size.** C-WAH consists of only 10 episodes (line 180). While the paper does run 3 LLM backbones and TDW-MAT has 24 episodes, the C-WAH results are based on a small number of trials per condition.

### Trivial
- The paper states PCE yields "comparable token usage" (abstract, conclusion) but then in Section 5.1 explains the per-step vs. episode-length tradeoff. The abstract and conclusion should be harmonized to match the more nuanced discussion.
- The method section (Section 4.3, lines 140-142) describes the Composer's expansion policy as using "LLMs' commonsense reasoning" to select which assumption to branch on, but provides no information about the prompt or criteria used. While acceptable for a conference paper with an appendix, a brief illustrative example in the main text would help.

## Nice-to-Haves
- A simple sanity check comparing the LLM's $\mathcal{L}$ estimates to empirical frequencies in a held-out subset of environment states (even 2–3 illustrative examples) would significantly strengthen confidence in the Evaluator's reliability.
- An ablation where the Composer's tree expansion is replaced by a rule-based mechanism (e.g., expand all action-relevant assumptions without LLM guidance) would isolate the value of the LLM-driven tree construction, complementing the existing "w/o Composer" ablation that removes the tree entirely.
- A discussion of failure cases — examples where PCE makes a poor assumption or where the Evaluator's ranking leads to a suboptimal action — would provide a balanced view.

## Removed Points
- **"Composer's expansion stopping condition is vague"** (Harsh Critic #1): This is described in Section 4.3 as stopping at depth D or when "further splits would not materially affect action choice." While some readers might want more precision, this is standard in tree-based methods and is a minor implementation detail, not a structural weakness.
- **"GPT-OSS:20B baseline comparison not apples-to-apples"** (Harsh Critic, Section-by-Section): The paper explicitly states all LLM backbones are used consistently across all methods (line 188), so this concern is factually incorrect.
- **"C-WAH 10 episodes insufficient"** (Harsh Critic, indirectly): Reclassified to Minor. The sample size is noted as a limitation but is standard in this benchmark; the more serious issue is the absence of variance reporting.
- **"Token usage token vs. time cost"** (Harsh Critic, Section-by-Section): This observation about CoELA's token usage being close to PCE's on C-WAH-Gemma3:4B is actually a data point that supports the paper's claim, not a weakness.
- **"Baseline hyperparameters not disclosed"** (Strengthening the Paper, point 4): The paper states baseline details are in Appendix A.2, which is standard practice. This is downgraded to a minor concern about tuning, not a disclosure concern.
- Various formatting, presentation, and grammar nitpicks from the Harsh Critic's Section-by-Section notes are removed per the filtering rules (parser artifacts, not author errors).

## Novel Insights
The reviews collectively surface an important tension: the paper's central contribution is that implicit assumptions in LLM reasoning can be explicitly modeled and evaluated, but this very dependency on LLM estimates (for likelihood, gain, and tree expansion) means the "principled" nature of the uncertainty handling is only as reliable as the LLM's own calibration on these estimation tasks. This is a meta-level observation about the field: as LLM-based planning frameworks become more sophisticated in their structural design (trees, scoring functions, modular pipelines), the weakest link increasingly becomes the reliability of the individual LLM calls that populate those structures. The paper would be substantially strengthened by simply measuring — even on a small scale — whether its LLM-based estimates actually correlate with ground-truth outcomes, rather than treating these estimates as given.

## Suggestions
1. Add standard deviations (or better, episode-level results) to Tables 1–3. For C-WAH's 10 episodes, individual episode scores or a range would help. A paired bootstrap test comparing PCE to the best baseline would be ideal.
2. Qualify the token usage claim in the abstract and conclusion: e.g., "PCE improves task performance while maintaining token usage that is competitive with or moderately higher than baselines, with the largest increase in [specific condition]."
3. Include at least one validation experiment for the Evaluator's $\mathcal{L}$ estimates in the main paper — e.g., collect a held-out set of environment states, have the LLM estimate scenario likelihoods, and report Spearman correlation with actual frequencies.
4. State explicitly in the main text whether baseline hyperparameters were tuned on a validation set and, if so, what values were used.
5. For the user study, report at minimum the per-question standard deviations and, ideally, a simple significance test (e.g., Wilcoxon signed-rank comparing PCE to the next-best condition).

## Score and Decision
MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>