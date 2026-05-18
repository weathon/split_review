Now I have all the information I need. Let me produce the final consolidated review.

## Summary

This paper introduces a framework for O(d)-equivariant message passing based on local canonicalization, where the key innovation is using **tensorial messages** — node features that transform as vectors, tensors, and pseudotensors between local frames — rather than the scalar-only messages used in prior local-canonicalization methods. The authors prove that this strictly generalizes prior approaches, demonstrate it by adapting PointNet++ into an equivariant architecture, and report strong results on normal vector regression (0.961 cosine similarity on ModelNet40, outperforming prior methods), competitive results on ShapeNet segmentation, and a controlled comparison showing better data efficiency than data augmentation.

## Strengths

1. **Novel and principled tensorial message passing formalism**: The paper identifies a genuine limitation of prior local-canonicalization work (scalar messages lose directional information, illustrated in Fig. 1) and provides a mathematically clean solution: transforming features between local frames via tensor/pseudotensor representations (Eq. 12). The invariance proof (Eq. 13) and the handling of reflections (Eq. 5) are clear and self-contained.

2. **Strong empirical results on normal vector regression**: The equivariant PointNet++ adaptation achieves 0.961 cosine similarity on ModelNet40 (Table 1), outperforming prior methods including Luo et al. (2022) at 0.953. This is a task where precise directional information is critical, directly validating the benefit of tensorial messages.

3. **Strict generalization over scalar message passing is convincingly demonstrated**: Table 3 shows that tensorial messages significantly outperform scalar messages even with *random* local frames (0.964 vs. 0.851 with learned frames), confirming that the improvement comes from directional communication, not just better frame prediction.

4. **Fair comparison between equivariance and data augmentation**: The framework naturally degrades to data augmentation when frames are set to a random global rotation (Sec. 4.3), enabling a direct, architecture-controlled comparison that most prior equivariant work cannot provide. Figure 4 shows the equivariant model achieves better data efficiency (steeper scaling slope).

5. **Iterative frame refinement during message passing (Sec. 4.3.1)** is a clean architectural contribution that further improves results (e.g., 0.953 → 0.961 in Table 1), showing that the model can refine geometric understanding as the receptive field grows.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **The SOTA claim on normal vector regression needs qualification.** The paper asserts "state-of-the-art results" (abstract, line 20, Table 1 caption), but the comparison set in Table 1 includes methods with fundamentally different backbone architectures (e.g., Point Transformer, SE(3)-Transformer). While the result (0.961) is genuinely strong and beats all listed methods, the claim should be tempered — e.g., "state-of-the-art among compared methods on this task" or "competitive with state-of-the-art" — since architectural differences (not just equvariant mechanism) contribute to the gap. This does not invalidate the result but aligns the claim with what the evidence supports.

2. **The claim of applicability to "any existing message passing architecture" overreaches.** The introduction (line 5) states the framework "can be integrated with any architecture without restrictions," and the contributions (line 20) claim to "make any existing message passing architecture O(d)-equivariant." The formalism in Eq. (12) covers architectures expressible in a standard message-passing form, but architectures with cross-attention over edge features, dynamic graph structures, or non-standard aggregation schemes may require non-trivial modifications. The paper would be stronger by stating the framework applies to architectures expressible as Eq. (11)/Eq. (12) and acknowledging where limitations may arise.

3. **The data-efficiency experiment (Fig. 4) lacks error bars or confidence intervals.** The paper argues that the equivariant model has a steeper slope (better data efficiency) based on a log-log plot, but no measure of variance is reported. Given that the paper itself notes "the error rate is not necessarily smaller for all dataset sizes," the significance of the slope difference is unclear without uncertainty quantification. This weakens the data-efficiency claim; error bars from multiple runs or bootstrap estimates would strengthen it considerably.

4. **No explicit limitations section.** Important caveats are acknowledged only in passing: reliance on a radius graph and cutoff distance for frame prediction (line 100), possible degenerate frames in symmetric neighborhoods (alluded to in App. D), and the need to manually assign tensor representations (line 155, "one chooses the transformation behavior"). An explicit limitations section discussing these points would improve the paper's credibility and is standard practice in a mature subfield.

5. **Data augmentation baseline description could be clearer.** The paper states that choosing $\tilde{R} \in O(d)$ randomly for every training sample "amounts to data augmentation with random global rotations and reflections" (Sec. 4.3). It is not entirely clear whether this uses the same learned-frame-prediction network with random rotation applied to the input, or whether frame prediction is disabled entirely and frames are set to a random global rotation. A brief clarifying sentence would help reproducibility.

### Trivial

- **Section 4.3.1** ("Refining the Local Frames During Message Passing") is a subsection of Section 4.3 ("Relation to Data Augmentation"), which is structurally odd since frame refinement is an independent architectural contribution, not a sub-topic of data augmentation. This should be a separate subsection at the same level.

## Nice-to-Haves

- **Computational cost comparison**: The paper notes that other equivariant methods can be computationally intensive but does not report runtime or parameter counts for the proposed framework vs. baselines. This would be practically valuable.
- **Ablation isolating representation dimension**: An ablation comparing one vector channel vs. zero vector channels (controlling total capacity) would sharpen the demonstration that improvement comes from directional communication rather than extra parameters.
- **Algorithmic recipe**: A short pseudocode or step-by-step recipe for converting a general message-passing architecture into equivariant form would improve accessibility and reduce the gap between conceptual contribution and practical adoption.

## Removed Points

- **"Implementation of tensor representations for feature channels is underspecified"** (Harsh Critic, Critical Issue 4): The paper explicitly references Appendix A for this detail ("see App. A"). Since the appendix is present in the original submission and only stripped during PDF-to-text extraction, this criticism reflects a parser artifact, not an author omission.
- **"Cross-product and reflective equivariance stability"** (Harsh Critic, Other Observations): The paper references Appendix D for robustness analysis, which exists in the original submission.
- **"ScanObjectNN results should be in main paper"** (Harsh Critic, Missing Parts): The paper references Appendix D for these experiments, which is standard practice for supplementary material.
- **"Missing appendix" / "missing proofs in appendix"** type criticisms: All such points are removed per instructions, as the parser strips these sections.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface an interpretation of the paper's contribution that the authors themselves have not already stated.

## Suggestions

1. Qualify the SOTA claim in the abstract and contributions to match the specific comparison context (e.g., "state-of-the-art among compared methods on this task").
2. Bound the generality claim in the introduction — replace "any architecture without restrictions" with "any architecture expressible as Eq. (11)" and briefly discuss where the framework may need adaptation.
3. Add error bars (or bootstrap confidence intervals) to the data-efficiency plot in Fig. 4, and consider reporting variances for key results in Tables 1–2.
4. Add a brief limitations section (1–2 paragraphs) covering radius-graph dependence, potential frame degeneracy, and the manual assignment of tensor representations.
5. Clarify the data augmentation baseline: specify whether the frame-prediction network is used and whether random rotations are applied to inputs or to frames.
6. Promote Section 4.3.1 to a top-level subsection (e.g., Section 4.4) to reflect that it is an independent architectural contribution.

## Score and Decision

**Score**: 7.5  
**Decision**: Accept

The paper makes a clean, theoretically grounded contribution (tensorial messages between local frames) that addresses a real limitation in the local-canonicalization literature. The experiments are well-designed and support the core claims. The weaknesses identified above are real but minor — they concern framing, presentation, and missing uncertainty quantification, not any flaw in the core method or its validity. With the suggested revisions, the paper would be a solid addition to the conference.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>