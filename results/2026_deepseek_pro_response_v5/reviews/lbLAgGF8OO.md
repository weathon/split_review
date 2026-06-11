---

## Summary

This paper introduces Dig-DEC, a new model-free decision-estimation coefficient that replaces the optimism principle used in prior DEC-based algorithms with dual information-gain terms (KL divergence plus estimation-error divergence), enabling exploration driven purely by information gain. The framework generalizes the Algorithmic Information Ratio (AIR) approach to arbitrary convex divergences with a mirror-descent-style analysis. The paper applies Dig-DEC to obtain the first model-free regret bounds for hybrid MDPs with bandit feedback (resolving an open problem from LWZ25), achieves √T regret in Bellman-complete MDPs (matching optimism-based methods for the first time within the DEC framework), and improves online function estimation through an unbiased split-sampling estimator and a refined two-timescale posterior update procedure.

## Strengths

- **Resolution of the LWZ25 open problem**: The paper provides the first model-free regret bounds for hybrid MDPs with bandit feedback (Table 2). This is enabled by removing optimism (which required explicit reward estimator construction) and replacing it with information-gain-driven exploration. Concrete advance: prior work could only handle full-information feedback in this setting.

- **Dig-DEC is provably never worse than optimistic DEC**: Theorem 13 establishes dig-dec ≤ o-dec + η for any divergence D. Theorem 14 provides a concrete 3-armed bandit where Dig-DEC achieves O(1) regret while optimistic DEC suffers Ω(√T). This is a rigorous theoretical separation, not just an upper-bound comparison.

- **First DEC-based method achieving √T regret in Bellman-complete MDPs**: Theorem 11 shows the Est term can be bounded by log²|Φ| (constant in T), enabling overall regret of H√(dT)log|Φ| for BE Q-type and coverable MDPs (Table 1, rows with D_sq). This matches optimism-based approaches for the first time within the DEC framework, whereas prior DEC-based work only achieved T^(5/6).

- **Unbiased split-sampling estimator with sharper concentration**: Section 4.2.1 constructs an unbiased estimator L_h(φ) = Σ_h (2/τ Σ_{i=1}^{τ/2} ℓ_h)(2/τ Σ_{i=τ/2+1}^τ ℓ_h) by splitting each batch, improving over FGQ+23's biased squared-mean estimator. This yields improved regret rates (from T^(3/4) to T^(3/5) on-policy, from T^(5/6) to T^(7/8) off-policy, per the abstract).

- **Generalized AIR framework with flexible divergence and Bregman analysis**: Algorithm 1 and the analysis (Eqs. 5-6) introduce a general convex divergence D into the AIR objective, using Bregman divergence to connect to mirror descent. This replaces the restrictive "constructive minimax theorem" of XZ23/LWZ25 and recovers their results as special cases.

- **Insightful KL decomposition explaining the improvement over optimism**: Section 6 decomposes the KL term into regularization (KL(ν_φ, ρ) — replacing the optimism term V_φ(π_φ) in Eq. 9) and information gain (KL(ν_φ(·|π, o), ν_φ) — capturing distributional differences that mean-based divergences like bilinear divergence or squared Bellman error miss). This provides a clear conceptual understanding of *why* optimism can be removed and *when* improvements arise.

- **Broad applicability across diverse canonical MDP classes**: The paper instantiates Dig-DEC across bilinear classes (on/off-policy), Bellman-eluder dimension (Q/V-type), and coverable MDPs in both stochastic and hybrid settings (Tables 1-2, Lemmas 8, 12).

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **Regret derivation from stated bounds is not self-contained in the main text.** Theorem 7 gives Est ≲ N log|Φ| T^(1/2), and for the D_av rows in Table 1 dig-dec scales as O(η). With the regret formula T·dig-dec + Est/η, a straightforward η-optimization yields T^(3/4), yet Table 1 reports T^(2/3). The resolution — which likely involves the batching parameter τ introducing additional degrees of freedom in the optimization (via Algorithm 4) — is deferred entirely to the appendix. While standard for theory papers, the jump from Theorem 7 to the table's regret rates is not explained, leaving the reader to reverse-engineer the claimed improvement.

- **Theorem 14 separation is limited to a 3-armed bandit.** The strict improvement over optimistic DEC is demonstrated only in a toy bandit with no state, no horizon, and a specific distributional structure. The paper does not discuss whether analogous separation exists in any of the MDP settings (bilinear classes, Bellman-eluder, coverability) that constitute the paper's main applications. This leaves the practical significance of the KL information-gain term for structured MDPs ambiguous.

- **Abstract slightly overstates the LWZ25 resolution.** The abstract states Dig-DEC "resolves the main open problem left by [LWZ25]" without qualification. The paper itself acknowledges (lines 115-117) that Assumptions 3-4 restrict to known linear reward features, and that hybrid low-rank MDPs with unknown reward features are not captured. Since LWZ25 shared these same limitations even in their full-information results, the overstatement is mild, but the abstract would benefit from a brief qualifying phrase.

### Trivial

- Line 33 in the introduction has parser-garbled T-exponents: T^(3/2) appears where a sublinear rate was intended (should be T^(3/4), matching the abstract's statement of improving *from* T^(3/4)). Similarly, line 213 states Est improves "from √T to T^(1/2)" — these are the same quantity, clearly a parser artifact. These are presentation artifacts from PDF extraction, not author errors, but should be corrected in the final version.

## Nice-to-Haves

- Provide an MDP (not bandit) example where the KL term yields a strict improvement over optimistic DEC, to demonstrate the practical value of the information-gain term beyond the toy bandit.
- Walk through the η-optimization for one row of Table 1 in the main text to make the Est→regret derivation self-contained.
- Discuss which natural MDP classes satisfy Bellman completeness (Definition 10) in the hybrid setting alongside Assumptions 2-4.

## Removed Points

These points are flagged to be removed, treat them with caution.

- **Harsh Critic claim: "Parser corruption makes quantitative claims unverifiable"** — REMOVED. The T-exponent garbling in the introduction (line 33) and Table 2 is a parser artifact. The abstract and Table 1 render proper sublinear rates, and the introduction's T^(3/2) is clearly a corrupted rendering of T^(3/4) (matching the abstract's "improving from T^(3/4)"). This is a formatting/parser issue, not a paper problem.

- **Harsh Critic claim: "Inconsistency across abstract, introduction, and tables makes numerical claims unverifiable"** — REMOVED for the same reason. The inconsistencies are parser artifacts, not genuine disagreements in the paper. The abstract, Table 1, and Table 2 (when parser-rendered correctly) would be internally consistent.

- **Harsh Critic concern about missing appendix, Lemma 18, Lemma 29, Lemma 36, and Algorithm descriptions (2, 3, 4)** — REMOVED per instruction: "REMOVE weaknesses about missing appendix, missing proofs in appendix, or absent references. The parser strips those sections from all papers; they exist in the original submission."

- **Strength Finder: "Resolution of the open problem" described as unconditional** — Adjusted. The paper resolves the open problem under the same assumptions LWZ25 used for their full-information results, which is accurate but deserves qualification in the abstract.

## Novel Insights

The decomposition of the KL term into regularization (KL(ν_φ, ρ)) and information gain (KL(ν_φ(·|π, o), ν_φ)) in Section 6 provides a genuinely novel lens for understanding what optimism was doing in prior DEC frameworks: the regularization term alone can replace the optimism mechanism (enabling handling of adversarial/hybrid settings where explicit reward estimators are unavailable), while the information-gain term captures distributional differences that mean-based divergences miss (enabling strict improvements). This decomposition makes clear *why* removing optimism is possible and *when* it leads to improvements — an insight that could guide future work in DEC-based exploration beyond the specific settings studied here.

## Suggestions

- In the abstract, add a brief qualifying phrase for the LWZ25 resolution, e.g., "under the same linear reward assumption as their full-information results."
- Walk through one η-optimization derivation in the main text (Section 5) to make the Est→regret step self-contained for the reader.
- Consider adding even a constructed MDP example (beyond the bandit) where Dig-DEC strictly improves, to strengthen the case that the KL term matters in structured RL settings.

## Score and Decision

**Anchor Comparison:**

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| SQT rough conservative actor critic | hMjUnF3aQ8 | 2.00 | R1 | Much weaker; limited novelty, empirical-only |
| Regret measure continuous bandit | 4jzjexvJ7I | 2.33 | R1 | Much weaker; narrow scope, limited contribution |
| Value-Biased MLE for linear MDPs | 2h3m61LFWL | 4.25 | R1 | Weaker; limited novelty, rejected |
| Model-Free BPI in Online CMDPs | w8Zo7jACq7 | 5.20 | R1 | Weaker; stronger assumptions, partial novelty, rejected |
| Horizon-free RL Adversarial Linear Mixture | aPNwsJgnZJ | 6.00 | R1 | Comparable but our paper is broader (stochastic+hybrid, more MDP classes) and has a more elegant conceptual framework |
| Multi-Batch RL Lower Bounds | ey3GhWXQ97 | 6.33 | R2 | Comparable; both have novel theoretical insights with some scope limitations |
| Pessimistic Nonlinear LSVI | 4kLVvIh8cp | 6.25 | R2 | Comparable; solid theory paper with accept |
| Demonstration-Regularized RL | lF2aip4Scn | 6.50 | R2 | Comparable; our paper has broader applicability |
| Robust Bandits to Adversarial Attacks | vOFx8HDcvF | 6.50 | R1 | Comparable but different style (bandits + experiments vs. pure MDP theory) |
| Model-based RL Minimalist Horizon-Free | txD9llAYn9 | 7.00 | R1 | Stronger; delivers horizon-free AND second-order bounds, more surprising result |
| Robust RL Adaptive Defense | DFTHW0MyiW | 7.00 | R1 | Stronger; theory + strong empirical validation |

**Round 1 bracket:** 5.5–7.0. The paper is clearly stronger than the 5.20 rejected anchor and comparable-to-stronger than the 6.00 accepted anchor, but not at the 7.00 level.

**Round 2 narrowing:** Within the 5.5–7.0 bracket, the paper compares favorably to the 6.25–6.33 anchors. It has comparable theoretical depth but broader applicability (stochastic + hybrid, multiple MDP classes). The 6.50 anchors are the closest match — "Demonstration-Regularized RL" has similar scope and theoretical contribution level. Our paper's conceptual framework (Dig-DEC, KL decomposition) and resolution of an open problem are slightly more significant contributions, but the minor weaknesses (non-self-contained derivation, bandit-only separation) temper this.

**Final score: 6.5.** The paper makes a genuine and significant theoretical contribution — introducing a new model-free DEC that replaces optimism with information gain, resolving an open problem in hybrid MDPs, and achieving √T regret in Bellman-complete MDPs. The conceptual framework is elegant and the KL decomposition provides real insight. The minor weaknesses do not undermine the core contributions but prevent the paper from reaching the top tier.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>