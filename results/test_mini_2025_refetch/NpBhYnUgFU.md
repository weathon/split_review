Now I have all the evidence I need. Let me produce the final consolidated review.

## Round 1 — Bracketing

Based on initial calibration results:

- **Weak band (<3.5)**: Papers on remote sensing / ZSL with avg scores 1.67–3.00 (e.g., PSzDG612AC at 3.00, 11oqo92x2Z at 2.50) — these have fundamental flaws or trivial contributions.
- **Middle band (3.5–7.5)**: 
  - GC-CLIP (4.75, Reject) — added preprocessing to CLIP, had comprehensive ablations, rejected for limited novelty
  - Z-CBM (4.83, Reject) — new CBM method, rejected for lack of novelty
  - ZeroDiff (6.67, Accept Poster) — strong ZSL with diffusion, good ablations
  - ClusPro (6.0, Accept Poster) — solid CZSL method
- **Strong band (>7.5)**: Various top papers at 8.0 — clearly stronger than this submission.

**Initial bracket: between 3.5 and 5.5.**

## Round 2 — Narrowing

Pulling anchors inside the bracket:

The most relevant comparator is **GC-CLIP (4.75, Reject)**: simple method adding preprocessing to CLIP, with comprehensive ablations, yet still rejected for limited novelty and marginal improvement. **SuperCAT lacks ablations entirely**, making it weaker in evidential support. The **Z-CBM (4.83, Reject)** was also rejected for novelty issues. Comparing SuperCAT to these anchors, it is comparable or weaker.

**GenZSL (3.5, Withdrawn/Reject)** is a very weak ZSL paper. SuperCAT is clearly stronger than this anchor, showing consistent results across 12 settings.

I bracket the paper between 3.5 and 4.5 after narrowing.

Below is my final review:

---

## Summary

SuperCAT proposes a multi-module framework for conventional zero-shot scene classification in remote sensing images. The pipeline chains super-resolution (ResShift) as preprocessing, a cross-semantic attribute-guided Transformer (CAT, from Chen et al. 2021a), f-VAEGAN feature generation (from Xian et al. 2019), and a feature refinement module (FR, from Chen et al. 2021b). The method is evaluated on three benchmark datasets (UCM21, AID30, NWPU45) across multiple seen/unseen splits, reporting top-1 CZSL accuracy. Code is provided.

---

## Strengths

- **Consistent CZSL improvements across all three datasets and all splits.** SuperCAT outperforms all baselines (including the strongest, RSZero-CSAT) on all 12 settings (3 datasets × 4 splits). For example, on AID30 25/5, SuperCAT achieves 69.80% vs. RSZero-CSAT's 66.90%, and on NWPU45 25/20, 38.69% vs. 36.60%. The consistency of the direction of improvement across settings provides some evidence that the overall framework contributes positively.

- **t-SNE visualization shows qualitative feature separation improvement.** Figure 2 illustrates that visual features transition from a dense overlapping cloud (CNN backbone, 63.3% accuracy) to moderately separable clusters (after CAT, 73.4%) to well-separated clusters (after FR, shown as SuperCAT). While t-SNE has known limitations, the progression is visually clear and consistent with the quantitative gains.

---

## Weaknesses

### Fatal
None.

### Major

1. **No ablation study — the core contribution claim is untestable.** The framework chains four components from prior work (super-resolution + CAT + f-VAEGAN + FR). The paper provides zero ablation analysis: no single component is removed, replaced, or isolated to measure its contribution. The strongest baseline (RSZero-CSAT) already uses semantic attributes, a similar CAT module, and f-VAEGAN. Without ablations, the reader cannot determine whether the super-resolution, the FR module, the specific CAT instantiation, or mere hyperparameter differences drive the improvements. For a paper whose claimed contribution is a specific combination of modules, this is a critical evidential gap.

2. **GZSL results are not reported despite being motivated by the paper's own design.** The paper describes both CZSL and GZSL settings in the introduction (lines 19–23), defines the GZSL problem in the notation section (line 55), and uses a self-calibration loss (Eq. 30) explicitly designed to mitigate bias toward seen classes — a GZSL concern. Yet only CZSL top-1 accuracy is reported. The self-calibration loss is standard in GZSL; reporting only CZSL leaves a central design choice unevaluated. This omission undercuts the paper's claim that the framework handles the seen/unseen trade-off.

3. **Novelty relative to prior work is overstated; the paper does not clarify what architectural modifications were made to existing modules.** The CAT module is cited as "This module (Chen et al., 2021a) comprises…" (line 65), f-VAEGAN is from Xian et al. 2019, and the FR module is from Chen et al. 2021b. The paper states it "leverages," "employs," and "uses" these components, but never specifies what (if any) modifications distinguish the instantiation from the source papers. The contributions list (lines 30–35) frames these as proposed/provided contributions, which conflates adaptation with invention.

### Minor

- **Super-resolution contribution is claimed but unmeasured.** The paper "innovatively combines super-resolution with the zero-shot scene classification task" (line 31) as a contribution. However, ResShift is applied as a fixed preprocessing step before the CNN backbone (line 41), with no integration into the learning loop and no comparison of the pipeline with vs. without super-resolution. The claim is not supported by evidence.

- **Improvements are modest and standard deviations overlap.** Gains over the strongest baseline (RSZero-CSAT) range from ~0.8% to ~3%, while standard deviations are typically ±2–11%. For example, on NWPU45 35/10: SuperCAT 57.57±5.75 vs. RSZero-CSAT 56.80±6.23 — a 0.77% gain. No statistical significance tests are reported. The consistent direction of improvement across settings partially mitigates this concern, but the individual comparisons are not statistically compelling.

- **No discussion of limitations or failure cases.** The conclusion (Section 4) is a summary with no limitations section, no analysis of when the method fails, and no discussion of the substantial hyperparameter count (λ values in Eqs. 33–35, 42) or sensitivity thereof. This is a completeness issue for a paper proposing a complex multi-module pipeline.

- **Qualitative evidence relies solely on t-SNE** (Figure 2), which is known to create apparent structure even from noisy features. Quantitative cluster metrics (NMI, silhouette score) would strengthen this evidence.

### Trivial

- **Nonstandard notation:** The ⊙ symbol (Eqs. 40–41) is used to denote concatenation, which conflicts with standard usage for element-wise multiplication. Additionally, Eq. 41 (̃\(m_u = \tilde{m}_u \odot l_u \odot \tilde{r}_u\)) has a recursive definition that appears to be a typo — the left-hand side should likely use the unrefined feature \(m'\) or \(\tilde{m}\).

- **RS19 listed in Table 1** but never used in any experiment.

---

## Nice-to-Haves
- Hyperparameter sensitivity analysis for the multiple λ coefficients.
- Computational cost / runtime analysis for the multi-stage training pipeline.
- Comparison with more recent ZSL methods (e.g., transformer-based or CLIP-based approaches).

---

## Removed Points

- **Parser-artifact concern about Eq. 37** (duplicated variable on RHS): This is a likely PDF extraction artifact; the hard rule excludes formatting issues.
- **Attribute construction not described**: Attributes are cited from Rambabu et al. (2024); this is addressed by reference.
- **Criticism that the paper is "nothing more than stacking existing modules"**: While the modules are from prior work, the paper's claim is the combination and application to remote sensing ZSL, which is a valid (if incompletely supported) contribution framing. The core weakness is the lack of evidence for this combination, not the act of combining itself.
- **"The paper should demarcate which parts are original"**: The paper clearly cites sources. The absence of explicit "this is our modification" statements is a presentation gap, not a fatal flaw; it is subsumed by the ablation-and-novelty weakness above.
- **Strength about "detailed formulation with explicit loss functions"**: Providing equations is standard practice; this is not a distinguishing strength.
- **Strength about "super-resolution as a novel component"**: Conflicts with verified weakness (#4) — its impact is unmeasured.
- Missing related works (no external sources to verify).

---

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface an unanticipated synthesis or cross-cutting observation that the paper itself does not make.

---

## Suggestions

1. **Add a systematic ablation study** removing each component (super-resolution, the two-way CAT cross-attention, the FR module) individually. Report the CZSL and GZSL accuracy drops. Without this, the paper's central claim is unverifiable.
2. **Report GZSL results (harmonic mean of seen/unseen accuracy)** for all datasets and splits. The self-calibration loss is designed for this setting, so reporting GZSL is necessary to validate that design choice.
3. **Compare the pipeline with and without super-resolution** to substantiate the claim that it "innovatively combines" super-resolution with ZSL.
4. **Discuss limitations** — particularly the reliance on manually defined attributes, the high variance across random splits, and the sensitivity to hyperparameters.
5. **Clarify what modifications (if any) were made to the CAT, f-VAEGAN, and FR modules** relative to their source papers.

---

## Score and Decision

### Calibration Anchors

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| PSzDG612AC.md | 3.00 | 1 (weak band) | Much weaker — withdrawn with fatal flaws |
| wy9FRV8O5s (ZeroDiff) | 6.67 | 1 (mid band) | Stronger — clear novelty, good ablations, accepted |
| eE2PXlNydB (ClusPro) | 6.00 | 1 (mid band) | Stronger — well-motivated, good experiments, accepted |
| 9JxQyat11M (GC-CLIP) | 4.75 | 2 (narrowing) | Stronger — had comprehensive ablations, still rejected for limited novelty |
| 5Aem9XFZ0t (Z-CBM) | 4.83 | 2 (narrowing) | Comparable — also limited novelty and rejected |
| Jy0MJYZEuN (GenZSL) | 3.50 | 2 (narrowing) | Weaker — withdrawn, more fundamental flaws |

**Round-1 bracket:** 3.5 – 5.5  
**Round-2 narrowing:** 3.5 – 4.5, with anchors at 3.5 (much weaker), 4.75–4.83 (stronger in terms of evidence), and 6.0+ (clearly stronger).

The paper presents consistently positive results across 12 settings, which distinguishes it from the weakest anchors. However, the absence of ablation analysis and GZSL evaluation, combined with marginal per-split improvements and overclaimed novelty, place it clearly below the GC-CLIP (4.75) and Z-CBM (4.83) anchors — both of which had more complete experimental evidence and were still rejected.

**Score: 4.0** — Marginally below the acceptance threshold. The paper addresses a relevant problem and shows consistent (if modest) improvements, but the lack of an ablation study and missing GZSL evaluation prevent the reader from verifying the claimed contributions. Substantial revision is needed.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>