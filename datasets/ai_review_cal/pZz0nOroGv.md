- Decision: Accept
- Avg Score: 5.00
- Scores: 1, 5, 6, 8
Now I have a thorough understanding of the paper and can cross-check all reviewer claims. Let me produce the final consolidated review.

---

## Summary

TEOChat introduces the first vision-language model (VLM) capable of temporal reasoning over sequences of Earth observation (EO) images, together with TEOChat-Instruction-554k, a curated instruction-following dataset spanning seven temporal task categories (temporal scene classification, change detection, spatial change referring expression, change QA, region-based change QA, temporal referring expression, and region-based temporal QA) using data from fMoW, xBD, S2Looking, and QFabric. The model uses a LLaVA-1.5 architecture (CLIP ViT-L/14 + 2-layer MLP + Llama 2 with LoRA fine-tuning). Experiments show TEOChat substantially outperforms prior VLMs (Video-LLaVA, GeoChat) on temporal tasks, outperforms GPT-4o and Gemini 1.5 Pro with in-context learning, and demonstrates strong zero-shot and single-image capabilities.

## Strengths

- **First VLM to handle temporal EO data.** No prior VLM could reason over temporal sequences of EO images (e.g., change detection). Table 1 shows TEOChat dramatically outperforms both Video-LLaVA (a video VLM trained on natural images) and GeoChat (a single-EO-image VLM) on every temporal task — often by very large margins (e.g., fMoW RGB: 75.1% vs 16.6% Video-LLaVA, 59.2% GeoChat; xBD damage classification F1: 50.0 vs 8.3 Video-LLaVA, 11.8 GeoChat).

- **TEOChat-Instruction-554k is the first temporal EO instruction-following dataset.** The paper curates 554k examples spanning 7 task categories from 4 temporal EO datasets, filling a clear gap. Ablations (Table 2 row 1 vs row 2) confirm that training on this dataset is what enables temporal capabilities — without it, performance across all temporal tasks is near zero.

- **Systematic ablations isolate key design choices.** Table 2 tests LLM/projector initialization (LLaVA vs Video-LLaVA), image encoder (CLIP vs SkyScript), projector freezing vs fine-tuning, image references, and training duration. The final configuration (Video-LLaVA init, CLIP encoder, fine-tuned projector, image references, 14k steps) outperforms all alternatives on five canonical temporal tasks. This provides well-grounded empirical support for the design.

- **Outperforms GPT-4o and Gemini 1.5 Pro on temporal tasks.** Table 4 shows TEOChat achieves 50.0 F1 on xBD damage classification vs 38.3 (GPT-4o) and 35.8 (Gemini 1.5 Pro), and 33.6 F1 on S2Looking detection vs 21.5 and 16.5 respectively — even though the proprietary models use 3-shot in-context learning with full-resolution images.

- **Joint single-temporal training improves temporal performance.** Comparing TEOChat (joint training) to TEOChat-T (temporal-only) in Table 1, joint training yields better results on 11 of 13 metrics (e.g., xBD localization IoU: 35.5 vs 28.8), showing that including single-image tasks strengthens rather than degrades temporal reasoning.

- **Strong single-image capabilities despite lower resolution.** Table 5 shows TEOChat (at 224×224 resolution) outperforms GeoChat (at 504) on average across zero-shot scene classification and VQA benchmarks (+3.5 average), and outperforms GeoChat on 6 of 7 tasks.

## Weaknesses

### Fatal
None.

### Major

- **The "rivaling or outperforming specialist models" claim rests on weak specialist baselines that are not representative of current SOTA.** The paper claims TEOChat "achieves comparable or better performance than specialist models" (abstract) and "rivals specialist models on multiple tasks" (contributions). However, the specialist baselines used for change detection are the original dataset methods — a modified UNet from Gupta et al. (2019) for xBD and FC-Siam-Diff from Shen et al. (2021) for S2Looking — both producing F1 scores of exactly 26.5 on xBD damage classification and S2Looking detection. These numbers are far below what published methods achieve (xBD damage classification F1 scores typically exceed 0.60–0.70 in the literature; S2Looking baselines routinely exceed 50 F1). The paper describes these as "strong models" (Section 5.1), which is misleading. On the tasks where the specialists are stronger (xBD localization: 66.0 IoU vs TEOChat's 35.5; QFabric RQA-2: 77.0 vs TEOChat's 66.7; QFabric RQA-5: 81.6 vs TEOChat's 74.3), TEOChat substantially underperforms. The specialist comparison is not entirely without value — the fMoW specialist (SatMAE+Stack) is a reasonable self-supervised baseline, and TEOChat performs near it (−0.8%) — but the overall framing inflates the strength of the evidence. The authors should either (a) add stronger, modern specialist baselines (e.g., BIT, ChangeFormer for change detection) or (b) clearly and prominently state that these are the original dataset baselines and are not representative of current SOTA.

### Minor

- **Reproducibility: missing prompt templates, coordinate format, and metric details.** The paper describes converting benchmarks to instruction-following tasks at a high level but does not provide exact prompt templates for each of the 7 task categories, how class labels are verbalized (e.g., multiple-choice vs free-text), or whether bounding box coordinates are normalized to [0,1] or pixel-based. The paper states boxes are of the form `[x_min, y_min, x_max, y_max]` (Section 3) but does not specify the coordinate system. For xBD damage classification, it is also unclear how the specialist's F1 metric aligns with TEOChat's evaluation (the xBD literature typically evaluates damage classification weighted by building instances, not per-pixel). These details are standard to provide in supplementary material and would significantly improve reproducibility.

- **Low image resolution (224×224) is a notable limitation that receives insufficient discussion.** The paper uses CLIP ViT-L/14 at its native 224×224 resolution throughout, while GeoChat uses 504×504. For fine-grained tasks like building localization (TEOChat achieves only 35.5 IoU vs the specialist's 66.0), this is a significant handicap. The paper mentions resolution briefly in the single-image comparison (Section 5.5) and as a future work direction, but does not discuss how the 224×224 resolution may fundamentally limit the model's ability to perform tasks requiring precise spatial localization. This matters for interpreting the xBD localization and S2Looking detection results.

### Trivial
None.

## Nice-to-Haves

- An ablation replacing the CLIP image encoder with a higher-resolution variant (e.g., ViT-L/14 at 384×384) would strengthen the architectural claims and clarify the resolution-performance trade-off.
- Reporting variance or standard deviations across runs for key results would increase confidence in the reported numbers.
- A dedicated failure analysis for building localization (e.g., are errors from missed detections or poor box regression?) would help readers understand the limits of language-based coordinate representation.
- An analysis of temporal data scale sensitivity (e.g., training on 50% or 25% of the temporal subset) would characterize how much temporal data is needed.

## Removed Points

These points were raised by reviewers but removed after cross-checking against the paper:

- **GeoChat baseline may be unfairly weak** (Harsh Critic): The claim that GeoChat's evaluation "likely underestimates" what it could achieve with temporal adaptation is speculative. The paper transparently describes evaluating GeoChat via per-image predictions + pixel-wise difference, which is the natural approach for a model that cannot natively handle multiple images. No evidence is provided that an alternative temporal adaptation would materially change results. → REMOVED (speculative, no evidence).

- **Overstated dataset novelty** (Harsh Critic): The paper clearly states it "curates" (not collects) the dataset from existing benchmarks, which is standard practice in instruction tuning (e.g., LLaVA uses COCO captions). The claim "first temporal EO dataset for multimodal instruction-tuning" is factually accurate per the dataset comparison table. The paper is transparent about dataset composition. → REMOVED (the paper does not overclaim; "curate" is accurate).

- **Proprietary models only 3-shot ICL** (Harsh Critic): It is standard and expected to evaluate proprietary models via in-context learning since they cannot be fine-tuned. The paper is transparent about the setup. → REMOVED (standard practice, not a weakness).

- **Missing ablation for higher resolution encoder** (Harsh Critic): This is a reasonable suggestion but not a weakness — it is a direction for future work that the paper already partially acknowledges. → MOVED to Nice-to-Haves.

- **Statistical significance / variance reporting** (Harsh Critic): Reasonable suggestion, but single-run evaluation is common practice in instruction-tuning papers. → MOVED to Nice-to-Haves.

## Novel Insights

The most striking observation that emerges from the reviews — beyond the paper's own contributions — is the asymmetric value of the specialist comparisons. On the one hand, the fMoW comparison (SatMAE+Stack, a reasonable self-supervised baseline) is clean and informative: TEOChat's −0.8% gap is genuinely impressive for a generalist VLM operating at 224×224. On the other hand, the xBD and S2Looking specialist numbers (both F1=26.5) are so low relative to the literature that they actively undermine reader confidence in the other comparisons, even though the core claims about outperforming prior VLMs and proprietary models are well-supported by much larger margins. This suggests the paper would benefit from a two-tier comparison — one tier comparing against prior VLMs (where the evidence is strong and clean), and a separate, carefully-contextualized tier for specialist comparisons with clearer statements about baseline vintage and strength.

## Suggestions

1. **(Required for claim credibility)** Replace the xBD damage classification and S2Looking change detection specialist baselines with modern methods (e.g., ChangeFormer, BIT, a properly tuned Siamese U-Net) or, at minimum, add a clear statement in the abstract, contributions, and conclusion that the specialist comparisons use the original dataset-provided baselines and are not representative of current SOTA. Re-frame the "rivaling or outperforming specialist models" claim to match the actual evidence.

2. **(Reproducibility)** Include exact prompt templates for each of the 7 task categories, the coordinate normalization scheme, class verbalization format, and response parsing logic in the supplementary material.

3. **(Honesty)** Add a dedicated limitations section discussing the effects of 224×224 resolution on localization tasks, the vintage of specialist baselines, and the scope of zero-shot evaluation (only 2 datasets, both building-change-adjacent).

4. **(Nice-to-have)** Provide variance estimates for key results and a brief failure case analysis for xBD building localization to clarify whether errors are from missed detections or imprecise bounding box regression.
