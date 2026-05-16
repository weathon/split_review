Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper studies RL with preference-based feedback (RLHF) and proposes randomized algorithms that simultaneously achieve sublinear regret, polynomial running time, and controlled query complexity. For linear MDPs, it gives a randomized LSVI algorithm (Pref-RLSVI) with near-optimal regret–query tradeoff. For general function approximation, it provides a Thompson-sampling algorithm with Bayesian regret and query bounds using the ℓ₁-norm eluder dimension. Both algorithms use novel variance-style uncertainty for active querying, avoiding intractable version-space construction.

## Strengths

- **First computationally efficient algorithm for RLHF with sublinear worst-case regret.** The paper convincingly demonstrates (Sec. 2) that prior algorithms by Chen et al. 2022, Saha et al. 2023, Zhan et al. 2023 are statistically efficient but computationally intractable even for tabular MDPs due to non-standard oracles and exponentially large policy classes. Pref-RLSVI avoids these via randomization and standard dynamic programming, achieving polynomial running time.

- **Novel use of randomization to preserve Markovian structure and enable DP.** The key technical insight — adding Gaussian noise to the MLE reward estimate and LSVI parameters rather than using UCB-style bonuses — is well motivated (Sec. 1, Sec. 4). This preserves the Markovian property of the value function, allowing standard DP (argmax over actions) instead of intractable policy search over trajectory-level objectives.

- **Near-optimal regret–query tradeoff with a matching lower bound.** Theorem 3 shows Reg = Õ(T^{1-β}) and Qry = Õ(T^{2β}) with β ≤ 1/2. Theorem 4 cites a lower bound from Sekhari et al. (2023) for contextual dueling bandits, which the paper correctly notes is a special case of the RLHF setting (MDP with H=1). The tradeoff is claimed as optimal in T, which is supported.

- **Computationally tractable active learning via variance-style uncertainty.** The query condition (Eq. 4) uses expected absolute reward difference under the noisy reward distribution, approximated by i.i.d. samples from the Gaussian posterior. This avoids constructing version spaces or confidence intervals, which are standard but intractable in prior active learning work (Sec. 1, Sec. 4).

- **Extension to general function approximation with ℓ₁-norm eluder dimension.** The Thompson sampling algorithm (Sec. 5) uses the tighter ℓ₁-norm eluder dimension, which is strictly better than ℓ₂-norm used in prior work. The Bayesian regret decomposition into model and reward components is non-trivial and appropriate for preference feedback.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **The trajectory-feature norm assumption (Assumption 1) requires scaling that is acknowledged but not fully worked through.** The paper assumes ||φ(τ)||₂ ≤ 1 for trajectory features φ(τ) = Σ_h φ(s_h, a_h) while also assuming ||φ(s,a)||₂ ≤ 1. In tabular MDPs, this forces a scaling that multiplies the reward parameter bound B by H. The paper acknowledges this (line 123: "we can scale it down... at the expense of scaling B up by H") and notes that parameter dependencies "can be loose" (line 242). However, since B appears in γ = √(κ + B²), which propagates through the bounds as γ³ (Theorem 1), the H-dependence in the stated bounds is not the final story after proper scaling. The paper would benefit from either recomputing the bounds in the properly scaled parameterization or providing a cleaner self-normalized assumption. This does **not** undermine the core claims (the tradeoff in T, computational efficiency, or the qualitative results), but it leaves the quantitative H-dependence less sharp than claimed.

- **The Thompson-sampling query bound is a minimum of two expressions with no unified guarantee.** Theorem 2's query bound is min{ (i) Õ(T^{β+1/2} · eluderone), (ii) Õ(T^{2β} · eluderetwo) }. Neither term simultaneously achieves the best T-dependence and the best eluder-dimension dependence. The paper is transparent about this (line 343: "We leave it as future work"), but this means the claimed "near-optimal tradeoff" for the TS algorithm is partially aspirational — the optimal T-dependence (ii) uses ℓ₂-eluder (which is larger), and the better eluder dependence (i) has worse T-dependence. This softens the contribution relative to the linear-MDP case where the tradeoff is clean.

- **The distance function d for the eluder dimension is not specified in the main text for the model class P and the reward-difference class \~R.** The ℓₚ-eluder definition (Definition 1) takes a distance function d on the output space, but the main text of Theorem 2 does not specify which d is used for each class. The proof is deferred to the appendix. While this is standard for a theory paper with an appendix, it makes the bound in the main text harder to interpret without cross-referencing.

### Trivial
None.

## Nice-to-Haves

- The paper could explicitly note that the bandit lower bound (Sekhari et al. 2023, Theorem 5) applies to the RLHF setting by embedding an H=1 MDP. The paper currently says this is "a special case of our setting" (line 234), which is correct, but spelling out the embedding would preempt any concern about the optimality claim.

- A brief discussion of how the action space size |A| enters the polynomial running time (beyond the footnote on line 257) would strengthen the computational claims.

## Removed Points

These points are flagged to be removed; treat them with caution:

1. **"Unrealistic assumption on trajectory-feature norm" framed as a structural/fatal issue.** The reviewer claimed this "could undermine the validity of the linear MDP results." The paper explicitly acknowledges the scaling (line 123) and notes that H-dependencies "can be loose" (line 242). The reviewer's speculation that "the linear MDP assumption with μ integration condition may break under rescaling" is unsupported — rescaling φ while rescaling μ inversely preserves the transition kernel. The issue is a known limitation common to the linear MDP literature, not a structural flaw. Kept in Minor above.

2. **"Optimality claim not supported in the RL setting."** The reviewer claimed the bandit lower bound "does not automatically extend" and called this an "evidential gap." However, the paper explicitly states that contextual dueling bandits are "a special case of our setting" (line 234). An MDP with H=1 is a contextual bandit, so the lower bound directly applies. The claim is about optimality in T (not in d, H, etc.), which is correctly qualified. This is not a weakness.

3. **"No explicit discussion of dependence on |A|."** The paper includes a footnote (line 257) stating "assuming finite number of actions. This is to ensure that argmax_a Q(s,a) can be computed efficiently." The issue is already addressed.

4. **"Practical insights not validated by experiments."** This is a theory paper. Experiments are not required, and their absence is not a weakness. The paper correctly frames itself as a theoretical contribution.

5. **Missing related works.** Since I cannot verify the existence of unmentioned works, this is excluded per instructions.

6. **Eluder dimension distance functions not specified in main text.** The definitions are provided (Definition 1), the classes P and \~R are defined, and the proof is deferred to the appendix. This is standard practice for theory papers. It is a minor accessibility issue at worst. Moved to Minor above.

## Novel Insights

The meta-review reveals an interesting pattern: the paper's key strength — using randomization instead of UCB-style bonuses — is also the source of its main technical tensions. The randomization preserves Markovian structure for DP but introduces the trajectory-feature scaling subtlety (because trajectory-level uncertainty must be reconciled with state-action-wise value iteration). Similarly, the variance-style active learning is computationally tractable precisely because it builds on the same randomization used for exploration, creating a unified design principle. This self-consistency of the randomization theme across exploration, computation, and querying is a genuinely nice theoretical alignment, even if individual bounds are not yet tight in all parameters. The TS algorithm's split query bound (min of two terms) reveals a deeper open question: whether the ℓ₁-eluder dimension can simultaneously achieve the right T-dependence, which would require a tighter concentration argument than currently available.

## Suggestions

- Recompute or explicitly bound the effect of the trajectory-feature scaling on the H-dependence in Theorem 1 to show it does not worsen the polynomial degree beyond what is stated. Even a short note in the appendix showing how the scaling propagates through γ would resolve this cleanly.

- For the TS query bound, either (a) prove a unified bound with optimal T-dependence and ℓ₁-eluder, or (b) explicitly characterize the regime where each of the two terms dominates and provide a practical selection rule (e.g., use (i) when ε is large, (ii) when ε is small).

- Add a brief remark making explicit the embedding of contextual dueling bandits as H=1 MDPs to fully justify the optimality claim.

## Score and Decision

The paper makes a clear theoretical contribution: it presents the first RLHF algorithms that are simultaneously statistically efficient (sublinear regret), computationally efficient (polynomial time), and query-efficient (active learning with tunable tradeoff). The key ideas — randomization to preserve Markovian structure and variance-style active learning — are novel and well-motivated. The two substantive weaknesses (trajectory-feature scaling and the TS query bound being a min of two terms) are acknowledged by the paper and do not threaten the core claims about the regret–query tradeoff in T or computational tractability. The paper is clearly written, appropriately scoped, and properly situates itself against prior work.

MY FINAL SCORE: <pineapple>8.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>