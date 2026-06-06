Now I have enough information to write a thorough final review. Let me synthesize the findings.

---

## Summary

This paper introduces Dig-DEC (Dual Information Gain Decision-Estimation Coefficient), a model-free DEC that removes the optimism mechanism of prior work [FGQ⁺23] and drives exploration via dual KL information gain. The paper makes three coordinated contributions: (1) proving Dig-DEC ≤ o-DEC with strict separation demonstrated on a bandit instance; (2) resolving the open problem in [LWZ25] by establishing the first model-free regret bounds for hybrid MDPs with bandit feedback under linear reward and general transition structures; and (3) improving online function estimation procedures—achieving Est ≲ √T via an unbiased split-sample estimator (Theorem 7), and Est ≲ log²|Φ| (constant in T) for Bellman-complete MDPs (Theorem 11)—yielding T^{2/3} and √T regret bounds respectively in Table 1.

---

## Strengths

1. **Dig-DEC provably dominates o-DEC with a demonstrated strict separation.** Theorem 13 establishes dig-dec ≤ o-dec + η for any D̄, and Theorem 14 constructs a concrete 3-armed bandit instance where [FGQ⁺23]'s algorithm suffers Ω(√T) regret while the proposed algorithm achieves regret ≤ 1. The separation mechanism is clearly explained: the KL information-gain term decomposes into a regularization component (which alone recovers o-DEC bounds) and a Shannon information-gain component (which enables strict improvement by capturing distributional differences that mean-based divergences cannot).

2. **Resolution of [LWZ25]'s open problem on model-free hybrid MDPs with bandit feedback.** Table 2 provides explicit regret bounds for hybrid bilinear classes and coverable MDPs under Assumptions 2–4. The structural reason the removal of optimism enables bandit feedback is clearly articulated in Section 2.2 and Section 6: optimism requires explicit reward estimator construction, which is incompatible with bandit observations, whereas the information-gain approach sidesteps this.

3. **Substantially improved estimation procedures with concrete technical novelty.** Theorem 7 achieves Est ≲ √T·N log|Φ| via an *unbiased* split-sample estimator (contrasted with [FGQ⁺23]'s biased squared estimator), producing T^{2/3} regret for bilinear classes and Q/V-type Bellman eluder MDPs. Theorem 11 achieves Est ≲ log²|Φ| (independent of T) for Bellman-complete MDPs, yielding √T regret — the first DEC-based method to match optimism-based approaches [JLM21, XFB⁺23] in this setting.

4. **Flexible general framework unifying prior approaches.** Equation (6) and Theorem 6 derive a regret decomposition via first-order optimality and Bregman divergence, bypassing the "constructive minimax theorem" of [XZ23], which was restricted to strictly convex divergences. Appendix C is cited as showing that the framework recovers [XZ23] and [LWZ25] results cleanly. This flexibility is the mechanism enabling both the generalized divergence D and the improved estimation procedures to coexist.

---

## Weaknesses

### Fatal
None.

### Major

- **The strict improvement of Dig-DEC over o-DEC is demonstrated only for a 3-armed bandit, not for any structured MDP.** This is the paper's central claimed advantage: Theorem 14 is decisive for bandits, but for all concrete MDP settings in Table 1, the Dig-DEC bounds have the same order as o-DEC. The T-dependence improvements in Table 1 derive from better Est bounds (Theorems 7 and 11), not from Dig-DEC being numerically smaller than o-DEC. The paper is not dishonest about this (Section 6 clearly distinguishes the two mechanisms), but the central thesis—that replacing optimism with information gain yields a fundamentally better complexity measure for MDPs—rests almost entirely on one bandit example. An MDP instance where the Shannon information-gain term in Dig-DEC is parametrically smaller than the optimism term in o-DEC would substantially strengthen the core contribution.

### Minor

- **The hybrid setting results (Table 2) require Assumption 4 (known linear reward features), a meaningful scope restriction.** The paper is transparent about this: Section 3.2 explicitly states the restriction and explains why unknown reward features would inflate log|Φ| polynomially under Assumption 3 (and that [LWZ25] shares this limitation). Given this transparency, the concern is mild — but the claim "first model-free bandit hybrid MDP bounds" technically applies only to the known-linear-reward regime, and this scoping should be stated more prominently in the abstract.

- **The use of "model-free" departs from standard RL terminology without early disambiguation.** Section 1 correctly clarifies that "model-free" here means regret independent of |M|, not that no model class is accessed. However, readers in adjacent fields will encounter the abstract first and may be misled. A one-sentence disambiguation in the abstract would eliminate this confusion.

### Trivial

None.

---

## Nice-to-Haves

- **An MDP-level example of strict Dig-DEC improvement.** Within the paper's own scope, a structured MDP (e.g., a small bilinear class or tabular MDP) where the KL information-gain term is parametrically smaller than the optimism term would transform Theorem 14 from a "bandit proof of concept" into an "MDP-relevant separation." This is the single change that would most strengthen the paper's central claim.

- **A worked trace through Table 2 for a simple hybrid MDP instance.** Given that Table 2 entries involve parameter combinations including H, d, and |A|, a brief worked example (e.g., a linear MDP with adversarial rewards) showing how the regret bound scales with a concrete parameter choice would help readers independently verify the hybrid-setting claims and understand their quantitative behavior.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Abstract and Table 2 exponent inconsistencies (parser artifacts).** The harsh critic flagged: (a) the abstract reporting T^{7/8} as an "improvement" over T^{5/6} in off-policy bounds (7/8 > 5/6); (b) Table 2 entries like T^{3/2} and T^{13/8} implying superlinear regret despite the paper claiming "first sublinear regret" in hybrid settings; (c) Section 4.2.1 writing "improves their rate of Est from √T to T^{1/2}" (these are identical). All of these are PDF parsing artifacts that garble fractional exponents—the original LaTeX submission does not have these errors. Table 1 (clearly readable from the extracted text) shows well-formed sublinear T^{2/3} and T^{1/2} bounds consistent with the paper's claims. Per hard rules, formatting artifacts are excluded from evaluation.

- **Reproducibility concerns (hyperparameter disclosure, implementation details).** Not raised explicitly but the harsh critic mentioned parsing issues preventing "independent verification." Per rules, reproducibility nitpicks about deferred appendix content are removed.

- **"Strengthening the Paper" requests framed as scope extension.** The hybrid setting's restriction to known linear reward features is not a flaw — it is a well-motivated technical scope choice with an honest explanation of the barrier (polynomial vs. logarithmic |Φ| scaling for unknown features). Criticizing its absence is scope creep, retained only as a nice-to-have.

- **Strength Finder strength: "framework generalizes and simplifies prior approaches."** This is a genuine contribution (Appendix C, Section 4) and kept. Generic strengths about the problem being "important" or "interesting" were not asserted, so no removal needed from strengths.

---

## Novel Insights

The conceptual heart of the paper is the decomposition of the KL divergence term in Dig-DEC into a *regularization* component (KL(ν_φ, ρ)) and a *Shannon information-gain* component (E[KL(ν_φ(·|π,o), ν_φ)]). Regularization alone recovers the bounds of optimistic DEC; the information-gain component enables strict improvement. This decomposition also explains why removing optimism enables bandit feedback in hybrid settings: the information-gain term measures genuine distributional differences in observations without requiring an explicit reward signal, whereas the optimism term in [FGQ⁺23] requires constructing a reward estimator to execute an optimistic policy update. The mirror-descent-based analysis (Equation 6) that makes this decomposition possible—bypassing the constructive minimax theorem of [XZ23]—is a methodological contribution likely to be reused in subsequent DEC-framework work.

---

## Suggestions

1. Add a structured MDP example (even a small tabular MDP or a parametric bilinear class) in which the KL information-gain term in Dig-DEC is provably smaller than the optimism term in o-DEC. Theorem 14's bandit example is clear and decisive, but a single MDP example would make the claim that "Dig-DEC is more than a bandit improvement" concrete.

2. Add a sentence in the abstract specifying that the hybrid MDP results assume known linear reward features (Assumption 4). The current abstract says "linear reward and several general transition structures" but does not flag the known-feature requirement, which is a non-trivial restriction.

3. Include a brief disambiguation of "model-free" in the abstract, consistent with Section 1's existing clarification, to prevent reader confusion from the paper's non-standard usage of the term.

---

## Score and Decision

**Originality (4/5):** The Dig-DEC concept—replacing optimism with dual information gain—is a genuine conceptual advance over [FGQ⁺23]. The unbiased split-sample estimator and the constant-Est two-timescale procedure are technically novel. The general framework with flexible Bregman divergence unifies prior approaches.

**Importance (4/5):** Resolves an open problem from [LWZ25], extends DEC-based learning to adversarial rewards with bandit feedback, and achieves √T regret via DEC for the first time in Bellman-complete MDPs.

**Claims supported (3/5):** The Est-improvement claims are fully supported by Theorems 7 and 11. Theorem 13 (Dig-DEC ≤ o-DEC) is straightforward. Theorem 14 (strict bandit separation) is concrete. However, the headline claim that Dig-DEC improves over o-DEC in MDPs is supported only by the bandit example—no MDP-level separation is demonstrated.

**Soundness (4/5):** The framework and analysis are coherent and internally consistent. The mirror-descent-based proof technique is clean. Table 2's parsing artifacts prevent full numerical verification of hybrid bounds, but the framework's structure supports the qualitative claims.

**Clarity (3/5):** Well-organized for a theory paper. Section 6's explanation of the Dig-DEC decomposition is the paper's clearest section. The parsing artifacts in Table 2 and the abstract reduce effective clarity.

**Community value (4/5):** Advances the DEC/E2D framework meaningfully, generalizes [LWZ25] and [FGQ⁺23], and provides improved estimation techniques with independent-interest potential.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>4</soundness>
<clarity>3</clarity>
<community_value>4</community_value>
</subscores>