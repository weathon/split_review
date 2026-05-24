Now I have all the information needed. Let me write the consolidated review.

## Summary

KOALA proposes a reactive adversarial detector that flags attacks when class predictions from two complementary metrics—KL divergence (sensitive to dense perturbations) and an L₀-based distance (sensitive to sparse perturbations)—disagree. The detector operates as a nearest-prototype classifier and provides a formal proof (Theorem 1) that under certain conditions no norm-bounded perturbation can flip both predictions simultaneously, forcing disagreement and guaranteeing detection. Experiments on ResNet/CIFAR-10 and CLIP/Tiny-ImageNet are presented.

## Strengths

- **Formal guarantee of detection correctness under explicit conditions**: Theorem 1 (Section 3.2) establishes conditions under which adversarial detection is provably guaranteed via metric disagreement. The theorem is accompanied by a proof sketch in the main text and a reference to a full proof in the appendix. This theoretical framing distinguishes KOALA from prior empirical detectors that lack such guarantees.

- **Lightweight fine-tuning with clean images only**: The training procedure (Section 3.3, Equation 6) uses only clean, non-adversarial images, requiring no adversarial retraining or architectural modifications. All experiments confirm this (Tables 3-4 note: "All finetuning was done using clean images only").

- **Interesting empirical finding on adversarial robustness (Experiment 3)**: The KL+L₀ objective substantially improves adversarial accuracy on ResNet/CIFAR-10 (57.32% vs 45.5% baseline under PGD ε=2/255, Table 3), a significant and non-obvious result. The paper provides a reasonable explanation based on the complementarity of the two metrics.

- **Ablation study validating metric complementarity**: Table 2 compares several metric pairings and shows KL+L₀ outperforms alternatives on ResNet/CIFAR-10 across all four reported metrics, supporting the paper's central hypothesis that these metrics are complementary.

## Weaknesses

### Major

1. **Non-standard detection metrics conflate detection with correct classification**. The confusion matrix definitions in Experiment 1 (lines 192–195) define a True Positive (TP) as `[a=1] ∧ [ (â, ŷ) = (1, ⊥) ∨ (â, ŷ) = (0, y*) ]`. Under this definition, an adversarial input that is *correctly classified* (â=0, ŷ=y*)—meaning the detector never flagged it—counts as a detection success. A completely non-flagging detector that correctly classifies every adversarial example would achieve 100% recall under this definition. This means:
   - The headline claims in the abstract ("precision 0.94, recall 0.81 on ResNet/CIFAR-10") and the recall=1.0 on the theorem-compliant subset are not interpretable as standard detection performance. They conflate "attack causes disagreement (detected)" with "attack was ineffective (correctly classified)."
   - The experimental validation of the theorem's guarantee is ambiguous: recall=1.0 on the compliant subset could mean all attacks were flagged, or all attacks were correctly classified (not flagged), or a mix. These are very different outcomes.
   - This does not invalidate the paper's results, but the detection numbers cannot be taken at face value as standard detection metrics.

2. **No comparison to any prior detection method**. The experiments compare only different metric combinations (ablations). No comparisons to existing detection approaches (Mahalanobis distance, LID, feature squeezing, CADet, Bayesian uncertainty, or any other method) are provided. Without baselines, it is impossible to assess whether KOALA's performance is competitive. Given that the paper claims practical utility ("lightweight, plug-and-play solution"), this is a significant gap.

### Minor

3. **Theorem-compliance criterion for the test-set split is not operationalized**. The paper partitions test sets into "Theorem-Compliant" and "Non-Compliant" samples based on whether they "satisfy the conditions of Theorem 1" (lines 189–190), but does not specify the algorithmic procedure for determining compliance: how Γ_i(ε) is computed, which coordinate is used, or how the adversarial class prototype ĉ is chosen. This hinders reproducibility of the primary validation experiment. The full appendix (stripped by the parser) may contain this information, but it should be in the main text for this critical experiment.

4. **No evaluation against adaptive attacks**. The theoretical guarantee holds for any norm-bounded adversary on compliant samples, but on non-compliant samples (which are the majority for CLIP/Tiny-ImageNet: 4490/5000 samples at ε=2/255), the detector has no formal protection. An adversary aware of the detector could craft perturbations that specifically avoid triggering metric disagreement while still causing misclassification. Adaptive attacks are standard practice in the adversarial defense literature and their absence is a gap.

5. **Key hyperparameters not ablated**. The L₀ distance depends on threshold τ (set to 0.75) and smoothness φ (set to 0.5), and the loss weights are heavily asymmetric (ω_L₀=0.9, ω_KL=0.1). None of these are ablated, so it is unclear how sensitive the results are to these choices.

### Trivial

None.

## Nice-to-Haves

- Report standard detection metrics (TP = attacked ∧ flagged) alongside the paper's current definition, to enable direct comparison with prior work.
- Include at least 2–3 established detection baselines on the same models and attacks.
- Ablate the L₀ threshold τ and smoothness φ, and the loss weight ratio.
- Provide confidence intervals or variance estimates for the reported metrics.

## Removed Points

- **Harsh critic's point about Figure 1 labeling being backwards**: The figure labels the KL path as "Sparse Attack" and the L₀ path as "Dense Attack," which initially seems to conflict with the stated sensitivities (KL for dense, L₀ for sparse). However, examining the figure caption reveals the intended interpretation: each path detects the complementary attack type (KL is violated by sparse attacks, L₀ by dense attacks). This is clarified in the caption text and is internally consistent once parsed correctly. The point was based on a misreading.
- **Harsh critic's point about L₀ metric being "not standard" and "heuristic"**: The paper clearly defines this as a thresholded count (Equation 2), which is a valid design choice. The threshold τ is a hyperparameter, which the paper acknowledges. The critic's characterization as "heuristic" implies a lack of principled grounding, but the metric is well-defined and motivated.
- **Harsh critic's point about proof sketch being "too vague to be assessed"**: The paper explicitly states "A complete proof of Theorem 1 is provided in Appendix B" and provides a structured sketch with three propositions. Given that the appendix was stripped by the parser, this criticism cannot be evaluated. The sketch as presented conveys the core intuition.
- **Harsh critic's point about Assumption A3 being "quite restrictive"**: While this is a valid concern, it is presented as speculation rather than an identified concrete problem in the paper. The assumption is clearly stated and the paper acknowledges it as a "mild and practical condition." I have retained a related minor weakness but softened the framing.
- **Strength Finder's generic strengths** (e.g., "this paper addressed an important problem"): Removed as generic/superficial.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the metric definition concern prominently but do not provide any synthesis that the paper itself does not already contain.

## Suggestions

1. **Recompute all detection metrics using the standard definition**: TP = attacked ∧ flagged, FN = attacked ∧ not flagged. Report these alongside the current metrics. This would clarify exactly what fraction of attacks are actually *flagged* (vs. merely ineffective) and would align with the paper's own definition of detection ("flag input as attack when predictions disagree").
2. **Specify the compliance determination procedure explicitly**: Provide the exact computation of Γ_i(ε) and the decision rule for splitting compliant vs. non-compliant samples.
3. **Add at least 2-3 baseline detection methods** (e.g., Mahalanobis distance in feature space, LID) to contextualize KOALA's performance.
4. **Validate the theoretical claim directly**: On the compliant subset, report the fraction of adversarial examples that are actually flagged (â=1) vs. correctly classified without flagging (â=0, ŷ=y*). This would directly confirm whether the theorem guarantees *detection* or *robustness* (or both).

## Score and Decision

### Calibration Anchors

**Round 1 — Bracketing (3 queries)**

| Paper | Path | Avg Score | Round | Comparison |
|-------|------|-----------|-------|-----------|
| A Statistical Method for Attack-Agnostic Adversarial Attack Detection | kz78RIVL7G.md | 2.60 | R1 | Much weaker: no theory, poor presentation, limited experiments. KOALA is clearly above this. |
| Detecting Adversarial Examples | KAWlH5pfQu.md | 3.00 | R1 | Much weaker: flawed theory, no proper evaluation. KOALA is clearly above this. |
| Theoretical Understanding of Learning from Adversarial Perturbations | Ww9rWUAcdo.md | 5.50 | R1 | Accepted (poster). Comparable theoretical ambition but simpler model. KOALA has more experiments but flawed metrics. |
| Provably Safeguarding a Classifier (SPADE) | kwCHcaeHrf.md | 5.50 | R1 | Accepted (poster). Similar structure (theory + detection), but SPADE had proper metric evaluation and baselines (even if outperformed). KOALA has a more novel detection principle but worse evaluation. |
| Gradient Flow Provably Learns Robust Classifiers | 8CJDYx8GwF.md | 6.25 | R1 | Rejected despite strong theory due to restrictive assumptions. KOALA has more experiments but weaker theory presentation. |

**Initial bracket**: 4.0–6.0

**Round 2 — Narrowing (3 queries)**

| Paper | Path | Avg Score | Round | Comparison |
|-------|------|-----------|-------|-----------|
| Leveraging characteristics of the output distribution for identifying adversarial audio examples | R1crLHQ4kf.md | 5.00 | R2 | Rejected (all scores 5). Comprehensive evaluation with baselines and adaptive attacks on a simpler task. KOALA has a more novel idea and theory but flawed evaluation. KOALA is slightly weaker overall. |
| Prototype-based Optimal Transport for OOD Detection | J2we1sVd9m.md | 4.60 | R2 | Rejected. Strong experiments (21 baselines) but practicality concerns. KOALA has a more interesting theoretical contribution but worse evaluation. Comparable overall. |
| BaDExpert: Extracting Backdoor Functionality | s56xikpD92.md | 6.25 | R2 | Accepted (poster). Very strong empirical validation against 17 attack methods with proper metrics and baselines. KOALA is substantially weaker empirically. |

**Narrowing**: The 5.0 anchor (ASR Detection, rejected) had proper evaluation (baselines, adaptive attacks, standard metrics) and was rejected. KOALA has a more novel theoretical contribution but significantly worse evaluation (flawed metrics, no baselines, no adaptive attacks). The 4.6 anchor (POT, rejected) also had stronger evaluation. KOALA is comparable to or slightly weaker than these rejected papers. This places it around 4.0–5.0.

**Final score**: 4.5. The core idea and theoretical framing are interesting and potentially publishable, but the paper's central empirical claims are compromised by non-standard detection metrics that conflate detection with correct classification. Combined with the absence of baseline comparisons, the experimental support for the claimed contributions is substantially weaker than it appears at first reading. A major revision with corrected metrics and baselines could make this a credible submission.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>