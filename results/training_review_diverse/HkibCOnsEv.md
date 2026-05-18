Now I have a thorough understanding of the paper and can verify each claim against the actual content. Let me construct the final consolidated review.

---

## Summary

This paper extends the inverse-free natural gradient descent (INGD) method to produce memory-efficient and numerically-stable second-order optimization. It proposes (i) IKFAC, an inverse-free variant claimed to recover KFAC updates, and (ii) SINGD, which imposes structured sparsity (diagonal, triangular, hierarchical) on the Kronecker factors to reduce memory. Experiments on small-to-medium vision models (VGG, Compact-ViT, Swin-ViT, GC-ViT, Rep-ViT) show that SINGD achieves memory comparable to AdamW while maintaining numerical stability in half-precision, unlike KFAC which diverges.

## Strengths

1. **Numerical stability in low precision is clearly demonstrated.** Figure 1 (left/center) shows that IKFAC and SINGD remain stable in both FP-32 and FP-16 on a VGG net, while KFAC diverges in FP-16 due to matrix inversion instability. This directly supports the paper's central claim about robustness.

2. **Memory efficiency of structured Kronecker factors is empirically shown.** Figure 1 (right) demonstrates that SINGD-Diag in FP-16 approaches AdamW's memory footprint (dashed line), while INGD and KFAC require substantially more memory. This validates the core memory-efficiency contribution.

3. **Works on modern vision transformer architectures.** Figure 5 shows SINGD (hierarchical structure) achieving competitive test error on Compact-ViT, Swin-ViT, GC-ViT, and Rep-ViT in mixed-precision (BFloat16) training, extending INGD beyond its original convolution-only scope.

4. **Flexible structured Kronecker factor design.** The paper proposes multiple sparsity patterns (Table 1: diagonal, triangular, hierarchical, block-diagonal) with concrete subspace projection maps, using Lie-algebraic properties to maintain closedness under required matrix operations. This provides a principled framework for trading off memory and expressiveness.

## Weaknesses

### Fatal
None.

### Major

1. **The IKFAC–KFAC theoretical connection is asserted but not demonstrated in the main text.** Section 3.1 consists of a single paragraph of prose and a figure caption. The paper states "IKFAC corresponds to a specific setting of the INGD method" and "IKFAC behaves like KFAC (Theorem 1)," but no equations, derivation, or even a sketch of the correspondence appear in the main text. Theorem 1 is referenced only in passing in Figure 2's caption — the theorem statement itself is absent. While the full proof may reside in the appendix (stripped by the parser), the main text should at minimum provide a concrete outline of how IKFAC recovers KFAC. Without this, the paper's most novel theoretical contribution is unverifiable from the main manuscript alone. The empirical results (Figures 1 and 5) show IKFAC performs similarly to KFAC, which is correlational evidence but not a theoretical demonstration.

2. **Empirical validation does not match the title's scope of "Large Neural Nets."** The experiments are limited to small vision models (VGG) and compact vision transformers (Compact-ViT, Swin-ViT, GC-ViT, Rep-ViT) on small datasets (CIFAR-100, ImageWoof-10). The paper does not report model parameter counts, does not test any model above approximately 100M parameters, and conducts zero experiments on NLP or sequence-modeling tasks (e.g., GPT-2-scale or BERT-scale models). Given that the title and abstract explicitly promise a method for "large neural nets" and "transformer-based models," and the introduction cites billion-parameter language models as motivation, this gap between promise and validation is substantial. The paper's claim that SINGD "reliably train[s] both architectures" (CNNs and transformers) is overstated when only compact vision transformers on small datasets are tested.

### Minor

3. **Notation is dense and the MLE/Bayesian exposition is hard to follow.** The paper shifts between the MLE perspective (Section 2.1, KFAC) and the Bayesian variational inference perspective (Section 2.2, INGD/IKFAC) without clearly delineating for each equation which setting applies. Readers unfamiliar with Lin et al. (2023) and the Bayesian learning rule will struggle to understand what is being modified and why.

4. **"Riemannian momentum" is mentioned but never defined.** The term appears in Figure 1's caption and Section 2.2 ("it becomes a (Euclidean) gradient step, which makes it easy to add Riemannian momentum into A"), but the paper does not explain what it is, how it works, or why IKFAC omits it. This matters because the difference between IKFAC and INGD (and thus the relationship to KFAC) includes this momentum.

5. **KFAC's numerical instability in transformer experiments is stated qualitatively.** Figure 5's caption says "KFAC performs unstably," but no quantitative stability metrics (e.g., gradient norm statistics, divergence rates) are provided for the transformer experiments. The detailed stability demonstration (Figure 1 left/center) is only on a small VGG net.

6. **No ablation of the different structure designs' performance trade-offs.** Section 3.2 describes a general design principle with multiple structures (diagonal, triangular, hierarchical, block-diagonal), but the main text experiments only compare a subset. The paper would be strengthened by systematically showing how different structures lead to different memory-performance trade-offs, as claimed.

7. **No analysis of computational overhead.** The cost of computing subspace projections and the truncated matrix exponential is not characterized in the main text. For a method claiming practical utility, understanding this overhead is important.

### Trivial

- Model parameter counts are not reported for any architecture, making it hard to gauge the scale of the experiments relative to the paper's claims.
- The experiments section (Section 4) is unusually brief and reads more like a placeholder description than a detailed empirical study.

## Nice-to-Haves

- A concrete derivation (even a brief sketch) in Section 3.1 showing which specific parameter settings of INGD produce the KFAC update, so the theoretical bridge is self-contained in the main text.
- At least one medium-scale experiment on a language modeling task (e.g., GPT-2 125M or a moderate BERT variant) to substantiate the claim of relevance to transformer-based NLP training.
- Quantitative stability metrics (e.g., gradient variance, loss smoothness) for the KFAC instability episodes shown in Figure 5.

## Removed Points

- **Memory tables (Tables 2, 3) absent from main text**: These tables are referenced in the paper and likely reside in the appendix, which the parser strips. Per instructions, this is not a valid weakness.
- **Missing related works**: Per instructions, we do not assert missing citations without external verification.
- **Criticism that "the curves are not shown in the text" for KFAC instability in transformer experiments**: The curves ARE shown in Figure 5 (the caption states "KFAC performs unstably"). The critic's characterization is factually incorrect on this point.
- **The claim that the paper's contribution is "unverified" on theoretical grounds**: The full proof likely appears in the appendix. The weakness retained above is about the main text's thinness, not the existence of the proof.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a recurring tension: the paper's technical contributions (inverse-free KFAC updates, structured Kronecker factors via Lie-algebraic subspaces) are genuinely interesting, but the validation covers only a narrow slice of the "large neural nets" promised in the title, creating a credibility gap that neither the strengths nor weaknesses fully resolve.

## Suggestions

1. Expand the theoretical exposition in Section 3.1: provide concrete equations or a lemma showing the IKFAC-KFAC correspondence, even if the full proof is deferred to the appendix.
2. Either add experiments on larger-scale models (including at least one NLP transformer), or temper the title/abstract claims to match the actual experimental scope (e.g., "for Vision Transformers and CNNs").
3. Include model parameter counts for all tested architectures.
4. Add quantitative stability metrics (e.g., gradient norm tracking) for the KFAC instability claims.
5. Provide an ablation table comparing the downstream performance of different structure designs (diagonal vs. triangular vs. hierarchical vs. block-diagonal) across multiple models.

## Score and Decision

The paper proposes a sensible and potentially valuable extension to INGD, with clear empirical demonstrations of numerical stability and memory savings on vision models. However, the theoretical bridge to KFAC is not substantiated in the main text, and the empirical scope falls well short of the "large neural nets" promised by the title. The core contributions are real but incomplete as presented.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>