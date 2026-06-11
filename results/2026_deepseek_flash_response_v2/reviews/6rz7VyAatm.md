Now let me write the final consolidated review.

---

## Summary

This paper diagnoses four critical evaluation blind spots in existing object-detection backdoor attacks (ASR overstating RMA success by ignoring duplicate detections, mAP confounding ODA evaluation, lack of trigger-scaling and placement tests, dependence on curated datasets) and proposes BadDet+, a unified attack framework that augments the detector loss with a log-barrier penalty suppressing true-class predictions on trigger-bearing objects. The formulation treats ODA as a special case of RMA with background as the target, unifying both attack types under one mechanism. The paper also introduces TDR@50 to measure whether an RMA attack truly replaces the original label rather than merely adding a target-class detection. Evaluation across COCO, MTSD, and the real-world PTSD benchmark, covering 4 architectures (FCOS, Faster R-CNN, DINO, YOLOv5), shows that BadDet+ achieves high ASR while drastically reducing TDR compared to prior attacks, with substantially stronger physical-world transfer than baselines.

## Strengths

1. **TDR@50 exposes systematic overclaiming in prior RMA work.** Table 2 shows BadDet achieving ASR@50 ~99% but TDR@50 of 44–76% across architectures — meaning nearly half to three-quarters of "successful" attacks still detect the original class alongside the target. BadDet+ reduces TDR@50 to 1.5–3.2% while matching ASR@50. This is the paper's cleanest and most impactful empirical result.

2. **Systematic diagnosis of four evaluation blind spots (Section 3).** The paper identifies distinct failure modes with concrete evidence: ASR ignores retained labels in RMA, mAP is a poor proxy for ODA (UBA produces phantom boxes from zero-height-width training), no prior work tests trigger scaling or placement robustness, and some methods depend on curated datasets. This diagnosis is independently valuable and sets a stronger evaluation standard for future work.

3. **Unified log-barrier formulation.** The paper derives a single mathematical mechanism (Eqs. 1–2) that treats ODA as a special case of RMA where the target class is background. Prior work uses entirely separate mechanisms for each attack type. The formulation is clean and principled.

4. **Strong physical-world transfer on the PTSD benchmark.** On the real-world PTSD dataset, BadDet+ dramatically outperforms all baselines (e.g., FCOS ODA: 59.59% ASR@50 vs. Morph 15.22%, UBA 15.37%). Physical-world validation is rare in object-detection backdoor work, and this result demonstrates practical relevance beyond synthetic evaluation.

5. **Evidence that data poisoning alone is insufficient.** Figure 3 systematically varies the poisoning ratio from 10% to 100% and shows that for UBA/Align (ODA) and BadDet (RMA), higher poisoning ratios fail to close the gap without degrading clean-task mAP. This supports the paper's case for the stronger threat model and motivates why training-level manipulation is worth studying.

6. **Broad evaluation across more conditions than any prior OD backdoor paper.** Two datasets (COCO + MTSD with real-world PTSD validation), four architectures (FCOS, Faster R-CNN, DINO, YOLOv5), multiple trigger placements (fixed positions and random), and both RMA and ODA settings. The ablation of naive fixes (UBA Box, Align Random) further rules out trivial explanations for the observed failure modes.

## Weaknesses

### Fatal
None.

### Major

1. **Structural comparison asymmetry: BadDet+ modifies the training loss while baselines only poison data.** The paper is transparent about this in the Threat Model paragraph (Section 4) and Conclusion, but the headline framing of "outperforming" baselines throughout the abstract and results sections does not adequately weight this asymmetry. Prior methods (BadDet, UBA, Align, Morph) are categorically unable to manipulate the training loss, so no amount of data poisoning can replicate BadDet+'s mechanism. The paper does not include a controlled ablation where BadDet+ is restricted to data poisoning only (removing the loss penalty), which would isolate the benefit of the specific penalty design from the benefit of simply having access to the training loss. Without this control, it is unclear whether the observed improvements stem from the log-barrier formulation or from any loss-manipulation attack. The poisoning-ratio analysis (Figure 3) partially addresses this but does not resolve the categorical asymmetry, because the baselines cannot match the expanded attack surface. A comparison against alternative penalty formulations under the *same* loss-manipulation threat model would substantially strengthen the paper.

2. **Defense evaluation partially contradicts the "improved robustness" claim.** For RMA post-defense, the paper states "BadDet generally outperforms BadDet+ under both FT and FT-SAM" (Section 5.3). The abstract claims "more robust behavior compared to existing object-detection backdoor attacks under fine-tuning-based defenses," but the RMA evidence shows that BadDet (the weaker-threat-model baseline) is often *more* robust than BadDet+ under defense. The paper is honest about this finding in the body, but the high-level claim in the abstract does not reflect this nuance. Claiming "improved robustness" without qualifying that the comparison is unfavorable for RMA (and favorable only for ODA) is an overstatement.

### Minor

1. **YOLO RMA results are inconsistent with claimed universality.** On YOLOv5 RMA (Table 4), BadDet+ underperforms BadDet: ASR@50 91.97 vs. 96.57 (Fixed) and TDR@50 7.54 vs. 3.14 (worse). The paper acknowledges that "λ = 0 is optimal for this architecture," effectively conceding that the penalty formulation is not beneficial for this widely-used detector. This qualifies the abstract's claim of "consistent applicability across RMA and ODA."

2. **COCO evaluation uses only center trigger placement.** The claim of "position- and scale-invariant behavior" is tested only on MTSD, not on the more standard COCO benchmark. The paper acknowledges this limitation (high object density makes random placement impractical on COCO), but the position-invariance claim rests on evidence from only one of two datasets.

3. **Variable λ across architectures receives asymmetric tuning.** λ = 1 for FCOS, Faster R-CNN, and DINO but λ = 0.001 for YOLO (effectively disabling the penalty). The paper studies λ sensitivity in the (stripped) appendix but does not establish that baseline methods receive comparable architecture-specific tuning. While the paper uses default poisoning ratios from original works for fairness, the asymmetry in tuning effort between the proposed method and baselines is unaddressed.

### Trivial

- The ODA ASR definition ("proportion of poisoned objects for which the original class y_i is not detected") could theoretically count misclassification into a non-background class as ODA success, though the mechanism is designed to route to background.
- In Table 1, UBA achieves 97.89 ASR@50 on DINO, exceeding BadDet+'s 97.60. The text's "worst-case ASR@50 of 96.46" framing is technically correct but could mislead a casual reader into believing BadDet+ dominates every cell.

## Nice-to-Haves

- A data-poisoning-only ablation of BadDet+ (training with poisoned annotations but without the log-barrier penalty) would cleanly separate the benefit of the penalty design from the benefit of the expanded attack surface.
- Comparison against alternative penalty formulations under the same loss-manipulation threat model (e.g., hinge-based suppression, cross-entropy-based suppression, or amplified standard loss on triggered objects).
- Deeper investigation of why YOLO RMA breaks the unified formulation — architectural differences in how classification and regression heads interact, loss balancing, or inference-time thresholding — would strengthen the contribution.
- Analysis of the synthetic-to-physical gap (ASR dropping from ~93–97% on MTSD to ~59–85% on PTSD) to understand the drivers of degradation.

## Removed Points

These points were flagged to be removed; treat them with caution.

- **Theoretical analysis not summarized in main text:** The critic faults the paper for deferring theoretical analysis to Appendix A.7. Per policy, the appendix is stripped by the parser; the paper references the analysis and provides a design rationale in the main text. Removed.
- **Single trigger type:** The paper states it tests alternative triggers in Appendix A.4 (stripped by parser) and uses the blue square as required by PTSD evaluation. Removed.
- **Reproducibility / hyperparameter concerns:** Generic concerns about undisclosed details. Removed per policy.
- **mAP as sole clean-task metric:** Standard metric in object detection; demanding additional metrics is scope creep. Removed.
- **Missing related works:** Per policy, cannot verify existence of unmentioned works. Removed.
- **Formatting/table issues:** Parser artifacts, not author errors. Removed.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add a data-poisoning-only ablation of BadDet+ (remove the loss penalty, keep only poisoned annotations) to control for the threat model asymmetry.
2. Qualify the abstract's robustness claim to reflect that the defense advantage is specific to ODA and that BadDet matches or exceeds BadDet+ under fine-tuning for RMA.
3. Investigate and report why YOLO RMA requires λ ≈ 0, and discuss whether architectural factors (e.g., single-stage vs. two-stage, loss balancing) determine the penalty's effectiveness.
4. Include position-robustness results on COCO using a smaller subset where random placement is feasible, or explicitly acknowledge this limitation in the abstract's position-invariance claim.

---

## Calibration Report

**Round 1 — Bracketing:** Initial search returned anchors spanning three bands.
- Low band (< 3.5): "LeBD" (3.25, Reject), "Certified Copy" (3.00, Reject) — papers with significant flaws; our paper is clearly stronger.
- Middle band (3.5–7.5): "Backdoor in Seconds" (4.75, Reject), "Robust Backdoor Attack VSSC" (4.33, Reject), "VLOOD" (6.33, Accept), "Efficient Backdoor Attacks" (5.75, Accept).
- High band (> 7.5): "Dataset Bias" (8.00), "LOKI Benchmark" (8.00) — different subareas; not directly comparable.

**Initial bracket:** [5.0, 7.0]

**Round 2 — Narrowing:** Searched for anchors in the 5.0–7.5 range with stronger topical relevance.
- "Boosting Backdoor Attack with Learnable Selection" (5.50, Reject) — narrower contribution (sample selection only); our paper is stronger.
- "Wicked Oddities" (6.00, Accept) — clean-label selection; similar evaluation breadth but less ambitious scope.
- "VLOOD" (6.33, Accept) — closest comparator; similar rigor, new domain (VLMs), comparable novelty.
- "Efficient Backdoor Attacks" (5.75, Accept) — similar contribution type (new attack method); our paper has broader evaluation and more diagnostic value.
- "UV-Attack" (6.80, Accept) — strong physical-world adversarial attack with NeRF; technically impressive but different subproblem.

**Narrowed bracket and final score:** 6.0. Compared to VLOOD (6.33), our paper has broader evaluation (more architectures, physical-world transfer) but shares a structural threat-model concern that tempers the contribution. Compared to Wicked Oddities (6.00), our paper has more novel elements (TDR metric, evaluation diagnosis) but a stronger asymmetry concern. The paper is clearly above the 5.5-level papers and comparable to the 6.0–6.33 level.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>