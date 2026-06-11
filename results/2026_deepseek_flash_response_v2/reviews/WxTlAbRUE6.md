Now I have all the calibration data I need. Let me write the final consolidated review.

## Summary

This paper introduces GMD-25, a benchmark of four tasks (length extrapolation, functional group composition, functional group duplication, and functional group combination) designed to test compositional generalisation in machine learning force fields (MLFFs). The dataset comprises ~296K labelled geometries for 118 molecules computed with GFN2-xTB. Five MLFF architectures (SchNet, PAINN, DimeNet++, GemNet, EquiFormerV2) are evaluated, revealing that OOD errors are consistently one to two orders of magnitude larger than ID errors, and that ID performance does not predict OOD performance.

## Strengths

1. **Controlled compositional-generalisation tasks that isolate specific extrapolation abilities**: Unlike prior MLFF benchmarks (MD17, WS22, Transition1x) which primarily increase chemical diversity or sample non-equilibrium geometries, GMD-25 constructs four tasks each testing a distinct form of compositional generalisation (length extrapolation, functional-group composition, duplication, and combination). Section 3.1 defines each task with explicit train/OOD splits and explains why success requires compositional reasoning rather than interpolation. This design is a clear advance over existing benchmarks.

2. **Demonstration that ID performance rank order does not match OOD performance rank order**: The paper shows that a model's relative accuracy on in-distribution examples is a poor guide to OOD generalisation. In Length Extrapolation (Figure 2), EquiFormerV2 has the lowest Forces MAE yet its Energy MAE "increases dramatically in the OOD region, eventually becoming the worst-performing model" — while SchNet and DimeNet++, weaker on forces, have more stable energy predictions. This finding challenges the field's tendency to rank models by ID accuracy alone and is likely to influence future research directions.

3. **Quantification of generalisation gaps across all four tasks, with consistent failure patterns**: The results show that errors on OOD test molecules are "often one to two orders of magnitude higher than on in-distribution examples" (Conclusions). This pattern holds across diverse architectural families (invariant GNNs, equivariant GNNs, and equivariant Transformers), supporting the claim that compositional generalisation is a fundamental challenge for current MLFFs, not an artifact of a single model class.

4. **Reproducible and extensible data-generation pipeline**: Section 3.2 documents a four-step toolkit (RDKit → FlashMD → GFN2-xTB → ASE) with concrete parameters (Langevin thermostat at 300 K, 16 fs timestep, 200k steps per trajectory), enabling independent replication and extension. The dataset comprises 118 molecules and 296,534 labelled geometries.

## Weaknesses

### Fatal
None.

### Major

1. **No statistical analysis across runs**: All reported results appear to come from a single training run per model per task. MLFF training involves stochasticity from weight initialisation and optimisation; without multiple seeds it is impossible to distinguish genuine architectural differences from random variation. This is especially problematic for Figure 4, where several models show similar OOD error magnitudes (e.g., Functional Group Composition: EquiFormerV2 vs. PAINN vs. GemNet on forces MAE). A benchmark paper that aims to characterise which architectures generalise better needs to report whether these differences are reproducible. The absence of variance estimates weakens the central empirical claim and limits the benchmark's utility as a reference for future work. *Evidence: The paper contains no mention of multiple random seeds or variance estimates in the evaluation protocol (Section 4) or results (Section 4.3).*

2. **Missing MACE as a baseline**: MACE (Batatia et al., 2022, NeurIPS) is one of the most influential MLFF architectures and is discussed in the related work (line 38). The paper excludes it under the rationale of avoiding foundation models (line 104–105, citing Batatia et al., 2023), but the plain MACE architecture is *not* a foundation model — MACE-MP-0 is the foundation model, while standard MACE can be trained from scratch on the provided data. MACE's higher-order equivariant message passing represents a different inductive bias than the models tested (SchNet, PAINN, DimeNet++, GemNet, EquiFormerV2). Its absence is a notable gap, though it does not invalidate the existing results. *Evidence: Lines 104-105 state "we did not include any foundation models (Batatia et al., 2023) in our analysis" — this rationale does not apply to training plain MACE from scratch.*

3. **ID-tuned hyperparameters as a confound for an OOD benchmark**: The Bayesian hyperparameter optimisation (Section 4.2) targets in-distribution performance. For a benchmark that explicitly cares about out-of-distribution generalisation, this could systematically select hyperparameters that favour memorisation over transferable representations. Models that would generalise better with different hyperparameters (e.g., stronger regularisation, different learning rates) might be penalised. The paper does not acknowledge this trade-off or compare ID-tuned vs. default-hyperparameter results to assess whether the confound is consequential. *Evidence: Section 4.2 explicitly states "Bayesian hyperparameter optimisation to ensure that each model achieved its best possible performance on the in-distribution data."*

### Minor

1. **Overstated language about "learning physical principles"**: The paper repeatedly frames the benchmark as testing whether models "capture the underlying physical principles" (abstract, line 13, line 168). However, the reference labels come from GFN2-xTB, a semi-empirical tight-binding method with known systematic errors compared to higher-level theory. A model that perfectly reproduced GFN2-xTB would have learned an approximate model's physics, not the true quantum mechanical PES. This does not invalidate the benchmark (GFN2-xTB is consistent and widely used), but the framing overstates what the benchmark can diagnose. The authors should calibrate their language to more precisely describe what is being learned. *Evidence: Abstract line 9, Conclusions line 168.*

2. **Tension between compositional framing and non-additive physics in Task 2**: The Functional Group Composition task treats a carboxylic acid as a "composition" of an alcohol and an aldehyde. However, the electronic structure of a carboxylic acid involves strong coupling between -OH and -C=O groups on the same carbon — the properties are not additive. The paper acknowledges this in passing (line 76: "we do not expect the model to learn the chemical reaction pathway"), but the tension between the compositional framing and the non-additive quantum mechanical reality should be discussed more explicitly. *Evidence: Lines 68-76, Section 3.1.*

### Trivial
None.

## Nice-to-Haves

- Breakdown of OOD errors by atom type, distance from equilibrium, or force magnitude to deepen the diagnostic value of the benchmark beyond aggregate MAE.
- Check energy-force consistency for cases where the two metrics diverge sharply (e.g., EquiFormerV2 on Length Extrapolation — low forces MAE but high energy MAE).
- Include GFN2-xTB's own predictions on OOD test points as an upper-bound reference to help readers calibrate acceptable error levels.
- Compare ID-tuned vs. default-hyperparameter results to assess whether the ID-tuning confound is actually consequential or negligible.

## Removed Points

1. **"Slightly dated in its emphasis — EquiFormerV2 described as defining the current frontier"** — Cannot be independently verified without external knowledge of the evolving field as of 2026. Removed per instruction to not penalize for missing late-breaking related works.
2. **"Bayesian search space, budget, and selection criteria deferred to appendix"** — The parser strips appendix sections; this content exists in the original submission. Removed per instruction.
3. **"No analysis of whether generalisation failure correlates with model capacity, depth, or other architectural parameters"** — Goes beyond the stated scope of a benchmark paper; the benchmark's purpose is to provide tasks and baseline results, not to exhaustively diagnose architectural causes. Scope creep.
4. **"Pre-trained models excluded is a weakness"** (from Strength Finder) — This is actually a strength (principled exclusion to avoid confounding memorisation with generalisation), not a weakness. The paper's rationale for excluding foundation models is sound.
5. **"No comparison with the reference method's own accuracy"** — Moved to Nice-to-Haves; it would strengthen the paper but is not a core flaw.
6. Various formatting/style/parser-artifact nitpicks — Removed per instructions.

## Novel Insights

The reviews surface an interesting meta-observation: the paper's core finding (all models fail dramatically on compositional generalisation) is simultaneously its strongest contribution and its most problematic empirical feature. Because the OOD errors are so large (orders of magnitude), the absence of variance estimates is *less* likely to reverse the main qualitative conclusion — all models clearly fail at these tasks. However, the fine-grained comparisons (which model is best at which task, the ID vs. OOD rank reversal) cannot be trusted without error bars. This creates an unusual asymmetry where the headline finding is robust even as the detailed rankings are unsubstantiated. The paper would benefit from explicitly acknowledging this distinction and focusing more on the robust qualitative pattern (universal failure, large gaps) while tempering the quantitative comparisons.

## Suggestions

1. **Report results with at least 3 random seeds and include standard deviations or confidence intervals in all figures.** This is the single most important addition for a benchmark paper.
2. **Add MACE (trained from scratch, not pre-trained) as a baseline**, or explicitly justify its absence beyond the foundation-model rationale. MACE is a standard point of comparison in the MLFF literature.
3. **Acknowledge the ID-tuning confound explicitly** and ideally compare default vs. optimised hyperparameter results for at least one task to assess its practical impact.
4. **Calibrate language**: Replace phrases like "capture the underlying physical principles" with more precise wording such as "learn the GFN2-xTB potential energy surface" or "learn transferable representations of inter-atomic interactions."
5. **Discuss the non-additive physics of Task 2 more explicitly** so readers understand that the compositional framing is an approximation, not a claim about the physics being additive.

## Score and Decision

### Calibration Anchors

**Round 1 — Bracketing:**
| Path | Avg Score | Round | Comparison to this paper |
|------|-----------|-------|------------------------|
| kKXIYUi8ff (DynamicsDiffusion) | 3.00 | 1 | Weaker — less coherent contribution, rejected |
| ItPYVON0mI (ML-CG Potentials) | 3.00 | 1 | Weaker — fundamental methodological issues |
| zyBJodMrn5 (Multimodal Gen. Bench.) | 5.67 | 1 | Comparable genre (benchmark), accepted; but more narrowly scoped |
| dggRphAcCj (GeoCon) | 6.33 | 1 | Comparable topic, rejected; fundamental technical issues in that paper |
| tHHzfZSP6T (Transformer Capabilities) | 5.00 | 1 | Weaker — mixed reviews, no clear actionable finding |
| hKMPz3wkPV (Formal Comp.) | 6.75 | 1 | Different genre (theoretical); had fundamental technical flaws |
| NSVtmmzeRB (GeoBFN) | 8.00 | 1 | Stronger — clean method contribution with full evaluation |
| KbetDM33YG (Online GNN Eval.) | 8.00 | 1 | Stronger — novel problem framing with rigorous evaluation |

**Round 2 — Narrowing:**
| Path | Avg Score | Round | Comparison to this paper |
|------|-----------|-------|------------------------|
| NvJxTjTQtq (EGraFFBench) | 6.00 | 2 | Most directly comparable MLFF benchmark; had serious implementation concerns (model results contradicted known baselines) — our paper is methodologically cleaner |
| Xk9Q0CrJQc (MLFF Dist. Shifts) | 6.25 | 2 | Related topic but includes mitigation methods; weaknesses about modest gains |
| LixGd92Wri (GDL-DS) | 5.67 | 2 | Similar genre (OOD benchmark); had serious flaws in causal framing and unfair comparisons — our paper is more carefully designed |
| 4S2L519nIX (Geom-GNN Pre-training) | 6.50 | 2 | Accepted method paper; different genre (scaling/pre-training study) |
| Aemqy6Hjdj (CG Feature Alignment) | 5.67 | 2 | Rejected CG method paper; limited scope |
| CkozFajtKq (LiFlow) | 6.33 | 2 | Different genre (generative MD method) |

Round 1 placed the paper in the 4–7 bracket, clearly above the weak band (~3) and clearly below the strong band (~8). Round 2 narrowed this: the paper is stronger than EGraFFBench (6.0) due to cleaner methodology and no implementation concerns, and is more carefully designed than GDL-DS (5.67). However, the absence of variance estimates is a genuine weakness that prevents reaching the 6.5–7 range of the cleaner accepted papers. The paper sits between the comparable benchmarks at 5.67–6.0 and the stronger accepted method papers at 6.5.

**Final Score: 6.0**

**Rationale:** A solid benchmark contribution with well-designed tasks and important empirical findings. The weaknesses (no variance estimates, missing MACE baseline, ID-tuning confound, slightly overclaimed framing) are real but addressable and do not invalidate the core findings. The paper is methodologically sounder than comparable benchmark papers at 5.67–6.0 but lacks the statistical rigor expected of a reference benchmark.

**Decision: Weak Accept**

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>