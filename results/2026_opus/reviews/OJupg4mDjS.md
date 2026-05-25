Now I have enough calibration. Let me write the final review.

## Round 1 Bracket
- Weak anchors (≤3.5): Bh4BW69ILq (2.60), F5UgXkPgSn (3.00), RmOXAa5H5Y (3.00) — all rejects with weaker theory/execution than this paper.
- Middle anchors (3.5–7.5): HB4lr0ykTi (6.33 Reject — Wasserstein Flow Matching), WPz5e5V85k (6.00 Reject), mkDam1xIzW (7.33 Accept — Probabilistic Geometric PCA), rY8xdjrANt (6.20 Reject).
- Strong anchors (>7.5): cNmu0hZ4CL (8.00 Accept), g7ohDlTITL (8.00 Accept — Flow Matching on General Geometries).

This paper has clear theory and limited empirical validation — initial bracket: **[5.0, 7.0]**.

## Round 2 Narrowing
- q1t0Lmvhty (6.00 Accept — Riemannian Geometry covariance pooling): broader empirical validation than this paper; we sit below it.
- a72vorQK8v (5.50 Reject — VAE Euclidean latent geometry): narrower experiments, similar weakness profile.
- gIiz7tBtYZ (6.00 Accept — Neural OT general costs), sRaAt9OOnW (6.20 Reject — Continuous GW): paper sits closer to these in theory/experiment ratio.
- HB4lr0ykTi (6.33 Reject — WFM) is closest comparison: also has solid Wasserstein theory, similar limitation of narrow experimental validation in the general (point-cloud) regime.

The paper has more polished theoretical contributions than WFM (Otto parametrization without convexity, clean GL_d lift, two distinct algorithms, four theoretical propositions) but very similar empirical validation gap (qualitative only on a.c. case, no head-to-head with Seguy & Cuturi). Lands around 5.5–6.

---

## Summary
The paper introduces two methods for exact Geodesic PCA on Wasserstein space: (1) for centered Gaussians, by lifting computations to GL_d via the Bures-Wasserstein submersion, and (2) GPCAGEN, for absolutely continuous measures, parametrizing geodesics through Otto's representation (id + t∇f)_#(φ_#ρ) — crucially avoiding the convexity requirement of McCann's classical form — using MLPs. The headline contribution is a non-linearized GPCA in the Wasserstein space, distinguishing the work from prior generalized-geodesic approaches (Seguy & Cuturi, 2015) and template-based methods.

## Strengths
- **Gaussian case lift to GL_d (Proposition 3, Eqs. 12–13)** gives a clean, non-linearized algorithm for exact GPCA in the Bures-Wasserstein setting, replacing the geodesic with horizontal line segments and the Bures-Wasserstein distance with the Frobenius norm.
- **Otto's parametrization without convexity (Eq. 9, Section 4)** is a substantive methodological idea: using (id + t∇f) where f need not be convex sidesteps ICNN-style architectural constraints, with the trade-off being eigenvalue monitoring of I_d + tH_{f_ψ}. The paper makes this trade-off explicit (Section 6).
- **Proposition 4 + Figure 4 (right)** provide both an analytical formula and an empirical curve showing how TPCA-vs-GPCA distortion grows with (a−b)²/(a+b)² — the most rigorous piece of quantitative analysis in the paper.
- **Proposition 5** establishes that for univariate Gaussians the first GPCA component stays Gaussian, providing a non-trivial consistency result and motivating the Gaussian-restricted algorithm in d = 1.
- **Continuous sampling capability**: GPCAGEN's continuous-geodesic output lets one sample distributions at any t, which discrete TPCA cannot; Figure 16 (Appendix) shows TPCA's discretization artifacts (holes, mass concentration).

## Weaknesses

### Fatal
None. The theoretical claims are supported and the methodology is sound; the issues below are about evidential strength and framing, not correctness.

### Major
- **No quantitative comparison to the closest prior method on the a.c. case.** Section 5.2 reports only qualitative outputs for MNIST, ModelNet40 (chairs/lamps), and Landscape images. Seguy & Cuturi (2015), explicitly cited as the closest prior method that the paper aims to improve upon ("a method to solve the exact GPCA problem ... is still missing"), is never used as a numerical baseline. The justification on p. 9 — "A direct numerical comparison between the two methods is therefore not meaningful" — is unconvincing because one could discretize the learned continuous geodesic and evaluate Eq. 1, exactly as Figure 4 (right) does in the Gaussian case. Without this, the central claim that GPCAGEN improves over existing approximate GPCA methods is asserted but not demonstrated.
- **"Exact" framing vs. what is actually optimized in Algorithm 1.** The paper carefully scopes "exact" as "no linearization, true geodesics not generalized geodesics" (Section 1, Main Contributions). That is a defensible scope and the paper does not falsely claim hard-constraint optimization. However, three approximations stack between Eq. 1 and Algorithm 1: Sinkhorn divergence replaces W_2² (line 7), orthogonality and intersection are soft regularizers I and O with λ_I = λ_O = 1 (Eq. 211), and the diffeomorphism eigenvalue check is monitored only on minibatch samples {H_{f_ψ}(x_k)} (line 5). Each is reasonable individually, but together they make it hard to read off the recovered components' residual orthogonality/intersection error. Reporting these residuals at convergence would settle whether "exact GPCA components" is achieved to 10⁻² or 10⁻⁶.
- **Higher-order components claimed but never demonstrated.** Section 4 states "Higher-order components can be computed similarly" (l. 219), but every reported experiment uses exactly k = 2. The soft-penalty formulation for orthogonality+intersection does not obviously scale: for component k, the new geodesic must intersect π(A_2) and be orthogonal to all k−1 prior horizontal fields, and soft penalties typically degrade. A 3-component example, even on a toy problem, would substantiate this claim.

### Minor
- **Gaussian case results soften the practical motivation.** Section 5.1 honestly reports "GPCA reduces the objective in equation 11 of less than 1% w.r.t. TPCA, on average for 100 trials" (l. 229) and notes that in the regime where GPCA differs (matrices near the SPD boundary), "GPCA may be seen as worse-behaved as TPCA" (l. 253). The Gaussian contribution is thus structural/methodological rather than producing materially better empirical components in typical regimes. This is appropriately acknowledged but reframes what the Gaussian algorithm buys in practice.
- **Diffeomorphism certificate is only sample-based.** Algorithm 1, line 5 estimates t_min, t_max from {H_{f_ψ}(x_k)} on the minibatch. Outside the sampled set the eigenvalue bound is not enforced, so the returned interval is an estimator, not a certificate that μ_{θ,ψ}(t) is a true geodesic on Ω. The paper should acknowledge this limitation explicitly.
- **Open consistency check (Proposition 5 in d > 1) not probed empirically.** The paper notes that whether GPCAGEN agrees with the Gaussian algorithm in d ≥ 2 is open. Running GPCAGEN on Gaussian data in d = 2 and comparing to the Section 3 algorithm would be a natural validation of GPCAGEN against a near-ground-truth reference and an empirical probe of the open question — but no such check is reported.
- **Sensitivity of λ_I = λ_O = 1 not reported in the main paper.** Since I uses an unnormalized squared distance while O is a scale-invariant squared cosine, mixing them at equal weight against a Sinkhorn loss whose scale depends on ε, batch size, and data is non-obvious. The paper says these settings "ensure the algorithm works as expected in all experiments" and defers discussion to Appendix E, but at least a brief sensitivity figure in the main text would help.

### Trivial
None worth listing.

## Nice-to-Haves
- Report % improvement in Eq. 1 (computed via OT solvers, even non-Sinkhorn) for GPCAGEN vs. discretized Seguy & Cuturi GPCA and vs. TPCA on the ModelNet40 and Landscape experiments — analogous to what Figure 4 (right) does in the Gaussian case.
- Hard-constraint alternative for higher components: e.g., parametrize the second component's velocity field as the L²(ρ)-orthogonal complement of ∇f_{ψ_1}∘φ_{θ_1}, paralleling the explicit ⟨X_2, X_1⟩ = 0 construction in the Gaussian case.
- Cross-validation between Section 3 algorithm and GPCAGEN on Gaussian data in d = 2.
- A 3-component experiment on a toy dataset to substantiate "higher-order components can be computed similarly."
- Reporting residual O and I values at convergence so readers can quantify how "orthogonal" and "intersecting" the recovered second component actually is.

## Removed Points
*These points are flagged as removed; treat them with caution.*

- **Optimization landscape of F with auxiliary Q_i variables (Proposition 3)** — speculative weakness about local minima and restart counts; the paper presents a clear cost surface and empirical results matching theory in Figure 4. Without evidence of optimization failure, this is an area-sweep concern. Demoted/removed.
- **Generic strength "addresses an important problem"** — implied in the strength finder; removed as generic/sycophantic.
- **Reproducibility/hyperparameter concerns at large** — already addressed in Appendix E per the paper's own pointers; demanding more in the main text is presentation, not substance.

## Novel Insights
None beyond the paper's own contributions. The most genuinely novel observations are the paper's own: that Otto's geodesic parametrization sidesteps convexity (enabling ICNN-free networks at the price of eigenvalue monitoring), the closed-form distortion bound (a−b)²/(a+b)² between GPCA and TPCA on Bures-Wasserstein, and that in d = 1 GPCA on a.c. distributions stays Gaussian.

## Suggestions
- Add a single quantitative table on at least one a.c. dataset comparing GPCAGEN, TPCA (discretized), and Seguy & Cuturi (2015) on either reconstruction error of held-out distributions, the discretized Eq. 1 objective, or a downstream classification/clustering metric.
- Run GPCAGEN on Gaussian data in d = 2 and compare with the Section 3 algorithm; report the gap as a self-consistency check and as empirical evidence on the open question after Proposition 5.
- Report residual values of I and O at convergence (in absolute units, and as a fraction of the Sinkhorn loss term) for each experiment.
- Demonstrate at least 3 components on a synthetic dataset where higher-order structure is known; comment on whether soft constraints saturate as k grows.
- Move the brief justification of λ_I = λ_O = 1 — currently in Appendix E — into the main text alongside a sensitivity sweep.

---

## Calibration Notes

Anchors retrieved across both rounds (all listed; *read in full*):

Round 1:
- Bh4BW69ILq.md (2.60, Reject) — unbalanced OT solver; clearly weaker than this paper.
- F5UgXkPgSn.md (3.00, Reject) — Grassmannian matrix completion; weaker.
- 4mqt6QxSUO.md (3.25, Reject) — Riemannian framework for CT; weaker, more application-driven.
- RmOXAa5H5Y.md (3.00, Reject) — Tree-Wasserstein simplicial reps; weaker.
- HB4lr0ykTi.md (6.33, Reject) — *Wasserstein Flow Matching.* Closest comparator: solid Riemannian/Wasserstein theory, narrow experimental validation; this paper has stronger structural theory (Otto-without-convexity, Prop 4, Prop 5) but similar empirical thinness on the general/point-cloud regime.
- WPz5e5V85k.md (6.00, Reject) — Wasserstein proximal convergence theory; pure theory, comparable theoretical depth.
- *mkDam1xIzW.md* (7.33, Accept) — Probabilistic Geometric PCA. More empirical breadth than this paper; this paper is below it.
- rY8xdjrANt.md (6.20, Reject) — OT barycenter via minimax; comparable theory-heavy/experiment-light profile.
- cNmu0hZ4CL.md (8.00, Accept) — OT distances for neural dynamics; broader practical demonstration, above this paper.
- g7ohDlTITL.md (8.00, Accept) — Flow Matching on General Geometries; broader scope and validation, above this paper.
- JWtrk7mprJ.md (7.60, Accept) — Deep GPs on manifolds; above this paper in empirical breadth.
- TTrzgEZt9s.md (8.00, Accept) — DRO Prospect algorithm; off-topic and above.

Round 2 (narrowing inside [5.0, 7.0]):
- q1t0Lmvhty.md (6.00, Accept) — SPD/Riemannian covariance pooling; broader applied validation, above this paper.
- a72vorQK8v.md (5.50, Reject) — FlatVI VAE with Euclidean latent geometry; comparable theory-application gap.
- gIiz7tBtYZ.md (6.00, Accept) — Neural OT general cost; close in scope to this paper.
- sRaAt9OOnW.md (6.20, Reject) — Continuous Gromov-Wasserstein; theory-heavy with empirical caveats, similar profile.

**Final placement.** This paper has stronger theoretical content than Wasserstein Flow Matching (6.33 Reject) — Otto-without-convexity and the Bures-Wasserstein lift are clean structural contributions, and Propositions 4–5 deliver real analytical results — but its a.c. experimental validation is purely qualitative with no head-to-head against the closest prior method. It is slightly below the 6.0 accepts (q1t0Lmvhty, gIiz7tBtYZ) which have stronger empirical validation, and above the 5.50 reject (a72vorQK8v). The bracket narrows to [5.5, 6.0], landing at **5.5**.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>