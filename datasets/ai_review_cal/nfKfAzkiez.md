- Decision: Accept
- Avg Score: 5.75
- Scores: 6, 6, 5, 6
Now I have a thorough understanding of the paper and all reviewer claims. Let me construct the final consolidated review.

## Summary

The paper proposes ACC-Debate, a framework for jointly training a two-agent team (actor + critic) for multi-agent debate via iterative best-response optimization. It introduces "guided-debate" trajectory generation — steering debates toward/away from correct answers via prompt modification — to create off-policy preference data for DPO training. The method achieves the best or second-best accuracy on 14 of 15 task×model combinations across Llama-3, Mistral, and Gemma-2 on five QA benchmarks.

## Strengths

1. **First joint training of an actor-critic team for debate.** The paper formalizes debate as a bi-level max-max optimization (Eq. 1) solved via iterative best-response, treating collaboration as a learned behavior rather than emergent. This is a principled departure from prior work that trains only single models (DebateGPT) or relies on untrained off-the-shelf models (SoM, Persona). (Lines 100–121)

2. **Guided-debate trajectory generation.** Section 4.3 introduces an efficient off-policy scheme that uses answer-hint prompts to steer debate trajectories toward/away from correct answers, enabling the creation of high-quality preference pairs even when the model performs poorly on a dataset. This addresses a genuine limitation of naive rollout sampling. (Lines 189–219, Algorithm 1)

3. **Strong and broad empirical results.** ACC-Debate/ACC-Debate+ achieves the highest or second-highest accuracy on 14 of 15 task×model combinations (Table 1). On several settings the gains are large — e.g., BoolQ with Llama-3: 0.894 vs. next-best 0.815; Mistral BBH: 0.601 vs. next-best 0.48. The ablation in Table 2 usefully separates the contributions of the trained actor vs. trained critic.

4. **Qualitative analysis of learned critic behavior.** Figure 5 shows a concrete example where the trained critic becomes more willing to disagree and provides detailed feedback, in contrast to the untrained critic's agreeable but unhelpful responses. This provides interpretable evidence for what the training changes. (Lines 394–401)

## Weaknesses

### Fatal
None. The core contributions are novel and largely supported by the evidence.

### Major

- **Unaddressed failure on Gemma-2 MMLU.** ACC-Debate achieves 0.51 on Gemma-2 MMLU, substantially *below every baseline* (DebateGPT: 0.582, SoM-2x: 0.58, SFT: 0.579, Persona: 0.577). ACC-Debate+ (0.555) also underperforms all baselines. The paper's conclusion states "ACC-Debate outperforms all baselines on a wide array of domains" (line 409) without acknowledging or analyzing this counter-example. Understanding why the method fails — poor training data quality for this model+task, insufficient capacity of the 2B model, or harmful preferences — would significantly strengthen the contribution. As written, the claim of universal superiority is overstated.

- **Potential confound from answer-label injection in guided-debate training.** The guided-debate data generation (Section 4.3) explicitly provides the correct/incorrect answer in the prompt to produce steering trajectories. The resulting preference data compares trajectories where the correct answer was given as a hint against trajectories where a wrong answer was given. The paper does not present a control experiment (e.g., replacing guided trajectories with natural rollouts that happen to have high/low reward) to disentangle whether the model learns genuine collaborative reasoning versus imitation of answer-driven response patterns. This is a validity concern for interpreting *what* the method actually learns.

### Minor

- **Threshold ε never specified nor ablated.** Equation 3 defines a threshold ε for selecting preference pairs, but its numerical value is never reported, and no sensitivity analysis is provided. The value likely controls the size and quality of the training dataset.

- **Inconsistency between Algorithm 1 and Equation 3 thresholds.** Algorithm 1 (lines 164–168) uses the round number `t` as the threshold for accepting trajectory pairs (`v_+ - v ≥ t`), while Equation 3 uses ε. The relationship between these two thresholds is never explained.

- **Reward estimation procedure underspecified.** The paper states that "one-step roll-out heuristics" are used to estimate r(z^(t), x, y) (line 134) but does not specify how many rollouts per state are taken. If a single continuation is used, each estimate is binary (0/1), yielding a noisy signal. The paper provides no variance analysis or justification for why this suffices.

- **Missing ablations.** The paper does not isolate whether the gains come from (i) preference optimization (DPO) vs. supervised fine-tuning on the same guided trajectories, (ii) guided vs. unguided (natural) trajectory generation, or (iii) whether the trained actor's improved zero-shot accuracy (Table 2) accounts for most of the improvement rather than enhanced collaboration. These ablations would clarify which components drive the results.

- **Per-round analysis limited to a single dataset.** Figure 4 shows per-round accuracy only for BoolQ. Different datasets may show different convergence trends.

### Trivial
- The conclusion's claim that ACC-Debate "outperforms all baselines" (line 409) is contradicted by the Gemma-2 MMLU result. This should be qualified (e.g., "outperforms baselines on most benchmarks").

## Nice-to-Haves
- A signed-rank test or similar across datasets to establish whether the improvements are statistically significant as a whole.
- A comparison of training/inference computational cost against baselines, especially inference-time methods like SoM with 4 agents.
- Evaluation on a non-QA task (the paper acknowledges this limitation in the conclusion).

## Removed Points
These points from the inputs were removed because they were speculative, factually incorrect, or failed verification against the paper:

- **"No justification for why one iteration of iterative best-response is sufficient"** — The paper states "we find that a single iteration is sufficient" (line 121) and supports this with empirical results showing ACC-Debate (one iteration) works well across most settings. The critic's request for convergence analysis is beyond what is standard for an empirical systems paper.
- **"DPO loss treats all rounds equally with no ablation on weighting"** — While an ablation on round weighting could be nice, this is not a standard expectation and the uniform weighting is a reasonable default.
- **"No convergence analysis of iterative best-response"** — The paper cites the Stackelberg game and iterative best-response literature for theoretical grounding, and provides empirical validation. This is sufficient for a conference paper.
- **Formatting nitpicks** (table complexity, column labels) — These are parser artifacts and do not reflect the original submission.
- **"Evaluation on held-out datasets outside QA"** — The paper acknowledges this limitation explicitly in the conclusion; criticizing it further adds no new information.
- **"Computational cost comparison missing"** — A nice-to-have, not a core weakness.

## Novel Insights
None beyond the paper's own contributions. The reviews largely surface expected concerns about a first-of-its-kind training method (label leakage confound, missing ablations) without adding fundamentally new analysis angles. The observation that the critic's improved disagreeing behavior (Figure 5) is the most interpretable evidence of learned collaboration is already present in the paper's own qualitative analysis.

## Suggestions
1. **Explicitly discuss the Gemma-2 MMLU failure.** Analyze why it occurs and what it implies about the method's适用范围 (e.g., is the 2B model too small for the guided-debate signal to be effective? Is MMLU's breadth causing training data sparsity?).
2. **Add a control experiment** that replaces guided trajectories with naturally sampled trajectories matched for reward, to test whether label injection is essential.
3. **Report the numerical value of ε** and provide a sensitivity analysis (e.g., ε ∈ {0.05, 0.1, 0.2}).
4. **Clarify how the threshold in Algorithm 1 (using round number t) relates to ε** in Equation 3. If they are the same, unify the notation.
5. **Specify the number of rollouts** used for the one-step reward estimation and, if practical, add multi-rollout variance estimates.
