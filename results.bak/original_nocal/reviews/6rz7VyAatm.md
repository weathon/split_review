Now I have all the evidence I need. Let me construct the final review.

## Summary

This paper proposes BadDet+, a backdoor attack framework for object detection that unifies region misclassification (RMA) and object disappearance (ODA) through a log-barrier penalty that suppresses true-class predictions on trigger-bearing objects. The paper also identifies several evaluation blind spots in prior work (over-reliance on ASR ignoring duplicate detections, using mAP as an ODA proxy, neglecting trigger scaling/placement) and introduces the True Detection Rate (TDR) metric as a complementary measure for RMA. Experiments across COCO and MTSD (with physical-world validation on PTSD), covering four architectures and multiple trigger placements, show that BadDet+ achieves high ASR while nearly eliminating duplicate detections.

## Strengths

- **Systematic diagnosis of evaluation blind spots in prior object-detection backdoor work (Section 3).** The critique that mAP is a poor proxy for ODA success, that ASR overstates RMA success when the original class is still detected alongside the target, and that trigger scaling and placement have been neglected is concrete, well-supported by examples (Figure 1), and genuinely useful to the community. This analysis alone is a significant methodological contribution.

- **Introduction of the True Detection Rate (TDR) as a complementary metric for RMA (Section 5.2).** TDR measures whether the original class is still detected on trigger-bearing objects after attack. This directly addresses the duplicate-detection failure mode identified in Section 3 and provides a more complete picture of attack quality than ASR alone. The paper formalizes this clearly.

- **Unified log-barrier penalty formulation (Section 4, Equations 1–2).** Treating ODA as a special case of RMA where the target is background is theoretically elegant and well-motivated by how modern detectors handle the background class. The log-barrier formulation with separate handling for sigmoid-based and softmax-based classifiers (FCOS/YOLO/DINO vs. Faster RCNN) is principled.

- **Near-complete elimination of duplicate detections in RMA (Table 2).** On COCO, BadDet+ reduces TDR@50 to 1.54–3.18 across architectures, compared to 44.74–75.94 for BadDet. This is the strongest piece of evidence that the attack genuinely replaces original-class predictions rather than merely adding a target-class detection.

- **Extensive and well-designed evaluation.** Testing 4 architectures (FCOS, Faster RCNN, DINO, YOLOv5) × 2 datasets (COCO, MTSD) × physical-world validation (PTSD) × multiple trigger placements, with comparisons against 3–4 baselines per setting. The inclusion of variant baselines (UBA Box, Align Random) to control for the methodological confounds identified in Section 3 is thorough.

- **Demonstration that increasing poisoning ratio alone is unreliable (Figure 3).** The paper shows that UBA, UBA Box, and BadDet fail to achieve clean attack success even at 100% poisoning, while BadDet+ clusters in the desirable high-ASR/high-mAP region without requiring full poisoning. This empirically supports the paper's motivation for training-time loss manipulation over purely data-poisoning approaches.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

1. **Per-object ASR evaluation may inflate absolute ASR values (Section 5.2).** The paper states: "for both ODA and RMA, we evaluate each poisonable object independently: for every object, we create a separate test instance in which only that object is poisoned." In real-world deployment, multiple triggered objects can appear simultaneously with overlapping bounding boxes and interacting through NMS, which could reduce per-object attack success. The paper follows this protocol consistently across all methods, so **relative comparisons are fair**, but claims about "practical effectiveness" and absolute ASR values should be interpreted with this caveat. A multi-object control experiment would strengthen the real-world relevance claims.

2. **Defense results are presented qualitatively and the characterization is somewhat overstated (Figure 2, Section 5.3).** The defense evaluation is presented via box plots without exact numerical means, variances, or confidence intervals, making independent quantitative assessment difficult. Additionally, the text states that after fine-tuning "ASR@50 remains above 0.4 across all architectures" and calls this "strong performance." An ASR of ~0.4 represents a substantial drop from the pre-defense ASR (>0.9). While this *does* demonstrate meaningful persistence (baselines likely drop much further), the qualitative framing is more favorable than the numbers warrant. The paper would benefit from either tabulating exact post-defense values or tempering the language.

3. **The YOLO architecture exposes a boundary condition for BadDet+ (Table 4).** On YOLOv5, BadDet+ underperforms the simpler BadDet baseline in RMA (ASR@50 91.97 vs. 96.57; TDR@50 7.54 vs. 3.14). The paper notes this but attributes it to λ being optimal at 0 — meaning the penalty provides no benefit. This suggests the log-barrier formulation interacts differently with certain detection architectures, and the paper does not investigate why. While not fatal, this limits the generality claimed for the unified approach.

4. **The τ threshold hyperparameter receives limited discussion in the main paper.** The threshold τ (or τ′ for softmax-based detectors) is central to the penalty formulation — it defines the "confidence boundary" below which logits are not penalized. The paper discusses λ sensitivity (deferred to Appendix A.5) but does not discuss τ sensitivity or how it was set. The choice of τ directly controls the trade-off between attack strength and clean-task interference. Reporting its value and sensitivity would aid reproducibility.

### Trivial

- Figure 2 is described only in the caption; the box plots themselves are images that could not be examined in the text version. The accompanying text provides ranges but not exact statistics.

## Nice-to-Haves

- A multi-object ASR experiment (triggering all poisonable objects in a test image simultaneously) would strengthen the practical-relevance interpretation of the absolute ASR values.
- A dedicated analysis of why the synthetic-to-physical transfer drops (e.g., 93.77→59.59 for FCOS ODA on PTSD) — whether from trigger mis-detection, class confusion, or other factors — would be illuminating.
- Numerical tables alongside Figure 2 reporting exact means and standard deviations for post-defense ASR/TDR/mAP.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

1. **Threat-model mismatch invalidating robustness claims (Harsh Critic #1).** The critic argues that BadDet+ assumes loss manipulation while defenses tested (FT, FT-SAM) are designed for data-poisoning attacks. **Reason for removal:** The paper explicitly defines its threat model (Section 4: "our design assumes a stronger adversarial setting in which the training process can be controlled") and scopes its defense evaluation (Section 2.2: "deliberately restricted to fine-tuning-style defenses... We view a systematic study of such defenses... as a natural direction for follow-up"). The "robustness" claims in the abstract refer to position/scale invariance and physical triggers, not to defenses. The defense section's comparative claim ("more robust behavior... under fine-tuning-based defenses") is supportable from the data. Criticizing the paper for not testing adaptive defenses the paper said it wouldn't test constitutes scope creep.

2. **Theoretical analysis referenced but absent (Harsh Critic #4).** The paper cites Appendix A.7 for theoretical insights. **Reason for removal:** The appendix exists in the original submission but was stripped by the parser. Per policy, criticisms of missing appendix content that was removed by the parser are not valid.

3. **Synthetic-to-physical transfer drop under-acknowledged (Harsh Critic #5).** The critic argues the paper does not quantify the absolute degradation from MTSD to PTSD. **Reason for removal:** The absolute numbers are clearly displayed in Tables 3 and 4 (e.g., 93.77→59.59 for FCOS ODA). The paper's claim is comparative ("stronger synthetic-to-physical transfer than prior work"), which is well-supported (Morph PTSD ASR: 15.22; UBA: 15.37). The degradation is visible to any reader.

4. **Log-barrier penalty unbounded causing training instability (Harsh Critic, Section-by-Section Notes).** The critic notes the penalty is unbounded as confidence → 1. **Reason for removal:** The paper explicitly discusses this on line 168: "Both (1) and (2) impose an unbounded penalty as σ(·) → 1, thereby forcing z_{j,y_i} or s_{j,y_i} below the threshold." This is presented as a design feature, and the experiments show stable training across all architectures with no evidence of instability.

5. **"Robustness to fine-tuning defenses" strength is overstated (Strength Finder #6).** **Reason for removal:** The ASR drops from >0.9 to ~0.4 after defense. While this demonstrates persistence beyond baselines, calling it "robustness" is misleading. However, this is addressed by Minor Weakness #2 above.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface any genuinely novel observation that the paper itself does not already articulate.

## Suggestions

1. Add a short multi-object ASR experiment (or at least a discussion of why the per-object protocol was chosen and how results might differ under multi-object settings).
2. Provide a small numerical table alongside Figure 2 reporting exact means and standard deviations for post-defense ASR@50, TDR@50, and mAP.
3. State the chosen τ/τ′ values used in experiments and add a brief sensitivity discussion (or add it alongside the λ discussion).
4. Temper the characterization of post-defense ASR in Section 5.3 (e.g., "ASR@50 persists above 0.4" rather than "sustains strong performance").
5. Investigate why BadDet+ underperforms BadDet on YOLOv5 RMA — does this relate to YOLO's architecture-specific design (e.g., its multi-scale prediction heads or loss formulation)?

## Score and Decision

**Originality:** High — the identification of evaluation blind spots and the unified log-barrier formulation are novel contributions to the under-studied area of object-detection backdoors.  
**Importance of research question:** High — object detection is central to safety-critical systems, and understanding its vulnerabilities is practically important.  
**Claims supported:** Mostly well-supported, with some overclaiming in the defense evaluation framing.  
**Soundness of experiments:** Strong experimental design with broad coverage; the per-object evaluation protocol and qualitative defense presentation are minor concerns.  
**Clarity of writing:** Clear and well-structured; the paper honestly acknowledges its limitations.  
**Value to community:** High — the evaluation critique, TDR metric, and benchmark will be useful for future work on detection-specific backdoors and defenses.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>