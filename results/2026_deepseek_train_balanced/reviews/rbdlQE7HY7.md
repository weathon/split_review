Now I have all the information needed. Let me write the consolidated review.

---

## Summary

This paper introduces "uniform wrappers" — a meta-algorithm framework that transforms any online optimization algorithm (and its regret proof) from convex/concave settings to a broader class of non-convex functions called quadratizable/up-concave functions. The framework is instantiated on ZO-FTRL (a zeroth-order Follow-the-Regularized-Leader variant) to obtain three concrete algorithms for three classes of weakly DR-submodular functions. The paper claims improved regret rates: $\tilde{O}(T^{2/3})$ for noisy zeroth-order feedback (vs. prior $\tilde{O}(T^{3/4})$), $\tilde{O}(T^{3/4})$ for bandit feedback (vs. prior $\tilde{O}(T^{4/5})$ for non-monotone and noisy settings), and $\tilde{O}(1/\epsilon^{3})$ offline sample complexity (vs. prior $\tilde{O}(1/\epsilon^{4})$).

## Strengths

- **Genuine rate improvements under zeroth-order feedback**: Theorem 6 and Remark 3 (lines 254–262) establish $\tilde{O}(T^{2/3})$ $\alpha$-regret for all three function classes under noisy zeroth-order feedback, improving on the prior SOTA of $\tilde{O}(T^{3/4})$. This is a concrete, quantitative improvement.

- **First improvement for non-monotone bandit feedback**: Remark 5 (lines 273–274) shows that for non-monotone up-concave functions over general convex sets under bandit feedback, the $\tilde{O}(T^{3/4})$ bound beats the prior SOTA of $\tilde{O}(T^{4/5})$ — a gap of $T^{1/20}$. For monotone $\gamma$-weakly functions over convex sets containing the origin under noisy bandit feedback, the same bound improves from $\tilde{O}(T^{4/5})$ to $\tilde{O}(T^{3/4})$.

- **Offline sample complexity improvement**: Theorem 8 (lines 278–284) achieves $\tilde{O}(1/\epsilon^{3})$ sample complexity for all three function classes, improving on the prior SOTA of $\tilde{O}(1/\epsilon^{4})$ by a full factor of $1/\epsilon$. This is a substantial improvement with practical implications.

- **Generalizes prior work from first-order to zeroth-order, bandit, and offline settings**: The paper explicitly contrasts with (Pedramfar & Aggarwal, 2024a) (lines 28–32), which was limited to first-order semi-bandit feedback with fully adaptive adversaries. The uniform wrapper framework handles zeroth-order, bandit, and offline settings (Theorems 6–8) — none of which were covered by the prior approach.

- **Wrappers defined for arbitrary query order $i$**: Definitions 4 and 5 (lines 213–241) define uniform wrappers $\mathcal{W}_i^{\mathrm{M0}}$ and $\mathcal{W}_i^{\mathrm{NM}}$ for any $i \ge 0$, supporting zeroth-order ($i=0$), first-order ($i=1$), and higher-order oracles. Remarks 1 and 2 (lines 219, 243) show that the prior work's meta-algorithms are special cases at $i=1$, demonstrating genuine unification.

## Weaknesses

### Fatal
None.

### Major

- **Informal proof-conversion "guideline" undermines the "general framework" claim.** Section 6 (lines 130–136) describes proof conversion via two vague steps — "rewrite the parts of proof... to isolate the use on concavity" and "verify that the results could be adapted to upper-quadratizable setting" — which the paper explicitly calls a "guideline" rather than a theorem. The term "wrappable algorithm" (line 130) is defined simply as an algorithm whose bounds *can* be converted, with no characterization of sufficient conditions. Claim 1 (line 41) states the paper develops "a general framework for converting algorithms and their regret guarantees," but the proof-conversion component is not formalized into any theorem. What is actually provided is a single fully-worked example (ZO-FTRL). This gap between the claimed generality and the delivered formalism is significant. The paper would be strengthened by either (a) proving sufficient conditions for wrappability, or (b) explicitly recasting the contribution as a case study of ZO-FTRL enriched with a wrapper vocabulary.

- **The "cone" condition for zeroth-order M0 and NM settings is restrictive and under-discussed.** The paper introduces (line 252) the condition $|Q_f(\mathbf{z}) - f(\mathbf{x})| \leq C\|\mathbf{z} - \mathbf{x}\|$ for zeroth-order query oracles. This requires that the oracle's randomness vanishes *at least linearly* as the query point approaches $\mathbf{x}$ — a condition violated by standard constant-variance stochastic oracles (e.g., additive Gaussian noise with fixed variance). The paper acknowledges this condition is necessary (the wrapped oracle would otherwise "blow up," line 252), but does not discuss how restrictive it is, nor does it clarify whether the SOTA results it compares against (Remark 3, lines 262) require similarly strong assumptions. For the M0 and NM function classes under zeroth-order feedback, the claimed improvements ($\tilde{O}(T^{2/3})$ over $\tilde{O}(T^{3/4})$, and $\tilde{O}(1/\epsilon^3)$ over $\tilde{O}(1/\epsilon^4)$) directly depend on this condition being satisfied. (For the M class the wrapper is identity, so no cone condition is needed.) The paper would benefit from explicitly stating which SOTA algorithms require the same assumption and which do not.

### Minor

- **Novelty relative to (Pedramfar & Aggarwal, 2024a) is moderate; the framing overstates distance from prior work.** Remarks 1 and 2 (lines 219, 243) confirm that the $i=1$ (first-order) cases of the proposed wrappers are identical to the prior work's meta-algorithms. The three lemmas (Lemmas 1–3) establishing quadratizability for the three function classes are inherited from prior work. The paper's concrete additions — extension to zeroth-order oracles, stochastic feedback, the ZO-FTRL worked example with improved rates, and the offline conversion — are genuine contributions, but the abstract and introduction (lines 3–4, 40–46) frame them as a "general framework" with "novel contributions" and "superior regret guarantees" without sufficiently delineating what is inherited versus new. The paper explicitly acknowledges the relationship in Remarks 1–2, but the high-level claims in the abstract and contributions list are broader than the technical novelty warrants.

- **No discussion of limitations.** The paper has no limitations section and never explicitly acknowledges that the cone condition is restrictive, that the wrappability notion is informal, or that the general framework has only been fully instantiated on one base algorithm (ZO-FTRL). A brief limitations paragraph would improve credibility and help readers assess the scope of the contributions.

### Trivial
None.

## Nice-to-Haves

- **Empirical validation**, even in a simple synthetic setting (e.g., verifying that $\mathcal{W}(\text{ZO-FTRL})$ achieves $\tilde{O}(T^{2/3})$ regret on a constructed DR-submodular function compared to a $\tilde{O}(T^{3/4})$ baseline), would substantially strengthen the paper by demonstrating that the asymptotic rates are realized in practice. The paper's purely theoretical nature makes this optional, but given the strong "superior" claims, an experiment would be convincing.

- The heavy notation in Section 3 (lines 67–81) — especially the 15-line agent definition with nested product spaces — could be streamlined for readability.

## Removed Points

- **Tables 1 and 2 appearing as unparsed images (line 58).** This is a parser artifact; the original submission would have properly rendered tables. Per the removal rules for parser artifacts, this criticism is not carried into the evaluation.
- **Criticism that the "wrappability" definition is "circular."** Line 130 defines "wrappable" as algorithms whose bounds can be converted. This is a labeling definition, not logically circular. The substantive criticism (that no sufficient conditions for wrappability are given) is retained in the Major weaknesses above.
- **Criticism about "no empirical validation."** Moved to Nice-to-Haves, as this is a theoretical paper in online optimization where empirical validation is not standard for the contribution type.
- **Strength Finder's claim about "systematic proof-conversion guideline."** This strength conflicts with the verified weakness that the guideline is informal; the weakness takes precedence. The guideline exists but is not formalized, so it is not a strength at the claimed level of generality.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Formalize the wrappability condition** in Section 6, or explicitly state that the paper provides a worked example (ZO-FTRL) plus a recipe, rather than a fully general theorem. This would close the gap between the claims and the delivery.
2. **Add explicit discussion of the cone condition's restrictiveness** in Section 8: which practical stochastic oracles satisfy it, and whether the SOTA baselines being compared also require it. This is especially important because the improved zeroth-order results for M0 and NM classes depend on it.
3. **Add a limitations paragraph** (or subsection) acknowledging: (a) the cone condition restricts the zeroth-order M0/NM results, (b) the proof-conversion guideline is informal, and (c) only ZO-FTRL is fully worked out as a base algorithm.
4. **Tone down framing** in the abstract and contributions list to match what is delivered. Replace "general framework" with "a meta-algorithm framework and a worked example on ZO-FTRL" or similar. The concrete rate improvements are strong enough to stand on their own.

## Score and Decision

The paper makes real contributions — concrete rate improvements for zeroth-order, bandit, and offline settings for quadratizable function classes. However, two significant issues temper enthusiasm: (1) the "general framework" claim is not matched by the formalism (the proof-conversion component is an informal guideline), and (2) the improved zeroth-order results for the M0 and NM classes depend on a restrictive oracle assumption (the cone condition) whose restrictiveness and relationship to SOTA baselines is not discussed. These are addressable in revision, and the underlying rate improvements are genuine.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Reject</decision>