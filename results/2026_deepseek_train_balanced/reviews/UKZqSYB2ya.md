## Summary

This paper proposes a two-stage pipeline for lung nodule segmentation in CT scans: Stage 1 uses Deformable-DETR with Focal Loss to detect nodules on 7.5mm Maximum Intensity Projection (MIP) images under extreme class imbalance; Stage 2 fine-tunes SAM (initialized from MedSAM) to refine the detected bounding boxes into pixel-wise segmentation masks. The method reports a 92.4% Dice coefficient, 95.2% sensitivity, and 93.2% precision on a processed LUNA16 dataset with 5% nodule sparsity in the test set.

---

## Strengths

- **Controlled comparison demonstrates the two-stage design is necessary**: The paper reports that SAM deployed independently achieves only a 45% Dice coefficient (Section 5, lines 150–152), while the full pipeline reaches 92.4%. This directly shows that the detection-then-segmentation division of labor drives performance, rather than the components independently.

- **Ablation of DETR vs. Deformable-DETR justifies the architectural choice**: Standard DETR achieved 42% sensitivity after 20 epochs, while Deformable-DETR exceeded 90% sensitivity after 8 epochs (Section 3.3, line 75). This concrete empirical comparison motivates the specific choice of deformable attention for sparse small-object detection.

- **Evaluation under clinically realistic class sparsity**: The test set is explicitly constructed with a 5% nodule rate (Section 3.2, line 68) to mimic real-world clinical conditions, and the paper calls out that many existing methods use processing techniques that over-emphasize positive slices (Section 5, lines 143–148). This design choice is a methodological strength.

- **Clinically grounded MIP preprocessing**: The 7.5mm MIP slab thickness is chosen based on cited radiologist practice (Gruden et al. 2002; Zheng et al. 2019) and is motivated by the specific challenge of distinguishing compact nodule blobs from elongated vessels (Section 3.1, lines 54–58).

- **Size-categorized reporting**: Metrics are reported separately for small (≤7mm), medium (7–15mm), and large (>15mm) nodules (Table 1 context, lines 122–126), providing useful granularity beyond a single aggregate score.

---

## Weaknesses

### Fatal

None.

### Major

1. **MIP-to-slice data flow is incoherent as described (Section 3.4, line 87).** The paper states that Stage 2 performs segmentation "by splitting the MIP images back into their individual CT slices." A Maximum Intensity Projection is a non-invertible many-to-one mapping — it projects the highest-attenuation voxel along the z-axis and discards the original slice information. You cannot "split" a MIP back into individual slices. The Figure 3 caption suggests a different (and physically possible) flow: "Bounding boxes from Stage 1 are split into individual CT slices." But the main text is contradictory. This must be corrected: the reader needs to know whether (a) Stage 2 operates on the original individual slices with bounding boxes projected back from the MIP, or (b) something else entirely. This is not a typo; the current text prevents the reader from understanding the actual data flow.

2. **Evaluation protocol is critically under-specified, making the headline results uninterpretable as reported.** Several key decisions are missing:
   - **No IoU threshold for Stage 1 detection metrics.** Precision, recall, and F1 are reported without specifying what IoU defines a correct detection (e.g., IoU ≥ 0.5 is standard). Without it, the detection metrics are not interpretable.
   - **Unclear whether evaluation is per-slice or per-scan.** The paper describes a dataset of 9,676 slices and reports metrics on them, suggesting per-slice evaluation. The LUNA16 standard is FROC-based scan-level evaluation. Per-slice metrics can differ substantially from scan-level metrics, especially since multiple slices may contain the same nodule. The paper does not mention scan-level evaluation at all.
   - **Unspecified how the Stage 2 Dice coefficient is computed.** If Dice is computed only on slices where Stage 1 successfully detected a nodule (conditioned on detection), it bypasses the harder cases and inflates the number. If computed on all test slices, the denominator includes many negative slices where Dice is undefined. The paper does not clarify this, yet 92.4% Dice is the headline result.
   - **Unclear what ground truth the Dice compares against** — original 3D segmentation masks, or masks projected through the same MIP operation?

3. **The 92.4% Dice coefficient lacks sufficient supporting evidence for a claim at this level.** Lung nodule segmentation on LUNA16 typically achieves Dice scores in the 70–85% range for published methods. A result of 92.4% would represent a substantial advance, yet the paper provides:
   - No ablation study isolating the contribution of each component (MIP preprocessing, Deformable-DETR vs. standard DETR, SAM fine-tuning vs. frozen SAM, Focal Loss vs. alternatives)
   - No oracle upper bound (e.g., SAM prompted with ground-truth bounding boxes to separate detection quality from segmentation quality)
   - No error analysis or discussion of failure cases
   - No variance estimates or confidence intervals (given the test set has approximately 97 positive slices, variance could be substantial)

4. **Comparison to prior work is not verifiably on equal footing (Table 2).** The paper claims to outperform U-Net, V-Net, MRUNet-3D, DB-Net, 3D-MSViT, and SW-UNet. It is not stated whether these baselines were re-implemented on the exact same test split (same 5% sparsity test set, same 2D slice-level evaluation, same MIP preprocessing) or whether the numbers are taken from papers using different datasets, different train/test splits, different evaluation metrics (e.g., 3D Dice vs. 2D Dice), and different class distributions. Without this information the comparison is not valid.

### Minor

1. **Computational complexity claim is internally inconsistent (Section 3.3, line 77).** The paper says the encoder uses "Deformable Self-Attention (DSA) layers" but then states "The computational complexity of self-attention is O(H²W²C)" — which is standard self-attention complexity, not deformable attention (whose complexity is O(NK) for a small constant K). Additionally, with H=256, W=256, standard self-attention would operate on 65,536 tokens, which is computationally prohibitive. This inconsistency suggests a misunderstanding or a critical missing contrast to explain why deformable attention was chosen.

2. **Stage 2 training hyperparameters are omitted.** The paper specifies hyperparameters for Stage 1 (learning rate, epochs, batch size, optimizer, weight decay, gradient clipping — Section 3.5) but provides no equivalent details for Stage 2: no learning rate, no number of epochs, no batch size, no data augmentation details specific to SAM fine-tuning. SAM fine-tuning is non-trivial, and these omissions affect reproducibility and the ability to assess the adequacy of training.

3. **Construction of the 5% sparsity test set is not explained.** The paper reports a test set with 5% nodule rate (Section 3.2, line 68), but does not specify whether this was achieved by subsampling positive slices, adding negative slices, or some other procedure. Each approach changes what is being measured.

4. **Novelty claim is overstated.** The paper calls itself "the first method to combine various elements... into a unified framework specifically tailored for sparse lung nodule segmentation" (line 36). Combining Deformable-DETR and SAM is a reasonable engineering contribution, but this framing is not a strong novelty argument given existing work on transformer-based medical image segmentation.

### Trivial

None.

---

## Nice-to-Haves

- **Add an oracle experiment**: Report SAM's Dice when prompted with ground-truth bounding boxes. This establishes an upper bound and cleanly separates detection quality from segmentation quality.
- **Add an ablation without MIP preprocessing**: This would directly test the paper's own claim that MIP helps differentiate nodules from vessels.
- **Report variance**: Single-point metrics should be accompanied by confidence intervals or standard deviations over multiple runs or bootstrapping.

---

## Removed Points

These points are flagged to be removed — treat them with caution:

- **"No code or reproducibility checklist"** — Removed per hard rule: questioning code availability for reproducibility is standard reviewer practice but noted here as a minor concern; not included in the main weaknesses because the paper's other issues are more pressing.
- **"Table 2 is an image"** — Removed per hard rule: this is a parser artifact (the PDF extraction strips table structures); the original submission presumably had a proper table.
- **"No statistical significance"** — Moved to Nice-to-Haves rather than weaknesses, as this is a standard request that does not invalidate results.
- **The "Introduction" and "Related Work" section-level criticisms** (framing is generic, reads as textbook summary) — Removed as overly vague "area-of-concern" criticisms without specific anchors. The core weaknesses above are concrete and verifiable.
- **"Missing appendix, missing proofs in appendix, or absent references"** — Not present; no such criticisms raised by the reviewer.

---

## Novel Insights

None beyond the paper's own contributions. The review surfaces no genuinely novel observations that the paper itself does not claim.

---

## Suggestions

The paper's core idea — a two-stage pipeline with Deformable-DETR for detection and SAM for segmentation — is conceptually reasonable and the paper provides some useful evidence for its design decisions (DETR vs Deformable-DETR comparison, SAM-alone baseline). To make the paper suitable for a top-tier venue, the authors should:

1. **Rewrite the MIP-to-slice data flow description.** Clarify explicitly: Stage 1 detects on MIP images → bounding boxes are projected back to the original individual CT slices → Stage 2 segments each slice independently. Remove the phrase "splitting the MIP images back into their individual CT slices" entirely, as it is physically incorrect.

2. **Fully specify the evaluation protocol.** State the IoU threshold for detection, whether metrics are per-slice or per-scan, and exactly how Dice is computed (denominator, which slices it covers). Add FROC-based scan-level evaluation to align with LUNA16 community standards.

3. **Add supporting experiments for the headline result.** At minimum: (a) an oracle experiment with ground-truth boxes → SAM, (b) an ablation without MIP, (c) variance estimates, and (d) an error analysis showing where and why the model fails, especially on small nodules.

4. **Ensure comparison fairness.** Either re-implement baselines on the exact same protocol or clearly specify the differences and why comparisons still hold.

---

## Score and Decision

**MY FINAL SCORE: <score>3.5</score>**
**MY FINAL DECISION: <decision>Reject</decision>**