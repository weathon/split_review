## Summary

This paper proposes Slerp+, a unified framework for composed visual retrieval that handles both images and videos within a single model. The method extends the existing Slerp (spherical linear interpolation) approach from image-only to a joint image-video-text setting by training a BLIP-based model on both image-caption and video-caption pairs with VTC and VTM losses, then applying Slerp at inference for zero-shot composition. The paper also introduces a new video benchmark, Activitynet-CoVR (800 triplets). Results across four benchmarks (WebVid-CoVR, CIRR, FashionIQ, Activitynet-CoVR) show competitive or state-of-the-art zero-shot performance.

## Strengths

1. **First unified image-video-text composed retrieval framework**: The paper consolidates previously separate CoIR and CoVR tasks into a single Composed Visual Retrieval (CVR) task (lines 4–5, 30), and demonstrates a working system that processes both modalities with the same encoder. This is a practically useful formulation.

2. **Joint training demonstrably improves both modalities over single-modality**: Ablation entries (f) and (g) in Table 5 show that training on both images and videos outperforms training on either modality alone. The mutual enhancement claim, while needing stronger quantification in text, is supported by this ablation and is a notable result.

3. **Strong zero-shot results on a new challenging benchmark**: On Activitynet-CoVR (Table 2), Slerp+ outperforms all zero-shot methods across all recall ranks and even surpasses the supervised CoVR model fine-tuned on triplets, demonstrating generalization where domain shift hurts the supervised baseline.

4. **Extreme parameter efficiency**: Only 0.32% of total parameters are trainable (LoRA on the text encoder, line 145), the vision encoder is frozen, and training runs for a single epoch. Despite this, the method achieves competitive or SOTA results across all four benchmarks.

## Weaknesses

### Fatal
None.

### Major
1. **Central mutual-enhancement claim lacks quantitative specificity in text**: The paper's headline claim — "mutually enhances image and video retrieval performance" (abstract, line 4) — is supported by ablation entries (f) and (g) in Table 5. However, the text (line 184) only describes the result qualitatively ("improves both image and video composed retrieval accuracy") without reporting the actual recall numbers or the magnitude of improvement. Since the mutual-enhancement thesis is what distinguishes this work from a straightforward engineering extension of Slerp, the quantitative magnitude must be clearly stated in the text so readers can assess its practical significance. The authors should state, e.g., "joint training improves R@1 on WebVid-CoVR from X to Y and on CIRR from A to B."

### Minor
1. **No analysis of Slerp *t* parameter sensitivity**: The paper sets *t* = 0.6 for videos and *t* = 0.7 for images (line 147) with no description of how these values were chosen and no sensitivity sweep. A simple ablation showing R@K vs. *t* for both modalities would demonstrate robustness.

2. **Missing a "BLIP + Slerp without video training" baseline on image benchmarks**: The paper compares against CLIP-based zero-shot methods, but does not include the natural control of "take the BLIP backbone, apply Slerp inference, train on images only (no video data)." Table 5(f) partially serves this role but the text does not state the numbers explicitly. The contribution of unified training vs. the stronger backbone (BLIP with cross-attention) is therefore partially conflated.

3. **Activitynet-CoVR benchmark documentation is thin**: The 800-triplet benchmark is generated via VideoMAE-Large similarity filtering, LLaMA3 prompting, and human filtering (line 135), but no details are given on number of annotators, inter-annotator agreement, or the filtering discard rate. For a benchmark intended to drive future research, these details matter.

4. **Limitations section is too sparse**: The only limitation discussed (line 197) is training data quality. Missing from discussion: the sensitivity of *t*, the lack of temporal modeling in video (simple frame averaging), the small size of Activitynet-CoVR, and the reliance on BLIP's cross-attention architecture.

### Trivial
None.

## Nice-to-Haves
- Reporting variance or confidence intervals for recall scores (common practice in some but not all retrieval work; not a flaw in this field's standards)
- Ablation separating the contribution of the BLIP backbone vs. unified training by testing a CLIP + unified-training variant

## Removed Points
These points were raised but are either incorrect, overblown, or better classified elsewhere:

- **"Method novelty is marginal / integration is 'almost literal'"**: The paper acknowledges Slerp and BLIP as pre-existing. The contribution is the unified CVR formulation and joint training — a valid type of contribution. The severity claimed by the critic is disproportionate.
- **"Apples-to-oranges comparison (BLIP vs CLIP)"**: Comparing one's best system against others' best systems is standard practice. The paper is transparent about using BLIP and explains why. This is not a fairness issue.
- **"'Not far behind' wording is evasive"**: This is a wording nitpick. The actual numbers are in the table.
- **"No statistical significance reported"**: Single-run evaluation is standard in retrieval benchmarks. Not a genuine weakness for this venue.
- **"Supervised CoVR's poor generalization is predictable / domain shift not discussed"**: The paper reports results honestly. Explaining domain shift is not required.
- **"No temporal modeling"**: The VTM loss uses concatenated frame tokens with cross-attention (line 101), giving some temporal awareness during training. The retrieval embedding uses averaging, which is a design choice, not an oversight. Demoted from the critic's framing.
- **Criticism that the paper doesn't engage with multi-task visual representation learning (VideoCLIP, ALBEF)**: Missing related works cannot be verified externally and should not be included per instructions.

## Novel Insights
None beyond the paper's own contributions. The reviews surface no observation about the method or results that the paper itself does not already articulate.

## Suggestions
1. In the ablation discussion (Section 4.4), explicitly state the recall numbers for entries (f), (g), and the full method in the text, not just in the table.
2. Add a sensitivity analysis for the Slerp *t* parameter (R@1 vs. *t* for images and videos, showing both modalities).
3. Document the Activitynet-CoVR annotation process more thoroughly: number of annotators, instructions, agreement, discard rate.
4. Expand the limitations paragraph to cover *t* sensitivity, temporal modeling, and benchmark scope.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>