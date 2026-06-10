## Summary

This paper proposes LoRA3D, a self-calibration pipeline that specializes pre-trained 3D geometric foundation models (primarily DUSt3R) to target scenes using sparse RGB images alone. The pipeline has three components: robust multi-view alignment with a closed-form confidence calibration rule derived from Geman-McClure M-estimation, confidence-based pseudo-labeling, and LoRA fine-tuning on the pseudo-labels. Evaluated on 161 scenes across Replica, TUM, and Waymo datasets, the method shows consistent improvements over the pretrained model across reconstruction, pose estimation, and novel-view rendering tasks, with per-scene adaptation completing in under 5 minutes on a single GPU.

## Strengths

- **Principled confidence calibration via closed-form update from Geman-McClure robust M-estimation (Sec. 4.2, Eq. 7-8).** The paper identifies that its joint optimization objective aligns with the Geman-McClure robust M-estimator and derives a closed-form weight update rule $w_p = C_p / (1 + \|e_p\|/\mu)^2$ that avoids gradient back-propagation. The ablation (Fig. 4a,b) directly validates that this calibrated confidence is necessary — using un-calibrated confidence for pseudo-labeling consistently harms performance regardless of the cutoff threshold. This is a concrete mathematical contribution beyond a generic "use confidence" approach.

- **Large-scale, consistent evaluation across 161 diverse test scenes spanning three datasets (Sec. 5.1).** The evaluation covers all available test scenes from Replica (8) and Waymo (150), plus 3 from TUM. Improvements are substantial on Waymo pose estimation (ATE reduction from 0.80m to 0.09m on segment-10980), pairwise reconstruction (14.29cm to 8.84cm on Replica office0), and novel-view rendering (+0.97dB PSNR). The breadth goes well beyond cherry-picked results.

- **Concrete time and memory efficiency with measured specifications (Sec. 4.4).** The paper reports that fine-tuning on 10 calibration images converges in under 3.5 minutes with batch size 2, peak GPU memory under 20GB, and each LoRA adapter requiring under 18MB storage. These numbers enable the entire pipeline to complete within 5 minutes on a single standard GPU, which is verifiably more efficient than alternatives like full fine-tuning.

- **Ablation reveals the non-obvious failure mode of naive pseudo-labeling (Fig. 4a,b).** The ablation demonstrates that using the original predicted confidence for pseudo-labeling (without calibration) consistently degrades model performance regardless of confidence cutoff value. This provides critical evidence that the confidence calibration step is not just an incremental addition but a necessary component, surfacing a non-trivial insight about the pretrained model's confidence quality.

## Weaknesses

### Major

- **No uncertainty quantification in any main result (all tables, Sec. 5).** Calibration images are randomly sampled from a pool (Sec. 5: "we randomly sample 10 images from the calibration split"), yet every table reports only point estimates without variance, standard deviation, or confidence intervals. The seed-ablation (Fig. 4c) tests stability across seeds on only one Replica scene — this does not generalize to all 161 scenes. Since the main tables all use seed=0, the reader cannot assess whether observed improvements (e.g., 14.29→8.84 cm) are reliable or could arise from a favorable random draw. For a method that relies on random sampling and makes quantitative claims across 161 scenes, this is a significant methodological gap that limits scientific rigor.

### Minor

- **Pairing strategy for calibration images is underspecified (Sec. 4.1, 3.3).** The paper uses N=10 calibration images and states DUSt3R makes predictions for "all calibration image pairs" (line 161), but never specifies how pairs are formed from the 10 images. Are all C(10,2)=45 pairs used? Are pairs selected based on estimated visual overlap or a threshold? This detail directly determines: (a) the connectivity graph for global alignment, (b) the multi-view consistency signal for confidence calibration, and (c) the quantity of pseudo-labeled training data. Without it, the method cannot be precisely reproduced.

- **Claim of robustness to dynamic elements is asserted without direct evaluation (Sec. 4.3, line 294-295).** The paper states the method is "naturally robust to dynamic elements in the scene" and references Table 5, but Table 5 reports pose estimation on Waymo segments — it does not measure dynamic content or test whether dynamic points are actually filtered. The novel-view rendering evaluation explicitly selects only "mostly static" Waymo segments (line 362-363). A proper evaluation would involve scenes with known dynamic objects or at minimum measure what fraction of filtered pseudo-labels correspond to moving objects. The claim is plausible but unsupported as presented.

- **Hyperparameter sensitivity not explored.** The confidence cutoff ($w_{\text{cutoff}}=1.5$, line 292) and the regularization weight $\mu$ (Eq. 9) directly control the quantity/quality of training data, but no sensitivity analysis is shown. The paper states $w_{\text{cutoff}}=1.5$ "works effectively for most test scenes" without reporting the distribution of optimal values or sensitivity to this choice.

### Trivial

- The figure caption claims the method "generalizes to other 3D foundation models" (Fig. 2 caption) but the only evidence is a reference to the appendix (Sec. 5.3), so ICLR reviewers cannot verify this claim from the main paper alone.

## Nice-to-Haves

1. **Disentangle the contributions:** An ablation replacing the confidence-weighted optimization with standard global optimization (Eq. 6), then adding components, would isolate which part drives the improvement.
2. **Characterize the 34/150 failure cases on Waymo:** The paper attributes failures to "static vehicle" scenarios but does not analyze the remaining 33 scenes. A breakdown would deepen understanding of the method's limits.
3. **Report COLMAP with different configurations on Waymo** rather than a flat "Fail" — showing that COLMAP can succeed on some subset under different parameters would make the baseline comparison more informative.

## Removed Points

These points were raised by reviewers but removed after cross-checking against the paper:

- **"88% claim is misleading":** Removed. "Up to X%" is standard practice for best-case results. The paper contextualizes this: "our method reduces camera trajectory estimation errors by up to 88%" (line 524). The abstract's phrasing is a standard summary.
- **"COLMAP Fail insufficiently explained":** Removed. The paper provides an explanation (line 530: "due to the presence of dynamic objects and the larger baselines between forward-facing cameras"). The critic's speculation that COLMAP should not fail is not evidence against the paper's reported results.
- **"Robustness to dynamic objects" as a strength:** Removed because it conflicts with the verified weakness that this claim is not directly evaluated.
- **LoRA rank evidence limited:** Removed. The paper states the choice was validated on "multiple test scenes" (line 312) and the example plot is for illustration. This is adequate.

## Novel Insights

None beyond the paper's own contributions. The two reviewer perspectives largely converge — both recognize the closed-form weight update as a genuine technical contribution and the 161-scene evaluation as a strength, while noting the absence of uncertainty quantification and the underspecified pairing strategy.

## Suggestions

1. Add variance estimates (multiple random seeds, e.g., 5 seeds) to at least a representative subset of results (e.g., 10-20 scenes from each dataset) and report means ± std in the main tables.
2. Explicitly specify the calibration image pairing strategy: how pairs are formed from the N calibration images, whether all pairs are used, and any overlap-based filtering.
3. Either remove the claim of robustness to dynamic elements or provide direct experimental support (e.g., compare on scenes with known dynamic objects, or quantify what fraction of filtered points correspond to dynamic content).
4. Add a sensitivity analysis for the confidence cutoff $w_{\text{cutoff}}$ and regularization weight $\mu$ across several diverse scenes.

## Score and Decision

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>