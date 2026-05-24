Now I have a thorough picture of the paper and the anchors. Let me synthesize.

**Round 1 Bracket**: Based on the anchors, the paper clearly sits in the **5.5–7.0** range. The most relevant comparators are EGraFFBench (6.00, Reject) and the Distribution Shifts for MLFFs paper (6.25, Reject). GMD-25 is a pure benchmark paper, similar to EGraFFBench, with a more principled compositional-generalization framing but some methodological gaps.

**Round 2 Narrowing**: Within the bracket, GMD-25 is clearly stronger than GDL-DS (5.67) — which had a problematic causal framework and unfair experiments — and comparable to EGraFFBench (6.00). It is weaker than the Distribution Shifts paper (6.25), which offered mitigation methods in addition to diagnosis, and weaker than AU-GOOD (6.67, Accept), which contributed a novel evaluation metric. GMD-25's principled task design gives it an edge over EGraFFBench, but the solvability concern (Major) pulls it back. I place it at **6.0**.

---

## Summary

This paper introduces GMD-25, a benchmark designed to test compositional generalization in Machine Learning Force Fields (MLFFs) through four carefully constructed tasks: length extrapolation, functional group composition, functional group duplication, and functional group combination. Each task forces models trained on one set of molecules to predict energies and forces for molecules that recombine seen chemical motifs in novel ways. The authors evaluate five state-of-the-art MLFF architectures (SchNet, PAINN, DimeNet++, GemNet, EquiFormerV2) and find consistent, large generalization gaps — OOD errors are often one to two orders of magnitude higher than ID errors — demonstrating that strong ID performance does not guarantee compositional reliability.

## Strengths

- **Principled benchmark design grounded in compositional generalization theory.** The four tasks systematically operationalize length generalization and systematicity (Section 3.1, Figure 1), requiring models to recombine seen components (chain lengths, functional groups) in unseen configurations. This controlled setup isolates generalization failures invisible in standard same-molecule benchmarks.

- **Comprehensive and consistent empirical findings.** All five models show substantial degradation across all four tasks (Section 4.3, Figures 2–4), with OOD errors reaching two orders of magnitude above ID errors in cases like Functional Group Duplication (Figure 4e). The finding that the best ID performer (e.g., EquiFormerV2) is sometimes the worst OOD performer for energy predictions (Figure 2a) is a genuinely informative result that underscores the benchmark's diagnostic value.

- **Rigorous experimental protocol.** The use of Bayesian hyperparameter optimization over ID data for each model (Section 4.2) ensures the observed OOD degradation is not an artifact of poor tuning. The FlashMD + GFN2-xTB pipeline (Section 3.2) provides a reproducible, extensible workflow for trajectory generation.

- **Broad model coverage.** The evaluation spans five distinct architectural families — invariant GNNs (SchNet), equivariant message-passing (PAINN), angle-aware models (DimeNet++, GemNet), and transformer-based equivariant architectures (EquiFormerV2) — providing a representative picture of the current MLFF landscape.

## Weaknesses

### Fatal

None.

### Major

- **Task solvability is not established.** The paper's central interpretive claim is that the benchmark tasks measure whether MLFFs capture underlying physical principles rather than interpolating training data. For this to hold, it must be plausible that a model with perfect compositional reasoning *could* succeed given the training data. For the length-extrapolation task this is intuitively reasonable, but for functional-group composition (aldehyde + alcohol → carboxylic acid) and duplication (mono- → di-acid), the assumption that properties are additively transferable across groups is a strong physical claim. Electronic interactions in test molecules may differ qualitatively from those in training fragments. Without a simple baseline — e.g., an additive model summing fragment contributions, or a classical force field with transferable parameters — the reader cannot distinguish whether model failures reflect a lack of compositional generalization or whether the tasks are fundamentally unsolvable from the provided training data. This weakens the diagnostic interpretation of all results in Sections 4.3 and 5. The paper acknowledges the challenge in passing ("we do not expect the model to learn the chemical reaction pathway") but provides no experimental evidence to support the solvability assumption itself.

### Minor

- **Error magnitudes lack chemical-accuracy context.** The paper describes OOD errors as "orders of magnitude higher" than ID errors and concludes models face "fundamental challenges," but never contextualizes whether the absolute OOD error values (e.g., ~0.1 eV in energy for Length Extrapolation OOD, Figure 2a) are practically acceptable or prohibitive. A brief discussion referencing standard chemical-accuracy thresholds (~1 kcal/mol ≈ 0.043 eV) would substantially strengthen the conclusions.

- **No statistical variance reported.** The paper uses secondary trajectories for ID test sets but reports results as single-point MAE values without error bars or discussion of trajectory-to-trajectory variance. Given that each trajectory contains ~2000 snapshots, reporting the variability across the two held-out trajectories per molecule would clarify whether reported differences between models are reliable.

- **Hyperparameter tuning scope unclear.** Section 4.2 states Bayesian optimization was used to maximize ID performance "within our computational allowance," but does not specify whether models were tuned independently per task or with a single hyperparameter set across all tasks. If a single set was used, some architectures may have been disadvantaged on specific tasks, affecting model rankings.

- **Imprecise terminology for functional-group composition tasks.** The text introduces "complex carbonyls" and "complex alcohol" molecules (Section 3.1, Task 2) as training-set components without defining their chemical structures. While detailed molecule lists presumably appear in the stripped appendix, the main text would benefit from at least a brief structural characterization so readers can verify the logic of the compositional splits.

### Trivial

- The "augmented" variant of Length Extrapolation is described as a sub-type of length extrapolation, but is more accurately a length × functional-group combination task. Clarifying the naming or restructuring the presentation would reduce potential reader confusion.

## Nice-to-Haves

- Add a simple additive or classical-force-field baseline to demonstrate (or test) whether the OOD tasks are solvable in principle. This would simultaneously calibrate the benchmark's difficulty and strengthen the interpretive claim.

- Overlay chemical-accuracy threshold lines (e.g., 1 kcal/mol for energy, 1 kcal/mol/Å for forces) on the MAE plots to help readers gauge practical significance.

- Decompose force errors by atom type (hydrogen, backbone carbon, functional-group atoms) to reveal whether models fail uniformly or at specific interaction sites — this would enhance the benchmark's diagnostic value.

- Provide a brief hypothesis or analysis of why EquiFormerV2's energy predictions degrade so dramatically in the OOD region despite strong force performance (Figure 2).

## Removed Points

These points were flagged for removal, with justification:

- *"The paper does not discuss that standard MD datasets like MD17 and MD22 are often used with scaffold-based splits"* — This is a reviewer-side observation about what the paper could additionally discuss, not a flaw in what the paper actually does. The paper's focus is on compositional generalization, and it adequately contrasts GMD-25 with existing benchmarks in Section 2.3.

- *"The NLP connection in Section 2.2 is tangential"* — The compositional generalization literature originates substantially in NLP; the paper uses this connection to motivate and frame its tasks in a principled way. The section is brief and functional.

- *"The appendix supposedly contains additional force metrics; in the stripped version we cannot verify their informativeness"* — This references content the parser stripped from the review copy. Appendix content exists in the original submission and cannot be evaluated here.

- *"A table of SMILES or chemical formulas is essential for reproducibility and should be in the main paper"* — The paper explicitly states that detailed dataset information appears in the appendix. Demanding main-text inclusion of appendix-level detail is a presentation preference, not a substantive weakness.

## Novel Insights

The paper's most distinctive insight is the observation that strong ID force prediction does not translate to strong OOD *energy* prediction — EquiFormerV2 achieves the best OOD forces but the worst OOD energies in Length Extrapolation (Figure 2), while SchNet and DimeNet++ show the reverse pattern. This systematic decoupling between force and energy generalization suggests that current MLFF training objectives and architectures may optimize for different aspects of the potential energy surface in ways that do not transfer compositionally. This is a genuinely novel diagnostic finding that goes beyond the expected "OOD is hard" narrative.

## Suggestions

- The most impactful revision would be to include a solvability baseline (e.g., an additive fragment model or a classical force field with bond increments) for each task. Even a partial demonstration that a simple model can achieve non-trivial OOD performance would substantially strengthen the paper's central claim and improve the benchmark's diagnostic power.

- Clarify whether hyperparameters were tuned per-task or globally, and if globally, discuss whether this could affect model rankings.

- Add a short paragraph contextualizing the observed error magnitudes against standard chemical-accuracy thresholds.

## Score and Decision

**Anchor comparison summary:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| EGraFFBench (NvJxTjTQtq) | 6.00 | R1/R2 | Most similar: pure MLFF benchmark. GMD-25 has more principled task design but similar methodological gaps. Comparable quality. |
| Distribution Shifts for MLFFs (Xk9Q0CrJQc) | 6.25 | R1/R2 | Stronger: offers mitigation methods beyond diagnosis. GMD-25 is benchmark-only. |
| GDL-DS (LixGd92Wri) | 5.67 | R2 | Weaker: problematic causal framework, unfair experimental setting. GMD-25 is clearly stronger. |
| AU-GOOD framework (qFZnAC4GHR) | 6.67 | R1 | Stronger: novel metric contribution with methodological depth. GMD-25 is a pure benchmark. |
| Molecular Conformer Ensembles (NSDszJ2uIV) | 6.33 | R2 | Slightly stronger: first-of-its-kind benchmark for a specific problem. |
| LiFlow (CkozFajtKq) | 6.33 | R2 | Different category: generative method paper. Not directly comparable. |
| Pushing Limits All-Atom Geom-GNNs (4S2L519nIX) | 6.50 | R2 | Stronger: pre-training + transfer contribution beyond benchmarking. |

**Round 1 bracket**: 5.5–7.0. **Round 2 narrowing**: GMD-25 is clearly above the 5.67 anchor and comparable to the 6.00 anchor. It is below the 6.25+ anchors. **Final placement**: 6.0.

The paper is a well-constructed benchmark with principled task design and informative empirical findings. The Major weakness — unestablished task solvability — is fixable but currently undermines the central interpretive claim. In a competitive venue, a pure benchmark paper needs to be airtight on its own terms; the solvability gap prevents that.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Reject</decision>