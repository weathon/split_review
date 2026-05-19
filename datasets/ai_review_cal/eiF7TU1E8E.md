- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6
Here is the consolidated review.

---

## Summary

This paper addresses whether GAN optimization actually moves the generator distribution closer to the target distribution. The authors derive three sufficient conditions (*direction optimality*, *separability*, *injectivity*) under which the discriminator serves as a distance between distributions — connecting GAN objectives to sliced optimal transport theory. They propose the Slicing Adversarial Network (SAN), a simple modification that normalizes the discriminator's final linear layer onto a hypersphere and adds a loss term to enforce *direction optimality*. Experiments on DCGAN, BigGAN, and StyleGAN-XL show consistent FID/IS improvements across multiple loss variants.

---

## Strengths

1. **Novel theoretical framework connecting GANs to sliced optimal transport.** The paper formally derives sufficient conditions (direction optimality, separability, injectivity) under which the discriminator acts as a distance between distributions without requiring optimality (Theorem 1, Section 4). This reframes GAN optimization in terms of metrizability and is supported by a chain of lemmas and propositions (Lemmas 1–4, Propositions 1–3).

2. **Simple, broadly applicable modification.** SAN requires only two changes to existing GAN implementations: constraining the final linear layer's weight to lie on the hypersphere and adding the direction-optimality loss term (Eq. 9, Section 5). It works with Hinge, Saturating, and Non-saturating losses and is demonstrated on three distinct architectures (DCGAN, BigGAN, StyleGAN-XL).

3. **Consistent empirical improvements across architectures and losses.** On DCGAN (Table 2), SAN outperforms GAN on CIFAR10 and CelebA for all three loss types. On BigGAN (Table 3), SAN improves both FID (8.25 → 6.20 on CIFAR10) and IS. This consistency across multiple settings demonstrates the generality of the approach beyond a single configuration.

4. **Synthetic validation of direction optimality.** Figure 2 directly measures the inner product between the learned direction ω and the numerically computed optimal direction on a mixture-of-Gaussians task. SAN's direction stays substantially closer to optimal throughout training, providing direct experimental evidence for the condition the method targets.

---

## Weaknesses

### Fatal
None.

### Major

- **StyleGAN-XL CIFAR10 SOTA claim is confounded by model size.** The paper honestly discloses (Table 3 caption) that "our StyleSAN-XL model trained on CIFAR10 is larger in model size than StyleGAN-XL." This means the reported improvement (1.36 vs. 1.85 FID) cannot be attributed solely to the SAN scheme — it could partly reflect the added capacity. Since the abstract's headline claim of "state-of-the-art FID score amongst GANs for class conditional generation on CIFAR10" rests partly on this result, the comparison needs a size-matched ablation to be persuasive. (The ImageNet 256×256 result does *not* have this disclosed confound, so it stands as given.)

### Minor

- **Theory–method gap is acknowledged but unresolved.** Theorem 1 requires three joint conditions (direction optimality, separability, injectivity) for full metrizability. SAN explicitly addresses only direction optimality. Separability is asserted to be induced by the first loss term (line 392) without proof or empirical verification in the main paper, and injectivity is noted as "not directly controlled by loss designs" (line 348). The paper is transparent about this, but the theoretical framework and the practical method remain partially decoupled — the guarantee of metrizability does not strictly apply to the trained SAN model.

- **Stop-gradient operator is introduced without motivation or ablation.** Line 391 introduces a stop-gradient operator on ω (for the first term) and h (for the second term) in Eq. 18. The paper does not explain why stop-gradients are needed, what would happen without them, or provide any ablation study justifying this design choice.

- **No hyperparameter sensitivity study for λ.** The trade-off parameter λ is set to 1 throughout (line 393). No sensitivity analysis (e.g., λ ∈ {0.1, 1.0, 10.0}) is provided. This omission makes it unclear whether the method is robust or requires tuning.

- **Missing direct measurement of metrizability.** The paper's central theoretical claim is that under the proposed conditions, the discriminator "serves as the distance between the distributions." Yet the experiments evaluate FID/IS and mode coverage — standard quality metrics — rather than directly testing whether the discriminator loss actually tracks a known distance (e.g., by correlating generator loss against an independently computed Wasserstein distance during training). The inner-product plot (Figure 2) verifies direction optimality but is only one of the three conditions.

---

### Trivial
None.

---

## Nice-to-Haves

- An ablation comparing SAN with and without the 𝒢^h term would help isolate how much of the improvement comes from direction optimality alone versus the combination of both terms.
- For reproducibility, a brief description of how the reweighted measures (̃μ₀^{r∘f} and ̃μ_θ^{r∘f}) are sampled in practice would be helpful.
- An analysis of whether injectivity is approximately satisfied (e.g., via Jacobian rank or reconstruction error) for typical discriminator architectures could tighten the theory–experiment link.

---

## Removed Points

- **BigGAN baseline concern (harsh critic #8):** The reviewer questions that the authors' Hinge GAN implementation (8.25 FID) already outperforms the original BigGAN paper (14.73 FID). This asymmetry favors the baseline (the comparison is against a *stronger* baseline, not a weaker one), making the SAN improvement *more* credible, not less. Removed per the rule that unfair comparisons are only a weakness when they favor the author's method.

- **Speculation about ImageNet model size (harsh critic #1, partial):** The reviewer states "The same size discrepancy likely applies to the ImageNet result (the paper does not state otherwise)." The paper only mentions the size difference for CIFAR10, and no statement is made about ImageNet. This is speculation and is removed.

- **Missing appendix content about separability/injectivity (harsh critic #2, partial):** The reviewer claims "the paper provides no empirical verification that the learned discriminator in SAN actually satisfies separability and injectivity during training." The paper explicitly states (lines 26, 347, 506) that these investigations are in Appendix A.3. The appendix is stripped by the parser; per the rules, criticisms about missing appendix content are removed.

- **"L^h term asserted to induce separability without proof" (harsh critic, Section-by-Section notes):** The paper claims the first term induces separability on h. This is asserted as part of the method design. While it would be strengthened by formal proof, the paper is a machine learning submission, not a pure mathematics paper; the assertion is part of the architectural contribution. Weakened to a minor note in the main review above.

- **Generic scope-creep weaknesses from harsh critic's "Missing Parts" section:** Suggestions like "test whether violating separability degrades performance" and comparisons with ADM-G / Projected GAN ask the paper to address problems outside its stated scope. Removed.

- **Strength Finder strength #3 ("State-of-the-art results")** partially conflicts with the verified model-size confound on CIFAR10. The ImageNet results (2.14 vs 2.30, no known size issue) are retained as evidence, but the CIFAR10 SOTA claim is qualified by the weakness above.

---

## Novel Insights

None beyond the paper's own contributions. The reviews surface the model-size confound on the CIFAR10 StyleGAN-XL experiment and the theory-method gap, but these are limitations the paper partially acknowledges. No reviewer provides a fundamentally new perspective not already present in the paper.

---

## Suggestions

1. **Retrain StyleSAN-XL on CIFAR10 with the same model size as StyleGAN-XL** to remove the capacity confound and either validate or reframe the SOTA claim. If the improvement persists, the headline result is robust; if not, the contribution should be pitched around the consistent (if smaller) gains on DCGAN/BigGAN and the theoretical framework.

2. **Add an ablation of the stop-gradient operator** — show the effect of removing (·)^- from one or both terms to justify this design choice.

3. **Provide a λ sensitivity study** (e.g., 0.1, 1.0, 10.0) on at least one dataset to establish the method's robustness to this hyperparameter.

4. **Add a direct metrizability check:** during training on a simple task, plot the generator's SAN loss against an independently computed distance (e.g., sliced Wasserstein) to verify that the discriminator tracks a distance in practice.

---
