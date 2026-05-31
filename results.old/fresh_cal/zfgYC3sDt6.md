Now I have all the information needed. Let me write the consolidated review.

---

## Summary

This paper studies confidence calibration in prompt-tuned CLIP models. It identifies a miscalibration trade-off: CoOp (trained with cross-entropy loss) becomes overconfident on new classes by increasing textual feature divergence, while KgCoOp (which regularizes toward zero-shot features) becomes underconfident on base classes because its accuracy improves but confidence stays anchored. To resolve this, the authors propose Dynamic Outlier Regularization (DOR), which samples "relevant but non-overlapping" textual outliers from WordNet and regularizes their features toward zero-shot CLIP features during fine-tuning. Experiments on 11 datasets with 6 prompt-tuning methods show large and consistent improvements in calibration (e.g., CoOp new-class ECE drops from 14.58% to 6.49%) while maintaining or improving accuracy on both base and new classes.

---

## Strengths

1. **Large and consistent calibration improvements on new classes.** Table 1 shows DOR reduces new-class ECE substantially across all six prompt-tuning methods. For CoOp, ECE drops from 14.58% to 6.49% (an 8.09% absolute reduction); for CoCoOp, from 6.14% to 4.02%; for DEPT, from 14.58% to 7.50%. These improvements are consistent across four different calibration metrics (ECE, ACE, MCE, PIECE). This is the paper's strongest evidence.

2. **Novel analysis of the miscalibration trade-off through textual divergence.** Section 3.2 provides a quantitative explanation linking cross-entropy training to increased feature divergence (FD) scores of textual labels, which widens the logit gap for new classes and causes overconfidence in CoOp. It also explains why KgCoOp's regularization produces underconfidence on base classes (accuracy improves while confidence stays anchored). This analysis goes beyond prior work by explaining miscalibration on both base and new classes.

3. **Algorithm-agnostic and broadly applicable.** DOR is demonstrated with six different prompt-tuning methods (CoOp, CoCoOp, MaPLe, KgCoOp, DEPT, TCP) in Table 1, and extended to visual fine-tuning methods (VPT, CLIP-adapter) with image outliers in Table 4. This breadth of applicability is a concrete advantage — many prior calibration methods target only a single tuning approach.

4. **DOR improves accuracy alongside calibration.** Table 2 shows consistent harmonic-mean accuracy improvements across methods. For example, CoOp's HM accuracy increases from 72.36% to 77.61%, and DEPT's from 74.37% to 77.60%. This demonstrates that DOR does not trade accuracy for calibration but benefits both.

5. **Domain generalization robustness.** Table 3 shows DOR substantially improves calibration on out-of-distribution target domains — CoOp average target ECE drops from 7.18% to 4.89%, and MaPLe from 5.23% to 4.58% — while also improving accuracy. This is a practically important result for real-world deployment.

---

## Weaknesses

### Fatal
None.

### Major

1. **Claim of "without calibration trade-offs" is overstated.** The paper states (lines 348, 352) that DOR works "without calibration trade-offs on base and new classes" and "without compromising the vanilla fine-tuning objectives." However, Table 1 shows that for 4 out of 6 methods, base-class ECE increases (worsens) after adding DOR: CoCoOp (3.60→4.22), MaPLe (2.75→2.83), KgCoOp (5.82→6.07), DEPT (6.04→7.67), TCP (4.71→4.79). For DEPT the increase is particularly large (+1.63 on base ECE). The trade-off is dramatically reduced — DOR does not make base-class calibration catastrophically worse while fixing new-class calibration — but the claim of *no* trade-off is imprecise. This should be qualified to reflect that the trade-off is substantially mitigated, not eliminated for all methods.

### Minor

2. **Outlier selection procedure under-analyzed.** The selection pipeline (filtering WordNet nouns → ranking by zero-shot similarity to base classes → selecting top-K) introduces several design choices whose impact is not measured:
   - **No ablation on K** (only K=5000 is used). It is unclear whether performance is sensitive to this hyperparameter.
   - **No comparison against random WordNet nouns** (without similarity ranking) to isolate whether the ranking procedure is essential or merely a convenience.
   - **No runtime/memory cost reported** for the preprocessing step, despite the paper claiming DOR is "easy-to-use" (line 261). For datasets with many base classes (e.g., ImageNet with 1000 classes), computing pairwise similarities across ~150K candidate words × all base classes is non-trivial.
   
   Table 5 (near-OOD vs. far-OOD) shows that near-OOD (the paper's default) outperforms far-OOD, which supports the selection strategy. However, the missing ablations leave uncertainty about how much of DOR's benefit comes from the specific selection process vs. simply having any regularization target outside the base classes. The authors should address this in a revision.

3. **Accuracy improvement mechanism not explained in sufficient depth.** The paper states (line 359) that DOR "preserves the zero-shot generalization on new classes." This explains matching zero-shot performance but does not explain why DOR sometimes *surpasses* zero-shot accuracy on new classes (e.g., MaPLe: 73.89% → 75.89% vs. zero-shot 74.32%; CoOp HM: 72.36% → 77.61% vs. zero-shot 71.90%). If DOR simply pulls features toward zero-shot, surpassing zero-shot suggests a non-trivial interaction with the CE loss that is not analyzed. A brief analysis — e.g., measuring feature similarity between DOR and zero-shot models and correlating it with accuracy gains — would strengthen the story.

4. **Hyperparameter sensitivity shown for only one method.** Figure 4 (λ sensitivity) shows results only for CoOp+DOR. The λ values used differ substantially across methods (λ=8 for CoOp vs. λ=2 for all others), so demonstrating robustness for at least one more method (e.g., MaPLe or TCP) would strengthen the claim that DOR is not fragile.

5. **No error bars or variance reported.** The paper states "results averaged over 3 runs" but no standard deviations are shown in any table. For the largest improvements (e.g., CoOp ECE 14.58→6.49), variance is unlikely to change the qualitative conclusion. But for smaller gains (e.g., KgCoOp ECE 4.48→3.99, an 0.49% reduction), error bars would clarify whether the difference is statistically meaningful.

### Trivial

6. **Figure 3 (logit gap analysis) shown only on DTD.** The paper's central explanatory figure — comparing logit gaps between base and new classes — is shown for a single dataset (DTD). Repeating this on a few more datasets would strengthen the claim that the pattern is general.

7. **M hyperparameter in FD score not specified.** The Feature Divergence score (Definition 3.1) uses M nearest neighbors, but the value of M used in experiments is never reported.

8. **Accuracy claim about CoOp is imprecise.** Line 360 says CoOp and MaPLe with DOR show improvements "outperforming zero-shot accuracy on new classes." For CoOp, the new-class accuracy (72.01%) is actually *below* zero-shot (74.32%). The HM accuracy does surpass zero-shot, but the phrasing as written is misleading.

---

## Nice-to-Haves

- An analysis of why DOR interacts with the CE loss to sometimes *improve* accuracy beyond zero-shot (point 3 above). This is not a core flaw — the empirical results are convincing regardless — but it would tighten the narrative.
- A brief discussion of the computational cost of the outlier selection step, to substantiate the "easy-to-use" claim.
- Showing λ sensitivity for a second method.

---

## Removed Points

These points were raised by the reviewers but are removed after cross-checking against the paper:

- **Causal explanation is "correlational not causal" (Harsh Critic).** The paper frames its analysis as an explanation ("leads to," "caused by") using empirical evidence that FD and confidence move together under varying λ. This is standard practice for empirical analysis papers. The method does not depend on a rigorous causal proof, and the reviewer acknowledges this ("the method itself does not depend on this causal story being proven"). This is an area-of-concern lens rather than a concrete problem with the paper as presented. → Removed.

- **WordNet version and exact filtering criteria not specified.** The paper's claim that DOR is easy-to-use does not collapse if version numbers are omitted. This is a trivial implementation detail that would be resolved in a code release. → Removed.

- **Strengths about "addressed an important problem" / "targeted an interesting question" (from Strength Finder).** No such generic strengths were present; the Strength Finder's outputs were all grounded in specific evidence. → No removals needed.

---

## Novel Insights

None beyond the paper's own contributions. The two reviews converged on the paper's core strengths and weaknesses and did not surface any observation that the paper itself does not already articulate or address.

---

## Suggestions

1. **Qualify the "no trade-off" claim** to reflect that DOR substantially reduces the calibration trade-off (with small base-class ECE increases for some methods) rather than eliminating it entirely.
2. **Add ablations on outlier selection:** (a) vary K (e.g., 100, 500, 1000, 5000, 10000), (b) compare ranked selection vs. random WordNet nouns, (c) report the runtime of the preprocessing step.
3. **Add error bars** to the main tables (or a statement that variance was negligible if true).
4. **Show λ sensitivity** for at least one additional method beyond CoOp.
5. **Provide a brief explanation** for why DOR can improve new-class accuracy beyond zero-shot, e.g., by measuring feature alignment between DOR and zero-shot models and correlating it with accuracy gains.

---

## Score and Decision

**Originality:** The paper identifies a specific, understudied calibration trade-off in prompt-tuned VLMs and proposes a motivated solution. While the idea of using outliers for regularization is not entirely new, the application to calibration in this setting and the specific selection strategy are novel.

**Importance of research question:** Calibration is critical for safe deployment of VLMs, and the paper addresses a practical problem that arises when fine-tuning widely-used models. High importance.

**Claims support:** The core claim — DOR improves new-class calibration while maintaining base-class performance — is well-supported by extensive experiments. The "no trade-off" sub-claim is slightly overstated but does not undermine the core contribution.

**Soundness of experiments:** 11 datasets, 6 methods, 4 calibration metrics, domain generalization, and extension to visual tuning. The evaluation is thorough. Missing ablations on outlier selection and lack of error bars are the main gaps.

**Clarity of writing:** Clear and well-structured. The motivation section is effective, and the method is explained concisely.

**Value to community:** High. DOR is simple, compatible with existing methods, and produces large improvements. It can be immediately adopted by practitioners.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>