## Summary

This paper introduces GMD-25, a benchmark for evaluating compositional generalisation in Machine Learning Force Fields (MLFFs), comprising four tasks — length extrapolation, functional group composition, functional group duplication, and functional group combination — with training-test splits designed so that all sub-components needed for generalisation are present in the training data. Five state-of-the-art MLFFs (SchNet, PAINN, DimeNet++, GemNet, EquiFormerV2) are evaluated, consistently showing large OOD error gaps and diverging ID/OOD performance rankings across architectures.

## Strengths

- **Well-motivated benchmark design grounded in compositional generalisation theory**: The four tasks are explicitly mapped to established concepts from Hupkes et al. (2020) — length generalisation and systematicity — providing principled theoretical framing. The training-test splits are carefully designed so that every functional group and chain-length segment in the test set appears in the training data (Section 3.1, Figure 1), making observed failures interpretable as genuine generalisation failures rather than coverage gaps.

- **Compelling evidence that ID/OOD model rankings diverge**: The paper demonstrates that EquiFormerV2 achieves the lowest Forces MAE on ID data for Length Extrapolation but becomes the worst for Energy MAE in the OOD region, while SchNet and DimeNet++ show more stable energy predictions OOD despite weaker ID performance (Section 4.3, Figure 2). This finding is concrete and challenges the assumption that standard benchmark performance predicts generalisation ability.

- **Base and augmented task variants provide nuanced insight**: The augmented variants (with explicit compositional demonstrations) show that even when models have seen all relevant sub-components, they still struggle on unseen combinations (Figures 3, 4c–d). This suggests the failures are not purely data-driven, strengthening the case for architectural limitations.

- **Broad architectural coverage**: The evaluation spans invariant GNNs (SchNet), equivariant message passing (PAINN, DimeNet++, GemNet), and equivariant Transformers (EquiFormerV2), ensuring the generalisation failures are not attributable to a single architectural family (Section 4.1).

## Weaknesses

### Fatal
None.

### Major

- **Training data volume confounds the interpretation of generalisation failures**: For the base variant of Task 1, models are trained on only ~10,000 snapshots from 5 small molecules (C2–C6 alkanes, ~2000 snapshots each). For Task 3, training uses ~12,000 snapshots from 6 molecules. These are very small training sets by MLFF standards. When the paper reports "errors on OOD test molecules are often one to two orders of magnitude higher," the alternative explanation — that models simply haven't been given enough data to learn robust representations — is not ruled out. A data-scaling ablation (e.g., 4–10× more snapshots or more training molecules within the same distributional constraints) would substantially strengthen the central claim that the failures are architectural rather than data-related. The augmented variants partially address this by adding more data, but they confound data volume with the nature of added demonstrations. This is the most significant gap between the paper's evidence and its conclusion about "fundamental challenges in learning transferable representations" (Section 5, line 193).

- **Results are descriptive rather than diagnostic**: The paper systematically reports that generalisation gaps exist but does not probe *why* models fail. For Length Extrapolation, do errors concentrate at chain ends, near the centre, or uniformly? For Functional Group Duplication, is the failure due to incorrect long-range interaction modelling or something else? Without per-atom or per-region error analysis, the benchmark identifies that models fail but offers limited guidance on what specifically they fail to learn, reducing its utility as a tool for model development.

### Minor

- **Energy MAE is computed on total energy, conflating extensive scaling with generalisation failure**: Energy is an extensive quantity — larger molecules have larger absolute energies and potentially larger absolute errors even for a well-calibrated model. The MAE formula (Section 4.2) computes error on total molecular energy, not per-atom or per-bond energy. For the Length Extrapolation task in particular, part of the observed OOD error growth may reflect extensive scaling rather than compositional generalisation failure. Reporting per-atom energy MAE alongside total energy MAE would help disentangle these effects.

- **Snapshot sampling procedure is not described**: The paper describes trajectory generation parameters (Langevin thermostat, 300K, 16fs timestep, 200k steps in FlashMD, Section 3.2) but does not specify how the ~2000 snapshots per trajectory were subsampled from the full trajectory (uniformly? Boltzmann-weighted? at fixed intervals?). This affects the distributional properties of training and test sets and is relevant for reproducibility.

- **No variance or confidence intervals reported**: With only 5–7 test molecules per task, a single outlier molecule could dominate the reported MAE. While the per-chain-length plots (Figures 2, 3) provide some granularity, the summary bar charts (Figure 4) collapse all test molecules into a single MAE without showing per-molecule results or variance, limiting interpretability.

- **Augmented Task 1 has an unusual discontinuous training distribution**: The augmented variant trains on alcohols with chain lengths {2,3}∪{9,15} and carboxylic acids with lengths {4,8} (Section 3.1). This discontinuous distribution introduces its own distributional complexity beyond simply having "more" training data, which should be discussed more explicitly when interpreting the augmented variant results.

- **MACE architecture is absent**: MACE (Batatia et al., 2022) is one of the most popular current MLFF architectures, featuring higher-order equivariant message passing that could be relevant to the compositional generalisation question. Its absence from the evaluation is notable given the paper's goal of covering diverse architectural paradigms.

### Trivial
None.

## Nice-to-Haves

- A brief discussion of what architectural modifications might help with compositional generalisation would add depth. The paper draws on the algorithmic alignment literature (Section 2.2), suggesting physics-informed architectures should help, yet the most physics-informed model (EquiFormerV2) does not consistently win — discussing this tension would be valuable.

- Brief validation of GFN2-xTB labels against higher-level DFT on a small subset would strengthen the benchmark's credibility. The paper acknowledges GFN2-xTB as a "balance of efficiency and accuracy" (Section 3) but does not examine whether the reference method itself has compositional generalisation limitations for the test molecules.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **MACE as "not yet released" or unavailable**: The harsh critic's concerns about model availability are removed per policy. MACE is cited in the paper and exists.
- **Typos/formatting**: Any formatting artifacts are parser issues, not author errors.
- **Missing appendix content**: The appendix is stripped by the parser; proofs and hyperparameter tables exist in the original submission.

## Novel Insights

The paper's most genuinely novel empirical observation — that ID and OOD model rankings diverge across multiple tasks and architectures (Section 4.3) — has significant implications for how the MLFF community selects and benchmarks models. If the model that performs best on standard benchmarks does not generalise best to novel molecules, then current benchmark-driven model development may be optimising for the wrong objective. This finding, if robustly established with scaling studies, could reshape evaluation practices in the field.

## Suggestions

1. **Add a data-scaling ablation** on at least one task (e.g., Task 1 base variant). If the generalization gap persists with 4× or 10× more training snapshots, the paper's central claim becomes much more convincing and the benchmark moves from descriptive to diagnostic.
2. **Report per-atom energy MAE** alongside total energy MAE to disentangle extensive scaling effects from genuine generalisation failures, especially for the Length Extrapolation task.
3. **Add per-region error analysis** for at least one task (e.g., in Length Extrapolation, does error grow uniformly along the chain or concentrate at structurally novel positions?).
4. **Include MACE** in the model evaluation to close a notable gap in architectural coverage.

## Calibration Report

**Anchors retrieved:**

| Round | Anchor ID | Topic | Avg Score | Decision | Comparison |
|-------|-----------|-------|-----------|----------|------------|
| 1 | ItPYVON0mI | CG potential dynamic accuracy | 3.00 | Reject | Unrelated methods paper; our paper is much stronger |
| 1 | kKXIYUi8ff | Diffusion for MD trajectories | 3.00 | Reject | Unrelated generative model; our paper is much stronger |
| 1 | CgkAGcp9lk | Composition search with diffusion | 3.00 | Reject | Unrelated generative model; our paper is much stronger |
| 1 | OcTUquFXfx | Global minima energy landscapes | 2.60 | Reject | Unrelated optimization paper; our paper is much stronger |
| 1 | NvJxTjTQtq | EGraFFBench (MLFF benchmark) | 6.00 | Reject | Most topically similar anchor. Our paper has cleaner task design, better theoretical framing, and a more focused research question. Clearly above. |
| 1 | Xk9Q0CrJQc | Distribution Shifts for MLFFs | 6.25 | Reject | Very relevant. Proposes methods rather than a benchmark. Our paper is more focused and has cleaner design; comparable or slightly above. |
| 1 | rwmWd2rjP1 | Molecule relaxation by diffusion | 4.75 | Reject | Different topic; our paper is stronger. |
| 1 | 4S2L519nIX | Geom-GNN pre-training scaling | 6.50 | Accept | Mixed reviews (6,6,8,6). Our paper has a cleaner, more focused contribution. Slightly above. |
| 1 | NSVtmmzeRB | Bayesian Flow Networks for molecules | 8.00 | Accept | Generative model; not directly comparable. Our paper is weaker as a contribution. |
| 1 | kJFIH23hXb | Flow matching for protein backbones | 8.00 | Accept | Different domain; not comparable. |
| 1 | gHLWTzKiZV | Unbalanced flows for docking | 8.00 | Accept | Different topic; not comparable. |
| 1 | KSLkFYHlYg | ShEPhERD drug design | 8.00 | Accept | Different topic; not comparable. |
| 2 | VTYg5ykEGS | ImageNet-OOD benchmark | 6.50 | Accept | OOD detection benchmark, different domain but similar spirit. Our paper is comparable in quality. |
| 2 | AhMEkBSdIV | LCA-on-the-Line OOD benchmark | 5.33 | Reject | OOD generalization benchmark; our paper is stronger. |
| 2 | aAcOaJYbUg | LAION-C OOD benchmark | 5.25 | Reject | OOD robustness benchmark; our paper is stronger. |
| 2 | LixGd92Wri | GDL-DS benchmark for GDL | 5.67 | Reject | Geometric DL distribution shift benchmark. Our paper is clearly better designed and more focused. |
| 2 | hiHZVUIYik | Path-norm toolkit | 7.33 | Accept | Theoretical generalization work; not directly comparable. |
| 2 | wAXsx2MYgV | Dynamic social vision | 7.00 | Accept | Different domain; not comparable. |
| 2 | sahQq2sH5x | Predictive Coding benchmarking | 7.33 | Accept | Benchmark paper for a different community; somewhat comparable in structure. |
| 2 | yOhNLIqTEF | Transformers generalization ICL | 6.67 | Accept | Generalization study; somewhat comparable. |

**Round 1 bracket**: 5.5–7.0. The paper is clearly above the rejected MLFF benchmarks (EGraFFBench at 6.0, Distribution Shifts at 6.25) and comparable to accepted anchors at 6.5.

**Round 2 narrowing**: The (5.0, 7.0) range anchors confirm: our paper is above GDL-DS (5.67, rejected), comparable to ImageNet-OOD (6.50, accepted), and the 6.5 bracket is well-supported. The data scaling weakness prevents scoring above 7.0. The paper sits at the boundary of the 6.5–7.0 range, closer to 6.5 given the unresolved data volume confound.

## Evaluation on Key Axes

**Originality**: Good. The compositional generalisation framing applied to MLFFs is novel, and the task design is carefully controlled rather than simply expanding molecular coverage. The benchmark fills a genuine gap between configurational diversity benchmarks (MD17, WS22) and property-prediction OOD benchmarks (DrugOOD, MatBench).

**Importance of research question**: High. Whether MLFFs learn transferable physical principles or merely interpolate training data is a fundamental question for the field.

**Soundness of claims**: The central empirical observation (models fail at compositional generalisation) is well-supported. The stronger claim about "fundamental challenges in learning transferable representations" is not fully supported without a data-scaling study.

**Soundness of experiments**: Adequate but with gaps. The controlled task design is strong, but the absence of data scaling, per-atom energy metrics, and diagnostic error analysis limits the interpretability of results.

**Clarity of writing**: Good. The paper is well-organised, the tasks are clearly described, and the figures are informative.

**Value to the community**: High. The benchmark and toolkit are valuable contributions that could guide future model development, even without the diagnostic analyses.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>