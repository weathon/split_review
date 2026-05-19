- Decision: Reject
- Avg Score: 3.00
- Scores: 3, 3, 3, 3
Now I have a thorough understanding of the paper. Let me verify the calibration directory exists but note that I have sufficient information.

Let me produce the final consolidated review.

## Summary

UCAN proposes a universal theoretical framework (Theorem 3.2) that transforms any existing randomized smoothing certification with isotropic noise into certification with anisotropic noise, covering multiple noise distributions and ℓₚ perturbations. It also designs three Noise Parameter Generators (pattern-fixed, universal, input-dependent) that learn per-dimension mean and variance parameters. Experiments on MNIST, CIFAR10, and ImageNet report substantial certified accuracy improvements over SOTA methods.

## Strengths

- **Universal theoretical transformation for anisotropic randomized smoothing** — Theorem 3.2 provides a general method to convert any isotropic-noise certification into anisotropic-noise certification without requiring Lipschitz assumptions on the base classifier. Table 1 derives explicit certified-radius formulas for Gaussian, Laplace, and Uniform noise against ℓ₁, ℓ₂, and ℓ∞ perturbations. This goes beyond Eiras et al. (2022), which was restricted to Lipschitz networks.

- **Three practically motivated Noise Parameter Generators (NPGs)** — The paper designs pattern-fixed (heuristic spatial variance map, Section 4.1), universal (fixed-input MLP, Section 4.2), and input-dependent (dense-block architecture, Section 4.3) NPGs, each with custom loss functions balancing variance maximization and classification accuracy. This provides a practical framework for learning anisotropic noise parameters beyond grid-search or heuristic approaches.

- **Strong empirical gains across multiple datasets** — Tables 2–4 report certified accuracy improvements of up to 142.5% on MNIST, 182.6% on CIFAR10, and 121.1% on ImageNet over best baselines. Even in the controlled pattern-fixed setting (same ALM as isotropic baseline), the paper shows strict improvements on all datasets (Figure 4a–c). The input-dependent NPG achieves the best results, with up to 54% improvement in certified accuracy.

- **Demonstrated universality across noise distributions and ℓₚ perturbations** — Figure 5 shows that UCAN amplifies certification for Laplace noise against ℓ₁, Gaussian against ℓ₂, and Uniform noise against ℓ∞ perturbations on CIFAR10, confirming that the framework applies broadly.

- **Introduction of ALM for fair anisotropic evaluation** — The Alternative Lebesgue Measure (Section 3.2) provides a principled metric for comparing anisotropic and isotropic methods, accounting for the asymmetric certified region.

## Weaknesses

### Fatal
None.

### Major

- **Baseline comparison fairness is not fully established** — The paper reports dramatic improvements (up to 182.6%) over SOTA methods in Tables 2–4, but the text only states that UCAN "follows the same settings" as prior work (line 209). It does not clarify whether the baseline numbers were obtained by re-training those methods in an identical pipeline (same architecture, same training budget, same augmentation) or taken from published tables. Given the magnitude of reported gains, this conflation of implementation differences with the effect of anisotropic noise is a significant concern. Figure 4 provides a cleaner controlled comparison (same ALM level) and shows more modest improvements (up to ~54%), which is more credible. The headline SOTA comparison in Tables 2–4 needs explicit clarification or controlled re-implementation. This is the most impactful weakness because it directly affects whether the paper's central empirical claim is supported at the claimed magnitudes.

- **No derivation or intuition for the core theorem in the main text** — Theorem 3.2 is the paper's foundational contribution, but the main text contains only the word "Proof." (line 76) with no sketch of the change-of-variables argument, no statement of required conditions (e.g., separability of the noise PDF under independent scaling), and no explanation of why the isotropic certified-radius function R(·) transfers directly to the anisotropic case. The reader cannot assess the theory's soundness without consulting the appendix (which is standard practice, but the main text should provide at least a paragraph of intuition). This weakens the paper as a self-contained theoretical contribution.

### Minor

- **No ablation of mean offset μ** — The paper claims μ can improve p_A' and p_B' (line 80), yet all pattern-fixed experiments fix μ=0 (line 133), and the universal/input-dependent NPGs learn μ jointly with σ (lines 141, 162–163). Without comparing the full method against a version with μ=0 for the same NPG architecture, the separate contributions of variance scaling (σ) and mean shifting (μ) cannot be disentangled. The paper notes that μ's benefit must come from shifting the decision boundary (which is a legitimate effect), but this should be ablated explicitly.

- **No error bars or statistical significance measures** — Certified accuracy is reported as point estimates without any indication of variance. Given the Monte Carlo certification procedure (n₀=100, n=100,000) and training stochasticity (especially for the NPGs), reporting results across multiple seeds is important for assessing the reliability of the claimed improvements. (Note: I acknowledge that single-run evaluation is common in this subfield, but the training of the NPG introduces additional randomness beyond standard randomized smoothing, making this more consequential.)

- **NPG architecture and training details underspecified** — The universal NPG uses "5 linear layers" (line 143) without hidden dimensions. The input-dependent NPG uses "dense blocks" (line 164) without specifying block count, growth rate, or depth. The relative weight between variance loss and smoothing loss in Equation 5 is not given. These details are needed for reproducibility.

- **Sensitivity to hyperparameters not explored** — Only one setting is examined for the pattern-fixed method (κ=1, ι=1, line 132). The sensitivity of results to κ, ι, and the amplification factor γ (reported on line 185 as tuned per dataset) is not discussed.

### Trivial

- The notation ε^T σ in line 63 is ambiguous — the paper defines σ as a diagonal matrix (line 60), so this is elementwise multiplication, but using ε⊙σ (Hadamard product) or diag(σ)ε would be clearer.

## Nice-to-Haves

- A controlled experiment where the isotropic baseline is re-trained under the same pipeline (same architecture, data augmentation, training budget) as UCAN would cleanly isolate the effect of anisotropic noise.
- Ablating learned σ vs. random σ (e.g., random permutations or random sampling at the same geometric mean) would show whether the NPG discovers genuinely beneficial structure.
- Reporting computational overhead (wall-time or FLOPs) for training the NPGs and for inference-time certification would help readers assess practicality.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- "Missing appendix / proof not in main text, so theory cannot be verified" — The appendix is stripped by the parser for all papers; the proof exists in the original submission. However, the *related* point about the main text lacking intuition/derivation is retained as a Major weakness above.
- "Certification procedure not confirmed (same α, n₀, n)" — The paper explicitly states α=0.001, n₀=100, n=100,000 (line 179) and says it follows Cohen et al. (2019). This concern is addressed.
- "Variance loss could lead to degenerate solutions" — Speculative; no evidence of degenerate solutions is presented in the paper.
- "Universal NPG is over-parameterized; simpler baseline would be better" — This is a suggestion for a different approach, not a weakness of the presented method.
- "ALM-based numbers not shown in main tables" — The paper shows ALM curves in Figure 4 and discusses ALM throughout; the ℓ₂ radius tables are one of two metrics presented.
- "Related work missing" — Per instructions, this is not verifiable and should not be included.
- "Formatting/style nitpicks" — Per instructions, parser artifacts are not author errors.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a novel perspective that reinterprets the paper's contributions or limitations beyond what the authors discuss.

## Suggestions

1. Clarify in the experimental section whether the SOTA baseline numbers in Tables 2–4 are re-implemented under identical conditions or taken from published tables. If the latter, provide a controlled re-implementation comparison (even for a subset of baselines) to confirm the magnitude of gains.
2. Add a paragraph in Section 3.2 sketching the change-of-variables intuition behind Theorem 3.2 — even a few sentences explaining why the isotropic R(·) transfers when perturbations are weighted by σ_i^{-1} would greatly help readers.
3. Add an ablation comparing the input-dependent NPG with μ fixed to zero vs. learned μ, on at least one dataset, to separate the effect of anisotropic variance from mean shifting.
4. Report certified accuracy over at least 3 random seeds for the main experiments, or provide a justification for single-run reporting.
5. Specify hidden dimensions for the universal NPG and block architecture details for the input-dependent NPG in the main text or appendix.
