Now I have sufficient calibration data. Let me synthesize the final review.

**Calibration summary:**

| Anchor | Avg Score | Decision | Comparison to GMD-25 |
|--------|-----------|----------|----------------------|
| EGraFFBench (NvJxTjTQtq) | 6.00 | Reject | More models/datasets but less principled task design; GMD-25 is cleaner and better motivated |
| Distribution Shifts MLFF (Xk9Q0CrJQc) | 6.25 | Reject | Method+brief benchmark; different paper type, GMD-25 has stronger empirical contribution |
| MARCEL (NSDszJ2uIV) | 6.33 | Accept | Comparable benchmark paper; GMD-25 has more striking results and generates own data |
| Scaling Geom-GNNs (4S2L519nIX) | 6.50 | Accept | Empirical study; GMD-25 has comparable quality with clearer task design |

**Bracket:** GMD-25 sits between 6.0 and 6.5. The MARCEL benchmark (6.33, accepted) is the closest comparator — both are well-designed benchmarks with some limitations. GMD-25's task design is more principled and its results more dramatic, but it has a notable gap in model coverage (missing MACE). I place it at **6.5**, slightly above MARCEL, as its compositional-generalization framing is genuinely novel and the empirical signal is unambiguous.

---

## Summary

This paper introduces GMD-25, a benchmark for evaluating compositional generalization in machine learning force fields (MLFFs). It proposes four controlled tasks—length extrapolation, functional group composition, duplication, and combination—each with base and augmented variants, where training and test molecules differ but the building blocks overlap. Evaluating five diverse architectures (SchNet, PAINN, DimeNet⁺⁺, GemNet, EquiFormerV2), the paper shows that all models suffer orders-of-magnitude error increases on out-of-distribution molecules, revealing a fundamental generalization gap in current MLFFs.

## Strengths

- **Principled task design grounded in compositional generalization theory.** The four tasks systematically probe length extrapolation and systematicity (novel recombination of known components), with base/augmented variants serving as built-in ablations that test whether models can exploit compositional demonstrations (Section 3.1, Figure 1). This goes beyond prior benchmarks that either focus on interpolation or lack controlled OOD splits.

- **Striking and consistent empirical signal.** Across all five models and all four tasks, force and energy MAE rise by one to two orders of magnitude at the distribution shift (Figures 2–4). The gap is unambiguous and does not depend on marginal differences between models, making the core finding robust even without error bars.

- **Nuanced architectural findings that a single-task benchmark would miss.** For example, EquiFormerV2 achieves the lowest force MAE on length extrapolation but the worst energy MAE, while SchNet and DimeNet⁺⁺ show the opposite pattern (Section 4.3, Figure 2). These task-dependent trade-offs provide actionable insight for architecture design.

- **Methodologically sound evaluation setup.** In-distribution test trajectories are drawn from entirely separate simulations (secondary trajectories), not held-out frames from the same run, preventing train–test leakage (Section 3.1). The accompanying toolkit (Section 3.2) is built on standard open-source libraries and follows a reproducible workflow.

## Weaknesses

### Fatal

None.

### Major

None. The core claims are well-supported by the evidence presented.

### Minor

- **Missing key equivariant architectures (MACE, NequIP).** The paper evaluates five diverse models but omits MACE and NequIP—widely adopted equivariant architectures that can be trained from scratch on this data. The paper discusses both in related work (Section 2.1) and explicitly excludes only foundation models, not trainable architectures. While the five evaluated models span invariant GNNs, equivariant MPNNs, directional message passing, and Transformer-based architectures, adding MACE would strengthen the claim that the generalization failures are universal across state-of-the-art MLFFs. The core finding is unlikely to be reversed by adding these models, but the omission weakens the "state-of-the-art" framing.

- **No seed variation or uncertainty estimates reported.** All MAE values come from single training runs. Given that the observed OOD gaps span orders of magnitude, the qualitative conclusion is not threatened, but reporting run-to-run variance would let readers assess the reliability of model rankings, particularly on tasks where the ID/OOD gaps are smaller (e.g., Functional Group Combination, Figure 4g–h).

- **Limited diagnostic breakdown beyond aggregate and per-chain-length MAE.** The benchmark convincingly detects generalization failures but offers limited insight into *why* models fail—no breakdown by atom type, bond-length regime, or distance from functional groups. The base/augmented variants provide partial diagnostic signal (e.g., whether compositional demonstrations help), and the per-chain-length plots in Figures 2–3 offer some granularity, but the paper's claim of serving as "a valuable diagnostic tool for identifying architectural biases" is only partially supported by the current analysis.

- **Training data scarcity as a potential confound.** Training sets contain only 5–8 trajectories per task (roughly 10k–16k geometries). While in-distribution errors are low (suggesting models fit the training distribution adequately), a sanity check varying training-set size per molecule would help confirm that the OOD gap reflects compositional difficulty rather than data insufficiency. This is a reasonable concern but does not undermine the main result.

### Trivial

- The paper could benefit from reporting the standard deviation of ground-truth forces/energies to contextualize absolute MAE values, making it easier for readers to judge practical significance.
- The Functional Group Composition task's assumption that constituent-group information should be sufficient to predict the composite group would benefit from a more explicit chemical justification.

## Nice-to-Haves

- Adding MACE (and optionally NequIP) to the evaluation would substantially strengthen the paper's claim to cover state-of-the-art architectures.
- A concise ablation varying training data per molecule would rule out data insufficiency as an alternative explanation for the generalization gap.
- Summarizing the force-magnitude MAE and other appendix metrics in the main paper would improve completeness.
- Breaking down errors by atom type or chemical environment would elevate the benchmark from detection to genuine diagnosis.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Harsh critic claimed "PBE0" and "m4s" in figures are labeling errors.** These are OCR/parser artifacts from PDF extraction, not present in the original manuscript. Removed.
- **Harsh critic claimed the "orders of magnitude" language is overstated for Functional Group Combination.** The paper already notes this task shows a "notably smaller" gap (Section 4.3, last paragraph), and the conclusion acknowledges variation across tasks. The critic's framing overstates the paper's imprecision. Removed.
- **Harsh critic claimed no diagnostic insight at all.** The paper provides per-chain-length analysis (Figures 2–3), per-task comparisons (Figure 4), and base vs. augmented variant comparisons, which constitute meaningful diagnostic signals. The criticism is partially valid but overstated; retained at Minor level with appropriate qualification.
- **Strength Finder: "This paper addressed an important problem" / "targeted an interesting question."** Generic framing without concrete evidence. Removed per filtering rules.

## Novel Insights

The paper's most novel insight is that compositional generalization—long studied in NLP and vision—provides a productive framework for diagnosing MLFF failures. The four-task decomposition (length extrapolation, composition, duplication, combination) maps cleanly onto chemical structure variation and reveals that even models with strong in-distribution accuracy have not internalized the physical principles needed to recombine known building blocks. The finding that energy and force errors can trade off dramatically across architectures (EquiFormerV2 excels at forces but collapses on energy for length extrapolation) suggests that architectural choices influence which physical quantity a model prioritizes during generalization—a dynamic that standard interpolation benchmarks cannot surface.

## Suggestions

- Add MACE to the evaluation suite to strengthen the claim of covering state-of-the-art architectures. This is the single highest-impact improvement.
- Report mean and standard deviation over at least 3 random seeds for key results to establish result stability.
- Include a baseline such as the mean absolute force magnitude in the test set, or a trivial constant-zero predictor, to calibrate the reported MAE values.
- Add a brief discussion or figure in the appendix showing how ID error evolves with increasing training data per molecule, to address the data-scarcity confound.
- Consider adding a simple atom-type error breakdown (e.g., carbon vs. heteroatom) to provide initial diagnostic signal without extensive additional computation.

## Score and Decision

**Round-1 bracket:** Based on the topical anchors, the paper sits between ~5.5 and ~7.5, with the closest comparators being benchmark/evaluation papers in the 6.0–6.5 range.

**Round-2 narrowing:** The MARCEL benchmark (6.33, accepted) and Scaling Geom-GNNs (6.50, accepted) are the closest quality comparators. GMD-25's task design is more principled than MARCEL's, and its empirical signal (orders-of-magnitude gaps) is more striking. The main limitations—missing MACE, no error bars, limited diagnostic depth—are real but addressable and do not undermine the core contribution.

**Final score:** 6.5 — a solid benchmark contribution with a clear, well-executed core idea, held back from a higher score by incomplete model coverage and limited diagnostic depth. The paper is above the acceptance threshold for a benchmark paper at this venue.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>