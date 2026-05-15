Now I have all the information needed to produce the final consolidated review. Let me compose it.

## Summary

This paper proposes Guided Stochastic Exploration (GSE), an always-sparse dynamic sparse training algorithm that never materializes dense weights or computes dense gradients. GSE samples a subset of inactive connections, computes gradients only for those sampled connections, and grows the ones with the largest gradient magnitudes. The method achieves competitive or superior accuracy to existing DST methods (including RigL and SET) across CIFAR-10/100 and ImageNet with ResNet, VGG, and ViT architectures, while offering asymptotic complexity of O(n) with respect to model width versus RigL's O(n²) for the growing step.

## Strengths

- **Truly always-sparse training that avoids dense gradient computation**: Unlike RigL, which periodically computes dense gradients, GSE never materializes dense weights or gradients at any point during training (Section 3, Algorithm 1). Forward passes use only sparse weights, and gradient computation is limited to a sampled subset of inactive connections. This directly addresses a key limitation of prior DST methods.

- **Consistent accuracy improvements over DST baselines under controlled conditions**: On CIFAR-10/100 (Table 1), where all methods share identical optimization settings, GSE consistently matches or exceeds RigL. At 98% sparsity on CIFAR-100 with ResNet-56, GSE achieves 68.77% vs. RigL's 68.40%, and this pattern holds across architectures (VGG, ViT) and sparsity levels. The CIFAR results are particularly reliable because they use a controlled setup with all baselines reproduced under the same conditions.

- **Systematic analysis of the subset sampling mechanism**: Section 4.2 thoroughly investigates the effect of subset size (γ) and sampling distributions (uniform, GraBo, GraEst). The finding that γ=1 (subset size equal to active set) suffices to match RigL's accuracy is clean and well-supported. The analysis of why uniform sampling works best, corroborated by the saturation and eventual decline of biased distributions, is insightful and empirically grounded.

- **Model scaling experiment demonstrating wider sparse models improve accuracy**: Section 4.5 (Figure 3) shows that increasing model width while keeping the number of active connections fixed improves accuracy by 6.5% on average for CNNs. This is a non-obvious and practically useful result with implications for hardware-constrained deployment.

- **FLOPs analysis showing efficiency gains at high sparsity**: Section 4.6 quantifies that GSE uses 11.8% fewer FLOPs than RigL at 99% sparsity, with the gap widening at higher sparsities. This directly supports the complexity claims.

## Weaknesses

### Fatal
None.

### Major

- **ImageNet comparison uses uncontrolled baselines from prior publications**: The paper states explicitly (Section 4.4) that ImageNet baseline numbers were "obtained from prior publications" with potentially different hyperparameters, training durations, and data augmentation. GSE uses a 100-epoch schedule with learning rate warm-up and label smoothing, while the baselines may use different recipes. This means Table 2 is not a controlled comparison, and the claimed superiority cannot be definitively attributed to the method rather than training setup differences. The controlled CIFAR experiments are reassuring but do not fully mitigate this concern for the ImageNet results.

### Minor

- **Tables lack variance information despite the paper stating experiments are repeated three times**: The paper states (Section 4.1) that experiments are repeated three times and the mean and 95th percentile are reported/plotted, but the main accuracy tables (Tables 1, 2) only show point estimates. Without error bars or confidence intervals, the reader cannot assess whether differences between methods (e.g., 68.77% vs. 68.40%) are significant relative to run-to-run variance. This is especially important at high sparsity where differences are small.

- **The method description's efficient sampling discussion is scoped to fully-connected layers, but the method's application to convolutional layers is not fully spelled out**: The paper states on line 53 that the efficient sampling discussion (alias method, factorized distributions) applies "in the case of fully-connected layers." While uniform sampling (which GSE ultimately uses) trivially extends to any connection set regardless of layer type, the paper does not explain how the non-uniform distributions (GraBo, GraEst) or the connection-indexing scheme map to the 4-dimensional structure of convolutional kernels. The activation and delta tensors for conv layers have spatial dimensions, and the GraBo/GraEst formulas (which sum over dimensions via the 1 vector) naturally handle these, but this is never explicitly discussed. The method is clearly implementable and the uniform approach is architecture-agnostic, but the paper would benefit from a brief clarification.

- **The FLOPs analysis uses simulated counts rather than wall-clock time, and the brain-sparsity extrapolation is purely illustrative**: Section 4.6 correctly uses the same FLOPs estimation method as prior work (Evci et al., 2020), and the 11.8% saving at 99% sparsity is meaningful. However, the right panel of Figure 4 extrapolates to brain-level sparsities (10^-7 to 10^-8) far beyond anything trained with deep learning. While the paper labels this as "for illustration," the framing as a quantitative comparison (e.g., "RigL uses 131 times more FLOPs") could mislead readers about practical applicability. Verified kernels for unstructured sparsity on current hardware would be needed to confirm real speedups.

### Trivial
None.

## Nice-to-Haves

- Reproducing ImageNet baselines under the same training recipe used for GSE would strengthen the comparison.
- Reporting standard deviations or confidence intervals in the main tables.
- A brief paragraph explaining how the connection-sampling framework maps to conv layers (e.g., treating each kernel position as a connection, or summing over spatial dimensions in the distributions).
- Wall-clock timing measurements (even simulated) to complement the FLOPs analysis.

## Removed Points

- **"Method defined for fully-connected layers only" (fatal framing)**: The harsh critic framed this as a fatal flaw undermining all experimental results. In fact, the paper scopes the efficient sampling discussion to FC layers (line 53: "in the case of fully-connected layers"), and uniform sampling (the method's final choice) extends transparently to any layer type. The GraBo/GraEst distributions also naturally extend via spatial summations. The method is not "defined for FC layers only" — the core algorithm is architecture-agnostic. This is a clarity issue, not a fatal omission.

- **"O(n) complexity claim is not justified for conv layers"**: The O(n) complexity is with respect to model width n (number of channels/units). The spatial dimensions of conv layers contribute a multiplicative constant factor (kernel size, input spatial resolution) that is independent of n. The asymptotic claim is sound. The critic's assertion that O(H·W) invalidates the O(n) claim misunderstands complexity analysis — H and W are not functions of model width.

- **"Brain sparsity extrapolation is speculative"**: The paper explicitly calls this "for illustration" (line 167). This is not a claim being evaluated but a motivational visualization.

- **Generic formatting/style nitpicks and missing related work concerns**: Removed per instructions.

- **Strengths from Strength Finder that were generic and lacked specific content**: The finder's listed strengths were contentful and specific — none needed removal.

## Novel Insights

The most interesting observation emerging from the reviews is the tension between the method's elegant simplicity (uniformly sample a subset of inactive connections, compute gradients only for those, grow the top-k) and the paper's framing of complexity guarantees in fully-connected terms, despite evaluating on CNNs. The conflation is not fatal — the method clearly works on CNNs, and the uniform distribution is architecture-agnostic — but it points to a broader pattern in sparse training papers: theoretical analyses are often developed for the simpler FC case, while experiments are run on the practically relevant CNN case, with the adaptation left implicit. This paper would be strengthened by acknowledging this gap explicitly and providing the straightforward generalization. The empirical finding that uniform sampling outperforms gradient-biased distributions is also more significant than the paper's brief discussion suggests, as it implies that exploration diversity matters more than gradient-informed priors — a finding that could inform future DST design beyond this specific method.

## Suggestions

1. Add a brief section or paragraph explicitly describing how the method applies to convolutional layers — e.g., "For conv layers, each kernel weight connects an input channel, output channel, and spatial offset; uniform sampling treats all such connections as equally likely, and GraBo/GraEst distributions sum over spatial dimensions using the activation/delta tensors as shown."

2. Include error bars (standard deviation or 95% CI) in Tables 1 and 2. With 3 runs, this is trivially computable and would greatly improve the reader's ability to assess the significance of reported differences.

3. Either reproduce ImageNet baselines under consistent settings, or clearly caveat Table 2 as a literature comparison and weight the paper's conclusions more heavily on the controlled CIFAR experiments.

4. Consider adding a small ablation study on a purely fully-connected architecture (e.g., MLP on CIFAR-10) to cleanly validate the method end-to-end as described, decoupling the conv-layer ambiguity from the core evaluation.

## Score and Decision

Overall assessment: The paper presents a genuinely useful algorithmic contribution to dynamic sparse training — the idea of sampling a subset of inactive connections and computing gradients only for those is simple, principled, and demonstrably effective. The controlled CIFAR experiments provide credible evidence of accuracy improvements over strong baselines. The main weaknesses — uncontrolled ImageNet comparison and missing variance reporting — are significant but addressable. The conv-layer clarity issue is minor and does not threaten the paper's core findings. The contribution is valuable to the sparse training community, and the paper is sound in its core claims.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>