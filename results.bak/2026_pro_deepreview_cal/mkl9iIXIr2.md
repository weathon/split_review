Now I have all the information I need. Let me write the consolidated review.

---

## Summary

This paper addresses online inventory optimization (OIO) in non-stationary environments, an open problem raised by Hihat et al. (2023). The key insight is a two-stage projection strategy that reduces OIO to smoothed online convex optimization (SOCO) with switching costs proportional to cycle lengths (Lemma 1). This reduction yields the first dynamic regret guarantee for OIO: \(\tilde{\mathcal{O}}(\sqrt{L_{\max} T (1+P_T)})\), improves the static regret from \(O(L_{\max}\sqrt{T})\) to \(O(\sqrt{L_{\max} T})\), and provides a matching lower bound \(\Omega(\sqrt{L_{\max} T})\) establishing near-optimality. A doubling trick handles the unknown maximum sell-out period \(L_{\max}\).

## Strengths

- **Novel reduction from OIO to SOCO (Lemma 1, Eq. 7–8).** The two-stage projection and cycle analysis show that the carryover stock constraint translates into a switching-cost term proportional to the current cycle length. This is the pivotal insight that enables the first dynamic regret guarantee for OIO and is likely to be useful beyond this paper. The connection is clean and rigorously stated.

- **Matching lower bound for static regret (Theorem 5).** The \(\Omega(\sqrt{L_{\max}T})\) lower bound is the first such bound for the OIO setting and matches the paper's static upper bound, confirming that the \(\sqrt{L_{\max}}\) factor is necessary. This resolves the open question from Hihat et al. (2023) about the tightness of the dependence on \(L_{\max}\).

- **Adaptive algorithm via doubling trick (Algorithm 2, Theorem 2).** The algorithm tracks observed cycle lengths online and restarts the base learner when the current estimate of \(L_{\max}\) is exceeded, requiring no prior knowledge of \(L_{\max}\) or \(P_T\). Theorem 2 provides a generic regret bound for any base learner satisfying a decomposition condition, making the approach modular.

- **Clear positioning and well-structured presentation.** The paper is well-organized, with Table 1 clearly situating the contribution against prior work, and the technical narrative (Lemma 1 → SOCO reduction → doubling trick → base learner instantiation → lower bound) is logical and easy to follow.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **The lower bound is only for the static case (Theorem 5).** The paper claims near-optimality of the dynamic regret bound \(\tilde{\mathcal{O}}(\sqrt{L_{\max}(1+P_T)T})\) but proves a lower bound only for a fixed comparator \(u \in \mathcal{C}(0)\). The argument for dynamic near-optimality relies on combining this static lower bound with the known OCO lower bound \(\Omega(\sqrt{(1+P_T)T})\) from Zhang et al. (2018b). While this reasoning is plausible — when \(P_T = 0\), the dynamic regret reduces to static regret, so \(\Omega(\sqrt{L_{\max}T})\) is a valid lower bound on dynamic regret — a direct dynamic lower bound for OIO would be more convincing. The paper should clarify this reliance on the static lower bound plus the standard OCO result rather than implying a unified dynamic lower bound.

- **Linear capacity constraint is a meaningful restriction.** The paper explicitly acknowledges (Section 6, line 359) that the linear-sum capacity constraint \(\sum_i y_t^i \leq D\) is "critical to the proof of Lemmas 5 and 6" and that extension to general convex constraints is left for future work. Since Hihat et al. (2023) handled arbitrary convex sets for the static case, this limits the generality of the dynamic-regret results. The linear case covers many practical scenarios (and the paper notes that weighted sums reduce to it via rescaling), so this is a scope limitation rather than a flaw.

### Trivial

- The conditions on \(T\) relative to \(L_{\max}\) and \(P_T\) in Theorems 3 and 4 (e.g., \(T \geq L_{\max}(3 + P_T/D)\), \(T \geq \sqrt{L_{\max}(\log_2 T + e)}\)) could use brief commentary on whether they are mild in typical inventory applications, though the paper does note the \(\mathcal{O}(L_{\max} \log L_{\max})\) overhead is subdominant for \(T > L_{\max} \log^2 L_{\max}\).

## Nice-to-Haves

- A short proof sketch of Lemma 1 in the main text would help readers appreciate why the two-stage projection yields the OIO-to-SOCO reduction. The current text states the lemma and uses it but does not convey the proof mechanics.
- A small worked example (e.g., two items, simple demand pattern) illustrating cycle dynamics and the projection would make the concepts more concrete.
- Explicitly verifying in the main text that OGD and SOGD satisfy the decomposition condition \(\mathcal{R}_{L,T}^{\mathcal{E}(L,T)} = L^\alpha \mathcal{R}(T)\) used in Theorem 2 would underscore the plug-and-play nature of the framework.

## Removed Points

*These points are flagged to be removed, treat them with caution.*

- **"The paper does not discuss how the choice of base learner affects practical performance when \(L_{\max}\) is estimated online" (Harsh Critic).** Removed — this is a generic request for empirical analysis in a theory paper with no experiments. The analysis already handles the restart mechanism in the aggregate regret bound.
- **"Transient behavior of the doubling trick could temporarily increase regret" (Harsh Critic).** Removed — this is speculation about transient effects not analyzed in the paper and carries no weight in evaluating the theoretical contribution.
- **"All key proofs rely on the warehouse capacity constraint being a linear sum" framed as a structural limitation that could be fatal.** Kept but demoted to Minor — the paper transparently acknowledges this in Section 6 and the linear case is practically common. This is a scope limitation, not a flaw.
- **Request for Lemma 1 proof walk-through, OGD/SOGD condition verification, and cycle illustration in main text.** Moved to Nice-to-Haves — these are presentation preferences, not weaknesses.

## Novel Insights

The paper establishes a bidirectional relationship between OIO and SOCO that was not previously known: the two-stage projection shows that OIO regret can be upper-bounded by SOCO regret with cycle-length-dependent switching costs, and the OIO lower bound (Theorem 5) implies a lower bound for SOCO (Corollary 1). This cross-pollination — where a lower bound in one problem constrains the other — is an intriguing structural insight that may generalize to other constrained online learning settings.

## Suggestions

- Clarify in the abstract and introduction that the lower bound (Theorem 5) is for static regret, and that the dynamic near-optimality argument combines this with the known \(\Omega(\sqrt{(1+P_T)T})\) OCO lower bound, rather than a direct dynamic lower bound.
- The linear capacity assumption could be discussed earlier (e.g., in Section 3 alongside Eq. 3–4), rather than waiting until the conclusion, so readers understand the scope from the start.
- Consider adding a brief remark on whether the conditions \(T \geq L_{\max}(3 + P_T/D)\) in Theorem 3 are mild in practice, to help applied readers assess applicability.

## Score and Decision

**Calibration anchors consulted:**

| Anchor | Score | Round | Comparison |
|---|---|---|---|
| iZgECfyHXF ("On the Hardness of Online Nonconvex Optimization…") | 6.50 | R1/R2 | Similar structure (lower + upper bounds), but lower bounds restricted to algorithm family; our paper has a more general lower bound and a stronger novel reduction |
| pA8Q5WiEMg ("Improved Regret Bounds for Non-Convex OWO Meta Learning") | 6.00 | R2 | Solid theory paper with improved bounds but acknowledged limitations and no lower bounds; our paper has stronger technical novelty and matching lower bounds |
| OvU9u6wS2J ("An Online Learning Theory of Trading-Volume Maximization") | 7.00 | R2 | Complete characterization with tight bounds across settings, techniques relatively standard; our paper has a more novel reduction (OIO→SOCO) but narrower scope (linear constraint) |
| WIerHtNyKr ("Adaptive Algorithm for Non-Stationary Online Convex-Concave Optimization") | 5.25 | R1 | Rejected for unclear novelty and incremental techniques; our paper is substantially stronger |
| 5t57omGVMw ("Learning to Relax") | 8.00 | R1 | Very polished, complete results with practical impact; our paper is not at this level due to the linear constraint limitation and missing dynamic lower bound |

**Round 1 bracket:** 6.0–8.0. The paper is clearly stronger than the 5.25 reject anchor (which had unclear novelty) and not at the 8.0 level (which requires complete results with no notable gaps).

**Round 2 narrowing:** 6.5–7.5. The paper is stronger than pA8Q5WiEMg (6.00), comparable to or slightly better than OvU9u6wS2J (7.00) in technical novelty, but below the 8.0 anchors due to the linear constraint scope limitation and the missing direct dynamic lower bound.

**Final assessment:** The paper makes a genuine contribution — the OIO-to-SOCO reduction is elegant and opens up dynamic regret analysis for inventory optimization. The improved static bound and matching lower bound are solid results. The linear constraint limitation and the static-only lower bound are real but minor issues that do not undermine the core contribution. Score: **7.0**.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>