Now let me write the final consolidated review.

## Summary

This paper diagnoses evaluation blind spots in prior object-detection backdoor attacks (e.g., ASR ignoring retained labels in RMA, mAP as a poor proxy for ODA) and proposes BadDet+, a penalty-based framework that unifies region misclassification (RMA) and object disappearance (ODA) attacks under a single log-barrier penalty that suppresses true-class predictions for trigger-bearing objects. The key empirical contributions are: (i) the True Detection Rate (TDR) metric that reveals that prior RMA attacks produce massive duplicate detections (TDR 44–76% on COCO), while BadDet+ reduces this to below 3.2%; (ii) strong physical-world transfer on the PTSD benchmark; and (iii) resilience to fine-tuning defenses.

## Strengths

1. **Rigorous diagnosis of previously overlooked evaluation blind spots.** Section 3 systematically identifies four critical flaws in prior work: (i) ASR ignores retained original-class detections in RMA, (ii) mAP is a poor proxy for ODA success (confounded by phantom boxes and duplicate detections), (iii) trigger scale and placement robustness is never tested, and (iv) some attacks depend on unrealistic dataset assumptions. This analysis is a standalone methodological contribution that the community should adopt regardless of the specific attack method.

2. **Demonstrably superior RMA performance via the TDR metric.** The True Detection Rate (TDR) is a well-motivated metric that directly measures whether an RMA attack *replaces* a detection or merely *adds* a target-class detection. On COCO (Table 2), BadDet+ achieves ASR@50 ≥ 97.3% while reducing TDR@50 to 1.54–3.18% across FCOS, Faster R-CNN, and DINO — compared to BadDet's 44–76% TDR. This is striking quantitative evidence that the penalty mechanism suppresses true-class predictions rather than producing spurious duplicate detections.

3. **Strong physical-world validation and broad experimental scope.** The paper evaluates across two datasets (COCO, MTSD), four architectures (FCOS, Faster R-CNN, DINO, YOLOv5), multiple trigger positions, and physical-world transfer (PTSD). The PTSD results (Tables 3–4) show BadDet+ achieving synthetic-to-physical transfer as high as 85% ASR@50 (DINO ODA), substantially outperforming all baselines. This goes well beyond the typical digital-only evaluation in prior backdoor work.

## Weaknesses

### Major

1. **Training procedure is underspecified — labels may or may not be changed.** The paper states that BadDet+ "goes beyond prior approaches... which modify only the training data (e.g., removing or relabeling ground-truth boxes)" by introducing a penalty (Section 4). For RMA, the penalty suppresses original-class logits, but the paper claims "the standard classification objective then naturally steers the model towards... predicting the attacker's target class." For this to work, either (a) ground-truth labels must be changed to the target class (contradicting the "no data modification" framing), or (b) the penalty alone must somehow redirect predictions, which is not how sigmoid-based classification losses function — they provide positive signal only for the labeled class. The paper never resolves this ambiguity. If labels are changed (the most plausible interpretation), BadDet+ is a *combination* of data poisoning and loss manipulation, and the description should say so explicitly. This underspecification impairs reproducibility and obscures the actual mechanism.

2. **ODA evaluation metric is a proxy measure, inconsistent with the paper's own critique.** The paper defines ODA ASR as "the proportion of these objects for which the original class y_i is not detected" (Section 5.2). The attacker's goal in ODA is for the object to *disappear entirely* from detection. A detection under a wrong class would count as "success" under this metric while the object has not actually vanished. This is precisely the kind of proxy-measure issue that Section 3 criticizes in prior work (critiquing mAP as a proxy for ODA). The paper does not verify whether BadDet+ produces phantom boxes under wrong classes — a failure mode it documents for UBA (Figure 1b,c). This inconsistency weakens the ODA claims in Tables 1 and 3.

### Minor

3. **Unequal threat-model comparisons weaken attribution.** BadDet+ controls the training loss (stronger threat model), while all baselines (BadDet, UBA, Align, Morph) are data-poisoning only. The paper acknowledges this asymmetry, but still presents head-to-head comparisons as evidence of BadDet+'s superiority. An ablation equipping baselines with the same penalty (or removing the penalty from BadDet+) would isolate whether the specific penalty design — rather than generic loss-level control — drives the improvement. Without this, the gains could largely reflect the asymmetry.

4. **Limited defense evaluation.** The defense study tests only fine-tuning and FT-SAM. The only detection-specific mitigation (Zhang et al. 2024b) is excluded because it is "architecture-specific," yet Faster R-CNN (one of the architectures studied) is compatible with it. Including it would have strengthened the paper's argument that detection-specific defenses are necessary. The paper acknowledges this limitation but the claim about defense necessity remains partly unsupported.

5. **Position- and scale-"invariant" claim is overstated.** The abstract lists "position- and scale-invariant behavior" as a key advantage, but the experiments cover three fixed positions + one random condition on MTSD and centered placement only on COCO. This limited set does not support the strong term "invariant." The results do show BadDet+ is more stable than baselines across the tested conditions, which is a valid finding, but the claim should be toned down.

### Trivial

6. **No variance reporting in main tables.** Tables 1–4 report single runs without confidence intervals. Given the stochastic nature of detector training, variance over at least 3 seeds would strengthen the reliability of comparative claims.

## Nice-to-Haves

- An ablation that compares (a) BadDet+ with full penalty + data modification vs. (b) data modification only vs. (c) penalty only (if feasible), to directly isolate the penalty's contribution.
- A qualitative or quantitative check for phantom boxes in BadDet+ ODA detections (e.g., checking whether any non-background detection at >0.5 IoU exists for poisoned objects).
- Continuous position/scale sensitivity plots (e.g., ASR as a function of trigger offset from box center) to support the "invariant" claim more rigorously.

## Removed Points

- **Critic's claim that comparisons under unequal threat models are invalid** — The paper clearly acknowledges the asymmetry and justifies it by showing data-poisoning alone is unreliable. The comparisons still provide information about what different threat models achieve. However, the attribution of gains specifically to the penalty design (vs. generic loss control) is weakened, so I moved this to Minor rather than removing entirely.
- **Critic's request to test Zhang et al. 2024b defense** — This is scope-expansion; the paper explicitly scopes out architecture-specific defenses and acknowledges the limitation in the conclusion. Kept as a Minor suggestion rather than a Major gap.
- **Strength Finder's claim about "strong empirical validation of defense resilience"** — The defense results (Figure 2) show RMA ASR often drops substantially after defense; the claim overstates the resilience. Demoted from a core strength.
- **Complaints about missing appendix content or single-run evaluations** — The paper already studies λ sensitivity and poisoning ratio variations (Appendix A.3, A.5). Single runs without variance is common practice in this sub-field for large-scale detection training.

## Novel Insights

The paper's most novel insight, not fully articulated by either the strengths or criticisms, is that the RMA failure mode of existing attacks is *qualitatively different* from what was previously assumed. Prior work implicitly treated RMA as a classification problem (does the target class get predicted?), but the paper reveals it is actually a *competition* between the original-class and target-class logits — both can fire simultaneously, and the original-class prediction is the harder one to suppress. This reframing (attack success = suppressing the correct class, not just activating the target) is what motivates the log-barrier penalty and explains why data-poisoning-only approaches inevitably produce high TDR. The penalty is not adding new capability; it is targeting the *right* optimization objective that prior work missed. This is a useful conceptual contribution that extends beyond the specific attack method.

## Suggestions

1. **Explicitly specify the training pipeline:** State plainly whether ground-truth labels are changed to the target class for RMA and whether poisoned boxes are removed for ODA. A simple bullet list of "data modifications performed" + "loss modifications performed" would resolve the ambiguity.
2. **Fix the ODA metric or add a complementary check:** Either report ASR as "no detection of any class at IoU > 0.5" (true disappearance), or at minimum include a qualitative analysis table showing how often BadDet+ produces phantom boxes under wrong classes for ODA.
3. **Add an ablation that removes the penalty:** Compare BadDet+ (penalty + standard data modifications) vs. using only the same data modifications (without penalty) to quantify the penalty's contribution beyond the threat-model asymmetry. Even showing a single architecture-dataset pair would substantially strengthen the attribution.
4. **Tone down the "invariant" language:** Replace "position- and scale-invariant" with "more robust to trigger-position and scale variation than prior methods" or similar.

## Score and Decision

**MY FINAL SCORE: <score>5.0</score>**
**MY FINAL DECISION: <decision>Reject</decision>**

**Calibration anchors used:**
| Anchor | Score | Round/Query | Comparison to current paper |
|--------|-------|-------------|------------------------------|
| 7vKWg2Vdrs (LeBD) | 3.25 | R1-topic-low | Much weaker — limited to YOLO-only defense, straightforward CAM extension |
| 66e22qCU5i (Certified Copy) | 3.00 | R1-topic-low | Much weaker — limited novelty, old baselines, small datasets |
| S5JCqTJyKj (Deferred Backdoor) | 3.00 | R1-topic-low | Not object-detection specific; weaker evaluation |
| H6XiAoyugv (VSSC Triggers) | 4.33 | R1-topic-mid | Weaker — marginal gains over baselines, unclear advantage |
| ZyPRwskBli (Backdoor in Seconds) | 4.75 | R1-topic-mid | Different direction (model editing); similar quality tier |
| Ud7I21wHnl (CLIP Backdoor) | 5.25 | R1-topic-mid | Similar quality — empirical study of CLIP backdoors, well-executed |
| tZozeR3VV7 (VLOOD) | 6.33 | R1-topic-mid | Stronger — novel OOD setting, cleaner evaluation, accepted |
| vRyp2dhEQp (Efficient Backdoor) | 5.75 | R2-narrow | Similar quality — novel CLIP approach, practical scenario, accepted |
| 9rtlfjWMXI (PADetBench) | 4.75 | R2-narrow | Similar quality — comprehensive benchmark but lacks insights |
| NI0RsRuFsW (Evasive Trojans) | 4.00 | R1-weakness-metric | Different topic; weaker — incremental, small datasets |
| MLShfiJ3CB (Reliable Backdoor ViT) | 4.50 | R1-weakness-ablation | Different topic; similar quality tier |

**Bracket and narrowing:** Round 1 placed the paper between 4.0 and 6.0 based on comparison with low-band (3.0–3.25) and mid-band (4.33–6.33) topic anchors plus weakness-anchored queries (3.0–5.25). Round 2 retrieved anchors in the 4.25–5.75 range, confirming the bracket. The paper's contributions (evaluation diagnosis, TDR metric, strong RMA results, physical-world validation) are clearly above the low-band papers, but the training-procedure underspecification and ODA metric issue are meaningful weaknesses that none of the mid-band Accept papers share at the same severity. Score 5.0 reflects a paper with genuine contributions that needs nontrivial revisions before acceptance.