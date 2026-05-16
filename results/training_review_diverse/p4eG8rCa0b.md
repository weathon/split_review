Now I have a thorough understanding of the paper and can verify all claims against the actual text. Let me produce the consolidated review.

## Summary

This paper presents Compose and Conquer (CnC), a diffusion-based framework with two technical contributions: (1) Depth Disentanglement Training (DDT), which uses synthetic image triplets (foreground, background, mask) to teach the model about relative depth ordering and occlusion of multiple objects; and (2) soft guidance, which reuses the binary mask to selectively mask cross-attention similarity matrices, allowing CLIP image embeddings to influence specific regions without concept bleeding. The unified framework enables simultaneous control over 3D depth-aware object placement and region-specific global semantics.

## Strengths

- **DDT demonstrably improves depth-aware generation.** Figure 2 directly contrasts a DDT-trained model (correct occlusion and depth ordering) with a model trained only on source-image depth maps (fused or ignored objects). This is the paper's strongest piece of evidence — it isolates the effect of the synthetic triplet training and shows a clear qualitative improvement in handling overlapping objects at different depths.

- **Soft guidance prevents concept bleeding across regions.** Figure 4 (conflicting semantics experiment) shows that when two contradictory global semantics (e.g., "igloo" foreground vs. "water" background) share a single depth map, soft guidance maintains the foreground semantic identity even as the background weight increases. This convincingly demonstrates that masking the cross-attention similarity matrix effectively localizes global conditions.

- **The synthetic triplet generation pipeline is well-motivated.** Adopting image-composition techniques (inpainting with Stable Diffusion) to create explicit "see-behind" training data is a clever solution to the fundamental problem that occluded content is lost in 2D images. The pipeline is clearly described and justified.

- **Reconstruction metrics show strong depth fidelity.** Table 2 reports substantially lower LPIPS and depth MAE compared to baselines on both COCO-Stuff and Pick-a-Pic. Figure 3 qualitatively confirms that baselines produce flat images while CnC preserves depth of field — a genuine advantage that aligns with the paper's core claims.

## Weaknesses

### Fatal
None.

### Major

- **Evaluation protocol does not control for asymmetric conditioning inputs, undermining quantitative comparisons.** In both Table 1 (FID/IS/CLIPScore) and Table 2 (reconstruction), CnC receives *two* depth maps (foreground + background) and *two* CLIP image embeddings, while every baseline receives one depth map and at most one exemplar image. For reconstruction in particular, the paper states: "our model utilizes the depth maps and CLIP image embeddings extracted from the image triplets of ground truth validation images, and baseline models utilize the depth maps and CLIP image embeddings extracted from the ground truth images, since they do not support more than one condition per modality." CnC's access to *separate* foreground and background depth maps from ground truth gives an inherent advantage on reconstruction metrics (LPIPS, depth MAE) that has nothing to do with methodological superiority. The paper acknowledges the asymmetry in passing but never controls for it — e.g., by evaluating CnC with only a single depth map, or by providing baselines with a second (duplicated) condition. As a result, the quantitative headline claims of "substantially outperforms" are not interpretable as evidence of a methodological advantage. This is the paper's most serious weakness.

### Minor

- **Soft guidance uses the binary mask — the claim of "no additional localization cues" is overstated.** The abstract says soft guidance imposes global semantics "without the use of any additional localization cues" and the introduction says "without any explicit structural signals." However, the method explicitly uses the binary mask \(M\) to construct \(M'\) that restricts cross-attention (line 82: "our method leverages the binary foreground mask \(M\)"). A binary mask is a localization cue — minimal but real. The paper is transparent about this (line 77), and "additional" suggests the mask is already part of the pipeline (from DDT triplets), so no *new* signal is introduced. Still, the framing is misleading: the technique does not avoid localization cues; it reuses one that exists. This should be honestly characterized as "reuses the existing binary mask to spatially restrict attention."

- **The inference pipeline is underspecified.** During training, DDT uses synthetic triplets with inpainted backgrounds. At inference, the user must supply two depth maps (foreground and background) and a binary mask. The paper never explains how a user would obtain these in practice — are they expected to draw masks manually? Use automated segmentation from depth discontinuities? Extract depth maps separately? This gap affects reproducibility and practical applicability.

- **No confidence intervals or statistical significance reported for quantitative metrics.** FID differences can be within noise range; reporting significance would strengthen the quantitative claims.

- **Claim that DDT "identifies the absolute positions of unseen objects" (abstract) is slightly overreaching.** The method learns relative depth ordering from paired synthetic depths; the model generalizes to new objects, but the mechanism is relative (foreground/background), not "absolute positioning" in any metric 3D sense.

- **The paper does not discuss whether DDT training on SD-inpainted backgrounds causes the model to learn inpainting artifacts that could affect generalization.** This is a reasonable concern worth addressing.

### Trivial

- The phrase "spatial information of \(M\) is forfeited" (end of §3.3) is confusing on first read — the mask's spatial structure is lost when flattened into the attention matrix (only per-location boolean membership remains), but the paper could clarify this more directly.

## Nice-to-Haves

- An ablation controlling for input count: evaluate CnC with a single depth map (foreground only, or the single source depth) against baselines on the same metrics.
- A discussion of how users would obtain the two depth maps and mask during inference (e.g., user-drawn segmentation + off-the-shelf monocular depth estimation).
- Show failure cases when foreground and background depth maps partially overlap or conflict in non-binary ways, as a stress test of the claimed disentanglement.

## Removed Points

These points are flagged to be removed, treat them with caution:
- **"Soft guidance is same core idea as Paint-by-Example"** — This is a judgment about similarity to an external work that cannot be verified against the paper's content alone; it is also a claim about a cited work whose existence is assumed, per the hard rules.
- **"Missing ethical considerations"** — Not a standard requirement for a method paper; scope creep.
- **"Code/model release not mentioned"** — Not a required component of a conference submission.
- **"Mask acquisition during sampling not specified"** — Subsumed by the inference pipeline underspecification weakness above; the original formulation as a separate point was redundant.
- **Strength Finder strengths #4, #5, #6** (synthetic triplet pipeline, modular training, dataset choice ablation) — These are generic or already subsumed by stronger strengths. The dataset choice discussion is reasonable but conflicts with the fact that the asymmetric data construction is part of the fairness problem. Moved here.
- **Section-by-section note about "spatial information forfeited" being confusing** — On re-reading, the paper's meaning is defensible (2D spatial structure is forfeited in the flattened attention matrix; only binary per-position membership remains). Moved to Trivial.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the evaluation fairness problem but do not add new interpretive perspectives beyond what the paper presents.

## Suggestions

1. **Run a controlled ablation for the evaluation.** The most impactful fix is to evaluate CnC with only a single depth map (the source image's depth, as baselines use) while keeping soft guidance enabled. If CnC still outperforms baselines, the methodological claim is cleanly supported. If not, the paper should honestly characterize the advantage as coming from access to more conditioning inputs rather than a better method.

2. **Rephrase the soft guidance claim.** Replace "without the use of any additional localization cues" with a precise statement: "Soft guidance reuses the binary mask \(M\) (already available from the triplet pipeline) to spatially restrict cross-attention, requiring no additional structural signals beyond this binary mask."

3. **Specify the inference workflow.** Add a short paragraph explaining how a practitioner would obtain the required inputs (e.g., user-provided binary mask + monocular depth estimation on the composite or on both regions separately).

4. **Add statistical significance or confidence bands for FID/CLIPScore** to verify that reported differences exceed evaluation noise.

## Score and Decision

The paper proposes two genuinely interesting techniques (DDT and soft guidance) and provides good qualitative evidence that both work as intended. The DDT results (Figure 2) are the cleanest evidence: training on synthetic triplets clearly enables better depth ordering. However, the quantitative evaluation is undermined by a failure to control for asymmetric conditioning inputs — CnC receives strictly more information than any baseline. This makes the headline quantitative claims uninterpretable as evidence of methodological superiority. The core techniques remain valuable, but the paper needs a fair evaluation to support its strongest claims.

**Score**: 5.0 (marginally below accept threshold; would need fairer evaluation to warrant acceptance)

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>