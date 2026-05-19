- Decision: Reject
- Avg Score: 4.25
- Scores: 3, 6, 5, 3
Now I have verified all claims against the paper. Let me produce the final consolidated review.

## Summary

This paper proposes DMD-GEN, a metric for detecting mode collapse in time series generative models. The method extracts coherent spatiotemporal patterns via Dynamic Mode Decomposition (DMD), compares the resulting eigenvector subspaces using Grassmann manifold distances (principal angles), and aggregates these comparisons across a set of samples via Optimal Transport (Wasserstein distance). The approach is tested on one synthetic and three real-world datasets (Stock, Energy, ETTh) with three generative models (TimeGAN, TimeVAE, DiffusionTS).

---

## Strengths

1. **Novel and principled combination of tools for time series evaluation.** The idea of using DMD eigenvectors as "temporal modes," comparing them via Grassmann manifold distances (which correctly handles the fact that eigenvectors from different time series live in unaligned bases), and then aggregating via OT is genuinely novel. This is a technically sound pipeline for comparing the dynamics of multivariate time series, and the geometric grounding through principal angles is a strength over ad-hoc similarity measures.

2. **Training-free efficiency with claimed consistency to trained metrics.** The paper demonstrates (Table 1) that DMD-GEN's ranking of three generative models (DiffusionTS, TimeGAN, TimeVAE) agrees with the rankings produced by Predictive Score, Discriminative Score, and Context-FID across four datasets. Achieving this without the training overhead of these baselines is a practical advantage if the consistency holds more broadly.

3. **Controlled sensitivity analysis on synthetic data.** Section 4.5 provides a clean synthetic setup with controllable mode collapse severity (λ parameter) and shows that DMD-GEN's Perf(λ) changes systematically as λ deviates from the reference value. This is the strongest evidence that the metric responds to mode collapse in a meaningful way.

4. **Principled handling of eigenvector subspace alignment.** The paper correctly identifies that DMD eigenvectors from different time series span subspaces that are not naturally aligned, and uses Grassmann manifold distances (via principal angles) to define a geometrically meaningful distance between them. This is a theoretically well-founded choice and is a real contribution over methods that would naively compare eigenvectors element-wise.

---

## Weaknesses

### Fatal
None.

### Major

1. **Unaddressed degeneracy for univariate time series.** The sine dataset generates scalar-valued time series (y(t) is a scalar, so state dimension n=1). For n=1, the DMD operator A* is 1×1, its eigenvector is a scalar (always 1 after normalization), and the Grassmann manifold Gr(k,1) requires 1 ≤ k ≤ 1, meaning only k=1 is possible and the "subspace" is always ℝ¹ itself — making all Grassmann distances trivially zero. The paper neither acknowledges this issue nor describes any workaround (e.g., time-delay embedding via Hankel matrices, which is a standard technique in DMD for univariate signals). Since the sine dataset is used in Table 1 rankings, the validity of those results is in question. **This does not invalidate the method for the other datasets** (Stock has n=6, Energy n=28, the synthetic experiment has d=65), but it is a significant scope oversight that must be clarified.

2. **Quantitative validation of "consistency" is thin.** The paper claims DMD-GEN "consistently aligns with" baselines, but the support is limited to Table 1 showing that all four metrics agree on the best model per dataset. No rank correlation statistics (Spearman's ρ, Kendall's τ) are reported, no error bars or confidence intervals are provided, and there is no evaluation across multiple random seeds or hyperparameter configurations of the same generative model. Without a fuller characterization, the reader cannot assess whether agreement holds beyond the single best-model comparison.

3. **Interpretability claim is asserted but not demonstrated.** The paper repeatedly states that DMD-GEN provides interpretability by "pinpointing which modes have collapsed." However, the only supporting evidence is Figures 1 and 2, which show aggregate eigenvalue distributions of the full set of generated time series vs. the real set. There is no mode-by-mode analysis — e.g., showing which specific DMD eigenvectors are preserved or absent in the generated data, mapping generated modes to their closest real counterparts, or analyzing principal angles between individual real and generated mode subspaces. The interpretability advantage remains a claim, not a demonstrated capability.

### Minor

1. **No sensitivity analysis for the number of retained modes k.** The metric depends on selecting k (the number of DMD eigenvectors retained). Spurious, including for clean periodic data where the intrinsic rank may be low. The paper does not report which k was used in experiments nor study how the metric's rankings change with k. This is a free parameter whose influence is unexamined.

2. **"New definition of mode collapse" is overstated as a contribution.** The paper's first listed contribution is a "New Definition of Mode Collapse for Time Series," but what is actually provided is an operationalization: modes are DMD eigenvectors, and collapse is a large OT distance between mode sets. This is a measurement framework, not a conceptual definition. This is a relatively minor framing issue but inflates the contribution.

3. **Missing hyperparameter details and limitations discussion.** The paper does not report the DMD rank r used, the specific k value, or details of how the OT problem was solved (exact vs. approximate solver). There is also no discussion of when DMD might fail (noisy data, very short sequences, non-stationary dynamics, or systems with strong nonlinearities that violate the local linearity assumption).

### Trivial
None.

---

## Nice-to-Haves

- If the method is intended to work on univariate time series, incorporating time-delay embedding (Hankel matrix construction) would lift the dimension and make the Grassmann distance meaningful. This is a natural extension from the DMD literature.
- A runtime/complexity comparison against the training-requiring baselines would strengthen the efficiency claim.
- An ablation showing the contribution of each component (DMD → Grassmann → OT) would clarify which piece adds the most value.

---

## Removed Points

- **"Tables are garbled / unreadable"** — removed because this is a PDF extraction artifact, not a paper problem.
- **"Algorithm 1 is missing"** — removed; algorithms often appear in appendices which are stripped by the parser.
- **"Section 2.1 doesn't reference prior attempts to define modes"** — removed as factually incorrect; the paper cites Lin et al. (2020) and DC-GAN in that section.
- **"Predictive/Discriminative score behavior is unexplained for synthetic experiment"** — weakened to minor point about missing limitations; the paper does explain the Perf(λ) formulation.
- **"Missing related works"** — removed per instruction (cannot verify existence of external works).
- **Generic formatting/style nitpicks** — removed.
- **Strength Finder's generic/unsupported strengths** (e.g., "this paper addressed an important problem") — removed.
- **Strength Finder's claim that Figures 1-2 provide interpretability** — kept only as a qualified strength (the figures show eigenvalue distributions, not mode-by-mode interpretability), since the weakness (#3 above) supersedes the overclaim.

---

## Novel Insights

None beyond the paper's own contributions.

---

## Suggestions

1. **Clarify the regime of validity.** State explicitly that DMD-GEN requires the time series state dimension n ≥ k (number of retained modes). For datasets where n is small or n=1, either (a) provide a time-delay embedding procedure to lift the dimension, or (b) acknowledge that the metric currently applies only to multivariate data and remove/qualify the sine dataset results.

2. **Strengthen the quantitative validation.** Compute rank correlation (Spearman's ρ or Kendall's τ) between DMD-GEN and each baseline across multiple configurations or random seeds of the same generative model. Include error bars or confidence intervals. Show the full ranking, not just the top model.

3. **Demonstrate interpretability concretely.** Take one trained generative model and show a mode-by-mode comparison: for each of the k retained DMD eigenvectors, compute the principal angle to the closest real-mode subspace, and identify which dynamic patterns are well-preserved and which are missing. This would substantiate the "pinpointing" claim.

4. **Report sensitivity to k.** Show the metric's rankings for a range of k values (e.g., k = 2, 4, 8, 16) to establish robustness, or provide a principled criterion for choosing k.

5. **Add a limitations section** that discusses edge cases (univariate data, noisy sequences, short time series, non-stationary dynamics) honestly.

---
