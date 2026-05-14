Now I have all the information I need. Let me synthesize the final review.

---

## Summary

This paper makes three contributions to the theoretical understanding of separable neural networks (SepNNs): (1) a universal approximation theorem showing that CP, TT, and Tucker SepNNs with non-polynomial activations can approximate any continuous multivariate function on a compact set, unifying previous bivariate-only results; (2) characterization of SepNN NTK regimes (deterministic kernel under joint infinite width+rank, random kernel under infinite width+fixed rank), with rigorous convergence proofs; and (3) a separable preconditioned gradient descent method (SepPGD) that leverages the Kronecker structure of SepNN NTK on grid data to reduce per-iteration complexity from O(n^D) to O(nD), while empirically mitigating spectral bias. Experiments on kernel ridge regression, image/surface INRs, and PINNs demonstrate practical speedups.

## Strengths

1. **Universal approximation theorem for multivariate SepNNs (Theorem 1).** The proof uses a Stone-Weierstrass argument that cleanly unifies CP, TT, and Tucker forms. This is the first such result for general multivariate SepNNs and extends prior work (Cho et al., 2023) beyond the bivariate case. The proof is detailed in Appendix A.5.

2. **Rigorous NTK regime analysis (Theorem 2, Corollary 1, Theorem 3).** The paper derives the NTK of CP SepNN (Lemma 1) and proves convergence to a deterministic kernel under joint infinite width+rank, and to a random GP kernel under infinite width+fixed rank. The analysis of NTK stability during training (Theorem 3) is technically nontrivial and extends classic NTK theory to the separable architecture. The empirical validation in Figure 1 confirms the theoretical predictions.

3. **Efficient separable preconditioned gradient descent (SepPGD).** The method exploits the Kronecker-product structure of SepNN NTK on grids to reduce preconditioner application from O(n^D) to O(nD). Lemma 2 proves equivalence to classical NTK-based PGD (Geifman et al., 2024) under a Kronecker-structured preconditioner in the bivariate case. The complexity advantage over Hessian-based, MSK, and mini-batch methods is clearly quantified in Table 1.

4. **Comprehensive experimental validation across diverse tasks.** SepPGD shows consistent convergence improvements over SepNN and MLP baselines in KRR (Figure 2a), image representation (Figures 2b, 3, 6–9), surface representation (Figure 3), and PINNs (Figures 4, 13, 14). The results are measured in wall-clock time (not iterations) and include ablations on modulation function, rank, width, preconditioner update frequency, and noise robustness (Appendix Tables 2–7).

## Weaknesses

### Fatal
None.

### Major

1. **The claim that SepPGD "provably" adjusts the NTK spectrum is not fully substantiated.** The reasoning chain (lines 804–812) goes: (a) SepPGD is equivalent to classical NTK-based PGD with a Kronecker-sum preconditioner **S̃** = **S₁**⊗**Iₙ** + **Iₙ**⊗**S₂** (Lemma 2, bivariate case). (b) **S̃** improves the conditioning of the approximate NTK **K̃** = **K₁**⊗**Iₙ** + **Iₙ**⊗**K₂** because each **S_d** improves upon **K_d**. (c) "Suppose that **K̃** is close to the true NTK matrix **K**" — then **KS̃** would have better spectrum than **K**. The gap is that step (c) is asserted without a quantitative bound on ∥**K** − **K̃**∥/∥**K**∥. The pseudo-NTK approximation (10) provides an O(1/√W) error bound, but this is for a different approximation (the pseudo-NTK replacing exact factor NTK matrices), not the gap between **K̃** (which uses the Kronecker-sum structure) and the true SepNN NTK (which Lemma 3 shows is a sum of Kronecker products with cross terms). A quantitative bound or a formal statement of the regime where **K̃** ≈ **K** would be needed to fully justify the "provably" language. The empirical results strongly suggest SepPGD works, but the theoretical support for the spectrum-adjustment claim is conditional on an unverified approximation.

2. **Extension of Lemma 2 (equivalence to classical PGD) to multivariate D > 2 is not provided.** The paper states (line 815) "it is believed that the result … can be readily extended to multivariate cases." However, the multivariate NTK (Lemma 3 shows even the bivariate case is a sum of Kronecker products with cross terms) becomes substantially more complex. Since SepPGD is presented as a general D-dimensional method, proving the equivalence for D > 2 is important for the theoretical foundation. This is not merely an incremental extension.

### Minor

3. **Comparison with MSK on the primary grid-based INR/PINN tasks is missing.** While MSK is compared in the KRR toy experiment (Figure 2a) and the non-grid experiment (Appendix Table 9), the main image representation and surface representation experiments only compare SepPGD against plain SepNN and plain MLP. The authors explain (Appendix lines 4610–4621) that MSK runs out of memory for full-batch settings on their platform. This is a hardware limitation rather than a methodological flaw, and the complexity analysis (Table 1) provides a clear theoretical efficiency argument. Still, some head-to-head comparison on at least one small-scale grid task (where MSK would fit in memory) would strengthen the empirical case.

4. **The O(nD) complexity claim primarily covers preconditioner application, while preconditioner construction involves O(R n^{D−1}) operations.** The paper acknowledges this in Footnote 3 (line 780–784) and argues that the matrix product in (8) is "orders of magnitude less expensive in practice" than the NTK computation and EVD. While this pragmatic argument is reasonable, a cleaner asymptotic accounting breaking down every sub-computation (factor network forward, outer product construction, matrix multiply, unfold) with its exponent in n would better support the central efficiency claim.

5. **The spectral bias mitigation argument relies on the Kronecker-sum structure, which Lemma 3 shows is only approximate.** The exact SepNN NTK (Lemma 3) is a double-sum of Kronecker products with cross terms (over factor output indices r, s). The method's pseudo-NTK approximation (10) drops the cross terms (r ≠ s) and uses sum-of-logits approximations. While the O(1/√W) error bound for the pseudo-NTK is mentioned, the paper does not empirically verify how well the preconditioner built from this approximation actually flattens the eigenvalue spectrum of the true **K** (rather than **K̃**). A spectral plot of **K** vs. **KS̃** on a small problem would provide direct visual evidence.

### Trivial
None beyond typical formatting artifacts from PDF extraction.

## Nice-to-Haves
- Extend Lemma 2 to the general multivariate case with a full proof.
- Provide a quantitative bound on ∥**K** − **K̃**∥/∥**K**∥ in terms of width and rank, even a rough asymptotic one (e.g., O(1/√W) + O(1/√R)).
- Plot the eigenvalue spectrum of the true NTK matrix **K** vs. the preconditioned **KS̃** for a small grid problem.
- Include MSK comparison on at least one small-scale grid task where memory permits.

## Removed Points
These points are flagged to be removed; treat them with caution.

- *"The experimental evaluation does not compare SepPGD to existing NTK-based preconditioning methods on the core grid-based tasks"* — Retained and weakened to Minor (point 3). The authors explain the memory constraint (Appendix lines 4610–4621), and the theoretical efficiency advantage is clearly established in Table 1, so this is not a fatal omission.
- *"Missing appendix, missing proofs in appendix"* — Parser artifact; proofs are present in Appendix Sections A.5–A.11.
- *"The proof sketch is clear... one minor concern: the construction for the Tucker case requires that the core tensor C also be learned"* — This is not a weakness; Theorem 1 explicitly includes C as a learnable parameter, consistent with standard Tucker decomposition.
- *"Variance bands (e.g., shaded regions) would strengthen it"* — Minor presentational suggestion, not a substantive weakness.
- *"Vary the width and rank in the experiment to test how the pseudo-NTK approximation error affects SepPGD"* — Already present in Appendix Tables 3 and 6 (rank and width sensitivity analyses).
- *"A systematic study (e.g., PSNR vs. width/rank with and without SepPGD)"* — Already present in Appendix Tables 3, 6.

## Novel Insights
None beyond the paper's own contributions. The reviews do not surface a perspective that the paper itself does not articulate.

## Suggestions
1. **Tone down the "provably" language** in the abstract and Section 4, replacing it with more precise phrasing such as "can provably adjust the spectrum of the approximate Kronecker-sum NTK, which is shown to be close to the true NTK under increasing width (O(1/√W) pseudo-NTK error)." Alternatively, provide the missing quantitative bound.
2. **Prove Lemma 2 for D > 2** in the next revision, or at minimum provide the multivariate extension in the appendix with a clear statement of any additional assumptions required.
3. **Add a small-scale grid experiment** where MSK fits in memory and compare SepPGD, MSK, and plain SepNN on the same architecture for image INR, even if on a tiny image (e.g., 32×32).
4. **Add a spectral plot** (eigenvalues of **K** vs. **KS̃**) for a small (e.g., n=16) 2D grid to visually confirm that SepPGD flattens the true NTK spectrum.

## Score and Decision

**Calibration anchors (all from the ICLR 2026 human review corpus):**

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `/home/wg25r/review_agent/human_reviews_2026/CXlsqTAf1E.md` | 5.0 | Studies PGD and spectral bias with similar scope; this paper has more theoretical depth (three theorems vs. one) and broader experiments, but the theory in CXlsqTAf1E is cleaner. Comparable quality; this paper is slightly stronger in scope. |
| `/home/wg25r/review_agent/human_reviews_2026/X63V2CWjj3.md` | 6.5 | A tight, well-written theory paper with clear experimental validation. Our paper is comparably rigorous in its NTK analysis but has a wider scope (approximation theory + NTK + optimization), which dilutes focus. Slightly weaker overall. |
| `/home/wg25r/review_agent/human_reviews_2026/B4zcoLvjw0.md` | 6.0 | A focused theoretical paper with one clean result. Our paper has more results but also more gaps in the SepPGD justification. Comparable. |
| `/home/wg25r/review_agent/human_reviews_2026/8ZQ0HjBOEc.md` | 4.0 | NTK depth analysis criticized for lack of novelty and incomplete comparisons. Our paper has stronger novelty (first universal approximation for multivariate SepNNs, first NTK analysis for SepNNs) and is more thoroughly validated. |
| `/home/wg25r/review_agent/human_reviews_2026/P2m7gvtfrE.md` | 4.5 | Preconditioning + feature learning paper criticized as "unsurprising." Our paper's contributions are more novel. |
| `/home/wg25r/review_agent/human_reviews_2026/Vq9vhod9fL.md` | 3.5 | Contrastive learning theory with strong assumptions and limited experiments. Our experiments are more comprehensive. |
| `/home/wg25r/review_agent/human_reviews_2026/YzjS4jcfmS.md` | 5.0 | Muon/spectral optimizer study. Comparable strength. |

The paper makes three distinct theoretical contributions backed by full proofs in the appendix, and the proposed SepPGD method is practically useful with consistent gains across multiple tasks. The main weaknesses are (a) the "provably" claim about NTK spectrum adjustment is not fully quantified, and (b) the multivariate extension of Lemma 2 is deferred. These are addressable but non-trivial gaps. The overall contribution is solid: first universal approximation theorem for multivariate SepNNs, first NTK analysis for this architecture class, and an efficient, empirically effective preconditioning method. This is a clear accept at a mid-range poster level.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>