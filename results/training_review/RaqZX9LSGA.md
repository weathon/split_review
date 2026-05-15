I have thoroughly verified each claim against the paper. Let me now produce the final consolidated review.

---

## Summary

This paper introduces Stochastic Execution-Delay MDPs (SED-MDPs), a formalism for RL with random action execution delays. It proves that Markov policies are sufficient for optimality in this setting (extending Derman 2021's deterministic-delay result), and proposes DEZ, a model-based algorithm built on EfficientZero that uses action/delay queues and a learned forward model to predict future states. Experiments on 15 Atari games with delays M∈{5,15,25} show DEZ outperforms oblivious EfficientZero and Delayed-Q in the vast majority of settings under both constant and stochastic delays.

## Strengths

- **Theoretical result extending Markov policy sufficiency to stochastic delays.** Theorem 2 generalizes Derman's (2021) deterministic-delay result, showing that for any history-dependent policy there exists a Markov policy producing the same conditional process distribution. This justifies searching over the exponentially smaller class of Markov policies, which is a non-trivial generalization.

- **DEZ achieves strong empirical results across diverse Atari games and delay settings.** In 39/45 constant-delay experiments and 42/45 stochastic-delay experiments, DEZ attains the highest average score. The stochastic delay uses a random-walk process without episode reinitialization, which is more realistic than the fixed-initialization approach used in prior work.

- **The algorithm avoids the exponential state-space growth of augmentation.** Standard augmentation yields |S|×|A|^M states; DEZ replaces this with two fixed-length queues (size M) and a learned forward model. This makes the approach practical for delay values up to M=25, whereas prior augmentation methods (bouteiller2020) were tested only with maximal delay 6.

- **Clear formulation of the SED-MDP framework.** The paper defines a rigorous probability space, introduces the effective decision time τ_t (Eq. 1), and derives the process distribution (Theorem 1). These provide a formal foundation that cleanly separates the delay process from the MDP dynamics.

## Weaknesses

### Fatal
None.

### Major

- **The claim that DEZ "yields non-stationary Markov policies" (Contribution 3) is in tension with the algorithm's design and is not adequately reconciled.** DEZ maintains queues of past actions [a_{t-M},...,a_{t-1}] and delays [z_{t-M},...,z_{t-1}] (Section 5). These queues are used to compute "expected pending actions" [â_t,...,â_{t+z_t-1}], which in turn feed the forward model that produces the MCTS input ŝ_{t+z_t}. If these expected pending actions depend on the queues (past decisions), then the policy's input implicitly encodes history, contradicting the Markov claim. The paper does not specify whether the "expected pending actions" are (a) computed from the policy itself (e.g., by rolling out π on predicted states), which would preserve the Markov property, or (b) derived from the action queue, which would make the policy history-dependent. This ambiguity undermines the claimed connection between Theorem 2 and the algorithm. The authors should clarify this mechanism and, if the queues are indeed used to inform the policy, either reconcile or retract the Markov claim.

- **Theorem 2's proof is not verifiable from the main paper and its exact meaning for algorithm design is unclear without it.** While the harsh critic's objection about "conditioning on future delays" is based on a misunderstanding of the probability notation (the conditioning on z̃=z is in the measure, not the policy's input; the quantifier ∃π'∀z is standard), the theorem's correctness depends on a proof deferred to the appendix. Moreover, the theorem conditions on the entire delay sequence z; even if correct, the algorithmic implications — how a Markov policy that works for all possible z sequences can be learned in practice from sampled trajectories with unknown z — are not discussed. The paper would benefit from a proof sketch and a discussion of how the existence result translates into a learning objective.

### Minor

- **Experimental comparison is not fully controlled for step count.** DEZ uses 130K environment steps while EfficientZero (the baseline) uses 100K (Section 6). The paper acknowledges this ("the presence of delay adds complexity… requiring mildly more interactions") but does not run a controlled ablation with DEZ at 100K steps or baselines at 130K steps. A 30% data advantage can inflate relative performance, especially for a sample-efficient method.

- **Only one stochastic delay distribution (a specific random-walk process) is tested.** The paper claims DEZ is "agnostic to the delay distribution" (Contribution 3), but the experiments exclusively use the random walk defined by lines 259–269. Showing robustness to at least one additional distribution (e.g., uniform over [0,M], geometric) would substantiate this claim.

- **The "expected pending actions" are underspecified.** Section 5 says "we take the expected pending actions denoted by [â_t, …, â_{t+z_t-1}]" without explaining what "expected" means here — are these sampled from the policy? Are they the actions already in the queue? Are they an average? This is critical for reproducibility and for understanding whether the forward model prediction is stochastic or deterministic.

- **No uncertainty or significance measures are reported in the main figures.** The bar charts (Fig. 1) show only mean scores; standard deviations and significance tests are deferred to the appendix. While the appendix presumably contains this information, the reader cannot assess which differences are meaningful from the main paper.

### Trivial
None.

## Nice-to-Haves

- Ablation of forward model quality: compare DEZ against DEZ with a perfect (oracle) forward model to quantify the cost of learned prediction errors.
- Error propagation analysis: plot the prediction error of ŝ_{t+z_t} versus true state as a function of rollout length z_t.
- Additional analysis of queue depth sensitivity: how performance varies when the queue length M is mismatched with actual maximal delay.

## Removed Points

These points from the reviews were removed because they are factually incorrect, based on misunderstandings, or violate the review guidelines. They are listed here for completeness but should not be weighted in the evaluation.

1. **"Theorem 2 conditions on future delays, making it unrealistic / allowing the Markov policy to depend on future delays."** — The conditioning on z̃=z is in the probability measure (standard for exogenous processes), not in the policy's input. The Markov policy π' takes only (s_t, z_t) as input. The quantifier structure (∃π' ∀z) means a single policy works for all delay sequences. This criticism misunderstands the theorem's notation.

2. **"DEZ's architecture contradicts the theoretical result."** — Overstated. The algorithm uses queues for practical forward-model prediction. Whether this contradicts the Markov claim depends on how "expected pending actions" are computed, which is ambiguous but not a definitive contradiction. The paper should clarify, but the claim of contradiction is not supported by the available text.

3. **"Missing appendix / missing proofs / missing tables"** — These sections exist in the original submission; the parser strips them from all papers. By the review guidelines, this is not a valid weakness.

4. **"Missing comparison to Karamzade2024"** — That work focuses on continuous control (Mujoco, DMC), which is outside the paper's stated scope. The related work section correctly cites it.

5. **Formatting, grammar, and typo nitpicks.** — These are parser artifacts or too minor to include.

6. **"Delayed-Q forced to compete at 100K steps is unfair."** — The paper acknowledges this (line 245) and frames the comparison as a sample-efficiency argument. This is a valid research positioning, not an unfair comparison.

7. **"No error bars in main text"** — The paper explicitly references appendices containing standard deviations and full tables. While showing error bars in main figures would be better, the information exists in the submission.

## Novel Insights

None beyond the paper's own contributions. The cross-referencing of reviews does not yield a novel insight not already present in the paper's theoretical or empirical findings.

## Suggestions

1. **Clarify the "expected pending actions" computation.** Specify whether these are derived from the action queue (past decisions) or from rolling out the current policy on predicted future states. This is essential for understanding whether DEZ implements a Markov policy or a history-dependent one.

2. **Address the step-count discrepancy.** Run DEZ at 100K steps (matching the EfficientZero baseline) or run all baselines at 130K steps, and report the results. This would address the most significant experimental fairness concern.

3. **Include error bars or confidence intervals in the main bar charts.** If the appendix contains standard deviations, incorporate them into the main figures so the reader can assess significance at a glance.

4. **Add at least one additional stochastic delay distribution** (e.g., uniform over [0,M]) to support the "agnostic to delay distribution" claim.

5. **Provide a proof sketch of Theorem 2** in the main paper, clarifying the construction of π' and why it does not require knowledge of future delays.

## Score and Decision

The paper addresses a realistic and understudied problem (stochastic execution delay) with a principled framework, a meaningful theoretical generalization, and an algorithm that demonstrates strong empirical results. The main weaknesses are: (a) an unresolved tension between the "Markov policy" claim and the algorithm's queue-based forward prediction, (b) an underspecified algorithm component ("expected pending actions"), and (c) experimental controls that could be tightened. None of these are fatal — they require clarification and additional analysis, not a refutation of the core contribution. The theoretical foundation (SED-MDP formalism, Theorem 2 after correcting the quantifier reading) and the strong empirical results on 15 Atari games under two delay paradigms constitute substantive value to the community.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>