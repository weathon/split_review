Now I have a comprehensive picture of the paper and the calibration landscape. Let me write the final consolidated review.

---

## Summary

This paper introduces Dig-DEC, a new model-free decision-estimation coefficient that replaces the optimism mechanism of prior DEC approaches with information-gain-driven exploration. The framework is applied to both stochastic and hybrid MDPs, yielding improved regret bounds for the stochastic setting and establishing the first model-free regret bounds for hybrid MDPs with bandit feedback under linear reward and several transition structures — resolving an open problem from [LWZ25]. The paper also refines online function-estimation procedures (unbiased batching estimator and improved two-timescale update) and proves that Dig-DEC is always no larger than optimistic DEC, with a strict separation example.

## Strengths

- **Theorem 13 and Theorem 14 provide a compelling theoretical advantage.** Theorem 13 proves that Dig-DEC ≤ optimistic DEC + η for any divergence, guaranteeing the new framework never does worse. Theorem 14 constructs a 3-armed bandit where optimistic DEC forces Ω(√T) regret while the Dig-DEC algorithm achieves constant regret — a clean separation result that strongly motivates the new approach.

- **First model-free regret bounds for hybrid MDPs with bandit feedback.** Under Assumptions 2–4, the paper instantiates Dig-DEC for hybrid bilinear classes and coverable MDPs (Table 2), obtaining explicit sublinear regret bounds that depend only on log|Φ|. This resolves the main open question from [LWZ25], which only handled the full-information case for model-free hybrid learning.

- **The general framework (Algorithm 1, Theorem 6) cleanly unifies prior DEC and AIR analyses.** The mirror-descent-style analysis via first-order optimality conditions (Eq. 5–6) is elegant and more flexible than the prior constructive minimax theorem approach. The framework admits arbitrary convex divergence measures and flexible posterior updates, and recovers results of [XZ23] and [LWZ25] as special cases.

- **Genuine algorithmic refinements in the estimation procedures.** The unbiased split-sample batching estimator (Section 4.2.1) improves over the biased estimator of [FGQ⁺23] by reducing variance. The redesigned two-timescale posterior update (Section 4.2.2) achieves a constant Est bound where prior work had T^{1/2}, enabling √T regret for Bellman-complete MDPs via a DEC-based method for the first time.

- **Broad applicability.** The framework is instantiated across bilinear classes, MDPs with bounded Bellman-Eluder dimension, and coverable MDPs, in both stochastic and hybrid settings (Tables 1–2), demonstrating the generality of the approach.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Inconsistency between the abstract and Table 1 in regret exponents.** The abstract claims improvement from T^{3/4} to T^{3/5} (on-policy) and T^{5/6} to T^{7/8} (off-policy), while Table 1 reports final regret bounds of T^{2/3} for both on-policy and off-policy bilinear classes. T^{2/3} ≠ T^{3/5}, and T^{2/3} ≠ T^{7/8}. For a paper whose main selling points include quantitative improvements in T-dependence, this makes it impossible to be confident in which specific exponents are correct. The core theoretical framework does not depend on these arithmetic details, but the inconsistency must be resolved.

- **Estimation procedure details are entirely deferred to the appendix.** The main text provides only high-level descriptions of the unbiased batching estimator (Section 4.2.1) and the two-timescale procedure (Section 4.2.2), while Algorithms 2–4 and their full analysis live in the stripped appendix. A reader of the main text must take the Est bounds (Theorem 7, Theorem 11) largely on faith.

### Trivial

- The sentence in Section 4.2.1 claiming improvement of Est "from √T to T^{1/2}" is tautological (these are the same quantity) — clearly a typo for the intended improvement.

## Nice-to-Haves

- **Computational feasibility discussion.** The framework assumes access to an oracle solving the minimax AIR problem (Eq. 3) at every round. While standard in the DEC literature, a brief acknowledgment of this information-theoretic nature and any prospects for efficient approximation would preempt a natural objection.

- The high-probability variants mentioned for the stochastic setting are only hinted at ("We remark without giving details"). Either elaborating or removing the remark would improve clarity.

## Removed Points

*These points are flagged to be removed — treat them with caution.*

- **"Improving T^{3/2} bounds to T^{3/2}" (harsh critic).** The introduction text reading "improve the T^{3/2}/T^{5/8} regret... to T^{3/2}/T^{5/6}" is a parser artifact — T^{3/2} is clearly garbled from T^{3/4} in the original LaTeX. This is not an author error. **Removed.**

- **"From √T to T^{1/2}" being identical (harsh critic).** Already captured above as a Trivial typo; the harsh critic elevated it to a structural concern, which is disproportionate. Downgraded.

- **"'Substantially simplify the analysis' claim not exemplified" (harsh critic).** Section 4 explicitly demonstrates how the first-order optimality analysis (Eq. 5–6) replaces the constructive minimax theorem, and the paper references Appendix C for recovering prior results. The claim is supported, not empty. **Removed.**

- **Missing related work / missing appendix criticisms.** Per instructions, parser strips appendices and we do not flag missing references. **Removed.**

- **High-probability variants "only hinted at."** The paper explicitly says "We remark without giving details" — this is a conscious scope limitation, not a hidden promise. Moved to Nice-to-Haves.

- **Strength: "This paper addresses an important problem" and similar generic framings from Strength Finder.** These are superficial and do not cite concrete evidence. **Removed from strengths.**

## Novel Insights

None beyond the paper's own contributions. The harsh critic and strength finder did not surface any genuinely new observations not already articulated by the paper itself.

## Suggestions

- Reconcile all regret exponents between the abstract, introduction, body text, and tables. If the correct on-policy bilinear bound is T^{2/3} (as Table 1 suggests), update the abstract accordingly. If rounding conventions differ, explain them explicitly.
- Add a short subsection or paragraph in the main text giving the precise definitions of Algorithms 2, 3, and 4 and a sketch of their key mechanisms, so the Est bounds are not purely appendix-dependent.
- Fix the "√T to T^{1/2}" typo.

---

## Calibration Report

**Round 1 bracket:** Based on the three bands, the paper clearly sits above the weak band (≤3.5) and plausibly in the 6.0–8.0 range. The 7.0 anchor (txD9llAYn9, model-based RL with horizon-free bounds) and 8.0 anchors (policy gradient for POMDPs, all-8s) framed the bracket.

**Round 2 narrowing:** Retrieved anchors in (5.5, 8.5) range with tighter topical relevance:

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| aPNwsJgnZJ | 6.00 | 2 | Horizon-free adversarial linear mixture MDPs. First result in its setting. Our paper has broader scope (stochastic + hybrid) and introduces a new fundamental concept. **Our paper is stronger.** |
| R4q3cYkQf | 6.75 | 2 | MaxInfoRL: information-gain exploration with bandit theory + deep RL experiments. Our paper is purely theoretical but deeper. **Comparable theoretical depth, our paper is more focused.** |
| txD9llAYn9 | 7.00 | 1 | Model-based RL with horizon-free bounds. Strong theory, some presentation concerns. **Our paper is comparable in contribution magnitude, slightly broader in settings covered.** |
| RMgqvQGTwH | 7.00 | 2 | Offline data enhanced on-policy PG. Hybrid RL with provable guarantees. **Comparable scope, our paper's theoretical machinery is more fundamental (new DEC concept).** |
| 8BAkNCqpGW | 8.00 | 1 | Policy gradient for confounded POMDPs. Novel identification, global convergence, all-8s. **Our paper's theoretical framing is comparably novel but presentation issues (exponent inconsistency) pull it slightly below this tier.** |

**Final score determination:** The paper introduces a new fundamental concept (Dig-DEC), resolves an open problem, provides strict improvement guarantees (Theorem 13, 14), and covers multiple settings. It is clearly stronger than the 6.00 anchor and comparable in contribution depth to the 7.00 anchors. The presentation inconsistency (abstract vs. table exponents) prevents it from reaching the 8.00 tier where presentation is uniformly clean. The score lands at **7.0**.

---

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>