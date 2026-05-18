Now I have a thorough understanding of the paper and can verify all claims. Let me produce the final consolidated review.

## Summary

This paper studies how pretraining label granularity affects transfer learning in image classification. Theoretically, it proves (using a two-layer ReLU network trained with SGD on a hierarchical data model) that fine-grained pretraining enables learning of rare features while coarse-grained training only learns common features, explaining why fine-grained pretraining boosts accuracy on hard test samples. Empirically, it shows leaf-level labels on ImageNet21k outperform coarser levels for transfer to ImageNet1k, and on iNaturalist reveals a U-shaped effect where both too-coarse and too-fine labels hurt, along with the importance of label hierarchy quality and source-target alignment.

## Strengths

- **Novel theoretical result linking label granularity to feature learnability**: Theorems 1 and 2 prove that under a hierarchical data distribution with orthonormal features, coarse-label training cannot learn fine-grained features even after polynomially many SGD steps, while fine-grained training learns both common and rare features. This provides a formal mechanism—grounded in cross-entropy loss and a two-layer ReLU network—that goes beyond prior theory using NTK or hinge loss. The proof traces how gradient dynamics respond to feature frequency in the training data, which is the paper's most distinctive contribution.

- **Discovery of the U-shaped effect of pretraining granularity**: The iNaturalist experiment (Figure 2) reveals that transfer error first decreases then increases as granularity grows, with manual labels showing a clear U-curve. This is a novel empirical finding that challenges any simplistic "finer is always better" narrative and highlights the existence of a sweet spot.

- **Systematic ablation of label hierarchy quality and alignment**: The paper controls for hierarchy meaningfulness (manual vs. random vs. kMeans) and alignment (kMeans per superclass vs. whole dataset) on iNaturalist (Figure 2). This provides practical guidelines: a meaningful hierarchy that aligns well with the target is necessary for fine-grained pretraining to succeed.

- **Clean ImageNet21k→ImageNet1k benchmark results**: Table 1 shows monotonic improvement as granularity increases, with leaf-level (21,843 classes) achieving 82.51% accuracy. This validates the common practice in the community and provides a clear reference for future work.

## Weaknesses

### Fatal
None.

### Major

- **The core theoretical mechanism is not directly tested empirically**: The theory predicts that fine-grained pretraining specifically improves accuracy on *hard* test samples (where common features are missing/weak), while coarse training already handles easy samples. However, the experiments only report aggregate accuracy on the full test set. The paper does not partition test samples into easy vs. hard groups—using, e.g., prediction confidence under a coarse-trained model or the WordNet hierarchy to define hard samples—to verify that gains concentrate on the hard subset. Without this analysis, the proposed mechanism remains unvalidated; the aggregate gains are consistent with alternative explanations (better optimization dynamics, higher model capacity from more output heads, etc.). This is the single most important gap between the paper's explanatory claim and its evidence.

- **Gap between theoretical setting and experimental protocol**: The theory assumes (a) source and target inputs are drawn from the *same distribution* (Section "Target data distribution assumptions"), and (b) classifier weights are frozen ($a_{c,r}=1$) throughout training. In contrast, the ImageNet21k→ImageNet1k experiment involves *different datasets* with distribution shift, and all experiments use *full finetuning* of the network. The theory most directly supports the in-dataset iNaturalist experiments, but the introduction (lines 43–46) positions the theory as explaining the ImageNet21k→ImageNet1k observation in Figure 1, which is somewhat misleading. The distribution-shift limitation is acknowledged only in the conclusion ("future work"), and the frozen-classifier assumption means the theory does not analyze how finetuning would reweight features. The footnote that finetuning "can further boost" the feature extractor does not constitute analysis.

### Minor

- **Per-class sample count varies inversely with granularity in ImageNet21k experiment**: With ~14M fixed images, leaf-level has ~640 images/class while level 9 has ~368,000 images/class. This confound is not discussed. (The observed trend—finer is better despite fewer images per class—actually goes *against* what a sample-starvation hypothesis would predict, so it does not threaten the conclusion. But it should still be addressed for completeness.)

- **Theoretical bounds on fine-grained classes are restrictive**: The requirement $k_+, k_- \in [\text{polylog}(d), d^{0.4}]$ (Note 2) means the theory only applies when the number of subclasses falls in a specific polynomial window. Real hierarchies often have widely varying numbers of subclasses per superclass, making it unclear how broadly the theory applies.

- **Size of the "mini version" of iNaturalist is not specified**: The paper states it uses "a mini version of the training set" (line 256) without reporting the exact number of samples or the fraction of the full dataset. This hurts reproducibility and makes it harder to assess whether the U-shaped curve might shift with more data.

### Trivial

- Theorem 1 notation: "$\mathcal{L}(F^{(T)}) \le o(1)$" uses $o(1)$ as an asymptotic statement where a concrete bound (e.g., $O(d^{-c})$) would be clearer.
- Figure 1's x-axis ("Number of classes") spans 38 to 21,843; a log scale would improve readability. The paper should also clarify whether the single curve is from one run or averaged.

## Nice-to-Haves

- **Easy/hard sample breakdown in experiments**: As argued above, testing the theory's specific prediction about hard samples would be the highest-leverage addition.
- **Control for per-class data size in ImageNet21k**: Subsampling coarser levels to match leaf-level per-class counts, or training for more epochs at coarser levels, would eliminate the confound.
- **Discussion of how finetuning interacts with learned features**: Even a brief heuristic argument about how finetuning preserves or amplifies the feature-learning advantage of fine-grained pretraining would bridge the theory-experiment gap.
- **Synthetic fine-grained labels with known alignment properties**: This would strengthen the alignment claims beyond the current cluster-based baselines.

## Removed Points

- *"The paper does not explain the right-side rise of the U-shape"*: **Removed** because the paper does explain this (lines 267–268), attributing it to learning "frivolous details" when granularity is too fine.
- *"The green curve (kMeans per superclass) is a weak baseline that nearly guarantees alignment with the target"*: **Removed** because the paper explicitly acknowledges this design choice (lines 260–261: "its label function is forced to align better") and uses it as a controlled comparison, not as a claimed strong baseline.
- *"The paper's central claim is not supported by the theory"* (in the strongest sense): **Downgraded**. The theory does support the claim about feature learning in the idealized setting. The gap is between idealized theory and practical experiments, not absence of support.
- *"Missing appendix" / "missing proofs in appendix"*: Not present in the reviewer's text, so no action needed.
- *"Cumulative" and generic formatting/style nitpicks*: Removed per instructions.

## Novel Insights

The reviewer's most incisive observation is that the paper's central explanatory claim (the hard-sample mechanism) is not directly tested, creating a disconnect between the theoretical contribution and the empirical validation. This is not merely a missing ablation—it means the paper's signature claim about *why* fine-grained pretraining helps (as opposed to *that* it helps) remains a theoretical possibility rather than an established finding. The reviewer's suggestion to define hard samples operationally (e.g., via coarse-model confidence) is a concrete path to close this gap that the authors should prioritize.

## Suggestions

1. **Directly test the hard-sample mechanism**: Partition the ImageNet1k test set into easy vs. hard samples (using coarse-trained model confidence or WordNet hierarchy position), and show that the accuracy gain from leaf-level pretraining is concentrated on the hard subset. This single addition would substantially validate the theoretical mechanism.
2. **Add a discussion of the per-class sample count confound** in the ImageNet21k experiment, explaining why the trend's direction rules out simple sample-starvation explanations, or run a controlled subsampling experiment.
3. **Clarify the scope of the theory** in the introduction: explicitly state that the theory applies to the same-distribution setting (iNaturalist-like experiments) and that cross-dataset transfer involves additional considerations, rather than presenting the theory as explaining the ImageNet21k→ImageNet1k results.
4. **Report the size of the "mini" iNaturalist dataset** used in experiments.

## Score and Decision

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>