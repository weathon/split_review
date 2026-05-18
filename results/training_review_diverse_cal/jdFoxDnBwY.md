Now I have a thorough understanding of the paper and can cross-check all reviewer claims. Let me write the final consolidated review.

---

## Summary

This paper proposes Part321, a method that recognizes 3D object parts from a single 2D image using only one annotated 3D mesh per object category. The key ideas are: (1) learning mesh-to-mesh correspondence to build a category-level shared feature bank, (2) learning mesh-to-image correspondence to align 3D vertex features with 2D image features via contrastive learning on synthetic data, and (3) a per-image render-and-compare optimization that infers each part's 3D configuration (position, rotation, scale, shape). Experiments on VehiclePart3D, PartImageNet, UDA Part, and 3D DST show competitive 2D segmentation and demonstrate a novel 3D part detection capability.

## Strengths

- **Novel pipeline for one-shot 3D part recognition from a single image.** The paper proposes an ambitious and technically coherent method that bridges 3D mesh representations with 2D image observations using two types of correspondence (mesh-to-mesh and mesh-to-image). To my knowledge, this is a genuinely new capability that prior work on part segmentation does not address. Table 4 quantitatively demonstrates 3D pose estimation (62.5% average accuracy), Chamfer Distance, and 3D BBox IoU on the synthetic 3D DST dataset, and Figures 4 and 6 show qualitative 3D reconstructions on real images.

- **Quantitatively strong 2D segmentation performance across multiple real-world datasets.** On VehiclePart3D (Table 1), Part321 achieves 42.3 mIoU compared to 27.9 for the best baseline (DeepLabv3+ w/ Pseudo). On PartImageNet (Table 2) and UDA Part (Table 3), it consistently outperforms baselines, often by large margins (e.g., 14+ points on fine-grained categories). These results demonstrate that the 3D reasoning pipeline produces accurate 2D projections.

- **Ablation study validates the necessity of key components.** Table 5 systematically removes part scaling, geometry consistency loss, and part deformation. Each removal causes measurable degradation in both 2D mIoU and 3D detection metrics (e.g., 3D mIoU on 3D DST drops from 80.5 to 63.4 without part scaling, and to 68.3 without geometry constraints). This supports the claim that the proposed components contribute meaningfully.

- **Introduction of VehiclePart3D as a new benchmark.** The paper contributes a dataset of 279 real images with part segmentations, 47 CAD models across 5 categories, and synthetic training data — a useful resource for future work on one-shot part recognition.

- **Principled use of two-stage correspondence.** The mesh-to-mesh correspondence (via self-supervised geometry descriptors) enables feature sharing across diverse object instances, while the mesh-to-image correspondence (via contrastive learning on synthetic renders) provides a learnable bridge between 3D vertices and 2D pixels. This two-stage design is well-motivated by the challenge of bridging a single 3D annotation to diverse real-world appearances.

## Weaknesses

### Fatal
None.

### Major

- **Quantitative 3D evaluation is limited to synthetic data, leaving the central claim unsubstantiated on real images.** The paper's headline contribution is recognizing *3D* parts from a single image. However, Table 4 — the only quantitative 3D evaluation — is conducted exclusively on 3D DST, a synthetic dataset whose images come from the same DST pipeline used for training. On real datasets (VehiclePart3D, PartImageNet, UDA Part), 3D accuracy is assessed only qualitatively (Figures 4, 6). The domain gap between synthetic training and real testing could significantly affect 3D localization, deformation, and pose estimation in ways that 2D projection metrics (mIoU) cannot fully capture. Without quantitative 3D evaluation on real images, the paper's core claim remains incompletely validated in the setting where it matters most. This is the most significant weakness.

- **The 2D segmentation comparison is framed as a head-to-head win despite acknowledged unfairness.** The abstract, contributions list, and conclusion state that Part321 "outperforms baselines significantly" and achieves "State-of-the-Art performance on one-shot 2D part segmentation" without caveat. The paper does include a brief acknowledgment in Section 4 ("Note that this is an unfair comparison since our framework performs the extra task, which is more challenging"), but the framing throughout the paper presents these results as a direct improvement over 2D methods. In reality, Part321 uses additional resources unavailable to the baselines: 3D geometric structure during inference, a pre-built category-level feature bank from mesh-to-mesh correspondence, and synthetic training data paired with 3D ground truth. The comparison is informative as a sanity check (the 3D reasoning produces good 2D projections), but claiming superiority as a *2D segmentation method* conflates fundamentally different tasks and data requirements.

### Minor

- **Inference uses per-image optimization with no analysis of efficiency, convergence, or failure modes.** Inference involves gradient-based optimization over whole-object pose and per-part translation, rotation, scale, and shape latent for 300 steps (Section 3.4). The paper does not report per-image wall-clock time, discuss initialization sensitivity, analyze convergence behavior, or characterize failure cases (e.g., severe occlusion, extreme viewpoints, symmetric parts, out-of-distribution appearance). This makes it difficult to assess whether the method is a practical solution or a proof-of-concept that works only on favorable examples. While not a fatal omission (optimization-based inference is a legitimate design choice), the missing analysis limits the paper's contribution to a conceptual demonstration.

- **The mesh-to-mesh correspondence — a cornerstone of the method — is not directly ablated or quantitatively evaluated.** The correspondence is used to build the category-level feature bank and train the deformation network. However, Table 5 does not include a variant that removes or degrades the correspondence (the closest is "w/o Part Deformation," which still uses the shared feature bank built from correspondences). The paper provides no evaluation of correspondence accuracy (e.g., how often the nearest neighbor in descriptor space yields the correct semantic part on held-out meshes). Without this, it is unclear whether the correspondence is reliable enough to justify the complexity it adds over simpler alternatives (e.g., direct template projection).

- **Framing of "one-shot 2D part segmentation" is unconventional and could mislead readers.** The one annotation is a 3D mesh, not a 2D image. Methods like PerSAM or other prompt-based segmenters that operate in a more standard one-shot 2D setting are not compared. The paper is clear about its setup, but the "SOTA on one-shot 2D part segmentation" claim risks being interpreted in the context of prior one-shot segmentation literature where the annotation modality is different.

### Trivial

- **The geometry consistency loss (Eq. 6) leaves hyperparameter values unreported.** The paper describes how paired vertices are selected (those with inter-vertex distance below threshold τ) and the loss formulation is clear, but the specific values of τ and the loss weight w_consist are not provided. These are small empirical details that should be reported or released with the code.

- **The caption of Table 5 has a typo: "Tabel" instead of "Table."** (Line 187)

## Nice-to-Haves

- A small-scale quantitative 3D evaluation on real images (e.g., manually aligning CAD models from VehiclePart3D with real images via PnP and reporting Chamfer distance or 3D part IoU on a subset of 20–30 images) would substantiate the core claim far more than the current entirely synthetic 3D evaluation.
- Reporting average inference time per image and discussing failure cases would improve the paper's empirical contribution.
- An ablation that replaces the learned mesh-to-mesh correspondence with a naive baseline (e.g., projecting the single annotated mesh without deformation) would help validate whether the correspondence learning is essential.

## Removed Points

- **"The paper does not describe how camera poses are sampled for DST image generation."** — Removed because the paper references supplementary material ("3 for more details") which the PDF parser strips. This detail likely exists in the appendix of the original submission.
- **"Methods like PerSAM or other point/box-prompted segmenters are not compared."** — Removed because PerSAM is a SAM-based promptable segmenter operating in a fundamentally different paradigm (foundation model with test-time prompting) that does not share the same training or annotation setup. Comparing against it would not isolate the contribution of the proposed pipeline.
- **"The paper does not state how the paired vertices are selected [for the geometry consistency loss]."** — This is factually incorrect. Section 3.4 clearly states: "We select the paired vertices... which have distances ρ_ij = ||V̄_i - V_j||_2 smaller than a threshold τ." The remaining concern about missing τ and w_consist values is kept above under Trivial.
- **"It is unclear whether the paired vertex selection is fixed or dynamic."** — This level of implementation detail is a trivial nitpick about optimization mechanics; the loss formulation is self-contained and reproducible from the information given.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a fundamental re-interpretation of the work.

## Suggestions

1. **Add quantitative 3D evaluation on real images.** This is the single most impactful improvement. Even a small-scale experiment (VehiclePart3D has 47 CAD models and 279 images — use PnP alignment to measure 3D pose accuracy and Chamfer distance on a held-out subset) would transform the credibility of the central claim.

2. **Reframe the 2D comparison honestly.** Separate the narrative into two tracks: (a) 2D segmentation as a *proxy* showing that the 3D reconstruction is accurate enough to project well, not as a direct method comparison; (b) 3D part detection as the primary contribution, where no 2D-only baseline is possible. Remove unqualified "SOTA on one-shot 2D part segmentation" language from the abstract and contributions.

3. **Report inference time and discuss failure modes.** Add a brief analysis of per-image optimization time, number of steps needed for convergence, and at least a qualitative discussion of conditions under which the optimization fails (occlusion, symmetry, unusual viewpoints).

4. **Validate the mesh-to-mesh correspondence directly.** Either (a) add an ablation that compares the full method against a variant using a single fixed template with no correspondence-based feature sharing, or (b) report correspondence accuracy on held-out meshes (e.g., semantic part correspondence accuracy).

5. **Release code and hyperparameter values for reproducibility.** Report τ, w_consist, learning rates, and optimization settings (or release code).

## Score and Decision

This paper presents a novel and technically ambitious approach to a genuinely new problem (one-shot 3D part recognition from a 2D image). The two-stage correspondence learning and render-and-compare inference are well-motivated. However, the evidence for the central 3D claim is incomplete — quantitative 3D evaluation exists only on synthetic data — and the 2D comparison framing overstates the method's standing by not consistently caveating the asymmetric setup. The missing inference analysis and un-ablated correspondence component are secondary concerns.

The paper's core idea and pipeline are promising, and the weaknesses are addressable with additional experiments and revised framing. I recommend **major revision** rather than rejection, contingent on adding quantitative 3D evaluation on real images and honestly reframing the comparisons.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>