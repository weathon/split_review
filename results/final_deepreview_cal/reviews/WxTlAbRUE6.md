Now I have all the information I need. Let me write the final consolidated review.

## Calibration Report

**Round 1 bracket:** 5.5–7.5 (between weak anchors avg ~3.0 and strong anchors avg ~8.0)

**Round 2 anchors used:**
| anchor_id | avg_score | Decision | Comparison to GMD-25 |
|-----------|-----------|----------|---------------------|
| NvJxTjTQtq (EGraFFBench) | 6.00 | Reject | MLFF benchmark with implementation concerns; GMD-25 is cleaner and more novel |
| Xk9Q0CrJQc (MLFF Dist. Shifts) | 6.25 | Reject | Similar domain; GMD-25 has clearer contribution without weak mitigation methods |
| NSDszJ2uIV (MARCEL) | 6.33 | Accept | Comparable benchmark paper; GMD-25 is similarly solid |
| qFZnAC4GHR (AU-GOOD) | 6.67 | Accept | Similar quality; GMD-25 has more concrete empirical findings |

**Final score determination:** GMD-25 is clearly stronger than EGraFFBench (6.00) and MLFF Distribution Shifts (6.25), and comparable to MARCEL (6.33, Accept) and AU-GOOD (6.67, Accept). Score: **6.5**.

---

## Summary

This paper introduces GMD-25, a benchmark for evaluating compositional generalisation in machine learning force fields (MLFFs). Four tasks—length extrapolation, functional group composition, duplication, and combination—are designed such that training molecules cover the sub-components needed for out-of-distribution test molecules. Five MLFFs (SchNet, PAINN, DimeNet++, GemNet, EquiFormerV2) are evaluated, and all show substantial OOD performance degradation, often by orders of magnitude. The benchmark and toolkit are released to facilitate future research.

## Strengths

- **Systematic construction of controlled compositional generalisation tasks for MLFFs.** The four tasks (Section 3.1) isolate specific challenges—extrapolating chain length, composing functional groups, duplicating motifs, and recombining functional groups—where the training data covers all sub-components needed for test molecules. This goes beyond prior MLFF benchmarks (Section 2.3) that test interpolation over broader chemical space or equilibrium geometries, making the evaluation novel and diagnostically useful.

- **Clear empirical demonstration of severe OOD failures across all architectures.** Figures 2 and 4 show that every evaluated model suffers OOD errors one to two orders of magnitude higher than ID errors (Section 4.3). This provides concrete, quantified evidence for the paper's central claim.

- **Non-trivial finding that ID performance does not predict OOD generalisation.** EquiFormerV2 has the lowest forces MAE on Length Extrapolation but its energy MAE becomes the worst in the OOD region (Figure 2), while SchNet and DimeNet++ maintain more stable OOD energy errors despite weaker ID performance. This challenges the common assumption that high ID accuracy implies robust physical understanding.

- **Extensible, reproducible pipeline.** The custom toolkit (Section 3.2) automates dataset generation from SMILES to AIMD trajectories using GFN2-xTB, and is released with curated splits and preprocessing scripts.

- **Augmented task variants for controlled analysis.** Tasks 1 and 2 include "augmented" variants with additional training data, allowing readers to assess whether more data closes the generalisation gap or not (Figures 3, 4).

## Weaknesses

### Major

- **Energy MAE not normalised by atom count inflates Length Extrapolation errors.** The energy MAE is computed as `(1/M) Σ |Êⱼ − Eⱼ|` — total energy per molecule, not per atom. For Length Extrapolation (Task 1), training molecules have 2–6 carbons and test molecules have 7–13 carbons. Larger molecules necessarily have larger absolute total energy errors, even if per-atom performance were comparable. This partially confounds the sharp error increase at C7 in Figure 2. Forces MAE (per-atom, effectively) is more diagnostic and does show the same qualitative trend, so the conclusion is not invalidated but is weakened. **The authors should report per-atom energy MAE or normalise by atom count for Task 1.**

- **The "Functional Group Composition" task framing as compositional is chemically imprecise.** The paper states that a carboxylic acid (test) can be seen as a composition of alcohol and aldehyde (training moieties). Chemically, –COOH is not a straightforward concatenation of –OH and –CHO — the two moieties are covalently bonded at the same carbon, creating a resonance-stabilised system with distinct electronic structure. The paper partially acknowledges this is a "challenging evaluation" (Section 3.1), but does not provide evidence that the composite group's energy surface is even approximately additive from the constituent parts. The task is still a meaningful generalisation challenge (models must handle a novel, chemically distinct functional group), but **the authors should either provide chemical justification for the compositionality framing or explicitly reposition the task** as testing generalisation to chemically distinct functional groups (which is a different, harder claim).

### Minor

- **No variance or uncertainty quantification across runs.** The paper does not report whether results are stable across random seeds or model initialisations. Given the small training sets (e.g., 5 molecules for Task 1), variance could be substantial, and readers cannot assess whether the reported performance gaps are statistically significant.

- **GFN2-xTB label quality is not cross-validated.** The labels use semi-empirical tight-binding, which is a standard and acknowledged trade-off (Section 3). However, if the reference method itself systematically underperforms on OOD molecules (e.g., dicarboxylic acids vs. monocarboxylic acids), some of the observed generalisation gap could reflect reference method failure rather than model failure. **Cross-validating a subset of test molecules with a higher-accuracy method (e.g., DFT) would bound this effect.**

- **SchNet struggles on ID data for Task 3 (Figure 4e,f), making its OOD failure less diagnostically informative.** If a model cannot fit the training distribution well, its OOD degradation may reflect insufficient capacity rather than a lack of compositional generalisation.

### Trivial

- The paper uses "fail" to describe OOD performance without a quantitative threshold (e.g., OOD error > 10× ID error). A definition would sharpen the claims.

## Nice-to-Haves

- A diagnostic analysis showing *where* errors concentrate (e.g., at functional groups vs. chain ends) would strengthen the paper's conclusions about what kind of generalisation models fail at.
- Discussion of how each model's receptive field (number of message-passing steps or interaction layers) constrains the Length Extrapolation task would help interpret the results.
- Connecting the Length Extrapolation findings to the literature on size-consistency/extensivity in MLFFs (e.g., Behler-Parrinello type models) would add useful context.

## Removed Points

- **"16 fs timestep may produce unphysical trajectories"** — Removed. This is speculative without evidence of instability. FlashMD is a peer-reviewed method designed for this timestep.
- **"Repeatedly states models fail without defining failure"** — Moved to Trivial.
- **"Missing appendix content / proofs"** — Removed. The appendix exists in the original submission; the parser strips it.
- **Various formatting/style nitpicks** — Removed per instructions.

## Novel Insights

None beyond the paper's own contributions. The key insight — that OOD generalisation failures in MLFFs are severe and that ID performance does not predict OOD robustness — is well articulated by the paper itself.

## Suggestions

1. **Normalise energy MAE by atom count** for the Length Extrapolation task, or add per-atom energy MAE as a primary metric.
2. **Reframe the Functional Group Composition task** honestly: either justify (with chemical evidence) why alcohol+aldehyde energy surfaces are additive enough to test compositionality, or explicitly reposition it as testing generalisation to chemically distinct functional groups.
3. **Add variance estimates** across at least 3 random seeds for the main results.
4. **Cross-validate a subset of OOD labels** (e.g., 2–3 molecules per task) against DFT to bound reference-method confounding.

## Score and Decision

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>