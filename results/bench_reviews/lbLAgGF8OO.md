Here is my consolidated review:

---

## Summary

This paper introduces Dig-DEC (Dual Information Gain Decision-Estimation Coefficient), a new model-free complexity measure for decision making with structured observations. Dig-DEC replaces the optimism principle of prior work (FGQ+23) with information-gain-driven exploration. The paper proves that Dig-DEC is never worse than optimistic DEC (Theorem 13) and shows improved regret bounds in stochastic settings (e.g., from $T^{5/6}$ to $\sqrt{T}$ for Bellman-complete MDPs). The key application contribution is the first model-free regret bounds for hybrid MDPs (stochastic transitions, adversarial rewards) with bandit feedback, under linear reward structure. The paper also provides improved online function estimation procedures for both average and squared estimation error.

## Strengths

- **General framework with flexible divergence.** The paper generalizes the AIR framework to handle arbitrary convex divergences $D$ (Equation 2), with a new analysis technique that connects to mirror descent. This recovers prior results (XZ23, LWZ25) with simpler proofs and enables new instantiations. The unified treatment of stochastic and hybrid settings under a single algorithmic framework (Algorithm 1) is a genuine contribution.

- **First model-free regret bounds for hybrid MDPs with bandit feedback.** The paper delivers the first sublinear regret for model-free learning in hybrid bilinear classes and Bellman-complete coverable MDPs under bandit feedback with linear rewards (Table 2), resolving an open question from LWZ25. This is a concrete advance over prior work that was limited to full-information rewards.

- **Improved estimation procedures.** For average estimation error, the paper constructs an unbiased estimator via sample splitting that improves regret from $T^{3/4}$ to $T^{3/5}$ (on-policy) and $T^{5/6}$ to $T^{7/8}$ (off-policy). For squared estimation error under Bellman completeness, a refined two-timescale procedure achieves constant-level Est ($\log^2|\Phi|$), improving from $T^{1/2}$ to constant and yielding $\sqrt{T}$ total regret — the first DEC-based method to match optimism-based approaches (JLM21, XFB+23) in this setting.

- **Theorem 13 provides a clean complexity measure comparison.** The proof that $\text{dig-dec} \leq \text{o-dec} + \eta$ for any $\overline{D}$ directly compares the two complexity measures, showing Dig-DEC is never worse than optimistic DEC at the level of the DEC itself.

## Weaknesses

### Fatal
None.

### Major
None that threaten the core claims.

### Minor

- **Theorem 14's support for the "strict improvement" claim is partly about algorithm regret, not the complexity measure itself.** Theorem 14 shows that the optimistic E2D *algorithm* (FGQ+23) suffers $\Omega(\sqrt{T})$ regret on a 3-armed bandit while the authors' algorithm achieves ≤1 regret. This is an algorithmic separation, not a direct comparison of the complexity measures Dig-DEC and optimistic DEC. Theorem 13 already gives the clean complexity measure comparison ($\text{dig-dec} \leq \text{o-dec} + \eta$). The paper's surrounding text (Section 6, line 311) claims the KL term "allows Dig-DEC to *strictly improve* over optimistic DEC even in the stochastic setting" and uses Theorem 14 as evidence, but the theorem compares algorithm performance, not DEC values. The paper should clarify this gap — the "strict improvement" at the complexity measure level is established by Theorem 13 only additively ($+\eta$), while the strict improvement at the algorithmic level is shown in Theorem 14. These are different statements and should be cleanly separated.

- **The hybrid setting results require strong assumptions (Assumptions 3 and 4) that limit scope.** Assumption 3 (unique reward-to-value mapping given $\phi$) is a strong "policy-specific Bellman closure" condition. The paper acknowledges this immediately (line 121): "[Assumption 3] does not capture all learnable hybrid MDPs we are aware of," and notes that LMWZ24 handles some cases outside this framework. Similarly, Assumption 4 requires linear reward with *known* features. Since LWZ25 had the same limitation even in the full-information case, the paper's claim of "resolving the open problem" is accurate but should be read as "resolving it under the same structural assumptions as prior work." The paper is transparent about this, but the limitations are worth emphasizing.

- **All derivations deferred to appendix.** The regret bounds in Tables 1-2 are presented without any derivation in the main text. The Dig-DEC bounds, the Est bounds, and the optimal $\eta$ tuning are all relegated to the appendix. While this is common for theory papers, the main text would benefit from at least one concrete calculation (e.g., deriving the $\sqrt{T}$ regret for Bellman-complete MDPs). The tables also suffer from parser-induced formatting issues (e.g., "log Φ" instead of "log|Φ|") that make them hard to parse.

- **Comparison with LWZ25's specific prior results is vague.** The paper states that LWZ25 "obtained $\sqrt{T}$ regret for linear $Q^*/V^*$ MDPs...before their result, the best known rate is $T^{3/4}$" but then says their algorithm "cannot handle other canonical settings." The precise landscape of prior results and how the current paper improves on each is difficult to assess without the appendix.

### Trivial

- The notation $\log\Phi$ in the tables is ambiguous — it should be $\log|\Phi|$ or clarified.
- Some exponent labels in introduced contribution claims (line 39: "$T^{\frac{3}{2}}/T^{\frac{5}{8}}$" and "$T^{\frac{3}{2}}$") appear to be garbled (likely parser artifacts from $T^{3/4}$ and $T^{5/6}$ respectively).
- The line "the best known rate is $T^{\frac{3}{4}}$" (line 85) — the critic notes this isn't precisely attributed to a specific paper.

## Nice-to-Haves

- **Concrete $\log|\Phi|$ bounds for at least one application.** For linear MDPs, the paper could state an explicit bound on $\log|\Phi|$ in terms of the feature dimension $d$ and a discretization scale, showing concretely how the "model-free" property (independence from $|\mathcal{M}|$) plays out. This would make the tables more interpretable.
- **A small worked example** (e.g., 2-state MDP) tracing the algorithm's $\rho_t$, $p_t$, $\nu_t$ and posterior update would make the abstract framework more accessible.
- **Discussion of computational complexity.** The paper mentions "model-free" only in terms of regret bounds, but the algorithmic steps (minimax optimization in Equation 3, posterior updates) have computational costs that are not discussed.

## Removed Points

These points are flagged to be removed — treat them with caution:

- **Criticism about the 3-armed bandit "contradicting the paper's own MDP framing":** Removed because a bandit is an MDP with H=1 and a single state — it is a standard special case. The critic's claim that "optimistic DEC applied to a 3-armed bandit would trivially achieve O(1) regret" is about the complexity measure, whereas Theorem 14 is specifically about the *algorithm* of FGQ+23. The paper is clear that Theorem 14 compares algorithms ("the algorithm in [FGQ+23]"), not complexity measures. The complexity measure comparison is handled by Theorem 13.

- **Criticism that the "model-free" label is misleading:** Removed because the paper explicitly defines what it means by "model-free" at line 43: "the term 'model-free' learning in our work does not mean that the learner has no access to the model class $\mathcal{M}$ or has computational constraints. Instead, it only means that the regret bound is independent of the size of the model set $\mathcal{M}$." The paper cannot be faulted for following its own clearly stated definition.

- **Criticism that Theorem 7's estimator fails under adversarial rewards (i.i.d. violation):** Removed because Assumption 5 (line 201) explicitly restricts the adversary: "the adversary is restricted such that for any $\pi, \phi$ and $t, t' \in [T]$, it holds that $\mathbb{E}^{\pi, M_t}[\ell_h(\phi; o_h)] = \mathbb{E}^{\pi, M_{t'}}[\ell_h(\phi; o_h)]$." This ensures the estimation function's expectation is invariant across rounds, which is exactly what the estimator needs. The critic overlooked this restriction.

- **Criticism about Theorem 13 comparison being "apples-to-oranges" because $\overline{D}$ might differ:** Removed because Theorem 13 explicitly states "for any $\overline{D}$" — it is a universal comparison.

- **Formatting/style nitpicks about tables, missing symbol definitions, spacing, etc.:** These are parser artifacts from the PDF extraction, not errors in the original submission.

- **Criticism about missing appendix material or missing concrete bounds on $\log|\Phi|$:** Deferred to Nice-to-Haves. The paper structure follows standard practice for theory papers at this venue.

- **Generic or one-size-fits-all weaknesses** (e.g., "requesting a larger dataset," "adding more models"): Not applicable to this theory paper.

- **Strawman weakness about Assumption 3 being "extremely strong":** The paper itself acknowledges this limitation explicitly (line 121). It is not a hidden weakness — the paper is transparent about it. I keep the spirit of this as a Minor weakness (the strong assumptions limit scope) but remove the framing that the paper is being disingenuous.

## Novel Insights

The reviewers' interaction surfaces one genuinely novel observation beyond the paper's own contributions: **the relationship between information-gain-based and optimism-based exploration is more nuanced than prior work suggests.** The paper shows that optimism can be replaced by an *information gain + regularization* mechanism (the two KL terms in Dig-DEC), and this substitution is provably harmless in stochastic settings (Theorem 13) while enabling adversarial generalization. The key insight is that the regularization term ($\text{KL}(\nu_\phi, \rho)$) — not the information gain term — does the work of matching optimistic DEC's guarantees, while the information gain term ($\mathbb{E}[\text{KL}(\nu_\phi(\cdot|\pi, o), \nu_\phi)]$) provides genuine improvement opportunities. This decomposition clarifies *why* optimism could be removed: regularization substitutes for the "optimistic pull" toward high-value regions, while information gain provides additional signal. This conceptual separation is a valuable contribution to the DEC literature.

## Suggestions

1. **Clarify the Theorem 14 framing.** State explicitly that Theorem 14 compares the optimistic E2D *algorithm* against the Dig-DEC *algorithm* (not the complexity measures), while Theorem 13 already provides the complexity measure comparison. This would prevent confusion.
2. **Work out one explicit $\log|\Phi|$ bound** for a concrete setting (e.g., linear MDPs with discretized feature expectations) in the main text to make the tables self-contained.
3. **Add a paragraph on the relationship between Assumption 3 and the LWZ25/LMWZ24 assumptions** to help readers understand the scope of the contribution relative to prior work.
4. **Fix the garbled exponents** in line 39 (the claimed $T^{3/2}/T^{5/8}$ improvement appears to be a parser error for $T^{3/4}/T^{5/6}$).

## Score and Decision

**Calibration anchors** (retrieved from human review corpus):

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `/home/wg25r/review_agent/human_reviews_2026/fE0RJto3Na.md` | 6.50 | Tabular RL with gap-dependent bounds; similar theoretical depth but includes experiments. Current paper is broader but lacks empirical validation. Slightly weaker. |
| `/home/wg25r/review_agent/human_reviews_2026/QEcSLhfOoQ.md` | 6.50 | Adversarial RL with matching lower bounds; cleaner, more self-contained contribution. Current paper is less crisp in its claims. Slightly weaker. |
| `/home/wg25r/review_agent/human_reviews_2026/AKUSUkWj6p.md` | 6.50 | Hybrid learning with oracle efficiency; similar setting. Comparable level of contribution. |
| `/home/wg25r/review_agent/human_reviews_2026/Ccflf8sqjF.md` | 5.00 | Replicable RL with linear FA; mixed reviews, moderate contribution. Current paper has stronger theoretical depth. Slightly stronger. |
| `/home/wg25r/review_agent/human_reviews_2026/vR3wRYaucr.md` | 4.00 | GLMDP; rejected due to unclear writing and incremental contributions. Current paper is stronger. |
| `/home/wg25r/review_agent/human_reviews_2026/2LpoMDXuJf.md` | 3.00 | Grid world experiments; far less theoretical depth. Current paper is much stronger. |
| `/home/wg25r/review_agent/human_reviews_2026/kxVHb58g3J.md` | 2.00 | Weak paper, withdrawn. Current paper is far stronger. |

**Score rationale**: The paper makes genuine theoretical contributions — a novel complexity measure, first hybrid bandit DEC results, and improved estimation procedures — that place it above the reject-level anchors (3-4 range). However, the gap between some claims and their evidence (Theorem 14 supporting a complexity measure claim with algorithmic evidence), the strong assumptions limiting the hybrid results, and the heavy reliance on appendix material prevent it from reaching the level of the strongest anchors (6.5+). Positioned relative to the anchors, it sits comfortably between the 5.0 and 6.5 range. The technical contributions are solid but the presentation of claims needs more precision.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>