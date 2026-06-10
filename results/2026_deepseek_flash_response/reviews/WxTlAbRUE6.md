## Summary

This paper introduces GMD-25, a benchmark of four tasks (Length Extrapolation, Functional Group Composition, Functional Group Duplication, Functional Group Combination) designed to test whether ML force fields (MLFFs) learn physically generalizable principles rather than merely interpolating training labels. The benchmark is carefully constructed so that training molecules contain all atomic/functional-group building blocks needed for test molecules, making failure diagnostic of a genuine compositional generalization deficit. The paper evaluates five diverse MLFFs (SchNet, PAINN, DimeNet++, GemNet, EquiFormerV2) and finds that OOD errors exceed ID errors by 1–2 orders of magnitude across all tasks, with ID performance rank failing to predict OOD performance rank.

## Strengths

1. **Controlled compositional task design where training covers all needed primitives**: Each task is constructed so that the training molecules contain the atomic and functional-group "building blocks" required to solve the test molecules, making failure diagnostic of a genuine inability to compose learned knowledge rather than missing information. For example, in Task 2 (Section 3.1), the training set includes alcohols (OH) and aldehydes (CHO) while the test set contains carboxylic acids (COOH = OH + CHO). This controlled decomposition goes beyond prior MLFF benchmarks (MD17, WS22, Transition1x, MD22) that only test broader coverage without explicitly ensuring composability.

2. **Clear empirical evidence that OOD errors exceed ID errors by 1–2 orders of magnitude across all models and tasks**: The paper measures both ID and OOD performance for five architecturally diverse models on all four tasks (Figures 2–4, Section 4.3). For Functional Group Duplication, Energy MAE OOD errors are "higher by two orders of magnitude" compared to ID errors. This systematic quantification of the generalization gap across architectures is a novel contribution.

3. **Demonstration that ID performance rank does not predict OOD performance rank**: The results reveal a decoupling — models that excel on ID data are not necessarily those that generalize best. EquiFormerV2 achieves the lowest OOD Forces MAE on Length Extrapolation but its Energy MAE "increases dramatically in the OOD region, eventually becoming the worst-performing model," while SchNet and DimeNet++ show more stable OOD energy predictions. This finding is important because it shows that standard ID-only benchmarks may give misleading signals about model quality.

## Weaknesses

### Major

1. **No uncertainty quantification (multiple seeds, error bars)**: The paper reports single-point MAE values for each model on each task without any variance information. For a benchmark that aims to rank models and draw architectural conclusions (e.g., "GemNet overall performed best in the OOD region for Functional Group Composition and Functional Group Duplication"), the absence of at least 3–5 seed runs means the reported differences between models cannot be assessed for statistical significance. While the core finding (OOD errors are orders of magnitude larger than ID errors) is so dramatic that it is likely robust, the finer comparative claims and rankings are on weaker footing. This is the most consequential gap for a benchmark paper that the community is expected to rely on.

### Minor

2. **GFN2-xTB reference method limitation not discussed**: The benchmark uses a semi-empirical tight-binding method (GFN2-xTB) as its reference. The paper acknowledges its "balance between computational efficiency and accuracy" (Section 3) but does not discuss whether the observed generalization failures are properties of the models or potential artifacts of the chosen reference (e.g., GFN2-xTB surfaces may have different compositional generalization properties than DFT-level surfaces). This limitation should be acknowledged.

3. **No limitations section**: The paper lacks any dedicated discussion of what the benchmark does not cover: the restriction to linear alkyl chains, vacuum (gas-phase) simulations, fixed temperature (300 K), single-reference method, and whether tasks are likely to scale to larger chemical spaces.

4. **Augmented variant results under-analyzed**: The paper introduces augmented variants for Tasks 1 and 2 with additional training data expected to make tasks easier. The finding that augmentation often does not help is noted but not analyzed for root causes (e.g., was additional data insufficient? Not covering the right compositional relationships?). The paper notes this but does not analyze *why*, which is a missed diagnostic opportunity.

5. **Missing per-model parameter counts or training costs**: Readers cannot assess whether compared models have similar capacity. EquiFormerV2 and SchNet differ substantially in parameter count; this contextualizes the results but is not reported.

6. **No justification for why Tasks 3 and 4 lack augmented variants**: The paper introduces augmentation as a general feature for Tasks 1 and 2 (Section 3.1) but Tasks 3 and 4 have only base variants, with no explanation for this asymmetry.

7. **Hyperparameter tuning for ID performance may be suboptimal for OOD**: The paper tunes hyperparameters on ID data then evaluates OOD (Section 4.2) without acknowledging this as a conservative choice that may systematically penalize some architectures over others.

### Trivial

8. **Figure caption text contains likely OCR artifacts**: Figure 2's alt-text mentions "PBE0" (a DFT functional, not a model) and Figure 3's alt-text mentions "m4s" — neither match the model list in Section 4.1. These are almost certainly parser misreadings of embedded figure image text rather than actual author errors, but should be corrected in the final version.

## Nice-to-Haves

- Add a small-scale DFT validation for one task (e.g., Length Extrapolation) to verify that generalization gaps at the GFN2-xTB level transfer to higher-fidelity methods.
- Define explicit passing criteria (e.g., "OOD force MAE within 2× of ID") to make the benchmark more actionable for future work.
- Analyze why energy MAE and force MAE decouple for specific models, as this could reveal architectural biases.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Model identity inconsistencies (PBE0, m4s)**: Moved from "Critical Issue" to Trivial (#8) because "PBE0" in Figure 2 caption and "m4s" in Figure 3 caption are almost certainly OCR/parser misreadings of embedded figure image text. The hard rules require removing criticisms about formatting artifacts.
- **"The paper also does not report how many training runs were performed"**: Subsumed by Major weakness #1 about missing multiple seeds.
- **"Task 2 compositional justification needed"**: The paper already addresses this at lines 75–76 ("we do not expect the model to learn the chemical reaction pathway, but rather to infer the properties of the composite group from the learned effects of its constituent parts"). This is reasonable.
- **"Force MAE vs Energy MAE not disentangled"**: Moved to Nice-to-Have; the paper does discuss the decoupling for specific models (EquiFormerV2 on Length Extrapolation), and deeper analysis is a strengthening opportunity, not a weakness.
- **"Strengthening the Paper on Its Own Terms" DFT validation suggestion**: This is a nice-to-have improvement, not a weakness. Moved to Nice-to-Haves.

## Novel Insights

The most striking finding is the severity of the compositional generalization failure despite training on all the chemical building blocks — models fail not just marginally but by 1–2 orders of magnitude. The fact that augmentation (adding more training data covering the missing compositional combinations) still does not rescue performance on Functional Group Composition suggests something deeper than data scarcity is at play, possibly that current MLFF architectures lack the right inductive biases for systematic composition. The decoupling of force and energy prediction quality is also noteworthy: it suggests these architectures learn different representational strategies for different prediction targets even when the energy and forces are connected by a gradient relationship, which could point to architectural design choices that trade off one type of accuracy for another.

## Suggestions

1. Report results with at least 3–5 random seeds and include variance/error bars in all figures. This is the single highest-impact improvement.
2. Add an explicit limitations section discussing scope (linear alkyl chains, GFN2-xTB reference, gas phase, fixed temperature).
3. Provide per-model parameter counts and training costs to contextualize comparisons.
4. Analyze why augmented variants fail to improve performance — this could yield insights about what the models are actually learning.
5. Resolve figure caption artifacts and ensure consistency between text and figures.

---

**Calibration Anchors Used:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| EGraFFBench (NvJxTjTQtq.md) | 6.00 | R1/R2 | MLFF benchmark paper; our paper has cleaner task design but less thorough evaluation |
| Understanding & Mitigating Distribution Shifts for MLFFs (Xk9Q0CrJQc.md) | 6.25 | R2 | Similar topic; their paper proposes mitigation methods, ours a reusable benchmark |
| AU-GOOD framework (qFZnAC4GHR.md) | 6.67 | R2 | More formal OOD evaluation framework with statistical rigor; ours is more domain-specific |
| Towards Fast, Specialized MLFFs (1durmugh3I.md) | 7.00 | R2 | Methods paper, not directly comparable |
| Force-Guided Bridge Matching (NSlvSDQ8aE.md) | 7.00 | R1 | Methods paper, not directly comparable |
| Flow Matching for Atomic Transport (CkozFajtKq.md) | 6.33 | R1 | Methods paper, not directly comparable |
| Multi-Grained Group Symmetric Framework (J4V3lW9hq6.md) | 5.00 | R1 | Methods paper, different contribution type |
| BenchMol (1JgWwOW3EN.md) | 2.50–4.80 | R1 | Unrelated benchmark paper |

Round 1 bracket: 5.0 – 7.0. Round 2 narrowed to 5.5 – 6.5. Final score: 6.0 — positioned between EGraFFBench (6.00, similar quality with different tradeoffs) and the AU-GOOD framework (6.67, more formal rigor).

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Reject</decision>