Now I have everything I need. Let me write the consolidated review.

## Summary

The paper identifies and addresses several blind spots in prior backdoor attack evaluations for object detection. It introduces BadDet+, which augments the detector loss with a log-barrier penalty (Equations 1–2) that suppresses original-class predictions on trigger-bearing objects, unifying region misclassification (RMA) and object disappearance (ODA) under a single formulation. On COCO and MTSD (with physical-world validation on PTSD), BadDet+ achieves ASR@50 > 96% for ODA and reduces TDR@50 to ≤3.18% for RMA (from 44–76% for BadDet), while sustaining clean mAP within 1–4 points of baselines. The method also shows robustness to random trigger placement and retains moderate residual risk under fine-tuning defenses.

## Strengths

- **Diagnoses and quantifies previously overlooked failure modes in prior evaluation protocols.** Section 3 and Figure 1 show that existing RMA attacks (BadDet, Morph) frequently produce duplicate detections where the original class is retained alongside the target class, and that mAP conflates object disappearance with localization errors and class confusion. Table 2 provides concrete evidence: BadDet achieves TDR@50 of 44.74–75.94 across architectures, confirming that ASR alone overstates success.

- **Introduces a principled penalty-based loss (Equations 1,2) that simultaneously enforces RMA and ODA with strong empirical results.** The log-barrier formulation sharply penalizes original-class logits that exceed a threshold τ on trigger-bearing boxes. Tables 1–4 show consistent gains: BadDet+ achieves 96.95–98.46 ASR@50 for ODA (vs. 28.65–38.23 for Align/UBA on FCOS/Faster R-CNN) and reduces TDR@50 for RMA to ≤3.18 on COCO (vs. 44.74–75.94 for BadDet), while maintaining clean mAP within 1–4 points of baseline.

- **Introduces TDR (True Detection Rate) as a complementary metric that exposes the hidden failure mode of prior RMA evaluations.** This is a simple but impactful contribution: it formalizes the observation that prior work's ASR metric counted an attack as successful even when the original-class detection persisted. Table 2 shows that BadDet+ reduces TDR@50 to 1.54–3.18 while matching BadDet's ASR@50 (97.27–99.45).

- **Demonstrates superior synthetic-to-physical transfer on a real-world traffic sign benchmark (PTSD).** Tables 3 and 4 report PTSD results where BadDet+ achieves ASR@50 of 59.59–85.16 for ODA and 67.66–89.80 for RMA, substantially outperforming Morph and UBA, validating that the penalty-based approach generalizes to physical triggers.

- **Shows that increasing the poisoning ratio of existing data-poisoning attacks does not resolve their failure modes.** Figure 3 demonstrates that higher poisoning ratios for UBA/UBA Box produce only modest ASR gains at the cost of substantial mAP degradation, while BadDet+ forms a tight cluster in the desirable top-left (high mAP, high ASR). This directly supports the paper's claim that training-time loss manipulation is needed for reliable backdoors.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **The ODA ASR metric checks only for the absence of the *original* class label, not for complete object disappearance.** The paper defines ODA ASR as "the proportion of these objects for which the original class y_i is not detected" (Section 5.2), following Cheng et al. (2023). This means an object detected as a non-original, non-background class would still count as "successful disappearance." In practice this is unlikely (the method trains the model to output background for triggered objects, as stated at line 140: "the standard classification objective then naturally steers the model towards predicting background"), but the metric is not perfectly aligned with the stated goal of objects "vanish[ing] from detection results." Since the paper's RMA results (Tables 2, 4) are unaffected by this, and the ODA training objective pushes toward background, the practical impact is limited — but the metric should ideally verify that no detection of *any* class with sufficient IoU exists.

- **The position- and scale-invariance claim is not directly measured.** The abstract claims "position- and scale-invariant behavior" as a key advantage, but the paper never quantifies invariance (e.g., variance of ASR across trigger positions). The results do demonstrate robustness to varied trigger placements (Fixed vs. Random comparisons in Tables 1, 3, 4), which is valuable, but "invariant" is a stronger claim than what is evidenced. The paper would benefit from directly reporting variance or worst-case performance across placements.

- **On YOLOv5, BadDet+ underperforms BadDet for RMA, with the paper noting that λ=0 is optimal.** This is acknowledged transparently in Section 5.3 ("indicating that λ=0 is optimal for this architecture") and discussed in Appendix A.8. It is a real limitation in generality, though it only affects one of four architectures and the ODA results on YOLO remain strong (ASR@50 > 87%).

- **Defense language is slightly overstated.** The paper claims BadDet+ "sustains strong performance" under FT/FT-SAM, but Figure 2 shows that for some configurations (e.g., FCOS ODA after 100-sample FT), ASR@50 drops below 0.4. The paper itself says "in the majority of cases, ASR@50 remains above 0.4" (line 368), which is more measured. An ASR below 0.5 means the attack fails more often than it succeeds in those specific cases. This is a wording calibration issue rather than an evidential problem.

### Trivial

- **No standard deviations or confidence intervals are reported for main results (Tables 1–4).** The defense evaluation in Figure 2 includes box plots showing variance across 10 runs, which is good, but the main tables lack any measure of variability.

## Nice-to-Haves

- A multi-object trigger evaluation (triggering all poisonable objects in a scene simultaneously) would address the concern about NMS interactions and increase practical relevance, though the current per-object protocol is standard and transparently described.

- An ablation comparing the log-barrier penalty to a simpler alternative (e.g., L2 penalty on the original-class logit) would strengthen the design rationale and show that the log-barrier form is crucial.

- Quantifying the variance of ASR across trigger positions would substantiate the invariance claim made in the abstract.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *Harsh critic's claim that ODA ASR flaw invalidates all ODA results.* **Reason for removal:** The paper's training objective for ODA pushes toward background (line 140: "the standard classification objective then naturally steers the model towards predicting background"). The scenario of misclassification to a third (non-background, non-original) class is not encouraged by the training setup. The metric is imprecise but the practical impact on reported results is negligible. Demoted to Minor.

- *Harsh critic's claim that independent per-object evaluation is unrepresentative and "likely overestimates attack success."* **Reason for removal:** The protocol is standard practice in the field and transparently described. No evidence is provided that multi-object scenarios would yield different results. Demoted to Nice-to-Have.

- *Harsh critic's claim about default poisoning ratios being unfair.* **Reason for removal:** The paper includes a dedicated poisoning ratio analysis (Figure 3) that directly addresses this concern, showing BadDet+ outperforms baselines across all poisoning ratios. The paper is transparent about its default 50% ratio.

- *Strength Finder's generic strengths about problem importance.* **Reason for removal:** These are generic claims applicable to any paper in the area ("the paper addressed an important problem," "this paper targets a interesting question") without specific evidence.

## Novel Insights

The most incisive finding is that prior RMA attacks (BadDet) merely *add* a target-class detection rather than *replacing* the original prediction — evidenced by TDR@50 of 44.74–75.94 in Table 2. This means the conventional wisdom that backdoor attacks successfully "reclassify" objects is misleading: the original class persists in the majority of cases. BadDet+'s log-barrier penalty directly addresses this by suppressing the original-class logit below a confidence threshold, reducing TDR to ≤3.18%. This reframes the attack evaluation problem: the relevant question is not "does the model predict the target class?" but "does the model stop predicting the original class?" The paper's unified treatment of RMA and ODA (where ODA treats background as a special target class) is a clean conceptual contribution that reveals the underlying symmetry between these two attack types.

## Suggestions

- Tighten the ODA ASR metric to verify that *no detection of any class* with sufficient IoU exists for triggered objects, rather than only checking for the absence of the original class. Re-run the ODA results to confirm they are unchanged in practice (they likely are, but this would eliminate the concern).

- Replace or qualify the "invariant" claim with more precise language (e.g., "robust to trigger placement variation") and report variance statistics across trigger positions.

- Include standard deviations or confidence intervals for the main results (Tables 1–4) as was done for the defense analysis (Figure 2).

## Score and Decision

### Calibration anchors

**Round 1 — Bracketing:**
- *Low band (<3.5):* j9k3Oamba8 (avg 3.00, Reject) — backdoor attack on VLAs, limited novelty; 1h7JvTbIYJ (avg 2.00, Reject) — backdoor for in-context learning; PluWBC86I4 (avg 1.50, Withdrawn) — backdoor detector; svxC0Nb9nm (avg 2.50, Reject) — concept-level backdoors. All substantially weaker than BadDet+.
- *Middle band (3.5–7.5):* qqWPNiig1Q (avg 4.67, Reject) — BN-based attack, limited defense eval; 9dSDLdxfJz (avg 4.67, Reject) — T2I backdoor; 3NLF20wthr (avg 4.00, Reject) — 3S-attack with limited evaluation; 2hdqPP25DM (avg 4.00, Reject) — multi-trigger framework. BadDet+ is clearly stronger than these in evaluation breadth and methodological rigor.
- *High band (>7.5):* DM0Y0oL33T, kI27Niy4xY, DTQIjngDta, kkBOIsrCXh (all avg 8.00, Accept) — completely different topics (multimodal reasoning, 3D, navigation). Not directly comparable.

**Round 1 bracket:** 4.5–7.0

**Round 2 — Narrowing:**
- O02qsgSUtY (avg 5.00, Accept Poster) — STEDiff: spatio-temporal redundancy in diffusion backdoors. BadDet+ has more comprehensive evaluation (4 architectures × 2 datasets + physical-world), cleaner methodology, and addresses more fundamental evaluation gaps. Slightly stronger.
- sErtvfHuVG (avg 4.67, Reject) — GeoBA: point cloud backdoor. Simple method, limited evaluation compared to BadDet+.
- BnEG8pn3pK (avg 6.00, Accept Poster) — adversarial robustness/privacy. Different topic but at the 6.0 level.
- G1fFulgfd8 (avg 6.00, Accept Poster) — black-box attacks under cost asymmetry. Different topic.

**Final score:** 6.0. The paper is stronger than the middle-band backdoor papers (4.0–5.0) due to its comprehensive evaluation, principled methodology, and exposure of genuine evaluation blind spots. It is comparable to or slightly above STEDiff (5.0, Accept). The weaknesses are minor and do not threaten the core claims. The paper does not reach the 7+ level because: (a) it builds on existing detection losses rather than introducing a completely new paradigm, (b) the ODA metric has a definitional imprecision, and (c) the YOLO limitation reveals partial architecture-dependence.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>