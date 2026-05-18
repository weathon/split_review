Here is my consolidated review:

## Summary

This paper proposes Successor Feature Matching (SFM), a non-adversarial inverse reinforcement learning method that directly optimizes a policy to match the expert's successor features via policy gradient descent. The key idea is to exploit the linear factorization of returns as inner products of successor features and reward weights, then define an actor loss that minimizes the ℓ₂ gap between the agent's and expert's expected successor features. SFM works with state-only demonstrations (no action labels needed), learns base features jointly during training, and integrates as a drop-in replacement for the actor loss in standard deterministic policy gradient algorithms. Empirical results on 10 DMC tasks with single demonstrations show SFM outperforming both adversarial state-only methods (MM, GAIfO) and non-adversarial methods requiring expert actions (IQ-Learn, BC), with notable robustness to weaker policy optimizers.

## Strengths

- **Strong empirical performance across a standardized multi-task benchmark.** SFM achieves a 16% improvement in mean normalized return over the next best baseline (Fig. 1) with 95% bootstrap confidence intervals across 10 seeds. Per-task learning curves (Fig. 2) and Rliable plots (Fig. 3) consistently show SFM exceeding all baselines on most tasks.

- **First non-adversarial state-only IRL method with an imitation gap bound.** Proposition 3 shows that if the ℓ₂ error between agent and expert successor features is bounded by ε, the imitation gap for any linear reward in the learned feature space is at most Bε. This provides a principled justification for feature matching as an IRL objective, unlike adversarial methods that lack such direct error propagation bounds.

- **Robustness to weaker policy optimizers, unlike adversarial baselines.** When switching from TD7 to the weaker TD3 optimizer, SFM's performance remains nearly unchanged (Fig. 5), while MM and GAIfO degrade severely (Fig. 6). This is a concrete practical advantage for deployment on resource-limited systems.

- **Effective imitation from a single state-only demonstration without expert actions.** SFM achieves higher normalized returns than IQ-Learn and BC (both of which require expert actions) while operating on state-only demonstrations. The ablation over Random, IDM, FDM, and Hilbert features (Fig. 7) demonstrates flexibility in base feature learning.

## Weaknesses

### Major

- **Proposition 1 (telescoping sum) is technically incorrect for arbitrary off-policy replay buffers as stated.** The proposition claims that for *any* replay buffer ℬ containing transitions from arbitrary stationary Markovian policies, the expected successor feature under the current policy's initial-state distribution equals an expectation over buffer transitions without any correction term. This equality only holds when the buffer's state-transition distribution matches the on-policy occupancy measure d^π (or with importance weighting). Standard off-policy RL methods face the same distribution mismatch, but they do not present it as a provable equality — they treat it as an approximation. Since the actor loss (Eq. 11) and gradient (Proposition 2) are derived directly from this claimed equality, the paper's central theoretical justification is overstated. The paper later uses the word "approximates" (line 216), which is at odds with the proposition's claim of exact equality. **Why this matters:** This does not invalidate the empirical results — the method clearly works — but it undermines the paper's framing of a "principled reduction" of IRL to direct policy optimization. The authors should either (a) restrict the proposition to on-policy or near-on-policy settings, (b) derive a corrected loss with importance weights, or (c) explicitly recast it as an off-policy approximation that is standard in actor-critic methods and discuss the error.

### Minor

- **The imitation gap bound (Proposition 3) assumes the expert is optimal for a *linear* reward in the learned features — this is not guaranteed.** The bound requires that the expert's true reward be representable as r(s) = w^⊤φ(s) within the feature class induced by the learned φ. The paper acknowledges this limitation (lines 130–131) and argues that diverse learned features may be rich enough, but this is an empirical claim without theoretical support. The presentation gives the impression that Proposition 3 fully justifies the method, when in fact the bound's applicability depends on an unverified assumption.

- **The coupled training of base features, SF network, and actor creates non-stationary targets.** The expert SF estimate ψ̂ᴱ is updated via EMA as φ changes (lines 179–181). This means the "expert features" the actor aims to match drift over time. The paper acknowledges this and uses EMA to mitigate it, but provides no analysis of how this coupling affects convergence or whether it introduces bias. A clear ablation separating offline-pretrained features from online-coupled training would strengthen the paper.

- **Overclaiming in the statement that SFM is "the *only* online method capable of learning from a single unlabeled demonstration without requiring an expensive and difficult-to-stabilize bilevel optimization" (line 59).** This is a very strong claim that would need a thorough literature survey to substantiate. The paper should qualify this (e.g., "to our knowledge") or provide direct evidence that no prior non-adversarial state-only method exists.

### Trivial

- **Proposition 2 (actor gradient) is a straightforward application of the chain rule to Eq. (11) via the deterministic policy gradient theorem.** It does not contain a new theoretical insight; labeling it as a separate "proposition" inflates the technical contribution. It could be stated as a standard derivation without special emphasis.

- **No discussion of the bias from truncating expert demonstrations.** Equation (7) uses a single truncated demonstration (1000 steps) to estimate ψ̂ᴱ. The bias from truncation and variance from a single trajectory are not discussed, even though this estimate is central to the objective.

- **The critic's point about comparing against MM and GAIfO with careful tuning is noted**, but the paper's own results show SFM performs well even with the weaker TD3 optimizer, which mitigates concerns about baseline tuning quality.

## Nice-to-Haves

- An ablation with frozen (offline-pretrained) features to separate the contribution of feature learning from the IRL objective. This would clarify whether the coupled online training is essential or whether features learned offline suffice.
- A discussion of the approximation error introduced by using off-policy replay buffer expectations vs. on-policy occupancy in the telescoping sum, perhaps noting the connection to standard off-policy actor-critic bias.
- An analysis (even heuristic) of why the EMA target for expert SFs does not destabilize learning in practice.

## Removed Points

- **Criticism about Proposition 2 being straightforward**: Kept but downgraded to Trivial — it's a valid observation but not a real weakness.
- **Criticism about baseline tuning (gradient penalties, learning rate decay, OAdam)**: Kept in the Minor section because it's noted as an observation, but the paper's own TD3 robustness experiment already addresses this concern.
- **None of the critics' points were removed for being factually wrong** — the Proposition 1 criticism is correct, just over-stated in severity by the harsh critic. All other criticisms were verified against the paper and adjusted in severity where appropriate.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the tension between the paper's theoretical framing (exact equality in Proposition 1) and the practical reality (off-policy approximation), but this tension is well-understood in the off-policy RL literature and the paper's empirical results speak for themselves.

## Suggestions

1. **Revise Proposition 1** to honestly reflect the off-policy approximation. Either state that it holds exactly when the buffer distribution matches the on-policy occupancy (and note that the paper uses it as an approximation otherwise), or derive a corrected expression with importance weights. This is the single most important fix.
2. **Add an ablation** with frozen, offline-pretrained features to clarify whether the coupled feature+policy training is necessary or whether the IRL reduction stands on its own.
3. **Soften the claim** about being "the only" method (line 59) by adding a qualifier or by providing explicit evidence that no prior non-adversarial state-only method exists.
4. **Discuss the bias/variance** of the expert SF estimate from a single truncated demonstration, and its effect on the imitation gap.

## Score and Decision

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>