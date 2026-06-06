## Summary
This paper introduces Dig-DEC (dual information gain decision-estimation coefficient), a model-free complexity measure for decision-making that removes the optimism mechanism of [FGQ+23] and instead drives exploration through KL information gain. The paper proves Dig-DEC ≤ o-DEC (Theorem 13) with a strict 3-armed bandit separation (Theorem 14), achieves the first model-free regret bounds for hybrid MDPs with bandit feedback (resolving an open problem in [LWZ25]), and improves estimation procedures to achieve constant Est for Bellman-complete MDPs (Theorem 11).

---

## Rebuttal Assessment

### Weakness: Strict improvement of Dig-DEC over o-DEC shown only for a 3-armed bandit, not for any MDP

- **Author's response:** Partially address
- **Assessment:** Partially convincing — The author correctly points to Section 6's decomposition of the KL term into regularization (KL(ν_φ, ρ)) and information gain (E[KL(ν_φ(·|π,o), ν_φ)]) components, which is indeed present in the paper at the paragraph following Theorem 13. The theoretical argument that this information gain term "can capture" distributional differences ignored by mean-based divergences is in the paper. However, I verified that the paper itself explicitly says "We give a *toy example* in the next theorem to show this" (referring to Theorem 14, the 3-armed bandit). This means the paper's own framing limits the concrete separation to the bandit setting. The author's claim that the Table 1 improvements partially come from Dig-DEC's structure is somewhat circular — it's the constant Est enabled by the redesigned PosteriorUpdate procedure, not Dig-DEC being numerically smaller than o-dec, that drives the improvement. The weakness stands but is mitigated by the presence of the theoretical mechanism in Section 6.
- **Score impact:** Weakness unchanged

### Weakness: Hybrid setting results limited to known linear reward features (Assumption 4)

- **Author's response:** Refute (on prominence); Acknowledge (on scope itself)
- **Assessment:** Partially convincing — I verified that the abstract (line 11) does contain "under linear reward" and that Section 3.2 (lines 115–117) explicitly states "we consider linear reward with known features." Section 3.2 also contains a two-paragraph discussion of why this restriction is necessary and why the [LMWZ24] case (unknown features) remains out of scope. The abstract's phrase "under linear reward" is present but is slightly imprecise — it doesn't explicitly convey that the features must be *known* to the learner, which is the more restrictive aspect of Assumption 4. Still, the paper does honestly disclose the limitation in Section 3.2, and the reviewer's original concern about prominence is largely addressed.
- **Score impact:** Weakness downgraded (from Minor to Trivial)

### Weakness: "Model-free" terminology differs from common RL usage

- **Author's response:** Refute
- **Assessment:** Convincing — I verified that Section 1 (line 37) contains an explicit clarification: "the term 'model-free' learning in our work does not mean that the learner has no access to the model class M or has computational constraints. Instead, it only means that the regret bound is independent of the size of the model set M." This matches the reviewer's suggested remedy, and placing it in Section 1 (where a reader encountering the term in the abstract/title would naturally look next) is appropriate.
- **Score impact:** Weakness removed (was already Trivial)

---

## Strengths

- **Dig-DEC ≤ o-DEC with concrete separation (Theorems 13 and 14):** Theorem 13 establishes dig-dec ≤ o-dec + η for any D̄. Theorem 14 provides a 3-armed bandit with Ω(√T) lower bound for [FGQ+23] while the proposed algorithm achieves ≤ 1.
- **Resolution of open problem in hybrid MDPs (Table 2):** The first model-free regret bounds for hybrid bilinear classes and Bellman-complete coverable MDPs with bandit feedback under linear reward.
- **Improved estimation procedures (Theorems 7 and 11):** The split-sample unbiased estimator of Section 4.2.1 improves Est over [FGQ+23]'s biased estimator. Theorem 11 achieves Est ≲ log²|Φ| (constant in T), enabling √T regret for Bellman-complete MDPs — the first DEC-based method to match optimism-based approaches.
- **Unified framework generalizing AIR:** Equation (2) generalizes [XZ23] and [LWZ25]'s KL-specific AIR to general Bregman divergences, with a mirror-descent-based analysis that avoids the "constructive minimax theorem" of [XZ23] and recovers prior results as special cases.

---

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Strict improvement of Dig-DEC over o-DEC is demonstrated only for a 3-armed bandit.** For Table 1's stochastic MDP settings, the T-dependence improvements derive from improved estimation procedures (Theorem 7, Theorem 11) and the redesigned PosteriorUpdate, not from Dig-DEC being numerically smaller than o-dec in those settings. The paper itself frames the separation as a "toy example" (before Theorem 14). The theoretical mechanism in Section 6 is present and compelling, but no MDP-level parametric separation is demonstrated.

### Trivial

- **Assumption 4 scope restriction is not maximally precise in the abstract.** The abstract says "under linear reward," which covers the known-features restriction, but a reader familiar with linear MDPs with unknown features might not immediately recognize this scoping. Section 3.2 provides a full disclosure and honest comparison with [LMWZ24].
- **Abstract exponent comparisons have parser artifacts** (e.g., "T^{5/6} to T^{7/8}" in off-policy appears regressive; "√T to T^{1/2}" in Section 4.2.1 appears identical). These are formatting corruptions of fractional exponents and do not reflect errors in the underlying mathematics.

---

## Nice-to-Haves

- An MDP-level example (even a simple contextual bandit or linear MDP) where dig-dec is provably smaller than o-dec parametrically would move the Dig-DEC contribution beyond "bandit-only" and substantially strengthen the headline claim.
- Clarify in the abstract that Assumption 4 requires features to be *known* to the learner (not just that rewards are linear), to sharpen the scope of the hybrid result.
- Clarify in the introduction which Table 1 improvements come from Dig-DEC being smaller vs. from improved estimation — the two contributions are currently presented together and the distinction is blurred.

---

## Novel Insights
The paper's structural insight — that removing optimism from the DEC objective is possible because KL regularization (KL(ν_φ, ρ)) alone recovers o-dec bounds, while the information gain term (E[KL(ν_φ(·|π,o), ν_φ)]) enables strict improvement — cleanly explains why DEC-based methods have historically required optimism and how it can be avoided. Crucially, this removal of optimism is not merely an aesthetic simplification: it is the structural property that eliminates the need for an explicit reward estimator when handling adversarial reward feedback in hybrid MDPs. The Bregman divergence generalization of AIR (Equation 2) provides a cleaner proof path via mirror descent that bypasses the "constructive minimax theorem" of [XZ23], potentially enabling future extensions to settings where that theorem does not apply.

---

## Suggestions

1. Add an MDP-level example (even in a short remark or corollary) where Dig-DEC is strictly smaller than o-DEC, to substantiate the claim beyond the 3-armed bandit setting.
2. Replace "under linear reward" in the abstract with "under known linear reward features" to accurately scope Assumption 4.
3. Provide a numerical worked example tracing the hybrid bilinear Table 2 rate for a concrete linear MDP, to help readers independently verify the H, d, |A| dependence.

---

## Score and Decision

The rebuttal is honest and competent. The key weakness (bandit-only separation for Dig-DEC as a complexity measure) is acknowledged by the authors and partially addressed by pointing to the theoretical mechanism in Section 6 — but the paper's own language ("toy example") confirms this is the current state. The Assumption 4 scope weakness is largely refuted since "under linear reward" is in the abstract and Section 3.2 provides full disclosure. The terminology weakness is resolved.

The original score of 7.0 was well-calibrated. The rebuttal does not uncover significant errors in the original review, nor does it fully overcome the main weakness. No change to the score is warranted.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>