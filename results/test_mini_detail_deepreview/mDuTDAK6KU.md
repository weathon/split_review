This completes my analysis. Now let me write the final consolidated review.

## Summary

KOALA proposes an adversarial detector that flags an input as attacked when two nearest-prototype classifiers—using KL divergence and an L₀-based metric on embeddings—produce different class predictions. The paper provides a formal theorem stating conditions under which detection is guaranteed, a lightweight fine-tuning procedure using only clean images, and experiments on ResNet/CIFAR-10 and CLIP/Tiny-ImageNet.

## Strengths

1. **Novel dual-metric disagreement approach with clear geometric motivation.** The core idea—using KL divergence (sensitive to dense, low-amplitude shifts) and L₀ (sensitive to sparse, high-impact changes) and detecting attacks when they disagree (Fig. 1, Section 3.1)—is genuinely novel. The geometric grounding makes the design principled rather than ad hoc, and contrasts with prior detectors that lack such a rationale.

2. **Formal theorem with empirical validation on compliant samples.** Theorem 1 (Section 3.2) provides conditions under which no norm-bounded perturbation can simultaneously fool both metric classifiers, which is a stronger form of guarantee than existing detection methods offer. Table 1 shows that on the Theorem-compliant subset, KOALA achieves 1.0 across all metrics (Accuracy, Precision, Recall, F1) for both ResNet/CIFAR-10 and CLIP/Tiny-ImageNet under ℓ∞ perturbations. This directly confirms that the theorem's conditions translate to perfect detection in practice.

3. **Lightweight fine-tuning using only clean images.** The training procedure (Section 3.3, Eq. 6) requires no adversarial examples, no architectural changes, and minimal compute (SGD for fine-tuning). This is reflected consistently across the paper's tables ("All finetuning was done using clean images only"). Avoids the computational cost and attack-type dependence of adversarial-training-based approaches.

4. **Ablation study supports metric complementarity.** Table 2 shows that the KL+L₀ combination outperforms all other metric pairs (L₀+Cosine, KL+Cosine, KL+L₀+Cosine) on ResNet/CIFAR-10 (e.g., F1=0.87 vs. next-best 0.74). This provides direct evidence that KL and L₀ are complementary for detection.

5. **Substantial adversarial accuracy improvements on ResNet/CIFAR-10.** Table 3 reports that KL+L₀ fine-tuning yields adversarial accuracy of 57.32% (PGD ℓ∞ 2/255), significantly higher than the baseline (45.5%) and all other objectives, without sacrificing clean accuracy (94.78% vs. baseline 95.16%).

## Weaknesses

### Major
1. **Evaluation metrics conflate detection with correct classification.** The confusion matrix (Section 4.2, lines 192-195) defines a True Positive as an attacked input where *either* the detector flags it *or* it is not flagged but correctly classified: `TP := [a=1] ∧ [(â,ŷ)=(1,⊥) ∨ (â,ŷ)=(0,y*)]`. This means a detector that never flags any attack but always classifies correctly would achieve perfect Precision, Recall, and F1. **Mitigation**: On the Theorem-compliant subset (where the paper reports 1.0 on all metrics), this does not change the results because attacked inputs ARE flagged (disagreement is guaranteed by Theorem 1), and clean inputs are correctly classified. So the paper's main empirical claim about the theorem is robust. However, the full-set results (Table 2, and the non-compliant subset in Table 1) are inflated by this definition. The reported 0.94 precision and 0.81 recall on the full ResNet/CIFAR-10 test set are not interpretable as standard detection metrics and would likely be lower with proper definitions (flag vs. no-flag, independent of classification accuracy).

2. **No comparison to existing adversarial detection baselines.** The paper compares its own metric combinations internally but does not benchmark against any established detection method—e.g., Feature Squeezing (Xu et al. 2018), Local Intrinsic Dimensionality (Ma et al. 2018), Mahalanobis-based detection (Lee et al. 2018), NIC (Ma & Liu 2019), or CADet (Guille-Escuret et al. 2023). The paper's related work section (Section 2) discusses these methods but provides no experimental comparison. Without this, it is impossible to assess whether KOALA offers any practical advantage over existing approaches, or whether its "lightweight, plug-and-play" claim translates to competitive performance.

3. **No adaptive attack evaluation.** KOALA's detection criterion (disagreement between two metric-based predictions) is fixed and knowable. An adaptive adversary aware of the defense could explicitly minimize the probability of disagreement while maintaining misclassification on the original classifier, e.g., via a joint loss that penalizes disagreement. The paper evaluates only against standard attacks (PGD, CW, AutoAttack) that target the classifier alone, not the detector. For any defense paper, adaptive attacks are critical to avoid overestimating robustness. This omission casts significant doubt on the method's practical security.

### Minor
4. **Theorem statement leaves key quantities undefined in the main text.** Theorem 1 depends on the threshold `Γ_i(ε)`, which is mentioned but never defined in the main body. The proof sketch (Section 3.2) refers to three propositions and an "Incompatibility Condition" but is too vague to verify the logic. Assumption A3 (`|δ_i| ≤ 1.5|p_i^*|`) appears engineered to enable the proof rather than naturally motivated. The full proof in the appendix was stripped, so the theorem's validity cannot be assessed from the submitted manuscript.

5. **"Theorem-compliant" split criterion is not defined.** Section 4.2 states that the test set is partitioned based on "sufficient inter-class prototype separation" but never specifies the precise numerical criterion. The fact that only 510/5000 CLIP/Tiny-ImageNet samples are compliant (Table 1) is reported without analyzing why. This makes it impossible to reproduce the split or assess whether the condition is meaningful in practice.

6. **Missing Euclidean nearest-prototype baseline in adversarial accuracy experiments.** Table 3 includes Cosine similarity as a baseline, but Euclidean distance is the standard nearest-prototype metric and is not included. Given that Cosine similarity achieves 45.8% (close to the baseline 45.5%) while KL+L₀ achieves 57.32%, the improvement appears real, but the gap would be better contextualized with a Euclidean baseline.

### Trivial
None.

## Nice-to-Haves
- Sensitivity analysis on the loss weights (ω_L₀=0.9, ω_KL=0.1) — the strong bias toward L₀ is stated but not justified or ablated.
- Analysis of detection failure cases on the non-compliant subset — why does detection degrade, and is there a pattern?
- An analysis of how the L₀ threshold τ was chosen and its impact on the "energy consumption" argument in the proof sketch.

## Removed Points
These points from the input reviews are removed because they are not supported by the paper text or reflect reviewer knowledge gaps:

- **"Theorem is disconnected from the detection setting"**: Removed. Theorem 1 makes a statement about *any* perturbation within the norm bound, regardless of how it was generated. It does not require the adversary to be targeting the KOALA classifiers specifically. The paper does not specify that attacks are generated only against the baseline model — standard practice is to generate attacks against each evaluated model (the paper states attacks are generated for "both the ResNet and CLIP models," which is ambiguous but consistent with per-model generation). Even if attacks were transferred, the theorem's bound on `‖δ‖` still applies.
- **"Adaptive L₀ metric complicates proof"**: Removed. The reviewer's concern about the L₀ metric being defined relative to the mean absolute difference μ(c,p) making it "data-adaptive" is a valid technical nuance, but it is speculation about the proof's soundness without having seen the full proof. The paper acknowledges the threshold τ as a hyperparameter.
- **"Fine-tuning loss weights are arbitrary"**: Removed (moved to Nice-to-Haves). This is a reasonable ablation request, not a core flaw.
- **"Improvement may be due to prototype-based classification, not dual metric"**: Removed. The paper includes Cosine similarity as a nearest-prototype baseline (Table 3), which addresses this concern. The fact that Cosine achieves 45.8% (near baseline 45.5%) while KL+L₀ achieves 57.32% suggests the improvement is not merely from switching to prototype-based classification.
- **"Strength Finder: Formal proof of correctness"**: Re-evaluated and kept as a genuine strength (the theorem IS a contribution, even if the full proof cannot be assessed).
- **"Strength Finder: Empirical validation on Theorem-compliant subset"**: Kept, as the perfect scores on this subset are robust to the metric issue (since attacked inputs are flagged, not just correctly classified).
- Various formatting nitpicks, speculative concerns about missing appendix content, and generic "reproducibility" issues: Removed per hard rules.

## Novel Insights
None beyond the paper's own contributions. The dual-metric disagreement idea is the paper's central innovation, and the reviews add no new interpretation of it.

## Suggestions
1. **Fix the evaluation metrics.** Define a standard detection confusion matrix: `TP := [a=1 ∧ â=1]`, `FP := [a=0 ∧ â=1]`, `TN := [a=0 ∧ â=0]`, `FN := [a=1 ∧ â=0]`, independent of classification accuracy. Report TPR at low FPR and/or AUC-ROC. Re-compute all detection results (Tables 1, 2) with these proper definitions.
2. **Add 2–3 established detection baselines** (e.g., Feature Squeezing, Mahalanobis, LID) evaluated on the same attacks and metrics. This is essential to contextualize KOALA's performance.
3. **Evaluate against adaptive attacks.** Design an attack with a joint loss that minimizes `λ·ℒ_classifier + (1-λ)·ℒ_agreement` where ℒ_agreement encourages KL and L₀ predictions to match. Show detection rates under such attacks.
4. **Define the compliance criterion.** State the precise numerical threshold for "sufficient inter-class prototype separation" used to partition the test set. Report the distribution of the key gap measure across the full test set.
5. **Provide the full theorem and proof** in a format that reviewers can assess. Define Γ_i(ε) explicitly.

## Score and Decision

### Calibration Report

**Round 1 — Bracketing:**
- Weak band (avg < 3.5): Anchors at 2.33 (nearest neighbors classification), 2.60 (compressive sensing detection), 3.00 (adversarial example detection), 3.00 (thresholding strategies). These papers have fundamental flaws or thin contributions. KOALA is clearly stronger (novel idea, formal theorem, experiments).
- Middle band (3.5–7.5): Anchors at 4.60 (prototype-based OOD detection), 5.00 (Bregman divergence robustness), 5.50 (cluster-driven adversarial contrastive learning), 4.00 (sharpness-aware OOD). These have interesting ideas with methodological concerns.
- Strong band (avg > 7.5): Anchors at 8.00 (robust diffusion classifier, GNN certification). These are clearly stronger than KOALA in both methodology and evidence.
- **Initial bracket**: 4.0–6.0

**Round 2 — Narrowing:**
- Anchors within bracket: 6.20 (DDAD detection, rejected), 6.00 (oracle for errors), 5.75 (dummy classes AT), 5.50 (concept extrapolation), 5.33 (test-time defense), 6.25 (gradient flow provably robust).
- The DDAD paper (6.20) had: strong motivation, theoretical proof, experiments on CIFAR-10 and ImageNet-1K, comparison to baselines, adaptive attacks, but still rejected due to evaluation concerns. KOALA is weaker (no baseline comparisons, metric issue).
- The Bregman divergence paper (5.00, rejected) had similar profile: novel idea with theory, experiments on limited datasets, missing baselines. KOALA is comparable but has a more significant metric issue.
- **Final score**: 5.0 — lower than DDAD (6.20) due to missing baselines and adaptive attacks; comparable to Bregman divergence (5.00) but weaker on evaluation rigor.

**Round 3:** Not needed — bracket clearly narrowed.

### Anchors used
| Paper | Avg | Round | Comparison |
|-------|-----|-------|------------|
| kz78RIVL7G (compressive sensing detection) | 2.60 | R1 | Weaker: simpler method, no formal guarantee |
| 4Hf5pbk74h (nearest neighbor boundaries) | 2.33 | R1 | Weaker: minor improvements, no detection focus |
| KAWlH5pfQu (detecting adversarial examples) | 3.00 | R1 | Weaker: less principled, no formal proof |
| J2we1sVd9m (prototype OOD) | 4.60 | R1 | Slightly weaker: comparable idea density, has baselines |
| 7GCRhebJEr (Bregman divergence robustness) | 5.00 | R1 | Comparable: similar strengths and gaps |
| rlsWIBDWhW (cluster-driven ACL) | 5.50 | R1 | Slightly stronger: more extensive experiments |
| RzdtpxL0H5 (DDAD detection) | 6.20 | R2 | Stronger: has baselines, adaptive attacks, larger-scale eval |
| sBpYRQOrMn (dummy classes AT) | 5.75 | R2 | Stronger: rigorous AT baseline comparisons |

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>