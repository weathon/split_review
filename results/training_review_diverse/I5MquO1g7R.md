Now I have a comprehensive understanding. Let me write the final review.

---

## Summary

This paper proposes TV-HMM, a time-varying hidden Markov model for offline change point detection. The key idea is to encode change point locations via a left-to-right Markov chain with a learnable upper-triangular transition matrix; diagonal entries can converge to 1 during learning, automatically pruning redundant change points. The paper presents a variational EM algorithm with stochastic approximation for inference, a theoretical consistency result for change point location estimation, and a semi-parametric extension using Maximum Mean Discrepancy (MMD) to remove distributional assumptions.

## Strengths

- **Novel modeling approach with automatic selection of the number of change points.** Encoding change point locations via a time-varying transition matrix with learnable entries is a genuinely creative idea. The ARD-like behavior where diagonal elements of Πₖ converge to 1 effectively prunes spurious regimes without requiring the user to specify the number of change points *a priori*. This is illustrated empirically in Figure 2(c,d), where the converged transition matrix becomes sparse with mass concentrated at true locations and diagonals — a concrete demonstration that the mechanism works.

- **Semi-parametric MMD extension removes parametric assumptions.** Generalizing the likelihood term to a kernel-based MMD distance and deriving an MMD-ELBO objective (Section 4) is a principled extension. The paper explicitly shows the connection to the parametric Gaussian case (where the term reduces to MMD with linear kernel), and reports promising Rand index values (0.94, 0.87, 0.89) on three non-Gaussian distributions (Poisson, chi-squared, exponential) without incorporating distributional knowledge. This extension is useful for practitioners working with data where parametric assumptions are hard to justify.

- **Stochastic approximation reduces per-iteration cost from O(K N²) to O(K S²).** The chronological subsampling scheme is practical and the paper reports convergence within ~30 iterations, suggesting real applicability to long sequences.

## Weaknesses

### Major

- **Theorem 1 is garbled and its logical content cannot be verified as stated.** The core theoretical claim — the paper's headline contribution — is presented in a form that is not coherent. The piecewise function in Equation (line 138-140) has mismatched cases (the "if n=T_k" case is paired with a rate that would be O(1) at that point, and the case boundaries are unclear). The second unlabeled equation (line 143) seems intended for junction points but its relationship to the first equation is unspecified. The Remark (line 146) cuts off mid-sentence ("those segments whose lel"). More substantively, the theorem appears to assert that both junction and non-junction points' marginals concentrate on the true locations, but the paper never formally establishes the mechanism by which redundant points are discarded — the Remark gestures at "unduplicated set" but this is not derived from any stated property of the marginals or of Πₖ. The connection between the ARD behavior of Πₖ (diagonal elements → 1) and the consistency theorem is never formally established. Until the theorem is restated with unambiguous cases, clearly separated behavior for junction vs. non-junction points, and an explicit link to the pruning mechanism, the paper's central theoretical contribution is not assessable.

- **Algorithm 1 is incompletely specified.** Several critical steps are missing or heuristic: (i) Line 8 reads "Set new prior by" with no continuation — a core update step is simply absent. (ii) The update for πₖ (π ← π + η · Q^S(...)) is presented as an M-step but is not derived from maximizing the ELBO with respect to Π; it is stochastic gradient ascent on an unspecified objective with no convergence guarantee. (iii) The message-passing in the E-step (line 5) has garbled conditional logic ("if m,n ∈ Ω, ..., or n=1,1,...,N"). These gaps make it impossible to reproduce the algorithm from the description alone. A conference paper's inference routine must be fully specified.

### Minor

- **The empirical evaluation is too narrow to fully support the claimed advantages.** The simulated comparison (Table 1) uses only the Rand index — while defensible as a partition-similarity metric, standard CPD metrics (F1 score, Hausdorff distance, coverage probability) are absent, making comparison with the broader literature difficult. The semi-parametric experiments (Section 4) report promising Rand indices on three non-Gaussian datasets but include **no baselines at all** — there is no comparison showing that the MMD extension improves over a misspecified parametric TV-HMM on the same data. The real-data experiment (Well-log) is qualitative only, with no quantitative metric. These are not fatal omissions but they weaken the otherwise interesting empirical claims.

- **No ablation studies.** The method has several tunable components (initial overspecification factor K̃, subset size S, step size η, constant G), yet none are ablated. Readers cannot gauge sensitivity or get guidance on how to set these in practice.

- **Assumption A3 is strong.** It requires an initial grid where each segment either contains exactly one true change point or lies entirely within a true regime. This effectively assumes a "good" initialization that matches the unknown structure at a coarse level. While such assumptions are common in theoretical CPD analyses, their strength should be acknowledged more explicitly and the paper would benefit from discussing what happens when A3 is violated (e.g., two true change points in one initial segment).

### Trivial

- The visual quality of Figure 2(c,d) heatmaps is low (images appear to suffer from resolution issues in the extracted PDF).
- Notation inconsistencies: line 50 has stray characters ("K+1$ $\{p(\theta_{k};\alpha_{k})\}_{k=1}^{K+1}$ $\alpha_{k}$ $k$").

## Nice-to-Haves

- A comparison of the parametric TV-HMM against the MMD-based TV-HMM on the same non-Gaussian data to directly measure the benefit of the semi-parametric extension.
- A comparison against at least one standard penalty-based method (e.g., PELT with a suitable cost) to contextualize performance against the broader CPD literature.
- An ablation varying the initial over-specification factor K̃ to show the method's robustness to this hyperparameter.

## Removed Points

- **"Sign error in MMD-ELBO (factor (m-n-1) vs (n-m+1))":** Removed. The message functions use exp(-(n-m+1)/G · MMD) and the ELBO term is (m-n-1)/G · MMD. Since (m-n-1) = -(n-m+1), these are algebraically identical. No sign error exists.
- **"Mean-field assumption broken by joint Q(t₁,...,t_K)":** Removed. The paper uses a structured mean-field that factorizes θ from t while keeping the t's as a joint distribution, then extracts marginals via sum-product. This is a standard and valid variational approximation, not an error.
- **"Missing related works":** Removed per instructions (cannot verify existence of missing references without external sources).
- **"Reproducibility concerns about hyperparameters, trivial implementation details":** Removed per instructions — these are impractical to include in a submission.
- **"Missing appendix/proofs":** Removed per instructions — the parser strips these; they exist in the original submission.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a genuine tension: the paper has a clever modeling idea (time-varying transition matrix for automatic CP count selection) and a useful extension (MMD-based distribution-free CPD), but its presentation of the theoretical result is too garbled to evaluate, and the algorithm is incompletely described. The core innovation deserves scrutiny on its own terms, but the current write-up does not yet deliver a verifiable paper.

## Suggestions

1. **Restate Theorem 1 completely.** Separate the junction-point and non-junction-point cases with clear, independent equations. State explicitly what happens to each marginal Q(t_i) as N→∞ for both cases, and explain — in a sentence with a complete predicate — how the algorithm recovers the unduplicated set {T_k}. Connect this to the ARD property of Π_k or explicitly derive that redundant marginals collapse to the same mode.

2. **Complete Algorithm 1.** Specify every step. Derive the M-step for Π from the ELBO (or justify the gradient step as a natural gradient / stochastic variational inference update with a reference). Complete line 8. Fix the garbled conditional in line 5.

3. **Add at least one baseline to the semi-parametric experiment.** Compare the MMD-based TV-HMM to the parametric TV-HMM on the same non-Gaussian data to demonstrate that the MMD extension provides a concrete benefit under model misspecification.

4. **Add ablation studies.** Vary the initial overspecification factor K̃, subset size S, and step size η to show sensitivity and provide practical guidance to users.

## Score and Decision

The paper introduces interesting ideas — the time-varying transition matrix for automatic CP count selection and the MMD-based semi-parametric extension are both genuinely creative. However, the main theoretical contribution (Theorem 1) is presented in a form that cannot be verified, and the inference algorithm is incompletely specified. In a conference setting where claims must be assessable and methods reproducible, these are significant barriers. The ideas are salvageable, but the paper in its current form does not meet the bar for acceptance.

MY FINAL SCORE: <pineapple>3.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>