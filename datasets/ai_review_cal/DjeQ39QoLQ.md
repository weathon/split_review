- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 8, 6, 6
Now I have thoroughly verified all claims against the paper. Here is my consolidated review.

---

## Summary

This paper proposes a "perturb-then-diagonalize" (PTD) method for initializing diagonal state-space models (S4-PTD, S5-PTD). It provides a rigorous theoretical analysis showing that while S4D/S5 outputs converge pointwise to the HiPPO (S4) system for smooth inputs, the convergence is non-uniform in the operator norm, creating persistent spikes in the transfer function that make diagonal SSMs brittle to certain Fourier-mode perturbations. The paper then uses pseudospectral theory to regularize the ill-conditioned HiPPO diagonalization: perturb the matrix by a small E, diagonalize the perturbed matrix, and use its eigenvectors/values as initialization. Experiments show modest improvements on LRA (S4-PTD 86.58% vs S4D 84.89%; S5-PTD 87.61% vs S5 87.46%) and targeted robustness gains on Fourier-corrupted sCIFAR.

## Strengths

- **Rigorous theoretical identification of a fundamental failure mode in diagonal SSMs.** Section 3 (Lemma 1, Theorems 1–2) proves that S4D/S5 transfer functions have persistent non-vanishing spikes, providing the first formal explanation of why discarding the low-rank part of HiPPO makes diagonal models brittle to Fourier-mode perturbations. The rate of weak* convergence (Theorem 1) is a genuine addition over prior work (Gu et al., 2022).

- **Demonstrated robustness improvement on both synthetic and real data.** The synthetic sinusoid regression experiment (Figure 2) shows S4D suffering an "extrapolation disaster" while S4-PTD avoids it. The sCIFAR experiment (Figure 3a–b) shows S4-PTD maintaining high accuracy on a test set with worst-case Fourier-mode noise where S4D collapses. These directly support the paper's central robustness claim.

- **Improved LRA accuracy over the direct diagonal models.** Table 1 reports S4-PTD averaging 86.58% (vs S4D's 84.89%, a +1.69% gain), and S5-PTD achieving 87.61% (vs S5's 87.46%). The S4-PTD improvement on Path-X (96.39 vs 91.95) is particularly notable and suggests PTD helps on the longest-range tasks.

- **Theoretically grounded perturbation bound with mild dimension dependence.** Theorem 3 provides a uniform bound on the transfer-function error that is linear in the perturbation size and grows only logarithmically with n, giving practitioners a clear guarantee that the PTD initialization stays close to the robust HiPPO system.

- **Ablation study confirming the predicted trade-off.** Section 5.3 (Figure 3c) shows the eigenvector condition number scaling as 1/ε (matching Theorem 5's prediction) and identifies the optimal perturbation size range (‖E‖/‖A_H‖ between 10⁻² and 1).

## Weaknesses

### Fatal
None.

### Major

- **Insufficient specification of the PTD optimization algorithm.** The paper states the objective (Eq. 4: minimize κ(Ṽ_H) + γ‖E‖ s.t. A_H+E = Ṽ_H Λ̃ Ṽ_H⁻¹) and says "We implement a solver using gradient descent" (line 383). This is the core algorithmic contribution, yet the paper provides no details on: how κ(Ṽ_H) is handled in optimization (κ is non-differentiable at repeated eigenvalues; the standard approach is either automatic differentiation through the eigendecomposition when eigenvalues are distinct, or a smooth surrogate), the parameterization of E (dense? sparse? structured?), its initialization, step-size/tuning of the optimizer, convergence criteria, or the computational cost of this pre-processing step. While an expert practitioner could plausibly fill in these gaps (e.g., using PyTorch's autograd through torch.linalg.eig), the omission hinders direct reproducibility and independent verification of the claimed improvements. The method as presented in the main paper is incomplete.

### Minor

- **Robustness evaluation is narrow.** The paper's robustness evidence consists of: (1) a synthetic sinusoid task, and (2) an sCIFAR experiment with 10% sinusoidal noise at frequencies matching the spikes of |G_Diag|. Both are worst-case adversarial tests designed to exploit the specific weakness identified in the theory. The paper candidly acknowledges this ("the noises in this experiment are the 'worst-case' noises and intentionally made to fail the S4D model," line 443). The claim of "resilience to Fourier-mode noise-perturbed inputs" is supported by these targeted experiments, but the practical significance would be strengthened by evaluating on standard corruptions (e.g., Gaussian noise, missing data) or by showing that the robustness translates to better performance on naturally noisy LRA subsets.

- **Missing comparison with a random perturbation baseline.** The paper's theoretical discussion (Theorem 4) establishes that a random Ginibre perturbation already provides statistical guarantees on the eigenvector condition number. The ablation study varies the perturbation size but always uses the optimized E from Eq. 4. Without comparing against a simple random perturbation of equivalent norm, the reader cannot assess whether the optimization is necessary or whether a cheaper alternative (e.g., sample a Gaussian matrix, scale to a target norm, add, then diagonalize) would already achieve most of the benefit.

- **S4 comparison is cross-architecture.** The paper states S4-PTD "outperforms the S4 model" (line 405). While this is true in aggregate (86.58% vs 86.09%), the comparison crosses architectures: S4 uses DPLR, while S4-PTD uses a diagonal architecture with PTD initialization. The gains could partly arise from the architectural improvements in S4D/S5 (parallel scans, MIMO) rather than the PTD initialization alone. The fair and controlled comparison is S4-PTD vs S4D (+1.69%), which is positive. The S4 comparison should be presented with this caveat more prominently.

### Trivial
None.

## Nice-to-Haves

- A pseudocode block for the PTD optimization algorithm would significantly improve usability.
- Analysis of the computational cost (time, memory) of the PTD pre-processing step for varying n.
- Evaluation on one additional initialization beyond HiPPO (as claimed in "flexible framework") would substantiate the generality claim.
- Variance or multi-seed reporting for LRA results would improve statistical rigor.

## Removed Points

The following points from the original reviews were removed after verification:

- **Criticism about the Dirac delta not being in L²** (Section 3.2). The paper mentions the Dirac delta only as intuitive motivation (line 205); the rigorous Theorem 2 uses functions in L¹ ∩ L². The paper does not rely on the Dirac delta formally.
- **"No statistical significance or variance reporting for LRA results."** LRA reporting conventions in this literature commonly use single runs; demanding confidence intervals is a methodological preference, not a verified flaw.
- **Criticism that the PTD optimization is a "fatal/structural" flaw.** The optimization objective (Eq. 4) is clearly stated, the constraint is simply that A_H+E is diagonalizable (true for almost all perturbations), and the optimization can be implemented via standard autodiff through eigendecomposition. The specification is sparse but not empty; this is a Major weakness, not Fatal.
- **"No discussion of the cost of PTD preprocessing"** — moved to Nice-to-Haves.
- **Accusation that the paper's claim about S4 outperformance is misleading.** The paper's primary comparison is S4-PTD vs S4D (same architecture); the S4 comparison is secondary and factually correct (S4-PTD > S4 on all six tasks). The caveat about differing architectures is a Minor point, not a "selective comparison" critique.
- **"Some typos: In Lemma 1, the expression includes..."** — parser artifact, not an author error.
- **Strength Finder's generic strength about "addressing an important problem"** — not specific enough; omitted.
- **Strength Finder's claim that PTD provides "flexible framework applicable beyond HiPPO"** — the paper states this but does not test it; kept in Strengths as stated but noted as untested.

## Novel Insights

None beyond the paper's own contributions. The harsh critic's observations about the non-differentiability of the condition number and the need for a smooth surrogate are technically accurate but represent standard practice in optimization through eigendecompositions, not a novel discovery about the paper.

## Suggestions

1. **Specify the PTD optimization in full.** Provide: the parameterization of E (dense matrix of size n×n), the initialization scheme (zeros? small random?), differentiation method (autograd through torch.linalg.eig or a smooth surrogate for κ), step-size schedule, convergence criterion, and approximate wall-clock cost. A pseudocode listing would be ideal and would transform the method from a statement of intent into a reproducible contribution.

2. **Add a random-perturbation baseline.** Compare S4-PTD against S4 initialized by adding a random Gaussian (Ginibre) perturbation of the same norm to A_H, then diagonalizing. This would isolate the benefit of the optimization and clarify whether the real value is in the perturbation itself or in the optimized choice of E.

3. **Broader robustness evaluation.** Add one or two standard perturbation types (e.g., additive Gaussian noise at varying SNR, temporal masking) on the sCIFAR task. Even a small-scale experiment would connect the targeted Fourier-mode robustness to more general notions of robustness.

4. **Caveat the S4 comparison.** When stating that S4-PTD outperforms S4, note explicitly that the architectures differ and that the controlled comparison is S4-PTD vs S4D.
