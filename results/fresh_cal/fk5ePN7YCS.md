I now have a thorough understanding of the paper and all reviewer claims. Let me produce the final consolidated review.

---

## Summary

This paper proposes NEPENTHE, an entropy-guided unstructured pruning method that aims to reduce the depth of over-parametrized neural networks. The key idea is to iteratively redistribute the pruning budget toward layers with already-low neuron entropy, driving those layers to zero entropy (all neurons always ON or always OFF), at which point the layer's activation becomes redundant and the layer can be removed. The authors provide a theoretical derivation showing that unstructured pruning naturally reduces neuron entropy under Gaussian assumptions, design an entropy-weighted pruning budget allocation, and validate the method on ResNet-18, MobileNet-V2, and Swin-T across several datasets. The central empirical finding is that NEPENTHE drives entire layers to zero entropy while maintaining accuracy, whereas standard iterative magnitude pruning (IMP) does not.

## Strengths

- **Theoretical grounding that unstructured pruning reduces neuron entropy.** Section 3.2 provides a closed-form derivation (Eqs. 3.2–3.4, Fig. 3c) showing that under Gaussian assumptions on inputs and weights, increasing the magnitude-pruning threshold monotonically decreases the entropy of a rectifier-activated neuron's output. This gives a principled reason to expect that unstructured pruning can drive layer entropy toward zero.

- **Clean ablation study validating each design component.** Table III (ResNet-18/CIFAR-10) shows that adding the entropy-weighted budget allocation alone enables 3/17 layer removal with accuracy rising from 91.66% to 92.18%; adding the "don't care" state handling and the non-zero entropy neuron filtering progressively improves accuracy to 92.55% while maintaining 3/17 layers removed. Each component contributes positively.

- **Robustness across multiple rectifier activations.** Table IV tests five different activations (ReLU, SiLU, PReLU, LeakyReLU, GELU) on ResNet-18/CIFAR-10. In every case, NEPENTHE removes exactly 3/17 layers and achieves top-1 accuracy at or above the dense baseline (e.g., 92.55% for ReLU, 92.77% for SiLU, 92.57% for GELU), showing the method is not tied to a specific non-linearity.

- **Clear empirical demonstration that NEPENTHE drives layers to zero entropy where IMP does not.** Table I shows that after several pruning iterations with NEPENTHE, the bottom three layers reach exactly zero entropy (and layers 4–5 are near-zero), while IMP at best reduces Layer 1 to 0.055 but never to zero, with all other layers remaining at moderate-to-high entropy.

## Weaknesses

### Fatal
None.

### Major

- **The central claim of depth reduction is not fully validated: the paper demonstrates that layers *can* be removed (zero entropy) but does not actually remove them or measure the computational benefit.** The algorithm (Alg. 1) ends with a pruned weight vector; there is no step for physically folding/removing zero-entropy layers. The paper reports "Rem." (removed layers) based on the entropy condition alone, but does not confirm that the architecture is modified or that this translates into measurable savings (FLOP reduction, parameter reduction, or wall-clock latency). The motivation for depth reduction is explicitly tied to reducing the critical path for GPU/TPU computation (Introduction, Conclusion), yet no efficiency metric is reported. This is the most significant gap: the evaluation measures the proxy (entropy) rather than the quantity the paper ultimately cares about (depth reduction with computational payoff). The paper would be substantially strengthened by actually folding zero-entropy layers (replacing identity activations, removing always-zero neurons) and reporting the resulting FLOPs or inference speed, even on CPU.

### Minor

- **Missing comparison with one cited depth-reduction baseline (Ali-Mehmeti-Gopel 2023).** The paper cites Ali-Mehmeti-Gopel 2023 (a channel-wise approach to removing non-linear units) in the related work but does not include it as a baseline. The comparison against Layer Folding (Dror et al. 2021) is present and favorable, but adding this additional depth-reduction method would strengthen the experimental evaluation.

- **No statistical significance reported.** Results are presented from single runs without standard deviations. For a pruning method that involves iterative retraining, multiple seeds would improve confidence in the results.

- **Key hyperparameters are not justified or ablated.** The pruning ratio ζ is set to different values per architecture (0.5 for ResNet-18, 0.25 for Swin-T, 0.1 for MobileNet-V2) without explanation of how these were chosen. The stopping threshold θ is not specified. An ablation of these parameters would help readers understand sensitivity and transferability.

### Trivial
None.

## Nice-to-Haves
- Reporting FLOPs or parameter counts for the architecture *after* hypothetical layer folding would give a quantitative efficiency metric even without hardware benchmarks.
- A larger-scale experiment on ImageNet with a suitable over-parametrized architecture (e.g., ResNet-50) would extend the scope; the paper acknowledges this limitation and notes an underfitting failure case in the supplementary material, which is honest but limits impact.

## Removed Points

- **"No comparison with core depth-reduction baselines"** (Harsh Critic) — Partially inaccurate. The paper *does* compare against Layer Folding (Dror et al. 2021), which is one of the two cited depth-reduction methods. The only missing baseline is Ali-Mehmeti-Gopel 2023, which I have noted as a Minor weakness above. The broader claim that "no core depth-reduction baselines" were compared is too strong and has been removed.

- **"Larger-scale experiment on ImageNet"** (Harsh Critic) — The paper acknowledges this limitation explicitly ("unable to reduce the depth of an already under-fitting architecture like ResNet-18 trained on ImageNet"). Criticizing a paper for not solving a problem it acknowledges as a limitation is not fair. Moved to Nice-to-Haves.

- **"The paper never demonstrates that the architecture is actually modified" overstated as fatal** — I have kept this as a Major weakness (the central gap) but removed the framing that it invalidates the paper entirely. The method's core contribution is the entropy-guided pruning strategy that drives layers to zero entropy, which is demonstrated. The missing step is closing the loop to actual computational benefit, which is a significant but not fatal omission.

- **Strength Finder's claim of "Demonstrated layer removal with no accuracy loss"** — Modified to note that what is demonstrated is zero-entropy (potential for removal). The distinction matters and is reflected in the Major weakness above.

- **Generic strengths** (Strength Finder's "Core strengths" framing about the paper addressing an important problem and making a well-motivated contribution) — These are already captured by the more specific strengths listed above.

## Novel Insights

The harsh critic and strength finder converge on a key observation that neither fully articulates: the paper's strongest empirical evidence is the *comparative entropy trajectory* in Table I. What makes NEPENTHE's result non-obvious is not just that it drives some layers to zero entropy — IMP also reduces entropy — but that NEPENTHE's budget reallocation *concentrates* the entropy reduction in a few layers while preserving entropy in others, creating a clean separation that enables selective layer removal. This "entropy polarization" effect (some layers at exactly zero, others at near-maximum) is the real mechanism behind the method's success and is more interesting than the pruning strategy itself. The paper's theoretical derivation (Sec. 3.2) explains why pruning reduces entropy in general, but does not explain why the reweighted budget produces polarization rather than uniform reduction. This polarization phenomenon is an empirically robust finding (it holds across architectures and activations) that deserves deeper theoretical analysis.

## Suggestions

1. **Close the loop on depth reduction:** After pruning with NEPENTHE, physically fold the zero-entropy layers (replace identity-activation layers with their linear equivalent and merge with the next layer; remove always-zero neurons). Then report FLOPs, parameter count, and/or wall-clock time for the folded architecture vs. the dense model. This single addition would address the paper's largest weakness.

2. **Add the missing depth-reduction baseline (Ali-Mehmeti-Gopel 2023)** to the experimental comparison, or at minimum explain why it is not comparable (e.g., different architectural assumptions).

3. **Report results over 3–5 random seeds** with standard deviations for the main experiments (especially Table II / the main results table).

4. **Ablate or justify the ζ and θ hyperparameters.** Show a sensitivity analysis for ζ on at least one architecture-dataset pair, or explain the heuristic used to set different values per architecture.

5. **Compute FLOP reduction** from the zero-entropy-layer configuration even if you do not physically modify the model. This is a simple arithmetic calculation and would provide a quantitative efficiency metric that is currently missing.

## Score and Decision

**Originality:** Moderate. Entropy-guided pruning has been explored before, but applying it specifically to drive whole-layer entropy to zero for depth reduction via unstructured pruning is novel.

**Importance of research question:** Good. Reducing depth (vs. width) addresses a genuine gap in the pruning literature and has practical implications for parallel computation.

**Claims supported:** Partially. The claim that NEPENTHE drives layers to zero entropy is well-supported. The claim of "depth reduction" / "layer removal" is supported only by the entropy proxy, not by actual architecture modification or computational measurement.

**Soundness of experiments:** Adequate but incomplete. The ablation study and activation analysis are clean. The main gap is the missing computational-efficiency evaluation and one missing baseline.

**Clarity of writing:** Good. The paper is well-structured and the method is clearly explained.

**Value to the community:** Moderate. The insight that unstructured pruning can be steered to produce zero-entropy layers is useful, but the impact would be higher with a complete evaluation.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Reject</decision>