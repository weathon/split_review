- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 3, 5, 8
Now I have a clear picture of the paper's content. Let me finalize the consolidated review.

---

## Summary

This paper introduces and formalizes the problem of *temporal label noise* — label corruption that varies over time in sequential classification tasks. It proposes (i) backward and forward sequence losses that are provably robust when the temporal noise function Q(t) is known, and (ii) TENOR, a method that jointly learns a classifier and estimates Q(t) from data using a neural network parameterization with a volume-minimization penalty. Experiments on synthetic and four real-world time-series datasets show that temporal methods outperform static baselines.

## Strengths

- **Novel problem formalization**: Section 3 and Definition 1 are the first to formalize label noise that varies over time in sequential classification, giving a precise matrix-valued noise function Q(t). This provides a clear foundation for a genuinely underexplored problem.
- **Provably robust loss functions extended to temporal setting**: Theorems 1 and 2 show that the backward and forward sequence losses yield consistent estimators when Q(t) is known, extending static noise-robust losses (Patrini et al.) to the temporal setting.
- **TENOR learns the noise function from data without prior knowledge**: Section 4.3 presents the first method to explicitly model and estimate temporal label noise using a neural-network parameterization of Q(t) jointly trained with the classifier.
- **Strong empirical evidence**: Table 1 shows temporal methods consistently outperform static baselines across all five datasets, with TENOR achieving the best clean-test accuracy and Q(t) reconstruction error (MAE) in most cases. Table 2 and Figure 3 confirm these gains across six different temporal noise functions and varying noise levels.
- **Demonstrates that ignoring temporal structure degrades performance**: Figure 2 directly compares using the true temporal Q(t) vs. a static average approximation, showing the static approximation consistently underperforms — particularly for mixed noise. This provides clean evidence that temporal modeling is necessary.
- **Diverse evaluation with realistic temporal noise functions**: Six functional forms of noise (exponential decay, linear decay, sigmoid, sinusoidal, mixed, and time-independent) are tested on four real-world sequential tasks, strengthening generalization claims.

## Weaknesses

### Fatal
None.

### Major

- **Unsubstantiated claim about TENOR's volume penalty**: The paper states (line 167) that "Given the constraints imposed in Definition 1, minimizing the Frobenius norm of Q, a convex function, amounts to minimizing the volume of Q." This claim is presented as fact without proof or citation. The minimum-volume simplex framework (Li et al. [25]) uses the determinant/log-determinant — not the Frobenius norm — as the proper measure of simplex volume. Meanwhile, VolMinTime (Eq. 6) correctly uses log-det, creating an inconsistency: the authors seem aware of the correct measure but substitute a different one for TENOR without justification. The Frobenius norm as a volume surrogate is not generally equivalent, and the paper's stated justification is insufficient. This does **not** invalidate TENOR's empirical results (the Frobenius norm may still act as a useful regularizer), but it means the method's theoretical grounding for identifiability is incomplete. The authors should either provide a justification, replace the penalty with log-det, or reframe the motivation.

- **Theorem 2 uses undefined notation**: The right-hand side of Theorem 2's equation uses ℓ_{t,φ}(⋅) which is never defined in the paper. Only ℓ_{t,ψ}(⋅) (with ψ as the link function) is defined in Definition 3. This makes the theorem's statement incomplete and unverifiable as written. Additionally, the verbal claim ("maximizes the empirical likelihood of the data over the clean labels") is imprecise — the standard result is consistency of the argmin, not equivalence of the loss values. The theorem should be restated with clearly defined notation and framed as a consistency result.

### Minor

- **Backward loss numerical stability acknowledged but not analyzed**: The paper notes (line 260) that the backward sequence loss requires inverting Q_t at each time step, and that "the inverse-determinant of the matrix will scale the loss and therefore the gradients," attributing underperformance to "gradient-related issues." However, no analysis is provided of when Q_t is invertible, how near-singular matrices are handled, or what regularization (if any) is applied. Figure 2 shows the backward loss frequently underperforms the forward loss, but without controlled analysis the cause remains speculative.

- **Statistical significance not assessed**: Results are reported as mean ± std over 10 runs, but no pairwise significance tests or effect sizes are provided. In cases where error bars overlap (e.g., the critic estimates ~2% std with differences ~2% for some comparisons), it is unclear whether improvements are statistically robust. Standard practice in this setting is to include at least a discussion of significance or confidence intervals.

- **Overstated "state-of-the-art" claim**: The abstract claims "state-of-the-art performance," but since no prior temporal noise methods exist, the comparisons are necessarily against self-constructed extensions of static methods. The paper should qualify this as "outperforms static baselines and their temporal extensions." This is a minor overclaim given the lack of external prior art.

- **Single classifier architecture**: All experiments use a GRU-based classifier. Given the variety of sequential architectures (LSTM, Transformers), testing a second architecture on at least one dataset would strengthen generalizability claims.

### Trivial

- The notation in the Theorem 2 equation uses both ψ (in the left-side →ℓ_{seq,ψ}) and φ (in the right-side ℓ_{t,φ}) without distinguishing or defining the latter. This is a typographical/inconsistency issue that should be fixed.

## Nice-to-Haves

- Include a clean-label oracle baseline to contextualize how far all methods are from the upper bound.
- Add an ablation study isolating the benefit of temporal coupling (TENOR's neural network across time) vs. the volume penalty — comparing TENOR with a corrected volume penalty against VolMinTime would clarify the source of improvement.
- Provide controlled analysis of forward vs. backward loss gradient behavior (e.g., gradient norms, convergence curves) for at least one dataset.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"The proofs are not in the body, so the reader cannot verify them"** — Removed per hard rules: appendix content is stripped by the parser and exists in the original submission.
- **"No discussion of hyperparameter selection for the augmented Lagrangian (λ, c, penalty schedule)"** — Removed per hard rules: this is a reproducibility nitpick about undisclosed hyperparameters, not a substantive flaw.
- **Frobenius norm called "conceptually wrong" / "structural flaw"** — Downgraded from the critic's "fatal/structural" framing to Major. While the justification is insufficient, the relationship between Frobenius norm and volume for row-stochastic, diagonally dominant matrices is not *clearly false* (it holds for the 2×2 case and may approximately hold more generally); the real problem is the lack of proof or citation, not a "conceptual error."
- **"TENOR's reported improvements may arise from regularization rather than correctly identifying Q(t)"** — This is speculation that the reviewer cannot verify from the paper. The empirical Q(t) reconstruction error (MAE) in Table 1 provides evidence that TENOR does learn Q(t) reasonably well.
- **Strength Finder: generic/problem-importance strengths** — Removed per filtering rules (e.g., "this paper addressed an important problem"). Only concrete, evidence-grounded strengths are retained.
- **Criticism that baselines are "self-constructed" as a weakness** — Downgraded: since no prior temporal methods exist, any baseline must be constructed. This is a limitation of the problem area, not the paper. Reframed as part of the "state-of-the-art" overclaim above.

## Novel Insights

None beyond the paper's own contributions. The reviews surface no genuinely novel observation about the paper that the paper itself does not already articulate. The key insight from the reviews is that the discrepancy between TENOR's Frobenius-norm penalty and VolMinTime's log-det penalty warrants deeper justification — this is a gap the authors can address, not a discovery.

## Suggestions

1. **Fix the volume penalty**: Either replace ∥Q_ω(t)∥_F in Eq. (4) with a proper log-det penalty (consistent with the VolMinTime formulation), or provide a rigorous justification (proof or citation) for why the Frobenius norm serves as a valid convex surrogate for simplex volume under the constraints of Definition 1. If the latter route is taken, also explain why the same surrogate was not used in VolMinTime.
2. **Clarify Theorem 2**: Define ℓ_{t,φ} explicitly. Restate the theorem as a consistency result (argmin equivalence under correct specification) rather than making an imprecise claim about "maximizing likelihood."
3. **Address backward loss numerical stability**: Add a brief analysis or at minimum a practical note about conditions under which Q_t is invertible, and whether regularization (e.g., adding ϵI) is used.
4. **Add statistical significance**: Include pairwise tests (e.g., paired t-test or Wilcoxon) or report confidence intervals for key comparisons in Tables 1 and 2.
5. **Qualify the "state-of-the-art" claim**: Rephrase to reflect that comparisons are against static methods and their natural temporal extensions, since no prior temporal noise methods exist.
6. **Add a second architecture**: Test one additional sequential classifier (e.g., LSTM) on at least one dataset to strengthen generalizability.
