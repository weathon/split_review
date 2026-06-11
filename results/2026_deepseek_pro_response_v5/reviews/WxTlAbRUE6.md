Now I have a clear calibration picture. Let me finalize.

**Cross-anchor comparison:**

| Anchor | Score | How GMD-25 compares |
|--------|-------|---------------------|
| MoreRed (rwmWd2rjP1) | 4.75 | GMD-25 is stronger: better motivation, cleaner evaluation, principled task design with theoretical grounding |
| NeuralMD (J4V3lW9hq6) | 5.00 | GMD-25 is comparable but has clearer benchmark contribution |
| Symmetry Discovery (e4PL5zssJ9) | 5.00 | GMD-25 has more concrete empirical contribution |
| **EGraFFBench (NvJxTjTQtq)** | **6.00** | **Most similar anchor. Both are MLFF benchmarks. EGraFFBench has more breadth (8 datasets, new metrics, dynamic sims) but had experimental validity concerns. GMD-25 has more principled task design (COGS-based, augmented variants) but less analysis depth and no statistical characterization.** |
| Distribution Shifts (Xk9Q0CrJQc) | 6.25 | Stronger contribution (proposes methods + benchmarking), but GMD-25 has cleaner benchmark design |
| LiFlow (CkozFajtKq) | 6.33 | Clearly stronger — novel method with thorough evaluation |

GMD-25 lands between the 5.0 cluster and EGraFFBench (6.00). Its principled task design and augmented-variant control are real strengths, but the lack of result analysis, missing statistical characterization, and under-specified methodology hold it below EGraFFBench level. **Final score: 5.5.**

---

## Summary
This paper introduces GMD-25, a benchmark for evaluating compositional generalization in machine learning force fields (MLFFs). The benchmark consists of four tasks — Length Extrapolation, Functional Group Composition, Functional Group Duplication, and Functional Group Combination — systematically testing whether MLFFs can generalize to molecules with different carbon chain lengths or novel functional group arrangements. Five state-of-the-art architectures are evaluated, revealing large generalization gaps (OOD errors often 1–2 orders of magnitude above ID) and rank reversals between ID and OOD performance, demonstrating that current MLFFs fundamentally struggle with compositional generalization.

## Strengths
- **Principled task design grounded in the COGS framework**: The four tasks are derived from the cognitive-science taxonomy of compositional generalization (Hupkes et al., 2020) — length generalization (Task 1) and systematicity (Tasks 2–4) — giving the benchmark a theoretical foundation that prior molecular benchmarks lack (Section 3.1, lines 60–66). The tasks are cleanly specified and test genuinely distinct aspects of generalization.
- **Augmented variant design as a diagnostic control**: For Tasks 1 and 2, the paper introduces augmented training sets that provide explicit demonstrations of the compositional pattern being tested. The finding that all models still fail in the augmented setting (Section 4.3, line 138) strengthens the claim that failures reflect fundamental architectural limitations rather than mere lack of exposure.
- **ID-best ≠ OOD-best: concrete evidence that standard benchmarks mislead model selection**: The results clearly demonstrate rank reversals — EquiFormerV2 achieves the lowest Forces MAE on Length Extrapolation but its Energy MAE degrades to worst-in-class in the OOD region, while SchNet and DimeNet++ maintain stable energy predictions (Section 4.3, lines 134–135; Figure 2). This directly supports the paper's central thesis.
- **Broad and representative model coverage**: Five models spanning invariant GNNs (SchNet), equivariant MPNNs (PAINN), angle-aware models (DimeNet++, GemNet), and equivariant transformers (EquiFormerV2) cover the major architectural design axes in MLFFs (Section 4.1). The deliberate exclusion of foundation models is correctly justified.
- **Reproducible and extensible toolkit**: A complete Python-based workflow for generating AIMD trajectories — from SMILES strings through FlashMD simulation to GFN2-xTB recalculation — yielding 296,534 labeled geometries across 118 molecules (Section 3.2), with plans for open release.

## Weaknesses

### Fatal
None.

### Major
- **Energy-forces dissociation is reported but left unanalyzed**: The paper's most striking empirical finding is the dissociation between energy and force generalization — EquiFormerV2 achieves the best Forces MAE but the worst Energy MAE on OOD data, while SchNet and DimeNet++ show the opposite pattern (lines 134–137, 166–167). This is noted repeatedly but never investigated. For a benchmark paper whose value depends on providing diagnostic insight, cataloging failures without helping readers understand *why* they occur leaves the contribution incomplete. A basic investigation (e.g., examining whether models that derive forces as energy gradients vs. direct outputs show different trade-off patterns) would substantially strengthen the paper.
- **No statistical characterization of results**: All figures and numerical claims report point estimates only. Given that per-task training sets are small (5 molecules for Task 1 base variant) and models can exhibit run-to-run variability, the absence of error bars, standard deviations, or any variance characterization means readers cannot assess whether reported differences between models (e.g., "GemNet overall performs best" for Task 3, line 156) are meaningful or fall within noise. This weakens the comparative claims central to the benchmark's diagnostic purpose.

### Minor
- **Training loss function not stated in the main text**: Section 4.2 describes hyperparameter optimization and evaluation metrics (MAE) but never specifies the training objective — whether models use a joint energy+forces loss, what the relative weighting is, or whether forces are learned as direct outputs or energy gradients. While a weighted sum of energy and force losses is standard in MLFFs, this information is essential for interpreting the energy-forces dissociation finding.
- **GFN2-xTB vs. DFT framing tension**: The introduction (line 13) invokes DFT as the gold-standard reference method, but the benchmark itself uses GFN2-xTB, a semi-empirical method. While the paper notes GFN2-xTB's "balance between computational efficiency and accuracy" (line 56), it does not discuss whether the reference method's own transferability across compositional splits limits what can be concluded about models "learning underlying physical principles."
- **Task 2 chemical framing is imprecise**: The claim that a carboxylic acid (-COOH) "can be seen as a composition" of alcohol (-OH) and aldehyde (-CHO) functional groups (line 72) ignores resonance stabilization between the carbonyl and hydroxyl moieties in -COOH that is absent in the separated fragments. This does not invalidate the task, but treating the compositional decomposition as chemically straightforward when it is not warrants acknowledgment.
- **Small per-task training sets limit diagnostic resolution**: Task 1 base variant uses only 5 training molecules. With such small sets, it is difficult to disentangle whether OOD failures reflect fundamental architectural limitations or insufficient data. A brief discussion of this limitation would strengthen the conclusions.

### Trivial
None.

## Nice-to-Haves
- Investigate the energy-forces trade-off through loss-weight ablation or by comparing gradient-derived vs. direct force prediction.
- Per-atom or per-region error analysis to provide architectural insights beyond aggregate MAE.
- Data-scaling experiments (e.g., subsets of 1, 3, or 5 training molecules) to separate data insufficiency from architectural limitations.
- Error bars or variance characterization where computationally feasible.

## Removed Points
These points are flagged to be removed, treat them with caution:
- **Figure labeling errors ("PBE0" and "m4s")**: These appear in auto-generated figure captions (lines 120–122, 144–146) and are parser artifacts from PDF-to-text conversion, not author errors. Removed per formatting-artifact rule.
- **Missing engagement with existing OOD MLFF papers**: The harsh critic suggested the paper should discuss prior OOD MLFF evaluations. This is a missing-related-work claim that cannot be verified without external sources. Removed per the rule against flagging missing references.
- **Hyperparameter optimization details (per-task vs. joint)**: These are standard implementation details presumably in the stripped appendix. Removed as a minor reproducibility nitpick.
- **Training loss framed as "fatal"**: The harsh critic labeled the missing loss function as critically under-specified. In MLFF practice, the loss formulation (weighted energy + forces) is standard, making this a real but minor omission rather than a fatal gap. Demoted to Minor.
- **"Models should learn underlying physical principles" vs. GFN2-xTB as a major disconnect**: The paper acknowledges the trade-off (line 56), and using semi-empirical labels for benchmarking ML architectures is a pragmatic choice. Kept as a Minor framing issue rather than a major methodological flaw.
- **Strength Finder: "well-motivated gap" and "important problem"**: Generic framing strengths removed — the concrete strengths are captured in the kept items above.

## Novel Insights
None beyond the paper's own contributions. The core insight — that current MLFF architectures exhibit large and consistent generalization gaps on controlled compositional splits, that models optimal for ID are not optimal for OOD, and that augmented training with explicit compositional demonstrations fails to close the gap — is the paper's own finding and is genuinely informative for the field.

## Suggestions
- Add at minimum a sentence in Section 4.2 specifying the training loss formulation.
- Include a dedicated analysis subsection exploring the energy-forces dissociation — even a brief diagnostic would substantially increase the paper's value without requiring new experiments.
- Acknowledge the chemical non-additivity of -COOH in Task 2 and the scope limitations of GFN2-xTB as a reference method for claims about "physical principles."

## Score and Decision

**Anchor papers considered across all rounds:**

| Paper | Path | Avg Score | Round | Comparison |
|-------|------|-----------|-------|------------|
| CypST | ZyAwBqJ9aP | 2.00 | R1 | Clearly weaker — narrow domain, limited contribution |
| Sources of Gain | p1b96KC6rj | 2.17 | R1 | Different domain, clearly weaker |
| Retrosynthesis | o1efpbvR6v | 2.33 | R1 | Different domain, clearly weaker |
| CG Potentials | ItPYVON0mI | 3.00 | R1 | Weaker — less principled benchmark design |
| MoleculeCLA | P5jreWnIjV | 4.00 | R1 | Weaker benchmark contribution |
| Conformer Fields | XSwxy3bojg | 4.40 | R1 | Different focus, weaker evaluation |
| MoreRed | rwmWd2rjP1 | 4.75 | R2 | GMD-25 has stronger evaluation design and clearer contribution |
| NeuralMD | J4V3lW9hq6 | 5.00 | R2 | GMD-25 has clearer benchmark contribution |
| Symmetry Discovery | e4PL5zssJ9 | 5.00 | R2 | Different focus; GMD-25 has more concrete empirical contribution |
| Equivariant Approx | wmw3Jy8MVF | 5.75 | R1 | Different focus (method + benchmark) |
| **EGraFFBench** | **NvJxTjTQtq** | **6.00** | **R1/R2** | **Closest match. Both MLFF benchmarks. EGraFFBench has more evaluation breadth but had experimental validity concerns. GMD-25 has more principled design but less analysis depth.** |
| Lattice GNN | smy4DsUbBo | 6.00 | R1 | Different domain |
| Distribution Shifts MLFF | Xk9Q0CrJQc | 6.25 | R1/R2 | Stronger — proposes methods + benchmarking |
| LiFlow | CkozFajtKq | 6.33 | R2 | Stronger — novel method with thorough evaluation |
| Force-Guided Bridge | NSlvSDQ8aE | 7.00 | R1 | Clearly stronger contribution |
| Boltzmann Priors | pRCOZllZdT | 7.00 | R1 | Clearly stronger contribution |
| Online GNN Eval | KbetDM33YG | 8.00 | R1 | Different domain, clearly stronger |
| GeoBFN | NSVtmmzeRB | 8.00 | R1 | Different domain, clearly stronger |
| Hölder Stability | P7KIGdgW8S | 8.00 | R1 | Different domain, clearly stronger |

**Round 1 bracket:** 5.0–6.5. The paper sits clearly above the weak-anchor cluster (2.0–4.5) and below the strong-anchor cluster (7.0+). Within the middle range, EGraFFBench (6.00) and the Distribution Shifts paper (6.25) provide the closest comparisons.

**Round 2 narrowing:** Within the narrowed 4.5–6.5 bracket, GMD-25 is clearly stronger than the 4.75–5.00 papers (which have significant methodological issues) but falls short of EGraFFBench (6.00) due to less evaluation breadth, less result analysis, and missing statistical characterization. It is notably below the Distribution Shifts paper (6.25), which additionally proposes novel methods.

**Final assessment:** GMD-25 addresses a real and important gap — MLFF benchmarks overwhelmingly test interpolation, and a systematic benchmark for compositional generalization is genuinely needed. The task design is thoughtful and principled, the COGS grounding is a distinguishing strength, and the augmented-variant controls are an elegant experimental design choice. However, the paper's execution has significant gaps: the most striking result (energy-forces dissociation) is reported but never analyzed, no statistical characterization is provided, and key methodological details are absent from the main text. These issues prevent the benchmark from fully delivering on its diagnostic promise in its current form. **Score: 5.5.**

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>