Now I have enough calibration data to score the paper. Let me synthesize everything.

**Round 1 Bracketing:**
- Low band (weak): scores 2.60–3.40 — clearly below our paper
- Middle band: 4.75–6.33 — EGraFFBench (6.00), Understanding Distribution Shifts (6.25), MARCEL (6.33)
- High band: 7.60–8.00 — generative model papers, not comparable

**Initial bracket: 4.5–6.5**

**Round 2 narrowing:** Our paper is most comparable to EGraFFBench (6.00) and MARCEL (6.33). EGraFFBench is another MLFF benchmark with similar scope but had implementation concerns (models performing worse than expected) and weaker conceptual framing. MARCEL is a conformer ensemble benchmark that was accepted. Our paper has cleaner task design and a stronger conceptual framing than EGraFFBench, but fewer models and missing analyses. It's likely between EGraFFBench and MARCEL, perhaps slightly below MARCEL due to the interpretive gaps from missing feasibility baseline and data scaling experiments.

**Final score: 5.5**

Now let me write the review.

---

Let me now verify all my remaining concerns against the paper one more time to make sure they're accurate:

1. **Feasibility baseline**: The paper says "training data is chosen such that generalisation to the test examples should be feasible for models that learn the physical principles" (Abstract). No model is shown to solve any task. This claim is unsupported. VERIFIED - KEEP as Major.

2. **No statistical treatment**: No error bars, no multiple seeds. VERIFIED - but per soft rules, single-run is standard in MLFF benchmarks. DEMOTE to Minor.

3. **Data quantity not explored**: Training sets are small, no scaling experiments. VERIFIED - KEEP as Major.

4. **Baseline coverage**: 5 models, no MACE. The paper says "we did not include any foundation models" - MACE has both foundation and non-foundation versions. SchNet is a simple baseline. DEMOTE to Minor.

5. **Compositional claim strained for Task 2**: The paper acknowledges this: "we do not expect the model to learn the chemical reaction pathway, but rather to infer the properties of the composite group from the learned effects of its constituent parts." KEEP as Minor.

6. **Energy MAE per molecule**: Makes comparison across chain lengths harder. PER the paper, Eq. 1: MAE_energy = 1/M * sum |E_hat - E|. So it is per molecule, not per atom. This is a reasonable design choice but worth noting. KEEP as Trivial.

7. **Missing details (convergence criteria, thermostat, velocity distributions)**: The paper mentions "Langevin thermostat (300 K) and a 16 femtosecond timestep for 200k steps" but not convergence criteria. Minor point, but the main text should summarize essentials. KEEP as Trivial.

Now let me also evaluate the strength finder's points:

1. "Comprehensive and controlled task design" — VERIFIED, concrete. KEEP.
2. "Clear empirical demonstration of severe generalization gap" — VERIFIED, concrete. KEEP.
3. "Reproducibility and extensibility via dedicated toolkit" — VERIFIED, concrete. KEEP.
4. "Rigorous model evaluation protocol" — VERIFIED, though the two-stage tuning is described vaguely (search space, trials not in main text). Soften slightly. KEEP.

Let me also check for any points I should remove:

Harsh critic's "Missing Parts" section:
- "No ablation on GFN2-xTB reference method" — This is a nice-to-have. REMOVE from weaknesses.
- "No force-component directional accuracy" — The paper says "Additional force analysis metrics are presented in the appendix." Since we can't verify the appendix, but the paper acknowledges this, it's reasonable. REMOVE from weaknesses (it's addressed).
- "Discussion of why certain models fail could be deepened" — Nice-to-have. MOVE to Nice-to-Haves.
- "No evaluation of computational cost" — Nice-to-have. MOVE to Nice-to-Haves.

Other harsh critic points to remove:
- "missing details that affect reproducibility: convergence criteria for GFN2-xTB, thermostat settings beyond temperature, and the handling of the initial velocity distributions. These may appear in the stripped appendix" — Per hard rules, we can't criticize missing appendix content. The main text does have the key parameters. But noting that the description could be more complete is reasonable. DEMOTE to Trivial.

Strength Finder points to keep/drop:
All four seem valid and grounded. None conflict with verified weaknesses.

Now let me write the review.Now let me produce the final consolidated review.

---

## Summary

This paper introduces GMD-25, a benchmark for evaluating compositional generalisation in machine learning force fields (MLFFs). It constructs four tasks — length extrapolation, functional group composition, functional group duplication, and functional group combination — using AIMD trajectories computed at the GFN2-xTB level. Five state-of-the-art models (SchNet, PAINN, DimeNet++, GemNet, EquiFormerV2) are evaluated, and all show large OOD generalisation gaps, often one to two orders of magnitude above ID error. The benchmark is accompanied by a reusable data-generation toolkit. The paper makes a timely contribution by providing systematic, controlled tests of whether MLFFs learn transferable physical principles or merely interpolate their training data.

## Strengths

- **Well-designed, controlled task structure for compositional generalisation.** The four tasks systematically probe length extrapolation and systematicity (functional group composition, duplication, combination), each with clearly defined training/OOD splits that isolate a specific generalisation capability (Section 3.1, Figure 1). This goes beyond prior benchmarks that focus on chemical coverage or equilibrium dynamics without controlled OOD splits.

- **Clear empirical demonstration of a severe generalisation gap.** Across all five architectures and all four tasks, OOD errors are one to two orders of magnitude higher than ID errors (Figures 2–4, Section 4.3). This directly validates the claim that current MLFFs struggle to generalise beyond their training molecules.

- **Reproducibility and extensibility via a dedicated toolkit.** The paper describes a complete, reusable data-generation pipeline (Section 3.2) and commits to releasing the dataset, splits, and preprocessing scripts, lowering the barrier for future research.

- **Diverse set of evaluated architectures.** The five models span invariant (SchNet) and equivariant (PAINN, DimeNet++, GemNet, EquiFormerV2) designs, plus both GNN and Transformer approaches, giving a reasonably broad picture of the current landscape.

## Weaknesses

### Fatal

None.

### Major

- **No feasibility baseline — the benchmark's solvability is unsubstantiated.** The paper repeatedly states that "training data is chosen such that generalisation to the test examples should be feasible for models that learn the physical principles" (Abstract, Section 3.1). Yet no model — not even a simple physics-inspired baseline — is shown to solve any task. The reader cannot distinguish whether the observed failures reflect fundamental limitations of current neural architectures or whether the tasks themselves may be poorly conditioned for the given training data (e.g., the electronic structure of a carboxylic acid is not a simple sum of alcohol and aldehyde fragments). A classical additive force field, or an explicit per-atom/additive energy model, would calibrate whether the tasks are solvable in principle and dramatically strengthen the benchmark's diagnostic value.

- **Data quantity is not explored — the failure may reflect data starvation rather than architectural limitations.** Training sets are small (5–16 molecules per task, ~2000 snapshots each). It is well established that MLFFs can require substantial data. No experiment varies training data volume (e.g., subsampling trajectories) to see whether OOD performance improves. The augmented variant of Task 1 does add data but confounds quantity with distribution, so the effect of data volume alone is not isolated. If adding more data shrinks the gap, the central claim that architectures fundamentally fail to learn physical principles would need qualification. This is the most actionable missing experiment.

### Minor

- **No statistical treatment (error bars, multiple seeds).** All results are single-run point estimates with no standard deviations or confidence intervals. While single-run evaluation is the norm in many MLFF benchmarks, a benchmark intended to guide the field would benefit from reporting variation across seeds, especially given the modest test-set sizes (e.g., one trajectory per chain length in Task 1). The comparative claims (e.g., "EquiFormerV2 consistently exhibits the lowest Forces MAE") rest on unreplicated point estimates.

- **The compositional mapping for Task 2 is somewhat strained.** In the functional group composition task, the test carboxylic acid has OH and carbonyl on the *same* carbon, whereas training aldehydes and alcohols have them on *different* carbons. This changes the local electronic environment substantially and is not a straightforward recombination of previously seen building blocks. The paper does acknowledge this indirectly ("we do not expect the model to learn the chemical reaction pathway, but rather to infer the properties of the composite group"), but a more precise discussion of what kind of compositionality is being tested would clarify interpretation.

- **Omission of MACE.** MACE (Batatia et al., 2022) is a prominent equivariant GNN that is not a foundation model and would be a natural inclusion alongside the five evaluated architectures. Its higher-order message passing might show different generalisation behaviour. This is a gap in baseline coverage, though the five evaluated models already span a reasonable range of design choices.

### Trivial

- **Energy MAE normalisation.** Energy MAE is reported per molecule rather than per atom (Eq. 1). This makes direct comparison across chain lengths harder, since longer molecules naturally accumulate larger total energy errors. The log-scale plots partially absorb this, but per-atom normalisation would be cleaner.

- **Hyperparameter search details are in the stripped appendix.** The main text (Section 4.2) mentions Bayesian optimisation but does not specify the search space, number of trials, or the validation split strategy. These details should be summarised in the main text for the paper to be self-contained.

## Nice-to-Haves

- **Data-scaling curves** for at least one task to separate data-efficiency issues from genuine compositional failures.
- **A simple classical or additive baseline** (e.g., harmonic bond/angle terms fitted to training data) to calibrate whether the tasks are solvable in principle.
- **Discussion of why certain model behaviours occur**, e.g., why EquiFormerV2's energy MAE blows up in Task 1 while its force MAE remains best — this asymmetry may point to specific architectural properties.
- **Computational cost reporting** (training time, inference speed) for practical adoption.
- **Ablation on sensitivity to the GFN2-xTB reference method**, or at least a discussion of its limitations for these chemical spaces.

## Removed Points

*These points are flagged to be removed — treat them with caution.*

1. **Harsh critic: "No simple baselines (e.g., invariant model using only pairwise distances plus a linear head)."** — Removed. SchNet already serves as an invariant pairwise baseline. The claim that no simple baselines exist is inaccurate.

2. **Harsh critic: "The paper lacks any ablation on the effect of the GFN2-xTB reference method."** — Moved to Nice-to-Haves. This is outside the paper's stated scope (it's a benchmark, not a reference-method comparison) and is a reasonable limitation for a benchmark of this scale.

3. **Harsh critic: "The evaluation does not include a measure of force-component directional accuracy."** — Removed. The paper explicitly states that "Additional force analysis metrics are presented in the appendix." This is addressed.

4. **Harsh critic: "Missing details — convergence criteria for GFN2-xTB, thermostat settings beyond temperature, handling of initial velocity distributions. These may appear in the stripped appendix."** — Per hard rules, we cannot criticise missing appendix content. The main text provides the core simulation parameters (Langevin thermostat, 300K, 16 fs timestep, 200k steps), which is a reasonable summary.

5. **Harsh critic: "The augmented variant does not improve OOD performance for any model; this is a puzzling result that is not discussed."** — Removed. The paper does report and discuss the augmented variant results (Section 4.3), noting that while it was expected to be easier, it still shows substantial gaps. The observation is presented; deeper analysis would be nice-to-have but its absence is not a weakness.

6. **Strength Finder: "The benchmark addresses an important problem / interesting question."** — Removed as generic/superficial.

## Novel Insights

The paper's most genuinely novel observation is the *disconnect between ID and OOD model rankings*: the model that performs best on in-distribution examples is not always the one that generalises best to out-of-distribution examples. For instance, in the length extrapolation task, EquiFormerV2 dominates forces MAE but has catastrophically poor energy MAE in the OOD region, while SchNet — a much simpler invariant model — maintains stable energy predictions. This suggests that current architectural innovations aimed at improving ID accuracy (e.g., higher-order equivariance) may not translate to better compositional generalisation and may even harm it. This finding has practical implications for model selection in deployment scenarios where OOD molecules are expected.

## Suggestions

- The highest-leverage improvement would be adding a **classical/additive baseline** to establish whether the tasks are solvable in principle. Even a simple harmonic model with bond-length and angle terms fitted to the training data would calibrate task difficulty.
- Run each model with **3+ random seeds** on at least one task and report means with standard deviations. This is inexpensive and would substantially strengthen the comparative claims.
- Add a **data-scaling experiment** for one task (e.g., length extrapolation base) by training on {200, 500, 1000, 2000} snapshots to separate data-efficiency from architectural limitations.
- **Normalise energy MAE per atom** for fairer cross-length comparisons, or at minimum discuss the per-molecule choice.

## Score and Decision

**Originality:** The benchmark addresses a genuine and underexplored gap — systematic compositional generalisation testing for MLFFs. The task design is conceptually well-motivated and goes beyond prior benchmarks.

**Importance:** The question of whether MLFFs learn transferable physical principles is central to the field, and the benchmark provides a useful diagnostic tool.

**Claim support:** The central claim — that SOTA MLFFs struggle with compositional generalisation — is well-supported by consistent results across five models and four tasks. However, the interpretation of *why* they fail is undermined by the absence of a feasibility baseline and data-scaling experiments.

**Soundness:** The experimental setup is reasonable, but the lack of statistical treatment and unexplored data-quantity effects limit the strength of conclusions.

**Clarity:** The paper is well-written and well-organised. Task descriptions and figures are clear.

**Value to community:** The benchmark fills a real gap and the released toolkit enables extension. The paper would be a useful resource, particularly if the major weaknesses are addressed.

**Calibration anchors:**
- `kKXIYUi8ff` (3.00, Round 1): DynamicsDiffusion — generative MD paper; much weaker contribution, not comparable.
- `ItPYVON0mI` (3.00, Round 1): CG potential paper; not comparable.
- `OcTUquFXfx` (2.60, Round 1): Global minima discovery; not comparable.
- `XeGSIr7z6u` (3.40, Round 1): Memorization-generalization in diffusion models; not comparable.
- `NvJxTjTQtq` (6.00, Rounds 1–2): EGraFFBench — closest comparison. Similar benchmark scope but had implementation concerns (models underperforming published results). Our paper has cleaner task design and stronger conceptual framing. GMD-25 is slightly stronger.
- `Xk9Q0CrJQc` (6.25, Rounds 1–2): Distribution shifts for MLFFs — method paper with analysis; stronger because it proposes solutions, but gains were modest. Our benchmark-only paper is slightly below this.
- `rwmWd2rjP1` (4.75, Round 1): Molecule relaxation; not directly comparable.
- `CkozFajtKq` (6.33, Round 1): Flow matching for atomic transport; not directly comparable.
- `1JgWwOW3EN` (4.80, Round 2): BenchMol — multi-modality MRL benchmark. Had serious design questions and weaker labels. GMD-25 is clearly stronger.
- `NSDszJ2uIV` (6.33, Round 2): MARCEL — conformer ensemble benchmark, accepted. Similar quality of contribution. GMD-25 has more original data generation but fewer models and missing analyses. GMD-25 is slightly below MARCEL.
- `NSVtmmzeRB`, `kJFIH23hXb`, `uKZdlihDDn`, `gHLWTzKiZV` (7.60–8.00, Round 1): Generative model papers; clearly above GMD-25 in contribution depth.

**Round 1 bracket:** 4.5–6.5. **Round 2 narrowed:** The paper sits between EGraFFBench (6.00) and MARCEL (6.33), with conceptual strengths that edge it above EGraFFBench but omission of a feasibility baseline and data-scaling experiments that place it below MARCEL. Final score: **5.5**.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>