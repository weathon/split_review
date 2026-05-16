Here is the consolidated final review:

---

## Summary

This paper introduces a theoretical framework connecting GAN optimization to sliced optimal transport by deriving *metrizable conditions* — direction optimality, separability, and injectivity — under which a discriminator's minimization objective behaves as a distance between distributions. Based on this analysis, the authors propose the Slicing Adversarial Network (SAN), a simple modification to the discriminator's objective that enforces direction optimality. SAN converts existing GANs with minimal implementation changes and yields consistent FID improvements across DCGAN, BigGAN, and StyleGAN-XL setups, including a reported state-of-the-art FID among GANs on CIFAR10 and ImageNet 256×256.

## Strengths

1. **Novel theoretical framing of GAN discriminators through metrizability.** The paper connects GAN optimization to sliced optimal transport via the FM\* and max-ASW divergences (Lemmas 1–2, Propositions 1–2), establishing sufficient conditions (*direction optimality*, *separability*, *injectivity*) under which a discriminator's minimization objective serves as a distance between distributions (Theorem 1). This goes beyond prior analyses that assume an optimal discriminator, providing a new lens for understanding GAN training dynamics.

2. **Simple, broadly applicable modification with consistent empirical gains.** The SAN modification (Eq. 9) adds a single loss term to the discriminator's objective that maximizes the inner product between the direction ω and the weighted feature mean difference, with only two implementation changes (normalized final layer + extra term; λ=1 fixed). Despite its simplicity, it yields consistent FID improvements across three GAN loss variants (hinge, saturating, non-saturating) on DCGAN (e.g., CIFAR10: ~24→~20 FID across all losses, Table 1) and on BigGAN (FID 8.25→6.20, Table 2), with non-overlapping confidence intervals in most cases.

3. **Synthetic experiments directly verify the proposed mechanism.** On a mixture of Gaussians (Figure 3), SAN's learned direction ω consistently achieves higher inner product with the estimated optimal direction than GAN's weight, directly confirming that the proposed objective enforces direction optimality as intended. The mode-coverage visualization (Figure 2) further corroborates that SAN avoids the mode collapse observed in hinge and non-saturating GAN baselines.

4. **ImageNet 256×256 improvement without confound.** The StyleSAN-XL model improves FID from 2.30→2.14 and IS from 265.12→274.20 on ImageNet 256×256 (Table 3), where the paper does **not** report a model size increase, making this a cleaner demonstration of SAN's effectiveness at scale.

## Weaknesses

### Fatal
None.

### Major

1. **StyleGAN-XL CIFAR10 result is confounded by increased model capacity.** The caption of Table 3 explicitly states that the StyleSAN-XL model on CIFAR10 is "larger in model size than StyleGAN-XL." The FID improvement from 1.85→1.36 on CIFAR10 — which supports the paper's strongest claim ("state-of-the-art FID score amongst GANs") — cannot be cleanly attributed to the SAN training scheme rather than to added parameters. Without controlling for architecture size (e.g., training a StyleGAN-XL baseline with the matching larger backbone), the headline empirical claim is weakened. This is a structural flaw in the experimental design for the paper's most prominent result. (Note: this concern does **not** apply to the ImageNet 256×256 result, where no model size difference is reported.)

### Minor

1. **No ablation separating the two components of SAN.** SAN modifies two things: (i) the final linear layer is constrained to the hypersphere (normalization), and (ii) the maximization objective is augmented with an extra loss term (Eq. 6). All experiments compare GAN (neither modification) to SAN (both). Without an ablation isolating (a) normalized layer alone, (b) extra loss alone without normalization, and (c) both, the claimed mechanism — that *direction optimality* drives improvement — is not directly supported. The gains could partly stem from the Lipschitz-like effect of normalization or the extra term acting as a generic regularizer. A simple DCGAN-based ablation would resolve this.

2. **Metrizability theory is only partially operationalized.** The main theorem requires all three conditions (direction optimality, separability, injectivity), but SAN only directly enforces direction optimality. The paper acknowledges that injectivity "cannot be directly controlled by loss designs" (line 348) and that separability relies on the original GAN loss. This means the full theoretical guarantee does not apply to SAN in practice. While the paper is transparent about this, it does not discuss what this partial satisfaction means for the practical behavior of SAN-trained discriminators — e.g., whether failure of the other conditions could explain the remaining FID gap to other methods, or whether they are approximately satisfied by high-capacity networks.

3. **No empirical comparison to sliced-Wasserstein-based GAN methods.** Given the paper's framing around sliced optimal transport and its claim that SAN "removes the necessity of the approximation [sorting]" (line 421), a direct comparison to methods such as max-sliced Wasserstein GAN (deshpande2019max) or distributional sliced Wasserstein GAN (nguyen2021distributional) would clarify whether SAN's advantage stems from avoiding sorting or from the metrizability perspective more broadly. The paper discusses these methods conceptually but provides no empirical benchmark against them.

4. **Motivating question and theoretical result have a subtle mismatch.** The introduction asks "whether GAN optimization actually provides the generator with gradients that make its distribution close to the target distribution" — a question about training *dynamics*. The main theorem, however, gives conditions under which the *optimal* solution of the minimization objective coincides with a distance — a statement about the *loss landscape*, not about gradient dynamics. This mismatch may mislead readers about what the theory actually establishes.

### Trivial

- Table 1's use of gray checkmarks and asterisks with a long caption is difficult to parse at a glance. The key takeaway (only SAN achieves direction optimality) could be stated more directly in the table itself.
- The synthetic experiment is 2D, which is standard for illustrative purposes but noted as a limitation.

## Nice-to-Haves

- A brief ablation on the hyperparameter λ (e.g., 0.1, 1, 10) for one dataset would strengthen the claim that the method requires no tuning. Currently λ=1 is fixed without discussion.
- Discussion of potential instability from the weighting functions r_J∘f(x) (e.g., when sigmoid saturates) would be useful for practitioners.
- Reporting recall/density/coverage metrics alongside FID would better connect the synthetic mode-coverage results to the image experiments.
- A small-scale experiment validating whether SAN-trained discriminators actually better satisfy the metrizability definition (beyond the inner-product plot) would strengthen the theory-practice link.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"The same concern [model size confound] applies to the ImageNet results"** (Harsh Critic, Section 6): The paper only reports a model size increase for CIFAR10, not for ImageNet 256×256. This sub-claim is factually unsupported.
- **"The theoretical section is heavy but does not directly drive the method"**: The theory motivates the method through the metrizable conditions framework; this is an opinion rather than a substantive weakness.
- **"Synthetic experiment is low-dimensional"** as a standalone criticism: This is standard for diagnostic experiments and acknowledged by the paper's design; moved to Trivial.
- **"Missing discussion on computational overhead"**: This is a nice-to-have detail, not a weakness affecting the paper's validity.
- **"Limited evaluation metrics"** (only FID/IS): FID and IS are the standard metrics for this class of experiments. Additional metrics are a nice-to-have.

## Novel Insights

The reviews surface two key insights not fully developed in the paper. First, the partial satisfaction of the theoretical conditions in practice (SAN enforces only one of three sufficient conditions) is an important limitation that deserves deeper treatment — the paper acknowledges it but does not analyze whether the remaining conditions hold approximately or what happens when they fail. Second, the confound in the StyleGAN-XL CIFAR10 experiment creates an unusual situation where the paper's strongest empirical claim is also its least controlled; this suggests the paper would be better served by emphasizing the clean, controlled DCGAN/BigGAN experiments as its primary evidence rather than the StyleGAN-XL result.

## Suggestions

1. **Disentangle the SAN modifications with an ablation.** Add an experiment (e.g., on DCGAN CIFAR10) comparing: (a) GAN + normalized final layer only, (b) GAN + extra loss only (without normalization), (c) full SAN. This would reveal whether the direction-optimality loss, the normalization, or both together drive the gains, and would substantially strengthen the causal link to the theory.
2. **Re-run or qualify the StyleGAN-XL CIFAR10 experiment.** Either train a StyleGAN-XL baseline with the same larger architecture as StyleSAN-XL (to control for model size), or explicitly qualify the state-of-the-art claim to acknowledge the confound. The ImageNet result already provides a clean large-scale validation.
3. **Discuss the practical status of the three metrizability conditions.** Add a paragraph explaining whether separability and injectivity are expected to hold approximately in practice (e.g., due to network capacity or data properties) and what the implications are when they do not.
4. **Add a comparison to at least one sliced-Wasserstein GAN variant** (e.g., max-SWGAN) on a small-scale experiment to empirically contextualize the relationship between SAN and sliced optimal transport methods.

## Score and Decision

This paper makes a genuine conceptual contribution (the metrizability framework for GAN discriminators) and proposes a simple method that delivers consistent, non-trivial FID improvements across multiple GAN variants in controlled experiments. The DCGAN and BigGAN results alone convincingly demonstrate the method's value. However, the headline StyleGAN-XL CIFAR10 result — which supports the paper's strongest claim — is confounded by increased model size, and the missing ablation prevents full attribution of the improvement to the proposed mechanism. These are addressable issues that do not invalidate the core contribution, but they limit the paper's current form.

**Score: 6.5** — a solid paper with a notable but fixable flaw in its strongest experiment.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>