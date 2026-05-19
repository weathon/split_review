- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 6, 5, 6
Now I have all the information I need. Let me compose the final consolidated review.

## Summary

This paper proposes "Wigner kernels"—a method for computing body-ordered equivariant kernels iteratively in kernel space via Wigner iterations (Eq. 4), thereby avoiding the exponential growth of the feature-space basis that limits methods like ACE when body order increases. The kernels require no explicit radial-chemical basis selection, scale linearly with body order, and achieve state-of-the-art accuracy on QM9 (4.3 meV MAE for energies, surpassing Allegro) as well as strong results on gold clusters and random methane.

## Strengths

1. **Iterative kernel construction that eliminates exponential scaling with body order**: The Wigner iteration (Eq. 4) builds body-ordered equivariant kernels with cost growing only linearly in maximum body order ν, whereas feature-space models like ACE/MTP/NICE grow exponentially. Section 3.1 explicitly contrasts this: "the possibility of computing the value of the kernel without any truncation, and eliminating completely the exponential scaling with ν_max is particularly appealing."

2. **State-of-the-art accuracy on QM9 energies**: Table 1 reports test MAE of 4.3 meV (σ=0.1), surpassing the prior best model Allegro (4.7 meV) and all other compared equivariant neural networks—achieved by a local, non-message-passing kernel model.

3. **Superior performance on vectorial (dipole) regression**: Figure 3 shows Wigner kernels avoid the saturation observed with optimized λ-SOAP kernels and achieve lower MAE across all training set sizes, attributed to the use of a full body-ordered equivariant kernel as opposed to the ν=2+nonlinear-scalar combination used in prior SA-GPR.

4. **Systematic body-order convergence on metallic clusters**: Figure 1 demonstrates that increasing ν (2→6) systematically lowers validation error for gold cluster energies. ν=6 outperforms both polynomial SOAP-GPR and LE-ACE, with the paper explicitly contrasting this against the non-systematic saturation of polynomial SOAP.

5. **High accuracy on random methane with low angular truncation**: Figure 2 shows Wigner kernels with λ_max=3 outperform SOAP-GPR (l_max=6) and NICE (λ_max=10) and are competitive with LE-ACE (l=20). The physical argument for why tensor-product structure generates higher-frequency components is clearly laid out.

## Weaknesses

### Fatal

None.

### Major

- **Missing computational-cost characterization**: The paper acknowledges the λ_max⁷ scaling of the Wigner iteration and argues that low λ_max suffices, but it never reports actual run times, memory usage, or scaling with dataset size. For a method whose practical viability depends on whether the λ_max⁷ vs. λ_max⁵ trade-off is favorable at realistic settings, this omission is significant. How long does training on 110k QM9 structures take? What is the per-iteration cost relative to computing explicit ACE features at equivalent ν and λ_max? Without this information, the reader cannot assess whether the method is a conceptual advance that happens to be practical or one that is currently too expensive for routine use. The paper honestly flags the limitation but provides no data to contextualize it.

### Minor

- **No error bars or multiple-run statistics on gold clusters and methane learning curves (Figs. 1–2)**: The QM9 results (Table 1, Fig. 4) properly report means and standard deviations over multiple train/test splits. The gold and methane figures show only single learning curves without any indication of variance. Since KRR has no stochasticity from the solver, variance comes from the train/test split; reporting this (as done for QM9) would strengthen the evidence, especially for the methane result where the Wigner kernel is claimed to rival LE-ACE.

- **Explanation for low-λ_max performance is plausible but unsubstantiated**: Section 3.2 argues that Wigner kernels with λ_max=3 match LE-ACE (l=20) because the tensor-product structure generates higher-frequency components (the sin² ωx analogy). This is physically reasonable but remains a hypothesis. The paper does not provide spectral analysis (e.g., kernel eigenvalue decomposition, effective rank comparison, or explicit demonstration that the kernel spans high-frequency functions at low λ_max). Given that the practical case for the method partly rests on low λ_max sufficing, stronger support would be valuable.

- **Cutoff radius values not reported**: The paper defines r_cut symbolically and mentions a cutoff function, but never states the specific cutoff radii used in any of the experiments. While this is a standard hyperparameter in atomistic ML, reporting the chosen values would improve reproducibility and allow readers to assess the locality assumptions.

### Trivial

- **Incomplete sentence at line 152**: "The integrals in Eq." is followed by a paragraph break with no completion. The ν=1 kernel equation (Eq. 5) is fully presented, so the closed form of the Gaussian overlap is inferable or standard, but this fragment should be completed.

## Nice-to-Haves

- **λ_max ablation study**: The methane results suggest saturation at λ_max=3. Showing QM9 results with λ_max=4 or 5 would confirm that low λ_max is not handicapping the model.
- **Statistical significance comment on QM9 energy improvement**: 4.3±0.1 vs. 4.7±0.2 (Allegro)—a brief comment on significance would be helpful.
- **Spectral analysis for the methane case**: Computing eigenvalues of the Wigner kernel matrix and comparing effective rank to LE-ACE at the same λ_max would turn the plausible explanation into a demonstrated property.

## Removed Points

- **"Incomplete specification of the ν=1 kernel as a reproducibility risk" (from harsh critic's Critical Issues)**: The ν=1 kernel equation (Eq. 5, labeled Eq. \ref{eq:nu1-kernels}) is fully presented in the main text. The sentence following it ("The integrals in Eq...") appears to be truncated, likely a parser artifact from PDF extraction. The Gaussian overlap integral of two Gaussians is a standard result, and any closed form would appear in the appendix. This does not constitute a reproducibility risk.

- **"Statistical significance of the QM9 improvement — paired test would help" (from harsh critic's Missing Parts)**: The paper already reports means and standard deviations over 16 splits, which is the standard reporting practice on this benchmark. Requesting a paired test goes beyond typical norms.

- **"Missing discussion on cutoff-radius sensitivity" (from harsh critic)**: Moved to Minor as the specific cutoff values not being reported is the real gap; sensitivity analysis is a nice-to-have.

## Novel Insights

An interesting thread that emerges across the harsh critic and strength finder is that the paper's theoretical framing—kernel-space iteration vs. feature-space expansion—implicitly redefines what "computational cost" means. In the feature-space ACE paradigm, cost is dominated by the basis size (exponential in ν). In the kernel-space paradigm, cost shifts to the angular momentum channel count (λ_max⁷). The paper convincingly shows that low λ_max works surprisingly well, but neither review fully explores whether this is because the kernel-space construction fundamentally changes the effective rank of the learned functions, or because the QM9/methane benchmarks have intrinsic spectral properties that happen to favor low λ_max. This question (is the λ_max efficiency a property of the method or the data?) is a natural follow-up the paper's framing invites but does not fully resolve.

## Suggestions

1. **Report wall-clock time and memory for the QM9 full-dataset run** (110k training points, λ_max=3, ν_max=4) with hardware specs. Even a rough breakdown (kernel construction, training solve, inference per structure) would transform the scaling discussion from asymptotic to actionable.
2. **Add error bars or multiple-split standard deviations to the gold clusters and methane learning curves**, consistent with the QM9 reporting.
3. **State the specific cutoff radius values** used in each experiment.
4. **Consider a brief spectral analysis** (e.g., kernel eigenvalue decay or effective rank comparison) to substantiate the claim that low-λ_max Wigner kernels span high-frequency components.
