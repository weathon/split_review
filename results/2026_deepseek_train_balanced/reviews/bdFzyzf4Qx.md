## Summary

This paper applies independent Q-learning to the Lowest Unique Positive Integer (LUPI) game. The authors train Q-learning agents and compare their learned strategy to the Poisson–Nash equilibrium from Östling et al. (2011), reporting visual similarity. They also test their agent against historical Limbo lottery data by inserting its choices retroactively, claiming win rates of 16.33% (8/49 rounds) and 12.24% (6/49) that "outperform" theoretical predictions. The paper argues that learning-based approaches are more flexible than static equilibrium models when the Poisson assumption on player counts is violated.

## Strengths

- **First Q-learning implementation for LUPI.** The paper is the first to demonstrate that independent Q-learning can be applied to the LUPI game without requiring the Poisson distribution assumption. This directly follows Östling et al.'s own suggestion (line 39) that learning models are the natural next step beyond their cognitive hierarchy model.

- **Minimal information setting.** Each agent observes only its own action and the global "no one won" signal (line 92). This matches the practical constraints of real Limbo where players cannot observe others' choices before the draw closes, making the approach more realistic than methods assuming full opponent observability.

- **Hyperparameters fully specified.** The paper provides all Q-learning parameters (α=0.01, ε=0.95, T=0.15, 3000 episodes, lines 108–112), enabling replication.

## Weaknesses

### Major

**1. Exploration rate (ε=0.95) makes convergence unlikely; no convergence analysis is provided.** With ε=0.95, only 5% of actions (≈150 out of 3000 per agent) use learned Q-values; the remainder are purely random. For the K=100 action space (Figure 2) used in the Nash equilibrium comparison, each action receives roughly 1.5 exploitative updates on average. For the Limbo experiment with K=1000 (Figure 3), the per-action exploitative updates fall to ~0.15 — meaning most actions are never exploited at all. The paper presents no learning curves, Q-value trajectories, or any convergence diagnostic. The "large standard deviation observed for higher k values" (line 176) is far more likely to reflect agents that are still essentially random than the claimed "exploring a wider range of strategies." This undermines both the Nash equilibrium comparison (Section 5) and the Limbo analysis (Section 6).

**2. Limbo experiments rely on arbitrary data manipulations and undefined baselines.** 
- The first experiment removes the "top 700 most popular numbers" and keeps "~1,000 potentially winning numbers" (line 142). No justification is given for these specific thresholds. The "1% chance of winning" baseline is computed from this manipulation, not from any theoretical model.
- The second experiment (line 160) involves further ad-hoc modifications: "we set the best choice to a winning one," "removed the best choices to give a 10% chance of winning," and removed "100 numbers with the fewest selections." The cumulative effect of these manipulations makes the results uninterpretable as evidence about either the Limbo game or the Q-learning method.
- The "theoretical 'agent'" comparison baseline (line 160) is never defined — it is unclear whether this refers to sampling from the Poisson–Nash distribution, the CH distribution, or some other benchmark. A claim of "outperforming" an undefined baseline is not meaningful.

**3. No quantitative comparison to the Nash equilibrium.** The central claim of Section 5 — that Q-learning "successfully emulates the Nash equilibrium" with only "minimal discrepancies" — rests entirely on a visual inspection of Figure 1. No KL divergence, mean squared error, or any statistical test is reported. Given the concerns about convergence (weakness #1), a quantitative measure is essential to substantiate this claim.

### Minor

**1. Missing experimental specifications.** The action space size *K* for the Section 5 equilibrium comparison is not stated. The number of agents used during training is not specified. Whether results come from a single run or multiple independent runs is unclear. These gaps hinder reproducibility and interpretation.

**2. No variance reporting.** If the Q-learning experiment is stochastic, the paper should report the mean and variance of the learned strategy distribution across runs. Without this, it is impossible to assess whether the visual match in Figure 1 is reproducible or a favorable single trial.

**3. Inconsistent action selection description.** The text (line 94) states that softmax is used for exploitation, but the ε-greedy formula (line 97) shows argmax. While softmax with T=0.15 is near-argmax, the specification should be self-consistent.

### Trivial

None.

## Nice-to-Haves

- A convergence analysis (learning curves over episodes, Q-value evolution) would directly address the most serious weakness and strengthen the paper's central claim.
- Ablating ε (testing values like 0.05, 0.1, 0.3) would clarify whether the observed results are robust or artifacts of near-random exploration.
- Comparing against the cognitive hierarchy model, which the paper cites as its natural predecessor (line 39), could provide additional insights, though this is outside the paper's stated scope.

## Removed Points

The following criticisms from the submitted reviews were removed after verification against the paper:

- *"Limbo evaluation does not constitute playing LUPI"* (Harsh Critic point 1) — The counterfactual evaluation (inserting the agent's choice into historical data where other players' choices are fixed) is a valid approach for testing against an empirical distribution. Limbo players place bets independently without viewing others' real-time choices, so the assumption of independent fixed choices is reasonable. The core framing of this criticism overstates the problem. However, the legitimate concerns about data manipulation and undefined baselines (retained above as Major weakness #2) remain.

- *"Missing baseline: cognitive hierarchy model"* (Harsh Critic point 4) — The paper explicitly positions itself as the follow-up to Östling et al.'s CH model suggestion (line 39: "should...be considered an initial step towards a more formal investigation using a learning model"). The CH model is a behavioral model, not a directly comparable baseline that the paper needs to benchmark against. This is a scope-creep criticism.

- *"Comparison to Nash equilibrium is comparing different objects"* (Harsh Critic point 2, framing) — The paper acknowledges (lines 42–43) that fixed-n and Poisson-n equilibria are "nearly identical" in straightforward cases. The comparison is informative even if the two are not exact matches to the same game. The real issue (retained as Major weakness #3) is the absence of quantitative metrics, not the conceptual mismatch.

- *Strength Finder's generic/superficial strengths* — Broad claims about the problem's importance that lacked specific evidence were dropped. The retained strengths are concrete and verifiable from the paper.

## Novel Insights

None beyond the paper's own contributions. The reviews surface no unexpected analytical angles beyond what the paper itself provides.

## Suggestions

1. **Rebuild around a quantitative convergence study.** Train Q-learning agents for multiple fixed *n* and small *K* where the fixed-*n* Nash equilibrium is computable, and report KL divergence or MSE between learned and theoretical strategies. This would directly validate the method.

2. **Redesign the Limbo evaluation.** Either (a) use the agent's expected payoff against the empirical distribution of human choices (marginalizing over rounds) as a well-defined out-of-sample test, or (b) clearly define the theoretical baseline and report the win-rate comparison with proper statistical error bars and justification for any data filtering.

3. **Ablate the exploration rate.** Test ε ∈ {0.05, 0.1, 0.3, 0.5, 0.95} and show convergence curves for each. The current ε=0.95 is pathological for the reported episode count and needs justification or replacement.

4. **Specify all experimental parameters upfront:** action space size *K* for each experiment, number of agents, number of independent runs, and whether results are averaged or from a single run.

MY FINAL SCORE: <score>3.0</score>
MY FINAL DECISION: <decision>Reject</decision>