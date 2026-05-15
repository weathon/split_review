Now I have all the information needed. Let me write the consolidated review.

## Summary

This paper introduces Slerp⁺, a unified framework for zero-shot composed image and video retrieval. The method extends the Slerp (spherical linear interpolation) approach, previously proposed for composed image retrieval, to jointly handle both images and videos by training a single model on image-caption and video-caption pairs using VTC and VTM losses with a frozen ViT vision encoder and LoRA-tuned text encoder. The key contribution is demonstrating that a single model can perform both composed image retrieval (CoIR) and composed video retrieval (CoVR) without any supervised triplets, achieving strong results on CIRR, FashionIQ, WebVid-CoVR-Test, and a newly introduced Activitynet-CoVR benchmark.

## Strengths

- **First unified framework for composed image and video retrieval**: The paper is the first to explicitly consolidate CoIR and CoVR into a single model (Section 1, lines 14–18, 30). The unified training using both image-caption and video-caption pairs is a clean and well-motivated contribution that addresses an actual gap in the literature.

- **Strong zero-shot performance across multiple benchmarks**: Slerp⁺ achieves top Recall@1 on WebVid-CoVR-Test (Table 1), outperforming both zero-shot and supervised CoVR methods. On CIRR and FashionIQ (Tables 3–4), it achieves the highest recall at all ranks. The gains are especially notable given that the model uses only 0.32% trainable parameters.

- **Ablation study cleanly validates design choices**: Table 5 provides clear evidence that (1) both VTC and VTM losses contribute positively, (2) joint training on images+video outperforms single-modality training on both downstream tasks, and (3) Slerp outperforms simple embedding averaging for composition. This directly supports the paper's core methodological claims.

- **Parameter efficiency**: The model fine-tunes only LoRA adapters on the text encoder while freezing the vision encoder (0.32% of total parameters, Section 4.1). Despite minimal tuning, it achieves state-of-the-art results, which is a practical advantage for scalability and reproducibility.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Incomplete documentation of zero-shot image baselines' video adaptation**: The paper states that zero-shot image methods (SEARLE, CLIP4CIR, TAT, etc.) were run using "provided checkpoints on our setup" (Section 4.2, line 151), and describes adaptation for BLIP specifically (frame averaging or cross-attention, lines 147–148). However, for methods with different architectures (CLIP-based), the specific frame-level adaptation strategy (e.g., single frame vs. frame averaging vs. other pooling) is not stated. While the paper references the CoVR protocol, this should be made explicit for reproducibility. This does not undermine the core results, as the most controlled comparisons (BLIP Avg, BLIP CA, CoVR+Slerp, X-CLIP+Slerp) are all adequately described.

- **Hyperparameter *t* selection procedure not reported**: The Slerp balancing parameter *t* is set to 0.6 for videos and 0.7 for images (Section 4.1, line 147) without describing the selection process (validation split, grid search, or reference to prior work). A sensitivity analysis or a statement about how these values were chosen would strengthen the paper, especially since the same *t* is used for all comparisons.

- **Activitynet-CoVR benchmark lacks validation analysis**: The new benchmark (Section 4.1, line 135) is a useful contribution, but the paper provides no inter-annotator agreement, statistics on modification complexity (caption length, edit distance), example triplets, or discussion of potential artifacts. While the results are consistent with trends on other benchmarks, the benchmark's quality and difficulty are asserted rather than demonstrated.

- **No confidence intervals or variance estimates**: Several test sets are modest in size (e.g., 800 triplets for Activitynet-CoVR), yet all results are reported as point estimates without standard deviations across runs or bootstrapped intervals. This makes it difficult to assess whether the reported gaps (e.g., 23.4 vs. 21.8 R@1 on WebVid-CoVR-Test) are statistically significant.

### Trivial

- **"Slerp⁺ TAT" in Table 3 is undefined**: The paper mentions "Slerp⁺ TAT" (line 170) but does not explain what this row represents—e.g., whether it is the TAT method with Slerp applied or a different variant. This should be clarified.

## Nice-to-Haves

- Ablation comparing Slerp against linear interpolation without spherical normalization would isolate the benefit of the spherical geometry.
- Failure case analysis (qualitative examples where Slerp⁺ retrieves wrong results) would help assess whether unified training introduces systematic biases.
- A sensitivity plot of performance vs. *t* on a held-out validation set would strengthen the paper's hyperparameter claims.

## Removed Points

These points were raised by reviewers but removed or weakened after cross-checking against the paper. Treat with caution.

- **"Baseline adaptation for zero-shot image methods is a structural flaw"**: Overstated. The paper does describe video adaptation for BLIP-based methods (Avg and CA, lines 147–148) and references the CoVR protocol for others. The core comparisons (BLIP Avg, BLIP CA, CoVR+Slerp, X-CLIP+Slerp) are all documented. This is a documentation gap, not a structural flaw undermining the central evidence.

- **"CC3M subset selection is vague"**: The paper states "a subset of 2.3M pairs that was accessible to us" (line 129). This is a standard level of detail for web-crawled datasets; the specific filtering criteria are present in Section 4.1.

- **"Training for only 1 epoch is notable but not justified"**: Single-epoch training is common in zero-shot composed retrieval literature for efficiency, and the paper reports strong results with this setting. No justification is needed beyond the good performance.

- **"The ablation does not include a baseline that uses linear interpolation without spherical normalization"**: The ablation (Table 5c) already compares Slerp against simple embedding averaging—a different, simpler composition method. The critic's request for a specific variant is a nice-to-have, not a missing critical baseline.

## Novel Insights

None beyond the paper's own contributions. The key insight—that a single model trained on both image-caption and video-caption pairs with standard VTC/VTM losses can support both CoIR and CoVR via Slerp—is clearly articulated in the paper.

## Suggestions

1. **Document video adaptation for all baselines**: Specify exactly how each zero-shot image method (SEARLE, CLIP4CIR, TAT) was applied to video—frame sampling rate, pooling strategy, whether cross-attention was used. Even a brief statement ("following the standard frame averaging protocol from CoVR") would suffice.

2. **Report confidence intervals**: Add standard deviations from multiple runs or bootstrapped confidence intervals, especially for Activitynet-CoVR (800 triplets) and WebVid-CoVR-Test.

3. **Provide a sensitivity analysis for *t***: A figure showing R@1 vs. *t* (e.g., 0.3 to 0.9) on a validation subset would demonstrate that the chosen values are not overfitted to the test sets.

4. **Validate the new benchmark**: Add example triplets, modification complexity statistics, and ideally a small human evaluation or inter-annotator agreement score for the filtering step.

5. **Define "Slerp⁺ TAT"**: Add a footnote or sentence clarifying what this row in Table 3 represents.

## Score and Decision

The paper makes a genuine contribution by unifying composed image and video retrieval under a single model, with strong empirical results and clean ablations. The weaknesses are documentation-oriented rather than methodological. All issues are addressable in a revision. I recommend acceptance.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>