Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper identifies and addresses a fundamental weakness in the diagonal initialization used by S4D/S5 state-space models: the non-uniform convergence of their transfer functions creates sensitivity to specific Fourier-mode input perturbations. The authors provide a rigorous theoretical analysis proving that the S4D/S5 initialization converges only weakly (pointwise for fixed smooth inputs) and fails uniformly, with persistent spikes in the transfer function. They propose a "perturb-then-diagonalize" (PTD) methodology that approximately diagonalizes the ill-conditioned HiPPO matrix by solving for a small perturbation E that keeps the eigenvector condition number manageable, yielding uniform (L∞) approximation guarantees (Theorem 3). The resulting S4-PTD and S5-PTD models demonstrate improved robustness to Fourier-mode noise and achieve strong LRA performance (S5-PTD: 87.61% average, highest among compared models).

## Strengths

- **Rigorous theoretical analysis of S4D vs. S4 convergence gap.** The paper derives an explicit closed-form formula for the transfer function difference (Lemma 1), proves weak* convergence with linear rate for fixed smooth inputs (Theorem 1), and, crucially, proves non-convergence in operator norm with persistent Θ(1)-magnitude spikes at frequencies Θ(n²) (Theorem 2, Figure 1). This goes well beyond prior empirical observations and provides a principled explanation for the diagonal models' fragility.

- **Identification and empirical demonstration of a novel failure mode.** Figure 2 shows that S4D catastrophically fails on a synthetic frequency-extrapolation task (predicted amplitude decreasing to −4 near s≈80), while S4 and S4-PTD do not. This failure is traced to the spike in |G_Diag|, and the real-world impact is confirmed on sCIFAR (Figure 3a,b): S4D accuracy drops significantly under Fourier-mode noise near spikes, whereas S4-PTD remains robust.

- **Clean theoretical guarantee for the PTD methodology.** Theorem 3 proves that the transfer function error between the perturbed system and the DPLR system scales as (2ln n + 4)ε + O(√(log n)ε²), showing linear dependence on perturbation size and only logarithmic dependence on state dimension. This provides a quantitative trade-off justifying approximate diagonalization, contrasting with the ad-hoc discarding of the low-rank term in S4D.

- **Empirical state-of-the-art on LRA.** S5-PTD achieves the highest average accuracy (87.61%) among all compared models on the Long-Range Arena benchmark (Table 1), and S4-PTD (86.58%) outperforms S4D (84.89%) and nearly matches S4 (86.09%). The robustness experiment on sCIFAR directly validates that the theoretical robustness translates to practical gains.

## Weaknesses

### Fatal
None.

### Major

- **The optimization procedure for Equation (4) is critically underspecified.** The paper states (line 383): "We implement a solver to this optimization problem using gradient descent." This single sentence is the only description of how the perturbation matrix E — the central object of the PTD methodology — is computed. The problem involves a non-trivial constrained optimization where the objective (κ(Ṽ_H)) and the constraint (eigendecomposition A_H+E = Ṽ_H Λ̃ Ṽ_H^{-1}) are coupled. The paper provides no details on: (i) what the actual optimization variables are (E alone, or jointly E, Ṽ_H, Λ̃), (ii) how gradients of κ(Ṽ_H) through the eigendecomposition are computed, (iii) initialization and convergence criteria, (iv) computational cost for the state sizes used (e.g., n=64, 128), or (v) whether the solver reliably converges across different γ values. The ablation study (Figure 3c) empirically validates the trade-off, showing the optimization was solved successfully for a range of γ, but without algorithmic details the method is not reproducible and cannot be adopted by other researchers for new initialization schemes. This is the paper's core methodological component — the models are named after it — and the current description is insufficient for a methods contribution.

### Minor

- **Ambiguity in the robustness experiment description.** The paper states (line 439) that the test set is "contaminated by 10% of sinusoidal noises whose frequencies are located near the spikes of |G_Diag|." It is unclear whether "10%" refers to the fraction of test samples corrupted, the amplitude of the noise relative to the signal, or some other quantity. The state dimension n used in this experiment is also not specified in the main text. (Some experimental details may be in the appendix section referenced at line 403, which was stripped by the parser.)

- **The synthetic experiment (Section 3.4) would benefit from more detail.** The paper states (line 226) that the goal is "to learn s and A from the sequential input," but does not specify the model architecture used for this task, the training procedure, or the number of training samples. (These details may reside in the stripped appendix.)

### Trivial
None.

## Nice-to-Haves

- **Comparison with random perturbation.** Theorem 4 (on Ginibre matrix perturbation) provides an expected bound on the condition number, and the paper could strengthen its case by comparing PTD's optimized perturbation against simply adding a random Gaussian matrix of the same norm without optimization. This would help isolate whether the optimization is genuinely necessary or whether any small perturbation regularizes the diagonalization adequately for SSM purposes.

- **Clarify the "strong convergence" framing.** The paper's use of "strong convergence" in the abstract and introduction correctly contrasts uniform (L∞) approximation of the transfer function (Theorem 3) with the pointwise/weak* convergence of S4D (Theorem 1) — a meaningful mathematical distinction. However, the practical magnitude of the bound for ε ≈ 0.1 is moderate (~O(1)), and a brief clarification that the term refers to the topology of convergence (uniform vs. pointwise) rather than implying small absolute error would prevent potential misinterpretation.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"The theoretical guarantee is too weak to support 'strong convergence'"** (from Harsh Critic #2). The paper's claim about "strong convergence" refers to uniform (L∞) convergence of the transfer function, contrasting with the weak*/pointwise convergence of S4D. This is a mathematically precise and well-supported distinction (Theorem 3 vs. Theorem 1). The critic conflates the type of convergence (topological property) with the magnitude of the bound. The bound's practical size for ε~0.1 is a separate issue and does not invalidate the uniform-convergence claim.

- **"Missing experimental details"** (synthetic experiment, robustness experiment details). The paper references \Cref{sec:experimentdetail} (line 403) for hyperparameter details and \Cref{sec:proofdifftransfer}, \Cref{sec:proofnoconverge} for deferred proofs. These sections were stripped by the parser and exist in the original submission. Per the meta-review guidelines, weaknesses about missing appendix content are removed.

- **"Comparison with random perturbation is missing"** as a weakness. This is a reasonable suggestion for future work but not a flaw in the current paper. The paper already provides a theoretical bound for random perturbation (Theorem 4) and shows that PTD's optimized perturbation works well empirically.

- **"Missing related works."** Per guidelines, I cannot confirm the existence or absence of missing citations.

- **Formatting/style nitpicks and claims about typos.** These are parser artifacts, not author errors.

## Novel Insights

The most interesting observation that emerges from the integration of the reviews is that the paper's theoretical contribution works at two different levels that are easy to conflate. First, the analysis of S4D's non-uniform convergence (Theorems 1-2, Lemma 1) is self-contained and does not depend on the PTD methodology at all — it stands as an independent contribution explaining why diagonal SSMs can be fragile. Second, the PTD methodology provides a principled solution whose theoretical guarantee (Theorem 3) cleanly quantifies the trade-off between perturbation size and approximation quality. These two halves — diagnosing the problem and providing a tunable solution — are somewhat decoupled, meaning the analytical contribution has value even independent of the PTD solver, and the PTD concept remains valid even if one implements the solver differently.

## Suggestions

1. **Fully specify the optimization algorithm for Equation (4).** This is the single most important revision. At minimum, the paper should state: the optimization variables (e.g., optimize over E while computing Ṽ_H, Λ̃ via an off-the-shelf eigendecomposition); how gradients of κ(Ṽ_H) are obtained (e.g., via automatic differentiation through the eigendecomposition, or a surrogate); the initialization scheme for E (e.g., a small random matrix or zeros); the stopping criterion; and the computational cost (e.g., wall-clock time to solve for n=64, 128). Pseudocode or a reference to a standard library routine would be ideal.

2. **Clarify the "10% of sinusoidal noises" description.** Specify whether this refers to the fraction of samples, the noise amplitude, or another quantity. Report the state dimension n used in the robustness experiment. These are small changes that greatly improve reproducibility.

3. **Consider adding a random-perturbation baseline** in the ablation study (or at least discussing it in the text) to help readers understand whether the optimization is necessary or whether simple random perturbation already achieves similar robustness.

## Score and Decision

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>