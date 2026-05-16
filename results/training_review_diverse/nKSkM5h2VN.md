Now I have all the information I need. Let me produce the final consolidated review.

---

## Summary

This paper proposes a test-time adversarial defense with three components: (1) an Opposite Adversarial Path (OAP) baseline purifier that excessively denoises inputs along the direction opposite to the adversarial gradient, (2) integration of this OAP prior with reverse diffusion for guided purification, and (3) a dual-path cleaning (DPC) design that forces adaptive attackers to compute gradients through two paths, increasing attack cost by an order of magnitude. The paper also observes that using a finer-grained adjoint-method approximation in AutoAttack (Rand) reveals robustness overestimation in prior diffusion-based defenses.

## Strengths

- **OAP concept — excessive denoising along the opposite adversarial direction.** The idea of pushing data multiple steps along the negative adversarial gradient (K=-3 to -20) to move away from the decision boundary is genuinely different from single-step Anti-Adv approaches. Table 1 demonstrates this effect dramatically (e.g., 99.86% robust accuracy at K=-10 in a controlled training-set experiment), and Table 2 shows that plugging OAP into DISCO improves both clean accuracy (89.57% → 90.71%) and non-adaptive robust accuracy (73.13% → 86.10%).

- **Dual-path design with explicit attack-cost analysis.** The DPC method is deliberately designed to increase the computational burden on adaptive attackers. Table 4 shows attack time per image: 6,880 sec (DPC) vs 592 sec (DiffPure) for BPDA+EOT, and 22,722 sec vs 3,633 sec for PGD+EOT. The paper transparently studies this trade-off, which is a useful contribution regardless of whether the accuracy gains alone would be convincing.

- **Identification of the AutoAttack (Rand) adjoint-method granularity pitfall.** The paper shows that DiffPure's robust accuracy drops from 76.56% to 64.06% (CIFAR-10/WRN-28-10) when using a multi-call adjoint method instead of a single call, revealing a concrete source of robustness overestimation. This is a practical evaluation note that other researchers can adopt.

## Weaknesses

### Fatal

None.

### Major

- **Adaptive-attack evaluation rests on an undisclosed tiny subset, making the headline numbers uninterpretable.** The 64-image subset is explicitly stated only for the AutoAttack (Rand) comparison (Table "tab: AutoAttack diff," line 356). For the main adaptive-attack table (Table 4, "Adaptive robustness comparison"), the sample size is **not stated**. However, the reported clean accuracies — 100% for Ours under PGD+EOT, 95.31% under DiffAttack — are effectively impossible on the full CIFAR-10 test set (10,000 images) for any input-modifying defense, strongly implying that this table also evaluates on a tiny subset (almost certainly the same 64 images). The paper only vaguely notes that "the data size and the given random seeds between adaptive and non-adaptive attacks are quite different" (line 491). On a 64-image test, a single misclassification shifts accuracy by ~1.5 percentage points, and the standard error at 50% accuracy is ~6.25 percentage points. Claiming state-of-the-art robustness or superiority over baselines from these numbers is not credible without full test-set evaluation or at minimum explicit disclosure with confidence intervals. This is the single most consequential weakness in the paper.

- **BPDA+EOT advantage is within noise.** Table 4 reports 81.25±3.62% (Ours, DPC) vs 80.92±3.53% (DiffPure) for BPDA+EOT — a 0.33 percentage point difference with overlapping confidence intervals. This is a tie, not a win. The paper's claim of superior robustness under adaptive attacks is unsupported by this comparison.

- **DiffAttack result is largely an artifact of attack design mismatch, not fundamental robustness.** The paper explicitly states (line 488) that "DiffAttack focuses on attacking the only one path by computing the gradient on it without meeting our dual path strategy." This means the 93.75% vs 46.88% gap is primarily because the attack was not designed to handle the two-path architecture, rather than because the defense is fundamentally stronger. A properly adaptive attack targeting both paths jointly would be needed to substantiate the claimed advantage.

- **Missing adaptive ablations that isolate the contribution of each component.** The paper includes three components: (i) OAP baseline training, (ii) integration with reverse diffusion, (iii) dual-path cleaning. Table 2 shows the OAP+non-adaptive gain over DISCO, but there is **no adaptive-attack evaluation of the single-path version** (Sec. 3.3) to compare against the dual-path version (Sec. 3.4). Without this ablation, it is impossible to determine how much of the robustness comes from the dual-path architecture vs the OAP-diffusion combination, and whether the 10× attack cost buys any genuine robustness increase beyond attacker ignorance.

### Minor

- **The "safer area" claim is not directly validated.** The central thesis — that excessive denoising along the opposite adversarial direction pushes data to a lower-loss region on the decision surface — is supported only by end accuracy numbers. No loss-landscape visualization, decision-boundary distance measurement, or certified radius comparison is provided. The motivating experiment (Table 1) uses ground-truth labels and a training-set setup that does not directly translate to the test-time defense scenario.

- **"First to present" claims are overstated.** The claim of being "first to present the idea of excessive denoising along the opposite adversarial path" (Contribution 1) should acknowledge that moving data along the opposite gradient direction is present in Anti-Adv (Alfarra et al., 2022), which the paper cites. The novelty is in doing *multiple* steps and training a purifier to learn this mapping, which is a meaningful distinction but should be framed more precisely. Similarly, the "first time" claim for the AutoAttack pitfall (Contribution 4) could be softened given prior work on gradient approximation in diffusion defenses (Lee et al., 2023, cited in the paper as the "surrogate process").

- **The color-transfer / optimal transport step (Sec. 3.4) is introduced without validation.** The paper does not analyze whether the Sinkhorn divergence selects a meaningful target image or whether the color-transfer step actually contributes to robustness. It remains a somewhat ad-hoc engineering choice whose effect is not isolated.

### Trivial

- None.

## Nice-to-Haves

- Running the BPDA+EOT and PGD+EOT evaluations on the full CIFAR-10 test set (10,000 images) would resolve the most critical uncertainty. If computational cost is prohibitive, the paper should be clearly reframed as a proof-of-concept on small subsets and all strong claims of superiority should be retracted.
- A single-path ablation (Sec. 3.3 version) in the adaptive-attack table would isolate the benefit of dual-path complexity.
- A brief analysis (e.g., decision-boundary distance, certified radius, or a loss-surface visualization) supporting the claim that OAP moves data to a "safer area" would strengthen the paper's conceptual contribution.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"The paper does not apply this finer-grained approximation to its own defense in a consistent way."** The paper explicitly states (lines 360, 417-418) that the finer-grained adjoint strategy "will be used in implementing stronger adaptive attacks" in all evaluations. This criticism is contradicted by the text.

- **"The selective use of this attack to deflate DiffPure but not to stress-test competing methods (e.g., Hill et al., ADP)."** Hill et al. and ADP are not diffusion-based; the adjoint-method trick is specific to differentiable diffusion processes and cannot be applied to them. This criticism expects the paper to apply an inapplicable method.

- **"The min-max formulation in the introduction is not used later; it appears decorative."** This is a standard adversarial defense framing that sets up the problem; it does not need to be directly re-derived in later sections.

- **"The derivation from Equation (5) to (8) has thin justification."** While the derivation uses a heuristic approximation (replacing the classifier-condition gradient with a direction toward x^K), this is a design choice that the paper explicitly describes and tests empirically. Reasonable researchers can disagree about its elegance, but this is a methodological taste issue, not a correctness error.

- **"The entire section reads as a collection of ad-hoc engineering choices."** This is a subjective characterization of the dual-path design. The design is described with clear motivation and is tested.

## Novel Insights

The reviewers surface one genuinely insightful observation beyond the paper's own contributions: the paper's core advantage in the DiffAttack comparison (93.75% vs 46.88%) is largely attributable to the attack targeting only one path of a dual-path defense — an artifact of attack design lagging behind architecture, rather than evidence of fundamental robustness. This distinction is important because it means the paper's main claimed win is contingent on attackers not adapting to the dual-path structure, which is an inherently unstable foundation for a defense claim. The paper acknowledges this (line 488) but does not temper its narrative accordingly.

## Suggestions

1. **Disclose the sample size for every experiment in the main tables**, including the adaptive-attack evaluations. If adaptive evaluation is on a subset (e.g., 64 images), state this explicitly alongside the results and add confidence intervals or error bars. Better yet, evaluate BPDA+EOT on the full CIFAR-10 test set.

2. **Add an adaptive-attack ablation comparing the single-path version (Sec. 3.3) to the dual-path version (Sec. 3.4)** under identical attacks (BPDA+EOT, PGD+EOT, DiffAttack). This would isolate the actual robustness contribution of the dual-path complexity from the OAP-diffusion combination.

3. **Design a proper adaptive attack that targets both paths jointly** for the dual-path method. Currently the DiffAttack comparison is uninformative because the attack does not account for the second path.

4. **Soften the "first to present" claims.** The distinction from prior work (especially Anti-Adv) should be clearly articulated rather than claimed ex nihilo. The AutoAttack pitfall finding should be positioned as a practical implementation note rather than a first-ever discovery.

5. **Provide at least one piece of direct evidence** (loss landscape, boundary distance, certified radius) supporting the claim that excessive opposite-direction denoising moves data to a safer region of the loss surface.

## Score and Decision

The paper proposes a genuinely interesting idea (excessive denoising along OAP, dual-path cost increase) and makes a useful practical observation (adjoint granularity for AutoAttack). However, the empirical evaluation has a critical transparency gap: the adaptive-attack results — the paper's main evidence for superiority — appear to be on a 64-image subset without clear disclosure, the BPDA+EOT "gain" is within noise, and the DiffAttack "win" is an artifact of attack design mismatch. The core claims of state-of-the-art robustness are not supported by the evidence as presented. The paper could be strong with substantial revisions, but in its current form it does not meet the standard for acceptance.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>