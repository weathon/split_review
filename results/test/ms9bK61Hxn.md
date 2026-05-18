Now I have everything I need. Let me write the final consolidated review.

## Summary

This paper proposes Similarity Group Equivariant Convolutional Networks (SECNNs), which achieve continuous translation, rotation, and scale equivariance by extending the Analytical Fourier-Mellin Transform basis to be steerable and approximately shiftable and scalable. The authors construct 5D convolution kernels within a position-orientation-scale-reflection space and implement practical deep networks through computational optimizations (cropped Fourier series, spatial-domain nonlinearities). Experiments show strong results on translated/rotated/scaled MNIST variants and competitive performance on CIFAR10/100.

## Strengths

1. **Principled theoretical framework for full similarity group equivariance.** The paper derives 5D steerable, approximately shiftable and scalable basis functions from the AFMT, providing a formal foundation for achieving continuous translation, rotation, scaling, and reflection equivariance simultaneously — a broader equivariance than most prior methods (Section 3.1, Table 1). This directly addresses the gap identified in the paper where "most methods... do not guarantee continuous translation equivariance."

2. **Strong empirical results on challenging MNIST variants combining all three transformations.** SECNN-Mix achieves the lowest error rates on several translated-rotated-scaled MNIST datasets (e.g., 5.46% on TRS, compared to 12.68% for E2CNN and 7.92% for Sim2CNN; Table 2), demonstrating clear improvements on tasks requiring combined transformation robustness.

3. **Competitive CIFAR10/100 accuracy while providing the broadest equivariance among compared methods.** SECNNs achieve 3.77% error on CIFAR10 (best among compared methods) and rank third on CIFAR100, while being equivariant to the full similarity group — a wider transformation range than any baseline in the comparison (Table 3).

4. **Practical implementation strategies that make 5D convolutions tractable.** Cropping the Fourier series to 5×5 kernels after computing with large frequencies (Section 3.1.1), precomputing the basis, and using spatial-domain real-valued ReLU/BatchNorm (Section 4) are concrete design choices that enable training on standard hardware (36 GB for MNIST, 154 GB for CIFAR on 4 A100s).

## Weaknesses

### Fatal

None. The paper's core theoretical contribution — constructing a steerable, approximately shiftable and scalable basis for similarity group convolution — is valid and well-motivated.

### Major

1. **Missing experimental comparisons with the most relevant prior work undermines the claimed state-of-the-art.** The paper claims "state-of-the-art results on translated, rotated and scaled MNIST datasets" (abstract, conclusion) but Table 2 compares only against E2CNN (rotation/reflection equivariant, not designed for scale) and Sim2CNN (standard CNN with augmentation). SREN (Sun & Blu, 2023) and RST-CNN (Gao et al., 2022) are both discussed in the Related Work (Section 1.1) as pursuing similarity group equivariance, yet neither appears in the experimental comparison. The gap is significant: the comparison against E2CNN is uninformative for scale transformations, and without SREN/RST-CNN results, the reader cannot evaluate whether SECNNs advance the state of the art or simply match it. The authors should either include these baselines or explain why a direct comparison is not feasible (e.g., different experimental setups).

### Minor

1. **The "approximately shiftable and scalable" property lacks quantitative analysis.** The paper repeatedly describes the basis as "approximately shiftable and scalable" (Section 3.1.1, Figure 1, conclusion), but there is no measurement of how large the approximation error is, how it varies with the number of frequency components, or whether it degrades equivariance in practice. The paper states that the polynomial decay functions are "not band-limiting" and that cropping avoids aliasing, but the relationship between these operations and the approximation error is not quantified. A direct measurement — e.g., applying a small translation to an input and measuring how much the simConv output deviates from the translated version of the original output — would strengthen the paper.

2. **The claimed benefit of continuous translation equivariance is not experimentally isolated.** The paper motivates continuous translation equivariance as a key advantage over methods that only achieve discrete translation equivariance. However, all experiments involve integer-pixel translations (MNIST) or centered images (CIFAR), where standard discrete translation equivariance is already effective. The strong MNIST results could be driven primarily by rotation/scale equivariance rather than continuous translation equivariance per se. An experiment with sub-pixel translations, or a direct ablation comparing the shiftable basis against an exact discrete translation version, would clarify whether the approximate shiftable property adds practical value.

3. **The SECNN-4D vs. SECNN-3D/-Mix performance tradeoff is attributed to channel count without a controlled ablation.** The paper notes that SECNN-4D performs worse than SECNN-3D and -Mix and suggests "the number of channels also plays a critical role" (Section 5, Table 2 discussion). However, no controlled experiment varies channels while holding weight dimensionality fixed, leaving the reader unable to distinguish between a fundamental disadvantage of 4D weights and a suboptimal hyperparameter choice.

4. **No description of how frequency components ($\omega_\phi$, $\omega_\rho$, etc.) are chosen in practice.** The number of frequency components directly affects both approximation quality and computational cost, yet the paper does not explain how these are selected for the experiments.

5. **Group pooling layer design choices are underspecified.** For natural image classification, the paper uses "an orientation histogram approach" (Section 4) but does not specify the grid resolution or other design parameters, which may matter for CIFAR results.

### Trivial

None.

## Nice-to-Haves

- Report inference FLOPs and timing to substantiate the "Computational Optimization" contribution.
- Sub-pixel translation experiments to isolate the practical value of the approximate shiftable property over discrete translation equivariance.
- Estimate the impact of a custom CUDA kernel optimization on the reported memory consumption (36–154 GB), which is acknowledged as severe in the Limitations.

## Removed Points

These points were raised by reviewers but removed per the filtering guidelines:
- **Typographical errors** ("fliter," "flited," "$\\dot{-}2$," missing parentheses): Removed as these are parser artifacts or formatting issues, not author errors.
- **Criticism about no inference/FLOPs reporting being a major omission**: Moved to Nice-to-Haves; the paper already provides memory and training time figures.
- **Claim that continuous translation equivariance is not demonstrated to be practically better at all**: Revised to Minor — the concern has merit but the paper's contribution is broader than just continuous translation.
- **Demand for CUDA kernel optimization estimates**: Removed as speculative and not a reasonable ask for an academic submission.
- **Complaint about missing description of how frequencies are chosen**: Kept but downgraded to Minor; this is a legitimate reproducibility concern but not fatal.
- **"The paper should also cover additional tasks" type demands**: Removed as scope creep.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Add experimental comparisons against SREN and RST-CNN on the same MNIST-RS variants**, or clearly state why a direct comparison is not possible (e.g., different dataset splits, different metrics). This is essential to substantiate the SOTA claim.
2. **Provide a quantitative equivariance error analysis** for the approximate shiftable property: measure output deviation under sub-pixel translations as a function of the number of frequency components.
3. **Include a controlled ablation** that varies the number of channels while holding weight dimensionality (4D vs. 3D vs. Mix) fixed, to clarify whether the SECNN-4D weakness is structural or due to channel budget.
4. **Specify the frequency component selection** and the group pooling grid resolution in the experimental setup for reproducibility.

## Score and Decision

This paper makes a genuine theoretical contribution — constructing a basis for full similarity group equivariance — and shows competitive results. However, the omission of experimental comparisons against the most relevant prior work (SREN, RST-CNN) prevents the SOTA claim from being verified, and the "approximately shiftable" property is asserted without quantitative analysis. These issues are significant but fixable. The paper's core contribution is real and well-motivated, but the evidence presented is incomplete relative to the claims made.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>