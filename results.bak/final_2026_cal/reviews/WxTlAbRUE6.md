Now I have enough calibration data. Let me write the consolidated review.

**Bracket Report:**
- Round 1 bracket: between ~4.0 and ~5.6 (middle band)
- Round 2 anchors: TRErr3HucA (5.50, Reject), UVmMNagKvK (4.00, Reject), ftANj24sfU (5.00, Reject), e9cV4xSjbR (4.67, Accept Poster), qyjaVda7t2 (4.50, Accept Poster), T8VcTykTf1 (5.60, Accept Poster)
- Final comparison: The paper is a pure benchmark contribution (no new architecture/metric). It is better structured than StructEval (4.00) and ComMat (4.00), and has a clearer narrative than BSCT (5.50). But it has figure labeling errors (PBE0, m4s) and no uncertainty quantification. I place it at 5.0 — a solid benchmark with important findings but correctable presentation issues.

Let me now write the full review.

---

## Summary
2-3 sentence summary.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses

### Fatal
(usually empty)

### Major
- weakness 1 — why it matters
- weakness 2 — why it matters

### Minor
- weakness 1 — why it matters

### Trivial

## Nice-to-Haves

## Removed Points

## Novel Insights

## Suggestions

## Score and Decision
<score>5.0</score>
<decision>Reject</decision>

Let me now write this up properly.## Summary

This paper introduces GMD-25, a benchmark for evaluating compositional generalization of machine learning force fields (MLFFs) through four controlled tasks: length extrapolation, functional group composition, functional group duplication, and functional group combination. The training data for each task is designed so that the atomic-level components needed for test molecules are present, isolating compositional generalization from pure memorization. Evaluation of five SOTA models (SchNet, PAINN, DimeNet++, GemNet, EquiFormerV2) reveals OOD errors 1–2 orders of magnitude above ID errors across all tasks, with ID performance failing to predict OOD performance — a practically important finding for the MLFF community.

## Strengths

- **Systematic generalization tasks that isolate compositional reasoning**: Unlike prior MLFF benchmarks (MD17, WS22, Transition1x) which focus on interpolation within equilibrium dynamics or broad coverage, GMD-25 designs each task so that all atomic components present in the test molecules also appear in the training set. This controlled setup cleanly tests whether models capture physical principles rather than interpolating seen molecules. The augmented variants (Tasks 1–2) further isolate which specific failure mode dominates (e.g., Length Extrapolation augmented variant removes the "unseen length" confounder to test compositionality of length × functional group). *Evidence: Section 3.1 describes each task with explicit train/test splits and the rationale for base vs. augmented variants.*

- **Empirical finding that all evaluated models fail and ID performance does not predict OOD**: Across all four tasks, every model shows OOD errors 1–2 orders of magnitude higher than ID errors. Critically, the model with the best ID forces MAE (EquiFormerV2 on Length Extrapolation) simultaneously has the worst OOD energy MAE — demonstrating that standard ID-only benchmarks are insufficient for assessing model quality. *Evidence: Figure 2 shows a sharp error increase at the distribution shift for all models; Section 4.3 explicitly notes "EquiFormerV2 consistently exhibits the lowest Forces MAE... However, its Energy MAE increases dramatically in the OOD region, eventually becoming the worst-performing model."*

- **Controlled experimental design that excludes foundation models**: The authors deliberately exclude pre-trained foundation models to avoid conflating memorization from large-scale pre-training with genuine architectural generalization, making the benchmark a cleaner diagnostic of inductive bias. *Evidence: Section 4.1 states "did not include any foundation models... to make it harder to untangle memorisation and generalisation effects."*

## Weaknesses

### Major

- **Figure 2 and Figure 3 contain unlabeled/unexplained model names that undermine result attribution.** Figure 2's caption lists "PBE0" (orange squares) as one of the five evaluated models, but "PBE0" is a DFT functional, not an ML model — and it does not appear among the five models listed in Section 4.1 (SchNet, PAINN, DimeNet++, GemNet, EquiFormerV2). Meanwhile, PAINN is missing from the figure legend. Figure 3's caption lists "m4s" among six models, a name never defined or introduced anywhere in the paper. The reader cannot determine which architecture produced which curve. Since the central empirical claim depends on attributing performance to specific architectures, this is a non-trivial presentation failure. *Verification: Comparing Section 4.1 (the five models) against the Figure 2 caption (page 6, line 149) which lists "EquiFormerV2, PBE0, DimeNet++, SchNet, GemNet" and Figure 3 caption (page 7, line 173) which lists "DimeNet++, m4s, GemNet, EquiFormV2, PAINN, and SchNet."*

- **No uncertainty quantification from multiple training runs.** All reported results are from a single run per model per task, with no error bars, standard deviations, or any indication of variance across random seeds or initialization conditions. The paper makes comparative claims about which model "performs best" on which task (e.g., "GemNet overall performs best in the OOD region for Functional Group Composition and Functional Group Duplication," "EquiFormerV2 consistently exhibits the lowest Forces MAE"), but these claims are not statistically supported. Given that MLFF training can be sensitive to random seeds and the paper used Bayesian hyperparameter optimization (which may overfit to a specific split), the observed differences between models could be within the noise range of a single run. *Verification: The paper (Section 4.2) describes a single training run per model with Bayesian HP tuning; a grep for "multiple run|random seed|error bar|standard deviation|variance|uncertainty" returns no relevant hits.*

### Minor

- **GFN2-xTB reference data limits the claim about learning "physical principles."** The benchmark uses GFN2-xTB, a semi-empirical tight-binding method with known systematic errors relative to DFT. The paper frames OOD failures as models failing to learn "physical principles," but the benchmark evaluates generalization *within the xTB potential energy surface*, not to the true physical PES. While this is a legitimate methodological choice (computational tractability for 296k geometries), the paper would benefit from explicitly discussing whether the observed generalization patterns would transfer to DFT-level targets. A small-scale verification on DFT data for at least one task would strengthen the benchmark's credibility. *Verification: Section 3 (page 3, line 85) and Section 3.2 (page 5, line 123) both describe the GFN2-xTB approach.*

- **Modest dataset scope limits diagnostic resolution.** The benchmark comprises 118 molecules and 296k geometries. While sufficient for the controlled evaluation, the small number of molecules per task (e.g., 5–16 per group) means results could be sensitive to the specific molecular choices. Moreover, the paper does not include any error analysis at the atom or functional-group level to diagnose *why* models fail — e.g., whether OOD errors concentrate near specific atoms, correlate with bond distances, or reflect specific force components.

### Trivial

- Typo: "GNF2-xTB" on page 3 (line 85) should be "GFN2-xTB" (correctly written on page 5, line 123).
- Figure 3 caption writes "EquiFormV2" instead of "EquiFormerV2" (line 173).

## Nice-to-Haves

- The augmented variant of Length Extrapolation (Task 1) trains on alcohols with {2,3}∪{9,…,15} carbons and carboxylic acids with {4,…,8} carbons, then tests on the swapped combinations. This design conflates functional group identity with length distribution. An alternative that trains on alkanes with gaps (e.g., {2,…,6}∪{9,…,15}) and tests on the missing lengths {7,8} would more cleanly isolate length extrapolation from functional group effects.
- Adding simple baselines (e.g., predicting mean training energy/forces, or a linear model on hand-crafted features) would calibrate whether the observed OOD errors are genuinely large relative to trivial predictors.
- An analysis of which specific atoms or bonds contribute most to OOD errors would increase the benchmark's diagnostic value for guiding future architecture design.

## Removed Points

- *Criticism about "no comparison to simple baselines"* — This is a nice-to-have, not a weakness, as the paper's focus is on relative comparison among SOTA architectures. Moved to Nice-to-Haves.
- *Criticism about GFN2-xTB being a "methodological gap" rather than a limitation* — The paper clearly states GFN2-xTB is "known for its balance between computational efficiency and accuracy" and the dataset size would be infeasible at DFT level. Demoted to Minor weakness.
- *Harsh critic's claim that the paper "never discusses whether the generalization behavior observed on xTB labels would transfer to DFT-level targets"* — This is a valid limitation but softened to Minor as it is standard practice in this field to use a single reference method for a benchmark; the claim is not about "physical principles" being a strong phrasing choice. Retained as Minor.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Correct the figure labeling errors**: Replace "PBE0" with "PAINN" in Figure 2 and define or remove "m4s" from Figure 3. Verify that all model names in every figure match the list in Section 4.1.
2. **Add at least 3 random seeds per model-task combination** and report means ± standard deviations (or min/max ranges) for all metrics. At minimum, show that the main comparative claims (e.g., "GemNet performs best on Composition/Duplication") hold across seeds.
3. **Add a brief discussion** of how the GFN2-xTB reference level limits the scope of the claims about learning "physical principles," and ideally include a small-scale DFT verification for at least one task.
4. **Include atom-level error diagnostics** (e.g., per-atom force error heatmaps on OOD molecules) to increase the benchmark's diagnostic utility for architecture designers.

## Score and Decision

**Calibration anchors consulted (all rounds):**

| Anchor ID | Avg Score | Round | Comparison |
|-----------|-----------|-------|------------|
| TRErr3HucA | 5.50 | R1/R2 | PES smoothness benchmark + architecture; rejected. Comparable benchmark quality but our paper has figure errors. |
| UVmMNagKvK | 4.00 | R1/R2 | StructEval crystal benchmark; rejected. Our paper has better motivation, task design, and results clarity. |
| ftANj24sfU | 5.00 | R1/R2 | Dilated MP for MD; rejected. Different contribution type (method vs. benchmark). |
| heBJ8TOEZm | 4.00 | R1 | ComMat materials benchmark; rejected. Our paper is stronger in task design. |
| T8VcTykTf1 | 5.60 | R1/R2 | GGND for stable MD; accepted poster. Method + evaluation; stronger rigor but had contradictory theory claims. |
| e9cV4xSjbR | 4.67 | R1/R2 | ATOM pretrained operator; accepted poster. Method paper with benchmark; had significant rigor concerns. |
| qyjaVda7t2 | 4.50 | R2 | Scaling laws for NFFs; accepted poster. Empirical study with methodological concerns. |

Round 1 bracket: between ~4.0 and ~5.6. Round 2 narrowed: the paper is a cleanly designed benchmark with an important empirical finding, but the figure labeling errors (PBE0, m4s) and absence of uncertainty quantification place it below anchors like TRErr3HucA (5.50) and T8VcTykTf1 (5.60), while it is stronger than StructEval (4.00) and ComMat (4.00). Final score: **5.0**.

The paper addresses a well-motivated gap — compositional generalization of MLFFs — with carefully designed tasks and a finding that should influence the field. However, the figure labeling errors (PBE0 replacing PAINN in Figure 2, undefined "m4s" in Figure 3) are not trivial: they make it impossible to trust which model produced which result. Combined with the total absence of uncertainty quantification for comparative claims about model ranking, these issues prevent acceptance in the current form. The core benchmark design and empirical observation are sound and could form a strong paper after correction and strengthening.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>