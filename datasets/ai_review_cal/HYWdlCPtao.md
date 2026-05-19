- Decision: Reject
- Avg Score: 6.25
- Scores: 6, 5, 6, 8
Now I have all the information needed to construct the final consolidated review. Let me compose it.

---

## Summary

This paper introduces CEMS (Curvature Enhanced Manifold Sampling), a data augmentation method for regression that uses second-order (Hessian-aware) local approximations of the data manifold. Building on the first-order FOMA framework, CEMS estimates both the gradient and Hessian of the normal-coordinate map g, samples a perturbation η in the tangent space, evaluates the second-order expansion of g, and un-projects to the ambient space. The method is evaluated on four in-distribution and five out-of-distribution regression benchmarks, achieving best or second-best results in nearly all settings. The paper also provides a theoretical error bound (Theorem 4.1) showing that second-order approximation error decays as O(‖u−u₀‖³) versus O(‖u−u₀‖²) for first-order.

## Strengths

- **Clear methodological extension of FOMA.** The paper explicitly shows how FOMA is a special case of CEMS (Section 4, "Comparison with FOMA"), where FOMA omits gradient/Hessian estimation and instead scales normal components. This frames CEMS as a principled generalization, not an ad-hoc modification.

- **Complexity analysis grounded in the manifold hypothesis.** The derivation of O(b²D) time complexity and O(bD + min(b,D)(b+D)) memory (Section 4, lines 102–117) shows that computational cost is governed by the intrinsic dimension d (which is assumed small), making the second-order approach plausible where naive second-order methods would be intractable.

- **Ablation validating the batch-wise variant.** Table 3 compares per-point basis estimation (CEMSₚ) against the shared-basis batch variant (CEMS) on three datasets, showing nearly identical errors while the batch variant avoids repeated SVD. This justifies a key practical design choice.

- **Strong OOD results on multiple benchmarks.** Table 2 shows CEMS achieves the best result in 6 of 9 metrics across five OOD datasets, with relative improvements of 1% and 8% on SkillCraft over the second-best method. This provides concrete evidence that the method delivers on its claimed generalization benefits.

- **Visual demonstration of curvature handling.** Figure 1 (described in Section 5.1) shows the sine-wave toy example where first-order approximations (FOMA and first-order CEMS) visibly deviate from the manifold near high-curvature points, while CEMS stays close.

## Weaknesses

### Fatal
None.

### Major

- **Baselines are not re-implemented under controlled conditions.** The paper explicitly states that "the results of all previous methods are reported as they appear in the corresponding original papers" (Section 5.2, line 168; Section 5.3, line 177). While the paper uses the same datasets and architectures as the baselines, not re-running baselines in a unified codebase means that uncontrolled factors (e.g., hyperparameter tuning protocols, data splits, training schedules, random seeds) could confound the comparison. This weakens the central quantitative claim of "superior" performance. The paper's empirical contribution would be substantially stronger with a controlled re-implementation.

### Minor

- **No ablation isolating the benefit of the second-order term.** The existing ablation (Table 3) compares per-point vs. batch-wise basis estimation. It does not compare CEMS to a first-order-only variant of CEMS itself (i.e., setting H=0). Figure 1C qualitatively shows a first-order CEMS on the sine example, but no quantitative comparison on real datasets isolates whether the Hessian term provides measurable gains on actual benchmarks. Such an ablation would directly test the core novelty.

- **Theoretical link between Theorem 4.1 and the sampling procedure is not fully explicit.** Theorem 4.1 provides standard Taylor remainder bounds for the full embedding map f. CEMS operates by approximating the normal-coordinate map g (via Eq. 2–3) and then composing with the linear basis projection. Since B_u is orthonormal, the error in f is proportional to the error in g, so the connection holds, but the paper does not explicitly argue this transfer. Additionally, the bound is local (requiring ‖u−u₀‖ small) while sampling uses a Gaussian with unbounded support — the paper does not discuss how the choice of σ interacts with the manifold's curvature scale to keep samples in the valid region.

- **No empirical runtime measurements.** The paper claims "mild computational overhead" (abstract) and provides complexity analysis, but reports no wall-clock time or FLOP comparisons against baselines. Given that CEMS adds per-batch SVD and per-point least-squares solves, timing data would help readers assess the practical cost.

- **No sensitivity analysis for key hyperparameters.** The paper does not report how results vary with the number of neighbors k or the Gaussian noise scale σ on any dataset. The limitations section (Section 6) acknowledges that the linear system may be underdetermined for large d, but no experiments test stability as k varies.

### Trivial
- The sine toy example (Section 5.1) is one-dimensional; this is appropriate for visualization but the paper could note that multi-dimensional toy settings would strengthen the illustration.

## Nice-to-Haves
- Adding a comparison against CEMS with H=0 (first-order only) on the real datasets would directly validate the second-order contribution.
- Reporting intrinsic dimension estimates d for the experimental datasets would help readers assess the method's practical regime.
- A brief discussion of how σ should be set relative to the manifold's curvature radius (or local neighborhood size) would strengthen the theoretical framing.

## Removed Points

These points are flagged to be removed, treat them with caution:

1. **"Missing standard deviations" (Harsh Critic: "Standard deviations are relegated to Appendix H, which is absent from the extracted text")** — Removed because the parser strips appendices; the original submission contains App. H. The paper states "Detailed results, including standard deviation, are available in App H" (Table 1 caption, line 153; Table 2 caption, line 181).

2. **"The paper does not explain how intrinsic dimension d is estimated"** — Removed as overly harsh: the paper cites a specific estimator (Facco et al., 2017) and states it is estimated in practice. Implementation details likely appear in the appendix.

3. **"Hyperparameters unspecified (k, σ, λ)"** — While the main paper does not list these in a dedicated table, the paper references App. F for "additional details on experimental settings and hyperparameters." The parser strips this appendix. The core concern about transparency is valid, but the information likely exists in the full submission.

4. **"Linear system of equations (Eq. 9) is referenced without being shown"** — Removed as a parser artifact; Eq. 9 is likely defined in Appendix A (which the paper references: "See also App. A for additional details").

5. **Several generic or speculative weaknesses from the Harsh Critic** (e.g., "the paper does not test whether the underdetermined system problem actually occurs," "batch adaptation is described only briefly") — These are not specific verified errors; they are suggestions for expansion. Moved here because they ask the paper to address issues outside its stated scope or beyond what is standard for a conference paper.

6. **Strength Finder's claim that "Theorem 4.1 directly supports the claim that CEMS provides a more accurate local manifold representation"** — This is retained as a valid strength (the theorem does support the motivation), but the strength finder's framing was slightly inflated; I have kept a measured version above.

## Novel Insights

None beyond the paper's own contributions. The two reviews largely surface the same issues from different angles. The most interesting observation is that the core gap in the paper — the missing H=0 ablation — is actually prefigured in the paper itself (Figure 1C shows a first-order CEMS qualitatively), yet the authors did not extend this comparison to the quantitative benchmarks. This suggests the authors have the machinery to run this ablation but chose not to report it, which is a missed opportunity to strengthen the paper's central claim.

## Suggestions

1. **Re-run the key baselines (at least FOMA and C-mixup) in the same codebase** with identical architectures, data splits, and evaluation protocol. Even a single dataset would substantially increase confidence in the comparisons.

2. **Add an ablation comparing CEMS against CEMS with H=0** (first-order only) on the real datasets. This directly tests whether the Hessian term provides measurable gains and is the cleanest way to justify the added complexity.

3. **Report wall-clock times** per epoch or per-batch for CEMS versus FOMA and the standard ERM baseline on at least one dataset, to substantiate the "mild computational overhead" claim.

4. **Include a sensitivity table** showing the effect of varying k and σ on one dataset, to give readers intuition about the method's robustness and to support the hyperparameter choices.

5. **Strengthen the theoretical narrative** by explicitly noting that because B_u is orthonormal, ‖f(u)−f̂(u)‖ = ‖[u,g(u)]−[u,ĝ(u)]‖ = ‖g(u)−ĝ(u)‖, so the error bound on f (Theorem 4.1) applies to the approximation of g, which is what CEMS actually computes.
