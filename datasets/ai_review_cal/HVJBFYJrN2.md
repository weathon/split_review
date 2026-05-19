- Decision: Reject
- Avg Score: 5.25
- Scores: 6, 5, 5, 5
Now I have the full picture. Let me produce the final consolidated review.

## Summary

This paper proposes STARS, a two-stage self-supervised framework for skeleton-based action recognition. Stage 1 uses MAMP (a masked autoencoder) to pretrain a ViT encoder; Stage 2 performs lightweight contrastive tuning (20 epochs) via NNCLR on the encoder's top half, without hand-crafted data augmentations. The key findings are that MAE-based methods produce poorly-separated clusters and struggle in few-shot settings, and that a short contrastive tuning stage remedies this while preserving within-dataset performance. STARS achieves state-of-the-art results on linear evaluation and KNN protocols across NTU-60, NTU-120, and PKU-MMD, and delivers large gains in few-shot settings (63.5% vs. 47.6% for MAMP in 1-shot). However, it does not improve over MAMP in full fine-tuning, and the claimed training efficiency advantage is not adequately documented.

## Strengths

- **Large few-shot improvements over MAE baselines**: Table 6 (tab:fewshot) shows STARS raises 1-shot accuracy from 47.6% (MAMP) to 63.5%, and 5-shot from 48.4% to 65.7% (pretrained on NTU-60, tested on 60 novel NTU-120 actions). This directly validates the paper's core motivation that MAE features lack generalizability in low-data regimes and that contrastive tuning fixes it.

- **State-of-the-art linear evaluation without hand-crafted augmentations**: Table 1 (tab:linear-eval) shows STARS achieves 87.1%/90.9% on NTU-60 XSub/XView and 79.9%/80.8% on NTU-120 XSub/XSet, outperforming all prior contrastive and MAE methods, while the contrastive tuning stage uses no data augmentations. The gap over MAMP (84.9%/89.1% on NTU-60) is substantial and consistent across benchmarks.

- **Empirically demonstrated cluster separation improvement**: Figure 6 (fig:tsne) provides t-SNE visualizations showing that STARS produces clearly separated clusters with smaller intra-class spread and larger inter-class margins compared to MAMP, directly supporting the claim that contrastive tuning enhances semantic clustering. The qualitative evidence is convincing.

- **NNCLR is shown to be the most effective contrastive objective for this setting**: Table 3 (tab:ablation-strategy) compares NNCLR, DINO, and MoCo under identical conditions; NNCLR achieves 81.9% KNN accuracy (NTU-60 XSub) vs. 77.6% (DINO) and 72.2% (MoCo), even though DINO and MoCo are tested with augmentations. This is a non-trivial finding that goes beyond simply "adding a contrastive loss."

- **Thorough ablation of key design choices**: The ablation on layer-wise learning rate decay (Fig. 5a), queue size (Fig. 5b), augmentation effects (Table 4), and tuning strategies (Table 3) provides a clear picture of why the method works and which hyperparameters matter.

## Weaknesses

### Fatal
None.

### Major

- **The training efficiency claim in Figure 1 is insufficiently documented**: The figure caption states training time is "evaluated on a single NVIDIA GeForce RTX 3090 GPU," but line 144 reports all pretraining used "four NVIDIA A40 GPUs." It is not explained whether Figure 1 reports a separate single-GPU timing benchmark (which would be a fair relative comparison across methods) or whether it extrapolates from the actual 4-GPU setup. More critically, the paper never states whether the plotted STARS time includes both the MAE stage (~300 epochs on 4 GPUs, following MAMP) and the contrastive tuning stage (20 epochs), or only the second stage. Since the paper's motivation emphasizes that STARS "requires significantly less resources" (line 29), this ambiguity undermines a central claim. The paper should clarify the exact breakdown and hardware used; if the advantage only holds when starting from a public MAMP checkpoint and only counting the tuning stage, that should be stated explicitly.

- **Fine-tuning shows no improvement, narrowing the contribution substantially**: Across all fine-tuning evaluations (Table 5, tab:finetune-eval), STARS essentially matches MAMP (93.0 vs. 93.1 on NTU-60 XSub; 89.9 vs. 90.0 on NTU-120 XSub; STARS-3stage shows a marginal 93.2 vs. 93.1). The paper acknowledges this in the conclusion (line 397) but does not analyze *why* the benefit disappears when the full encoder is fine-tuned. Since fine-tuning is the most commonly used evaluation protocol for self-supervised skeleton-based methods, this is a significant structural limitation. A discussion of whether the contrastive tuning is overwritten during fine-tuning, or why linear separability improves but fine-tuning initialization does not, would meaningfully strengthen the paper.

### Minor

- **The claim that STARS works "without hand-crafted data augmentations" is underexplained**: NNCLR in the image domain relies heavily on augmentations to create meaningful positive pairs. Here, positives come from nearest neighbors in a queue populated by single-view samples from earlier batches. The paper does not analyze what these nearest neighbors correspond to — are they predominantly same-class samples? Do failure cases (cross-class nearest neighbors) occur, and what effect does the contrastive loss then have? Table 4 shows augmentations add only minor benefit (85.0 with spatial flip vs. 84.5 without), which empirically defends the claim, but a qualitative analysis of the queue's nearest-neighbor behavior would provide the missing mechanistic understanding.

- **The "Masked Prediction + Contrastive Learning" category in all results tables contains only STARS variants**: The paper discusses MAE-CT and other image-domain sequential MAE+contrastive methods in the related work (Section 2), but no existing combined approach is adapted or baselined on skeletons. Even a brief discussion of why these methods do not transfer directly to the skeleton domain would help situate STARS's novelty. As it stands, the combined-method category reads as a single-data-point comparison.

- **STARS-3stage vs. STARS distinction is not sufficiently explained in the main text**: Line 193 mentions that STARS-3stage has a "Head Initialization" stage followed by contrastive tuning, then defers to the supplementary. The main text should briefly describe what the head initialization does and why it sometimes performs differently (e.g., fine-tuning: 93.2 vs. 93.0 for STARS; few-shot: 59.3 vs. 63.5 for STARS). The discrepancy matters for understanding the method.

- **No standard deviations or multiple-seed results reported**: Given the small differences between MAMP and STARS in fine-tuning (sometimes <0.2%), single-run results cannot distinguish signal from noise. While this is standard practice for large-scale benchmarks in the field, the paper would be stronger with variance estimates, especially for the fine-tuning and transfer tables where margins are thin.

### Trivial

- **"Second-half of the encoder parameters" (line 119) is ambiguous**: With a ViT of 8 blocks, specifying that layers 5–8 are tuned (or equivalently, decay is applied starting from the last 4 blocks) would be clearer.

- **The paper says "second stage" training uses "4 NVIDIA A40 GPUs" (line 144) but Figure 1 evaluates on "a single RTX 3090"**: The discrepancy is not explained and should be reconciled with a brief note (e.g., "Figure 1 reports a separate timing benchmark on a single GPU for fair comparison across methods").

## Nice-to-Haves

- **Adapt and compare against at least one existing sequential MAE+contrastive method (e.g., MAE-CT) on a skeleton benchmark** to directly demonstrate STARS's advantages over the closest image-domain counterpart.
- **Probe representation at different layers before and after contrastive tuning** to explain why linear evaluation benefits but fine-tuning does not.
- **Run the few-shot evaluation with episodic training (support/query splits)** to align with the standard few-shot literature and confirm that the n-NN protocol's results are not an artifact of the simplified evaluation.

## Removed Points

**These points are flagged to be removed; treat them with caution.**

1. **Criticism that MAE-CT comparison is a "missing related work"** — The paper already cites MAE-CT in Section 2. The issue is about a missing *baseline comparison*, not a missing citation. I re-classified this as a minor weakness (not removed entirely) rather than a missing-citation complaint.

2. **Criticism that "more details in supplementary" is a weakness** — Per the instructions, parser-stripped appendix content exists in the original submission. I retained the spirit of the criticism (the main text could briefly clarify the STARS vs. STARS-3stage distinction) but removed the framing that the paper is deficient because details are in the supplementary.

3. **Strength Finder's strength #4 (training efficiency advantage)** — This strength conflicts with the verified weakness that the efficiency claim is inadequately documented. Per rules, when a strength and weakness disagree, the weakness wins. I kept a qualified reference to it under Strengths (since the data does exist and the relative ordering may hold) but caveated it in the Major weakness section.

4. **Pure formatting/style nitpicks from the Harsh Critic** (e.g., the reviewer's note about "the notation for the second stage uses NNCLR but the loss in Eq. 5 is the standard InfoNCE-style loss" — this is neither a problem nor incorrect; NNCLR uses InfoNCE with nearest-neighbor positives). Removed.

5. **The Harsh Critic's speculation that "the queue provides enough diversity after MAE pretraining"** — This is a hypothesis, not a grounded criticism of a specific paper deficiency. Removed from weaknesses; it is now implicitly addressed by the request for qualitative queue analysis in the Minor section.

## Novel Insights

The two reviews together surface an interesting tension: STARS's contrastive tuning *improves* linear separability of features (large KNN gains, t-SNE confirms better clusters) but does *not* improve full fine-tuning initialization. This suggests that the contrastive tuning primarily reorganizes the *top-layer feature geometry* without enriching the lower-level features that fine-tuning can exploit. The fact that NNCLR without augmentations outperforms DINO and MoCo *with* augmentations (Table 3) is also noteworthy — it implies that after MAE pretraining, the skeleton feature space already has enough structure that simple nearest-neighbor search in a queue provides useful positives, unlike in images where the same ablated NNCLR would likely collapse. This points toward a domain property (skeleton sequences have less intra-class variation than images) worth investigating further.

## Suggestions

- **Clarify Figure 1**: Report the exact breakdown of wall-clock time for both stages of STARS on a single GPU, state whether the MAE stage is included or pre-supplied from a public checkpoint, and note the hardware configuration explicitly.
- **Add variance estimates**: Report at least 3 seeds for the fine-tuning and transfer tables where margins are thin, or state if the community standard precludes this.
- **Analyze the queue's nearest neighbors qualitatively**: Show examples of what NN(z, Q) retrieves for a few sequences, including both successes and failures, to substantiate the augmentation-free claim.
- **Discuss the fine-tuning gap**: Add a paragraph (possibly in the ablation section or conclusion) hypothesizing why linear separability improves but fine-tuning does not benefit, and provide probing evidence if possible.
