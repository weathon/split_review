Now I have a complete picture. Let me produce the final consolidated review.

## Summary

This paper proposes SINGD (Structured Inverse-Free Natural Gradient Descent), which extends the INGD method from Lin et al. (2023) in two key ways: (1) it establishes an inverse-free KFAC update (IKFAC) that avoids the matrix inversions causing numerical instability in standard KFAC, and (2) it imposes sparse structures (diagonal, triangular, hierarchical) on the Kronecker factors in the matrix logarithm space to reduce memory consumption. The paper evaluates on CIFAR-100 and ImageWoof-10 using vision transformers and ConvNets, showing that SINGD remains stable in BFloat16 while KFAC diverges, and that structured variants can approach AdamW's memory footprint.

## Strengths

- **Inverse-free KFAC formulation addresses a real problem.** The paper identifies that KFAC's reliance on matrix inversions/decompositions creates genuine numerical instability in low-precision training (BFloat16/FP-16). Figure 1 experimentally demonstrates this: KFAC diverges in FP-16 while IKFAC remains stable. This is a practical contribution given the growing adoption of low-precision training pipelines.

- **Structured Kronecker factors in the logarithm space are a principled design.** Rather than imposing ad-hoc sparsity on the curvature estimates (as in diagonal/block-diagonal KFAC variants), the paper exploits Lie-algebraic structure to design subspaces closed under the required operations (matrix multiplication, elementwise ops). The triangular and hierarchical structures (Figure 6, Table 1) are non-obvious and the paper provides a clear algebraic rationale for why certain structures are admissible while others (e.g., tridiagonal) are not.

- **Demonstrates stability on transformer-based architectures in low precision.** Prior INGD (Lin et al., 2023) was only evaluated on ConvNets in FP-32. The paper shows that both IKFAC and SINGD work stably in BFloat16 on vision transformers (Compact-ViT, Swin-ViT, GC-ViT), extending the applicability of inverse-free second-order methods.

## Weaknesses

### Fatal
None.

### Major

- **Scope overclaiming relative to experimental validation.** The paper's title, abstract, and framing repeatedly invoke "large neural nets" and contrasts with "billions of parameters" (line 14), yet experiments are limited to CIFAR-100 (32×32 images, 100 classes) and ImageWoof-10 (a 10-class, ~10K-image subset of ImageNet). The models used (Compact-ViT, Swin-Tiny) are small-scale vision transformers. No experiments on language models, ImageNet-scale vision (1K classes, 1.2M images), or models with more than ~100M parameters are presented. The concluding claim that the work "expands the scope of second-order methods to training transformer-based NNs" is overstated: it expands the scope to *small* vision transformers, not to the large-scale transformers (BERT, GPT, ViT-L/16) that dominate modern deep learning. This gap between the claimed generality and the actual evaluation significantly weakens the paper's impact claims.

- **No statistical significance or multiple-run reporting.** All test error curves (Figures 1, 5) appear to be single runs with no error bars, confidence intervals, or mention of multiple seeds. Given known variance in deep learning optimization (especially with random hyperparameter search), the observed differences between methods could be noise. This is a methodological concern that makes it difficult to assess whether SINGD reliably matches AdamW or whether the reported advantage over block-diagonal structures is robust.

- **Memory efficiency claims lack supporting measurements for transformer models.** The paper's central thesis is that SINGD reduces memory. However, the only memory comparison (Figure 1, right) is for VGG-16 on CIFAR-100 — a small model (≈15M parameters). For the transformer models where memory is claimed to matter most, no memory measurements are reported in the main text. Table 3 (referenced but stripped) may contain this data, but the main text does not present a single memory number for Swin-ViT, Compact-ViT, or any other transformer. This is a significant omission for a paper whose core contribution is memory efficiency.

### Minor

- **KFAC baseline may be at a disadvantage due to implementation choices.** The paper states that KFAC requires casting to FP-32 for matrix inversion (line 186), which is inherent to KFAC's design. However, KFAC's poor performance could also reflect suboptimal tuning of damping or update frequency. The paper reports tuning hyperparameters via random search but does not specify the search budget, number of trials, or ranges — making it hard to assess whether KFAC was given a fair comparison. Since KFAC is the primary baseline, more detail is needed.

- **Connection between IKFAC and KFAC (Theorem 1) is deferred to the appendix.** The paper states in Section 3.1 that "IKFAC corresponds to a specific setting of the INGD method" and Figure 2 references "Theorem 1," but no derivation or theorem statement appears in the main text. While appendix deferral is acceptable, the main text would benefit from at least stating the result informally to ground the experimental claims (especially since IKFAC is presented as a central contribution in the abstract and introduction).

- **Hyperparameter tuning details are underspecified.** "Random search" is mentioned but the budget (number of trials) and the search ranges for learning rate, damping, etc., are not reported. This limits reproducibility and makes it difficult to assess whether the comparisons are fair.

### Trivial
- The same symbol $F$ is used for both the MLE-based Fisher (Section 2.1) and the variational-distribution Fisher (Section 2.2). While the paper notes they "should not be confused" (line 104), using distinct notation would improve clarity.

## Nice-to-Haves
- Reporting wall-clock time per iteration for each method would help practitioners assess the practical speed-memory tradeoff (beyond asymptotic FLOPs counts).
- An ablation study isolating the effect of each component (inverse-free update vs. structured factors) on a single architecture with multiple seeds would strengthen the contribution.
- An analysis of numerical stability (e.g., measuring gradient norm growth or NaN frequency during training) would substantiate the claimed robustness advantage.

## Removed Points
These points are flagged to be removed; treat them with caution:
- **Missing theoretical derivation of IKFAC (structured as "Critical Issue").** The reviewer claimed Theorem 1 is entirely missing. Theorem 1 is referenced in Figure 2 and the derivation is almost certainly in the appendix, which the parser strips from all submissions (per instructions). The experimental validation of IKFAC (Figure 1) is present in the main text.
- **"INGD has not been derived from popular NGD approaches for DL" is misleading.** This is a matter of interpretation about framing, not a factual error. The paper later correctly positions both methods as approximate NGD.
- **Critique that the paper doesn't use large-scale NLP experiments (GPT-2, BERT).** Demanding experiments on billion-parameter language models when the paper's scope is about the algorithmic framework, and the experiments already cover vision transformers, is a request that exceeds the paper's stated scope. This is moved from "Missing Experiments" to a Nice-to-Have.
- **Critique about missing Tables 2/3 for computational complexity.** Tables 2 and 3 are referenced in the main text and are likely in the stripped appendix.
- **Pure formatting/style nitpicks** about presentation density, equation readability, etc.

## Novel Insights
The most interesting finding from the cross-review analysis is that the harsh critic's strongest critique (missing derivation of IKFAC) is a non-issue per the parsing constraints, while the genuinely substantive weaknesses are about experimental rigor (no error bars) and scope overclaiming (claiming "large neural nets" from small-scale vision experiments). This pattern — where reviewers conflate structural issues (appendix-stripped content) with real evidential gaps — is worth noting. The paper's core algorithmic idea (structure-preserving updates in the logarithm space) is sound and non-obvious, but the evaluation falls short of the paper's own framing.

## Suggestions

1. **Right-size the claims in the title and abstract.** Replace "Large Neural Nets" and "Large Neural Networks" with language that accurately reflects the evaluation scale (e.g., "Modern Neural Network Architectures"). The current framing sets expectations the experiments cannot meet.

2. **Add multiple-seed experiments with error bars** for at least one representative architecture (e.g., Compact-ViT on ImageWoof-10) and report final numerical results (test error ± std) for all methods.

3. **Provide memory measurements for transformer models in the main text.** Even a simple table showing peak GPU memory for Swin-Tiny or Compact-ViT under each optimizer would substantially strengthen the paper's central memory-efficiency claim.

4. **State the IKFAC-KFAC equivalence result informally in Section 3.1** even if the formal proof is in the appendix. A 2–3 line statement like "IKFAC update (Eq. X) differs from the KFAC update only by an O(β²) term due to the matrix exponential truncation" would let readers evaluate the contribution without diving into the appendix.

5. **Report the random search budget and hyperparameter ranges** used for each optimizer to improve reproducibility and fairness assessment.

## Score and Decision

The paper addresses a genuine practical challenge (KFAC's instability in low precision and memory overhead) with a technically sound approach. However, the experimental evaluation falls substantially short of the paper's own framing: the experiments are on small-scale datasets and models, lack statistical rigor, and omit the key memory measurements for the architectures where the contribution is most relevant. The paper would need significantly broader and more rigorous experimentation (larger models/datasets, multiple seeds, memory profiling on transformers) to support its claims about "large neural nets." In its current form, the contribution is promising but incompletely validated.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>