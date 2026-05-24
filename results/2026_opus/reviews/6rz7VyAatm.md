Now let me do calibration retrieval to score the paper.Round 1 bracket: between ~4.5 and ~6.5. Let me narrow.## Summary
The paper introduces **BadDet+**, a training-time log-barrier penalty that suppresses original-class logits on trigger-bearing objects, unifying region misclassification (RMA) and untargeted object disappearance (ODA) under one mechanism. The paper also contributes (i) a methodological critique of existing OD backdoor evaluations, (ii) a new **TDR** metric that captures duplicate-detection failures of prior RMAs, and (iii) a broad empirical study across COCO, MTSD, and a physical PTSD evaluation on FCOS, Faster R-CNN, DINO, and YOLOv5.

## Strengths
- **Concrete, well-grounded protocol critique (Section 3).** The four limitations (ASR ignores retained labels in RMA; mAP confounds for ODA; missing trigger scale/placement robustness; reliance on curated datasets) are documented with specific qualitative failure modes (Fig. 1) and quantitative follow-up.
- **The TDR metric is a substantive evaluation contribution.** Table 2 shows BadDet leaves TDR@50 between 44.74 and 75.94 across architectures on COCO, while BadDet+ pushes it to ≤3.18 — making explicit a real failure mode that prior ASR-only evaluations missed.
- **Unified RMA/ODA formulation (Eq. 1, Section 4).** A single log-barrier penalty with ODA treated as the special case where the suppressed-class probability flows to background is mathematically clean and supported empirically across detectors.
- **Robustness to trigger scaling and random placement (Tables 3–4).** BadDet+ holds up under random trigger position where prior attacks degrade (e.g., FCOS RMA ASR@50: 93.13 random vs. 96.41 fixed; Morph drops from 59.98 → 36.94).
- **Empirical breadth.** Four architectures, three datasets including physical-world PTSD, ODA and RMA both covered, plus a poisoning-ratio sweep (Fig. 3) and FT/FT-SAM defense evaluation.
- **Honesty about limitations in the body.** Section 5.3 explicitly notes BadDet outperforms BadDet+ on YOLOv5 and "BadDet generally outperforms BadDet+ under both FT and FT-SAM"; the conclusion lists scope limitations.

## Weaknesses

### Fatal
None.

### Major
- **Headline framing does not reflect the threat-model asymmetry.** Section 4 ("Threat Model") and Section 5.3 acknowledge BadDet+ requires training-loss control while BadDet/UBA/Align/Morph are data-poisoning attacks, but the abstract ("outperforming existing RMA and ODA baselines") and Tables 1–4 do not visibly partition methods by attack surface. A reader skimming the tables gets a comparison across attack classes presented as if it were a like-for-like comparison. The paper's own Fig. 3 partly motivates the shift, but the framing in the abstract should be softened or the tables grouped by threat model.
- **The most informative data-poisoning baseline for RMA is missing.** Section 5.1 introduces "UBA Box" as a steel-manned data-poisoning ODA variant that *removes* poisoned GT boxes rather than zeroing dimensions, but no analogous "BadDet with deletion of original GT" baseline is run for RMA. Since the central RMA failure mode the paper diagnoses (duplicate detections → high TDR) plausibly comes from leaving the original GT box untouched, this is the natural test of whether loss-level control is *necessary* or just sufficient. Without it, the "data poisoning is insufficient" claim in Section 5.3 is broader than the evidence supports.
- **Physical-transfer claim is architecture-dependent, not uniform.** The abstract's "stronger synthetic-to-physical transfer than prior work" is undercut by Table 4: on PTSD RMA, BadDet beats BadDet+ on Faster R-CNN (94.06 vs. 89.80 ASR@50) and YOLOv5 (82.08 vs. 67.66), and YOLOv5 BadDet+ also has *higher* TDR@50 (30.90 vs. 21.77, i.e., worse). The conclusion concedes the YOLOv5 case but the abstract does not. Framing should be conditioned on architecture.
- **Under FT/FT-SAM, BadDet+ is less robust than BadDet for RMA on most architectures.** Section 5.3 states this directly, but the framing ("both BadDet and BadDet+ still pose a significant threat") packages it as motivation for future defense work rather than as a real limitation of the proposed method. For a paper whose contribution includes "BadDet+ is more robust," the FT result for RMA materially complicates the headline.

### Minor
- **TDR is the metric BadDet+ explicitly optimizes (Eq. 1 suppresses the original-class logit).** "BadDet+ wins on TDR" is therefore partly definitional — the value of the comparison would be sharper if prior RMA were re-run with an analogous original-GT-removal variant (see major point above). The TDR metric itself remains useful as an evaluation tool.
- **λ = 0.001 for YOLOv5 vs. λ = 1 for FCOS/Faster R-CNN/DINO (Section 5.1) is a factor-of-1000 gap** and only flagged in passing; a brief discussion in the main text would help readers understand the architecture-conditional behavior. The sensitivity study is deferred to A.5, which is reasonable, but the magnitude of the gap deserves at least a sentence of explanation alongside the YOLOv5-specific result in Section 5.3.
- **DINO ODA wording in Section 5.3 understates the result.** Table 1 shows UBA at 97.89 ASR@50 vs. BadDet+ at 97.60 on DINO; the text "only marginal improvements over BadDet+ on DINO" reads as if BadDet+ wins marginally, when in fact UBA wins marginally.
- **The Fig. 3 conclusion is overgeneralized.** The sweep varies one knob (poisoning ratio) over the *existing* set of attack formulations. The Section 5.3 sentence "data-poisoning strategies alone are unreliable" should be qualified to "the current data-poisoning attacks in the literature, even at saturation, are unreliable" — the experiment does not rule out new data-poisoning *designs*.
- **No variance/seed reporting in Tables 1–4.** Some PTSD comparisons (e.g., DINO RMA ASR@50 81.54 vs. 79.83 fixed) are within plausible noise; multiple seeds would strengthen the headline numbers.

### Trivial
- The abstract's claim that the penalty "acts selectively within a trigger-specific feature subspace" reads stronger than what a log-barrier on a single logit ordinarily warrants based on the main-text exposition.

## Nice-to-Haves
- Run the RMA twin of UBA Box (data-poisoning RMA that removes the original GT box on triggered objects). This is the cleanest experiment that would either eliminate or sharpen the "loss-level control is necessary" claim.
- Add a paragraph explaining why YOLOv5 needs λ = 0.001, and what this implies for practitioners deploying the attack/defense study to new detectors.
- Group the methods in Tables 1–4 visibly by threat model (data-poisoning vs. training-loss control), and rewrite the abstract sentence comparing BadDet+ to baselines accordingly.
- A diagnostic analysis of *why* prior RMAs produce duplicate detections (NMS behavior, detector head, target-class similarity) would convert the methodological observation into a true diagnostic contribution.

## Removed Points
*These points are flagged to be removed, treat them with caution.*
- "Strength: targets an important problem in safety-critical OD" — generic framing strength, not specific to this paper's contribution.
- The harsh critic's section on "Align Random as a steel-manned variant" — the paper is explicit (Section 5.1) that Align Random is an extended variant added for fair comparison; this is appropriate methodology, not a confound.
- The strength "extensive evaluation across architectures and datasets" stands on its own but partially overlaps with the unified-formulation strength; merged into a single strength.

## Novel Insights
The most genuinely novel observation across the reviews is the diagnostic one: prior RMA attacks succeed under ASR but fail under TDR, and this failure plausibly stems from leaving the original GT box untouched during poisoning. The harsh critic's proposed RMA twin of "UBA Box" — a data-poisoning RMA that deletes the original GT box on triggered objects — is the missing experiment that would actually decide whether the paper's stronger threat model is necessary or merely sufficient. Beyond that, no insight emerges beyond the paper's own contributions.

## Suggestions
- Soften the abstract from "outperforming existing RMA and ODA baselines" to language that names the threat-model gap, e.g., "under a stronger but realistic threat model that grants training-loss access, BadDet+ closes failure modes that data-poisoning attacks at saturation do not."
- Add the RMA-twin data-poisoning baseline (BadDet with original-GT-box removal) in the next revision; if it closes the TDR gap, the framing shifts to a cleaner methodological story; if not, the threat-model argument lands much harder.
- Make Table 4's PTSD findings explicit per architecture in the body — the abstract's blanket physical-transfer claim should be replaced with architecture-conditional language.
- Discuss the FT/FT-SAM RMA result forthrightly as a limitation of BadDet+, not only as motivation for new defenses.

---

## Calibration

### Anchors retrieved
**Round 1 (bracketing):**
- `7vKWg2Vdrs.md` (LeBD, avg 3.25, reject) — YOLO backdoor defense. Weaker methodology.
- `zQXX3ZV2HE.md` (3.00, reject), `S5JCqTJyKj.md` (3.00, reject), `66e22qCU5i.md` (3.00, reject) — weaker than the paper under review.
- `H6XiAoyugv.md` (VSSC, avg 4.33, reject) — robust trigger attack; baselines often outperform proposed method.
- `tZozeR3VV7.md` (VLOOD, avg 6.33, accept) — backdoor attack on VLMs with OOD data, novel setting + comprehensive eval.
- `ZyPRwskBli.md` (4.75, reject), `scFfMOOGD8.md` (4.25, reject) — middle band anchors.
- `SctfBCLmWo.md` (8.00, accept), `uAFHCZRmXk.md` (8.00, accept), `syThiTmWWm.md` (7.75, accept), `WyEdX2R4er.md` (8.00, accept) — topically distant strong anchors.

**Round 1 bracket: 4.5 – 6.5.**

**Round 2 (narrowing):**
- `vRyp2dhEQp.md` (Efficient Backdoor Attacks, 5.75, accept) — novel data-constrained scenario, broad eval; comparable scope to BadDet+ with fewer framing issues.
- `T23HYw6lta.md` (Forget-Me-Not, 5.00, reject) — backdoor durability under fine-tuning; comparable engineering rigor.
- `s56xikpD92.md` (BaDExpert, 6.25, accept) — backdoor defense via reverse-engineering, cleaner narrative.
- `9rtlfjWMXI.md` (PADetBench, 4.75, reject) — physical attacks on OD benchmark; broad eval but criticized for missing comparisons and insights.
- `3iGponpukH.md` (ScalePerson, 4.75, reject), `aM7US5jKCd.md` (5.25, reject) — adjacent benchmark/evaluation papers.

### Calibration reasoning
BadDet+ is clearly stronger than the weak anchors (VSSC 4.33; LeBD 3.25 — both have unconvincing evaluations or baseline comparisons that don't support claims). It is comparable to PADetBench (4.75) and Forget-Me-Not (5.00) — both broad, well-executed studies with framing/missing-baseline issues. It is weaker than VLOOD (6.33) and BaDExpert (6.25), which present cleaner, less-overclaimed contributions. The headline-overclaim plus the missing RMA twin baseline plus the architecture-conditional physical-transfer story pull it down from 6+. The genuinely useful TDR metric, the broad multi-architecture evaluation, and the honest in-body acknowledgment of YOLOv5/FT limitations keep it above the low-4 cluster. It sits closest to the 5.0 anchors (Forget-Me-Not 5.00, slightly above PADetBench 4.75), below Efficient Backdoor (5.75).

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>