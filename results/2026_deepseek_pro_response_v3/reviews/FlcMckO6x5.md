Now I have a clear picture. Let me finalize.

**Comparison summary:**
- **dpDw5U04SU (7.00, Accept)**: Pure theory, tight exact bounds on minimum width for universal approximation. More focused and rigorous than the current paper, which is broader but has an incomplete proof on its central algorithmic claim.
- **H8CtXin7mZ (5.25, Reject)**: Applied neural preconditioner for Poisson. The current paper has substantially more theoretical depth and a more elegant algorithm.
- **TNYLCF7vZA (4.75, Reject)**: The Shi et al. INR paper (baseline for current work). Current paper clearly stronger with more theory and algorithmic novelty.

The current paper sits between 5.25 and 7.00 — strong theory contributions + practical algorithm, but the abstract's "provably" claim overreaches the actual proof (hedging language in Section 4 reveals the gap). **Final score: 6.0, Decision: Accept.**

---

## Summary
This paper provides a three-part treatment of separable neural networks (SepNNs): (1) a unified universal approximation theorem for CP, TT, and Tucker SepNNs using a clean Stone-Weierstrass argument, (2) an NTK analysis revealing a double-asymptotic regime where both width and decomposition rank must diverge for a deterministic kernel, and (3) SepPGD, a separable preconditioned gradient descent method that achieves O(nD) preconditioner complexity for n^D grid samples via Kronecker-product decomposition. Experiments on KRR, INR-based image/surface representation, and PINNs demonstrate faster convergence over baselines.

## Strengths
- **Unified universal approximation theorem (Theorem 1)**: The Stone-Weierstrass proof strategy cleanly establishes that CP, TT, and Tucker SepNNs can approximate any continuous multivariate function on compact sets for arbitrary D ≥ 2. The proof explicitly verifies the three Stone-Weierstrass conditions (identity, point separation, algebraic closure), providing a substantially simpler and more general alternative to the orthogonal-basis construction in prior work (Cho et al., 2023), which only covered the bivariate CP case.
- **Novel double-asymptotic NTK characterization (Theorem 2 + Corollary 1)**: The paper identifies that SepNN NTK convergence depends on both network width W and decomposition rank R. Theorem 2 proves almost-sure convergence to a deterministic kernel when W,R → ∞, while Corollary 1 proves convergence in distribution to a stochastic kernel when only W → ∞ with fixed R. This is empirically validated in Figure 1(a-b), where NTK variance persists at fixed R=50 even as width grows — a practically relevant insight for SepNN training.
- **Efficient O(nD) preconditioning via Kronecker-product decomposition (Lemma 2, Table 1)**: The algorithmic insight — decomposing an n^D × n^D preconditioner into D factor preconditioners of size n × n using the identity (C^⊤ ⊗ A)vec(B) = vec(ABC) — genuinely reduces complexity. Lemma 2 formally proves equivalence to classical NTK-based PGD for D=2. Table 1 quantifies the complexity gap.
- **Consistent empirical improvements across diverse tasks (Figures 2-4)**: SepPGD achieves faster convergence than MLP, SepNN, and MSK-preconditioned variants across KRR, image representation (PSNR 26.48 → 33.30), 3D surface representation (IoU 0.983 → 0.992), and PINN PDE solving.

## Weaknesses

### Fatal
None.

### Major
- **Unsubstantiated "provably" claim in the abstract regarding NTK spectrum adjustment**: The abstract states SepPGD "provably adjust[s] its NTK spectrum," but the paper does not complete this proof. Section 4 (lines 196-202) reveals the gap: the argument that K S̃ has improved spectrum relies on (i) S̃ having better spectrum than the factor-NTK proxy K̃, (ii) K̃ ≈ K via Lemma 3 (referenced but never stated in the main text), and (iii) the product K S̃ inheriting improved eigenvalues. The paper's own hedging — "This can possibly be verified," "Suppose that," "It is believed that… can be readily extended" — acknowledges the incompleteness. The eigenvector non-alignment issue (eigenvalues of K S̃ are not products of individual eigenvalues when K and S̃ lack simultaneous diagonalization) is not addressed. Lemma 2 (equivalence to classical PGD) and the empirical results remain valid, but "provably" should be downgraded to "motivated by spectral considerations."

### Minor
- **No direct measurement of spectral bias alleviation**: The paper claims SepPGD works by alleviating spectral bias, but experiments only show faster convergence — there are no eigenvalue/condition-number measurements during training, no spectral decomposition of residuals tracking which NTK eigenmodes are being accelerated, and no ablation isolating the spectral mechanism from other effects.
- **NTK and SepPGD analysis restricted to CP SepNNs, with Lemma 2 proved only for D=2**: The approximation theory (Theorem 1) covers CP, TT, and Tucker SepNNs for general D ≥ 2, but the NTK analysis (Section 3) and SepPGD (Section 4) are developed only for CP SepNNs. Lemma 2, the strongest theoretical result for SepPGD (equivalence to classical PGD), is proved for D=2 with multivariate extension described as "readily extended" without elaboration. The paper is transparent about these limitations (footnote 1, lines 118, 201), but the gap between broad framing and narrower technical depth is noticeable.

### Trivial
None.

## Nice-to-Haves
- Extend Lemma 2 beyond D=2 using the general Kronecker sum structure to make SepPGD genuinely multivariate with formal guarantees.
- Add an ablation on preconditioner update frequency and SepNN rank R to characterize SepPGD's sensitivity to these hyperparameters.
- Test the non-grid input formulation experimentally to validate that SepPGD extends beyond grid-structured data.

## Removed Points
*These points are flagged to be removed, treat them with caution.*

- **HC: "The mini-batch PGD method of Shi et al. (2025) is never included in any experimental comparison"** — REMOVED. The MSK baseline from Geifman et al. (2024) / Shi et al. (2025) IS included in all experiments (Fig. 2, labeled "MSK"; line 221 explicitly cites both references as the MSK source).
- **HC: "The convergence improvements could in principle arise from other effects (e.g., factor-wise gradient rescaling acting as an adaptive learning rate)"** — REMOVED as a standalone criticism. This is speculative without a concrete paper-specific anchor. The concern about mechanism-isolation is already captured in the "no direct spectral bias measurement" weakness.
- **HC: "The paper's central practical contribution rests on a theoretical justification that the paper does not actually complete"** — PARTIALLY RETAINED. The spectral proof gap is real (Major weakness). But the claim that this undermines the entire practical contribution is excessive: Lemma 2 provides rigorous equivalence, efficiency gains are structural (Kronecker decomposition), and empirical results would stand without the spectral argument.
- **SF: "Generalization from grid to non-grid inputs discussed and tested"** — REMOVED as a standalone strength. The non-grid formulation is one paragraph at the end of Section 4 with experiments only in appendix; too minor as a paper-level strength.

## Novel Insights
The double-asymptotic NTK analysis (Theorem 2 vs. Corollary 1) reveals a novel insight for separable architectures: NTK determinism requires both width and decomposition rank to diverge, unlike standard MLPs where width alone suffices. This explains why finite-rank SepNNs retain stochastic training behavior even at large width, and suggests rank scaling is as important as width scaling for predictable SepNN training dynamics. This insight has no clear antecedent in prior SepNN or NTK literature.

## Suggestions
- Modify the abstract and introduction to replace "provably adjusts its NTK spectrum" with language accurately reflecting what is proved (equivalence to classical PGD with a Kronecker-structured preconditioner) and what is motivated (spectral improvement). The hedging from Section 4 should inform the abstract's framing.
- Add a simple experiment tracking the condition number of the (approximate) NTK matrix during training with and without SepPGD, to directly validate the spectral bias alleviation mechanism rather than relying solely on convergence curves.
- State Lemma 3 in the main text of Section 4, since it is the bridge between the factor-NTK proxy K̃ and the true NTK K in the spectral argument.

## Calibration Anchors Referenced
- **TNYLCF7vZA** (Shi et al. IGA, avg 4.75, Round 1): The closest baseline paper. Current paper has substantially more theory and a more novel algorithm. Clearly stronger.
- **2C3CWCPxNS** (PINN preconditioning, avg 5.00, Round 1): Applied preconditioning paper. Current paper has broader theoretical contributions. Stronger.
- **H8CtXin7mZ** (Neural Poisson preconditioner, avg 5.25, Round 2): Applied neural preconditioner with less theoretical depth. Current paper is stronger.
- **FK8tl47xpP** (Greedy L2O, avg 6.25, Round 2): Learning-to-optimize with convergence guarantees. Has tighter theoretical guarantees than current paper, but narrower scope. Current paper slightly below.
- **dpDw5U04SU** (Minimum width for universal approx, avg 7.00, Round 2): Focused pure theory paper with exact tight bounds. More rigorous than current paper. Current paper is broader but less theoretically tight.

**Round 1 bracket: 5.5–7.5. Round 2 narrowed to 5.25–7.0, with the paper sitting clearly above 5.25 and below 7.00. Final score: 6.0.**

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>