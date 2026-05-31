Now I have enough information for final calibration. Let me write the final review.

## Final Review

**Calibration Summary:**

| Anchor Paper | Avg Score | Round | Comparison |
|---|---|---|---|
| DynamicsDiffusion (kKXIYUi8ff) | 3.00 | R1 | Much weaker — different topic, serious flaws |
| CG Potentials (ItPYVON0mI) | 3.00 | R1 | Much weaker — narrow scope, significant issues |
| BenchMol (1JgWwOW3EN) | 2.50 | R1 | Much weaker — lacks specific contribution |
| EGraFFBench (NvJxTjTQtq) | 6.00 | R1/R2 | Similar benchmark paper, cleaner presentation, comparable contribution |
| Force-Guided Bridge Matching (NSlvSDQ8aE) | 7.00 | R1 | Stronger paper, cleaner results, accepted-quality work |
| LiFlow (CkozFajtKq) | 6.33 | R1 | Stronger paper, proposes method + evaluation |
| Molecule Relaxation (rwmWd2rjP1) | 4.75 | R1/R2 | Comparable quality, different domain |
| Understanding Mitigating MLFF (Xk9Q0CrJQc) | 6.25 | R2 | Stronger paper — proposes mitigation methods plus analysis |
| AU-GOOD (qFZnAC4GHR) | 6.67 | R2 | Stronger paper — accepted, more polished presentation |
| GDL-DS (LixGd92Wri) | 5.67 | R2 | Comparable benchmark, similar quality |

**Round 1 bracket**: 4.5–6.5 (clearly above weak anchors at ~3.0, clearly below strong anchors at 7.5+)

**Round 2 narrowing**: Among comparable papers (4.75–6.67), this paper sits in the lower end. EGraFFBench (6.00) achieves cleaner presentation with fewer ambiguities. The AU-GOOD paper (6.67, accepted) is more polished. The "Understanding Mitigating MLFF" paper (6.25) adds a methodological contribution. Our paper has better task design than GDL-DS (5.67) but worse presentation. Final anchor cluster puts this paper around **5.0**.

---

## Summary

This paper introduces GMD-25, a benchmark for evaluating compositional generalization in Machine Learning Force Fields (MLFFs) through four systematically designed tasks: Length Extrapolation, Functional Group Composition, Functional Group Duplication, and Functional Group Combination. The benchmark uses GFN2-xTB to generate AIMD trajectories for 118 molecules (296k labeled geometries) and evaluates five SOTA MLFFs (SchNet, PAINN, DimeNet++, GemNet, EquiFormerV2). The core finding is that all models suffer catastrophic OOD failures with errors 1–2 orders of magnitude higher than ID errors, and ID performance does not predict OOD generalization.

## Strengths

- **Systematic task design that isolates specific compositional generalization challenges**: The four tasks cleanly separate length generalization from different forms of systematicity (composition, duplication, combination). For example, the Functional Group Duplication task trains on mono-carboxylic acids and tests on di-carboxylic acids, isolating whether models can reuse a learned pattern in a repeated context (§3.1). This is a clear methodological improvement over existing MLFF benchmarks (MD17, MD22, Transition1x) which do not decompose generalization into atomic challenges.

- **Strong and consistent negative finding across all architectures**: The empirical results (§4.3, Figures 2–4) convincingly show that all five evaluated models exhibit OOD errors one to two orders of magnitude higher than ID errors on every task. Energy MAE on Functional Group Duplication shows OOD errors "higher by two orders of magnitude" compared to ID errors (§4.3). This finding is robust across architectural families (invariant GNNs, equivariant message-passing, Transformers).

- **ID performance does not predict OOD generalization**: The paper demonstrates a striking decoupling — EquiFormerV2 achieves the best ID force errors but simultaneously has poor OOD energy errors, while SchNet and DimeNet++ show the opposite pattern (§4.3). This provides concrete evidence that standard ID-only benchmarks (the norm in MLFF evaluation) give a misleading signal about model quality.

- **Extensible toolkit and dataset release**: The paper introduces a Python toolkit (§3.2) that automates the pipeline from SMILES to AIMD trajectories, releasing 118 molecules with 296,534 labeled geometries and curated splits. The toolkit is designed for extension to new molecular families, differentiating it from one-off static datasets.

- **Theoretical grounding in compositional generalization literature**: The benchmark connects to formal concepts from NLP/cognitive science (Hupkes et al., 2020 on length generalization and systematicity; Xu et al., 2020 on algorithmic alignment), giving the task definitions a principled basis (§2.2).

## Weaknesses

### Fatal
None.

### Major

- **Figure captions contain inconsistent and undefined model labels**: Figure 2 caption lists "PBE0" as a model — PBE0 is a DFT functional, not an MLFF, and is never defined in the paper text. This caption also omits PAINN (listed in §4.1 as one of the five evaluated models). Figure 3 caption lists "m4s" (completely undefined in the paper) alongside "EquiFormV2" (typo for EquiFormerV2). While the textual discussion in §4.3 only refers to the five models from §4.1, a reader cannot confidently map figure curves to specific models. This undermines trust in the specific comparative claims (e.g., which model "performed the best" on which metric), which are a central part of the paper's contribution.

### Minor

- **No statistical uncertainty reported**: All results are single-point estimates with no error bars, confidence intervals, or multiple-seed runs. For a benchmark drawing comparative conclusions about model rankings, it is unclear whether observed differences between models are statistically significant. The large OOD vs. ID gaps (orders of magnitude) are likely robust, but more nuanced comparisons — which model performed "best" on each metric — cannot be evaluated without variance estimates.

- **GFN2-xTB as ground truth is not critically examined**: The paper uses GFN2-xTB (a semi-empirical tight-binding method, §3) for energy/force labels. While noting it balances efficiency and accuracy, the paper does not discuss whether GFN2-xTB's known systematic biases could confound the generalization measurements. If the reference method itself extrapolates poorly to larger molecules or novel functional-group combinations, the MLFF errors might partly reflect inaccuracies in the training labels rather than a failure of the ML architectures. Validation against higher-fidelity methods (e.g., DFT on a subset) is absent.

- **Limited diagnostic analysis of why models fail**: The paper reports the negative finding that all models fail but offers no diagnostic experiments to explain *why*. For example: does error in the Duplication task correlate with distance between functional groups (suggesting a receptive-field limitation)? Do models with more layers or larger cutoff radii generalize better? The paper identifies a critical gap but stops short of providing actionable architectural insights beyond a call for "more robust, physically-informed models."

- **Augmented vs. base variant comparison is confounded**: Both the training molecules and the split logic change simultaneously between the base and augmented variants of Tasks 1–2 (§3.1). The claim that the augmented variant "should be easier" is plausible but not rigorously justified, as the two variants differ in multiple dimensions.

### Trivial
None.

## Nice-to-Haves

- A mapping table linking each model name to figure legend symbols would resolve the caption ambiguities.
- Running models with 3–5 random seeds and reporting mean ± std would strengthen comparative claims.
- Validating GFN2-xTB against DFT on a small subset of OOD configurations would address the ground-truth concern.
- Including diagnostic analysis for at least one task (e.g., correlating error with inter-group distance for duplication) would deepen the contribution.

## Removed Points

- **"Feasible" assertion in Introduction**: The harsh critic claimed the paper pre-judges tasks as "feasible." This is a framing nitpick; the paper introduces a benchmark to test this very question, not to assert a foregone conclusion.
- **ID test set starting at C4 in Figure 2**: The paper states ID range is C2–C6 in §3.1. The figure axis starting at C4 is a visualization choice; the training range is clearly specified in text.
- **Missing hyperparameter details / appendix content**: The paper explicitly states these are in the appendix (§4.2: "The resulting optimised hyperparameters can be found in the appendix"). The appendix was stripped by the PDF parser.
- **Missing related works**: Cannot verify without external sources.
- **Formatting/style nitpicks**: Parser artifacts, not author errors.
- **Missing foundation models**: The paper explicitly scopes out foundation models (§4.1: "we did not include any foundation models...making it harder to untangle memorisation and generalisation effects"). This is a deliberate, justified design choice.
- **Task 4 non-compositional physical effects**: The concern about steric/electronic interactions is a reasonable discussion point but not a flaw — the task tests systematicity, and any non-compositional effects are precisely what makes the task a valid probe of generalization.

## Novel Insights

None beyond the paper's own contributions. The figure-caption inconsistencies were not independently noticed by the Strength Finder and emerged primarily from the Harsh Critic; the GFN2-xTB ground-truth concern is worth noting as a potential confound that the paper does not address.

## Suggestions

1. **Fix the figure captions (critical)**: Provide a clear mapping from model names to legend entries. Clarify whether PBE0 is a DFT baseline or a labeling error; define "m4s" or correct it to the intended model name. A simple table mapping each model to its figure-legend symbol and noting which tasks it appears in would resolve the ambiguity.

2. **Add uncertainty quantification**: Run each model with 3 random seeds and report mean ± std for all metrics. This would confirm whether the rank ordering of models is statistically meaningful.

3. **Include a limitations section** discussing GFN2-xTB's potential biases and scoping the benchmark's claims accordingly.

4. **Add diagnostic analysis for at least one task** (e.g., does duplication error correlate with functional group separation distance? does cutoff radius affect OOD performance?) to turn the benchmark from a reporting tool into an analytical one.

5. **Add brief DFT validation** on a small subset (5–10 configurations per task) to establish whether GFN2-xTB and DFT agree on the relative difficulty of ID vs. OOD molecules.

## Score and Decision

- **Originality**: 6/10 — The compositional generalization framing for MLFFs is novel and well-motivated, though benchmarking OOD performance itself has prior art.
- **Importance of research question**: 8/10 — The question of whether MLFFs learn physics or interpolate is timely and practically important.
- **Claims supported**: 5/10 — The headline claim (all models fail at OOD) is well-supported, but specific comparative claims are weakened by figure caption issues and lack of uncertainty quantification.
- **Soundness of experiments**: 5/10 — Task design is strong, but the ground-truth method choice is not critically examined, and absence of error bars limits evidential strength.
- **Clarity of writing**: 5/10 — Generally clear, but figure caption inconsistencies undermine interpretability of results.
- **Value to community**: 7/10 — The benchmark fills a genuine gap and the extensible toolkit is valuable, assuming the presentation issues are fixed.

The paper's core contribution — a principled compositional generalization benchmark for MLFFs — is real, useful, and well-motivated. The negative finding that all evaluated models fail is potentially impactful. However, the figure caption inconsistencies (PBE0 undefined, m4s undefined, PAINN absent from Figure 2) are a significant presentation flaw that makes specific comparative claims unverifiable from the paper alone. Combined with the absence of uncertainty quantification and limited diagnostic depth, these concerns prevent acceptance in the current form. A corrected version addressing these issues would be suitable for resubmission.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>