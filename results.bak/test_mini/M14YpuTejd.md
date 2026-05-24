Now I have all the information I need. Let me compile the final review.

## Summary

This paper identifies and addresses three fundamental protocol flaws in the emerging paradigm of online-map-based motion prediction for autonomous driving: (1) the train-validation gap caused by overlapping spatial splits and the two-stage training paradigm, (2) misaligned perception ranges between online mapping models (~30×60m) and motion prediction needs (agents up to 100m away), and (3) non-discriminative metrics that evaluate only the ego vehicle. The authors propose **OMMP-Bench**, a benchmark with a spatially-disjoint three-way split, refined metrics evaluating moving non-ego agents with close/far stratification, and a boundary-free baseline that uses Deformable Attention to retrieve raw image features for out-of-range agents. Experiments across 16 model configurations validate the proposed corrections and reveal patterns hidden under prior evaluation protocols.

## Strengths

1. **Identifies three genuine, nontrivial protocol flaws.** The train-val gap (Fig. 3 Upper: mAP drops 87.6→50.3), the perception range mismatch (Table 2: MapTR mAP collapses from 0.124 to 0.014 when extending range from 30×60m to 100×100m), and the ego-only evaluation masking real performance (Table 6: static agents achieve minADE 0.002 while moving non-ego reach 0.6307) are all concretely documented with evidence. These are not speculative concerns — the paper quantifies each issue.

2. **The spatially-disjoint split is a principled fix.** Table 1 shows the proposed split (Setting 1) achieves better minADE (0.6308) than the default protocol (Setting 3: 0.6839), demonstrating that eliminating the train-val gap meaningfully improves motion model evaluation. The overlap reduction from 87% to 5% (Fig. 4 caption) is a concrete, measurable improvement.

3. **Reformulated metrics (moving non-ego only, close/far stratification) reveal structure that prior metrics hide.** Table 7 shows that some methods improve ego prediction while harming non-ego far agents (e.g., MapTRv2-CL+DenseTNT unc increases far-agent minADE from 2.2742 to 2.3666). This finding is practically important for safety-critical deployment and would be invisible under the old protocol.

4. **Comprehensive results across 16 configurations.** Table 7 evaluates 2 map models × 2 motion models × 4 methods, with per-group metrics (ego, close, far), providing a useful reference for the community. The analysis of map element types (Table 5) offers actionable guidance for online mapping design.

## Weaknesses

### Fatal
None.

### Major
- **Single-dataset evaluation (nuScenes only).** The paper acknowledges that nuScenes is currently the only dataset providing raw camera data, HD maps, and agent trajectories simultaneously. However, this limits the generality of the benchmark's conclusions. The spatial overlap patterns, perception range requirements, and agent distributions may differ on other datasets (e.g., Waymo Open Motion, Argoverse 2). Without at least discussion or partial validation on additional data, it is unclear whether the identified issues and proposed fixes transfer.

- **Limited model zoo.** Only 2 mapping models (MapTR, MapTRv2-CL) and 2 motion models (HiVT, DenseTNT) are evaluated. While this is a reasonable starting point, a benchmark aiming to "become the standard" would benefit from broader coverage — e.g., StreamMapNet for mapping, MTR/QCNet for motion prediction. The current coverage makes it difficult to assess whether the findings (e.g., about the baseline's effectiveness) generalize across architectural families.

### Minor
- **Split construction methodology is underspecified in the main paper.** The paper states "we manually check the whole dataset and split it into three spatially disjoint sets" (line 179) and provides scene counts (367, 397, 86). The Appendix (removed by the parser) is referenced for "detailed rules of the pipeline." While the high-level approach is clear, the main text alone does not provide enough detail for exact reproduction — e.g., how spatial overlap was determined (GPS coordinates? driving route boundaries?), what threshold was used to declare two scenes "disjoint," and how edge cases were handled. This is addressable in a camera-ready version.

- **The boundary-free baseline is technically incremental.** Using Deformable Attention to retrieve image features from projected agent positions (Eq. 1) is a sensible and effective approach, achieving best minADE (0.6163 vs 0.6375 base for HiVT+MapTR, Table 4). However, it is a straightforward application of an existing mechanism (Deformable Attention). The contribution here is the *identification* of the out-of-range problem and the *idea* of bypassing map-range limitations with image features, not a novel architectural innovation. This does not weaken the paper (the benchmark framing does not require a novel method), but it should be accurately characterized.

- **No error bars or statistical significance.** Results are reported as point estimates without variance across runs. While single-run evaluation is standard practice in this subfield, the absence is worth noting given that some improvements (e.g., 0.6308 vs 0.6373 in Table 1 Setting 1 vs 4) are small enough that run-to-run variance could affect conclusions.

### Trivial
None.

## Nice-to-Haves
- Including a third motion prediction model (e.g., MTR or QCNet) would strengthen the generality of the findings.
- The boundary-free baseline could be compared more directly by ablating the Deformable Attention mechanism itself (e.g., average pooling vs attention as a simpler alternative).

## Removed Points

- **"Uncontrolled comparison for the baseline" (Harsh Critic):** Removed. The comparison in Tables 4 and 7 is controlled: all methods (base, unc, bev, img) are applied on top of the same base architectures (HiVT+MapTR, HiVT+MapTRv2-CL, DenseTNT+MapTR, DenseTNT+MapTRv2-CL). Each adds a different conditioning mechanism, but the base model, data split, and evaluation protocol are held constant. This is a fair comparison.
- **"Underspecified split procedure" framed as a major weakness:** Downgraded from major to minor. The paper provides scene counts, the non-overlap principle, and a figure showing spatial coverage. The Appendix (removed by parser) contains additional details. The main text is sufficient to understand the methodology, though not for exact reproduction without the appendix.
- **Strength Finder generic strengths (#1, #2 about the problem being important/gaining attention):** Removed. These are framing motivations, not evidence-backed strengths of the paper.
- **Formatting nitpicks and parser artifacts:** Removed per Hard Rules.

## Novel Insights

The reviews do not surface observations beyond the paper's own contributions. The paper itself already articulates the key insight clearly: the online-map-based motion prediction community has been operating under a protocol with three intertwined flaws that systematically overestimate performance and mask important failure modes. The finding that one method can simultaneously improve ego prediction and *worsen* far-agent prediction (Table 7, MapTRv2-CL+DenseTNT unc) is a genuinely non-obvious result that the proposed benchmark uniquely surfaces.

## Suggestions

1. Provide a precise algorithmic description of the split construction procedure (overlap detection method, distance threshold, edge case handling) — either by restoring Appendix A content into the main paper or by giving a self-contained summary.
2. Add a discussion section on dataset scope: what would be needed to extend OMMP-Bench to other datasets (Waymo, Argoverse 2), and what properties of nuScenes might affect the generality of the findings.
3. Include variance estimates (or at minimum, multi-seed runs) for key comparative results, especially Table 1 and Table 4.

## Score and Decision

### Calibration

**Round 1 (Bracketing):**
- Weak anchors (avg < 3.5): papers on low-quality end-to-end driving papers (scores 2.00–3.00). Our paper is clearly stronger.
- Middle anchors (avg 3.5–7.5): 
  - `/home/wg25r/review_agent/human_reviews_2026/mxz5RqhCMe.md` (4.67, Poster) — Online HD mapping stability benchmark. Narrower focus (one metric dimension) but 42 model variants. Our paper: broader conceptual contribution, fewer models.
  - `/home/wg25r/review_agent/human_reviews_2026/aqwtK0OIGs.md` (4.50, Reject) — SD map motion prediction. Method+benchmark paper, weaker contributions. Our paper is stronger.
  - `/home/wg25r/review_agent/human_reviews_2026/epbzV3FLcI.md` (6.00, Poster) — ONR: new dataset (30K scenarios), model, and metric. More comprehensive than our paper.
  - `/home/wg25r/review_agent/human_reviews_2026/DUtfVs1xxD.md` (4.00, Reject) — Uni-PrevPredMap. Weaker contribution.
- Strong anchors (avg > 7.5): papers on unrelated topics (embodied navigation, RL, 3D reconstruction). Not comparable.

Initial bracket: **4.5–6.5**

**Round 2 (Narrowing):**
- `/home/wg25r/review_agent/human_reviews_2026/FDDKQD0Imb.md` (5.00, Reject) — Rebenchmarking monocular occupancy. Similar structure (identifying training-evaluation inconsistencies, proposing corrected benchmark). Our paper is stronger: more issues identified, better-validated solutions. → Our paper should score above 5.00.
- `/home/wg25r/review_agent/human_reviews_2026/OrgL5DsU0f.md` (6.50, Poster) — DrivingGen benchmark. Much more comprehensive (14 models, diverse dataset, novel metrics). Our paper's scope is more limited. → Our paper should score below 6.50.
- `/home/wg25r/review_agent/human_reviews_2026/t1vMYl1yhe.md` (6.67, Poster) — Motion forecasting with trajectory grids. Method paper, different type of contribution. Not directly comparable.

Final score: **5.5**. The paper sits between the weaker benchmark papers (4.67–5.00) and the comprehensive benchmarks (6.00–6.50). It identifies real, important issues and provides practical fixes, but is limited by single-dataset evaluation and a small model zoo. The conceptual contribution is solid and the evidence supports the claims.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>