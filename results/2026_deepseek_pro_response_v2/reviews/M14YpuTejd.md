Now let me finalize my assessment. Comparing our paper against the Round 2 anchors:

- **ESDMotion (5.25):** Our paper is clearly stronger — ESDMotion has baseline fairness issues, misleading claims, and poor presentation that our paper does not suffer from.
- **SEPT (7.00):** A stronger paper — SOTA results across two benchmarks, thorough ablations, cleaner execution. Our paper has a different contribution profile (protocol correction vs. method) and doesn't match SEPT's empirical strength.
- **SmartPretrain (6.75):** Cross-dataset evaluation, model-agnostic design. Stronger empirical validation than ours.

Our paper sits between ESDMotion and SmartPretrain/SEPT. The core protocol diagnosis is solid, but the Setting 4 issue, under-specified baseline, missing variance estimates, and nuScenes-only limitation cap the score. Final score: **6.0**.

---

## Summary
This paper identifies three protocol flaws in the emerging online-map-based motion prediction paradigm (inappropriate data splits causing a train-validation gap, perception range mismatch between mapping and motion prediction, and non-discriminative ego-only/static-dominated metrics), and proposes OMMP-Bench — a corrected benchmark with a geographically-disjoint three-way split, moving-agent-only metrics stratified by distance, and a boundary-free baseline using deformable attention on raw image features to handle out-of-range agents.

## Strengths
- **Clear demonstration of the train-validation gap (Table 1, Fig. 3, Fig. 4):** The paper provides concrete evidence that the default protocol trains the motion model on highly accurate maps (map model inferring on its own training set) but evaluates on degraded maps from unseen data, creating a substantial distribution shift. The proposed three-way split directly addresses this.
- **Well-quantified perception range mismatch (Tables 2-3, Table 6):** MapTR's mAP collapses from 0.124 at 30×60m to 0.014 at 100×100m, making it impossible for online maps to cover distant agents. Table 6's stratified metrics (Close vs. Far agents) concretely exposes the performance gap (e.g., minADE 0.5585 vs. 0.6997 for HiVT+MapTR).
- **The boundary-free baseline is conceptually sensible and empirically effective (Table 7):** Using deformable attention on raw image features sidesteps the BEV range limitation. Table 7 shows consistent improvements, most notably 12.7% minADE reduction for MapTRv2-CL+HiVT on far non-ego agents (0.6274 vs. 0.6999 base).
- **The moving-agent-only metric with distance stratification (Section 3.4, Table 6):** Table 6 convincingly shows static agents are trivially predicted (minADE ≈ 0.002) while moving agents have orders-of-magnitude higher error, making the case for metric refinement that aligns with Argoverse/Waymo conventions.
- **Comprehensive benchmark spanning multiple model combinations (Table 7):** 2 map models × 2 motion models × 4 methods across 3 agent categories provides a solid empirical foundation for protocol-level claims.

## Weaknesses

### Fatal
None.

### Major
- **The random-split baseline (Table 1, Setting 4) is presented but never discussed, and it partially undercuts the spatial-overlap argument.** Setting 4 uses a random 50/50 split of nuScenes train — which inherits the same spatial overlap the authors decry — yet achieves minADE of 0.6373, close to the proposed spatial split's 0.6308 and far better than the default split's 0.6839. This suggests the train-val gap (issue 1: in-distribution vs. out-of-distribution map inference) is the dominant factor, while spatial overlap (issue 2) may matter much less than the paper claims. The paper lists Setting 4 in Table 1 without a single sentence analyzing what it means. The authors must either explain why this near-identical performance does not weaken the spatial-split rationale, or restructure their claims to focus on the train-val gap, which is already well-supported.

### Minor
- **The boundary-free baseline is under-specified in the main text.** The entire method description spans roughly five sentences and Eq. 1. While the paper references Appendix A for details, critical choices (which backbone layer provides features, number of deformable attention points, multi-view fusion strategy for agents visible in multiple cameras, spatial sampling radius) are absent from the body. The claim that the baseline "works" cannot be fully assessed from the main text alone.
- **No variance estimates across any experiment.** All tables report single scalar numbers with no standard deviations, confidence intervals, or significance testing. The motion validation set contains only 86 scenes (Section 4.1). With a set this small, variance across scenes could be large enough that the reported rankings are unstable. Adding scene-level bootstrap confidence intervals would substantially strengthen every quantitative claim.
- **The "SOTA" claim (line 198) is too narrow.** The proposed baseline is compared only against two prior methods (uncertainty prediction and BEV feature attention) from the same research group. Calling this "SOTA performance" is an overstatement and should be qualified.
- **The spatial split may introduce its own confound.** Different geographic regions may have different road geometries, traffic densities, and agent behaviors, which could make the motion validation set systematically harder or easier in ways unrelated to map quality. This should at minimum be acknowledged as a limitation.

### Trivial
- **Table 5 contains a formatting error:** Rows 2 and 3 both show "Boundary only" (✗ ✓ ✗ ✗) but with different minADE values (0.6829 vs. 0.6558). Row 3 is likely meant to be "Ped. crossing only" (✗ ✗ ✓ ✗).

## Nice-to-Haves
- Deeper analysis of *why* MapUncertaintyPrediction and MapBEVPrediction sometimes degrade non-ego close-agent prediction while improving ego prediction (Table 7) — this is a striking finding that receives only a passing mention.
- Ablation of the boundary-free baseline's design choices (feature source layer, number of deformable attention points, spatial extent of feature sampling).
- Discussion of whether the motion validation set's 86 scenes provide sufficient coverage, and computational cost of the proposed baseline.

## Removed Points
These points are flagged to be removed, treat them with caution.

- **"The introduction claims keen attention but only cites Gu et al."** — The paper cites a full related work section; the introduction's framing is reasonable for a 2024-emerging field. Removed as a nitpick.
- **"No discussion of computational overhead of spatial split"** — The spatial split is about evaluation protocol, not computational cost. Removed as category noise.
- **Demand for missing related works** — No external sources available to verify. Removed per hard rules.
- **"Limited set of mapping and motion models tested"** — 2×2×4 is reasonable coverage for a benchmark paper. Removed as a generic one-size-fits-all criticism.
- **"Statistical significance testing needed"** — Weakened to noting that variance estimates are missing, which is a real concern given the 86-scene validation set. The demand for formal significance testing is removed; scene-level CIs are sufficient.
- **Demand that the paper address why prior methods regress on non-ego agents** — Moved to Nice-to-Haves since it's a suggestion for deeper analysis, not a flaw in the paper's core claims.

## Novel Insights
The comparison between Setting 1 (spatial split) and Setting 4 (random 50/50 split) in Table 1 is genuinely revealing — it suggests the dominant factor in the train-val gap is whether the map model infers on its own training data, not spatial overlap. This is an insight the paper itself has the data for but does not discuss, and resolving this tension would sharpen the paper's contribution considerably.

## Suggestions
- Add a discussion paragraph analyzing Setting 4 of Table 1: explain what it demonstrates about the relative importance of the train-val gap vs. spatial overlap, and adjust claims accordingly.
- Move key boundary-free baseline implementation details from the appendix into the main text (even if condensed).
- Add scene-level bootstrap confidence intervals to at least Table 7's key comparisons.
- Fix Table 5's duplicate row and clarify the intended map element in row 3.
- Acknowledge that the spatial split confounds geographic region with other variables as a limitation.

## Calibration Anchors

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| pzZjyYee6L (Don't Reinvent the Steering Wheel) | 2.50 | R1 | Much weaker — marginal contribution, little empirical rigor |
| MI0UiWeqOl (Poly-Autoregressive) | 2.33 | R1 | Much weaker — unclear methodology |
| V1N6MmDY27 (Commonsense Reasoning AV) | 2.50 | R1 | Much weaker — limited evidence, niche scope |
| 1W6oINj8ne (BRSSD10k) | 3.00 | R1 | Much weaker — dataset-only, limited analysis |
| UapxTvxB3N (Trajectory-LLM) | 5.75 | R1/R2 | Weaker — unclear methodology, limited benchmarks, questionable dataset |
| sEJYPiVEt4 (ESDMotion) | 5.25 | R2 | Weaker — unfair baselines, misleading claims, poor presentation |
| k3y0oyK7sn (BEV uncertainty benchmark) | 5.40 | R2 | Weaker — narrower scope, less thorough analysis |
| LLWj8on4Rv (RouteFormer) | 6.67 | R1/R2 | Stronger — new dataset + model + metric, better empirical validation |
| mDIXfHvoqH (ITPNet) | 6.75 | R2 | Stronger — cleaner problem formulation, better execution |
| Bmzv2Gch9v (SmartPretrain) | 6.75 | R1/R2 | Stronger — cross-dataset, model-agnostic, better ablations |
| efeBC1sQj9 (SEPT) | 7.00 | R2 | Stronger — SOTA on two benchmarks, thorough ablations |

Round 1 bracket: 5.5–7.0. Round 2 narrowed: the paper is clearly stronger than the ~5.3 anchors (ESDMotion, BEV uncertainty benchmark) and Trajectory-LLM (5.75), but does not match SEPT (7.00) or SmartPretrain (6.75) in empirical thoroughness or clean execution. Final score: **6.0**.

## Score and Decision
The paper makes a genuine contribution by diagnosing real protocol flaws in online-map-based motion prediction and proposing sensible corrections. The train-val gap analysis and perception range mismatch are well-supported. However, the Setting 4 issue in Table 1 (presented but undiscussed) partially undercuts the spatial-overlap argument, the boundary-free baseline is under-specified in the main text, and the lack of variance estimates with a small validation set weakens confidence in the reported rankings. These are fixable issues that do not invalidate the core contribution but prevent a higher score.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>