Now I have a thorough understanding of the paper and can verify the reviewer's claims against the actual text. Let me produce the final consolidated review.

## Summary

This paper introduces NN-ResDMD, a method that learns Koopman eigenpairs by minimizing the spectral residual (from ResDMD) using neural-network-parameterized dictionaries. The core idea — using the spectral residual as a training loss rather than as a post-hoc filter on precomputed eigenpairs — is well-motivated and eliminates the need for manual basis selection. The method is demonstrated on a pendulum system, a turbulent flow, and neural recordings from mouse visual cortex.

## Strengths

- **Direct spectral-residual minimization as a learning objective**: Unlike ResDMD, which filters spurious eigenpairs from EDMD, NN-ResDMD directly optimizes the total spectral residual \(J\) (Eq. 3.4) to learn Koopman eigenpairs. This reframing of the spectral residual from evaluation metric to loss function is the paper's core contribution and is principled (Section 3.2).

- **Automatic basis-function learning replacing manual selection**: By parameterizing dictionary functions with a feedforward network and minimizing \(J(\theta)\), the method eliminates the need for hand-crafted basis functions (Fourier, Hermite, RBF) whose optimal choice is unknown a priori. This is demonstrated on a high-dimensional turbulence system (~30k dimensions) and neural data (>7k neurons) where traditional basis design is impractical (Sections 4.2, 4.3).

- **Demonstration across diverse dynamical regimes**: The method is validated on a measure-preserving system (pendulum), a high-dimensional fluid system, and real biological neural data — three settings with fundamentally different spectral structures, showing broad applicability.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **Pendulum comparison does not isolate the source of improvement.** The paper claims NN-ResDMD needs fewer basis functions (300) than ResDMD (964) to capture the full pendulum spectrum, presenting this as evidence of efficiency. However, the comparison conflates two factors: (a) the spectral-residual loss function, and (b) the greater per-function expressivity of NN-generated dictionary functions (which are learned from data via a network with many internal parameters) versus fixed Hermite/Fourier functions. The paper does not include an ablation that trains the *same* neural network architecture while minimizing the standard EDMD prediction loss \(\|\Psi_Y - \Psi_X K\|_F^2\) instead of the spectral residual \(J\). Without this, it is unclear whether the advantage comes from the spectral-residual objective or simply from using a flexible neural network to parameterize the dictionary.

- **Turbulence experiment relies on purely qualitative evidence.** The claim that NN-ResDMD's first Koopman mode reveals pressure-field patterns that Kernel ResDMD and Hankel-DMD "cannot" is supported by a single figure with no quantitative metric (e.g., correlation with the true pressure field, reconstruction error, or mode stability across runs). Comparing against Kernel ResDMD with a "generic normalized Gaussian kernel" without exploring alternative kernel choices further weakens the comparison (Section 4.2, Figure 5).

- **Neural dynamics evaluation does not control for differing eigenfunction dimensionality.** The competing methods produce very different numbers of eigenfunctions (NN-ResDMD: 501, Hankel-DMD: 50, EDMD+RBF: 1301, Kernel ResDMD: 299). The Davies-Bouldin Index is sensitive to cluster count and dimensionality, yet the paper does not report whether the advantage persists when methods are matched in eigenfunction count (e.g., truncating NN-ResDMD to 50 eigenfunctions for a direct comparison with Hankel-DMD). Additionally, no error bars, statistical significance tests, or alternative clustering metrics are reported across the five mice, although individual mouse DBI values are shown in Figure 6F (Section 4.3).

- **Theoretical guarantees are slightly overclaimed.** The paper states that NN-ResDMD "retains the theoretical convergence guarantees that EDMD lacks" (Section 3.2). ResDMD's convergence guarantees (Colbrook & Townsend, 2024) apply to the spectral residual as a filter on computed eigenpairs assuming a fixed dictionary. Whether these guarantees transfer to dictionaries *learned* via non-convex optimization is not analyzed — the paper provides no bound connecting the minimized empirical residual to the true residual for learned dictionaries, and no discussion of when the learning problem is well-posed. The weaker assumption (closed/densely defined vs. bounded operator) is genuinely inherited from ResDMD, but this is a fact about the operator class, not a convergence guarantee about the learning procedure.

- **Reproducibility details are incomplete.** The neural network hidden layer sizes are not specified (the paper only says "each hidden layer size can be specified during training"). The regularization parameter \(\sigma\) for the Koopman matrix inversion, the learning rate, number of epochs, and the stopping criterion for alternating optimization are also omitted. These are needed to reproduce the results.

### Trivial

None.

## Nice-to-Haves

- A convergence study in the pendulum experiment showing that the shaded pseudospectral region collapses toward the unit circle as dictionary size or data increases, which would strengthen the interpretation of the pseudospectrum plots.
- A comparison between NN-ResDMD and a variant of Kernel ResDMD with a data-adapted kernel (e.g., using the neural network embedding as a kernel) to make the turbulence comparison more informative.
- Standard deviations or confidence intervals across multiple runs for all quantitative results.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Claim about sentence fragment "here.5)" in conclusion:** This is a PDF-parser artifact — the original submission does not have this formatting issue. Removed per parser-artifact rule.
- **Claim that the paper should "also cover Y / domain Z":** The reviewer suggests matching the effective number of trainable parameters between methods, but the paper's claim is about dictionary/output dimension (a standard metric in Koopman methods, since it determines the Koopman matrix size). The comparison is valid on its own terms; the real gap is the missing ablation isolating the loss function, which is kept above. Removed (partly mischaracterized).
- **Strengths conflict rule — removed "Retains theoretical convergence guarantees of ResDMD":** This strength conflicts with the verified weakness about overclaimed theoretical guarantees. The paper does build on weaker operator assumptions than EDMD, but claiming the method "retains" convergence guarantees without analyzing the learning component is an overstatement. Strength dropped per conflict rule.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the expected concerns about ablation design and quantitative rigor but do not contribute a novel perspective not already apparent from reading the paper.

## Suggestions

- Add an ablation experiment: train the same neural network architecture while minimizing the EDMD prediction loss \(\|\Psi_Y - \Psi_X K\|_F^2\) instead of the spectral residual \(J\). This directly tests whether the spectral residual is the source of improvement or simply the neural network expressivity.
- Add a quantitative metric to the turbulence experiment (e.g., correlation between the leading Koopman mode and the true pressure field, or reconstruction error on held-out snapshots).
- In the neural dynamics experiment, either (a) match the number of eigenfunctions across methods (e.g., truncate NN-ResDMD to 50 eigenfunctions to compare with Hankel-DMD), or (b) report a dimensionality-invariant clustering metric.
- Specify hidden layer sizes, learning rate, \(\sigma\) value, and convergence criteria for all experiments.

## Score and Decision

The paper proposes a genuinely novel and well-motivated approach — using the spectral residual as a training loss for learning Koopman dictionaries — and demonstrates it on diverse systems. The main contribution (using the ResDMD residual as a differentiable loss function for dictionary learning) is solid and clearly presented. However, the experimental validation has several gaps: the pendulum comparison does not isolate the effect of the spectral-residual loss from the neural network's expressivity, the turbulence evidence is purely qualitative, and the neural dynamics evaluation does not control for differing eigenfunction counts across methods. The theoretical framing is also slightly overclaimed. These are all addressable in revision and do not invalidate the core contribution, but they prevent a stronger endorsement.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>