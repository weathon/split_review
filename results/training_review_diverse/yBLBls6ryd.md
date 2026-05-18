Now I have a thorough understanding of the paper. Let me write the consolidated review.

## Summary

This paper proposes a Riemannian framework for learning spectral factorizations (eigendecompositions) of curvature matrices on the fly for fractional natural gradient descent (FNGD). By maintaining $\mathbf{S} = \mathbf{B}\,\mathrm{diag}(\mathbf{d})\,\mathbf{B}^\top$ directly via Riemannian gradient descent in specially constructed local coordinates, the method avoids expensive matrix decompositions when applying fractional powers — it simply performs elementwise operations on $\mathbf{d}$. The framework handles orthogonal constraints on $\mathbf{B}$, eigenvalue ordering ambiguities, and Kronecker structure via novel local-coordinate constructions that diagonalize or block-diagonalize the Fisher-Rao metric. Experiments on synthetic preconditioner estimation (Figures 2–3) validate that the spectral update matches the behavior of standard (non-spectral) schemes, and half-precision ViT training on ImageWoof (Figure 4) shows competitive performance against AdamW and Shampoo.

## Strengths

1. **Principled Riemannian derivation handling spectral constraints and redundancies.** The paper constructs local coordinates (Section 3.1–3.2) that explicitly handle the orthogonality constraint on $\mathbf{B}$, the positivity of $\mathbf{d}$, and the permutation ambiguity of eigendecomposition. Claims 4 and 5 show that the Fisher-Rao metric in these local coordinates is diagonal (full-matrix case) or block-diagonal (Kronecker case), enabling efficient closed-form inversion. This provides a rigorous foundation beyond ad-hoc updates.

2. **Enables cheap application of arbitrary fractional powers for non-diagonal preconditioners.** The spectral parametrization $\mathbf{S}^{-1/p} = \mathbf{B}\,\mathrm{diag}(\mathbf{d}^{-1/p})\,\mathbf{B}^\top$ reduces matrix fractional powers to elementwise operations on eigenvalues (Section 2). This directly addresses the limitation that prior non-diagonal methods (K-FAC, Shampoo) face expensive and numerically unstable matrix fraction computations. The empirical results in Figure 4 demonstrate that the method can flexibly use $p=1$ and $p=2$, with $p=1$ outperforming the standard square root ($p=2$) on vision transformers.

3. **Efficient Kronecker-structured updates.** The Kronecker-based scheme (Figure 1) avoids matrix decompositions and eigendecompositions entirely, enabling preconditioner updates every 10 iterations (versus every 100 for Shampoo) while matching AdamW's wall-clock time (Section 4). This efficiency is the key enabler for using the method in practice and is clearly demonstrated.

4. **Empirical validation of equivalence to default schemes.** The controlled synthetic experiments (Figures 2 and 3) show that the proposed spectral update scheme converges to the same fixed-point and matches the iterates of the default (non-spectral) update scheme for both full-matrix and Kronecker-structured cases. This validates that the spectral parameterization does not sacrifice fidelity of curvature estimation.

5. **Demonstrated effectiveness in half-precision NN training.** The method trains three vision transformer architectures (ViT, FocalNet, FlattenViT) on ImageWoof in half-precision and outperforms strong baselines (AdamW, Shampoo) as shown in Figure 4. This provides preliminary evidence that the method's design — avoiding unstable matrix decompositions — translates to practical low-precision viability.

## Weaknesses

### Fatal
None.

### Major
None. The paper's core algorithmic contribution is sound, the theoretical derivation is principled, and the synthetic validation is convincing. The weaknesses below are substantive but do not invalidate the paper's central claims.

### Minor

1. **Neural network experiments are limited in scope relative to the paper's framing.** The paper's title, abstract, and conclusion emphasize "training neural nets" broadly, but the only NN experiments use ImageWoof (a 10-class ImageNet subset) with three vision transformer variants (all in the same architectural family). While this is reasonable for a methods paper demonstrating a proof-of-concept, the claim that the method is "efficient and flexible for training neural nets" in a general sense would be strengthened by at least one additional setting — e.g., a CNN on a standard vision benchmark, or a small-scale language modeling task. The positive-definite matrix optimization experiment (d=60) is a useful sanity check but does not fill this gap. This is the most significant limitation of the empirical validation.

2. **The half-precision stability claim lacks direct systematic evidence.** The paper asserts stability in half-precision (abstract: "does not require matrix decompositions and, therefore, is stable in half precision"; Section 2.4), but provides no head-to-head comparison between half-precision and full-precision runs of the same method. Without such a comparison (or an analysis of eigenvalue drift, orthogonal-matrix drift, or error propagation from the truncated Cayley map), the claim is supported only by the plausible reasoning that the method avoids decompositions, not by direct measurement. The experiments do show the method works in half-precision, which is positive, but the specific "stable in half precision" claim would benefit from an ablation where the same method is also run in full precision to confirm there is no degradation.

3. **The demonstration of "arbitrary" fractional powers is narrow.** The ability to apply any fractional power is the paper's core selling point, but the only NN experiment varying $p$ (Figure 4, second plot) compares $p=1$ to $p=2$ on a single architecture (ViT) on ImageWoof. This shows the capability works, but does not constitute a "deep investigation into the role of fractional powers" (which the paper mentions as motivation). Showing at least one additional $p$ value (e.g., $p=4$ as in Chen et al., 2021, which the paper cites) across multiple tasks would substantially strengthen the case that the "arbitrary" capability matters in practice.

4. **The Shampoo comparison could be better isolated.** The paper compares its method (preconditioner updated every 10 iterations) against Shampoo (updated every 100 iterations) at matched wall-clock time. This is a valid system-level comparison — the method's efficiency IS the advantage — but it confounds algorithmic improvement with update frequency. An ablation that (a) compares both methods at the same update frequency (even if Shampoo is slower), and (b) compares the proposed method with and without grafting-style tricks, would help attribute performance differences to the core algorithmic innovation versus the engineering advantages of cheaper updates. The paper is transparent about the setup (Section 4), but the current comparison does not fully isolate which components drive the gains.

5. **The algorithm presentation in the main text is dense and relies heavily on deferred material.** While Figure 1 gives explicit update formulas and Section 3 provides derivations, the main text frequently defers to the appendix for even basic definitions (e.g., the full derivation of the Kronecker update, the truncated Cayley map details). A reader attempting to implement the method from the main text alone would struggle with nested dependencies in the notation and the lack of a self-contained algorithmic summary. This is not a fatal flaw — the formulas in Figure 1 are explicit — but it is a practical concern for a paper whose primary contribution is an algorithm.

### Trivial
- The paper would benefit from an explicit statement of per-iteration computational complexity (in terms of matrix dimensions and update frequency) to help readers compare against alternatives at a glance.
- Section 3 discusses handling repeated eigenvalues via Moore–Penrose inversion (which the paper does address), but a brief discussion of how close eigenvalues can be before numerical issues arise would be helpful.

## Nice-to-Haves
- **Computational complexity summary**: A clear table or equation summarizing the per-iteration cost in terms of Kronecker factor dimensions and update frequency would aid quick comparison with Shampoo, K-FAC, and AdamW.
- **Convergence analysis**: While not expected for a practical methods paper, a minimal analysis (e.g., showing that the fixed point of the spectral scheme matches the true covariance in expectation) would strengthen the theoretical grounding.
- **Visualization of learned eigenvalues**: Showing how the eigenvalues $\mathbf{d}$ evolve during training and whether they have interpretable structure (e.g., curvature directions) would increase the paper's appeal and connect to the broader optimization literature.

## Removed Points
These points from the reviews were considered but removed for the reasons stated:
- **"Notation is confusing (extra term in Kronecker update)."** Removed per rule: this is a PDF extraction/parser artifact, not an issue in the original submission.
- **"Does not compare to online eigendecomposition methods (Oja's rule, randomized SVD)."** Removed per rule: do not mention missing related works.
- **"Does not discuss whether eigenvalues have meaningful interpretations."** This is a nice-to-have suggestion, not a weakness, and was moved to Nice-to-Haves.
- **"Missing convergence analysis / convergence guarantees."** This is standard for practical optimizer papers and the scope is clear; moved to Nice-to-Haves.
- **"Handling of repeated eigenvalues is insufficiently discussed."** The paper does discuss this (lines 240–241), explicitly noting the Moore–Penrose inversion approach and addressing numerical stability for close entries.
- **"The Shampoo comparison is unfair."** Removed as the comparison at equal wall-clock time is standard and the paper transparently describes the setup. The useful part of this critique (isolating update frequency) is retained as a minor weakness above.
- **"Comparison to alternative eigendecomposition learning methods."** Removed per rule: do not mention missing related works.

## Novel Insights
None beyond the paper's own contributions. The key insight — using local coordinate transformations to diagonalize the Fisher-Rao metric for spectral parametrizations of positive-definite matrices — is well-executed but essentially contained in the paper's own presentation.

## Suggestions
1. **Expand NN evaluation to at least one additional setting** — a CNN (e.g., ResNet on CIFAR-10) or a small language modeling task with a transformer — to demonstrate that the method generalizes beyond ViT-style architectures on ImageWoof.
2. **Add a half-precision vs. full-precision ablation** for the proposed method on at least one experiment, to directly validate the "stable in half precision" claim.
3. **Include a comparison with matched update frequencies** (e.g., both methods updated every 10 iterations) even if Shampoo is slower, to isolate the effect of the algorithmic improvement from the efficiency advantage.
4. **Test at least one additional fractional power** (e.g., $p=4$) on a NN task to substantiate the claim that "arbitrary" fractional powers are practically useful.
5. **Provide a self-contained algorithmic pseudocode block** in the main text or appendix with all quantities defined locally, to improve reproducibility.

## Score and Decision

The paper proposes a clever and principled framework for learning spectral factorizations on the fly, with a thorough Riemannian derivation and convincing synthetic validation. The core idea — maintaining the eigendecomposition directly via local-coordinate RGD — is novel and addresses a real bottleneck in non-diagonal preconditioning (the cost and instability of matrix fractional powers). The half-precision NN experiments provide encouraging proof-of-concept results. However, the empirical support for the claimed practical benefits is limited: one dataset, one architectural family, narrow fractional-power exploration, and a stability claim that is plausible but not systematically validated. These are real but addressable weaknesses; the paper would be significantly strengthened by expanding the experimental scope and adding targeted ablations. On balance, the contribution is solid and worth publication, with the expectation that these gaps can be addressed in a camera-ready version.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>