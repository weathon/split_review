Now I have a clear picture. Let me compile my final review.

The GMD-25 paper is stronger than BenchMol (4.80) — its tasks are more principled and better motivated. It's comparable to EGraFFBench (6.00) — both are MLFF benchmark papers with similar scope, though EGraFFBench had more models/datasets but also more serious methodological concerns. GMD-25 is a bit weaker than the Distribution Shifts paper (6.25), which added methodological contributions alongside benchmark analysis. It is clearly below FreeCG (6.50), a methods paper with SOTA results.

GMD-25's central weaknesses are real but addressable: no error bars, energy metric not size-normalized, and limited analysis of the energy-force divergence. These don't invalidate the core contribution but do limit the strength of its comparative conclusions. I place it at **5.5**.

---

## Summary

This paper introduces GMD-25, a benchmark for evaluating compositional generalization in machine learning force fields (MLFFs). It proposes four carefully designed tasks (Length Extrapolation, Functional Group Composition, Duplication, and Combination) where training and test molecules share atomic building blocks but differ in chain length or functional group arrangement. Five state-of-the-art MLFF architectures are evaluated, revealing order-of-magnitude performance degradation on out-of-distribution examples across all models and tasks. The benchmark is accompanied by a reproducible toolkit for trajectory generation using GFN2-xTB.

## Strengths

- **Principled task design grounded in compositional generalization**: The four tasks systematically probe different generalization axes (length extrapolation, systematicity via composition, duplication, and combination) with carefully controlled train/test splits. Each task ensures training data covers all atomic building blocks present in test molecules, creating a clean test of whether models learn transferable principles rather than memorizing training distributions. This is a genuine advance over existing MLFF benchmarks that focus on broader chemical coverage without controlled generalization tests.

- **Clear and convincing empirical evidence of OOD failure**: The evaluation across five diverse architectures (SchNet, PAINN, DimeNet++, GemNet, EquiFormerV2) consistently shows errors increasing by one to two orders of magnitude at distribution shifts (Figures 2–4). The results are presented clearly with log-scale plots that make the generalization gap immediately visible. The finding that models with strong ID performance do not necessarily generalize best OOD (e.g., EquiFormerV2 excels at forces OOD but catastrophically fails on energy OOD) is an insightful diagnostic that the benchmark surfaces.

- **Reproducible and extensible toolkit**: The data generation pipeline (RDKit → FlashMD → GFN2-xTB → ASE) is well-documented with clear parameters, uses standard tools, and the commitment to release the full dataset and training scripts supports reproducibility and future task extensions.

- **Fair model comparison with hyperparameter optimization**: The use of Bayesian hyperparameter tuning for all evaluated architectures ensures baseline performance is optimized within computational constraints, making the comparative conclusions more credible than evaluations using only default hyperparameters.

## Weaknesses

### Fatal

None.

### Major

- **No variance estimates across training seeds**: The training sets are extremely small (5–8 molecules per task variant, each with ~2000 snapshots). Only point estimates of MAE are reported, with no error bars, standard deviations, or cross-validation. Given this data scarcity, the observed differences between models (e.g., "GemNet overall performed best in the OOD region for Functional Group Composition") may not be statistically reliable. This lack of uncertainty quantification weakens the comparative claims that are central to the benchmark's diagnostic purpose. Running even 3–5 independent training runs per model would substantially strengthen the conclusions.

- **Energy metric is not normalized by system size**: The energy MAE is computed as per-molecule total energy error (Section 4.2, Eq. for MAE_energy). In the Length Extrapolation task, test molecules have 7–13 carbons while training molecules have 2–6, meaning test molecules have roughly 1.5–2× more atoms. Since total ground-state energy scales with system size, a constant per-atom relative error manifests as a larger absolute MAE for larger molecules, partially confounding the apparent generalization gap. While the log-scale plots (Figure 2) show jumps far exceeding what size scaling alone would explain, reporting per-atom energy MAE alongside (or instead of) total energy MAE would eliminate this confound and make energy comparisons across tasks fairer.

### Minor

- **Energy-force divergence is reported but not analyzed**: A striking result is that EquiFormerV2 achieves the best force MAE in OOD regions but the worst energy MAE (Section 4.3, Length Extrapolation). For MLFFs where forces are computed as the gradient of the energy, such decoupling signals that the learned potential may not be conservative — a concern for MD stability. The paper notes this observation but offers no hypothesis or analysis, missing an opportunity to turn it into a concrete diagnostic of physical consistency, which directly aligns with the benchmark's stated goal of assessing whether models learn physically plausible representations.

- **Physical plausibility of composition tasks deserves more explicit discussion**: The paper acknowledges that "interactions between repeated moieties can introduce complex, non-linear effects" for the Duplication task, but does not extend this discussion to the Composition and Combination tasks. The Functional Group Composition task, for instance, tests whether models can infer carboxylic acid properties from alcohol + aldehyde training — but the local electronic environment of a carboxylic acid differs qualitatively from its components. While the tasks remain valid as diagnostics (the paper does not claim they should be perfectly solvable), discussing the fundamental physical limits of composability would strengthen the task rationale and help readers interpret the observed failure patterns.

- **Missing prominent equivariant architectures**: The evaluation omits NequIP and MACE, two well-known equivariant architectures that have demonstrated strong data efficiency and generalization. NequIP is cited in the related work (Section 2.1) but not evaluated. Including them would broaden the architectural coverage and strengthen claims about which design choices matter for compositional generalization. (The decision to exclude foundation models is reasonable and explicitly justified.)

### Trivial

- The paper does not discuss whether the GFN2-xTB level of theory might introduce artifacts relevant to specific tasks (e.g., long-range interactions in length extrapolation). A brief note would improve interpretability.
- It is unclear whether the GFN2-xTB recalculation step respects the same thermostat settings as the initial FlashMD run — a minor detail for reproducibility.

## Nice-to-Haves

- A "glass ceiling" estimate for each composition task — e.g., training a model on a few molecules that contain the target functional group combination and comparing its error to the zero-shot OOD setting — would quantify the irreducible difficulty of the compositional gap and make the benchmark more interpretable.
- A simple non-ML baseline (e.g., a sum-of-group-contributions model or Lennard-Jones) would contextualize the absolute error levels and demonstrate the benchmark is not trivially solvable.
- Computing a conservative-force check (curl of the force field) for models showing large energy-force discrepancies would turn the observed divergence into a concrete diagnostic.
- A per-atom energy metric alongside the total energy MAE.

## Removed Points

These points are flagged to be removed, treat them with caution:

1. **"Physical plausibility makes composition tasks fundamentally unfair" (Harsh Critic, claimed as structural/evidential)** — REMOVED as a fatal claim. The paper explicitly acknowledges non-linear effects for duplication (line 109: "interactions between repeated moieties can introduce complex, non-linear effects") and does not claim models should achieve zero error. The tasks remain valid diagnostics; the benchmark's claim is that they are challenging for current models, which is supported. The critic's assertion that even a "physically perfect model" couldn't compose is speculative and not grounded in any specific evidence in the paper. Demoted to Minor (the paper should discuss physical limits more explicitly).

2. **"Standard benchmarks already evaluate OOD generalization — the paper sets up a straw man"** — REMOVED. The paper explicitly discusses existing OOD benchmarks (DrugOOD, MatBench, BOOM) in Section 2.2 and existing MLFF benchmarks (MD17, MD22, Transition1x, WS22, xxMD) in Section 2.3, and clearly distinguishes its focus on controlled compositional generalization from broader coverage or property extrapolation. This criticism is factually wrong.

3. **"Missing appendix / cannot assess force analysis metrics"** — REMOVED per instructions. The parser strips appendices from all papers; they exist in the original submission.

4. **"GFN2-xTB thermostat inconsistency"** — REMOVED from major criticism level. This is a minor implementation detail; the critic frames it as a potential problem without evidence that it actually causes issues. Moved to Trivial.

5. **Strength Finder: "This paper addressed an important problem" (generic)** — REMOVED. This is a generic, non-specific strength. Replaced with concrete, evidence-backed strengths.

## Novel Insights

The benchmark reveals a consistent pattern that cuts across architectures: models that optimize well for in-distribution performance do not necessarily develop the most transferable representations. The most striking example is EquiFormerV2, which achieves the best OOD force predictions but simultaneously produces the worst OOD energy predictions — an inversion that suggests the model has learned to predict accurate force vectors without an underlying physically consistent energy surface. This energy-force decoupling pattern, observed across multiple tasks and not just for one architecture, is a genuinely interesting diagnostic signal that the benchmark surfaces. It suggests that standard ID validation may actively mislead model selection for generalization, and that force MAE alone — the most commonly reported metric in the MLFF literature — may be insufficient for assessing whether a model has learned physically sound representations.

## Suggestions

- Run 3–5 independent training seeds per model-task combination and report mean ± standard deviation for both energy and force MAE. With only 5–8 training molecules per task, this is computationally feasible and would dramatically strengthen the comparative conclusions.
- Add per-atom energy MAE as a metric alongside total energy MAE, particularly for the Length Extrapolation task where molecule sizes differ between train and test.
- Include NequIP and/or MACE in the evaluation to broaden architectural coverage — both are standard baselines in the equivariant MLFF literature and omitting them is a noticeable gap.
- Add a brief analysis or hypothesis for the energy-force divergence observed in EquiFormerV2. Even a qualitative discussion connecting it to how the model predicts forces (direct output vs. gradient of energy) would add diagnostic value.
- For the composition tasks, add a short paragraph discussing what physical knowledge would be necessary for compositional generalization (e.g., additivity of bond contributions, independent bond polarization), and what fundamental limits exist. This would preempt questions about task validity and help readers interpret failure modes.

---

**Score and Decision Calibration:**

Round 1 bracket: 5.0–7.0 based on:
- BenchMol (4.80) — broader but less principled benchmark; GMD-25 is clearly better
- EGraFFBench (6.00) — closest comparator, similar scope; GMD-25 comparable
- Distribution Shifts for MLFFs (6.25) — adds methods; GMD-25 is benchmark-only
- FreeCG (6.50) — methods paper with SOTA; different category, GMD-25 is below

Round 2 narrowed anchor comparisons:
- BenchMol (4.80, round 2): GMD-25 has more principled task design, clearer motivation, and better-grounded evaluation. GMD-25 is stronger.
- EGraFFBench (6.00, round 1): Both are MLFF benchmark papers. EGraFFBench evaluated more models (6 vs 5) on more datasets but had potentially invalid results (one reviewer flagged models not run correctly). GMD-25's evaluation is cleaner but less comprehensive, with metric confounds and no error bars. Comparable quality, with GMD-25 slightly weaker due to less rigorous evaluation practices.
- Distribution Shifts (6.25, round 1): Added methodological contributions alongside analysis. GMD-25 is benchmark-only. GMD-25 is somewhat weaker.
- FreeCG (6.50, round 2): Methods paper with SOTA results, different category entirely. GMD-25 is weaker.

GMD-25 lands at 5.5: clearly above BenchMol (4.80), slightly below EGraFFBench (6.00) due to less rigorous evaluation (no error bars, energy metric confound), and below methods-contributing papers in the 6.0–6.5 range.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>