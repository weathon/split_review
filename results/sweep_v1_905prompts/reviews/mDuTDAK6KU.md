I now have a thorough understanding of the paper. Let me produce the final consolidated review.

---

## Summary

KOALA proposes an adversarial detector that flags an attack when nearest-prototype classifications from two complementary metrics—KL divergence (sensitive to dense, low-amplitude perturbations) and an L₀-based metric (sensitive to sparse, high-impact changes)—disagree. The method requires only lightweight fine-tuning of the backbone encoder on clean images using a composite KL+L₀ loss, with no architectural changes or adversarial training. The paper provides a formal theorem (Theorem 1) stating conditions under which detection is guaranteed, and validates it empirically on ResNet/CIFAR-10 and CLIP/Tiny-ImageNet under PGD, CW, and AutoAttack.

## Strengths

- **Novel and well-motivated detection principle.** The idea of using disagreement between KL divergence and an L₀-based similarity as an adversarial detector is genuinely novel. The intuition that dense perturbations affect KL divergence more while sparse perturbations affect L₀ more (Figure 1) is clearly explained and physically plausible. This is a creative contribution compared to the large body of feature-statistics-based detectors.

- **Lightweight training with no adversarial examples.** The fine-tuning procedure (§3.3) uses only clean images, avoiding the expense and attack-model dependence of adversarial training. The paper shows clean accuracy is preserved (Table 3: all ResNet variants within ~1% of baseline), which is a practical advantage.

- **Ablation study cleanly supports the metric-complementarity claim.** Table 2 systematically compares KL+L₀ against L₀+Cosine, KL+Cosine, and KL+L₀+Cosine. On ResNet/CIFAR-10, KL+L₀ dominates all alternatives across accuracy, precision, recall, and F1. This directly validates the paper's core design choice.

- **Adversarial accuracy gains as a side benefit.** Table 3 shows ResNet-18 fine-tuned with KL+L₀ achieves substantially higher adversarial accuracy (e.g., 57.32% vs. baseline 45.5% under PGD ℓ∞²/²⁵⁵) while all other metric combinations perform worse. This demonstrates a non-trivial side benefit of the composite objective beyond detection.

- **Theoretical framing with explicit assumptions.** Theorem 1 and its four assumptions (A1–A4) are stated concretely. Even if the proof is deferred to the appendix, the assumptions and the theorem statement are clearly scoped, which is more than most empirical detection papers provide.

## Weaknesses

### Major

1. **Non-standard evaluation metrics make the headline detection numbers misleading.** Section 4.2 defines TP/TN/FP/FN with a non-standard confusion matrix. For example, TP includes attacked inputs that are *not flagged by the detector* as long as the classifier predicts the correct label (â=0, ŷ=y*); FP includes clean inputs that are *misclassified* even without a false alarm (â=0, ŷ≠y*). This conflates classification accuracy with detection accuracy. The abstract reports "precision 0.94, recall 0.81" (from Table 2), but these do not mean what readers expect—they measure something closer to "overall system correctness" rather than detection performance. While the paper does define its metrics, using standard evaluation terms (precision, recall) with non-standard definitions without explicit caveat is misleading and prevents comparison with any prior detection method. This issue directly affects the paper's central performance claims.

   *Evidence:* Section 4.2 lines 192-195 define TP/FP/FN/TN as shown. The abstract and Table 2 report these as "precision" and "recall" without disclosing that these are non-standard definitions.

2. **No comparison against existing adversarial detectors.** The paper mentions prior detectors (Mahalanobis, LID, NIC, MagNet, CADet, etc.) in the Related Work, cites the need for "proof-of-correctness guarantees" they lack, but provides *no experimental comparison* against any of them. The evaluation is entirely internal (different metric combinations). Without a baseline detector comparison, readers cannot assess whether KOALA's detection performance is practically competitive. This is a critical gap for a paper claiming a new detection method.

3. **No adaptive attack evaluation.** The detector's decision rule (flag when ŷ_KL ≠ ŷ_L₀) is transparent. An attacker aware of KOALA could craft perturbations designed to make both metrics agree on an incorrect class (e.g., by targeting the intersection of the KL and L₀ stability bands). The paper mentions "adaptive attacks" in the Related Work (line 48) as a limitation of prior methods, but does not evaluate its own method against them. For a paper claiming a "formal guarantee," absent adaptive evaluation is a serious omission.

### Minor

4. **The theoretical guarantee's practical force is unclear.** The proof sketch (§3.2) is high-level; the full proof is in the appendix (stripped by parser, so unverifiable). More importantly, Experiment 1 partitions the test set into "Theorem-compliant" and "non-compliant" samples based on sufficient inter-class prototype separation, but the paper never specifies how this partition is operationalized (the criteria are mentioned only vaguely as "sufficient inter-class prototype separation"). For CLIP/Tiny-ImageNet at ℓ∞²/²⁵⁵, only 510/5000 samples (10.2%) are compliant. The paper does not characterize compliance at inference time, so the guarantee cannot be checked on new inputs. The result (perfect metrics on the compliant subset) is partially circular: the subset is defined to satisfy the theorem's conditions.

5. **Missing hyperparameter sensitivity analysis.** The L₀ distance has two hyperparameters (τ = 0.75 fixed, φ = 0.5 fixed), and the composite loss has weights (ω_L₀ = 0.9, ω_KL = 0.1). No sensitivity analysis is provided for any of these values. Given that the entire detection mechanism depends on these thresholds, this limits confidence in the method's robustness.

6. **No confidence intervals or statistical significance.** All metrics (Tables 1–4) are reported as point estimates. Given the moderate sample sizes (e.g., 510 compliant samples for CLIP), variance could be substantial.

### Trivial

7. Table 4's caption states "The KL+L₀ objective demonstrates superior adversarial accuracy" for CLIP, but the table actually shows KL+L₀ performing worse than L₀-only and KL-only on CLIP for most attacks (e.g., PGD ℓ∞²/²⁵⁵: L₀ = 53.31%, KL = 60.02%, KL+L₀ = 26.50%). This caption-text mismatch is confusing.

## Nice-to-Haves

- **Lipschitz constant between pixel-space ℓ∞ and feature-space ℓ2.** Assumption A2 bounds perturbations in feature space, but attacks are applied with ℓ∞ bounds in pixel space. Computing or estimating the Lipschitz constant of the backbone encoder would tighten the link between theory and experiments.

- **Ablation on loss weights (ω_L₀, ω_KL).** The weights are set empirically (0.9/0.1) with the comment that "L̂₀ is harder to optimize." A targeted ablation showing how performance varies with this ratio would strengthen the practical guidance.

- **Inference cost.** Computing KL and L₀ distances to all class prototypes is O(m·d) per input. For CLIP on Tiny-ImageNet (m=200, d=512), this is negligible, but a brief runtime comparison would be useful.

## Removed Points

*These are points from the reviewers that, on verification against the paper, were found to be inaccurate, speculative, or not genuinely problematic.*

- *"The theoretical guarantee is not substantiated by the evidence presented" / "Experiment 1 verification is tautological":* The reviewer overstates this. Table 1 reports sample sizes for the compliant subset (e.g., 3345/5000 for ResNet), so the characterization is partially provided. The perfect metrics on the compliant subset are a meaningful sanity check of the theorem, not purely tautological—the theorem predicts detection under certain conditions, and the experiment confirms that prediction. However, I note above that the operationalization of the partition criteria is not explained.

- *"Comparison fairness is limited — baseline model uses a standard linear classifier head":* The paper's main comparisons are between different metric combinations *within the same nearest-prototype architecture* (Tables 2, 3). The "baseline model" row is an additional reference point, not the primary comparison. The single-metric rows (Cosine, KL, L₀) provide fair baselines within the same classifier paradigm. This complaint conflates a reference comparison with the main evaluation.

- *"Assumption A4 makes the theorem circular":* Assumption A4 states that on clean inputs both metrics agree on the true class. This is a premise that the fine-tuning procedure aims to satisfy, not a conclusion. The theorem's value is in what it guarantees *under* that premise (and other assumptions). This is standard mathematical reasoning, not circular.

- *"L₀ distance is non-standard and motivation is unclear":* The paper clearly motivates why an L₀-like count of significantly perturbed dimensions captures sparse attacks, and Eq. (2) provides a concrete definition. It is non-standard but well-defined and purpose-built.

- *"Assumption A3 is arbitrary" / "prediction stability band is never formally defined":* A3 bounds |δ_i| ≤ 1.5|p*_i|, which is a reasonable coordinate-wise constraint. The concept of "stability band" is conveyed intuitively in the proof sketch and is standard in the certified robustness literature. These are exposition choices, not errors.

- *Strength Finder's generic strengths* ("the paper addresses an important problem", "the paper is well-written") are removed as they lack specific content tied to this paper's contributions.

## Novel Insights

The review process surfaced a genuine tension in the paper that the authors do not fully address: the evaluation metrics conflate detection and classification performance, which is particularly problematic for the CLIP/Tiny-ImageNet results. In Table 2, KL+L₀+Cosine achieves the *highest* detection F1 on CLIP (0.79), but Table 4 shows this same configuration has near-zero adversarial accuracy (0.97% under AutoAttack ℓ∞²/²⁵⁵). The paper acknowledges this as an "artifact" where "high detection rate does not always equate to a truly robust model," but this undercuts the premise that detection metrics (as the paper defines them) measure meaningful security. If the detector can achieve high scores simply by destroying the model's classification ability, the evaluation framework is not separating robust detection from model collapse. This tension warrants a more careful treatment than the paper provides.

## Suggestions

1. **Re-report all detection results with standard metrics.** Define TP = attacked input ∧ â=1, FP = clean input ∧ â=1, and report detection precision, recall, F1, and/or AUROC separately from classification accuracy on clean and undetected-adversarial inputs. Report classification accuracy for undetected attacks as a separate informative metric.

2. **Add at least one baseline detector comparison.** The Mahalanobis detector (Lee et al., 2018) and LID (Ma et al., 2018) are cited in the paper and would be straightforward to implement. Even a single comparison would contextualize KOALA's performance.

3. **Evaluate against a simple adaptive attack.** Construct an attack that minimizes the objective L = ℓ_CE(ŷ_adversarial, y_true) + λ · (KL(c_adv, p+δ) − L₀(c_adv, p+δ))² to force agreement. The paper's claim of a "formal guarantee" demands at least a discussion of why this attack would or would not succeed.

4. **Specify how the Theorem-compliant partition is operationalized** and report whether this can be checked at inference time (e.g., using distance to nearest prototype).

5. **Add hyperparameter sensitivity** for τ, φ, and ω_L₀/ω_KL. A simple grid over 2–3 values each would suffice.

## Score and Decision

**Round 1 bracketing:** I queried three score bands with queries related to adversarial detection and defense. The weak band (avg < 3.5) returned papers with flawed theorems, no adaptive attacks, and weak evaluations (exemplified by "Detecting Adversarial Examples" at avg 3.00). The middle band (3.5–7.5) returned papers with theoretical motivation, moderate experiments, but recognized limitations (DDAD at 6.20, "Near-Zero Eigenvalues" at 5.50, D-PDDM at 5.00). The strong band (>7.5) returned papers with careful adaptive evaluation, SOTA comparisons, and thorough theoretical support (RDC at 8.00). KOALA sits clearly in the middle band: it has a stronger conceptual contribution than the weak-band papers but lacks the rigorous evaluation and baseline comparisons of strong-band papers.

**Round 2 narrowing:** I queried the 3.5–6.0 and 4.5–7.0 ranges with topic-specific queries. The "Near-Zero Eigenvalues" paper (5.50) is a reasonable comparison point: it has a theoretical framework with formal proofs, narrow experiments, and recognized limitations—similar strengths and weaknesses profile to KOALA. D-PDDM (5.00) provides theoretical guarantees and experiments but with assumptions that limit applicability. The KOALA paper's non-standard evaluation metrics and missing baselines place it slightly below the clearer contributions of these anchors.

**Final score: 5.0.** The paper has a genuinely interesting idea and a clean experimental demonstration of metric complementarity. However, the non-standard evaluation metrics (which make the headline numbers misleading), the absence of any comparison to existing detectors, and the lack of adaptive attack evaluation are significant gaps that prevent acceptance in the current form. The paper would benefit from a focused revision addressing these issues.

**Decision: Reject**

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>