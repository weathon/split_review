Now let me write the final review.

## Summary

BadDet+ proposes a unified log-barrier penalty framework for backdoor attacks on object detectors, covering both region misclassification (RMA) and object disappearance (ODA). The paper also makes a significant diagnostic contribution by identifying evaluation blind spots in prior work (ASR ignoring retained labels, mAP as a poor ODA proxy, lack of trigger scaling/placement robustness tests, and dependence on curated datasets).

## Strengths

1. **Unified log-barrier formulation for both RMA and ODA** — The paper proposes a single penalty term (Eq. 1/2) that treats ODA as a special case of RMA (target = background). This is a clean, principled contribution that goes beyond prior works which design separate attack mechanisms. (Section 4, paragraph 2)

2. **Drastic reduction of true-class duplicate detections in RMA** — On COCO, BadDet+ reduces TDR@50 to 2.78 (FCOS) and 3.18 (Faster R-CNN) while retaining ASR@50 near 99%, whereas BadDet leaves TDR@50 at 75.94 and 44.74 respectively (Table 2). This directly addresses the overlooked failure mode of "retained labels" that the paper diagnoses.

3. **Systematic diagnosis of evaluation blind spots in prior object-detection backdoor work** — Section 3 identifies four specific limitations (ASR ignoring retained labels, mAP as poor ODA proxy, no trigger scaling/placement tests, reliance on curated datasets). This provides a methodological foundation that goes beyond any single attack and is a genuine service to the community.

4. **Introduction of the True Detection Rate (TDR) metric for RMA** — TDR (Section 5.2) quantifies the proportion of trigger-bearing objects that still receive a correct-class detection. This is a cleaner evaluation than the previously used single-number ASR, which could hide duplicate-detection failures.

5. **Consistent effectiveness across four architectures and two datasets with physical-world transfer** — BadDet+ is evaluated on FCOS, Faster R-CNN, DINO, and YOLOv5 on both COCO and MTSD (with physical transfer to PTSD). It shows strong ASR and low TDR in nearly all configurations (Tables 1–4), and the synthetic-to-physical transfer results on PTSD substantially outperform prior methods.

6. **Demonstration that data poisoning alone is insufficient** — Figure 3 shows that increasing the poisoning ratio for existing methods does not reliably produce strong backdoors without degrading clean mAP, motivating the stronger threat model adopted in the paper.

## Weaknesses

### Fatal

None.

### Major

1. **Unequal poisoning ratios in the main comparison tables** — BadDet+ is evaluated at a 50% poisoning ratio (stated in §5.1), while the comparison methods (BadDet, UBA, Align, Morph) are run at their default poisoning ratios from the original papers. The paper acknowledges this and provides a partial remedy in Figure 3, which sweeps poisoning ratios. However, the headline results in Tables 1–4 are not apples-to-apples. Since Figure 3 shows that for DINO, BadDet's TDR drops as poisoning ratio increases, the advantage in the main tables may be partially attributable to the higher poisoning budget rather than the penalty term itself. The authors should either report baselines at 50% in the main tables or explicitly quantify how much of the gap closes under equal poisoning.

2. **YOLOv5 RMA failure** — Table 4 shows that for YOLOv5 RMA, BadDet+ (ASR 91.97, TDR 7.54) is strictly *worse* than BadDet (ASR 96.57, TDR 3.14) on fixed placements, and also worse on random placements. The paper acknowledges this and states "λ=0 is optimal for this architecture" — i.e., the penalty offers no benefit. This is a genuine failure mode for the proposed method on a widely used detector. The paper speculates about "detector-specific characteristics" and points to Appendix A.8 (not available in the submitted manuscript). A concrete explanation or explicit scope limitation is needed. This does not invalidate the method (which works well on other architectures), but it weakens the claim of a "unified and principled" framework.

### Minor

3. **The per-object evaluation protocol is a departure from prior work with unexamined limitations** — Section 5.2 states that "for both ODA and RMA, we evaluate each poisonable object independently: for every object, we create a separate test instance in which only that object is poisoned." In practice, an adversary might trigger multiple objects simultaneously, and the model's behavior could differ (e.g., due to competition between detections). The paper does not discuss this limitation or compare the per-object protocol to the all-objects-poisoned protocol.

4. **Missing hyperparameter values for ρ, τ, τ' in the main text** — The IoU threshold ρ and the confidence boundaries τ (for independent-logit detectors) and τ' (for softmax-based detectors) are introduced in §4.1 but their default values are not stated in the main text. While ρ likely defaults to 0.5 (standard), τ and τ' are not given. These should be reported for reproducibility.

5. **Threat model framing asymmetry** — The paper criticizes existing methods for relying on unrealistic assumptions (e.g., curated datasets, fixed trigger scales) and then proposes a method that assumes training-time control over the loss function — a stronger, arguably less realistic assumption than simple data poisoning. The paper justifies this (Section 4, "Threat Model") by showing data-poisoning alone is insufficient (Figure 3) and notes it is standard in the image classification literature. The contribution is still valid, but the motivation framing should be more careful to acknowledge that the two types of assumption are on different axes.

6. **PTSD physical-world transfer gap is not highlighted** — Table 3 shows BadDet+ PTSD results with ASR@50 around 59–85% (Fixed) depending on architecture, which is far from the near-100% MTSD results. While the paper reports these numbers honestly and they still outperform baselines, calling the method "Robust" in the title creates an expectation that is only partially met by the physical results. The paper could discuss this gap more explicitly.

### Trivial

None.

## Nice-to-Haves

- An analysis of sensitivity to the IoU threshold ρ used in the penalty term would strengthen the method.
- A runtime or training-cost comparison between BadDet+ and standard training / baselines would help assess practical overhead, since the penalty adds a forward-pass-time IoU computation for each pair of predictions and ground-truth boxes.
- Evaluating on more diverse defense methods (beyond FT and FT-SAM) would strengthen the claim that detection-specific defenses are needed. The paper scopes this out, which is acceptable, but it leaves the defense evaluation narrow.

## Removed Points

- **Theoretical analysis claim in abstract not delivered in main text:** The abstract states "We further present a theoretical analysis..." and the paper explicitly says "In Appendix A.7, we provide a more formal perspective on the induced optimization behavior." The appendix is stripped by the parsing pipeline (as noted in the paper). Per the review guidelines, parser-stripped sections exist in the original submission and should not be penalized. This criticism is removed.

- **Strength about "theoretical characterization in Appendix A.7":** Cannot verify due to appendix stripping. Removed.

- **Inference/training cost criticism:** While a runtime analysis would be useful (moved to Nice-to-Haves), this is not a core flaw. The paper states it provides "a computational analysis in Appendix A.6" (also stripped). Removed as a weakness.

- **Criticism about limited defense evaluation scope:** The paper explicitly scopes itself to FT and FT-SAM (§2.2), acknowledging other defenses are out of scope. A paper should be evaluated on what it does, not on what it explicitly sets aside. Moved to Nice-to-Haves.

## Novel Insights

None beyond the paper's own contributions. The key insight from the reviews — that the per-object evaluation protocol may not capture multi-object competition effects — is worth flagging but stems from the paper's own design choices rather than uncovering something unexpected.

## Suggestions

1. **Run baseline methods at the same 50% poisoning ratio used for BadDet+** and report those numbers in a revision of Tables 1–4, or explicitly quantify how much of the advantage shrinks. This would isolate the effect of the penalty from the effect of higher poisoning.

2. **Either explain the YOLO RMA failure or explicitly scope it out** as an architecture-specific limitation in the abstract and conclusion. The fact that λ=0 is optimal means the method provides zero benefit there; readers should be told this upfront rather than discovering it in a paragraph three pages in.

3. **State the default values of ρ, τ, and τ' in the main text** for reproducibility.

4. **Discuss the limitation of the per-object evaluation protocol** and ideally provide a small experiment comparing it to the all-objects-poisoned setting to show conclusions are robust.

## Score and Decision

**Calibration procedure:**

**Round 1 (Bracketing)** — Three parallel queries for backdoor/object-detection papers in the weak (score < 3.5), middle (3.5–7.5), and strong (>7.5) bands:
- Weak band anchors (avg 3.0–3.25): "Certified Copy" (3.0), "Deferred Backdoor Functionality" (3.0), "Adversarial Instance Attacks" (3.0), "LeBD" (3.25). All rejected papers with limited contributions or major methodological gaps. The BadDet+ paper is clearly stronger.
- Middle band anchors (avg 4.33–6.33): "VSSC Trigger" (4.33, rejected), "Backdoor in Seconds" (4.75, rejected), "Test-Time Backdoor Attacks" (4.50, rejected), "Backdooring VLMs with OOD" (6.33, accepted). BadDet+ is stronger than the 4.33–4.75 papers and comparable to the 6.33 paper.
- Strong band anchors (avg 7.6–8.0): Papers scoring 8.0 are on unrelated topics (dataset bias, diffusion classifiers, watermarking, LiDAR detection). BadDet+ does not reach this level.

Initial bracket: **5.5–7.0**.

**Round 2 (Narrowing)** — Querying inside the bracket for backdoor-attack papers with strong evaluation:
- "Efficient Backdoor Attacks" (5.75, accepted): addresses a practical scenario with good experiments but has runtime/scope limitations. BadDet+ has broader architecture coverage and a diagnostic contribution.
- "PADetBench" (4.75, rejected): a benchmark paper with a different focus; BadDet+ is clearly stronger.
- "Demystifying Poisoning Backdoor" (5.75, accepted): theoretical contribution; BadDet+ is comparable in quality but different in nature.
- "BaDExpert" (6.25, accepted): defense paper with strong empirical validation. BadDet+ is comparable.

Final assessment: BadDet+ sits at approximately the same level as the accepted papers in the 5.75–6.25 range. Its diagnostic contribution and evaluation breadth are strengths, but the unequal poisoning ratio comparison and YOLO failure mode prevent it from reaching the 6.5+ tier. 

**Score: 6.0** — A solid paper with a real contribution (the diagnostic analysis alone is useful) and a well-motivated method. The two major weaknesses are concrete and fixable; neither is fatal.

**Decision: Accept**

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>