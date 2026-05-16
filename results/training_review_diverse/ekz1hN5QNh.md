Now I have thoroughly verified all reviewer claims against the actual paper text. Here is my consolidated review.

---

## Summary

This paper presents HCNN, a fully hyperbolic convolutional neural network built entirely in the Lorentz model, and a hybrid variant HECNN. The authors propose novel Lorentz formulations for 2D convolution, batch normalization, multinomial logistic regression, residual connections, and activations — filling gaps explicitly identified in prior hyperbolic vision work. Experiments on CIFAR-10/100, Tiny-ImageNet, and CelebA show that Lorentz-based models outperform Euclidean and Poincaré baselines on classification, adversarial robustness, low-dimensional embeddings, and most generation metrics.

## Strengths

1. **Novel Lorentz formulations for missing CNN components**: The paper provides the first complete set of Lorentz-model generalizations for 2D convolution (Section 4.1), batch normalization with closed-form centroid (Section 4.2), and MLR (Section 4.3). These components fill a gap identified in prior work ("crucial components for vision, like the standard convolutional layer and the MLR classifier, are still missing") and enable fully hyperbolic vision encoders that previously did not exist in the literature.

2. **Consistent classification improvements with statistical grounding**: On CIFAR-100, HECNN achieves 78.76% vs. 77.72% Euclidean, and HCNN achieves 78.07% — both improvements with non-overlapping standard deviations over five runs. On Tiny-ImageNet, HECNN (65.96%) and HCNN (65.71%) outperform Euclidean (65.19%). These gains demonstrate the practical value of the approach.

3. **Substantial adversarial robustness gains**: Under PGD attacks at ε=3.2/255 on CIFAR-100, HCNN achieves 31.77% accuracy vs. 26.30% for Euclidean (+5.47% absolute). The improvement is consistent across all perturbation levels and attack types (Table 2), directly supporting the claim that fully hyperbolic representations increase decision boundary slack.

4. **Convincing low-dimensional embedding performance**: Figure 4 (labeled as Fig. 3) shows that at embedding dimensions 8, 16, and 32, HECNN and HCNN substantially outperform Euclidean and Poincaré baselines on CIFAR-100, validating the argument that hyperbolic geometry is especially beneficial in low-dimensional feature spaces.

5. **Modular one-to-one replacement design**: All proposed modules are explicitly designed as one-to-one replacements for Euclidean components, demonstrated by directly translating standard ResNet-18 and VAE architectures without changing overall topology. This makes the approach practically accessible.

## Weaknesses

### Fatal
None.

### Major

1. **Overclaiming on VAE generation results**: The paper states "our HCNN-VAE outperforms all baselines" (Section 5.2, paragraph "Main results"). However, Table 2 shows that on CIFAR-100 generation FID, HCNN (100.27) is *worse* than both Hybrid Poincaré (98.19) and Hybrid Lorentz (98.34). The HCNN-VAE is best on 5 of 6 metrics, but the blanket claim is factually incorrect for this specific metric. This is a meaningful negative result that could lead to insights about when fully hyperbolic architectures help versus hurt; ignoring it weakens the paper's credibility.

### Minor

2. **Convolution specification relies on undefined sub-operations**: The Lorentz convolutional layer (Eq. 89) is defined as `LFC(HCat(...))`, where `LFC` is referenced as "similar to chen2021" and `HCat` (hyperbolic concatenation) is from shimizu-et-al-2020 but never defined in this paper. While referencing prior work for sub-operations is standard practice, a brief description of how the kernel weights interact with hyperbolic feature vectors (e.g., whether via tangent-space linearization or some other mechanism) would make the paper more self-contained and reproducible.

3. **Missing ablation for residual connection claim**: Section 4.4 states the proposed residual connection "provides the best empirical performance compared to other viable methods" (citing tangent-space addition, parallel transport addition, Möbius addition, and fully-connected layer addition). No ablation table or quantitative comparison is shown to support this claim.

4. **Weak theoretical justification for BN rescaling**: The batch normalization rescaling step (Eq. 118) multiplies tangent vectors by γ/(√σ²+ε) and maps back via the exponential map. The paper states "a simple multiplication re-scales the features" but does not address whether scaling tangent vectors corresponds to meaningful scaling of Lorentzian distances after the non-linear exponential map (it does not, except asymptotically near the origin). The algorithm is fully specified and may work well as a heuristic, but it is presented without mathematical justification.

5. **Hybrid vs. fully hyperbolic comparison not deeply analyzed**: The paper notes that HECNN (hybrid encoder) outperforms HCNN (fully hyperbolic) on CIFAR-100 and Tiny-ImageNet classification, and provides brief interpretation ("indicating that not all parts of the model benefit from hyperbolic geometry" and "hybrid encoder HNNs might make better use of the combined characteristics"). This observation is potentially the most interesting finding of the paper, but it receives only two sentences of discussion with no deeper analysis or ablation.

### Trivial
- The notation `β` is reused in Section 4.3 (both as a variable defined in Eq. 173 and inside the `sinh⁻¹` argument). This causes momentary confusion but is resolvable by reading the derivation.
- Figure 4 (bar chart) could be complemented by a numeric table for the low-embedding results.

## Nice-to-Haves
- An ablation study evaluating the effect of numerical stability tricks (feature clipping, Euclidean reparameterization) on performance.
- Runtime and parameter count comparisons to help readers assess the computational cost of hyperbolic components.
- Clarification in the adversarial robustness section about whether attacks were generated using standard Euclidean approaches or adapted for hyperbolic geometry (though FGSM/PGD on cross-entropy in pixel space is the standard and fair comparison).

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"The Lorentz convolutional layer is not actually specified — core component is underspecified"** (Harsh Critic, Critical Issue 1): The paper gives a clear high-level definition referencing shimizu-et-al-2020 and chen2021 for sub-operations (LFC, HCat). This is standard practice in method papers. The level of specification is sufficient for reproducibility given the cited references. Kept as a minor clarity point instead.

- **"BN rescaling undermines confidence that LBN actually normalizes in a geometrically meaningful way"** (Harsh Critic, Critical Issue 2): The paper presents the algorithm as a practical heuristic (the text says "we propose to re-scale" without claiming it is a theorem). The formula is fully specified. The criticism overstates the impact of the weak theoretical justification. Kept as a minor weakness instead.

- **"Experimental results contradict the paper's central thesis"** and **"text says 'Our HCNN-VAE outperforms all baselines' — this is inaccurate"** (Harsh Critic, Critical Issue 3): The VAE overclaim is genuine and kept as a Major weakness. However, the broader claim that results "contradict the central thesis" is unsupported — the paper clearly acknowledges HECNN > HCNN and offers interpretation. On VAE, 5/6 metrics favor HCNN; the overclaim applies to only one. The adversarial robustness results are uniformly positive for HCNN. The "central thesis" (that fully hyperbolic models can work well and provide benefits) is supported.

- **"The paper offers no analysis"** of the hybrid vs. fully hyperbolic comparison: The paper does offer analysis: "indicating that not all parts of the model benefit from hyperbolic geometry" (Section 5.1) and "hybrid encoder HNNs might make better use of the combined characteristics" (Section 5.1, low-embedding paragraph). The analysis is brief but present.

- **"The low-embedding experiment ... numeric tables would be more informative"** and **"The paper does not report how the number of parameters changes"**: These are presentation preferences and nice-to-haves, not core weaknesses.

- **"The adversarial attack setting ... should be specified"**: The paper uses standard FGSM/PGD, which is clear from context. Specifying the exact loss function is a minor detail that doesn't affect the validity of the comparison.

- **Missing related works**: Removed per instructions (no external sources to confirm).

## Novel Insights

The reviews surface an important tension that the paper under-explores: HECNN (hybrid encoder) consistently matches or exceeds HCNN (fully hyperbolic) on classification tasks. This suggests that the benefits of hyperbolic geometry in vision may come primarily from the decoder/classifier layers rather than from making every layer hyperbolic. The paper's brief acknowledgment of this finding without deeper analysis leaves a significant open question. Additionally, the CIFAR-100 generation FID result (where HCNN is worse than hybrid models) hints that the relationship between full hyperbolicity and generation quality is not monotonic — a point that deserves investigation rather than omission.

## Suggestions

1. **Correct the VAE overclaim**: Qualify the statement in Section 5.2 to acknowledge that while HCNN-VAE is best on 5 of 6 metrics, it underperforms hybrid models on CIFAR-100 generation FID. Discuss why this might be the case.
2. **Add a brief forward-pass description for the Lorentz convolution**: A few sentences describing how kernel weights are applied to hyperbolic feature vectors (tangent-space approach or otherwise) would substantially improve reproducibility without adding much length.
3. **Add the missing residual connection ablation**: A single table comparing the five mentioned addition methods would justify the "best empirical performance" claim.
4. **Expand the discussion of HECNN vs. HCNN**: This is the paper's most surprising finding and deserves analysis — is the trade-off optimization difficulty, are early layers not benefiting from hyperbolicity, or are there other factors?

## Score and Decision

The paper makes a genuine contribution by providing the first complete set of Lorentz-model CNN components for vision, and the experimental evidence broadly supports their effectiveness. The VAE overclaim is the most significant flaw and needs correction, but it does not invalidate the paper's overall contribution. The remaining issues (minor underspecification of the convolution, missing ablation, weak BN justification) are addressable in revision.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>