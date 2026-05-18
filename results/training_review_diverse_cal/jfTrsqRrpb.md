Here is my final consolidated review.

---

## Summary

This paper proposes UDOS, a framework for open-world instance segmentation that trains a Mask R-CNN with weak supervision from unsupervised bottom-up segmentations (e.g., Selective Search). The trained network predicts part-level masks, which are then merged into complete object instances via a lightweight affinity-based agglomerative clustering module and refined by a jointly trained refinement head. The method achieves state-of-the-art results across five datasets (COCO, LVIS, UVO, ADE20K, OpenImages) on cross-category and cross-dataset generalization, consistently outperforming prior methods OLN, LDET, and GGN by sizable margins (e.g., +8.0% mask AR on VOC→NonVOC over GGN).

## Strengths

- **Part-level affinity grouping that generalizes to unseen categories.** The paper demonstrates that learning to group part-level mask predictions via pairwise cosine similarity on expanded RoI features, followed by agglomerative clustering, generalizes effectively to objects never seen during training. This is a meaningful departure from pixel-level affinity grouping (GGN) and is supported by quantitative results (Tables 2, 4) and qualitative visualizations (Figure 5, Figure 6), showing correct grouping on novel objects from UVO.

- **Consistent and substantial SOTA results across multiple benchmarks.** UDOS outperforms all baselines and prior open-world methods (OLN, LDET, GGN) on every evaluation setting: VOC→NonVOC (31.6% AR_M^{100} vs. 23.6% GGN), COCO→UVO (39.4% vs. 34.4% GGN), COCO→ADE20K, COCO→OpenImagesV6 (66.2% AR_M^{100} vs. 61.4% GGN), and LVIS→COCO. The gains are consistent and non-trivial in magnitude.

- **Thorough ablation studies validating each design choice.** Table 5 shows the grouping+refinement pipeline raises mask AR from 11.8% (no grouping) to 31.6%. Additional ablations cover the context expansion factor δ (Table 6), IoU scoring functions (Table 7), and proposal generation methods including uniform grids, SSN, SS, and MCG (Table 8). Every design choice is supported by evidence.

- **Practical training and inference setup.** The unsupervised part-masks are generated once offline (1.5 CPU-days for COCO) and are not needed at inference. The grouping module adds only 0.01s/image overhead (0.13s vs. 0.12s for OLN). This makes the method practical for deployment.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **Novelty framing overstates relative to GGN.** The paper claims to be "the first approach that effectively combines top-down architecture and bottom-up supervision into a unified framework for open-world instance segmentation" (p.3). However, GGN (Wang et al., 2022) already combines bottom-up grouping (pixel-level pairwise affinities) with a top-down detection backbone in an end-to-end trainable system. The paper does acknowledge GGN and correctly notes that its own contribution is *part-level* (rather than pixel-level) affinity grouping with "fundamentally different grouping principles." But describing this as the "first" combination is overstated. The contribution is better framed as a novel and more effective *variant* of bottom-up + top-down integration, not the invention of the paradigm itself. This is a framing issue, not a flaw in the method, but it should be corrected.

- **Non-exhaustive annotation in the VOC→NonVOC evaluation is acknowledged but not fully discussed.** The paper notes that COCO has non-exhaustive annotations and states that AR^{100}/AR^{300} mitigates this (p.6). However, the specific VOC→NonVOC setting inherits this issue: valid NonVOC objects present in images but unlabeled in COCO can distort recall-based evaluation. The paper correctly evaluates on UVO and ADE20K (which have exhaustive annotations) for the cross-dataset setting, which addresses this concern for those benchmarks. But the paper should more explicitly discuss this limitation for the VOC→NonVOC numbers and note that while relative comparisons across methods using the same protocol are fair, the absolute AR values should be interpreted with caution.

- **Limited analysis of why the refinement module generalizes to unseen objects.** The refinement head is trained exclusively on seen-class annotations yet improves boundary quality on unseen objects (Table 5). The paper does not analyze whether this is because the refinement head learns a class-agnostic boundary-smoothing function, because backbone features are generic enough, or something else. An experiment (e.g., before/after visual comparisons, or testing with a refinement head trained on synthetic edges) would strengthen the mechanistic claim.

- **No comparison to a learned grouping alternative.** The grouping module uses parameter-free agglomerative clustering with cosine similarity. The paper acknowledges this as a limitation and identifies learnable grouping as future work (p.10), but a brief comparison to a simple learned alternative (e.g., an MLP predicting merge probabilities) would give the reader a more complete picture of the tradeoffs.

### Trivial

- The paper mentions that AR^{100}/AR^{300} metrics "avoid penalizing predictions of valid, yet unannotated, objects" (p.6). This is somewhat imprecise — AR is recall-based and does not directly penalize extra detections, but unannotated objects in the top-N set can still displace correctly-detected annotated objects. The intended meaning is clear, but the phrasing could be tightened.

## Nice-to-Haves

- Report performance on seen categories separately (e.g., mask AR on VOC classes) to verify that the inclusion of noisy part-mask supervision does not degrade seen-class segmentation. If there is no degradation, this strengthens the paper.
- Provide an explicit comparison to pixel-level affinity grouping (as in GGN) under the same backbone and training conditions, controlling for all factors except grouping granularity. Currently, the comparison to GGN uses published numbers with possibly different backbones.
- Report the average number of proposals produced by the grouping module per image and how the 100/300 proposal limit affects the final results, which is standard for proposal-based methods.
- Include failure-mode analysis beyond the single example in Figure 6 — e.g., what fraction of grouped masks are impure, and how often does oversegmentation of similar objects occur?
- Analyze the learned feature space (e.g., t-SNE of RoI features for seen/unseen parts) to more concretely demonstrate that cosine similarity captures object identity even for unseen categories.

## Removed Points

These points were raised by reviewers but are removed from the main assessment after verification:

1. **"Use of selective search masks in training is not novel per se"** — Removed because the paper does not claim novelty of Selective Search itself. It is presented as a tool, and the paper shows that using SS alone (Mask R-CNN_{SS}) performs poorly (11.8% AR), making the full pipeline's contribution clear. This is a strawman criticism.

2. **"The paper should test the effect of different proposal generators"** — Removed because the paper already does this (Table 8, ablating uniform grids, SSN, SS, and MCG as proposal generation methods). The suggestion is already addressed.

3. **"Average Recall computed against incomplete ground truth can be misleading: a model that detects a valid but unlabeled object will be penalized (counted as a false positive)"** — Partially removed because this mischaracterizes AR. AR is recall-based (TP/(TP+FN)); detecting an unlabeled object does not directly count as a false positive in the recall computation. The underlying concern about incomplete GT data is real and is preserved in the Minor weaknesses. The specific "counted as a false positive" claim is factually incorrect for AR and is removed.

4. **Pure formatting/style nitpicks** — None present in the reviews.

## Novel Insights

The reviews surface an interesting tension: the paper's claimed "first" combination of top-down and bottom-up approaches is challenged by GGN, but the specific mechanism — using *part-level* rather than *pixel-level* affinity, learned via weak supervision from over-segmented bottom-up proposals — is genuinely novel and empirically superior. This suggests that the granularity of the bottom-up signal (part-level vs. pixel-level) is a critical design dimension for open-world generalization, and that coarse over-segmentation may actually be a feature, not a bug, of the training supervision. The consistent 5–8 point gains over GGN across all five benchmarks are hard to attribute to implementation details alone and point to a genuine architectural advantage worth deeper mechanistic investigation.

## Suggestions

1. **Reframe the novelty claim.** Replace "the first approach that effectively combines top-down architecture and bottom-up supervision" with phrasing that acknowledges GGN's prior combination while emphasizing the novel contribution of part-level (vs. pixel-level) grouping and weak-supervision training from bottom-up proposals. For example: "We introduce a novel approach that integrates top-down learning with weak supervision from bottom-up segmentations, using part-level affinity grouping — differing fundamentally from prior pixel-level grouping methods such as GGN."

2. **Add a brief discussion of the non-exhaustive annotation limitation** for the VOC→NonVOC setting specifically, noting that while relative comparisons are valid (all methods use the same evaluation protocol), the absolute AR figures may be affected by missing annotations for NonVOC objects.

3. **Add a simple analysis of the refinement module's generalization** — e.g., a visual comparison of refinement before/after on unseen objects, or testing the refinement head on synthetic boundary data — to support the claim that boundary refinement is class-agnostic.

4. **Consider a one-paragraph failure analysis** documenting the fraction of grouped masks that are pure vs. impure, and the most common failure modes (undersegmentation of distinct objects vs. oversegmentation of a single object).

## Score and Decision

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>