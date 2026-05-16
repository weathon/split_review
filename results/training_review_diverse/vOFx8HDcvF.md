Now I have a complete picture. Let me write the consolidated review.

## Summary
This paper provides a systematic theoretical study of stochastic multi-armed bandits under strong adversarial attacks (where the attacker observes both the pulled arm and realized reward before corrupting the observation). It covers four regimes: known/unknown attack budget C, with additive or multiplicative C dependence in the regret bounds. The paper proposes several algorithms (SEWR, SEWR-ST, PEWR, MSSEWR) with tight upper and lower bounds, and demonstrates a fundamental separation between the attack model and the better-studied corruption model.

## Strengths

- **Improved gap-dependent bound for the known-C case (Theorem 1).** The paper achieves \(O(\sum \log T/\Delta_k + KC)\), improving over Lykouris et al. (2018)'s \(O(\sum \log(KT/\delta)/\Delta_k + \sum C/\Delta_k)\) by eliminating the multiplicative \(1/\Delta_k\) dependence on the attack term. This bound matches the lower bound \(\Omega(\sum \log T/\Delta_k + KC)\), establishing optimality of SEWR for the known-C setting.

- **Tight gap-independent bounds across multiple regimes.** For known C, the bound \(O(\sqrt{KT\log T} + KC)\) matches the lower bound \(\Omega(\sqrt{KT} + KC)\) up to log factors. For unknown C, the phase elimination algorithm (PEWR) achieves \(\tilde{O}(\sqrt{KT} + KC^2)\), and the model selection algorithm (MSSEWR) with EXP3.P achieves \(\tilde{O}(KC\sqrt{T})\), each matching respective lower bounds in terms of T and C exponents.

- **Clear separation between corruption and attack models.** The paper shows the attack model incurs \(\Theta(KC)\) regret (K times worse than the \(\Theta(C')\) in the corruption model for known budget), and for unknown budget, attack forces an unavoidable \(KC^2\) term while corruption can achieve additive \(C'\). This is a structurally novel insight supported by both upper and lower bounds.

- **Novel algorithmic techniques for unknown attack budget.** The multi-phase elimination (PEWR) and model selection (MSSEWR) designs are elegant constructions that convert known-budget algorithms into unknown-budget ones while maintaining tightness. The PEWR analysis tightens a prior linear-bandit reduction by a factor of K on both the \(\sqrt{T}\) term and the \(C^2\) term.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Empty "Experiments" section is a presentational flaw.** The paper has `\section{Experiments}` followed by blank space and then "Conclusion Remark" with no experimental content. The paper is purely theoretical and makes no empirical claims in its abstract or contributions, so this does not undermine the core contribution. However, the empty section heading and the forward references to empirical performance (e.g., "Practically, SEWR should have better empirical performance than that of SEWR-ST" in Remark 1) are sloppy. The section should either be filled with synthetic simulations validating the regret bounds, or removed entirely along with any empirical-language phrasing.

- **Tightness claims for unknown-C additive bound could mislead casual readers.** The paper states (line 366) that the PEWR upper bound is "tight in terms of both T and C" by comparing to Proposition 4's \(\Omega(\sqrt{T}+C^2)\). However, this lower bound applies only to algorithms whose regret admits an additive decomposition \(O(T^\alpha + C^\beta)\), not to all algorithms. The general lower bound (Proposition 3) gives \(\Omega(KC)\), not \(\Omega(KC^2)\), leaving a genuine gap: can one achieve \(\tilde{O}(\sqrt{KT} + KC)\) for unknown C? The paper does acknowledge this gap in a footnote (line 101) and the table caption, but the main text's phrasing ("tight in terms of both T and C") could be read as claiming general optimality. A brief discussion of whether \(KC\) is achievable for unknown C (or why the \(C^2\) dependence may be fundamental given the attack model's power) would significantly strengthen the presentation.

### Trivial
- The paper lacks a "Limitations" paragraph in the conclusion. A brief discussion of the model assumptions (budget defined as sum of absolute deviations, assumption that \(C\) is known in Sections 4.1–4.2) would improve completeness.
- The conclusion is a single sentence; a short summary of open questions would be helpful.

## Nice-to-Haves
- Synthetic simulations validating the regret scaling (e.g., plotting regret vs. T for fixed C, or vs. C for fixed T) would confirm the theory, though not required for a theory paper.
- A brief runtime/complexity note for the proposed algorithms would be useful but is not standard for theory papers.

## Removed Points
These are flagged to be removed per the filtering instructions; treat them with caution if referenced:
- **"Figure 2 implies empirical validation."** Removed. The figure compares regret exponents theoretically (Remark 6 explains this clearly). There is no implication of empirical results.
- **"Proposition 4's restricted scope is not explicitly noted."** Removed. The paper explicitly states in the table caption (line 67–68), the section intro (line 179), and the footnote (line 101) that these lower bounds are for special classes of algorithms.
- **"Missing related works."** Per the review guidelines, I cannot verify existence of missing citations.
- **"No runtime/complexity analysis."** Not a standard expectation for theory papers. Removed.
- **"Formatting/style nitpicks."** Removed per instructions.

## Novel Insights
The reviews surface one genuinely novel observation beyond the paper's own contributions: the paper's analysis shows that the phase elimination technique from linear bandits (Bogunovic et al., 2020) can be tightened by a factor of \(K\) when specialized to multi-armed bandits, because the tighter confidence radius in SEWR (which removed the \(\Delta_k\)-dependence on the attack term) propagates through the multi-phase construction. This insight explains why naively reducing linear-bandit results to MAB yields suboptimal bounds, and it highlights the value of problem-specific analysis even when generic reduction strategies exist. The reviews do not reveal any other insight beyond what the paper itself already articulates.

## Suggestions
- Either remove the empty "Experiments" section and its forward references, or add synthetic simulations that validate the regret scaling of the proposed algorithms.
- Add a paragraph after the tightness discussion for the unknown-C additive bound (around line 366) clarifying: (1) the lower bound in Proposition 4 is conditional on the additive form \(O(T^\alpha + C^\beta)\); (2) whether closing the gap between \(\Omega(KC)\) (general lower bound) and the achieved \(KC^2\) is possible remains open.
- Add a brief limitations paragraph to the conclusion discussing the model assumptions.

## Score and Decision

MY FINAL SCORE: <pineapple>4.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>