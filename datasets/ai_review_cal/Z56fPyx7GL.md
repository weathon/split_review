- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 3, 5, 3
Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper proposes a remarkably simple method for object-centric representations: running multi-scale k-means on frozen SSL backbone patch features (e.g., DINOv2). The method is training-free, backbone-agnostic, and produces overlapping masks at multiple granularities. On downstream classification tasks (ImageNet, SUN397, Places205, CLEVR, COCO), the clustering-based representations outperform the current state-of-the-art trained slot-based method (SPOT) by substantial margins. The method is also competitive on unsupervised segmentation under the recall@N protocol, though it underperforms under the total-partitioning protocol — a tradeoff the paper openly acknowledges. The core challenge to the community: the field may be over-investing in complex slot-training pipelines when frozen SSL features plus k-means already produce superior object embeddings.

---

## Strengths

1. **Clustering-based representation outperforms fine-tuned slot methods on downstream tasks.** Table 1 shows the proposed method surpasses SPOT across all five classification benchmarks by 2–13% margin using both DINO and DINOv2 backbones. This directly supports the claim that training-free clustering preserves backbone embedding quality better than slot-based auto-encoding.

2. **Multi-scale k-means captures part-whole hierarchies that slot methods cannot represent.** Section 3.3 describes running k-means with geometrically increasing K (e.g., K ∈ {1,2,4,…,128}) to produce overlapping masks at different granularities. Figure 1 visually demonstrates this (laptop → screen + keyboard). The paper correctly notes (Section 3.2) that slot-based methods use argmax attention maps that enforce hard pixel-to-slot assignments, precluding such part-whole overlap.

3. **Training-free and backbone-agnostic flexibility.** Table 4 shows the method works with five different SSL backbones (DINOv2, DINO, MAE, CLIP, AM-RADIO) without re-training or dataset-specific tuning. This flexibility contrasts with slot-based methods that require per-dataset fine-tuning (Section 4.2).

4. **Efficient video action recognition with orders-of-magnitude token reduction.** Figure 3 shows that S₁₆ (256 tokens for 16 frames) recovers 97.8% of top-line K400 accuracy and 92.3% of SSv2 accuracy while using 64× fewer tokens than the full-patch baseline (256 vs. 16,384). This concretely demonstrates the practical value of compact object-centric representations.

5. **State-of-the-art unsupervised segmentation under the recall@N protocol.** Table 2 reports mBOᶜ of 33.8 and DRateᶜ of 38.1 on COCO 2017 (DINOv2 ViT-B/16), surpassing both ODIN (27.4/30.3) and SPOT ensemble (30.7/33.7). Notably, these results come from frozen features with simple clustering, whereas baselines require task-specific training.

6. **Scalable performance with backbone size.** Figure 2 shows classification accuracy on complex tasks (Places205, COCO multi-label) improves monotonically as the DINOv2 backbone scales from base to giant. The 512-token object-centric representation matches the full dense representation (2,576 tokens) on Places205, confirming effective leverage of stronger backbones with no added overhead.

---

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Self-trained SPOT baselines lack training details.** The paper compares against 8-slot and 16-slot SPOT models trained by the authors using the official code, but reports no training hyperparameters (epochs, learning rate, convergence criteria) or validation curves (lines 102–103). The large performance gap (e.g., 80.0% vs. 66.6% mAP on COCO with DINOv2) invites the question of whether the self-trained SPOT models are undertrained. This concern is partially mitigated by the open-source 7-slot SPOT checkpoint also underperforming, and by the paper's note that "we also attempted to train SPOT with DINOv2, but it failed to converge." However, providing training details or variance across runs would substantially strengthen the comparison.

2. **Missing all-patches attention-pooling baseline in Table 1.** The "all patches" baseline (attention-pooling on 256 tokens) appears in Figure 2 (scaling experiments) but not in the main Table 1. Without it, the reader cannot directly judge how much of the gap between the proposed method and SPOT is simply attributable to using a stronger classifier or more tokens. Including this baseline in Table 1 would sharpen the paper's central argument that clustering-based tokens recover most of the dense upper-bound performance.

3. **No estimate of variance or statistical significance for classification results.** Many numbers in Table 1 are close (e.g., 80.0 vs. 79.5 mAP on COCO with DINOv2). The paper reports single runs without variance estimates across classifier training runs. While single-run probing is common practice in SSL evaluation, brief variance reporting would help assess whether small gaps are meaningful.

4. **Computational cost of multi-scale k-means is stated but not quantified.** The paper says the overhead is "negligible w.r.t. the backbone" (line 174) but does not report wall-clock time relative to the backbone forward pass, even for a single image. A short quantification would help practitioners assess the practical trade-off.

### Trivial

1. **Query vector initialization in Eq. 2 not specified.** The paper states that q, W^{key}, W^{value}, and W^{out} are "learnable parameters trained by gradient descent" (line 93) but does not describe how q is initialized. This is a minor reproducibility detail.

---

## Nice-to-Haves

- **Analysis of why SPOT embeddings degrade.** The paper attributes degradation to "compression of semantic and positional information into small-dimensional vectors" (Section 3.2). An analysis measuring reconstruction loss vs. embedding quality, or showing that slot embeddings compress positional information that hurts classification, would deepen the paper's own argument.
- **Qualitative failure cases for mask quality.** Figure 4 shows k-means masks have noisy boundaries. A few examples where clustering fails entirely (e.g., grouping disparate objects into one cluster) would help calibrate expectations.
- **Ablation of the number of hierarchical k-means steps.** The paper uses a geometric progression K ∈ {1,2,4,…,128} for segmentation. An ablation testing different progressions (e.g., denser or sparser) would help understand sensitivity to this design choice.

---

## Removed Points

- **"Claim that object-centric methods overlook representation quality is overstated"** — The Harsh Critic acknowledged this is "defensible," and the paper uses the word "mostly" (line 16), which is appropriately qualified. This is a framing opinion, not a substantive weakness.
- **"K-means mask quality criticisms that demand pixel-perfect masks"** — The paper explicitly acknowledges its masks are noisy (Section 4.2, Figure 4, line 172: "our method... produces noisier masks") and argues this is an acceptable trade-off. Criticizing it as a weakness would be re-asserting something the paper already concedes.

---

## Novel Insights

The most striking insight from reading the reviews together is that the paper's core weakness — its simplicity — is also its greatest strength. The Harsh Critic's main concern (SPOT might be undertrained) and the missing-baseline concern are both, at root, about whether the comparison is too flattering to the proposed method. But the paper's own narrative consistently frames the comparison favorably precisely because the method is *so simple* that it needs no training, no tuning, no dataset-specific configuration. This tension — "is this too good to be true?" — is exactly the productive discomfort the paper aims to create. The reviews converge on the same conclusion: the paper's claims are well-supported, the method is clearly described, and the remaining concerns are about tightening an already-strong comparison rather than fixing a broken one.

---

## Suggestions

1. **Add the all-patches attention-pooling baseline to Table 1.** This directly addresses the most common question a reader will have: how close does clustering get to the dense upper bound?
2. **Provide SPOT training details in the appendix** — hyperparameters, number of epochs, and a statement about convergence — to rule out undertraining as an explanation for the performance gap.
3. **Add a brief statistical note** (variance over 3 classifier training seeds) for the key comparisons in Table 1.
4. **Quantify k-means overhead** with a single wall-time measurement (e.g., "k-means for K ∈ {1,...,128} adds X ms on top of Y ms backbone forward pass").

---
