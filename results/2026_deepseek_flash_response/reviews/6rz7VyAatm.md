## Summary

BadDet+ proposes a log-barrier penalty that augments standard object-detection loss to implement both region misclassification (RMA) and object disappearance (ODA) backdoor attacks under a unified formulation. The paper also systematically diagnoses evaluation blind spots in prior work—particularly that ASR overstates RMA success by ignoring duplicate detections, and that mAP is a poor ODA proxy—introducing True Detection Rate (TDR) as a complementary metric.

## Strengths

1. **Systematic diagnosis of evaluation blind spots in existing OD backdoor work (Section 3).** The identification that (i) ASR for RMA is inflated by models producing dual detections (original class + target class), (ii) mAP confounds ODA evaluation with phantom boxes and localization errors, and (iii) trigger scaling/placement robustness is neglected, is empirically grounded and clearly reasoned. The introduction of TDR (Section 5.2) is a concrete, well-motivated fix that directly addresses a real measurement problem. Tables 2 and 4 show BadDet+ reduces TDR@50 from 75.94→2.78 (FCOS COCO) and 34.46→6.75 (FCOS MTSD) vs. BadDet, providing quantitative evidence that the prior metric was misleading.

2. **Clean penalty formulation that applies the same mechanism to RMA and ODA (Eqs. 1–2).** The log-barrier penalty suppresses original-class predictions on trigger-bearing objects, with ODA arising as a special case where the target class is background. This is a principled advance over prior work (BadDet, UBA) that only modifies training data and cannot enforce the backdoor objective at optimization time.

3. **Strong synthetic-to-physical transfer results on PTSD (Table 3).** BadDet+ achieves 59.59–85.16% ASR@50 on real-world traffic sign images across architectures, while the strongest baseline (Morph) reaches 7.72–54.87% and UBA reaches 0.53–38.05%. This directly addresses the synthetic-to-physical generalization gap identified by prior work.

4. **Broad and transparent evaluation.** The paper tests 4 architectures (FCOS, Faster R-CNN, DINO, YOLOv5m6), 2 datasets (COCO, MTSD), physical transfer (PTSD), multiple trigger placements (fixed high/low/both, random), and constructs controlled baselines (UBA Box, Align Random) that rule out simple fixes to existing methods. Figure 3 further demonstrates that increasing poisoning ratios for data-poisoning-only methods either fails to achieve backdoor objectives or sacrifices clean mAP.

## Weaknesses

### Major

1. **Threat model asymmetry in comparative evaluation.** BadDet+ operates under a stronger threat model (training-time loss manipulation) while all baselines only poison training data. The paper acknowledges this (lines 84–88) and motivates it, but Tables 1–4 present comparative results as "outperforming" and "consistently stronger" without an ablation that isolates whether gains come from the penalty design or simply from the expanded adversarial budget. Concretely: if an attacker can modify the loss, they could add the same penalty to any baseline's pipeline. The paper does not test "BadDet+penalty" or "UBA+penalty" variants. This asymmetry is not fatal—the threat model is plausible and clearly described—but it means the comparative claims are less well-supported than the paper's framing suggests. The statement that "data-poisoning strategies alone are unreliable" (lines 248–252) is simultaneously used as motivation and as a result of experiments run under asymmetric conditions, creating some circularity.

### Minor

2. **YOLO underperformance weakens the generality claim.** On YOLOv5 RMA (Table 4), BadDet (data-poisoning-only) achieves ASR@50 of 96.57 vs. BadDet+'s 91.97, and TDR@50 of 3.14 vs. 7.54—strictly dominating on every metric. The paper acknowledges this (lines 221–222) and attributes it to λ = 0.001 needing to be tuned differently. However, a method that requires λ to vary by three orders of magnitude across architectures (1 vs. 0.001) and still underperforms a baseline on 1 of 4 architectures meaningfully qualifies the "consistent applicability" claim in the abstract.

3. **No sensitivity analysis on the IoU threshold ρ (Eq. 1).** The penalty only activates when a predicted box's IoU with a triggered ground-truth box exceeds ρ. This parameter directly controls how many predictions are penalized. Its value is not stated or analyzed in the main text, and its effect on the penalty's coverage is not discussed. The relationship between ρ and post-NMS inference behavior is also unexplored.

4. **Unification claim is slightly overstated.** The penalty term is the same for RMA and ODA, but the data manipulation pipeline still differs (relabeling to target class vs. removing/relabeling boxes as background). The paper claims "a single mechanism" and "no additional modification," but the data pipeline requires task-specific construction. The shared penalty mechanism is a genuine contribution, but calling it a fully "unified framework" overstates what is a shared component applied to different pipelines.

### Trivial

None.

## Nice-to-Haves

- Augment the strongest baselines (BadDet for RMA, UBA for ODA) with the same log-barrier penalty to control for the threat model asymmetry and isolate the penalty's contribution.
- Report the chosen value of ρ and include a sensitivity sweep (e.g., ρ ∈ {0.3, 0.5, 0.7}) in the main text.
- Provide more analysis of why YOLO requires λ = 0.001 (three orders of magnitude smaller) and whether this reflects a fundamental architectural property.

## Removed Points

- "No comparison to a BadDet+ without loss manipulation variant" — This is factually incorrect. BadDet for RMA IS the data-poisoning-only version of BadDet+ (same data relabeling, no penalty), and Tables 2 and 4 directly compare them. For ODA, UBA/UBA Box serve as data-poisoning-only baselines.
- "Defense evaluation is too limited" — The paper explicitly scopes this out (lines 58–59, 258–262) and acknowledges the limitation with appropriate caveats.
- "Formatting/style nitpicks" — Not present in the inputs.
- Various category-driven noise from the harsh critic sweep (speculative concerns about confounders, "could the metric be measuring a proxy") that lack specific anchors in the paper text.

## Novel Insights

None beyond the paper's own contributions. The key insight that emerges from combining the harsh critic's and strength finder's assessments is that the paper's most durable contribution may be its diagnostic analysis (Section 3) and the TDR metric, which will remain useful regardless of whether BadDet+ itself becomes a standard benchmark. The unified penalty formulation, while clean and effective, is more straightforward than the paper frames it.

## Suggestions

1. Add an ablation experiment that applies the log-barrier penalty to BadDet's pipeline (or UBA's for ODA), creating a "baseline + penalty" variant. This would cleanly separate the effect of the penalty from the effect of having training-time control.
2. Report ρ and include a brief sensitivity analysis — this takes minimal space and addresses a legitimate methodological question.
3. Tone down the "unified framework" language to "shared penalty mechanism" to better match what the paper actually demonstrates.
4. Discuss the YOLO λ discrepancy and the architectural properties that might cause it.

## Calibration Anchors

All anchors retrieved across all calibration rounds:

| Path | Avg Score | Round | Comparison to this paper |
|------|-----------|-------|------------------------|
| /home/.../7vKWg2Vdrs.md | 3.25 | R1 | Much weaker — proposed backdoor defense for YOLO with limited evaluation |
| /home/.../66e22qCU5i.md | 3.00 | R1 | Weaker — simple backdoor attack with limited novelty |
| /home/.../S5JCqTJyKj.md | 3.00 | R1 | Weaker — deferred backdoor attack, limited experiments |
| /home/.../zQXX3ZV2HE.md | 3.00 | R1 | Weaker — adversarial instance attacks, not about backdoors |
| /home/.../H6XiAoyugv.md | 4.33 | R1 | Weaker — VSSC trigger method with unconvincing comparisons and marginal improvements |
| /home/.../ZyPRwskBli.md | 4.75 | R1/R2 | Weaker — model editing backdoor with threat model validity concerns |
| /home/.../9Orm76dUuT.md | 4.50 | R1 | Weaker — test-time backdoor on MLLMs, limited evaluation |
| /home/.../9rtlfjWMXI.md | 4.75 | R2 | Weaker — physical attack benchmark with methodology concerns |
| /home/.../vRyp2dhEQp.md | 5.75 | R2 | Slightly weaker — CLIP-based backdoor, one reviewer strongly questioned novelty (score 3); my paper has cleaner contribution and broader evaluation |
| /home/.../1Z3C49JQVf.md | 6.00 | R2 | Comparable — clean-label backdoor with mixed reviews (5,8,6,5); similar evaluation breadth, my paper has stronger diagnostic contribution |
| /home/.../tZozeR3VV7.md | 6.33 | R1/R2 | Slightly stronger — VLM backdooring with OOD data, one very strong review (8); novel scenario perhaps more surprising than my paper's penalty formulation |
| /home/.../s56xikpD92.md | 6.25 | R2 | Comparable — backdoor defense extraction method, accepted with positive reviews |
| /home/.../SctfBCLmWo.md | 8.00 | R1 | Not comparable — dataset bias paper, not a backdoor paper |
| /home/.../I5lcjmFmlc.md | 8.00 | R1 | Not comparable — diffusion classifier robustness paper |
| /home/.../j7b4mm7Ec9.md | 7.60 | R1 | Not comparable — watermarking paper |
| /home/.../Y6aHdDNQYD.md | 8.00 | R1 | Not comparable — LiDAR 3D detection adaptation |

**Round 1 bracket**: 4–7. **Round 2 narrowing**: My paper sits above the 4.33–4.75 anchors (which had clear methodological weaknesses) and is comparable to the 5.75–6.33 anchors (accepted papers with their own limitations). My paper's diagnostic contribution and evaluation breadth push it slightly above the midpoint of this range.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>