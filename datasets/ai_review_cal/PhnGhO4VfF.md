- Decision: Reject
- Avg Score: 5.67
- Scores: 6, 5, 6
Now I have all the information needed. Let me write the final consolidated review.

---

## Summary

This paper studies how pretraining label granularity affects transfer learning performance in image classification, focusing on the fine-to-coarse setting. It provides a theoretical analysis in a simplified hierarchical-feature model showing that coarse-grained pretraining fails to learn rare features while fine-grained pretraining succeeds, and conducts empirical experiments on ImageNet21k→ImageNet1k and iNaturalist 2021. The key empirical finding is that leaf-level pretraining on ImageNet21k yields best transfer accuracy, and the iNaturalist experiments reveal a U-shaped curve where intermediate granularities outperform both too-coarse and too-fine labels, with the additional insight that label hierarchy meaningfulness and source-target label alignment are critical.

## Strengths

1. **Systematic iNaturalist 2021 study isolating conditions for effective fine-grained pretraining** (Section 5.2, Figure 2). The experiments compare manual hierarchy, kMeans-per-superclass (aligned), kMeans-whole-dataset (misaligned), random labels, and the label-per-sample extreme. This design cleanly separates the effects of granularity from the effects of hierarchy meaningfulness and label alignment. The finding that manual hierarchy outperforms all alternatives but exhibits a U-shaped curve as granularity increases is a nuanced, non-obvious result that goes beyond a naive "finer is always better" narrative.

2. **Large-scale empirical validation on ImageNet21k→ImageNet1k** (Section 5.1, Table 1). ViT-B/16 finetuning accuracy decreases monotonically from 82.51% (21,843 leaf classes) to 72.75% (38 coarse classes), with a clear advantage over the 77.91% baseline. This confirms the phenomenon on a widely-used benchmark at practical scale.

3. **Theoretical result establishing a formal link between label granularity and feature learnability** (Theorems 4.1–4.2). The analysis shows that, under a hierarchical data model, coarse-grained pretraining provably fails on hard test samples lacking common features, while fine-grained pretraining succeeds. This formalizes an intuitive explanation for why fine-grained labels help, going beyond prior theoretical work that studied simplicity bias without examining the granularity-specific transfer mechanism.

4. **Discovery of the U-shaped granularity effect** (Figure 2). The finding that error decreases then increases as granularity grows provides practical guidance for choosing an appropriate granularity, and the paper identifies that label-per-sample pretraining (red star) actually hurts performance — a counterintuitive result.

## Weaknesses

### Fatal
None.

### Major
None. The core claims are supported by the evidence provided, and no weakness identified undermines the paper's central conclusions.

### Minor

1. **Several experimental details are not reported, reducing reproducibility.** (a) The "mini version" of the iNaturalist 2021 training set is used throughout but its size is never stated (Section 5.2, paragraph 2). This matters because the U-shaped curve at very fine granularities could be influenced by overfitting when class samples become scarce. (b) The kMeans clustering experiments do not specify the number of clusters used at each granularity level, making it impossible to assess whether the comparison with manual hierarchy levels is on equal footing. (c) The paper states "We experiment with ResNet 34 and 50 on this dataset" (line 262) but only shows ResNet34 results without explanation. These are all addressable in a revised version.

2. **The theoretical explanation is slightly overclaimed relative to the evidence.** The abstract and contributions (lines 7, 45) say the theory "explains" the benefit of fine-grained pretraining, but the theoretical model makes strong assumptions (orthonormal dictionary features, two-layer network with frozen second-layer weights, no hard training examples, no distribution shift). The paper acknowledges this gap (lines 193–194: "Our theoretical result is intended to present the 'feature-learning bias'...in an exaggerated fashion"), but the language of "explanation" overstates what is better described as a theoretical intuition or illustration in an idealized setting. The theory is consistent with the empirical observations and provides useful intuition, but it does not constitute an explanation of the real-world phenomenon.

3. **Theorems 4.1 and 4.2 are presented only as summaries in the main text.** The statements use informal phrases like "with proper choice of step size η" and probability bounds written as o(1)/Ω(1) without specifying the implied constants or the meaning of "with high probability." While this is standard practice for main-text theorem summaries (with full formal statements presumably in the appendix, which was stripped by the parser), the main-text presentation is too imprecise for a reader to fully assess the theoretical contribution without the appendix.

### Trivial
None.

## Nice-to-Haves

- A formal perturbation analysis or discussion of how the theory's conclusions change when a small fraction of hard training samples is included would strengthen the bridge between theory and practice. The paper currently mentions this as left for future work.
- Adding cross-dataset transfer experiments (e.g., pretrain on iNaturalist fine labels and test on a different coarse-labeled dataset) would test generality beyond the in-dataset design, though the current design is reasonable for isolating label granularity as a causal factor.
- A brief discussion of the computational cost implications of finer-grained pretraining (larger final linear layer, slower training) would be useful for practitioners.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Leaf-level pretraining result is not novel"** (Harsh Critic, Issue 4). The paper explicitly frames the ImageNet21k→ImageNet1k result as "support[ing] the common practice used in the community" (lines 6, 47). It does not claim this as a novel finding. The novelty resides in the theoretical analysis and the systematic iNaturalist study. This is a strawman criticism.

- **"The gap between theoretical setting and real problem is so large that the theory provides at best a suggestive parable"** (Harsh Critic, Issue 2 — in its strongest wording). The paper devotes a full paragraph (lines 193–194) to acknowledging this gap explicitly, describing the theory as "an exaggerated fashion" of feature-learning bias. The criticism as stated ignores these qualifiers. The softened version of this concern is retained in Weakness #2 above (slight overclaim).

- **Several sub-claims in the harsh critic's Issue 1 are factually incorrect.** The critic states the theorems do not specify what asymptotics are with respect to — but the paper clearly states "all our asymptotic statements are made with respect to d" (line 125). The critic states the theorems do not state "the probability that holds with high probability" — but the paper states "With high probability" in the theorem body (line 185), which is standard terminology. The footnote example of f(σ_ζ) = d^{0.4} is provided. The valid core concern (informal presentation) is retained in Weakness #3.

- **Criticism about comparison not being perfectly controlled because x-axis positions differ** (Harsh Critic, Section-by-Section Notes). This is speculative and not clearly supported by the paper's description of the experimental design.

## Novel Insights

None beyond the paper's own contributions. The reviewers did not surface any observation about the paper that the authors themselves had not articulated.

## Suggestions

1. Report the size of the iNaturalist "mini" training set, the number of clusters used in kMeans at each granularity level, and clarify whether ResNet50 results were omitted for space or did not differ materially from ResNet34.
2. Reframe the theoretical contribution's language from "explains" to something like "provides a theoretical intuition consistent with" or "offers a formal illustration in an idealized setting that parallels," to better match the evidence level.
3. If space permits, include a brief formal statement of at least one theorem in the main text (with full details deferred to appendix) so that a reader can see the precise conditions and conclusions without consulting the supplement.
