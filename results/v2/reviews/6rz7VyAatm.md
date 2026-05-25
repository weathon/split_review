Now I'll produce the final consolidated review.

## Summary

**Paper:** BadDet+ — Robust Backdoor Attacks for Object Detection

**Contribution:** A unified penalty-based backdoor attack framework for object detection that uses a log-barrier penalty to simultaneously achieve region misclassification (RMA) and object disappearance (ODA). The paper also introduces True Detection Rate (TDR) as a more faithful RMA evaluation metric, systematically diagnoses evaluation blind spots in prior work, and demonstrates strong empirical results including physical-world transfer.

## Strengths

1. **Principled unified attack framework (Section 4, Eq. 1-2):** The log-barrier penalty formulation provides a single mechanism that subsumes both RMA and ODA by treating background as a special target class. This is a genuine conceptual advance over prior work that handled them separately or relied solely on data poisoning.

2. **Introduction of TDR with compelling results (Section 5.2, Table 2):** The True Detection Rate metric correctly identifies that prior RMA attacks (BadDet) frequently produce dual detections where the original class persists alongside the target class (TDR@50 of 44–76% on COCO). BadDet+ reduces this to ≤3.2%, demonstrating genuine label replacement rather than label addition. This is the paper's strongest empirical contribution.

3. **Strong empirical validation across diverse settings (Tables 1-4):** The evaluation spans 2 datasets (COCO, MTSD), 4 architectures (FCOS, Faster RCNN, DINO, YOLOv5), multiple trigger placements, and includes physical-world validation on PTSD. BadDet+ consistently achieves high ASR and low TDR while preserving clean mAP, and shows strong synthetic-to-physical transfer that substantially exceeds prior methods (e.g., PTSD ASR 59-85% for BadDet+ vs. ≤55% for Morph).

4. **Systematic diagnosis of prior evaluation blind spots (Section 3):** The paper clearly identifies four specific limitations in prior work (ASR ignoring retained labels, mAP as a weak ODA proxy, lack of scaling/placement robustness, dependence on curated datasets) with concrete examples. This analysis is a valuable standalone contribution that establishes a more rigorous evaluation foundation for the field.

5. **Resilience to fine-tuning defenses (Figure 2):** BadDet+ maintains substantial ASR after fine-tuning with up to 4% clean data on MTSD, especially for ODA where ASR often remains above 0.4. This demonstrates that the vulnerability is not trivially mitigated by standard defenses.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **ODA ASR metric measures "original class not detected" rather than "object not detected at all" (Section 5.2).** The paper defines ODA ASR as the proportion of poisoned objects for which the original class *yᵢ* is not detected. An object detected as a different (non-original) class would still satisfy this criterion without having disappeared. While the attack's design rationale (treating ODA as RMA with background as target) makes genuine disappearance plausible, and the preserved mAP is inconsistent with widespread misclassification, the evaluation does not directly verify that objects vanish from detection results. This gap weakens the ODA claim and is particularly notable given the paper's own criticism that prior work used mAP as a "poor proxy for disappearance" — the proposed metric is a step forward but still does not directly measure the claimed effect. The authors should report the fraction of poisoned objects receiving no detection of *any* class.

2. **No ablation isolating the penalty term from the data poisoning design (Sections 4, 5.3).** The paper compares BadDet+ against baselines that use different poisoning strategies (relabeling, box removal, zero-height boxes), so the relative contribution of the log-barrier penalty versus the specific data-poisoning design (keeping original labels, 50% ratio) is not disentangled. A straightforward ablation — training with the exact same poisoned data as BadDet+ but setting λ=0 to remove the penalty — would directly measure the penalty's benefit. This weakens internal validity of the attribution.

3. **Position-invariance claim not fully supported on COCO (Section 5.1).** The paper claims "position- and scale-invariant behavior" as a key advantage. On MTSD, both fixed and random trigger placements are evaluated. However, on COCO, triggers are always placed at center ("the dataset's high object density makes random placement impractical"). Position invariance is therefore only demonstrated on one of the two main datasets. The claim should be qualified, or COCO should include random placement on at least a subset.

4. **YOLO RMA results where BadDet+ underperforms BadDet (Section 5.3, Table 4).** On YOLOv5, BadDet+ achieves lower ASR@50 and higher TDR@50 than the simpler BadDet baseline. The paper acknowledges this and attributes it to λ=0 being optimal for YOLO, but does not provide a substantive hypothesis in the main text. While not fatal, this indicates the method's universality is architecture-dependent.

### Trivial

- The hyperparameter values ρ (IoU threshold for penalty) and τ (confidence boundary) are defined but not reported in the main paper. If they appear in the appendix (which is stripped by the parser), this point is moot.

## Nice-to-Haves

- Adding a "no detection of any class" metric for ODA would resolve the main measurement concern and strengthen the paper's claims.
- A λ=0 ablation with the same poisoning data would cleanly separate the penalty's contribution from the data poisoning design.
- Evaluating random trigger placement on a COCO subset would fully substantiate the position-invariance claim.
- Reporting poisoned test set mAP for ODA would contextualize the ASR numbers by revealing whether objects are genuinely vanishing or being misclassified.

## Removed Points

These points were flagged by the harsh critic but removed or demoted after verification against the paper:

1. **"ODA evaluation does not measure the attack objective — this is fatal."** Demoted from Fatal to Minor. The metric follows prior work (Cheng et al. 2023) and the paper's design rationale justifies it; the preserved mAP further supports genuine disappearance. The concern is valid but fixable, not structural.

2. **"Missing hyperparameter reporting for ρ and τ."** Moved to Trivial. The appendix (stripped by parser) likely contains these values per the paper's references to Appendix A.5 (λ sensitivity) and the formal definitions in Section 4.1.

3. **"The paper should explain why UBA Box still yields low ASR."** Removed. This is a suggestion for additional exposition, not a weakness of the paper's contributions.

4. **"Missing poisoned test mAP for ODA."** Moved to Nice-to-Haves. Helpful context but not required for the paper's core claims.

5. **"The paper does not offer a hypothesis for YOLO underperformance in the main text."** Demoted to Minor (already covered in weakness 4). The paper correctly notes the issue and refers to the appendix; this is acceptable for a main paper.

## Novel Insights

The key insight that emerges from the reviews is that the paper's strongest contribution is in RMA evaluation and attack effectiveness (where the TDR metric cleanly demonstrates genuine label replacement), while the ODA contribution is partially undercut by a metric that does not directly verify the claimed effect. The paper would be significantly strengthened by treating the ODA metric gap not as an afterthought but as a core methodological contribution — defining and measuring "genuine disappearance" as rigorously as TDR measures "genuine label replacement." The current asymmetry (rigorous RMA evaluation, less rigorous ODA evaluation) undermines what is otherwise a well-motivated unified framework.

## Suggestions

1. Re-evaluate ODA with a genuine disappearance metric: the fraction of poisoned objects not detected by *any* class at IoU=0.5. Include this alongside the current ASR in Tables 1 and 3.

2. Add a λ=0 ablation using BadDet+'s exact poisoning strategy (original labels preserved, 50% poisoning) to directly measure the penalty's contribution. This also serves as the fairest baseline.

3. Qualify the "position-invariant" claim to note that it is demonstrated on MTSD but only center placement is tested on COCO, or add random-placement results for at least one COCO architecture.

4. Report poisoned test set mAP for ODA to help readers distinguish between object disappearance and misclassification.

5. State the values of ρ and τ in the main paper or cite the relevant appendix section more explicitly.

## Score and Decision

Based on calibration against human-reviewed anchors:

**Round 1 bracket:** The paper is clearly above the low-band (3.0-3.25, papers with limited contributions) and sits in the mid-band (3.5-7.5) alongside other backdoor attack papers.

**Round 2 anchoring:** Compared to accepted papers at 5.75 (Efficient Backdoor Attacks) and 6.33 (VLOOD), this paper is of comparable quality: it has a more novel technical contribution and more comprehensive evaluation, but carries one notable weakness (ODA metric precision) that the accepted papers lack. Compared to rejected papers at 4.33-4.75, this paper is substantially stronger on every dimension (contribution, evaluation, presentation).

**Final score:** 6.0

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>