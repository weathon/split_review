- Decision: Accept
- Avg Score: 5.20
- Scores: 6, 8, 6, 3, 3
Now I have all the information needed. Let me produce the consolidated review.

## Summary

This paper introduces ANaGRAM (Adapted Natural Gradient Relative to Adapted Model), a Gauss-Newton-type optimizer for Physics-Informed Neural Networks that is derived from a function-space geometric analysis of the PINN training problem. The paper makes two main contributions: (1) Algorithm 1 ("vanilla ANaGRAM"), which computes the update via an SVD-based pseudoinverse of the empirical Jacobian with complexity O(min(P²S, S²P)), and is explicitly acknowledged to be equivalent to Gauss-Newton; and (2) a theoretical connection (Theorem 2) showing that the natural gradient for PINNs corresponds to applying the Green's function of the differential operator restricted to the tangent space. Experiments on four PDE benchmarks (2D Laplace, Heat, 5D Laplace, Allen-Cahn) show competitive accuracy compared to E-NGD and L-BFGS.

## Strengths

- **Green's function connection (Theorem 2, Section 4.2):** The theoretical result that the natural gradient update for PINNs with a linear differential operator implicitly uses the generalized Green's function of that operator on the tangent space is genuinely insightful and provides a principled interpretation of the optimizer's behavior. This is a non-trivial theoretical contribution that connects optimization geometry to classical PDE theory.

- **Scalable SVD-based implementation:** The algorithm achieves O(min(P²S, S²P)) complexity by computing the SVD of the P×S empirical Jacobian rather than inverting the P×P Gram matrix. This is a practical advantage for PINNs where the number of parameters P can be large relative to the batch size S, and the paper demonstrates it on problems with up to P=921 parameters.

- **Consistent empirical improvement on fair comparisons:** On the 2D Laplace, Heat, and 5D Laplace problems where ANaGRAM, E-NGD, and L-BFGS are all run for the same number of iterations (2000 or 1000), ANaGRAM achieves competitive or better median L² errors, demonstrating genuine practical value.

- **Clean reformulation of PINNs:** The reinterpretation of the PINN loss (Equation 7) as a least-squares problem on the compound model (D,B)∘u (Section 4.1) is a clean framing that enables the direct application of the ANaGRAM framework with minimal modification.

## Weaknesses

### Fatal
None.

### Major

- **Unjustified neglect of the correction terms (Section 3, Theorem 1 → Algorithm 1):** The paper's central theoretical machinery decomposes the natural gradient update into a main term plus two correction terms, E^{metric}_θ and E^⊥_θ. The paper then says "As a first approximation, we can neglect those two terms" (line 184) and defines Algorithm 1 without them. No theoretical bound, error analysis, or empirical check is provided to justify this neglect. The paper acknowledges that Algorithm 1 "is equivalent to Gauss-Newton algorithm" (line 201). This means the paper's practical algorithm is simply Gauss-Newton, while the title and framing emphasize "natural gradient" — a significantly stronger claim. The paper would be more honest and impactful if it either (a) analyzed when the correction terms are provably small, (b) provided an empirical ablation showing they are negligible in practice, or (c) reframed the contribution as a principled Gauss-Newton method with interesting geometric interpretations.

- **Asymmetric experimental comparison for Allen-Cahn (Section 5, Figure 4):** In the Allen-Cahn experiment, ANaGRAM and L-BFGS are trained for 4000 iterations each, while E-NGD (the primary baseline) is trained for only 1000 iterations (line 389). This makes the comparison fundamentally unfair — of course a method given 4× the iterations may show better final accuracy. The paper's concluding claim that "ANaGRAM consistently outperforms both E-NGD and L-BFGS" relies in part on this asymmetric comparison, which does not support the claim.

### Minor

- **No statistical significance testing:** Results are reported as medians over 10 runs with interquartile ranges. For several comparisons (e.g., 2D Laplace, 5D Laplace), the quartile ranges overlap between ANaGRAM and E-NGD. Without a statistical test (e.g., Wilcoxon signed-rank), the claim of "significant margin" is unsupported. This is a common issue in ML papers but worth noting given the strength of the claims.

- **Green's function connection (Theorem 2) is not empirically leveraged or tested:** While Theorem 2 is an elegant theoretical result, it remains entirely separate from the algorithm and experiments. The paper does not test the Green's function interpretation, use it to derive insights about convergence, or connect it to the choice of hyperparameters. It reads as a standalone observation rather than an integral part of the paper's contribution.

- **Unclear theoretical distinction between ANaGRAM and E-NGD:** The paper compares against E-NGD (Müller & Zeinhofer, 2023) experimentally but does not provide a side-by-side derivation or analysis explaining exactly where the algorithms differ and why ANaGRAM should be expected to outperform. The reader cannot tell whether improvements come from the pseudoinverse vs. a different approximation, the line search, the cutoff strategy, or architecture choices.

- **No sensitivity analysis for the cutoff factor ε:** The cutoff factor is manually chosen per problem and varies by orders of magnitude (1×10⁻⁶, 1×10⁻⁵, 5×10⁻⁷×Δ_max). No study of how performance varies with ε is provided, yet this is a key hyperparameter of the method. The paper acknowledges this as a limitation but does not investigate it.

### Trivial

- **Theorem 1 presentation is difficult to parse:** The theorem statement (lines 174–182) is presented with notation that is incompletely defined in the main text, and the connection between the theorem and the subsequent algorithm is not clearly explained. Improving clarity here would strengthen the paper's central theoretical contribution.

## Nice-to-Haves

- An ablation experiment (even on one PDE) comparing the full update (with E^{metric}_θ and E^⊥_θ approximated) against vanilla ANaGRAM would directly address the central theoretical weakness.
- Testing on larger architectures (P > 10⁴) would better demonstrate the scalability claim.
- A time-to-accuracy comparison (wall-clock time to reach a given L² error threshold) would complement the iteration-based results.

## Removed Points

These points are flagged to be removed, treat them with caution:
- **CPU time tables not shown:** The reviewer notes CPU time tables are referenced but not visible. However, these were likely in the appendix/supplementary which was stripped by the parser. Per the rules, removed.
- **Scaling not new (inherent to SVD):** The critic argues the O(min(P²S, S²P)) scaling is not new because Gauss-Newton methods have this complexity. The paper reports this as a property of the algorithm, not as a claim of novelty. The strength finder correctly lists it as a practical strength. Removed.
- **Missing related works:** Per instructions, removed as this cannot be verified without external sources.
- **Figures show "substantial overlap" in interquartile ranges:** This claim cannot be verified from extracted text alone (figures are images). The point about no statistical tests is retained above, but the specific claim about degree of overlap is removed.
- **Nitpick about Theorem 1 being "garbled and incomplete":** Some of the garbled quality is from PDF parsing artifacts. The substantive point about clarity is retained in Trivial.

## Novel Insights

An interesting cross-perspective emerges from synthesizing the harsh critic and strength finder: the same structural fact — that Algorithm 1 discards the correction terms — is simultaneously the paper's greatest vulnerability (it severs the link from the natural gradient theory to the practical method) and the source of its computational efficiency (it reduces to a simple SVD-based Gauss-Newton). This tension suggests that the paper's most honest framing would be: "Gauss-Newton on PINNs, reinterpreted through a natural-gradient lens, with an elegant Green's function aside" — which is still a solid contribution. The Green's function connection genuinely enriches understanding even if the algorithm itself does not implement the full natural gradient.

## Suggestions

1. **Reframe the contribution honestly.** Either provide a justification (theoretical or empirical) for neglecting the correction terms and keep the natural gradient framing, or explicitly reframe the paper as a principled Gauss-Newton method with natural-gradient-inspired analysis and a Green's function connection. The latter is more defensible given the current content.

2. **Re-run the Allen-Cahn experiment** with E-NGD for 4000 iterations (matching ANaGRAM) to produce a fair comparison, or remove the claim that ANaGRAM "consistently outperforms" E-NGD for this problem.

3. **Add a statistical test** (e.g., Wilcoxon signed-rank at a fixed iteration count) to support the "significant margin" claims.

4. **Include a sensitivity analysis** for the cutoff factor ε on at least one problem, showing how accuracy and iteration count vary with ε.

5. **Improve the clarity of Theorem 1** by fully defining all terms in the main text and explicitly connecting the theorem to the algorithm that follows.

**Originality:** The Green's function connection is novel. The algorithm itself is acknowledged as Gauss-Newton, limiting the algorithmic novelty. The overall package is moderately original.

**Importance of research question:** Training PINNs efficiently is an important and active research area.

**Claims support:** Claims about outperforming baselines are moderately supported but weakened by the asymmetric Allen-Cahn experiment and lack of statistical tests.

**Soundness of experiments:** Reasonable for 3 out of 4 benchmarks; the Allen-Cahn comparison is unsound as presented.

**Clarity of writing:** Mixed — the theoretical sections are dense and somewhat unclear in places (Theorem 1), while the experimental setup is described clearly.

**Value to community:** Moderate — the Green's function connection offers genuine insight, and the algorithm is practically useful despite the framing issues.
