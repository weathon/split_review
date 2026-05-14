Now I have all the information I need. Let me write the consolidated review.

## Summary

This paper diagnoses evaluation blind spots in prior object-detection backdoor attacks (RMA/ODA), proposes new metrics (TDR, instance-level ASR), and introduces BadDet+, a unified framework that augments the detector's training loss with a log-barrier penalty to suppress original-class predictions on trigger-bearing objects. The method is evaluated across two datasets (including physical transfer to PTSD), four architectures, multiple trigger placements, and two defense settings, achieving high ASR with near-zero TDR in RMA while preserving clean mAP.

## Strengths

- **Systematic diagnosis of evaluation blind spots (Section 3).** The paper identifies four specific, reproducible failures in prior work: ASR ignoring retained duplicate detections in RMA, mAP conflating multiple failure modes in ODA, lack of trigger-scale/placement robustness testing, and dependence on curated datasets. These are non-obvious and will improve evaluation standards for future work.

- **Introduction of TDR and instance-level ASR as corrective metrics.** TDR cleanly captures the duplicate-detection failure mode that ASR misses, and the instance-level ASR protocol evaluates each poisoned object independently. Both are principled and directly address the identified blind spots.

- **Clean, unified penalty formulation.** The log-barrier penalty (Eq. 1/2) treats ODA as a special case of RMA (target class = background), unifying both attack types under a single mechanism. The soft-constraint design — activating only when original-class logits exceed a threshold — is well-motivated by the diagnosis in Section 3. Results confirm it achieves high ASR with TDR@50 ≤ 3.18% on COCO RMA while maintaining clean mAP within ~2 points of baseline on most architectures.

- **Convincing demonstration that data-poisoning alone is insufficient (Figure 3).** The poisoning-ratio analysis shows that even at 100% poisoning, UBA and BadDet cannot simultaneously achieve high attack success and high clean mAP, whereas BadDet+ forms a tight cluster in the desirable region. This empirically motivates the stronger threat model the paper adopts.

- **Thorough experimental scope.** Evaluation spans COCO and MTSD/PTSD (physical transfer), four architectures (FCOS, Faster RCNN, DINO, YOLOv5), fixed and random trigger placements, both RMA and ODA, poisoning-ratio analysis, and defense evaluation with variance (10-run box plots for FT/FT-SAM). This is substantially more comprehensive than prior backdoor detection papers.

## Weaknesses

### Fatal
None.

### Major
- **Main results (Tables 1–4) lack variance estimates.** The paper reports single numbers for mAP, ASR@50, and TDR@50 across the core COCO and MTSD experiments with no indication of how many runs these represent or any measure of stability. Given that backdoor attacks are sensitive to random seeds and optimizer stochasticity, the reader cannot assess whether BadDet+'s advantages over baselines are systematic or reflect a single favorable run. The defense evaluation (Figure 2) shows the authors *can* compute variance (10-run box plots), making this omission in the main results conspicuous. While training object detectors is expensive, reporting at least mean±std over 3 seeds for one representative pair (e.g., FCOS on COCO) is necessary to support the headline quantitative claims.

### Minor
- **The specific benefit of the log-barrier penalty over other loss modifications is not isolated.** The paper adopts a stronger threat model (loss manipulation) than all baselines (data-poisoning only) and acknowledges this distinction. However, the paper's empirical claims conflate two factors: (i) having access to loss manipulation, and (ii) the specific log-barrier formulation. A λ=0 ablation under the *same* data-poisoning scheme (same triggers, same label changes) across all architectures would isolate the penalty's contribution. The paper provides this for YOLO (finding λ=0 is optimal), but not for FCOS, Faster RCNN, or DINO. Without this, it is unclear whether *any* reasonable penalty that suppresses original-class logits would work equally well, or whether the log-barrier's specific properties are essential.

- **Hyperparameters ρ (IoU threshold for penalization) and τ (confidence boundary) are not stated.** The penalty in Eq. 1/2 depends on these values, but the paper does not report them or analyze sensitivity to them. While defaults can be inferred (ρ=0.5 is standard, τ=0 corresponds to a 50% sigmoid confidence), the values should be explicitly stated for reproducibility.

### Trivial
- The notation τ is used in Eq. 1 for the sigmoid-based formulation and τ' in Eq. 2 for the softmax-based formulation, but the relationship between τ and τ' is not explained. Clarifying how the confidence boundary translates between the two logit normalization schemes would help.

## Nice-to-Haves

- Comparing against alternative penalty functions (e.g., hinge-like max(0, σ(z-τ)), or an explicit margin loss) under the *same* threat model would strengthen the claim that the log-barrier's specific form matters. This is a natural extension but goes beyond what is necessary for acceptance.
- A qualitative comparison (e.g., detection visualizations for BadDet+ vs. BadDet on the same image, showing the duplicate-detection failure mode and its removal) would help readers connect the numbers to concrete behavior.
- Reporting the distribution of IoU between trigger-bearing ground-truth boxes and the predictions caught by the penalty during training would illustrate whether the penalty affects the correct predictions.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Incomparable threat models" as a fatal/major gap.** The paper explicitly acknowledges the stronger threat model ("Compared to related existing work, our design assumes a stronger adversarial setting") and motivates it empirically (Figure 3). The comparison against baselines serves to show what current methods can achieve under their own paradigms, not to claim an apples-to-apples comparison. The paper's contribution includes demonstrating that data-poisoning alone is insufficient, which makes the comparison informative. This criticism is overstated; the λ=0 ablation (preserved above as a minor weakness) is the appropriate way to isolate the penalty's contribution.

- **Criticism about missing appendix sections.** The Harsh Critic references Appendix A.5, A.7 as stripped. Per policy, these exist in the original submission and were removed by the parser. Not a valid weakness.

- **"Not compared against alternative penalty functions" as a major weakness.** The paper is not required to exhaustively compare against every possible loss modification under the same threat model to validate its specific contribution. This is a nice-to-have rather than a core flaw, and I have moved it to Nice-to-Haves.

- **"Scope creep" criticism about missing defense evaluations.** The paper explicitly scopes out pruning-based and test-time defenses (Section 2.2, Section 6) and acknowledges this limitation. Criticizing its absence is ignoring the paper's stated scope.

## Novel Insights

The reviewer critiques converge on one theme that the paper's authors should reflect on: the paper's strongest contribution is arguably its *diagnosis* of evaluation blind spots (Section 3) rather than the specific penalty formulation. The TDR metric and the demonstration that data-poisoning alone is insufficient are robust findings that stand independently of whether the log-barrier penalty is the optimal instantiation. The penalty formulation, while clean and effective, would benefit from a sharper ablation isolating its specific effect from the general advantage of loss manipulation access.

## Suggestions

1. **Report variance for the main results.** Add a small table or footnote showing mean±std over at least 3 seeds for FCOS on COCO (the most standard setting), and briefly state in the setup that remaining evaluations use a single seed due to computational cost.
2. **Add a λ=0 ablation column to Tables 1–4.** Use the same data-poisoning scheme as BadDet+ but set λ=0, to show what data-poisoning alone achieves under the same trigger/label regime.
3. **State the chosen values of ρ and τ** in Section 4.1 or 5.1, and if space permits, add a short sensitivity table in the appendix.
4. **Clarify the τ vs τ' relationship** in the softmax formulation (Eq. 2).

---

## Score and Decision

### Calibration Anchors

| Path | Avg Score | Comparison |
|------|-----------|-----------|
| `/home/wg25r/review_agent/human_reviews_2026/1h7JvTbIYJ.md` | 2.00 | This paper is substantially stronger — it has a novel formulation (not just porting existing attacks), systematic diagnosis of evaluation issues, and thorough empirical evaluation. The 2.00 paper reuses standard triggers with no new attack mechanism. |
| `/home/wg25r/review_agent/human_reviews_2026/j9k3Oamba8.md` | 3.00 | The GoBA paper was seen as technically incremental (simple data poisoning adapted to VLA). The current paper has a novel penalty formulation, new metrics, and deeper analysis, making it clearly stronger. |
| `/home/wg25r/review_agent/human_reviews_2026/Y1UhUy7qAQ.md` | 3.50 | The VOS attack paper was a "first" but method was straightforward adaptation. The current paper has a more sophisticated attack mechanism (log-barrier penalty) and more thorough evaluation with multiple architectures and physical transfer. |
| `/home/wg25r/review_agent/human_reviews_2026/gJgcwQSMiq.md` | 3.50 | The RAG-DM backdoor paper received criticism for unfair baselines and limited scope. The current paper's evaluation is more comprehensive and its claims are better supported. |
| `/home/wg25r/review_agent/human_reviews_2026/qqWPNiig1Q.md` | 4.67 | The batch-oriented attack paper had mixed reviews (one reviewer saw limited novelty). The current paper has clearer novelty (diagnosis of evaluation blind spots + new unified formulation) and more thorough evaluation. |
| `/home/wg25r/review_agent/human_reviews_2026/Kpij6oOnJl.md` | 5.00 | Accepted Poster. The CLIP detection paper had a novel insight (shallow vs deep matching) but limited baselines. The current paper has a similar level of contribution — novel diagnosis + clean solution — with a more thorough empirical evaluation. |
| `/home/wg25r/review_agent/human_reviews_2026/O02qsgSUtY.md` | 5.00 | Accepted Poster. The STEDiff paper identified spatio-temporal redundancy with practical acceleration. The current paper is comparable in contribution depth — both identify underexplored phenomena and propose practical solutions. |
| `/home/wg25r/review_agent/human_reviews_2026/jUuXNrG7wh.md` | 6.00 | Accepted Poster. The OVD false-positive paper had a clear problem diagnosis and a simple, well-validated solution. The current paper has a similar structure (diagnosis → proposed solution → thorough evaluation) but slightly more variance-reporting gaps. |

**Decision Rationale:** The paper makes solid contributions: the diagnosis of evaluation blind spots (Section 3) is genuinely useful to the community, the TDR metric addresses a real gap, and the unified penalty formulation is clean and effective. The evaluation is more comprehensive than most prior backdoor detection papers. The main weakness — lack of variance reporting for central results — is significant but fixable, and the λ=0 ablation is a modest gap. No fatal flaws are present. Relative to anchors, the paper sits comfortably in the 5.5–6.5 range, comparable to Poster-level papers.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>