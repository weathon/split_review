Now I have enough to calibrate. Let me synthesize my final review.

**Calibration summary:**

| Anchor | Score | Round | Comparison to GMD-25 |
|---|---|---|---|
| EGraFFBench (NvJxTjTQtq) | 6.00 | R1/R2 | Very similar MLFF benchmark; GMD-25 has cleaner task design, fewer implementation concerns |
| Understanding Distribution Shifts (Xk9Q0CrJQc) | 6.25 | R1/R2 | Studies MLFF OOD + proposes solutions; GMD-25 has stronger task design but no technical contribution |
| GDL-DS (LixGd92Wri) | 5.67 | R2 | Broader but had serious causal-framework issues; GMD-25 is clearly stronger |
| AU-GOOD framework (qFZnAC4GHR) | 6.67 | R2 | Novel evaluation metric, accepted; GMD-25 has no comparable technical novelty |
| Pushing Limits (4S2L519nIX) | 6.50 | R2 | Pre-training + scaling study, accepted; has technical contribution GMD-25 lacks |
| DynamicsDiffusion (kKXIYUi8ff) | 3.00 | R1 | Weak, unrelated |
| Achieving Dynamic Accuracy (ItPYVON0mI) | 3.00 | R1 | Weak, unrelated |
| EGraFFBench NSlvSDQ8aE / CkozFajtKq / etc. | 6.00–7.00 | R1 | Various MLFF papers |

**Round 1 bracket: 5.5–7.0 → narrowed by Round 2 to 5.5–6.5.** GMD-25 is cleaner than EGraFFBench (6.00) but lacks the technical contribution of the 6.25–6.67 anchors. 

**Final score: 6.0.**

---

## Summary

This paper introduces GMD-25, a benchmark for evaluating compositional generalisation in machine learning force fields (MLFFs). It proposes four controlled tasks — length extrapolation, functional group composition, functional group duplication, and functional group combination — that isolate specific generalisation capabilities not tested by existing MD benchmarks. Evaluating five state-of-the-art architectures (SchNet, PAINN, DimeNet++, GemNet, EquiFormerV2), the paper finds consistent and severe degradation (1–2 orders of magnitude) on out-of-distribution molecules across all tasks, and shows that the best in-distribution model does not necessarily generalise best. A reproducible data-generation toolkit is also provided.

## Strengths

- **Systematic, well-motivated task design**: The four tasks cleanly isolate distinct compositional generalisation abilities (length extrapolation, systematicity via composition, duplication, and asymmetric combination). Training molecules are chosen so that all atomic-scale components appearing in the test set also appear in training — a careful setup that makes the OOD failure diagnostically informative (Section 3.1).

- **Clear empirical demonstration of generalisation failure**: Across all tasks and all five architectures, OOD errors are 1–2 orders of magnitude higher than ID errors (Figures 2–4, Section 5). This pattern is robust and not model-specific.

- **Decoupling of ID and OOD performance**: A genuinely interesting finding — EquiFormerV2 achieves the lowest ID forces MAE on Length Extrapolation but becomes the worst model on OOD energy MAE, while SchNet and DimeNet++ show the opposite pattern (Section 4.3). This directly challenges the assumption that better ID accuracy implies better physical representations.

- **Diverse architectural coverage**: The evaluation spans invariant (SchNet), equivariant message-passing (PAINN, DimeNet++, GemNet), and Transformer-based (EquiFormerV2) architectures, making the conclusion that all current designs struggle with compositional generalisation broadly applicable.

- **Reproducible data-generation toolkit**: The pipeline (RDKit → FlashMD → GFN2-xTB → ASE, Section 3.2) is clearly described and extensible, providing practical value beyond the specific benchmark.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **Energy MAE not normalised by atom count**: The energy MAE is computed as total absolute energy error averaged over molecules (Eq. in Section 4.2), while forces MAE is correctly normalised by 3N. Since test molecules can differ in size from training molecules (e.g., longer alkanes in Task 1), a constant per-atom error produces a larger total-energy MAE, potentially inflating the apparent generalisation gap on energy. The paper should report per-atom energy MAE alongside the current metric. The forces MAE (which is normalised) shows the same qualitative OOD degradation, so this does not threaten the core conclusions, but it weakens the energy-specific claims and cross-model comparisons on energy.

- **No variance estimates across training runs**: Hyperparameter optimisation was performed, but results are reported as single values with no standard deviations or confidence intervals across seeds. Differences between models in the OOD regime are sometimes small (e.g., Figure 4 panels g–h), and without run-to-run variance it is unclear which differences are meaningful.

### Trivial

- The paper does not discuss whether using GFN2-xTB (a semi-empirical method) rather than DFT-level reference calculations might affect the physical principles present in the label distribution, and whether the observed generalisation failures could be sensitive to this choice.

## Nice-to-Haves

- Including a simple physics-informed baseline (e.g., a group-additivity or bond-energy model) for the simpler tasks would anchor what level of OOD performance is plausible and strengthen the claim that "learning the principles" should enable better generalisation.

- Acknowledging that longer alkanes (Task 1) or multiply-functionalised molecules (Tasks 2–3) may explore conformational spaces absent from training trajectories would clarify a potential confound beyond the intended compositional shift.

- Reporting per-atom energy MAE alongside the current total-energy metric.

## Removed Points

These points are flagged to be removed, treat them with caution.

- **Harsh critic: "Overstated claim that the tasks should be feasible for models that learn the physical principles" (framed as a critical/fatal issue)**: The paper explicitly qualifies this for Task 2 (line 105: "we do not expect the model to learn the chemical reaction pathway, but rather to infer the properties of the composite group from the learned effects of its constituent parts"). The abstract's phrasing ("should be feasible for models that learn the physical principles") is somewhat strong, but the paper does not claim these tasks are easy or guaranteed to be solvable — it presents them as diagnostic probes. The critic's assertion that the task is "chemically unrealistic" and that this is a "structural" flaw overreaches; the task's purpose is precisely to test whether models can handle composition of familiar fragments, and the paper acknowledges the challenge. The claim is adequately hedged in the body text. Demoted from "critical" to reflected in the minor framing note above.

- **Harsh critic: "Missing reference to simple additive baselines (group-contribution methods)"**: Group-contribution methods predict thermodynamic properties, not per-atom forces from MD trajectories, so they are not directly comparable. Moved to Nice-to-Haves as a suggestion.

- **Harsh critic: "Conformational landscape confound"**: A reasonable observation, but the paper's use of off-equilibrium FlashMD trajectories (Section 3.2) already broadens conformational coverage. This is a nuance rather than a weakness. Moved to Nice-to-Haves.

- **Strength finder: generic strengths about problem importance**: Removed — "this paper addressed an important problem" is not a concrete, verifiable strength.

- **Harsh critic: "Strengthening the Paper on Its Own Terms" reframing suggestion**: This is editorial advice about presentation, not a weakness. Filtered.

## Novel Insights

The most novel and well-supported insight is the decoupling of in-distribution and out-of-distribution performance rankings: the model that performs best on ID forces (EquiFormerV2) can simultaneously be the worst on OOD energy, and vice versa for invariant models like SchNet. This is not an obvious or previously documented finding in the MLFF literature, and it carries practical implications — it suggests that the field's current focus on lowering ID force/energy errors may select for architectures that are actually less physically robust, rather than more.

## Suggestions

- Report per-atom energy MAE in addition to total-energy MAE to remove the size-scaling confound from energy comparisons.
- Include standard deviations across at least 3 training seeds to support claims about which model "performs best" in the OOD regime, where differences are often small.
- Briefly discuss the implications of using GFN2-xTB vs. DFT for the physical principles encoded in the labels.

---

## Score and Decision

**Originality**: The compositional-generalisation framing for MLFFs is novel and well-motivated. The four-task design is systematic and goes beyond prior benchmarks that primarily vary molecular diversity or property ranges.

**Importance of research question**: Whether MLFFs learn physical principles or merely interpolate is a central open question. This benchmark provides a concrete diagnostic for it.

**Claims well supported**: The core claim — that current MLFFs exhibit severe OOD degradation on compositionally-motivated shifts — is robustly supported. The stronger claim that this demonstrates a failure to learn physical principles is partially supported but should be more carefully qualified given the task difficulty.

**Soundness of experiments**: The hyperparameter tuning strategy is reasonable, the model selection covers the architectural space well, and the dataset generation pipeline is sound. The lack of error bars and the energy MAE normalisation issue are the main gaps.

**Clarity of writing**: The paper is well-organised and easy to follow, with clear task descriptions and informative figures.

**Value to the community**: The benchmark and toolkit fill a genuine gap and will be useful for MLFF development, particularly as the field increasingly recognises the limitations of ID-only evaluation.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Reject</decision>