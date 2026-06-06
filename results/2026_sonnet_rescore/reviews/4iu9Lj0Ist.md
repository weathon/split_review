## Summary

This paper establishes the first theoretical framework connecting machine unlearning and continual learning. It formalizes the "continual learning-unlearning" problem (Definition 2.1), decomposes the post-unlearning excess risk into unlearning loss (Eq. 6) and CL excess risk (Eq. 7), proves an explicit excess-risk bound for ℓ₂-regularized CL on nonlinear convex models (Theorem 3.1), and proposes two certified unlearning algorithms — a zero-storage natural forgetting approach (Alg. 1) and a Hessian-based approach (Alg. 2) — with corresponding performance guarantees and a storage-saving hybrid (Section 5.3).

---

## Strengths

- **Clean two-component decomposition of post-unlearning excess risk** (Eq. 6–7) separating unlearning loss from CL excess risk. This is the structural linchpin of the entire analysis: it directly enables the combined bounds in Theorem 4.1 and Corollary 5.3 by handling each component separately, then assembling a joint guarantee.

- **Theorem 3.1 extends prior CL excess-risk analysis from linear to nonlinear convex models.** The bound in Eq. (8) explicitly characterizes how task heterogeneity (‖wᵢ* − wⱼ*‖) and dataset sizes jointly determine the forgetting-generalization tradeoff. The proof extends Lin et al. (2023) in a non-trivial direction and is reused as a building block throughout Sections 4 and 5.

- **Hessian-based continual unlearning (Alg. 2 and Proposition 5.2)** provides a second-order approximation error bound that scales quadratically in the initial error (Eq. 15), theoretically tighter than the first-order bound in Theorem 4.1. The algorithm handles arbitrary unlearning request orderings, which is non-trivial given the complex model evolution in CL.

- **Natural forgetting algorithm (Alg. 1) achieves certified unlearning with zero storage overhead** by exploiting the inherent forgetting of ℓ₂-regularized CL. Theorem 4.1 gives an explicit bound (Eq. 9) showing the approximation error decays exponentially with the number of tasks remaining after the unlearned task.

- **Analysis of unlearning sequence disruptions (Proposition 5.1)** is a genuinely novel insight: out-of-order deletion requests inflate approximation error (captured by the last line of Eq. 14), while well-ordered arrivals simplify the correction (Lemma 5.4). This yields actionable design guidance for production systems and motivates the storage-reducing hybrid in Section 5.3.

- **Storage-saving hybrid (Section 5.3)** is theoretically grounded: Lemma 5.4 justifies discarding historical information under ordered requests, reducing storage from O(td²) to O(max-gap · d²). The modified algorithm retains performance guarantees.

---

## Weaknesses

### Fatal
None.

### Major

- **The central empirical claim contradicts Figure 2(b).** The abstract and conclusion both assert that "the Hessian-based adaptation algorithm largely outperforms the gradient-based algorithm," and Section 7 states "the Hessian-based method achieves lower unlearning loss." However, the figure caption for Figure 2(b) explicitly states that the natural forgetting algorithm achieves approximation error ~0.08–0.10, while the Hessian-based algorithm achieves ~0.20–0.24 across all tested λ. The natural forgetting approach has *lower* approximation error (i.e., lower unlearning loss in the metric the paper defines) throughout the entire sweep. The text in Section 6.1 acknowledges that λ=40 minimizes approximation error for natural forgetting and λ=20 for Hessian-based, but even at their respective optima, natural forgetting (0.08) beats Hessian-based (0.20). The theoretical argument for Hessian superiority rests on Proposition 5.2's second-order bound, but this bound's advantage requires the approximation error to already be small (below 1), which may not hold in the non-strongly-convex MNIST setting. The paper does not acknowledge or reconcile this inversion anywhere in the main text. This is a substantive inconsistency: the experiments should either corroborate the main claim or explain why they do not.

- **No direct comparison of post-unlearning test accuracy between the two algorithms.** Table 1 compares Hessian-based against perfect retraining only. The paper's claim of superiority requires showing that Hessian-based outperforms natural forgetting on the joint post-unlearning excess risk metric (Definition 2.2) — but natural forgetting's post-unlearning test accuracy is never reported. Without this comparison, the central tradeoff argument ("Hessian-based is better at the cost of storage") is not experimentally substantiated; readers only see half the comparison.

### Minor

- **Experiments conducted under settings where the theorems do not apply.** Section 6 explicitly states: "Regarding Assumption 2.1, we relax its assumption of μ-strong convexity here in order to show the more general results under a non-strongly convex setting." But the term ρ = λ/(μ+λ), which drives all bounds in Theorems 3.1, 4.1, and Corollary 5.3, is undefined when μ = 0. The experimental section thus cannot serve as validation of the theoretical bounds. For a theory paper, experiments should at minimum be run in a regime where the theorems hold (e.g., ridge regression on a synthetic task sequence), and departures from the theorem's assumptions should be flagged as a limitation rather than framed as demonstrating generality.

- **Table 1 anomaly (71.59% > 71.05%) with no statistical reporting.** Perfect retraining is the target that the unlearning algorithm approximates; the unlearning algorithm cannot exceed it in expectation. The 0.54% overshoot almost certainly reflects run-to-run variance from a single-seed experiment, but no error bars or seed information are reported. For such a small, claim-critical comparison, at minimum multiple seeds should be used.

### Trivial

- The claim in Introduction that current certified unlearning algorithms "cannot function" in CL is imprecise — they would produce suboptimal results without guarantees, but are not undefined. "Have no theoretical guarantees in this setting" would be more accurate.

---

## Nice-to-Haves

- Designing an experiment under a genuinely strongly convex loss (e.g., ridge regression on a synthetic task sequence with controlled task heterogeneity) would let the paper illustrate the regime where all theorems apply and directly test whether Hessian-based achieves lower approximation error as theory predicts.

- A dedicated figure comparing approximation error and post-unlearning accuracy under ordered vs. disordered unlearning sequences would directly illustrate the Proposition 5.1 / Lemma 5.4 findings — one of the paper's more original insights that is currently only partially visible in Table 2 (referenced in text but not reproduced in the main submission).

- The discussion of Footnote 1 ("easily extend to individual sample unlearning") would benefit from acknowledging why per-sample unlearning is more complex: it requires per-sample Hessians or gradient information and substantially increases the storage overhead of Alg. 2 beyond O(td²+2td).

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Strength Finder claim**: "in Figure 2(b) the Hessian-based approximation error is significantly lower than that of the natural-forgetting algorithm, especially at larger λ." **Removed**: Directly contradicted by the figure description in the paper. The natural forgetting algorithm has lower approximation error (0.08–0.10) vs. Hessian-based (0.20–0.24).

- **Harsh Critic**: "calling [Alg. 1] an algorithm is generous." **Removed as nitpick**: The paper is transparent that Alg. 1 does not adapt gradient-based methods and simply adds noise. This is a legitimate design choice, not a misrepresentation.

- **Harsh Critic**: Storage barrier for Alg. 2 in non-convex / high-d settings. **Demoted/Removed**: The paper explicitly scopes to convex models and honestly presents storage cost as a known tradeoff. The critique is valid in principle but the paper already acknowledges this is principally of theoretical interest.

- **Harsh Critic**: The internal model (w_t) still containing deleted information. **Removed as already addressed**: Section 4 explicitly acknowledges this: "Alg. 1 internally maintains the secret model w_t... which may still contain information from all deleted tasks. We extend Alg. 1 to ensure stronger certified unlearning in Appendix C.2." The issue is flagged and handled.

- **Harsh Critic**: Interpretability of the bound in Eq. (8) and the claim that "positive λ is needed." **Removed**: Complexity of theoretical bounds is not a flaw. The paper states the discussion is in Appendix B.2.

---

## Novel Insights

The paper's most original contribution beyond the algorithms themselves is the analysis of unlearning sequence disruptions in Proposition 5.1 and Lemma 5.4. The observation that out-of-order deletion requests inflate the approximation error via interference terms (the last line of Eq. 14), while well-ordered arrivals allow storage to be discarded, has no direct precedent in either the CL or unlearning literature. This provides a concrete systems-level design principle — that unlearning systems should incentivize or enforce ordered request patterns — derived from first principles rather than heuristics.

---

## Suggestions

1. **Resolve the Figure 2(b) inconsistency**: either explain theoretically why natural forgetting achieves lower approximation error in the non-strongly-convex regime (possibly showing this is an artifact of relaxed assumptions), or revise the abstract/conclusion claims to accurately describe the tradeoff as "better post-unlearning accuracy at the same λ" rather than "lower unlearning loss."

2. **Add natural forgetting to Table 1** to enable direct comparison of post-unlearning test accuracy between the two algorithms at matched λ values.

3. **Run at least 5 seeds** for all Table 1 entries and report standard deviation; the 0.54% gap between Hessian-based and perfect retraining needs confidence intervals to be interpretable.

4. **Add a synthetic strongly convex experiment** (e.g., ℓ₂-regularized logistic regression on a linearly separable task sequence) where Assumption 2.1 holds exactly, so that the theorem bounds can be numerically verified and the Hessian advantage can be confirmed in the regime the theory analyzes.

---

## Score and Decision

**Originality**: 4/5 — First formal framework for this intersection of CL and unlearning, with non-trivial algorithm design.
**Importance**: 4/5 — The problem is timely and the gap in the literature is real.
**Claims Supported**: 2/5 — The central empirical claim ("Hessian-based largely outperforms") is contradicted by Figure 2(b), and the direct comparison needed to validate it is absent from Table 1.
**Soundness**: 3/5 — The theoretical framework and proofs appear sound; the experimental validation is structurally flawed.
**Clarity**: 3/5 — The framework and algorithms are clearly described; the bounds (Eq. 8, 14) are dense but expected for theoretical work. The disconnect between Figure 2(b) and the main claims creates meaningful confusion.
**Community Value**: 4/5 — Opens a new research direction with formal tools that others can build upon.

The paper makes a genuine theoretical contribution — the decomposition framework, Theorem 3.1, and the sequence-disruption analysis — that is worth publishing. However, the claim that the Hessian-based algorithm "largely outperforms" the gradient-based algorithm is the paper's headline result, and Figure 2(b) directly contradicts it on the approximation error metric, while Table 1 fails to provide the comparison needed to support it on the test accuracy metric. Resolving this inconsistency is a prerequisite for publication, not a rebuttal item. With that fix, this paper is a solid accept.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>

<subscores>
<originality>4</originality>
<importance>4</importance>
<claims_supported>2</claims_supported>
<soundness>3</soundness>
<clarity>3</clarity>
<community_value>4</community_value>
</subscores>