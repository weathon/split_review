Now I have all the information I need. Let me synthesize the final review.

## Summary

The paper introduces Slerp+, a unified framework for zero-shot composed visual retrieval (CVR) that handles both images and videos using a single model. The approach fine-tunes a BLIP model (with frozen vision encoder and LoRA-adapted text encoder) on image-caption (CC3M, 2.3M pairs) and video-caption (WebVid, 94K pairs) data using Vision-Text Contrastive (VTC) and Vision-Text Matching (VTM) losses. At inference, Spherical Linear Interpolation (Slerp) composes visual and textual embeddings. The paper also introduces Activitynet-CoVR, a new video benchmark for composed retrieval. Results across four benchmarks (CIRR, FashionIQ, WebVid-CoVR, Activitynet-CoVR) show Slerp+ outperforms prior zero-shot and some supervised methods.

## Strengths

1. **First unified formulation of composed retrieval across images and videos**: The paper consolidates CoIR and CoVR into a single CVR task and demonstrates a single model can handle both modalities (Section 1, Figure 1). Prior work treated these tasks separately, and the results show joint training benefits both.

2. **Strong empirical results across multiple benchmarks**: Slerp+ achieves state-of-the-art or competitive results on CIRR (Table 3), FashionIQ (Table 4), WebVid-CoVR (Table 1), and the new Activitynet-CoVR (Table 2), often by noticeable margins over prior zero-shot methods. This breadth of superior performance is the paper's strongest evidence.

3. **Zero-shot capability surpassing supervised methods**: Slerp+ is trained only on image-caption and video-caption pairs (no compositional triplets), yet outperforms the supervised CoVR model on WebVid-CoVR-Test (R@1 and R@5, Table 1) and on Activitynet-CoVR (all metrics, Table 2), demonstrating that expensive triplet annotation can be bypassed.

4. **Simple and practical method**: The recipe (BLIP + LoRA + VTC/VTM + Slerp) is straightforward and computationally efficient (only 0.32% of parameters updated). The ablation in Table 5 confirms each component contributes positively.

5. **New benchmark (Activitynet-CoVR)**: Introduces a more challenging video composed retrieval benchmark with longer, more complex textual modifications, providing a valuable resource for the community.

## Weaknesses

### Fatal
None.

### Major

1. **Data quantity confound undermines the "mutual enhancement" claim**: The paper's thesis that joint training on both image and video data mutually improves both modalities is supported by ablation rows (f) and (g) in Table 5. However, the joint model is trained on CC3M (2.3M pairs) **plus** WebVid (94K pairs) — approximately 2.4M total. The image-only condition (row f) uses only CC3M (2.3M), and the video-only condition (row g) uses only WebVid (94K). The observed improvement could therefore come entirely from increased data quantity rather than cross-modal synergy. A proper control would compare the joint model against a model trained on CC3M plus an additional 94K *image*-caption pairs (e.g., from CC12M or YFCC). If the CC3M+94K-image model underperforms the CC3M+WebVid model on image retrieval, then the video modality provides genuine benefit beyond more data. Without this control, the paper cannot attribute the gains to multimodal synergy — a central claimed contribution.

### Minor

2. **Slerp interpolation parameter \(t\) is not justified**: The inference hyperparameter \(t\) is set to 0.6 for videos and 0.7 for images "by default" (line 147). The paper provides no sensitivity analysis, no validation-based selection procedure, and no discussion of whether these values generalize across datasets. Given that Slerp's composition quality depends on this scalar (as noted in the original Slerp paper), this omission is a reproducibility gap. At minimum, a sensitivity curve (R@1 vs. \(t\)) should be shown for one image and one video dataset.

3. **Comparisons in main tables (1–4) are confounded by different base models**: Slerp+ uses BLIP (ViT-L/16 + BERT with cross-attention), while many compared zero-shot methods (Slerp, SEARLE-XL, TAT) use CLIP (ViT-L/14 or ViT-B/32). The ablation in Table 5 (row f, "w/o video") does provide a BLIP-only baseline, but it is not included in the main comparison tables, making it difficult for readers to assess how much of the gain comes from the backbone architecture vs. the unified training. Including the BLIP-only baseline in Tables 1–4 would resolve this.

4. **Limited analysis of the new Activitynet-CoVR benchmark**: The benchmark construction uses VideoMAE-Large to filter video pairs with cosine similarity > 0.8, which may bias toward already-similar pairs. No analysis is provided of the complexity of the resulting textual modifications (e.g., average modification length, types of changes, proportion of intra-pair vs. inter-pair). This makes it difficult to assess the benchmark's difficulty beyond raw recall numbers.

5. **Overstated novelty**: The claim of being "the first to attempt to build a unified composed retrieval system" (line 30) is accurate in the specific framing of the CVR task, but the method itself is a straightforward assembly of existing components (BLIP's VTC/VTM losses, Slerp from Jang et al. 2024a, average frame features). The paper does not discuss challenges specific to unifying modalities (e.g., modality imbalance, differing temporal scales, domain gap between CC3M still images and WebVid videos). A more measured framing would better reflect the contribution's nature as a well-executed combination/extension rather than a conceptual leap.

### Trivial

6. Missing implementation details: The hard negative mining strategy for VTM is referenced to Li et al. (2021) but not described concretely (e.g., whether negatives are drawn cross-modally or within modality). Maximum token length for the concatenated video frame tokens is not stated.

7. No failure cases or qualitative error analysis in Figures 3–4, which would strengthen confidence in the method's behavior.

## Nice-to-Haves

- A controlled experiment isolating the effect of adding video data (as described in Major weakness #1). This would substantially strengthen the paper's core claim.
- Sensitivity analysis of the \(t\) parameter across datasets.
- Reporting results with multiple random seeds to establish statistical significance, though single-run evaluation is common in this setting.
- A brief discussion of potential negative transfer when modalities are highly imbalanced in data volume.
- Including the BLIP-only baseline in the main comparison tables.

## Removed Points

- **"The paper does not mention releasing code or checkpoints"**: Removed per rule — reproducibility concerns about missing code/checkpoints for a submission are not valid weaknesses; these are typically released post-acceptance.
- **"The ablation row (a,b?) actually shows the influence of frame count, not this control"**: Removed as factually incorrect — row (f) is explicitly "excluding video" and IS the BLIP-only baseline the reviewer claims is missing.
- **"Broader impact paragraph is generic"**: Removed per rule — societal impact paragraphs are not required to be detailed and this criticism is a formatting nitpick.
- **Missing related work discussion**: Removed per rule — I cannot verify existence of claimed missing references.
- **Various typo/formatting concerns**: Removed per rule — parser artifacts.
- **Strength Finder's claim about "mutual enhancement" as a strength**: Downgraded/qualified — it conflicts with the verified data quantity confound weakness. The claim may still be true, but the evidence is insufficient as presented.

## Novel Insights

The most interesting observation from the reviews is that the paper's central claim of "mutual enhancement between modalities" rests on an experimental design that does not control for data quantity — a subtle but consequential gap. While the paper shows that adding video data helps image retrieval, it does not show that this help is specific to video (as opposed to any additional data). Conversely, the paper's strongest contribution may not be the mutual enhancement claim at all, but rather the practical demonstration that a single, simple pipeline (BLIP + LoRA + Slerp) can achieve competitive performance across both image and video composed retrieval tasks without compositional supervision, and that the Activitynet-CoVR benchmark reveals supervised methods can generalize poorly to new video distributions. These two findings — the practical utility of the pipeline and the brittleness of supervised CoVR — are well-supported and do not depend on resolving the data quantity confound.

## Suggestions

1. **Isolate the cross-modal synergy claim**: Add a controlled experiment comparing (a) CC3M only, (b) CC3M + 94K extra image captions, (c) CC3M + 94K video captions. If (c) outperforms (b) on image retrieval, the claim of genuine cross-modal benefit is proven.

2. **Provide a sensitivity curve for \(t\)**: Show R@1 vs. \(t\) (e.g., 0.1 to 1.0) for at least one image dataset and one video dataset. If performance is stable over a range, state this; if not, justify the chosen value via a held-out validation split.

3. **Add a BLIP-only baseline to main tables**: Include the "w/o video" ablation (row f) in Tables 1–4 to clarify how much of the gain comes from BLIP itself vs. the addition of video data.

4. **Analyze Activitynet-CoVR complexity**: Report statistics on the textual modifications (length, edit distance between captions, proportion of intra- vs. inter-pairs) to help the community understand the benchmark's difficulty.

5. **Tone down novelty claims**: Replace "first to attempt to build a unified composed retrieval system" with a more precise description (e.g., "first to extend Slerp-based zero-shot composed retrieval to jointly handle images and videos in a single model") to better match the incremental but solid contribution.

## Score and Decision

The paper addresses a worthwhile goal (unified composed retrieval) with a clean, practical method and achieves strong results across multiple benchmarks. However, a core supporting claim — that joint training creates mutual enhancement between modalities — is not convincingly isolated from a data quantity confound. This gap is significant but not fatal to the paper's overall contribution, since the method's practical effectiveness stands on its own empirical results. The SOTA results, new benchmark, and simple recipe constitute a solid empirical contribution. The paper would benefit from the controlled experiment described above, but the current work is still a reasonable submission.

**Score**: 6.0

**Decision**: Accept

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>