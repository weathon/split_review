Now I have sufficient calibration material. Let me write the final consolidated review.

## Summary

This paper introduces GMD-25, a benchmark for evaluating compositional generalisation of machine learning force fields (MLFFs). It defines four tasks—length extrapolation, functional group composition, functional group duplication, and functional group combination—each with training and OOD test splits from different molecules. Five architectures (SchNet, PAINN, DimeNet++, GemNet, EquiFormerV2) are evaluated, and the paper reports that OOD errors are often one to two orders of magnitude larger than in-distribution errors.

## Strengths

1. **Novel, targeted benchmark design.** Unlike existing MLFF benchmarks that broaden chemical coverage (ANI-1) or focus on equilibrium dynamics (MD17), GMD-25 isolates specific generalisation challenges through controlled train/OOD splits. Task 1 (length extrapolation on alkanes) and Task 3 (mono→dicarboxylic acids) cleanly operationalize length generalisation and motif repetition. This targeted design is a genuine step forward.

2. **Consistent failure pattern across diverse architectures.** The paper evaluates 5 models spanning invariant, equivariant, angle-aware, and transformer-based families (Section 4.1), and all exhibit large OOD→ID error gaps on every task. This breadth strengthens the claim that the problem is fundamental rather than architecture-specific.

3. **Augmented variants rule out a trivial explanation.** The augmented variants of Tasks 1 and 2 include demonstration examples (e.g., amines/amides showing how functional groups compose, discontinuous chain lengths). Models still fail (Figure 4c,d), which goes beyond simply showing OOD degradation and suggests the failure is not merely about lacking a compositional example in the training set.

4. **ID ranking ≠ OOD ranking.** The paper documents that EquiFormerV2 achieves the best forces MAE but worst energy MAE on length extrapolation, while SchNet/DimeNet++ show the opposite pattern (Section 4.3). This non-obvious finding suggests that current architectures may exploit dataset-specific shortcuts rather than learning physically generalisable representations.

## Weaknesses

### Fatal
None.

### Major

1. **The benchmark tasks are not validated as tests of compositional generalisation.** The paper asserts that "the training data is chosen such that generalisation to the test examples should be feasible for models that learn the physical principles" (Abstract, line 13), but provides no evidence that a model that *genuinely* learns compositional or physical principles *could* solve these tasks. For example:
   - **Task 1 (length extrapolation):** Do alkanes C2–C6 contain all the information needed to predict forces on C7–C13? Many-body interaction terms in interatomic potentials are not strictly additive, and the paper does not analyse whether longer chains have collective modes absent in short chains.
   - **Task 2 (functional group composition):** A carboxylic acid has resonance stabilization and electronic structure not present in alcohols or aldehydes. The paper partially acknowledges this ("we do not expect the model to learn the chemical reaction pathway," line 105), but the task label *composition* implies a decomposability that is not justified.
   - A simple additive baseline (e.g., a bond-order potential, or per-atom energy summing) would demonstrate whether the tasks are even solvable through compositional reasoning. Without such grounding, the reported failures may reflect task difficulty rather than a lack of compositional generalisation. This undercuts the paper's central claim.

2. **Results lack statistical reliability.** All results are reported as single runs without variance, confidence intervals, or multiple seeds. The training sets are small (5–8 trajectories of ~2000 snapshots each), making observed model differences potentially noisy. The paper draws comparative conclusions (e.g., "EquiFormerV2 performed best on Length Extrapolation in terms of forces MAE, but it failed completely on energy MAE"), but without multiple seeds we cannot assess whether these patterns are reproducible. For a benchmark paper—where the primary output is empirical findings—this is a significant gap.

### Minor

3. **Task 2 conflates compositionality with functional-group transfer.** Training on alcohols and aldehydes and testing on carboxylic acids tests whether a model can predict a *new functional group* that shares sub-structural overlap with trained groups. This is a departure from the standard notion of systematicity (recombining known components in novel ways), since the carboxyl group is not simply an alcohol + an aldehyde. The augmented variant partly mitigates this, but the task framing overclaims what it tests.

4. **No discussion of cutoff radii.** Many MLFFs use a finite cutoff radius (e.g., 5 Å). For longer alkanes (Task 1), effective interatomic interactions may extend beyond the cutoff, introducing a confounding factor that could explain OOD degradation. The paper does not mention cutoff radii or whether this could affect the results.

### Trivial
None.

## Nice-to-Haves

- A simple non-ML baseline (e.g., UFF, GAFF) would provide a useful point of reference for the scale of OOD errors, though this is not necessary for the paper's core claims.
- Ablation on training set size/diversity: showing sensitivity to data quantity would help distinguish whether failures are due to insufficient data or architectural limitations.
- Reporting distribution of errors (e.g., box plots) rather than only bar-chart aggregates would help gauge practical significance of the reported gaps.

## Removed Points

- *Missing appendix content / stripped by parser*: Removed per rules—the parser strips these sections from all papers; they exist in the original submission.
- *"Cannot be independently verified" (reproducibility concerns about cited entities)*: Removed per hard rules.
- *GFN2-xTB vs DFT accuracy*: The paper notes GFN2-xTB is "known for its balance between computational efficiency and accuracy" (line 85). The benchmark evaluates generalisation for this level of theory; this is a standard choice and not a weakness.
- *Strength Finder generic strengths (e.g., "this paper addresses an important problem")*: Removed as generic.
- *Criticism about no classical force field baseline*: Downgraded to nice-to-have. The paper aims to benchmark MLFFs specifically; a classical baseline would add context but is not required.
- *Request for hyperparameter sensitivity on OOD performance*: The paper performs Bayesian HP optimisation on ID data (Section 4.2), which is appropriate; OOD HP tuning would be circular.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Validate task solvability.** Implement a simple baseline—e.g., a per-atom energy model that learns linear/bond contributions from training molecules and sums them on test molecules. If this baseline succeeds, the tasks are demonstrably compositionally solvable and the MLFF failures are meaningful. If it fails, the tasks may be inherently harder than assumed, and the paper should reframe its claims accordingly.

2. **Report multiple seeds.** Run each model with 3–5 random seeds and report mean ± std. This is essential for a benchmark paper that draws comparative conclusions between architectures.

3. **Reframe Task 2.** Either (a) redesign it as a genuine test of systematicity (e.g., train on molecules with *either* alcohol OR aldehyde, test on molecules with *both* on the same scaffold), or (b) rename it "functional group transfer" and adjust the claims.

4. **Discuss cutoff radii.** Include the cutoff values used for each model and briefly discuss whether finite cutoffs could confound the length extrapolation results.

## Score and Decision

**Calibration anchors** (from `calibration_search` batch; all paths under `deepreview_13k_calibration`):

| Path | Avg Human Score | Comparison to This Paper |
|------|----------------|--------------------------|
| `Xk9Q0CrJQc.md` (Understanding and Mitigating Distribution Shifts for MLFFs) | 6.25 | Stronger — includes proposed methods to address OOD, thorough experiments across datasets; this paper is purely a benchmark with no mitigation solutions |
| `NvJxTjTQtq.md` (EGraFFBench) | 6.00 | Similar — both are MLFF benchmark papers with OOD evaluation; EGraFFBench has more models/metrics but was still rejected due to experimental reliability issues; current paper has cleaner design but lacks error bars |
| `qFZnAC4GHR.md` (AU-GOOD Framework) | 6.67 | Stronger — comprehensive OOD evaluation framework with novel metric, statistical tests, accepted; this paper has narrower scope and no statistical rigor |
| `czVzzXPCkw.md` (On Extrapolation in Material Property Regression) | 4.33 | Slightly weaker — criticized for small dataset, narrow scope, lack of novelty; current paper has better task design and clearer motivation |
| `7Jer2DQt9V.md` (Unreasonable Effectiveness of Pretraining in Graph OOD) | 4.50 | Similar — both are benchmark papers with known limitations; current paper has more controlled task design but similar depth of analysis issues |

Positioning relative to these anchors: The paper makes a clearer conceptual contribution than the extrapolation benchmark (4.33) and the pretraining benchmark (4.50), with better-motivated task design. However, it lacks the methodological rigor (multiple seeds, statistical tests, task validation) of the higher-scored papers (6.25, 6.67). The unvalidated central claim (that tasks test compositionality) is a genuine weakness that prevents acceptance at a top venue.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>