Now I have a thorough understanding of the paper. Let me synthesize the final review, carefully cross-checking each reviewer claim against the actual paper content.

---

## Summary

This paper introduces CONDA, the first test-time adaptation framework for Concept Bottleneck Models (CBMs) with foundation model backbones. It formally categorizes distribution shift types (low-level vs. concept-level) and corresponding failure modes for CBMs, then proposes three adaptation components — Concept-Score Alignment (CSA), Linear Probing Adaptation (LPA), and Residual Concept Bottleneck (RCB) — each targeting a specific failure mode. Experiments on five real-world shift datasets (CIFAR10/100-C, Waterbirds, Metashift, Camelyon17) with multiple backbones (CLIP, adversarially robust CLIP, BioMedCLIP) and CBM construction methods show accuracy improvements of up to 28%.

## Strengths

- **First formal categorization of CBM failure modes under distribution shifts**: The paper provides rigorous mathematical definitions of low-level shift (Eq. 2) and concept-level shift (Eq. 3) and identifies three concrete failure modes (Section 2.3): non-robust concept bottleneck, non-robust classifier, and incomplete concept set. This formalization is novel and directly motivates the framework design.

- **Principled three-component framework tied to diagnosed failures**: Each CONDA component targets a specific failure mode — CSA addresses non-robust concept scoring under low-level shifts, LPA addresses classifier mismatch under concept-level shifts, and RCB addresses incomplete concept sets. The ablation (Figure 3) validates this design empirically, showing the expected differential contributions across shift types.

- **Significant and consistent empirical gains across diverse settings**: CONDA improves test-time accuracy by up to 28% across five datasets, three CBM construction pipelines (PCBM, unsupervised learned concepts, GPT-3 concepts), and three backbones (CLIP:ViT-L/14, adversarially robust CLIP, BioMedCLIP). Performance often matches or exceeds non-interpretable zero-shot and linear probing baselines, particularly on worst-group accuracy.

- **Generality across foundation model backbones and CBM pipelines**: The framework works with three different CBM construction methods and three backbones, including a domain-specialized medical model (BioMedCLIP). This breadth supports the claim that CONDA is a versatile solution rather than one tied to a specific pipeline.

## Weaknesses

### Fatal
None.

### Major
- **No direct comparison against standard TTA methods adapted to CBMs**: The paper compares CONDA against non-adapted CBMs and non-interpretable classifiers but does not include straightforward TTA baselines such as entropy minimization (TENT) applied directly to the CBM's label predictor. While the ablation shows LPA alone (label predictor adaptation via pseudo-labels), a TENT baseline would test whether concept-specific adaptation (CSA and RCB) is necessary beyond simple output-space adaptation. The paper's core claim that *concept-level* adaptation matters would be substantially strengthened by directly comparing against a CBM + TENT baseline. Without this, the reader cannot fully judge whether the complexity of CSA and RCB is warranted beyond what simpler adaptation of the label predictor could achieve.

### Minor
- **Pseudo-label quality is unaudited**: The entire adaptation pipeline depends on pseudo-labels from an ensemble of zero-shot and linear probing predictors. The paper does not analyze pseudo-label accuracy on target data, does not compare the chosen ensemble strategy against alternatives (e.g., only zero-shot, only linear probe, or confidence thresholding), and does not include an oracle experiment with ground-truth labels to bound the best possible performance. Given that TTA methods are known to be sensitive to pseudo-label noise, this analysis would help interpret the reported gains.

- **Methodology for interpreting residual concepts is not clearly described**: The paper claims that RCB discovers interpretable concepts (e.g., "feathers, wings, and beak") but does not describe the procedure for mapping learned residual concept vectors to semantic labels. The coherency regularization (L_coh) encourages interpretability by design, but the actual assignment of human-readable labels to residual vectors is not explained in the main text. (This may be elaborated in the appendix, which was not available for review.) Given that interpretability is a core promised contribution, this gap should be addressed.

- **Gaussian assumption for concept-score distributions is untested**: CSA uses Mahalanobis distance under the assumption that class-conditional concept scores are multivariate Gaussian (Section 3.1). The paper does not validate this assumption (e.g., via normality tests or visual inspection) for any dataset or backbone. While the LPA step partially mitigates potential mismatch, this weakens the theoretical grounding of CSA.

- **Hyperparameter sensitivity is unexamined**: The method introduces several hyperparameters (λ_frob, λ_sparse, λ_sim, λ_coh, r, α) that are fixed across all experiments without sensitivity analysis. The ablation shows that CSA alone outperforms the full CONDA under low-level shifts, suggesting that performance may be sensitive to component weighting. A sensitivity study would improve reproducibility and practical applicability.

- **Pseudo-labeling strategy not ablated**: The confidence-based ensemble of zero-shot and linear probing predictors is not compared against alternatives such as using only the zero-shot predictor, only the linear probe, or self-labeling with the unadapted CBM. This is a consequential design choice that deserves ablation.

### Trivial
None.

## Nice-to-Haves
- Reporting standard deviations or confidence intervals for main results would improve reliability assessment.
- An oracle experiment using ground-truth test labels would quantify the ceiling of CONDA and the cost of pseudo-label noise.
- Visualizing concept-score distributions before/after CSA for a representative shift type would help demonstrate alignment.

## Removed Points
These points are flagged to be removed, treat them with caution:
- *"Table is embedded as image and cannot be verified from prose"* — This is a PDF parsing artifact; the table exists in the original submission.
- *"Section 4.2 only reports source-domain numbers"* — The paper quotes source-domain numbers for context; target-domain results are in Table 1. This reflects the parser stripping the table, not an author omission.
- *"CSA alone exceeding CONDA under low-level shifts is not discussed"* — The paper *does* discuss this: "Interestingly, using CSA alone even surpasses the performance achieved when all components are combined" and provides an explanation citing Lee et al. (2023). The critic's claim is factually incorrect.
- *"Section 2 formalization is unrealistic because it never addresses cases where both modes operate"* — The framework's three components collectively handle both shift types, and the Camelyon17 experiment (natural shift) likely involves both. The formal categorization is a conceptual tool, not a claim that shifts are mutually exclusive.
- *"LPA alone is not presented as a full baseline"* — Figure 3 explicitly shows LPA alone as a comparison point in the ablation analysis.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. **Add a CBM + TENT baseline**: Adapting the CBM's label predictor via entropy minimization (without pseudo-labels) would directly test whether concept-level adaptation (CSA and RCB) is necessary. If this baseline performs comparably to CONDA, the claim that concept-specific adaptation is needed would be undermined; if it does not, the paper's contribution would be substantially strengthened.
2. **Provide a pseudo-label quality analysis**: Report pseudo-label accuracy on target data for each dataset, and include an oracle experiment using ground-truth labels to bound the best achievable performance.
3. **Clarify the residual concept interpretation methodology**: Describe how the semantic labels (e.g., "feathers, wings, beak") were assigned to learned residual concept vectors, whether through nearest-text retrieval, human inspection of top-scoring images, or another method. A human evaluation or at least a qualitative example with supporting evidence would substantiate the interpretability claim.
4. **Validate the Gaussian assumption**: Include normality tests or visualizations of concept-score distributions for a representative class to justify the use of Mahalanobis distance in CSA.
5. **Report hyperparameter sensitivity**: Perform a sensitivity analysis for key hyperparameters (especially λ_frob, λ_sim, λ_coh, and r) on at least two datasets to demonstrate robustness.

## Score and Decision

The paper addresses a timely and well-motivated problem — making interpretable CBMs robust to distribution shifts at deployment. It provides the first formal treatment of CBM failure modes under shifts and proposes a principled, three-component adaptation framework. The empirical results are strong and consistent across diverse datasets, backbones, and CBM pipelines. However, the evaluation has notable gaps: the absence of a CBM + TENT baseline weakens the claim that concept-specific adaptation is necessary, the pseudo-labeling pipeline is not audited or ablated, and the interpretability claim for residual concepts is not fully substantiated. These issues are addressable and do not invalidate the core contribution, but they prevent a stronger rating.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>