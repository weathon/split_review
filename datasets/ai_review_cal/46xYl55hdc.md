- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 8, 6, 6
Now I have all the information I need. Let me produce the final consolidated review.

## Summary

This paper studies the vulnerability of multi-agent learning in strongly monotone games under bandit feedback. It proposes the Single-agent Utility Shifting Attack (SUSA), which poisons only one agent's utility observations and provably steers the learning dynamics away from the unique Nash equilibrium with sublinear total corruption cost. The paper also characterizes an efficiency-robustness trade-off showing that faster-converging algorithms are more vulnerable to such attacks, and provides a defense analysis for MD-SCB.

## Strengths

- **Provable single-agent attack with sublinear budget**: Theorem 1 provides explicit worst-case bounds for both the NE deviation lower bound (Eq. 10) and the expected total corruption cost (Eq. 11), demonstrating that SUSA succeeds against any (α,p)-MAL dynamics in strongly monotone games. The attack construction (Definition 5 via the Δ offset function) is elegant and the reasoning for why budget decays sublinearly is theoretically sound.

- **First characterization of the efficiency-robustness trade-off in multi-agent learning**: Corollary 2 derives quantitative bounds ρ(α) ∈ [1−α, 1−2α/3] linking the budget exponent to the convergence rate α, and Theorem 3 shows that by tuning the learning rate decay φ, MD-SCB can maintain convergence under general attacks at the cost of slower rates. The paper convincingly argues this is the first such trade-off characterization in multi-agent learning.

- **Welfare manipulation guarantee**: Theorem 2 and Corollary 1 provide a clean sufficient condition (non-zero gradient condition, Eq. 13) under which SUSA can strictly decrease any differentiable welfare function W, with a quantitative bound on the decrease. This goes beyond just shifting NE to directly manipulating socially-relevant metrics.

- **Empirical validation of core theoretical predictions**: Figure 2 confirms three key predictions: (1) SUSA steers MD-SCB away from the original NE, (2) the induced NE deviation shrinks with the number of agents n (consistent with Remark 1), and (3) faster-converging algorithms (larger α) incur smaller cumulative attack budgets (consistent with Theorem 1). Error bars from 20 runs are reported.

## Weaknesses

### Fatal

None.

### Major

- **Exponent inconsistency between Theorem 1 and Remark 1**: Theorem 1 (Eq. 11) gives a total budget bound of $T^{1-\frac{p\alpha}{p+1}}$, while Remark 1 states the bound as $\mathcal{O}(\sqrt{n}T^{1-\frac{p\alpha}{p+\alpha}})$. The exponents differ: with $p=2,\alpha=0.25$, the first yields $T^{5/6}\approx T^{0.833}$ and the second $T^{0.778}$ — a non-trivial gap. The proof sketch on line 174 uses $t^{-p\alpha/(p+1)}$, consistent with the theorem but not with the remark. This mathematical inconsistency must be resolved; it is unclear which formula is correct, and the discrepancy is unexplained. This undermines trust in the derived bounds.

- **Gap between the "ruin" claim and the minimum guaranteed deviation for large systems**: The lower bound on the NE deviation guaranteed by Theorem 1 scales as $O(n^{-1})$ for Cournot and $O(n^{-5/2})$ for Tullock contests. For the Tullock case with $n=100$, the minimum guaranteed deviation is $O(10^{-5})$, which is extremely small relative to typical action spaces. While the paper acknowledges this briefly (lines 166–167), it deflects by pointing to the multi-agent attack case (Section 4.2) rather than defending the single-agent claim. The title and abstract claim that the attack "suffices to ruin" multi-agent learning, but for large systems the guarantee may correspond to a practically insignificant shift. This is not a correctness issue, but a significant gap between the bold framing and the strength of the guarantees for the single-agent setting.

- **Narrow experimental scope**: The experiments are limited to one game (Cournot), one attack parameter ($\delta=10$), one algorithm (MD-SCB), and only test three convergence rates. No experiments on Tullock contests (mentioned in the theory), no variation of $\delta$, and no experiments with MAMD (the other algorithm discussed in the paper). The experiments thus confirm the qualitative predictions but provide limited independent validation of the broader theoretical claims.

### Minor

- **Strong assumptions limit practical relevance**: SUSA requires the adversary to have full knowledge of the victim agent's utility function and the ability to corrupt observations in real time. The paper acknowledges this (Section 7) and briefly suggests learning-based approaches as a path to relaxation, but does not develop this direction. Additionally, the theoretical guarantee (Theorem 1) is conditioned on the dynamics being $(\alpha,p)$-MAL, which requires last-iterate convergence — a property that many multi-agent algorithms do not satisfy. The paper is transparent about this scope but it narrows applicability.

- **The bound on the attack budget depends on unspecified constants**: Theorem 1's budget bound depends on Lipschitz constants $L_1$ and $L_2$ folded into $C_0$, but no explicit or game-specific expressions for $C_0$ are given (e.g., for Cournot or Tullock). This makes it hard to appreciate the concrete size of the budget in practice.

### Trivial

- The paper's text is occasionally garbled in the extracted version (presumably parser issues), but this does not affect the scientific content.

## Nice-to-Haves

- **Quantify "ruin" via downstream metrics**: Instead of reporting $L_2$ deviation alone, computing the change in social welfare or individual agent utilities under the attacked NE would make the practical impact clearer and better justify the title's claim.
- **Tighten the analysis of budget constants**: Providing explicit, game-specific bounds for $C_0$ in the attack budget (e.g., for Cournot and Tullock) would give the reader a concrete sense of how small the budget actually is.
- **Widen the experimental evidence**: Adding even a small Tullock contest experiment or testing a second $\delta$ value would strengthen the empirical support.

## Removed Points

These points were identified by reviewers but are removed from the main evaluation because they are factually incorrect, address parser artifacts, or stem from misunderstandings of the paper.

- *"The paper does not provide a path to relaxation of assumptions"* — **Removed (factually wrong).** The paper explicitly states (Section 7) that this assumption can be relaxed and suggests learning-based approaches as a future direction.
- *"Last-iterate convergence is a restrictive hidden assumption"* — **Removed (misunderstands scope).** Definition 4 and Theorem 1 explicitly condition on $(\alpha,p)$-MAL dynamics (which require last-iterate convergence). The paper is transparent that the guarantee applies only to algorithms with this property.
- *"Unstated Lipschitz constants make the bound opaque"* — **Downgraded to Minor.** The constants $L_1$ and $L_2$ are stated in Theorem 1, though game-specific values are not provided.
- *"Grammar/formatting/typo criticisms"* — **Removed (parser artifacts, not author errors).**

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface any observation about the paper that the authors themselves do not already discuss.

## Suggestions

1. **Resolve the exponent inconsistency** between Theorem 1 (Eq. 11) and Remark 1. Determine the correct formula and ensure consistency throughout the paper.
2. **Temper the title/abstract claims** about "ruining" learning to match the actual guarantee — for large $n$ in Tullock contests, the minimum guaranteed deviation is $O(n^{-5/2})$. A more precise qualifier (e.g., "can significantly disrupt nearest-optimal behavior under moderate $n$") would align the framing with the results.
3. **Provide game-specific expressions** for $C_0$ in Cournot and Tullock contests so readers can appreciate concrete budget scales.
4. **Add at least one additional experiment** (e.g., Tullock contest with small $n$, or a second $\delta$ value) to broaden empirical validation beyond Cournot.
