Now I have a thorough understanding of the paper. Let me write the consolidated review.

## Summary

This paper proposes SINGD (Structured Inverse-Free Natural Gradient Descent), extending the INGD method of Lin et al. (2023) in two directions: (i) establishing a theoretical connection between INGD and KFAC through "IKFAC" (claimed but incompletely presented), and (ii) imposing sparse triangular/hierarchical structures on Kronecker factors in the matrix logarithm space to reduce memory consumption. The method aims to make second-order optimization numerically stable in low-precision training and memory-efficient enough for modern architectures. Experiments on CIFAR-100 and ImageWoof-10 with several vision transformer variants show SINGD can match AdamW's test error while being stable in BFloat16 — something KFAC cannot achieve.

## Strengths

1. **Numerical stability in low-precision training is convincingly demonstrated.** Figure 1 (left/center) directly shows KFAC diverging in FP-16 while IKFAC and SINGD remain stable across both FP-32 and FP-16. Figure 5 further confirms this on transformer models in mixed BFloat16 precision. This addresses a concrete, practical limitation of KFAC in modern training pipelines where low precision is standard.

2. **Memory efficiency through structured Kronecker factors is a principled contribution.** The paper identifies that sparsity patterns must be closed under matrix multiplication and elementwise operations to work in the logarithm-space update. It then constructs triangular and hierarchical structures that satisfy this requirement — a non-trivial design constraint that rules out many obvious patterns (e.g., tridiagonal matrices are not closed under multiplication). SINGD-Diag achieves memory consumption comparable to AdamW (Figure 1, right), which is notable for a second-order method.

3. **Extends inverse-free second-order methods beyond convolutional networks.** Prior work (INGD) had only been tested on convolution-based models. This paper evaluates on transformer-based architectures (Compact-ViT, Swin-ViT, GC-ViT), showing that the approach generalizes beyond convnets. This broadens the applicability of the method family.

4. **Competitive with AdamW on the tested settings.** Figure 5 shows SINGD (with hierarchical structure) achieves test error comparable to AdamW across multiple architectures, while providing the additional benefits of numerical stability and curvature information.

## Weaknesses

### Fatal
None.

### Major

1. **Theorem 1 is referenced but not presented.** The paper claims a theoretical bridge between IKFAC and KFAC, labeling it "Theorem 1" in Figure 2, but Section 3.1 contains only two paragraphs of high-level description and no theorem statement, proof sketch, or mathematical derivation showing how IKFAC recovers the KFAC update. Without this, the paper's central theoretical contribution — bridging INGD to the predominant KFAC optimizer — is asserted rather than demonstrated. This is a significant gap, whether due to a genuine omission or a parsing artifact.

2. **Claims about "large neural nets" substantially exceed the experimental evidence.** The title and abstract explicitly emphasize applicability to "large neural nets" and "transformer-based models." However:
   - The experiments use compact/efficient vision transformer variants (no parameter counts reported anywhere) on small-scale datasets (CIFAR-100 with 60K images, ImageWoof-10).
   - The only memory measurement shown for transformers is absent — Figure 1's memory plot is for a VGG net on CIFAR-100, not for a transformer.
   - No experiments on models with >100M parameters, no ImageNet-1K-scale evaluation, and no language modeling experiments are presented.
   
   The paper extends INGD to transformer architectures but falls far short of demonstrating applicability to "large neural nets."

3. **No error bars, multiple seeds, or statistical significance.** Figure 5 presents test error curves from what appear to be single runs. Without variance estimates, it is impossible to determine whether the observed differences between SINGD, AdamW, and INGD are meaningful or just run-to-run noise. For a paper making comparative claims ("performs as well as AdamW"), this is a critical omission.

4. **No wall-clock time or throughput comparisons.** For a second-order optimizer to be practically useful, the per-iteration computational overhead must be quantified against baselines. The paper reports no timing data whatsoever. SINGD's use of truncated matrix exponentials and subspace projections may add significant overhead; without timing, it is unclear whether the memory and stability benefits come at an unacceptable computational cost.

### Minor

1. **The method description is abstract and lacks concrete update rules.** The paper describes the structured update through subspace projection maps but does not provide a self-contained summary of the SINGD update equations in the main text. The relationship between the various matrix symbols (S, S_K, S_C, K, C, A, precision matrix) shifts across sections, making the flow harder to follow than necessary.

2. **No hyperparameter sensitivity analysis.** The paper mentions random search for hyperparameter tuning but does not report search ranges, selected values, or sensitivity to damping/momentum — all of which are important for second-order methods.

3. **No discussion of limitations.** The paper does not discuss when structured factors might hurt performance (e.g., for highly anisotropic curvature where expressive preconditioners are needed), or when the matrix exponential overhead might exceed the cost of matrix inversion. A candid limitations paragraph would strengthen credibility.

### Trivial
- The preliminaries section on BLR (Section 2.2) is lengthy and overlaps substantially with prior work. It could be condensed to focus on the details directly needed for the paper's contributions.
- The notation for Kronecker factors uses different conventions for KFAC (U_l, G_l → S_K, S_C) and INGD (K, C), which could be unified.

## Nice-to-Haves
- An ablation study showing the performance–memory trade-off across dense, diagonal, block-diagonal, triangular, and hierarchical structures on a single model+dataset would make the design choices more transparent.
- Providing the IKFAC derivation (even a brief sketch) in the main text would make the theoretical contribution self-contained.
- A runtime breakdown (time spent in matrix exponential vs. gradient computation vs. preconditioning) would help practitioners assess practical utility.

## Removed Points
The following points from the reviews were removed per guidelines:
- **Missing Tables 2/3 and pseudocode/algorithm boxes**: These may have been in appendix sections that were stripped by the parser. The rules instruct us not to penalize papers for absent appendix content.
- **Criticism about INGD/KFAC not being cited models**: Not applicable — all cited references are assumed to exist.
- **"BLR derivation is direct repetition"**: Section 2 is explicitly labeled "PRELIMINARIES"; reviewing known material at some length is expected for background sections.
- **"IKFAC still requires matrix exponentials" as a major weakness**: The paper is transparent that it uses truncated matrix exponentials — calling it "inverse-free" describes what it avoids (matrix inversion), not that it is free of all matrix operations. This is a descriptive label, not a misleading claim. However, the point about quantifying overhead of the exponential vs. inversion is kept as a useful question.

## Novel Insights
None beyond the paper's own contributions. The reviews converge on the same observations: the core idea (structured Kronecker factors in logarithm space) is interesting and novel, but the theoretical claims are underdeveloped and the experimental scope does not match the paper's stated ambitions.

## Suggestions
1. **State Theorem 1 explicitly** in the main text with a clear derivation showing how the IKFAC update recovers the KFAC update under what conditions. Even a short proof sketch would substantially strengthen the paper.
2. **Scale up the experimental evaluation** to at least one model with >50M parameters on a standard benchmark (e.g., ResNet-50 on ImageNet-1K, or a GPT-style small transformer on WikiText). Report final accuracy/perplexity, peak memory, and training time.
3. **Add error bars** (multiple seeds with mean ± std) to all experimental figures.
4. **Report wall-clock time per iteration** and total training time for all methods to contextualize the computational cost of the matrix exponential vs. KFAC's matrix inversion vs. AdamW's first-order update.
5. **Provide model parameter counts** for all architectures tested, and add a figure or table showing memory consumption for the transformer experiments (not just VGG).
6. **Add a limitations section** discussing when structured factors may be insufficient and when the matrix exponential overhead dominates.

## Score and Decision

The paper proposes a genuinely interesting approach to mitigating KFAC's two core weaknesses (numerical instability and memory cost) through structure-preserving updates in the matrix logarithm space. The empirical demonstration of low-precision stability is clear, and the design of sparse structures that are closed under the required algebraic operations is non-trivial. However, the paper suffers from a significant gap in its claimed theoretical contribution (Theorem 1 is referenced but not presented), and the experimental evaluation falls well short of the scope claimed in the title and abstract ("large neural nets"). The absence of error bars, wall-clock timing, and scaling experiments makes it difficult to assess the practical significance of the proposed method. These issues are structural rather than cosmetic. I would encourage the authors to complete the theoretical exposition and expand the evaluation; the paper in its current form is not ready for acceptance.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>