## Summary

This paper studies Online Inventory Optimization (OIO) in non-stationary environments. The central contribution is an algorithm with a near-optimal dynamic regret bound of $\tilde{\mathcal{O}}(\sqrt{L_{\max}(1+P_T)T})$, where $L_{\max}$ is a demand-difficulty indicator (the sell-out period) and $P_T$ is the comparator path-length. The algorithm employs a two-stage projection that decouples the base learner from the time-varying carryover stock constraints, revealing a formal connection between OIO and Smoothed Online Convex Optimization (SOCO). As a byproduct, the authors provide the first $\Omega(\sqrt{L_{\max}T})$ lower bound for OIO, resolving an open question from Hihat et al. (2023) and improving the static regret upper bound from $\mathcal{O}(L_{\max}\sqrt{T})$ to $\tilde{\mathcal{O}}(\sqrt{L_{\max}T})$.

---

## Strengths

- **Resolves an open problem.** Hihat et al. (2023) left the optimal static regret for OIO open. Theorem 5 proves $\Omega(\sqrt{L_{\max}T})$, and the improved upper bound matches it (up to log factors), giving a complete answer. The earlier bound of $\mathcal{O}(L_{\max}\sqrt{T})$ had a gap of $\sqrt{L_{\max}}$, which is practically significant when $L_{\max}$ is large.

- **First dynamic regret guarantee for OIO.** Prior OIO algorithms only handle static regret. Extending to dynamic regret requires fundamentally new ideas because (i) the standard two-layer meta-algorithm architecture conflicts with the carryover stock assumption, and (ii) the comparator lives in a strictly larger feasible region than the learner. The two-stage projection addresses both difficulties cleanly.

- **Non-trivial technical connection to SOCO (Lemma 1).** The key lemma shows that the regret gap between $y_t$ and $\hat{y}_t$ (caused by projection onto the carryover constraint) decomposes into a switching cost proportional to $L_{\max}$. This reduction is elegant: it transforms OIO into a SOCO problem without carrying the explicit carryover constraint into the base learner, enabling the use of known SOCO algorithms (OGD, SOGD).

- **Doubling trick for unknown $L_{\max}$ (Theorem 4).** The algorithm does not require $L_{\max}$ or $P_T$ in advance. The doubling trick restarts the base learner at most $\mathcal{O}(\log L_{\max})$ times, incurring only logarithmic overhead in the regret.

- **As a byproduct, a new SOCO lower bound (Corollary 1).** The OIO lower bound implies $\Omega(\sqrt{LT})$ for SOCO, since any improvement in SOCO would translate to an improvement in OIO via the same two-stage projection, contradicting the OIO lower bound. This cross-problem implication is a novel observation.

---

## Weaknesses

### Fatal
None.

### Major

- **Restriction from convex to linear capacity constraint.** Hihat et al. (2023) handle a general convex capacity set $\mathcal{C}$. This paper specializes to the linear constraint $\sum_i y_t^i \leq D$, citing that Lemmas 5 and 6 require it. This is a meaningful step backward in generality, even though linear constraints cover many practical scenarios. The paper does not provide intuition for why convexity is problematic or what specific property of the linear constraint enables the proof. Without this, it is unclear how fundamental the restriction is and whether it can be lifted with modest effort.

- **No lower bound for the dynamic regret including $L_{\max}$.** Theorem 5 proves $\Omega(\sqrt{L_{\max}T})$ only for the static case ($P_T = 0$). The dynamic regret bound is $\tilde{\mathcal{O}}(\sqrt{L_{\max}(1+P_T)T})$, and the claim of near-optimality for the dynamic setting rests on combining the OCO lower bound $\Omega(\sqrt{(1+P_T)T})$ (from unrelated prior work) with the OIO lower bound $\Omega(\sqrt{L_{\max}T})$ (from this paper) informally. A unified lower bound of $\Omega(\sqrt{L_{\max}(1+P_T)T})$ directly for OIO is missing and would significantly strengthen the optimality claim.

### Minor

- **Definition 1 ($L_{\max}$) requires cumulative demand to reach the full warehouse capacity $D$ rather than per-item capacity.** For multi-item instances where individual items have much smaller per-item capacity, this definition may be overly loose or tight in unintuitive ways. The relationship between the per-item demand scale and $D$ (which bounds the total stock across all items) is not discussed.

- **Theorem 3 requires knowing $P_T$ a priori** to set the learning rate $\eta$. While the SOGD-based Theorem 4 avoids this at a $\sqrt{\log T}$ cost, Theorem 3 is presented first as the main result for OGD; the caveat about $P_T$ being unknown deserves more prominent treatment.

- **Condition in Theorem 4:** $T \geq \sqrt{L_{\max}(\log_2 T + e)}$ is an unusual assumption. For large $L_{\max}$, this could be restrictive and is not discussed in terms of when it might fail.

### Trivial
None worth raising.

---

## Nice-to-Haves

- A simulation experiment comparing the proposed algorithm with MaxCOSD on a non-stationary demand sequence (e.g., seasonal demand) would corroborate the theoretical improvement and ground the contributions for applied readers.
- A concrete example illustrating how $L_{\max}$ changes across different demand scenarios (e.g., i.i.d., slowly drifting, adversarial) would aid intuition.

---

## Novel Insights

The central novel insight is the reduction of OIO to SOCO via two-stage projection. Specifically, Lemma 1 shows that the regret gap introduced by projecting the base learner's decision onto the carryover-constrained feasible region is bounded by the switching cost of the base learner weighted by the cycle length, which is itself bounded by $L_{\max}$. This transforms the difficult time-varying feasibility constraint into a standard switching cost — a known quantity in SOCO — enabling the direct application of SOCO algorithms and their associated regret analyses. The cross-problem lower bound implication (Corollary 1), where an OIO lower bound yields a SOCO lower bound, is an additional elegant observation that demonstrates the tightness of the reduction.

---

## Suggestions

- Provide a formal unified lower bound $\Omega(\sqrt{L_{\max}(1+P_T)T})$ for the dynamic OIO regret, or explicitly discuss whether such a bound is achievable and what technical barriers exist.
- Add a brief discussion of what specifically prevents extending the proof from a linear to a general convex capacity set, pointing to the exact step where the linear structure is exploited. This would help readers assess the practical scope of the result.
- Consider adding a simulation to validate the theoretical gains empirically, especially since the improvement from $\mathcal{O}(L_{\max}\sqrt{T})$ to $\mathcal{O}(\sqrt{L_{\max}T})$ can be dramatic when $L_{\max}$ is large.

---

## Score and Decision

The paper makes solid and well-scoped theoretical contributions: it resolves an open question on static regret optimality for OIO, provides the first dynamic regret algorithm for OIO, and uncovers a clean connection between OIO and SOCO. The proofs are technically sound at the level visible in the paper, and the results are clearly presented. The restriction to linear capacity constraints is the most significant limitation, but the new dynamic regret result and the matching lower bound are genuine contributions that outweigh this drawback. This is a borderline-accept paper with clear technical merit.

MY FINAL SCORE: <score>6</score>
MY FINAL DECISION: <decision>Accept</decision>