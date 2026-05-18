Now I have everything I need. Let me produce the final consolidated review.

---

## Summary

This paper introduces a new task — image-based referring segmentation for multi-modality abdominal MRI — where a weak scribble on a single reference modality (T1w) guides simultaneous segmentation of four abdominal organs across five MRI modalities. The authors contribute a new dataset of 534 cases (3,277 annotated organs) across T1w, T2w, DWI, In-phase, and Opposed-phase modalities, and propose CrossMR, a model built on SEEM with paired data augmentation and organ-specific bipartite matching. Results show competitive performance on the in-distribution T1w modality and substantially better DSC/NSD on four out-of-distribution modalities compared to several baselines, with 5–19% DSC improvements.

## Strengths

- **First formulation of a clinically motivated task.** The paper defines a novel referring segmentation task for multi-modality MRI where one weak scribble on a single reference modality enables segmentation across multiple unseen modalities with one model. This cleanly departs from prior cross-modality domain adaptation work, which typically targets one modality at a time with multi-stage pipelines (Section 1). The clinical motivation — reducing annotation burden when patients undergo multiple MRI sequences — is clear and well-articulated.

- **Large, carefully annotated multi-modality dataset.** The authors produced and will release a dataset of 534 cases (3,277 organ masks) across five modalities, annotated by a junior radiologist and verified by a senior radiologist (Section 4.1). This provides the first public benchmark for the proposed referring segmentation task and is a tangible community contribution.

- **Strong empirical results with ablative validation.** On four OOD modalities, CrossMR outperforms the second-best method by large margins (5.66–19.56% average DSC, Table 1) and similarly on NSD (e.g., 15.98 points for liver on In-phase). The ablation study (Table 2) systematically evaluates five architectural variants — removing visual tokens, organ-specific matching, paired augmentation, and cross-batch visual tokens — and each variant underperforms the full model while still beating the SEEM baseline. This provides credible evidence that each proposed component contributes positively.

- **Practical annotation efficiency.** Unlike scribble-prompt baselines that require a new prompt per target image, CrossMR uses only one scribble on the reference modality to segment all targets (Section 5). Compared to one-shot models like PerSAM-F, it requires weaker supervision (scribble vs. full mask) and no test-time fine-tuning, making the efficiency advantage concrete.

## Weaknesses

### Fatal
None.

### Major

- **Ambiguity in baseline training protocols undermines quantitative comparison.** The paper compares CrossMR against MedSAM-Scribble and nnUNet-Scribble but does not clearly state what data these baselines were trained on. The description for MedSAM-Scribble — "trained with samples of size 256×256 and the same data augmentation used for the target images in CrossMR is used for consistency" (Section 4.3) — does not specify whether "samples" means T1w images only, all five modalities, or some other set. Similarly, nnUNet-Scribble's training data is not explicitly stated. Since the paper's core claim is that "our goal is to leverage only the annotations of the reference T1w modality for model training" (Section 1), it is critical to confirm that all baselines follow the same constraint. If baselines were trained on target modalities they should not have access to, the comparison is unfair; if they were also limited to T1w data, the paper should state this explicitly. Without this clarity, the large performance gaps claimed (9–19% DSC) cannot be confidently attributed to CrossMR's design rather than differential training conditions. Additionally, PerSAM-F receives a full reference mask rather than a scribble — a different annotation strength — and the paper should note this asymmetry in the comparison. A summary table of each baseline's training data, supervision type, and annotation strength would resolve this issue.

### Minor

- **Paired data augmentation's claimed mechanism is not validated.** The paper states that the first augmentation set "translates the T1w reference image to an image that resembles one of the five modalities" (Section 3.2), yet the only operations listed (Section 4.2) are generic intensity perturbations — Gaussian/Gibbs noise, contrast adjustment, and scale intensity. These are standard augmentations, not modality-specific transformations. No examples of augmented images compared to real target-modality images are provided, nor is any distributional analysis (e.g., feature-space overlap) that would demonstrate the augmentation actually bridges the domain gap. The ablation study confirms the augmentation is empirically beneficial (Table 2), which is valuable, but the mechanism claim ("resembles one of the five modalities") remains unsupported. The paper should either provide evidence that the augmented distribution meaningfully covers the target modality distributions, or revise the mechanistic claim to more accurately describe what the augmentation achieves.

- **No standard deviations, confidence intervals, or significance tests reported.** The DSC/NSD results in Tables 1 and 3 report only point estimates. Given the large number of evaluation pairs (4,277), reporting variability is straightforward and would help assess whether the reported margins are reliable or within natural variation. This is especially relevant for the smaller OOD modality subsets (e.g., 284 pairs for DWI).

### Trivial
None.

## Nice-to-Haves

- **Cross-subject evaluation.** The paper evaluates same-subject pairs, which is aligned with the stated clinical scenario (same patient, multiple modalities). However, a cross-subject evaluation (training on one set of subjects, testing on unseen subjects) would strengthen the generalization claims and is suggested as future work by the authors themselves (Section 5). Adding even a small-scale cross-subject experiment would make the robustness claims more concrete.

- **Qualitative visualization of augmented images.** Showing examples of paired-augmented images alongside real target-modality images would help the reader assess whether the augmentation indeed produces target-like appearances, addressing the mechanism validation concern above.

- **Model size and inference speed.** For clinical deployment, reporting parameter count and runtime vs. baselines would be useful context.

## Removed Points

- **Criticism that evaluation is limited to same-subject pairs, overstating generalization.** Removed because the paper clearly scopes the task to the same-subject setting ("our goal is to leverage only the annotations of the reference T1w modality for model training to segment all five modalities during inference," Section 1). The term "out-of-distribution" explicitly refers to modality shift, not subject shift (Section 4.3). The paper acknowledges cross-subject as future work. This criticism evaluates the paper against a different (cross-subject) task than the one proposed. Moved to Nice-to-Haves as a suggestion for further strengthening.

## Novel Insights

The reviewers collectively identify an important tension in the paper: the paired augmentation is simultaneously the method's most innovative training strategy and its least validated component. The ablation shows the augmentation *helps*, but the paper's narrative about *how* it helps (making T1w resemble other modalities via generic intensity perturbations) lacks mechanistic evidence. This creates an explanatory gap: if the augmentation is too generic to be modality-specific, the strong OOD performance may be driven more by the cross-attention mechanism matching reference scribble features to target features — meaning the augmentation may serve primarily as a regularizer rather than a modality translator. Resolving this would sharpen both the paper's technical contribution and its reproducibility.

## Suggestions

1. **Clarify baseline protocols explicitly.** Add a table specifying for each baseline: training data modality (T1w-only vs. all), supervision type (scribble vs. full mask), whether fine-tuned or zero-shot, and annotation strength. This single addition would resolve the paper's most worrying ambiguity.

2. **Provide augmented image examples.** Include a figure showing real T1w → augmented → real T2w/DWI/In-phase/Opposed-phase side-by-side comparisons, ideally with a quantitative distributional measure (e.g., classifier-based modality prediction accuracy on augmented images).

3. **Report standard deviations** for the main DSC/NSD results, computed across subjects or evaluation pairs.

4. **Tone down the mechanistic claim** about the augmentation unless supporting evidence is added. Replace "resembles one of the five modalities" with a more precise description of what the augmentation achieves (e.g., "introduces contrast and noise diversity to improve robustness to domain shift").

## Score and Decision

The paper makes a meaningful contribution: a new task, a useful dataset, a sensible architecture with clean ablations, and strong quantitative results. The main unresolved issue — ambiguity in baseline training conditions — is addressable in a rebuttal and does not invalidate the core contribution. The paper should be accepted with the expectation that the baseline protocols are clarified.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>