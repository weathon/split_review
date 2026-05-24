Now I'll synthesize the final review.

## Summary

This paper makes two interconnected contributions: (i) **ContrastiveCAMs**, an interpretability method that is provably invariant to a spurious shift redundancy in HiResCAMs arising from softmax invariance, and (ii) **Core-Focused Cross-Entropy (CFCE)**, a training loss that leverages ContrastiveCAMs to suppress non-core region contributions, encouraging models to base predictions on target-relevant features. Experiments on Hard-ImageNet, Oxford-IIIT Pets, and PASCAL VOC demonstrate large IoU gains (e.g., 93.39% vs. 30.27% ContrastiveCAM IoU on Hard-ImageNet) and positive transfer to downstream segmentation, with competitive results even when using approximate SAM or bounding-box masks.

## Strengths

- **Theoretical identification of a genuine redundancy in HiResCAMs.** Theorem 3.2 proves that adding an arbitrary matrix \(M\) to all class HiResCAMs leaves probability predictions unchanged, establishing a non-obvious identifiability issue. This is a novel mathematical observation about a widely-used explanation method.

- **ContrastiveCAMs provably remove this redundancy.** Theorem 3.5 proves invariance to the spurious shift \(M\), and Proposition 4.1 shows ContrastiveCAMs directly relate to probability predictions. This is a principled fix, not an ad-hoc heuristic.

- **Principled bridge from interpretability to feature alignment.** Deriving CFCE from ContrastiveCAMs (Definition 4.5) and proving its consistency with core-constrained risk (Theorem 4.6) provides a rigorous foundation for the training objective — this goes well beyond "use explanations during training."

- **Large and consistent empirical improvements.** On Hard-ImageNet, CFCE+KL achieves 93.39% ContrastiveCAM IoU vs. 30.27% for CE w/ Arch, and a positive relative foreground sensitivity (+0.236 vs. −0.23 for baselines). On Oxford Pets, CFCE+KL with ground-truth masks reaches 92.72% IoU (vs. 78.37% for CE). Improvements hold across binary, multiclass, and multilabel settings.

- **Practical deployability with approximate masks.** Table 3 shows CFCE with SAM-generated masks achieves 83.95% IoU on Pets, closing most of the gap to the 92.72% with ground-truth masks, demonstrating utility without expensive pixel-level annotations.

- **Downstream segmentation gains.** Figure 4 shows consistent per-class IoU improvements when CFCE-trained backbones are used for segmentation, especially in end-to-end fine-tuning, validating that the alignment transfers to dense prediction tasks.

## Weaknesses

### Fatal
None.

### Major

- **Missing comparison against directly competing feature-alignment training methods.** The paper cites Aniraj et al. (2023, masking strategies) and Ismail et al. (2021, saliency regularization) in its related work but does not compare against them experimentally. The baselines in Table 2 (CORM, DFR) are evaluation/diagnostic methods, not alternative training approaches for alignment. Without such comparisons, it is unclear whether CFCE's large IoU gains are unique to this method or could be achieved by simpler masking or regularization during training. This weakens the paper's central claim about the superiority of its approach.

- **Only one architecture tested.** All experiments use ResNet-50. Given that the method relies on assumptions about the classifier (single-layer linear after GAP), results on at least one additional architecture (e.g., VGG, DenseNet, or a ConvNeXt variant) are needed to demonstrate generality.

### Minor

- **Accuracy-alignment trade-off underexplored.** On Hard-ImageNet, CFCE drops unablated accuracy from ~94% to ~90% (a ~4% reduction). On Oxford Pets multiclass, validation accuracy drops from ~94% to ~90-93%. The paper acknowledges these drops but does not analyze whether the trade-off is acceptable or whether core-focused models offer benefits (e.g., OOD robustness) that justify the cost.

- **Hyperparameter sensitivity not reported.** The regularized loss (Definition 4.7) introduces three hyperparameters \((\lambda_1, \lambda_2, \lambda_3)\). The paper does not discuss their values, sensitivity, or how they were selected. This is a practical concern for adoption.

- **ContrastiveCAM-IoU metric asymmetry in Table 2.** The main Hard-ImageNet baselines (Cross-Entropy, CORM, DFR) lack ContrastiveCAM IoU values (shown as "—"), while CFCE methods have both GradCAM and ContrastiveCAM IoU. The paper explains this choice, but it makes a direct apples-to-apples comparison of IoU across all methods incomplete.

- **CE w/ Arch baseline has very high IoU variance on Oxford Pets** (std 16.98 for binary valid IoU), reducing the reliability of comparisons for that particular entry.

- **Segmentation bar chart (Figure 4) lacks error bars.** While the classification tables include standard deviations, the segmentation results are presented without error bars, making it difficult to assess significance.

### Trivial
None.

## Nice-to-Have

- Compute forward/backward cost (runtime and GPU memory vs. standard cross-entropy) would help practitioners assess the overhead.
- A brief hyperparameter sensitivity study (e.g., varying \(\lambda_1\) over an order of magnitude) would substantially strengthen practical guidance.
- Mentioning extension to Vision Transformers as future work acknowledges the natural next direction.

## Removed Points

These points are flagged to be removed; treat them with caution:

1. **Harsh critic's "overstated theoretical flaw in HiResCAMs":** The critic claims the redundancy is between "different possible logit vectors, not between explanations of the same model." However, Theorem 3.2 correctly identifies that for a given probability prediction, HiResCAMs have an additive degree of freedom. While this is a theoretical rather than empirical limitation, the paper is clear that HiResCAMs *may* not faithfully explain predictions ("may" in the abstract, "fail to guarantee" — a standard phrasing for identifiability results). The paper also quantifies this redundancy empirically in Table 1 (\(\gamma\) values). The criticism is a disagreement about framing strength rather than a factual error and does not threaten the paper's core contribution (ContrastiveCAMs + CFCE). Demoted from the review.

2. **"Loss implementation is underspecified":** The harsh critic claims the paper "never states" the gradient is constant for a single-layer classifier. However, the paper explicitly states (line 108): "In this paper, we assume that the classifier is of the form in Eq. (1)" which is \(h(\mathbf{z}) = W\mathbf{z} + \mathbf{b}\). For readers familiar with CAM literature, this makes the gradient computation straightforward. The critic's reproducibility concern is overstated — the main text defines the loss, states the classifier form, and defers derivations to the appendix (a standard practice).

3. **Strength Finder generic strengths removed:** None of the Strength Finder outputs needed removal — all were specific, evidence-grounded, and conflict-free with verified weaknesses.

## Novel Insights

None beyond the paper's own contributions. The two reviews converge on the same set of genuine strengths and weaknesses. An interesting observation that emerges from reading both is that the paper's theoretical contribution (ContrastiveCAMs) is arguably stronger than its experimental evaluation can fully showcase — the empirical sections focus on CFCE (the downstream application) rather than on rigorously benchmarking ContrastiveCAM as an explanation method in its own right (e.g., sanity checks, faithfulness metrics, comparison to GradCAM/GradCAM++/HiResCAM on standard explainability benchmarks). This gap between theoretical contribution breadth and experimental coverage is worth noting but not a weakness per se, given the paper's stated focus on feature alignment.

## Suggestions

1. Add at least one comparison against a masking-based or saliency-regularized training baseline (e.g., Aniraj et al. 2023) on Hard-ImageNet to strengthen the claim that CFCE offers unique value.
2. Test on at least one additional architecture (e.g., DenseNet-121 or ConvNeXt-T) to demonstrate generality beyond ResNet-50.
3. Report the hyperparameter values used for \(\lambda_1, \lambda_2, \lambda_3\) and include a brief sensitivity analysis.
4. Discuss the ~4% accuracy drop on Hard-ImageNet more thoroughly — is this inevitable for any core-focused method, or specific to CFCE?
5. Add error bars to the segmentation bar chart (Figure 4).

## Score and Decision

I position the paper against the retrieved calibration anchors as follows:

- **Low anchor: WYsLU5TEEo** (avg 2.50) — Counterfactual Image Generation for robust/interpretable classifiers. Poor writing, unclear methodology, limited to binary tasks. **Current paper is far stronger in theory, experiments, and clarity.**
- **Low anchor: qW9GVa3Caa** (avg 3.67) — Prototype Generation for interpretability. Qualitative, limited to 2 classes, missing details. **Current paper is substantially more rigorous.**
- **Low anchor: L7jtdGhWzT** (avg 4.67) — Faithfulness-guided Ensemble Interpretation. Unclear methodology, mixed results. **Current paper is stronger in both theory and experiments.**
- **Mid anchor: bkdWThqE6q** (avg 6.00) — Interpretable Transformer for fine-grained classification. Clear idea, good presentation, but mostly qualitative evaluation. **Current paper has stronger theory and more comprehensive quantitative experiments.**
- **Mid anchor: 57NfyYxh5f** (avg 6.25) — How to Probe: improving post-hoc explanations. Well-written, extensive experiments but only ResNet-50 (same limitation). **Current paper has richer theoretical contributions and similar experimental scope.**
- **High anchor: GjfIZan5jN** (avg 7.33) — Enhancing Pre-trained Representation Classifiability can Boost its Interpretability. Novel metric, experiments across many architectures and datasets. **Current paper has stronger theoretical novelty but less architectural breadth.**

The paper makes genuine theoretical contributions (ContrastiveCAM invariance, CFCE consistency) and backs them with impressive empirical gains. Its main limitations are architectural scope (only ResNet-50), missing alignment-method baselines, and limited discussion of the accuracy-alignment trade-off. These are addressable and do not undermine the core contribution. The paper is stronger than the mid-range anchors (6.0–6.25) due to its theoretical depth, but slightly below the high anchor (7.33) in experimental breadth. I assign 6.5.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>