## Summary

This paper proposes STNAdam, a stochastic optimization algorithm for "nonconvex + weakly-convex" composite problems that introduces a two-track iteration framework — an extrapolation track and a regular update track governed by Nesterov momentum and Adam-style adaptive conditioning. The algorithm supports multiple variance-reduced gradient estimators (SGD, SAGA, SARAH) through a unified interface, schedules hyperparameters within proof-derived finite intervals, and provides convergence analysis under the Kurdyka-Łojasiewicz property with explicit rates. The empirical evaluation is on a low-light image enhancement (LIE) task using the LOL dataset.

## Strengths
- **Novel two-track algorithmic framework**: The STNAdam algorithm (Algorithm 1) maintains three distinct iterates — \(x^{k+1}\) (Adam-style regular update using fixed step size \(\alpha\)), \(\bar{x}^{k+1}\) (extrapolation track as convex combination of \(x^k\) and \(\tilde{x}^k\)), and \(\tilde{x}^{k+1}\) (Nesterov-accelerated update using \(\tilde{\varpi}^{k+1}\) and adaptive step size \(\alpha_{k+1}\)) — forming coupled two-track dynamics absent from single-track methods like NAdam or SNAdam. The structural differentiation from prior work is clear and genuinely novel.
- **Complete multi-step convergence proof under KL with explicit rates**: The convergence analysis constructs a carefully designed energy function \(G^k\) (equation 9) that accounts for coupled two-track dynamics, stochastic variance, and adaptive step sizes. Lemma 2 establishes expected decrease with eight nonnegative descent terms, Theorem 1 derives the finite-length property, and Theorem 2 delivers explicit convergence rates separated into three regimes based on the KL exponent \(\vartheta\) — linear for \(\vartheta \in (0, 1/2]\), sublinear \(O(k^{-(1-\vartheta)/(2\vartheta-1)})\) for \(\vartheta \in (1/2, 1)\), and finite termination for \(\vartheta = 0\).
- **Unified variance-reduction interface**: Lemma 1 abstracts the variance-reduced gradient estimator requirements into a mean-squared-error bound, geometric decay, and convergence condition, verified concretely for SGD, SAGA, and SARAH. This modular design allows the theory to cover all three estimators simultaneously without separate analyses.
- **Analysis-driven parameter scheduling**: The feasible intervals for \(\gamma_{k+1}\), \(\lambda_{k+1}\), and \(\alpha_{k+1}\) (equations 6-8) are derived directly from the convergence proof rather than heuristically set, and Remark 3 verifies the lower bounds stay bounded away from zero under mild conditions.

## Weaknesses

### Fatal
None.

### Major
- **The two-track mechanism is not cleanly ablated**: The paper's headline contribution is the two-track framework, but the experiments compare STNAdam variants (which differ in gradient estimator) against baselines (SGD, SAdam, SNAdam) that lack the two-track structure entirely. While STNAdam-SGD vs. SGD partially isolates the two-track (both use the same SGD gradient estimator), the two-track is confounded with the adaptive parameter scheduling and Nesterov-style momentum correction \(\tilde{\varpi}^{k+1}\). Without a comparison against a single-track variant using the same gradient estimator and parameter scheduling, the core contribution's causal role in the observed improvements remains unverified. This goes to whether the central thesis is substantiated.
- **Empirical evaluation is confined to a single narrow task**: The paper motivates STNAdam with references to deep learning challenges (massive network parameters, datasets, training dynamics) and frames it as a general-purpose optimizer for "nonconvex + weakly-convex" composite problems. Yet the entire empirical evaluation is a single task — low-light image enhancement on the LOL dataset using a hand-crafted Retinex-style model (14), which is not a learned neural network. A new optimizer submitted to ICLR would typically be evaluated across multiple domains to demonstrate generality. The results could be largely explained by task-specific tuning rather than algorithmic superiority.
- **Theory and experiments are disconnected**: The convergence analysis assumes the KL property on \(\Phi\), a proximal-friendly weakly-convex \(g\), and variance-reduced estimators satisfying Lemma 1's conditions. The LIE model uses \(g(R,L) = h\|\nabla L\|_{1/2}^{1/2} + \ell\|\text{NN}_i(R)\|_*\). The paper never establishes that this \(g\) satisfies the KL property, that its proximal operators are tractably computable (\(\ell_{1/2}\) and nuclear norm proximals are nontrivial), or that the variance-reduced estimators satisfy Lemma 1's conditions in this setting. The theoretical results guarantee convergence to a stationary point, while the empirical metric is image quality (PSNR, SSIM, LPIPS) — no connection is drawn between these two types of outcomes.

### Minor
- **"Removing hand-tuning" claim is overstated**: The parameter intervals (6)-(8) depend on unknown problem constants — the Lipschitz modulus \(L\), weak-convexity modulus \(\tau\), variance-reduction constants \(V_1, V_T, \rho\), and auxiliary parameters \(M, s\). In practice, users must estimate or tune these. The claim that dynamic scheduling "removes hand-tuning" (line 48) is misleading; it shifts the tuning burden to interval-bound parameters that are equally opaque.
- **Unclear time reporting**: The time values (~2-8 × 10⁻⁵ seconds) in Tables 2-3 are implausibly small for full image enhancement and are likely per-iteration times, but this is not stated anywhere.
- **SAdam citation is incorrect**: Line 281 and Table 2 attribute SAdam to "(Kingma & Ba, 2014)," which is the Adam paper, not SAdam. The SAdam baseline's actual provenance is unclear.
- **No error bars or multiple-run statistics**: Results are reported as single numbers without variance estimates or any description of hyperparameter tuning protocols for baselines.
- **Table 3 uses only two images** ("Wardrobe" and "Doll"), which is insufficient for meaningful statistical conclusions about joint denoising performance.

### Trivial
None.

## Nice-to-Haves
- Add an ablation comparing STNAdam against a single-track variant (e.g., NAdam with the same variance-reduced estimator and adaptive scheduling) to isolate the two-track contribution.
- Add at least one standard optimization benchmark (e.g., training a small CNN on CIFAR-10) to demonstrate generality beyond the single LIE task.
- Verify that the LIE model (14) satisfies the KL property, or add a synthetic experiment where all theoretical conditions are verifiably satisfied.
- Report optimization traces (e.g., subgradient norm vs. iteration) alongside image quality metrics to bridge theory and experiments.
- Include a limitations section discussing doubled per-iteration proximal cost, dependence on unknown constants, and settings where the two-track approach may not help.

## Removed Points
These points are flagged to be removed, treat them with caution:
- **"Teleman & Hinton (2012)" typo**: This is a trivial formatting/spelling issue (should be "Tieleman"). Removed per formatting nitpick rule.
- **SAdam strong convexity vs. nonconvex+convex inconsistency claim**: The harsh critic claimed inconsistency between line 13 and line 33 regarding SAdam. The paper correctly distinguishes: Wang et al. (2019) originally proposed SAdam for strongly convex problems; Le-Duc et al. (2024) extended it to "nonconvex + convex." No actual inconsistency exists. Removed as a misreading.
- **Figure 1 being "entirely qualitative"**: Qualitative illustration of an iterative scheme via a trajectory figure is standard in optimization papers. Removed as a presentation nitpick.
- **"Nesterov aspect limited to momentum correction" — gradient not evaluated at extrapolated point**: The harsh critic claimed the two-track is not a true Nesterov lookahead because the gradient is evaluated only at \(x^k\). This is a misunderstanding: Nesterov momentum in Adam-style methods (NAdam) also evaluates the gradient at the current point and applies momentum correction. The extrapolation in STNAdam serves a different role from classical NAG lookahead. Removed as a misunderstanding.
- **Demand for full hyperparameter tuning protocols and complete training logs**: These are standard reproducibility requests but impractical to include in full detail for a paper submission. The absence of error bars (kept as minor) is the substantive residue.
- **Criticism about comparing with LIE-specific algorithms being "apples-to-oranges"**: The paper clearly separates generic optimizers from LIE-specific algorithms in the tables and discussion. Comparing different methods that solve the same task is standard practice. Removed.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
- The single highest-impact revision would be to add an ablation experiment comparing STNAdam against a single-track variant (e.g., NAdam with the same variance-reduced estimator and adaptive scheduling), which would directly test whether the two-track structure drives the observed improvements.
- Consider reframing the empirical contribution more modestly — as evidence that STNAdam works well for LIE specifically — rather than claiming broad generality that the experiments do not support. Alternatively, add experiments on standard deep learning benchmarks.
- Bridge theory and experiments by plotting optimization-theoretic quantities (e.g., estimated subgradient norm) alongside image quality metrics during training, showing that theoretical convergence translates to practical performance.

## Calibration Anchors

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| Federated Composition Optimization | Og7ZZd7hDm | 3.25 | R1 (weak) | STNAdam is stronger: more novel algorithm, better experiments, sounder theory |
| Adam Convergence Non-uniform Smoothness | mEBSeSk49H | 4.25 | R1 (weak) | STNAdam is stronger: fewer mathematical errors, more complete theory, plus has empirical results |
| isPPA Tight Convergence | n3TkrH7fEr | 6.25 | R1 (mid) | STNAdam is weaker: isPPA has tight theory-experiment connection and validated convergence rates |
| Tight Lower Bounds | fMTPkDEhLQ | 8.00 | R1 (strong) | STNAdam is much weaker — different league entirely |
| Unified SPPM Theory | AqHbMV28o7 | 4.50 | R2 (narrow) | STNAdam is comparable/stronger: more novel algorithm and more realistic experiments than toy linear regression |
| NGN-M Momentum Adaptation | CYa4FKjYM9 | 6.00 | R2 (narrow) | STNAdam is weaker: NGN-M has proper deep learning benchmarks (CIFAR-10/100, ImageNet, ViT) |
| Memory-Augmented Adam | 6rEcB9m9AI | 4.75 | R2 (narrow) | Comparable: similar novelty level, STNAdam has stronger theory but much narrower experiments |

**Round 1 bracket**: 4.5 – 6.0.  
**Round 2 narrowing**: The 4.50 SPPM paper (toy experiments only) is weaker than STNAdam; the 6.00 NGN-M paper (proper deep learning benchmarks) is stronger. The 4.75 memory-augmented Adam paper has comparable algorithmic novelty but substantially broader empirical evaluation (ImageNet, CIFAR, PTB). STNAdam lands at 4.5 — the narrow empirical evaluation (single task, hand-crafted model) and theory-experiment disconnect place it below borderline for a paper claiming a general-purpose optimizer.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>