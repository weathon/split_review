Now I have all the information I need. Let me synthesize the final review.

## Summary
This paper introduces a novel task—cross-modality referring segmentation for abdominal MRI—where a scribble on a reference T1w modality guides segmentation across four target modalities (T2w, DWI, In-phase, Opposed-phase). The authors contribute a new multi-modality MRI dataset with 3,277 organ annotations across five modalities and propose CrossMR, built on SEEM with paired augmentation and organ-specific bipartite matching. The core claim is that CrossMR achieves competitive performance on the in-distribution modality and significantly better generalization on out-of-distribution modalities compared to state-of-the-art approaches.

## Strengths
1. **Novel task formulation.** The paper is the first to define image-based referring segmentation for multi-modality MRI, where a single weak annotation (scribble) on a reference modality simultaneously guides segmentation of multiple target modalities. This is a genuine conceptual advance over single-target cross-modality domain adaptation and over scribble-prompt models that require per-image scribbles (Section 1, Section 2).

2. **Large-scale, multi-modality annotated dataset.** The authors provide a publicly available dataset with 3,277 organ masks across five MRI modalities (T1w, T2w, DWI, In-phase, Opposed-phase) from 534 scans, double-annotated by a junior and senior radiologist (Section 4.1). This fills a gap for benchmarking cross-modality referring segmentation.

3. **Significant quantitative gains on OOD modalities.** On the four OOD target modalities, CrossMR outperforms the second-best method by margins of 9.83%, 9.72%, 19.56%, and 5.66% in mean DSC (Table 1, Section 4.4). These improvements are substantial, consistent across organs, and supported by qualitative visualizations (Figure 3).

4. **Ablation validates key design choices.** Each component—visual tokens from reference scribbles, organ-specific bipartite matching, and paired data augmentation—is shown to be critical, with the full model achieving the highest average DSC across OOD modalities (Table 2, Section 4.5).

5. **Practical reduction of annotation burden.** CrossMR uses a single scribble on one reference modality to segment all five modalities, unlike MedSAM-Scribble or nnUNet-Scribble which require direct scribble input on every target image (Section 5). The end-to-end single-model design also contrasts with multi-stage cross-modality pipelines.

## Weaknesses

### Fatal
None.

### Major
1. **Insufficiently validated slice-pairing protocol.** The evaluation pairs reference and target slices "in a one-to-one fashion while maintaining the relative order of the slices" (Section 4.3). The paper does not discuss whether different modalities have different slice thicknesses, slice counts, or resolutions, nor does it validate that the matching produces anatomically corresponding slices. The widely varying number of evaluation pairs per modality (e.g., 284 for DWI vs. 1,969 for In-phase) suggests different volumetric resolutions, yet no analysis of potential misalignment is provided. If slices are mismatched, ground-truth masks from the reference slice would not correspond to the target anatomy, making quantitative results partly uninterpretable. This is the most significant gap in the current paper and should be addressed by reporting slice counts per modality, describing the matching algorithm in detail (e.g., truncation, interpolation), and showing example paired slices with overlay masks to confirm alignment.

### Minor
1. **SEEM baseline setup is underspecified.** The ablation study reports a ~46% DSC gap between baseline SEEM and CrossMR on T2w, yet the incremental ablations (removing individual components) account for only a few percentage points each. The paper says SEEM was evaluated "to observe how the overall change in the architecture impacts the performance" (Section 4.5) but does not clarify whether SEEM was trained on the same data, fine-tuned, or used with original pretrained weights. If the latter, the comparison is not informative. The unexplained gap undermines the ablation study's ability to attribute improvements to specific components.

2. **nnUNet training data needs clarification.** The paper states nnUNet was "trained from scratch with the same data split as the CrossMR" (Section 4.3). Since the dataset has full annotations for all five modalities, it is unclear whether nnUNet was trained only on T1w images (fair comparison) or also on target modality ground truth. The paper should explicitly state what supervision nnUNet received. (Note: this does not invalidate the results—if nnUNet used only T1w data, the comparison is sound; if it used target-modality masks, the comparison is even more favorable to CrossMR—but the ambiguity should be resolved.)

3. **No confidence intervals or variance estimates.** None of the quantitative results include standard deviations, confidence intervals, or per-subject variability. Given the moderate dataset size and the highly variable number of evaluation pairs per modality (284–1,969), reporting only point estimates is insufficient to assess the reliability of the claimed improvements.

4. **Scribble quality sensitivity not analyzed.** The automatic scribble generation uses random parameters (Section 3.4). The paper presents no analysis of how sensitive results are to scribble length, width, location, or sparsity. This is important for practical deployment where clinicians may draw scribbles of varying quality.

5. **Inference time and computational cost not reported.** A key claim is that CrossMR reduces annotation burden relative to methods requiring per-image prompts, but no inference speed or memory comparison is provided. This is a practical missing component.

### Trivial
None.

## Nice-to-Haves
- Visual examples of the paired augmented images alongside real target modality images, to support the claim that augmentation produces "target-like" appearances.
- Failure case analysis for organs/modalities with unusually low DSC.
- A discussion of how the method would handle scenarios where the reference modality and target modalities are acquired at different time points or are missing for some subjects.

## Removed Points
- **Criticism about nnUNet being "inappropriate" / "apples-to-oranges":** The critic claims nnUNet was trained with "full supervision on the target modalities" and that CrossMR outperforming it is suspicious. The paper says nnUNet was "trained from scratch with the same data split." There is no statement that nnUNet used target-modality ground truth; the critic's inference is unsupported. If nnUNet was trained on T1w data only, the comparison is standard and the large OOD gap is simply evidence that CrossMR's referring mechanism is effective. This criticism is removed as a misunderstanding.
- **Criticism about "out-of-distribution" language:** The critic argues these modalities are not truly OOD because they come from the same subjects/scanner. The paper clearly defines OOD as modalities not seen during training (Section 4.3), which is standard usage. Removed.
- **Criticism about PerSAM-F scribble conversion:** The paper says it uses "the reference-mask pair as the support set" — the full mask is used, not the scribble. This is clear from the text. Removed.
- **Criticism about MedSAM-Scribble/nnUNet-Scribble scribble standardization:** The paper describes scribble input as a "second channel." This is sufficiently specified. Removed.
- **Criticism that T1w results are "suspicious":** The paper notes nnUNet is a "specialized model" on the T1w task. CrossMR matching it is not suspicious—it demonstrates that the referring formulation can match a fully supervised model when tested on the training modality. Removed.
- **Criticism about visual tokens contributing little:** The paper discusses this result and provides a plausible explanation (organ shape priors from queries + paired augmentation). Removed as the paper already addresses it.

## Novel Insights
The reviews surface a useful observation: the paper's paired data augmentation uses standard intensity augmentations (Gaussian noise, contrast, scale intensity) to simulate different MRI modalities. The harsh critic rightly notes that simple intensity scaling cannot fundamentally change tissue contrast (e.g., T1w→T2w contrast reversal where fat and water signal are inverted). This raises the question of whether CrossMR's generalization stems more from organ shape priors and the bipartite matching mechanism than from genuine cross-contrast feature alignment. The near-parity of CrossMR on T1w (ID) and its strong OOD performance, combined with the relatively modest drop when visual tokens are removed (~4%), suggests the model may be learning robust organ shape representations that are relatively invariant to contrast—a finding that is interesting but not explicitly discussed in the paper.

## Suggestions
1. **Validate and document the slice-pairing protocol.** Report the slice count range per modality, describe how mismatches are handled (truncation, interpolation, registration), and show example paired slices with overlaid masks to confirm anatomical correspondence.
2. **Clarify the nnUNet baseline** by explicitly stating what training data and annotations it received.
3. **Clarify the SEEM baseline** — was it trained on the same data, zero-shot, or fine-tuned? This affects how readers interpret the ablation.
4. **Add confidence intervals** (e.g., bootstrapped or per-subject) to the main results.
5. **Analyze scribble sensitivity** with a small ablation varying scribble sparsity and location.

## Score and Decision
This paper makes a clear contribution: a novel task formulation, a valuable new dataset, and a well-designed model that achieves substantial empirical gains. The weaknesses identified are genuine but addressable—none are fatal. The slice-pairing concern is the most significant and requires attention, but the overall contribution is solid and the results are likely robust. On balance, this is a strong paper that makes a meaningful contribution to the medical imaging community.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>