- Decision: Reject
- Avg Score: 3.75
- Scores: 6, 3, 3, 3
Now I have all the evidence needed. Let me synthesize the final review.

## Summary

The paper proposes a lightweight, training-free adversarial attack detection scheme for autonomous driving perception systems. The key idea is to detect attacks by measuring inconsistency between outputs of two vision models (object detection and instance segmentation) via a harmonic-mean consistency score. Evaluated on BDD100k with PGD attacks across 30 model pairs (6 OD × 5 SEG), the best pairs achieve 99.9% ROC-AUC. The paper also provides a systematic analysis of which model architectures yield the best detection performance.

## Strengths

1. **Novel detection principle with clear empirical validation.** The cross-task inconsistency idea is well-motivated and the paper provides direct visual evidence (Figure 2, kernel density estimates on 1,000 images) that clean and perturbed images produce diverging consistency-score distributions. The divergence is striking and supports the core claim.

2. **Training-free, reactive architecture.** The detector computes consistency scores from off-the-shelf model outputs without requiring adversarial training, data generation, or model modification. Section 4.2.3 reports 350 MB combined model size, which is practical for deployment scenarios that already run both tasks.

3. **Systematic 30-model-pair analysis with actionable selection guidance.** The paper evaluates all 6 OD × 5 SEG pairs and shows that pairs sharing similar backbones (ResNet) and baseline architectures (RCNN) achieve the highest AUC (99.9%), while cross-architecture pairs are weaker. Figure 5's heatmap provides a clear, deployable recommendation. This goes beyond a single fixed design.

4. **Thorough transferability analysis.** Table 1 systematically documents mAP degradation across all 11 models and shows that even when attacks transfer between architectures (e.g., FRCNN R50 → MRCNN R50), the fine-grained effects on detection count and bounding-box size differ across models (Figure 4), which is the mechanism the detector exploits.

5. **Perturbation-strength sweep.** The paper evaluates ε ∈ {1/255, 2/255, 4/255, 8/255, 16/255} (Table 2, Figure 6) and confirms that stronger perturbations yield higher detection AUC, which is the expected and desired behavior.

## Weaknesses

### Fatal

None. The core idea is valid, the method is sound, and the results within the tested scope are strong. No issues that invalidate the paper's central claims.

### Major

1. **Narrow attack evaluation — only PGD, only single-task attacks, one perturbation bound.** All adversarial datasets are generated with PGD-40 (ε = 16/255) targeting a single model. No experiments against FGSM, C&W, patch attacks, physical attacks, or any attack type besides PGD. Crucially, no evaluation against a coordinated attack that simultaneously fools both OD and SEG models (e.g., optimizing a combined loss). The paper acknowledges this in Section 5 ("Our attacker model targets only one perception task. A stronger attacker could target both tasks") and speculates that cross-task attacks "do not create cross-task consistent adversarial output" — but this claim is unsupported by any experiment. Since the detector's mechanism depends on uncoordinated discrepancies between two models, a coordinated attack is the most relevant threat model for the claimed autonomous-driving use case. Without testing it, the paper's empirical scope is substantially narrower than its title and abstract imply. This is the single most significant weakness.

2. **Single dataset (BDD100k only).** All experiments use one driving dataset. Evaluation on a second dataset (e.g., Cityscapes, KITTI) would meaningfully strengthen claims of generality. As it stands, the results may reflect dataset-specific properties.

### Minor

3. **No per-image inference-time measurement.** The paper claims in Section 4.2.3 that the detector "achieves faster inference speeds on the same hardware due to its less complex architecture" but provides zero timing numbers (FPS, ms/image, or relative speedup). This is the paper's primary efficiency claim and it is entirely unquantified. Given that the detector runs two models sequentially, concrete timing data is essential for the efficiency narrative.

4. **Limited baseline comparison.** The comparison in Section 4.2.3 is against RobustDet, an adversarial training method (not a detection method). The paper is transparent about this, observing that "our detector functions as a binary classifier [while] RobustDet... enhances the model's robustness." The comparison is informative but incomplete: no detection-specific baselines (e.g., feature squeezing, Mahalanobis-based detection, energy-based detection adapted to object detection) are included. Adding at least one such baseline would calibrate how much value the multi-task signal adds beyond single-model detection approaches.

5. **Operating point and false-positive rate not specified.** The paper discusses the threshold trade-off qualitatively (Section 3.1: "setting a high cut-off threshold... would trigger false positives") and reports AUC, which is threshold-independent. But the 99.9% detection rate in Table 4 is a point estimate; the corresponding threshold value and false-positive rate on clean data are not reported. For a deployed detector, these operating characteristics matter.

### Trivial

6. **No confidence intervals or variance estimates for AUC.** AUC values are reported as point estimates without error bars. For the 1,000-image sample, indicating variance across random splits would improve confidence.

## Nice-to-Haves

- **Test against a coordinated multi-task attack.** Even a simple baseline (PGD with a combined OD+SEG loss) would either validate or refute the method's core robustness assumption and is the most important missing experiment.
- **Expand attack types to at least one additional method (e.g., FGSM with multiple ε values) and one patch attack.** This would show that the consistency signal is not specific to PGD's optimization trajectory.
- **Measure and report per-image inference time** for the two-model pipeline vs. single-model baselines.
- **Specify the matching criterion** (IoU threshold, label-matching procedure) used for consistent detection in a prose description, since Algorithm 1 was not recoverable from the extracted PDF.

## Removed Points

These points were flagged by reviewers but are removed for the stated reasons:

- **"Algorithm 1 matching details are missing"** — The paper references Algorithm 1 for the consistency score calculation. The parser strips appendices and supplementary material, which likely contained the algorithm. A prose description would be nice, but this is not a missing detail from the submission as authored. → REMOVED (parser artifact).

- **"RobustDet comparison is misleading"** — The paper explicitly identifies RobustDet as "an adversarial training method" and contrasts it with their own binary classifier. The comparison is transparent about what is being compared and the asymmetry is clear. The weakness is better framed as "limited baseline coverage" (included above as Minor weakness 4), not as a misleading comparison. → REFRAMED, original framing removed.

- **"350MB is not lightweight"** — 350 MB for two full vision models (OD + SEG) is reasonable for modern GPU-equipped systems and is presented in context relative to RobustDet's larger dynamic kernels. Subjective judgment replaced with the concrete request for runtime measurements. → REMOVED (subjective nitpick).

- **"Only one model pair in Figure 2"** — Figure 2 is an illustrative empirical study of the detection principle; the full evaluation in Section 4.2.2 covers 30 model pairs. → REMOVED (addressed by paper's own broader evaluation).

## Novel Insights

None beyond the paper's own contributions. The reviewers' comments surface no observation that the authors themselves do not state or acknowledge (the coordinated-attack gap is explicitly flagged in Section 5; the need for broader attack types is implicit in the narrow evaluation; inference time is claimed without evidence — all observations the authors could and should have made). The most actionable reviewer insight is that the severity of the coordinated-attack gap warrants experimental validation rather than just discussion.

## Suggestions

1. **Broaden the threat model tested.** Before claiming a general detection scheme, evaluate against (a) a coordinated multi-task attack (PGD with combined OD loss + SEG loss), (b) at least one non-PGD attack (e.g., FGSM with multiple ε), and (c) a patch-based attack. This is the single change that would most increase the paper's impact.
2. **Quantify inference time.** Report per-image runtime (ms or FPS) for the two-model pipeline on the hardware used, and ideally compare to a single-model baseline.
3. **Add one detection-specific baseline.** Compare against an existing single-model detection method adapted to object detection (e.g., energy-based detection on the output logits of one model) to isolate the value added by the cross-task signal.
4. **Report the operating point.** State the threshold and corresponding FPR for the 99.9% detection rate claim in Table 4.
5. **Evaluate on a second driving dataset** (Cityscapes or KITTI) to strengthen generality claims.
