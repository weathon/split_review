Now I have a clear picture of the paper. Let me proceed with calibration searches.Initial bracket: **4 to 6.5**. The paper has genuine theoretical contributions in a new area (CL + unlearning) but has a significant inconsistency between its abstract claim ("Hessian largely outperforms") and Figure 2(b), plus experiments run under assumptions that violate the theorems. Let me read relevant anchors and narrow further.Now I have sufficient anchors. Let me write the final review.

**Anchor comparison summary:**
- Round 1 weak anchors (2.5–3.0): Simple unlearning methods, rejected, clearly weaker
- Round 1 middle anchors: Privacy-Aware Lifelong Learning (6.25, Accept); UnCLe (5.75, Reject); In/Out-Dist Unlearning (6.60, Accept)
- Round 2 anchors: System Aware Unlearning (5.50, Reject); Provable Unlearning in Topic Models (5.75, Accept); HVFMooKrHX (6.60, Accept)

**Round-1 bracket: 4.5–6.5**

**Round-2 narrowing:** The paper has a genuinely novel setting and non-trivial theory (comparable to Provable Unlearning in Topic Models, 5.75, Accept), but the critical mismatch between (a) the abstract's central claim that "Hessian largely outperforms" and (b) Figure 2(b) showing the opposite, plus the deliberate assumption violation in experiments, pulls it below that anchor. HVFMooKrHX (6.60) is stronger: cleaner theory-experiment alignment, no internal contradiction. I place this paper slightly below Provable Unlearning at **5.0**.

---

## Summary

This paper establishes the first theoretical framework for certified machine unlearning within a continual learning (CL) setting. It introduces two adapted algorithms — a zero-storage "natural forgetting" approach (Algorithm 1) and a Hessian-based second-order correction algorithm (Algorithm 2) — and derives explicit post-unlearning excess risk bounds by decomposing the error into a CL excess risk term and an unlearning loss term. The analysis extends prior results from linear to nonlinear convex models. Light empirical validation is provided on MNIST with a 30-task setup.

---

## Strengths

- **Novel problem formulation and decomposition (Eqs. 6–7):** The separation of post-unlearning excess risk into "unlearning loss" (depending on the unlearning algorithm) and "CL excess risk" (depending on the CL algorithm) is clean and analytically useful. It enables the two terms to be bounded independently and combined, and forms the backbone of both Theorem 4.1 and Corollary 5.3.

- **Extension from linear to nonlinear convex models (Theorem 3.1):** The excess risk bound in Eq. (8) extends prior results (Lin et al., 2023) from linear models to general convex losses under ℓ₂-regularized CL. While the bound is complex, this extension is a real technical contribution — the heterogeneity terms ‖wᵢ* − wⱼ*‖ and the role of ρ = λ/(μ+λ) are explicitly tracked.

- **Hessian-based algorithm design for arbitrary unlearning sequences (Algorithm 2, Eq. 13):** The correction formula in Eq. (13) handles arbitrary (possibly disordered) unlearning request sequences, explicitly accounting for interference from prior corrections. The analysis in Proposition 5.1 and Proposition 5.2 (second-order bound under Hessian-Lipschitz) provides meaningful bounds on the approximation error, and Lemma 5.4's simplification for ordered request sequences yields a concrete storage-reduction insight.

- **Experiments illustrate the λ tradeoff:** Figure 2(a) and (b) together correctly demonstrate that the optimal λ for CL excess risk (range 5–10) differs from the optimal λ for unlearning loss (20–40), which is the paper's central practical insight about the balancing problem.

---

## Weaknesses

### Fatal
None.

### Major

- **Abstract claim directly contradicted by Figure 2(b).** The abstract states that "our Hessian-based adaptation algorithm largely outperforms the gradient-based algorithm," and the conclusion repeats "the Hessian-based method achieves lower unlearning loss." However, the paper's own description of Figure 2(b) shows the opposite: "The natural forgetting algorithm starts at approx. 0.10 and decreases slightly to approx. 0.08. The Hessian-based algorithm starts at approx. 0.24 and decreases to a plateau of approx. 0.20 for λ ≥ 40." Natural forgetting achieves consistently lower approximation error (unlearning loss) across all tested λ values. The paper does not explain or acknowledge this inversion. Table 1 shows the Hessian-based achieves high test accuracy at λ=30 (71.59%), but Algorithm 1's test accuracy at that same λ is never shown in Table 1, making the comparison incomplete. The abstract's comparative claim is stronger than what either the theory (which proves tightness only under Hessian-Lipschitz conditions not verified in experiment) or the experiments support.

- **Experimental setting violates the theorems' assumptions.** Section 6 explicitly states: "we relax its assumption of μ-strong convexity here in order to show the more general results under a non-strongly convex setting." But Theorem 3.1 and all subsequent bounds (Theorem 4.1, Corollary 5.3) require μ-strong convexity; the term ρ = λ/(μ+λ) and its role in controlling forgetting are only defined under strong convexity. Conducting experiments under a regime where the theorems technically do not apply, and presenting these as "validating our theoretical findings" (Section 6), is misleading for a theory paper. The experiments should either be conducted under a setting where the theorem assumptions hold (e.g., with a quadratic penalty making the problem strongly convex), or the paper should provide a separate analysis for the non-strongly convex case.

### Minor

- **Table 1 anomaly with no uncertainty quantification.** At λ=30, the Hessian-based unlearning achieves 71.59% test accuracy while perfect retraining achieves 71.05% — the unlearning algorithm *exceeds* its own target. This is impossible in expectation and almost certainly reflects single-run variance (no seeds, no error bars are reported). For a paper where the experiments are already minimal, reporting results from single runs without confidence intervals makes the Table 1 comparisons unreliable.

- **Internal model contains deleted task information (Section 4, footnote).** The paper acknowledges: "Alg. 1 internally maintains the secret model w_t for future continual learning on task t+1, which may still contain information from all deleted tasks." This is a conceptually significant gap — the certified guarantee applies only to the published model, not the internal state used for future training. While the paper defers resolution to Appendix C.2, the main text gives only one sentence on this, which understates its importance for a framework claiming certified privacy.

### Trivial

- The claim that individual sample unlearning (Footnote 1) is "easily extended" from task-level unlearning is unsubstantiated. Per-sample Hessians or per-sample gradient buffers would be needed, substantially increasing storage costs. This claim should be qualified.

---

## Nice-to-Haves

- Conduct at least one experiment under a genuinely strongly convex loss (e.g., ℓ₂-regularized logistic regression with a sufficiently large regularizer on a synthetic task sequence with controlled task heterogeneity). This would let the paper demonstrate the regime where the theorems actually hold.
- Provide a direct side-by-side comparison of Algorithm 1 vs. Algorithm 2 post-unlearning test accuracy (Table 1 only shows Hessian-based). The paper's central comparative claim requires both algorithms' combined performance.
- A dedicated figure comparing ordered vs. disordered unlearning request sequences for approximation error would make Lemma 5.4's practical relevance concrete.
- Provide confidence intervals across multiple seeds for Table 1.

---

## Removed Points

*These points are flagged to be removed — treat them with caution.*

- **Strength Finder's claim 3 (reversed):** "in Figure 2(b) the Hessian-based approximation error is significantly lower than that of the natural-forgetting algorithm, especially at larger λ." This is **factually wrong** — Figure 2(b) shows the opposite. Removed.

- **Strength Finder's claim 4 (Experiments validate the theory):** "Experiments validate the theory by showing the Hessian-based method attains 71.59% accuracy close to retraining." This is partially correct but misleading because (a) no Algorithm 1 comparison is shown at λ=30 in Table 1, and (b) the abstract's claim of "largely outperforms" is not validated by Fig 2(b). Strength partially removed.

- **Harsh critic's "non-trivial to extend to individual sample unlearning":** Valid concern but the paper positions it as a footnote extension, not a core claim. Kept as Trivial.

- **Harsh critic's claim about the precise content of Eq. (8)'s discussion of λ:** The concern that "it is not clear for what range of heterogeneity parameters λ=0 is better" is a precision nitpick. Appendix B.2 is cited. Removed (appendix content stripped from parser).

- **Harsh critic's framing about "cannot function" being imprecise:** The paper says prior algorithms "cannot function" in CL, which the harsh critic weakens to "would produce suboptimal solutions." The paper's claim is about the absence of theoretical guarantees in the CL setting, not that they produce undefined outputs. The original framing is defensible. Removed.

---

## Novel Insights

The paper's analysis of how unlearning request ordering affects approximation error (Proposition 5.1, Lemma 5.4) is the most practically insightful contribution beyond the problem setup. The observation that "disrupted" unlearning sequences — where later requests target tasks trained before the most recent unlearning time — incur additional error terms in Eq. (14), while well-ordered arrivals (tasks unlearned in chronological order) allow substantial storage savings via Algorithm 2's forgetting-enhanced variant, offers concrete guidance for system designers: when unlearning requests can be batched or delayed to arrive in order, both storage costs and approximation error can be simultaneously reduced. This insight does not appear in prior work on CL or unlearning and has practical implications for how unlearning request queues should be managed.

---

## Suggestions

1. Run experiments under strongly convex settings (e.g., logistic regression with L₂ regularization large enough to enforce strong convexity) and report results where Theorem 3.1's conditions provably hold.
2. Replace the abstract's "largely outperforms" claim with a precise statement tied to either the theoretical bound (Proposition 5.2) or a combined post-unlearning accuracy comparison (which requires adding Algorithm 1 to Table 1).
3. Report all Table 1 results averaged over at least 5 seeds with standard error to make the retraining comparison meaningful.
4. Add a paragraph in the main text (not just Appendix C.2) discussing the privacy implications of the internal model w_t retaining deleted task information.

---

## Score and Decision

**Axis evaluation:**
- *Originality*: High — first theoretical framework for this specific problem; extends linear-to-nonlinear; discovers ordering effects on unlearning error.
- *Importance*: High — CL + unlearning is a timely and relevant problem intersection.
- *Claims well-supported*: Weak — the abstract's central comparative claim is empirically contradicted; experiments violate theorem assumptions.
- *Soundness of experiments*: Poor — non-strongly convex setting, single runs, no comparison of Algorithm 1 in Table 1.
- *Clarity of writing*: Adequate — formalism is clear; bounds are complex but trackable; experimental narrative is misleading.
- *Value to community*: Moderate-to-high if the experimental issues are resolved.

**Anchor comparison:**
- Round 1: Paper sits in the 5–6.5 range.
- Round 2 narrowing: Below HVFMooKrHX (6.60, Accept) — that paper has better theory-experiment alignment and no internal contradiction. Comparable to or below Provable Unlearning in Topic Models (5.75, Accept) — similar "first theory in new setting" flavor but this paper has the experimental contradiction problem. Closer to System Aware Unlearning (5.50, Reject) in terms of experimental quality issues.

The paper's genuine theoretical novelty warrants recognition, but the contradiction between the abstract's core claim and Figure 2(b), combined with experiments conducted under assumption-violating conditions, means the paper does not clearly validate what it claims. This positions it as a **borderline reject** at 5.0.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>