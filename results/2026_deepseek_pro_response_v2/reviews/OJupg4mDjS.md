Now I have sufficient calibration data to finalize. Let me compile the final review.

**Round 1 Bracket:** 5.0 – 6.5
**Round 2 Narrowing:** The paper is stronger than FlatVI (5.50) — which reviewers found incremental — and Riemannian SPD classifiers (5.00). It is somewhat below WFM (6.33) which had stronger quantitative evaluation and below the GW benchmark (6.20) which had more thorough benchmark analysis. It is comparable to the Wasserstein Proximal Algorithm (6.00). Final placement: **5.5**.

---

## Summary
This paper introduces two methods for solving exact Geodesic PCA (GPCA) on probability measures using the Wasserstein geometry. The first method handles centered Gaussian distributions by lifting computations to GL_d via the Bures-Wasserstein fiber-bundle geometry (Proposition 3). The second method, GPCAGEN, handles general absolutely continuous probability measures by parametrizing Otto geodesics with neural networks, avoiding the need for input-convex neural networks. The paper provides theoretical results including a closed-form characterization of when TPCA and GPCA diverge (Proposition 4) and a proof that 1D Gaussian GPCA stays within the Gaussian submanifold (Proposition 5). The Gaussian experiments are well-controlled and quantitative; the GPCAGEN experiments are qualitative only.

## Strengths
- **Clean theoretical framework for Gaussian GPCA via fiber-bundle lifting (Proposition 3):** The lifting of the GPCA problem from S_d^{++} to GL_d converts a Riemannian optimization into Frobenius-norm minimization over invertible matrices with orthogonal group variables. The handling of the second component with intersection and orthogonality constraints is mathematically sound, providing a principled and implementable algorithm.
- **Otto parametrization avoids ICNN constraints (Section 4, Algorithm 1):** By using Otto's formulation where ∇f need not be convex, the paper avoids the architectural overhead of input-convex neural networks required under McCann's parametrization. This is a genuine technical simplification, and Algorithm 1 provides a concrete, implementable training loop.
- **Proposition 4 quantifies when TPCA and GPCA diverge:** The closed-form expression (equation 14) parameterized by (a-b)/(a+b) provides a precise, interpretable curvature metric predicting TPCA distortion. Figure 4(right) empirically validates this prediction with error bands, showing cost improvement rising from near 0% to ~35% as the eigenvalue ratio approaches 1.
- **Proposition 5 is a clean, non-obvious theoretical result:** Proving that 1D Gaussian GPCA performed in the full space of a.c. distributions remains within the Gaussian submanifold addresses a subtle question that arises naturally from presenting two separate algorithms (Sections 3 and 4).
- **Controlled MNIST recovery experiment (Figure 5):** Constructing two known orthogonal geodesics (digit interpolation + color variation) and verifying GPCAGEN recovers both with correct orthogonality is a strong sanity check with ground truth.
- **Explicit handling of geodesic domain constraints:** Both methods operationalize the finite time interval [t_min, t_max] concretely — via clipping in the Gaussian case and Hessian eigenvalue monitoring in GPCAGEN — where many prior works elide this technical complication.
- **Multi-modal empirical exploration:** The method is demonstrated on Gaussians, MNIST, ModelNet40 point clouds (chairs and lamps), and landscape image color distributions, showing breadth of applicability.

## Weaknesses

### Fatal
None.

### Major
- **Diffeomorphism requirement for φ_θ is unenforced (Section 4):** Proposition 2 requires φ to be a diffeomorphism for the Otto construction — the line φ + t∇f ∘ φ must lie in Diff(Ω). Yet φ_θ is parametrized with a standard MLP without any architectural constraint or regularization to ensure invertibility. The paper monitors the diffeomorphism condition only for the inner map (id + t∇f_ψ, via Hessian eigenvalue positivity, line 161–162) but leaves φ_θ unconstrained. This means the curve t ↦ (id + t∇f_ψ)#(φ_θ#ρ) is not theoretically guaranteed to be a Wasserstein geodesic. The practical impact is unclear (the MNIST experiment shows recovery), but the theoretical claim of producing true geodesics is unsubstantiated without this condition.
- **No quantitative evaluation for GPCAGEN (Section 5.2):** All GPCAGEN results are presented through visual inspection of sampled distributions along geodesics (Figures 5–7). There are no numerical metrics: no reconstruction error, no variance explained, no comparison of attained objective values against baselines, no statistical reporting of run-to-run variance. Even the MNIST experiment with known ground truth reports no quantitative recovery metric (e.g., correlation between recovered and true t_i values, or geodesic alignment error). The paper explicitly declines numerical comparison with TPCA (line 264: "A direct numerical comparison between the two methods is therefore not meaningful"), and the latent-space PCA baseline is mentioned but not developed in the main text. For a method paper claiming to solve exact GPCA, quantitative validation is essential for readers to assess whether the method finds good geodesic components or merely visually plausible ones.

### Minor
- **GPCA ≈ TPCA tension under-explored:** The paper reports that for random Gaussian data, GPCA improves the objective by less than 1% over TPCA (line 208), and that in the regime where they diverge significantly, GPCA "may be seen as worse-behaved as TPCA" (line 232). The Discussion acknowledges this but the paper never identifies a concrete regime where GPCA meaningfully outperforms TPCA on a downstream task, which weakens the practical motivation for the Gaussian method.
- **Sinkhorn divergence bias undiscussed:** The optimization replaces W_2^2 with the Sinkhorn divergence S_ε (line 168). The entropic regularization parameter ε biases the objective — the minimizer of the Sinkhorn-regularized problem is not the minimizer of the true GPCA objective. The paper does not discuss how ε is chosen, what bias it introduces, or whether recovered geodesics are robust to this choice. While using Sinkhorn is standard practice, the paper's claim of solving the "exact" GPCA problem warrants discussion of this approximation.
- **Orthogonality condition simplified in GPCAGEN:** The paper acknowledges (lines 196–197) that the orthogonality regularization uses a simplified condition — enforcing ξ_1 = ξ_2 at intersection rather than the composition with R* — and that this is adopted because computing R* is computationally expensive. Per Proposition 2, the theoretically correct condition requires the composition, so this is a non-trivial deviation, though the paper is transparent about it.
- **Hessian eigenvalue estimation from finite samples:** The bounds on t_min, t_max rely on eigenvalue estimates from a finite sample set {x_k} (line 168). Eigenvalues that become negative between sample points would go undetected, so the "geodesic" could leave the valid domain at unsampled locations without the algorithm knowing.
- **Compact-support theory vs. unbounded-domain practice:** The theoretical framework uses Prob(Ω) for compact Ω ⊂ ℝ^d (line 72), but the method uses ℝ^d throughout (φ: ℝ^d → ℝ^d, line 156). This discrepancy is not addressed.
- **Post-hoc interpretations without verification:** The ModelNet40 and landscape experiments interpret the learned components qualitatively ("captures the distinction between hanging lamps and standing lamps," line 260). These interpretations are post-hoc narratives without ground truth or quantitative verification, though this is common for exploratory unsupervised methods.

### Trivial
- Algorithm 1 specifies "while not converged" without specifying a convergence criterion.
- The claim that latent-space PCA is "computationally expensive" (line 268) is asserted without supporting evidence in the main text.

## Nice-to-Haves
- Measure and report how close φ_θ is to being invertible in practice (e.g., reconstruction error under an approximate inverse, or condition number of the Jacobian).
- Vary the Sinkhorn parameter ε and demonstrate robustness of the recovered geodesics.
- Provide a quantitative downstream application (classification, clustering, or outlier detection as mentioned in line 282) to demonstrate practical utility beyond visual inspection.
- Include a discussion of initialization sensitivity for the non-convex joint optimization over A, X, and Q_i in the Gaussian case.

## Removed Points
These points are flagged to be removed, treat them with caution:

- **HC claimed the diffeomorphism gap is "fatal" / "structural":** Demoted to Major. The gap is real and merits attention, but its practical impact is unverified (the MNIST experiment shows the method can work). It is addressable with architectural constraints, normalizing flows, or an invertibility regularizer. A fatal flaw requires unambiguous impossibility; this is a theoretical gap that may or may not affect empirical performance.
- **HC claimed "no quantitative evaluation of any kind":** Narrowed to apply specifically to GPCAGEN (Section 5.2). The Gaussian experiments (Section 5.1) do include quantitative metrics: cost improvement percentages with standard deviation bands in Figure 4(right), objective comparisons between GPCA and TPCA. The claim was overbroad.
- **HC demanded downstream task results (classification, clustering):** Moved to Nice-to-Haves. The paper's stated scope is solving the GPCA problem; demonstrating downstream applications is desirable but not a core requirement for evaluating whether the method solves GPCA.
- **HC criticized the MNIST experiment as "only a recovery test on synthetic construction":** Controlled recovery tests with known ground truth are standard and valuable validation practice, not a weakness. Retained as a strength.
- **HC claimed the paper "undermines its own motivation" as a structural flaw:** Demoted to Minor. The paper is transparent about the GPCA ≈ TPCA finding in both the experiments and Discussion; this is honest reporting rather than a structural flaw. The contribution stands on introducing methods for exact GPCA, not on proving GPCA universally outperforms TPCA.
- **Strength Finder generic strengths removed:** "The paper addresses an important problem" and similar framings are generic and removed. The kept strengths are all anchored to specific results, equations, or figures.
- **Strength Finder "multi-modal experimental validation" framed as strong evidence:** Retained but noted that the GPCAGEN evaluations are qualitative, while the Gaussian evaluations are quantitative.

## Novel Insights
None beyond the paper's own contributions. The reviewers' observations mainly confirm or question the paper's claims without introducing independently novel perspectives.

## Suggestions
- Add an invertibility measure or use invertible architectures (e.g., coupling layers, normalizing flows) for φ_θ to close the diffeomorphism gap. At minimum, report the approximate inverse reconstruction error of the learned φ_θ.
- Report the final GPCA objective value (the Sinkhorn sum) for GPCAGEN and compare against a random baseline or against TPCA evaluated under the same Sinkhorn metric to give readers a quantitative sense of performance.
- Confront the GPCA ≈ TPCA finding directly in the Discussion: either identify a concrete regime (perhaps beyond Gaussians, in the GPCAGEN setting) where GPCA meaningfully improves over TPCA, or reframe the contribution to acknowledge TPCA as a strong practical baseline whose limitations are mostly theoretical in the Gaussian case.

## Score and Decision

**Anchor comparison summary:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| COT (9WG1ga39Dq) | 3.00 | R1 (weak) | Paper is much stronger |
| Unbalanced OT (Bh4BW69ILq) | 2.60 | R1 (weak) | Paper is much stronger |
| Simplicial Wasserstein (RmOXAa5H5Y) | 3.00 | R1 (weak) | Paper is much stronger |
| Schrödinger Bridge (FjifPJV2Ol) | 3.40 | R1 (weak) | Paper is much stronger |
| Riemannian SPD Classifiers (EyWKb7Ltcx) | 5.00 | R2 | Paper is stronger — more novel theory, more varied contributions |
| FlatVI (a72vorQK8v) | 5.50 | R2 | Paper is comparable/slightly stronger — significantly more novel method |
| Wasserstein Proximal (WPz5e5V85k) | 6.00 | R1 (mid) | Paper is comparable — more diverse but less rigorous in evaluation |
| Riemannian DDPM (ZwO2I8gS5O) | 6.00 | R2 | Paper is comparable — different domains |
| Energy-guided Neural OT (d6tUsZeVs7) | 6.00 | R2 | Paper is comparable |
| GW Benchmark (sRaAt9OOnW) | 6.20 | R2 | Paper is slightly weaker — less thorough empirical analysis |
| WFM (HB4lr0ykTi) | 6.33 | R2 | Paper is weaker — WFM has quantitative evaluation, our GPCAGEN does not |
| Neural Sampling Wasserstein (TUvg5uwdeG) | 6.40 | R2 | Paper is weaker |
| Federated Wasserstein (rsg1mvUahT) | 6.50 | R1 (mid) | Paper is weaker |
| Flow Matching on Geometries (g7ohDlTITL) | 8.00 | R1 (strong) | Paper is much weaker |
| Neural Population OT (cNmu0hZ4CL) | 8.00 | R1 (strong) | Paper is much weaker |

**Bracket:** Round 1 placed the paper between 5.0 and 6.5. Round 2 narrowed to 5.0–6.0 by comparison with the FlatVI (5.50), SPD classifiers (5.00), and GW benchmark (6.20). The paper is clearly stronger than 5.00 (SPD classifiers, which reviewers found incremental and overclaimed) and comparable to FlatVI at 5.50, but the GPCAGEN evaluation gap (fully qualitative) and the diffeomorphism issue place it below the 6.0+ papers that have quantitative validation. **Final score: 5.5.**

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>