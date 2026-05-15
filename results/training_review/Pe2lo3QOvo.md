I now have all the information I need. Let me produce the consolidated review.

---

## Summary

This paper studies RL with preference-based feedback (RLHF) and proposes randomized algorithms that are computationally efficient — a first for this setting with worst-case regret guarantees. In linear MDPs, Algorithm 1 (RLSVI-style) injects Gaussian noise into reward and value-function estimation to enable standard dynamic programming, avoiding the intractable oracles required by prior work. It also introduces a variance-style active query rule and achieves a tradeoff of $\tilde O(T^{1-\beta})$ regret and $\tilde O(T^{2\beta})$ queries. For nonlinear function approximation, Algorithm 2 (Thompson sampling) provides Bayesian regret and query bounds using $\ell_1$- and $\ell_2$-norm eluder dimensions.

## Strengths

- **First computationally efficient RLHF algorithm with sublinear worst-case regret.** Prior theoretical works on RL with preference feedback (e.g., Saha et al. 2023, Chen et al. 2022, Zhan et al. 2023) rely on intractable oracles such as $\argmax_{\pi,\pi'} \| \mathbb{E}_{s,a\sim\pi}\phi(s,a) - \mathbb{E}_{s,a\sim\pi'}\phi(s,a) \|_A$ or version-space maintenance over exponentially large policy classes. By injecting random Gaussian noise into LSVI estimates, this paper preserves the Markovian structure of the value function and enables standard dynamic programming, achieving polynomial running time in $d$, $H$, and $A$. This is a genuine algorithmic contribution that opens a path toward practical RLHF algorithms with formal guarantees.

- **Near-optimal regret-query tradeoff in $T$.** Theorem 1 establishes $\text{reg} = \tilde O(T^{1-\beta})$ and $\text{qry} = \tilde O(T^{2\beta})$ (focusing on $T$-dependence), matching the lower bound from contextual dueling bandits (Sekhari et al., 2023) in its dependence on $T$. The paper explicitly discusses the $\beta$ spectrum from $\beta=0$ (linear regret, zero queries) to $\beta=1/2$ ($\sqrt{T}$ regret, query every episode), providing a clear picture of the tradeoff. The query rule based on a variance-style uncertainty measure (Equation 4) is computationally tractable via sampling from the reward distribution, unlike prior version-space approaches.

- **Extension to nonlinear function approximation with eluder-dimension-based analysis.** Theorem 2 provides Bayesian regret and query bounds for general function classes via $\ell_1$- and $\ell_2$-norm eluder dimensions. The use of $\ell_1$-norm eluder dimension is strictly tighter than the $\ell_2$-norm version used in prior work. The regret decomposition separating model error from reward error (Equation under point (1) in Section 5.2) is a reusable technical contribution.

- **Novel technical components.** The paper introduces several reusable technical ideas: (a) trajectory-wise covariance matrices combined with state-action-wise randomization to preserve DP compatibility, (b) a regret decomposition tailored to preference feedback that isolates the reward-difference estimation error, and (c) use of $\pi_t^1 = \pi_{t-1}^0$ to guarantee conditional independence for the optimism argument.

## Weaknesses

### Fatal
None.

### Major

1. **Exponential $H$-dependence through $\kappa_{\text{low}}$ is not acknowledged as a limitation.** The bounds depend polynomially on $\kappa_{\text{low}}$, and for the Bradley–Terry–Luce model (the primary and most standard link function, Example 2.2), $\kappa_{\text{low}} = 2 + e^H + e^{-H} = O(e^H)$. This makes the regret and query bounds exponential in horizon $H$, not polynomial. The paper states in Section 3 that "the bounds depend polynomially on $\kappa_{\text{low}}$" and gives the explicit value in Example 2.2, but never discusses the implication that this produces exponential $H$-dependence for the BTL model. The abstract and introduction claim "sample efficient" and "near-optimal worst-case regret bounds" without qualification. For the linear link function ($\Phi(x) = (x+1)/2$), $\kappa_{\text{low}} = 2 = O(1)$, and the bounds are fully polynomial — but this distinction is not discussed, and the BTL example is arguably the practically relevant one. The paper should either: (a) restrict its claims to link functions with $\kappa_{\text{low}} = O(1)$ and clearly state the limitation for BTL, or (b) derive a refined analysis avoiding exponential $H$-dependence.

### Minor

2. **"Near-optimal tradeoff" claim relies on a bandit lower bound.** The paper claims the regret-query tradeoff in $T$ is optimal, citing Theorem 5 of Sekhari et al. (2023), a lower bound for *contextual dueling bandits* ($H=1$). While the paper does note this (line 233: "Their lower bound was originally proposed for contextual dueling bandits, which is a special case of our setting"), the RL setting involves multi-step transitions and state-action features that create additional structure and constraints. A matching lower bound for the RL setting (linear MDPs or general function approximation) would be needed to fully substantiate "near-optimal." The claim is plausible and carefully qualified, but it remains a gap.

3. **TS query bound is presented as two incomplete forms.** The query bound in Theorem 2 has two forms: term (i) with $\tilde O(T^{\beta+1/2})$ dependence on $T$ but using the tighter $\ell_1$-eluder dimension, and term (ii) with optimal $\tilde O(T^{2\beta})$ $T$-dependence but using the looser $\ell_2$-eluder dimension. The paper notes (line 343) that the desired combination — $\tilde O(T^{2\beta} \cdot \text{eluder}_1)$ — is left as future work. This is honestly disclosed, but it means the TS algorithm does not *fully* achieve a near-optimal tradeoff in a single unified bound. The contribution of the TS section is somewhat qualified as a result.

4. **Regret accounting for $\pi_t^1$ equivalence is slightly imprecise.** The paper states (line 152) that the cumulative regret of $\pi_t^1$ is "equivalent" to that of $\pi_t^0$. Since $\pi_t^1 = \pi_{t-1}^0$, the sums differ by boundary terms: $V^{\pi_0^0}$ (an arbitrary initial policy) appears in the $\pi_t^1$ sum but not the $\pi_t^0$ sum, and $V^{\pi_T^0}$ appears in the $\pi_t^0$ sum but not the $\pi_t^1$ sum. The difference is at most $O(H)$, negligible in the final regret bound, but the word "equivalent" is too strong and the boundary terms are not explicitly handled in the main text.

### Trivial
None.

## Nice-to-Haves

- A small-scale simulation in a tabular MDP with BTL feedback would strengthen the practical insights claimed in the introduction (e.g., the benefit of drawing trajectories from old and new policies vs. two trajectories from the same policy). The paper is theoretical, so this is not expected, but given the explicitly stated "practical insights" (Section 1, final paragraph), a simple empirical demonstration would increase the paper's impact.
- A schematic figure illustrating the query condition and its dependence on feature difference vectors would improve readability for a non-specialist audience.

## Removed Points

These points from the reviewer inputs are flagged to be removed; treat them with caution:

- **Critic's claim that "polynomial running time" is false due to $\kappa_{\text{low}}$.** The "polynomial running time" claim refers to *computational complexity* (runtime in $d, H, A$), which is separate from the regret bound's statistical complexity. The runtime analysis (line 257) does not depend on $\kappa_{\text{low}}$; for the BTL model, the MLE objective is concave and solvable in polynomial time. The $\kappa_{\text{low}}$ issue affects sample efficiency (the regret bound), not computational efficiency. The critic conflates these two distinct claims.

- **Critic's statement that the paper "never point[s] out that $\kappa_{\text{low}}$ itself grows exponentially with $H$."** The paper gives the explicit formula $\kappa_{\text{low}} = 2 + \exp(-H) + \exp(H)$ in Example 2.2, from which any reader can immediately see the exponential growth. The paper's omission is not stating the *implication* — that bounds become exponential in $H$ — which I have included as Weakness 1 above.

- **Strength Finder's "Extension to nonlinear function approximation with near-optimal Bayesian regret and query bounds."** The word "near-optimal" is too strong for the TS result given Weakness 3 (the two-form query bound). I have kept a version of this strength but adjusted the wording.

- **Critic's claim about missing comparison to "methods that rely on convex reward learning or linear link functions."** Per the rules, I cannot include missing-related-work criticisms.

- **Critic's claim that experiments are "needed" — the paper is purely theoretical, and this is not a weakness.** Moved to Nice-to-Haves.

## Novel Insights

None beyond the paper's own contributions. The review surfaces a tension that the paper itself does not discuss: the primary algorithmic contribution (computational efficiency via randomization) is genuinely novel and unaffected by $\kappa_{\text{low}}$, while the sample-efficiency claims are partly undermined by the $\kappa_{\text{low}}$ dependence for the BTL model. This distinction — separating the computational contribution (robust to $\kappa_{\text{low}}$) from the statistical one (exponential in $H$ for BTL) — is not made explicit in the paper but would significantly strengthen its presentation.

## Suggestions

1. **Explicitly discuss the $\kappa_{\text{low}}$ limitation.** Add a paragraph in Section 3 or after Theorem 1 stating that for the BTL model, $\kappa_{\text{low}} = O(e^H)$ makes the regret bound exponential in $H$, and that for the linear link function $\kappa_{\text{low}} = O(1)$, the bounds are fully polynomial. Qualify the "sample efficient" and "near-optimal" claims accordingly.

2. **Clarify the $\pi_t^1$ boundary term.** Add a brief sentence acknowledging the $O(H)$ boundary shift between the $\pi_t^0$ and $\pi_t^1$ regret sums and explaining why it is negligible.

3. **Unify or reframe the TS query bound presentation.** Either state clearly that term (ii) achieves the optimal $T$-dependence (with larger eluder dimension) and term (i) a suboptimal $T$-dependence with smaller dimension, avoiding the "near-optimal" language for the TS section, or reorganize the presentation so the incomplete combination does not appear as a claimed contribution.

4. **Add a lower-bound discussion.** Explicitly note that the optimality claim for the regret-query tradeoff in $T$ relies on the bandit setting and that a matching RL lower bound is an open problem.

## Score and Decision

**Overall assessment:** The paper makes a genuine contribution — it provides the first *computationally efficient* RLHF algorithms with provable sublinear regret and query guarantees, using clever randomization techniques to bypass intractable oracles. The weakness about $\kappa_{\text{low}}$ is real and significant: the BTL model's exponential $H$-dependence means the sample-efficiency claims are overstated in their current form. However, this issue does not invalidate the core computational contribution, and it can be addressed transparently in a revision. The remaining weaknesses (bandit lower bound, TS two-form bound, $\pi_t^1$ accounting) are minor and typical of a paper at the theory frontier. With an honest discussion of the $\kappa_{\text{low}}$ limitation, the paper would be a solid contribution.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>