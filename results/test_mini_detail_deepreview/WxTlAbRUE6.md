Now let me produce the final review.

## Summary

This paper introduces GMD-25, a benchmark for evaluating compositional generalization of machine learning force fields (MLFFs). It defines four tasks — Length Extrapolation, Functional Group Composition, Functional Group Duplication, and Functional Group Combination — that test whether models can generalize to molecules with longer carbon chains or novel combinations of functional groups that were not seen during training. The benchmark is built on GFN2-xTB semi-empirical reference calculations. An evaluation of five popular MLFFs (SchNet, PAINN, DimeNet++, GemNet, EquiFormerV2) shows that all models exhibit OOD errors that are often 1–2 orders of magnitude larger than ID errors, and that ID performance does not predict OOD performance.

## Strengths

1. **Principled compositional-generalisation task design.** The four tasks isolate specific aspects of compositionality (length extrapolation and systematicity) with clear training/OOD splits and explicit rationale for why generalization should theoretically be possible. Each task has a controlled setup: e.g., Task 1 tests whether models extrapolate from alkanes C2–C6 to C7–C13, while Task 3 tests generalization from mono- to di-carboxylic acids with identical chain lengths. This is a genuine advance over existing MLFF benchmarks (MD17, MD22, Transition1x) which do not systematically probe compositional generalization.

2. **Empirical finding that ID performance does not predict OOD performance.** The paper demonstrates concretely that the best ID model is often not the best OOD model — for example, EquiFormerV2 achieves the lowest Forces MAE on Length Extrapolation but its Energy MAE degrades to worst among all models. This finding is a useful signal for the community and goes beyond simply reporting that OOD is harder.

3. **Reproducible pipeline.** The dataset generation workflow (RDKit → FlashMD → GFN2-xTB → ASE orchestration) is clearly described, and the authors state they will release the full dataset and toolkit. The curated splits and pre-processing scripts accompany the release.

## Weaknesses

### Fatal
None.

### Major

1. **Figure/model inconsistencies that undermine trust in the results.** Section 4.1 lists the evaluated models as SchNet, PAINN, DimeNet++, GemNet, and EquiFormerV2. However, the Figure 2 caption references "PBE0" (an orange squares series) and omits PAINN from the legend. The Figure 3 caption introduces an unlisted model "m4s" alongside six total models including PAINN. Figure 4 (correctly) matches the Section 4.1 model list. These discrepancies mean a reader cannot trust which models actually generated the plotted results. For a benchmark paper whose entire evidence is comparative, this is a serious flaw — the conclusions about relative model performance rest on attribution that is inconsistent across figures. *Verified from the paper: Section 4.1 (line 131–133) lists five models; Figure 2 caption (line 149) replaces PAINN with PBE0; Figure 3 caption (line 173) adds m4s as a 6th model.*

2. **No uncertainty quantification across runs.** Not a single result reports error bars, standard deviations, or confidence intervals. Model training for MLFFs is stochastic (weight initialization, data shuffling, optimizer noise). Without multiple independent runs, the reported differences between models (e.g., "EquiFormerV2 performed the best on Length Extrapolation in terms of forces MAE") cannot be assessed for statistical significance and may reflect noise rather than systematic advantages. This is especially problematic for a benchmark intended to compare architectures. *Verified from the paper: the experimental setup (Section 4.2) describes hyperparameter tuning but never mentions random seeds or number of repeated runs; no error bars appear in any figure.*

3. **Misleading "ab initio" framing of the reference calculations.** The paper calls the trajectories "ab initio molecular dynamics (AIMD)" (line 55), but Section 3 explicitly states labels come from the GFN2-xTB semi-empirical tight-binding method (line 85), which is not ab initio/DFT. This mischaracterization is significant because semi-empirical methods have known systematic biases, and the paper's conclusions about generalization may not transfer to DFT-level reference data. The authors should transparently frame this as a semi-empirical benchmark. *Verified from the paper: line 55 says "ab initio molecular dynamics (AIMD) trajectories"; line 85 says "energy and forces were calculated using the GNF2-xTB semi-empirical tight-binding approach."*

### Minor

4. **The "augmented" task variants are not clearly established as compositional generalization tasks.** The augmented Length Extrapolation variant (Task 1) trains on alcohols with chain lengths {2,3}∪{9,…,15} and tests alcohols with lengths {4,…,8}. Since all chain lengths appear in the training set, this looks more like interpolation over functional-group×length combinations than true compositional generalization. The paper acknowledges this may be easier but does not fully argue why it still qualifies as a compositional generalization test.

5. **Missing discussion of the GFN2-xTB limitation.** The paper acknowledges GFN2-xTB in Section 3 but does not discuss how using a semi-empirical (rather than DFT) reference might affect conclusions about generalization. Models that learn to approximate semi-empirical labels may not transfer to true DFT-level physics. A brief discussion of this limitation and the rationale for using GFN2-xTB as a proxy would strengthen the paper.

### Trivial
None.

## Nice-to-Haves

- Adding simple baselines (e.g., nearest-neighbor prediction, linear regression on structural features) would quantify the difficulty of each task relative to trivial predictors.
- An analysis of per-atom force errors by functional group or by chain length would strengthen the claim that errors are compositional rather than generic.

## Removed Points

The following points from the inputs are removed with justification:

- *"Related work overlap is overstated; MD22 and Transition1x also test extrapolation."* The paper's Section 2.3 already acknowledges these benchmarks and provides a reasonable contrast — MD22 tests larger systems but not compositional generalization, Transition1x tests off-equilibrium geometries but not compositional recombinations. This criticism does not hold up against the paper's clear scoping.
- *"Model selection excludes non-neural baselines (kernel methods, nearest-neighbor)."* While a reasonable suggestion, this is scope creep for a benchmark focused on neural MLFFs. Moved to Nice-to-Haves.
- *"Reproducibility: toolkit not yet released, appendix stripped, computational resources not mentioned."* These are standard for a conference submission under review; the paper states the toolkit will be released upon acceptance.
- *"Augmented variants are interpolation not compositional generalization."* The paper already acknowledges the augmented variant may be easier (Section 3.1). Retained as Minor (point 4 above) rather than Major.
- *"PAINN absent from Figure 2."* This is folded into the Major weakness about figure inconsistencies (point 1), not a separate issue.
- *"Small font and overlapping curves in figures."* Parser artifact; the figures are embedded images that render fine in original PDF.
- *"Hyperparameter tuning biased against OOD."* This is standard practice and the paper acknowledges tuning is on ID performance. Not a real flaw.
- *Strength Finder's generic strengths about "important problem" / "timely topic"* — removed as they lack specific evidence anchored in the paper.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface an angle that the paper itself missed.

## Suggestions

1. **Fix the figure/model inconsistencies immediately.** Clarify whether PBE0 and m4s are labeling errors, model variants, or different models entirely. Ensure every figure legend matches the model list in Section 4.1 exactly. If the same plot was generated with different model configurations, document this transparently.
2. **Run all experiments with at least 3 random seeds and report mean ± std.** This is the single most impactful improvement for a benchmark paper.
3. **Replace "ab initio" with "semi-empirical" throughout** when referring to the GFN2-xTB reference, or clearly qualify the term.

## Score and Decision

**Calibration Anchors:**

| Paper | Path | Avg Score | Round | Comparison |
|-------|------|-----------|-------|------------|
| EGraFFBench | NvJxTjTQtq.md | 6.00 | 1 (middle) | Benchmark paper on equivariant GNN force fields with similar evaluation scope. Current paper has better task design but worse execution (model inconsistencies, no error bars). Weaker than this anchor. |
| DistShift MLFFs | Xk9Q0CrJQc.md | 6.25 | 1 (middle) | Proposes mitigation methods for OOD shifts in MLFFs. More comprehensive than current paper which only diagnoses failure. Current paper is weaker. |
| AU-GOOD OOD framework | qFZnAC4GHR.md | 6.67 | 2 (narrow) | Formal framework for OOD evaluation in biochemical domain. Cleaner theoretical contribution. Accepted. Current paper is notably weaker in execution polish. |
| MARCEL conformer benchmark | NSDszJ2uIV.md | 6.33 | 2 (narrow) | Benchmark on conformer ensemble learning. Well-executed, accepted. Current paper has more interesting task design but significantly worse presentation consistency. |
| BenchMol | 1JgWwOW3EN.md | 4.80 | 1 (middle) | Benchmark platform for molecular representation learning. Highly split review (10,1,5,3,5). Current paper has more principled task design and is slightly stronger overall. |
| DynamicsDiffusion | kKXIYUi8ff.md | 3.00 | 1 (low) | Method paper, not comparable. |

**Round-1 Bracket:** 4.5 – 6.5  
**Round-2 Narrowing:** The paper is weaker than EGraFFBench (6.00) and the conformer benchmark (6.33) due to execution issues, but stronger than BenchMol (4.80). Final score: **5.0**.

**MY FINAL SCORE: <score>5.0</score>**
**MY FINAL DECISION: <decision>Reject</decision>**