Now I have a thorough understanding of the paper. Let me construct the final consolidated review.

---

## Summary

This paper theoretically analyzes the sensitivity of preference models (Bradley-Terry and Plackett-Luce) used in value alignment for LLMs. It shows that the probability of an unseen preference can become highly sensitive to small changes in other preferences when those preferences are dominant (probabilities near 0 or 1). The paper provides exact closed-form characterizations of the "M-sensitive" regions for both models, proves that K-tuple (K>2) Plackett-Luce models are more robust than pairwise Bradley-Terry models, and validates the pairwise sensitivity experimentally on DPO-trained Llama-3-8B.

## Strengths

1. **Exact, closed-form characterization of M-sensitive regions for Bradley-Terry (Proposition 1) and Plackett-Luce (Proposition 2) models.** Eqs. (6), (10)–(11) give concrete, analytic expressions for when and how severely robustness is compromised, enabling quantitative comparisons that go beyond heuristic observations.

2. **Theorem 2 (K>2 PL is strictly more robust than K=2 BT).** The proof uses series expansions of inverse hyperbolic functions to bound the BT sensitive area below and the PL area above, establishing a clean ranking. This is the paper's strongest theoretical result and is correctly proved.

3. **Empirical confirmation of pairwise sensitivity in a realistic LLM setting.** The experiment trains Llama-3-8B-Instruct with DPO on synthetic pairwise data and shows that small changes in training distribution induce large shifts in learned probabilities for an unseen pair. This grounds the theoretical analysis in a practical value-alignment context.

4. **Actionable practical implications.** Section 4 identifies a concrete robustness-versus-dominance trade-off (accept reduced robustness for narrow safety domains vs. weaken dominant preferences for general-purpose models) and suggests longer preference tuples as a mitigation. These connect the theory to practitioner concerns.

## Weaknesses

### Fatal

None.

### Major

1. **Quantifier error in Theorem 1 (general pairwise model).** The theorem statement reads "there exists $p_0, \ppr_{kj} < 1$ s.t. for all $p_0 < \ppr_{ik} < 1$, $\ppr_{ij}$ is $M$-sensitive to $\ppr_{ik}$" — implying a single fixed $\ppr_{kj}$ works for all $\ppr_{ik}$ in that range. However, the proof (line 202) constructs $\ppr_{kj} = g(g^{-1}(1-\ppr_{ik})+\delta)$, which makes $\ppr_{kj}$ a **function of $\ppr_{ik}$**. The quantifier order in the statement is therefore inconsistent with what the proof actually demonstrates. The result is correctly an **existence claim** about configurations where sensitivity arises, not a claim about arbitrary or realistic joint distributions. Since the paper immediately transitions to concrete models (BT, PL) where the analysis is rigorous and the proof errors do not propagate, this flaw does not threaten the paper's core contributions, but it is a genuine mathematical imprecision that should be corrected. The theorem should be restated to make the dependency of $\ppr_{kj}$ on $\ppr_{ik}$ explicit (e.g., "there exists $\delta>0$ and $p_0$ such that for all $\ppr_{ik} > p_0$, setting $\ppr_{kj} = g(g^{-1}(1-\ppr_{ik})+\delta)$ yields $|\partial\ppr_{ij}/\partial\ppr_{ik}| > M$").

### Minor

2. **Experiments cover only the pairwise (Bradley-Terry) case, not Plackett-Luce with K>2.** The core theoretical novelty regarding K-tuple PL models (Section 3.4) and the comparison in Theorem 2 receive no empirical support. Additionally, the paper acknowledges (line 425) that "not all significant changes occur in M-sensitive regions," attributing the gap to "biases in the LLMs and difficulties in optimization" without evidence. These gaps do not undermine the theoretical contribution (which stands on its own) but weaken the applied claims the paper uses the experiments to support.

3. **The claim that longer tuples monotonically improve robustness (Section 5.2) is heuristic, not a theorem.** The argument that increasing $K$ reduces the $M$-sensitive area because $\alpha$ grows and $\beta$ shrinks is directionally sound — adding positive terms to $\alpha$ and additional $(0,1)$ factors to $\beta$ both push the area in the right direction — and the dependence of ratios on score differences (not on $K$) is correctly noted. However, the paper does not provide a formal monotonicity proof for $K$ vs. $K+1$ (only the $K=2$ vs. $K>2$ case is rigorously proved in Theorem 2). The conclusion "yields more robust models" (line 394) is a plausible extrapolation, not a theorem. The language is already somewhat tentative ("suggests," "could mitigate") but the paper should either supply a formal proof or explicitly downgrade this to a conjecture.

4. **Area measure limitations not discussed.** The paper uses the Lebesgue measure of the $M$-sensitive region (treating all probability pairs uniformly) to quantify robustness. Real preference datasets are not uniformly distributed over $(0,1)^2$ — probabilities near 0 or 1 are common in RLHF data. The paper never acknowledges this choice or discusses how conclusions might change under an alternative weighting. Since Theorem 2 relies on this measure, the practical interpretation of "more robust" depends on it. This is standard mathematical practice for a first analysis, but an acknowledgment would strengthen the paper.

### Trivial

None.

## Nice-to-Haves

- A small-scale experiment with $K=3$ preferences (e.g., using a Plackett-Luce ranking approach) would strengthen the empirical connection to the PL results, though it is not required for the theoretical contribution.
- A discussion of how the Lebesgue measure choice affects the practical interpretation of the area comparisons in Theorem 2.

## Removed Points

- **Criticism that the symmetry assumption (Assumption 3) is too restrictive.** The paper focuses on Bradley-Terry and Plackett-Luce models anyway, both of which satisfy this assumption; the criticism evaluates the general analysis against models the paper does not actually use.
- **Criticism that the paper should add formal proof for the monotonicity of sensitivity area in $K$ for arbitrary fixed score differences.** This amounts to requesting a new theorem that the paper does not currently claim to have. The existing heuristic is clearly labeled as suggestive, and the request goes beyond reasonable scope for a single paper. The underlying concern (that the current reasoning is heuristic rather than proof) is already captured in Weakness #3.

## Novel Insights

None beyond the paper's own contributions. The reviewer inputs did not surface any novel observation about the theory or experiments that the paper itself does not already make.

## Suggestions

- **Fix Theorem 1's quantifier order.** Restate it to make explicit that $\ppr_{kj}$ is constructed as a function of $\ppr_{ik}$ in the proof, or rephrase as an existence claim about configurations rather than about a single fixed $\ppr_{kj}$. This is a small fix that removes a genuine imprecision.
- **Downgrade the K-monotonicity claim in Section 5.2** from "yields more robust models" to a clearly labeled conjecture, or supply a formal proof that for any fixed set of score differences, sensitivity area decreases monotonically with $K$.
- **Add a sentence acknowledging the area measure's limitations** (e.g., "This measure treats all probability pairs uniformly; in practice, the distribution of preferences may be concentrated near 0 or 1, which could affect the practical interpretation of area-based comparisons").
- **Tighten the experimental narrative.** Explicitly state that the experiments are designed to validate the pairwise (BT) predictions only, and that K-tuple PL validation is left to future work, rather than presenting the experiments as full support for all theoretical claims.

## Score and Decision

The paper makes a genuine theoretical contribution — the exact characterization of sensitivity regions for Bradley-Terry and Plackett-Luce models, and the proof that K-tuple models are strictly more robust than pairwise — that is valuable for the value-alignment community. The quantifier issue in Theorem 1 is a fixable imprecision, not a structural flaw, and does not affect the paper's main results. The experimental component is limited but appropriately positioned as a sanity check. With the minor corrections above, this would be a solid publication.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>