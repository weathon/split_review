Now I have a thorough understanding of the paper and all reviewer claims. Let me synthesize the final review.

## Summary

The paper introduces UniDisc, the first unified multimodal discrete diffusion model that jointly processes text and images using absorbing-state masking diffusion. The key technical contributions are modality-specific timestep schedules and KV-caching that exploit the fact that image tokens require far fewer denoising steps than text tokens, improving inference efficiency. The paper evaluates UniDisc against autoregressive baselines on unconditional/conditional generation, retrieval, and joint inpainting, reporting competitive or superior results, particularly with classifier-free guidance.

## Strengths

1. **First unified multimodal discrete diffusion with shared architecture and loss**: UniDisc applies a single discrete diffusion objective (absorbing-state masking) jointly across text and image tokens within one transformer, unlike prior work (UniD3) that used separate operations per modality. The architecture shares parameters across modalities rather than decoupling them, which is a genuine design contribution.

2. **Modality-specific caching and separate timestep schedules are well-motivated and validated**: The paper identifies (Figure 4c–d) that text requires ~400 denoising steps while image FID saturates at ~32 steps. The proposed solution—KV-caching image tokens with modality-specific schedules (Section 3.3–3.4)—is clearly motivated and quantitatively shown to reduce latency, especially at longer sequence lengths and higher batch sizes (Figure 2).

3. **Classifier-free guidance yields substantially better conditional generation**: Table 2 shows UniDisc with CFG achieves noticeably lower FID (12.3 vs. 17.8) and higher CLIP score (0.38 vs. 0.33) compared to the AR baseline with CFG, using the same architecture and capacity. Without CFG, both models perform similarly, isolating the advantage to diffusion's ability to blend conditional and unconditional predictions.

4. **Joint image-text inpainting without explicit training**: Figures 1, 11, and 12 demonstrate a genuinely novel capability — jointly inpainting content across both modalities (e.g., replacing an object in the image while rewriting the caption) that arises naturally from the unified diffusion objective, which AR models cannot do without explicit fine-tuning.

5. **Retrieval performance and inference-compute flexibility**: Table 3 reports consistently higher retrieval accuracy across multiple datasets (e.g., joint retrieval 72.3% vs. 58.1% on DataComp1B). Figure 5 further shows that retrieval accuracy improves with more denoising steps, a flexibility absent in AR models where inference steps are fixed to sequence length.

## Weaknesses

### Fatal
None.

### Major

1. **The conditional generation advantage rests entirely on CFG, but the AR baseline's CFG implementation is not shown to be near-optimal.** The paper notes (Section 4.1, Table 2) that without CFG both models perform similarly; the claimed superiority hinges on CFG helping UniDisc more than AR. However, the AR implementation drops the first modality in the input sequence (following Liu et al., 2024), while UniDisc blends conditional and unconditional predictions iteratively—a fundamentally different mechanism. The paper provides no ablation showing that the AR CFG is equivalently tuned (e.g., no sweep over guidance scales, no exploration of alternative AR decoding strategies). Without evidence that the AR baseline is reasonably optimized for CFG, the conclusion that diffusion is inherently superior for conditional generation is not fully supported. This is the paper's most consequential quantitative claim, and the evidence for it is incomplete.

### Minor

2. **Training efficiency comparison (Figure 3) uses non-comparable metrics.** The paper compares UniDisc's NLL (an upper bound / ELBO) to AR's exact NLL and reports an "8x training-inefficiency factor." While the paper acknowledges UniDisc's values are upper bounds, the factor is derived from comparing a bound to an exact quantity, which could be misleading. The factor also varies substantially by modality (image vs. text), and the paper's use of it as a unified number (e.g., for CLEVR training in Section 4.3) should be interpreted cautiously. This does not affect the paper's core generation or retrieval claims, but it weakens the training-efficiency narrative.

3. **Several hyperparameter values for the proposed method are underspecified.** The modality-specific schedule parameters N_min, N_max, and K are central to the method (Section 3.3), but the paper does not state their concrete values used in training, only that K ≈ 10 is "inferred from Figure 4." Figure 2 caption says "k = 10" but it is unclear whether this was set post-hoc based on results or chosen ex ante. This makes reproduction more difficult than it should be.

4. **The 1.4B scaling results are only qualitatively demonstrated.** Section 4.6 describes training a 1.4B model on web-scale data but only provides qualitative visualizations in the main paper. While the paper references appendix sections (A.5, A.6) for additional results, the main text's claim that "UniDisc scales well across parameters and dataset size" would benefit from at least one quantitative validation metric (e.g., validation loss curve, FID at this scale) in the main paper.

### Trivial
None of consequence.

## Nice-to-Haves
- An ablation isolating the contribution of each proposed technique (modality-specific caching, SandwichNorm, Min-SNR) would strengthen the paper.
- Reporting zero-shot FID/CLIP on MS-COCO for text-to-image generation would connect the results to the broader image generation literature.
- Ablating different numbers of denoising steps for the AR CFG (e.g., generating multiple candidates and selecting by confidence) could address concerns about whether the AR baseline's CFG was fairly tuned.

## Removed Points
These points are flagged to be removed, treat them with caution:

1. **"ELBO vs exact likelihood comparison invalidates retrieval and other claims"** — The paper is explicitly transparent about this (Section 4.1: "perplexity values from AR are exact likelihoods, values from UniDisc are upper bounds"). For Table 1 and Table 3, the comparisons are not invalidated by this: Table 1 only claims similar performance, not superiority; Table 3 uses each model's own likelihoods for *ranking* (accuracy, not raw score comparison), which is standard practice. The retrieval comparison compares ranking accuracy, not the raw likelihood values across models, so this concern does not invalidate it.

2. **"Retrieval evaluation uses a fundamentally incomparable metric"** — As above, the comparison is on ranking accuracy (whether the correct item has the highest score within each model's own scoring), not on the magnitude of scores across models. This is a standard and valid evaluation protocol for generative-model-based retrieval.

3. **"The 1.4B scaling claims are unsupported"** — The paper references appendices A.5 and A.6 for training curves and additional results. These sections are stripped by the parser but exist in the original submission. Per policy, criticisms about missing appendix content are removed.

4. **"Missing ablation for stability tricks (QK-Norm, SandwichNorm, etc.)"** — Ablations of design choices are referenced in appendix A.3, which was stripped.

5. **"Formatting/style nitpicks"** — Removed as pure presentation concerns.

6. **"Unfair baseline comparison"** — The AR baseline uses standard Chameleon architecture with same tokenizers, architecture, hyperparameters, and data — the comparison is fair by design. The CFG tuning question is a separate (and valid) concern that is kept in the Major weaknesses section above.

## Novel Insights

The most interesting observation to emerge from combining the reviews is the tension between what the paper claims as evidence and what the evidence actually supports. The reviewer correctly notes that the CFG-only advantage is the paper's strongest quantitative result, but the review process reveals that this advantage is asserted rather than investigated: we don't know whether the AR baseline's poor CFG response is inherent to autoregressive decoding or a consequence of the specific (and not obviously optimal) CFG implementation used. This is a recurring pattern in diffusion-vs-AR comparisons that this paper does not address beyond what prior work has already observed. A genuinely insightful contribution would have been to ablate why CFG helps diffusion more — is it the iterative refinement, the bidirectional context, or something else? — rather than simply reporting the performance gap.

## Suggestions

1. **Strengthen the CFG comparison**: Add a sweep over guidance scales (and additional decoding strategies like top-p/temperature) for the AR baseline, report the best AR CFG result, and discuss whether AR CFG has inherent limitations or simply requires different parameter tuning. This is the single most important improvement.

2. **Clarify the training efficiency factor**: Either (a) use a comparable metric (e.g., importance-sampled likelihood estimates for UniDisc) or (b) reframe the comparison as "NLL upper bound vs. exact NLL" and explicitly note the factor is directional, not a precise inefficiency estimate.

3. **Report concrete values for N_min, N_max, K**: These are essential for reproducibility of the proposed modality-specific schedule.

4. **Add one quantitative metric for the 1.4B model** in the main paper (e.g., validation loss or FID) to substantiate the scaling claim.

## Score and Decision

The paper presents a genuinely novel and well-motivated approach — unified multimodal discrete diffusion — with clear technical contributions (modality-specific schedules, KV-caching) and compelling qualitative results (joint inpainting). The main quantitative claims are partially supported: the conditional generation advantage (Table 2) is real but lacks evidence that the AR baseline's CFG was optimally tuned; the retrieval results (Table 3) are valid and consistent; the inference speed advantage (Figure 2) is well-supported. The training efficiency comparison is the weakest quantitative claim. Overall, the paper's core contributions are meaningful and the evidence is sufficient for acceptance, though the CFG comparison needs strengthening and several claims are slightly over-stated relative to the evidence.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>