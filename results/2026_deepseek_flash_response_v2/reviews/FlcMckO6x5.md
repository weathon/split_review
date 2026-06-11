Now I have all the calibration data. Let me produce the final review.

## Summary

This paper provides a theoretical and methodological framework for separable neural networks (SepNNs). It makes three contributions: (1) a universal approximation theorem proving that CP, TT, and Tucker SepNNs can approximate any continuous multivariate function on compact sets; (2) NTK regime analysis for SepNNs under both deterministic (infinite width + infinite rank) and random (infinite width, fixed rank) asymptotic regimes; and (3) a separable preconditioned gradient descent (SepPGD) method that exploits the separable structure to achieve O(nD) complexity for n^D grid training samples — an exponential reduction over prior PGD methods. Experiments on kernel ridge regression, implicit neural representations, and PINNs demonstrate the practical benefits.

## Strengths

- **Unified universal approximation theorem for all three SepNN forms (Theorem 1).** The proof uses Stone-Weierstrass combined with vector-valued universal approximation, providing a single framework covering CP, TT, and Tucker decomposition types. This extends the prior bivariate-only result (Cho et al., 2023) to arbitrary D and multiple decomposition forms. The proof sketch in the main paper (lines 74–82) is clear, and the claim is well-supported.

- **Dual NTK regime characterization (Theorem 2, Corollary 1).** The paper derives the SepNN NTK (Lemma 1, line 102–106) and proves convergence to a deterministic kernel under infinite width+rank and to a stochastic kernel under infinite width+fixed rank. This dual characterization goes beyond standard MLP NTK analysis, is motivated by the practical distinction between these regimes (line 128), and is empirically validated in Figure 1 with variance over 10 random seeds.

- **Exponential-to-linear complexity reduction for preconditioning (Table 1, Lemma 2).** SepPGD achieves O(nD) complexity for n^D samples compared to O(n^D) for the standard NTK-based PGD (Geifman et al., 2024) and O(n^D/p) for mini-batch variants (Shi et al., 2025). Lemma 2 proves equivalence to classical NTK-based PGD for D=2 under a Kronecker-structured preconditioner (line 197), demonstrating that the efficiency gain does not sacrifice the preconditioning structure. The complexity comparison (line 174) and the equivalence proof are well-supported.

## Weaknesses

### Fatal
None.

### Major

- **Claim-evidence gap on "provably" adjusting the NTK spectrum.** The abstract (line 9) and contribution list (line 50) state that SepPGD "provably adjusts the eigenvalue distribution of NTK matrix, effectively alleviating spectral bias." However, the theoretical argument in Section 4 (line 201) is conditioned on an assumption: "Suppose that  $\tilde{\mathbf{K}}$  is close to the true NTK matrix  $\mathbf{K}$  which can be verified using the NTK matrix formulation in Lemma 3." The true SepNN NTK (Lemma 1) involves factor output coupling terms $\mathbf{a}_d(\mathbf{x})$ that the Kronecker-sum approximation $\tilde{\mathbf{K}} = \mathbf{K}_{\Theta_1}\otimes\mathbf{I} + \mathbf{I}\otimes\mathbf{K}_{\Theta_2}$ drops, and establishing closeness of these matrices under any meaningful norm is non-trivial. The main text then concludes that SepPGD "could provably" adjust the spectrum — shifting from the definite "provably" of the abstract to hedged "could provably" in the body. The paper references Lemma 3 (in the appendix) to fill this gap. While the appendix may provide the missing steps, the *main text as written* uses conditional language that contradicts the strong claim in the front matter. Either the full argument (with explicit theorem and assumptions) should be presented in the main paper, or the "provably" language should be retracted and the contribution reframed as a well-motivated heuristic with rigorous complexity guarantees.

- **Experiments lack statistical rigor.** None of the reported metrics (MSE for KRR and PINNs, PSNR for image representation, IoU for surface representation) are accompanied by error bars, confidence intervals, or standard deviations across multiple runs. Figures 2–4 present single-run convergence curves and single-number performance values. For example, Figure 3 reports PSNR values of 26.48 (SepNN) vs. 33.30 (SepPGD) without any variance information, making it impossible to assess whether improvements are statistically reliable. Only Figure 1 (NTK validation) reports variance over 10 random seeds. This is a significant gap for an empirical section that claims to "validate the effectiveness" of the proposed method.

### Minor

- **Only CP-form SepNNs are tested.** The universal approximation theorem covers CP, TT, and Tucker forms, and the NTK analysis focuses on CP (footnote 1 states extension "can be readily extended"). However, all experiments (KRR, image/surface INRs, PINNs) use only CP-form SepNNs. At least one experiment demonstrating SepPGD on TT or Tucker SepNNs would strengthen the claim of generality.

- **No ablation of the rank parameter R.** The rank R controls both SepNN capacity and the SepPGD preconditioner computation. The paper does not include any experiment showing how performance varies with R.

### Trivial
None.

## Nice-to-Haves

- Include the full (non-separable) NTK-based PGD as a baseline on a small-scale problem where O(n^D) is tractable, to directly quantify the approximation error of the Kronecker-structured preconditioner relative to the exact one.
- Add an ablation study of rank R across tasks.
- Include a limitations paragraph discussing when SepPGD may be less effective (e.g., small D, non-grid data where the Kronecker structure does not apply).
- Report wall-clock training time that accounts for the overhead of constructing $\mathbf{S}_d$ (NTK computation and eigendecomposition for each factor).

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"Spectral bias analysis recapitulates standard NTK theory."** — This is an observation, not a weakness. The paper's Section 3 contribution is the SepNN-specific NTK derivation (Lemma 1) and the dual-regime analysis (Theorem 2, Corollary 1). The spectral bias discussion (Equation 5) explicitly notes it follows standard NTK analysis applied to SepNNs. The paper does not claim novelty for this derivational step. Removed because critiques a non-claimed contribution.

2. **"Full NTK-based PGD baseline not included."** — The paper explicitly compares against MSK (Modified Spectrum Kernel), which IS the full NTK-based PGD method from Geifman et al. (2024). The KRR experiment description (line 221) states "compare SepPGD with the classical NTK-based PGD, the modified spectrum kernel (MSK)." Removed as factually incorrect.

3. **"No comparison of wall-clock training time."** — The convergence curves in Figure 2 are plotted against execution time, not iteration number. Removed because the paper already does this.

4. **Criticisms about missing appendix content, absent references, unspecified hyperparameters.** — The parser strips appendices and references from all papers; they exist in the original submission. These criticisms cannot be evaluated from the available text and are removed per filtering rules.

5. **Strength Finder's generic strengths** (e.g., "addresses an important problem"). — Removed as generic/superficial.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

- **Resolve the "provably" claim-evidence gap.** Either bring Lemma 3's full argument into the main text with a clear theorem stating assumptions and conclusions, or honestly characterize SepPGD as a theoretically-motivated heuristic with rigorous complexity guarantees and strong empirical support.
- **Add statistical reporting** (error bars, confidence intervals, or run-to-run variance) to all experimental results.
- **Test SepPGD on at least one TT or Tucker SepNN problem** to support the claimed generality.
- **Include an ablation study** over rank R.
- **Explicitly state limitations** of SepPGD (small D, non-grid data scenarios).

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>