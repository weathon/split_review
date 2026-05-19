- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 5, 6, 5
Now I have a thorough understanding. Let me produce the final consolidated review.

## Summary

The paper proposes PointMIL, the first framework to apply Multiple Instance Learning (MIL) to point cloud classification for inherent local interpretability. It replaces standard global pooling with four MIL pooling strategies (Instance, Attention, Additive, Conjunctive) and introduces a contextual attention mechanism that smooths attention weights over k-NN neighborhoods. The method is evaluated on five backbones (PointNet, DGCNN, CurveNet, PointMLP, PointNeXt) plus a proposed transformer backbone, across three classification datasets (IntrA, RBC, ModelNet40) and a segmentation task (ShapeNetPart). The paper claims state-of-the-art on IntrA (97.3% mACC, 97.5% F1) and demonstrates interpretability gains over post-hoc methods (CLAIM, PSM).

## Strengths

- **First application of MIL to point cloud classification for inherent local interpretability.** The paper explicitly establishes this novelty (abstract, Section 2, line 31: "to our knowledge, no one has used MIL for interpretable point cloud classification"), and the mapping from points→instances, clouds→bags is sound and naturally adapted.

- **Consistent classification improvements across diverse backbones and datasets.** Table 2 shows that PointMIL improves over the original backbone on IntrA, RBC, and ModelNet40 for all five adapted backbones, with gains up to 11.3% mACC on RBC. This demonstrates plug-and-play utility rather than tuning-specific success.

- **Quantitative interpretability gains over post-hoc methods (CLAIM, PSM) across multiple backbones.** Table 1 reports that PointMIL achieves higher AOPCR and NDCG@n on IntrA compared to both post-hoc methods across nearly all backbone combinations (the sole exception is CLAIM on DGCNN for AOPCR). This is direct evidence that inherent MIL-based explanations can be more faithful.

- **Contextual attention mechanism validated by ablation.** Figure 8 shows that using contextual attention (k > 0) consistently improves F1, mACC, AOPCR, and NDCG@n for all three attention-based pooling methods over the baseline without it (k = 0), confirming the design's empirical benefit.

- **Visual robustness to noise demonstrated.** Figure 9 shows that after adding noisy points, PointMIL's attention still focuses on salient shape motifs, indicating practical reliability.

## Weaknesses

### Fatal
None.

### Major

1. **No statistical variance or significance reporting for any quantitative result.** Every metric in Tables 1, 2, and 3, as well as the ablation in Figure 8, is reported as a single point with no error bars, standard deviations, or indication of multiple runs. On IntrA (a small biomedical dataset) and RBC, classification and interpretability metrics can vary with random seeds and data splits. The paper claims SOTA (97.3% mACC on IntrA) and improvements over baselines (up to 11.3% on RBC), but without variance the reader cannot assess whether these differences are reliable or within noise. This is the single most important evidential gap and weakens every quantitative claim.

2. **Ambiguous basis for baseline comparisons.** Table 2 reports results for competing methods (PCT, CurveNet, PointMLP) on IntrA and RBC, but the paper never states whether these numbers were obtained from the authors' own controlled re-implementation under identical train/val splits, preprocessing, and hyperparameters, or are cited from original publications. While the Table 2 caption notes "All results are shown without voting strategy on 1024 points" and marks adapted architectures with †, the experimental protocol for the non-adapted baselines is unspecified. The SOTA claim on IntrA is therefore not fully substantiated — the reported margins over e.g., PointMLP (97.3% vs. 89.8%) may reflect different training conditions rather than genuine improvement.

### Minor

1. **Transformer feature extractor description lacks architectural details.** Section 3.1 states the extractor "follow[s] much of the Transformer block from Yu et al. (2021) but without point sampling strategies and without multi-graph reasoning." Key details — number of layers, hidden dimensions, number of heads, activation functions, positional encoding specifics — are not provided. Reproducibility would benefit from a concise specification.

2. **Contextual attention limitations not discussed.** The mechanism (averaging attention weights over k-NN neighbors) is a simple smoothing heuristic. The paper does not discuss when this smoothing could harm interpretability, e.g., at object boundaries or high-curvature regions where neighborhood averaging may blur discriminative structure. The trade-off between sparsity and fidelity is acknowledged only in terms of computation, not explanation quality.

3. **Attention pooling interpretability compared to class-specific methods without explicit caveat in results.** Section 3.4 correctly states that Attention pooling weights are "a measure of general importance… not class-specific." However, in Table 1 and the Section 5.1 discussion, Attention pooling results are compared alongside class-specific methods (CLAIM, PSM) without noting this mismatch. While the comparison is not invalid (general importance can still be useful), it would strengthen the presentation to explicitly caveat that Attention pooling is at a disadvantage for this particular comparison.

4. **Segmentation evaluation lacks detail.** Section 5.4 describes the segmentation setup in one sentence — "The class-specific point-level interpretations were used as segmentation predictions" — and presents mixed results (the original 3DMedPT outperforms PointMIL on ShapeNetPart "by a relatively larger margin" that is not quantified). The segmentation experiments feel like an afterthought and do not strongly support the framework.

5. **Dataset-dependent performance pattern unanalyzed.** PointMIL's gains are large on biomedical data (IntrA, RBC) but marginal on ModelNet40 (e.g., PointNet 89.2→89.6). This pattern is noted but not analyzed. Given that the MIL assumption (discriminatory points are a subset) fits biomedical data well, discussing why would strengthen the paper's positioning.

### Trivial
- Line 207: "backone" → "backbone" (typo).
- The image-based tables (Tables 1-3 are rendered as embedded images) make precise numerical comparison difficult; text tables would be preferred.

## Nice-to-Haves
- Adding multiple runs with variance reporting (this is listed as Major because it's an evidential gap, not a nice-to-have — it should be prioritized).
- A brief runtime/inference-time comparison for the transformer backbone with and without contextual attention, beyond the theoretical O(N²) discussion already present.
- A discussion of failure cases from the interpretability perspective (e.g., whether misclassifications are systematically driven by attention to irrelevant regions).

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Contextual attention adds O(N²) — runtime analysis missing"**: The paper already explicitly discusses this trade-off in Section 5.3 (line 236: "there is a trade-off in computation since the time complexity for k-NN graph search is O(N²)"). The harsh critic's suggestion for a runtime comparison is a nice-to-have, not a gap.

- **"IntrA has 'likely fewer than 200 shapes'"**: This is speculation by the reviewer not verifiable from the paper text. The core criticism (no error bars on small datasets) stands without this speculation.

- **"The paper should compare to prototype-based methods (XPCC, Interpretable3D)"**: These methods are correctly identified in the paper as global rather than local. The paper explicitly scopes its contribution to local interpretations. Criticizing absence of comparison to global methods is scope creep.

- **"Segmentation description insufficient"**: The paper does describe the approach (line 249: "The class-specific point-level interpretations were used as segmentation predictions"). While brief, this is a correct description. The weakness about insufficient quantification of the "relatively larger margin" is retained in Minor.

- **"Post-hoc comparison fairness not acknowledged"**: The harsh critic suggests the comparison to post-hoc methods may be unfair because PointMIL is trained with an interpretability-oriented objective while post-hoc methods are applied after standard training. This is a reasonable observation but does not invalidate the comparison — the paper's claim is simply that its explanations are more faithful, which is a legitimate empirical finding regardless of training differences.

- **Strength: "this paper addressed an important problem"** / **Strength: "this paper targeted an interesting question"**: Removed as generic; the remaining strengths are concrete and evidence-backed.

## Novel Insights

The harsh critic's framing of the dataset-dependent performance pattern (large gains on biomedical data where the MIL assumption naturally holds, marginal gains on ModelNet40) is an insight that the paper itself notes but does not develop. This pattern suggests the method's value proposition is domain-dependent, and future work on the boundary conditions of when MIL pooling helps vs. hurts would sharpen the contribution. Apart from this, no genuinely novel observations emerge beyond the paper's own stated contributions.

## Suggestions

1. **Add variance reporting (highest priority).** Report mean ± std over at least 5 runs with different random seeds for all metrics (mACC, F1, AOPCR, NDCG@n). This single change would dramatically increase the credibility of every claim.

2. **Clarify baseline protocol explicitly.** State whether each baseline number in Table 2 comes from the authors' own re-implementation (with the same splits/preprocessing) or is cited. If some are cited, mark them as such. If all are reimplemented, say so and provide a brief description of the experimental control.

3. **Specify transformer backbone architecture.** Add a concise table listing layers, dimensions, heads, activations, and positional encoding for the transformer backbone.

4. **Discuss contextual attention's failure modes.** Add a brief discussion of when neighborhood smoothing could harm interpretability (boundaries, high-curvature regions) to strengthen the analysis.
