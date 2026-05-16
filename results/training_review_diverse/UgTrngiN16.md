Here is the consolidated meta-review.

---

## Summary

LangProp proposes a framework for iteratively optimizing LLM-generated code by drawing a direct analogy to neural-network training: code is treated as parameters, the LLM as an optimizer, and execution feedback as gradients. The framework supports IL, DAgger, and RL training paradigms. It is demonstrated on Sudoku, CartPole (9/10 seeds converge to optimal within ~10k steps vs PPO's ~80k), and CARLA autonomous driving, where the best LangProp agent (Online IL/RL) achieves a testing-route score of 80.9 — competitive with several hand-crafted expert agents.

## Strengths

1. **Well-motivated and clearly described framework.** The analogy between code-as-parameters and neural-network training is conceptually clean. The priority-based evolutionary update (Equation 1), the prompt template engine, and the checkpoint design are clearly presented. The framework is task-agnostic and does not require an LLM at inference time — a practical advantage for real-time systems.

2. **Demonstrated transfer of ML training paradigms to code optimization.** The paper provides an explicit ablation showing the expected ordering: offline IL (0.07) → DAgger IL (36.2) → DAgger IL/RL (64.2) → Online IL/RL (70.3) on CARLA training routes (Table 1). This is a non-trivial finding that validates the core thesis — that standard training paradigms (IL, DAgger, RL) can be ported to LLM-based code optimization with the expected relative performance.

3. **Competitive CARLA results.** The best LangProp agent (Online IL/RL) achieves a testing-route score of 80.9, outperforming the Roach expert (63.4), TransFuser (73.1), and InterFuser (78.6) experts, and coming close to TF++ (86.1) and the authors' own expert (95.2). This is a meaningful proof-of-concept for automated code optimization in a complex, safety-critical domain.

4. **Interpretability advantage demonstrated concretely.** The causal confusion analysis (Section 4.3.4) identifies a specific code pattern — returning 0 speed when the agent's speed is already near 0 — that explains offline IL failure, and shows how online data alleviates it. This is a genuine strength of code-as-policy: the failure mode is readable and fixable, which is not possible with neural network weights.

5. **Sample efficiency in CartPole.** 9/10 LangProp seeds converge within ~10k environment steps vs PPO's ~80k (Figure 2). While CartPole is relatively simple, the 8× sample efficiency is striking and supports the claim that LLM-as-optimizer can be efficient in tasks amenable to symbolic reasoning.

## Weaknesses

### Fatal
None.

### Major

1. **No variance reporting for CARLA results (Table 1).** The paper's central empirical claim — that LangProp produces competitive driving policies — rests on single-number entries with no standard deviations, no number of independent runs, and no significance tests. The LLM's stochastic responses and the evolutionary selection loop introduce multiple sources of randomness, so single-run numbers could be outliers. The CartPole experiment reports 10 seeds, showing awareness of the need for multiple runs, yet this practice is not extended to the far more complex CARLA setting. This is the most significant weakness: the reader cannot assess the reliability of the headline comparison. The authors should provide results from at least 3–5 independent training runs with mean ± std for the driving score and its components.

### Minor

2. **Training curve bands are unexplained (Figure 4).** The caption describes score ranges and axis limits but never states what the shaded bands around each line represent. Are they standard deviations across seeds? Across batches within a single run? Min-max ranges? Without this information, the figure's evidentiary value is diminished.

3. **Sudoku demonstration is too thin.** Section 4.1 provides no quantitative metrics (success rate, iterations to convergence, comparison to baselines). It merely states that the LLM initially failed and LangProp found a working solution. As presented, it does not add meaningful evidence for the framework's capabilities and could be moved to an appendix.

4. **No limitations or failure-case discussion.** The paper never addresses what happens when the LLM cannot generate sensible updates, when the policy space exceeds the prompt context window, or under what conditions LangProp is likely to fail. A brief limitations paragraph would strengthen the conclusion and help readers assess applicability to their own problems.

5. **Hyperparameter choices are stated but not justified.** The values \(N^U = N^R = N^K = 3\) are given for CartPole (Section 4.2), but there is no sensitivity analysis or justification for these choices. It is unclear whether the same values are used across all experiments, or whether performance is sensitive to them.

### Trivial

None.

## Nice-to-Haves

- Report the number of LLM queries, approximate token usage, and total wall-clock time for the CARLA experiment. This would help practitioners gauge practicality.
- Add a brief comparison of LLM call cost for LangProp vs. the zero-shot baseline.
- Report total LLM queries alongside environment steps in the CartPole experiment.
- A quantitative breakdown of priority distributions before and after DAgger would strengthen the causal confusion analysis, though the qualitative analysis already makes the point effectively.

## Removed Points

- **Missing related works (Reflexion, Self-Refine, LEAP):** Removed per hard rule — I cannot verify the existence or relevance of these references, and the paper already cites several relevant iterative code-improvement works (Voyager, CLAIRify, CodeRL).
- **Sudoku section described as "too weak to be meaningful":** Downgraded from the reviewer's framing. The section is indeed thin but the paper's main evidence comes from CartPole and CARLA, not Sudoku. Classified as Minor (weakness #3 above) rather than a structural flaw.
- **"Causal confusion analysis is only qualitative":** Removed. The qualitative code-snippet analysis is actually a *strength* demonstrating interpretability — the ability to read the exact line causing failure is the point. Requesting quantitative breakdowns goes beyond what is needed to make this contribution.
- **Criticism about y-axis truncation being "unexplained":** Partially removed. The caption *does* explain the score range ([-10, 1]) and that the axis is limited to [-1, 1]; the reviewer appears to have missed this. The remaining valid sub-point (bands unexplained) is kept as Minor weakness #2.
- **Criticism that paper should discuss whether methods like CodeRL are complementary/competing:** Removed. The paper already cites CodeRL (line 36 in related work) as "orthogonal" and compatible. The reviewer's request for a deeper discussion is a nice-to-have, not a weakness.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface any novel perspective on the work that the paper itself does not already articulate.

## Suggestions

1. **Add multiple-seed CARLA results (3–5 runs, mean ± std for all columns of Table 1).** This is the single highest-leverage change and would address the most serious weakness. The trend across training paradigms (offline IL → DAgger → online) is strong enough that variance is unlikely to flip the conclusion, but reporting it would make the paper's central empirical claim verifiable.

2. **State what the shaded bands in Figure 4 represent** in the caption — e.g., "shaded regions denote standard deviation across X runs" or "across batches within a single run."

3. **Add a brief limitations paragraph** to the conclusion discussing: (a) dependence on LLM capability for generating sensible updates, (b) context-window constraints, and (c) scenarios where LangProp would not be expected to work well.

## Score and Decision

The paper proposes a well-motivated framework, demonstrates it across multiple domains, provides clean ablations validating the transfer of ML training paradigms to code optimization, and achieves competitive results in a realistic driving benchmark. The most significant weakness — lack of variance reporting for CARLA — is addressable and does not undermine the paper's core contribution (the framework itself and the validation of the training-paradigm analogy). The framework is novel, clearly described, and the interpretability advantage is convincingly demonstrated.

**Score: 7.0 / 10** — A solid paper with a useful framework, one significant but fixable methodological gap, and several minor presentation issues.

**Decision: Accept**

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>