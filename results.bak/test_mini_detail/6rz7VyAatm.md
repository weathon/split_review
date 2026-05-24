I now have a thorough understanding of both the paper and the calibration landscape. Let me write the final consolidated review.

## Summary

This paper identifies four evaluation blind spots in existing backdoor attacks for object detection (ASR ignoring retained labels in RMA, mAP as a poor proxy for ODA, lack of trigger scale/placement robustness, reliance on curated datasets) and proposes BadDet+, a unified penalty-based attack framework. The core technical contribution is augmenting the detector loss with a log-barrier penalty term that suppresses original-class predictions on trigger-bearing objects, unifying both region misclassification (RMA) and object disappearance (ODA) under a single mechanism. Experiments across COCO, MTSD, and PTSD with FCOS, Faster R-CNN, DINO, and YOLOv5 architectures show that BadDet+ achieves high ASR@50 with drastically reduced TDR in RMA and strong ODA, while data-poisoning-only baselines fail even at high poisoning rates.

## Strengths

1. **Log-barrier penalty unifies RMA and ODA under a single loss term.** Section 4 formulates both attack types as suppressing the original-class logit for trigger-bearing objects, with ODA as the special case where the target is the background class. Tables 1–4 empirically confirm that the same penalty achieves high ASR@50 for both settings across architectures. This is technically clean and non-trivial.

2. **The TDR metric exposes a genuine failure mode that ASR alone misses, and BadDet+ nearly eliminates it.** Section 5.2 defines TDR, and Table 2 shows that on COCO, BadDet+ reduces TDR@50 to 1.54–3.18 across three architectures, whereas BadDet has TDR@50 between 44.74 and 75.94. This demonstrates true class replacement rather than the duplicate detections that plague prior RMA attacks — the paper's single most compelling quantitative result.

3. **Strong synthetic-to-physical transfer on the PTSD real-world benchmark.** Tables 3 and 4 show PTSD results where BadDet+ substantially exceeds baselines: for ODA (Table 3), BadDet+ achieves ASR@50 of 59.59–85.16 on PTSD (Fixed) versus 15.22–54.87 for Morph and 0.53–38.05 for UBA. This real-world validation is a significant strength that goes beyond typical synthetic-only evaluation.

4. **Systematic diagnosis of evaluation blind spots in prior object-detection backdoor research.** Section 3 itemizes and provides concrete failure examples (Figure 1a–e) for each limitation: ASR ignoring retained labels, mAP as a proxy for ODA, lack of trigger scaling/placement robustness, and dependence on curated datasets. This diagnostic analysis grounds the paper's methodological contributions and is not merely generic criticism.

5. **Empirical demonstration that data-poisoning alone is insufficient.** Figure 3 shows that increasing the poisoning ratio of existing attacks to 100% still produces failure cases — for ODA, UBA points drift to bottom-right (low mAP ratio, moderate ASR); for RMA, BadDet shows residual TDR@50 even at 100% poisoning. This convincingly motivates the need for training-time loss manipulation.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Threat-model dimension not flagged in results tables.** BadDet+ assumes the attacker can manipulate the training loss function (adding a penalty term), while baselines (BadDet, UBA, Align, Morph) are pure data-poisoning attacks that only modify training data. The paper acknowledges this distinction in Section 4 ("Compared to related existing work, our design assumes a stronger adversarial setting") and in Section 5.3/Conclusion. However, Tables 1–4 present the comparison without a column or header row clearly separating methods by attacker capability. Adding a simple row like "Attacker capability: Data poisoning vs. Training loss control" would prevent readers from interpreting the comparison as apples-to-apples. This does not invalidate the method (the paper transparently discusses the distinction in text, and Figure 3 explicitly motivates why the stronger threat model is needed), but it would improve clarity.

2. **No variance reporting for main results.** Tables 1–4 and the poisoning-ratio experiments (Figure 3) report single runs without variance. Given that some mAP differences between methods are small (e.g., FCOS mAP of 56.43 vs. 56.94 for BadDet+ vs. Morph on MTSD Fixed), it is impossible to assess statistical significance. The defense experiments (Figure 2) do report multiple runs, which is good. Reporting results across 3 seeds for the main configurations would substantially strengthen confidence in the conclusions.

3. **YOLO failure case not deeply analyzed.** The paper notes that BadDet+ underperforms BadDet on YOLO RMA (Table 4) and attributes this to λ=0.001 being effectively near-zero, concluding that "λ=0 is optimal for this architecture." This is acknowledged but not analyzed — is the issue YOLO's different loss landscape, its confidence-objectness structure, or something else? A brief analysis would deepen the contribution.

4. **No discussion of potential false positives from the penalty.** The penalty term suppresses original-class predictions on any prediction with high IoU to a triggered ground-truth box. Could it ever suppress predictions on non-triggered objects (e.g., due to spurious high IoU between a prediction and a wrong ground-truth box containing a trigger)? The clean mAP results suggest this is not a practical problem, but a brief discussion would be useful.

### Trivial

- In Table 3, the PTSD rows for BadDet+ show two values separated by a space (e.g., "59.59 62.25") without clear labeling of which column corresponds to which setting (Fixed vs. Rand are labeled in the header but the dual values are ambiguous).
- Figure 3's caption mentions "mAP Ratio vs. Poisoning ratio" but the x-axis of subplot (a) is labeled ASR@50 while subplot (b) is TDR@50, which is slightly confusing given the caption text.

## Nice-to-Haves

- Discussion of whether the log-barrier penalty formulation could be adapted to a data-poisoning-only setting (e.g., via a surrogate loss approximated through data manipulation), even if less effective. This would bridge the threat-model gap.
- Evaluation on a larger variety of trigger types beyond the blue square, since the paper notes in Appendix A.4 that alternative triggers are tested but these results are not visible in the main submission.

## Removed Points

- **"The paper does not verify that the Align Random modification was done faithfully"** — This is speculative. The paper describes the modification in Section 5.1 as a straightforward extension (placing background triggers at random scales) and presents results. There is no evidence of unfaithful implementation.
- **"Missing related works"** — Removed per instructions (cannot verify external knowledge).
- **Reproducibility nitpicks about undisclosed hyperparameters** — Removed per instructions. The paper provides main hyperparameters (λ, poisoning ratio, trigger types, training pipelines).
- **"No analysis of false positives" point from harsh critic** — Actually I kept a softened version as Minor #4, since it's a reasonable but minor concern.
- **Generic strengths** from Strength Finder: "The paper addresses an important problem" — Removed as generic/superficial.
- **"Value to the research community"** — Too generic; merged into specific evidenced strengths.

## Novel Insights

None beyond the paper's own contributions. The two novel perspectives that do emerge from the reviews are (a) the paper's diagnosis of evaluation blind spots may be at least as valuable as the method itself — the Section 3 analysis could influence how future object-detection backdoor papers design their evaluation protocols; and (b) the TDR metric and the demonstration that duplicate detections are the dominant failure mode in prior RMA methods reframes the problem from "can we achieve high ASR" to "can we achieve true class replacement."

## Suggestions

1. Add a row or annotation to Tables 1–4 indicating attacker capability (training-loss control vs. data-poisoning-only) to prevent misinterpretation of the comparison.
2. Report main results across 3 random seeds, showing mean and standard deviation.
3. Add a brief analysis (even 2–3 sentences) of why YOLO is resistant to the log-barrier penalty, potentially connecting to its architecture-specific loss structure.
4. Clarify the dual values in the PTSD rows of Table 3 (e.g., label them as "Fixed" and "Rand" directly in the BadDet+ row).

## Score and Decision

**Calibration Report:**

**Round 1 (Bracketing):** Three queries for "backdoor attack object detection" with bands (-1, 3.5), (3.5, 7.5), (7.5, 11). Low band returned papers averaging 2.50–3.00 (rejects/withdrawn). Middle band returned papers averaging 4.25–7.33. High band returned papers averaging 7.60–8.00 (oral/spotlight, but on unrelated topics — dataset bias, watermarking, contrastive learning). **Initial bracket: 6.0–7.5.**

**Round 2 (Narrowing):** Queried for "backdoor attack unified framework object detection training-time penalty" (5.5–7.5), "backdoor attack object detection comprehensive evaluation benchmark" (5.5–7.5), and "backdoor attack novel method systematic evaluation" (6.5–8.5).

Key anchors read in full:

- **Poisoned Forgery Face (7.33, spotlight accept)** — Clean-label backdoor on face forgery detection. Comparable structure (novel method for underexplored task, comprehensive experiments). That paper had apples-to-apples threat-model comparisons. BadDet+ is slightly weaker due to presentation issues around the threat-model axis in tables.
- **Influencer Backdoor Attack (7.50, spotlight accept)** — Backdoor on semantic segmentation. Similar scope (first systematic backdoor on a dense prediction task). That paper lacked real-world physical validation (a noted weakness), while BadDet+ provides it via PTSD. BadDet+ is slightly weaker overall due to comparison-framing issues.
- **BaDExpert (6.25, poster accept)** — Backdoor defense. BadDet+ is clearly stronger in novelty and scope.
- **Backdoor Contrastive Learning (5.75, poster accept)** — BadDet+ is clearly stronger — more extensive evaluation, real-world validation, new metric.
- **Towards Faithful XAI Evaluation (6.75, poster accept)** — Mixed reviews (8,8,6,5). BadDet+ is comparable or slightly stronger.
- **Rethinking CNN's Generalization to Backdoor Attack (5.75, poster accept)** — BadDet+ is stronger.

The paper lands between the 6.25 and 7.33 anchors. It is stronger than BaDExpert (6.25) in originality and scope, but below Poisoned Forgery Face (7.33) and Influencer Backdoor Attack (7.50) due to the threat-model presentation issue in tables and lack of variance reporting. The core contribution — diagnosis of evaluation blind spots + a clean unified formulation + strong empirical evidence including real-world transfer — warrants acceptance. The weaknesses are addressable and do not threaten the core claims.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>