Now I have a thorough understanding of the paper and all the reviews. Let me synthesize the final consolidated review.

## Summary

The paper proposes extracting object-centric representations by running multi-scale k-means clustering on the patch features of a frozen SSL backbone (e.g., DINOv2). The method produces a set of cluster centroids (object vectors) and their assignment masks, capturing objects and parts at different granularities without any additional training. The paper evaluates on both representation quality (image classification, multi-label classification, video action recognition) and mask quality (unsupervised segmentation), showing that this simple baseline is competitive with or superior to specialized slot-based methods on representation tasks while falling short on standard segmentation protocols.

## Strengths

- **Training-free extraction on SSL backbones achieves strong representation quality.** The paper convincingly demonstrates (Table 1, Figure 2) that k-means centroids from DINOv2 features outperform fine-tuned SPOT slot embeddings on all five classification benchmarks, including multi-label tasks on CLEVR and COCO that require compositional understanding. This is a direct refutation of the assumption that object-centric representations require specialized training.

- **Multi-scale k-means captures part-whole hierarchies without dataset-specific tuning.** Running k-means with K on a geometric progression (1,2,4,...,128) produces segments at multiple granularities (e.g., laptop → screen → keyboard in Figure 1). Under the recall@N protocol (Table 2), this achieves category-level mBO of 47.5 on COCO and 38.5 on ADE20K with 255 masks, surpassing the SPOT ensemble (45.7 and 33.2) which was trained on COCO and thus biased to its annotation granularity.

- **Scaling analysis (Figure 2) cleanly demonstrates the value of object-centric grouping over fixed-grid pooling.** At equivalent token counts (e.g., 9 or 16 tokens), clustering-based tokens consistently outperform average-pooled patch grids across all backbone sizes (ViT-B, L, G) on SUN397 and Places205. This shows the improvement comes from capturing semantic structure, not just adding more tokens.

- **The method preserves backbone embedding quality,** unlike slot-based auto-encoders that degrade it due to compressing both semantic and positional information into low-dimensional vectors. Table 1 shows all SPOT variants perform worse than a linear classifier on the backbone CLS token, while the proposed method improves over it.

- **Video action recognition experiments (Figure 3)** show the method recovers most of the dense-patch performance with 64× fewer tokens (82.8% vs 84.7% on K400 with 256 vs 16,384 tokens), demonstrating a practical compute–accuracy trade-off.

- **Comprehensive backbone ablation (Table 4)** across MAE, CLIP, DINO, DINOv2, and AM-RADIO demonstrates the method is not tied to a specific pre-training objective.

## Weaknesses

### Fatal
None.

### Major

- **The headline comparison to SPOT is confounded by the backbone choice.** The paper's best results use DINOv2, but SPOT cannot be trained on DINOv2 ("failed to converge," as the paper discloses). The DINOv1+Ours row in Table 1 provides a same-backbone comparison, but the paper's narrative ("our approach largely outperforms SPOT") emphasizes the DINOv2 numbers, which are achieved on a backbone inaccessible to the baseline. This makes it impossible to cleanly attribute the improvement to the clustering method versus the stronger backbone features. The paper would be strengthened by a more explicit discussion of the DINOv1-vs-DINOv1 comparison and by scoping claims accordingly.

### Minor

- **The claim that the method "surpasses the performance of fine-tuned object-centric learning methods" (abstract) is too broad.** The paper's own Table 3 shows the method is *consistently worse* than SPOT and DINOSAUR under the standard total-partitioning segmentation protocol. The conclusion is more carefully scoped ("outperforms... in terms of representation quality"), but the abstract gives the impression of an unqualified win. The abstract should be tightened to match the evidence.

- **The mask quality comparison under recall@N (Table 2) uses a non-standard protocol that favors methods producing many masks.** The method produces up to 255 masks per image while slot-based baselines typically predict ≤10. The paper argues this protocol is "more aligned with the goal of object-centric learning," but this claim is under-defended — many practitioners define object-centric learning as producing a *compact* set of semantically coherent tokens. Without showing results for a moderate number of masks (e.g., 16), the segmentation claim remains weak.

- **Missing an all-patches attention-pooling baseline in Table 1.** Figure 2 includes this reference, but Table 1 (the main comparison table) omits it. The reader cannot see the absolute performance gap between the object tokens and the full patch set for the same probe architecture in the primary results. Adding this would contextualize how much information is lost by token reduction.

- **Video action recognition results (Figure 3) compare only against CLS and all-patches baselines, not against any other object-centric method.** The results show that using more tokens (from any source) improves performance, but do not demonstrate that the *clustering-based* object-centric representations are uniquely beneficial for video compared to, e.g., slot-based video models or even random token subsets. This limits the support for claims about video-level superiority.

### Trivial

- The paper describes the attention-pooling classifier as having "a minimal number of trainable parameters" — with 2D² + D·C parameters, this is not as minimal as a linear probe (D·C). The terminology is slightly misleading.
- The dummy mask for the global token (Equation 1) is included in the set but never ablated or analyzed separately.
- The impact of hierarchical vs. direct k-means on representation quality (not just mask resolution) is not evaluated.

## Nice-to-Haves

- Report mask quality (mBO/DetRate) for a moderate number of masks (e.g., 16) under the recall protocol to demonstrate the method does not rely on oversegmentation.
- Add a superpixel baseline (e.g., SLIC + feature averaging) to show k-means clustering is specifically beneficial beyond generic oversegmentation.
- Measure IoU between masks from different K values to quantify whether multi-scale k-means captures distinct objects or redundant partitions.
- Report variance across multiple k-means restarts for representation quality and mask metrics.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"SPOT evaluated on classification is unfair because it was trained for segmentation"** — Removed. The paper's entire point is to evaluate representation quality, which the field has overlooked. Both methods produce set-structured object embeddings; testing them on classification is a symmetric and legitimate comparison. SPOT's own paper claims its slots are useful representations. This is a feature of the evaluation, not a bug.

- **"Mask quality criticism about 255 masks being non-standard"** — Moved to Minor (weakened). The paper honestly presents both protocols. The recall protocol was introduced by Hénaff et al. (2022) in NeurIPS, so it is a published protocol. The criticism is that the paper's defense of it is insufficient, not that the protocol is invalid.

- **"Sensitivity to k-means initialization"** — Removed as a reproducibility nitpick. The paper could add this, but absence does not undermine the results.

- **"Hierarchical k-means impact not evaluated"** — Moved to Trivial. The paper mentions this is for high-resolution masks only; representation quality uses native resolution.

- **Formatting/style nitpicks and missing-appendix concerns** — Removed per hard rules (parser artifacts).

## Novel Insights

The most interesting observation to emerge from these reviews — beyond the paper's own contributions — is the fundamental tension between two competing goals in object-centric learning: (1) producing a compact, semantically coherent set of object tokens for downstream tasks, and (2) producing pixel-accurate segmentation masks. The paper forcefully argues for prioritizing (1) and shows that a crude clustering method excels there while failing at (2). This suggests that the field's heavy investment in complex training procedures to improve mask quality may be partially misplaced if the ultimate goal is representation quality. Whether the community agrees with this re-prioritization or not, the paper provides a valuable stress test. A second insight is that the k-means approach acts as an "upper bound" diagnostic for slot-based methods: since slot attention is a soft approximation of k-means (as the paper notes), any learned slot method that performs worse than hard k-means on representation quality has a genuine problem — its training objective is actively degrading the backbone features rather than improving them.

## Suggestions

1. **Tighten the abstract** to specify that the method surpasses fine-tuned methods *on representation quality (classification) tasks*, not uniformly across all evaluations. The current wording invites readers to infer an unqualified claim that the evidence does not support.

2. **Add an explicit same-backbone discussion**: highlight the DINOv1+Ours vs. SPOT comparison alongside the DINOv2 results, and state directly what gap is attributable to the method vs. the backbone, and what gap remains open because SPOT could not be trained on DINOv2.

3. **Include an "all patches" attention-pooling row in Table 1** so readers can immediately see how much of the dense representation's performance is recovered by the object tokens.

4. **Add a moderate-mask-count segmentation result** (e.g., masks from K ∈ {2,4,8,16}) under the recall protocol to show that the method's segmentation competitiveness does not require 255 masks.

5. **Weaken the claim about the recall protocol being "more aligned with the goal of object-centric learning"** — or defend it with a specific argument about what property of object-centric representations the protocol measures. As written, it reads as opinion and is contested by standard practice in the field.

## Score and Decision

The paper makes a real contribution: it provides a refreshingly simple, training-free baseline for object-centric representation extraction, backed by a broad evaluation across multiple tasks and backbones. The core finding — that k-means on SSL features gives competitive or superior object representations without any training — is important and will likely become a standard reference point. The main weaknesses are overclaiming in the abstract, a backbone confound in the headline comparison to SPOT, and insufficient defense of the non-standard segmentation protocol. These are all addressable with revision. No fatal flaw exists.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>