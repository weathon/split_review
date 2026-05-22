Now I have all the information needed. Let me produce the final consolidated review.

---

## Summary

KOALA proposes an adversarial detector that flags inputs as attacks when class predictions from two complementary nearest-prototype classifiers disagree: one using KL divergence (sensitive to dense, low-amplitude perturbations) and one using an L₀-based metric (sensitive to sparse, high-impact changes). The paper provides a formal proof that under sufficient inter-class prototype separation, no bounded perturbation can simultaneously fool both metrics, forcing disagreement and thus detection. The only training required is lightweight fine-tuning on clean images to align embeddings with both metrics. Experiments on ResNet/CIFAR-10 and CLIP/Tiny-ImageNet with PGD, CW, and AutoAttack attacks are presented.

## Strengths

- **Formal theoretical guarantee with direct empirical verification on the compliant subset.** Theorem 1 establishes explicit conditions under which detection is guaranteed, and Table 1 shows that on samples satisfying these conditions, precision, recall, accuracy, and F1 are all 1.0 across both datasets and perturbation budgets. This direct alignment between theory and experiment is a significant step beyond purely empirical detectors.

- **Lightweight training without adversarial examples or architectural changes.** The fine-tuning procedure uses only clean images and standard losses (Section 3.3), requires no adversarial retraining, no architectural modifications, and no prior knowledge of attack types. This makes KOALA a practical plug-and-play solution for any pre-trained encoder — a clear practical advantage over methods that depend on costly adversarial training.

- **Complementary metric design validated by ablation (on ResNet/CIFAR-10).** The ablation study in Table 2 shows that the KL+L₀ combination consistently outperforms alternative pairings (L₀+Cosine, KL+Cosine) on ResNet/CIFAR-10 by a substantial margin (F1 of 0.87 vs. 0.66–0.74), supporting the claimed complementarity.

- **Substantial improvement in adversarial accuracy on ResNet/CIFAR-10.** Table 3 shows that KL+L₀ fine-tuning achieves 57.32% adversarial accuracy under PGD ℓ∞²/²⁵⁵ versus 45.5% for the baseline — a relative improvement of ~26%. This demonstrates that the dual-metric alignment not only enables detection but also strengthens intrinsic classification robustness on this setup.

## Weaknesses

### Fatal
None.

### Major
- **The detection metric conflates detection with classification robustness, inflating full-test-set results.** The confusion matrix (Section 4.2) defines a True Positive for an attacked input as: `(â, ŷ) = (1, ⟂) ∨ (â, ŷ) = (0, y*)`. This means an input is counted as a detection success even when the detector entirely misses the attack (â=0) — as long as the classifier happens to still output the correct class. This is not measuring detection; it is measuring the combined system's ability to either detect the attack or withstand it. The paper's central claim is about *detection* (title: "Adversarial DETECTOR", abstract: "detects an adversarial attack"), yet the metric conflates two distinct phenomena. The full-test-set numbers reported in the abstract (precision 0.94, recall 0.81 on ResNet/CIFAR-10) are inflated by this definition. **Importantly, this does not affect the Theorem-compliant subset results in Table 1** — on those samples the theory guarantees the two metrics must disagree (â=1), so no attacked input would fall into the (â=0, ŷ=y*) category there. The core theoretical claim stands, but the reported full-test-set detection performance is not trustworthy as a measure of detection ability.

### Minor
- **No comparison against any prior detection method.** The paper evaluates KOALA in isolation (ablations of different metric combinations within its own framework) but provides zero comparison to existing detectors such as Mahalanobis-based detection, feature squeezing, LID, MagNet, or Bayesian uncertainty — all cited in the related work section. Without external baselines, the reader cannot assess whether KOALA's detection performance (even if correctly measured) is competitive or weak relative to the state of the art. This limits the paper's empirical contribution to a demonstration that the method works, not how well it works.

- **The Theorem-Compliant partition criterion is not operationally defined.** The paper states (Section 4.2) that the test set is split based on whether samples "satisfy the conditions of Theorem 1, specifically the sufficient inter-class prototype separation," but does not specify the concrete threshold Γᵢ(ε) or the algorithm used to determine compliance. While the full details are likely in the stripped appendix, the main text provides no way for a reader to understand, evaluate, or reproduce the partition. Given that the perfect scores on this subset are central to validating the theoretical claim, the lack of an explicit criterion is a reproducibility gap.

- **No evaluation against adaptive attacks.** The threat model assumes the adversary does not know about the disagreement-based detector. A security-motivated paper with formal guarantees should ideally test whether an adversary aware of the KOALA detection criterion can craft perturbations that simultaneously fool both metrics while maintaining agreement, or at minimum discuss why adaptive attacks are not applicable to the proposed threat model.

- **Mixed results on CLIP/Tiny-ImageNet weaken generality claims.** On the CLIP model, the KL+L₀ combination does not consistently outperform alternatives (Table 2), and the adversarial accuracy results (Table 4) are substantially less clear-cut than on ResNet/CIFAR-10, with L₀-only fine-tuning often giving the best robustness. The paper's post-hoc explanations are reasonable but the lack of a clean pattern weakens the claim of general applicability.

### Trivial
- Assumption A3 (|δᵢ| ≤ 1.5·|p*ᵢ|) is stated without justification for why this specific bound is "mild and practical." A brief comment on how this relates to the ℓ∞ attack budget would improve clarity.

## Nice-to-Haves

- Adding even one standard detection baseline (e.g., Mahalanobis score on the same encoder, or feature squeezing) would substantially strengthen the empirical positioning of the method.
- Reporting detection performance both with the paper's current metric and with a standard detection metric (TP iff â=1) would allow readers to see the effect of the metric choice and would make the detection claims directly interpretable.
- A sensitivity analysis of the threshold parameter τ in the L₀ metric (Equation 2) would help understand its role in the trade-off between detection sensitivity and specificity.

## Removed Points

The following points from the inputs were removed with justification:

- *"The proof sketch is too vague and the full proof is relegated to the (missing) appendix, so the theoretical contribution cannot be evaluated."* — The appendix is stripped by the PDF parser, not missing from the original submission. The proof sketch in the main text provides the high-level intuition, which is standard for conference papers with appendix proofs.
- *"Assumption A3 is arbitrary and seems restrictive for small embedding coordinates."* — The paper provides a brief justification. This is a standard type of assumption in theoretical robustness work. It is a reasonable modeling choice, not an oversight.
- *"L₀ distance is not standard L₀ norm."* — The paper explicitly defines its own L₀-based metric (Equation 2), and using a non-standard variant is clearly disclosed. This is a notation choice, not an error.
- *"The paper does not report detection performance under adaptive attacks"* (from the Harsh Critic's "Critical Issues" section) — Already listed as a Minor weakness above; kept but downgraded from the critic's implied severity.
- *Several strengths from the Strength Finder were removed:* The strength about "formal guarantee verified experimentally" and "lightweight training" were kept. Strength about "complementary metric design supported by ablation" was kept but qualified. Generic statements about the problem being important were removed as superficial.
- *Strength Finder's claim about "formal proof of correctness" being directly verified* — This is valid and kept, as it anchors a key contribution.
- *Criticism that samples sizes are provided but the partition method isn't explained* — Kept as a Minor weakness. The critic's framing as an "uninterpretable" experiment that could be circular is too harsh; the partition is clearly based on the conditions of Theorem 1, but the criterion is not operationalized.

## Novel Insights

None beyond the paper's own contributions. The core insight — using disagreement between KL and L₀ nearest-prototype classifiers for adversarial detection — is genuinely novel, and the theoretical argument connecting complementary metric sensitivity to forced disagreement is the paper's main intellectual contribution.

## Suggestions

1. **Revise the detection metric** to use a standard definition (TP iff â=1 for attacked inputs). Report both the combined-system metric (current) and the pure detection metric in separate columns so readers can see the effect. This would not change the Theorem-compliant subset results (where detection is guaranteed) but would give honest numbers for the full test set.

2. **Specify the compliance-checking procedure explicitly** — provide the exact formula or algorithm used to determine whether a sample satisfies the conditions of Theorem 1, even if it's deferred to the appendix with a clear statement in the main text.

3. **Add at least one external detection baseline** — even a simple method like Mahalanobis-score-based detection on the same encoder or feature squeezing would provide critical context for the reported detection numbers.

4. **Acknowledge and discuss the metric issue** — explicitly state that on the full test set, some "true positives" correspond to cases where the detector did not fire but the classifier remained correct, and present the pure-detection numbers alongside the combined-system numbers for transparency.

## Score and Decision

### Calibration Report

**Round 1 (Bracketing):** Searched for "adversarial example detection using disagreement between metrics" across three bands. Weak anchors (avg < 3.5): kz78RIVL7G (2.60), KAWlH5pfQu (3.00), l5ouuojPGe (3.00) — all rejected papers with flawed evaluations or incomplete methods. Middle anchors (3.5–7.5): MZ324wU7Hj (6.00), adhxppqQAn (3.75), RzdtpxL0H5 (6.20), 7GCRhebJEr (5.00). Strong anchors (> 7.5): 84n3UwkH7b (8.00), I5lcjmFmlc (8.00), P7KIGdgW8S (8.00), KbetDM33YG (8.00) — accepted papers with thorough, polished evaluations. Initial bracket: **4.5–6.5**. The paper has real theoretical contributions but evaluation issues that prevent it from being in the strong band.

**Round 2 (Narrowing):** Searched for more specific topics within the 4.5–7.5 range. Anchors consulted in full:
- **YmQyEdLIkU** (avg 5.50, Reject) — Theoretical analysis of adversarial examples via kernel eigenvalues, limited experiments on MNIST only. KOALA has broader experiments and a more practical contribution, so it is slightly stronger.
- **adhxppqQAn** (avg 3.75, Reject) — Multi-task consistency detection, tested only against PGD. KOALA is clearly stronger (multiple attack types, two architectures, theoretical proof).
- **1zhM0XkQh0** (avg 5.75, Reject) — ProFeAT, self-supervised adversarial training with strong baselines but marginal novelty. KOALA has more novel architecture but weaker evaluation.
- **RzdtpxL0H5** (avg 6.20, Reject) — DDAD, theory + denoising defense with baselines and adaptive attacks, but impractical batch-processing requirement. KOALA's evaluation is less thorough (no baselines, no adaptive attacks) but the approach is more practical. KOALA is slightly weaker than DDAD.
- **pE6gWrASQm** (avg 6.50, Accept) — On adversarial training without perturbing all examples. Solid experiments, clean paper, accepted. KOALA is not as polished in evaluation.

**Final score determination:** The paper's novel theoretical contribution and clean training recipe are genuine strengths at the ~5.5–6.0 level of the mid-range anchors. However, the detection metric issue and missing baselines prevent it from reaching the level of papers like DDAD (6.20) or the accepted pE6gWrASQm (6.50). The paper is stronger than the 3.75–5.0 anchors that had narrow evaluations. Placing it at **5.5**, which is between the weaker mid-range (adhxppqQAn at 3.75) and the stronger mid-range (DDAD at 6.20, ProFeAT at 5.75), reflecting that the contributions are real but the evaluation has meaningful gaps that need addressing.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>