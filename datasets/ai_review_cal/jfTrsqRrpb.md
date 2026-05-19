- Decision: Reject
- Avg Score: 4.75
- Scores: 3, 5, 6, 5
Now I have all the information needed. Let me write the final consolidated review.

---

## Summary

This paper proposes UDOS (Bottom-Up and Top-Down Open-World Segmentation), a method for open-world instance segmentation that trains a class-agnostic Mask R-CNN with weak supervision from classical bottom-up proposals (e.g., selective search). The network predicts part-masks, which are then grouped into whole objects via affinity-based correlation clustering, and refined by a boundary refinement module. The core idea is that bottom-up proposals provide training signal for unseen objects, while the grouping and refinement stages (trained only on seen-class ground truth) generalize to novel categories. The method is evaluated on five datasets (COCO, LVIS, ADE20K, UVO, OpenImages) and consistently outperforms prior open-world methods (OLN, LDET, GGN).

## Strengths

- **Consistent state-of-the-art performance across multiple benchmarks.** The method outperforms prior SOTA (GGN, OLN, LDET) on cross-category generalization (COCO VOC→nonVOC: 33.5% AR_box, 31.6% AR_mask, +3.5%/+2.5% over GGN), cross-dataset transfer (UVO, ADE20K, OpenImages), and large-taxonomy training (LVIS→COCO). On OpenImages, UDOS achieves 71.6% AR_box100, 7.1% higher than GGN. These results directly support the core claim.

- **Clean and well-motivated integration of bottom-up supervision into top-down learning.** The idea of using one-time offline bottom-up proposals to augment ground-truth labels for training a class-agnostic Mask R-CNN is simple yet effective. The ablation in Table 4 confirms its critical role: removing unsupervised supervision drops mask AR from 31.6% to 6.1%.

- **Affinity-based part grouping demonstrably generalizes to unseen categories.** The grouping module (cosine similarity on expanded ROI features + correlation clustering) is shown to correctly merge parts for novel objects (qualitative in Fig. 5). The ablation (Table 4) shows grouping is essential: without it, mask AR drops from 31.6% to 11.8%.

- **Comprehensive and rigorous evaluation protocol.** The paper evaluates on five diverse datasets covering both cross-category and cross-dataset transfer, including exhaustive-annotation benchmarks (UVO) and large-vocabulary datasets (LVIS, OpenImages). This provides robust evidence of generalization beyond a single benchmark.

- **Minimal inference overhead.** The grouping and refinement add only +0.01s/image compared to Mask R-CNN (0.13s vs 0.12s), making the method practical for deployment.

- **Ablation studies isolate each component's contribution.** The paper systematically ablates the refinement module, proposal ranking (IoU scores), expansion factor δ, and choice of proposal method, with clear trends that validate design choices.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Clustering algorithm details are underspecified for full reproducibility.** The paper states the grouping uses "an off-the-shelf agglomerative clustering algorithm" from scikit-learn (citing bansal2004 correlation clustering) and claims it is "parameter-free." However, it does not specify the exact scikit-learn function call, linkage criterion, or distance threshold used. While the high-level approach (correlation clustering on pairwise affinities) is clear, the implementation details matter for exact reproduction. This is a minor but fixable gap.

- **Training details for the part-mask predictor with unsupervised proposals could be clearer.** The paper specifies that augmented masks \( A = S \cup U \) are used to train the part-mask prediction network and that masks from \( U \) overlapping ground-truth masks with IoU > 0.9 are excluded. However, it does not explicitly describe how the bounding box targets are derived from the unsupervised masks (e.g., tight bounding box from mask), or the exact matching/assignment strategy used during training (standard IoU-based assignment, as in Mask R-CNN). These are standard practice in the field but stating them explicitly would aid reproducibility.

- **No variance or error bars on any main results (Tables 1–3).** Given the relatively small performance differences in some settings (e.g., +1–2% AR), the statistical significance of the gains is unclear. While single-run evaluation is common in this benchmark setting, reporting variance (e.g., across seeds or train/test splits) would strengthen the evidence.

- **Inference post-processing details (NMS thresholds, score thresholds) are not specified.** The paper describes the ranking score \( s = \sqrt[3]{c \cdot b \cdot m} \) but does not state how final predictions are filtered (e.g., NMS IoU threshold, minimum score threshold). This is a small clarity gap for full reproducibility.

- **The refinement module's loss on unseen objects is not discussed.** The paper states the refinement head is trained "exclusively on annotated ground truth instances from \( S \)". This implies that during training, predictions matched to unseen-object proposals receive no refinement loss. This is a reasonable design choice, but the paper could explicitly acknowledge how (or whether) the refinement head receives training signal for unseen objects.

### Trivial
None.

## Nice-to-Haves

- **Ablation replacing part-level affinities with pixel-level affinities** (like GGN) would further substantiate the claim that part-level grouping is superior and not simply a result of the overall framework. The paper correctly draws this distinction in related work but does not experimentally isolate it.

- **Quantitative evaluation of the grouping module's quality** (e.g., clustering purity, adjusted Rand index on seen-class ground truth) would directly validate the claim that "such grouping generalizes well to unseen objects." The qualitative examples in Fig. 5 are useful but isolated.

- **Testing SAM-generated proposals** as a better bottom-up proposal method, as the paper itself suggests as future work, would be a natural extension that could further improve results.

## Removed Points

These points were identified by reviewers but are removed after verification against the paper:

1. **Missing comparison with SAM as a baseline** — SAM is a foundation model trained on 11M images with 1.1B masks; it is not a method trained on the same data or evaluated under the same protocol. The paper treats SAM as complementary/future work, which is appropriate. Prior open-world instance segmentation papers (OLN, GGN, LDET) do not compare to SAM. This criticism reflects scope creep. *Removed.*

2. **Unjustified choice of δ=0.1** — The paper explicitly ablates δ (Table 6) and shows 0.1 achieves the optimum trade-off. Using the same value across datasets is a justified simplification. *Removed.*

3. **Missing comparison with GGN + OLN backbone** — The paper transparently states "we use the result from GGN without the OLN backbone" for fair comparison. This is a deliberate methodological choice, not an omission. *Removed.*

4. **Refinement module training is unclear** — The paper clearly states "We train the refinement head exclusively on annotated ground truth instances from S." This is unambiguous. *Removed (partially kept as a minor clarity point about loss on unseen objects).*

## Novel Insights

None beyond the paper's own contributions. The reviewers did not surface any insight about the paper that the authors did not already articulate.

## Suggestions

1. Specify the exact scikit-learn clustering function, linkage criterion, and any threshold parameters used for the agglomerative/correlation clustering in the grouping module.
2. Clarify how bounding box targets are derived from unsupervised masks and describe the assignment/matching procedure used during Mask R-CNN training with augmented labels.
3. Report variance (e.g., across 3 seeds) on main results to establish statistical significance.
4. Specify NMS and score thresholds used during inference.
5. Consider adding a brief discussion of how (or whether) the refinement module receives training signal for unseen objects during training.
