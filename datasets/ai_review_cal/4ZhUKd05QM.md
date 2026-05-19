- Decision: Reject
- Avg Score: 3.80
- Scores: 3, 5, 3, 3, 5
Now I have a thorough understanding of the paper and have verified the reviewer claims against the actual text. Let me compose the consolidated review.

---

## Summary

This paper proposes LGDiffGait, a gait recognition framework that explicitly models frame differences at two levels: local (sliding-window pooling-based subtraction, LDM) and global (temporal-average subtraction, GDM), followed by a Temporal Alignment Module (TAM) to integrate the difference features with the main spatial-temporal features. Experiments on CASIA-B, OUMVLP, GREW, and Gait3D report competitive or state-of-the-art results, and an ablation study on Gait3D shows consistent 1–3% gains from each module.

## Strengths

- **State-of-the-art or competitive results across four diverse benchmarks.** The paper reports Rank-1 accuracies of 95.2% (CASIA-B), 92.3% (OUMVLP), 82.7% (GREW), and 74.2% (Gait3D), outperforming a range of set-based, conv3D, and temporal-modeling methods (Tables 1–4). These results cover controlled indoor, large-scale multi-view, and in-the-wild settings.

- **Clean ablation study confirming the contribution of each proposed module.** Table 5 on Gait3D shows that LDM alone (+1.7% Rank-1), GDM alone (+1.4%), both combined (+2.6%), and the addition of TAM (+0.4%) each provide measurable improvements. The ablation is controlled (same data augmentation, same training pipeline) and demonstrates that the modules are complementary.

- **Thorough evaluation across diverse real-world covariates.** The four datasets span indoor/outdoor settings, varying camera views (11 views on CASIA-B, 14 on OUMVLP), clothing/carrying variations, and large-scale unconstrained environments (GREW with 26K subjects, Gait3D with occlusion/misalignment). This breadth supports claims of robustness.

## Weaknesses

### Fatal
None. The paper's core idea — explicit local and global differencing in a 3D CNN pipeline — is sound, and the ablation study provides controlled evidence for its effectiveness.

### Major

- **The LDM description contains an unresolved dimensional inconsistency (documentation error).** Equation (2) defines `F_l_diff = F_in - AvgPool3d^{3×1×1}(F_in)`, and line 102 explicitly states that AvgPool3d uses *both a kernel size and a stride of 3×1×1* along the temporal dimension. With stride 3, the pooled output has temporal length approximately T/3, which cannot be subtracted from the original `F_in` (size C×T×H×W). The paper claims that replicate padding "allows the sliding window pooling to operate across the entire sequence without changing the temporal length" — this is false for stride 3. The surrounding description ("sliding window," "adjacent frames," "without changing the temporal length") strongly suggests the authors intended stride 1, but the text as written specifies stride 3, making the operation dimensionally impossible as described. This must be corrected for the method to be reproducible.

### Minor

- **SOTA comparison may conflate architecture gains with augmentation pipeline gains.** The implementation section lists several aggressive augmentations (rotation, perspective transformation, affine transformation) that are not standard in gait silhouette recognition. The paper does not explicitly state whether competitor numbers are taken from original publications (which likely did not use these augmentations) or re-implemented with the same augmentation in OpenGait. The ablation study (Table 5) is controlled and provides the strongest evidence for the modules' contributions, but the headline SOTA claim is harder to interpret without a controlled comparison.

- **No statistical variance reported.** The results are presented as single-run point estimates. The improvements over strong baselines are modest (2–4%), and in a crowded benchmark where methods cluster within a few percent, run-to-run variance could affect the ordering. Reporting mean ± std over multiple runs (even 3) for at least one dataset would substantially strengthen the evidence.

- **Baseline model in the ablation study is not clearly defined.** The ablation baseline is "when neither LDM nor GDM is applied," but the paper does not specify the architecture, channel count, or number of layers of this baseline. Without this, the reader cannot assess whether the baseline is reasonable or weak, making the ablation percentages harder to contextualize.

- **No analysis of window size sensitivity.** The LDM uses a fixed window size of 3 frames with no experiment showing how performance varies with window size 2, 4, or 5. This design choice appears arbitrary.

### Trivial

- None that are not parser artifacts.

## Nice-to-Haves

- **Visualization of difference features.** The paper motivates its approach with Figure 1 (frame differences) but never shows what the LDM or GDM actually learns (e.g., t-SNE, saliency maps, or difference feature visualizations). Such analysis would strengthen the intuition.

- **Computational cost analysis.** The conclusion acknowledges that LDM and GDM increase network complexity, but no FLOP/parameter/inference-time comparison is provided. Quantifying the cost of the 2–3% gain would help practitioners assess the trade-off.

- **Per-condition analysis of where the modules help most.** On CASIA-B, the CL (coat) condition sees the largest gain. A discussion of *why* — e.g., LDM being more valuable when static shape cues are obscured — would add scientific depth beyond descriptive reporting.

## Removed Points

- **"Tables are missing from the extracted text"** — This is a PDF parser artifact, not an author error.
- **"Abstract numbers presented without qualification"** — This is standard practice in research papers; the contributions are supported by the full experimental section.
- **Strength: "Clear and well-specified formulation of local and global difference operators"** — Removed because it conflicts with the verified Major weakness (the LDM has a dimensional inconsistency in its description, so it is *not* clearly specified).
- **Various generic criticisms about the method section** (e.g., "no justification for TAM architecture choice over simpler alternatives") — These are design-preference concerns, not actual weaknesses; the paper provides a reasonable design and ablation evidence.
- **Criticisms about missing appendix content, missing proofs, or unreleased references** — Per policy, these sections are stripped by the parser and are assumed to exist in the original submission.

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface any unexpected perspective on the paper that the authors themselves do not already articulate.

## Suggestions

1. **Fix the LDM specification:** Change the stride of AvgPool3d from 3×1×1 to 1×1×1 (overlapping windows) to match the text's claim about preserved temporal length. Alternatively, include explicit pseudocode or a tensor-shape trace to resolve the ambiguity.
2. **Clarify the comparison methodology:** State explicitly whether competitor results are from published papers or from re-implementations in OpenGait with the same augmentation pipeline. Ideally, re-run the strongest baseline (e.g., DeepGaitV2 or GaitGL) with the paper's augmentation and report that controlled comparison.
3. **Report variance:** Add mean ± std over at least 3 runs for one dataset (CASIA-B or Gait3D) to demonstrate that the improvements are stable.
4. **Define the ablation baseline:** Specify the architecture of the baseline model used in Table 5.
5. **(Optional)** Add a window-size sensitivity experiment for LDM, and a FLOP/parameter comparison.
