Now I have a thorough understanding of the paper and can cross-check every claim. Let me produce the consolidated review.

---

## Summary

This paper studies how the granularity of pretraining labels affects the downstream generalization of deep neural networks. The authors provide a theoretical analysis (on a simplified same-distribution setting) proving that coarse-grained pretraining only learns common features, while fine-grained pretraining forces the network to additionally learn rare, fine-grained features — improving accuracy on hard test samples. Empirically, they verify that leaf-level labels on ImageNet21k outperform coarser granularities for transfer to ImageNet1k, and use iNaturalist 2021 to systematically identify conditions (meaningful hierarchy, label alignment) required for effective fine-grained pretraining.

## Strengths

- **Novel theoretical proof linking label granularity to feature learning (Section 4.4).** Theorems 1 and 2 formally establish that coarse-grained training on easy samples fails on hard test samples, while fine-grained training succeeds on both. The multi-view data model with hierarchical feature structure is a clean framework for isolating this mechanism. This is the paper's strongest contribution.

- **Systematic empirical isolation of label granularity on iNaturalist 2021 (Section 5.2).** By holding the input distribution fixed and varying only the pretraining label hierarchy (manual, kMeans-clustered, random), the experiments cleanly attribute performance differences to label granularity and hierarchy quality. The comparison between separate-per-superclass clustering (green curve) and whole-dataset clustering (purple curve) is a clever demonstration that label alignment matters.

- **Cross-dataset validation on ImageNet21k→ImageNet1k (Section 5.1, Table 1).** The results confirm that the community's standard practice (leaf-level pretraining) yields the best accuracy (82.51%), with a clear degradation as granularity coarsens. This provides real-world evidence that the phenomenon extends beyond controlled settings.

- **Clear identification of the operating regime.** The paper documents a U-shaped curve (too few or too many classes hurt), distinguishes meaningful from meaningless hierarchies (manual vs. random/cluster labels), and identifies label alignment as a necessary condition. These practical observations are useful.

## Weaknesses

### Fatal
None.

### Major

1. **Theory and main experiments do not model cross-dataset distribution shift, which limits their explanatory scope for the paper's stated setting.** The theory (Section 4.2, lines 166–167) assumes source and target input samples are generated from the same distribution (footnote 4 explicitly equates the setting to training on two label versions of the same dataset). The iNaturalist experiments (Section 5.2) likewise use identical input samples for source and target (line 256: "set X_src_train and X_tgt_train both equal to the training split"). The paper is *transparent* about this — the iNaturalist figure is captioned "In-dataset transfer" and the conclusion mentions future work on distribution shift — but the overall framing consistently invokes "transfer learning" and the ImageNet21k→ImageNet1k cross-dataset experiment as the motivating example. Consequently, the theoretical mechanism (rare features → better hard-sample accuracy) is convincingly proven only for same-distribution settings, and the conditions (meaningful hierarchy, label alignment) are demonstrated only when there is no domain shift. The paper's contribution would be more accurately scoped as *understanding the effect of label granularity on hierarchical classification tasks*, not on cross-dataset transfer learning broadly. This is a nontrivial gap between the paper's framing and its actual validation.

2. **The ImageNet21k→ImageNet1k result, which is the paper's only cross-dataset evidence, is empirically thin.** Table 1 reports a single run per hierarchy level with no variance, confidence intervals, or statistical significance. The baseline (77.91%) is taken from the ViT paper rather than reproduced under the same pipeline, introducing uncontrolled differences. Only one architecture (ViT-B/16) and one target dataset (ImageNet1k) are tested, with no ablation. While the trend is consistent with existing practice, the evidence is not strong enough to constitute a novel empirical finding about cross-dataset transfer. The paper would benefit from multiple seeds, at least one additional source-target pair, or another architecture.

### Minor

1. **Limited analysis of the U-shaped curve's cause.** The paper attributes the high error at extreme granularity (e.g., one label per sample) to "frivolous details" (line 267) but provides no corroborating analysis — no feature visualizations, validation loss curves, or ablation isolating where the degradation comes from. The observation is useful, but the mechanism remains speculative.

2. **Single-source theoretical setup (2 superclasses, 2 hierarchy levels).** The theory considers only two levels of hierarchy and one feature per class. The paper claims extension is easy (footnote 1, line 130), but the analysis leaves the reader uncertain about how the results generalize to deeper hierarchies or multiple features per class.

### Trivial
None.

## Nice-to-Haves

- Additional cross-dataset transfer experiments (e.g., ImageNet21k → Places365, or iNaturalist → any other dataset) would substantially strengthen the paper's claim that its findings generalize beyond same-distribution settings.
- Feature-level analysis (e.g., probing which features are learned under different granularities) would deepen the understanding of the U-shaped curve.
- Multiple training seeds for the ImageNet21k→ImageNet1k results would add basic statistical grounding.

## Removed Points

These points are flagged to be removed, treat them with caution:

1. **Critic's claim that "the paper does not acknowledge that these experiments are not cross-dataset transfers" (from Critical Issue #2):** The paper explicitly labels the iNaturalist experiments as "In-dataset transfer" in Figure 3 (line 249) and explains the deliberate design choice (line 258). This claim is factually incorrect and is removed.

2. **Critic's claim that the theory is "not a transfer learning scenario" (from Critical Issue #1, first sentence):** Changing the label granularity while keeping the same data IS a form of transfer learning (different task, same domain). The paper studies this setting and is transparent about it. Labeling it "not transfer learning" is an overstatement.

3. **Strength Finder's strength #4 (Definitions 3.1–3.4 capture hierarchical structure):** While this is a reasonable supporting point, it overlaps substantially with strength #1 (the theoretical proof) and is better subsumed under it. Moved here for conciseness.

4. **Strength Finder's strength #5 (systematic experimental design isolates label granularity):** This is valid but is already captured in the systematic iNaturalist discussion under Strengths #2. Kept in the main review implicitly.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a genuinely novel observation that the paper itself does not already articulate.

## Suggestions

- Reframe the contribution to honestly reflect the scope: the theory proves that fine-grained labels help learn rare features *in a same-distribution hierarchical classification setting*, and the iNaturalist experiments validate conditions for effective fine-grained pretraining *in the absence of domain shift*. The cross-dataset ImageNet21k→ImageNet1k result should be presented as a corroboration of the theoretical intuition under real-world conditions, not as the primary object of explanation.
- Add at least one more cross-dataset transfer experiment (even a simple one) and multiple seeds for the ImageNet21k→ImageNet1k result.
- Include a brief analysis of the U-shaped curve (e.g., feature visualizations or a diagnostic with validation loss per granularity level) to move from speculation to evidence.
- If the paper is not extended to cross-dataset settings, consider a title change from "transfer learning" to something like "hierarchical classification" or "label granularity in pretraining" to avoid misleading readers.

**Evaluation axes:**

- **Originality:** Moderate. The theoretical formalization of label granularity's effect on feature learning is novel. The empirical findings largely confirm existing practice.
- **Importance of research question:** High. Understanding why fine-grained labels help is practically relevant.
- **Claims supported by evidence:** Partially. The theory is well-supported in its simplified setting. The empirical conditions are well-supported in same-distribution experiments. But the cross-dataset framing significantly outstrips the evidence provided.
- **Soundness of experiments:** The iNaturalist experiments are well-designed. The ImageNet21k→ImageNet1k experiment lacks variance and baselines.
- **Clarity of writing:** Clear. The paper is well-structured and transparent about its assumptions.
- **Value to community:** The theoretical insights and practical conditions (meaningful hierarchy, label alignment) are useful, but the gap between framing and evidence limits the paper's impact as a standalone contribution.

## Score and Decision

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>