Now let me write the final review with proper calibration.

## Summary

This paper introduces GMD-25, a benchmark of four compositional generalization tasks (Length Extrapolation, Functional Group Composition, Functional Group Duplication, Functional Group Combination) for evaluating whether ML force fields capture underlying physical principles rather than interpolating training labels. The benchmark includes base and augmented variants for controlled comparisons, and an empirical study of five MLFFs (SchNet, PAINN, DimeNet++, GemNet, EquiFormerV2) reveals that all models fail substantially on OOD generalization, with ID ranking often not predicting OOD ranking.

## Strengths

- **Systematic compositional-generalisation tasks that fill a genuine gap in MLFF evaluation.** The four tasks (Section 3.1) each isolate a specific aspect of compositional generalisation, whereas existing MLFF benchmarks (MD17, WS22, Transition1x, MD22) focus on configurational diversity, reaction pathways, or system size without probing compositional generalisation. This distinction is made explicit (lines 48–53).

- **Demonstrates that in-distribution leaderboard ranking does not predict out-of-distribution ranking.** Results in Section 4.3 show that EquiFormerV2 achieves the best ID forces MAE but the worst OOD energy MAE on Length Extrapolation; on Functional Group Composition, DimeNet++ has the lowest ID error yet all models show poor OOD performance. This finding — that strong ID accuracy does not imply physically meaningful learning — is something standard benchmarks cannot reveal.

- **Base+augmented variant design provides controlled diagnostic evidence.** Each task includes an augmented variant that adds structurally relevant training data (Section 3.1). For Functional Group Composition, all models fail even when the composition pattern is explicitly shown in training (lines 138–139), pointing to architectural limitations rather than data coverage.

- **Physically realistic trajectory generation (AIMD at 300 K with Langevin thermostat)** rather than perturbed geometries improves ecological validity (Section 3.2, line 92). The toolkit and benchmark are designed to be extensible.

- **Thoughtful exclusion of foundation models** keeps the benchmark diagnostic rather than a performance contest, avoiding confounding memorization with generalization (line 104).

## Weaknesses

### Major

- **No uncertainty quantification for any comparative claim.** The paper makes statements about relative model performance throughout Section 4.3 (e.g., "EquiFormerV2 consistently exhibits the lowest Forces MAE," "GemNet overall performed best in the OOD region for Functional Group Composition," "SchNet and DimeNet++ generalise effectively") — all supported only by single-run point estimates. Without multiple random seeds, standard deviations, or confidence intervals, it is impossible to determine whether the observed performance differences between models are reproducible or reflect noise. For a benchmark intended to guide architecture selection and future research, this is a significant evidential gap. All models appear to have been trained once with optimized hyperparameters; the paper does not mention any replication across seeds.

### Minor

- **The mapping from tasks to "compositional generalization" is imprecise in places.** Task 2 (Functional Group Composition) frames carboxylic acid as a "composition" of alcohol and aldehyde (lines 69–72), but these functional groups have distinct electronic structures, different bond orders, and different acidity — failures could reflect genuine physical novelty rather than a compositional generalization deficit. Task 3 (Functional Group Duplication) introduces new non-linear inter-moiety interactions that even a perfect model of single carboxyl groups would need additional physics to handle. While the paper acknowledges some of this complexity (line 80), the framing occasionally overinterprets what a failure diagnoses about model capabilities. The paper would benefit from more circumspect language about what each task specifically tests.

- **No classical force field baseline is included** (e.g., UFF or GAFF). Such a baseline would help distinguish whether the tasks are genuinely hard for physics-based reasons or specifically due to neural network architectural limitations.

- **MACE (Batatia et al., 2022), a prominent non-foundation MLFF, is referenced in context but not evaluated.** While five models already provide meaningful coverage, MACE's absence leaves a visible gap given its standing in the field.

- **No tabular summaries of numerical results.** The paper relies entirely on figures with logarithmic scales; exact numerical values in table form would be essential for the community to use the benchmark results for comparison and as a reference point.

- **The algorithmic alignment theory (Xu et al., 2020) is mentioned in Section 2.2 but never operationalized in the analysis** — a missed opportunity to test whether models with more explicit geometric/physical priors align better with compositional tasks.

### Trivial

- The augmented variant of Task 1 tests interpolation across length/functional-group combinations rather than extrapolation per se. The paper acknowledges this ("we might expect this augmented variant to be easier," line 64) but still groups it under "Length Extrapolation," which could be clarified for precision.

- Hyperparameter optimization budget is not specified (e.g., how many configurations were explored per model), though the two-stage procedure (default + Bayesian optimization) is reasonable.

## Nice-to-Haves

- Error analysis beyond aggregate metrics: analyzing *where* errors concentrate within molecules (near novel functional groups vs. distributed across the molecule) would strengthen the compositional failure diagnosis.
- Oracle experiments establishing a performance ceiling (e.g., training and testing on the same molecule type but different conformations) would help contextualize the generalization gap.

## Removed Points

- "Data and code not available during review" — removed per policy: the paper explicitly states the data will be released upon acceptance (line 170). Questioning the future availability of a cited resource is out of scope.
- "Figure caption inconsistencies (PBE0, m4s)" — these appear only in parsed alt-text from PDF extraction and are parser artifacts, not author errors. The actual paper text correctly lists the five models.
- "C2 ethane has no dihedral degrees of freedom" — technically true but this level of detail about training set composition is a minor design choice unlikely to affect conclusions.
- "2000 snapshots per molecule is modest" — this is a deliberate design choice for a controlled generalization benchmark, not a weakness.

## Novel Insights

The reviews do not surface a genuinely novel insight beyond the paper's own contributions. The harsh critic's observation that the benchmark's most interesting finding (ID ranking ≠ OOD ranking) lacks uncertainty quantification is valid but is a criticism of the evidence base, not a new insight. The suggestion that classical force field baselines would help separate task difficulty from architectural limitations is a methodological refinement, not a novel observation.

## Suggestions

1. **Run all experiments with at least 3–5 random seeds** and report mean ± standard deviation for all metrics. This is the single most important improvement and would transform the evidential quality of the paper.
2. **Include a classical force field baseline** (e.g., UFF or GAFF) to contextualize whether the tasks are fundamentally hard or specifically hard for neural architectures.
3. **Add a numerical results table** reporting all model × task × variant × seed combinations with exact values, so the community can reference them directly.
4. **Tighten the framing** around Tasks 2 and 3 to more precisely distinguish compositional generalization from irreducible physical novelty — acknowledging what each failure mode does and does not diagnose.

## Score and Decision

### Calibration Anchors

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| o1efpbvR6v.md (retrosynthesis metric learning) | 2.33 | R1 | Much weaker — not a benchmark paper, poor technical quality |
| czVzzXPCkw.md (extrapolation in material property regression) | 4.33 | R1 | Weaker — method-overclaims, limited datasets, fairness concerns |
| LixGd92Wri.md (GDL-DS benchmark) | 5.67 | R1 | Slightly weaker — overclaiming issues, less focused benchmark design |
| NvJxTjTQtq.md (EGraFFBench) | 6.00 | R1 | Comparable — both are MLFF benchmarks; EGraFFBench has broader scope but implementation correctness concerns; GMD-25 has cleaner, more novel task design but lacks UQ |
| Xk9Q0CrJQc.md (Understanding & Mitigating Distribution Shifts for MLFFs) | 6.25 | R2 | Slightly stronger — includes both diagnostic analysis and new mitigation methods, though methods showed only modest gains |
| zyBJodMrn5.md (gCOG multimodal generalization benchmark) | 5.67 | R2 | Comparable — accepted with divergent scores (8,3,6); had weak baseline concerns but was still accepted; GMD-25 is similarly structured as a benchmark with important findings |
| UVSKuh9eK5.md (CLIP compositional generalization) | 5.67 | R2 | Comparable — analysis paper without new benchmark; both probe compositional generalization |
| Aemqy6Hjdj.md (CG-Bench compositional feature alignment) | 5.67 | R2 | Comparable — benchmark + method paper for compositional generalization in vision |

### Round 1 Bracket

The paper clearly sits above the strong-reject band (papers at 2–3) and below the strong-accept band (papers at 8). Initial bracket: **4.5–7.0**.

### Round 2 Narrowing

The two most directly relevant anchors — EGraFFBench (6.0, MLFF benchmark) and Understanding & Mitigating Distribution Shifts for MLFFs (6.25, MLFF distribution shifts) — place the expected score around **5.5–6.5**. GMD-25's benchmark design is more focused and novel than EGraFFBench's, but lacks the method component of the Understanding & Mitigating paper. GMD-25 is comparable to the gCOG benchmark (5.67, accepted) and GDL-DS (5.67, rejected) in scope and quality, but addresses a more clearly identified gap.

The paper's core contribution (the benchmark) is solid and the findings are interesting, but the lack of uncertainty quantification weakens the evidential basis for all comparative claims — a particularly important issue for a benchmark that aims to guide architecture selection.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Reject</decision>