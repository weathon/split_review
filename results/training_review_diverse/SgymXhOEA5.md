Now I have all the information I need. Let me synthesize the final review.

## Summary

This paper provides an empirical study of camera bias in person re-identification (ReID) models across three threads: (1) quantifying camera bias on unseen domains across diverse model architectures and training paradigms, (2) analyzing why camera-specific feature normalization removes this bias via a dimensional-sensitivity mechanism, and (3) identifying and mitigating camera bias in unsupervised learning. The paper demonstrates that camera bias is large on unseen domains for nearly all ReID models, reveals that the debiasing effect of normalization is driven primarily by centering high-variance feature dimensions, and shows that simple strategies (debiased pseudo labeling + discarding single-camera clusters) yield substantial improvements on unsupervised benchmarks.

## Strengths

- **First systematic quantification of camera bias on unseen domains across diverse models**: Table 1 reports NMI between cluster labels and camera labels for six state-of-the-art models on four datasets, showing that bias on unseen domains is large and consistent regardless of model architecture or training paradigm. This goes well beyond prior work, which focused on seen-domain bias only.

- **Mechanistic explanation for why feature normalization debiases**: Figures 2(a)–(c) decompose the embedding space and show that (i) dimensions have heterogeneous sensitivity to camera variations, (ii) features move consistently along sensitive dimensions under camera changes, and (iii) centering on just the top-50 high-variance dimensions (~13% of total) achieves roughly half the total mAP gain. This provides a principled understanding that was missing in prior empirical uses of camera mean subtraction.

- **Demonstrates that normalization generalizes to other bias factors**: Figure 3(b) shows group-specific normalization on brightness, sharpness, and area improves mAP, and Table 2 shows angle-specific normalization works. Combining camera labels with these factors yields further gains, revealing that camera bias is intertwined with other nuisance factors.

- **Identifies severe camera bias in unsupervised models and proposes effective mitigation**: Table 1 shows unsupervised models have NMI camera bias >50 on the seen MSMT17 dataset. Table 6 reports that debiased pseudo labeling + discarding single-camera clusters improves CC by +19.3 mAP on MSMT17 and PPLR by +8.0 mAP. The toy experiments (Figure 6) provide causal evidence that camera-biased pseudo labels are harmful, even when they have higher accuracy than less-biased alternatives.

- **Strong ablation isolating the dominant component**: Table 4 decomposes normalization into camera-specific centering, scaling, and ZCA whitening, showing centering alone yields the vast majority of the gain (44.7→60.7 mAP vs. full 44.7→62.1). This gives practitioners a clear recipe.

- **Analysis of sample volume requirements and compatibility with postprocessing**: Figure 5 shows ≥25 samples per camera suffices, and Table 5 shows normalization adds ~9 mAP on top of re-ranking and query expansion, confirming it addresses residual bias orthogonal to conventional postprocessing.

## Weaknesses

### Fatal
None.

### Major

- **The dimensional analysis explaining *why* normalization works is a single case study**: Section 4.2 performs the dimensional sensitivity analysis on *one* model (TransReID-SSL) evaluated on *one* unseen dataset (CUHK03-NP). While Section 4.4 confirms that the normalization procedure improves results across many models and datasets, it does *not* confirm that the same dimensional-sensitivity mechanism is at work in those other cases. The paper's central explanatory claim — that features move consistently along camera-sensitive dimensions and that centering those dimensions drives the gain — thus rests on one setup. Replicating this analysis on at least one additional model-dataset combination would substantially strengthen the claim. Without it, the reader cannot assess whether the mechanism is general or specific to this particular configuration. **Why it matters**: This is the paper's core analytical contribution; its evidentiary base is narrower than the narrative suggests.

### Minor

- **No discussion of failure modes for discarding single-camera clusters**: The paper discards single-camera clusters during USL training under the assumption they are "likely" incorrect groupings driven by camera bias. However, identities that genuinely appear in only one camera view in the training data would produce valid single-camera clusters that get discarded, removing useful positive pairs. The paper does not discuss this failure mode or analyze its frequency. The strong empirical results suggest the strategy is net beneficial, but an honest accounting of its limitations is missing.

- **Body angle label acquisition method is unspecified**: Section 4.3 states that the authors "define three body angle classes (front, back, and side) and construct four angle-labeled datasets from Market-1501" but does not explain how these labels were obtained. Market-1501 does not have native body angle annotations. Whether this required manual annotation, was inferred from camera positions, or used some other method matters for reproducibility and for assessing the practical utility of angle-specific normalization.

- **Framing of novelty could be sharper**: The paper acknowledges prior use of camera mean subtraction and camera-specific batch norm (Gu et al. 2020, Luo et al. 2021a, Zhuang et al. 2020), and positions its contribution as a "revisit" focused on analysis and generalizability. However, some phrasing (e.g., abstract: "we revisit feature normalization") risks being read as claiming more methodological novelty than the paper delivers. A more explicit upfront statement that the normalization operation itself is not new, and that the contribution is the analysis of its mechanism and breadth, would eliminate ambiguity.

### Trivial
None.

## Nice-to-Haves

- A comparison to camera-specific batch normalization re-estimated on the test set would be informative for situating the normalization approach among existing test-time debiasing alternatives, though this would require architectural modification beyond simple postprocessing.
- A breakdown of which improvement comes from debiased pseudo labeling alone (vs. discarding single-camera clusters alone) beyond the ablation in Figure 7(a) would help practitioners choose between the two strategies.
- An analysis of cluster purity (against identity labels) for discarded single-camera clusters would directly validate the assumption that these clusters are incorrect.

## Removed Points

- **"The paper does not compare normalization to... using only centering without scaling"**: This is factually incorrect. Table 4 explicitly evaluates camera-specific mean centering vs. full centering+scaling, and the text (line 106) notes that "camera-specific mean centering has a dominant effect and the scaling operation provides a small but additional gain." The comparison is already present.
- **"Re-estimated camera-specific BN comparison"**: Moved to Nice-to-Haves — this is a suggestion, not a weakness, and would require architectural modification beyond the paper's postprocessing scope.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

- **Replicate the dimensional analysis of Section 4.2 on at least one additional model-dataset combination.** The strongest version would pair a different model architecture (e.g., ResNet-based) with a different unseen dataset (e.g., Market-1501) to show the camera-sensitive dominance pattern holds beyond the TransReID-SSL/CUHK03-NP setup. If the pattern replicates, the paper's central explanatory claim becomes much more credible. If it does not replicate cleanly, the paper should acknowledge the boundary conditions.
- **Add a paragraph in Section 5.3 explicitly discussing the failure mode** where discarding single-camera clusters removes legitimate positive pairs (identities appearing in only one camera), and ideally provide a quantitative estimate of how often this occurs.
- **Clarify how body angle labels were obtained** for the Market-1501 experiments in Section 4.3.

## Score and Decision

This is a solid empirical paper with well-executed experiments, clear writing, and practical findings. The main weakness — that the mechanistic explanation rests on a single case study — is real but does not invalidate the paper's core contributions: the systematic quantification of unseen-domain camera bias, the practical demonstration that normalization works broadly, and the effective USL mitigation strategies. The paper makes a clear contribution to the ReID literature. I recommend acceptance.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>