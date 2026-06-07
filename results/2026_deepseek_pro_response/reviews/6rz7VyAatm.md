Now I have thorough comparisons. Let me write the final review.

## Summary

This paper introduces BadDet+, a penalty-based framework for backdoor attacks on object detection that unifies region misclassification (RMA) and object disappearance (ODA) attacks. The core technical contribution is a log-barrier penalty term added to the detector training loss that suppresses original-class predictions on trigger-bearing objects. The paper also contributes a diagnostic analysis revealing that standard metrics (ASR, mAP) systematically overstate attack success in prior work, and introduces the True Detection Rate (TDR) as a complementary metric. Experiments span two datasets (COCO, MTSD), four architectures (FCOS, Faster RCNN, DINO, YOLOv5), and include physical-world validation on PTSD, with BadDet+ consistently outperforming prior attacks.

## Strengths

- **Principled diagnosis of prior evaluation failures**: The paper identifies that ASR alone is misleading for RMA — trigger-bearing objects can be detected as both target and original class simultaneously (Figure 1a). Table 2 quantifies this starkly: BadDet achieves 99.45% ASR@50 on FCOS while retaining 75.94% TDR@50, meaning ~76% of poisoned objects are still detected under their correct label. This is a genuine, previously overlooked failure mode with implications for the entire subfield.

- **TDR as a well-motivated and empirically justified complementary metric**: The True Detection Rate fills a critical gap by measuring whether an attack truly replaces detections rather than merely adding target-class detections. BadDet+ drives TDR@50 from BadDet's 44.74–75.94 down to 1.54–3.18 across COCO architectures (Table 2), providing compelling evidence that the penalty genuinely replaces rather than augments detections.

- **Clean, unified formulation grounded in the diagnosis**: The log-barrier penalty (Eq. 1-2) directly addresses the root cause identified in Section 3 — that prior attacks fail because models continue to assign high confidence to the original class on trigger-bearing objects. The formulation is mathematically precise, generalizes across sigmoid-based (Eq. 1) and softmax-based (Eq. 2) detectors, and naturally unifies RMA and ODA by treating background as a target class.

- **Convincing demonstration that data poisoning alone is insufficient**: Figure 3 shows that increasing poisoning ratios of existing attacks to 100% fails to yield strong ASR@50 without severely harming mAP, and residual duplicate detections persist even at full poisoning. This empirical finding directly and effectively motivates the departure from pure data poisoning.

- **Broad and consistent empirical validation**: The evaluation spans four detector architectures, two datasets plus physical validation (PTSD), multiple trigger positions (fixed high/low/both and random), and both ODA and RMA settings. BadDet+ achieves ASR@50 ≥ 96.95% on COCO ODA and ≥ 91.97% on MTSD ODA across all architectures (Tables 1, 3), with consistent improvements over baselines.

- **Substantial physical-world transfer improvement over baselines**: On PTSD, BadDet+ achieves 59.59–85.16% ASR@50 (Fixed), substantially exceeding Morph (7.72–54.87%), UBA (0.53–27.13%), and UBA Box (0.53–70.28%) — demonstrating meaningful progress on synthetic-to-physical generalization.

- **Honest acknowledgment of limitations**: The paper explicitly notes the YOLO RMA underperformance (line 221-222), the threat model escalation, the narrow defense evaluation, and the OGA scope exclusion in the conclusion (Section 6). This forthrightness strengthens the credibility of positive results.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **Architecture-dependent λ sensitivity**: The penalty coefficient differs by three orders of magnitude across architectures (λ=1 for FCOS/Faster RCNN/DINO vs. λ=0.001 for YOLO). The paper acknowledges this and places sensitivity analysis in Appendix A.5, but such extreme variation suggests λ must be carefully tuned per detector — a practical limitation for applying BadDet+ to new architectures. The YOLO RMA case where λ=0 (equivalent to BadDet) outperforms BadDet+ further highlights this sensitivity.

- **Narrow defense evaluation**: The defense study covers only FT and FT-SAM on MTSD using 2–4% clean data. The paper explicitly and honestly scopes this limitation (Section 2.2, line 58; Section 6), so this is a known limitation rather than a hidden flaw. However, a paper claiming to "expose underestimated vulnerabilities" and "establish a stronger benchmark" would be strengthened by broader defense coverage.

- **Physical-transfer gap under-analyzed**: BadDet+ drops from 93.77 ASR@50 (MTSD Fixed) to 59.59 (PTSD Fixed) for FCOS ODA — a 34-point gap. While this is substantially better than baselines (Morph: 13.21→15.22), the paper does not investigate what drives the residual gap (trigger appearance variation, lighting, resolution). Given the safety-critical motivation, understanding this gap would strengthen the practical claims.

### Trivial

- Defense results (Figure 2) are presented as box plots without accompanying numerical tables, making precise quantitative comparison difficult. Mean and standard deviation values would improve interpretability.

- The five contributions listed in the introduction partially overlap (e.g., contribution iii on "ruling out simple fixes" and iv on "data poisoning alone is insufficient" are closely related empirical demonstrations).

## Nice-to-Haves

- An ablation isolating the penalty from data poisoning (penalty-only, poisoning-only, both) would clarify how much each component contributes and whether the penalty alone can induce the backdoor — directly relevant to the threat model discussion.

- A deeper analysis of why YOLO's RMA performance under BadDet+ regresses relative to BadDet (beyond noting λ=0 is optimal) would strengthen the architectural generality claim.

- Including at least one test-time detection defense baseline would broaden the defense picture without requiring a full defense benchmark.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Methodological contribution is a direct translation of the diagnosis with limited depth"** (from Harsh Critic): The simplicity of the log-barrier penalty is arguably a strength — it directly addresses the diagnosed problem and works. The paper does not need to explore alternative penalty forms to make its contribution valid. The diagnosis + well-motivated solution is a sufficient contribution.

- **"Threat model shift is substantial and incompletely examined"** (from Harsh Critic): The paper has an explicit threat model paragraph (Section 4, lines 84-88) justifying the escalation, empirically demonstrates that data poisoning alone is insufficient (Figure 3), and honestly acknowledges this as a limitation in the conclusion. The framing as "under-examined" goes beyond what the paper actually neglects.

- **"Abstract overpromises on theoretical analysis"** (from Harsh Critic): The theoretical analysis is in Appendix A.7, which is stripped. Per instructions, criticisms based on stripped appendix content should not be included.

- **"OGA is out of scope" raised as a weakness** (from Harsh Critic): The paper explicitly scopes OGA out and states existing methods perform well under the new protocol. This is honest scoping, not a weakness.

- **"The five contributions overlap"** treated as major: The overlap between contributions (iii) and (iv) is minor and noted in Trivial.

- **"Requires modifying training loss — what stops more direct approaches?"** (from Harsh Critic): This is speculative and not grounded in a specific verifiable flaw in the paper. The paper justifies its threat model and empirically motivates why data poisoning alone fails.

- **"Defense evaluation should include COCO, pruning, test-time detection"** (from Harsh Critic): The paper explicitly scopes these out and acknowledges the limitation. Demanding full defense coverage for an attack paper is scope creep.

- **"BadDet+ drops from 93.77 to 59.59 — paper downplays this"** (from Harsh Critic): The paper transparently reports these numbers in Table 3. The claim of "downplaying" is not supported — the paper reports the numbers accurately. The gap is noted as a minor weakness above.

- **Strength Finder generic strengths**: All kept strengths are concrete and grounded in specific evidence from the paper. Generic strengths such as "the paper addressed an important problem" were removed.

## Novel Insights

The paper's most genuinely novel insight is the demonstration that ASR and mAP — the standard metrics in object-detection backdoor evaluation — systematically overstate attack success. Specifically, the finding that BadDet achieves 99.45% ASR@50 while retaining 75.94% TDR@50 on FCOS reveals that the field has been measuring the wrong thing: prior attacks succeed at adding target-class detections but fail at suppressing original-class detections, meaning the "backdoor" does not actually replace model behavior. This insight has implications beyond this paper's specific method — it suggests that the entire object-detection backdoor literature needs to adopt TDR as a standard evaluation metric.

## Suggestions

- Provide a numerical table alongside Figure 2 reporting mean ± std of ASR@50 and TDR@50 before and after FT/FT-SAM for each method and architecture.
- Add a brief qualitative analysis of the physical transfer gap — even a few examples showing what kinds of trigger degradations cause failures would strengthen the practical narrative.
- Consider an ablation experiment isolating the penalty term from data poisoning to strengthen the threat model justification.

## Anchor Comparison

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| LeBD (7vKWg2Vdrs) | 3.25 | R1 weak | Our paper is substantially stronger — broader scope, better evaluation, clearer contribution |
| VSSC (H6XiAoyugv) | 4.33 | R1 mid | Our paper has much stronger and more consistent empirical results plus diagnostic contribution |
| Backdoor in Seconds (ZyPRwskBli) | 4.75 | R2 | Our paper has broader evaluation and stronger motivation |
| Boosting Backdoor (uDNP1q5aZq) | 5.50 | R2 | Our paper achieves consistently high ASR; that paper often falls below 90% |
| Efficient Backdoor Attacks (vRyp2dhEQp) | 5.75 | R2 | Comparable — our paper has the advantage of diagnostic analysis, TDR metric, and physical-world validation |
| BaDExpert (s56xikpD92) | 6.25 | R2 | Comparable — both well-executed with strong methodology and evaluation; ours is attack, theirs is defense |
| VLOOD (tZozeR3VV7) | 6.33 | R1 mid | Comparable — similar level of contribution and evaluation quality |

**Bracket**: Round 1 placed the paper between ~4.5 and ~6.5. Round 2 narrowed to 5.5–6.5 by comparison against Efficient Backdoor Attacks (5.75), BaDExpert (6.25), and VLOOD (6.33). The paper is stronger than the 5.50–5.75 anchors due to its diagnostic contribution and comprehensive evaluation, and comparable to the 6.25–6.33 anchors. Final score: **6.0**.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>