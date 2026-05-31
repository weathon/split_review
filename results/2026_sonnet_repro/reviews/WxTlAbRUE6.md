Now let me perform calibration searches to score the paper.**Round 1 bracket: 5.0 – 7.0**

Now let me narrow within this bracket.Now I have enough to write the final consolidated review. Let me compile everything.

---

## Summary

GMD-25 is a new benchmark for evaluating the compositional generalization of machine learning force fields (MLFFs), comprising four controlled tasks—Length Extrapolation, Functional Group Composition, Functional Group Duplication, and Functional Group Combination—applied to ab-initio-generated MD trajectories of linear substituted alkyl chains. The benchmark is accompanied by a data-generation toolkit and an empirical evaluation of five representative MLFF architectures (SchNet, PAINN, DimeNet++, GemNet, EquiFormerV2), all of which show severe performance degradation on out-of-distribution molecules.

---

## Strengths

- **Systematic task design grounded in compositional generalization theory.** The four tasks (Section 3.1, Figure 1) each isolate a distinct generalisation axis—chain length, functional group compositionality, duplication of a motif, and asymmetric recombination—rather than relying on random or scaffold-based splits. The training data is explicitly chosen to contain all "building blocks" needed for the test molecules, making the benchmark's definition of "should be solvable in principle" concrete and verifiable.

- **Consistent, quantitative OOD failure demonstrated across five architectures.** Figures 2–4 show that all five architectures degrade substantially at the distribution shift in every task. For forces MAE (the properly atom-normalized metric), OOD errors are at least one order of magnitude above ID errors across tasks (Section 4.3), providing robust evidence that current models over-interpolate rather than capturing transferable physical principles.

- **Augmented task variants provide diagnostic depth beyond the base tasks.** The inclusion of augmented training sets for Tasks 1 and 2 tests whether simply exposing models to additional compositional examples closes the gap. The negative results (Figures 3, 4c–d) are informative: the generalisation failure persists even when models have seen all "components," pointing toward architectural rather than data-coverage issues.

- **New dataset and toolkit with 118 molecules and 296k geometries.** The curated dataset with pre-processing scripts and data splits, and the modular Python toolkit using RDKit, FlashMD, and XTB-Python (Section 3.2), are genuine community contributions that make the benchmark extensible to new functional groups and chain lengths.

---

## Weaknesses

### Fatal
None.

### Major

- **Energy MAE is not per-atom normalized, creating a systematic confound in the headline quantitative claims.** The paper defines energy MAE as $\frac{1}{M}\sum_j|\hat{E}_j - E_j|$ (Section 4.2, Equation 1), dividing by the number of molecules $M$ rather than by atom count. Because total molecular energy is an extensive quantity, a model with uniformly good per-atom errors will still accumulate larger raw absolute errors on larger molecules. This is most consequential for Task 1 (OOD chains have 7–13 carbons vs. 2–6 in training) and Task 3 (dicarboxylic acids have an additional –COOH group vs. monocarboxylic acids of the same chain length). The paper asserts "OOD errors two orders of magnitude higher than ID" (abstract and Conclusion Section 5) relying substantially on energy panels, but this claim is partially confounded by the size difference between ID and OOD molecules. The forces MAE (atom-averaged, size-extensive) tells a consistent and credible story on its own; the energy metric should either be replaced by per-atom energy MAE or the two should be analyzed separately, with the force-based findings bearing the evidentiary weight of the "orders of magnitude" claim.

- **Broad conclusions are not supported by the scope of evaluation.** Section 5 concludes that current approaches have "fundamental challenges in learning transferable representations of inter-atomic interactions" and the Introduction frames this as a gap in the MLFF field at large. However, the evaluation excludes foundation/universal models entirely (Section 4.1 acknowledges this in one sentence). A domain scientist choosing a force field would reach for MACE-MP-0 or a similar universal model, not train SchNet from scratch. The paper's conclusions read as field-wide verdicts but are actually restricted to single-task, scratch-trained architectures on a narrow chemical space. The paper should either scope conclusions explicitly to "single-task models trained from scratch on small datasets" or include at least one zero-shot or fine-tuned foundation model comparison.

### Minor

- **Augmented variant failures are not analyzed.** The paper notes (Section 4.3) that augmented training does not close the OOD gap for either Task 1 or Task 2, but does not investigate why. Since augmented training exposes models to all relevant chain lengths or functional group combinations, a brief mechanistic discussion of what the models apparently fail to learn from augmented data would substantially strengthen the empirical narrative.

- **Hyperparameter optimization protocol is ambiguous with respect to the ID test set.** Section 4.2 states that Bayesian hyperparameter search is used to achieve "best possible performance on the in-distribution data," but it is not stated whether this search used a dedicated ID validation split or the ID test set directly. If the latter, there is mild circularity in the reported ID numbers. This should be clarified.

- **Chemical space scope is narrow but not adequately foregrounded.** The benchmark is restricted to linear, unbranched alkyl chains with a small number of functional group types. The introduction and conclusions invoke drug discovery and polymer science as motivating contexts, but these involve ring systems, branching, and more complex multi-body interactions. The paper should be more explicit that GMD-25 is a controlled first step and not a representative sample of the chemical spaces it is motivated by.

### Trivial

- The "best ID model ≠ best OOD model" framing (Conclusion) is slightly overstated: the dominant pattern in the results is universal OOD failure, and the ranking differences between architectures in the OOD regime are small relative to the ID-to-OOD performance collapse. Framing the finding as "architectural choices influence which failure mode you get" would be more precise.

---

## Nice-to-Haves

- Adding a size-extensive additive baseline (an atom-additive model summing per-atom contributions learned from training) as a reference point would establish whether the observed failures reflect a lack of expressivity or a specific missing inductive bias. If even an additive model fails on duplication and composition tasks, the benchmark is probing something deeper than pure size-extensivity.

- Including a brief post-hoc per-atom energy MAE comparison alongside the current energy metric would let the forces and energy results tell a unified, internally consistent story.

- A more detailed per-task analysis of the augmented variant failures—e.g., tracing whether models learn the length pattern but fail to combine it with functional group identity—would turn a negative result into a diagnostic finding.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"Task 2 chemistry is imprecise / carboxylic acid is not a true composition of alcohol and aldehyde."** (Harsh critic, Section 3.1 note) — The paper explicitly acknowledges (Section 3.1) that it is not expecting the model to learn a chemical reaction pathway, and carboxylic acid shares C=O and –OH bonds with aldehydes and alcohols. The task is defined as testing whether models can transfer learned interaction patterns; the chemical argument about electronics is valid in principle but the paper's use of "composition" is contextually reasonable. Removed as overreach of scope.

- **"GFN2-xTB systematic errors for polar functional groups."** (Harsh critic) — This is a general concern about any semi-empirical method, not a specific demonstrated problem with this benchmark. No concrete evidence is provided that it affects the particular functional groups studied. Removed as speculative.

- **EGraFFBench-style concern about foundation model exclusion being a reproducibility/availability issue.** Not applicable here — the paper explicitly cites MACE-MP-0 as existing and explains the methodological reason for exclusion. Not a reproducibility concern.

- **Strength: "Clear contrast with existing benchmarks / accurate positioning."** The positioning in Section 2.3 is reasonable but relatively standard for a benchmark paper. Removed as generic.

- **Strength: "Thorough evaluation with augmented task variants easier than base."** The augmented variants are not easier (results show persistent failure), so the strength claim about "easier" is not borne out. The diagnostic value of the negative result is kept under Strengths in a modified form.

---

## Novel Insights

The most genuinely novel observation—one the existing MLFF literature has largely missed—is the clean separation between *what a model fails at* depending on the failure mode. EquiFormerV2 exhibits the lowest forces MAE OOD in Length Extrapolation but catastrophically fails on energy MAE; GemNet generalizes best on Functional Group Duplication; PAINN leads on energy MAE for Functional Group Combination. This cross-task profile suggests that different architectures encode different inductive biases that are only revealed under compositional stress tests, and that ID performance is a poor predictor of which failure mode a model will exhibit. This is a diagnostic contribution that motivates architecture-specific analysis of compositional failure modes.

---

## Suggestions

1. **Replace total-energy MAE with per-atom energy MAE** across all tasks and re-run the analysis. This will allow the energy and forces results to be compared on the same extensivity basis and will clarify which "orders of magnitude" claims survive.

2. **Explicitly scope the conclusions** to "single-task models trained from scratch" and add a one-paragraph discussion of how foundation/universal models would fit into or be evaluated by GMD-25 in future work.

3. **Add a short analysis of augmented variant failures**, even if qualitative (e.g., visualizing learned representations of training vs. OOD molecules), to convert a negative empirical observation into a mechanistic insight.

4. **Clarify the hyperparameter tuning protocol**: state explicitly whether ID test or a separate ID validation split was used for model selection.

---

## Score and Decision

**Calibration anchors retrieved:**

| Path | Avg Human Score | Round | Comparison to GMD-25 |
|---|---|---|---|
| NvJxTjTQtq.md (EGraFFBench) | 6.00 | R1 | Most topically similar; GMD-25 has cleaner concept but narrower scope and no MD simulation evaluation |
| NSlvSDQ8aE.md (Force-Guided Bridge Matching) | 7.00 | R1 | Method paper; richer contribution; not directly comparable |
| CkozFajtKq.md (LiFlow) | 6.33 | R1 | Method paper with benchmark; richer than GMD-25 |
| rwmWd2rjP1.md (MoreRed) | 4.75 | R1 | Method paper; weaker baseline choice |
| LixGd92Wri.md (GDL-DS) | 5.67 | R2 | Broader benchmark but with causal-reasoning errors and overclaiming issues |
| NSDszJ2uIV.md (MARCE) | 6.33 | R2 | Accepted benchmark paper; broad dataset, multiple tasks; GMD-25 is narrower |
| Xk9Q0CrJQc.md (Distribution Shifts for MLFFs) | 6.25 | R2 | Method+benchmark; addresses same OOD theme in MLFFs; includes foundation models; richer contribution |
| an3kPpce6b.md (GODD) | 5.25 | R2 | Method paper; weaker contribution |
| SBCMNc3Mq3.md (ECD) | 6.50 | R2 | Accepted benchmark paper; new dataset with good chemical diversity; similar scope to GMD-25 |

**Round 1 bracket:** 5.0 – 7.0

**Round 2 narrowing:** The most topically close anchors (EGraFFBench at 6.0, "Distribution Shifts for MLFFs" at 6.25) both sit in the lower-middle of the bracket. GMD-25 has a tighter conceptual contribution (compositional generalization framing) than EGraFFBench but a narrower evaluation scope and lacks the methodological additions of the "Distribution Shifts" paper. The energy MAE normalization concern is a genuine methodological gap affecting the headline quantitative claims. The narrow chemical space and overreaching conclusions are meaningful weaknesses for a benchmark paper, where scope and generalizability of findings are primary evaluation criteria. GMD-25 is slightly weaker than EGraFFBench on scope (only linear chains, no simulation-level evaluation, exclusion of foundation models) but has a cleaner conceptual design and no experimental correctness concerns. It is weaker than the "Distribution Shifts" paper, which adds methods on top of analysis. I place GMD-25 just below the cluster of R2 anchors, at **5.5**.

**Originality:** Moderate — compositional generalization framing for MLFFs is novel and well-motivated.
**Importance:** Moderate — addresses a real gap but restricted to narrow chemistry.
**Claims support:** Moderate — forces MAE results clearly support OOD failure claim; energy MAE claims partially confounded.
**Experimental soundness:** Moderate — clean protocol but energy metric choice is problematic.
**Writing clarity:** Good — well-organized, tasks clearly described.
**Community value:** Moderate — toolkit and dataset are useful; narrow scope limits immediate applicability.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>