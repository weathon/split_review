Now let me run the calibration search to score the paper appropriately.Now I have sufficient information to write the final review.

## Summary
This paper introduces Dig-DEC (dual information gain decision-estimation coefficient), a model-free complexity measure that removes the optimism mechanism of prior work [FGQ+23] and instead drives exploration purely through KL information gain. The paper proves that Dig-DEC is always at most optimistic DEC (Theorem 13) and can be strictly smaller (Theorem 14, 3-armed bandit). It applies the framework to hybrid MDPs with stochastic transitions and adversarial bandit reward feedback, yielding the first model-free regret bounds for this setting and resolving an open problem in [LWZ25]. It also improves online function-estimation procedures, achieving constant Est for Bellman-complete MDPs (Theorem 11) and enabling √T regret via DEC for the first time.

---

## Strengths

- **Dig-DEC is provably no larger than o-DEC with a concrete strict separation (Theorems 13 and 14).** Theorem 13 establishes dig-dec ≤ o-dec + η for any D̄. Theorem 14 constructs a concrete 3-armed bandit where the [FGQ+23] algorithm suffers Ω(√T) regret while the proposed algorithm achieves ≤ 1. The separation is mathematically decisive.

- **Resolution of an important open problem in hybrid MDPs.** Table 2 gives the first model-free regret bounds for hybrid bilinear classes and Bellman-complete coverable MDPs with bandit feedback under linear reward. The structural reason — removing optimism eliminates the need for an explicit reward estimator — is clearly articulated in Sections 2.2 and 6.

- **Improved estimation procedures that concretely advance the state-of-the-art.** Section 4.2.1 introduces an unbiased split-sample estimator that improves over [FGQ+23]'s biased estimator, improving Est from T^{3/4} to T^{1/2}. Section 4.2.2 (Theorem 11) achieves Est ≲ log²|Φ|, a constant in T, enabling √T regret via DEC in Bellman-complete MDPs — matching optimism-based approaches [JLM21, XFB+23] for the first time with a DEC-based method.

- **A unified, flexible framework extending AIR.** Equation (2) generalizes the KL-specific AIR of [XZ23] and [LWZ25] to general Bregman divergences, bypassing the "constructive minimax theorem" of [XZ23]. The new analysis connects cleanly to mirror descent (Section 4), is compositional, and recovers prior results as special cases (Appendix C noted in the paper). The paper demonstrates the framework's value by achieving results for bilinear classes, Bellman-Eluder dimension, and coverability in a single sweep.

---

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **The strict improvement of Dig-DEC over o-DEC is demonstrated only for a 3-armed bandit, not for any MDP.** For the stochastic MDP settings in Table 1, the T-dependence improvements (e.g., T^{3/4} → T^{2/3} for bilinear on-policy) derive primarily from the improved estimation procedures (Theorem 7 and Theorem 11), not from dig-dec being numerically smaller than o-dec in those settings. Section 6 explicitly states this — the KL information-gain term enables strict improvement, but the only concrete demonstration is Theorem 14 for a bandit. An MDP-level example where dig-dec is parametrically smaller than o-dec would substantially strengthen the paper's headline claim about Dig-DEC as a complexity measure rather than as just a different proof technique.

- **The hybrid setting results are limited to known linear reward features (Assumption 4).** The paper acknowledges this explicitly in Section 3.2 and the footnote following it — the unknown-feature case of [LMWZ24] is out of scope because partitioning under Assumption 3 would inflate log|Φ| polynomially. This is an honest and well-explained limitation, but it constrains the "first model-free bandit hybrid MDP bounds" claim to a specific reward regime that should be foregrounded more prominently in the abstract and introduction.

### Trivial

- The term "model-free" is used differently here (regret independent of |M|) from common RL usage (no model is learned). The paper correctly clarifies this in Section 1, but the distinction could be flagged earlier given how prominently the term appears in the title and abstract.

---

## Nice-to-Haves

- A structured MDP example (beyond the 3-armed bandit) where dig-dec is parametrically smaller than o-dec would move the Dig-DEC contribution from "strictly better in a bandit" to "strictly better in MDPs," which is the paper's primary domain.
- A brief worked example tracing through Table 2's regret bound for a simple linear MDP with adversarial rewards would help readers independently verify the hybrid-setting rates and understand their dependence on H, d, and |A|.
- For the hybrid setting, a short paragraph explaining mechanically *why* the absence of optimism avoids the need for an explicit reward estimator — beyond the one sentence in Section 2.2 — would improve accessibility.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

1. **Table 2 superlinear T-exponents (T^{3/2}, T^{13/8}) as genuine errors.** The harsh critic notes entries like T^{3/2} and T^{13/8} in Table 2 appear superlinear. However, the off-policy bilinear★ entry correctly shows T^{1/2} (sublinear), and back-of-envelope computation with the dig-dec = (H^5 d^3 η)^{1/2} formula and Est ≈ d log|Φ| T^{1/2} yields a T^{5/6} optimal rate — not T^{3/2}. These are parser artifacts corrupting fractional exponents (common when PDF fractional exponents are extracted as text). The underlying framework in Section 4 is internally coherent. REMOVED per the rule on parser/formatting artifacts.

2. **Abstract T-exponent inconsistencies (T^{5/6} → T^{7/8} as "improvement", T^{3/5} in abstract vs T^{2/3} in Table 1).** The abstract says "improving from T^{5/6} to T^{7/8} (off-policy)" which would be a regression, and claims T^{3/5} while Table 1 shows T^{2/3}. These are parser artifacts corrupting fractional exponents. REMOVED per the rule on formatting artifacts.

3. **"Est from √T to T^{1/2}" in Section 4.2.1 being identical.** The paper reads "improves their rate of Est from √T to T^{1/2}" — these are identical. This is a parser artifact where a fraction like T^{3/4} was corrupted to √T or T^{1/2}. REMOVED per parser artifact rule.

4. **"Model-free" terminology as a significant flaw.** The paper explicitly defines its use of the term in Section 1. This is at most a minor presentation choice, not a substantive weakness. REMOVED as addressed.

5. **Criticisms about missing appendix proofs and undisclosed hyperparameters.** The parser strips appendices. REMOVED per hard rules.

---

## Novel Insights

The paper's most conceptually interesting observation — articulated in Section 6's decomposition of the KL term into a regularization component (KL(ν_φ, ρ)) and a Shannon information-gain component (E[KL(ν_φ(·|π,o), ν_φ)]) — explains why the removal of optimism is mechanically possible in the DEC framework: regularization alone recovers o-dec bounds, while information gain allows strict improvement. Crucially, the removal of optimism is not just a mathematical simplification; it is the structural property that enables handling adversarial reward feedback without constructing explicit reward estimators. This insight cleanly connects two previously separate threads (model-free learning in stochastic MDPs and hybrid MDPs with adversarial rewards) and may generalize to other settings where optimism-based approaches are blocked by adversarial components.

---

## Suggestions

1. Add an MDP-level separation example (even simple, e.g., a contextual bandit or small linear MDP) where dig-dec is provably smaller than o-dec, to supplement Theorem 14.
2. Promote the "known linear reward feature" scope restriction (Assumption 4) to the abstract, alongside the claim of "first model-free bandit hybrid MDP bounds."
3. In the introduction's bullet on T-dependence improvements, clarify which improvements come from Dig-DEC being smaller vs. from improved estimation procedures — the distinction is currently blurred.

---

## Calibration Against Anchors

**Round 1 anchors:**
- L143pPpIHv (3.0, Reject): RL curiosity paper — far below this paper in rigor
- 2h3m61LFWL (4.25, Reject): VBMLE linear MDPs — narrower scope, less contribution
- en3NwykrHW (5.5, Reject): Trajectory-feedback RL minimax regret — single contribution, weaker theoretical framework
- nIEjY4a2Lf (6.0, Accept): Misspecified Q-learning tight bounds — solid but narrower scope than this paper
- stUKwWBuBm (8.0, Accept): Multi-agent RL behavioral economics — similar theoretical ambition

**Initial bracket: 6–8**

**Round 2 anchors:**
- aPNwsJgnZJ (6.0, Accept): Horizon-free adversarial linear mixture MDPs — resolves one open question, single technique; this paper is broader with multiple contributions
- 8eNLKk5by4 (6.0, Accept): Optimal strong regret CMDP — resolves an open problem with policy optimization, similar tier but narrower
- 0oWGVvC6oq (6.5, Accept): Bits and Bandits regret-information tradeoff — information-theoretic framework, comparable depth; this paper has broader MDP applications
- R4q3cY3kQf (6.75, Accept): MaxInfoRL — empirical information-gain framework, shallower theory

**Comparison:** The paper under review is comfortably stronger than the 6.0 anchors in scope and ambition (multiple simultaneous contributions, resolved open problem, new complexity measure). It is comparable to or slightly stronger than the 6.5 anchor. The strict limitation that Dig-DEC's improvement over o-DEC is shown only for bandits (not MDPs) in the stochastic regime tempers the score from a potential 7.5.

**Final score: 7.0**

---

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>