Now I have a thorough understanding of both the paper and the reviews. Let me produce the final consolidated review.

## Summary

This paper formulates a new task — cross-modality referring segmentation for abdominal MRI — where a single scribble annotation on one reference modality (T1w) guides segmentation of the same organs across four unseen target modalities (T2w, DWI, In-phase, Opposed-phase). The authors contribute a labeled dataset of 3,277 organ annotations across 534 scans from five MRI modalities, and propose CrossMR, a model based on SEEM with paired data augmentation and organ-specific bipartite matching. The key experimental finding is that CrossMR substantially outperforms several baselines on all four out-of-distribution modalities while remaining competitive on the in-distribution T1w modality.

## Strengths

- **First formulation of multi-modality MRI referring segmentation as a task.** The paper defines a meaningful new problem where weak scribble annotations on one modality can drive segmentation across multiple modalities, directly addressing the annotation bottleneck in multi-modality clinical workflows. The paper is explicit about the task setup and its differences from unsupervised domain adaptation (Section 1, Figure 1).

- **Publicly released dataset of substantial scale.** The dataset contains 3,277 annotated organs (liver, left kidney, right kidney, spleen) across 534 scans covering T1w, T2w, DWI, In-phase, and Opposed-phase, validated by a senior radiologist (Section 4.1). This is the paper's most concrete and durable contribution — it provides a common ground for future work on this task.

- **CrossMR achieves large and consistent gains on all OOD modalities.** Despite seeing only T1w images paired with augmentation-based surrogates during training, the model outperforms the second-best baseline by 9.83% (T2w), 9.72% (DWI), 19.56% (In-phase), and 5.66% (Opposed-phase) average DSC (Table 1). These margins are clinically meaningful and hold across all four organs.

- **Paired data augmentation is a simple and effective alternative to generative cross-modality synthesis.** Instead of requiring CycleGAN-style image translation to bridge modality gaps, the method applies two independent augmentation pipelines to the same T1w image during training. The ablation (Table 2) confirms this contributes ~3–4 DSC points on OOD modalities, validating the design choice without adding complexity.

- **Organ-specific bipartite matching addresses a practical multi-organ failure mode.** The modification prevents spatial queries for one organ from being matched to a different organ's ground truth during training. Ablation results (Table 2) show clear gains, especially on the challenging in-phase modality (+7.3 DSC).

## Weaknesses

### Fatal
None.

### Major

1. **Evaluation is limited to same-subject, slice-aligned pairs, which does not match the full clinical scenario.** The paper evaluates on reference–target pairs from the same subject with slice-to-slice correspondence (Section 4.3: "Paired images are chosen from the same subject… matching slices from the reference volume to slices from the target volume in a one-to-one fashion"). While the core claim — generalizing to *unseen modalities* — is supported (the model transfers from T1w to T2w, DWI, etc.), the clinical scenario described in Figure 1(b) implicitly involves new patients. The paper acknowledges cross-substitution as future work only in the conclusion (line 209), but the abstract and introduction do not convey this restriction. **Without cross-subject evaluation, it is unclear whether the model's cross-modality ability depends on anatomical correspondence between matched slices of the same patient.** Adding a cross-subject, unpaired-slice condition would significantly strengthen the contribution.

2. **Missing unsupervised domain adaptation baselines creates an incomplete comparison.** The paper explicitly excludes multi-stage cross-modality methods (e.g., CycleGAN + segmentation model) because they "heavily rely on transferring the source domain images into the target domain using image-level alignment" (Section 4.3). While this scope decision is understandable, it means the paper does not compare against the most relevant class of existing approaches for cross-modality segmentation. Many such methods can handle multiple targets, and readers cannot assess whether CrossMR's end-to-end design offers advantages over a pipeline-based alternative. At minimum, a comparison with one UDA method (e.g., CycleGAN-synthesized T2w → nnUNet) would ground the reported gains in the broader literature.

### Minor

1. **Paired augmentation coverage is not analyzed.** The method's reliance on paired augmentation to simulate target-like images is central, but the paper provides no quantitative analysis of whether the augmentations actually produce images whose intensity/contrast distributions match real T2w, DWI, In-phase, or Opposed-phase images (e.g., distributional distance metrics or visual similarity analysis). This makes it difficult to assess how the augmentation strategy might need to change for new modalities.

2. **The nnUNet baseline comparison is informative but predictable.** nnUNet is trained with full supervision on T1w only and tested on other modalities. The resulting performance drop is expected — it serves to illustrate the domain shift problem rather than to provide a competitive baseline. The large reported margins over nnUNet on OOD modalities are therefore less surprising than the paper implies. The comparison is not invalid, but it should be contextualized more carefully.

3. **The method is limited to 2D slice-level inference.** The paper acknowledges this as a limitation (Section 5) and mentions 3D extension as future work, but since the evaluation itself uses slice-matched pairs, the 2D design reinforces concerns about how the method would perform on unpaired slices in a true clinical volume.

### Trivial
None.

## Nice-to-Haves

- Evaluate sensitivity to scribble variability (placement, size, shape) on the reference image to confirm the method is robust to the natural variation of user input.
- Report cross-subject results on the existing dataset (the training/testing split is already at patient level, so this is feasible).
- Include distributional similarity metrics between augmented T1w images and real target-modality images.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"MedSAM-Scribble and nnUNet-Scribble comparison is unfair."** The paper states these baselines require scribbles on the target image (line 206), meaning they receive *more* information per modality than CrossMR (which uses one reference scribble for all targets). The asymmetry favors the baseline, not the proposed method. Per the review guidelines, criticisms where the asymmetry favors the baseline are removed.
- **"PerSAM-F comparison is unfair because it uses a full mask."** PerSAM-F uses a full mask as support (stronger annotation). CrossMR uses only a scribble (weaker annotation). If CrossMR still outperforms PerSAM-F, this asymmetry favors the baseline. Removed per review guidelines.
- **"nnUNet is a strawman baseline."** nnUNet is a standard supervised segmentation model. Testing it on OOD modalities is a common way to demonstrate the domain shift problem. The comparison is not a strawman; it is simply a known-expected gap. The point about missing UDA baselines (kept above) is the more substantive concern.
- **"Evaluation protocol invalidates the claimed generalization."** The paper's core claim is generalization to *unseen modalities* (T1w → T2w, DWI, etc.), which the experiments do support. Same-subject evaluation is a limitation (kept above as Major weakness 1) but does not invalidate the modality generalization claim. The paper acknowledges cross-subject as a harder future benchmark.

## Novel Insights

The most interesting insight from the reviews is that the paper's key design choice — paired data augmentation as a substitute for generative cross-modality translation — is both its primary strength and its least examined component. The ablation confirms that augmentation contributes meaningfully (~3–4 DSC), but the paper does not analyze what the augmentation pipeline actually learns about modality-specific intensity/contrast distributions. A deeper analysis could reveal whether the model is learning to be invariant to contrast variation or is doing something more nuanced. Additionally, the organ-specific bipartite matching contribution is well-motivated for multi-organ settings and addresses a problem (query-to-organ mismatch) that is likely to arise in other multi-organ referring segmentation frameworks.

## Suggestions

1. **Add cross-subject evaluation.** The existing patient-level split already supports this. Report DSC when reference and target come from different subjects (preferably with unpaired slices). This is the single most impactful addition the authors could make.
2. **Add at least one unsupervised domain adaptation baseline.** Compare against a pipeline of CycleGAN (or QS-Attn) + nnUNet trained on synthetic images for each target modality. This grounds the results against the most relevant family of existing methods.
3. **Analyze augmentation fidelity.** Report distributional similarity (e.g., Wasserstein distance on intensity histograms, or Fréchet Inception Distance adapted for MRI) between augmented T1w and real target-modality images to clarify what the augmentation strategy does and does not capture.
4. **Clarify same-subject evaluation in abstract and introduction.** Add a sentence explicitly stating that the current evaluation uses intra-subject, slice-matched pairs and that cross-subject generalization is left for future work. This would align the claims with the evidence.

## Score and Decision

This paper makes a genuine contribution by defining a new task, releasing a curated dataset, and demonstrating that weak-reference-guided segmentation across MRI modalities is feasible with a relatively simple architecture and no generative image translation. The reported performance gains on OOD modalities are large and consistent. The primary weaknesses are (a) the evaluation is restricted to same-subject, slice-aligned pairs, which is a weaker setting than full clinical deployment, and (b) the comparison set omits the most relevant class of existing approaches (unsupervised domain adaptation pipelines). These are addressable in a revision and do not invalidate the core contribution. I recommend acceptance with the expectation that the authors will address the cross-subject evaluation and UDA comparison in a revision.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>