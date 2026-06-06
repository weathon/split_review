## Summary

This paper applies Goal-Oriented Environment Inference (GOEI) — an existing variational Bayesian state-reduction algorithm introduced by Takahashi et al. (2024) — to the competitive card game Hol's der Geier. The main result is that GOEI discovers a 452-state representation (2.9% of the 15,542 reachable observations under the training distribution) while achieving near-Nash equilibrium performance, substantially outperforming tabular Q-learning. The paper is a validation study extending GOEI from an abstract environment to a more realistic competitive setting.

---

## Strengths

- **Quantitative demonstration of near-Nash performance with extreme compression**: Table 1 (best parameters β=0.2, α=25) shows median reward −0.010 vs. NE's 0.000, with 452 total states across rounds (5+8+31+408) against 15,542 reachable observations. Figure 2A confirms rapid convergence to this near-optimal level. The compression result is concrete and internally consistent.

- **Clear superiority over Q-learning baseline in the same data regime**: Best Q-learning achieves a median reward of only −0.079 (Table 1), never approaching the NE level even with tuned learning rates (η=0.05–0.50). The performance gap is large and consistent, providing strong evidence that state reduction is the decisive factor.

- **Informative hyperparameter sensitivity analysis**: Section 4.3 and Figure 4 systematically vary α (Dirichlet process) and β (Dirichlet distribution) across 9 combinations, with principled reasoning about why small β accelerates but destabilizes learning, and why large α enhances exploration at the cost of slower convergence. The analysis matches the observed outcomes.

- **Information-theoretic dissection of retained information**: Figure 3 reveals a non-trivial pattern: CT and RT information is preserved at early rounds, SD becomes important only at round t=4 (as the game approaches its terminal state), and AH/OH are almost entirely discarded. This partial structural account of the learned representation goes beyond a black-box success metric.

---

## Weaknesses

### Fatal
None.

### Major

- **Framing gap between the stated RL motivation and the actual experiment**: The introduction and abstract motivate GOEI as a solution for "online learning to adapt to opponents" in environments with "overwhelming observations." However, Section 3.3 describes a purely offline training protocol: GOEI is trained on a fixed dataset of games between two frozen strategies (Rand vs. NE) and then evaluated by running the Bellman equation on the inferred static model. This is model-based planning on a fixed-opponent distribution, not interactive RL. Section 5 explicitly concedes: *"environment inference and strategy optimization may interfere with each other… The effectiveness of the GOEI function in interactive learning should be further confirmed."* The gap between motivation and experimental design is substantial and is not a minor caveat — the entire RL and adaptability framing in the abstract and introduction describes a capability that is never actually tested.

- **Weak and uninformative baseline selection**: The only learning baseline is tabular Q-learning, a method provably ill-suited to environments with ~15K states due to sample complexity — its failure is expected, not surprising. No alternative state-abstraction or model-compression methods are compared (e.g., bisimulation-based approaches, POMDP belief compression, or other model-based RL methods). The comparison confirms that GOEI works better than a method guaranteed to fail, but provides no information about where GOEI stands relative to the broader landscape of state-reduction methods.

### Minor

- **XAI goal is stated but not delivered**: The paper's opening motivation includes explainability as a key driver, and the mutual information analysis in Section 4.2 is presented within that framing. However, Section 5 honestly admits: *"we could not give a verbal explanation of the reduced state representation more concretely than Figure 3."* The XAI motivation is not fulfilled — state reduction is achieved, but interpretable explanation of *what* the core states represent is not.

- **Compression figure is relative to the restricted training distribution, not the full game**: The paper's Section 2.1 states the game has 28,477 possible total observations; Section 3.3 clarifies that under Rand vs. NE games, only 15,542 are reachable. The headline "2.9% (452/15,542)" is computed over the restricted distribution, not the full observation space. The abstract explicitly uses "15,542" as the denominator, so this is technically accurate, but the framing in Section 5 ("2.9% of the number of observations") does not flag that this denominator is itself already restricted. If GOEI operated interactively in the full game, the compression ratio would be different (452/28,477 ≈ 1.6%, and more importantly, generalization to unseen states would be untested).

- **Hyperparameter selection not acknowledged as model selection on the evaluation criterion**: Table 1 presents 9 GOEI parameter combinations, the best (*0.2, 25) is starred and used throughout. The procedure of selecting the best configuration by median reward and reporting that configuration's result is a form of model selection on the test metric, but this is not discussed. The table does transparently report all 9 results, which partially mitigates this concern.

### Trivial

- **"Equivalent to Nash equilibrium" slightly overstates**: The abstract writes "a nearly optimal strategy equivalent to the Nash equilibrium," but the best median reward is −0.010 vs. NE's 0.000 — these are very close but not identical. "Nearly equivalent" or "statistically close to" would be more precise.

---

## Nice-to-Haves

- **Generalization test across opponent strategies**: Train GOEI on Rand vs. NE data, then evaluate its frozen model against a different opponent (e.g., π₂ or π₃). If the 452 core states truly capture essential game structure rather than just summaries of the Rand-vs-NE distribution, performance should transfer. This test is within the existing experimental framework and would directly support the "core" framing.

- **Alignment with theoretically minimal state partition**: Section 3.3 already computes NE states as a byproduct. Comparing GOEI's 452-state representation structurally to the NE-derived state partition (reported in Table 1 as 247+945+69 = 1,261 states across rounds 2–4) would sharpen the claim about what "core" means. At rounds t=2 and t=3, GOEI actually uses *fewer* states than NE (8 and 31 vs. 247 and 945 respectively), which is notable and deserves closer analysis.

- **Wall-clock timing or computational cost**: The paper mentions GPU memory constraints (RTX 4080 SUPER, 12GB) but provides no timing information. Since GOEI is iterative variational inference running for up to 50 iterations per epoch over 3,000 epochs, reporting training time would help assess practical tractability.

---

## Removed Points

*These points are flagged to be removed — treat them with caution:*

- **"Fatal: GOEI is never exposed to the exploration-exploitation feedback loop that constitutes actual reinforcement learning"** (Harsh Critic): Demoted from fatal to major. The paper is transparently honest about this limitation in Section 5 and never claims to have tested interactive RL — it explicitly scopes the experiment to pure environment inference evaluation. The experiment is internally valid for what it actually measures; the problem is the overclaiming in the framing, not a methodological deception.

- **"The 2.9% figure is technically accurate but misleading"** (Harsh Critic): Removed as a standalone weakness. The paper defines 15,542 as its reference population in Section 3.3 and uses it consistently. The distinction from 28,477 is stated in Section 2.1. While a reader could be confused, the paper provides the necessary information; this is a minor clarity issue, not a data framing problem.

- **"Clean evaluation design that isolates inference from strategy optimization" as a strength** (Strength Finder): This was simultaneously claimed as a strength (clean isolation) and a major weakness (never testing interactive RL). The weakness wins: the isolation is a consequence of not testing what the paper claims to motivate, not a deliberate design virtue.

- **Generic strengths about problem importance** (Strength Finder: "improve explainability by reducing state representations"): Removed as insufficiently specific to this paper's contributions.

---

## Novel Insights

The information-theoretic dissection in Section 4.2 / Figure 3 offers the most genuinely novel observational insight: GOEI's core discards virtually all AH (agent's remaining hand) and OH (opponent's remaining hand) information while retaining CT (current table card), RT (remaining table cards), and — crucially only at round t=4 — SD (score difference). This ordering aligns with an intuitive but nontrivial account of game dynamics: in early rounds the current and future prize cards matter more than hand configurations; the score differential only becomes decisive when fewer prizes remain. That this structure emerges from unsupervised state reduction rather than hand-coding is the paper's most interesting empirical observation, even if the authors are honest that they cannot verbalize it more concretely.

---

## Suggestions

1. **Reframe the contribution accurately**: The paper is a model-learning-and-planning study, not an RL study. Rewriting the abstract and introduction to position GOEI as a method for compressed model-based planning from fixed-strategy data (a meaningful contribution) would remove the gap between claim and experiment.

2. **Add at least one alternative baseline from the state-abstraction literature**: Any method that also reduces the state space for planning — even a simple bisimulation-based aggregation or a factored MDP approach — would make the comparison informative rather than confirmatory.

3. **Run the generalization experiment** (train on Rand vs. NE, test frozen model on π₂ vs. π₃ or an arbitrary opponent): This is the single most impactful experiment that can be done within the existing setup and would determine whether the learned core states are game-intrinsic or distribution-specific.

4. **Be explicit about the model-selection procedure**: Acknowledge in the main text that Table 1 stars the best hyperparameter combination identified by median reward, and discuss whether the ranking is stable across seeds.

---

## Score and Decision

**Originality**: Low — the method (GOEI) is from a prior paper; this is a domain validation.
**Importance**: Moderate — game AI and state abstraction are active areas; near-Nash performance with extreme compression is an interesting empirical finding.
**Claims supported**: Partially — the compression and near-Nash performance claims are well-supported, but the RL adaptability framing is not tested.
**Soundness**: Moderate — the experiment is internally valid for what it measures, but what it measures is narrower than what is claimed.
**Clarity**: Moderate — generally readable, but the XAI and online-RL framing is inconsistent with the actual methodology.
**Community value**: Limited — the result is real but narrow, and the absence of alternative baselines limits its informativeness.

The paper's core finding is genuine but modest: a Bayesian state-reduction algorithm, previously validated in abstract settings, also reduces states dramatically in a simple card game while achieving near-Nash performance under an offline training regime. This is a real contribution. However, the RL/XAI framing overclaims significantly, baselines are weak, and the experiment does not test the motivating scenario. For a venue like ICLR, a validation paper needs either a stronger framing match or substantially richer comparison; neither is present here.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>

<subscores>
<originality>2</originality>
<importance>3</importance>
<claims_supported>2</claims_supported>
<soundness>3</soundness>
<clarity>3</clarity>
<community_value>2</community_value>
</subscores>