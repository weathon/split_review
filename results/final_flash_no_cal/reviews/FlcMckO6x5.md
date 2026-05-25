Now I have a thorough understanding of the paper. Let me compose the final consolidated review.

## Summary

This paper studies separable neural networks (SepNNs) and makes three contributions: (1) a universal approximation theorem for CP, TT, and Tucker SepNNs (Theorem 1), extending prior bivariate results to arbitrary dimension and multiple tensor formats; (2) an NTK analysis characterizing deterministic and random kernel regimes for SepNNs (Lemma 1, Theorem 2, Corollary 1); and (3) a separable preconditioned gradient descent method (SepPGD) to alleviate spectral bias during SepNN training.

## Strengths

**1. First universal approximation theorem for multivariate SepNNs across multiple tensor formats.** Theorem 1 proves that CP, TT, and Tucker SepNNs can approximate any continuous multivariate function on compact sets. The proof combines the Stone-Weierstrass theorem with vector-valued universal approximation and is clearly sketched. This meaningfully extends prior work (Cho et al., 2023) that only covered the bivariate case, and provides a unified treatment across CP, TT, and Tucker architectures.

**2. Comprehensive NTK analysis with identification of two asymptotic regimes.** Lemma 1 derives the exact NTK expression for CP SepNNs; Theorem 2 proves convergence to a deterministic kernel when both width and rank go to infinity; Corollary 1 proves convergence to a random kernel under infinite width but fixed rank. This is the first NTK characterization for SepNNs and is empirically validated (Figure 1). The analysis also notes that the SepNN NTK on grid inputs admits Kronecker-product structure (Appendix A.3), enabling efficient computation.

**3. Broad empirical validation across diverse tasks.** Experiments span kernel ridge regression, image representation (INRs), 3D surface representation, and PINNs for PDEs (Figures 2–4). SepPGD consistently accelerates convergence in wall-clock time compared to baselines, with visual quality gains (e.g., PSNR 33.30 vs 26.48 for image representation; IoU 0.992 vs 0.983 for surface reconstruction). This breadth strengthens the practical relevance of the proposed method.

**4. Clean theoretical connection between SepPGD and NTK-based PGD for the bivariate case.** Lemma 2 proves equivalence between SepPGD and the classical Kronecker-structured preconditioner (Geifman et al., 2024) for D=2, grounding the algorithm in established preconditioning theory.

## Weaknesses

### Fatal
None.

### Major

**1. The claimed O(nD) per-iteration complexity for SepPGD (and for SepNN training on a grid) is not adequately justified and appears inconsistent with the described operations.** 

The paper repeatedly states that SepPGD scales as O(nD) for n^D training samples (Abstract, Table 1, Remark 4). However, the construction of the mode-d preconditioner M_d in equation (8) involves: (i) a Khatri-Rao product producing an R × n^{D-1} matrix; (ii) computing Σ_{d=1}^D (ℛ ×_d S_d) which requires D tensor-matrix products on an n^D tensor, each costing O(n^{D+1}); and (iii) a matrix product between the Khatri-Rao matrix and the unfolded result. The paper's own Footnote 3 acknowledges O(n^{D-1}) for "the matrix product in (8)," which is already exponential in D and contradicts the O(nD) entry in Table 1. The tensor-matrix products (R ×_d S_d) are not accounted for in this complexity claim at all.

Similarly, the claim that standard SepNN training costs O(nD) per epoch (Section 1) — comparing to O(n^D) for a conventional NN — counts only the factor network forward passes (nD queries) but omits the combination cost for producing all n^D function values needed for the MSE loss, which is O(R n^D) for arbitrary labels. While SepNNs are indeed more efficient than dense MLPs on grids, the magnitude of the advantage is not correctly characterized.

**Why this matters:** The efficiency advantage of SepPGD over prior NTK-based preconditioning methods is the paper's central algorithmic selling point. If the complexity analysis is incomplete or overstated, the reader cannot properly assess the algorithm's computational profile. The theoretical contributions (approximation theorem, NTK analysis) are unaffected, but the algorithmic contribution is presented with an unsupported efficiency claim.

**2. The theoretical justification for SepPGD is established only for D=2; the extension to D>2 is not provided.**

Lemma 2 proves that SepPGD is equivalent to classical Kronecker-structured NTK-based PGD for the bivariate case. For D>2, the paper states only that "it is believed that the result in Lemma 2 (and the analysis following) can be readily extended to multivariate cases D > 2" (Section 4). No explicit formula for the multivariate preconditioner is given, and the belief is not substantiated with a proof or even a sketch. Since the algorithm and its complexity claims apply to general D (and the experiments include D=3 for PINNs), the missing theoretical foundation for D>2 is a significant gap.

### Minor

**1. The preconditioner construction cost is not reported separately in the experiments.** The wall-clock convergence curves in Figures 2–4 include the preconditioner construction time (NTK computation + eigendecomposition of n×n factor matrices) in the total time, but do not isolate this overhead. For practical applications, the one-time cost of building the preconditioners matters for assessing when SepPGD becomes beneficial over standard GD.

**2. The "sum-of-logits" method for constructing the pseudo NTK matrix K_Θ_d for multi-output factor networks is not explained.** The paper references (Mohamadi et al., 2023) but does not clarify how an R-output factor network is reduced to a scalar n×n kernel, or under what approximation this provides a valid preconditioner. This makes the algorithm harder to reproduce independently.

**3. Non-grid experiments are mentioned but not shown.** The paper states in Section A.2 that SepPGD extends to non-grid inputs and that this formulation is used for testing, but no non-grid experimental results are presented in the main paper.

**4. Iteration-based convergence curves are not provided alongside time curves.** Since the complexity analysis is in question, showing convergence in iterations (independent of per-iteration cost) would help separate the preconditioning benefit from any implementation optimization. Only wall-clock time is reported.

### Trivial

- The paper says M_d ∈ ℝ^{R×n} in (8) but Remark 4 refers to "n-by-n preconditioning matrices {M_d}." This is an imprecision, though not consequential for the algorithm's operation.
- The notation "⊕" is used both for concatenation (Definition 1) and for summation (Σ variation of S_d), which could be clarified.

## Nice-to-Haves

- An ablation study showing the effect of the preconditioner on the NTK matrix spectrum (e.g., eigenvalue distribution before and after applying S_d), which would directly demonstrate how SepPGD alleviates spectral bias.
- Separate reporting of preconditioner construction time vs. per-iteration time in the experimental evaluation.
- An explicit construction or proof-sketch for the D>2 generalization of Lemma 2.

## Removed Points

These points were flagged by the reviewers but are removed from the main assessment for the following reasons:

- **"The algebra must contain the constant function 1, not the identity function" (Harsh Critic, Stone-Weierstrass condition).** This is a misunderstanding of standard terminology: in function algebras the multiplicative identity (constant 1) is routinely called the "identity function" or "identity element." The paper's usage is correct.
- **"The paper does not distinguish between theoretical contributions and the algorithmic one in its conclusions" (Harsh Critic).** This is an organizational suggestion rather than a scientific weakness. The paper clearly enumerates three contributions; the issue is that one of them (SepPGD) has an unsupported complexity claim, which is already captured above.
- **"The small imprecision (the algebra must contain the constant function 1, not the identity function) is not consequential" (Harsh Critic).** As noted, this is not actually an imprecision, and the reviewer agreed it is inconsequential.
- **Strength Finder claim about "dramatically lower complexity."** The strength itself (Lemma 2 connection, empirical benefits) is retained, but the "dramatically lower complexity" framing inherits the same complexity-analysis issue identified above; this caveat is noted in the assessment.
- **Strength Finder claim about "efficient NTK matrix computation for SepNNs."** This is a supporting operational detail (Kronecker structure of the NTK on grids) rather than a core strength. It is noted in the NTK analysis strength.

## Novel Insights

The most interesting insight emerging from this review is the tension between the paper's two distinct contributions: the theoretical NTK and approximation analyses are clean and self-contained, while the algorithmic contribution (SepPGD) rides on a complexity claim that has not been carefully vetted even in the paper's own accounting. A productive path forward would be to treat SepPGD as a *heuristic* for D>2 that empirically works well (as the experiments suggest) and to separate the complexity analysis from the convergence analysis — the per-iteration cost and the iteration-count benefit are distinct claims that should be evaluated independently. The Kronecker-product equivalence for D=2 (Lemma 2) is a genuinely valuable theoretical anchor, and a similar construction for D>2 using Tucker/TT algebra would strengthen the paper considerably.

## Suggestions

1. **Provide an honest, step-by-step complexity accounting for both standard SepNN training and SepPGD.** Distinguish between: (a) cost of factor-network forward/backward passes; (b) cost of assembling the full n^D output tensor (if needed for the loss); (c) cost of computing M_d (Khatri-Rao product, tensor-matrix products, matrix multiplication); and (d) cost of applying the preconditioner gradient. Be explicit about which terms dominate and under what regimes (e.g., n vs. D scaling). If the O(nD) claim is meant only for a narrow sub-operation, state this clearly and qualify the table entry accordingly.

2. **Either prove the generalization of Lemma 2 to D>2 or characterize SepPGD for D>2 as a heuristic with empirical support.** If a proof is not immediately available, provide a plausibility argument (e.g., using Tucker/TT tensor algebra to express the preconditioner) and clearly label it as an open theoretical question.

3. **Report the preconditioner construction time separately** (NTK computation + eigendecomposition for the n×n factor matrices) in the experiments, so readers can assess the amortization break-even point.

4. **Include iteration-based convergence curves** alongside wall-clock time to separate iteration-count benefit from per-iteration cost reduction.

5. **Clarify the "sum-of-logits" construction** for the factor pseudo-NTK matrices, specifying how the multi-output (R-dimensional) factor network is reduced to a scalar kernel.

## Score and Decision

The paper makes solid theoretical contributions — the universal approximation theorem and the NTK analysis are novel, well-argued, and extend the understanding of separable architectures. The SepPGD algorithm also demonstrates clear empirical benefits. However, the central efficiency claim (O(nD) complexity) is not properly justified, and the theoretical grounding of the algorithm for D>2 is incomplete. Because the paper prominently markets algorithmic efficiency as a core contribution, this is a significant weakness that needs to be addressed before the paper can be accepted in its current form.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>