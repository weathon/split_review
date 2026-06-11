## Summary

This paper applies Goal-Oriented Environment Inference (GOEI, Takahashi et al., 2024) — a model-based RL method that learns compressed "core" state representations via variational Bayes with Dirichlet processes — to the competitive card game Hol's der Geier. The authors show GOEI reduces 15,542 possible observations to just 452 states (2.9%) while achieving near-optimal performance (median reward rate -0.010) against the Nash equilibrium opponent, substantially outperforming Q-learning and simple heuristic strategies.

## Strengths

- **Extreme state compression (2.9%) with near-optimal performance against NE opponent.** The best GOEI configuration (β=0.2, α=25) yields median 452 states across rounds vs. 15,542 observations, with reward rate -0.010 (Table 1). This is a striking empirical result — the compression factor is large and the performance gap from optimal is tiny.

- **Substantially outperforms Q-learning and all simple heuristic strategies.** GOEI's best median reward rate (−0.010) exceeds Q-learning's best (−0.079 at η=0.20), π₀ (−0.125), and Rand (−0.527). Learning curves (Figure 2A) show GOEI reaching near-zero reward within ~500 epochs while Q-learning remains negative even after 2,000 epochs.

- **Systematic hyperparameter ablation with plausible mechanistic explanations.** The paper varies β (Dirichlet prior concentration) and α (Dirichlet-process concentration) across nine combinations (Table 1) and explains their effects: small β accelerates learning but causes instability; large α enhances exploration but slows learning. These claims are supported by learning curves in Figure 4.

- **Principled information-theoretic analysis (Section 4.2, Figure 3).** The mutual information analysis shows which individual features are preserved vs. discarded (e.g., score difference preserved at round 4 where it becomes critical; agent/opponent hand information almost entirely reduced throughout).

- **Solid empirical methodology.** 21 random seeds with quartile reporting, separate training and test sets, careful hyperparameter search.

## Weaknesses

### Fatal
None.

### Major
- **Single-opponent evaluation limits the "core states" claim.** GOEI is trained on games between Rand and the NE opponent, and tested only against that same NE opponent. This makes the evaluation equivalent to computing a best response to a known opponent behavior that was observed during training. The paper frames the discovered states as "core" states of the game (Section 2.2: "If an agent based on a reduced state representation could compete equally well against the NE opponent, then the agent is considered to have successfully learned core information to win the game") but provides no evidence that these states would generalize to other opponents (e.g., π₀, π₂, or a different mixed strategy). Testing against even one additional opponent strategy would substantially strengthen the claim that the compression captures intrinsic game structure rather than opponent-specific patterns.

### Minor
- **The headline metric (average reward rate across all 3,000 epochs) systematically understates GOEI's converged performance.** Because GOEI starts negative and improves, the full-run average is lower than final-epoch performance. Fixed baselines (NE, π₀, Rand) have constant performance and are unaffected. Table 1 should also report final-epoch or last-N-epoch performance for a cleaner comparison.

- **Inconsistent measurement time in Table 1.** Reward rate is averaged across epochs 1–3,000, but state representation size is measured at epoch 3,000. These should be aligned.

- **Framing mismatch on explainability.** The Introduction motivates GOEI as addressing the explainability problem of deep RL, but the paper cannot "give a verbal explanation of the reduced state representation more concretely than Figure 3" (Section 5, acknowledged honestly by the authors). The mutual information analysis shows what is *discarded*, not what the compressed states actually represent or how they can be interpreted. The result — dramatic compression with maintained performance — is interesting on its own; the explainability framing creates an unmet expectation.

- **No statistical test for "indistinguishable" from NE.** The quartiles for the best GOEI configuration [-0.012, -0.010, -0.009] are consistently negative with no overlap with 0. The paper characterizes this as "indistinguishable from the optimal one (≃0)" (line 228) without a statistical test. Given all 21 seeds show negative reward rates, the true mean is almost certainly below 0, even if very close.

- **"Significantly more epochs" claim (Section 4.1) lacks a quantitative convergence-speed comparison.** The visual difference in Figure 2A is clear, but the wording implies a formal comparison.

### Trivial
- None beyond the minor points above.

## Nice-to-Haves
- Add a simple state-ablation baseline (e.g., Q-learning on a coarsely bucketed observation space) to distinguish whether the benefit comes from state reduction in general or GOEI's specific algorithm.
- Deeper analysis of what the compressed states encode (e.g., examining which observations map to the same compressed state and whether the equivalence classes are interpretable).
- Test against multiple opponents to support the "core states" framing.
- Report final-epoch reward rate alongside the full-run average.
- Add a bootstrap confidence interval or similar test for the claim that performance is indistinguishable from NE.

## Removed Points
*These points were flagged by the reviewers or the filtering process but are removed from the main review. Treat with caution.*

- **"The relationship between 28,477 and 15,542 observations is not explained"**: Factually wrong. The paper explicitly states on line 134 that the restriction to 15,542 is "because of action sequences never caused by the NE strategy."
- **"Comparison to Q-learning structurally limited because it does not isolate state reduction"**: The paper's contribution is demonstrating GOEI's effectiveness in this domain; the Q-learning baseline is a reasonable model-free comparison. A state-ablation baseline would strengthen the paper but its absence is not a structural flaw — the paper does not claim to be a controlled study isolating state reduction.
- **"Limitation about separating inference and optimization is more consequential than discussed"**: The paper already discusses this limitation in Section 5. Separating inference from optimization is a standard experimental choice for evaluating inference methods and is honestly acknowledged.
- **Formatting/style nitpicks and parser artifacts**: Removed per instruction.

## Novel Insights
None beyond the paper's own contributions. The paper is a clean empirical application of an existing method to a new domain.

## Suggestions
1. **Test against at least one additional opponent** (e.g., π₀ or a randomly sampled mixed strategy). If performance holds, the "core states" claim is substantially strengthened. If it collapses, the paper should reframe its claims as best-response learning rather than core-state discovery.
2. **Report final-epoch or last-N-epoch reward rate** in Table 1 alongside the full-run average for a cleaner comparison to the NE baseline.
3. **Add a simple bootstrapped confidence interval** to support the claim that GOEI's performance is "indistinguishable" from the NE optimum.
4. **Either deliver on or de-emphasize the explainability framing.** The compression result is interesting without it.

## Score and Decision

**Round 1 bracket:** 4.0–6.0 (the paper is clearly stronger than the 1.67–3.0 papers which have fundamental flaws, and clearly weaker than the 8.0 papers which introduce novel algorithms with extensive evaluation).

**Round 2 narrowing:**
- 5.25 (Optimal Action Abstraction, Reject) — Novel algorithm with mixed reviews; my paper has less novelty but cleaner execution. Slightly weaker overall.
- 5.75 (Efficient Online Pruning, Accept) — Novel method with strong empirical results on poker; my paper is weaker on novelty and scope.
- 5.00 (Constrained Exploitability Descent, Reject) — Novel algorithm with theory; comparable quality level with different trade-offs.
- 4.75 (Tree Search for Simultaneous Move Games, Reject) — Strong results but soundness concerns flagged; comparable quality.
- 4.75 (Learning Abstract World Models, Reject) — Theoretically motivated but weak experiments; my paper has cleaner empirics.
- 4.00 (KrwEmd, Reject) — Practical algorithm but weaker results; my paper is stronger.

**Final score:** 5.0. The paper is a well-executed empirical validation with a genuinely striking compression result. However, the contribution is significantly limited by (a) applying an existing method with no algorithmic novelty, (b) single-opponent evaluation, and (c) narrow scope (one game). These limitations prevent it from meeting the acceptance bar at this venue. The core empirical finding is worth reporting, and the gap to a stronger paper is modest.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>