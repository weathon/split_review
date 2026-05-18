Now I have everything I need. Let me compose the final consolidated review.

---

## Summary

This paper introduces CONDA, the first test-time adaptation (TTA) framework for concept bottleneck models (CBMs) paired with foundation model backbones. It formally categorizes distribution shifts into low-level and concept-level shifts, identifies three corresponding failure modes, and proposes three adaptation stages (concept-score alignment, linear probing adaptation, and a residual concept bottleneck) to address them. Experiments on five datasets with multiple backbones and CBM construction methods show accuracy improvements of up to 28% over unadapted CBMs, often approaching parity with non-interpretable classifiers.

## Strengths

- **First TTA framework for CBMs with foundation models.** The paper correctly identifies that existing TTA methods target non-interpretable classifiers, and that CBMs suffer from unique failure modes under distribution shifts that no prior method addresses. This is a genuinely novel problem formulation. (Lines 37–39, Section 1 contributions.)

- **Principled component design grounded in failure-mode analysis.** Each adaptation stage (CSA, LPA, RCB) is motivated by a specific failure mode identified in Section 2.3. The component analysis in Figure 3 validates the design: CSA dominates under low-level shifts, while LPA and RCB are key under concept-level shifts. This goes beyond a black-box method and provides structural insight.

- **Strong empirical gains with thorough evaluation scope.** CONDA improves accuracy by up to 28% (Waterbirds, PCBM AVG: 14.00% → 42.00%) and the evaluation covers 5 datasets, 3 foundation models (CLIP variants and BioMedCLIP), and 3 CBM construction methods (Yuksekgonul et al., Yeh et al., Oikarinen et al.), showing meaningful generalizability.

- **Component ablation diagnostics.** Figure 3 empirically confirms the design intuition that different components handle different shift types — CSA alone sometimes outperforms full CONDA under low-level shifts, while LPA and RCB are critical under concept-level shifts. This transparency is a genuine strength.

## Weaknesses

### Fatal

None.

### Major

- **No comparison against simpler TTA baselines adapted to the CBM setting.** The paper claims the multi-stage CONDA design is necessary, but never evaluates straightforward TTA baselines applied to the same CBM pipeline. For example, one could freeze the concept bank and adapt only the linear layer via entropy minimization (à la TENT), or update pseudo-labels iteratively with confidence filtering. Without such baselines, it is impossible to determine whether the reported gains come from the sophisticated CSA/RCB components or from any form of online adaptation. This is the single most important gap: if a one-line entropy-minimization baseline achieves comparable results on concept-level shifts, the paper's central motivation for the three-stage design is weakened. The paper compares against zero-shot and linear probing (which are *no-adaptation* baselines), not against *alternative adaptation* baselines. Addressing this does not require new data or compute — it is a straightforward experiment the authors should run.

### Minor

- **Pseudo-label quality is not validated.** The adaptation pipeline (CSA and LPA both train on pseudo-labels via cross-entropy or distance-based losses) is entirely dependent on pseudo-label quality, yet the paper does not (i) report pseudo-label accuracy on any target domain, (ii) compare against simpler pseudo-labeling alternatives (e.g., using the base CBM itself, or confidence-based filtering), or (iii) analyze how pseudo-label noise affects downstream performance. The paper acknowledges that "more sophisticated pseudo-labeling methods … can be used to potentially improve our method" (line 140), but this does not substitute for empirical analysis of the chosen approach. The fact that the method improves overall suggests pseudo-labels are reasonable, but without analysis the reader cannot assess whether the remaining errors stem from label noise or from the adaptation design itself.

- **Interpretability evaluation is largely qualitative and lacks a repeatable methodology for the residual concept analysis.** Figure 4a provides a useful visualization of concept weight changes. However, the claim that residual concepts correspond to "feathers, wings, and beak" (line 276) is stated without explaining *how* the residual concept vectors (which live in the FM's feature space) were mapped to these textual descriptions. Additionally, only one dataset and one CBM variant are shown qualitatively. To make the interpretability claim credible, a more systematic evaluation would be needed — e.g., reporting cosine similarity between residual concept vectors and class-relevant text embeddings via the CLIP text encoder across multiple datasets.

- **Hyperparameter specification and sensitivity analysis are absent.** The paper defines several regularization coefficients (λ_frob, λ_sparse, λ_sim, λ_coh), the number of residual concepts *r*, and a sparsity parameter α (only α=0.99 is specified). It does not state how these are chosen, whether they are fixed across all experiments, or whether they were tuned on target-domain data. Given the complexity of the three-stage pipeline, a sensitivity analysis (or at minimum, explicit enumeration of all hyperparameter values) would help assess robustness.

### Trivial

- The WG accuracy for Label-free CBM on CIFAR10-C slightly decreases under CONDA (89.4 → 88.5 per Table 1). This does not undermine the paper's overall positive results but should be acknowledged in the discussion for completeness.
- Residual concept r is stated as 5 in the interpretability section but not as a general hyperparameter across all experiments.

## Nice-to-Haves

- A confidence-based filtering or thresholding mechanism for pseudo-labels could further improve results and would be a natural extension.
- The formalization in Section 2 (push-forward measures, distributional equations) is somewhat abstract for an empirical paper; the failure-mode categorization could be conveyed more concisely without loss of rigor.

## Removed Points

These points are flagged to be removed — treat them with caution.

1. **"FARE2 is not explained"** — The paper cites Schlarmann et al. (2024) and briefly describes it as "adversarially fine-tuned to be more robust." Per the hard rules, cited references are assumed to exist and are not required to be fully described in-text.

2. **"The formalization in Section 2 is abstract and not tightly connected to the method"** — This is a subjective judgment rather than an objective weakness. The failure modes in Section 2.3 directly motivate the three components of CONDA.

3. **"The 'up to 28%' claim is imprecise"** — The paper uses the phrase "up to" which is standard and accurate (the maximum improvement is indeed 28% on Waterbirds). Language like this is standard practice in ML papers.

4. **"No method is given for how residual concept vectors are mapped to textual descriptions"** — The superscript "4" after "beak" (line 276) indicates a footnote that the parser strips. The methodology may be present in the original submission. The broader point about insufficient quantitative evaluation is retained above as a Minor weakness.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Add TTA baselines.** Implement the simplest possible TTA baseline for the CBM setting: freeze the concept bank (C_s) and apply entropy minimization (TENT) to the linear layer (W, b) using test batches. This directly tests whether the CSA and RCB stages are needed. If CONDA outperforms this baseline, the paper's core claim is strongly supported; if not, the authors should discuss why the simpler approach is insufficient and what the added complexity buys.

2. **Report pseudo-label accuracy.** On at least one representative dataset per shift type (e.g., CIFAR10-C for low-level, Waterbirds for concept-level), report pseudo-label accuracy of the ensemble method vs. the base CBM's own predictions. This takes minimal effort and would significantly strengthen trust in the adaptation pipeline.

3. **Systematize the interpretability evaluation.** Use the CLIP text encoder to embed candidate concept descriptions and compute cosine similarity with the learned residual concept vectors. Report top-3 matches for each residual concept across datasets, making the "feathers, wings, beak" claim reproducible and quantitative.

4. **Specify all hyperparameter values** and include a brief sensitivity analysis (at least varying the most critical term, λ_frob or λ_sparse, by an order of magnitude) to show the method is not brittle.

## Score and Decision

The paper addresses a novel and well-motivated problem with a principled design and solid empirical results across diverse settings. However, the absence of the most natural and low-cost baselines (simple TTA methods adapted to the CBM setting) significantly weakens the claim that the full three-stage design is necessary — this is the central contribution claim. The paper would be substantially stronger by addressing this gap. On balance, the contribution is genuine but the evidence for it is incomplete.

**MY FINAL SCORE:** <pineapple>5.5</pineapple>
**MY FINAL DECISION:** <orange>Accept</orange>