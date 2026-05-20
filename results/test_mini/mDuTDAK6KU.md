Now I have a good understanding of the calibration landscape. Let me produce the final consolidated review.

## Summary
2-3 sentence summary of the paper's contribution.

The paper proposes KOALA, an adversarial detector that flags attacks when class predictions from KL divergence and an L₀-based similarity metric disagree. The key contribution is a formal theorem claiming that under certain assumptions (prototype separation, bounded perturbations), no single adversarial perturbation can simultaneously fool both metrics, guaranteeing detection. Experiments on ResNet/CIFAR-10 and CLIP/Tiny-ImageNet validate the theory on a "Theorem-compliant" subset and demonstrate detection performance through ablation studies.

## Strengths

- **Novel detection principle with formal grounding**: The idea of combining KL divergence (sensitive to dense, small shifts) with an L₀-based metric (sensitive to sparse, large changes) is well-motivated and intuitive (Figure 1). The paper provides a formal theorem (Theorem 1) stating conditions under which the two metrics must disagree on adversarial inputs, which is a stronger claim than most empirical detectors offer. The proof sketch in §3.2 lays out a clear logical structure (Propositions 2–4 → incompatibility condition).

- **Empirical validation of the theorem on the compliant subset**: Table 1 shows that on samples satisfying the theorem's conditions, recall is a perfect 1.0 across both models and perturbation levels. Every attacked input in this subset is detected, which directly supports the theoretical claim that when the conditions hold, detection is guaranteed. This result is not affected by the metric definition debate (discussed below), since on the compliant subset the detector flags everything (â=1), making standard and paper-specific metrics coincide.

- **Lightweight training procedure**: The fine-tuning recipe (§3.3) uses only clean images, does not require architectural changes, adversarial examples, or adversarial training. This makes KOALA a practical plug-in option for existing encoders, which differentiates it from methods that require expensive adversarial retraining or specialized architectures.

- **Thorough ablation across metric combinations**: Tables 2–4 evaluate seven different loss objectives across two architectures and three attack types (PGD, CW, AutoAttack). The analysis in §4.4 explains why different objectives work differently depending on pre-training (cross-entropy vs. contrastive), showing nuanced understanding. The paper also honestly discusses a failure mode on CLIP where KL+L₀+Cosine achieves high detection by "breaking the underlying classification" rather than preserving it.

## Weaknesses

### Fatal
None.

### Major

1. **Non-standard detection metrics inflate reported performance (§4.2).** The paper defines the confusion matrix so that an adversarial input that is *not flagged* by the detector is still counted as a true positive as long as the base classifier predicts the correct class:
   - TP: \(a=1\) ∧ [(â,ŷ) = (1,⟂) ∨ (â,ŷ) = (0, \(y^*\))]
   - FN: \(a=1\) ∧ [(â,ŷ) = (0, \(-y^*\))]
   
   Under standard adversarial detection conventions, *every* adversarial example is a positive instance, and a missed detection (â=0) is an FN regardless of whether the attack happened to change the classifier's prediction. The paper's definition bundles detection with the base classifier's accuracy, making the reported precision (0.94) and recall (0.81) on the full test set uncomparable to any prior work. The headline quantitative claims are therefore not interpretable relative to the existing literature. To be clear: this does *not* invalidate the results on the Theorem-compliant subset (where recall=1.0 corresponds to the detector actually flagging all inputs), but it undermines the non-compliant and overall numbers and the claim that KOALA achieves "strong detection performance" in absolute terms.

2. **No comparison to any existing detection method.** The experiments evaluate only ablations of the paper's own metric combinations (KL, L₀, Cosine). The paper itself cites numerous prior detection approaches (MagNet, LID, Mahalanobis, NIC, CADet, Bayesian uncertainty) in §2. Without comparisons against even a representative subset — say, Mahalanobis-based detection or feature squeezing — there is no evidence that KOALA is competitive as a practical detector. Since the paper presents KOALA as both a theoretically grounded and an empirically effective detector, the absence of baselines is a significant gap. This can be addressed in a revision by adding at least 2–3 baselines on the same datasets and attacks.

3. **The compliant/non-compliant partition is insufficiently explained.** The paper partitions the test set into "Theorem-Compliant Samples: Inputs that satisfy the conditions of Theorem 1, specifically the sufficient inter-class prototype separation" and non-compliant samples, but does not specify how compliance is determined algorithmically (e.g., what is the exact formula for \(\Gamma_i(\epsilon)\)? How is the "sufficiently large coordinate gap" checked? Is it computed per-input or per-class?). Without this information, the perfect results on the compliant subset cannot be fully assessed. The partition is a critical part of the empirical validation and must be reproducible.

### Minor

4. **The proof sketch is too vague to evaluate the theorem's strength.** The sketch in §3.2 claims a necessary condition for a KL prediction flip (positive inner product with \(\hat{c}-c^*\)), but KL divergence is not linear in the input, and this condition is derived from a first-order argument whose validity under the normalization constraints (A1) is not explained. Similarly, the L₀ metric's behavior under perturbation (Eq. 2) depends on a threshold \(\tau\) and the average \(\mu\), both of which shift with the input; the claim that a "minimum number of flipped coordinates" is needed may not follow straightforwardly. The full proof is in the appendix (removed by the parser), so these concerns cannot be resolved from the submission. The assumptions, particularly A3 (coordinate-wise bound \(|\delta_i| \leq \frac{3}{2}|p_i^*|\)), are described as "mild" but are not standard in the adversarial robustness literature and are not empirically verified.

5. **The "adversarial accuracy" metric in Experiment 3 (§4.4) is confusing.** The paper defines it as "performance on successfully attacked images that were not detected." The interaction between the detection step and the accuracy computation is not made explicit. The large gap between KL+L₀ and other objectives (e.g., 54.60% vs. 32.86% on ResNet/CIFAR-10 PGD ε=4/255 in Table 3) is interesting but hard to interpret without knowing how many attacks were detected (and thus removed from the accuracy denominator) under each objective.

6. **No standard detection metrics (AUROC, AUPR, FPR@TPR) are reported.** The field standard for detection papers is AUROC or detection accuracy at a fixed false positive rate. Reporting only accuracy/precision/recall/F1 with the non-standard definition (Point 1) further limits comparability.

### Trivial
None.

## Nice-to-Haves
- The paper could strengthen its theoretical validation by explicitly measuring how often the theorem's conditions are satisfied across architectures and datasets (beyond the compliant/non-compliant split), and by varying prototype separation synthetically to show that detection rate rises with the gap as predicted.
- A controlled adaptive-attack evaluation (e.g., PGD that optimizes against the detection score directly) would strengthen the security claims.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"The theoretical guarantee is not convincingly established"** — The harsh critic makes specific mathematical claims about the proof being flawed. However, the full proof is in the appended material (removed by the parser). Speculating about gaps in a removed appendix without being able to confirm them goes beyond what can be verified from the available text. The vagueness of the sketch (listed as Minor Weakness 4) is a fair criticism; the unverifiable mathematical claims about proof correctness are not.
- **"Assumption A3 is strong... prevents large perturbations on any single coordinate"** — This is a substantive criticism but is speculative: the paper explicitly describes the assumption and calls it mild; the reviewer's disagreement is a judgment call. I have kept the gist of this in Minor Weakness 4 (the assumption is not empirically verified) but removed the stronger claim that the assumption "is not standard and is strong."
- **"The claim that detection is not a probabilistic outcome but a mathematical certainty is misleading"** — The paper qualifies this with "if the feature space is properly structured (which our fine-tuning encourages)," so the claim is explicitly contingent on the conditions. This was an overreading by the harsh critic.
- **"The CLIP results (KL+L₀+Cosine outperforms KL+L₀) undermines the claim that KOALA preserves classification"** — The paper itself acknowledges this limitation explicitly (§4.4: "a high detection rate does not always equate to a truly robust model... this outcome underscores a critical distinction"). The paper does not try to hide this; it discusses it as a finding. This is evidence of good scientific practice, not a weakness.
- Strengths from the Strength Finder that were removed: "Lightweight training recipe" and "Thorough comparison across architectures" are retained. Generic statements about "addressing an important problem" or being "well-written" without specific evidence were dropped.

## Novel Insights

The two reviews together surface an interesting tension: the paper has a genuinely novel theoretical framing (complementary metric disagreement as a provable detection signal) but evaluates it in a way that makes the empirical results uncomparable to prior work. The metric definition issue is the most consequential finding — it is not a minor formatting or presentation issue but a substantive evaluation design choice that must be corrected before the paper's quantitative claims can be assessed. At the same time, the core theoretical result (Table 1 on the compliant subset) survives this criticism intact, suggesting the paper could be substantially rehabilitated with standard evaluation practices and a few baseline comparisons.

## Suggestions

1. **Fix the detection metrics** to follow standard definitions: TP = (a=1) ∧ (â=1); FN = (a=1) ∧ (â=0); FP = (a=0) ∧ (â=1); TN = (a=0) ∧ (â=0). Recompute all numbers and re-evaluate whether the core claims still hold.
2. **Add at least 2–3 baseline detection methods** (e.g., Mahalanobis, LID, or feature squeezing) on the same datasets and attacks. This is essential to demonstrate that KOALA is competitive.
3. **Clearly specify the compliant/non-compliant partitioning algorithm** — provide the exact formula for \(\Gamma_i(\epsilon)\) and describe how the per-input condition is checked.
4. **Report AUROC** alongside the corrected precision/recall metrics to enable direct comparison with prior work.
5. **Include a discussion of limitations** — in particular, the strength of Assumption A3, the fraction of inputs that satisfy the theorem, and whether the detection guarantee holds under adaptive attacks.

## Score and Decision

**Calibration Round 1 (Bracketing):** Queried three bands on adversarial detection topics.
- Band A (avg < 3.5): Papers on gradient-based detection (2.0), prediction inconsistency detection (2.67), and automotive object detection (2.0) — all clearly weaker than KOALA.
- Band B (3.5 < avg < 7.5): Included "A Few Large Shifts" (4.50), "GeoDetect" (4.00), "Gradient Manifold Geometry" (3.00), "Conformal Novelty Detection" (4.00). KOALA sits within this band.
- Band C (avg > 7.5): Results were on unrelated topics (kernel functions, verifiers, rotation estimation) — not comparable.

**Round 1 bracket:** 3.0–5.5.

**Calibration Round 2 (Narrowing):** Focused on 3.0–6.5, retrieving papers on detection + lightweight plug-in + theoretical guarantees. Key anchors:
- "A Few Large Shifts" (4.50, scores 2,6,6,4) — adversarial detection with thorough evaluation, baselines, clear presentation. KOALA has a stronger theoretical claim but weaker evaluation. **KOALA is somewhat weaker → below 4.5.**
- "GeoDetect" (4.00, scores 4,6,4,2) — geometric detection with theory and baselines. KOALA has a more formal proof but the metric definition issue is more damaging than GeoDetect's weaknesses. **KOALA is comparable or slightly weaker → near 4.0.**
- "Conformal Novelty Detection" (4.00, scores 6,4,2,4) — theory for adversarial robustness of an existing detector. KOALA has a stronger original contribution but worse evaluation. **Comparable → around 4.0.**

**Final comparison:** KOALA has a genuinely novel theoretical idea and strong proof-of-concept results on the compliant subset. However, the non-standard evaluation metrics, absence of baseline comparisons, and opaque compliant partition are significant weaknesses that are heavier than those of the 4.0–4.5 anchors. The paper is better than the 3.0 band (papers with fatal evaluation flaws) but below the 4.5 anchor (which had baselines, clear evaluation, thorough adaptive attacks).

MY FINAL SCORE: <score>3.5</score>
MY FINAL DECISION: <decision>Reject</decision>