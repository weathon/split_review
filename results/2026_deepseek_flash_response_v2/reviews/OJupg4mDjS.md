Now I have sufficient calibration context. Let me write the final review.

## Summary

This paper addresses Wasserstein Geodesic Principal Component Analysis (GPCA), proposing two methods: one for centered Gaussian distributions via a lift to GL_d using the Bures-Wasserstein geometry, and one (GPCAGEN) for general absolutely continuous probability measures using Otto's fiber bundle parametrization with neural networks. The Gaussian case is well-developed, including theoretical quantification of when tangent PCA (TPCA) distorts the geometry (Proposition 4). The GPCAGEN method parametrizes geodesics via standard MLPs without input-convex neural networks, and is demonstrated qualitatively on 3D point clouds, images, and MNIST.

## Strengths

1. **Exact GPCA for Gaussians via lift to GL_d**: Proposition 3 provides a sound reduction of the GPCA problem to an optimization over GL_d with rotation variables, yielding true Wasserstein geodesic components rather than approximations. The connection to the fiber bundle geometry is clearly explained.

2. **Provable quantification of TPCA distortion**: Proposition 4 (Equation 14) gives a closed-form asymptotic expression for the ratio of the true Bures-Wasserstein distance to its linearized approximation: \(1 - \left(\frac{a-b}{a+b}\right)^2 \cos^2 \theta + O((a-b)^4)\). The accompanying experiments (Figure 4, right) support the theory and show GPCA improving the cost by ~35% in high-distortion regimes.

3. **Neural parametrization of Wasserstein geodesics without input-convex neural networks**: GPCAGEN (Section 4) uses Otto's parametrization \(\mu(t) = (\text{id} + t\nabla f_\psi)_\#(\varphi_\theta\#\rho)\) to represent geodesics via standard MLPs, avoiding the need for ICNNs. The trade-off (Hessian eigenvalue monitoring instead of hard convexity constraints) is explicitly stated in Section 6.

4. **Proof that univariate Gaussian GPCA stays in the Gaussian manifold**: Proposition 5 establishes that for univariate Gaussian data, the first GPCA component remains within the Gaussian submanifold, with honest acknowledgment that higher dimensions remain open.

5. **Proper handling of finite-time geodesic validity**: The paper explicitly addresses that Wasserstein geodesics cannot be extended for all time (citing Kloeckner, 2010) and incorporates clipping operators (Equation 12) and Hessian eigenvalue monitoring (Algorithm 1, line 5) to ensure validity, a practical contribution prior neural OT work often glosses over.

## Weaknesses

### Major

1. **GPCAGEN experiments lack quantitative evaluation — the central claim is unvalidated.** The paper's main advertised contribution (GPCAGEN for general a.c. measures) is supported only by qualitative visualizations. The synthetic experiment with known geodesics is mentioned in Section 5.2 but its results are not reported in the main text. The MNIST, 3D point cloud, and landscape experiments show interpolations but provide no reconstruction error, explained variance, or objective value numbers. The paper states that "A direct numerical comparison between [GPCAGEN and TPCA] is therefore not meaningful" (lines 263–264), but this does not excuse the absence of any quantitative assessment of GPCAGEN's own performance. For a paper whose title and abstract claim to solve the *exact* GPCA problem for general a.c. measures, the evidence presented does not allow a reader to evaluate whether GPCAGEN actually works. Reporting the objective value of Equation 15 achieved by GPCAGEN alone would be straightforward and meaningful even without cross-method comparisons.

2. **No quantitative validation of the orthogonality constraint.** The second and higher GPCAGEN components rely on regularization terms with coefficients \(\lambda_I = \lambda_O = 1.0\). The paper does not report whether the resulting components are actually orthogonal in the Wasserstein sense (e.g., the inner product between velocity fields after training), how sensitive results are to these hyperparameters, or whether the intersection constraint is satisfied. Given that orthogonality is definitional to PCA, this is a significant gap.

### Minor

3. **The Gaussian pathological regime raises practical questions.** The paper admits that in the same-eigenvalue regime where GPCA differs most from TPCA, it "may be seen as worse-behaved as TPCA, as some of the Gaussian distributions will project onto the first geodesic component boundaries, yielding a poor separation" (lines 232–233). The Discussion (line 282) mentions this only in passing. While honesty about limitations is commendable, the paper does not provide guidance on when practitioners should prefer GPCA over TPCA, which matters given that GPCA improves the objective by less than 1% on average.

4. **No runtime or scaling analysis.** GPCAGEN involves computing Hessian eigenvalues per sample per iteration, which is computationally demanding for high-dimensional data. The paper reports no wall-clock times or scaling behavior with dimension \(d\) or number of distributions \(n\).

5. **The "exact" claim could be better calibrated to the implementation.** The paper defines "exact" as "not rely[ing] on a linearization of the Wasserstein space" (line 28), which is clear and appropriate. However, the practical algorithm uses the Sinkhorn divergence (an approximation to \(W_2^2\)), finite minibatches, Hessian eigenvalue estimates from finite samples, and neural networks with no convergence guarantees. The gap between the theoretical parametrization (Equation 15) and the implemented algorithm is not explicitly acknowledged.

### Trivial

6. Algorithm 1 trains on one distribution per iteration with shared \(t_i\) parameters; the convergence behavior of this stochastic scheme is not discussed.

## Nice-to-Haves

- Report the objective value of Equation 15 achieved by GPCAGEN for each experiment. Even without cross-method comparisons, this lets future work benchmark against the method.
- Run a controlled synthetic experiment where ground-truth geodesics are known and report quantitative recovery error (e.g., angle between recovered and true velocity fields, or relative objective error).
- Report quantitative orthogonality measures (e.g., \(\langle g, h \rangle_{L^2(\rho)} / (\|g\|\|h\|)\)) for the second component across experiments, with sensitivity analysis for \(\lambda_I, \lambda_O\).
- Add wall-clock training times and discuss how the method scales with dimension and dataset size.

## Removed Points

These points are flagged to be removed, treat them with caution:
- Harsh Critic's framing that "exact is only theoretical, not practical" as a fatal weakness: the paper explicitly defines "exact" as "not relying on a linearization" (line 28), which is a clear and appropriate definition. Demoted to Minor (#5 above) — the issue is about acknowledging the practical gap, not about the claim being wrong.
- Implementation detail complaints about computing \(\nabla f_\psi\) and \(H_{f_\psi}\): these are standard automatic differentiation operations for MLPs; the paper references Appendix E for architecture details. This falls under normal implementation specificity for ML papers.
- Deferred synthetic experiment results: the critic acknowledges the experiment exists in the appendix. Hard rules forbid penalizing missing appendix content. However, the broader point about absent quantitative evaluation in the main text stands and is kept as Major weakness #1.
- Strength Finder's strengths are all concrete and specific to the paper; none were removed.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add a quantitative evaluation table for GPCAGEN reporting the objective of Equation 15 for each experiment, as well as a synthetic recovery experiment with measured recovery error.
2. Report quantitative orthogonality measures for the second component and include sensitivity analysis for \(\lambda_I\) and \(\lambda_O\).
3. Include wall-clock training times and scaling information to help readers assess practical applicability.
4. Add a brief discussion offering guidance on when GPCA should be preferred over TPCA in practice, given the pathological regime.

## Score and Decision

### Calibration Anchors

**Round 1 — Bracketing (all queries: "Wasserstein geodesic PCA probability measures optimal transport"):**

Weak band (score < 3.5): avg 2.60–3.40 — papers with significant flaws or marginal relevance. Current paper is clearly stronger.

Middle band (3.5 < score < 7.5): avg 3.80–6.33. Key anchors read:
- Wasserstein Flow Matching (HB4lr0ykTi, avg 6.33, scores 5/8/6): Reject. Similar topic (Wasserstein geometry + neural networks), stronger experiments (quantitative on Gaussians), weaker theory (no original theoretical contributions comparable to Proposition 4). Current paper has stronger theory but weaker experiments.
- Wasserstein Proximal Algorithm (WPz5e5V85k, avg 6.00, 6/6/6/6): Reject. Theory-heavy, weak experiments, some technical errors. Current paper is cleaner and has better experiments.
- OT Barycenter via Minimax (rY8xdjrANt, avg 6.20, 8/6/6/6/5): Reject. Theory + experiments but gap between theory and practice. Current paper comparable.
- Neural OT with General Cost (gIiz7tBtYZ, avg 6.00, 6/6/6/6): Accept. Theory + quantitative experiments (though described as "toyish"). Current paper has comparable theory but weaker experiments.
- Continuous GWOT (sRaAt9OOnW, avg 6.20, 6/5/6/8/6): Reject. Mixed reviews, analysis + proposed method. Current paper comparable.
- Relative-Translation Invariant Wasserstein (CrOHzVtWmH, avg 3.80): Lower-scored. Current paper is clearly stronger.

Strong band (score > 7.5): avg 8.00 — papers with strong theory, thorough experiments, and clear practical significance. Current paper does not reach this bar.

**Round 1 bracket: 4.5 – 6.5**

**Round 2 — Narrowing (geodesic PCA / Wasserstein neural qualitative evaluation):**
- Riemannian DDPMS (ZwO2I8gS5O, avg 6.00, 8/5/5/6): Reject. Strong experiments (quantitative on several manifolds), reasonable theory. Better validated than current paper.
- SPD Riemannian Classifiers (EyWKb7Ltcx, avg 5.00, 6/3/5/6): Reject. More specialized, mixed reviews.
- Generative Modeling on Manifolds (ZLSdwjDevK, avg 5.67, 6/6/5): Reject. Interesting approach but limited validation.
- Neural OT + General Cost (gIiz7tBtYZ, avg 6.00): All 6s, accepted. Current paper has comparably strong theory but weaker experiments.

**Final calibration:** The paper is comparable to the ~5–6 band anchors. It has genuine theoretical contributions (Proposition 4 is novel and well-supported; the Otto parametrization for GPCA is a legitimate idea) that lift it above the 3–4 range. However, its central claim — solving *exact* GPCA for general a.c. measures via GPCAGEN — lacks quantitative validation. The Gaussian GPCA part is solid but mostly shows marginal improvement over the existing baseline (TPCA). Papers like Neural OT (avg 6.00, accepted) had both theory and quantitative experiments; the current paper falls short of that standard on the experimental side. Papers like Wasserstein Flow Matching (avg 6.33, rejected) had quantitative experiments but weaker theory; the current paper's experimental gap is larger in a different direction.

**Score: 5.0** — Below acceptance threshold due to insufficient validation of the central contribution, but with genuine theoretical merit that makes it above the bottom of the scale.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>