Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper introduces Dig-DEC (Dual Information Gain Decision-Estimation Coefficient), a new model-free complexity measure for decision-making with structured observations. Unlike prior optimistic-DEC approaches [FGQ⁺23] that rely on optimism to drive exploration, Dig-DEC replaces optimism with two information-gain terms (KL regularization + KL information gain). The paper shows Dig-DEC is always no larger than optimistic DEC (Theorem 13), achieves improved regret bounds in stochastic settings (e.g., √T for Bellman-complete MDPs, Table 1), and — most significantly — provides the first model-free regret bounds for hybrid MDPs with bandit reward feedback (Table 2), resolving an open problem from [LWZ25]. The framework also refines online function estimation with an unbiased estimator construction.

## Strengths

1. **Novel complexity measure strictly generalizing prior work (Theorem 13, Section 6).** Theorem 13 proves Dig-DEC ≤ optimistic DEC + η for any divergence D̄, establishing that the new complexity is never worse than prior optimistic DEC and can be strictly smaller. The 3-armed bandit example (Theorem 14) demonstrates an instance where optimistic DEC suffers Ω(√T) regret while Dig-DEC achieves ≤ 1 regret — the improvement can be arbitrarily large.

2. **First model-free regret bounds for hybrid MDPs with bandit feedback (Table 2, Section 5.2).** Table 2 gives explicit sublinear regret bounds for hybrid bilinear classes and coverable MDPs under linear reward with bandit feedback (e.g., Õ(T³ᐟ²) for on-policy bilinear classes). This resolves the main open problem left by [LWZ25], who only handled the full-information case. The removal of optimism is key here, as optimistic DEC requires an explicit reward estimator that is unavailable under bandit feedback.

3. **Improved regret rates in the stochastic setting (Table 1, Section 5.1).** For Bellman-complete MDPs with squared estimation error, the regret improves from T⁵ᐟ⁶ (FGQ⁺23) to √T — the first time a DEC-based method matches optimism-based approaches. For bilinear classes with average estimation error, the rate improves from T³ᐟ⁴ to T²ᐟ³.

4. **Unbiased estimator and refined analysis (Section 4.2.1).** The paper constructs an unbiased estimator for the average estimation error by splitting each epoch's samples into two halves, in contrast to the biased estimator of [FGQ⁺23]. This refinement, along with the new Bregman-based analysis framework (Section 4), allows the algorithm to handle a general divergence D and recovers prior AIR results [XZ23, LWZ25] with a simpler algorithm.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Scaling of |Φ| not discussed in the main text.** The regret bounds in Tables 1 and 2 depend on log|Φ|, where |Φ| is the size of the value-function partition. The paper does not discuss how |Φ| scales with natural problem parameters (number of features, horizon, state/action spaces) in the settings it considers. For infinite function classes requiring discretization, this could be substantial. This omission makes it difficult to assess the practical tightness of the bounds. A brief discussion of how |Φ| relates to standard quantities (e.g., covering numbers) would strengthen the presentation.

2. **Motivation for the specific divergence form in Eq. (7) could be clearer.** The chosen divergence D^π(ν‖ρ) contains both a KL information-gain term and a D̄ discrepancy term. The paper states the KL term serves "regularization" purposes and the D̄ term captures estimation error, but the necessity of having both terms (rather than just one) and their interaction is not fully explained. A more detailed intuition linking this specific form to the prior DEC/AIR definitions would help readers understand the design choices.

3. **High-probability bounds mentioned but not developed.** A single paragraph (end of Section 5.1) states that "in the stochastic setting, we can achieve same results with high-probability" by modifying the divergence, but notes this variant "cannot handle the hybrid setting." Since the adversarial hybrid setting would especially benefit from high-probability guarantees, and since prior work often provides such guarantees, this is a limitation worth noting.

4. **Scope limitations honestly acknowledged but restrict generality.** Assumption 3 (unique reward-to-value mapping given φ) and Assumption 4 (known linear reward features) do not cover all learnable hybrid MDPs — e.g., low-rank MDPs with unknown reward features as noted by the authors. While the paper is transparent about this (Section 3.2), and the same limitation appears in [LWZ25], it means the resolution of the open problem is partial.

### Trivial
None.

## Nice-to-Haves

- A brief calculation in the main text showing how the final regret exponents in one representative row of Table 1 follow from the stated dig-dec and Est bounds, to make the link more transparent.
- A discussion of other possible divergences (χ², Hellinger) that could be used in the general D framework beyond D̄_av and D̄_sq.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **Abstract/Table 1 inconsistency (regret rates).** The harsh critic flags that the abstract claims T³ᐟ⁵ / T⁷ᐟ⁸ while Table 1 shows T²ᐟ³. Reason for removal: Line 39 of the parsed text shows clearly garbled fractions ("T^{3/2}/T^{5/8}" → "T^{3/2}/T^{5/6}"), where T^{3/2} is impossible as a regret bound exponent — evidence of systematic PDF-to-text fraction corruption. The abstract and Table 1 numbers would be consistent in the original submission; the parsed garbling is not an author error.

2. **Missing derivation from Theorem 7 to Table 1 entries.** Reason for removal: The paper states "Dig-DEC bounds are provided in Appendix H.3 for bilinear classes, Appendix H.4 for BE, and Appendix H.5 for coverable MDPs." The appendix exists in the original submission and contains these derivations. Per the evaluation protocol, missing content in the stripped appendix is not a valid criticism.

3. **Est improvement claim ("from √T to T^{1/2}").** Line 219 says the rate improves from "√T to T^{1/2}" — these are the same order. Reason for removal: Given the systematic fraction garbling on line 39, this is almost certainly a parser artifact where the original had a different exponent.

4. **Questioning the "model-free" terminology.** Not a substantive criticism; the paper explicitly defines its use of the term on lines 43.

## Novel Insights

None beyond the paper's own contributions. The harsh critic and strength finder did not surface any perspective on the paper that the authors themselves do not already articulate.

## Suggestions

- Add a short paragraph or footnote in the main text discussing how |Φ| scales with standard problem parameters (e.g., covering number arguments for continuous function classes), to help readers assess the practical implications of the bounds.
- Expand the intuition behind Eq. (7)'s divergence form, perhaps with a brief comparison to the standard AIR (KL-only) and optimistic DEC (D̄-only) formulations, explaining why both terms are needed and what each contributes.

## Score and Decision

### Calibration Summary

**Round 1 — Bracketing:**
| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| /home/.../BN4vhB5IRy.md | 3.20 | R1 weak | Deployment-efficient RL; less relevant, lower quality |
| /home/.../fE0RJto3Na.md | 6.50 | R1 mid | Tabular model-free RL with gap-dependent bounds; comparable contribution depth |
| /home/.../kW0SudrQEQ.md | 6.00 | R1 mid | Linear Q^π realizability; similar theoretical rigor |
| /home/.../l8YvuTQ0FA.md | 5.50 | R1 mid | Exogenous MDPs; narrower scope, stronger assumptions |
| /home/.../xIycolc5Xw.md | 7.00 | R1 mid | Fixed-budget exploration; cleaner/ tighter results |
| /home/.../oBXfPyi47m.md | 8.00 | R1 strong | World models; applied RL, different methodology |

**Round 1 bracket:** 3.5–7.5 (clearly not in weak or top-tier range given the paper's theoretical contribution).

**Round 2 — Narrowing:**
| Anchor | Avg Score | Comparison |
|--------|-----------|------------|
| /home/.../fE0RJto3Na.md | 6.50 | Comparable — both make clear theoretical contributions; this paper has broader scope but no experiments |
| /home/.../kW0SudrQEQ.md | 6.00 | Comparable — both strong theory papers; this paper has wider applicability |
| /home/.../KASqlcI6Nm.md | 6.00 | Bayesian RL with epistemic uncertainty; similar level of theoretical contribution |
| /home/.../xCelVyUVO2.md | 6.50 | Multi-model RL; comparable theoretical depth and generality |

The paper is stronger than the 5.50 anchor (exogenous MDPs — more restrictive assumptions, narrower scope) and comparable to the 6.00–6.50 anchors. It is somewhat weaker than the 7.00 anchor (which had tighter results and a cleaner presentation). The paper's scope (resolving an open problem from LWZ25, providing a unified framework covering both stochastic and hybrid settings) argues for the upper end of this range.

**Final Score: 6.0** — Solid theoretical contribution with meaningful results (novel complexity measure, first model-free hybrid bandit bounds, improved stochastic bounds). The paper is let down slightly by minor presentation gaps (scaling of |Φ| not discussed, intuition for divergence form could be clearer) and the lack of developed high-probability bounds, but none of these undermine the core contributions.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>