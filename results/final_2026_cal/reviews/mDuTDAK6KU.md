Now I have all the information needed. Let me write the consolidated review.

## Summary

KOALA introduces an adversarial detector that flags attacks when class predictions from two complementary nearest-prototype classifiers—one using KL divergence (sensitive to dense perturbations) and one using an L₀-based metric (sensitive to sparse perturbations)—disagree. The key contribution is a formal proof (Theorem 1) specifying conditions under which disagreement is guaranteed. Training is lightweight: only fine-tuning a backbone encoder on clean images with a composite loss. Experiments on ResNet/CIFAR-10 and CLIP/Tiny-ImageNet are presented.

## Strengths

- **Formal theoretical guarantee (Theorem 1).** The paper provides a proof-of-correctness under Assumptions A1–A4, showing that when inter-class prototype separation is sufficiently large, no bounded perturbation can cause both the KL and L₀ classifiers to simultaneously favor a wrong class. This contrasts with most prior detection methods, which the paper correctly notes "lack formal proof-of-correctness guarantees" (Section 2). This is the paper's strongest and most distinctive contribution.

- **Lightweight, plug-and-play training.** KOALA requires only fine-tuning a backbone encoder on clean images (no adversarial examples, no architectural changes, no auxiliary networks). The composite loss (Eq. 6) is straightforward, and the resulting detector can be attached to any existing encoder. Tables 3–4 confirm that clean accuracy is largely preserved.

- **Empirical confirmation of the theorem on the compliant subset.** On inputs satisfying the theorem's conditions, Table 1 reports perfect detection metrics (accuracy, precision, recall, F1 = 1.0) for both ResNet/CIFAR-10 and CLIP/Tiny-ImageNet. Since Theorem 1 guarantees that attacked compliant inputs *must* produce disagreement (â=1), these results directly corroborate the theory rather than being artifacts of the evaluation metric.

- **Ablation demonstrating metric complementarity.** Table 2 shows that the KL+L₀ combination outperforms single-metric and cosine-inclusive pairings on ResNet/CIFAR-10, supporting the paper's central motivation that the two metrics cover different perturbation types (dense vs. sparse).

## Weaknesses

### Major

- **Evaluation metrics conflate detection with classification, inflating overall results.**  
  The confusion matrix (Section 4.2) defines a true positive as an attacked input where *either* the detector flags it (â=1, ŷ=⊥) *or* the detector misses it but the predicted class happens to be correct (â=0, ŷ=y*). This means an undetected attack that nonetheless produces the right class label is counted as a successful detection. Consequently, the overall precision (0.94) and recall (0.81) reported in the abstract and the metrics in Tables 2–4 are inflated relative to standard detection evaluation. *On the theorem-compliant subset this issue is moot* (the theorem forces â=1, so the second case never occurs there), but for the non-compliant subset and full test sets the reported numbers overstate detection performance. The paper never reports the simple binary detection rate (â=1 vs. â=0).

- **No comparison against any existing detection method.**  
  The paper surveys a wide range of prior detectors in Section 2 (feature squeezing, LID, MagNet, Mahalanobis, NIC, CADet, etc.) but provides zero quantitative comparisons. Without baselines, it is impossible to assess whether KOALA's detection performance is competitive with existing approaches, even on a single dataset or attack setting.

- **No evaluation against adaptive attacks.**  
  For a security-oriented detector, evaluating against an adversary aware of the detection mechanism is standard practice (Carlini & Wagner, 2017; Tramer et al., 2020). KOALA's decision rule is simple (check whether ŷ_KL = ŷ_L₀), and an adaptive adversary could directly optimize to cause agreement on a wrong class. The theoretical guarantee covers this only when the theorem's conditions are met, but for the substantial fraction of non-compliant inputs the detector's robustness against a knowledgeable adversary is entirely unknown.

### Minor

- **Theorem coverage is limited, especially on CLIP/Tiny-ImageNet.**  
  Only ~67% of ResNet/CIFAR-10 test inputs satisfy the theorem's condition, and only ~10% of CLIP/Tiny-ImageNet inputs do. On the remaining 90% of CLIP inputs, the detector's accuracy drops to 0.65–0.67 and precision to 0.62–0.63. The paper discusses possible reasons (CLIP's compact embedding space) but offers no practical way to check the condition at inference time or to extend coverage.

- **Threshold τ is not ablated.**  
  The L₀ metric (Eq. 2) depends critically on τ (set to 0.75). No sensitivity analysis is provided, so the impact of this hyperparameter on detection performance is unknown.

- **Assumption A3 (coordinate-wise bound) is not empirically verified.**  
  Theorem 1 relies on |δᵢ| ≤ 1.5|pᵢ*|, but the paper does not check whether actual adversarial perturbations (PGD, CW, AutoAttack) satisfy this bound for the models tested.

- **Experiment 3 comparisons are not apples-to-apples.**  
  Tables 3–4 compare adversarial accuracy of models using different fine-tuning objectives, but the baseline model uses a standard softmax classifier head while the KOALA models use nearest-prototype classification. The improvements in adversarial accuracy could stem from the different classifier rather than the detection mechanism itself, and the paper does not disentangle these factors.

- **On CLIP, the best detection setup works by breaking classification.**  
  The paper honestly reports (Section 4.3, Table 2) that KL+L₀+Cosine achieves the highest detection metrics on CLIP but attributes this to the model's adversarial accuracy collapsing so that "all three metrics are essentially 'randomly guessing'." This reveals that on CLIP, detection succeeds through classifier failure rather than through the intended complementary-metric mechanism.

### Trivial

- None of substance beyond what has been discussed above.

## Nice-to-Haves

- An ROC or AUC analysis for the full test set (using â as the pure detection signal) would strengthen the empirical contribution.
- Comparison against at least one baseline detector (e.g., Mahalanobis or feature squeezing) on the same datasets would help calibrate KOALA's performance.
- Adaptive attack testing (e.g., optimizing against the disagreement signal) would substantially improve confidence in the method's security.

## Removed Points

- **"Perfect recall on theorem-compliant samples is uninformative about actual detection performance"** (Harsh Critic #1, part): This claim is incorrect for the compliant subset, because Theorem 1 guarantees â=1 for attacked inputs, so the (â=0, ŷ=y*) case that would inflate recall cannot arise. The metric issue is real but does not affect the theorem-compliant results.
- **Criticisms about missing appendix/proofs:** The appendix is stripped by the parser; the paper references it. This is a parsing artifact, not an author error.
- **Reproducibility nitpicks** (hyperparameters, training logs, etc.): The paper provides standard training details; asking for full logs or every implementation detail is excessive.
- **Formatting and style complaints:** Parser artifacts, not author errors.
- **Strength Finder items conflated or generic:** Dropped strengths about "semantics-free" being a demonstrated strength (it is a claimed property) and generic framing such as "addressed an important problem."

## Novel Insights

None beyond the paper's own contributions. The harsh critic and strength finder both surface the same landscape: a genuinely novel theoretical contribution paired with an evaluation that has significant gaps. The most insightful observation is that the metric definition, while not fatal to the core theorem-supported claim, substantially weakens the paper's overall empirical reporting and makes it hard to compare against other work.

## Suggestions

1. **Fix the detection metrics:** Report standard detection metrics based solely on the binary â decision (attack vs. benign). Add ROC curves and AUC for the full test set. This would both correct the inflated numbers and provide a cleaner evaluation.
2. **Add at least one baseline comparison:** Even a single comparison against feature squeezing or Mahalanobis distance on the same datasets would allow readers to calibrate KOALA's performance.
3. **Evaluate against adaptive attacks:** Test an adversary that minimizes the probability of disagreement between KL and L₀ predictions.
4. **Ablate τ:** Show detection performance as a function of τ (e.g., 0.5–0.95) and discuss how to select it in practice.
5. **Empirically verify Assumption A3:** Check whether the coordinate-wise bound |δᵢ| ≤ 1.5|pᵢ*| holds for the perturbations generated by PGD, CW, and AutoAttack on the models tested.

## Score and Decision

### Calibration Report

**Round 1 (Bracketing):** Three queries on adversarial detection with formal guarantees retrieved anchors in three bands:
- Weak band (avg < 3.5): "Robust Detection of Directional Adversarial Attacks" (2.5), "DeepDefense" (1.5), "Gradient Manifold Geometry" (3.0), "Automotive Object Detection" (2.0)
- Middle band (3.5–7.5): "A Few Large Shifts" (4.5), "Conformal Novelty Detection" (4.0), "Adversaries Fight Back" (4.0), "GeoDetect" (4.0)
- Strong band (avg > 7.5): Generative Universal Verifier (8.0), Polar Express (8.0), Probabilistic Kernel Function (8.0), Feedback-driven QNN (8.0) — these are topically unrelated and not useful for comparison.

Initial bracket: 3.5–5.5.

**Round 2 (Narrowing):** A tighter query retrieved:
- "A Few Large Shifts" (4.5) — robust plug-in detection with baselines, adaptive attacks, weaker theory — this is the most topically similar anchor. KOALA has stronger theory but substantially weaker evaluation. KOALA is slightly worse overall.
- "Prediction Inconsistency Detection" (2.67) — too weak to anchor.
- "Conformal Novelty Detection" (4.0) — different focus (novelty detection robustness).
- "When Less Is More" (4.4) — robustness of pruning, different topic.

**Final score:** 4.0. The paper's core idea and theoretical contribution are genuinely novel, but the evaluation has multiple significant gaps (flawed detection metrics, no baselines, no adaptive attacks, limited theorem coverage) that prevent it from being a strong paper. Compared to "A Few Large Shifts" (avg 4.5), which had proper evaluation metrics, baseline comparisons, and adaptive attack testing, KOALA is weaker empirically despite a stronger theoretical contribution.

### Score and Decision

**Score:** 4.0

**Decision:** Reject

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>