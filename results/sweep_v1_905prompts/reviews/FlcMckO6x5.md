Now I have all the information needed. Let me compose the final review.

## Summary

This paper provides three contributions to separable neural networks (SepNNs): (1) a universal approximation theorem for CP, TT, and Tucker SepNNs covering multivariate functions with D ≥ 2; (2) a neural tangent kernel (NTK) analysis characterizing two asymptotic regimes (deterministic under infinite width+rank, random under infinite width+fixed rank); and (3) a separable preconditioned gradient descent method (SepPGD) with O(nD) per-iteration complexity that provably adjusts the NTK eigenvalue distribution for D=2 and is conjectured to do so for D>2. Experiments on kernel ridge regression, INR-based image/surface representation, and PINNs demonstrate practical speedups.

## Strengths

- **First universal approximation theorem for multivariate SepNNs (CP, TT, Tucker) across D ≥ 2.** Theorem 1 proves density of separable function classes in C(𝒳) using a Stone–Weierstrass argument combined with vector-valued universal approximation, extending prior results that were limited to bivariate CP SepNNs or specific activation functions. The proof technique is clean, systematic, and generalizes to multiple tensor decomposition formats.

- **NTK characterization of SepNNs under two distinct asymptotic regimes.** Lemma 1, Theorem 2, and Corollary 1 derive the NTK of CP SepNNs, establishing convergence to a deterministic kernel when both width and rank → ∞, and to a random (stochastic) kernel under infinite width but fixed rank. This is the first NTK analysis for SepNNs and correctly identifies that fixed-rank SepNNs do not enter the classical deterministic NTK regime, which has practical implications since rank is often kept small.

- **SepPGD algorithm with O(nD) complexity and theoretical connection to classical NTK-based PGD.** Definition 1 and Lemma 2 show that for D=2, SepPGD is equivalent to the preconditioned gradient descent of Geifman et al. (2024) with preconditioner S̃ = S₁⊗Iₙ + Iₙ⊗S₂, while reducing per-iteration cost from O(n^D) to O(nD). The Kronecker-product insight elegantly connects the factor-wise preconditioners to a global preconditioner. The complexity comparison in Table 1 is clear and compelling.

- **Empirical validation of NTK convergence behavior.** Figure 1 uses 10 random seeds with variance reporting to verify the theoretical NTK predictions: fixed-rank NTK remains random at large width (panel a), joint width+rank growth yields deterministic convergence (panel b), the NTK stays approximately fixed during training under large width+rank (panel c), and the eigenvalue decay confirming spectral bias (panel d). This figure is well-designed and properly supports the theory.

## Weaknesses

### Major

- **The SepPGD theoretical justification for D > 2 is limited to a conjecture.** The paper states "It is believed that the result in Lemma 2 (and the analysis following) can be readily extended to multivariate cases D > 2" (p. 8), but provides no proof, conjecture statement, or even a sketch for D > 2. Since the algorithm is defined and used for arbitrary D, this weakens the claim that SepPGD "provably" adjusts the NTK spectrum for the general case. The spectral analysis of sums of Kronecker products for D > 2 is nontrivial and the paper glosses over this.

- **Experiments lack statistical rigor and are too thin to fully support the method's claimed generality.** Outside of Figure 1 (NTK verification), no experiment reports error bars or variance across multiple runs. The image experiment uses a single bird image; the surface experiment uses a single occupancy grid; the PINN experiment shows one equation (diffusion) in the main text. The paper calls these "extensive experiments" (abstract) but the main text evidence is limited. While this is a theory-first paper, the algorithm is presented as a practical contribution, and the validation should meet a higher bar. Additionally, no ablation studies on the rank R or preconditioner update frequency are provided.

- **The experimental design partially conflates per-iteration efficiency with spectral bias alleviation.** Convergence curves plot MSE vs. wall-clock time. When comparing SepPGD (O(nD)) against SepNN+MSK (O(n^D)), the time advantage conflates cheaper per-step cost with improved conditioning. The surface representation experiment (Fig. 3, right) uses "the same iteration number" which partially addresses this, but the primary convergence plots (Fig. 2, Fig. 4) do not. Showing iteration-count curves alongside time curves would cleanly separate the two effects.

### Minor

- **No comparison against standard optimizers (Adam, L-BFGS, SGD with momentum).** The paper only compares SepPGD against the MSK preconditioned variant and plain gradient descent. Since practitioners commonly use Adam for INRs and PINNs, the practical significance of SepPGD relative to widely-used optimizers is unclear.

- **No discussion of failure cases or limitations.** The paper would benefit from acknowledging when SepPGD might not help (e.g., if factor NTK matrices are already well-conditioned, or if the rank is too low to capture interactions). This would strengthen scientific rigor.

### Trivial

- None beyond what the parser would introduce.

## Nice-to-Haves

- Reporting iteration counts alongside wall-clock time for the main convergence plots (Fig. 2, Fig. 4) would cleanly separate spectral bias alleviation from per-iteration speedup.
- Ablation studies on rank R and preconditioner update frequency would help practitioners understand sensitivity.
- A scaling plot showing wall-clock time per epoch for increasing n and D would substantiate the claimed O(nD) scalability.
- Adding error bars (±std over 5+ seeds) to the main experiment figures.

## Removed Points

- *"No error bars on any convergence curve outside the NTK verification plots (Fig. 1)."* — This is kept (moved to Major weakness 2) because it is factually correct and substantive.
- *"The paper conflates per-iteration speed with spectral bias alleviation"* — Kept (Major weakness 3) but toned down from the critic's framing. The paper does include one iteration-controlled experiment (surface representation, Fig. 3), so the claim is partially addressed.
- *"No theorem or proof for D>2"* — Kept (Major weakness 1) because it is factually accurate and important.
- *"Missing comparison to Adam/LBFGS"* — Kept (Minor weakness 1) as a legitimate gap.
- *"No discussion of limitations/failure cases"* — Kept (Minor weakness 2).
- *"Non-grid inputs not tested"* — The paper references non-grid extension (Section A.2) and the main scope explicitly assumes grid inputs. This is scope-appropriate. Moved here.
- *"Missing ablation on rank and preconditioner frequency"* — Kept as part of Major weakness 2 (experiments too thin).
- *"Scalability: never tests on larger grids"* — The paper's experiments involve reasonable grid sizes for the tasks. This is a nice-to-have rather than a core weakness.
- *"Criticism about the paper not discussing practical implications of random NTK"* — The paper provides a remark (Remark 3) addressing this explicitly. Removed.
- *"Criticism that the approximation result requires sufficient rank"* — The paper says "for any ε > 0" which already implies the required rank may depend on complexity. This is standard for approximation theorems. Removed.
- *"Disconnected strengthening suggestions"* about measuring condition number of the effective NTK — these are nice-to-haves, not weaknesses.

## Novel Insights

The paper's key technical insight is the Kronecker-product structure relating SepPGD to classical NTK-based PGD (Lemma 2). This shows that "separating" the preconditioner across the D dimensions — constructing small n×n factor preconditioners S_d rather than one n^D×n^D global preconditioner — yields an equivalent update for D=2 while slashing the cost from exponential to linear. The implication is that the separable architecture of SepNNs is not merely an efficiency trick for forward passes; it also structurally enables efficient preconditioning in a way that dense architectures cannot replicate without the tensor-product grid structure. This observation bridges the NTK-preconditioning literature (Geifman et al., 2024; Shi et al., 2025) with the tensor-decomposition literature and suggests that other tensor-structured architectures (e.g., TT, Tucker) may admit similarly efficient preconditioners.

## Suggestions

- Provide a proof or at least a formal conjecture for the D > 2 case of SepPGD's spectrum adjustment. The non-grid reformulation (Einstein product) mentioned in Section 4 is a starting point.
- Add iteration-count convergence curves to Figures 2 and 4 alongside the time curves, to isolate spectral bias alleviation from per-iteration cost differences.
- Include error bars (±std over 5+ seeds) for the main experimental results, consistent with the rigor shown in Figure 1.
- Compare against at least one standard optimizer (e.g., Adam) to contextualize the practical improvements.

## Score and Decision

**Round 1 (Bracketing):** Three queries over different score bands. Weak anchors (score < 3.5): papers with thin experiments and limited contributions; the SepNN paper is clearly above these. Middle anchors (3.5–7.5): papers with mixed theory–experiment balance, averaging 5.75–6.25; the SepNN paper fits here. Strong anchors (score > 7.5): papers with comprehensive theory and/or extensive experiments; the SepNN paper's experimental thinness and D>2 gap place it below these.

**Round 2 (Narrowing):** Two queries targeting (4.5, 6.5) and (5.0, 7.0). I read anchor GqI4fTVUXC (6.00, rejected — primarily empirical with negative results), VEJzjAvaIy (5.75, accepted — NTK divergence theory, mixed reviews), PCTqol2hvy (6.25, rejected — ResNet approximation, controversy about incremental novelty), and wOSYMHfENq (6.00, accepted — BN universal approximation, similar theory+experiment scope). The SepNN paper compares favorably to these: it has stronger originality than the incremental-novelty ResNet paper, more practical relevance than the NTK divergence paper, and broader theoretical contributions than the BN paper.

**Round 3:** One query (5.5, 6.5) confirming that comparable papers at this score level (FK8tl47xpP at 6.25, 8wAL9ywQNB at 6.00, jqVj8vCQsT at 5.60) span accept/reject decisions based on how clean the experiments are.

**Final Position:** The paper's theoretical contributions (approximation theorem, NTK regimes) are genuinely novel and well-supported. The algorithm is clever and well-motivated with clear complexity analysis. The experiments, while limited, demonstrate the method works on representative tasks. The main weaknesses — the D>2 gap, thin experimental validation without error bars, and conflated per-iteration/spectral-bias comparison — are real but do not invalidate the core theoretical contributions. Placed relative to the anchors, the paper sits above the purely empirical or incremental papers (~5.75) but below papers with comprehensive experiments (~7.0). **Score: 6.0. Decision: Accept.**

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>