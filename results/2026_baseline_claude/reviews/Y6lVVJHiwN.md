## Summary
FEDSGM is a unified federated optimization framework for constrained problems of the form $\min_{w \in \mathcal{X}} f(w)$ s.t. $g(w) \leq 0$ that simultaneously addresses four challenges: functional constraints, bidirectional compression with error feedback, multi-step local updates ($E > 1$), and partial client participation. Building on the switching gradient method (SGM), it provides projection-free, primal-only updates. The paper proves $\mathcal{O}(1/\sqrt{T})$ convergence for both hard and soft switching variants, with additional high-probability bounds under partial participation, and validates the approach on Neyman–Pearson classification and constrained RL (Cartpole CMDP).

---

## Strengths

- **Genuine unification over existing work.** The closest prior framework, Islamov et al. (2025), handles constrained FL with bidirectional compression but requires full participation and $E = 1$. FEDSGM is the first to combine all four challenges at once. The specialization results (centralized, unidirectional compression, no compression, EF-14) correctly recover known rates, which increases confidence in the main result.

- **Technically complete convergence analysis with high-probability bounds.** Theorem 1 provides separate full/partial participation guarantees under unified notation. The partial-participation bound cleanly decouples optimization error from estimation noise via a sub-Gaussian concentration argument with union bound over $T$ rounds. The geometric analysis of oscillation sources through the skew-symmetric matrices $K_{\text{glob}}$ and $K_{\text{loc}}$ is an insightful theoretical observation that directly motivates soft switching.

- **Soft switching is well-motivated and analyzed.** The connection between client heterogeneity (through $K_{\text{loc}}$) and oscillatory behavior near the feasibility boundary is novel. The characterization that $K_{\text{loc}} \neq 0$ even when $K_{\text{glob}} = 0$ (Remark 1) is a genuinely new insight for the constrained federated setting.

- **Multi-application experiments.** The logistic NP classification task provides controlled empirical validation of the theoretical predictions (impact of $E$, $m/n$, $K/d$). The Cartpole CMDP experiment demonstrates applicability to the non-convex, highly stochastic regime where the theory does not apply, which is an honest and practically relevant extension.

---

## Weaknesses

### Fatal
None.

### Major

1. **Rate degradation with $E$ undermines the "multi-step local updates" contribution.** The convergence bound scales as $\mathcal{O}(DG\sqrt{E}/\sqrt{T})$, meaning that increasing $E$ strictly worsens the sub-optimality bound. In the unconstrained federated literature, the benefit of local steps is realized through a more favorable communication–computation trade-off, not through asymptotic rate improvement. The paper never analyzes when $E > 1$ is actually beneficial, and the experiments confirm diminishing (and eventually harmful) returns as $E$ grows (Figure 2). This leaves the handling of $E > 1$ as a theoretical existence result rather than a practical recommendation. A communication-round-normalized convergence comparison (e.g., fixing total gradient computations) would be needed to substantiate the practical claim.

2. **No experimental comparison with any baseline.** The paper argues correctly that no prior method handles all four challenges simultaneously. However, partial baselines exist: constrained FL under full participation (He et al., 2024), compressed FL without constraints (EF-SGD variants), or AL/ADMM approaches with full participation. Comparing against these partial baselines on the NP classification task would establish whether the additional generality comes at a cost and would validate the unified framework more rigorously.

3. **Extra communication round for constraint evaluation is not accounted for.** Algorithm 1 (lines 3–4) requires every participating client to send a scalar $g_j(w_t)$ to the server at the start of each round, before gradient communication. This additional broadcast–aggregation step is not counted in the communication budget used in the convergence analysis or in the discussion of communication efficiency, creating a mild inconsistency in the "communication-efficient" framing.

### Minor

1. **Soft switching parameter requirement $\beta \geq 2/\epsilon$ forces near-hard behavior at convergence.** Since $\epsilon = \mathcal{O}(1/\sqrt{T})$ at optimality, the required $\beta$ grows as $\mathcal{O}(\sqrt{T})$, effectively recovering hard switching at the theoretical operating point. The practical setting of $\beta = 100$ (fixed) is not consistent with this requirement for large $T$, leaving a gap between the theory and the experiments.

2. **Assumption 4 (sub-Gaussianity of constraint gap) is stated without verification conditions.** The assumption that $\hat{G}(w_t) - g(w_t)$ is $\sigma^2/m$-sub-Gaussian holds automatically under bounded $g_j$ and i.i.d. client sampling, but neither of these conditions is explicitly stated. Clarifying the sufficient conditions would strengthen rigor.

3. **The $\Gamma$ factor in Theorem 1 (partial participation) is presented in a way that is difficult to parse.** The long inline formula spanning multiple lines makes it hard to verify the rate in special cases. A brief corollary or table of specific instantiations would aid reproducibility.

### Trivial
- The argument in Section 4 that "noise introduced by FL can smooth the optimization landscape and encourage exploration" (explaining why federated outperforms centralized in CMDP) is speculative and unsupported within the paper.

---

## Nice-to-Haves

- A formal communication-computation trade-off analysis (total rounds × $E$ fixed) showing when $E > 1$ is preferred over $E = 1$.
- Explicit verification that Assumption 4 is satisfied for the NP classification and CMDP experimental setups.
- A convergence curve normalized per total gradient computation, not per round, for Figure 2 (top row).
- Extension of the high-probability partial-participation guarantees to soft switching (Theorem 2 currently only covers the full-participation case).

---

## Novel Insights

The geometric decomposition of oscillation sources into a global component $K_{\text{glob}} = \nabla f \nabla g^\top - \nabla g \nabla f^\top$ and a local heterogeneity component $K_{\text{loc}}$ is the most genuinely novel theoretical insight beyond the algorithmic contribution. The observation that $K_{\text{loc}} \neq 0$ even when global gradients are perfectly aligned—and that this local skewness is bounded by $\sqrt{V_f V_g}$ (the product of objective and constraint heterogeneities)—provides a principled, geometry-grounded justification for soft switching in federated settings that goes beyond what exists in the centralized SGM literature.

---

## Suggestions

- Provide a table comparing FEDSGM against partial baselines (e.g., constrained FL with $E=1$, no-compression FL with constraints, ADMM-type FL) on NP classification, even if those methods require simplifying assumptions.
- Clearly state in the algorithm description that line 3 incurs a separate, lightweight communication round, and either include it in the communication count or argue why it is negligible.
- Add a corollary to Theorem 2 for the partial-participation case, or explicitly state why the soft switching analysis is more complex in that setting.
- Provide the value of $\sigma$ used in the NP classification and CMDP experiments, and verify that Assumption 4 holds for these setups.

---

## Score and Decision

The paper makes a genuine first-of-its-kind contribution: a provably convergent, projection-free, duality-free federated constrained optimization framework that simultaneously handles compression, local steps, and partial participation. The analysis is sound, connects correctly to prior work, and provides a novel geometric perspective on switching stability. The main deficiencies are the lack of experimental baselines, the incomplete practical argument for $E > 1$, and a minor gap between the soft-switching theory and the experiments. These are significant but not fatal.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>