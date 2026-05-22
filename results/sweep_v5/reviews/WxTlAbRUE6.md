Now I have a thorough understanding of the paper and the calibration landscape. Let me produce the final review.

---

## Summary

This paper introduces GMD-25, a benchmark with four tasks (length extrapolation, functional group composition, duplication, and combination) designed to evaluate whether ML force fields can compositionally generalise. Training sets are deliberately constrained so that test molecules differ systematically from training molecules in chain length or functional group arrangement. Five popular architectures (SchNet, PAINN, DimeNet++, GemNet, EquiFormerV2) are evaluated. The key finding is that OOD errors are often one to two orders of magnitude higher than ID errors, and the best ID models are not always the best OOD models — suggesting current MLFFs do not learn physically transferable representations.

## Strengths

1. **Controlled OOD task design.** Unlike most MLFF benchmarks (MD17, WS22, Transition1x) that evaluate on broader chemical coverage or equilibrium dynamics, GMD-25 constructs targeted train/test splits with clear distribution shifts — longer chains, novel functional-group combinations, duplication, and asymmetric functionalisation. This is a genuine advance for diagnosing what MLFFs fail at.

2. **Consistent evidence of generalisation failure.** Across all four tasks and all five architectures, Figure 2 and Figure 4 show that OOD errors are systematically elevated — often by 1–2 orders of magnitude. The consistency across models, task variants (base vs. augmented), and metrics (energy + forces) makes this a robust empirical finding, not a statistical fluke.

3. **ID-to-OOD rank reversal.** The paper documents that EquiFormerV2 is best on forces in Length Extrapolation but worst on energy (Figure 2), DimeNet++ excels on ID forces for composition but fails OOD (Figure 4), and PAINN outperforms on combination energy while EquiFormerV2 wins on forces (Figure 4, panels g–h). This "non-correlation" finding is a valuable diagnostic: standard ID leaderboards are misleading for generalisation.

4. **Base + augmented variants.** Each task has a base and an augmented setting that provides more coverage (e.g., intermediate chain lengths, additional functional-group examples). The augmented variants generally help modestly but do not close the OOD gap — this controlled comparison is more informative than a single-split benchmark.

5. **Extensible toolkit.** The data generation pipeline (RDKit → FlashMD → GFN2-xTB, integrated via ASE) and the dataset (118 molecules, ~300k labelled geometries) are released with the paper, enabling extension to new molecular families.

## Weaknesses

### Fatal
None.

### Major

1. **The connection to "compositional generalisation" is substantially overclaimed.** The paper frames all four tasks as tests of compositional generalisation (title, abstract, Section 2.2, Section 3.1), citing Hupkes et al. (2020), but the tasks lack the formal primitive-composition structure that gives compositionality its predictive content.
   - **Task 2** (Functional Group Composition) claims a carboxylic acid is a "composition" of an alcohol and an aldehyde. The paper says this "can be seen as" a composition, but no well-defined composition rule is provided, and the training data includes "complex carbonyls and alcohol molecules" whose relationship to the test group is not clearly compositional.
   - **Task 3** (Duplication) tests repetition of a single motif — a different cognitive operation from systematic recombination of distinct primitives.
   - **Task 4** (Combination) trains on symmetric diacids and diamines and tests on asymmetric arrangements. This tests symmetric→asymmetric extrapolation, not recombination of isolated primitives.
   - **Task 1** (Length Extrapolation) is about scaling to larger molecules, not about combining learned components in novel ways.
   
   These are valid OOD generalisation tasks — but calling them "compositional" without defining primitives, composition rules, or establishing that the training set covers all required primitives oversells the conceptual contribution. The paper should reframe the contribution as a **systematic OOD generalisation benchmark** and dial back the compositionality claims.

2. **Per-molecule energy MAE confounds molecule size with accuracy in Task 1 (Length Extrapolation).** The paper reports energy MAE as (1/M) Σ|Êⱼ − Eⱼ|, averaged over molecules. For the base variant of Task 1, OOD molecules (C7–C13) have more atoms than ID molecules (C2–C6). Total energy scales roughly linearly with atom count, so even if per-atom error were constant, total energy MAE would increase for larger molecules. The sharp rise at the distribution shift in Figure 2(a) is therefore partly a size artifact. The paper interprets this rise as evidence of generalisation failure, but the metric itself guarantees a baseline increase. The force MAE (which is per-atom) does not have this issue and is more reliable for Task 1. The energy results for Task 1 need to be re-analysed with a per-atom metric before quantitative claims can be trusted.

3. **No statistical uncertainty reported.** Figures 2–4 show single-curve/shared data with no error bars, confidence intervals, or multi-seed variability. Given the modest dataset sizes (5–8 training molecules per task), it is unclear whether the observed model rankings (e.g., which model is best OOD on which metric) are robust or driven by a single training run. Some ranking differences appear small; without variance estimates, the conclusions about which architectures generalise better are unverifiable.

### Minor

1. **The figure descriptions mention model names not described in Section 4.1.** Figure 2's parsed description lists "PBE0 (orange squares)" among the five compared models. PBE0 is a DFT functional, not one of the MLFFs described. Figure 3 similarly lists "m4s." Section 4.1 and the Conclusion only list SchNet, PAINN, DimeNet++, GemNet, and EquiFormerV2. This is likely a labeling artifact or OCR misreading (PAINN may be misread as PBE0), but it undermines confidence in the reported experimental protocol and should be clarified.

2. **No foundation model baselines.** The paper excludes foundation models (e.g., MACE-MP-0, or pretrained models) to avoid "untangling memorisation and generalisation effects." While this is a stated design choice, a benchmark that aims to measure the state of the art in generalisation but excludes the most capable current models limits its practical relevance. The finding that even foundation models fail on these tasks would significantly strengthen the paper's impact.

3. **Ground truth is GFN2-xTB, a semi-empirical method.** The paper makes strong claims about "physical principles" and "physically plausible representations" (abstract, conclusion). GFN2-xTB is a reasonable and well-established reference for organic molecules, but it is not exact physics. The models are learning to reproduce GFN2-xTB's approximations, not necessarily true quantum mechanics. While this is a limitation shared by essentially all MLFF benchmarks, the paper's language should be tempered to acknowledge that the benchmark tests generalisation *within the GFN2-xTB model chemistry*, not absolute physical principles.

### Trivial

- The augmented variant results (Figure 3) mention PAINN in the figure description, but Section 4.1 lists PAINN only in the context of other tasks — it appears PAINN was used in all tasks but the text is inconsistent about listing it for Figure 3 specifically.

## Nice-to-Haves

- **Per-atom energy MAE** for Task 1 would cleanly separate size effects from genuine generalisation failure.
- **Multi-seed experiments (≥3 seeds)** with standard deviations would establish whether the observed model rankings are statistically significant.
- **A simple additive baseline** (e.g., summing fragment-level contributions) would show whether the tasks are even *solvable* by any approach, clarifying whether failures are due to model limitations or task design.
- **Inclusion of at least one foundation model** (e.g., MACE-MP-0 or a pre-trained equivariant model) would improve practical relevance.
- **Error decomposition** for Task 1: decompose energy error into per-atom vs. per-bond contributions to determine whether the OOD increase is truly a size artifact.

## Removed Points

**Critical Issue 3 from Harsh Critic (GFN2-xTB cannot support "physical principle" claims — Structural):** This criticism is too severe for what is standard practice. Every MLFF benchmark uses approximate reference methods (DFT, semi-empirical). GFN2-xTB is a well-established method for organic molecules. The paper's "physical principles" language is somewhat aspirational but not deceptive. Demoted to Minor weakness #3 above — the paper should soften this language, but this is not a structural flaw.

**Section-by-section notes about the abstract overstating novelty:** These are generic. The paper's claim that existing benchmarks "only test interpolation to the same molecules" is somewhat reductive (e.g., Transition1x evaluates on unseen reaction pathways), but this is a common framing device. Removing as it adds no actionable insight.

**"Deeper Analysis Needed" items about clarifying compositionality:** Already covered in Major weakness #1.

**Request for force component residuals and cosine similarity:** This is a nice-to-have analysis but not a standard expectation for a benchmark paper.

**Missing related works citation:** Removed per instructions (cannot verify external sources).

## Novel Insights

The most interesting emergent observation from this review, beyond the paper's own contributions, is that the harsh critic's strongest structural argument (compositional framing) and the paper's strongest contribution (systematic OOD task design) can co-exist if reframed. The paper does not need to prove its tasks are "compositional" to be useful — the tasks are well-designed OOD generalisation probes regardless of what label they carry. The review process reveals that the paper's real value lies in its diagnostic power (showing that model rankings invert between ID and OOD, and that no architecture generalises robustly), not in advancing compositionality theory. This suggests the paper would be stronger if it rebranded as a **systematic OOD generalisation benchmark** and made the compositionality framing a secondary discussion rather than the headline.

## Suggestions

- Reframe the contribution away from "compositional generalisation" and toward "systematic OOD generalisation with controlled molecular structure variations." This aligns the paper's claims with what the tasks actually demonstrate and avoids the definitional criticisms.
- Report per-atom energy MAE for the Length Extrapolation task to disentangle size effects from genuine generalisation failure.
- Add at least 3 random seeds per model/task with standard deviations to establish robustness.
- Clarify the PBE0/m4s figure-labeling discrepancy — verify that the published figures correctly label PAINN where PBE0 appears.
- Soften the "physical principles" language in the abstract and conclusion to acknowledge that the reference level is GFN2-xTB.
- Consider adding a simple group-contribution baseline (e.g., energy = sum of fragment contributions) to demonstrate task solvability.

## Score and Decision

### Calibration Anchors

| Anchor Path | Avg Score | Comparison |
|---|---|---|
| `Xk9Q0CrJQc` (Understanding & Mitigating Distribution Shifts for MLFFs) | 6.25 | Similar MLFF-OOD topic, but that paper proposes *methods* to mitigate shifts in addition to benchmarking. The current paper is only a benchmark (no mitigation method), so slightly weaker overall contribution. |
| `NvJxTjTQtq` (EGraFFBench) | 6.00 | Also an MLFF benchmark; that paper has broader scope (more models, new datasets, dynamics metrics) but implementation quality was questioned. The current paper is cleaner but narrower. Comparable quality. |
| `qFZnAC4GHR` (AU-GOOD framework) | 6.67 | Accepted. Proposes a general framework/methodology rather than a fixed benchmark. Higher abstraction and broader applicability. The current paper is more domain-specific. |
| `1durmugh3I` (Distilling MLFFs) | 7.00 | Accepted. Proposes a new method with experiments. Stronger contribution type than a pure benchmark. |
| `ItPYVON0mI` (CG potentials) | 3.00 | Very low score due to limited experiments, poor writing, lack of novelty. The current paper is substantially stronger than this. |
| `P5jreWnIjV` (MoleculeCLA) | 4.00 | Low score. Computationally generated benchmark with questionable ground truth and narrow scope. The current paper has better task design and clearer evaluation protocol. |

Comparing against these anchors: the current paper sits between the low-scoring benchmarks (~3–4) and the higher-scoring benchmark/method papers (~6–7). Like EGraFFBench (6.0, rejected), it tackles a timely problem with clean experiments, but is held back by an overclaimed conceptual framing (compositional generalisation) and a metric issue (per-molecule energy MAE for Task 1). These are real weaknesses that the authors can address, but in its current form the framing and Task 1 energymetric reduce confidence in the central claims.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>