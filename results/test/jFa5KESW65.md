Now I have all the information I need. Let me synthesize the final consolidated review.

## Summary

This paper introduces IRAD, a test-time adversarial defense based on image resampling. It constructs an implicit neural representation of the input image (via LIIF-like networks) and learns a SampleNet that predicts pixel-wise coordinate shifts to resample the image, with the goal of breaking adversarial perturbations while preserving semantic content. The method achieves state-of-the-art robust accuracy under standard (oblivious) AutoAttack across CIFAR10 (89.72%), CIFAR100 (72.49%), and ImageNet (71.60%), and also shows strong results under BPDA-based adaptive attacks (74.32% on CIFAR10), outperforming all non-diffusion baselines. Additionally, IRAD can be combined with DiffPure to achieve ~5× speedup with comparable robustness.

## Strengths

- **Novel perspective on adversarial defense.** The paper is the first to systematically study image resampling as a defense mechanism, framing it as simulating "recapture" of a scene. This is a genuinely different angle from prior purification and adversarial training approaches.

- **State-of-the-art results under standard AutoAttack.** IRAD achieves the highest robust accuracy among all compared methods on all three datasets (Table 1): CIFAR10 89.72%, CIFAR100 72.49%, ImageNet 71.60%, while maintaining high clean accuracy (91.70% on CIFAR10, only ~3 points below the undefended model). The improvements over DISCO (85.63% → 89.72% on CIFAR10) and DiffPure (87.54% → 89.72%) are meaningful and well-supported.

- **Strong BPDA adaptive results.** Under BPDA — the standard adaptive attack in the literature — IRAD achieves 74.32% RA on CIFAR10, far exceeding all non-diffusion methods (next best: Randomization at 34.81%, DISCO at 22.60%). This demonstrates the defense is not trivially broken when the adversary has knowledge of it.

- **Learned SampleNet clearly outperforms naive resampling.** The ablation (Table 7) shows SampleNet achieves 89.72% RA vs. 84.60% (implicit representation alone, w.o. Sampling), 77.90% (spatial-variant naive), and 47.55% (spatial-invariant naive). This cleanly demonstrates the value of learned, input-adaptive pixel shifts.

- **Practical acceleration of DiffPure.** IRAD+DiffPure(t=20) achieves 74.05% RA and 93.42% SA at 27.70 ms/image vs. DiffPure(t=100) at 75.12% RA and 89.73% SA at 132.8 ms/image — a ~5× speedup with near-equal robustness. This is a practically useful result.

- **Strong generalization across architectures and datasets.** IRAD trained on ResNet18 transfers effectively to WRN70-16 (91.66% RA), VGG16_bn (90.50%), and ResNet34 (88.82%). Cross-dataset transfer (CIFAR10→CIFAR100) achieves 67.14% RA vs. 72.49% for a CIFAR100-trained model, which is impressive for a test-time defense.

- **Thorough ablation of training strategies.** Table 6 shows adversarial denoising pre-training is essential (76.69% RA), while clean reconstruction and super-resolution tasks yield near-zero robustness — providing clear evidence for why the implicit representation must be trained to remove perturbations.

## Weaknesses

### Fatal
None.

### Major

- **Standalone IRAD achieves 0% RA under adaptive AutoAttack with no analysis of the failure mechanism.** When the adversary differentiates through the full defense pipeline (Table 5, `tab:AutoAttack_adaptive`), IRAD's robust accuracy collapses to 0% — identical to an undefended model. The paper acknowledges this honestly but offers no analysis of *why* this happens: e.g., is the failure because IRAD is fully differentiable (implicit representation + SampleNet are both neural networks), allowing exact gradient attacks? Does the vulnerability lie in the implicit representation or in SampleNet? Without this analysis, readers cannot assess whether the approach has any fundamental advantage over simpler differentiable defenses that also fail adaptively. This is a significant gap in a paper whose core claim is about enhancing adversarial robustness. While BPDA results (74.32%) mitigate this concern somewhat, the complete lack of analysis for the stronger adaptive scenario is a serious omission.

### Minor

- **Missing adaptive AutoAttack results for ablation variants.** The paper reports adaptive AutoAttack results only for the full IRAD and IRAD+DiffPure, not for the "w.o. Sampling" baseline (implicit representation alone) or other ablation variants. Since the "w.o. Sampling" baseline achieves 84.60% RA under standard AutoAttack, reporting its adaptive AutoAttack result would clarify whether the vulnerability stems from the implicit representation itself or the SampleNet. This is a straightforward experiment that should be added.

- **The hybrid IRAD+DiffPure combination is empirically presented but not analyzed.** The paper shows that IRAD+DiffPure(t=20) matches DiffPure(t=100) at 5× speedup, but offers no principled explanation for *why* this combination works. Does IRAD compensate for the reduced diffusion steps by providing additional perturbation removal? Could similar acceleration be achieved by other light-weight pre-processors? Without analysis, this reads as an empirical observation rather than a principled contribution.

### Trivial

- The motivation example (Figure 1a, real-world viewpoint change) is evocative but the paper explicitly acknowledges at line 34 that "with a single-view input, we can only simulate the 2D transformations," so this is transparently scoped.

## Nice-to-Haves

- Report computational cost for all methods under BPDA adaptive attacks (Table 2 already shows SA/RA; adding cost would mirror Table 5's presentation).
- Include a discussion of *why* differentiable defenses (IRAD, DISCO) fail under adaptive AutoAttack while DiffPure (with its stochastic sampling) does not — this would strengthen the paper as a case study for the community.

## Removed Points

These points were removed from the main weakness section for the following reasons:

1. **"Cross-dataset generalization is weak in absolute terms"** — Removed: The paper's claim is that cross-dataset *transfer* is impressive, which it is. A CIFAR10-trained IRAD achieving 67.14% RA on CIFAR100 (vs. 72.49% for a dedicated CIFAR100-trained model) is a strong generalization result, not a weakness. The critic evaluated against the wrong expectation.

2. **"The motivation example is overclaimed / the method never simulates viewpoint change"** — Removed: The paper explicitly states at line 34 that "with a single-view input, we can only simulate the 2D transformations." The scope is clearly defined. The metaphor in the introduction is typical framing and does not constitute a technical flaw.

3. **The suggestion about DiffPure(t=20) as a standalone baseline** — The paper already includes DiffPure(t=20) as a standalone row in Table 5 (RA 8.01%), so this suggestion is already addressed.

## Novel Insights

The most interesting insight from these reviews — one that goes beyond what the paper itself states — is that the adaptive AutoAttack failure of IRAD (and DISCO) likely stems from architectural differentiability rather than any specific design flaw in the resampling mechanism. The fact that DiffPure survives adaptive AutoAttack while IRAD does not suggests that the stochasticity/differentiability boundary is the key factor: DiffPure's reverse diffusion process involves sampling steps that create a non-differentiable or high-variance gradient estimate, while IRAD's feedforward neural networks provide clean gradients for the attacker. This observation, if validated, would imply that any fully differentiable test-time defense will likely fail under exact-gradient adaptive attacks, and that the practical contribution of such methods lies either in (a) settings where the adversary has limited capability (oblivious or BPDA-approximate attacks) or (b) as components in hybrid systems where another defensive mechanism (like DiffPure) provides gradient obfuscation. This reframing would give the paper a clearer intellectual contribution: not "a robust standalone defense" but "a learned resampling component that is most valuable as an efficiency accelerator for stochastic defenses."

## Suggestions

1. **Add a section analyzing the adaptive AutoAttack failure.** At minimum, report whether the "w.o. Sampling" baseline also collapses to 0% RA under adaptive AutoAttack, and explain *why* — connect the failure to the differentiability of the implicit representation and SampleNet. This would turn a current weakness into a useful community insight.

2. **Reframe the paper's contribution** to better match the evidence. The strongest supported claim is: (a) image resampling is a novel and effective defense against standard oblivious attacks, (b) IRAD is partially robust under BPDA adaptive attacks, and (c) IRAD can substantially accelerate diffusion-based purification. The claim that IRAD is a "generally robust standalone defense" needs qualification given the adaptive AutoAttack results.

3. **Add a comparison of DiffPure(t=K) with vs. without IRAD for several values of K** beyond just t=20, to better characterize where IRAD provides the most benefit in the hybrid setting.

## Score and Decision

The paper makes a genuinely novel contribution to adversarial defense by identifying and systematically studying image resampling. The empirical results under standard evaluation protocols are strong, the ablations are thorough, and the practical acceleration of DiffPure is valuable. The paper is honest about its limitations (the 0% adaptive AutoAttack result is reported, not hidden). However, the lack of analysis for the adaptive AutoAttack failure is a significant gap that prevents readers from understanding the fundamental properties of the approach, and the core claim needs more careful scoping. The paper would benefit from a revision that adds this analysis and reframes the contribution accordingly.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>