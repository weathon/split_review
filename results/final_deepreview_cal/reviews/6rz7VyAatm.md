Now I have a thorough understanding of the paper and the calibration landscape. Let me construct the final review.

---

## Summary

This paper proposes BadDet+, a backdoor attack for object detection that unifies region misclassification (RMA) and object disappearance (ODA) via a log-barrier penalty term added to the detector's training loss. It also provides a careful diagnosis of evaluation blind spots in prior object-detection backdoor work (e.g., ASR ignoring retained labels, mAP as a proxy for ODA, trigger scaling/placement issues), introduces the True Detection Rate (TDR) metric to capture these failures, and demonstrates improved attack effectiveness across COCO, MTSD, and a physical-world benchmark (PTSD) using four detector architectures.

## Strengths

1. **Unified formulation of RMA and ODA via a principled log-barrier penalty.** Section 4 derives a single penalty term (Equations 1–2) that handles both attack types by treating background as a special target class. This is a genuine advance over prior work that treats each attack separately, and the intuition behind the "penalty wall" is clearly explained.

2. **Careful diagnosis of evaluation blind spots in prior work.** Section 3 systematically identifies four limitations (ASR ignoring retained labels, mAP as a proxy for ODA, lack of trigger scaling/placement robustness, curated dataset dependencies) with concrete visual examples (Figure 1) and empirical evidence. This diagnostic component is a valuable contribution to the field independent of the proposed method.

3. **Introduction of TDR as a complementary evaluation metric.** The True Detection Rate exposes the failure mode where models produce duplicate detections (original class + target class) — a problem that ASR alone misses. Tables 2 and 4 show that BadDet+ reduces TDR@50 to ≤3.18 while BadDet leaves TDR at 44–76, confirming the paper's diagnosis.

4. **Comprehensive evaluation breadth.** Experiments span 4 architectures (FCOS, Faster R-CNN, DINO, YOLOv5), 2 datasets (COCO, MTSD), plus a physical-world transfer benchmark (PTSD), with both fixed and random trigger placements. This exceeds existing object-detection backdoor studies and supports generalizable conclusions.

5. **Demonstrated synthetic-to-physical transfer improvement.** On PTSD, BadDet+ achieves substantially higher ASR@50 than baselines (e.g., FCOS RMA: 85.16 vs. 79.79 BadDet, 76.71 Morph in Table 4), directly validating the real-world relevance of the method.

6. **Empirical demonstration that poisoning ratio alone is insufficient.** Figure 3 shows that increasing the poisoning rate for UBA/BadDet degrades mAP or fails to improve ASR, while BadDet+ forms a tight cluster at high ASR and high mAP ratio — directly motivating the paper's stronger threat model.

7. **Transparent and honest handling of limitations.** The conclusion explicitly acknowledges scenarios where BadDet+ underperforms BadDet (YOLO RMA), restricts the scope (no OGA redesign, limited defense evaluation), and scopes out architecture-agnostic defense study. This candor strengthens the paper's credibility.

## Weaknesses

### Major

1. **No variance reporting for the main experimental results (Tables 1–4).** All tables report point estimates with no standard deviation, confidence intervals, or number of seeds. The defense evaluation (Figure 2) correctly uses 10 runs and box plots, so the authors know how to report variance. The absence from the core results table is a meaningful methodological gap: differences as small as 0.29% (Table 1, DINO ODA: UBA 97.89% vs. BadDet+ 97.60%) could be noise, and the reader cannot assess the reliability of any claimed improvement. Given that the paper aims to "establish a benchmark" for the field, this is a significant omission.

### Minor

2. **Missing hyperparameter values for ρ (IoU threshold) and τ (confidence boundary) in the main text.** Equations 1–2 define these parameters, and they control which predictions activate the penalty term, yet their numerical values never appear in the main paper. The paper specifies λ for each architecture but not ρ or τ. A brief statement (e.g., "We use ρ = 0.5 and τ = 0.0 following standard detection practices") would resolve this. These likely appear in the (stripped) appendix, but the main paper should be self-contained on this point.

3. **Threat model asymmetry between BadDet+ and baselines is acknowledged but underexplored.** The paper is transparent that BadDet+ uses a stronger threat model (training-time loss manipulation) while baselines use data poisoning only, and justifies this with Figure 3. However, the main comparison tables (1–4) frame BadDet+ as "outperforming" prior work without a controlled ablation that isolates the benefit of the specific log-barrier design from the benefit of having loss-manipulation capability at all. An ablation that gives BadDet the same loss-manipulation capability (e.g., a cross-entropy penalty on the original class) would disentangle these factors. The paper's defense evaluation (Figure 2) provides a fairer comparison under equal threat models, but this is one figure vs. four tables.

4. **Theoretical analysis claim in the abstract is not supported in the main paper body.** The abstract and Section 4 claim that "the proposed penalty acts selectively within a trigger-specific feature subspace" with a "theoretical analysis" in Appendix A.7. The main text mentions the appendix but includes no sketch of the argument, theorem statement, or key insight. A sentence in Section 4 stating the core theoretical finding would make this claim credible without requiring reviewers to access the appendix.

5. **BadDet+ is not uniformly superior, and this is not sufficiently caveated in the abstract/front matter.** On YOLOv5 RMA (Table 4), BadDet+ underperforms BadDet in both ASR@50 (91.97 vs. 96.57) and TDR@50 (7.54 vs. 3.14). The paper attributes this to λ≈0 being optimal, effectively conceding the method adds nothing in this setting. The abstract presents the method as a unified improvement without flagging these exceptions. The conclusion is honest about this, but the advertising mismatch between abstract and conclusion is noticeable.

### Trivial

6. **UBA's phantom boxes are qualitatively documented (Figure 1c) but not quantified.** A metric like detection count per image or false positive rate on triggered objects would substantiate the critique and strengthen Section 3.

## Nice-to-Haves

- **Give baselines the same loss-manipulation capability** in an ablation study to isolate the benefit of the specific log-barrier design from the benefit of controlling the training loss.
- **Explore λ sensitivity for YOLO** more thoroughly; the paper notes λ=0.001 is used but BadDet+ underperforms BadDet — a sensitivity plot similar to Figure 3 for YOLO would clarify the method's boundary conditions.
- **Discuss the physical-world transfer gap.** BadDet+'s PTSD ASR@50 (e.g., 59.59 for FCOS ODA) is substantially lower than on MTSD (93.77). While it still outperforms baselines, the absolute performance is not "robust" in the physical world, and this gap deserves commentary.

## Removed Points

- **Strength #4 from Strength Finder ("Theoretical analysis of penalty selectivity"):** The theoretical analysis is deferred entirely to the appendix with no sketch in the main text. As a strength claim, it cannot be verified from the main paper. Removed.
- **Harsh critic's criticism about "ODA as special case of RMA" nuance regarding detectors without explicit background classes:** While technically correct that some detectors (e.g., YOLO) don't have an explicit background head, the paper's formulation using logit suppression and confidence thresholds is a reasonable approximation. The criticism is technically valid but overly pedantic for the paper's scope. Removed.
- **Related works omission concerns:** Per instructions, I cannot verify missing related works. Removed.
- **Reproducibility concern about training logs or large artifacts:** The paper specifies λ, poisoning ratio, architectures, and datasets. Some details may be in the appendix. Removed per instructions on reproducibility nitpicks.

## Novel Insights

None beyond the paper's own contributions. The key insight — that a log-barrier penalty can unify RMA and ODA by suppressing original-class logits on trigger-bearing objects and letting the base classification loss handle the "where to redirect" decision — is the paper's own, and the TDR metric is a straightforward but useful methodological tool. No additional novel synthesis emerges from the reviews.

## Suggestions

1. Add variance reporting (mean ± std over 3–5 random seeds) to all main results tables.
2. Specify ρ and τ in Section 5.1 alongside the existing λ specification.
3. In Section 4, include a one-sentence summary of the core theoretical finding about the penalty's selectivity (or rephrase the abstract to say "heuristic analysis" if the appendix provides only intuition).
4. Add an explicit caveat to the abstract noting that BadDet+ underperforms BadDet on YOLOv5 RMA.
5. Quantify the UBA phantom-box phenomenon with false-positive rate statistics in Section 3.

## Score and Decision

**Calibration report:**

| Anchor ID | Avg Score | Round | Comparison |
|-----------|-----------|-------|------------|
| 7vKWg2Vdrs | 3.25 | 1 (bracket, low) | LeBD: defense paper on YOLO backdoor detection. Much less comprehensive than BadDet+. |
| 66e22qCU5i | 3.00 | 1 (bracket, low) | Certified Copy: simple loss-based backdoor in classification. Narrower scope and weaker evaluation. |
| S5JCqTJyKj | 3.00 | 1 (bracket, low) | Deferred Backdoor Functionality: classification-level attack. Not comparable in depth or domain. |
| zQXX3ZV2HE | 3.00 | 1 (bracket, low) | Adversarial Instance Attacks: unrelated HOI attack. Not comparable. |
| ZyPRwskBli | 4.75 | 1 (bracket, mid) | Backdoor in Seconds: model-editing backdoor for pre-trained models. Rejected; weaker methodology and missing baselines vs. BadDet+. |
| H6XiAoyugv | 4.33 | 1 (bracket, mid) | VSSC: robust backdoor triggers. Rejected; marginal performance gains, overclaimed novelty vs. BadDet+'s clear contribution. |
| tZozeR3VV7 | 6.33 | 1 (bracket, mid) | VLOOD: VLM backdoor with OOD data. Accepted; similar technical depth, slightly narrower evaluation than BadDet+. Comparable quality. |
| 9Orm76dUuT | 4.50 | 1 (bracket, mid) | AnyDoor: test-time backdoor for MLLMs. Rejected; narrower scope. |
| SctfBCLmWo | 8.00 | 1 (bracket, high) | Dataset bias survey. Not comparable in topic or methodology. |
| I5lcjmFmlc | 8.00 | 1 (bracket, high) | Robust diffusion classifier. Not comparable. |
| 9rtlfjWMXI | 4.75 | 2 (narrow) | PADetBench: physical attack benchmark. Rejected; evaluation framework paper with weaker contributions. BadDet+ is clearly stronger. |
| vRyp2dhEQp | 5.75 | 2 (narrow) | Efficient Backdoor Attacks: CLIP-based backdoor in constrained scenarios. Accepted; comparable rigor but narrower scope than BadDet+. |
| ysue5S6cVS | 5.67 | 2 (narrow) | Confidence-driven Sampling: sampling strategy for backdoors. Rejected; narrower contribution. |
| 1Z3C49JQVf | 6.00 | 2 (narrow) | Wicked Oddities: selective poisoning for clean-label attacks. Accepted; similar quality, narrower evaluation. |

**Round-1 bracket:** between ~4 and ~7 (clearly above the 3.0–3.5 weak anchors, within the middle band).

**Round-2 narrowing:** BadDet+ is clearly stronger than the 4.33–4.75 rejected papers (VSSC, Backdoor in Seconds, PADetBench). It is comparable to the 5.75–6.33 accepted papers (Efficient Backdoor Attacks, Wicked Oddities, VLOOD) but slightly stronger due to its diagnostic contributions, physical-world validation, and evaluation breadth. The main weakness holding it back from the 7+ range (papers like the dataset bias survey and robust classifier at 8.0) is the missing variance reporting and the hyperparameter gap.

**Final score:** 6.5 — a solid paper with meaningful contributions and fixable weaknesses, in the accept range comparable to the strongest backdoor-attack papers in the calibration corpus.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>