Now I have a thorough understanding of the paper and both reviews. Let me produce the final consolidated review.

## Summary

The paper proposes a non-uniform noise injection method for DNNs: a learning-based approximation module (random projection + low-precision learned mapping) identifies "essential" neurons per input, keeps their exact values, and replaces non-essential neurons with approximate values. The method aims to simultaneously improve adversarial robustness and computational efficiency. Experiments across CIFAR-10 and ImageNet with five attack types show consistent robust accuracy improvements (up to ~12.88%) compared to the original model, and the method is shown to combine orthogonally with adversarial training.

## Strengths

- **Consistent robustness improvements across diverse settings**: The method (particularly structured 4:8) improves robust accuracy by 10.49% (BIM, CIFAR-10 ResNet18), 6.61% (DeepFool, CIFAR-10 ResNet50), 10.81–12.30% (ImageNet ResNet18), and 8.63–12.88% (ImageNet ResNet50) against the original model, across five attack types, two architectures, and two datasets (Tables 1–2).

- **Orthogonality with adversarial training**: Table 3 shows that combining structured 4:8 with FGSM-RS and PGD-10 improves robust accuracy by 2.08–3.19% over adversarial training alone, with only 0.46–1.86% clean accuracy drop — demonstrating the method's value as an add-on defense.

- **Clean accuracy is preserved with theoretical backing**: Section 3.3 provides a Johnson-Lindenstrauss-based argument (Theorem 1) showing that inner products can be preserved in the low-dimensional space used for essential neuron selection. Empirically, clean accuracy drops are negligible across all experiments (e.g., 94.32% vs 94.72% for CIFAR-10 ResNet18 with 4:8).

- **Clean accuracy retention is empirically validated**: Across all settings, clean accuracy losses are minor (typically <1–2%), supporting the claim that essential neurons are identified correctly.

## Weaknesses

### Fatal
None.

### Major

- **The theoretical justification for robustness (Section 3.4) is mismatched with the actual method.** Theorem 2 from Pinot et al. (2019) is invoked to argue for robustness improvement, but that theorem concerns *probabilistic* mappings M: 𝒳 → P(𝒵) that output a distribution over predictions. The proposed method (Eq. 1: *z' = z ⊙ m + z̃ ⊙ (1-m)*) is entirely deterministic: the mask *m* and approximate values *z̃* are fixed functions of the input, learned via MSE minimization. The paper does not argue that this deterministic perturbation can be modeled as sampling from a distribution, nor does it provide an alternative theoretical foundation. The cited theorem is therefore inapplicable as formal support. This is a significant gap: the paper's central explanation for *why* the method improves robustness is disconnected from what the method actually does. The empirical results may still stand, but the theoretical framing is misleading.

- **The efficiency analysis (Section 4.3) is too preliminary to support the claimed efficiency benefits.** The method requires computing approximate outputs *z̃* for *all* neurons (via random projection + low-precision matmul) *before* the mask can be generated and precise computations skipped. The paper asserts that the projection overhead is "negligible" (line 100) but provides no quantitative analysis of its actual latency, energy, or FLOPs relative to the full-precision compute it replaces. The hardware analysis in Figure 4 uses normalized metrics and BitOps, but does not compare against a baseline running the full-precision network end-to-end, nor does it isolate the overhead of the approximation + selection mechanism. Without this, it is unclear whether the approximation module costs as much as it saves — or more. The paper's own contribution statement calls this "preliminary" (line 18), which is honest, but the paper still claims efficiency as a core advantage.

### Minor

- **No adaptive attack evaluation.** The defense is deterministic (gradients flow through both the mask and the approximate computation), so an adaptive attacker could craft adversarial examples that exploit the mask selection. The paper evaluates only against standard (non-adaptive) attacks (FGSM, BIM, PGD, DeepFool, C&W). Without an adaptive attack analysis, the robustness numbers may overstate the method's security.

- **The "non-uniform > uniform" claim would benefit from a stronger uniform-noise baseline.** The paper compares Irregular (50%, 80%, 90%) patterns — which apply noise to varying *percentages* of neurons — against Structured (2:4, 4:8) patterns. This is a comparison of coverage rates, not a direct comparison of non-uniform vs. truly uniform noise (e.g., adding the same noise distribution to 100% of neurons). While the Irregular 80%/90% results (minor robustness losses) *support* the claim, including a baseline that perturbs all neurons with a simple noise distribution (e.g., layerwise Gaussian noise of controlled variance) would make the central claim more directly testable.

- **No ablation studies on key design choices.** The paper does not report sensitivity to: the reduced dimension *k* in the random projection, the quantization bit-width of approximation parameters (stated as INT4), the sparsity of the random projection matrix, or how the top-K threshold is selected per layer. These choices likely affect both robustness and efficiency but are not explored.

- **Standard deviations and multiple runs are not reported.** Given the variance inherent in adversarial evaluation (especially with PGD and C&W attacks), reporting single-run results weakens confidence in the numerical comparisons.

- **The JLL argument (Section 3.3) preserves inner products but does not directly guarantee ordering preservation.** The paper uses approximate inner products to *rank* neurons and select the top-K as essential. Preserving individual inner products up to ε does not guarantee that the ranking of a large set of similarly-valued neurons is preserved. The empirical clean accuracy results suggest this is not a problem in practice, but the theoretical argument as presented does not fully close this gap.

### Trivial
None.

## Nice-to-Haves

- Including an ablation comparing the learned approximation against simpler importance metrics (e.g., using the full-precision activations as an oracle for essential neuron selection) would strengthen the argument that the approximate selection is faithful.
- Reporting absolute latency/energy numbers (ms, µJ) alongside normalized metrics in the hardware analysis would make the efficiency claims more concrete.
- Evaluating against AutoAttack (Croce & Hein, 2020) as a more rigorous robustness benchmark.

## Removed Points

These points from the reviews are flagged to be removed; treat them with caution:

- **"No comparison against any uniform noise injection baseline"** (Harsh Critic, Critical Issue #2): This is factually inaccurate. The paper's Tables 1–2 compare against Irregular 50%, 80%, 90% patterns, which are noise injection methods applied at different coverage rates. These serve as baselines closer to uniform injection. The softened version of this concern is retained in Minor weaknesses above.
- **"Figure 1 x-axis label missing"**: Parser artifact — the figure is an embedded image that lost its axis labels during extraction.
- **"Learning procedure underspecified" (Section 3.1)**: The paper does specify the MSE loss (line 61) and that parameters are trained to minimize it. While some hyperparameters (training data source, threshold selection) are not exhaustively detailed, this is typical for a conference submission and not a core flaw.
- **"Missing related works" / overclaimed contribution**: Per hard rules, missing related works criticisms are removed. The "first to identify" claim is a contribution statement, not a weakness.
- **"No AutoAttack" as a standalone criticism**: This is a nice-to-have, not a weakness — many robustness papers still use the attacks evaluated here.
- **Strengths from Strength Finder that are generic or conflict with verified weaknesses**: The Strength Finder's claim that "Non-uniform injection outperforms uniform injection: Tables 1 and 2 show... uniform patterns (Irregular 80%, 90%) cause minor robustness losses" uses imprecise terminology (Irregular ≠ uniform noise injection) and overstates the evidence. The core empirical finding (robustness improvements over original model) is kept as a genuine strength above.

## Novel Insights

The most interesting observation arising from the reviews is the tension between the paper's deterministic mechanism (learned approximation + top-K masking) and its probabilistic theoretical framing. If the learned approximation produces values that are *functionally* noisy (i.e., the approximation errors are well-characterized and input-dependent), the method could potentially be reframed as a learned, input-dependent noise distribution rather than a deterministic mask. The reviews collectively suggest that the paper would be stronger if it leaned into the *empirical* contributions (which are solid) and either dropped or rewritten the theoretical section (Section 3.4) to match the actual mechanism — possibly connecting to Lipschitz regularization or the smoothing effects of low-precision approximations rather than probabilistic noise injection theorems.

## Suggestions

1. **Restructure or remove Section 3.4.** Either drop the Pinot et al. theorem entirely and present the robustness improvement as an empirical finding, or provide a rigorous argument for why the deterministic approximation+masking procedure satisfies the premises of a probabilistic robustness bound.
2. **Add a direct uniform-noise baseline.** Compare against a method that adds a simple noise distribution (e.g., Gaussian with matched variance) to *all* neurons at each layer. This directly tests the paper's central claim that non-uniformity is the source of improvement.
3. **Quantify the overhead of the approximation module.** Report wall-clock latency, FLOPs, and/or energy for the approximation+selection+masking pipeline vs. the full-precision forward pass, on actual hardware or a cycle-accurate simulator.
4. **Evaluate against an adaptive attack.** Since gradients flow through the mask (via the straight-through or differentiable approximation), craft PGD or C&W attacks that are aware of the defense mechanism.
5. **Report standard deviations** across multiple random seeds/runs, and include ablation studies on the reduced dimension *k*, projection sparsity, and top-K threshold selection.

## Score and Decision

On the evaluation axes:
- **Originality**: Moderate — non-uniform, data-dependent noise injection is a novel angle on noise-based defenses.
- **Importance of research question**: High — adversarial robustness and computational efficiency are both practically important.
- **Claims well-supported**: Partially — robustness claims are supported by experiments; theoretical justification and efficiency claims are not.
- **Soundness of experiments**: Moderate — reasonable scope (5 attacks, 2 datasets, 2 architectures) but missing adaptive attacks, standard deviations, and key ablations.
- **Clarity of writing**: Adequate — the method description is understandable but the theoretical section is misleading.
- **Value to the community**: Moderate — interesting direction that would benefit from a more rigorous evaluation.

The paper identifies a worthwhile direction and provides consistent empirical evidence for robustness improvement. However, the theoretical justification is mismatched with the method, the efficiency analysis is too preliminary to support the claimed efficiency benefits, and several important baselines and controls are missing. These issues are addressable in a revision, but in its current form the paper does not convincingly establish that non-uniform noise injection is a meaningful advance over existing approaches.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>