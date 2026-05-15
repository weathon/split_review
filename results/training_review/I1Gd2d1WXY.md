Now I have a thorough understanding of the paper and all reviewer claims. Let me compile the final review.

## Summary

The paper introduces Adaptive Resolution Residual Networks (ARRNs), which substitute standard residuals with Laplacian residuals to enable a trained network to be "rediscretized" (adapted) to lower resolutions nearly instantaneously, without retraining. Two key components are proposed: (1) **Laplacian residuals** structured as a cascade where bandlimited inputs produce zero-valued difference signals, allowing early residuals to be skipped via a precomputed linear projection; and (2) **Laplacian dropout**, a training augmentation that randomly zeros consecutive difference signals to simulate lower-resolution inputs, improving robustness. Experiments on four image classification datasets (CIFAR-10/100, TinyImageNet, STL-10) show that ARRNs outperform standard CNN families (ResNet, WideResNet, MobileNet, EfficientNet) at lower resolutions while reducing inference time.

## Strengths

- **Novel and well-motivated architecture.** The combination of Laplacian pyramid decomposition with residual networks is a clever idea that is well-grounded in signal processing theory. The key insight — that under bandlimited inputs, difference signals become zero and inner blocks can be skipped — is clearly derived (Section 4.1, Equations 12–15). This provides a principled foundation rather than a purely heuristic approach.

- **Laplacian dropout is an effective and elegant augmentation.** Figure 5 convincingly shows that ARRNs trained with Laplacian dropout (red lines) drastically outperform those trained without it (black lines) across all four datasets at every lower resolution. This directly validates the core claim that the dropout mechanism improves low-resolution robustness. The conceptual link — randomly zeroing consecutive residuals simulates randomly lowering input resolution — is clean and well-explained.

- **Practical efficiency gains demonstrated.** Rediscretization reduces inference time at lower resolutions (Figure 6), and the adaptation cost is under 750 µs (Figure 7), making it viable for near-real-time applications. The paper formally proves that under ideal conditions, rediscretization is exact, and empirically shows that even with practical filter approximations, performance is maintained (with Laplacian dropout).

- **Compatibility with standard architectural blocks.** Unlike neural operators and implicit neural representations, ARRNs allow nesting standard layers (Conv, BN, ReLU, transformers) within residuals, requiring only the mild condition that the block output is constant for zero input (Equation 6). This significantly lowers the barrier to adoption.

- **Thorough multi-dataset comparison against diverse CNN families.** Experiments span four datasets and four strong convolutional architecture families (ResNet, WideResNet, MobileNetV3, EfficientNetV2) with varying parameter counts, providing comprehensive evidence of ARRNs' practical utility.

## Weaknesses

### Fatal

None.

### Major

None. The core claims are supported by a combination of theoretical derivation and empirical evidence. The weaknesses below are substantive but do not invalidate the paper's main contributions.

### Minor

1. **Lack of error bars / statistical rigor for accuracy results.** The paper's central quantitative claim — that "rediscretized ARRNs have identical or better performance than non-rediscretized ARRNs" (Section 5.2) and that ARRNs outperform baselines (Figure 5) — is presented without error bars, confidence intervals, or evidence of multiple training runs. Without variance estimates, the reader cannot assess whether observed differences are reproducible or within noise. (Note: timing measurements in Section 5.3 do use 10 repeats with median aggregation, which is good practice, but accuracy results lack this treatment.) This is the paper's most significant methodological gap.

2. **Model parameter counts are not matched across methods.** ARRNs range from 5M–20M parameters depending on resolution, while baselines span 1.5M (MobileNetV3) to 124M (WideResNetV2). Performance differences could be partially attributed to capacity rather than architectural advantages. A size-controlled comparison (e.g., matching ARRN and a baseline to similar parameter counts) would strengthen the evidence.

3. **Gap between ideal theory and practical implementation is acknowledged but not quantified.** The derivation in Section 4.1 assumes ideal (Whittaker-Shannon) filters and perfect bandlimitation. The implementation uses Kaiser-windowed approximations (6 zero-crossings, β=14.77), and the paper acknowledges that without Laplacian dropout, rediscretization degrades due to "bleed-through" from these approximations (Section 5.2). The claim that Laplacian dropout zeroes out this bleed-through is plausible but is never verified by measuring the spectral content of difference signals or quantifying the filter approximation error. Bridging this gap with even a simple spectral analysis would significantly strengthen the theoretical grounding.

4. **Laplacian dropout hyperparameter not reported.** The Bernoulli probability \( p_n \) for Laplacian dropout is a potentially impactful hyperparameter that is not stated. The paper specifies the chaining mechanism (Equation 20) but does not report what value(s) of \( p_n \) were used, how it was selected, or how sensitive results are to this choice.

5. **No comparison against any adaptive-resolution method.** The paper positions ARRNs relative to neural operators (Li et al., Kovachki et al.) and INRs (Park et al., Mildenhall et al.), arguing these methods impose "difficult design constraints" and are incompatible with standard layers. However, the experiments compare only against standard CNNs that are *not* designed for variable resolution. While the paper's contribution is about enabling adaptive resolution with standard layers — which makes the comparison against standard CNNs the more direct one — including at least one neural operator or INR baseline under a fair protocol would substantiate the claimed advantages over prior adaptive-resolution approaches. As it stands, the comparison is incomplete relative to the paper's positioning.

6. **Timing comparisons may be unfair due to implementation optimization asymmetry.** The paper notes ARRNs are "not highly optimized" (Figure 6 caption). Comparing inference time of unoptimized ARRNs against well-engineered baselines (EfficientNetV2) could be misleading. A FLOP-based comparison or a version of ARRNs with matched optimization effort would be more informative.

### Trivial

- The paper does not include an explicit limitations section. While many limitations are implicitly addressed (e.g., the bandlimitation requirement, reliance on approximations), a dedicated discussion would improve clarity.
- The condition \( b_n(0) = a \) (constant output for zero input) is derived as a theoretical requirement for exact rediscretization but is not explicitly verified for the blocks used in experiments. For Conv-BN-ReLU blocks with biases it clearly holds, but stating this explicitly would be helpful.

## Nice-to-Haves

- **Ablation on the \( b_n(0) = \text{constant} \) condition:** Testing a block that violates this condition (e.g., one without bias or with zero-centered normalization) and checking whether rediscretization degrades would validate the theoretical requirement.
- **Quantification of filter approximation error:** Showing the spectral response of the implemented Kaiser-windowed filters vs. ideal filters, and measuring the energy in difference signals for typical inputs, would directly justify the "bleed-through" explanation.
- **Visualization of difference signals \( r_n^\text{diff} \)** for low-resolution vs. high-resolution inputs to confirm that low-resolution inputs yield near-zero early difference signals.
- **Extension to other modalities** (audio, volumetric data) or tasks (segmentation, depth estimation) to demonstrate generality.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Harsh Critic's claim that "the protocol gives ARRNs a structural advantage" over standard CNNs.** This is not a weakness — ARRNs are *designed* to handle variable resolution natively. The fact that they have an advantage at their design goal is the point of the paper. The comparison against standard CNNs is fair because it tests the real-world scenario the paper addresses: given a standard CNN and an ARRN, which handles resolution shift better?

- **Harsh Critic's claim that "exact computation" in the abstract is misleading.** The paper consistently qualifies "exact" within the theoretical framework (ideal filters, bandlimited signals) and acknowledges practical approximations in the implementation. The abstract's phrasing is appropriate for describing the theoretical result.

- **Harsh Critic's demand that the paper justify "why ideal filters are preferred over standard Gaussian-based pyramids."** The paper states that ideal filters "act as binary masks in the frequency domain" (Section 3.1), which is a clear justification — ideal filters enable clean frequency-domain analysis, which is essential for the theoretical derivation.

- **Strength Finder's generic strengths that lack specific content.** Filtered to avoid inflating the assessment.

## Novel Insights

The most interesting observation emerging from reading the reviews against the paper is the tension between the paper's two central claims — *exact* rediscretization and *practical* performance — and how Laplacian dropout elegantly resolves it. The paper shows that the ideal-theory guarantee of exact rediscretization breaks down in practice due to filter approximation error (bleed-through), yet rather than treating this as a flaw, the authors leverage the same insight in reverse: Laplacian dropout, which zeros difference signals during training, simultaneously acts as both a data augmentation (simulating lower resolution) and a regularizer that cancels the approximation error at inference time. This duality — where the training augmentation and the inference-time approximation correction are the same mechanism — is a neat insight that deserves more emphasis than the paper gives it. The reviews that focus on the ideal vs. practical gap miss that Laplacian dropout is specifically designed to address this gap.

## Suggestions

1. **Report accuracy with error bars.** Run experiments multiple times (e.g., 5 independent seeds) and report mean ± std for all accuracy measurements in Figure 5. This is the single most impactful improvement.

2. **Add a size-controlled comparison.** Match an ARRN variant and a baseline (e.g., ResNet) to have a similar parameter count, and compare their performance at various resolutions.

3. **Report the Laplacian dropout probability \( p_n \)** and, if possible, include a brief sensitivity analysis.

4. **Add a simple spectral analysis** quantifying the filter approximation error (e.g., the difference between the ideal and Kaiser-windowed filter responses) to bridge the theory-practice gap.

5. **Consider adding one adaptive-resolution baseline** (e.g., an FNO adapted for classification) to directly substantiate the claimed advantages over prior adaptive-resolution methods, or alternatively clarify that the paper's comparison is against fixed-resolution methods (which is the natural baseline for the stated contribution).

## Score and Decision

The paper presents a novel, well-motivated, and theoretically grounded method with clear empirical support for its core claims. The weaknesses are substantive but not fatal — they concern presentation rigor and completeness rather than fundamental correctness. The paper makes a genuine contribution to adaptive-resolution deep learning.

**Score:** 7.0

**Decision:** Accept

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>