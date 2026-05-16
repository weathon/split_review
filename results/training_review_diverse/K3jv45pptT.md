Now I have a thorough understanding of the paper and can verify the reviewer claims against the actual content. Let me produce the final review.

## Summary

This paper presents DSPart, a large-scale synthetic dataset with part annotations covering 50 rigid object categories and 40 animal categories (100K images, 24.5K 3D parts). It uses a diffusion-based synthesis pipeline (3D-DST) to generate realistic images from 3D CAD models with part annotations, addressing the domain gap that plagues traditional rendered synthetic data. The paper demonstrates that training on DSPart significantly improves unsupervised domain adaptation for part segmentation (7–12 mIoU gains on PartImageNet categories) and introduces a PRF filter for curating animal images.

## Strengths

- **Scale and category coverage far exceed existing part datasets.** Table 1 shows DSPart covers 90 categories with 100K images and 24.5K 3D parts, compared to 41 categories in 3DCOMPAT++ and ~20K images in Pascal-Part/PartImageNet. The inclusion of 40 animal categories is a particularly novel contribution — prior synthetic animal datasets (CC-SSL) cover only 2 species.

- **Diffusion-generated realism yields substantial UDA gains.** In the unsupervised domain adaptation setting (Table 2), training with DSPart-Rigid improves DAFormer by +7.08 mIoU (car), +11.72 (airplane), and +11.88 (bicycle) over UDAPart. The car category reaches 72.67 mIoU — nearly matching the 74.08 mIoU of models trained on real images. This is a concrete, measurable demonstration that the dataset narrows the synthetic-to-real domain gap.

- **PRF filter offers a principled approach to curating articulated animal data.** The paper identifies that the existing KCF filter (designed for rigid objects) fails for animals due to articulation, and proposes a filter using 3D animal pose estimation metrics (PA-MPJPE, S-MPJPE, PCK) with an ensemble of two PARE models. The resulting DSPart-Animal outperforms CC-SSL in both Syn-only and UDA settings (Tables 3, 4).

- **Clean annotation methodology for both rigid and non-rigid categories.** Rigid objects use super-category-based part templates with two inspection rounds. For animals, the shared SMAL vertex IDs mean a single 3D annotation propagates across all 3,065 poses — a well-exploited design choice.

## Weaknesses

### Fatal
None.

### Major
- **The evaluation of the PRF filter is incompletely described in the extracted text.** The paper claims "Section 4.3" demonstrates the filter's effectiveness, but this section is absent from the extracted manuscript (parser artifact). From what is visible, no precision/recall or agreement statistics against human judgments are reported for the PRF filter's output. Without quantifying how well PRF replicates human filtering, the claim that PRF "guarantees the scalability of DSPart-Animal" is not adequately supported. The paper should report agreement rates on a held-out subset and analyze which types of images pass/fail.

- **The ablation isolating the diffusion contribution (Table 6, Section 4.4) is described too briefly.** The paper states that "Table 6 exhibits the ablation studies on diffusion-generated object textures and realistic synthesized context" but provides almost no textual discussion of the methodology or results. It is unclear whether this compares DSPart against a non-diffusion rendering of the *same* 3D models (which would directly isolate the diffusion effect) or against a different dataset. This is the central scientific question the paper should answer, yet the description is a single garbled sentence. The authors must expand this description with clear methodology and results.

- **No limitations section.** The paper does not discuss known limitations: the SMAL model set may not capture all quadruped morphologies, diffusion artifacts in certain viewpoints, the dataset's restriction to quadruped animals (no birds, primates, etc.), or potential biases in the 3D CAD model selection. A dataset paper should include a candid limitations paragraph.

### Minor
- **Inter-annotator agreement and annotation workforce details are not reported.** The paper mentions "3 annotators" for animal filtering and "selected annotators" for rigid-object part annotation with two inspection rounds, but does not report inter-annotator agreement metrics, annotator qualifications, or the number of annotators involved in the rigid-object annotation. For a dataset claiming high-quality annotations, these details matter for reproducibility and trust.

- **No analysis of PRF threshold sensitivity.** The paper sets thresholds on PA-MPJPE, S-MPJPE, and 2D PCK but does not analyze how the quality or quantity of the final dataset changes with different thresholds, or whether the intersection of two models biases toward samples that are easy for both (potentially underrepresenting certain poses or species).

- **The number of part categories per super-category is not reported.** Understanding the label distribution is important for assessing dataset balance and task difficulty. The paper references an appendix that likely contains this, but it is not present in the extracted text.

- **No quantification or analysis of noisy samples in DSPart-Rigid.** The paper acknowledges "a small fraction of noisy samples" (image content inconsistent with 3D annotation) and uses this to explain the minimal Syn-only gains, but does not quantify this fraction, show representative failure cases, or analyze whether noise is concentrated in particular categories or viewpoints.

### Trivial
None.

## Nice-to-Haves

- A comparison showing PRF-filtered vs. human-filtered downstream performance (e.g., training a segmentation model on each set) would strengthen the scalability claim.
- An analysis of background/texture diversity (e.g., clustering generated image latents) would further characterize the dataset's coverage.
- Comparison with SAM-based part segmentation (e.g., fine-tuning SAM on DSPart vs. in-context prompting) would be a useful addition but is well outside the paper's stated scope.

## Removed Points

These points are flagged to be removed; treat them with caution.

- "Absence of a direct baseline comparing diffusion-generated images with simple rendering of the same 3D models" — The paper *does* have this ablation in Table 6 (Section 4.4), which explicitly studies "diffusion-generated object textures and realistic synthesized context." The critic incorrectly claimed it is absent. The description is brief, so I downgraded this to a Minor weakness about insufficient description rather than a missing experiment.
- "Syn-only results are not significantly better than UDAPart" — The paper transparently acknowledges this and provides a reasoned hypothesis (noisy samples mitigated by EMA pseudo-labels in UDA). This is honest reporting, not a weakness.
- "100 hours of human filtering undermines scalability" — The paper is upfront about this one-time cost. Scalability refers to the PRF filter automatically processing the remaining 39K images without additional human effort. The critic misreads the claim.
- "Paradigm shift is hyperbolic" — Style nitpick.
- "Testing with a simpler model (e.g., lightweight CNN)" — Scope creep; the paper uses two standard architectures (SegFormer, DAFormer) which is adequate for a dataset paper.
- "Baseline comparison with SAM-based part segmentation" — Scope creep.
- "Analysis of diversity of backgrounds/textures" — Nice-to-have, moved there.
- "Ethical considerations about generated images" — Nice-to-have; not standard for dataset papers of this type.

## Novel Insights

The reviews surface an interesting tension: the paper's strongest evidence for diffusion-generated realism comes from the UDA setting (7–12 mIoU gains), yet the Syn-only setting shows minimal improvement. The paper's hypothesis — that EMA pseudo-labels in UDA training are robust to the small fraction of noisy diffusion samples — is plausible but untested. This suggests that the value of diffusion-based synthetic data may lie specifically in cross-domain feature learning (where diverse textures and contexts help the model ignore domain-specific cues) rather than in-domain feature learning. This distinction, if systematically validated, would be a meaningful finding for the broader synthetic data community: it implies that dataset realism matters most for transfer, not for in-distribution training, which has implications for how synthetic datasets are evaluated.

## Suggestions

1. **Expand Section 4.4 (ablation) significantly.** Clearly describe whether Table 6 compares DSPart against a non-diffusion rendering of the *same* 3D models with flat textures and plain backgrounds. Report the exact numbers and conditions.
2. **Report PRF evaluation metrics.** Add precision, recall, and F1 against human judgments on a held-out set. Show that PRF-filtered and human-filtered subsets yield similar downstream performance.
3. **Add threshold sensitivity analysis.** Show how varying PA-MPJPE, S-MPJPE, and PCK thresholds changes the quantity and quality of the filtered set.
4. **Add a limitations section.** Discuss coverage gaps (quadruped-only, SMAL morphologies), diffusion artifact types, and potential biases in CAD model selection.
5. **Report inter-annotator agreement** for both the rigid-object part annotations and the animal image filtering.
6. **Quantify the noisy sample fraction** in DSPart-Rigid and show representative success/failure cases.

## Score and Decision

The DSPart dataset addresses a genuine need — realistic synthetic data with part annotations — at a scale that substantially exceeds prior work. The UDA results (7–12 mIoU improvements) are compelling evidence that the diffusion-based approach narrows the domain gap. The PRF filter is a principled solution to an articulation-specific problem that prior work (KCF) could not solve. The paper's weaknesses are primarily about incomplete documentation and insufficiently detailed ablations — none invalidate the core contribution, and all are addressable in a revision. I recommend acceptance.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>