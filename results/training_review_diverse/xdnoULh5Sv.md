Now I have all the information needed to write the consolidated review. Let me compose it.

Here is my final consolidated review:

---

## Summary

This paper proposes CARSO, a hybrid adversarial defence that tightly integrates adversarially-trained classifier with a conditional VAE purifier. The purifier learns to map the classifier's internal (pre)activation representations (extracted during a forward pass of a potentially perturbed input) back to clean reconstructions. At inference, multiple stochastic reconstructions are drawn, classified by the same adversarially-trained model, and aggregated via a novel double-exponential product. The architecture is end-to-end differentiable, avoiding gradient obfuscation. Evaluated on CIFAR-10, CIFAR-100, and TinyImageNet-200 under ℓ∞ white-box attacks (randAA, Pgd+EoT), CARSO reports substantial robust accuracy improvements over both the underlying classifier and prior state-of-the-art AT/purification methods, with a moderate clean accuracy cost.

---

## Strengths

- **Novel, principled integration of adversarial training and purification via internal representation conditioning.** The key idea — using the adversarially-trained classifier's own (pre)activation trace to condition a generative purifier — is architecturally novel and avoids the gradient-obfuscation pitfalls that plague many prior purification works (Defense-GAN, PuVAE, diffusion-based purifiers). The design makes the entire pipeline exactly differentiable end-to-end, enabling reliable adaptive attacks. The paper correctly distinguishes this "organic merge" from the mere stacking of a purifier before a classifier (Section 4.1).

- **Consistent and substantial robust accuracy gains across three datasets under standardised attacks.** On CIFAR-10, CARSO improves robust accuracy from 67.73% (classifier alone) to 76.13% under randAA, and from 71.07% (best AT model) to 76.13%. On CIFAR-100, the gain over the classifier is +27.47 percentage points (39.18% → 66.65%). On TinyImageNet-200, the gain is +22.26 points (31.30% → 53.56%). These gains are achieved while using the same classifier architecture as the base, unlike many SOTA AT methods that scale to much larger models.

- **Rigorous evaluation methodology for a stochastic defence.** The paper uses randAA (AutoAttack adapted for stochastic defences, with 20 EoT iterations), supplemented by the Pgd+EoT pipeline (200 steps, 20 EoT) from Lee2024Robust — the gold standard for evaluating stochastic purifiers. A gradient-obfuscation sanity check at ε=0.95 confirms accuracy below random chance (Table 5.2). Training hyperparameters are reported extensively in the appendix, supporting reproducibility.

- **Novel, theoretically-motivated aggregation strategy.** The double-exponential product aggregation (Section 4.5) is justified via a heuristic analysis showing it is more resistant to adversarial logit manipulation in individual reconstructions than standard logit averaging or probability averaging (Appendix 4). While empirical validation is needed, the theoretical motivation is clear and non-trivial.

---

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Missing ablation studies on key design choices.** The paper makes several strong claims without systematic empirical validation on the main datasets. No ablation is provided for: (a) the double-exponential aggregation strategy vs. simpler alternatives (logit averaging, probability averaging), (b) the number of reconstruction samples N (fixed at 8), (c) the necessity of each component in the adversarially-balanced batch composition (FGSM/PGD at two strengths each). The claim "any smaller subset of attack types and strengths… always experimentally results in a worse performing purification model" (Section 4.4) is stated without supporting data on CIFAR-10/100/TinyImageNet — the preliminary experiments on MNIST/Fashion-MNIST (Appendix 7) are described qualitatively. Without ablations, it is unclear which components drive the gains. This does not invalidate the paper's core contribution but weakens the method's analysis.

- **Large robust accuracy gains that would benefit from additional attack verification.** The gains on CIFAR-100 (+27.47 pp) and TinyImageNet (+22.26 pp) are unusually large relative to prior purification work. While the evaluation uses standard protocols (randAA with 20 EoT, Pgd+EoT, gradient-obfuscation check), the paper does not explore whether increasing EoT iterations (e.g., 40, 80) or checking convergence of the PGD objective would alter the reported numbers. This is a reasonable concern given that the stochasticity of the decoder interacting with learned conditioning on internal representations could create a challenging optimisation landscape for the adversary. The authors should demonstrate that robust accuracy stabilises with stronger attacks. This is a cautionary note, not a fatal flaw — the current evaluation follows community standards.

- **The "first-principles justification" (Section 4.2) is presented without empirical support.** The claim that the internal (pre)activation trace "constitutes a richer characterisation" than the input alone for reconstructing clean data is intuitively plausible but not empirically validated (e.g., by comparing performance when conditioning on input vs. internal representations). The paper would benefit from a brief citation to feature-inversion or representation-learning literature to ground this claim, or a small-scale supporting experiment.

### Trivial
None.

---

## Nice-to-Haves

- A small-scale ablation on CIFAR-10 comparing aggregation strategies (double-exponential product vs. logit averaging vs. probability averaging) would significantly strengthen the paper's methodological contribution.
- Reporting variance or confidence intervals on robust accuracy (e.g., over multiple test-set evaluations or random seeds) would be helpful for a stochastic defence.
- A convergence check on the PGD loss during attack generation would further reassure readers that the adversary has optimised sufficiently.

---

## Removed Points

- **"Incomplete and misleading comparison with purification baselines on CIFAR-100"** — REMOVED because the asymmetry favours the baseline, not the authors. The paper transparently states: "In the absence of a reliable robustness evaluation by means of Pgd+EoT for the best purification-based method [Lin2024Robust], we still obtain a +20.25% increase in robust accuracy upon its (largely overestimated) AA result." The baseline's AA result (46.09%) is known to be overestimated for stochastic defences; if properly evaluated, it would be *lower*, making CARSO's reported advantage a conservative estimate. Per the rule: when the asymmetry favours the baseline, such criticisms are removed.

- **"The claim of first attempt to organically merge AT and purification is slightly over-stated"** — REMOVED (moved here from harsh critic's section notes). The paper acknowledges Defense-GAN and PuVAE in its related work section. Its contribution is specifically about *organic* merging via internal representation conditioning, which is architecturally distinct from stacking a purifier before a classifier. The claim is appropriately qualified with "to the best of our knowledge." Not a valid weakness.

- **Strength Finder point 5 ("Practical training protocol with careful ablation")** — REMOVED because it conflicts with the verified weakness about missing ablation studies. The paper describes preliminary experiments on MNIST/Fashion-MNIST qualitatively, but does not provide systematic ablations on the main datasets — the strength overstates the evidence.

---

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface a novel interpretation that the authors had missed.

---

## Suggestions

1. **Add ablation studies on CIFAR-10** for the aggregation strategy (double-exponential product vs. logit averaging vs. probability averaging), the number of reconstruction samples (N=1,4,8,16), and the batch composition. This would validate which components drive the observed gains.
2. **Strengthen attack verification** on CIFAR-100 by evaluating with 40 and 80 EoT iterations, and report the final PGD loss values to demonstrate adversarial convergence. This would address the credibility concern about unusually large gains.
3. **Add an empirical sanity check** for the core claim that conditioning on internal representations is more informative than conditioning on the input directly — even a small-scale reconstruction quality comparison would help motivate the architecture.

---

## Score and Decision

This is a method paper presenting a novel, principled architecture that tightly integrates adversarial training and purification. The core idea — using internal classifier representations to condition a VAE purifier — is well-motivated and architecturally sound. The evaluation is largely thorough, following established protocols for stochastic defences (randAA, Pgd+EoT, gradient-obfuscation check). The results are consistent and substantial across three datasets.

The main weaknesses are: (1) missing ablation studies that leave the contribution of individual design choices unvalidated, and (2) unusually large gains that, while evaluated with standard tools, would benefit from additional attack verification to fully rule out underpowered-adversary concerns. Neither is fatal — both are addressable with additional experiments.

The paper makes a genuine contribution: it demonstrates that conditioning a generative purifier on an adversarially-trained classifier's internal representations can substantially improve robustness beyond either AT or purification alone, while maintaining a fully differentiable pipeline. This opens a new design direction for hybrid defences.

**Score:** 7.5

**Decision:** Accept

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>