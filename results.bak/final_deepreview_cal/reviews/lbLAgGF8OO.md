Now I have a clear picture of the calibration landscape. Let me write the consolidated review.

**Bracket (Round 1):** Between 4.5 and 7.0 — clearly stronger than the 2.0-3.2 papers, but with a notable presentation flaw.

**Narrowing (Round 2):** The paper is stronger than the 4.25-5.75 reject-range anchors (Value-Biased MLE, CMDP, Trajectory Feedback, Extensive-Form Games) due to its novel framework, open-problem solution, and cleaner analysis. It is weaker than the 6.25-7.00 accept-range anchors (Horizon-Free Model-Based, Demonstration-Regularized RL) because those papers have no unresolved presentation inconsistencies. The paper sits near the boundary between reject and accept: genuine contributions but a clear abstract/table mismatch.

**Final score:** 5.5

---

## Summary

This paper introduces Dig-DEC (Dual Information Gain Decision-Estimation Coefficient), a new model-free complexity measure for decision making with structured observations (DMSO). The framework replaces the optimism principle used in prior work (optimistic DEC) with information-gain-driven exploration via a regularized KL term, enabling the first model-free regret bounds for hybrid MDPs (stochastic transitions, adversarial rewards) with bandit feedback — resolving an open problem from [LWZ25]. The paper also refines online estimation procedures for both average and squared estimation errors, yielding improved regret exponents in several stochastic settings. The framework unifies and extends prior AIR-based analyses through a general divergence-based regret decomposition.

## Strengths

- **Novel and well-motivated framework (Dig-DEC).** The paper cleanly separates exploration into two information-gain terms (KL regularization and a divergence $\overline{D}$), removing the need for explicit optimism. This is both conceptually elegant and practically important: the removal of optimism enables handling adversarial environments without explicit reward estimators (Section 4, Eq. 7–8).

- **First model-free regret bounds for hybrid MDPs with bandit feedback.** Section 5.2 and Table 2 provide explicit sublinear regret bounds for hybrid bilinear classes and coverable MDPs under bandit reward feedback, resolving the main open problem left by [LWZ25]. This is a concrete contribution to a well-recognized problem.

- **Improved estimation procedures.** The unbiased estimator for average estimation error (Section 4.2.1) and the refined two-timescale procedure for squared error (Section 4.2.2) yield tighter control of the Est term, improving prior bounds from $T^{1/2}$-dependent to $\log^2|\Phi|$ in the squared-error case.

- **Clean analytical architecture.** The regret decomposition via Bregman divergences (Theorem 6) is more flexible than prior minimax-theorem-based analyses and recovers previous results as special cases (Appendix C). The modular structure — bound dig-dec, bound Est, optimize $\eta$ — makes the framework easy to apply to new settings.

## Weaknesses

### Major

- **Inconsistency between abstract rate claims and Table 1.** The abstract states that for average estimation error minimization, the paper improves regret bounds from $T^{3/4}$ to $T^{3/5}$ (on-policy) and from $T^{5/6}$ to $T^{7/8}$ (off-policy). However, Table 1 reports $T^{2/3}$ for all $\overline{D}_{\text{av}}$ entries (both on-policy and off-policy bilinear classes, both BE types). These exponents ($T^{0.6}$ and $T^{0.875}$) do not match the table's $T^{0.667}$. The numbers $T^{3/5}$ and $T^{7/8}$ do not appear elsewhere in the main body. This is not a cosmetic issue — it undermines reader trust in the paper's headline claims. The authors must either (a) correct the abstract to match the table, (b) explain clearly if these exponents refer to a specific subclass not captured in Table 1, or (c) provide a reconciliation. As presented, the abstract advertises results that the main paper does not substantiate.

### Minor

- **Overstatement in the abstract about Dig-DEC versus optimistic DEC.** The abstract claims "Dig-DEC is always no larger than optimistic DEC." Theorem 13 proves $\text{dig-dec} \le \text{o-dec} + \eta$, where $\eta>0$ is a tuning parameter. The bound allows Dig-DEC to be up to $\eta$ larger, not strictly "no larger." The paper's body clarifies this reasonably (noting that $\eta$ is dominated by the $\eta d$ scaling), but the abstract's phrasing is technically stronger than what is proven. This should be tightened.

- **The bandit example (Theorem 14) proving strict improvement is stated with proof deferred to the appendix.** The example — a 3-armed bandit where optimistic DEC suffers $\Omega(\sqrt{T})$ regret while Dig-DEC achieves constant regret — is claimed in the main text but its proof is in Appendix J (stripped by the parser). While proof deferral is standard, the "much smaller" claim is central to the narrative; a brief sketch of the instance and the intuition for the constant regret would improve the main text's self-containedness.

### Trivial

- The introduction contains garbled exponent text (line 39: "$T^{\frac{3}{2}}/T^{\frac{5}{8}}$ … $T^{\frac{3}{2}}/T^{\frac{5}{6}}$") that appears to be a PDF parsing artifact but is confusing as presented. The authors should clean this up.

## Nice-to-Haves

- A discussion of computational tractability: solving the minimax optimization in Eq. (3) is nontrivial for large $\Phi$. The paper focuses on information-theoretic complexity, but a sentence acknowledging the computational challenge would be helpful.
- A brief sketch of the posterior update rules for $\overline{D}_{\text{av}}$ and $\overline{D}_{\text{sq}}$ in the main text (rather than fully deferred to appendices) would improve accessibility.

## Removed Points

The following points from the input reviews were removed per the filtering rules:

- Criticism about Theorem 14's proof being in the appendix (missing appendix = parser artifact; exists in the original submission).
- Criticism about undisclosed hyperparameters or implementation details for Algorithm 1 (reproducibility nitpick).
- Strength from the Strength Finder about "improving regret rates from $T^{3/4}$ to $T^{3/5}$" — this is contradicted by Table 1 which shows $T^{2/3}$, so the weakness finding overrides this claimed strength.
- Several generic strengths from the Strength Finder ("this paper addressed an important problem") — removed as generic/superficial.

## Novel Insights

None beyond the paper's own contributions. The reviewers did not surface any insight about the paper that the authors themselves do not already articulate.

## Suggestions

1. **Reconcile the abstract with Table 1.** This is the most important fix. Either correct the abstract's exponents to $T^{2/3}$, or add an explanation if the abstract's numbers refer to a different subclass/regime and make that explicit with a pointer.
2. **Tighten the abstract's claim about Dig-DEC vs. optimistic DEC** to reflect Theorem 13's additive $\eta$ gap (e.g., "Dig-DEC is at most $\eta$ larger than optimistic DEC").
3. **Add a 2–3 sentence sketch of the bandit example (Theorem 14)** in the main text to make the "much smaller" claim self-contained.
4. **Clean up the garbled exponents in the introduction.**

## Score and Decision

**Calibration anchors used:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| Zi1QNJKXAD (Robust MDPs) | 3.20 | 1 | Much weaker: narrower scope, less principled |
| lFzUHGebeb (Var Forward Reg) | 2.00 | 1 | Unrelated, much weaker |
| 2h3m61LFWL (VBMLE Linear MDPs) | 4.25 | 1 | Weaker: novelty concerns, restrictive assumptions |
| GvsCOOPxoI (DEC-POMDPs) | 6.17 | 1 | Stronger on presentation but had scope limitations; comparable contribution level |
| en3NwykrHW (Trajectory Feedback) | 5.50 | 1 | Similar level: clean theory paper with clarity issues |
| 6PbvbLyqT6 (DCFR) | 8.00 | 1 | Stronger: polished, well-received at venue |
| w8Zo7jACq7 (Model-Free CMDPs) | 5.20 | 2 | Comparable but this paper has a more novel framework |
| U0c2IaQhHk (RKHS-RL) | 5.00 | 2 | Weaker: less clean analysis, no open-problem solution |
| Yx7TnC6AAp (Extensive-Form Games) | 5.75 | 2 | Comparable: strong theory but narrower scope |
| txD9llAYn9 (Horizon-Free Model-Based) | 7.00 | 2 | Stronger: no presentation inconsistencies, accepted |
| lF2aip4Scn (Demonstration-Regularized RL) | 6.50 | 2 | Stronger: clean presentation, accepted |
| Pe2lo3QOvo (RLHF with Randomization) | 6.25 | 2 | Comparable contributions but cleaner presentation |

**Final score: 5.5**

The paper makes genuine contributions (Dig-DEC framework, first hybrid bandit-feedback bounds, improved estimation), and the theoretical development is sound. However, the abstract/Table 1 inconsistency is a significant presentation failure that prevents clean acceptance. The paper is stronger than the 4.25–5.20 reject-range anchors but below the 6.25+ accept-range anchors due to this unresolved issue.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>