Now I have a thorough understanding of the paper. Let me write the consolidated review.

## Summary

CALM proposes a framework for automatic heuristic design that jointly evolves heuristic populations via evolutionary operators (verbal guidance) while fine-tuning the underlying LLM via GRPO reinforcement learning (numerical guidance). Using a quantized 7B model on a single 24GB GPU, CALM achieves state-of-the-art results across four optimization benchmarks (OBP, TSP, CVRP, OP), outperforming prior methods that rely on more powerful frozen API-based models.

## Strengths

- **RL-adapted small model beats stronger frozen models across all tasks**: Tables 1–3 consistently show that CALM (Qwen2.5-7B-INT4 + GRPO) outperforms all baselines using GPT-4o-mini or GPT-3.5-turbo without fine-tuning. On OBP (Table 1), CALM achieves 0.71% avg. gap vs. the best API-based method (MCTS-AHD) at 0.89%. On CVRP (Table 3), CALM achieves 3.83%/5.44%/3.95% at N=50/100/200 vs. MCTS-AHD's 5.44%/6.98%/4.70%. These results are consistent across all four problems and three runs each.

- **Verbal guidance operators alone are competitive with prior SOTA**: The API-based CALM variant (GPT-4o-mini, no GRPO, G=1) matches or exceeds prior methods across tasks — outperforming MCTS-AHD on OBP (0.82% vs. 0.89%), OP, and TSP N=200, while closely tracking on CVRP. This cleanly demonstrates that the newly designed operators (injection, replacement, diversity-aware crossover) are independently effective, independent of RL.

- **Ablations validate all major components**: Table 4 systematically ablates operators, collapse mechanism, and reward designs. Every removed operator degrades performance; the collapse mechanism improves results (0.98%→0.71% on OBP); and the progressive reward function outperforms two alternative designs. The breadth of the ablation study is a strength.

- **Resource efficiency with public code**: CALM runs on a single 24GB GPU with a quantized 7B model and provides open-source code, making the approach accessible for local deployment without API dependencies.

## Weaknesses

### Fatal
None.

### Major

- **Evaluation budget accounting between RL variant and baselines/ablations is not fully transparent.** The paper states "comparable evaluation budgets — specifically, 1,000 heuristic evaluations for baselines and a fixed budget of 2,000 LLM queries for CALM" (Section 5). However, "LLM queries" and "heuristic evaluations" are different units when GRPO samples G > 1 responses per query (as described in Section 3.2). The value of G for the main RL experiments is not stated in the main text. If G > 1, the RL variant evaluates G×2000 heuristics vs. baselines' 1,000, making the budgets asymmetric. Furthermore, the Table 4 ablation comparing "local, w/ GRPO" vs. "local, w/o GRPO" likely uses different G values (since GRPO requires G>1 to compute advantage), meaning the observed improvement (1.78%→0.71% on OBP) could partially reflect increased search evaluations rather than RL adaptation alone. This does **not** invalidate CALM's overall superiority — the API variant (G=1, 2000 queries) already matches or beats baselines, and the RL improvement over it is consistent across all four tasks — but it weakens the specific claim that "the reinforcement learning component has the most significant impact among all ablation settings" (Section 5.2). The authors should disclose G for all experiments and, ideally, provide a controlled comparison where total heuristic evaluations are equalized.

### Minor

- **Claim that fine-granularity operators improve RL credit assignment is plausible but unsubstantiated.** Section 4.1 argues that injection/replacement operators "encourage the LLM to retain more common parts" so that "GRPO is expected to more effectively identify the contribution of individual structural changes." The only evidence (Table 4) is that removing these operators degrades overall performance. This is consistent with many explanations (reduced diversity, narrower exploration, loss of useful operator types). No experiment isolates the interaction between these operators and the RL credit-assignment mechanism (e.g., comparing token-level advantage distributions with vs. without the operators, or controlling for search diversity). The operators clearly help; the specific mechanism claimed is reasonable but unproven.

- **Derivation of collapse timing (Equation 2) is presented but not empirically validated.** The paper provides an analytical approximation for expected rounds before collapse (Eq. 2) and states it "aids in hyperparameter selection." However, the collapse hyperparameters tested in Table 4 (δ₀ = 0.0005 or 0.005, C = 15 or ∞) are not derived from the formula, and no analysis validates that Equation 2 predicts collapse timing in practice. This component adds theoretical framing without demonstrated utility.

- **Main results tables lack variance information.** Tables 1–3 report averages over three runs without confidence intervals or standard deviations. While p-values are referenced for Appendix I (stripped), the main tables would benefit from including standard deviations or error bars to assess significance, especially for close comparisons (e.g., TSP N=50: 10.04% vs. 9.69%).

### Trivial

- Figure 2 is described in the caption text but the figure itself (images stripped by parser) is not visible; the description clarifies the trend and should be supplemented with the actual plotted data in the final version.
- The paper sometimes uses "comparable" to describe budgets that differ by a factor of 2 (API variant: 2000 evaluations vs. baselines' 1000) — this wording could be more precise.

## Nice-to-Haves

- Provide a budget breakdown table with columns: # LLM queries, # heuristic evaluations, G value, # rounds for each method.
- Analyze whether the injection/replacement operators actually reduce variance in performance changes across generations, which would indirectly support the credit-assignment narrative.
- Visualize collapse events and the stagnation counter on representative runs.
- Directly control for total heuristic evaluations in a follow-up experiment comparing "local, w/ GRPO" and "local, w/o GRPO" with equalized evaluation counts (e.g., by using the same G and discarding extra responses in the non-RL case).

## Removed Points

These points were raised by reviewers but are removed from the main weakness list with justification:

- **"Budget issue invalidates comparison with baselines" (Harsh Critic)** — Demoted from Fatal to Major. The API variant (G=1, 2000 queries) provides a fairer comparison and is already competitive with SOTA. The RL improvements are consistent across all four tasks. The paper's core claim (CALM outperforms baselines) is supported by multiple lines of evidence, not solely the RL ablation.

- **"Why EvoTune performs poorly on OBP" (Harsh Critic — Missing Analysis)** — The paper is under no obligation to explain why a specific baseline underperforms on one task. This is a curiosity question, not a valid weakness.

- **"Missing variance/confidence intervals in main tables"** — Demoted from what the harsh critic labeled to Minor. The paper reports 3-run averages and defers statistical tests to Appendix I (stripped). Standard practice in this field varies; this is addressable but not a serious flaw.

- **"Scaling to larger LLMs and transfer to new problems" (Harsh Critic — Obvious Next Steps)** — These are future work suggestions, not weaknesses of the current paper.

- **"Concurrent works acknowledged but..." (Harsh Critic — Abstract/Intro note)** — The paper explicitly acknowledges concurrent works (EvoTune, Liu et al. 2025) in Section 2. The criticism about framing is not substantiated.

- **Strength Finder: generic or overly broad strengths removed** — Removed generic statements about "addressing an important problem" and "targeting an interesting question." Kept only concrete, evidence-backed strengths.

## Novel Insights

The most interesting observation from the reviews is the *asymmetric comparison structure*: the same set of evolutionary operators, when paired with a weak local model fine-tuned via RL, can beat a stronger frozen model that uses the same operators. This suggests that in LLM-based AHD, the model's ability to *specialize* through fine-tuning can compensate for raw capability differences — a finding with implications beyond this specific paper. However, the evaluation budget confound tempers this conclusion, and the paper's current evidence does not fully disentangle RL-driven adaptation from the increased search evaluations that G>1 sampling entails.

## Suggestions

1. **Clarify G and the budget accounting in the main text.** State the value of G for all RL experiments (not just the API variant) and provide a table comparing total heuristic evaluations across all methods. This is the single most important fix.
2. **Run a controlled ablation** where "local, w/ GRPO" and "local, w/o GRPO" use the same G value (e.g., G=8 for both, with the non-RL variant keeping all responses as candidates but not computing advantages). This would isolate the effect of RL from the effect of additional search.
3. **Include standard deviations or confidence intervals** in the main tables, or at minimum note which comparisons are statistically significant.
4. **Add a diversity analysis** to support the claim about fine-granularity operators — e.g., show the number of unique heuristic structures generated per round with and without injection/replacement.
5. **Either validate Equation 2 empirically or remove it.** Show that the predicted collapse timing correlates with observed stagnation behavior on representative runs, or drop the equation to avoid overclaiming.

## Score and Decision

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>