I now have a complete understanding of the paper and all the review inputs. Let me write the final consolidated review.

## Summary

This paper studies linear bandits with stage-wise hard safety constraints in non-convex (and discrete) feature spaces. It identifies a phenomenon called "non-convexity bias" — where standard star-convex safe algorithms fail to explore enough in the right directions — and designs a modified UCB-based algorithm (NCS-LUCB) with a new bonus term ($g_t^\nu$) to counter this bias. The algorithm operates under local point assumptions (Assumption 3) that are strictly weaker than the star-convexity required by prior work. The paper provides a regret upper bound of $\tilde{\mathcal{O}}(d(1+\tau/(\varepsilon\iota))\sqrt{T})$ and an information-theoretic lower bound of $\Omega(\max\{d\sqrt{T}, 1/(\varepsilon\iota^2)\})$, with numerical validation on a discrete 2D instance.

## Strengths

1. **First safe algorithm for non-convex/discrete feature spaces under local assumptions.** The paper correctly identifies that existing safe linear bandit algorithms (Amani et al., 2019; Pacchiano et al., 2024) require star-convex or convex action sets, and provides the first result relaxing this to local conditions around the origin and the optimal point (Assumption 3). This is a genuine gap in the literature and the paper's framing is well-motivated (Section 1, Section 3).

2. **Novel bonus design that provably overcomes non-convexity bias.** The paper introduces $g_t^\nu(a)$ (Eq. 4), a bonus term that accounts for the distance from the optimal point to the available actions rather than to the safety boundary. Lemma 2 proves this restores optimism in non-convex spaces, and Lemma 4 bounds its cumulative cost at a sublinear rate. The toy example (Section 5.2) clearly illustrates why the star-convex bonus fails and how the proposed fix resolves the issue.

3. **Upper bound nearly matches star-convex rates.** Theorem 1 gives a regret bound of $\tilde{\mathcal{O}}(d(1+\tau/(\varepsilon\iota))\sqrt{T})$, which the paper correctly compares to Pacchiano et al. (2024) and shows the only additional factor is $1/(\varepsilon\iota)$ from the weaker local assumptions. The sublinearity of the bound is genuine.

4. **Local assumptions are strictly weaker than star-convexity.** Assumption 3 imposes conditions only in $\varepsilon$- and $\iota$-neighborhoods around the origin and the optimal point, rather than requiring every line from the origin to lie in the set. The paper provides clear visual intuition (Figure 3) and real-world motivation (venture capital example, Section 3).

## Weaknesses

### Fatal
None.

### Major

1. **The lower bound (Theorem 2) does not fully support the paper's claims about optimality and the necessity of $\varepsilon,\iota$ in the $\sqrt{T}$ scaling.** The bound is $\Omega(\max\{d\sqrt{T},\; \tfrac{1-2\varepsilon}{\varepsilon}(\tfrac{1-\iota}{\iota})^2\})$. The second term is a constant that does not grow with $T$. For any $T$ that is not tiny, the $\Omega(d\sqrt{T})$ term dominates, reducing the bound to the standard unconstrained linear bandit lower bound with no $\varepsilon,\iota$ dependence in the leading term. The paper's upper bound carries a multiplicative $1/(\varepsilon\iota)$ factor in front of $\sqrt{T}$, so as $\varepsilon,\iota\to 0$ the upper bound diverges, but the lower bound does not capture this multiplicative dependence in the $\sqrt{T}$ regime.  

   The paper claims this bound "highlights the necessity of $\varepsilon$ and $\iota$ in the upper bound" and "implies that Assumption 3 cannot be further relaxed" (Section 1, contribution 2). While the bound does show that $\varepsilon=0$ or $\iota=0$ would make the additive constant blow up (supporting the necessity of strictly positive parameters), it does **not** demonstrate that the $1/(\varepsilon\iota)$ multiplicative factor on $\sqrt{T}$ in the upper bound is necessary or near-optimal. The gap analysis in Remark 3 sidesteps this issue by evaluating at a single $T = \lceil 1/(\varepsilon\iota^2) \rceil$ where the constant term dominates, but this does not address the large-$T$ regime where $\sqrt{T}$ dominates and the $\varepsilon,\iota$ dependence vanishes from the lower bound.  

   *Why this is major:* The lower bound is listed as a main contribution and used to argue near-optimality. The paper must either (a) provide a lower bound that captures $\varepsilon,\iota$ dependence in the $\sqrt{T}$ term, or (b) significantly temper the claims about optimality and reframe the lower bound as showing only that an additive $\Omega(1/(\varepsilon\iota^2))$ regret is unavoidable and that $\varepsilon,\iota$ cannot be zero. As written, the claims outpace what the bound justifies.

2. **Dependence on unknown $\iota$.** The algorithm's bonus uses $\nu = (\tau+\iota)/\iota$, which requires knowledge of $\iota$ (the local radius around the optimal point). The paper acknowledges this and suggests a Bandits-over-Bandits approach (Cheung et al., 2019) as future work (Section 5.1), but provides no analysis of how misspecification (e.g., using a conservative lower bound for $\iota$) affects the regret. While theoretical papers sometimes assume knowledge of problem-dependent constants, this parameter is central to the algorithm's sublinearity guarantee, and the paper would benefit from at least a heuristic discussion of how underestimating $\iota$ degrades the bound.

### Minor

1. **Minimal experimental evaluation.** The numerical section (Section 6) tests only a single 2D instance with 5 actions, comparing NCS-LUCB to LC-LUCB. While the results demonstrate sublinear vs. linear regret as predicted, the paper would be strengthened by: (a) varying dimension $d$, (b) varying $\varepsilon$ and $\iota$ to verify the predicted scaling, and (c) testing cases where the local assumptions are approximately satisfied rather than exactly met.

2. **Computational tractability not addressed.** The argmax over $\mathcal{A}_t$ in line 6 of Algorithm 1 is over a potentially non-convex set, and the paper acknowledges this only in the conclusion as future work. For a "first result" paper this is acceptable, but the limitation should be noted earlier when the algorithm is presented (Section 4), as it is central to practical applicability in continuous non-convex spaces.

### Trivial
None.

## Nice-to-Haves

- A brief analysis (even heuristic) of how performance degrades when $\iota$ is estimated from below, or when the local assumptions are only approximately satisfied.
- Additional experiments varying dimension $d$ and the parameters $\varepsilon,\iota$ to confirm the predicted scaling of regret.

## Removed Points

These points were removed from the reviewer critiques for the following reasons:

- **"The gap calculation in Remark 3 is problematic: the lower bound at that T is at most a constant (or ~ 1/(√ει))"** — This is factually incorrect. At $T = 1/(\varepsilon\iota^2)$, the lower bound's second term $\tfrac{1-2\varepsilon}{\varepsilon}(\tfrac{1-\iota}{\iota})^2 \approx 1/(\varepsilon\iota^2)$ dominates the first term $d/(8e^2) \cdot 1/(\sqrt{\varepsilon}\iota)$ for small $\varepsilon,\iota$, so the bound is $\Omega(1/(\varepsilon\iota^2))$, not $\Omega(1/(\sqrt{\varepsilon}\iota))$. The paper's claimed gap of $1/\sqrt{\varepsilon}$ is correct. The reviewer appears to have considered only the first term of the max.

- **"Assumption 3 appears truncated — the actual conditions are not printed"** — Parser artifact; the original submission contains the full conditions.

- **"Toy example assumes the agent knows $\theta^*$ exactly"** — This is an intentional simplification for illustrative purposes, and the numerical experiment (Section 6) addresses the full setting with unknown $\theta^*$. The paper is clear about this pedagogical choice.

- **Criticism about missing appendix/proofs** — Parser artifact; proofs exist in the original submission.

## Novel Insights

The most interesting observation from these reviews is the precise nature of the disconnect between the lower and upper bounds. The lower bound is an additive constant $\Omega(1/(\varepsilon\iota^2))$ that does not grow with $T$, while the upper bound has a multiplicative $1/(\varepsilon\iota)$ factor on $\sqrt{T}$. This suggests that the true hardness of this problem may decompose into: (i) an unavoidable startup cost that scales with the "non-convexity gap" (small $\varepsilon,\iota$ require more initial exploration before any safe progress can be made), and (ii) a standard $\sqrt{T}$ exploration cost that is independent of $\varepsilon,\iota$. The paper's upper bound may be loose in its $\varepsilon,\iota$ dependence in the $\sqrt{T}$ term — closing this gap is a genuine open problem.

## Suggestions

1. **Revise the claims about the lower bound.** Either provide a corrected lower bound that captures $\varepsilon,\iota$ dependence in the $\sqrt{T}$ term, or explicitly state that the lower bound shows only an unavoidable additive $\Omega(1/(\varepsilon\iota^2))$ cost and that $\varepsilon,\iota>0$ are necessary, without claiming near-optimality of the $\sqrt{T}$ scaling.

2. **Discuss the effect of misspecifying $\iota$.** Provide a brief heuristic or bounding argument for how the regret degrades if the agent uses a conservative underestimate of $\iota$, showing the bound remains sublinear.

3. **Acknowledge the optimization tractability issue earlier** (in Section 4 when the algorithm is presented, not just in the conclusion).

4. **Expand the experimental section** with at least a variation in dimension or in the problem parameters to add credibility to the scaling predictions.

## Score and Decision

**Originality:** Good — the non-convexity bias and the local point assumption are genuinely novel contributions.
**Importance:** Solid — safe bandits in non-convex spaces are practically relevant and under-studied.
**Claims support:** Mixed — the upper bound is well-supported; the lower bound's interpretation is overstated relative to what the bound actually shows.
**Soundness:** The theoretical components appear correct; the main issue is the gap between claims and evidence for the lower bound.
**Clarity:** Generally clear, with helpful toy examples and visual intuition.
**Value:** The algorithm and upper bound are a meaningful step forward; the paper would be publishable after revisions tempering the lower bound claims.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>