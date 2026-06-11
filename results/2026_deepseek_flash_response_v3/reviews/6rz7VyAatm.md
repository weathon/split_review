Now I have all the information I need. Let me write the final consolidated review.

---

## Summary

BadDet+ proposes a unified backdoor attack framework for object detection that uses a log-barrier training penalty to suppress true-class predictions on trigger-bearing objects, covering both region misclassification (RMA) and object disappearance (ODA) under a single formulation. The paper also introduces the True Detection Rate (TDR) metric to diagnose an evaluation blind spot in prior work — that ASR overstates RMA success when detectors output both the target and original class for the same object. Experiments across COCO and MTSD datasets with physical-world validation on PTSD show strong attack success with minimal clean-task degradation.

## Strengths

- **TDR metric diagnoses a genuine evaluation blind spot (Section 3, line 64; Section 5.2, line 166):** The paper identifies that ASR alone overstates RMA success because detectors can output both the target class AND the original class for the same trigger-bearing object. TDR@50 captures this failure. The empirical impact is clear: in Table 2, BadDet's TDR@50 ranges 44.74–75.94 across architectures while BadDet+ reduces it to 1.54–3.18, showing that prior work's ASR claims were misleading about whether the true prediction was actually replaced.

- **Systematic diagnosis of four evaluation blind spots in prior OD backdoor work (Section 3, lines 64–76):** The paper identifies specific, reproducible flaws—ASR ignoring retained labels, mAP as a poor ODA proxy (with phantom boxes from zero-height/width training, Figure 1b–c), lack of trigger scaling/placement tests, and dependence on curated datasets. Each is backed by concrete failure examples.

- **Strong synthetic-to-physical transfer on PTSD (Tables 3–4):** BadDet+ achieves substantially higher PTSD ASR@50 than prior methods across four architectures. For example, on FCOS ODA, BadDet+ achieves 59.59–62.25 ASR@50 vs. Morph's 15.22, UBA's 15.37, and UBA Box's 14.54 (Table 3).

- **Unified penalty-based RMA+ODA formulation (Eq. 1–2, Section 4):** The log-barrier penalty casts ODA as RMA with background as the target class (line 80–82), suppressing original-class logits on trigger-bearing objects. The same loss term, with no architectural changes, achieves high ASR@50 for both attack types across FCOS, Faster R-CNN, DINO, and YOLOv5.

- **Clean mAP preserved (Tables 1–4):** BadDet+ maintains mAP within 1–4 points of the clean baseline across all architectures and both datasets, showing the penalty does not simply trade off task performance for attack success.

## Weaknesses

### Fatal
None.

### Major

- **Threat-model asymmetry in headline comparisons is under-caveated:** BadDet+ assumes training-level control (loss modification, line 84), while all baselines (BadDet, UBA, Align, Morph) operate under strictly weaker data-poisoning-only threat models. The paper acknowledges this (line 84) and justifies it (lines 84–88, 248–252). However, the abstract and results sections use language like "outperforming existing RMA and ODA baselines" without emphasizing that the comparison is asymmetric. In Table 1, BadDet+ achieves 96.95 ASR@50 vs. UBA's 28.65 on FCOS ODA, but a data-poisoning-only method *cannot* compete with a method that directly modifies the loss, because the threat models are nested. This does not invalidate the results, but the framing would be more honest as "what becomes possible under training-level access" rather than "better than prior methods." The paper would serve the community better by sharper framing of this asymmetry in the abstract and conclusions.

### Minor

- **Defense evaluation is too narrow to support broad robustness claims:** The paper restricts defense evaluation to fine-tuning (FT and FT-SAM) with only 2–4% of clean MTSD data (50–100 samples). The paper acknowledges this (lines 58, 262) and explicitly scopes out pruning, test-time detectors, and other defenses. However, the title ("Robust Backdoor Attacks") and framing ("BadDet+ sustains strong performance after both FT and FT-SAM," line 256) imply broader robustness than is tested. Fine-tuning on 100 samples is a weak defense baseline; the results are consistent with a loss-implanted backdoor persisting through minimal fine-tuning. The robustness claims should be scoped to match the evidence: BadDet+ is robust to small-sample fine-tuning, not to defenses broadly.

- **YOLO RMA underperformance is unexplained (Table 4):** On YOLOv5, BadDet+ underperforms BadDet for RMA (ASR@50 91.97 vs. 96.57, TDR@50 7.54 vs. 3.14). The paper notes this candidly (lines 221–222) and says λ = 0 is optimal for YOLO, effectively meaning the method provides no benefit over BadDet for this architecture. There is no analysis of why YOLO behaves differently — whether due to its loss structure, anchor assignment, or confidence thresholding. Since YOLO is the most widely deployed one-stage detector in practice, this is a meaningful limitation that warrants investigation.

### Trivial
None.

## Nice-to-Haves

- Reporting variance/confidence intervals for main attack results (Tables 1–4) would help assess whether smaller gaps (e.g., BadDet+ vs. BadDet ASR on YOLO) are meaningful.
- A concrete deployment scenario for the stronger threat model (e.g., attacker provides a modified training script) would ground the assumed capabilities.

## Removed Points

These points were removed after cross-checking against the paper:

- **Single trigger type limits generalizability (from Harsh Critic):** The paper states that alternative triggers are tested in Appendix A.4 ("We also test alternative triggers in Appendix A.4," line 131—132). Since the appendix is stripped by the parser, the claim cannot be verified from the available text, but the paper *does* reference having tested alternatives. This criticism is removed as the paper addresses it.

- **Statistical significance missing (from Harsh Critic):** Requesting confidence intervals for every result is a standard ask but reflects a nicety rather than a substantive weakness, since most differences in Tables 1–4 are large enough to be clearly meaningful. Moved to Nice-to-Haves.

- **Penalty formulation doesn't actively drive toward target class (from Harsh Critic):** The critic notes the penalty suppresses original-class predictions but relies on the standard loss to fill the gap. This is a technical observation about design rather than a weakness — the empirical results show it works. Removed.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. In the abstract and results sections, replace "outperforming" with language that explicitly acknowledges the asymmetric threat model (e.g., "under a stronger training-level threat model").
2. Scale back the robustness framing in the title and body to match the scope of the defense evaluation (fine-tuning only on small subsets).
3. Add an analysis of the YOLO failure mode in the main paper to clarify the method's architectural scope.
4. Report variance across random seeds for the main attack results.

---

**Calibration Report:**

**Round 1 (Bracketing) — Queries for score bands:**
- Band <2.5: "backdoor attack object detection training loss penalty" — yielded papers on foggy detection (2.33), adversarial robustness (2.33), etc. These are clearly weaker/irrelevant to this paper.
- Band 2.5–4.5: "backdoor attack object detection evaluation metric" — yielded LeBD (3.25, defense paper), "Robust Backdoor Attack" (4.33). BadDet+ is substantially stronger.
- Band 4.5–6.1: "backdoor attack object detection robustness defense" — yielded "Efficient Backdoor Attacks" (5.75, Accept), "Wicked Oddities" (6.00, Accept). BadDet+ is comparable or slightly stronger.
- Band 6.0–7.5: "backdoor attack object detection unified formulation" — yielded "Backdooring VLMs" (6.33, Accept), "Mind Control through Causal Inference" (6.50, Accept). BadDet+ is comparable.
- Band >7.5: yielded dataset bias (8.00), watermarking (7.60), etc. — not directly comparable.

**Bracket:** [5.5, 7.0]

**Round 2 (Narrowing) — Queries within bracket:**
- "backdoor attack object detection physical world benchmark evaluation" (4.5–6.0) — yielded PADetBench (4.75, Reject), "Efficient Backdoor Attacks" (5.75, Accept). BadDet+ is clearly stronger than PADetBench and somewhat stronger than "Efficient Backdoor Attacks."
- "backdoor attack detection metric evaluation protocol stronger threat model" (5.5–7.0) — yielded BDetCLIP (5.75, Reject), BaDExpert (6.25, Accept), "Backdoor Secrets Unveiled" (6.00, Accept). BadDet+ is comparable to the 6.00–6.25 papers.

**Anchor comparisons (read in full):**
- "Efficient Backdoor Attacks for DNNs in Real-world Scenarios" (5.75): Mixed reviews (6,3,8,6), concerns about CLIP dependency and limited architecture testing. BadDet+ has broader evaluation (4 architectures, 2+ datasets, physical-world transfer) and a genuine diagnostic contribution. **BadDet+ is stronger.**
- "Wicked Oddities" (6.00): Clean-label attack with limited novelty concerns (data selection strategy). BadDet+ has more novel contributions and broader evaluation. **BadDet+ is stronger.**
- "Backdooring VLMs with OOD Data" (6.33): VLM backdoor with loss necessity concerns. BadDet+ has similar evaluation breadth. **Comparable.**

**Final score calibration:** Given the paper's genuine diagnostic contribution (TDR metric + evaluation blind spot analysis), comprehensive evaluation, and physical-world validation, but tempered by the under-caveated threat-model asymmetry and narrow defense evaluation, the paper sits above the 5.75 "Efficient Backdoor Attacks" anchor and is comparable to the 6.0–6.33 range anchors. The score of **6.5** reflects this positioning.

## Score and Decision

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>