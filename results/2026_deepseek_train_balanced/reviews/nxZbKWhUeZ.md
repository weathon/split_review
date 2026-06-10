Here is the final consolidated review.

---

## Summary

This paper proposes HoughPL, a prompt learning framework for Segment Anything Models (specifically SEEM) that learns three spatial prompts and three semantic prompts per visual concept, processes each through a different morphological post-processing operation (max-pooling, max-then-min pooling, min-pooling — framed as "inner/middle/outer voting mechanisms"), and averages the results. The paper claims these mechanisms enforce prompts to specialize to different object sub-regions and capture complementary spatial/semantic clues. Experiments on Cityscapes, Mapillary Vistas, ADE20K, and ACDC report improvements over CoOp, LOCN, and SSPrompt.

## Strengths

- **Novel multi-prompt direction for SAM prompt learning.** Prior work (SSPrompt) learns a single spatial prompt per concept. The idea of learning three spatial prompts per concept — each with different post-processing — is a plausible and clearly differentiated direction, as illustrated in Figure 1. This reframes the prompt learning space from "learn one prompt" to "learn an ensemble of prompts with different spatial focus operations."

- **Compositional design validated by progressive ablation.** The ablation (Table 4, described in text) shows that adding inner-region, then middle-region, then outer-region voting, and finally semantic prompts yields progressively better performance on Cityscapes. Each component contributes positively, consistent with the design's internal logic.

- **Computational cost is reasonable.** Training efficiency (Table 5) is reported as comparable to CoOp and LOCN despite learning six prompts total, which is practically relevant for few-shot adaptation settings.

- **Parameter sensitivity is analyzed.** A sweep of the neighborhood size r from 3 to 11 (step 2) on Cityscapes (Table 6) identifies the optimal operating range and shows the trade-off between contextual coverage and boundary over-smoothing.

## Weaknesses

### Fatal
None. The method may have empirical value even if its claimed mechanism is unsupported and its framing is misleading.

### Major

- **The Hough Voting framing is misleading — the method performs morphological post-processing, not Hough voting.** The paper's title, narrative, and claimed novelty are built on an analogy to Hough Voting (Hough 1959; Ballard 1981), but the three "voting mechanisms" are standard morphological operations applied to predicted output masks: inner-region voting is dilation (max-pool over a neighborhood, Eq. 7), middle-region voting is morphological closing (max-pool then min-pool, Eq. 8), and outer-region voting is erosion (min-pool, Eq. 9). There is no parametric shape representation, no transformation to a parameter space, no peak detection, and no coordinate-space voting — i.e., nothing that constitutes a Hough transform. Section 2 devotes a full paragraph to the history of Hough Voting (lines 35–36) and cites HoughNet as a neural voting approach, but the proposed method shares none of these mechanisms. The method is more honestly described as "multi-prompt learning with morphological aggregation." This is not a minor naming issue; the paper's central framing and novelty claims depend on a connection that does not hold under scrutiny.

- **The claimed mechanism for prompt regional specialization is unsubstantiated.** The paper repeatedly asserts (e.g., lines 21, 120–142, 154) that the voting mechanisms "enforce" their respective prompts to "focus on and learn from" inner, middle, or outer object regions. However, the voting operations are applied to output masks *after* decoding, not to the prompts or to the feature extraction process. The three spatial prompts Z_inner^S, Z_middle^S, Z_outer^S are simply three sets of learnable embeddings passed through the same frozen encoder and decoder — the only differentiation comes from the different post-processing operations applied to their respective output masks. There is no explicit spatial decomposition, no attention masking, no region-specific feature pooling, and no regularization that would force different prompts to encode different spatial information. The prompts could converge to nearly identical representations with the morphological operations alone providing the differentiation. The paper provides zero evidence of specialization: no attention maps, no embedding visualizations (PCA/t-SNE), no spatial attribution analysis, no region-specific IoU breakdowns. This central claim — that prompts capture "complementary spatial clues from different sub-regions" — is asserted without mechanistic support or empirical verification.

- **The reported performance improvements are suspiciously uniform.** Section 4.2 states that HoughPL "outperforms the state-of-the-art methods by 5.5 in mIoU for semantic segmentation, 5.5 in AP for instance segmentation, and 5.5 in PQ for panoptic segmentation on average." Achieving exactly the same improvement magnitude (5.5) across three different metrics with different ranges and scales, averaged over multiple datasets, is highly improbable in practice. This suggests either rounding artifacts, selective reporting, or an error. Without per-dataset, per-metric breakdowns with standard deviations or significance tests, the reader cannot assess these claims.

- **Baseline comparisons are ill-matched to the task.** CoOp and LOCN are prompt learning methods designed for CLIP-based image *classification*, not for SAM-based *segmentation*. They learn text-side prompts for category prediction and do not learn spatial prompts at all. Using them as primary baselines for a SAM spatial-prompt-learning method inflates the apparent advantage. Only SSPrompt (Huang et al., 2024) addresses the same task (learning spatial prompts for SAMs). The paper should either adapt CoOp/LOCN to the segmentation setting properly or focus on segmentation-specific baselines.

### Minor

- **HoughSemPL lacks any architectural mechanism for region-specific semantic learning.** The three semantic prompts (Z_inner^T, Z_middle^T, Z_outer^T) are text-side embeddings processed by the text encoder — they have no access to spatial features. The paper claims they learn semantics from different spatial regions, but there is no cross-attention between spatial features and semantic prompts, no spatial masking, and no region-specific feature pooling. The "association" with spatial prompts is only by training pairing (Z_inner^S paired with Z_inner^T). Without an inductive bias, all three semantic prompts can converge to similar representations.

- **The method is evaluated on SEEM, not SAM (Kirillov et al.).** The title and abstract reference "Segment Anything Model" generically, but Section 4.1 specifies SEEM with Focal-Tiny and DaViT-Large backbones. While SEEM is also a SAM-family model, its architecture differs from SAM in prompt encoding and mask decoding. The paper should evaluate on SAM directly (the model most readers associate with the title) or qualify the title.

- **Table reference error.** Line 219 cites "As Tables 3 demonstrates" for evidence of generalization across backbones, but Table 3 is labeled "Performance versus number of data on semantic segmentation." The table or the text reference is misassigned.

### Trivial

- Several typos: "outter" for "outer" (lines 118, 162), "robuts" for "robust" (line 154), "sup-optimal" for "sub-optimal" (line 75), "perfomance" for "performance" (line 197), "illustraced" for "illustrated" (line 49), "perserve" for "preserve" (line 231), "learining" for "learning" (line 95).

## Nice-to-Haves

- Report standard deviations or confidence intervals across multiple runs, especially for 16-shot data where variance is expected to be high.
- Provide direct visual evidence of prompt specialization (e.g., GradCAM on mask decoder attention, or region-specific IoU per prompt).
- Disentangle the ensemble effect from the specific morphological design via ablations: (a) three prompts with identical post-processing, (b) one prompt with three different post-processing operations averaged.
- Report per-dataset breakdowns of the 5.5 average improvement claim.

## Removed Points

- Unreadable tables / inability to assess experimental evidence: This is a PDF extraction artifact; the original submission contains readable tables. However, the suspiciously uniform 5.5 claim is retained because it appears in the paper's text.
- Missing appendix content, proofs, or references: Parser strips these from all submissions; they exist in the original.
- Formatting/equation artifacts (e.g., "XdTefault", "XlSear", broken LaTeX): These are PDF-to-text extraction errors, not author issues.
- "The r parameter is not adequately analyzed": The paper does provide a sweep from r=3 to r=11; this criticism was inaccurate.
- "No evaluation on SAM": Weakened to Minor — SEEM is a SAM-family model, but the title's specificity is a fair concern.
- Various generic area-of-concern speculations (e.g., "could the prompts not specialize," "could confounders exist") without concrete evidence: removed as they lack specific anchoring in the paper's content.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Remove the Hough Voting framing or explicitly label it as a loose analogy. Rename the method to reflect what it actually does — e.g., "Multi-Region Spatial Prompt Learning with Morphological Aggregation" — and adjust the title, abstract, and narrative accordingly.
2. Provide direct evidence that the three prompts learn different spatial information (attention visualization, embedding analysis, or region-specific evaluation).
3. Report per-dataset, per-metric results with standard deviations to allow verification of the claimed 5.5 improvement.
4. Include SAM (Kirillov et al., 2023) as an evaluation backbone to justify the title.
5. Replace or supplement CoOp/LOCN baselines with segmentation-specific prompt learning methods.

MY FINAL SCORE: <score>3.5</score>
MY FINAL DECISION: <decision>Reject</decision>