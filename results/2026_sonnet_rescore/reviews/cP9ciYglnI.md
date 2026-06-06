## Summary
This paper introduces a shape-adaptive guidance signal — the Weighted Geodesic Distance Transform (WGDT) — for interactive cortical sulcal labeling on the spherical domain. The core contribution is solving the eikonal equation with a mean-curvature-based speed function (Eq. 4), causing wavefront propagation to follow sulcal valleys rather than expanding isotropically. This is integrated into a per-sulcus spherical CNN (SPHARM-Net) interactive framework that supports iterative click-based refinement. Experiments on 72 HCP subjects with 17 LPFC sulci show that a single WGDT-encoded click outperforms both equidistance-based signals (ADT, Disk) on all 9 small/variable sulci and three fully automatic baselines on those same structures.

---

## Strengths

- **Shape-adaptive coverage of small sulci is statistically validated**: WGDT achieves significantly higher single-click Dice scores (adjusted p < 0.05 under FDR correction) on all nine small and variable LPFC sulci compared to both ADT and Disk signals (Figure 4), directly supporting the central claim that curvature-aware encoding improves guidance for fine-grained sulcal structures.
- **Single-click interactive method outperforms automatic baselines on challenging sulci**: With one WGDT click, the model surpasses three retrained automatic baselines (Lyu et al., 2021; Lee et al., 2025a; Lee et al., 2025b) on all small sulci (Figure 5, Section 4.2). All baselines were retrained on the same dataset with the same features, making this a fair comparison.
- **Iterative refinement is consistently effective**: Dice scores increase monotonically from the 1st through 3rd click across all 17 sulci and all guidance signals (Figure 4), with small sulci reaching near-perfect accuracy by the 2nd–3rd click under WGDT (Section 4.2). The iteratively weighted loss (Eq. 7) appropriately incentivizes later corrections.
- **Rigorous evaluation design**: 5-fold cross-validation, 10 distinct initial click points per subject per sulcus, 72 subjects, and FDR correction for 17 simultaneous comparisons (Section 3.3) reflect solid experimental hygiene for a specialized neuroimaging domain.
- **Practical runtime**: A full single-click cycle (WGDT encoding + re-tessellation + forward pass) averages under 0.5 seconds (Table 2), confirming real-time usability.
- **Spherical domain avoids projection artifacts**: By operating directly on the unit sphere via spherical mapping, the framework avoids occlusion of buried cortical structures that afflicts 2D-projection-based approaches (Section 1, Figure 3).

---

## Weaknesses

### Fatal
None.

### Major

- **Missing k=0 ablation conflates two design decisions**: The key comparison in Section 4.1 pits WGDT (curvature-weighted geodesic propagation on the icosahedral mesh) against ADT and Disk (both angular-distance-based, purely on S²). This simultaneously changes two things: (1) using mesh-topology propagation vs. analytic angular distance, and (2) incorporating the curvature speed function. Setting k=0 in Eq. 4 yields F=e^0=1, i.e., unweighted geodesic propagation on the same mesh — a signal that is neither ADT nor WGDT. Without this baseline, the evidence supports "curvature-aware propagation outperforms angular distance" but does not cleanly establish that curvature weighting (the paper's stated contribution) is the active mechanism, versus mesh-based propagation topology alone. This is the paper's most important unfilled evidential gap.

### Minor

- **Idealized click simulation may inflate absolute claims**: Section 3.3 states that the 10 initial clicks are generated to "maximize both their distance from the label boundary and mutual separation," producing well-centered interior clicks. The paper's headline claim — "even a single click using the proposed encoding scheme outperforms fully automatic methods" — rests partly on near-optimal click placement. Because all guidance signals share this same click protocol, the relative WGDT-vs.-ADT/Disk comparison is unaffected. However, it is unknown whether WGDT's advantage over ADT/Disk holds when click quality degrades (e.g., clicks near sulcal boundaries or in ambiguous folds), which is directly relevant to the interactive use case the paper advocates.

- **Right hemisphere and cross-region generalizability not assessed**: All evaluations use the left hemisphere only (Section 3.1). For sulci with known lateralization differences, the scope of the claim that WGDT "outperforms" existing methods is implicitly restricted to left-hemisphere LPFC. The Discussion acknowledges generalization to other cortical regions as future work but does not address hemispheric symmetry.

- **No sensitivity analysis for the clamping range of F**: The speed function is clamped to [0.05, 10] "to mitigate propagation instability" (Section 2.3.3), but no justification for these bounds is given and no sensitivity analysis is reported. For subjects with high-amplitude curvature values, this clamping could materially alter propagation behavior.

### Trivial

- **k=8 selection for Figure 5 not fully justified in the main text**: Section 3.2 reports WGDT variants with k ∈ {6, 8, 10} in Figure 4 but uses k=8 exclusively in the automatic-baseline comparison (Figure 5). The main text does not state the criterion for choosing k=8 as the representative value; the σ selection is described as being in Appendix A.1, but the k selection criterion is absent from both the main text and the appendix reference.

---

## Nice-to-Haves

- **k=0 intermediate baseline** (addressed above as Major, but also the single highest-priority strengthening action): Adding this ablation would convert the evidential gap from a major concern into a confirmed causal claim about curvature weighting. The existing framework already supports it with trivial modification to Eq. 4.
- **Click robustness analysis**: The paper already has 10 click samples per subject. Stratifying performance by click proximity to the sulcal boundary (eccentricity) would directly test whether WGDT's advantage over ADT/Disk is robust to suboptimal placement — a practically important question for real interactive use.
- **Inter-rater reliability estimate**: Without any annotation variability metric, it is difficult to know how close to the ceiling the method is on small sulci. Even a single intra-rater test-retest Dice would anchor the results meaningfully.
- **Scalability discussion**: 17 per-sulcus models is a real operational constraint for full-cortex labeling. A brief analysis of compute cost scaling or a sketch of multi-sulcus extension would strengthen the practical case.
- **Right hemisphere validation** on a subset would increase the scope of the paper's claims substantially.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"Comparison to automatic baselines is unfair"** (raised implicitly via framing concerns): Removed. The paper explicitly states "automatic and interactive frameworks can be jointly used" and frames this comparison as demonstrating that user interaction adds value over no-input methods. The asymmetry (interactive receives a click; automatic does not) is inherent to the setup and actually favors the baselines in terms of setup fairness — this is intentionally asymmetric to prove a stronger point, and the paper's Discussion correctly identifies these as complementary. This criticism does not apply.
- **Comparison to 2D SAM-based mesh methods as missing baselines**: Removed. The paper explicitly motivates why 2D-projection methods are unsuitable for buried sulci (Section 1, Figure 3), and no interactive sulcal labeling baseline exists (Section 4.2). Demanding a comparison to methods the paper argues are architecturally unsuitable is scope creep.
- **Generic strength "addresses an important problem"**: Removed as non-specific. The domain-specific strengths (small-sulci cognition relevance) are real but were subsumed into the concrete evidential strengths above.
- **Strength Finder claim that "iterative refinement consistently improves labeling" as a distinct contribution**: Partially removed. Monotonic Dice improvement is real (Figure 4), but the iterative framework is adapted from prior work (Sun et al., 2024; Section 2.4); it is a supporting feature, not a novel contribution. Retained only as supporting evidence for usability.

---

## Novel Insights

The paper's key insight — that replacing isotropic angular distance with curvature-modulated wavefront propagation on the mesh naturally aligns the guidance footprint with sulcal valley geometry, thereby reducing spillover into adjacent non-target structures — is a principled and underexplored idea in neuroimaging interactive segmentation. The observation that guidance signal design matters disproportionately more for small/variable sulci than for large/consistent ones (a consistent pattern across Figure 4) suggests a general principle: as target structures become smaller and more variable, signal shape-awareness becomes increasingly critical relative to backbone model capacity. This has potential implications beyond sulcal labeling to any interactive segmentation task involving elongated, curved structures with complex topology.

---

## Suggestions

1. **Add k=0 unweighted geodesic baseline** in Figure 4 (trivial implementation change). This single addition resolves the paper's most important evidential gap and either confirms curvature as the active mechanism or prompts a more nuanced framing of the contribution.
2. **Stratify existing 10-click samples by distance to sulcal boundary** and report WGDT vs. ADT Dice as a function of click eccentricity. This uses data already in hand and directly addresses the click quality concern.
3. **Clarify k=8 selection criterion** in the main text (one sentence); explain whether it was chosen by validation Dice or as a middle representative, and whether results are robust across k ∈ {6,8,10}.
4. **Provide clamping sensitivity analysis** for F ∈ [0.05, 10] — even a brief table varying the bounds would justify the design choice.
5. **Include a brief right-hemisphere validation** on a subset of subjects to scope the generalizability claim more accurately.

---

**Evaluation on key axes:**
- **Originality**: Moderate-high. Applying the eikonal equation with curvature speed on the spherical domain for interactive cortical segmentation is a novel and principled combination not previously explored.
- **Importance of research question**: Moderate-high. Small sulci are increasingly implicated in higher cognitive function; reducing annotation burden is a genuine bottleneck in the field.
- **Claims support**: Moderate. Main comparative claims are statistically well-supported; the mechanistic attribution to curvature specifically is underdetermined without the k=0 ablation.
- **Soundness of experiments**: Moderate-high. Protocol is rigorous (5-fold CV, FDR correction, 10 clicks/subject), though scope is limited to left hemisphere and 72 subjects.
- **Clarity of writing**: High. The paper is well-organized, motivations are clear, and limitations are honestly acknowledged.
- **Value to research community**: Moderate-high. Useful to neuroscience interactive labeling community and potentially to the broader geometric deep learning / interactive segmentation community.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>3</originality>
<importance>3</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>4</clarity>
<community_value>3</community_value>
</subscores>