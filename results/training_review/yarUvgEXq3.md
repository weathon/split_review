Now I have all the evidence needed. Let me produce the final consolidated review.

---

## Summary

This paper introduces SAFER, a scalable collaborative filtering method that optimizes the Conditional Value at Risk (CVaR) to improve recommendation quality for tail users. The key algorithmic contribution is applying convolution-type smoothing to the CVaR check function, which enables a primal-dual splitting reformulation. This reduces the optimization to a re-weighted alternating least squares solver with per-epoch complexity identical to the highly efficient iALS algorithm. Experiments on MovieLens and Million Song Dataset demonstrate competitive tail-performance improvements while maintaining iALS-level scalability.

## Strengths

- **Convolution-type smoothing enables separable CVaR optimization.** The paper identifies a fundamental obstacle: the check function in CVaR destroys separability, preventing block-coordinate methods. By applying convolution smoothing (Section 3.1), the objective becomes smooth and convex, allowing a primal-dual splitting (Section 3.3) where dual variables have the closed-form solution $z_i = 1-K_h(-r_i)$ and the primal subproblem reduces to embarrassingly parallel re-weighted ALS. This directly overcomes the non-separability challenge identified in Section 2.

- **Competitive tail performance with iALS-level runtime.** On all three datasets, SAFER achieves superior Recall@K for tail users ($\alpha=0.3$) compared to iALS, ERM-MF, and MultVAE (Table 1). Per-epoch runtime (3.45s on ML-20M, 57.0s on MSD) is nearly identical to iALS (3.16s and 53.5s), and convergence requires a similar number of epochs. The method delivers on its central claim of excellent tail performance without sacrificing scalability.

- **Empirical validation that smoothing bandwidth is critical.** The convergence profile (Figure 5/4) shows that very small bandwidth ($h=0.01$, approximating non-smooth CVaR) causes fluctuation and poor validation performance, while very large bandwidth ($h=1e16$, effectively ERM) gives stable but suboptimal tail performance. A moderate bandwidth achieves both stability and strong semi-worst-case metrics. This provides direct evidence that smoothing is not a trick but a necessary algorithmic ingredient.

- **Efficient computational design.** The paper details two practical optimizations: (1) Gramian caching reduces per-epoch loss computation to $\mathcal{O}((|\mathcal{U}|+|\mathcal{V}|)d^2)$ avoiding materializing the full $\mathcal{O}(|\mathcal{U}||\mathcal{V}|d^2)$ matrix; (2) stochastic subsampling for the $\xi$ step with backtracking line search keeps NR iteration cost at $\mathcal{O}(|\mathcal{U}_b|L)$, independent of total user count.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **No comparison against other tail-focused recommendation methods.** The related work discusses Singh et al. (2020, CVaR-based healthiness for online recommendation), Wen et al. (2022, group DRO), and Shivaswamy et al. (2022, adversarial learning) as approaches that also target worst-case user performance. The paper states these methods "do not focus on practical scalability and rely on gradient descent" (line 318), which is a reasonable justification for exclusion given the paper's focus on scalability. However, the paper's central claim is "excellent tail performance," and some experimental evidence against at least one existing tail-focused method (even with a caveat about scalability) would substantially strengthen the empirical case. As is, the tail-performance comparison is only against methods that optimize average performance (iALS, ERM-MF, MultVAE) or a non-smooth CVaR baseline (CVaR-MF) that the paper itself shows performs poorly.

- **Evaluation uses a single CVaR level ($\alpha=0.3$).** The method is defined for any $\alpha$, and the evaluation metric also uses $\alpha=0.3$ for the tail case. There is no exploration of sensitivity to this parameter (e.g., $\alpha \in \{0.1, 0.2, 0.5\}$). While the quantile-vs-quality figures (Figure 2) show relative performance across quantile levels, the objective itself is only optimized for $\alpha=0.3$. This leaves an open question about whether SAFER effectively controls risk aversion at different levels.

- **No confidence intervals or variance reporting on main benchmark results (ML-20M, MSD).** The main results (Table 1) report single-point estimates. Robustness analysis with 50 data splits is only performed on ML-100k (the smallest dataset) and excludes two baselines (CVaR-MF and MultVAE). While single-run evaluation is standard practice in large-scale recommender system benchmarks, the lack of variance information makes it difficult to assess whether the often-modest improvements over iALS are statistically reliable.

- **GPU vs. CPU runtime comparison for MultVAE.** The paper acknowledges (line 431) that MultVAE was implemented in PyTorch on GPU while MF-based methods use multi-threaded C++ on CPU. While the paper notes this and focuses on wall-time convergence rather than per-epoch cost, the framing still risks misleading readers about relative efficiency. This does not undermine the core claim, since the main comparison of interest (SAFER vs. iALS) is fair.

### Trivial
- The paper would benefit from a discussion of how well the pointwise surrogate loss (Eq. 4) correlates with Recall for tail users, since the objective and evaluation metric differ.

## Nice-to-Haves
- An ablation study comparing SAFER with the proposed Tikhonov regularization vs. standard iALS-style regularization to clarify whether tail improvements come from CVaR or the new regularizer.
- A visual comparison of the user loss distribution for SAFER vs. iALS to illustrate reduction in the right tail.
- The evolution of dual variables $z_i$ over iterations to show how the algorithm identifies and upweights worse-off users.
- Extension to other model architectures (e.g., neural collaborative filtering) to demonstrate generality.

## Removed Points
These points are flagged to be removed; treat them with caution.
- **Robustness analysis uses only average-case Recall** — Factually wrong: the paper's robustness analysis (Section 5, Figure 4) reports performance for both $\alpha=0.3$ (tail) and $\alpha=1.0$ (average).
- **Symmetric kernel assumption needed for $z_i$ derivation** — The derivation $z_i = 1-K_h(-r_i)$ follows from the property $(\rho_1 \ast k_h)'(x) = 1-K_h(-x)$, which holds for any kernel without requiring symmetry.
- **CVaR-MF's faster per-epoch runtime undermines the computational-motivation framing** — The paper explicitly addresses this (lines 434-438): CVaR-MF requires many more epochs to converge, making SAFER faster in wall-clock time.
- **Algorithm 1 not visible** — Parser artifact; it exists in the original submission.
- **Term "safe" not defined** — The paper defines safe operationally as CVaR minimization for tail users (abstract, Section 2).
- **Tikhonov regularization "ad hoc" and "β₀ must still be tuned"** — The paper provides a condition-number-based derivation (Section 3.3); β₀ is a base-model hyperparameter, not introduced by the proposed regularization.
- **Generic strengths from Strength Finder** — Several claimed strengths (e.g., "extensive robustness analysis") were already noted above; generic phrasing without specific evidence was dropped.

## Novel Insights
The reviews do not contribute genuinely novel observations beyond the paper's own contributions. The key insight — that convolution-type smoothing of the CVaR check function enables a separable, iALS-equivalent solver — is the paper's own contribution.

## Suggestions
1. Add at least one tail-focused baseline (e.g., group DRO from Wen et al. or a simplified variant of Shivaswamy et al.'s adversarial approach) to the experimental comparison, even with a caveat about computational cost.
2. Report SAFER results at additional $\alpha$ values (0.1, 0.2, 0.5) for both training and evaluation to demonstrate control over risk aversion.
3. Add bootstrap confidence intervals or standard errors for the main benchmark results (ML-20M, MSD) to establish statistical reliability.
4. Include an ablation separating the effect of CVaR optimization from the effect of the new Tikhonov regularization scheme.

## Score and Decision

The paper makes a genuine algorithmic contribution: convolution smoothing + primal-dual splitting yields a scalable CVaR minimizer for CF with iALS-level complexity. The core claims — that this approach improves tail performance and that smoothing is essential — are supported by the experiments. However, the evaluation has notable gaps: no comparison against tail-focused baselines, single $\alpha$ value, and no variance estimates on the main results. These are addressable weaknesses, not fatal flaws. The paper should be accepted as a solid algorithmic contribution, with the understanding that further empirical validation against tail-focused methods would strengthen future versions.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>