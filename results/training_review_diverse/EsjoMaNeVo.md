Now I have all the information needed to produce the final consolidated review.

---

## Summary

This paper studies whether a benevolent mediator can steer no-regret-learning agents toward desirable (welfare-optimal) equilibria using nonnegative payments that vanish on average. It provides a systematic characterization across feedback models for extensive-form games: a positive result under full feedback (Theorem 5.2), an impossibility for bandit feedback with bounded per-iteration payments (Theorem 5.4), a positive result for bandit feedback with time-dependent payments (Theorem 5.6), and an online algorithm that learns while steering (Theorem 6.5). The paper also extends these results to a broad class of equilibrium concepts via mediator-augmented games.

## Strengths

- **Comprehensive possibility/impossibility characterization across feedback models.** The paper systematically maps out when steering is and is not possible under different informational assumptions (full feedback, bandit with bounded payments, bandit with time-dependent payments) for general extensive-form games, going well beyond prior work restricted to normal-form games or assuming player obedience. Theorems 5.2, 5.4, and 5.6 together form a coherent picture.

- **Novel information-theoretic lower bound for bandit steering.** Theorem 5.4 proves that constant per-iteration payments are fundamentally insufficient to steer players to the welfare-optimal equilibrium under bandit feedback in extensive-form games, even when players have zero regret. This impossibility result cleanly separates extensive-form steering (hard) from normal-form steering (easy) and is supported by an intuitive construction (Figure 2).

- **Unification of multiple equilibrium concepts via mediator-augmented games.** The framework in Section 6 shows how the steering algorithms extend to EFCE, communication equilibrium, mechanism design, and Bayesian persuasion, demonstrating broad applicability beyond pure Nash equilibria. This is a genuine conceptual contribution that links the steering literature to mechanism design and information design.

## Weaknesses

### Fatal
None.

### Major

- **The online steering algorithm's guarantee is not fully supported as stated.** Theorem 6.5 sets λ = |Z|²ᐟ³ε⁻¹ᐟ³ and produces a bound of 7λ*|Z|⁴ᐟ³ε¹ᐟ³, where λ* is the game-dependent threshold from Proposition 6.3 (Zhang et al., 2023). Proposition 6.3 guarantees that the max-min formulation characterizes optimal equilibria only for λ ≥ λ*. Since λ* is game-dependent, unknown to the mediator, and could be arbitrarily large, there is no guarantee that the chosen λ satisfies λ ≥ λ*. If λ < λ*, the Lagrangian formulation may no longer characterize optimal equilibria, and the convergence guarantee to an optimal equilibrium is unsupported. The bound's dependence on λ* further suggests the analysis assumes λ ≥ λ*. The paper does not address this gap — e.g., via a doubling schedule for λ or an explicit bound on λ* in terms of game parameters. Since online steering is prominently featured as a contribution, this is a significant unresolved concern. *(Note: this does not affect the offline results — Theorems 5.2, 5.4, 5.6 — or the lower bound.)*

### Minor

- **Experiments use a full-feedback player algorithm (CFR+) to illustrate bandit steering.** The bandit model (Definition 5.3) assumes players only observe the terminal node, but CFR+ is a full-feedback algorithm that requires counterfactual values at all infosets. The experiments therefore test steering under a *richer* informational regime than the bandit model permits. The paper does not acknowledge this discrepancy. The results remain useful as a proof-of-concept for the mediator's payment scheme, but they should not be interpreted as evidence for the bandit setting.

- **Limited experimental evaluation.** Only two games are shown (both involving EFCE). There are no error bars, no comparison to baselines, and the hyperparameters use a dynamic heuristic for α rather than the theoretical formulas from Theorem 5.6. The statement "a small constant P is enough" is interesting but is not explained by the theoretical framework, which requires P to grow with T.

- **The paper mentions "advice" as a mediator tool but the algorithms do not use it.** The introduction states the mediator can "offer advice" (Section 1), but all algorithms steer exclusively through payments. This is a minor inconsistency — either advice should be used substantively or the mention should be removed/qualified.

- **Proposition 3.2 (lower bound on finite budget) is stated without proof sketch or intuition.** The reader cannot evaluate whether the construction is tight or whether it relies on pathological features of the game.

### Trivial
- Table 1 hides game-dependent constants (|Z|¹ᐟ², |ℐ|¹ᐟ²) that vary across rows without explanation in the caption about which constants are shown versus hidden.

## Nice-to-Haves

- The paper could acknowledge that the mediator's knowledge of the regret bound R(T) and time horizon T is idealized, and note how these could be estimated or bounded by worst-case guarantees of common algorithms (CFR, IXOMD, etc.).
- A brief proof sketch for Proposition 3.2 would improve readability.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *"The bandit-derived payments are multilinear, not just linear in one and continuous in the other"* — This is factually correct but not a weakness: multilinearity is a *stronger* condition than the requirement (linear in x_i, continuous in x_{-i}), so the bandit payments satisfy the definition. No issue here.
- *"The strong informational assumptions limit practical applicability"* — The paper is transparent about these assumptions (full strategy observation in full feedback, knowledge of T in bandit). These are inherent to the theoretical framing, not oversights.
- *"Theorem 5.6 proof sketch is insufficient without the appendix"* — The appendix was stripped by the parser; in the original submission, the full proof exists there. Providing only a high-level sketch in the body is standard for theoretical papers.
- *"Missing discussion of k-implementation beyond normal form"* — This scope creep asks the paper to also cover a different line of work in detail, which would be a different paper.
- *"The paper should provide more proof structure for Theorem 5.6"* — The paper explicitly notes the proof is more involved and explains *why* it's nontrivial (the chicken-and-egg problem). This is appropriate for a theory paper with proofs in the appendix.

## Novel Insights

The reviews surface an interesting structural observation that the paper itself underplays: the bandit lower bound (Theorem 5.4) and the bandit positive result (Theorem 5.6) together reveal that extensive-form steering requires either "observing the unobserved" (full feedback) or "paying for off-path deviations at rates that make payments vanish only polynomially" (bandit with time-dependent payments). This tension between information and budget — you either need to see what players *would* do or pay them enough at rarely-reached nodes — is a genuinely new insight not present in the normal-form literature. The online steering gap (λ issue) suggests that learning the equilibrium *while* steering introduces yet another layer of difficulty that may require adaptive λ schemes.

## Suggestions

1. **Fix the λ issue in the online algorithm.** The cleanest resolution is to use a doubling schedule for λ (start small, double periodically, replay data) so the algorithm is adaptive and does not need to know λ* upfront. Alternatively, prove an explicit bound on λ* in terms of game parameters (e.g., |Z|, payoffs) and set λ to exceed it. Without this fix, the online steering claim is unsupported.

2. **Acknowledge the CFR+/bandit gap in the experiments.** Explicitly state that the players use CFR+ (a full-feedback minimizer), so experiments test steering under richer player information than the bandit model assumes. This does not weaken the results but prevents misinterpretation.

3. **Provide intuition or a structured sketch for Proposition 3.2.** Even a paragraph explaining the key construction (what game, how players can force unbounded payments or bad convergence) would help.

4. **Either use advice substantively or remove the mention** from the list of mediator tools in Section 1.

## Score and Decision

The paper's core contributions — the offline characterization across feedback models, the bandit lower bound, and the unification of equilibrium concepts — are solid and interesting. However, the online steering result (Theorem 6.5) has a structural gap concerning the choice of λ relative to the unknown λ*, which is not addressed. Since online steering is presented as a main contribution, this weakness is significant enough to prevent acceptance in the current form. With the λ issue resolved (e.g., via a doubling schedule) and minor experimental transparency improvements, the paper would be a valuable contribution.

**Score: 5.0**

**Decision: Reject**

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>