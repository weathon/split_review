Now I have all the information I need. Let me write the final consolidated review.

## Summary

This paper introduces *multimodal wild TTA*, a new test-time adaptation setting where the target domain contains a mixture of weakly-corrupted (single modality) and strongly-corrupted (multiple modalities corrupted/missing) samples. The proposed method, SuMi, combines three components: (1) IQR-based sample selection with an expanding threshold to gradually include strong OOD samples, (2) unimodal assistance to reject low-informative samples while retaining rich multimodal information, and (3) mutual information sharing to align predictions across modalities. Experiments on Kinetics50-C and VGGSound-C demonstrate consistent gains over prior TTA methods, with the largest improvements in strong-OOD scenarios.

## Strengths

- **Novel problem formulation.** The paper identifies and formalizes "multimodal wild TTA," a genuinely underexplored setting where test data mixes weak OOD, strong OOD (including missing modalities), and various distribution shifts. This is a practical extension beyond existing multimodal TTA work (READ) which only handles single-modality corruptions under single-domain settings. The motivation is clearly illustrated in Figure 1.

- **Comprehensive empirical evaluation.** The method is evaluated across two datasets (Kinetics50-C, VGGSound-C) with 15 visual + 6 audio corruptions at multiple severity levels, four strong-OOD scenarios (Both, Vmiss, Amiss, Mix), and mixed-ratio settings (Figures 4–5). Results are reported over 5 seeds with standard deviations. In strong OOD scenarios, SuMi achieves clear gains over the best prior method READ (e.g., Table 2: 33.4 vs 29.1; Table 4: 19.7 vs 14.5), and the mixed-domain results (Figure 5) show SuMi maintaining performance as the proportion of strong OOD samples increases while other methods collapse.

- **Empirical support for the unimodal assistance design.** The paper provides direct evidence (Figure 3c, Table 6) that low unimodal entropy does *not* always correlate with good multimodal performance — samples in the [20,40) unimodal entropy range outperform those in [0,20). This observation, formalized as the unimodal assistance criterion (Equation 4), is a concrete finding backed by quantitative analysis.

- **Consistent lower variance.** Across all tables, SuMi's standard deviations are smaller than those of most baselines (e.g., Table 1 Fog: SuMi 56.5±0.05 vs EATA 23.0±1.03, SoTTA 27.0±1.11), indicating the method achieves stability alongside accuracy.

## Weaknesses

### Fatal
None.

### Major
None that are unambiguously verifiable from the paper as written. The criticisms raised about the IQR mechanism are more about clarity and specification than a structural flaw that invalidates the core claims.

### Minor

- **IQR computation is ambiguously specified (Section 3.2.1, Algorithm 1).** The paper states "h is a vector" and that samples are selected if "β + (1-β)f(t) percent of the values in h satisfy Equation 3." Algorithm 1 writes `Q1 = quantile(h, 0.25)` without specifying whether quantiles are computed per sample across feature dimensions or across the batch. The intended behavior can be inferred but the ambiguity creates a reproducibility gap. This is a clarity issue, not a structural flaw — the core idea of an expanding threshold is valid and empirically supported — but it should be made precise.

- **Ablation table has an anomalous duplicate row (Table 5).** Two rows both show all three components checked (✓✓✓) but report different results (e.g., Kinetics50 severity 5: 44.6 vs 52.0). One of these is likely a copy-paste error or incorrect marker. This does not undermine the overall ablation conclusions (the valid full-model row at 52.0 outperforms all partial combinations), but the table needs correction.

- **The mutual information sharing loss is disabled after t₀ iterations in strong OOD, without ablation (Section 3.4).** The paper explains the intuition (later iterations include more corrupted samples that could harm alignment) but does not ablate this design choice. Showing what happens when MIS is applied throughout would strengthen the paper.

- **The unimodal threshold γᵤ = e⁻¹ is given without justification or sensitivity analysis.** A brief sensitivity sweep across datasets would improve confidence that the choice is not brittle.

- **Gains over READ in weak-OOD settings are marginal.** On single-corruption weak OOD (Tables 1, 3), SuMi's average improvement over READ is ~0.4-0.9 percentage points, and on several individual corruptions the results are within overlapping standard deviation intervals. The paper's "significant and consistent" claim is primarily supported by strong-OOD and mixed-domain results, which is where the real contribution lies.

### Trivial
- The claim that existing methods "always fail" (abstract) is slightly overstated for weak-OOD settings, where several baselines achieve ~60% accuracy. This is a minor wording issue.

## Nice-to-Haves
- An oracle baseline (e.g., ordering the test stream "weak first, then strong") would calibrate how close the IQR smoothing gets to an optimal schedule.
- Comparing against simpler expanding-threshold alternatives (e.g., a linear ramp of entropy quantiles) would isolate whether the specific IQR machinery is essential beyond the ramp itself.
- A sensitivity analysis for the unimodal threshold γᵤ would rule out brittleness.

## Removed Points
The following points raised by the reviewers were removed with justifications:

- **"IQR mechanism is a structural flaw"** — The harsh critic characterized this as a fatal flaw. However, the mechanism is described (expand fences over time using f(t), select samples where enough feature dimensions fall within fences). The ambiguity is about the axis of quantile computation, which is a clarity issue, not a conceptual invalidation. The empirical validation (Figure 3b) shows the method works as intended.
- **"Missing comparison against Guo et al. (2024b)"** — The paper explicitly states (Section 2) that Guo et al. (2024b) focuses on *multimodal regression* tasks, not classification, and therefore cannot be directly compared. The critic missed this justification.
- **"Overlapping std intervals on weak OOD"** — The standard deviations in Tables 1–4 are tiny (typically 0.01–0.05), so overlapping is negligible where it occurs.
- **"μ has opposite trends suggesting lack of robustness"** — The paper explains this as a consequence of modality dominance (Kinetics50 is video-dominant, VGGSound is audio-dominant), which is a coherent explanation. The claim of stability refers to the small magnitude of variation, not identical trends.
- **"Missing oracle baseline"** — Moved to Nice-to-Haves.
- **"Hyperparameters differ across datasets"** — Common practice in deep learning; not a weakness.
- **"Existing methods fail claim is overstated"** — Trivial wording issue; the paper's core claim is about strong OOD where methods genuinely fail.
- **"Missing simpler smoothing alternative baseline"** — Moved to Nice-to-Haves.
- Various formatting, typo, and style nitpicks — Removed per system rules.
- Missing related works — Removed per system rules (no external validation possible).
- Missing appendix content — Removed per system rules (appendix exists in original submission).

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Clarify the IQR computation.** Specify in Algorithm 1 whether `quantile(h, 0.25)` is computed per-sample over feature dimensions, per-dimension across the batch, or globally over all elements. State the precise tensor operation.
2. **Fix Table 5.** Remove or correct the duplicate row. Add footnotes or standard deviations.
3. **Add an ablation for disabling MIS after t₀.** Show the effect of applying MIS throughout all iterations vs. only the first half.
4. **Add sensitivity analysis for γᵤ** across a range (e.g., [e^{-2}, e^{0}]) on both datasets.
5. **Tone down the "always fail" language** in the abstract and introduction to match the empirical reality for weak OOD.

## Score and Decision

**Calibration anchors used (all rounds):**

| Paper | Avg Score | Round | Comparison |
|-------|-----------|-------|------------|
| READ (TPZRq4FALB) — multimodal TTA, reliability bias | 8.0 | R1 (strong) | Direct baseline; cleaner method and writing. Paper under review addresses a harder problem but has clarity issues that keep it below this anchor. |
| MDAA (UhKkWHkvfg) — multi-modal continual TTA | 5.0 | R1 (mid), R2 | Rejected; weaker motivation and incomplete ablation. This paper is clearly stronger. |
| AEA (sEMJ1PLSZR) — energy alignment TTA | 6.25 | R1 (mid), R2 | Accepted poster. Comparable quality — clear motivation but some concerns about limited improvements. |
| PASLE (3Z2flzXzBY) — selective label enhancement TTA | 6.4 | R2 | Accepted poster. Similar level: novel approach with some execution concerns. Paper under review has a more novel problem formulation but less theoretical analysis. |
| SlimTTT (7iuFxx9Ccx) — resource-efficient TTT | 6.0 | R2 | Rejected. Had motivation concerns. Paper under review has stronger motivation. |

**Round 1 bracket:** Between 4 and 7. Weak anchors (avg <3.5) are clearly below this paper. Strong anchors (avg >7.5: READ at 8.0) are cleaner papers. Middle band (3.5–7.5) is where this paper sits.

**Round 2 narrowing:** Comparing against PASLE (6.4) and AEA (6.25), the paper under review has a more novel problem formulation and more comprehensive evaluation, but suffers from specification ambiguity and the table anomaly. Compared to MDAA (5.0) and SlimTTT (6.0), this paper is stronger in motivation, novelty, and empirical support.

**Final score:** 6.0 — a solid paper with a clear novel contribution (multimodal wild TTA) and strong empirical evidence, particularly in challenging strong-OOD and mixed-domain settings. The main weaknesses are specification clarity and missing ablations — these are addressable and do not undermine the core contribution, but they prevent the paper from reaching the level of a cleaner, more polished paper like READ.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>