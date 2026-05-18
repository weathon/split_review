Now I have a thorough understanding of the paper. Let me construct the final review.

## Summary

This paper systematically investigates camera bias in person re-identification (ReID) models, with a focus on the previously overlooked setting of unseen domains. It makes three main contributions: (1) quantifying camera bias across diverse models on unseen domains (Table 1), (2) providing an empirical mechanistic analysis of why camera-specific feature normalization debiases features (Figure 2) and demonstrating its broad effectiveness across 17 models (Table 3), and (3) exploring camera bias in unsupervised learning and showing that simple training modifications yield substantial gains (Table 6, up to +19.3% mAP). The paper is primarily an empirical analysis contribution with practical methodological takeaways.

## Strengths

- **Systematic demonstration of camera bias on unseen domains, an overlooked setting**: Table 1 shows that across 10+ state-of-the-art ReID models (camera-aware, camera-agnostic, supervised, unsupervised, domain-generalizable, CNN and ViT backbones) and four datasets, camera bias (NMI between cluster labels and camera labels) is consistently large on unseen domains, often exceeding training-domain bias. This establishes the problem scope convincingly.

- **In-depth mechanistic explanation of why normalization debiases**: Section 4.2 (Figure 2) breaks down the feature space, showing that (a) dimensions vary in sensitivity to camera changes, (b) features translate consistently in camera-sensitive dimensions across samples, and (c) centering those sensitive dimensions dominates the performance gain. This goes beyond prior heuristic usage (Gu et al., 2020; Luo et al., 2021a) by explaining *why* it works.

- **Broad empirical validation of normalization across 17 models on three unseen-domain benchmarks**: Table 3 demonstrates consistent mAP and R1 improvements across diverse models regardless of training method (supervised, unsupervised, domain-generalized), backbone (ResNet, ViT), or camera-awareness. For example, +7.5% mAP for CC on Market-1501, +9.4% for TransReID. Ablations (Table 4), sample-size analysis (Figure 5), and compatibility with other postprocessing methods (Table 5) further support robustness.

- **Extension to fine-grained bias factors beyond cameras**: Section 4.3 shows that group-specific normalization for low-level image properties (brightness, sharpness, area) and body angle reduces bias, and that combining property-group and camera labels can surpass camera-only normalization (Figure 3c). This reveals new bias dimensions and demonstrates normalization as a flexible tool.

- **Identification and practical mitigation of camera bias in unsupervised learning**: Toy experiments (Figure 6) causally demonstrate that camera-biased pseudo labels hurt more than label accuracy alone would predict, and that single-camera clusters degrade performance. Simple strategies — debiased pseudo labels and discarding single-camera clusters — yield large gains (e.g., +19.3% mAP for CC on MSMT17, Table 6).

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Mechanism analysis (§4.2) is conducted on a single model–dataset combination.** The central explanatory claim — that normalization works because features move consistently in camera-sensitive dimensions and that centering those dimensions dominates the debiasing effect — is analyzed on one model (TransReID-SSL trained on MSMT17, evaluated on CUHK03-NP). While the practical effectiveness of normalization is convincingly demonstrated across 17 models in Table 3, the paper does not verify whether the dimensional sensitivity pattern holds for ResNet-based models, camera-aware models, or other unseen datasets. A second model–dataset pair in §4.2 would substantially strengthen the mechanistic claim. As it stands, the explanatory story rests on a single instance, which limits the generality of the mechanism analysis.

2. **USL training strategies validated on only one person ReID dataset.** The unsupervised learning modifications (§5.4) are evaluated on MSMT17 (person) and VeRi-776 (vehicle), but no additional person ReID dataset such as Market-1501 or CUHK03 is tested for the training strategies. While MSMT17 is the largest and most challenging person ReID benchmark, testing on at least one additional person dataset would directly support the claim of generalizability. The toy experiments in §5.2 use Market-1501, but these are controlled simulations, not full training strategy evaluations.

### Trivial

1. **Algorithm 1 could clarify how normalization statistics are computed during iterative USL training.** The pseudocode in §5.3 describes debiased features (Equation 2) but does not specify whether per-camera statistics are computed once from the initial model, recomputed each epoch, or accumulated via a running queue. In context it is natural to assume recomputation each clustering iteration, but explicit clarification would aid reproducibility.

2. **NMI bias measure dependency on clustering method.** The paper uses NMI between InfoMAP cluster labels and camera labels as the primary bias measure. While this is reasonable, a brief note on whether the observed patterns might be sensitive to the choice of clustering algorithm or its hyperparameters would strengthen the methodological rigor.

## Nice-to-Haves

- A limitations subsection (or paragraph in the conclusion) explicitly stating the dependency on camera labels at test time for the normalization method, and discussing settings where camera labels may be unavailable or noisy, would improve scholarly completeness. The paper is already transparent about the requirement, but a brief discussion of scope would be beneficial.
- Replicating the mechanism analysis (§4.2) on at least one additional model–dataset pair (e.g., a ResNet-based model on Market-1501, or a camera-aware model) to verify the dimensional sensitivity pattern.
- A brief acknowledgment that the toy experiments (§5.2) use clean simulation of pseudo-label bias and do not capture the iterative, self-reinforcing nature of bias in real USL training.

## Removed Points

These points were identified by reviewers but are removed or downgraded after verification against the paper:

- *"The method requires camera labels at test time without adequate discussion"* — The paper is explicit in §4.1 that the method "postprocesses embedding vectors leveraging camera labels at test time." In ReID, camera labels are a standard dataset annotation and a reasonable assumption for multi-camera deployments. The criticism misunderstands the paper's stated scope.
- *"Unfair comparison with other methods"* — Not raised by reviewers; included here for completeness. The comparisons favor baselines, not the proposed method.
- *Formatting/style nitpicks and parser artifacts* — These reflect PDF extraction issues, not author errors.

## Novel Insights

The reviews surface an interesting tension: the paper's core strength is its broad empirical validation (17 models, multiple benchmarks, consistent gains), yet the one place where the validation narrows — the mechanism analysis in §4.2 — is also where the paper makes its most specific explanatory claim about *why* normalization works. This creates a mismatch between the breadth of the "what" (normalization works) and the narrowness of the "why" (the mechanism on one model). The paper would benefit from either broadening the mechanism validation or softening the explanatory framing to match the evidence. This pattern — broad empirical sweep meeting narrow mechanistic analysis — is a recurring issue in empirical deep learning papers that aim to explain as well as demonstrate.

## Suggestions

1. Add at least one additional model–dataset pair to the dimensional sensitivity analysis in §4.2 (e.g., a ResNet-50 based model on Market-1501, or a camera-aware model). If the pattern holds, the mechanism claim becomes much stronger; if it differs, the paper gains useful nuance.
2. Evaluate the USL training strategies on at least one additional person ReID dataset (e.g., Market-1501 or CUHK03) to strengthen the generalization claim.
3. Explicitly state in Algorithm 1 or its surrounding text whether per-camera normalization statistics are computed once, recomputed each epoch, or estimated incrementally.
4. Add a brief limitations paragraph discussing the camera-label requirement for test-time normalization and the scope of the mechanism analysis.

## Score and Decision

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>