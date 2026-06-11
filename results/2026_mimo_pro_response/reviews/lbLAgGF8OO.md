Now I have sufficient calibration data. Let me finalize the review.

**Calibration Analysis:**

Key anchors retrieved:
- "Model-based RL as Minimalist Approach to Horizon-Free and Second-Order Bounds" (avg 7.0, Accept): Similar theoretical RL paper establishing strong bounds. The paper under review has more contributions (framework + estimators + hybrid MDPs).
- "Minimax Optimal RL with Quasi-Optimism" (avg 7.0, Accept): Also about simplifying exploration beyond optimism. More focused (tabular only), while the paper under review addresses a broader framework.
- "Horizon-free RL in Adversarial Linear Mixture MDPs" (avg 6.0, Accept): First results in a specific setting but more incremental than the paper under review.
- "Misspecified Q-Learning with Sparse Linear Function Approximation" (avg 6.0, Accept): Niche contribution, narrower than paper under review.
- "Model-Free, Regret-Optimal Best Policy Identification in Online CMDPs" (avg 5.2, Reject): Good theoretical results but strong assumptions and partial novelty.
- "DEC-POMDPs: Factored Models" (avg 6.17, Reject): Mixed reviews, strong assumptions, no proofs in main doc.

**Round 1 bracket: 6.5–8.0**

The paper under review is clearly at or above the 7.0 anchors due to: (1) more numerous contributions, (2) stronger conceptual novelty (replacing optimism with information gain is a fundamental shift), (3) broad applicability across multiple MDP classes. The weaknesses are genuinely minor — parser-garbled exponents and non-trivial assumptions for the hybrid results that are honestly discussed.

**Round 2 narrowing: 7.0–7.5**

The paper matches or exceeds the 7.0 anchors (EQO, minimalist model-based RL) in breadth and novelty. It doesn't quite reach 8.0 because the hybrid MDP assumptions (Assumptions 3–4) are non-trivial and the strict improvement example (Theorem 14) is a simple 3-armed bandit.

**Final score: 7.5**

## Summary
This paper introduces Dig-DEC, a new model-free decision-estimation coefficient that replaces optimism-based exploration with information-gain-based exploration. It proves Dig-DEC is never worse than optimistic DEC (Theorem 13) and can be arbitrarily better (Theorem 14), improves online function estimation subroutines, and establishes the first model-free regret bounds for hybrid MDPs with adversarial rewards and bandit feedback, resolving an open problem from [LWZ25].

## Strengths
- **Dig-DEC is provably no larger than optimistic DEC with arbitrarily large improvement possible (Theorems 13–14).** Theorem 13 (line 303) establishes dig-dec ≤ o-dec + η, and Theorem 14 (line 307) provides a concrete 3-armed bandit instance where optimistic DEC suffers Ω(√T) regret while Dig-DEC achieves O(1), directly validating the central claim.
- **First model-free regret bounds for hybrid MDPs with bandit feedback (Table 2, Section 5.2).** The paper achieves sublinear regret for hybrid bilinear classes and coverable MDPs with linear reward under bandit feedback, resolving the open problem from [LWZ25]. The key insight (line 305) is that removing optimism avoids explicit reward estimators.
- **Improved online function estimation yields concrete regret improvements (Theorems 7, 11).** The unbiased estimator for average error (Section 4.2.1, splitting samples into two halves) and the redesigned two-timescale procedure achieving Est ≲ log²|Φ| (constant in T, Theorem 11) match optimism-based methods in Bellman-complete MDPs for the first time under the DEC framework.
- **General framework with arbitrary convex divergence D simplifies prior AIR-based analyses (Eq. 2, Section 4).** The analysis via first-order optimality and Bregman divergence (Eqs. 5–6) replaces the "constructive minimax theorem" of [XZ23] restricted to strictly convex divergences, with the paper noting this recovers [XZ23] and [LWZ25]'s results more easily (line 153, Appendix C).
- **Clean conceptual decomposition of information-gain terms (Section 6, line 305).** Decomposing the extra KL term into KL(ν_φ, ρ) for regularization (replacing optimism) and expected KL(ν_φ(·|π,o), ν_φ) for information gain (capturing distributional differences that mean-based divergences miss) provides clear intuition for when the approach improves over optimistic DEC.
- **Broad applicability across canonical MDP settings with explicit rate derivations (Tables 1–2).** The framework is instantiated for bilinear classes, Bellman Eluder dimension, and coverable MDPs in both stochastic and hybrid settings, each yielding concrete Dig-DEC bounds and final regret rates.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
- **Scope of hybrid MDP results relative to framing.** The headline claim of resolving the open problem from [LWZ25] for hybrid MDPs requires Assumption 3 (unique reward-to-value mapping, line 111) and Assumption 4 (linear rewards with known features, line 119). The paper is admirably transparent about Assumption 3's limitation (line 115: for hybrid low-rank MDPs with unknown reward features, log|Φ| scales polynomially vs. [LMWZ24]'s logarithmic scaling). Assumption 4 is also a significant restriction — requiring known linear reward features rules out the unknown-feature case central to recent low-rank MDP work. The abstract appropriately says "under linear reward" but the broader title framing could be sharpened. This is a scope limitation, not a correctness issue.

### Trivial
- **Likely parser-garbled exponents in Table 2 and the introduction.** Several regret entries in Table 2 for hybrid settings appear superlinear (T^{3/2} at lines 291, 293, 295; T^{13/8} at line 292), contradicting the paper's claim of "first sublinear regret" (line 32). Similarly, line 33 in the introduction states T^{3/2}/T^{5/8} and T^{3/2} while the abstract (line 13) states T^{3/4}→T^{3/5} and T^{5/6}→T^{7/8}. These are almost certainly PDF parser artifacts where fractional exponents were garbled. The authors should verify all exponents in Tables 1–2 and the introduction.

## Nice-to-Haves
- A brief in-body sketch of the two-timescale procedure for squared estimation error (Theorem 11, currently described in one sentence at line 243 with details in Appendix F.2) would improve readability for this strong constant-in-T result.
- Theorem 14 demonstrates strict improvement on a 3-armed bandit. An example from a structured MDP class (e.g., a specific bilinear class) where the KL information gain provably helps would strengthen the narrative beyond the simplest possible setting.
- A more precise characterization of which existing settings fall within Assumptions 3–4 and what would be needed to relax Assumption 4 (even a partial impossibility result) would further strengthen the hybrid contribution.

## Removed Points
These points are flagged to be removed, treat them with caution:
- The harsh critic flagged exponent inconsistency as a "critical issue" — partially valid, but the critic themselves acknowledged it's "likely parser artifacts." The paper is not at fault for parser errors. Kept as Trivial for authors to verify.
- The harsh critic flagged "missing appendix details" — the parser strips appendices; they exist in the original submission per hard rules.
- Generic strengths about the problem being important or timely were dropped from the Strength Finder per filtering rules.

## Novel Insights
The key novel insight from reviewing this paper is the conceptual decomposition of Dig-DEC's information-gain terms (line 305): the KL(ν_φ, ρ) regularization term replaces optimism by preventing the marginal distribution from drifting too far from the prior, while the expected KL(ν_φ(·|π,o), ν_φ) term captures distributional differences that mean-based divergences (like squared Bellman error) miss. This decomposition explains both why the approach matches optimistic DEC in stochastic settings (regularization alone suffices, per Theorem 13's proof) and why it fundamentally enables hybrid MDPs with bandit feedback (removing optimism avoids the explicit reward estimator that fails under bandit feedback). The Theorem 14 example concretely demonstrates that the information-gain component can capture signal that optimism-based approaches structurally cannot.

## Suggestions
- Verify all fractional exponents in Tables 1–2 and introduction line 33 to correct parser artifacts before the camera-ready version.
- Add a brief in-body sketch of the two-timescale estimation procedure (Theorem 11) to make the constant-in-T Est bound more accessible.
- Sharpen the framing around hybrid MDP contributions to more precisely delineate which open problems are fully resolved vs. partially resolved given Assumptions 3–4.

## Reporting

**All retrieved anchors across rounds:**

Round 1:
- "KL Divergence Optimization with Entropy-Ratio Estimation for Stochastic GFlowNets" (avg 1.0) — Unrelated, very low quality.
- "An efficient implementation for all pairs minimax path" (avg 1.0) — Unrelated.
- "Variable Forward Regularization to Replace Ridge in Online Linear Regression" (avg 2.0) — Weak online learning paper, rejected.
- "Improved Sample Complexity for Global Convergence of Actor-Critic" (avg 3.0) — Weak RL theory, rejected.
- "Regret measure in continuous time limit for stochastic MAB" (avg 2.33) — Weak bandit theory, rejected.
- "Value-Biased Maximum Likelihood Estimation for Model-based RL" (avg 4.25) — Moderate RL theory, rejected.
- "Model-Free, Regret-Optimal Best Policy Identification in Online CMDPs" (avg 5.2) — Good CMDP results but strong assumptions, rejected.
- "Exploring State and Action Space with Infinite-Dimensional Confidence Balls" (avg 5.0) — Moderate RL theory, rejected.
- "Model-based RL as Minimalist Approach to Horizon-Free and Second-Order Bounds" (avg 7.0) — Strong theoretical paper, accepted. Paper under review has more contributions.
- "Misspecified Q-Learning with Sparse Linear Function Approximation" (avg 6.0) — Niche RL theory, accepted. Paper under review is broader.
- "Horizon-free RL in Adversarial Linear Mixture MDPs" (avg 6.0) — First horizon-free adversarial RL, accepted. Paper under review has more contributions.
- "Provable Learning for DEC-POMDPs" (avg 6.17) — Mixed reviews, rejected.
- "Dynamic Discounted CFR" (avg 8.0) — Game solving, less directly comparable.
- "A Policy Gradient Method for Confounded POMDPs" (avg 8.0) — Offline RL, less comparable.
- "MaxInfoRL: Boosting exploration through information gain maximization" (avg 6.75) — Related (information-gain exploration), accepted.
- "On Bits and Bandits: Quantifying the Regret-Information Trade-off" (avg 6.5) — Related (information-regret tradeoff), accepted.

Round 2:
- "Offline RL in Regular Decision Processes" (avg 7.0) — Accepted theoretical RL paper.
- "Beyond Worst-case Attacks: Robust RL with Adaptive Defense" (avg 7.0) — Robust RL, accepted.
- "Minimax Optimal RL with Quasi-Optimism" (avg 7.0) — Also explores beyond standard optimism, accepted. Paper under review has broader framework.

**Round 1 bracket: 6.5–8.0.** The paper exceeds the 6.0 anchors (multiple contributions vs. more incremental work) and matches or surpasses the 7.0 anchors (more contributions, broader framework, genuine novelty in replacing optimism).

**Round 2 narrowing: 7.0–7.5.** The paper matches the 7.0 anchors in quality and exceeds them in breadth. It doesn't reach 8.0 because the hybrid MDP assumptions are non-trivial and the strict improvement example is limited to a 3-armed bandit.

**Final score: 7.5.** This is a strong theoretical paper with multiple genuine contributions (Dig-DEC framework, improved estimators, hybrid MDP results), clean presentation, structural results (Theorem 13), and concrete improvement evidence (Theorem 14). The weaknesses are minor (assumption scope, parser artifacts) and do not threaten the core claims.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>