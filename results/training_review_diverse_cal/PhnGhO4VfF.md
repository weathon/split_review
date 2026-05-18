Now I have a thorough understanding of the paper and can verify each reviewer claim against the actual content. Let me write the consolidated review.

## Summary

This paper studies how the granularity of pretraining labels affects transfer learning in image classification, focusing on the fine-to-coarse setting (more source classes than target classes). Empirically, it shows that pretraining on the leaf labels of ImageNet21k transfers better to ImageNet1k than coarser levels, and that iNaturalist2021 experiments reveal a U-shaped relationship with granularity mediated by label hierarchy meaningfulness and alignment. Theoretically, it proves for a two-layer network on synthetic hierarchical data that coarse-label training fails to learn fine-grained ("rare") features when only "easy" training samples are present, whereas fine-grained labels allow those features to be learned.

## Strengths

1. **Clear empirical demonstration that leaf-level pretraining on ImageNet21k substantially outperforms coarser levels.** Table 1 shows ViT-B/16 finetuning accuracy reaches 82.51% with leaf labels (21,843 classes) versus 77.91% baseline and only 75.53% at hierarchy level 6 (160 classes), with a monotonic trend. This directly supports the paper's central empirical claim and validates common practice in the community.

2. **Identification and experimental verification of necessary conditions for effective fine-grained pretraining: meaningful hierarchy and label alignment.** The iNaturalist 2021 experiments (Figure 2) systematically compare manual hierarchies, random labels, and kMeans-based cluster labels. Manual hierarchies achieve the lowest validation error, and separate-per-class kMeans (which preserves alignment with target superclasses) outperforms whole-dataset kMeans. This goes beyond a simple "finer is better" observation to actionable design conditions.

3. **Clean experimental design that isolates the causal effect of label granularity.** In the iNaturalist transfer experiments (Section 5.2), the source and target datasets use the same input samples, differing only in label granularity. This design, explicitly motivated by the theoretical setup, ensures observed accuracy differences are causally attributable to granularity rather than distribution shift — a well-controlled experiment.

4. **Intuitive theoretical model capturing the common-versus-fine-grained feature hierarchy.** Definitions 1–5 formally define orthonormal features, easy/hard samples, and label mappings in a way that mirrors the cat-versus-dog intuition (Section 3.2). The theoretical framework cleanly formalizes the multi-view data structure, distinguishing the work from prior analyses that lack hierarchical structure.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **The theory's easy-only assumption limits its direct explanatory value for real transfer, and the paper's framing somewhat overstates what is proven.** Theorems 1 and 2 are proved only for training sets composed *entirely* of "easy" samples (Section 4.4, line 180). The paper acknowledges this limitation in a single paragraph (line 194), stating that allowing hard training samples "essentially yields a perturbed version of our results... which we leave for future work." However, the abstract and introduction claim to "explain the benefit of fine-grained pretraining" without emphasizing that the proof assumes away the presence of hard training samples — the very regime where the question is most interesting. The theory is best described as an *illustration* of a possible mechanism under idealized conditions, not a direct explanation of the observed empirical phenomenon. The paper would benefit from calibrating its claims about what the theory establishes.

2. **The empirical evaluation does not directly test the specific mechanism predicted by the theory.** The theory predicts that fine-grained pretraining improves accuracy specifically on "hard" test samples (where common features are weak or missing). However, the ImageNet21k experiment reports only overall validation accuracy (Table 1), and the iNaturalist experiments report only overall validation error (Figure 2). Neither experiment partitions test samples by difficulty to verify that the gains concentrate on hard samples. While aggregate improvements are consistent with the theory, they do not validate its specific causal mechanism. This leaves a gap between the theoretical prediction and the empirical evidence.

3. **The iNaturalist experiment does not control for varying samples-per-class as granularity changes.** As the number of pretraining classes increases, the average number of samples per class decreases (since the same training set is relabeled at different hierarchy levels). The paper attributes the right-side increase of the U-shaped curve to learning "frivolous details" (line 267), but the decreasing samples-per-class is a confound that could independently degrade pretraining quality at high granularities. The paper does not report per-class sample sizes for each hierarchy level nor attempt to control for this variable. (Note: this confound cannot explain the *left* side of the U-shape — where error decreases as granularity increases — so the overall finding that granularity matters is not threatened, but the specific interpretation of the right-side degradation is weakened.)

4. **The ImageNet21k experiment uses a single architecture (ViT-B/16) and a single transfer pipeline.** While this is acceptable, showing the trend holds across architectures or training budgets would substantially strengthen confidence in the generality of the finding.

### Trivial
- The iNaturalist experiment uses ResNet34/50, which are older architectures; it is unclear whether the same pattern holds for modern vision transformers, though the ImageNet21k experiment (using ViT) suggests consistency in the monotonic direction.
- The theoretical analysis does not discuss the role of finetuning in detail, though Theorem 2 mentions it in a footnote.

## Nice-to-Haves
- **Test the hard-sample mechanism directly.** Construct a controlled experiment (e.g., with synthetic data or a dataset where "hard" test samples are defined by the absence of common features) and show that fine-grained pretraining disproportionately benefits those samples. This would close the loop between theory and empirics.
- **Control for samples-per-class in the iNaturalist experiment.** Report per-class sample sizes for each hierarchy level, and if feasible, subsample to equate the average sample count. This would clarify whether the right-side U-shape is due to frivolous details or data-starved training.
- **Analyze how pretraining dataset size interacts with granularity.** The paper notes ImageNet21k has roughly 10× the samples of ImageNet1k but does not disentangle sample size effects from granularity effects. An ablation subsampling leaf-level classes to match coarser-level sample counts would be informative.
- **Relax the easy-only assumption in theory.** Even a preliminary extension (e.g., a small fraction of hard training examples, or a different noise model) would substantially increase the relevance of the theoretical results.

## Removed Points

- **"The theory is nearly a tautology."** — This characterization is overly harsh. The theory formalizes a non-trivial learning dynamics analysis (gradient descent on a two-layer network with cross-entropy loss) under well-specified conditions. While the easy-only assumption simplifies the setting, the proof is not trivial. The substantive concern (limited explanatory value) is preserved in Weakness #1.
- **"Cannot be independently verified" (reproducibility concern about unreleased artifacts).** — No such criticism was made. All models/datasets cited are publicly available.
- **Criticism about missing appendix content or proofs.** — No such criticism was made. The paper's theoretical results are presented in the main text.
- **Formatting/style nitpicks.** — None appeared in the reviewer comments.

## Novel Insights

The review's most useful insight is that the paper's own mechanism — fine-grained pretraining helps specifically on hard test samples — remains untested, creating a disconnect between the theory and the experiments. The theory shows *why* fine-grained labels should help on hard samples, and the experiments show *that* fine-grained labels help overall, but no experiment directly verifies the predicted localization of the benefit. This is a standard theory–experiment gap but worth noting because it is directly addressable. The reviewer's observation about the samples-per-class confound in iNaturalist is also useful: it provides an alternative (partial) explanation for the right-side U-shape that the paper's "frivolous details" interpretation does not fully rule out.

## Suggestions

1. **Calibrate the claims about the theory in the abstract and introduction.** State explicitly that the theoretical result holds for training sets composed only of easy samples, and that extending to mixed training sets is left for future work.
2. **Add a targeted experiment testing the hard-sample prediction.** Even a simple partition of ImageNet1k test samples by prediction confidence or feature strength from a coarse-label-pretrained model would directly test whether fine-grained pretraining disproportionately benefits low-confidence samples.
3. **Report per-class sample counts for each hierarchy level in the iNaturalist experiment** and discuss whether the right-side degradation could be partially explained by data scarcity per class rather than frivolous features.

## Score and Decision

The paper makes a solid contribution to understanding an under-explored aspect of pretraining. Its empirical findings are clean, well-controlled, and practically relevant (validating the common practice of using leaf labels, identifying conditions for success). The theoretical analysis, while limited by the easy-only assumption, provides a useful formal framework and an illustration of the mechanism. The weaknesses are genuine but addressable and do not undermine the core contributions.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>