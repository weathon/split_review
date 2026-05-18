Now I have all the information I need. Let me construct the consolidated review.

---

## Summary

This paper proposes CARSO, an adversarial defence that synergistically blends adversarial training and adversarial purification. CARSO uses a conditional VAE purifier trained to reconstruct clean images from the internal representations of a frozen adversarially-trained classifier. At inference, multiple reconstructions are sampled, classified, and their outputs aggregated into a robust prediction. The method achieves strong robust accuracy on CIFAR-10 (76.13% randAA), CIFAR-100 (66.65% randAA), and TinyImageNet-200 (53.56% randAA), substantially outperforming both AT-only and purification-only baselines.

## Strengths

- **Novel synergistic architecture with strong empirical results.** The core idea — conditioning a VAE-based purifier on the classifier's internal representations and aggregating multiple reconstructions — is conceptually clean and demonstrably effective. CARSO outperforms the best AT-only model by +5.03% (CIFAR-10), +23.98% (CIFAR-100), and +22.26% (TinyImageNet-200) on robust accuracy, and surpasses the best purification baseline even after correcting for overestimated diffusion-based evaluation. These gains are substantial and consistent across all three datasets.

- **Rigorous evaluation that addresses known pitfalls of stochastic defences.** The paper uses randAA (AutoAttack with 20 EoT iterations) for evaluation, explicitly designed for stochastic defences. It additionally performs a gradient obfuscation sanity check at ε∞=0.95, obtaining accuracy below random chance (Table 2). This level of evaluation rigour is commendable and strengthens confidence in the claimed robustness.

- **Fully differentiable end-to-end design.** By deliberately choosing a conditional VAE (decoder-only at inference) as the purifier, the architecture is algorithmically differentiable end-to-end, avoiding backward-pass approximations that can introduce gradient obfuscation. This design choice is principled and enables reliable white-box evaluation.

- **Significant gains on high-class-count datasets.** The improvements on CIFAR-100 (+23.98%) and TinyImageNet-200 (+22.26% over the base classifier) are particularly striking, demonstrating that the method scales effectively to more complex tasks where pure adversarial training has plateaued.

## Weaknesses

### Major

- **No ablation studies.** The paper introduces several specific design choices — the robust aggregation strategy (exponential of exponential, Section 4.6), the composition of adversarially-balanced batches (Section 4.4), the hierarchical internal representation encoding (Section 4.3), the number of reconstruction samples (N=8), and the adversarial batch fraction (0.5/0.15/0.01 per dataset) — but none are systematically ablated. Without ablations, it is impossible to know which components drive the observed gains, whether simpler alternatives (e.g., logit averaging, uniform adversarial fraction) would perform similarly, or how sensitive the method is to hyperparameter choices. The heuristic justification of the aggregation strategy (Appendix E) is purely analytical and does not substitute for empirical validation. For a methods paper introducing multiple new components, this is the most significant gap.

### Minor

- **Training–evaluation adversarial mismatch.** The purifier is trained on adversarial examples generated against the *classifier alone* (Section 4.1: "adversarially-perturbed examples are generated against the classifier"), never against the full CARSO architecture. At test time, however, the adaptive attacks in randAA (§6.1) optimize perturbations end-to-end through the entire system. This creates a distribution mismatch: the purifier learns to reconstruct from internal representations of inputs perturbed only by attacks on the frozen classifier, but during evaluation it must handle representations produced by attacks crafted to fool the combined system. The strong empirical results suggest the method generalizes despite this gap, but the authors should discuss why this mismatch does not undermine the defence or provide evidence (e.g., representation similarity analysis) showing it is benign.

- **Asymmetric headline comparison against the purification baseline (CIFAR-10).** The primary robust accuracy reported for CARSO is randAA (76.13%), while the diffusion baseline's comparison number is its Pgd+EoT result (66.41%). The headline "+9.72% increase" therefore compares two different evaluation protocols. The paper does transparently report CARSO's own Pgd+EoT result (76.89%) and notes that CARSO's randAA is *lower* than its Pgd+EoT, making the comparison conservative from one perspective. However, the headline asymmetry remains and could confuse readers. A fairer presentation would either compare both under Pgd+EoT or explicitly state both numbers in the headline comparison.

- **No variance or confidence intervals reported.** Given the stochastic nature of the purifier (random latent variable sampling), robust accuracy may vary across seeds and test-time sampling. Single-run results without variance estimates limit the reader's ability to assess result reliability.

- **Inference cost not reported.** The paper reports only training time (e.g., 159 minutes on CIFAR-10). CARSO requires 8 forward passes through the classifier plus one VAE decode per input, making it substantially more expensive than standard AT. Reporting wall-clock time or FLOPS would help readers assess practical trade-offs.

### Trivial

- The "first-principles justification" in Section 4.2 is speculative and does not add much beyond what is already conveyed by the architectural description. This is a presentation preference, not a flaw.

- The clean accuracy drop on TinyImageNet-200 (−8.87%) is noted but the paper could more thoroughly discuss whether better generative models (e.g., VQ-VAE) could mitigate this while preserving differentiable evaluation.

## Nice-to-Haves

- A qualitative figure showing clean images, adversarially perturbed inputs, and several reconstructed samples from the purifier would provide useful intuition about the method's behaviour and failure modes.
- Demonstrating CARSO with multiple AT backbone architectures on the same dataset (rather than one per dataset) would strengthen claims about generality.
- An analysis of the similarity of internal representations under classifier-only vs. end-to-end attacks would address the training-evaluation mismatch concern.

## Removed Points

- **"No purification comparison on CIFAR-100"** — Factually incorrect. Table 1 shows Best P/AA = 46.09% for CIFAR-100 (from Lin2024Robust), and the paper explicitly compares against this: "we still obtain a +20.25% increase in robust accuracy upon its (largely overestimated) AA result."
- **"Best P/AA column left empty for TinyImageNet-200"** — The paper openly states: "We are not aware of any published state-of-the-art adversarial purification-based model for TinyImageNet-200." This is an honest acknowledgement of a gap in the literature, not a weakness of the present work.
- **"The paper should add X" suggestions** that amount to scope creep (testing multiple backbones per dataset, covering additional domains) — The paper's scope is clearly defined and its claims are specific to the architectures evaluated.

## Novel Insights

The reviews collectively surface an interesting observation about the CARSO training paradigm. The purifier is trained on classifier-only attacks but evaluated against end-to-end attacks — and still performs well. This suggests that the internal representation of the adversarially-trained classifier may serve as a *sufficient statistic*: perturbations that differ in their outer objective (classifier-only vs. full-system) may produce similar internal representation perturbations because the classifier's forward pass compresses away information about the attack's downstream target. If true, this property could guide the design of more efficient purification training schemes that avoid expensive end-to-end adversarial generation. This is not claimed by the paper but is a natural hypothesis emerging from the training-evaluation gap.

## Suggestions

1. **Add a systematic ablation study (most critical).** Fix the base classifier and dataset (CIFAR-10) and ablate: (a) the aggregation strategy (vs. logit averaging and probability averaging), (b) the adversarial batch fraction (vary from 0.0 to 1.0), (c) the number of reconstruction samples N (e.g., {1, 4, 8, 16}), and (d) the use of hierarchical encoding vs. flat concatenation. Report both clean and robust accuracy.

2. **Discuss the training–evaluation mismatch explicitly.** Either provide analysis showing that internal representations under both attack regimes are similar, or justify why training on classifier-only attacks is sufficient. Even a small-scale experiment with end-to-end PGD training would strengthen the claim.

3. **Standardize evaluation comparisons.** When comparing against purification baselines, use the same evaluation protocol for both methods. The paper already reports CARSO's Pgd+EoT result — use this as the primary comparison number rather than randAA when comparing against baselines that only have Pgd+EoT results.

4. **Report variance estimates** (at least 3 runs on CIFAR-10) and inference cost in terms of wall-clock time or FLOPS.

## Score and Decision

The paper introduces a novel and conceptually clean approach with strong empirical results and a rigorous evaluation protocol. The main weakness — absence of ablation studies — is significant for a methods paper but does not invalidate the core contribution. The training-evaluation mismatch is a real concern but is partially mitigated by the strong empirical validation. With the addition of ablation studies and clarification of the evaluation comparisons, the paper would be a solid contribution.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>