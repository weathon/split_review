## Summary

This paper introduces the Marginal Fairness Sliced Wasserstein Barycenter (MFSWB) problem, which seeks a barycenter that is approximately equidistant from all input marginals—a formulation novel to the Wasserstein barycenter literature. To overcome computational difficulties of the formal constrained definition (intractable gradient, O(K²) complexity, sensitivity to a Lagrange multiplier λ), the authors propose three hyperparameter-free surrogate objectives (s-MFSWB, us-MFSWB, es-MFSWB) with a proven theoretical hierarchy (s-MFSWB ≤ us-MFSWB ≤ es-MFSWB), and connect them to a newly-defined variant of Sliced Multi-marginal Wasserstein distance with maximal ground metric. Experiments on Gaussian simulation, 3D point-cloud averaging, color harmonization, and fair sliced Wasserstein autoencoder show that the surrogates improve fairness over uniform-weighted SWB.

## Strengths

- **Novel problem formulation with honest treatment of its challenges.** Definition 1 formalizes marginal fairness as a constrained barycenter problem, and the paper openly discusses its computational drawbacks (admissible ε, λ tuning, biased gradient, O(K²) complexity) rather than glossing over them. This motivates the surrogate approach in a principled way.

- **Clean theoretical hierarchy linking the three surrogates.** Propositions 1–3 establish s-MFSWB ≤ us-MFSWB ≤ es-MFSWB, so optimizing any surrogate implicitly benefits the others. Proposition 2 provides a finite-sample O(L^{−1/2}) bound on the gradient estimation error for us-MFSWB, giving practitioners a concrete rate.

- **Hyperparameter-free and O(K) scalable surrogates.** Unlike the formal MFSWB dual objective which requires tuning λ and scales O(K²), all three surrogates require no λ tuning and have O(K) complexity in the number of marginals (Section 3.2, lines 215–216), making them directly usable.

- **SMW with maximal ground metric as a new theoretical object.** Proposition 4 shows this variant satisfies non-negativity, marginal exchangeability, generalized triangle inequality, and identity of indiscernibles. The paper correctly notes this is a new definition introduced as part of the analysis.

- **Consistent empirical improvement in fairness across tasks.** The surrogates consistently achieve lower F-metric than uniform SWB across Gaussian simulation (K=4), point-cloud averaging (K=2), color harmonization (K=2), and SWAE (K=10). In the point-cloud task, es-MFSWB outperforms even formal MFSWB with all three tried λ values.

## Weaknesses

### Fatal
None.

### Major

- **Insufficient multi-marginal forward barycenter evaluation for the paper's central claim.** The paper claims the surrogates yield fair barycenters for "many marginals," yet only one forward barycenter experiment uses K > 2: the Gaussian simulation (K=4), which uses simple 2D Gaussians. The point-cloud averaging (K=2) and color harmonization (K=2) do not stress-test the behavior with many marginals. The SWAE experiment (K=10) is an inverse barycenter problem (the "barycenter" μ₀ is fixed, marginals are learned), which is structurally different from the forward problem. Experiments with K ∈ {5, 10, 20} on real forward barycenter tasks (e.g., averaging multiple point-cloud shapes) would be needed to substantiate the core claim that the surrogates scale appropriately to many marginals. *(Note: the harsh critic incorrectly claimed the Gaussian simulation does not exist — it does, with K=4 — but this does not resolve the overall concern.)*

- **The formal MFSWB baseline is undertuned, weakening the comparison.** The paper evaluates the formal MFSWB dual objective with only three λ values (0.1, 1, 10), then concludes the surrogates are preferable because the formal MFSWB is "sensitive" to λ. This is insufficient: a proper λ sweep (e.g., 15–20 values on a log scale) or Pareto frontier analysis would be needed to determine whether a well-tuned λ can match the surrogates. The paper's conclusion rests on evidence from an undertuned baseline.

- **Proposition 5 provides a weak theoretical foundation for the surrogates.** The proposition states that the minimizer of us-MFSWB provides a *lower bound* on SMW with maximal ground metric. Minimizing a lower bound of a function is not equivalent to minimizing that function, and the argmin of the lower bound can be arbitrarily far from the argmin of the target. The paper's language ("could try to minimize," "can help to understand") is appropriately cautious, but the connection adds little theoretical weight. This is not a flaw in the paper's core methodology but reflects an overclaim in the contribution list (contribution 3).

### Minor

- **No analysis of s-MFSWB gradient bias magnitude.** The paper correctly notes the Monte Carlo argmax estimator for s-MFSWB is biased (line 153) but provides no empirical quantification. An ablation comparing s-MFSWB with a version using much larger L (e.g., L=10,000) for the argmax selection would clarify whether the bias is practically meaningful.

- **Caveat to us-MFSWB unbiasedness not discussed.** The unbiasedness claim (via Danskin's theorem) requires the argmax to be unique. When multiple marginals produce equal 1D Wasserstein distances for a given θ, the subdifferential is set-valued. This is a standard technical caveat but is not acknowledged.

- **Statistical significance not reported.** The point-cloud experiment reports three runs (line 271) but no variances or confidence intervals. The SWAE results are described qualitatively ("varies slightly across runs," "minor differences in performance order"). Standard errors would strengthen the empirical claims.

- **No comparison with reweighted barycenters as a baseline.** The most natural alternative to a fairness-constrained barycenter is to adjust the marginal weights ω_k (e.g., solving a minimax over both μ and ω to equalize distances). This baseline is not considered.

- **The sorting non-differentiability issue in SW gradients is not discussed.** The gradient formula (Equation 4) depends on sorting operations that are non-differentiable at ordering-change points. This is a known issue in the sliced Wasserstein literature, but given that the paper makes claims about unbiased gradient estimation, it should at least acknowledge the subgradient caveat.

### Trivial
None.

## Nice-to-Haves

- A λ sweep (15–20 values on a log scale) for the formal MFSWB baseline, showing a Pareto frontier of (F, W) trade-offs and where the surrogates fall relative to it, would significantly strengthen the paper.
- An explicit discussion of failure modes (e.g., s-MFSWB focusing only on the farthest marginal, potentially degrading distances to others) would improve scoping.

## Removed Points

- **"Only experiment with K > 2 is SWAE"** — Factually wrong. The Gaussian simulation (Section 4.1) uses K=4 marginals. The broader concern about limited multi-marginal evaluation is retained in Major weaknesses but corrected.
- **"Table 2 content not parseable"** — PDF parsing artifact. The table content is present as an embedded image; not an author error.
- **"The paper claims 'no prior work' may overstate novelty"** — The fairness approach (minimax) is structurally similar to Fair PCA, which the paper itself cites. However, applying it to the barycenter setting is genuinely novel, and the paper explicitly acknowledges the Fair PCA connection. This is a scope-creep criticism.
- **"Equation 4 non-differentiability at sorting boundaries"** — Retained as a Minor weakness (since it's a known SW issue), but the harsh critic's framing as a major gap is removed. Most SW papers do not address this in depth.

## Novel Insights

None beyond the paper's own contributions. The reviews reaffirm the paper's core contribution (novel fairness-aware barycenter formulation with tractable surrogates) but do not surface any deeper insight beyond what the paper already provides.

## Suggestions

1. **Add a forward barycenter experiment with K ≥ 5 real marginals** (e.g., averaging 5–10 point-cloud shapes from ShapeNet). Report F-metric and W-metric trajectories and show whether the surrogates equalize distances as expected. This is the single highest-leverage improvement.

2. **Run a proper λ sweep for formal MFSWB** (15–20 values on a log scale) across the point-cloud and color harmonization tasks, and present the Pareto frontier. This determines whether the surrogates genuinely outperform a well-configured formal MFSWB or merely an undertuned one.

3. **Quantify the s-MFSWB gradient bias** with a controlled experiment comparing s-MFSWB at standard L against a version using L=10,000 for the argmax selection.

4. **Tone down the Proposition 5 claim** (contribution 3) from "connection to SMW" to more clearly acknowledge that a lower-bound relationship does not guarantee the minimizer of the bound aligns with the minimizer of the target.

5. **Report standard errors or confidence intervals** for the main experimental results.

## Score and Decision

The paper addresses a genuine and underexplored problem with a clean theoretical hierarchy and sensible surrogate formulations. The surrogates are well-motivated, hyperparameter-free, and O(K) scalable. However, the experimental evaluation substantially lags the contribution: most forward barycenter experiments use only K=2 marginals, and the formal MFSWB baseline is compared with only three λ values. The Proposition 5 theoretical connection is too weak to carry weight. These gaps do not invalidate the core ideas, but they mean the paper's central claim — that the surrogates yield fair barycenters for many marginals — is not yet convincingly demonstrated. The paper would need stronger multi-marginal forward-barycenter experiments and a fairer baseline comparison to meet the acceptance bar.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>