Now I have sufficient calibration. Let me construct the final review.

**Round 1 bracket:** After the first calibration pass, the paper sits between the weak anchors (~2–3.33, all reject) and the strong anchors (8.0, accept). The middle-band anchor CoLLiS (5.0, reject) — a fellow semi-supervised LiDAR segmentation paper — is the most topically relevant. REPL has a more novel core idea than CoLLiS (pseudo-label refinement via masked reconstruction vs. multi-representation collaboration) and better ablations, but has a clear overclaiming issue. So the initial bracket is [5.5, 7.0].

**Round 2 narrowing:** A3Point (5.5, accept poster, LiDAR segmentation) has scores 6,6,8,2 and GOOD (6.0, accept poster, point cloud segmentation) has scores 6,6,6. Both are accepted with similar rigor levels. REPL is comparable to A3Point and GOOD in terms of experimental depth and contribution novelty, placing it at 6.0.

Now writing the review.

---

Let me think carefully about the weaknesses to include and their severity.

**Constructed Weaknesses:**

1. **Factual error in SOTA claim (Major):** The paper's text states "achieving the best performance at 1% and 50%" on SemanticKITTI, but Table 1 shows REPL at 54.7 mIoU, below LaserMix++ (56.2) and FrustumMix (55.7) at 1%. This is a factual discrepancy in the paper itself, not just a framing issue. The abstract's unqualified SOTA claim needs qualification.

2. **Theoretical analysis is post-hoc (Minor):** The empirical validation of Proposition 2's condition uses ground-truth labels unavailable during semi-supervised training. The paper doesn't claim it guides training — it's presented as post-hoc validation — but the introduction and framing overstate its role ("establishing the condition under which pseudo-label refinement improves...").

3. **Teacher-student agreement vs. student-only confidence not ablated (Minor):** The teacher is an EMA of the student, so predictions are highly correlated. An ablation replacing teacher-student agreement with student-confidence-only would isolate whether the teacher adds unique value.

4. **No explicit limitations section (Minor):** The paper discusses failure cases briefly (Figure 4) but has no dedicated limitations section discussing when the method might underperform (e.g., sparse regions, extreme class imbalance).

5. **No error bars / statistical significance (Trivial/Nice-to-have):** Single-run evaluation is standard practice in this benchmark setting (LaserMix, IT2, AIScene all report single runs). This is not a weakness that threatens validity; it's a nice-to-have.

Let me check: does standard practice in this field involve reporting error bars? Looking at the papers cited: LaserMix, IT2, AIScene all report single runs. So this is standard practice. I'll move this to nice-to-have.

Let me also consider the removed points.

The teacher-student agreement concern: The critic said "the teacher is an EMA of the student, so its predictions are highly correlated with the student's. The 'agreement' condition... may therefore detect voxels where both networks are confidently wrong together." This is a valid concern but needs to be verified as a real problem vs. a theoretical concern. The paper doesn't analyze this. I'll keep it as a minor weakness but weaken it.

Actually, thinking more carefully: in Mean Teacher (Tarvainen & Valpola, 2017), the teacher is an EMA of the student. This is a standard approach used in many semi-supervised learning papers. The fact that the teacher and student are correlated is well-known, but the agreement between them is still commonly used as a signal. The critic's concern is valid but very minor — it's a well-known limitation of the teacher-student paradigm, not something unique to this paper.

I'll keep it as a minor weakness because the paper could benefit from a student-only ablation, but it's not a structural flaw.

Let me now write the final review.## Summary

This paper proposes REPL, a semi-supervised LiDAR semantic segmentation framework that refines noisy pseudo-labels through a two-stage process: (1) detecting unreliable pseudo-labels via confidence-based teacher-student agreement with adaptive thresholds, and (2) correcting those unreliable predictions through masked reconstruction with a dedicated refiner network. The framework also introduces a training strategy combining mixed scenes and negative learning. The paper reports strong experimental results on nuScenes-lidarseg and SemanticKITTI, with the highest average mIoU across label ratios on both benchmarks.

---

## Strengths

- **Principled departure from post-hoc pseudo-label handling.** REPL directly corrects unreliable pseudo-labels via masked reconstruction rather than discarding or reweighting them. This is a clear conceptual advance over prior methods (e.g., confidence filtering in LaserMix, loss reweighting in IT2), and the ablation study (Table 2) shows that the refiner contributes a +9.1 mIoU gain over the supervised baseline (50.9 → 60.0).

- **Strong experimental results across benchmarks.** On nuScenes-lidarseg, REPL achieves the best performance at all four label ratios and exceeds the prior best (IT2) by +2.0 average mIoU (71.3 vs. 69.3). On SemanticKITTI, it achieves the highest average mIoU (61.6) and the best individual scores at 50% (65.9). Table 4's oracle-mask analysis (67.3 mIoU) honestly reveals the ceiling and upside for error detection, which is informative for future work.

- **Informative ablations and cost analysis.** Each loss component (ℒ_rsup, ℒ_runi, ℒ_mix) is shown to contribute additively (Table 2), and the symmetric cross-entropy benefit is isolated (Table 3). Table 7 reports the computational overhead of the refiner (+0.25s latency, +396 MB per batch) alongside the +9.1 mIoU gain — a quantitative trade-off rarely provided in LiDAR semi-supervised segmentation papers.

---

## Weaknesses

### Major

- **Factual error in SOTA claim within the paper body.** The paper states (Section 4.2): "On SemanticKITTI, REPL also showed strong results, achieving the best performance at 1% and 50%." However, Table 1 shows REPL achieves 54.7 mIoU at 1% on SemanticKITTI, which is *below* LaserMix++ (56.2) and FrustumMix (55.7) — making REPL third, not first. This is a factual discrepancy between the text and the paper's own data. The abstract and introduction also claim "state of the art in LiDAR semantic segmentation" without qualification, which overstates the results given that REPL is not uniformly top on all SemanticKITTI settings. The paper's overall contribution is strong enough that these claims do not need inflation. The text should be corrected and the SOTA framing appropriately qualified.

### Minor

- **Theoretical analysis is a post-hoc validation, not a design principle.** Proposition 2 derives a condition ζ > 0 under which refinement is beneficial, and Figure 2 empirically shows REPL operates in this regime. However, the quantities q (correction rate) and r (error introduction rate) used to compute ζ are measured against ground-truth labels that are unavailable during actual semi-supervised training. The paper does not claim the condition guides training — it is presented as empirical validation — but the introduction frames it as "establishing the condition under which pseudo-label refinement improves upon teacher-only baseline" in a way that implies more proactive guidance than the analysis delivers. The condition is mathematically valid, but its role is confirmatory rather than design-driving.

- **Teacher-student agreement component is not isolated.** The teacher is an EMA of the student, making their predictions highly correlated. The "agreement" condition for error detection uses both networks' predictions and adaptive thresholds. An ablation that replaces teacher-student agreement with a student-confidence-only baseline (keeping the same adaptive threshold) would clarify whether the teacher adds unique signal or if the student's own uncertainty suffices. This does not invalidate the method but is a missing diagnostic.

- **No explicit limitations discussion.** The paper mentions failure cases in one sentence (Section 4.3, "occasionally introduces errors by over-correcting") but has no dedicated limitations section. A candid discussion of when REPL may underperform — e.g., in highly sparse regions, for extremely rare classes, or under severe class imbalance — would strengthen the paper.

### Trivial

- None that survive filtering.

---

## Nice-to-Haves

- **Error bars / multiple runs.** The harsh critic flagged the absence of error bars as a "significant omission." However, single-run evaluation is the established standard in this benchmark setting (LaserMix, IT2, AIScene all report single runs). Reporting multiple runs would strengthen the evidence but is not required by community practice.
- **Discussion of the SemanticKITTI 1% gap.** LaserMix++ outperforms REPL at this setting by ~1.5 mIoU. A brief analysis of why (e.g., LaserMix++'s mixing strategy may be more beneficial in the extremely low-data regime) would improve the discussion.

---

## Removed Points

The following points from the inputs were removed:

1. *"Reproducibility: The paper does not mention the random seeds used, nor how the labeled/unlabeled splits were created."* — REMOVED per hard rules: requesting undisclosed hyperparameters or trivial implementation details is a nitpick. The split information and hyperparameters that are standard in this benchmark setting are provided.

2. *"Missing appendix, missing proofs in appendix"* — REMOVED per hard rules: the parser strips appendices; they exist in the original submission.

3. *"The teacher-student agreement may detect voxels where both networks are confidently wrong together"* — REMOVED as a standalone weakness. This is a known limitation of the teacher-student paradigm in semi-supervised learning generally, not specific to this paper. The concern is subsumed into the minor weakness about the missing ablation.

4. *Several strengths from the Strength Finder were removed as generic/superficial* (e.g., "the paper addressed an important problem", "the paper is clearly written") — these add no concrete information.

---

## Novel Insights

None beyond the paper's own contributions.

---

## Suggestions

- Correct the factual error in Section 4.2: replace "best performance at 1% and 50%" with the accurate statement. Qualify the abstract's SOTA claim (e.g., "achieves state-of-the-art average performance across two benchmarks" or "achieves competitive results with state-of-the-art on multiple settings").
- Add a brief ablation comparing teacher-student agreement vs. student-confidence-only for error detection. If the teacher adds no unique value, the framework simplifies; if it does, the result is informative either way.
- Add a limitations paragraph discussing scenarios where the refiner may struggle (e.g., extreme sparsity, rare classes).
- In the theoretical analysis (Section 3.5), clarify explicitly that the empirical verification of ζ > 0 is computed using ground-truth labels and is therefore a post-hoc sanity check, not a training-time guide.

---

## Score and Decision

### Calibration Anchors

| Anchor ID | Avg Score | Round | Comparison |
|-----------|-----------|-------|------------|
| XGYxmsrdok (TopoRefine) | 3.33 | R1 | LiDAR topology refinement; weaker contribution, rejected. REPL is substantially stronger. |
| R6I8P4DuRf (Instance-Level Retrieval) | 3.20 | R1 | Adaptive labeling; weaker and withdrawn. REPL is stronger. |
| 6ZZzta9lRx (Context-Enriched Embeddings) | 2.00 | R1 | 3D scene understanding; clearly rejected. REPL is much stronger. |
| XhkPu4AJ2n (CoLLiS) | 5.00 | R1,R2 | Semi-supervised LiDAR segmentation; most topically similar. CoLLiS scored lower due to incremental novelty. REPL has a more novel core idea and better experiments. REPL is stronger. |
| 8xjCp4OA6k (TriLA) | 4.00 | R1 | LiDAR domain adaptation; rejected/withdrawn. REPL is clearly stronger. |
| 3knS4J9isg (PLOT) | 5.00 | R1 | Pseudo-labeling for 3D detection; rejected. REPL is stronger. |
| l7Cwq08AO0 (A3Point) | 5.50 | R2 | LiDAR semantic segmentation under adverse weather; accepted (poster). REPL has comparable rigor and a more novel core contribution. REPL is comparable or slightly stronger. |
| HyNWlZd4iO (GOOD) | 6.00 | R2,R3 | Point cloud semantic segmentation (OSTTA); accepted (poster). Solid experimental contribution with identifiable weaknesses. REPL is comparable. |
| 9vlS8PSGG7 (Point2RBox-v3) | 7.00 | R2 | Pseudo-label refinement for oriented object detection; accepted (poster). Stronger experimental story and fewer overclaiming issues. REPL is slightly weaker. |

**Round 1 bracket:** [5.5, 7.0]  
**Round 2 narrowing:** Compared against A3Point (5.5, accepted) and GOOD (6.0, accepted), REPL has a comparable or slightly stronger contribution but a clear overclaiming issue that needs correction. Compared against Point2RBox-v3 (7.0, accepted), REPL has a weaker experimental story (no error bars, factual error in claims).  
**Final score:** 6.0 — The paper's core contribution (direct pseudo-label refinement via masked reconstruction in semi-supervised LiDAR segmentation) is novel and well-supported by experiments. The main issue is a factual error in the paper's own SOTA claims that needs correction. With that fixed, the paper merits acceptance.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>