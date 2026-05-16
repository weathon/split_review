Now I have a thorough understanding of the paper and have verified all claims against the text. Let me construct the final consolidated review.

---

## Summary

This paper introduces LayerAct, a novel activation mechanism for CNNs with BatchNorm where the activation scale function (e.g., sigmoid) uses layer-normalized input while the main path uses raw input. This design aims to: (i) bypass the trade-off between one-side saturation and zero-like mean activation, and (ii) reduce the variance of noise-robustness across samples. Experiments on CIFAR-10/100-C and ImageNet-C show that ResNets with LayerAct functions (LA-SiLU, LA-HardSiLU) outperform element-level activation baselines on noisy datasets, with statistical significance in 30/36 experiments.

## Strengths

- **Novel and well-motivated activation mechanism**: The idea of using layer-normalized input *only* for the scale function (sigmoid/HardSigmoid) while keeping the main input path untouched is genuinely novel. This cleanly sidesteps the homogenization problem of LayerNorm (Section 3.3, lines 152, 184–188) while still providing layer-level normalization benefits. The design is principled and grounded in a clear analysis of what the trade-off problem is.

- **Strong empirical results on noisy benchmarks with rigorous statistics**: On CIFAR-10-C, CIFAR-100-C, and ImageNet-C, LayerAct functions consistently outperform element-level baselines (ReLU, LReLU, PReLU, Mish, SiLU, HardSiLU). The paper reports statistical significance via T-tests/Wilcoxon signed-rank tests (p < 0.05 in 30/36 experiments, line 235) and 30-run averages for CIFAR experiments — a level of rigor uncommon in activation function papers.

- **Empirical verification of zero-like mean activation**: Figure 2 (Section 4.1) provides a clear demonstration that LayerAct functions maintain near-zero mean activation across training epochs on MNIST, while element-level functions with one-side saturation drift far from zero. This directly supports the claim that the method addresses the trade-off problem.

- **Compatibility analysis with BatchNorm is explicit and informative**: Section 3.3 explains why batch-direction normalization (BatchNorm) is the natural partner for LayerAct and why LayerNorm would undermine its benefits. This alignment grounds the method in the de facto standard for CNNs, increasing practical relevance.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **The claim of reduced *variance* of noise-robustness across samples is not directly measured in the deep network experiments.** The paper argues (line 10, line 86) that LayerAct reduces variance of noise-robustness across samples by lowering the upper bound of activation fluctuation. The MNIST experiment (Section 4.1.2, Figure 3) provides direct evidence for reduced mean *and* variance of activation fluctuation in a single-layer network. However, the main classification experiments (CIFAR-C, ImageNet-C) report only *mean* accuracy across corruptions — they do not report per-sample robustness variance or the distribution of robustness across samples. Showing that mean accuracy improves on corrupted data is consistent with the claim but does not directly verify that variance *across samples* is reduced in deep networks. The conclusion (line 279) hedges appropriately ("implying that networks...have potential to"), but the introduction and motivation frame variance reduction as a central advantage. Measuring per-sample accuracy variance on a noisy test set would strengthen this claim.

- **The theoretical bounds (Section 3.2) are heuristic and rest on explicit assumptions that are not fully characterized.** The derivation assumes σ_ε ≪ σ_y (line 156) and approximates away second-order effects from changes in σ_y. The claim ‖s(ˆn)‖ ≪ d (Equation 9) is reasonable for approximately standard-normal inputs (sigmoid averages ≈0.5, so ≈0.5d) but is stated without quantification of "≪." The bound's dependence on σ_y means it could be larger than the element-level bound if σ_y is small — the paper acknowledges that inputs should not be "excessively large" (line 14, line 180) but does not characterize when σ_y is safely large or the conditions under which the bound is tighter. These are standard limitations for a heuristic analysis in a conference paper and do not undermine the empirical results, but the theoretical framing could be more precise.

- **Training hyperparameters are not fully specified.** The paper states network architectures and the use of BatchNorm (lines 195–196, 226) but does not report learning rates, schedules, weight decay, or data augmentation policies. While these are standard for ResNet+CIFAR/ImageNet, and the paper reports 30-run averages (suggesting robustness to hyperparameter choice), the absence makes exact reproduction harder. The paper also does not clarify whether hyperparameters were tuned per activation function or held fixed — if fixed, some baselines may be disadvantaged.

- **The trade-off motivation (Section 2.2) could be more precise.** The paper acknowledges modern functions (ELU, SiLU, FReLU) and states the trade-off persists because "the restriction of negative outputs, designed to ensure saturation, prevents the allowance of large negative outputs" (line 63). This is a defensible position, but the paper does not provide quantitative evidence (e.g., mean activation values across layers) comparing SiLU to LayerAct on the same network. The conceptual argument is clear but would benefit from empirical backing.

### Trivial

- The norms in Equations 8–9 (line 177) are implicitly L1 norms (sum of absolute values) from the derivation context but are written as ‖·‖ without subscript, creating minor notational ambiguity.

## Nice-to-Haves

- **Per-sample variance analysis on CIFAR-C/ImageNet-C**: Reporting standard deviation or quantiles of per-sample accuracy under corruption would directly support the variance-reduction narrative.
- **Ablation using raw y_i instead of normalized n_i** in the scale function: This would isolate the effect of using layer-normalized input from other design choices.
- **Brief runtime comparison**: LayerAct requires computing μ_y and σ_y per layer; a wall-time comparison would address a natural practical concern.
- **Discussion of limitations**: The paper does not discuss edge cases like layers with very low channel count (where μ_y and σ_y are noisy) or networks without BatchNorm.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *Harsh Critic claim that "saturation in these functions does not allow negative outputs is false for SiLU/ELU."* — The paper's sentence (line 61) specifies "such as ReLU," clearly scoping to ReLU-like functions. The very next sentence (line 63) separately discusses ELU, SiLU, FReLU and acknowledges they allow negative outputs. This is a misreading by the reviewer.

- *Harsh Critic claim that the trade-off argument is "circular" and "not supported by quantitative evidence."* — The paper's argument (line 63) is straightforward: if you restrict negative outputs to achieve saturation, you cannot achieve fully zero-like mean. This is a coherent conceptual claim, and the paper later provides empirical evidence (Figure 2, Section 4.1) that LayerAct achieves more zero-like mean than element-level functions. The quantitative comparison is provided via the MNIST experiment.

- *Harsh Critic claim about "missing confidence intervals for ImageNet" framed as structural omission.* — ImageNet experiments use standard practices (single-run evaluation with 10-crop testing is the norm). The paper's 30-run evaluation on CIFAR is already above standard rigor.

- *Harsh Critic note that tables are "not present in the extracted text."* — This is a parser artifact from PDF extraction; the tables exist in the original submission as images.

## Novel Insights

The reviews surface an important subtlety: the paper's theoretical analysis would be substantially stronger if it replaced the vague ‖s(ˆn)‖ ≪ d with an explicit expected-value calculation under the assumption that normalized inputs are approximately standard normal (justified by BatchNorm). This would give a concrete bound like 𝔼[‖s(ˆn)‖] ≈ 0.5d, making the comparison with the element-level bound of d precise. Additionally, the reviews highlight that the variance-reduction claim, while intuitively plausible and partially supported by the single-layer MNIST experiment, requires explicit validation in deep networks — this is a methodological insight that could improve not just this paper but similar papers claiming robustness improvements through architectural changes.

## Suggestions

1. **Directly measure variance of noise-robustness** in the CIFAR-C/ImageNet-C experiments: report per-sample accuracy variance or standard deviation across corruptions/severities to directly support the variance-reduction claim.
2. **Tighten the theoretical analysis** by replacing ≪ d with an explicit expected bound under the standard-normal assumption for normalized inputs, and clearly state the conditions (σ_y range) under which the LayerAct bound is strictly tighter.
3. **Report training hyperparameters** (learning rate schedule, weight decay, augmentation) and clarify whether they were tuned per activation function or held fixed.
4. **Add a brief computational cost comparison** (forward-pass time per batch) to address the natural overhead concern.

## Score and Decision

The paper proposes a genuinely novel activation mechanism with a clear conceptual motivation and strong empirical results on multiple benchmarks, including rigorous statistical testing. The weaknesses — a gap between the variance-reduction claim and its direct measurement in deep networks, heuristic theoretical bounds, and minor presentation issues — are all addressable in a revision and do not undermine the core contribution. This is a solid, above-threshold paper that should be accepted.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>