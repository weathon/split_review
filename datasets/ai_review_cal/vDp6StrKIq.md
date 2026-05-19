- Decision: Accept
- Avg Score: 6.33
- Scores: 5, 8, 6
Now I have all the evidence I need. Let me write the consolidated review.

---

## Summary

This paper introduces a framework for O(d)-equivariant message passing that combines local canonicalization (equivariant local reference frames) with **tensorial messages** — transforming geometric node features between local frames via the change-of-basis matrix \(R_i R_j^{-1}\). This is a strict generalization of prior local-canonicalization methods that only communicate scalar (invariant) features. The authors adapt PointNet++ using this framework, achieving state-of-the-art results on normal vector regression (0.949 cosine similarity) and competitive results on segmentation/classification, with ablations showing that tensorial messages dominate the improvement even when local frames are random.

## Strengths

- **Tensorial messages outperform scalar messages, both with learned and random frames (Table 3).** The variant with tensorial messages + random frames achieves 0.920 cosine similarity vs. 0.901 with learned frames + scalar messages. This cleanly isolates the core claim — consistent communication of geometric features — from frame quality.

- **State-of-the-art on normal vector regression (Table 1).** The equivariant PointNet++ adaptation achieves 0.949 cosine similarity, substantially ahead of prior methods (e.g., EPN at 0.917, the scalar-message baseline at 0.930). This directly supports the practical value of the framework.

- **Fair head-to-head comparison against data augmentation (Tables 1–2).** The paper provides a direct, hyperparameter-matched comparison between built-in equivariance and data augmentation (0.949 vs. 0.884 on normal regression, 0.864 vs. 0.822 on segmentation). Most equivariant works omit such a comparison; Section 4.3 explains the insight that equating all local frames to a random global rotation reproduces data augmentation.

- **Rigorous mathematical grounding.** Equations (9)–(10) provide clear index-notation proofs of invariance of locally-expressed features and equivariance of the output for arbitrary representations. The formulation in Eq. (12) cleanly generalizes scalar-only local canonicalization.

- **Data efficiency analysis (Figure 4).** The steeper scaling-law slope for the equivariant model vs. data augmentation provides concrete evidence that built-in equivariance improves sample efficiency. The honest observation that data augmentation can match equivariance at smaller dataset sizes adds nuance.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **"Without restrictions" in the abstract is slightly overstated.** The abstract claims the framework "can be integrated with any architecture without restrictions." In practice, using tensorial messages requires splitting features into scalar/vector/tensor channel groups and applying the appropriate transformation (\(R_i R_j^{-1}\)) — the architecture must be modified to interpret certain channels as geometric tensor components. This is *straightforward* but not *completely free of restrictions*; a scalar-only architecture that treats every channel independently would need non-trivial modification. This framing gap does not diminish the contribution but should be tightened.

2. **Degenerate Gram-Schmidt case not discussed.** Section 4.1 predicts two vectors \(\mathbf{v}_{i,1}, \mathbf{v}_{i,2}\) and applies Gram-Schmidt. If these two vectors are collinear (or nearly so), the procedure fails or produces an unstable frame. The paper provides no fallback or regularization strategy (e.g., a small perturbation or alternative mechanism). While learned networks rarely produce exactly collinear outputs in practice, this gap affects reproducibility for potential adopters.

3. **Computational overhead not quantified.** The paper uses Einstein summation for tensor transformations (Eq. 12) but reports no runtime comparison against the scalar-message or data-augmentation baselines. This information would help potential adopters assess the practical cost of the additional expressivity, especially in resource-constrained settings.

### Trivial
None.

## Nice-to-Haves

- A comparison against native equivariant architectures (e.g., EGNN, SE(3)-Transformer) on normal regression would provide additional context, even though the paper's primary claim is about adapting *non-equivariant* architectures.
- The numerical values from Figure 4 (data efficiency plot) could be reported in the text for precise reference.
- Explicitly stating the exact tensor/pseudotensor decomposition used for \(\rho_{\mathrm{f}}\) in the main text (e.g., "1 scalar + 1 vector + 1 pseudoscalar") would improve reproducibility without requiring readers to consult the appendix.

## Removed Points

These points are flagged to be removed — treat them with caution if considering:

- **Refinement MLP "sixth number" not explained** (Harsh Critic): The paper states the vectors are used "by the Gram-Schmidt procedure **similar to Sec. 4.1**." Section 4.1 fully explains that Gram-Schmidt on two vectors yields two orthonormal vectors, and the third is obtained from the cross product. The specification is adequate. *(Reason: point is factually incorrect / already addressed.)*
- **Missing \(\rho_{\mathrm{f}}\) specification** (Harsh Critic): The paper says "see App. A" for the direct-sum decomposition. The appendix is stripped by the parser; it exists in the original submission. *(Reason: removed per rule about missing appendix content — parser artifact, not author omission.)*
- **Various formatting/typo criticisms**: The extracted text contains artifacts (e.g., line 206–207 showing a block of numbers). These are parser errors, not paper problems. *(Reason: parser-induced, not author errors.)*

## Novel Insights

A genuinely novel observation emerging from considering the two reviews together: the paper's framework enables a uniquely fair empirical comparison between built-in equivariance and data augmentation by treating global data augmentation as the special case where all local frames equal the same random rotation (Section 4.3). This conceptual bridge — rarely exploited in the equivariance literature — allows the paper to demonstrate that built-in equivariance provides better data efficiency (steeper scaling slope in Figure 4) while also honestly reporting that data augmentation can sometimes match it on small-data regimes. The combination of the "without restrictions" framing gap (Minor weakness 1) and the strong empirical results suggests the paper could be strengthened by reframing its claim as "any architecture *whose features can be partitioned into geometric representations*" rather than "any architecture without restrictions."

## Suggestions

1. Add a brief sentence in Section 4.1 addressing the degenerate frame case (e.g., "we add a small isotropic Gaussian perturbation to the predicted weights before Gram-Schmidt to ensure stability").
2. Report per-epoch runtime for the tensorial-message model vs. the scalar-message baseline.
3. Tighten the abstract's phrasing from "without restrictions" to something like "with minimal architectural modifications" or "without requiring specialized equivariant building blocks."
4. State the exact decomposition used for \(\rho_{\mathrm{f}}\) in the experiments directly in the main paper, even briefly.

---
