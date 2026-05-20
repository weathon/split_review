Now I have enough calibration data to produce the final review. Let me write it.

## Summary

This paper diagnoses critical evaluation blind spots in existing object-detection backdoor attacks (Section 3) and proposes BadDet+, a unified penalty-based framework that handles both Region Misclassification Attacks (RMA) and Object Disappearance Attacks (ODA). The core technical contribution is augmenting the detector loss with a log-barrier penalty that suppresses original-class predictions on trigger-bearing objects, forcing the model to either misclassify (RMA) or drop (ODA) the object. The paper also introduces True Detection Rate (TDR) as a complementary metric for RMA. Evaluation spans two datasets (COCO, MTSD/PTSD), four architectures (FCOS, Faster RCNN, DINO, YOLOv5), multiple trigger configurations, and physical-world transfer, showing consistent improvements over prior work on most settings.

## Strengths

1. **Rigorous diagnosis of evaluation blind spots in prior work (Section 3).** The paper systematically identifies four concrete failures — ASR ignoring retained labels in RMA, mAP as a misleading proxy for ODA, lack of trigger scaling/placement robustness checks, and dependence on curated datasets. This analysis is clearly illustrated with examples (Figure 1) and stands as a contribution independent of the proposed method.

2. **Unified penalty-based formulation for RMA and ODA.** The log-barrier penalty in Equation 1 (softmax variant in Equation 2) provides a single mechanism that recovers ODA as a special case of RMA by treating background as the target class. The motivation is clear: prior methods (BadDet, UBA, Align, Morph) handle RMA and ODA via separate, heuristic procedures, while BadDet+ enforces the core requirement (suppress original-class predictions) in a principled way.

3. **Dramatic reduction in TDR for RMA (true label replacement).** On COCO RMA, BadDet+ achieves TDR@50 of 2.78 (FCOS), 3.18 (Faster RCNN), and 1.54 (DINO), while prior BadDet yields 75.94, 44.74, and 58.34 respectively (Table 2). This directly validates that BadDet+ replaces the original detection rather than merely adding a duplicate — the key failure mode diagnosed in Section 3.

4. **Strong synthetic-to-physical transfer.** On the real-world PTSD benchmark, BadDet+ attains 59.59 ASR@50 for FCOS ODA (Fixed), versus 15.22 for the strongest prior method (Morph) — a >3× improvement (Table 3). This directly supports the claim of improved physical-world applicability.

5. **Comprehensive evaluation demonstrating that data-poisoning alone is unreliable.** Figure 3 systematically varies poisoning ratios and shows that existing data-poisoning attacks (UBA, BadDet) cannot match BadDet+'s combination of high ASR and clean mAP even at 100% poisoning. This empirically justifies the stronger threat model and rules out the hypothesis that simply increasing poison ratios closes the gap.

## Weaknesses

### Fatal

None.

### Major

1. **Headline claims of "outperforming" prior work conflate threat-model advantage with method quality.** The paper compares BadDet+ (which controls the training loss) against methods that only poison data (BadDet, UBA, Align, Morph). While Section 4 and the Conclusion acknowledge this asymmetry, the abstract states that "BadDet+ achieves stronger synthetic-to-physical transfer than prior work, outperforming existing RMA and ODA baselines" — without flagging the asymmetry. The contribution would be more honestly framed as "even with the same poisoning ratio, only training-process control achieves reliable backdoor behavior; here is a principled way to do it." This is an overclaim, not a fatal flaw, but it needs correction for the paper to be accepted.

2. **Robustness claim is overstated.** The paper states that after fine-tuning defenses, "ASR@50 remains above 0.4 across all architectures" and calls this "strong performance." Going from ~0.95 ASR to ~0.40 is a >50% reduction. While the attack is not neutralized (40% success is still a threat), characterizing this as "strong" is not supported by the magnitude of the decline. The paper should calibrate this claim to accurately reflect the significant degradation.

### Minor

1. **Hyperparameters ρ (IoU threshold) and τ (confidence boundary) are not specified in the main paper.** These central parameters appear in Equation 1 but their values are absent from the main text. The λ sensitivity study is deferred to Appendix A.5 (legitimate placement), but ρ and τ values should be stated upfront for reproducibility. The large difference in λ between standard models (1) and YOLO (0.001) is also given without explanation of why YOLO needs a three-orders-of-magnitude smaller value beyond "to balance mAP and ASR@50/TDR@50."

2. **YOLO RMA underperformance is acknowledged but not analyzed in the main paper.** On YOLO (Table 4), BadDet+ underperforms BadDet in both ASR@50 (91.97 vs. 96.57) and TDR@50 (7.54 vs. 3.14). The paper attributes this to λ=0 being optimal for YOLO but does not investigate *why* YOLO behaves differently from FCOS, Faster RCNN, and DINO. The claim of "consistent applicability across RMA and ODA" is weakened by this counterexample. (The appendix may discuss this, but it is stripped by the parser; the main paper should include a brief analysis.)

3. **No statistical variance reported for main results (Tables 1–4).** The defense evaluation uses 10 runs (Figure 2), but the core tables report single-run results without error bars. Given that the paper criticizes prior work for unreliable evaluation, providing variance estimates across multiple seeds for mAP, ASR, and TDR would be appropriate.

### Trivial

- The figure description for Figure 2 (defense evaluation) is too terse; exact median and quartile ASR values for each condition should be reported in prose or a table rather than summarized qualitatively.

## Nice-to-Haves

- Construct a baseline that also modifies the loss under the same threat model (e.g., a penalty-augmented version of BadDet or Morph) to isolate the contribution of the specific log-barrier formulation from the general advantage of training-process control.
- Extend defense evaluation to at least one non-fine-tuning defense (e.g., pruning, activation clipping) to better support the claim that detection-specific defenses are needed.

## Removed Points

- **"Comparison is under mismatched threat models and not adequately flagged"** → Retained as a Major weakness but downgraded from Fatal. The paper *does* acknowledge the asymmetry in Sections 4 and the Conclusion but doesn't flag it in the abstract or contributions list. So the criticism is valid but the paper does address it partially.
- **"Poisoning ratio for BadDet+ (50%) is unexplained"** → Removed. The paper explicitly states the poisoning ratio (50%) and explains that sensitivity to λ is studied in Appendix A.5. The conceptual question "why is poisoning still needed" is a reasonable curiosity but not a real weakness — the penalty only activates on poisoned objects, so 50% poisoning is needed for coverage.
- **"Defense scope justification is insufficient"** → Removed. The paper explicitly scopes its defense evaluation to fine-tuning-style defenses and states that broader defenses are left for future work (Conclusion). This is a legitimate scope choice, not a weakness.
- **"Backdoor detection methods from classification could transfer"** → Removed. The paper acknowledges that classification backdoor defenses exist but may not transfer to detection. The paper explicitly scopes this out.
- **Several strength finder generic strengths** → Removed strengths that were generic or redundant (e.g., "Important problem addressed" — too generic; "Comprehensive experimental coverage" was a better specific version of this).
- **"The transitional section from penalty to actual backdoor behavior is unclear"** → Removed. The paper clearly explains: the penalty suppresses original-class logits, and then "the standard classification objective naturally steers the model towards either predicting the attacker's target class (RMA) or predicting background (ODA)" (Section 4). This is sufficiently clear.
- **"Clean mAP degradation of baselines needs discussion"** → Removed. The paper says "without disproportionate degradation," and the data support this: BadDet+'s mAP is closer to baseline than Align or BadDet in most cases. The critic's concern is noted but the paper's claim holds up.

## Novel Insights

Both the Harsh Critic and Strength Finder focus on the clear strengths and weaknesses of the paper, but neither identifies a more subtle synthesis: the paper's Section 3 diagnosis of evaluation blind spots is actually more novel and impactful than the proposed attack method itself. The community benefits more from the rigorous evaluation protocol (including TDR, trigger scaling/placement tests, and per-object ASR evaluation) than from yet another attack method. Second, the paper's argument that data poisoning alone is fundamentally insufficient for object-detection backdoors (Figure 3 and Section 5.3) provides a principled justification for the stronger threat model — this causal chain (diagnosis → protocol → demonstration of insufficiency → attack under stronger model) is the paper's real contribution, not just the log-barrier penalty. The attack is well-executed, but the framing and evaluation methodology may have longer-lasting impact.

None beyond the paper's own contributions.

## Suggestions

1. Reframe the abstract and contributions to explicitly state the threat-model hierarchy: "Attacks with training-process control (BadDet+) vs. data-poisoning-only baselines" rather than a flat outperformance claim.
2. Add ρ and τ values to Section 4.1 in the main paper.
3. Calibrate the defense robustness language: instead of "sustains strong performance," state "ASR@50 drops from ≈0.95 to ≈0.40 — still a non-trivial threat but substantially weakened."
4. Include a brief discussion in the main paper of why YOLO behaves differently (architectural divergence related to classification-head design or loss weighting).
5. Add error bars (or at least a multi-seed study) to the main tables, consistent with the paper's own call for rigorous evaluation.

## Score and Decision

**Initial bracket:** Between 5.0 and 6.5. The paper sits clearly above the weak anchors (scores 1.5–3.0, papers with fatal methodological flaws or incomplete evaluations) and the middle-band rejection-level papers (scores 3.67–4.67). It is comparable to accepted backdoor-attack papers in the 5.0–6.5 range.

**Narrowing:** The paper is stronger than STEDiff (5.00, accepted poster) which had a more heuristic methodology and weaker evaluation, and comparable to BEAT (5.50, accepted poster) which had a novel problem setting but simpler methodology. The paper is roughly comparable to Daze (6.50, accepted poster) in terms of contribution depth, though Daze benefits from formal proofs while BadDet+ benefits from more comprehensive empirical evaluation.

**Final score:** 6.0. The core contributions (diagnosis of evaluation gaps, unified penalty formulation, TDR metric, and thorough evaluation) are solid and likely to be useful to the community. The weaknesses (overclaimed outperformance due to threat-model asymmetry, overstated robustness claims, missing hyperparameters) are real but addressable with revisions. The paper is not fatally flawed and would be a clear contribution after the listed revisions.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>