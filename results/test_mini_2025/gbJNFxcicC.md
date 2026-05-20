Now I have sufficient calibration data. Let me write the consolidated review.

**Round 1 bracket (from calibration):** Between ~2.5 and ~5.5. The paper is clearly weaker than the Virus Capsid Detection anchor (5.5, accepted poster) and MaskSAM (4.5, withdrawn), but sits above the genuinely thin papers at 2.5-3.0.

**Round 2 narrowing:** Against the Fertilizer Dataset (3.75 avg, rejected) — both are dataset+baseline papers — the current paper is comparable but has larger evaluation gaps; against the Mental Health Detection paper (4.0 avg, withdrawn/rejected) — similar structure — the current paper is slightly weaker. This places the paper at approximately 3.5.

---

## Summary

This paper applies Mask R-CNN to detect and segment malaria parasites from microscopic blood-smear images across four *Plasmodium* species (*P. falciparum*, *P. malariae*, *P. ovale*, *P. vivax*), using a dataset of 971 images collected from Rwandan healthcare facilities. The claimed contributions are: (1) a multi-species dataset with pixel-level polygon annotations, and (2) demonstration that Mask R-CNN provides accurate detection and segmentation across morphologically diverse species, with test mAP values ranging from 0.7737 (*P. falciparum*) to 0.9575 (*P. vivax*).

## Strengths

- **Multi-species dataset with pixel-level annotations from real clinical samples.** The dataset covers four *Plasmodium* species (278, 258, 260, and 175 images per species) annotated with polygon masks using VGG Image Annotator (Section 4.1). This extends prior work that often focused on a single species or used only bounding boxes, and the clinical sourcing through Rwanda Biomedical Centre's quality-control process gives the data real-world relevance.

- **Per-species detection mAP results demonstrate viability across species.** The model achieves test mAP of 0.9575 for *P. vivax*, 0.9459 for *P. malariae*, and 0.8915 for the combined multi-species experiment (Table 1), showing that Mask R-CNN can handle morphological variation across species at the detection level.

- **Real-world clinical data collection and ethical sourcing.** Images were acquired as part of RBC's quarterly quality control process from patients presenting with fever at Rwandan healthcare facilities, and ethical oversight is described (Section 4.1).

## Weaknesses

### Fatal
None.

### Major

- **The claimed advantage of pixel-level segmentation is never evaluated.** The paper repeatedly states that Mask R-CNN's main advance over prior work (Faster R-CNN, YOLOv5) is its ability to generate precise pixel-level masks rather than coarse bounding boxes. However, the only quantitative metric reported is mAP computed from bounding boxes (the paper states mAP uses IoU "comparing actual and predicted bounding boxes," Section 4.2). No mask AP, Dice coefficient, or pixel-wise IoU for the predicted masks is provided. Without any segmentation metric, the paper cannot substantiate its central claim — the reader has evidence only about detection quality, not delineation quality.

- **No direct, quantitative comparison to companion methods from the same project.** The literature review describes three companion studies — Faster R-CNN (Bogale et al., 2024), YOLOv5 (Karasira et al., 2024), and U-Net (Akpo et al., 2024) — and the discussion (Section 5.2) claims Mask R-CNN "outperforms" them. Yet none of those methods' results are compared in a table or against the same evaluation protocol. Without a controlled comparison (retraining on the same dataset split, using the same evaluation metric), the reader cannot tell whether the improvement stems from the architecture, the larger/augmented dataset, different hyperparameters, or simply different test splits.

- **Test mAP consistently exceeds validation mAP without any explanation.** In Table 1, test mAP is higher than validation mAP for every experiment (PF: 0.7737 vs. 0.7174; PM: 0.9459 vs. 0.8547; PO: 0.8620 vs. 0.8357; PV: 0.9575 vs. 0.9462; Combined: 0.8915 vs. 0.8759). This pattern is unusual — test and validation sets drawn from the same distribution typically yield similar metrics. The authors do not comment on this, nor do they report variance. Given the small test splits (~10% of 971 images, ~97 total test images across all species), this raises concern about an unrepresentative test split, data leakage, or a mismatch in set construction. The per-species test sets for *P. vivax* (175 images × 10% ≈ 17–18 images) are particularly small.

### Minor

- **Small test sets with no uncertainty quantification.** With approximately 18–28 test images per species, mAP has high variance, yet no error bars, confidence intervals, or bootstrapped estimates are reported. The reported values (e.g., 0.9575 for *P. vivax*) may not be statistically distinguishable from substantially lower values.

- **Ambiguous class definitions and evaluation scope.** The paper states models were trained with classes: background, parasites, and white blood cells (Section 4.2). It is unclear whether reported mAP is for the parasite class only or averaged over all classes. For the combined experiment, it is unclear whether species are distinguished as separate classes or treated as a single "parasite" class. No per-class AP breakdown is provided.

- **Unusual learning rate schedule not discussed.** A StepLR scheduler with step_size=5 and gamma=0.1 (Section 4.2) reduces the learning rate by 10× every 5 epochs, meaning after ~10–15 epochs the learning rate becomes vanishingly small. The authors do not discuss why this extreme schedule was chosen or how it affects convergence. The decision to use no data augmentation because it "reduced the quality of the results" (Section 4.2) is stated without ablation evidence and, combined with the aggressive LR decay, suggests the training protocol may not be well-optimized.

### Trivial
None.

## Nice-to-Haves

- Add segmentation metrics (mask AP, Dice, pixel IoU) — this is actually a major need, listed here only because addressing it would fix the paper's central evidential gap.
- Retrain companion methods (Faster R-CNN, YOLOv5, U-Net) on the same dataset and report comparative results.
- Clarify the mAP computation details: which IoU threshold(s)? Which classes are included?
- Release the dataset (or provide a clear access pathway) — this would significantly increase the paper's impact.
- Report bootstrapped confidence intervals for all mAP values.
- Analyze failure cases and false positives qualitatively.

## Removed Points

- **"The gt_0.2, gt_0.1 labels in Figure 3 are not explained"** — Removed as a minor presentation issue that does not affect the paper's substantive evaluation. These appear to be ground-truth annotation labels in the figure.
- **"No reproducibility checklist"** — Removed per instructions (parser-stripped sections).
- **"No ablation study on backbone"** — Removed as a nice-to-have that goes beyond the paper's stated scope; the paper uses standard ResNet-50/FPN and makes no claims about architecture search.
- **"The paper does not critically examine why Mask R-CNN might be expected to outperform"** — Removed as a subjective expectation about literature-review style rather than a concrete methodological weakness.
- **Strength: "Pixel-level segmentation surpasses coarse bounding box approaches"** — Removed because it conflicts with the verified weakness that segmentation quality is never evaluated. This is a claim, not evidence.
- **Strength: "Transfer learning with a pretrained ResNet-50/FPN backbone enables training on a moderate-sized dataset"** — Removed as generic; using a standard pretrained backbone is common practice and not a distinguishing contribution.
- **Strength: "Reproducible training configuration"** — Removed because the configuration itself is problematic (extreme LR schedule, no augmentation), making reproducibility of suboptimal settings less valuable.

## Novel Insights

None beyond the paper's own contributions. The core novel element is the multi-species dataset; the method itself is a standard application of Mask R-CNN, and the evaluation gaps prevent any deeper insight from emerging.

## Suggestions

1. **Add mask evaluation.** Compute mask AP (the standard Mask R-CNN metric from He et al. 2017), Dice coefficient, or pixel-level IoU for the predicted segmentation masks. This is essential — without it, the paper's central claim about segmentation improvement is unsupported.
2. **Run a controlled comparison.** Retrain Faster R-CNN, YOLOv5, and U-Net on the *same* dataset split used in this paper and report their detection and segmentation metrics alongside Mask R-CNN in a single table.
3. **Investigate and explain the test > validation mAP pattern.** If it is an error (e.g., swapped labels), correct it. If not, explain why the test set is systematically easier (e.g., distribution shift documented in the data).
4. **Report confidence intervals** for all mAP values using bootstrapping, given the small test set sizes.
5. **Clarify the experimental setup:** specify the IoU threshold(s) used for mAP, state which classes contribute to the reported mAP, and describe whether the combined experiment distinguishes species.
6. **Revisit the learning rate schedule and augmentation choices.** Provide ablations or justification for the extreme StepLR schedule and the decision to forgo augmentation.

## Score and Decision

**Anchor references:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| V9UsZBbTvZ.md (Masked Mamba) | 3.00 | R1 | Histopathology SSL paper, rejected — comparable quality, current paper has better dataset |
| UKZqSYB2ya.md (CT Anomaly Detection) | 2.50 | R1 | Lung nodule segmentation, rejected — weaker methodology |
| BefqqrgdZ1.md (UltraLightUNet) | 2.75 | R1 | Medical image segmentation, withdrawn/rejected — similar evaluation issues |
| TUUjIWntkU.md (Explainable Medical Image Clustering) | 2.50 | R1 | Cell clustering, rejected — less relevant domain |
| 0yVP49SDg0.md (Mamba-HMIL) | 3.25 | R1 | WSI classification, withdrawn/rejected — stronger technically |
| 11oqo92x2Z.md (Solar Farm Detection) | 2.50 | R1 | Satellite imagery, rejected — similar gap between claims and evidence |
| BUDLe7NIjQ.md (MaskSAM) | 4.50 | R1 | Medical image segmentation, withdrawn — stronger technical contribution |
| RJDjSXNuAZ.md (Virus Capsid Detection) | 5.50 | R1 | WSOD for EM, accepted poster — substantially stronger evaluation |
| OuUKXhV2Uz.md (UD-Mamba) | 4.33 | R1 | Medical image segmentation, withdrawn — more technical novelty |
| xUe1YqEgd6.md (Motion Segmentation) | 5.00 | R1 | Video segmentation, rejected — different domain |
| NhLBhx5BVY.md (Supervoxel Topological Loss) | 5.33 | R1 | Neuron segmentation, rejected — stronger technical contribution |
| 6nnWnLK8If.md (Fertilizer Dataset) | 3.75 | R1 | Dataset+baselines, rejected — most similar in structure; current paper has larger evaluation gaps |
| rSNkMy4OkJ.md (Mental Health Detection) | 4.00 | R2 | Dataset+baselines paper, withdrawn — similar structure, current paper slightly weaker |
| ARIQfWf4ll.md (GMAI-VL) | 4.00 | R2 | Medical VLM, withdrawn/rejected — much larger scope |
| Ci6OBuPuYW.md (Unsupervised Object Detection) | 3.00 | R2 | Contrastive learning for detection, withdrawn/rejected — thin evaluation |
| ywD00GsxgD.md (Synthetic Data as Validation) | 2.60 | R2 | Synthetic data for CT, rejected — very thin contribution |
| gAnRV4UaUv.md (ISCUTE Cable Segmentation) | 5.00 | R2 | Cable instance segmentation, rejected — stronger method evaluation |
| jfTrsqRrpb.md (Open-world Instance Segmentation) | 4.75 | R2 | Open-world segmentation, rejected — stronger technically |

**Reasoning:** The paper's dataset is a genuine resource and the detection mAP results are reasonable, but the evaluation has critical gaps: the paper's central claim (that Mask R-CNN's segmentation capability improves upon prior work) is never directly measured, no controlled comparison with companion methods is provided, and the anomalous test > validation mAP pattern is unexplained. The paper sits between the Fertilizer Dataset anchor (3.75, rejected) — which shares a similar dataset+baseline structure but has fewer evaluation gaps — and the weaker papers at ~3.0. The major gaps (no segmentation metric, no comparison) prevent this from reaching the 4+ range occupied by papers with stronger evidence for their claims.

MY FINAL SCORE: <score>3.5</score>
MY FINAL DECISION: <decision>Reject</decision>