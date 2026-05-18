Now I have all the evidence I need. Let me write the final consolidated review.

## Summary

This paper proposes a test-time adversarial defense method that purifies adversarial examples by moving them along the *opposite adversarial path* (OAP) before feeding them to a classifier. The OAP prior is integrated with diffusion-based purification (OAP+DiffPure) and extended to a dual-path cleaning mechanism (DPC) designed to increase the computational cost of adaptive attacks. The paper also identifies a pitfall in AutoAttack (Rand) evaluation for diffusion-based defenses, showing that using multiple adjoint-method calls yields stronger attacks than the single-call approach used in prior work.

## Strengths

1. **OAP improves robustness when combined with existing defenses.** Table 2 shows that adding the OAP prior (K=1) to DISCO raises robust accuracy from 73.13% to 86.10% under non-adaptive PGD-ℓ∞ (ResNet-18) and from 85.00% to 88.79% under non-adaptive AutoAttack (WRN-28-10). This demonstrates that the OAP direction is a generally useful signal that can be plugged into existing purification pipelines.

2. **Identification of the AutoAttack (Rand) evaluation pitfall.** Table 3 demonstrates that DiffPure's robust accuracy drops from 76.56% to 64.06% on CIFAR-10 when AutoAttack (Rand) uses multiple adjoint-method calls instead of a single call, exposing an overestimation in prior evaluations. This is a useful methodological finding for the community studying diffusion-based defenses.

3. **DPC dramatically increases attack time cost.** Table 5 shows the per-image attack time for BPDA+EOT rises from 592.92 sec (DiffPure) to 6880.97 sec (DPC), and for PGD+EOT from 3632.94 sec to 22721.90 sec. This supports the claim that the dual-path design creates a meaningful computational barrier for attackers.

4. **Non-adaptive robustness is strong.** Under non-adaptive attacks (Table 4), the OAP+DiffPure method achieves 88.48±2.04% (PGD-ℓ∞) and 89.06±2.62% (AutoAttack Standard), which are competitive with or better than DiffPure on the same settings.

## Weaknesses

### Fatal

None.

### Major

1. **No ablation study for the dual-path method (DPC).** The DPC design (Section 3.3) introduces multiple components — Sinkhorn divergence-based target selection, color transfer via optimal transport, two independent diffusion paths, and iterated halving of t* — but the paper provides no ablation isolating the contribution of each component. The method transitions from an oracle experiment (Fig. 3 test, where the clean image is assumed available in path p2) to a practical approximation (color-transferred adversarial image in p2) without validating how well this approximation preserves the oracle-level performance. For a method with this many moving parts, the absence of any component analysis is a significant gap.

2. **"Excessive denoising" framing does not match the actual implementation.** The paper is motivated by Table 1, where K=20 steps of opposite-direction movement yields 100% robust accuracy under oracle conditions. However, the actual purifier uses K=1 (a single step), and the paper acknowledges (lines 179–183) that larger K degrades performance when ground-truth labels are unavailable during training. While this inconsistency is discussed, it undermines the central conceptual selling point: the method is not actually "excessive" — a single gradient step is standard in the adversarial defense literature. The novelty reduces to training a purifier toward a shifted target rather than the clean image, which is a modest but non-trivial change.

3. **Test-set sizes for PGD+EOT and DiffAttack evaluations are unclear and likely very small.** In Table 5, the DPC method achieves 100% clean accuracy under PGD+EOT, which strongly implies a tiny test set (likely 32–64 images as with the AutoAttack experiment in Table 3). The paper does not state the sample sizes for these rows. Without knowing the sample size, it is impossible to assess whether the reported robust accuracy differences (e.g., 53.12% vs. 46.88% for PGD+EOT, or the dramatic 93.75% vs. 46.88% for DiffAttack) are statistically meaningful. The DiffAttack result is further discussed below.

### Minor

1. **OAP+DiffPure improvement over DiffPure under adaptive BPDA+EOT is marginal.** Table 5 shows 81.25±3.62% (Ours) vs. 80.92±3.53% (DiffPure) — a 0.33 percentage point difference well within one standard deviation. While the dual-path variant achieves this at 11× higher attack cost, the robustness *gain* from the OAP prior alone under properly adaptive attacks is not clearly established.

2. **The DiffAttack result (93.75%) lacks a properly adaptive attack.** The paper explicitly acknowledges (line 488) that "DiffAttack focuses on attacking the only one path by computing the gradient on it without meeting our dual path strategy." Presenting 93.75% robust accuracy against a non-adaptive-in-this-context attack in the main comparison table without strong qualification is misleading. The authors should either implement a properly adapted version of DiffAttack (e.g., BPDA+EOT through both paths, which is already reported separately) or clearly decouple this result from the main adaptive evaluation.

3. **Defense runtime is not reported.** The paper extensively analyzes attack time cost but never reports the defense's own inference/purification time. Without this, the trade-off analysis is one-sided: the method may increase attack cost by 11×, but if it also increases defense cost by 11×, the practical benefit is different from what is implied.

4. **The clean accuracy improvement from OAP is not discussed.** In Table 2, DISCO+OAP (K=1) improves clean accuracy from 89.26% to 92.5±2.06%. If the purifier pushes inputs *away* from the decision boundary, one would expect clean accuracy to potentially drop. The paper neither explains this nor provides a hypothesis, which leaves an open question about the mechanism.

5. **The AutoAttack pitfall finding is more about attack/evaluation methodology than defense contribution.** While identifying evaluation weaknesses is valuable, this contribution does not directly strengthen the proposed defense. It is tangential to the paper's main claims about the OAP and DPC methods.

### Trivial

- None.

## Nice-to-Haves

- A properly adapted version of DiffAttack (or other SOTA attacks) that differentiates through both diffusion paths and the color transfer step, to validate whether the dual-path design genuinely improves robustness or merely increases cost.
- Reporting defense purification time alongside attack time for a complete cost picture.
- Brief discussion of why OAP improves clean accuracy in the DISCO setting (Table 2).

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Training details insufficient (epochs, LR, batch size).** The paper references supplementary material for details. Per the rules, criticisms about content deferred to the appendix are removed.
- **Missing related works (DDA, GDMP).** Per the rules, suspected missing references cannot be verified and are removed.
- **"Equation not operationalized" criticism about the min-max formulation.** This is a standard general formulation of the test-time defense objective, not a claim that the authors solve the min-max problem jointly. The paper operationalizes a specific instantiation of this framework.
- **"Independence claim overstated" about purifier trained on PGD-7.** The paper states the purifier is trained on PGD-ℓ∞-7 but tested on *different* attacks (PGD-ℓ∞-40, AutoAttack, BPDA+EOT). This is standard usage of "independent of the attacks used in testing" and does not claim the training uses no attack at all.
- **Hyperparameter sensitivity concern.** The paper states the chosen values for η, t*, ε, etc. Ablation studies may be deferred to the supplementary. Removed per the rule on appendix content.
- **"The paper should also cover Y / additional tasks" (CIFAR-100/ImageNet full results).** The paper provides main results on CIFAR-10 and states supplementary results for other datasets. This is scope-appropriate for a methods paper.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Focus the clean evaluation on OAP+DiffPure.** This simpler method (Section 3.2) is well-motivated and its evaluation under non-adaptive attacks (Table 4) is solid. A rigorous adaptive evaluation of this method alone — with full test sets, error bars, and the multi-adjoint AutoAttack strategy — would constitute a cleaner contribution.
2. **For the dual-path extension, provide an ablation study** isolating the effect of: (a) the color transfer module, (b) the second diffusion path, (c) the halved t* iteration. Show whether each component contributes meaningfully to robustness or primarily to time cost.
3. **State sample sizes explicitly** for every row in the evaluation tables, especially where clean accuracy approaches 100%.
4. **Either implement a properly adaptive DiffAttack** for the dual-path method, or explicitly label the reported DiffAttack result as "non-adapted" and separate it from the main adaptive comparison.
5. **Add a brief explanation** for why OAP improves clean accuracy in the DISCO setting (Table 2).

## Score and Decision

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>