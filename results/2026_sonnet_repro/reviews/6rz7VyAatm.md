Now let me run calibration search to score this paper properly.**Round 1 Bracket: 5.0 – 6.5.** The paper is clearly above the weak reject band (avg ~3.0–3.25), which featured papers with fundamental flaws. The paper has real contributions (new evaluation metrics, physical validation, clean formulation), but is constrained by the threat model asymmetry and YOLO failure. It sits below the strong-accept band (~8.0). Let me narrow within 5–6.5.Now I have sufficient calibration data. Let me write the final consolidated review.

---

## Summary

BadDet+ is a unified backdoor attack framework for object detection that introduces a log-barrier penalty to suppress original-class confidence on trigger-bearing objects, unifying region misclassification attacks (RMA) and object disappearance attacks (ODA) under a single mechanism. Beyond proposing the attack itself, the paper makes a significant diagnostic contribution by identifying and formalizing evaluation blind spots in prior work — specifically, that ASR alone in RMA fails to capture retained true-class detections (motivating the new TDR metric), and that mAP is a poor proxy for ODA success. Experiments span COCO and MTSD/PTSD datasets across four architectures (FCOS, Faster RCNN, DINO, YOLOv5), with physical-world validation on the PTSD benchmark.

---

## Strengths

- **Well-motivated evaluation critique with concretely introduced metrics.** Section 3 precisely identifies (with Figure 1) how BadDet RMA produces dual detections that inflate ASR, and how UBA ODA's phantom boxes depress mAP for reasons unrelated to object disappearance. The proposed True Detection Rate (TDR) and instance-level ASR directly address these issues and are validated throughout Tables 1–4 — these are immediate contributions to the community regardless of BadDet+.

- **Clean, architecturally general penalty formulation.** Equations 1 and 2 instantiate a softplus/log-barrier that acts as a penalty wall above a confidence threshold τ, with a softmax-compatible variant for Faster RCNN. The design rationale is well articulated: the attack need only suppress original-class logits, then the standard classification loss redirects predictions to background (ODA) or target class (RMA). This unification is intellectually clean and directly verified: on COCO, ODA ASR@50 reaches 96.95–98.46% (Table 1) while RMA TDR@50 drops to ≤3.18% (Table 2), compared to 28–97% for baselines on ODA and 44–76% TDR for BadDet on RMA.

- **Genuine physical-world validation.** The paper evaluates on PTSD (a physical traffic-sign dataset), showing BadDet+ achieves ODA ASR@50 up to 85.16% and RMA ASR@50 up to 89.80% on PTSD across architectures, versus ≤50–55% for competing methods (Tables 3–4). This is a direct response to Doan et al. (2024)'s finding that synthetic-trigger attacks fail in the physical world.

- **Empirical evidence that data-poisoning alone is insufficient.** Figure 3 shows that increasing poisoning ratio for UBA and BadDet either fails to improve ASR@50 without crippling mAP (ODA), or still leaves residual duplicate detections (RMA), motivating the stronger threat model. This is not just claimed — it is demonstrated with a sweep from 10% to 100% poisoning across four architectures.

---

## Weaknesses

### Fatal
None.

### Major

- **Threat model asymmetry is unaccompanied by an ablation of the log-barrier form.** BadDet+ augments training with a loss penalty, placing it in a strictly stronger threat model than the data-poisoning-only baselines (BadDet, UBA, Align). The paper acknowledges this explicitly in Section 4: *"Compared to related existing work, our design assumes a stronger adversarial setting in which the training process can be controlled."* However, there is no comparison against a simpler training-loss baseline (e.g., a standard cross-entropy push toward the target class or a simple sigmoid penalty), so readers cannot determine whether the log-barrier form specifically contributes the observed improvements, or whether *any* training-loss modification over data-poisoning baselines would yield similar gains. This gap means the methodological contribution of the log-barrier design is not clearly isolated from the threat-model advantage. A direct ablation comparing log-barrier against a simpler penalty under the same training-manipulation threat model would resolve this.

- **YOLOv5 underperformance undermines the claimed architectural generality.** Table 4 shows that on YOLOv5 RMA, BadDet outperforms BadDet+ in both ASR@50 (96.57% vs 91.97% Fixed) and TDR@50 (3.14% vs 7.54% Fixed), with the paper itself stating: *"indicating that λ=0 is optimal for this architecture."* This is a substantive failure of the method on one of four tested architectures — not a fringe edge case, since YOLO-family detectors are among the most widely deployed in safety-critical settings (the paper's stated motivation). The paper defers investigation to Appendix A.8 and characterizes it as warranting "further investigation," but given that four architectures are the entire scope of evaluation, this failure is material. The paper's conclusion that BadDet+ establishes "a strong and representative benchmark" requires a principled account of when the penalty helps and when it does not.

### Minor

- **No variance reported in main result tables.** Tables 1–4 report single-run point estimates, while Figure 2 (defense evaluation) explicitly uses boxplots across 10 random seeds. The spread visible in Fig. 2 suggests that single-point main-table values — especially for TDR@50 under threshold-sensitive conditions — may not be representative. Reporting mean ± std across 2–3 training seeds for key entries would improve confidence in the conclusions.

- **Synthetic-to-physical degradation gap is underanalyzed.** For FCOS ODA, ASR@50 drops from 93.77% on MTSD to 59.59% on PTSD — a 34-point gap. The paper frames its PTSD results as "stronger transfer than prior work," which is accurate, but the absolute magnitude of the gap is non-trivial and deserves more than the current passing treatment. Breakdown by trigger position, sign category, or lighting condition would directly advance the paper's claim about physical-world validity.

### Trivial
None that are verified and not already stripped.

---

## Nice-to-Haves

- **λ sensitivity discussion in the main text.** The paper notes that λ=1 is used for FCOS/Faster RCNN/DINO and λ=0.001 for YOLO, with a sensitivity study deferred to Appendix A.5. Given that the optimal λ differs by three orders of magnitude across architectures, a brief summary of what λ-selection entails in practice would help practitioners understand the tuning overhead.

- **Broader defense evaluation.** The paper explicitly scopes out pruning, test-time detectors, and input-space defenses, which is reasonable. However, testing fine-tuning with larger clean data budgets (beyond 4% / 100 samples) would strengthen the robustness claim — the current defense experiments use only 2–4% of MTSD, which is a narrow operating range.

- **Simpler penalty ablation as a nice-to-have.** If the stronger comparison baseline (standard CE push under training manipulation) showed significantly worse performance than the log-barrier, this would provide concrete evidence for the specific log-barrier design choice, moving the key finding from "threat-model-assisted" to "design-validated."

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"The paper defers explanation to Appendix A.8 as if the appendix doesn't exist":** The harsh critic implied the YOLO failure should be fully resolved in the main text rather than an appendix. The paper's conclusion does acknowledge YOLO as a limitation. The criticism that moving discussion to an appendix is a flaw is removed (appended discussion exists in the original submission).

- **"Section 5.3's poisoning-ratio sweep is circular":** The harsh critic argued that showing data-poisoning alone fails is "what motivates the stronger threat model rather than a fair head-to-head." This is actually the *correct* use of the sweep — it empirically validates the paper's motivation for the stronger threat model, not a post-hoc rationalization. Removed as mischaracterized.

- **Missing variance in defense evaluation as a major flaw:** Fig. 2 explicitly uses boxplots across 10 seeds for defense results. The main tables not having CIs is common in this field at scale. Demoted to minor; not a major issue.

- **"Whether the log-barrier assumption holds uniformly across anchor-free vs. anchor-based detectors was not analyzed":** The paper does address both anchor-free (FCOS) and anchor-based (Faster RCNN) detectors in Tables 1–4 empirically. The theoretical analysis in Appendix A.7 is referenced. The YOLO failure is already captured under the Major weakness above; adding a separate criticism about assignment mechanism analysis would be redundant.

- **Defense evaluation scope labeled as a weakness:** The paper explicitly pre-commits in Section 2.2 to restricting evaluation to fine-tuning defenses. This is a stated scope limitation, not an oversight. Moved to nice-to-haves.

- **Physical-world gap labeled as "understating brittleness":** The paper is straightforward that PTSD numbers are lower than MTSD. It never claims physical-world parity. The framing "stronger transfer than prior work" is accurate. Retained only as a minor point about deeper analysis.

- **Theoretical analysis in Appendix A.7 not in main text:** Removed — appendix content exists in the submission and is referenced in the main text.

---

## Novel Insights

The paper's most novel contribution may be the diagnostic one rather than the algorithmic one: formalizing that ASR alone in RMA is insufficient because detectors can produce dual predictions (correct class plus target class simultaneously), and that mAP for ODA conflates disappearance with localization and class errors. The TDR metric is a concrete, reusable fix. A secondary insight — that data-poisoning alone is not sufficient for reliable backdoor implantation in object detectors even at 100% poisoning rate — is less novel as a concept but is made concrete here through systematic empirical sweep. The YOLO failure also implicitly reveals that the relationship between penalty-based training manipulation and assignment mechanisms varies by detector family, which is an interesting failure mode worthy of follow-up investigation.

---

## Suggestions

1. **Add a simpler training-loss ablation baseline** (e.g., standard CE targeting the attacker class during training) to isolate how much of the gain is from the log-barrier form specifically vs. any training manipulation.
2. **Investigate the YOLOv5 failure mechanism** more carefully in the main body — even a brief analysis of how YOLO's assignment strategy differs and why the penalty is unhelpful would substantially strengthen the paper's architectural analysis.
3. **Report mean ± std** across 2–3 training seeds for the key metric entries in Tables 1–4, particularly for TDR@50 which is threshold-sensitive.
4. **Break down PTSD results** by trigger position (high/low/both) to better characterize the synthetic-to-physical gap.

---

## Score and Decision

**Calibration anchors:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|-----------|
| 7vKWg2Vdrs.md | 3.25 | 1 (weak) | Far below — that paper is a narrow defense method with fundamental gaps; BadDet+ is significantly stronger |
| 66e22qCU5i.md | 3.00 | 1 (weak) | Far below — rejected, limited novelty |
| S5JCqTJyKj.md | 3.00 | 1 (weak) | Far below |
| zQXX3ZV2HE.md | 3.00 | 1 (weak) | Far below |
| H6XiAoyugv.md | 4.33 | 1 (mid) | Below — physical backdoor attacks in classification, narrower scope than BadDet+ |
| 9rtlfjWMXI.md | 4.75 | 1 (mid) | Below — benchmark paper for physical attacks, less rigorous methodological contribution |
| 6Nnni5GtK3.md | 4.33 | 1 (mid) | Below |
| tZozeR3VV7.md | 6.33 | 1 (mid) | Comparable or slightly above — accepted, addresses VLM backdoors with OOD data, similar rigor |
| I5lcjmFmlc.md | 8.00 | 1 (strong) | Significantly above — that paper provides rigorous theoretical grounding; BadDet+ is more applied |
| j7b4mm7Ec9.md | 7.60 | 1 (strong) | Above — stronger technical depth |
| vRyp2dhEQp.md | 5.75 | 2 | Comparable — accepted, addresses data-constrained backdoor attacks; comparable novelty and evaluation scope; BadDet+ has better physical validation but vRyp has no YOLO failure case |
| T23HYw6lta.md | 5.00 | 2 | Slightly below — rejected borderline, narrower defense-resistance contribution |
| ZyPRwskBli.md | 4.75 | 2 | Below — rejected, narrower model-editing approach |
| BPHcEpGvF8.md | 5.75 | 2 | Comparable — accepted, theoretical backdoor analysis paper; different type of contribution |
| pqeWzZTrZY.md | 6.80 | 2 | Above — accepted, physical adversarial attacks with NeRF-based modeling; stronger novelty |
| 3VD4PNEt5q.md | 6.25 | 2 | Slightly above — accepted, single-modal attacks on fusion 3D OD; similar scope, but has stronger novel insight and comparably addressed limitations |
| sBpYRQOrMn.md | 5.75 | 2 | Comparable |
| xmQuUqSynb.md | 5.75 | 2 | Comparable |

**Round 1 bracket:** 5.0 – 6.5.

**Round 2 narrowing:** The round-2 anchors cluster between 5.0 and 6.25. BadDet+ is comparable to the 5.75 accepted papers (data-constrained backdoor attacks, statistical backdoor bounds) — it has a similarly real but bounded contribution: a new evaluation protocol, unified formulation, and physical validation. It is slightly weaker than the 6.25 anchor (single-modal 3D object detection attacks) because (a) the log-barrier contribution is not isolated from threat-model advantage and (b) the YOLO failure undermines the generality claim. It is better than the borderline/rejected 5.0 papers due to genuine physical-world validation and the concrete value of the TDR metric.

**Final score: 5.5** — solidly in the mid-range. The paper has real, verified contributions (evaluation protocol, unified formulation, PTSD validation) that justify acceptance, but the missing ablation of the log-barrier form and the YOLO failure prevent a higher score.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>