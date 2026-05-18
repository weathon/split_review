Now I have a thorough understanding of the paper. Let me synthesize the final review.

---

## Summary

This paper introduces a novel referring segmentation task for multi-modality abdominal MRI, where weak scribble annotations on a single reference modality (T1w) simultaneously guide segmentation of four unseen target modalities (T2w, DWI, In-phase, Opposed-phase). The authors contribute a new annotated dataset of 534 cases with 3,277 organ annotations across five modalities, and propose CrossMR, a model using paired data augmentation and organ-specific bipartite matching built on SEEM. Results show CrossMR outperforms four baselines (nnUNet, PerSAM-F, MedSAMScribble, nnUNet-Scribble) by 9–20% DSC on out-of-distribution modalities while remaining competitive on the in-distribution T1w modality.

## Strengths

- **Novel task formulation with clinical motivation.** The paper is the first to formulate referring segmentation for multi-modality MRI, where scribbles on a single reference modality drive segmentation across multiple modalities. This directly addresses the real clinical burden of annotating each modality separately. The framing is clearly distinguished from traditional unsupervised domain adaptation, which focuses on a single target modality.

- **Large annotated multi-modality dataset.** The authors created a labeled dataset of 534 cases with 3,277 organ annotations (liver, left kidney, right kidney, spleen) across five MRI modalities (T1w, T2w, DWI, In-phase, Opposed-phase). Annotations were performed by a junior radiologist and reviewed by a senior radiologist. The dataset will be publicly released, providing a valuable benchmark for the community.

- **CrossMR achieves strong empirical results on OOD modalities.** In Table 1, CrossMR exceeds the second-best baseline by 9.83% DSC (T2w), 9.72% (DWI), 19.56% (In-phase), and 5.66% (Opposed-phase), with large and consistent improvements across all organs. These are not marginal differences — they represent substantial gains in segmentation quality on unseen modalities.

- **Ablation study validates each design component.** Table 2 systematically ablates visual tokens, organ-specific bipartite matching, and paired augmentation, showing each component contributes to the overall performance. All variants outperform the SEEM baseline, confirming that the proposed modifications are individually beneficial.

## Weaknesses

### Major

- **No measures of variance reported for any quantitative result.** Tables 1 and 3 report DSC and NSD as point estimates without standard deviations, confidence intervals, or any measure of variability. The test set contains only ~10 subjects (10% of 105 patients), and the evaluation is conducted at the slice-pair level (4,277 pairs) where pairs within the same subject are not independent. Given the small subject-level sample size, it is unclear whether the reported differences — especially smaller ones like the T1w liver DSC gap between nnUNet (94.10) and CrossMR (91.89) — are statistically reliable. For a paper that positions its dataset as a benchmark, this is a significant gap that limits the actionability of the results.

- **Missing UDA baselines leaves an empirical gap in the generalization claim.** The paper contrasts its approach with unsupervised domain adaptation methods in Sections 1 and 2, and claims "significantly better generalization ability on four out-of-distribution modalities" (abstract). However, it does not compare against any cross-modality domain adaptation baseline (e.g., cycleGAN-based image translation followed by segmentation on each target modality), even though such methods represent a natural competitor for the cross-modality setting. The paper explicitly excludes these (Section 4.3: "We did not consider multi-stage models..."), citing the multi-stage and single-modality nature of UDA. While this scoping is understandable given the paper's focus on a single end-to-end model for all modalities, the claim of "generalization ability" would be substantially stronger if the reader could see how CrossMR compares to a pipeline that makes direct use of unlabeled target data — especially since the ablation study shows paired augmentation helps, and a cycleGAN approach also uses unlabeled target data for alignment. This does not invalidate the paper's core contribution, but it weakens the strongest claim in the abstract.

### Minor

- **Paired augmentation description overclaims modality-specificity.** Section 3.2 states that the first augmentation path "translates the T1w reference image to an image that resembles one of the five modalities." However, the actual augmentations described in Section 4.2 are generic intensity perturbations: random Gaussian/Gibbs noise, random contrast adjustment, and random scale intensity. These cannot produce tissue contrast profiles or artifacts specific to e.g., DWI (which has distinct diffusion weighting) or Opposed-phase imaging (which has specific fat-water cancellation patterns). The mismatch between the claimed purpose and the actual implementation is misleading. The empirical result that paired augmentation improves performance is valid (Table 2 confirms this), but the explanation of *why* is unsupported. Renaming this "random intensity augmentation" or using truly modality-specific transforms would resolve the issue.

- **Evaluation uses automatic scribble generation rather than real clinician scribbles.** As noted in Section 3.4, scribbles are generated algorithmically from ground-truth masks following Yu et al. (2019). While this is a standard practice for reproducible evaluation, it does not account for the variability, sparsity, or placement noise of real clinician-drawn scribbles. The paper could acknowledge this as a limitation.

- **Dataset composition description could be clarified.** The paper states "534 cases" derived from "2,146 abdominal MRI scans from 105 subjects" (Section 4.1), but the relationship between "cases" and "scans" is not explicitly defined. The number of cases varies substantially across modalities (e.g., 1,969 In-phase pairs vs. 284 DWI pairs in the evaluation set), which may reflect the underlying data distribution but is not discussed.

### Trivial

None.

## Nice-to-Haves

- **Report subject-level statistics.** The evaluation is conducted at the slice-pair level (4,277 pairs), but pairs within a subject are not independent. Reporting per-subject means with standard deviations across subjects would provide a more reliable estimate of variability.
- **Add at least one UDA baseline comparison.** A cycleGAN→segmentation pipeline on one target modality (e.g., T2w) would substantially strengthen the paper's generalization claim, even if the comparison is acknowledged to be imperfect due to the multi-stage, single-modality nature of UDA.
- **Clarify the paired augmentation strategy.** The paper should state whether each training iteration randomly picks a target modality or applies fixed augmentations, and should temper the claim that augmentations "resemble" specific modalities.

## Removed Points

- **Criticism about nnUNet using full supervision as a weakness:** The reviewer acknowledges this is a positive result for CrossMR (competitive with a fully-supervised specialist using only scribbles). This supports the paper, not weakens it. Removed.
- **Criticism about the paper not discussing training data differences with nnUNet:** The paper explicitly states nnUNet uses the same data split and is "a specialized model on this task." The discussion is adequate. Removed.
- **"Statistical significance tests should be reported" framed as a separate missing part:** This is subsumed under the Major weakness about missing variance measures. Removed as a separate point to avoid redundancy.
- **Generic weakness about "the paper should also cover Y / domain Z":** The reviewer's request for subject-level evaluation is already covered in Nice-to-Haves. Not a core weakness.

## Novel Insights

None beyond the paper's own contributions. The reviews confirm the paper's stated contributions without surfacing contradictions or revealing hidden limitations beyond those the authors partially acknowledge.

## Suggestions

1. Report standard deviations or confidence intervals for all metrics in Tables 1 and 3, ideally computed across subjects (not slice pairs) or over multiple random data splits.
2. Add at least one UDA baseline (e.g., cycleGAN → nnUNet) on a representative target modality to benchmark the paper's generalization claim against a method that uses unlabeled target data.
3. Rename "paired data augmentation" to something like "random intensity augmentation" and temper the claim that it generates modality-specific images. Alternatively, incorporate actual modality-specific transformations and demonstrate their effect.
4. Acknowledge the limitation that scribbles are algorithmically generated and that real clinician scribbles may exhibit different variability.

## Score and Decision

The paper makes a clear contribution: a novel task formulation, a carefully annotated multi-modality dataset, and a baseline method with strong empirical results. The weaknesses are real (missing variance measures, overclaimed augmentation description) but do not invalidate the core contributions. The missing UDA comparison is somewhat mitigated by the paper's explicit scoping. I recommend acceptance with a request to address the variance and augmentation clarity issues in a revision.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>