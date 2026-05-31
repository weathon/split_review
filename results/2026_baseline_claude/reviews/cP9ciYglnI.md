## Summary

This paper presents a shape-adaptive guidance signal for interactive cortical sulcal labeling on spherical representations of the cortical surface. The core contribution is the Weighted Geodesic Distance Transform (WGDT), which encodes user click interactions by solving the eikonal equation with a curvature-based propagation speed function so that the signal spreads faster along sulcal valleys and slower along gyral ridges. The approach is validated on 72 HCP subjects with 17 manually labeled sulci in the lateral prefrontal cortex (LPFC), demonstrating that a single WGDT-guided click outperforms fully automatic labeling methods and equidistance-based encoding schemes, particularly for small and variable sulci.

---

## Strengths

- **Principled and novel signal design.** Encoding user guidance via the eikonal equation with a curvature-derived speed function is a genuinely novel idea for interactive segmentation on cortical surfaces. The connection between anatomical structure (mean curvature), wavefront propagation, and model attention is coherent and well-motivated. No prior work has combined structure-aware signal encoding on the spherical domain for interactive cortical labeling.

- **Statistically rigorous evaluation.** The evaluation uses 5-fold cross-validation, 10 initial click locations per subject to reduce stochasticity, paired t-tests with FDR correction across 17 ROIs, and Dice scores broken down per sulcus. This gives a principled view of performance gains rather than aggregate averages masking per-region variability.

- **Clear performance advantage for the targeted regime.** Figures 4 and 5 show consistent, statistically significant improvements of WGDT over ADT and Disk signals across all 9 small and variable sulci (adjusted p < 0.05), and over fully automatic baselines in most sulci with only one click. The qualitative visualizations in Figure 6 corroborate the quantitative results.

- **Practical runtime.** Sub-500 ms per click (including signal encoding, re-tessellation, and forward pass) for surfaces of 100k–170k vertices confirms the method is suitable for real interactive annotation workflows.

- **Honest discussion of limitations.** The paper explicitly acknowledges the single-region scope, hyperparameter sensitivity of k and σ, and the per-sulcus training paradigm as open issues.

---

## Weaknesses

### Fatal
None.

### Major

1. **Small dataset and single brain region.** Validation on 72 subjects (≈14 per fold) from a single HCP cohort and restricted to the left LPFC substantially limits the generalization evidence. Sulci in other cortical regions (e.g., temporal, occipital) may have different curvature characteristics, and the curvature-based speed function may need re-tuning or may not generalize. The paper's own conclusion flags this but does not empirically explore it.

2. **No quantitative comparison with traditional interactive mesh baselines.** The paper introduces graph cuts and harmonic fields as traditional alternatives in the introduction, but excludes them from the quantitative evaluation, citing their design limitations. Even a coarse numerical comparison would have clarified where the learning-based spherical approach gains over classical interactive methods and would give readers a fuller picture of the landscape.

3. **Per-sulcus model training is a scalability concern that is underexplored.** Training 17 separate models—one per sulcus—avoids the known challenges of multi-label interactive segmentation but at a significant cost in training time and storage. The paper does not report training runtimes or discuss how this scales to other regions with many more sulci (e.g., the full cortical surface). For a practical tool, this is a meaningful barrier.

### Minor

1. **Curvature-only ablation is missing.** The paper compares WGDT against angular-distance baselines (ADT, Disk), but does not isolate the role of the curvature signal specifically—for example, by testing a geodesic distance transform that uses random or uniform speed (removing curvature) but is otherwise identical. This would more cleanly attribute the gain to the curvature signal rather than to the eikonal framework itself.

2. **Click simulation may not reflect real annotator behavior.** The simulated clicks always target the largest mislabeled connected component. Real raters may correct different errors in different orders. A user study or at least an analysis of performance sensitivity to click placement would strengthen the claim of practical utility.

3. **Large k performance degradation is unexplained.** The paper observes that large k limits the benefit of additional clicks but does not offer an explanatory analysis. Understanding why broader signals reduce the marginal value of subsequent clicks would inform the hyperparameter guidance.

### Trivial
None beyond parser artifacts in the extracted text.

---

## Nice-to-Haves

- A unified multi-sulcus model (even as a secondary experiment) would substantially increase the practical appeal and scalability of the method.
- Reporting inter-rater agreement on the manual LPFC labels would contextualize the Dice scores—a model that approaches or exceeds inter-rater agreement is arguably sufficient.
- Analysis of failure cases where WGDT degrades (e.g., pathological anatomy or noisy curvature estimates) would help practitioners understand robustness boundaries.

---

## Novel Insights

The paper's most genuinely novel observation is that the *encoding strategy for user guidance signals*—not just the backbone model—is a first-class design variable in interactive segmentation on non-Euclidean surfaces. By demonstrating that a curvature-aware eikonal propagation systematically outperforms isotropic distance signals (especially under minimal supervision, i.e., a single click), the paper shows that shape-awareness injected into the input signal can compensate for inherent expressivity limitations of rotation-equivariant spherical CNNs. This insight has implications beyond cortical sulcal labeling: any interactive segmentation framework on structured surfaces (e.g., cardiac meshes, retinal surfaces) could benefit from replacing isotropic guidance signals with geometry-informed eikonal propagation.

---

## Suggestions

- Report training time for all 17 per-sulcus models and discuss strategies (e.g., shared encoder) to reduce this burden.
- Add a control WGDT variant with uniform speed (i.e., k = 0, equivalent to geodesic distance on the sphere) to isolate the curvature contribution from the eikonal framework.
- Consider reporting results on at least one additional hemisphere or brain region (even as preliminary experiments) to begin addressing the single-region generalization concern.
- Provide a concrete protocol or heuristic for selecting k and σ so practitioners can apply the method without exhaustive grid search.

---

## Score and Decision

The paper makes a targeted but technically sound and novel contribution to interactive mesh segmentation for neuroimaging. The WGDT signal is a principled design choice with strong experimental support, the evaluation methodology is rigorous for the dataset scale, and the practical runtime is appropriate. The main limitations—small cohort, single region, and absent curvature ablation—are real but do not invalidate the core claims. This sits at a solid borderline accept.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>