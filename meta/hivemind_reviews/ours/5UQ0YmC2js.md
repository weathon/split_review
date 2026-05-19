## Summary
The paper introduces AdvI2I, a framework that trains an adversarial image generator to perturb input images for Image-to-Image (I2I) diffusion models, causing them to output NSFW content even when paired with benign text prompts. An adaptive variant (AdvI2I-Adaptive) incorporates a safety-checker loss and Gaussian noise injection during training to maintain high attack success rates under defenses. Experiments on InstructPix2Pix and SDv1.5-Inpainting across nudity and violence concepts show ASR >78% (no defense) and >70% under Safety Checker for the adaptive variant.

## Strengths
- **Well-motivated and timely problem:** The paper convincingly shows (Table 1) that existing adversarial prompt attacks are detected by simple text filters (average ASR reduction of ~58% under perplexity filter), establishing that exploring the adversarial *image* modality is a necessary direction. This motivation is concrete and backed by data.

- **Novel attack paradigm for I2I diffusion models:** The idea of training a generator to craft adversarial inputs for I2I models—using latent feature matching at the final denoising timestep—is novel. The generator enables single-pass attack on new inputs without per-image optimization, a clear advance over per-instance optimization approaches.

- **Strong empirical evidence of adaptive attack resilience:** AdvI2I-Adaptive maintains 70.5% ASR under the Safety Checker (SC) defense on InstructPix2Pix (nudity), while the non-adaptive version collapses to 18.0% (Table 3). This large gap demonstrates that the adaptive training objective (safety-checker cosine-similarity loss + Gaussian noise injection) genuinely circumvents the most effective defense.

- **Generalization across models, concepts, and unseen inputs:** The method is evaluated across two diffusion models (InstructPix2Pix, SDv1.5-Inpainting) and two NSFW concepts (nudity, violence). Table 5 shows ASR >63.5% on unseen images and >68.5% on unseen prompts, supporting the claim that the generator transfers effectively.

- **Effectiveness at small perturbation budgets:** Table 6 shows AdvI2I-Adaptive achieves 61.0% ASR under SC even at a noise bound of 32/255 on InstructPix2Pix, demonstrating the attack remains potent with minimal visual distortion.

## Weaknesses
### Fatal

None.

### Major

- **Generator architecture is critically underspecified.** The paper states only that it "leverages a pre-trained VAE as the adversarial image generator" (line 130). It is never clarified whether this is the VAE decoder (fine-tuned), the encoder part, a separate network appended to the VAE, or the full VAE as a frozen feature extractor. Training details (learning rate, optimizer, batch size, number of steps, VAE variant used) are entirely absent. Algorithm 1 provides pseudocode but omits the architectural backbone. Without this information, the core mechanism of the attack is opaque and the results cannot be independently reproduced or built upon.

- **"W/o Generator" baseline is introduced but results are never reported.** The paper states in Section 4.1 that "we introduce another variation, 'W/o Generator,' as an ablation study, where we remove the adversarial noise generator and directly optimize adversarial perturbations." However, no results for this baseline appear in any table. This is the exact per-image optimization baseline that would establish an upper bound and contextualize the generator's advantage. Its absence leaves a significant evidential gap: we cannot tell whether the generator's batch generalization is critical or whether even simple per-image perturbations would achieve comparable ASR.

- **A claimed transferability experiment is never delivered.** The paper states (line 197–198) "We also evaluate the transferability of AdvI2I from SDv1.5-Inpainting to other SD inpainting models," but no such results are presented in the main paper. This appears to be an experiment that was planned or performed but omitted from the manuscript.

### Minor

- **Safety Checker modeling is vague and the proxy loss is unvalidated.** The paper describes the safety checker as "comparing [features] with predefined NSFW concepts using cosine similarity in the latent space" (line 142). It does not specify which exact safety checker implementation is used, how the NSFW concept vectors \(C_i\) are obtained, or whether \(\mathcal{L}_{sc}\) operates in the same feature space as the real checker. The loss uses the one-step denoised latent \(f^1\) as a proxy for the final output, but this approximation is validated neither quantitatively nor qualitatively. If the proxy is unfaithful to the full diffusion output, the reported ASR under SC could be misleading.

- **Dataset domain is narrow and potentially biased.** The training images come from the "sexy" category of an NSFW Data Scraper, filtered to remove NSFW-classified images. While this yields nominally safe images, they contain suggestive attributes (e.g., exposed skin, provocative posing) that may make transitioning to nudity easier than from general-purpose images. The "unseen" evaluation draws from the same distribution, so it does not test generalization to neutral domains (e.g., landscapes, objects). The attack's scope may thus be narrower than the paper's language suggests.

- **No confidence intervals or multiple-run statistics.** Results are reported as single percentages without variance estimates. With an evaluation set of 200 samples, a reported 81.5% ASR has a ~95% confidence interval of roughly ±5.3 percentage points. Some experiments should be repeated (e.g., 3 seeds) to establish reliability.

- **"Universal" terminology is non-standard.** The paper calls the attack "universal and transferable across multiple images" (line 127). In adversarial-attack literature, "universal" typically means a single perturbation fools a model on all inputs. Here, the generator produces different perturbations per input. The paper's usage is explained, but it will confuse readers familiar with standard terminology.

### Trivial

- **No limitations discussion in the conclusion.** The conclusion (Section 5) does not discuss limitations or failure modes of the attack (e.g., conditions under which it might underperform). Adding a brief paragraph would improve scholarly completeness.

## Suggestions
1. **Specify the generator architecture explicitly.** State whether the VAE decoder is fine-tuned, a separate network is attached, or something else. Provide a diagram or cite a specific architecture reference. Report training hyperparameters (learning rate, optimizer, batch size, steps).
2. **Report the "W/o Generator" baseline results.** This is the most informative missing data point—it would directly separate the value of the generator (convenience/generalization) from the value of the underlying attack objective.
3. **Validate the safety checker proxy loss.** Show a correlation between the \(\mathcal{L}_{sc}\) value computed on the one-step proxy \(f^1\) and the actual safety checker output on the full diffusion output. Report which exact safety checker implementation was used and how concept vectors \(C_i\) were obtained.
4. **Either deliver the promised transferability results or remove the claim.** The paper states it evaluates transferability to other SD inpainting models but provides no results.
5. **Add variance estimates.** Report results over at least 3 random seeds or provide confidence intervals for the main tables.

## Score and Decision

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>

## Questions


## Decision
Reject
