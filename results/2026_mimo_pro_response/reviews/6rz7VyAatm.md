## Summary
This paper introduces BadDet+, a penalty-based backdoor attack framework for object detection that unifies region misclassification attacks (RMA) and object disappearance attacks (ODA) through a log-barrier penalty on original-class logits. It also identifies evaluation blind spots in prior OD backdoor work (duplicate detections inflating ASR, mAP as a poor ODA proxy, trigger scale sensitivity), introduces the TDR metric, and conducts extensive experiments across four architectures, two datasets, physical-world validation, multiple trigger configurations, poisoning ratio sweeps, and defense evaluation.

## Strengths
- **Exposes critical evaluation flaws in prior work with empirical backing**: Section 3 identifies four specific blind spots in existing OD backdoor evaluations (reliance on ASR alone for RMA, mAP as ODA proxy, trigger scaling/placement, curated dataset dependence) supported by concrete examples (Figure 1). The TDR metric reveals that BadDet's 99.45 ASR@50 on FCOS (Table 2) masks a 75.94 TDR@50 — the original class is still detected three-quarters of the time. This diagnostic work has standalone value regardless of the proposed method.
- **Unified log-barrier penalty formulation (Eqs. 1-2) treating ODA as RMA with background as target**: By penalizing original-class logits above confidence boundary τ on trigger-bearing predictions, the model is pushed to either redirect to a target class (RMA) or to background (ODA). The softmax-compatible variant (Eq. 2) extends this to Faster RCNN. A single mechanism works across four architectures (FCOS, Faster RCNN, DINO, YOLO).
- **Consistently strong ASR across datasets, architectures, and trigger placements**: BadDet+ achieves worst-case ASR@50 of 96.46 for ODA and 97.27 for RMA on COCO (Tables 1-2). On MTSD (Tables 3-4), ASR@50 ranges 83.68–97.75 for ODA and 87.04–97.04 for RMA across four architectures with both fixed and random triggers. Prior methods show large fixed/random gaps (e.g., Align Random on DINO drops from 79.92 to 33.36, Table 1).
- **Superior synthetic-to-physical transfer on PTSD**: BadDet+ achieves 59.59–85.16 ASR@50 on PTSD for ODA (Table 3), substantially outperforming Morph (7.72–54.87) and UBA (0.53–38.05). For RMA (Table 4), BadDet+ outperforms baselines on PTSD TDR in 3 of 4 architectures.
- **Demonstration that data poisoning alone is insufficient**: Figure 3 and Section 5.3 show that increasing poisoning ratios for UBA/UBA Box produces only modest ASR gains while degrading mAP. For BadDet, FCOS and Faster R-CNN still exhibit residual duplicate detections at 100% poisoning. This provides concrete evidence motivating the stronger threat model.
- **Fair comparison with naive baseline fixes**: UBA Box and Align Random (Section 5.1) test whether simple modifications close the gap — they do not, ruling out easy fixes.
- **Thorough defense evaluation with distributions**: Figure 2 evaluates FT and FT-SAM with 10 random runs each at 2% and 4% clean data, reporting full distributions. BadDet+ sustains ASR@50 above 0.4 in most ODA cases after defense.

## Weaknesses

### Fatal
None.

### Major
- **Physical-world TDR@50 for RMA is substantially higher than synthetic results, and this gap is under-discussed**: On MTSD, BadDet+ TDR@50 ranges 2.00–7.54 (Table 4), but on PTSD it jumps to 18.53–44.41 — a 3–7× increase. For FCOS, nearly half (44.41%) of poisoned objects retain their original class even with the trigger present in the physical world. The conclusion states BadDet+ "markedly reduces TDR@50" without qualifying that this primarily holds on synthetic data while physical-world RMA TDR remains substantial. BadDet+ still outperforms baselines on PTSD TDR in most cases (e.g., FCOS: 44.41 vs BadDet's 81.24), so the contribution is not invalidated, but the paper's narrative overstates the headline finding by not honestly characterizing this gap. The discussion after Table 4 says "BadDet+ reduces TDR@50" without noting that PTSD TDR is 4–7× higher than MTSD TDR.

### Minor
- **Threat model asymmetry not consistently flagged in results tables**: BadDet+ modifies the training loss (stronger attack surface) while all baselines use data poisoning only. The paper acknowledges this in Section 4 ("our design assumes a stronger adversarial setting") and justifies it with poisoning ratio experiments (Section 5.3, Fig. 3). However, Tables 1–4 present results side-by-side without footnotes distinguishing loss-level from data-only methods. Even a simple footnote per table would improve clarity.
- **No ablation of the log-barrier penalty against alternative formulations**: The paper presents the log-barrier as a single design choice. An ablation comparing it against simpler alternatives (e.g., hinge penalty, direct cross-entropy suppression) would strengthen the claim that the specific formulation matters, not just the idea of penalizing original-class logits.
- **Main results (Tables 1–4) report single numbers without variance**: Given stochastic neural network training, even 2–3 seeds would add credibility, particularly for the YOLO results where BadDet+ underperforms BadDet.

### Trivial
None.

## Nice-to-Haves
- An ablation comparing the log-barrier penalty against 1–2 simpler penalty alternatives to validate the specific formulation choice.
- Discussion of why the physical-world TDR gap is so large (domain shift in trigger appearance, feature space differences) and what this means for practical attack reliability.
- Extension of defense evaluation beyond FT/FT-SAM to pruning or test-time detection methods, as explicitly scoped out in Section 2.2.

## Removed Points
These points are flagged to be removed, treat them with caution:
- **Table 3 formatting issues** raised by harsh critic: This is a parser artifact, not a paper problem. The underlying table structure with Fixed/Rand columns is clear in the original.
- **Reproducibility concerns**: The paper includes code with the submission and commits to releasing it upon acceptance. Hyperparameters (λ values, IoU thresholds, poisoning ratios) are specified.

## Novel Insights
The paper's most novel insight is the demonstration that data poisoning alone is fundamentally insufficient for reliable backdoors in object detection (Fig. 3, Section 5.3) — even at 100% poisoning ratio, data-only methods fail to achieve consistent behavior while degrading clean performance. This finding, combined with the four identified evaluation blind spots and the TDR metric, provides a genuinely useful methodological correction to the subfield. The unification of ODA as RMA with background as target class is a clean conceptual contribution that leverages detector architecture rather than fighting it.

## Suggestions
- Add a brief discussion after Table 4 explicitly comparing MTSD and PTSD TDR@50 values for RMA, acknowledging the physical-world gap and discussing possible causes.
- Add footnotes to Tables 1–4 indicating which methods have loss-level vs. data-only access to training.
- Consider a brief ablation with at least one alternative penalty (e.g., hinge loss) to validate the log-barrier choice.

## Calibration Anchors
| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| 7vKWg2Vdrs (LeBD) | 3.25 | R1 | Narrow defense for YOLO only, limited novelty. BadDet+ far exceeds. |
| 66e22qCU5i (Certified Copy) | 3.00 | R1 | Resistant backdoor, narrow scope. BadDet+ far exceeds. |
| H6XiAoyugv (VSSC Triggers) | 4.33 | R1 | Novel trigger design but evaluation doesn't support claims. BadDet+ has stronger evidence. |
| ZyPRwskBli (Backdoor in Seconds) | 4.75 | R1 | Model editing backdoor, less thorough evaluation. BadDet+ better. |
| LsTIW9VAF7 (GCB) | 5.80 | R1 | Clean-image backdoor, reviewers found limited novelty. BadDet+ has more distinct contributions. |
| 1Z3C49JQVf (Wicked Oddities) | 6.00 | R1 | Selective poisoning, only 2 datasets. BadDet+ more comprehensive. |
| vRyp2dhEQp (Efficient Backdoor) | 5.75 | R1 | Data-constrained attacks, some novelty concerns. BadDet+ has stronger evaluation. |
| tZozeR3VV7 (VLOOD) | 6.33 | R1 | VLM backdoor with OOD data, narrower evaluation. BadDet+ more thorough. |
| SctfBCLmWo (A Decade's Battle) | 8.00 | R1 | Dataset bias, different topic. Scored high for clean methodology; BadDet+ doesn't reach this level. |

**Round 1 bracket: 6.5–7.5.** BadDet+ clearly exceeds rejected backdoor papers (3.0–4.75) and is more comprehensive than accepted ones (5.75–6.33). It doesn't reach 8.0 level due to the physical-world TDR gap and threat model asymmetry concerns. The paper makes multiple genuine contributions (evaluation critique, TDR, unified formulation) with unusually thorough evaluation (4 architectures, 2 datasets, physical world, trigger variations, poisoning ratio sweeps, defense), firmly placing it above the 6.0–6.33 accepted anchors. Final score: 7.0.

MY FINAL SCORE: <score>7</score>
MY FINAL DECISION: <decision>Accept</decision>