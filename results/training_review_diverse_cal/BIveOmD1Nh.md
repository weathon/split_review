Now I have all the information I need. Let me synthesize the final review.

## Summary

This paper proposes a novel learned scoring function for molecular docking defined as the cross-correlation of equivariant scalar fields parameterized by E3NNs. The key insight is that this functional form enables rapid rigid-body pose optimization via fast Fourier transforms over both translational (ℝ³) and rotational (SO(3)) degrees of freedom, with computational cost amortizable across shared protein pockets. The method is evaluated on decoy pose scoring and rigid conformer docking using PDBBind crystal and ESMFold predicted structures, plus a PDE10A cross-docking set. Results show competitive accuracy with Vina/Gnina on crystal structures, superior robustness on predicted structures, and a 45× amortization speedup on the shared-pocket PDE10A dataset.

## Strengths

1. **Cross-correlation scoring function enables principled FFT-accelerated optimization**: The scoring function defined as the cross-correlation of learned scalar fields (Equation 1) is elegantly designed so that the convolution theorem applies, enabling simultaneous evaluation of all translations via FFT (160 μs) and all rotations via an SO(3) FFT (650 μs). This is orders of magnitude faster than per-pose neural network evaluations required by existing ML scoring functions (Table 1).

2. **Amortization yields dramatic speedups in the virtual screening setting**: On the PDE10A test set (77 ligands against a shared pocket), the RF procedure obtains a 45× speedup in total runtime (67 s → 1.5 s) with no loss of docking accuracy relative to baselines (Section 5.2). The paper carefully breaks down which computations are per-protein, per-ligand, and per-pose, making the amortization story concrete and credible.

3. **Superior robustness on predicted (ESMFold) protein structures**: On ESMFold structures where sidechain atoms are imperfectly predicted, ESF-N-RF achieves 47% docking success vs. 28% for Vina/Gnina (Table 3). In decoy scoring, ESF-TS obtains Top RMSD of 1.38 Å vs. 2.43 Å for Vina. This robustness is a direct consequence of the residue-level, learnable scalar field representation that does not explicitly depend on sidechain atom positions.

4. **Principled SE(3) equivariance guarantee**: Proposition 1 proves that the parameterization (Equation 2) with E3NN coefficient transformation yields an SE(3)-equivariant scalar field and an invariant scoring function, which is essential for enabling FFT-based optimization without re-evaluating the neural network for each pose.

5. **Efficient Fourier-domain formulation via analytic spherical Bessel transforms**: The closed-form expression for the Fourier transform of the scalar field (Equation 6) avoids explicit grid evaluation, and precomputation of the spherical Bessel transforms independently of molecular structure keeps per-example cost low.

## Weaknesses

### Fatal
None.

### Major
None. The paper's contributions are real and supported by evidence. The issues below are addressable and do not invalidate the core claims.

### Minor

1. **Training objective is an undiagnosed approximation.** The training loss (Section 3.4, Equations 7–8) maximizes conditional log-likelihoods p(translation | rotation) and p(rotation | translation) rather than the joint log-likelihood. The paper acknowledges only that "neither technically corresponds to the joint log-likelihood" and that the objectives "work well in practice." There is no theoretical or empirical analysis of whether these two conditional objectives conflict, whether the learned scoring function approximates a valid density, or how the sum-of-losses compares to alternatives. The empirical results are decent, which partially mitigates this concern, but the lack of any diagnostic (e.g., checking marginals, comparing to a joint loss, or analyzing calibration) leaves a methodological gap open. This is the most notable weakness.

2. **Acceleration framing overstates the general case.** The headline FFT runtimes (160 μs, 650 μs) reflect only the innermost kernel, not the full per-complex cost. On diverse-protein PDBBind (Table 3), ESF-RF total runtime is 67 s — slower than Vina (20 s) and Gnina (23 s). The paper acknowledges this ("comparable to or slower than the baselines when precomputations are taken into account") and correctly highlights the amortized PDE10A setting as the method's sweet spot. However, the introduction and title frame the contribution as accelerating "molecular docking" broadly, while the actual speed advantage is limited to (a) fixed protein pockets with many ligands and (b) the TF mode (8.3 s, faster than both baselines) rather than the more elaborate RF mode. A more precise upfront calibration of where the method excels versus where it does not would improve the paper.

3. **Rotational FFT projection error is unquantified.** To use the rotational FFT, the locally-defined scalar field must be projected onto a global spherical harmonic-radial basis via least squares (Equation 14/19). The paper acknowledges this "leads to a spatially coarser representation" and that RS underperforms TS, but does not quantify the projection error or its sensitivity to the choice of global basis (number of radial functions, maximum ℓ, grid discretization). The empirical gap between TS and RS is small (e.g., Table 2: ESF-TS Top RMSD 0.59 vs. ESF-RS 0.63), suggesting the error is not practically severe, but characterizing it would strengthen confidence in the rotational FFT as a core technical component.

4. **Missing grid specifications.** The paper repeatedly references grid-based evaluations (e.g., "evenly-spaced grid of points," "cube of side length 8 Å" for the search space) but never states the grid resolution or number of grid points used in any experiment. This information is essential for reproducibility and for understanding the runtime scaling reported in Table 1.

5. **ESF-N noise injection is introduced but not analyzed.** The ESF-N variant is trained with noise but receives no ablation or analysis — no noise level sensitivity, no mechanistic explanation of why it helps (beyond a brief mention of robustness), and no comparison showing the noise-robust fields are qualitatively different. Given that the robustness improvement on ESMFold structures is one of the paper's strongest results (47% vs. 28% success), understanding this component better would be valuable.

### Trivial
- The paper's title ("Molecular Docking") is broader than the evaluated scope (rigid conformer docking). The paper clearly scopes itself in the body, but the title could more precisely reflect the rigid-body focus.

## Nice-to-Haves
- A visualization of the learned scalar fields (e.g., for a known complex) and the corresponding cross-correlation maps would build reader intuition.
- A comparison of the FFT-based optimization runtime to a brute-force grid search at equivalent resolution would quantify the acceleration factor more directly.
- An analysis of how the gap between TF and RF modes (rotational search vs. rotational FFT) varies with the number of rotation samples would help practitioners choose between modes.

## Removed Points
- **Criticism about DiffDock comparison on docking**: The paper explicitly states "We do not evaluate these methods on pocket-level conformer docking as they cannot be easily adapted for this task." The reviewer's suggestion ignores this stated limitation.
- **Criticism about alpha-carbon assumption not being stated explicitly enough**: The paper states "the protein structure associated with alpha carbon coordinates" at line 54, at the start of the method section. This is appropriately placed and explicit.
- **Confusion about runtime breakdown in Table 1**: The paper explains that the per-translation global expansion is amortized across ligands in the PDE10A setting (Section 5.2, last paragraph). The reviewer's concern about computational cost is addressed by the amortization discussion.
- **Criticism about missing theoretical proofs**: The paper provides Proposition 1 with proof in Section 3.1. The reviewer's mention of "proofs in appendix" is a parser artifact — the paper contains the relevant proof in the main text.
- **Weaknesses about torsional flexibility**: The paper explicitly scopes itself to rigid conformer docking ("simplified docking-related tasks," "rigid conformer docking," conclusion mentioning torsional degrees of freedom as "future work"). Evaluating against the expectations of a full flexible-docking system is scope creep.

## Novel Insights
None beyond the paper's own contributions. The review surfaces no observation about the method, problem formulation, or results that the authors have not already articulated.

## Suggestions
- Add a diagnostic analysis of the training objective: compare the learned conditional scoring landscapes to empirical pose distributions, or train with a joint objective (e.g., NCE or contrastive loss) and compare performance.
- Quantify the rotational FFT projection error: for a set of test scalar fields, compute the RMS difference between the true field and the projected field, varying maximum ℓ, number of radial functions, and grid resolution.
- Report grid resolution and number of grid points used in all FFT-based experiments.
- Add an ablation study of the noise injection (ESF-N): vary noise magnitude and analyze its effect on field smoothness and docking accuracy.
- Recalibrate the framing: lead with the amortized virtual screening scenario (where the method excels) and present the diverse-protein results as "competitive but not universally faster," rather than the reverse.

## Score and Decision

**Originality**: High — first to propose learning cross-correlation based scoring functions for FFT-accelerated docking.  
**Importance**: High — addresses a real computational bottleneck in high-throughput virtual screening.  
**Claims**: Well-supported for the stated scope, though slightly overbroad in title and introductory framing.  
**Soundness**: Solid — careful experimental design, appropriate baselines, clear amortization analysis.  
**Clarity**: Well-written and structured; the method is explained clearly despite technical complexity.  
**Value**: A meaningful contribution that will be of interest to the molecular docking and ML for drug discovery communities.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>