- Decision: Reject
- Avg Score: 5.33
- Scores: 6, 5, 5
Now I have a thorough understanding of the paper. Let me produce the consolidated review.

## Summary

This paper proposes a test-time adversarial defense that excessively denoises inputs along an "opposite adversarial path" (OAP) — moving data further in the direction opposite to an adversarial gradient — and integrates this prior with diffusion models. It also introduces a dual-path diffusion design aimed at increasing attack computation cost, and identifies a pitfall in how AutoAttack (Rand) is applied to diffusion-based defenses (gradient approximation granularity via the adjoint method). The method is evaluated on CIFAR-10 against several attacks, with modest robustness improvements over DiffPure and a large claimed improvement against DiffAttack.

## Strengths

- **Direct empirical support for the core idea**: Table 1 shows that iterating opposite-gradient steps (K=20) on clean CIFAR-10 data raises robust accuracy from 0.18% to 100% using ground-truth labels, providing clear evidence that excessive denoising along the OAP direction can remove adversarial perturbations in principle.

- **Identification of a genuine evaluation pitfall for diffusion-based defenses**: Sec. 3.4 (Table 3) demonstrates across CIFAR-10, CIFAR-100, and ImageNet that using per-step adjoint-method calls (rather than a single call) in AutoAttack (Rand) reduces DiffPure's robust accuracy substantially (e.g., 76.56% → 64.06% on CIFAR-10). This is a concrete methodological contribution to robust evaluation.

- **OAP improves an existing defense as a plug-in**: Adding OAP (K=1) to DISCO raises clean accuracy from 89.26% to 92.5±2.06% and robust accuracy (PGD-ℓ∞) from 82.99% to 88.29±3.3% (Table 1, non-adaptive), demonstrating practical utility as a modular component.

- **Dual-path design imposes genuine computation overhead on attackers**: The proposed method requires 6,880s per image under BPDA+EOT vs. 592s for DiffPure (Table 2), and the paper reports that full-batch testing goes from <1 day to ~2 days on 8×V100s. While some of this is inherent to the dual-path architecture, the overhead is real and a relevant consideration.

## Weaknesses

### Fatal
None.

### Major

1. **Stronger AutoAttack identified but not applied to the proposed defense.** Sec. 3.4 identifies that per-step gradient approximation in AutoAttack (Rand) produces stronger attacks, and states "this kind of adjoint strategy will be used in implementing stronger adaptive attacks" (line 359-360). However, Table 2 (adaptive robustness of the proposed method) only reports results against BPDA+EOT, PGD+EOT, and DiffAttack — it does **not** evaluate the proposed method against the stronger AutoAttack (Rand-Ours) variant. The paper only shows how this attack affects DiffPure (Table 3). This is a critical gap: the paper's own diagnostic for robustness overestimation is not applied to its own defense, making the robustness claims unsupported against the most relevant strong attack.

2. **DiffAttack result (93.75% robust) is reported on an unspecified subset without variance, making it uninterpretable.** The DiffAttack row in Table 2 reports 93.75% robust accuracy (vs. 46.88% for DiffPure), but the clean accuracy for DiffPure in this row (89.02%) differs from the full-test-set values (88.06±2.65%), confirming this is a subset. The paper acknowledges "data size and the given random seeds between adaptive and non-adaptive attacks are quite different" (line 491) but never states the subset size. No standard deviation or confidence interval is given for the PGD+EOT or DiffAttack rows. A single accuracy on an unknown-size subset cannot support the claim that the method achieves near-perfect robustness against DiffAttack.

3. **Full evaluation is limited to CIFAR-10; CIFAR-100 and ImageNet results only cover the AutoAttack pitfall for DiffPure.** The paper claims evaluation on three datasets, but for CIFAR-100 and ImageNet (Table 3) the only results shown are the AutoAttack (Rand) comparison on DiffPure — not the proposed method's robustness on these datasets. The method's scalability and generalization to more complex data are unevaluated.

### Minor

1. **The K=1 choice in the trained purifier vs. the K=20 toy result is insufficiently explained.** Table 1 shows robust accuracy monotonically improving up to K=20 (100%) with ground-truth labels, but the trained purifier peaks at K=1 and degrades beyond (Table "tab: disco vs 3Attacks"). The paper's explanation ("similar to the effect of large step size in gradient descent," line 182) is plausible but vague, and no analysis is provided to verify this hypothesis. This limits understanding of the method's core design parameter.

2. **No ablation of the multi-scale noise training (Eq. 12).** The training in Eq. 12 adds random noise at different scales so the purifier works across diffusion time steps, but there is no comparison showing robustness with vs. without this multi-scale training. The contribution of this design choice is unverified.

3. **DPC design choices are not ablated.** The dual-path method (Sec. 3.3) involves multiple complex components — color transfer, optimal transport target selection, iterative halving of t* — none of which are individually ablated. The paper does not compare the single-path OAP+diffusion (Sec. 3.2) against the dual-path version (Sec. 3.3) under the same adaptive attacks to justify the extra complexity.

4. **Attack time cost conflates defense computation with attack difficulty.** The 6,880s vs. 592s comparison (BPDA+EOT) partly reflects that the dual-path method requires two forward passes per evaluation. The paper does not decompose time into (a) base defense inference per batch and (b) additional gradient computation overhead. While the time cost is relevant, the claim that the defense "forces attackers to spend a great deal of time" overstates what is partially a property of the architecture being inherently slower.

5. **Missing EOT and attack iteration specifications for Table 2.** The number of EOT samples and attack iterations for BPDA+EOT and PGD+EOT in Table 2 are not stated. These are needed for reproducibility and fair comparison.

### Trivial
None.

## Nice-to-Haves
- Evaluate the OAP baseline alone (without dual-path complexity) against the stronger AutoAttack (Rand-Ours) to directly test whether OAP provides genuine robustness or exploits weak gradient approximation.
- Decompose attack time costs into defense inference time and gradient computation overhead.
- Run the DiffAttack experiment on the full test set with confidence intervals.
- Analyze sensitivity to K in the trained purifier across different attacks to strengthen the K=1 choice empirically.
- Evaluate robustness when the downstream classifier is adversarially trained (e.g., AWP) to examine classifier dependence of the OAP direction.

## Removed Points
- "The contribution is overstated" (abstract claim about "first time" AutoAttack pitfall): This is a subjective judgment about presentation, not a specific factual error. The paper does demonstrate the pitfall empirically.
- "The DiffAttack result is anomalous and undermines credibility" (framing as "not believable"): The core concern (subset size, no variance) is retained as Major weakness #2, but the accusation of intentional deception is removed as unsupported. The paper provides an explanation (dual paths), and the anomaly concern is adequately captured by the subset/variance criticism.
- "The OAP baseline is trained with a specific attack, limiting generality": The paper explicitly addresses this (line 152-153) as a plug-and-play design, and the experiments do show generalization to unseen attacks. The critic's concern about classifier dependence is partly addressed by the training setup specification and is not a core flaw.
- Various speculations about what "may" be the case in missing appendix sections: These cannot be verified from the paper as written.
- Nitpicks about the DPC design being "ad-hoc": This is a qualitative judgment; the design is documented with equations and a flowchart. The lack of ablation (kept as Minor #3) is the concrete issue.

## Novel Insights
The reviews surface a pattern common in defense papers: a method identifies a weakness in existing evaluation protocols (here, the granularity of gradient approximation in AutoAttack (Rand)), leverages that diagnosis to argue that prior defenses are overestimated, but then fails to apply the same stricter evaluation to its own defense. This disconnect — diagnosing a problem without testing one's own method against it — is a recurring issue that the field should guard against. The OAP concept (excessive denoising toward a lower-loss region) is genuinely interesting and worth investigating under properly strong attacks; the paper's contribution would be better served by narrowing the scope to a cleanly evaluated OAP baseline rather than adding unfalsified complex components.

## Suggestions
1. **Apply the stronger AutoAttack (Rand-Ours) to your own defense**, at least for the OAP+diffusion baseline (Sec. 3.2), to establish whether the method's robustness holds under the evaluation protocol you yourself identified as necessary.
2. **State all subset sizes explicitly** in every table, and report standard deviations for all robust accuracy numbers.
3. **Add an ablation table** comparing: (a) single-path OAP+diffusion, (b) dual-path without color transfer, (c) full DPC, under the same adaptive attacks, to justify each design choice.
4. **Decompose the per-image attack time** into forward-pass inference cost and gradient-computation overhead, so readers can assess whether the higher time cost is a genuine barrier or an artifact of architectural overhead.
