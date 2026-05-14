Now I have enough information to write a thorough, calibrated review. Let me compile the final consolidated assessment.

## Summary

The paper proposes KOALA, an adversarial detector that flags attacks when predictions from two complementary similarity metrics—KL divergence and an L0-based score—disagree. The method requires only a lightweight fine-tuning on clean images, uses a nearest-prototype classifier, and comes with a claimed formal proof of correctness (Theorem 1). Experiments are conducted on ResNet-18/CIFAR-10 and CLIP ViT-B/32/Tiny-ImageNet.

## Strengths

- **Well-motivated complementarity intuition.** The idea that dense, low-amplitude perturbations and sparse, high-impact perturbations are naturally captured by different metrics (KL vs. L0) is conceptually appealing and clearly explained in Section 3.1 and Figure 1. The ablation study in Table 2 does show the KL+L0 combination outperforming individual metrics or other pairings on ResNet/CIFAR-10.

- **Lightweight training recipe.** KOALA requires no adversarial training or architectural changes—only fine-tuning with clean images (Section 3.3). This is a practical advantage over methods that need attack examples or model modification.

- **Theoretical condition is empirically verified on compliant samples.** Table 1 confirms that on the subset of test samples satisfying Theorem 1's conditions, KOALA achieves perfect detection (precision=1.0, recall=1.0) across all attack budgets, demonstrating that when the precondition holds, the mechanism works as intended.

- **Systematic ablation over metric combinations.** Experiment 2 (Table 2) and Experiment 3 (Tables 3-4) compare seven different metric objectives, providing a fairly thorough picture of trade-offs between detection and classification accuracy.

## Weaknesses

### Fatal

None. However, the combination of the following major issues collectively undermines the paper's core contributions.

### Major

1. **The formal proof contains significant mathematical gaps.** This is the paper's main distinguishing feature, so these issues are serious.

   - **Unjustified claim about δ.** Line 1198 states that δ lies in [0,1] "thanks to Assumption A1." But A1 only normalizes feature embeddings (coordinates sum to 1). The perturbation δ is bounded by A3 as |δ_i| ≤ (3/2)|p_i^*|, which permits individual |δ_i| > 1 when p_i^* is small. The subsequent remainder bounding relies on this claim.

   - **Inequality direction in Equation 14 is not justified.** The proof drops the negative second-order Taylor term plus remainder, concluding (ĉ − c^*)(δ/p^*) > Δ_KL(p^*). However, (ĉ_i − c_i^*) can be negative for some coordinates i, which would flip the inequality direction for those components. The proof does not account for this sign issue, so the claimed inequality does not follow from the preceding steps without additional assumptions not stated.

   - **Assumption A1 (softmax normalization) is non-standard for feature embeddings** and would fundamentally alter the geometry of the representation space. Assumption A3 (|δ_i| ≤ (3/2)|p_i^*|) is a per-coordinate bound that no standard attacker respects—attackers constrain ℓ_∞ or ℓ_2 norms, not coordinate-wise ratios to original values. The theorem's guarantee therefore applies in a setting that does not correspond to common threat models.

   These gaps mean the "formal guarantee" is not, in its current form, a valid mathematical proof.

2. **No comparison to any existing adversarial detector.** The entire experimental section is an ablation over metric combinations within KOALA's own framework. There is no comparison to NIC, MagNet, LID, Mahalanobis, CADet, or any other prior detection method. Without baselines, there is no evidence that KOALA is competitive with the state of the art. For a detector paper, this is a critical omission.

3. **No evaluation against adaptive attacks.** The decision rule is fully known (flag when ŷ_KL ≠ ŷ_L0). An attacker aware of this rule can optimize a perturbation to make both metrics predict the same wrong class, trivially bypassing detection. The paper never tests this scenario. Without adaptive attack evaluation, detection claims are unsubstantiated—prior work has shown that many detectors are broken under adaptive adversaries (see Tramer et al., 2020; Athalye et al., 2018).

4. **Non-standard confusion matrix definitions inflate detection metrics.** Under the paper's definition (lines 496-499), an attacked input that is *not* flagged by the detector but is still correctly classified (ŷ = y*) is counted as a True Positive rather than a False Negative. This means TP includes cases where the detector failed to detect the attack but the classifier happened to predict the right class. Standard evaluation treats "input is attacked" as the positive condition and "detector flags attack" as the positive prediction; applying that standard would lower the reported recall and precision. The paper should report standard confusion counts and justify why its definition is preferable.

### Minor

5. **Theorem's conditions are satisfied by very few CLIP/Tiny-ImageNet samples.** Only 510/5000 (10.2%) of CLIP/Tiny-ImageNet test samples satisfy the theorem's conditions. The paper notes this (attributing it to CLIP's compact embedding space) but does not discuss what this means for practical deployment—on CLIP, the formal guarantee is essentially vacuous for 90% of inputs. The ResNet/CIFAR-10 proportion (≈67%) is a majority, but still leaves a substantial non-compliant fraction.

6. **Key hyperparameters lack sensitivity analysis.** The L0 threshold τ = 0.75 and loss weights ω_L0 = 0.9, ω_KL = 0.1 are set without any ablation study. The paper says ω_L0 = 0.9 because "L0 is harder to optimize" but provides no evidence. The detector could be brittle to these choices.

7. **Only ℓ_∞ attacks with small perturbation budgets (2/255, 4/255) are evaluated.** No ℓ_2 attacks, no larger ϵ values, no attack parameter sweeps. The 4/255 ℓ_∞ bound is relatively weak.

8. **CLIP results show counterintuitive behavior that undermines the method's rationale.** The paper notes that on CLIP/Tiny-ImageNet, KL+L0+Cosine achieves high detection because "all three metrics are essentially 'randomly guessing' a class," making disagreement likely by chance. This suggests the detection mechanism on CLIP is not operating through the claimed geometric principle but through a degenerate artifact, calling into question the method's generality.

### Trivial

- None that survive the filtering rules.

## Nice-to-Haves

- Including ℓ_2 attacks and larger ℓ_∞ budgets would strengthen the evaluation.
- A sensitivity analysis of τ and loss weights would help validate the design choices.
- A t-SNE or PCA visualization of the embedding space before/after fine-tuning would help build intuition for the prototype separation claim.

## Removed Points

- The critic's claim that only a "small fraction" (3345/5000 = 66.9%) of ResNet/CIFAR-10 samples satisfy theorem conditions is misleading—a majority are compliant. Kept the point for CLIP (10.2%).
- The critic's claim about "no information about how many training images" and ambiguous "development sets"—the paper states "randomly split the development sets into two equal halves," which is clear enough.
- Formatting/style nitpicks (table formatting, typos, missing appendix references) are parser artifacts per instructions.
- The Strength Finder's strength about "provable detection guarantee" is removed because the verified proof weaknesses contradict it (weakness wins per rules).
- Missing related work mentions—cannot confirm these without external sources per instructions.
- Critic's demand for ImageNet-scale evaluation is scope creep for an ICLR paper proposing a new method.

## Novel Insights

None beyond the paper's own contributions. The core insight (complementary KL and L0 metrics for detecting different perturbation types) is clearly stated by the authors. The review process surfaces that the proof's mathematical gaps and the lack of standard experimental practices (baseline comparisons, adaptive attacks) prevent this insight from being convincingly validated.

## Suggestions

1. **Fix the proof.** The sign handling in Equation 14 needs to be corrected or additional assumptions on the sign of (ĉ − c^*) must be added and justified. The claim that δ ∈ [0,1] must be properly derived or the Taylor remainder bounding reworked. Alternatively, soften the "formal guarantee" framing to describe the result as a partial characterization under strong assumptions.

2. **Add baseline comparisons.** Compare KOALA against at least 3-4 established detectors (e.g., LID, Mahalanobis, NIC, CADet) under identical attack settings on CIFAR-10. Without this, there is no way to judge whether KOALA is useful relative to existing work.

3. **Add adaptive attack evaluation.** The most important experiment missing is: an attacker who knows the decision rule optimizes a perturbation to make ŷ_KL = ŷ_L0 = wrong_class. Report detection rates under this attack. If the method collapses, this must be honestly discussed.

4. **Use standard confusion matrix definitions.** Treat "input is attacked" as the positive condition and "detector flags attack" as the positive prediction. Report both standard and proposed metrics and explain any discrepancy.

5. **Provide τ and loss weight sensitivity analysis.** Vary τ ∈ {0.5, 0.6, 0.7, 0.8, 0.9} and ω_L0 ∈ {0.5, 0.7, 0.9} to show the method is not brittle to these choices.

---

## Calibration Anchors

I compared the paper under review against the following human-reviewed anchors (all from the ICLR 2026 corpus):

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `/home/.../7s3SQMiN3L.md` (Gradient Manifold Geometry) | 3.00 | Similar detection paper with no adaptive attacks. KOALA has an additional fatal issue: its core "provable" claim rests on a flawed proof. |
| `/home/.../64PMEKVZP1.md` (Prediction Inconsistency Detection) | 2.67 | Detection paper that at least included baseline comparisons and adaptive attack attempts. KOALA is weaker for omitting both. |
| `/home/.../Mr9a9XuLTI.md` (A Few Large Shifts) | 4.50 | Stronger detection paper with comprehensive baselines, adaptive attacks, and overhead analysis. KOALA lacks all of these. |
| `/home/.../CSfcpGj48W.md` (Conformal Novelty Detection) | 4.00 | Paper with theoretical analysis that had incomplete proof elements. KOALA's proof issues are more fundamental. |
| `/home/.../hZVSKjtaS5.md` (Adversaries Fight Back) | 4.00 | Well-executed empirical study with thorough adaptive attacks. KOALA lacks adaptive evaluation entirely. |

Relative to these anchors, KOALA has a weaker evaluation than every comparable paper. The lowest-scoring anchors (2.67, 3.00) at least included baseline comparisons or adaptive attacks, which KOALA completely omits. Combined with the genuine mathematical gaps in the proof that is the paper's headline claim, the paper falls below these anchors.

## Score and Decision

**Score:** 2.5

**Decision:** Reject

**Rationale:** The paper has a genuinely interesting intuition (complementary KL+L0 detection), but the central distinguishing contribution—a formal proof of correctness—has significant mathematical gaps that are not fixable through minor revision. The experimental evaluation is critically incomplete: no baseline comparisons to existing detectors, no adaptive attack evaluation, and non-standard metrics that inflate reported performance. The method's hyperparameters lack sensitivity analysis, and the CLIP results suggest the mechanism may not generalize via the claimed geometric principle. While the lightweight training recipe is a practical advantage, it does not compensate for the paper's inability to establish that KOALA is a valid, competitive, or theoretically sound detection method.

MY FINAL SCORE: <pineapple>2.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>