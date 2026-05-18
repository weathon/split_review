Now I have a thorough understanding of the paper and all reviewer claims. Let me construct the consolidated review, carefully verifying each claim against the paper.

---

## Summary

This paper proposes FoRDE (First-order Repulsive Deep Ensemble), which applies particle-based variational inference (ParVI) to promote diversity in the *input-gradient space* (rather than weight or function space) among ensemble members. The authors define a kernel over input gradients of the true class, introduce a data-dependent PCA-based lengthscale selection that encourages repulsion along high-variance data dimensions, and evaluate on image classification benchmarks (CIFAR-10/100, TinyImageNet) under covariate shift. FoRDE-PCA achieves consistent improvements on corrupted benchmarks (+1.3–2.4 percentage points accuracy) over deep ensembles and other repulsive ensemble methods.

## Strengths

- **Novel and well-motivated repulsion space.** The paper clearly identifies limitations of both weight-space repulsion (inefficient due to over-parameterization) and function-space repulsion (underfitting when restricted to training inputs), and proposes input-gradient space as a principled alternative with dimensionality advantages and functional guarantees (Section 2). This conceptual contribution is supported by toy experiments showing improved uncertainty capture.

- **Consistent empirical gains across multiple corruption benchmarks.** FoRDE-PCA achieves the best cA/cNLL/cECE on CIFAR-10-C (80.5 / 0.71 / 0.07, +2.4% over next best), CIFAR-100-C (56.1 / 1.90 / 0.05, +1.3% over next best), and TinyImageNet-C. The improvements are consistent across 5 seeds and three datasets. Table 3 further shows FoRDE-PCA outperforms baselines even when those baselines use the EmpCov prior, demonstrating synergy between input-gradient repulsion and data-manifold-aware kernels.

- **Thorough baseline comparison.** The paper compares against seven baselines (weight-RDE, function-RDE, feature-RDE, LIT, node-BNNs, SWAG, DE) with multiple FoRDE variants (Identity, PCA, Tuned), all using identical architecture (ResNet18), ensemble size (10), and 5 seeds. The EmpCov-controlled experiment (Table 3) is a particularly careful design choice.

- **Transfer learning extends practical applicability.** Experiments using pretrained Vision Transformer features (Figure 5) show FoRDE outperforms baselines under both in-distribution and covariate shift, with direct measurement of functional diversity via epistemic uncertainty (last column), supporting the core diversity argument.

## Weaknesses

### Fatal
None.

### Major

- **Missing error bars on corruption metrics.** Despite averaging over 5 seeds, the tables report cA/cNLL/cECE as single values without standard errors (Tables 1–3). Clean metrics (NLL, Accuracy, ECE) include ± ranges, but the corruption metrics do not. This makes it impossible to assess whether the observed gains (e.g., 56.1 vs. 54.8 on CIFAR-100-C) are statistically significant. Given the modest margins (1.3–2.4 pp), this is a meaningful gap in presentation.

### Minor

- **Theoretical justification for the data-dependent kernel is incomplete.** The paper acknowledges (line 147–148) that the KDE approximation depends on the data distribution through the kernel, and acknowledges (lines 207–208) that mini-batching introduces biased stochastic gradients. However, it does not analyze under what conditions the gradient-flow interpretation (which relies on a standard KDE over parameter space) remains valid with this non-standard kernel. The authors state "we found no convergence issues in practice," but a theoretical discussion of whether the kernel remains positive-definite on Θ (it does, as an expectation of a PSD kernel) and whether the KDE approximation remains reasonable would strengthen the contribution.

- **The PCA-kernel connection has an unvalidated assumption.** The PCA basis is computed from the training inputs **x** (line 178), but the repulsion operates on normalized input gradients ∇_x f(x; θ)_y / ||·|| (Eq. 9). The paper argues that repelling more strongly along high-variance data directions is beneficial (lines 171–172), and connects this to the EmpCov prior (lines 190–198). However, the paper does not empirically verify that input gradient directions actually align with the PCA basis of the input data during training. A synthetic experiment or correlation analysis would strengthen this reasoning.

- **The comparison to LIT reveals the ParVI framework's standalone contribution is unclear.** FoRDE-Identity and LIT perform nearly identically on clean data (CIFAR-100: 82.1% vs. 81.9%, both 0.70 NLL) and corruption (54.1 vs. 54.4 cA). The improvement over LIT comes almost entirely from the PCA kernel. The paper's claim that FoRDE is "more flexible" than LIT (line 228) is fair (PCA kernels are not available to LIT), but it would be informative to see whether the ParVI framework itself adds anything beyond the orthogonalization objective — e.g., an ablation replacing the RBF+PCA kernel with a simple cosine repulsion in the same ParVI framework.

- **Overclaiming in specific statements.** (a) The claim that FoRDE is "the only method that exhibits high uncertainty in all input regions outside the training data" (line 319) is based on visual inspection of 2D classification figures, and the paper's own Figure 2 suggests function-RDE also shows elevated uncertainty away from data. (b) The abstract's "significantly outperforms" language (line 11) is somewhat strong relative to the modest margins (1.3–2.4 pp), especially absent error bars on corruption metrics. The paper's own discussion more cautiously states "outperforms" (line 375), which is appropriate.

- **3× computational cost vs. modest gains is not fully contextualized.** The paper transparently reports the 3× training cost (Section 3.5) and discusses it as a drawback (Section 6), but a practitioner choosing between DE and FoRDE would benefit from a more explicit cost-benefit framing (e.g., a scatter plot of accuracy vs. training time, or results for smaller ensemble sizes).

### Trivial
None.

## Nice-to-Haves

- An analysis of which corruption types (blur vs. noise vs. digital) benefit most from FoRDE-PCA could clarify the mechanism and strengthen the PCA kernel motivation.
- A sensitivity analysis of the median heuristic (trajectory of h during training, effect of different batch sizes) would improve reproducibility.
- An ensemble size ablation (e.g., M=5, 10, 20) would help calibrate the cost-benefit tradeoff.
- Reporting the tuned lengthscale weight (selected on validation) would aid reproducibility — the paper says details are in the appendix (stripped by parser).

## Removed Points

These points are flagged for removal as they violate the stated rules; treat them with caution.

- **Criticism about the "Tuned variant not fully specified":** The paper says "Details on lengthscale tuning are presented in \cref{sec:tuning_lengthscales}" (line 324). This detail is in the appendix, which is stripped by the parser. Per the rule about missing appendix content, this criticism is removed.
- **Criticism that the paper "treats the WGD update rule as unchanged":** The paper acknowledges the data-dependent nature of the kernel explicitly (line 147–148). The update rule itself is structurally the same; the change is in the kernel definition, which the paper discusses.
- **Criticism about "no discussion of repulsion strength":** The paper discusses the median heuristic which adaptively sets the global bandwidth (lines 210–214), and the kernel structure controls repulsion magnitude. This is the standard approach in SVGD-based methods and is adequately described.
- **Criticism about "no analysis of ensemble size":** This is a useful extension but not a core weakness — the paper uses a fixed ensemble size of 10, consistent with prior work.
- **Criticism that the paper should also cover more domains/tasks:** Scope-creep demands outside the paper's stated image classification focus.
- **Strength from Strength Finder about "Large and consistent gains":** "Large" is softened to "Consistent gains" in the strengths section above, as the margins are modest (1.3–2.4 pp). The core observation of consistency is kept.

## Novel Insights

None beyond the paper's own contributions. The key insight — that input-gradient space offers a sweet spot between weight-space and function-space repulsion for ParVI ensembles — is the paper's own contribution and is well-articulated.

## Suggestions

1. **Add error bars to corruption metrics.** Since results are averaged over 5 seeds, reporting standard errors for cA/cNLL/cECE is straightforward and would significantly strengthen the paper's claims about significance.
2. **Tonel down absolute language.** Replace "significantly outperforms" (abstract) with "outperforms" or "consistently outperforms" and soften the "only method" claim about toy experiments.
3. **Add a small empirical validation of the PCA-gradient alignment assumption.** Even a simple correlation analysis or a toy experiment showing that gradient directions correlate with PCA directions during training would substantially strengthen Section 3.3.
4. **Consider an ablation separating the ParVI framework from the kernel choice.** Comparing FoRDE-PCA against a version of LIT with PCA-weighted repulsion (if feasible) or against FoRDE with a cosine kernel would clarify what the ParVI machinery contributes beyond the orthogonalization objective.

## Score and Decision

The paper presents a novel, well-motivated idea with consistent empirical support across multiple benchmarks and careful baseline comparisons. The main concerns — missing error bars on corruption metrics, modest theoretical depth on the non-standard kernel, and some overclaiming — are addressable. The contribution is solid and the method is likely to be of interest to the ensemble/uncertainty estimation community.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>