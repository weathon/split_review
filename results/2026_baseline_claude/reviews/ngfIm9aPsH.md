## Summary

OF-Diff (Object Fidelity Diffusion) proposes a controllable layout-to-image generation framework for remote sensing (RS) images designed to augment training data for object detection. It introduces three components: (1) an Enhanced Shape Generation Module (ESGM) that leverages RemoteCLIP and RemoteSAM to extract object-class shape priors from labeled bounding boxes; (2) an online-distillation dual-decoder architecture where a "mix-feature" decoder (conditioned on image features + shape features) serves as a teacher to guide a "shape-feature" decoder at training time, enabling inference without real-image references; and (3) DDPO fine-tuning with a custom KNN diversity + KL divergence reward to improve distribution alignment with real RS images. The method is evaluated on DIOR-R, DOTA-v1.0, and HRSC2016 across 13 metrics spanning generation fidelity, layout consistency, shape fidelity, and downstream detection utility.

---

## Strengths

- **Practically motivated and technically sound core idea.** The insight that RS objects have quasi-invariant shapes (airplanes, ships, tanks) makes shape-prior conditioning particularly well-suited to this domain. The online-distillation mechanism—training a dual decoder where the image-conditioned teacher transfers knowledge to the layout-only student—is a genuine and clever architectural contribution that removes real-image dependency at inference without sacrificing fidelity.

- **Comprehensive, multi-faceted evaluation.** The paper contributes a 13-metric evaluation framework covering generation quality (FID, KID, CMMD), semantic consistency (CAS, YOLOScore), shape fidelity (IoU, Dice, CD, HD, SSIM on Canny edge maps), and downstream detection mAP. The shape-fidelity metric set applied to instance-level edge comparisons is especially novel and directly relevant to the problem.

- **Consistent improvements across three datasets and multiple metrics.** On DIOR, OF-Diff achieves FID=24.92 vs. AeroGen's 27.78 and CC-Diff's 49.62. On DOTA, it achieves FID=20.84 vs. the next best 21.73. Shape fidelity (Table 2) shows SSIM of 0.2691/0.2938 on DIOR/DOTA vs. prior best of 0.2142/0.2261. Downstream mAP gains of +8.3% (airplane), +7.7% (ship), +4.0% (vehicle) on DIOR are meaningful for the target application.

- **Ablation study validates each component.** Table 4 clearly demonstrates the independent contributions of ESGM (+10% YOLOScore over baseline), online distillation Lc (−6 FID), and DDPO (+0.7% mAP). The sensitivity analysis of λ (Figure 5c/d) further justifies the hyperparameter choice.

---

## Weaknesses

### Fatal
None.

### Major

- **Ambiguous duplicate rows in the ablation table (Table 4).** Two rows both show "✓ ✓ ✓" (ESGM + Lc + DDPO all enabled) with dramatically different results: FID=37.98 vs. FID=24.92, YOLOScore=47.74 vs. 58.99. The distinction—one uses caption conditioning (which degrades fidelity) and one does not—is explained in Section 4.5 but is absent from the table itself. A reader analyzing the ablation in isolation would reasonably conclude that the full model sometimes *underperforms* partial ablations, which would undermine the conclusions. This should be a clearly labeled row distinguishing "w/ caption" vs. "w/o caption."

- **Sparse justification for the progressive mixing schedule in Eq. (3).** The teacher weight ramps linearly from 0 (pure shape features at iteration 0) to 1 (pure image features at the last iteration), but no ablation or theoretical argument is provided for this specific schedule vs. alternatives (fixed mixing ratio, cosine schedule, constant image-feature teacher). Early in training the teacher is nearly identical to the student (both shape-only), while late in training the teacher is entirely image-driven with no shape signal—it is unclear whether this trajectory is principled or a design choice that happened to work.

### Minor

- **DDPO's incremental contribution is modest.** From Table 4, DDPO alone (row 4) improves mAP from 52.13 to 53.41 and barely moves FID (41.26 vs. 42.59). The dominant gain comes from ESGM. The portrayal of DDPO as a co-equal contribution in the abstract and contributions list is somewhat overstated given the ablation evidence.

- **The mask pool design at inference is underspecified.** Section 3.3 states that at sampling time "ESGM selects enhanced shapes from a lightweight mask pool collected during or after training." The composition of this pool (size, diversity, per-class balance) and its sensitivity to test-distribution shift are not analyzed. For the unknown-layout generalization experiment (Table 3), this matters directly.

### Trivial

- The KL divergence reward in Eq. (9) is stated to be computed between generated and real images in CLIP embedding space, but the precise estimator (histogram, Gaussian approximation, mini-batch) is not specified in the main text.

---

## Nice-to-Haves

- An analysis of the mask pool composition (size, diversity) and its effect on quality would strengthen the ESGM contribution, especially for unknown layouts.
- Including a brief comparison of the progressive teacher schedule (Eq. 3) against a fixed-ratio alternative would solidify the design choice.

---

## Novel Insights

The most genuinely novel insight in this paper is the observation that RS image synthesis can be decomposed into a training-time and inference-time problem with asymmetric information: real images are available at training (enabling rich appearance conditioning), but only layout labels are available at test time (required for flexible data augmentation). The dual-decoder online-distillation framework exploits this asymmetry by maintaining two prediction heads within a single training run—one with full image context (teacher) and one with only shape context (student)—allowing the teacher's appearance knowledge to flow into the student at training while leaving the student capable of autonomous inference. This is a clean and practically impactful framing that distinguishes OF-Diff from prior work that either forgoes appearance guidance entirely or requires real-image references at test time.

---

## Suggestions

- Explicitly annotate Table 4 to distinguish the caption-enabled row from the caption-free row, and briefly note this split in the table caption.
- Ablate the progressive mixing schedule (Eq. 3) against a fixed mixing ratio to validate the linear ramp design.
- Report the mask pool statistics (e.g., number of masks per class, shape variance) to clarify the inference-time shape diversity.
- Provide a clear computation recipe for the KL divergence term in Eq. (9) to ensure reproducibility.

---

## Score and Decision

The paper addresses a practically important problem with a technically sound and conceptually novel online-distillation framework. The evaluation is unusually comprehensive for a generation paper (13 metrics, 3 datasets), the improvements are consistent and meaningful for downstream detection—particularly for difficult object classes—and the core design decision (removing real-image inference dependency via distillation) is well-motivated and well-executed. The main weaknesses are a presentation flaw in the ablation table and thin justification for the mixing schedule, neither of which invalidates the contributions. The work is somewhat domain-specific for ICLR but brings real value to the remote sensing and data augmentation communities.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>