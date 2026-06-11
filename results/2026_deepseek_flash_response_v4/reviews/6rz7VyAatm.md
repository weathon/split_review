Now I have all the calibration data I need. Let me write the final consolidated review.

**Round 1 bracket:** 5.5 – 7.0  
**Round 2 anchors consulted (full reads):** VLOOD (6.33, Accept), Efficient Backdoor Attacks (5.75, Accept), Wicked Oddities (6.00, Accept), Rethinking CNN's Generalization (5.75, Accept), A Change of Heart (5.50, Reject), VSSC Triggers (4.33, Reject). BadDet+ compares favorably to all of these — it has broader architectural/dataset coverage than VLOOD, a more principled method than Efficient Backdoor, and independently valuable diagnostic contributions. The missing hyperparameter reporting (ρ, τ) and asymmetric threat-model comparison keep it below the 7+ range, but neither is fatal. Final score: **6.5**, decision: **Accept**.

---

## Summary

BadDet+ is a backdoor attack framework for object detection that unifies region misclassification (RMA) and object disappearance (ODA) under a single log-barrier penalty formulation. Beyond the new method, the paper contributes a critical diagnostic of evaluation blind spots in prior object-detection backdoor work (ASR ignoring retained labels, mAP as a poor ODA proxy, lack of trigger scaling/placement robustness checks), introduces True Detection Rate (TDR) as a complementary metric, and establishes a more rigorous evaluation protocol. The method is evaluated across 4 architectures (FCOS, Faster RCNN, DINO, YOLOv5m6), 2 datasets (COCO, MTSD), and physical-world transfer (PTSD), consistently outperforming baselines.

## Strengths

- **Log-barrier penalty formulation unifies RMA and ODA under a single mechanism**: Equations (1)–(2) define a penalty that suppresses original-class logits on trigger-bearing objects, with ODA emerging as the special case where the target class is background. This is a principled mathematical unification — prior work treats these as separate attack paradigms — and it is validated across both attack types in Tables 1–4.

- **Introduction of TDR reveals that prior RMA attacks largely fail to replace the original label**: Table 2 shows BadDet achieves high ASR@50 (99.45% on FCOS) but retains TDR@50 = 75.94%, meaning the object is still detected under its true label in most cases. BadDet+ cuts TDR@50 to 2.78% on the same setting. This directly substantiates the claim that ASR alone overstates attack success.

- **Physical-world transfer validated on PTSD, significantly outperforming prior methods**: On PTSD (Tables 3–4), BadDet+ achieves ODA ASR@50 of 59.59–62.25% (FCOS, Fixed) compared to Morph (15.22%), UBA (15.37%), and UBA Box (14.54%). This ~4× improvement provides concrete evidence for the claim of stronger synthetic-to-physical transfer.

- **Systematic evaluation across architectures, datasets, trigger placements, and poisoning ratios**: Evaluation spans 4 architectures, 2 datasets, fixed and random trigger placements, and multiple poisoning ratios. The poisoning-ratio analysis (Fig. 3) shows that data-poisoning-only methods require near-100% poisoning to approach BadDet+'s performance while suffering mAP degradation, whereas BadDet+ at 50% poisoning forms a tighter cluster near ideal performance.

- **Honest documentation of failure modes and scope**: Section 6 explicitly documents that BadDet+ underperforms BadDet on YOLO RMA, that the threat model assumes training-time loss manipulation (stronger than data poisoning alone), and that object-generation attacks are out of scope. This candor strengthens the paper's credibility as a benchmark rather than a one-sided advocacy.

## Weaknesses

### Fatal
None.

### Major

- **Missing core hyperparameters ρ and τ**: Equations (1)–(2) define a log-barrier penalty parameterized by IoU threshold ρ and confidence boundary τ. The paper reports λ values for each architecture (1.0 for FCOS/Faster RCNN/DINO, 0.001 for YOLO) but never states what ρ and τ are set to, how they were chosen, or whether they were tuned per architecture. Since ρ controls which predictions get penalized (only those with high IoU to triggered ground-truth boxes) and τ determines the penalty boundary, these are not minor implementation choices — the method cannot be fully reproduced without them. The sensitivity analysis in Appendix A.5 studies λ but does not mention ρ or τ.

- **Asymmetric threat-model comparison**: BadDet+ assumes training-time loss manipulation (a stronger attacker with access to the training loss), while baselines (BadDet, UBA, Align, Morph) operate under data-poisoning-only — making head-to-head comparisons in Tables 1–4 structurally asymmetric. The paper is transparent about this (lines 84–88) and motivates it via poisoning-ratio experiments (Fig. 3) showing data-poisoning-only approaches are fundamentally limited. However, the reader cannot cleanly attribute the large performance gap (e.g., BadDet+ 96.95% ASR@50 vs. Align's 33.36% in Table 1) to the penalty mechanism versus the expanded control surface. A data-poisoning-only ablation of BadDet+ (trigger + label manipulation without the loss penalty) would disentangle these factors.

### Minor

- **Defense evaluation is narrow**: Only fine-tuning (FT) and FT-SAM are tested, on only 50–100 clean samples (2–4% of MTSD training data) — weak defenses unlikely to erase well-embedded backdoors. The paper is transparent about this scope (line 262), and the defense robustness claim in the abstract is primarily about physical-trigger robustness (well-supported), not defense robustness. But the "robust" framing could imply broader defense robustness than evaluated.

- **No variance/confidence intervals in main results**: Tables 1–4 report single-run results without error bars. The defense evaluation (Fig. 2) uses 10 runs, but the main experimental tables lack any measure of stability across architectures, datasets, or trigger placements.

- **YOLO failure case presented without analysis**: BadDet+ underperforms BadDet on YOLO RMA (Table 4). The paper flags this honestly (line 221, 242) but offers no investigation into why — e.g., whether YOLO's anchor-based design, assignment strategy, or specific loss formulation causes the log-barrier penalty to be ineffective.

- **Theoretical analysis not summarized in main text**: The abstract references a theoretical analysis showing the penalty "acts selectively within a trigger-specific feature subspace," but this analysis resides entirely in Appendix A.7 (stripped by the parser). If substantive, it deserves at least a paragraph in the main paper; if secondary, the abstract overstates it.

### Trivial
None.

## Nice-to-Haves

- A brief discussion or ablation of trigger size/visibility (currently only a blue square is used) would help calibrate the reader's assessment of the threat level.
- Reporting what fraction of the 10 defense runs the backdoor survives, rather than only showing box-plot aggregates, would increase the informativeness of the defense evaluation.

## Removed Points

- **Trigger visibility concern** ("if the trigger is highly visible, this could inflate attack success"): speculative; the paper uses a standard blue square trigger common in the backdoor literature, and no evidence is presented that visibility inflates results. Removed per filtering rule against speculation.
- **Missing related work**: not included (cannot verify externally).
- **Formatting/typo concerns**: parser artifacts, not author errors.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Report ρ and τ values** and include a brief sensitivity analysis (similar to the existing λ study in Appendix A.5). These are core hyperparameters and the paper cannot be reproduced without them.
2. **Add a data-poisoning-only ablation** of BadDet+ (trigger + label manipulation without the loss penalty) to disentangle the effect of the penalty mechanism from the expanded threat model.
3. **Add variance/confidence intervals** to main result tables (e.g., across random seeds or data subsets).
4. **Include a brief paragraph in the main text** summarizing the theoretical analysis from Appendix A.7, or temper the abstract's reference to it.

## Score and Decision

**Calibration anchors (all rounds):**

| Paper | Avg Score | Round | Comparison to BadDet+ |
|---|---|---|---|
| VLOOD (tZozeR3VV7) | 6.33 | R1, R2 | Weaker evaluation breadth, less principled method |
| Efficient Backdoor Attacks (vRyp2dhEQp) | 5.75 | R1, R2 | Weaker method rationale, narrower evaluation |
| Wicked Oddities (1Z3C49JQVf) | 6.00 | R2 | Limited to CIFAR-10/GTSRB, less novel method |
| Rethinking CNN's Generalization (mYhH0CDFFa) | 5.75 | R2 | Narrower scope, less comprehensive evaluation |
| A Change of Heart (Gf4KZIqLHD) | 5.50 | R2 | Impractical threat model, visible artifacts |
| VSSC Triggers (H6XiAoyugv) | 4.33 | R1 | Marginal gains over baselines, insufficient depth |
| CLIP Backdoors (Ud7I21wHnl) | 5.25 | R1 | Limited novelty, mainly empirical analysis |
| LeBD (7vKWg2Vdrs) | 3.25 | R1 | Much weaker — defense paper with low scores |

**Round 1 bracket:** 5.5 – 7.0  
**Round 2 narrowing:** Compared against VLOOD (6.33) as the closest anchor; BadDet+ has broader evaluation (4 architectures, 2 datasets, physical transfer) and independently valuable diagnostic contributions (Section 3, TDR). The missing hyperparameter reporting (ρ, τ) and asymmetric threat-model comparison prevent it from reaching the 7+ range but do not undermine the core contributions. **Final score: 6.5, Decision: Accept.**

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>