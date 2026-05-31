## Summary
The paper introduces **ReefNet**, a large-scale, taxonomically standardized dataset for hard coral classification. It aggregates ~925K genus-level annotations from 76 CoralNet sources and a new Red Sea site (Al-Wajh), mapping all labels to the World Register of Marine Species (WoRMS). The authors establish two benchmarking protocols: a *within-source* split for localized performance and a *cross-source* split to evaluate domain generalization. Experimental results across various supervised and zero-shot models (including VLMs and MLLMs) demonstrate that while local classification is relatively successful, domain shift remains a significant barrier to global coral monitoring.

## Strengths
- **Taxonomic Rigor:** Unlike many existing coral datasets that use ad-hoc or coarse labels, ReefNet maps annotations to the WoRMS database (AphiaIDs). This ensures biological consistency and makes the dataset highly valuable for the marine science community.
- **Scale and Diversity:** With nearly 1 million annotations across 44 taxa and 26 marine ecoregions, it significantly exceeds the geographic and taxonomic breadth of previous public coral benchmarks.
- **Expert Verification:** The authors conducted a manual review of ~9K samples to establish confidence scores for source-genus pairs, allowing for the creation of high-quality "filtered" benchmarks.
- **Realistic Benchmarking:** The inclusion of a cross-source benchmark (out-of-distribution) directly addresses the most critical bottleneck in coral AI: the failure of models to generalize to new reef sites with different lighting, turbidity, and camera setups.
- **Multimodal Potential:** The inclusion of genus descriptions from expert texts (Veron, Wallace) enables the testing of Vision-Language Models (VLMs), as demonstrated in the zero-shot experiments.

## Weaknesses
### Fatal
None.

### Major
- **Zero-Shot Performance Gap:** The zero-shot results (Table 5) are extremely low (Macro Recall < 11%). While this highlights the difficulty of the task, the paper lacks a deep error analysis of *why* MLLMs like Qwen2.5-VL fail so significantly even with book-derived context. It is unclear if the failure is due to the resolution of the point-crop, the quality of the text descriptions, or the models' inherent lack of marine domain knowledge.
- **Class Imbalance Mitigation:** The paper notes a severe class imbalance (Figure 2). While Table 4 explores loss functions, the performance on rare classes remains a major weakness in the results. The paper would be stronger if it explored more sophisticated sampling or data augmentation strategies specifically for the long-tail genera.

### Minor
- **Point Annotation Context:** The dataset uses sparse point annotations. The paper does not explicitly detail the crop size or context provided to the models during training/inference (e.g., how much surrounding texture is included), which is a critical factor for coral identification.
- **Macro Recall vs. Accuracy:** While Macro Recall is appropriate for imbalanced data, the paper lacks a discussion on the practical implications of these scores for ecologists (e.g., what level of recall is "usable" for automated reef surveys?).

### Trivial
- The mention of "May 13, 2025" in Table 1 suggests a future-dated or placeholder timestamp.

## Nice-to-Haves
- A comparison of the "Al-Wajh" dataset performance against a model trained *only* on Red Sea data to see if global data actually helps or hinders regional performance.
- Visualization of the feature space (e.g., t-SNE) of the MAE-pretrained ViT vs. BioCLIP to understand why the former generalizes better in cross-source settings.

## Novel Insights
The most significant insight is the quantitative demonstration of the "Generalization Gap" in coral reef monitoring: models that achieve >80% Macro Recall in-distribution drop to ~40-50% when moved to a new source. Furthermore, the paper reveals that for coral classification, **data quantity often trumps data quality**; models trained on the larger, noisier Train-S3 (80% agreement) frequently outperformed those trained on the smaller, cleaner Train-S4 (91% agreement). This suggests that the diversity of environmental "noise" in larger datasets is more beneficial for domain robustness than the precision of individual labels.

## Suggestions
- Provide a sensitivity analysis on the crop size around the point annotations. Since corals are colonial organisms, the amount of spatial context significantly impacts the visibility of corallites vs. colony morphology.
- In the final version, include a confusion matrix for the cross-source benchmark to identify which specific genera are most frequently confused under domain shift (e.g., *Acropora* vs. *Montipora*).
- Clarify the prompt structure used for the Qwen-Book experiments to ensure reproducibility of the zero-shot results.

## Score and Decision
The paper provides a high-quality, much-needed benchmark for a critical environmental application. The methodology is sound, the scale is impressive, and the taxonomic alignment is a major contribution to the field.

MY FINAL SCORE: <score>8.0</score>
MY FINAL DECISION: <decision>Accept</decision>