## Summary

The paper introduces GMD-25, a benchmark of four compositional generalization tasks (Length Extrapolation, Functional Group Composition, Functional Group Duplication, Functional Group Combination) designed to test whether ML Force Fields learn physical principles or merely interpolate. Five architectures (SchNet, PAINN, DimeNet++, GemNet, EquiFormerV2) are evaluated. The main finding is that all models show orders-of-magnitude error increases on OOD examples, and in-distribution performance rankings do not predict OOD performance.

## Strengths

1. **Well-designed tasks that isolate specific compositional generalization challenges (Section 3.1).** Unlike prior MLFF benchmarks (MD17, MD22, Transition1x) that focus on equilibrium diversity or broad coverage, GMD-25's tasks ensure training molecules contain all building blocks needed for OOD test molecules. For example, in Task 3 (Functional Group Duplication), models trained on monocarboxylic acids are tested on dicarboxylic acids at identical chain lengths — cleanly isolating motif repetition as the specific challenge.

2. **Augmented task variants control for trivial explanations of failure (Section 3.1).** Both Tasks 1 and 2 include variants where all chain lengths or functional group components appear in training data (just in different contexts), yet models still fail. This strengthens the case that failures reflect deeper generalization deficits, not merely missing length information.

3. **Empirical finding that ID performance does not predict OOD performance (Figures 2–4, Section 4.3).** EquiFormerV2 achieves the lowest forces MAE on Length Extrapolation but suffers dramatic energy MAE degradation OOD, while SchNet and DimeNet++ show more stable OOD energy predictions despite worse forces. This is a concretely useful result for practitioners deciding which architecture to deploy.

## Weaknesses

### Fatal
None.

### Major

1. **Undescribed models appear in figure captions.** Figure 2 (base Length Extrapolation) lists "PBE0" as one of five evaluated models, alongside EquiFormerV2, DimeNet++, SchNet, and GemNet. Figure 3 (augmented Length Extrapolation) lists "m4s" as one of six models alongside DimeNet++, GemNet, EquiFormV2, PAINN, and SchNet. Neither PBE0 nor m4s are described anywhere in the main text: not in Section 4.1 (Models, which lists exactly five architectures — SchNet, PAINN, DimeNet++, GemNet, EquiFormerV2), not in the results discussion (lines 134–136, which never mention PBE0 or m4s), and nowhere else in the paper. PBE0 conventionally refers to a DFT functional (not an ML model); m4s is not identifiable from the paper's content. This inconsistency means a reader cannot determine what was actually evaluated. This must be resolved before the results can be fully interpreted.

2. **No numerical result tables.** The paper reports all results exclusively through figures (Figures 2–4). For a benchmark paper that the community is expected to use for future comparison, this is a practical limitation — future work cannot reference baseline numbers without re-extracting from figures or downloading code. Numerical tables listing per-task ID and OOD MAE would significantly increase the benchmark's utility.

### Minor

3. **No variance reporting.** The paper reports a single MAE per model per task with no indication of variance across random seeds or training runs (no mention of multiple seeds anywhere). While the core finding (all models fail dramatically OOD) is robust enough to survive single runs, comparative claims (e.g., "EquiFormerV2 performed the best on Length Extrapolation in terms of forces MAE," line 166) are weakened by the absence of statistical grounding.

4. **No dedicated limitations section.** Key limitations worth acknowledging: (a) GFN2-xTB is an approximate semi-empirical method — reference labels have their own errors; (b) the benchmark is limited to gas-phase vacuum simulations of small organic molecules; (c) models are trained from scratch — transfer learning or foundation model fine-tuning may behave differently.

5. **No per-task data split breakdown.** The paper reports 118 molecules and 296,534 geometries total but does not break down per-task training/ID-test/OOD-test sizes.

### Trivial

6. **None beyond the above.**

## Nice-to-Haves

- A diagnostic analysis of *why* models fail (e.g., is failure on length extrapolation driven by architectural capacity limits or target distribution shift?) would increase the benchmark's diagnostic value.
- Computational cost comparison (training time, inference cost per model) would help practitioners decide which architectures to invest in.
- Providing multiple random seed results would strengthen the comparative claims about model rankings.

## Removed Points

- **"Fatal inconsistency that results are uninterpretable" (Harsh Critic).** This is an overstatement. The core finding (all described models fail OOD) is still supported. PBE0 and m4s appear to be additional baselines that were included in figures but not described — a fixable presentation issue, not a validity issue for the main claim.
- **"Augmented variant is mismatched to framing" (Harsh Critic).** The paper clearly describes what the augmented variant tests and explicitly acknowledges it "might be easier." The labeling as a variant of Length Extrapolation within a compositional generalization framework is reasonable; this is a framing preference, not a methodological gap.
- **Generic strengths from Strength Finder** ("important problem," "interesting question"). These lack specific evidence and are dropped.
- **Criticism about missing related works.** Cannot verify without external sources; all standard references appear to be covered.
- **Formatting/style nitpicks.** Parser artifacts, not author errors.

## Novel Insights

The harsh critic's identification of PBE0 and m4s in figure captions without any description in the main text is genuinely useful — this is a verifiable, specific, and consequential issue that the Strength Finder missed entirely. Interestingly, the harsh critic's most useful finding is a concrete presentation inconsistency rather than a methodological gap. The contrast shows that even when a reviewer's severity is over-calibrated, their close reading of figures versus text can surface real problems.

## Suggestions

1. **Clarify PBE0 and m4s.** Either describe them properly in Section 4.1 (if they are additional baselines) or correct the figure captions to remove them (if they are errors). If PBE0 is a DFT-level reference calculation, specify the computational parameters and what it adds to the comparison.
2. **Add a numerical results table** showing per-task ID and OOD MAE with model ranking so future work can reference baselines directly.
3. **Add a limitations section** acknowledging the GFN2-xTB approximation and gas-phase scope.
4. **If feasible, report results from 3+ random seeds** for the key comparative claims.

---

**Calibration Anchors (all rounds):**

| Paper (path) | Round | Avg Score | Comparison |
|---|---|---|---|
| ItPYVON0mI (ML CG potentials) | R1 | 3.00 | Much weaker — method paper with little benchmarking content |
| 1JgWwOW3EN (BenchMol) | R1 | 4.80 | Weaker — comprehensive MRL benchmark but had quality concerns; GMD-25 has cleaner task design |
| ihwRfc4RNw (MatText) | R1 | 4.00 | Weaker — thin empirical contributions; GMD-25 has more novel task design |
| NvJxTjTQtq (EGraFFBench) | R1 | 6.00 | Stronger — more comprehensive (8 datasets, 6 models, new metrics); GMD-25 is narrower and has the PBE0/m4s issue |
| Xk9Q0CrJQc (MLFF shifts) | R2 | 6.25 | Stronger — proposes mitigation methods alongside OOD analysis |
| qFZnAC4GHR (AU-GOOD) | R2 | 6.67 | Stronger — methodologically sophisticated OOD evaluation framework |
| zyBJodMrn5 (multimodal comp. gen.) | R2 | 5.67 | Slightly stronger — accepted paper on compositional generalization with less practical domain impact |
| tHHzfZSP6T (Transformer capabilities) | R2 | 5.00 | Comparable — similar score, also rejected |
| Hxm0hOxph2 (provable comp. gen.) | R2 | 5.25 | Comparable — similar score, also rejected |
| Bq3fEAGXUL (model merging) | R2 | 5.33 | Comparable — similar score, also rejected |
| 7Jer2DQt9V (graph OOD pretraining) | R2 | 4.50 | Slightly weaker — thinner empirical results |
| an3kPpce6b (3D molecule OOD) | R2 | 5.25 | Comparable — similar score |

**Round 1 bracket:** 4.0–6.0
**Round 2 narrowing:** After comparing against anchors inside the bracket, particularly EGraFFBench (6.0, stronger/more comprehensive) and MatText (4.0, weaker/thinner), GMD-25 sits closest to the 5.0–5.33 cluster (tHHzfZSP6T at 5.0, Hxm0hOxph2 at 5.25, Bq3fEAGXUL at 5.33). The paper has a genuinely novel task design that MatText lacks, but the PBE0/m4s model inconsistency is a concrete flaw that EGraFFBench does not have. Score 5.0 reflects this trade-off.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>