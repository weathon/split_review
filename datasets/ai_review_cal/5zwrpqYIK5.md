- Decision: Reject
- Avg Score: 3.50
- Scores: 5, 3, 3, 3
Now I have a thorough understanding of the paper. Let me synthesize the final review.

## Summary
The paper formulates Outlier-Robust Orthogonal Regression (OR²) on manifolds — an ℓ¹ minimization problem over a smooth manifold to find a vector orthogonal to as many data points as possible. It extends ℓ¹ orthogonal regression (previously studied only on the unit sphere) to arbitrary submanifolds of the sphere, motivated by geometric vision problems where manifold constraints are inherent (e.g., essential matrix, rotations). The main contributions are: (i) recovery guarantees (Theorems 1–3) based on novel geometric quantities that capture the interplay between data and manifold, which can succeed even when inliers are skewed — a setting where prior sphere-based theory fails; (ii) convergence guarantees for a Riemannian subgradient method (linear rate, Theorem 4) and an iteratively reweighted least squares method (sub-linear rate to a Huber surrogate, Theorem 5); and (iii) synthetic experiments on robust essential matrix estimation showing that enforcing the manifold constraint yields better robustness than the sphere relaxation.

## Strengths
- **Recovery guarantees that handle skewed inliers — a genuine theoretical advance.** Prior ℓ¹ orthogonal regression theory (e.g., Zhu et al. 2018) required inliers to be uniformly distributed in the true hyperplane, a condition violated in geometric vision applications (Example 1). The paper introduces manifold-aware quantities \(c_{\mathrm{in}}, \gamma_{\mathrm{in},\theta}\) and shows (Theorems 1–3) that the manifold constraint itself can compensate for non-uniform inlier skew, provided the manifold is appropriately "posed" relative to the inlier distribution. This is a novel and well-motivated theoretical insight.
- **Unified framework covering a broad class of applications.** The paper casts robust subspace recovery, rotation search (SO(3)), essential matrix estimation, fixed-rank matrix sensing, and trifocal tensor estimation as instances of (OR²-ℓ¹), providing a common theoretical and algorithmic lens that was missing in prior work.
- **First convergence guarantee for IRLS on manifolds for (OR²-ℓ¹).** Theorem 5 proves sub-linear convergence of the IRLS algorithm to a critical point of a Huber-type surrogate. As the paper notes, this has not been shown in the literature even for particular instances. The extension of Hong et al. (2017)'s convex analysis to non-convex manifolds is a technical contribution.
- **Synthetic experiments confirm the core empirical claim.** Figure 4 shows that OR² on the essential manifold consistently outperforms DPCP (sphere relaxation) as outlier ratios increase. For \(L=200\) at 50% outliers, OR² yields sub-1° errors while DPCP already shows 7.8° rotation error. The improvement is visible and consistent across settings.

## Weaknesses

### Fatal
None.

### Major
- **Empirical validation is limited to synthetic data with a single baseline.** The main experiment (§5) uses only synthetic random scenes (following Kneip & Furgale 2014), compares against only one baseline (DPCP), and evaluates only the IRLS variant (not RSGM). No real-world datasets (e.g., KITTI, NIST essential matrix dataset) are included. While the paper's primary contribution is theoretical, the abstract claims that experiments "demonstrate" the robustness benefit — a claim that would be substantially strengthened by validation on real data with additional baselines. The lack of runtime comparisons is also notable, since the SDP-based weighted least squares step for OR² is presumably more expensive than the SVD-based step for DPCP.

### Minor
- **IRLS convergence guarantee is for the Huber surrogate, not the ℓ¹ objective.** Theorem 5 proves convergence to a critical point of a smoothed (Huber) objective, not directly (OR²-ℓ¹). The paper transparently states this and notes that the Huber loss tends to ℓ¹ as \(\delta\to0\), but provides no bound on how close critical points of the two problems are. This partially decouples the theoretical guarantee from the motivating formulation.
- **The geometric quantities in §4.1 are not directly computable** — a limitation the paper explicitly acknowledges in §6. While this does not invalidate the theoretical analysis, it means the conditions in Theorems 1–3 cannot be verified or used to guide parameter choices in practice without further development (e.g., probabilistic bounds).
- **No experimental comparison between RSGM and IRLS** is provided. The paper proposes two algorithms with different computational oracles but evaluates only one of them, leaving practitioners without guidance on which to prefer.
- **No discussion of initialization strategy for RSGM.** Theorem 4 requires initialization in a neighborhood of \(b^*\) of size \(s/c_2\), but the paper does not discuss how such an initialization might be obtained in practice (e.g., spectral or random sampling).

### Trivial
- **The additive constant \(D\) in the definition of \(\bar{\eta}_{\mathrm{out}}\)** (line after eq. 14) is introduced without justification, somewhat breaking the flow of the otherwise clearly motivated geometric quantities.

## Nice-to-Haves
- Real-world experiments on a standard benchmark (e.g., KITTI visual odometry) would substantially strengthen the empirical claim.
- A bound on the distance between critical points of (OR²-Huber) and (OR²-ℓ¹) as \(\delta\to0\) would tighten the link between Theorem 5 and the paper's main formulation.
- A concrete, simplified corollary of Theorems 1–3 for a specific manifold (e.g., the essential manifold) would help readers interpret the abstract conditions.

## Removed Points
These points were raised by the reviewers but are removed for the reasons stated:
- **Criticism about missing RANSAC baselines.** RANSAC is a fundamentally different (sampling-based) paradigm; comparing against it would be natural for an applied paper but is not required for a theoretical contribution whose baseline is the strongest continuous-optimization method (DPCP). This is scope creep.
- **Criticism that Theorem 4's conditions are not stated in the main text.** The conditions may appear in the appendix (stripped by the PDF parser); the rule is to not penalize missing appendix content.
- **Criticism about missing retraction/projection maps for specific manifolds.** The paper provides a concrete sphere example and correctly notes these are standard Riemannian optimization primitives. A general framework paper is not required to list every implementation detail.
- **Criticism about "no discussion of noisy inliers."** The paper's assumptions are clearly stated; handling noise is a reasonable future extension but not a current flaw.
- **Various generic formatting and style nitpicks** from the harsh critic's section-by-section notes that do not identify concrete errors.
- **Strength Finder strengths that are generic or sycophantic** (e.g., "identifies limitations and future directions" — this is standard practice, not a distinguishing strength).

## Novel Insights
None beyond the paper's own contributions. The reviewer inputs did not surface additional observations that the paper itself does not already articulate. The key synthesis is that the theoretical framework is solid and novel, while the empirical validation is the paper's main gap.

## Suggestions
1. **Add real-data experiments** — even a small-scale test on a standard benchmark (e.g., KITTI) would substantially elevate the credibility of the empirical claim and allow comparison with RANSAC variants that dominate in practice.
2. **Characterize the IRLS objective gap** — prove or at least bound the distance between critical points of (OR²-Huber) and (OR²-ℓ¹) as \(\delta\to0\), or reframe IRLS as targeting the Huber objective directly.
3. **Add a concrete corollary** — instantiate Theorems 1–3 for a specific manifold (e.g., the essential manifold) under a simplified data model to illustrate when the conditions can be met.
4. **Report error bars** for the synthetic experiments across trials to convey reliability.
5. **Include RSGM results** in experiments to benchmark the two proposed algorithms.
