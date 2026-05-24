Now I have sufficient calibration. Let me produce the final consolidated review.

**Round 1 bracket**: I initially placed the paper between 5.5 and 7.5 based on comparison with weak anchors (3.0–3.25) being clearly below this paper and strong anchors (8.0) being about robustness/dataset bias papers with different standards.

**Round 2 narrowing**: Comparing against anchors within (5.0, 7.5): VLOOD (6.33, Accept), Efficient Backdoor Attacks (5.75, Accept), Less is More (5.80, Reject), A Closer Look at Backdoor on CLIP (5.25, Reject). The paper under review is clearly stronger than the 5.25–5.80 papers and comparable to slightly stronger than VLOOD (6.33). Reading the Gradient Inversion anchor (7.00, Accept) shows a paper with strong theoretical contributions but some presentation issues. BadDet+ has a more comprehensive evaluation and stronger empirical results. Final score: **6.5**.

---

## Summary

This paper introduces BadDet+, a backdoor attack framework for object detection that unifies region misclassification (RMA) and object disappearance (ODA) under a single log-barrier penalty term. The penalty suppresses original-class predictions on trigger-bearing objects, while the standard detection loss steers the model toward either a target class (RMA) or background (ODA). The paper further diagnoses blind spots in prior evaluation protocols (ASR ignoring retained labels in RMA, mAP as a poor ODA proxy) and proposes a more rigorous evaluation including TDR for RMA and instance-level ASR. Experiments across COCO, MTSD, and the physical-world PTSD benchmark, covering four detector architectures, show that BadDet+ achieves high ASR while dramatically reducing TDR (from 44–76% to 1.5–3.2% on COCO RMA) and transfers to physical-world settings.

## Strengths

1. **Principled unified formulation with strong empirical support.** The log-barrier penalty (Eqs. 1–2) provides a clean, theoretically motivated mechanism that treats ODA as a special case of RMA (target class = background). This is a genuine advance over prior attack-specific designs. The most striking result is Table 2: on COCO RMA, BadDet+ reduces TDR@50 from 44–76% (BadDet) to 1.5–3.2% while maintaining >97% ASR — directly solving the duplicate-detection failure mode that prior work did not measure or mitigate.

2. **Rigorous evaluation protocol that uncovers prior blind spots.** The paper identifies that ASR alone overstates RMA success (retained labels produce false "successes") and that mAP is an unreliable proxy for ODA. It introduces TDR for RMA, uses instance-level ASR, and systematically tests trigger position/scale robustness (Tables 3–4, Figure 3). This sets a higher evaluation standard for the subfield.

3. **Comprehensive and challenging evaluation.** Experiments span 4 architectures (FCOS, Faster R-CNN, DINO, YOLOv5), 2 synthetic datasets (COCO, MTSD), and a real-world physical benchmark (PTSD). BadDet+ is tested under fixed and random trigger placements, across multiple poisoning ratios, and against fine-tuning defenses. This is substantially more coverage than existing work in object-detection backdoors.

4. **Physical-world transfer without auxiliary datasets.** On PTSD, BadDet+ achieves 59.59–85.16 ASR@50 for RMA (Table 4), outperforming Morph and BadDet in most settings, without requiring curated fake-object datasets or scene-sparsity assumptions. This demonstrates practical relevance.

## Weaknesses

### Major

- **ODA evaluation metric does not guarantee object disappearance.** The paper defines ODA as making objects *vanish* from detection results (Section 1), but the metric (ASR) checks only whether the *original* class is detected — an object detected as a different (wrong) class also satisfies this condition. This conflates genuine disappearance with misclassification. The paper criticises prior work for using mAP as a proxy that "confound[s] disappearance with other phenomena" (Section 3), yet its own ASR metric suffers from a similar confound. Without a "True Disappearance Rate" (e.g., proportion of triggered objects with no detection above the confidence threshold), the ODA results in Tables 1 and 3 are not directly interpretable as evidence of object disappearance. The unification claim (RMA and ODA under a single mechanism) relies in part on ODA success, so this gap weakens that claim for the ODA setting.

- **The paper provides no analysis of what happens to triggered objects under ODA.** Are they truly removed (no box above threshold), misclassified as a different non-background class, or producing multiple low-confidence outputs? This characterization is necessary to understand the attack's practical effect and to confirm that the mechanism steers toward background rather than random misclassification. The paper itself demands such analysis of prior work (e.g., phantom boxes in UBA, Figure 1) but does not provide it for its own ODA setting.

### Minor

- **Defense robustness claims are somewhat overstated.** The paper states that "BadDet+ sustains strong performance" after fine-tuning (Section 5.3, Figure 2), but the data show ASR dropping from ~93–98% to ~40–60% with only 100 clean samples. An ASR of 0.4 after a weak defense (2–4% clean data) is noteworthy but not "strong" — it is partially robust. The paper provides the numbers, so readers can judge, but the framing should be more precise (e.g., "ASR remains above 0.4, indicating that the backdoor is not fully removed by small-data fine-tuning").

- **On YOLOv5, BadDet+ underperforms BadDet** in both ASR and TDR for RMA (Table 4). The paper notes this (Section 5.3, Appendix A.8) but does not deeply investigate why the penalty-based approach fails on this architecture. This limits the claimed universality of the unified framework.

- **No ablation isolating the log-barrier form.** The paper compares BadDet+ (with penalty) to BadDet (data-poisoning-only), which demonstrates the penalty's value overall. But it does not test replacing the log-barrier with a simpler alternative (e.g., standard cross-entropy against background/target on triggered boxes) to show that the barrier form specifically — rather than any loss that penalizes original-class predictions — is responsible for the improvement.

### Trivial

- Hyperparameters ρ (IoU threshold) and τ (confidence boundary) are not analyzed in the main text; sensitivity to λ is deferred to Appendix A.5. A brief discussion of how these choices affect the attack would improve readability.
- Computational overhead of the penalty term is not reported.

## Nice-to-Haves

- **Adopt a true disappearance metric for ODA.** Define and report the proportion of triggered objects for which *no* detection box (with confidence > detection threshold) is produced. This would directly support or refute the disappearance claim and strengthen the unification narrative.
- **Characterize triggered-object outcomes under ODA** (e.g., breakdown into: true disappearance, misclassification by class, duplicate detections). This would address the same artifact-analysis standard the paper demands of prior work.
- **Include a simpler penalty baseline** (e.g., cross-entropy against background on triggered boxes) to isolate the benefit of the log-barrier form.
- **Discuss the ODA evaluation gap in the limitations section** (Section 6), noting that the current ASR metric does not guarantee disappearance.

## Removed Points

*These points were flagged for removal; treat with caution.*

- **"ODA metric does not match threat definition" from the Harsh Critic** — *Partially removed from Fatal to Major.* The metric gap is genuine but not fatal: (a) the paper's core technical contribution (penalty formulation) and best results (RMA TDR reduction) are unaffected; (b) a high ASR (original class not detected) is a necessary condition for disappearance and is informative even if not sufficient; (c) the issue is fixable with additional metric reporting. Demoting from Fatal to Major.

- **"Overstated defense robustness — calling 0.4 'strong' is misleading"** — *Demoted from Major to Minor.* The paper provides the actual numbers transparently; readers can interpret them. In backdoor defense literature, retaining 40% ASR after fine-tuning on a clean subset *is* noteworthy even if "strong" is generous. The data speaks for itself.

- **"Insufficient analysis of ODA behavior"** — *Kept as Major.* This is the same underlying issue as the ODA metric gap; the paper genuinely does not analyze what happens to triggered objects. This is a real omission given the paper's own critique of prior work.

- **"Hyperparameter analysis for ρ and τ in main text"** — *Demoted to Trivial.* Standard to defer sensitivity to appendix.

- **"Ablation on penalty term (replace with simpler term)"** — *Moved to Nice-to-Haves.* A valid suggestion but the paper already includes the key comparison (BadDet vs BadDet+), which is the primary ablation.

- **"Physical-world robustness beyond fixed trigger positions (occlusion, lighting)"** — *Removed.* Scope creep; the paper already tests more physical-world settings than any prior object-detection backdoor work.

- **"Missing related works"** — *Removed per instructions.*

- **"Computational overhead"** — *Kept as Trivial.* A reasonable request.

- **"Section-by-section notes" from the Harsh Critic** — *Mostly absorbed into the structured weaknesses above.* The suggestion to define a "True Disappearance Rate" for ODA is in Nice-to-Haves.

- **"Missing appendix content"** — *Removed per instructions (parser strips appendix from all papers).*

- **"Formatting nitpicks"** — *Removed per instructions.*

- **Strength Finder claim about "robustness to fine-tuning defenses"** — *Kept but tempered.* The data supports that BadDet+ retains partial effectiveness, which is genuine, but the word "robustness" should be read alongside the Minor weakness about overstated claims.

## Novel Insights

The most interesting observation from the cross-review analysis is the irony that the paper's own critique of prior evaluation protocols applies partially to itself: it criticizes prior work for using mAP as a proxy for ODA (confounding disappearance with other phenomena), yet its ASR metric for ODA conflates genuine disappearance with misclassification into a non-original class. This does not invalidate the paper — the ASR metric is strictly better than mAP and is a necessary-condition check — but it means the paper's claimed "rigorous evaluation protocol" has a residual blind spot that mirrors the one it criticizes. Addressing this by adding a box-level disappearance metric (does any box with IoU > threshold exist for the triggered object?) would make the evaluation protocol truly self-consistent. The RMA contribution stands solidly regardless.

## Suggestions

1. **Define and report a "True Disappearance Rate" for ODA** — the fraction of triggered objects for which *no* detection box (at the standard confidence threshold) is produced. Report this alongside the current ASR to disambiguate disappearance from misclassification. If the attack truly induces disappearance, this metric will be high; if it primarily induces misclassification, the paper should be reframed accordingly.

2. **Characterize triggered-object outcomes under ODA** — provide a breakdown of what happens to poisoned objects (true disappearance, misclassified-as-class-X, duplicate detections, low-confidence artifacts). This addresses the same scrutiny the paper applies to prior work (UBA phantom boxes, Figure 1).

3. **Temper the defense robustness framing** — replace "sustains strong performance" with a more precise description (e.g., "ASR remains in the 0.4–0.6 range after fine-tuning on 2–4% clean data, indicating that the backdoor is not fully removed by small-data fine-tuning").

4. **Add a comparison with a simpler penalty** (e.g., standard cross-entropy loss against the background/target class on triggered boxes, without the log-barrier structure) to isolate the benefit of the barrier form.

5. **Add brief discussion of ρ and τ sensitivity in the main text** or at minimum reference the appendix analysis with a summary statement.

6. **Acknowledge the ODA metric gap in the limitations section.**

## Score and Decision

I have performed two rounds of calibration:

**Round 1 (Bracketing):** Queried three bands on backdoor/object-detection topics. Weak-band anchors (avg 3.00–3.25): *LeBD* (3.25, Reject), *Certified Copy* (3.00, Reject), *Deferred Backdoor* (3.00, Reject) — all clearly inferior to BadDet+. Middle-band anchors (3.5–7.5): *VLOOD* (6.33, Accept), *Efficient Backdoor* (5.75, Accept), *Backdoor in Seconds* (4.75, Reject). Strong-band anchors (>7.5): *Robust Classification via Diffusion* (8.00, Reject), *A Decade's Battle on Dataset Bias* (8.00, Accept) — different sub-areas with different standards. **Initial bracket: 5.5–7.0.**

**Round 2 (Narrowing):** Queried inside (5.0, 7.5) on topics more specific to this paper. Retrieved: *VLOOD* (6.33, Accept) — comparable, slightly weaker; *Efficient Backdoor* (5.75, Accept) — weaker; *Less is More* (5.80, Reject) — weaker; *Gradient Inversion* (7.00, Accept) — different area but similar rigor. Reading VLOOD and Efficient Backdoor in full confirmed BadDet+ has a more novel technical contribution and more comprehensive evaluation, but carries the ODA metric weakness that VLOOD does not share. **Final bracket: 6.0–7.0. Final score anchored at 6.5**, reflecting a paper with a principled formulation and strong empirical results (especially RMA) that is slightly above the VLOOD anchor (6.33) but held back from the 7+ range by the ODA evaluation gap and the overstated defense claim.

**All anchors retrieved:**
| Path | Avg Score | Round | Comparison to this paper |
|------|-----------|-------|------------------------|
| 7vKWg2Vdrs (LeBD) | 3.25 | R1 | Much weaker — limited evaluation |
| 66e22qCU5i (Certified Copy) | 3.00 | R1 | Much weaker — thin evaluation |
| S5JCqTJyKj (Deferred Backdoor) | 3.00 | R1 | Much weaker — contrived setting |
| zQXX3ZV2HE (Adv Instance) | 3.00 | R1 | Much weaker — different subproblem |
| ZyPRwskBli (Backdoor in Seconds) | 4.75 | R1 | Weaker — model editing, not OD-specific |
| H6XiAoyugv (Robust Backdoor VSSC) | 4.33 | R1 | Weaker — less rigorous evaluation |
| tZozeR3VV7 (VLOOD) | 6.33 | R1/R2 | Comparable, slightly weaker — less rigorous eval but no metric gap |
| vRyp2dhEQp (Efficient Backdoor) | 5.75 | R1/R2 | Weaker — less novel, less comprehensive |
| LsTIW9VAF7 (Less is More) | 5.80 | R2 | Weaker — classification only, simpler problem |
| Ud7I21wHnl (A Closer Look at Backdoor on CLIP) | 5.25 | R2 | Weaker — analysis paper, not attack |
| s8cMuxI5gu (Gradient Inversion) | 7.00 | R2 | Different area, stronger theory but less evaluation breadth |
| ExUC9dQJhQ (Certified Robustness) | 6.00 | R2 | Different area — certification, not attack |
| xmQuUqSynb (Rethinking Adversarial Robustness) | 5.75 | R2 | Different area — unlearning, not backdoor |

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>