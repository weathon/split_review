Now I have all the information I need. Let me synthesize the final review.

**Round 1 bracket**: Based on calibration search for similar benchmarks, the paper sits between the weak anchors (~3.0–3.4, not topically similar) and the strong anchors (8.0, also not topically similar). The informative band is the middle: anchors for MLFF benchmarks and OOD evaluation papers score 5.25–6.67. Narrowest plausible bracket: **5.5–6.5**.

**Round 2 anchors** (read in full):
- EGraFFBench (6.00, Reject) — similar benchmark paper, had implementation correctness concerns. GMD-25 is cleaner but shares a weakness in statistical rigor.
- GDL-DS (5.67, Reject) — OOD benchmark for GDL, flawed causal framing. GMD-25 has cleaner framing.
- Underst. Dist. Shifts for MLFFs (6.25, Reject) — methodological contribution (test-time refinement). GMD-25 is benchmark-only.
- Pushing Limits (6.50, Accept) — pre-training scaling analysis, more experiments.
- MARCEL (6.33, Accept) — benchmark paper on conformer ensembles, accepted.
- AU-GOOD (6.67, Accept) — novel OOD metric, accepted.

**Final calibration**: GMD-25 is cleaner than EGraFFBench (6.00) but has weaker statistical rigor than accepted benchmarks like MARCEL (6.33). Its task design is more novel than EGraFFBench but it lacks the methodological depth of Pushing Limits (6.50). Score: **6.0**.

---

## Summary

This paper introduces **GMD-25**, a benchmark for evaluating compositional generalization of machine-learning force fields (MLFFs). It defines four controlled tasks—Length Extrapolation, Functional Group Composition, Functional Group Duplication, and Functional Group Combination—each designed so that training data contains all components needed for generalization, enabling diagnosis of whether models learn transferable physical principles or merely interpolate. Five state-of-the-art MLFFs (SchNet, PAINN, DimeNet++, GemNet, EquiFormerV2) are evaluated, and the core empirical finding is that all models show error increases of one to two orders of magnitude on out-of-distribution molecules.

## Strengths

- **Systematic, well-motivated task design.** Each of the four tasks isolates a specific compositional generalization failure mode (length extrapolation, composing functional groups, duplicating motifs, recombining groups asymmetrically). The training splits are constructed so that all components needed for generalization appear in training, making the tasks diagnostic rather than merely hard. This is a genuine gap relative to existing MLFF benchmarks (MD17, Transition1x, MD22), which test interpolation within known molecules or broader coverage but not compositional generalization.

- **Clear and important empirical finding.** Every evaluated model, spanning invariant GNNs (SchNet), equivariant message-passing (PAINN, DimeNet++, GemNet), and transformers (EquiFormerV2), exhibits dramatic OOD degradation (1–2 orders of magnitude). This consistent failure across diverse architectures makes a compelling case that current MLFFs do not learn transferable physical principles—a finding that standard benchmarks cannot surface.

- **ID–OOD performance inversion.** The benchmark reveals that models with the lowest in-distribution error are not always the best generalizers, and different metrics (energy MAE vs. forces MAE) can rank models oppositely in the OOD regime. For example, EquiFormerV2 achieves the lowest forces MAE on Length Extrapolation OOD but its energy MAE degrades catastrophically, while SchNet and DimeNet++ maintain more stable energy MAE. This finding, uniquely surfaced by the benchmark's controlled splits, has direct implications for architecture design.

- **Extensible toolkit and clean release pipeline.** The data generation toolkit (ASE, RDKit, FlashMD, XTB-Python) is standardized and modular, and the dataset (118 molecules, 296k labeled geometries) with curated splits will be released. This lowers the barrier for community adoption and extension.

## Weaknesses

### Major

- **No multiple runs or error bars.** All results are from single training runs per model-task combination. No standard deviations, confidence intervals, or seed sensitivity analyses are reported. While the core finding (all models show large OOD degradation) is robust because the gaps span orders of magnitude across *every* model, the more nuanced comparative claims—e.g., "EquiFormerV2 consistently exhibits the lowest Forces MAE" or "SchNet and DimeNet++ exhibit more stable energy predictions in the OOD region"—cannot be verified without evidence of statistical reliability. Given that neural network training is stochastic, especially with Bayesian hyperparameter tuning, the model rankings should be interpreted as preliminary. This is the paper's most significant limitation and should be addressed with at least 3–5 seeds with reported means and standard deviations.

### Minor

- **No simple baseline for task difficulty calibration.** The paper compares five learned MLFFs against each other but provides no trivial reference point (e.g., predicting the per-atom mean force/energy from the training set, or a linear model on a fixed featurization). Such a baseline would help readers contextualize the reported OOD error magnitudes: a forces MAE of 0.5 eV/Å may look large or small depending on what a trivial predictor achieves. Adding this would strengthen the benchmark's diagnostic value at minimal cost.

- **Functional Group Composition task underspecified.** The task trains on alcohols and aldehydes and tests on carboxylic acids, on the premise that the carboxylic acid group is a "composition" of the alcohol and aldehyde groups. The paper acknowledges that "we do not expect the model to learn the chemical reaction pathway" (Section 3.1), but the justification for why a physically faithful force field *should* compositionally generalize here is not fully developed. A carboxylic acid has qualitatively different electronic structure and hydrogen-bonding behavior from its constituents. The universal failure of all models on this task may partly reflect this inherent mismatch rather than a failure of compositional generalization *per se*. The task is still useful as a stress test, but the framing should more explicitly acknowledge this assumption.

- **GFN2-xTB reference method not discussed as a limitation.** Ground truth labels are computed with GFN2-xTB, a semi-empirical tight-binding method rather than DFT. While this choice is standard for a dataset of this scale (~300k geometries) and GFN2-xTB is well-validated for organic molecules, the paper does not quantify or discuss the accuracy trade-off relative to DFT. Since one of the stated goals is probing whether models learn "physical principles," any discrepancy between GFN2-xTB and true DFT-level physics introduces a confound: models could fail on OOD molecules because the reference potential itself is less reliable for those molecules. A brief acknowledgment of this limitation would strengthen the paper's scientific framing.

### Trivial

- No comparison of training time or inference cost across models, which limits practical guidance for model selection.
- The related work section on compositional generalization in NLP (COGS, CFQ, SCAN) is very brief; citing these directly would help readers see the connection to the established compositional generalization literature.

## Nice-to-Haves

- A per-task qualitative analysis of *why* models fail (e.g., attention pattern visualizations, analysis of predicted energy components for one or two failure cases) would substantially strengthen the diagnostic value of the benchmark beyond descriptive error reporting.
- Including a discussion of whether foundation models (e.g., MACE-MP-0) close the OOD gap, and what that would imply, would sharpen the paper's impact even though their exclusion is defendable.

## Removed Points

- "Weakness about excluding foundation models (MACE, NequIP)" — The paper explicitly scopes this out in Section 4.1 with a clear rationale (pretrained models confound memorization vs. generalization). This is a design choice, not a weakness.
- "Weakness about the paper not discussing whether hyperparameters tuned on ID data might suboptimize OOD performance" — This is standard practice; criticizing it without evidence that ID-tuned HPs are poor for OOD is speculative.
- "Weakness about the FLOPs/computational cost" — Moved to trivial; relevant for practitioners but not central to a benchmark paper's contribution.
- "Weakness about lack of multiple seeds for data generation" — While two trajectories per molecule is noted, requesting more is a nice-to-have; the data scale is already substantial (296k geometries).
- Several generic strengths from the Strength Finder (e.g., "addresses an important problem") — removed as insufficiently specific to this paper's execution.

## Novel Insights

Beyond the paper's own contributions, the most interesting emergent observation is the **metric-dependent inversion** of model rankings in the OOD regime. The fact that EquiFormerV2 dominates on forces MAE while collapsing on energy MAE (and vice versa for SchNet/DimeNet++) suggests that architectural inductive biases create a trade-off between different physical quantities during OOD generalization—a finding that could motivate more principled multi-objective architecture design for MLFFs. The paper does not fully explore this implication, but the data clearly supports it.

## Suggestions

1. **Add 3–5 seeds with means and standard deviations** for all experiments. This is the single most impactful change. Report both the main findings (all models fail OOD) with the range across seeds, and flag which comparative claims survive statistical scrutiny.
2. **Add a trivial baseline** (e.g., training-set mean force/energy predictor) to calibrate the OOD error magnitudes across tasks.
3. **Explicitly discuss the GFN2-xTB limitation** in a dedicated paragraph in Section 3, and the assumption behind Task 2's compositionality claim.
4. **Add a short subsection or paragraph** with qualitative analysis of one or two failure cases to demonstrate how the benchmark can diagnose *why* a model fails, not just that it fails.

## Score and Decision

**Average anchor scores (all rounds):**

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| EGraFFBench (NvJxTjTQtq) | 6.00 | 1 | Topically closest; GMD-25 has cleaner implementation but shares the error-bars gap |
| Underst. Dist. Shifts (Xk9Q0CrJQc) | 6.25 | 1 | More methodological (test-time refinement); GMD-25 is benchmark-only |
| Pushing Limits (4S2L519nIX) | 6.50 | 1 | Stronger experimental scope; GMD-25 has more novel task design |
| Steering 3D (an3kPpce6b) | 5.25 | 1 | Different subproblem (generation not prediction) |
| GDL-DS (LixGd92Wri) | 5.67 | 2 | Broader but had flawed causal framing; GMD-25 is cleaner |
| MARCEL (NSDszJ2uIV) | 6.33 | 2 | Accepted benchmark paper; GMD-25 has comparable contribution level |
| AU-GOOD (qFZnAC4GHR) | 6.67 | 2 | More methodological novelty; GMD-25 is a different contribution type |
| BenchMol (1JgWwOW3EN) | 4.80 | 2 | Broader but weaker; GMD-25 is more focused and rigorous |
| Multi-Grained (J4V3lW9hq6) | 5.00 | 2 | Different subproblem |

**Round 1 bracket**: 5.5–6.5. **Final score**: 6.0 (cleaner than EGraFFBench at 6.00 which had implementation concerns; less experimental scope than Pushing the Limits at 6.50; comparable to the accepted MARCEL benchmark at 6.33 but slightly weaker on statistical rigor).

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>