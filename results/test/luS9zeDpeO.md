Now I have a complete picture of the paper. Let me write the consolidated review.

## Summary

This paper studies decentralized safe MARL for homogeneous multi-agent systems with entropy regularization. It formalizes homogeneous constrained Markov games, proves that policy sharing preserves optimality and safety (Theorem 1), develops an on-policy decentralized primal-dual algorithm with asymptotic convergence guarantees (Theorems 3–5), and extends it to a practical off-policy deep RL version (DPDAC-ER). Experiments on three continuous multi-robot coordination tasks compare against centralized safe MARL (MASAC-Lag), a non-safe decentralized method (DAC-ER), and an ablation without entropy (DPDAC).

## Strengths

- **First proof that policy sharing preserves optimality under safety constraints (Theorem 1):** The paper rigorously shows that in homogeneous constrained Markov games, there exists an optimal joint policy using shared observation-based local policies that achieves the same reward and safety as any unrestricted optimal policy. The paper correctly states this "justifies the use of the policy sharing mechanism in the safe MARL algorithm design for the first time" (Section 3).

- **Asymptotic convergence guarantees for the decentralized primal-dual algorithm:** Theorems 3–5 establish almost-sure convergence of critic, actor, and dual variables using multi-timescale stochastic approximation under standard assumptions. Proposition 1 further shows the converged policy approximately satisfies the safety constraint. This is a nontrivial theoretical contribution.

- **Formal model for homogeneous constrained Markov games (Definition 1):** Extends the homogeneous MG model of Chen et al. (2022) to the safe MARL setting with permutation-preserving reward/cost and permutation-invariant transitions, providing a principled foundation for the analysis.

- **Sensible set of ablations:** The communication ablation (Fig. 3) demonstrates that consensus is necessary for safe performance, and the threshold ablation (Fig. 4) confirms the expected reward-safety trade-off. The local observation ablation (referenced in Section 6) provides preliminary evidence of broader applicability.

## Weaknesses

### Fatal
None.

### Major

1. **Missing empirical comparison against existing decentralized safe MARL methods.** The paper cites Lu et al. (2021) and Ying et al. (2023b) as existing decentralized safe MARL methods and explicitly claims its contribution is "compared with existing works on decentralized safe MARL... a practical off-policy decentralized algorithm... which can effectively deal with continuous spaces" (Section 1, bullet 3). Yet the experimental evaluation does not include either method as a baseline. The paper provides reasons these methods face challenges in continuous spaces (vanilla policy gradient limitations for Lu et al., occupancy measure estimation issues for Ying et al.), but this is not the same as demonstrating that DPDAC-ER outperforms them. Since the paper's central empirical claim is that it advances decentralized safe MARL for continuous spaces, the absence of the most directly comparable methods — even in a reduced setting or with appropriate adaptations — leaves the empirical contribution only partially supported. The paper does include CT-based safe baselines (MASAC-Lag), a non-safe decentralized method (DAC-ER), and a self-ablation (DPDAC), but none of these fill the gap left by omitting the existing decentralized safe methods the paper positions itself against.

2. **Disconnection between theoretical convergence guarantees and the practical evaluated algorithm.** The convergence analysis (Theorems 3–5, Section 4) is established for the on-policy algorithm (6)–(8) under finite state/action spaces, linear function approximation, decreasing stepsizes, and on-policy data. The practical algorithm (Section 5) replaces all of these with neural networks, replay buffers, and off-policy updates with automatic entropy adjustment. The paper acknowledges this gap in the first sentence of Section 5, noting the theory is "severely limited by the standard assumptions," but does not explain how or whether the theoretical results inform the practical design beyond loose functional-form inspiration. The paper references an appendix discussing the relationship between the theoretical and practical update rules, but the core issue remains: the algorithm whose behavior is proven (linear, on-policy, finite spaces) and the algorithm whose behavior is evaluated (NNs, off-policy, continuous spaces) differ on every substantive dimension. This undermines the claim that the theory provides grounding for the practical method. A small-scale validation of the on-policy linear version, or a clearer separation of the theoretical and practical contributions, would substantially strengthen the paper.

### Minor

1. **The "decentralized" label relies on global state and joint action availability.** The paper follows the setting of Zhang et al. (2018) and Chen et al. (2022), where agents observe the global state and joint action but only have access to local policy/reward information and communicate via a sparse network. This is a legitimate and well-defined notion of decentralization, but it differs from the local-observation paradigm common in many practical multi-agent problems. The paper acknowledges this (Section 2.2) and includes a local observation ablation in the supplement, but the ablation result deserves more prominence, as it directly speaks to the algorithm's applicability scope. The current brief mention in Section 6 does not adequately convey this important finding.

2. **Approximation of other agents' policies by each agent's own policy.** In the practical algorithm (Equations 13, 14), each agent samples other agents' actions using its own policy, justified by Theorem 1 asymptotically (consensus). However, early in training, policies across agents may diverge before consensus takes effect. The paper does not discuss the resulting bias, how quickly consensus resolves this mismatch, or whether this approximation introduces instability. An analytical bound or a small diagnostic experiment would strengthen the practical claims.

### Trivial
None.

## Nice-to-Haves

- Report constraint violation rates (not just average cost curves) for the learned policies during evaluation, to provide a clearer picture of safety satisfaction beyond what the cost curves show.
- Discuss whether the automatic entropy adjustment (Equation 16) is compatible with the convergence analysis or whether it introduces additional non-stationarity that the theory does not cover.
- Discuss why consensus helps theoretically for the dual variable update beyond general parameter agreement (the communication ablation empirically shows its necessity, but a theoretical intuition would help).
- Validate the on-policy linear version on a small-scale (e.g., grid-world) version of one task to demonstrate that the theoretical convergence results are predictive of actual behavior.

## Removed Points

None of the harsh critic's core criticisms are factually wrong or misunderstand the paper. All are grounded in the paper's content and have been retained at appropriate severity levels. The Strength Finder's claimed strengths are all specific and contentful; none were generic or superficial enough to warrant removal.

## Novel Insights

The most interesting observation to emerge across the reviews is the tension inherent in the paper's architecture: the theoretical proof of concept relies on an on-policy, linear-function-approximation setting that deliberately uses decreasing stepsizes and finite spaces, while the practical contribution is explicitly motivated by overcoming those very limitations. This is a common pattern in RL theory-to-practice papers, but the gap here is wider than usual — every significant design element changes between the proven and the tested algorithm. This suggests the paper would be stronger if it presented the two contributions as more independent: (a) a self-contained theoretical analysis showing that a decentralized primal-dual algorithm *can* converge under standard assumptions in finite/linear/on-policy settings, and (b) a separate, heuristic deep-RL extension that is motivated by, but not claimed to inherit guarantees from, the theory. The current framing implicitly suggests the theory validates the practical method, which it does not.

## Suggestions

- Add comparisons to Lu et al. (2021) and/or Ying et al. (2023b), even if only in simplified/discrete-action variants of the tasks, or provide a concrete technical argument (not just a qualitative difficulty description) for why adaptation is infeasible. Without this, the paper cannot substantiate its claim of advancing the state-of-the-art in decentralized safe MARL for continuous spaces.
- Sharply separate the theoretical and practical contributions in the paper's structure and claims. The current presentation implies the theory supports the practical algorithm, but the gap between what is proven and what is tested is too large for this to hold. Frame the theory as a self-contained result and the DRL extension as a motivated heuristic.
- Move the local observation ablation from the supplement to a primary result in the main paper, with learning curves and a discussion of when/why performance degrades. This directly addresses the algorithm's practical applicability scope.
- Add a small diagnostic experiment or bound analyzing the bias from using each agent's own policy to approximate other agents' actions early in training.

## Score and Decision

**Originality:** Good. Theorem 1 is the first proof that policy sharing preserves optimality under safety constraints, and the convergence analysis extends primal-dual theory to the decentralized multi-agent setting.

**Importance of research question:** High. Safe decentralized MARL for continuous control is a practically relevant problem.

**Claims:** Somewhat overclaimed. The paper positions itself as improving upon existing decentralized safe MARL methods for continuous spaces but does not compare against them. The theory-practice connection is presented as tighter than it actually is.

**Soundness of experiments:** Moderate. The experiments show DPDAC-ER is competitive with centralized safe methods, but the absence of comparison to existing decentralized safe methods is a meaningful gap.

**Clarity:** Good. The paper clearly describes its setting, algorithm, and theoretical results.

**Value to community:** Moderate. The theoretical results (Theorem 1, convergence analysis) are genuine contributions. The practical algorithm may be useful, but its empirical standing relative to existing decentralized safe methods is unclear.

The paper has real theoretical contributions (the optimality preservation proof and the convergence analysis) that are novel and sound. However, the empirical evaluation has a significant gap — the absence of comparison to the existing decentralized safe MARL methods the paper explicitly positions itself against — and the theory-practice gap is wider than what would support the claim that the theory "grounds" the practical algorithm. A major revision addressing the empirical comparison would be needed for the paper's full contribution to be convincingly demonstrated.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>