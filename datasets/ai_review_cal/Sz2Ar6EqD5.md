- Decision: Reject
- Avg Score: 4.00
- Scores: 5, 6, 3, 5, 1
Now I have all the information needed. Let me write the consolidated review.

## Summary

This paper proposes a novel referring segmentation task for multi-modality abdominal MRI, where a single weak scribble on a reference T1w modality guides simultaneous segmentation of four other modalities (T2w, DWI, In-phase, Opposed-phase). The authors introduce the CrossMR model built on SEEM with two key modifications—paired data augmentation (to simulate target-like images without a generative model) and organ-specific bipartite matching (to enforce structural correspondence). They also release a new annotated dataset of 3,277 organs across 534 scans covering five modalities. CrossMR achieves consistent DSC gains of 5–20% over baselines on out-of-distribution modalities despite using only reference-side scribbles.

## Strengths

- **Novel task formulation with a concrete benchmark dataset.** This is the first referring segmentation formulation for multi-modality medical imaging (Section 1). The paper delivers a curated dataset of 3,277 organs across 534 scans and five modalities, with expert radiologist annotations, that makes the task benchmarkable. The dataset, code, and weights will be publicly released.

- **Large and consistent OOD segmentation gains.** CrossMR outperforms all four compared methods on every OOD modality by substantial margins: +9.83% DSC on T2w, +9.72% on DWI, +19.56% on In-phase, and +5.66% on Opposed-phase over the second-best method (Table 1). These margins hold across all four organs, not just a single structure, directly supporting the claim of a generalizable cross-modality model.

- **Organ-specific bipartite matching is a principled and ablated contribution.** The modification to the matching cost matrix (Eq. 3, Section 3.3) ensures that a query assigned to one organ cannot be matched to a different organ. The ablation (Table 2) confirms its value: removing it drops average In-phase DSC from 44.9% to 39.4%. This is cleanly motivated and empirically supported.

- **Paired data augmentation removes the need for cross-modality image translation.** By applying two independent augmentation streams to the same reference image (Section 3.2), the model learns to handle diverse contrasts without training a separate CycleGAN or synthesis network. The ablation confirms its contribution (Table 2), and this design choice simplifies the pipeline compared to standard domain adaptation approaches.

- **Reduced annotation burden is directly quantified.** CrossMR uses only a single scribble on the reference modality yet outperforms MedSAM-Scribble and nnUNet-Scribble that had access to scribbles on each target image (Section 5, Table 1), and outperforms PerSAM-F which uses a full mask as support with test-time fine-tuning.

## Weaknesses

### Fatal
None. The core contributions (novel task formulation, dataset, method) are all present and supported by evidence. The issues below are documentation and presentation gaps, not invalidations of the paper's claims.

### Major

- **Spatial alignment between reference and target slices is not fully documented.** The paper states that paired images "are chosen from the same subject" and slices are matched "in a one-to-one fashion while maintaining the relative order" (Section 4.3). However, it never explicitly states whether the volumes are co-registered (same FOV, resolution, orientation, slice positions). In clinical abdominal MRI, different modalities are often acquired with different geometries. If slices are not spatially aligned, the scribble on the reference slice does not provide a spatial prior for the target slice, and the mechanism changes fundamentally. The paper must either (a) confirm that the Duke Liver dataset provides inherently co-registered volumes and describe the slice-matching procedure precisely, or (b) if registration was applied, describe the method and report residual alignment error. This does not invalidate the results but is essential for interpreting what the model actually learns from the reference scribble.

### Minor

- **The visual sampler is underspecified for reproducibility.** The paper says the visual sampler "uses an interpolation function to sample the features from the scribbled region" (Section 3.1). It is not clear whether this is average pooling over scribble pixels, bilinear interpolation at scribble coordinates, or a learned sampling mechanism. This detail matters for implementing the method from scratch and should be specified.

- **The paired augmentation claim is slightly overstated.** The paper says the first augmentation set "translates the T1w reference image to an image that resembles one of the five modalities" (Section 3.2). The augmentations used are standard MONAI transforms (random Gaussian noise, Gibbs noise, contrast adjustment, intensity scaling — Section 4.2). While these diversify the training distribution (and the ablation shows this helps), they are unlikely to produce images that meaningfully mimic the tissue contrast characteristics of T2w, DWI, or opposed-phase MRI. Reframing this as "distributional augmentation for robustness" rather than "modality simulation" would be more accurate. No augmented images are shown in the paper to support the "resembles" claim.

- **The baseline input protocol could be stated more explicitly.** The paper's text implies (Section 5, line 206: "Unlike models such as MedSAM-Scribble and nnUNet-Scribble, which require direct scribble input on each target image") that these baselines received scribbles on the target image in their native mode, and that CrossMR still outperforms them using only reference scribbles. This interpretation makes the comparison favorable to CrossMR. However, the exact input given to each baseline during evaluation is never stated in a single unambiguous sentence in the experimental section. Adding one explicit sentence would preempt any confusion.

- **NSD results phrasing.** The paper reports NSD improvements as "increases of 15.98, 23.28, 16.19, and 16.08 points" (Section 4.4). Since NSD ranges 0–100, confirming these are absolute percentage points (not relative percentages) would improve clarity.

### Trivial
None.

## Nice-to-Haves

- Show examples of the paired augmentation output alongside real target-modality images from the same subject. This would help readers assess how much of the transfer is due to realistic simulation vs. model robustness to distribution shift.
- Report cross-subject vs. same-subject performance separately. The paper acknowledges this as future work; even a brief analysis would strengthen the contribution.
- Provide a table of augmentation ranges used for the "modality-simulating" stream.

## Removed Points

These points from the original reviews were removed or substantially weakened after verification against the paper:

1. **"nnUNet is trained on T1w only and expectedly fails on OOD modalities—its inclusion as a primary baseline is not informative."** — This is incorrect. Including a supervised nnUNet trained on T1w is standard and informative: it establishes the performance ceiling on the in-distribution modality and quantifies the OOD degradation that any cross-modality method must improve upon. This is a valid and useful baseline.
2. **"The automatic scribble generation section is overly detailed."** — Format/style nitpick about section length, not a substantive weakness.
3. **"The discussion of cross-modality domain adaptation... is a bit superficial."** — Vague opinion without a specific anchor or evidence.
4. **"Paired data augmentation lacks justification for modality simulation"** (framed as a critical issue). — Retained as a Minor point above (overstatement, not lack of justification). The ablation shows the augmentation works; the criticism is about phrasing precision, not validity.
5. **"PerSAM-F requires a full mask as support"** (as weakness). — This is actually a point in the paper's favor: CrossMR uses only a weak scribble and still outperforms PerSAM-F, which uses a full mask. Not a weakness of the paper.
6. **Criticisms about "unfair comparison" with baselines.** — The paper makes clear (line 206) that the scribble-prompt baselines were used in their native mode (scribble on target). If anything, this makes the comparison more favorable to CrossMR (less information, better results). The critic's framing of "unfairness" is not supported by the paper's text.

## Novel Insights

None beyond the paper's own contributions. The two reviews largely recapitulate the paper's claims and flag documentation gaps; no new cross-cutting observation emerges that isn't already in the paper.

## Suggestions

1. **Clarify spatial alignment explicitly.** Add a sentence confirming whether the Duke Liver volumes are co-registered (and if so, cite the original registration method), and describe the slice pairing procedure quantitatively (e.g., linear interpolation to match slice count? Resampling to common resolution?). This is the single most impactful fix.
2. **Add one sentence in Section 4.3 specifying the exact input protocol for each baseline.** E.g.: "For MedSAMScribble and nnUNet-Scribble, the scribble was drawn on the target image directly (their native protocol); for CrossMR, the scribble was drawn only on the reference T1w image."
3. **Rephrase the "resembles one of the five modalities" claim** in Section 3.2 to avoid over-promising. Something like "applies diverse intensity and contrast augmentations to improve robustness to domain shift" would be more accurate.
4. **Specify the visual sampler implementation** (average pooling? bilinear interpolation?).
5. **Show examples of augmented images** in an appendix or supplementary to support the claim.
