Now I have a thorough understanding of the paper. Let me write the consolidated review.

## Summary

OCEBO proposes the first framework for pretraining object-centric vision models from scratch on real-world data. It replaces the standard approach of using frozen non-object-centric target encoders (e.g., DINOv2) with an EMA-updated target encoder that is progressively enriched with object-centric inductive biases via slot attention. A novel cross-view patch filtering mechanism prevents slot collapse during early training by limiting supervision to patches with consistent cross-view correspondences. When pretrained on ~241k COCO images, OCEBO achieves unsupervised object discovery results comparable to DINOSAUR models whose target encoders were pretrained on 142M images, while demonstrating continued improvement with more data (unlike prior methods that plateau at ~16k images).

## Strengths

- **First demonstration of object-centric pretraining from scratch on real-world data.** This is the paper's central contribution and is well-supported. Prior work (DINOSAUR, FT-DINOSAUR, SPOT) all relied on frozen pretrained non-object-centric encoders as reconstruction targets. OCEBO shows that with EMA updates, an object-centric self-distillation loss, and cross-view patch filtering, training from scratch is viable. This opens a new direction for the field.

- **Cross-view patch filtering is a clean, effective solution to the cold-start problem.** The mechanism is simple and principled: only supervise patches whose cross-view nearest neighbors are consistent. Table 1(a) shows that omitting this mechanism causes immediate slot collapse (FG-ARI drops from 53.5→32.4 on MOVi-E). Figure 2 demonstrates the elegant behavior — the fraction of supervised patches grows from ~10% at epoch 0 to ~70% at epoch 200 as the target encoder improves, creating a natural curriculum.

- **Ablation confirms that object-centric biases in the target encoder are critical.** Setting λ_oc=0 (removing the object-centric loss) leads to full collapse (FG-ARI 2.1/11.5 on MOVi-E/EntitySeg), demonstrating that DINO-style self-distillation alone on COCO is insufficient. This directly supports the paper's core hypothesis that injecting object-centric inductive biases into the target encoder via EMA is what enables successful training.

- **Clear evidence of improvement over the prior saturation point.** Prior work showed performance plateaus at ~16k images with frozen encoders. OCEBO trained on 118k COCO images outperforms the same model trained on smaller subsets, and training on 241k (COCO+) yields further FG-ARI gains (e.g., +4.9 on MOVi-C, +3.8 on MOVi-E). This confirms that the EMA update removes the previously observed upper bound.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **The headline "comparable performance" claim is nuanced.** The abstract states OCEBO achieves "performance comparable" to models with frozen encoders pretrained on orders of magnitude more data. This is true for FG-ARI (e.g., OCEBO COCO+: 49.0 vs. DINOSAUR-DINOv2: 47.9 on MOVi-C) but substantially less true for mBO, where OCEBO is roughly half on MOVi-E (17.0 vs. 33.3) and notably lower on EntitySeg (13.6 vs. 22.4). The paper acknowledges this trade-off in Section 4.3, attributing low mBO to the MLP decoder, and notes that autoregressive decoders (SPOT) improve mBO at the cost of FG-ARI. However, for a reader scanning the abstract, "comparable performance" could be misleading. The contribution (first from-scratch pretraining) stands on its own and does not need this framing.

- **The mask sharpening stage partially re-introduces the frozen-target paradigm whose limitations motivate the paper.** The training pipeline ends with a 100-epoch stage where the target encoder is frozen and the self-distillation loss is replaced by an ℓ₂ reconstruction loss. The paper explicitly likens this to FT-DINOSAUR, and Table 1(c) shows it substantially improves performance. The authors frame this as optional, but it is part of the default 400-epoch training protocol. The paper does not analyze whether extending the EMA-based self-distillation stage for the same additional epochs would achieve similar or better results. This is a meaningful analysis gap: the method is not a pure bootstrapping framework, and the contribution of its second stage is not fully disentangled from the first.

- **Scalability evidence is limited to two data increments.** The paper compares COCO (118k) and COCO+ (241k) and shows FG-ARI gains. While this demonstrates improvement beyond the 16k saturation point of prior work, the gains are modest (e.g., MOVi-E: 62.7→65.2 FG-ARI) and mBO decreases somewhat on MOVi-E. Only two data sizes are tested, and there is no finer-grained scaling curve (e.g., 16k, 32k, 64k, 118k, 241k) that would help the reader assess whether performance is still trending upward or nearing a new plateau. The central motivation of the paper — that EMA updates remove the upper bound — would be strengthened by more granular evidence.

- **The value of *k* in cross-view patch filtering (Eq. 7) is never specified.** The paper introduces *k* nearest neighbors as a relaxation but never states what value of *k* is used. Given that this mechanism is central to preventing collapse, the choice of *k* likely affects the growth rate of the supervised patch mask and downstream performance. This is a reproducibility gap.

- **Results are reported without confidence intervals or multiple seeds.** Object-centric models can be sensitive to initialization and random seeds. All comparisons in Tables 1 and 2 appear to be single-run. While single-run evaluation is common in this line of work, reporting variance would increase credibility, especially for the claims about scalability where the gains are modest.

- **The "in-distribution" advantage of training on COCO is not discussed in the zero-shot evaluation.** OCEBO is trained on COCO and evaluated zero-shot on MOVi-C, MOVi-E, Pascal VOC, and EntitySeg. The baselines (DINOSAUR, FT-DINOSAUR, SPOT) use encoders pretrained on ImageNet (1.3M) or a large curated dataset (142M), not COCO. OCEBO's training distribution is closer to the evaluation datasets (especially Pascal VOC, which shares categories with COCO). The paper frames this as OCEBO seeing "orders of magnitude less images," but the distributional match is an alternative explanation for the competitive FG-ARI that is not addressed.

### Trivial

- The value of the slot-collapse diagnostic *d* is introduced but not reported for the SOTA comparison in Table 2; it appears only in the ablation table. Reporting *d* for the full OCEBO model and key baselines would strengthen the collapse-avoidance claim.

- Computational cost (GPU-hours) of OCEBO vs. fine-tuning a pretrained encoder is not discussed. This is a practical concern for researchers considering adopting the approach.

## Nice-to-Haves

- A direct comparison of OCEBO (with EMA) against an ablation that freezes the target encoder after the first 100 epochs would cleanly isolate the value of continued bootstrapping vs. the object-centric initialization.
- An analysis of how the choice of *k* in cross-view patch filtering affects the growth of the supervised-patch curve and final performance.
- Qualitative mask visualizations, especially for datasets where mBO is low, would help readers understand what the model captures vs. where it fails.
- Extending the mask sharpening stage analysis: does the sharpening stage converge faster or to a better optimum *because* the target encoder is already object-centric, compared to starting from a frozen DINO target?

## Removed Points

These points were identified by reviewers but removed or downgraded after verification against the paper:

1. *"It is not specified whether the target encoder remains frozen throughout the mask sharpening stage or whether it is initialised from the EMA-updated weights."* — The paper explicitly states: "we keep training the object-centric model with a frozen target" (Section 3.4, line 104). This is specified.
2. *"The EMA hypothesis is never directly tested."* — The ablation with λ_oc=0 (Table 1b) does test the necessity of the object-centric loss for EMA-based training. While a more precise test could isolate the EMA mechanism further, the existing ablation is a reasonable and informative test.
3. *"The d metric is not reported for the main OCEBO model."* — Table 1's first row reports the base OCEBO model (including d). The critic's concern applies only to Table 2 (SOTA comparison), which is a reasonable suggestion but not a factual error.
4. *"Parser artifacts in Table 1"* — Purely a parser issue, not an author error.
5. *"The models are not directly comparable because OCEBO is trained on COCO"* — This is already acknowledged in Section 4.3, though the specific "in-distribution advantage" angle is not discussed.

## Novel Insights

The most interesting insight from the reviews is that the interplay between the two stages of OCEBO (EMA-based self-distillation followed by frozen-target sharpening) remains underexplored, and this is where the most important future analysis would lie. If the mask sharpening stage is crucial because the constantly changing EMA target prevents sharp mask boundaries, then the fundamental limitation of the bootstrapping approach is not the lack of object-centric biases (which is solved) but the instability of a moving target during the late stages of training. Conversely, if extending the EMA stage for 100 more epochs matches the sharpening stage, then the two-stage procedure is merely a convenience rather than a necessity. Resolving this would sharpen the contribution narrative considerably. None beyond the paper's own contributions.

## Suggestions

- Tone down the "comparable performance" claim in the abstract to reflect the FG-ARI/mBO trade-off more accurately. Something like "achieves competitive FG-ARI while noting a gap in mask quality" would be more precise and would not diminish the paper's contribution.
- Specify the value of *k* in cross-view patch filtering and, ideally, include an ablation showing its impact.
- Provide a finer-grained scalability curve (4–5 data increments) or acknowledge the limited evidence as a limitation.
- Add an ablation comparing extended EMA training vs. the mask sharpening stage to clarify the role of each.
- Report confidence intervals or results across 3 seeds for key comparisons.
- Include a brief discussion of computational cost and training time.

## Score and Decision

The paper addresses an important open problem — enabling object-centric pretraining from scratch — and proposes a well-motivated solution with a clever cold-start mechanism. The experimental evidence supports the core claim (pretraining from scratch works and avoids collapse) but is weaker for secondary claims (comparable performance on mBO, convincing scalability). The weaknesses are addressable and do not invalidate the contribution. The paper is a solid contribution that opens a new direction for the field.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>