## Summary
The paper introduces GMD-25, a benchmark for compositional generalisation in Machine Learning Force Fields (MLFFs) with four tasks (length extrapolation, functional-group composition, duplication, and combination). Five popular MLFFs (SchNet, PAINN, DimeNet++, GemNet, EquiFormerV2) are evaluated, and all show one-to-two-orders-of-magnitude error blow-ups OOD; the authors release a configurable toolkit (RDKit + FlashMD + GFN2-xTB + ASE).

## Strengths
- A clean four-task taxonomy that operationalises Hupkes et al.'s notion of compositional generalisation in a molecular setting (Section 3.1), which is a genuinely useful conceptual decomposition for MLFFs.
- The compositional cross-molecule split is distinct from prior MLFF benchmarks (MD17, MD22, Transition1x, ANI-1) that primarily split by configuration within a molecule (Section 2.3), so the gap targeted is real.
- A reproducible, extensible data-generation pipeline (Section 3.2) and dataset of 118 molecules / 296,534 frames that enables others to construct similar splits.
- The empirical observation that ID and OOD model rankings diverge (e.g., EquiFormerV2 lowest force MAE but worst energy MAE OOD; Section 4.3, Figure 2) is a useful diagnostic finding if it survives more rigorous evaluation.

## Weaknesses

### Fatal
None.

### Major
- **Total-energy MAE used across splits with systematically different system size.** Equation in Section 4.2 defines $\mathrm{MAE}_{\text{energy}}$ per molecule with no division by atom count. Task 1 trains on $C_2$–$C_6$ alkanes and tests on $C_7$–$C_{13}$ (up to ~3× more atoms). Because energy is extensive, even a model with constant per-atom error will show a roughly linear rise in total-energy MAE across the ID→OOD boundary. Some fraction of the "orders of magnitude" gap in Figures 2(a) and 3(a,c) is therefore a metric artefact rather than a generalisation failure. Per-atom or extensivity-corrected reporting is needed to support the headline claim for Task 1, and is recommended for all tasks given that OOD molecules in Tasks 2–4 also vary in atom count.
- **Reference labels are GFN2-xTB, but the framing repeatedly appeals to DFT-level physics.** Section 1 motivates MLFFs as replacements for DFT, but Section 3 reveals all labels are semi-empirical tight-binding. Apparent compositional failures on Tasks 2–4 (carboxylic acids, dicarboxylic acids, mixed donor/acceptor molecules) can be partly attributed to xTB's own parameterised behaviour rather than to physical principles. The benchmark therefore cannot cleanly distinguish "fails to learn physics" from "fails to interpolate xTB's parameter surface." At minimum the framing should be tightened, or a subset re-labeled with DFT for cross-validation.
- **MACE / NequIP / Allegro class models are not evaluated.** The paper claims to "represent the current frontier of equivariant architectures" (Section 4.1) but tests only EquiFormerV2 from that frontier. MACE is even cited in Section 2 but not evaluated. The conclusion that "current MLFFs fail to learn transferable representations" cannot be sustained without the higher-body-order equivariant models that define the current SOTA and that have explicit physics priors plausibly relevant to compositional generalisation. The stated reason for excluding foundation models (memorisation confound) does not apply to MACE-class models trained from scratch on this benchmark.
- **No seeds / variance reported.** Figures 2–4 appear to show single runs, yet many headline qualitative claims rest on small relative orderings of models (e.g., "EquiFormerV2 worst on energy OOD, SchNet and DimeNet++ stable"). With per-molecule training sets of only ~10k frames and architectural conclusions resting on cross-model comparisons, seed variance could plausibly shift the rankings. Multi-seed runs with error bars are needed to support the comparative architectural claims in Section 4.3.

### Minor
- **Very small training sets in the base variants.** Task 1 base uses only five trajectories (~10k frames). Several evaluated models (especially EquiFormerV2) are designed for substantially larger data regimes. Without a data-scaling study, the paper cannot separate "architectural failure to compose" from "data-starved high-capacity model." This is part of the same evidentiary gap as the missing seeds.
- **Composition framing for Task 2 is chemically loose.** Describing a carboxylic acid as a composition of alcohol + aldehyde elides the emergent conjugation/acidity at the C(=O)OH group. Failure here may partly reflect that the chemistry is not strictly compositional in the sense the paper presupposes. The paper does note ("we do not expect the model to learn the chemical reaction pathway, but rather to infer the properties of the composite group from the learned effects of its constituent parts"), which is reasonable, but a more explicit caveat would sharpen interpretation.
- **Task 4 framing as pure "symbolic recombination" is incomplete.** Training on bis-acid and bis-amine, then testing on mixed acid/amine, introduces a polarity / charge-transfer shift (symmetric → asymmetric electronic structure) on top of the symbolic recombination. The paper presents it cleanly as the latter; both effects should be acknowledged.
- **Possible selection bias from FlashMD configuration sampling.** Configurations are sampled by a learned MD surrogate and then re-labeled with xTB. This could bias the configuration distribution toward regions FlashMD finds plausible. The paper does not discuss whether this selection effect could systematically flatter or harm the evaluated MLFFs.

### Trivial
- The introduction's claim that MLFFs are "typically trained and tested on the same molecules" is somewhat overstated relative to MD22, Transition1x, and SPICE, which include various cross-molecule splits. Tightening to "controlled compositional splits" would be more accurate.

## Nice-to-Haves
- Add a classical force-field (UFF/GAFF/MMFF) reference as a compositional-by-construction baseline to calibrate what "good compositional generalisation" looks like on each task.
- Decompose force error by atom type and distance to the functional group to show whether failure is localised at the novel chemistry or pervades the molecule.
- Re-label a small subset with DFT (e.g., ωB97X-D) and check whether rankings and generalisation gaps reproduce.
- A data-scaling sweep on Task 1 to show how OOD error responds to training-set size.

## Removed Points
These points are flagged to be removed; treat them with caution.

- **"PBE0 listed as a model in Figure 2 caption."** This appears only in the parser's alt-text reconstruction; the body of Section 4.3 consistently lists the five MLFFs. Likely a parser artefact, not an author error. Removed.
- **Missing related works (e.g., specific MLFF benchmark/method citations).** Not verifiable here; per the rules, omitted.
- **Strength: "important problem"-style statements.** Generic strengths (e.g., "addresses a real and important gap") were dropped; the kept strengths are tied to specific design or empirical content.
- **Strength: "comprehensive empirical validation across SOTA models."** This conflicts with the verified weakness that MACE / NequIP / Allegro are absent. The weakness wins; this strength is dropped here.

## Novel Insights
None beyond the paper's own contributions. The ID/OOD ranking disagreement among MLFFs is interesting but needs corroboration under per-atom metrics and multi-seed runs before it can be treated as a robust finding.

## Suggestions
- Replace total-energy MAE with per-atom energy MAE (and report the size-dependent residual separately) for every task. Re-interpret Tasks 1–4 in light of the corrected metric.
- Add MACE (and ideally NequIP or Allegro) to the model suite; the omission directly weakens the central claim about state-of-the-art MLFFs.
- Run ≥3 seeds per (model, task) and report error bars; without this the architecture-level conclusions are not adequately supported.
- Tighten framing: explicitly state that labels are xTB and that conclusions are with respect to that PES; reserve "physical principles" claims for a DFT cross-check on a subset.
- Add a data-scaling study and a classical force-field baseline.

## Score and Decision

**Evaluation by axis.** Originality: moderate — the four-task taxonomy is a meaningful refinement of compositional-generalisation analysis for MLFFs, but the benchmarking-OOD-for-molecular-models idea is not new (GDL-DS, BOOM, AU-GOOD). Importance: clear — MLFF generalisation across molecules is genuinely under-tested. Claim support: weak — the central "current MLFFs fail compositional generalisation" claim is materially weakened by non-size-normalised energy MAE, semi-empirical labels, single seeds, and a model suite that excludes the strongest physics-priored SOTA. Soundness: middling — methodology is reasonable but several decisions (metric, label fidelity, model selection) directly compromise the headline. Clarity: good. Community value: real if the issues above are addressed; toolkit and split design are reusable.

**Anchors retrieved.**
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/NvJxTjTQtq.md` — *EGraFFBench* (avg 6.00). Most similar comparable: also a benchmark of equivariant MLFFs, but with broader model coverage (NequIP, Allegro, MACE) and more datasets; GMD-25 is narrower and uses semi-empirical labels, suggesting a lower score.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/ItPYVON0mI.md` — CG potentials paper (avg 3.00). Methods paper, lower quality; not directly comparable, but a useful low anchor.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/CkozFajtKq.md` — *LiFlow* flow matching for MD (avg 6.33). A methods paper, broader empirical scope; GMD-25 has narrower empirical depth.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/kKXIYUi8ff.md` — DynamicsDiffusion (avg 3.00). Lower anchor; clearer methodological concerns.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/7Jer2DQt9V.md` — *Unreasonable Effectiveness of Pretraining in Graph OOD* (avg 4.50). Comparable in that it's a benchmark/analysis paper on graph OOD; reviewers found limited novelty/insight, similar tier.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/qFZnAC4GHR.md` — AU-GOOD framework for biochemical OOD (avg 6.67). Higher anchor: more methodological depth, conceptually novel metric; GMD-25 is below this.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/LixGd92Wri.md` — *GDL-DS* benchmark for geometric DL under distribution shifts (avg 5.67). Closest peer in scope; broader domain coverage; GMD-25 is more focused but narrower and methodologically thinner.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/QPVK1ne9gI.md` — *MPFBench* (avg 5.00). A dataset benchmark paper with mixed reviewer scoring; comparable tier.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/gNOW7ch3Ye.md` — *FAMMA* finance benchmark (avg 5.67). Off-topic; weak comparison.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/A23C57icJt.md` — *Open-CK* combustion benchmark (avg 6.25). Larger-scale dataset paper, more empirical depth.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/iRYExPKnxm.md` — *AcademicEval* (avg 4.00). Lower anchor; weaker benchmark contribution.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/Dj1PVLU8fK.md` — ∞-benchmarks (avg 3.50). Lower anchor; controversial methodology.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/ly10tMV6cD.md` — Structure-Rich Text Benchmark (avg 3.25). Lower anchor; weak technical contribution.

Positioning: GMD-25 is below EGraFFBench (6.0) — same general category but EGraFFBench has broader model coverage and clearer methodology. It is comparable to or slightly below GDL-DS (5.67) and the *Unreasonable Effectiveness* graph-OOD paper (4.5). The metric and label-fidelity issues are non-trivial but the benchmark idea and toolkit are real contributions. Settles between 4 and 5.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>