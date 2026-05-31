Now I have a clear picture. Let me compile the final review.

---

## Summary

This paper proposes SurfDesign, a framework for surface-conditioned protein inverse folding. The authors claim two core technical contributions: (1) surface-based equivariant message passing (SEMP) that incorporates manifold-aware geometric features (normals, curvatures) into a neural network, and (2) a hybrid parameter-efficient fine-tuning (PEFT) technique that integrates pretrained protein language models with the surface geometric encoder. The paper reports state-of-the-art sequence recovery on CATH, TS50, TS500, and PDB benchmarks.

## Strengths

- **Surface geometric feature computation**: The method section (2.2) provides a well-motivated theoretical framing of molecular surfaces as continuous manifolds, and describes the computation of tangent-space normals (from PyMol) and pseudo-curvatures (from local covariance eigendecomposition, Eq. 1–4). This geometric feature extraction is concrete and verifiable from the paper.

- **Structural context analysis (Figure 4)**: The paper analyzes performance by residue structural context (SASA, interaction interface) and shows that SurfDesign improves recovery specifically on surface and loop regions compared to structure-based methods like LM-Design. This analysis directly supports the claim that surface conditioning provides a benefit beyond backbone-only methods.

- **Strong claimed benchmark performance**: If the reported numbers are valid, SurfDesign achieves 74.13% recovery on CATH 4.2, 82.16% on TS50, and 81% on the PDB multi-chain set (Tables 1–4), substantially exceeding prior methods. The paper also evaluates zero-shot generalization on TS50/TS500 (Table 4) and reports consistency across multiple benchmarks.

## Weaknesses

### Fatal

- **The core technical contributions are not described.** The paper claims two primary innovations — surface-based equivariant message passing (SEMP) and a hybrid PEFT technique for PLM integration — but neither is specified in the method section.

  - **SEMP**: The term appears only in the abstract (line 5) and introduction (line 20). The method section (Section 2, lines 35–72) describes surface generation, denoising, normal vectors, Darboux frames, and pseudo-curvature computation, but provides *no equations or architectural description of the message passing mechanism itself*: no message function, no node/edge update rule, no equivariance property or proof, no network layers, no aggregation scheme. The paper simply states that these geometric quantities are computed and then jumps to experiments.

  - **Hybrid PEFT**: Mentioned as a key contribution in the abstract and introduction, but *never discussed in the method section at all*. The Figure 2 caption references a "structural adapter of the protein language models," but the text provides zero information about what this adapter is, how it works, its parameter count, at what layer PLM features are injected, or how the surface encoder and PLM are combined.

  Without these descriptions, the paper's central claims are unverifiable and the method is unreproducible. This is not a missing appendix or supplementary detail — it is a gap in the main exposition of the paper's contributions.

### Major

- **Evaluation does not match the stated motivation.** The introduction motivates surface-conditioned design as a path to *functional* proteins by incorporating biochemical properties (charge, hydrophobicity) that backbone-only methods miss. Yet the primary evaluation (Tables 1–4) is standard inverse-folding sequence recovery on CATH/TS50/TS500/PDB, where the ground-truth sequence is conditioned on the backbone structure, not on functional surface properties. The paper does not study any downstream functional task (binding affinity, enzymatic activity, antibody-antigen interaction). The paper's own framing ("opens another road to designing functional proteins") is not supported by the evidence presented.

- **Unclear baseline comparison setup.** The paper reports very large improvements over prior methods (e.g., 18.28% relative improvement over VFN-IF-ESM on CATH 4.2). However, it does not state whether these baselines were re-run under identical conditions (same PLM, same splits, same training pipeline) or whether the numbers are simply cited from prior publications. Without a controlled comparison, the reader cannot attribute the gains to the proposed method versus differences in implementation, compute budget, or PLM choice. (The paper does state data splits used, but this is insufficient to establish a controlled comparison.)

- **Ablation study is vaguely described.** The ablation discussion (Section 3.4) reports that PLMs contribute 13.43% relative improvement and curvatures/directionality contribute 11.86%, but does not specify the exact configurations being compared (e.g., what is the base model without PLM? What is the base model without curvatures? Are these cumulative or independent ablations?). The reader cannot verify that the ablations are properly controlled.

### Minor

- **Pseudo-curvatures ψ are computed but never connected to the network.** The method section derives three pseudo-curvature vectors ψ_i (Eq. 3–4) and states that they approximate the Darboux frame, but does not specify how ψ_i enters the message-passing computation (e.g., as edge features, node features, or attention biases). This leaves a gap between the feature computation and the network architecture.

- **The claimed equivariance property is asserted but not explained.** The paper uses the term "equivariant" in the method name (SEMP) and criticizes dMaSIF for destroying equivariance (line 58), but provides no definition of what equivariance means in this context, how SEMP achieves it, or any analysis/verification of this property.

### Trivial

- Line 92 reads "SurfDock is the foremost to exceed 70% recovery" — should be "SurfDesign." This appears to be a typographical error.

## Nice-to-Haves

- Provide training details (learning rate, batch size, optimizer, number of epochs, GPU hours, total parameter count).
- Report statistical significance or variance across runs for the main results.
- Discuss limitations and failure cases (e.g., scenarios where surface conditioning may hurt, such as buried residues).
- Report diversity metrics for generated sequences; the paper acknowledges that surface-conditioned design is underdetermined but does not evaluate sequence diversity.

## Removed Points

- *Criticism about tables being garbled in the parsed version* — This is a PDF parsing artifact, not a paper deficiency.
- *Criticism that the paper claims 70% on PDB while PDB recovery is >80%* — The claim is about exceeding 70% on *all* benchmarks, not that the recovery is exactly 70% on PDB. This misreads the statement.
- *Criticism about missing appendix content / missing proofs* — The parser strips these; they may exist in the original submission.
- *Strength Finder claim that "SEMP" and "hybrid PEFT" are described as technical contributions* — These are named but not technically described in the method section; the strength is unsupported by the paper content.
- *Strength Finder claim about "scaling law with PLM size" being a unique contribution* — This is a standard and expected phenomenon shown in prior work; not specific to SurfDesign.
- *Strength Finder's generic formulation of strengths about problem importance* — These are generic and lack specific evidence from the paper.

## Novel Insights

Beyond the paper's own contributions, the reviews surface two observations. First, the structural context analysis (Figure 4) is the most concrete evidence that surface conditioning provides a meaningful advantage over backbone-only methods — it directly shows improvement on surface and loop residues where backbone geometry alone is less informative. Second, the near-total absence of method specification combined with very large reported improvements creates an asymmetry that should be resolved by either a complete architectural description or a more measured presentation of results. Neither observation changes the paper's primary deficiency.

## Suggestions

1. **Provide a full architectural description of SEMP.** Include the message function, node/edge update equations, the equivariant mechanism (if any), network layers, and how the geometric features (normals, pseudo-curvatures) are integrated into the computation. This is the minimum requirement for the paper to be evaluable.

2. **Describe the hybrid PEFT technique.** Specify what adapter architecture is used, how the surface encoder and PLM are combined, at what stage in the network the PLM features are injected, the number of trainable parameters, and the training procedure.

3. **Re-run or clarify baseline comparisons.** Either report results from re-running all compared methods under identical conditions, or clearly indicate which numbers are cited and acknowledge the limitations of cross-paper comparisons. Report variance across runs.

4. **Align the evaluation with the stated motivation.** Either include a downstream functional task (binding prediction, enzymatic activity) to support the "functional design" claim, or reframe the paper's contribution as a geometric representation improvement for inverse folding and present the results accordingly.

---

MY FINAL SCORE: <score>2.5</score>
MY FINAL DECISION: <decision>Reject</decision>