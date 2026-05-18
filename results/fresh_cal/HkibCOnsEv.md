Now I have all the information needed. Let me produce the final consolidated review.

---

## Summary

This paper extends the inverse-free natural gradient (INGD) framework by (i) proposing IKFAC, claimed to be an inverse-free variant that recovers the KFAC update, and (ii) introducing structured Kronecker factors via Lie-algebraic subspace projections to reduce memory, yielding a method called SINGD. Experiments on compact vision models (Compact-ViT, Swin-ViT, GC-ViT, Rep-ViT) on CIFAR-100 and ImageWoof-10 show SINGD is competitive with AdamW while being stable in mixed precision, unlike KFAC.

## Strengths

- **Memory reduction via structured Kronecker factors is demonstrated.** Figure 1 (right) shows SINGD-Diag roughly matches AdamW's memory footprint (dashed line) on a VGG/CIFAR-100 setup, and the paper introduces a principled Lie-algebraic framework for designing sparse patterns (diagonal, triangular, hierarchical in Table 1) that remain closed under the required matrix operations. This is a concrete engineering contribution.

- **Numerical stability in low precision is shown empirically.** Figures 1 (left/center) and 5 show that IKFAC and SINGD converge stably in half-precision (BFloat16) while KFAC diverges in at least one configuration. The inverse-free formulation (relying only on matrix multiplies rather than inversions) provides a plausible mechanism for this stability.

- **The hierarchical structure demonstrates a meaningful memory-performance trade-off.** Figure 5 shows that the hierarchical structure (Table 1) performs comparably to the dense INGD and outperforms the simpler block-diagonal structure, suggesting the subspace projection framework can yield better structured approximations than naive diagonal/block-diagonal approaches.

- **Evaluated on both transformer-based and CNN architectures.** The experiments include Compact-ViT, Swin-ViT, GC-ViT (transformers) and Rep-ViT (CNN-inspired), showing the method's applicability beyond the convolution-only focus of prior INGD work (Lin et al., 2023).

## Weaknesses

### Fatal
None. The core technical approach (inverse-free updates + structured Kronecker factors) is not fundamentally flawed; the issues are in incomplete substantiation and insufficient evaluation.

### Major

- **Theorem 1 and the IKFAC-to-KFAC equivalence are referenced but not provided.** Section 3.1 contains only two sentences of text plus Figure 2. The caption of Figure 2 states "IKFAC behaves like KFAC (Theorem 1)," but no theorem statement, derivation, or proof appears anywhere in the paper. The paper claims as a core contribution that "a special case of INGD recovers the KFAC method" (Section 3.1), yet the actual correspondence is neither derived nor even written as equations. For a paper whose title and abstract foreground the KFAC connection, this is a major gap — the claimed theoretical bridge is simply not on the page.

- **The experimental evaluation is too thin to support the paper's claims.** The experiments consist of a single figure (Figure 5) showing test error curves. There are: no quantitative tables of final test errors, no error bars or multiple seeds, no training loss curves, no hyperparameter ranges or tuning details beyond a mention of random search, no wall-clock timing, and no comparison to SGD (despite the paper claiming SGD is "best for convolution-based models" in the introduction while testing a CNN model, Rep-ViT). The comparison includes only KFAC (second-order) and AdamW (first-order); no other memory-efficient second-order methods (e.g., Shampoo, SKFAC) are included to contextualize SINGD's claimed advantage. The paper claims SINGD is for "large neural nets" (title, abstract, Section 1), but the largest model tested is a compact vision model on CIFAR-100 (32×32 images) or ImageWoof-10. There are no experiments at the scale where memory and stability would be binding constraints (e.g., ImageNet-1K with ResNet-50, or a language modeling task).

- **The method is underspecified and not reproducible from the text.** There is no algorithmic pseudocode. Section 3.2 describes the subspace projection approach at a conceptual level ("we construct a new local reparameterization map... where map Π̂_K projects dense input m_K onto a subspace") but does not give concrete update equations, explain how the truncated matrix exponential is computed in practice, specify how the hierarchical structure is instantiated (rank k, number of blocks), or detail how the gradient N is obtained in the subspace. The hierarchical structure in Table 1 is defined only by a caption that says "replacing the diagonal matrix D_22... with another rank-k triangular matrix," which is not a precise algorithmic specification. A reader familiar with INGD (Lin et al., 2023) could infer the base algorithm, but the novel parts (structured projections, IKFAC variant) are not specified sufficiently for independent implementation.

### Minor

- **The numerical stability claim is supported by only anecdotal evidence.** Figure 5 shows KFAC diverging in one configuration, but there is no investigation of whether the divergence is due to a specific hyperparameter choice, no variation of damping/learning rate for KFAC, and no comparison to KFAC implementations that handle precision carefully (e.g., using double-precision for inverses). The paper attributes KFAC's instability to low-precision inversion, which is plausible, but does not isolate this cause experimentally.

- **Memory measurements are given in the introduction (Figure 1 for VGG) but not quantitatively tied to the models in Section 4.** Tables 2 and 3 are referenced but are not visible in the extracted text (they appear to exist as images); if they contain memory and timing data for the Section 4 models, that would partially address this point, but the connection between Figure 1 and the main experiments is left implicit.

### Trivial
None.

## Nice-to-Haves

- Including SGD as a baseline would strengthen the comparison, especially since the paper singles out SGD as best for convolutions yet does not compare against it when evaluating the CNN model (Rep-ViT).
- An ablation study comparing different sparse structures (diagonal, block-diagonal, triangular, hierarchical) on a single model with memory/accuracy trade-off numbers would help validate the design choices.

## Removed Points

- **Criticisms about missing code release, missing appendix content, or unverifiable claims about future open-sourcing** — removed per policy (parser artifacts and reproducibility nitpicks).
- **Criticism that no other second-order methods (Shampoo, M-FAC, SKFAC) are compared** — weakened to nice-to-have; the paper's scope is specifically inverse-free KFAC variants, and while additional baselines would strengthen the evaluation, their absence is not a fatal flaw.
- **Criticism about Section 2 being too long** — removed as a style nitpick.
- **Strength about "theoretical unification of INGD and KFAC"** — removed because it conflicts with the verified weakness that the theorem and derivation are not actually provided in the paper.
- **Strength about "broad architectural applicability"** — retained but weakened to reflect the limited scale of the experiments.

## Novel Insights

None beyond the paper's own contributions. The two reviewers' perspectives are largely concordant: both recognize the potential of the approach, while noting that the incomplete theoretical substantiation and thin experimental evaluation prevent the paper from meeting its stated claims.

## Suggestions

1. **Provide the missing Theorem 1** — give a clear statement and proof of the equivalence between IKFAC and KFAC (or specify the conditions under which they coincide). Alternatively, if the connection is more approximate than exact, state this honestly and characterize the approximation error.
2. **Add algorithmic pseudocode** for both IKFAC and SINGD (including the structured projection step and matrix exponential truncation) so the method is reproducible.
3. **Strengthen the experiments substantially:** report final test errors in a table with multiple seeds and standard deviations; include training loss curves; measure and report memory and wall-clock time for all optimizers on the models tested; include SGD as a baseline; and run at least one experiment at moderate scale (e.g., ResNet-50 on ImageNet-1K or a GPT-2-scale language model) to substantiate the "large neural nets" framing.
4. **Precisely specify the hierarchical structure used in experiments** — what rank k, how many blocks, how the projection is computed operationally.

## Score and Decision

MY FINAL SCORE: <score>3.0</score>
MY FINAL DECISION: <decision>Reject</decision>