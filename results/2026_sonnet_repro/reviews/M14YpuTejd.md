Now I have a clear picture of the paper. Let me verify the key claims — particularly Table 5's duplicate row and Table 1's split comparison — before proceeding to calibration.

**Verification of key reviewer claims:**

1. **Table 5 duplicate row** (Lines 246-247): Two rows both show ✗|✓|✗|✗ (Boundary only) but with values 0.6829 and 0.6558. This is a genuine inconsistency in the paper as parsed.

2. **Table 1 cross-val-set comparison** (Lines 108-113): Split 1 is evaluated on "Motion Val" (86 scenes), Split 3 on "nuScenes Val" — genuinely different test sets. Direct numeric comparison is confounded.

3. **86-scene val set** (Line 275): confirmed — 86 scenes, no variance/CI reported.

4. **"Centerlines most helpful" without a centerlines-only row**: Table 5 does not include a centerlines-only row but the text claims "centerlines only achieve the second best performance" (Section 3.5). The text appears to be comparing the combined rows rather than having an isolated centerlines row.

5. **Split 4 achieving 0.6373 vs Split 1's 0.6308**: confirmed — the spatial disjointness contribution is not cleanly isolated.

Now let me run calibration search.Round 1 bracket: **5 to 7**. This paper sits above the weak anchors (2.5-3.33) but below the strong anchors (8.0). It addresses real problems in an emerging protocol, but the val set is small, the table comparison is confounded, and Table 5 has inconsistencies. Let me narrow.Now I have enough to write the final consolidated review. Let me read one more anchor for calibration.Now I have sufficient calibration data. Let me write the final consolidated review.

---

## Summary

OMMP-Bench is a corrective benchmark paper that identifies three systematic methodological flaws in the emerging online map based motion prediction (OMMP) protocol: (1) a severe train-validation gap caused by an inappropriate two-stage data split, (2) a perception range mismatch between online mapping models (~30×60m) and motion prediction requirements (>100m), and (3) non-discriminative metrics due to inclusion of static agents and exclusive evaluation of the ego vehicle. The authors propose a three-way spatially disjoint data split, refined metrics for moving non-ego agents partitioned by distance, and a lightweight boundary-free baseline using deformable attention over image features. Experiments across two map models (MapTR, MapTRv2-CL) and two motion predictors (HiVT, DenseTNT) validate the benchmark's setup.

---

## Strengths

- **Compelling quantification of the train-validation gap.** Figure 3 directly shows MapTRv2-CL mAP dropping from 87.6 (on the training set, seen during map model training) to 50.3 (on the unseen val set). This demonstrates a genuine and large distribution shift — it is not a theoretical argument but a directly measured effect. Figure 4 confirms the underlying cause: 87% spatial overlap between training and validation sets under the default split, reduced to 5% under the proposed split.

- **Principled correction of agent selection and metric design.** Table 6 shows static agents achieve minADE ≈ 0.002 (essentially zero), confirming that including them in aggregate metrics renders comparisons meaningless. The two-group (close/far) partition by whether agents fall within the online map's perception range is well-motivated and directly tied to the paper's range-mismatch finding. These metric corrections are justified, specific, and grounded in experimental evidence.

- **Effective boundary-free baseline for the range-mismatch problem.** Table 7 confirms consistent improvements from the image-feature (img) baseline specifically for far agents across all four map+motion model combinations tested. The reduction for HiVT+MapTRv2-CL is 12.7% in minADE for far agents, while improvements for close or ego agents are much smaller, correctly confirming the mechanism (image features compensate only for out-of-range agents).

- **Systematic multi-model coverage.** Table 7 provides a 4×4 combination matrix across map models, motion models, and integration methods, confirming that the benchmark's trends (stronger map model → better motion, image fusion → better far-agent performance) replicate consistently rather than being method-specific artifacts.

---

## Weaknesses

### Fatal
None.

### Major

- **Table 1 comparison is confounded by different validation sets.** Split 1 (proposed) is evaluated on the motion val set (86 scenes), while Split 3 (default) is evaluated on nuScenes val. As stated in Table 1's own column header, the "Evaluation" sets differ. The authors conclude "the split of OMMP-Bench leads to an explicit performance enhancement compared to the default split," but comparing absolute minADE numbers across different validation sets is not valid — the populations of agents, their density distribution, and geographic diversity all differ. The train-val gap *argument* is independently supported by Figure 3's mAP comparison, which is compelling, but Table 1's quantitative comparison cannot carry the weight placed on it. The paper should either restrict this comparison to an internally consistent setting, or clearly frame the table as illustrating two different regimes rather than directly comparing split quality.

- **Motion validation set of 86 scenes is small, and no variance estimates are reported.** The paper states (Section 4.1) the split is 367/397/86 scenes. For a paper whose primary contribution is establishing a corrected benchmark, the reliability of the evaluation numbers is a foundational concern. Several comparisons in Table 7 involve minADE differences of 1–5% (e.g., base vs. unc vs. bev for moving non-ego close agents). Without standard deviations, confidence intervals, or multiple-run averages, it is impossible to determine whether these differences are statistically meaningful. The paper needs at minimum a characterization of result stability across random seeds, especially since this benchmark is intended as a community reference.

- **Table 5 contains a duplicate row that undermines the map element analysis.** Lines 246–247 in the parsed paper show two rows with identical element selection (✗|✓|✗|✗, boundary only) but different minADE values: 0.6829 and 0.6558. This is the central table for the map element analysis, and with an ambiguous row the conclusions about which elements are most informative cannot be reliably drawn. The paper also claims in Section 3.5 that "centerlines are most helpful and centerlines only achieve the second best performance," yet no row in Table 5 shows centerlines in isolation. The supporting evidence for the centerline claim is indirect at best and relies on a table with a parsing inconsistency.

### Minor

- **The necessity of spatial disjointness vs. stage separation alone is not cleanly established.** Table 1 shows Split 4 (random 50%/50% of training set) achieves minADE of 0.6373, close to Split 1's 0.6308. This suggests much of the gain comes from simply using separate data for each stage, not from spatial disjointness per se. The paper does not discuss this directly. The spatial disjointness contributes to better evaluation of the online map's generalization, which is independently valuable, but the paper presents both properties together without isolating their contributions.

- **The paper does not show whether rankings change under the new protocol.** The strongest argument for OMMP-Bench would be that methods ranked differently under the new protocol than under the old one — i.e., that the previous protocol was not just giving inflated absolute numbers but actually rewarding the wrong methods. The paper shows that absolute numbers change but does not demonstrate that old-protocol rankings are misleading. This omission weakens the practical necessity argument, reducing the claim to "our absolute numbers are more honest" rather than "the field has been reaching wrong conclusions about which methods are best."

- **The range collapse (mAP 0.164→0.002 for MapTRv2-CL when extended to 100×100m) is presented as evidence of a fundamental limitation.** But this could equally be a training distribution mismatch — the model was trained on 30×60m data and naively extended. Section 3.3 frames this as showing "current online map prediction models cannot fully meet the perception range requirements," which is accurate, but the implication that this is a hard ceiling is not supported. The paper should clarify whether fine-tuning on 100×100m data was attempted.

### Trivial
None beyond parser artifacts already excluded.

---

## Nice-to-Haves

- A centerlines-only ablation row in Table 5 would directly support the "centerlines are most helpful" claim in Section 3.5 rather than requiring the reader to infer it from increment-over-boundary comparisons.
- A breakdown of the image-feature baseline improvement as a continuous function of agent distance from ego (rather than the binary close/far split) would make the mechanism more transparent and help future work calibrate when image features are needed.
- Migration costs of the new benchmark (re-running prior methods to enable comparison to existing literature) should be explicitly acknowledged, even if re-runs are not provided.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"The comparison against the default (Split 3) should be framed as our split eliminates a known confound rather than our split achieves better performance"** — Retained as a Major weakness (Table 1 confound), but the underlying train-val gap claim is kept as a Strength since it is independently well-supported by Fig. 3.

- **"Variance in 1–2% could make several comparisons in Table 7 inconclusive"** — The specific numbers (1–2% variance) are speculative; the concern about variance is real and retained as Major, but the specific quantification is removed.

- **"SOTA claim in Table 4 is scoped narrowly"** — The paper does not explicitly claim a global state-of-the-art; the table shows comparisons on the new benchmark only. This is an implicit framing issue at most. Removed as too minor.

- **Strength: "comprehensive benchmark experiments spanning multiple map models and motion predictors"** — Retained as a strength but qualified; the coverage is multi-model but restricted to nuScenes only, two map models, and two motion predictors.

- **Strength: "systematic analysis of map element types"** — Partially removed because Table 5's duplicate row undermines this contribution; it is demoted to Major weakness rather than cited as a strength.

- **Harsh critic's "Strengthening the Paper" section regarding ranking changes** — Retained as a Minor weakness (paper does not show ranking changes under new protocol).

---

## Novel Insights

The paper's most genuinely novel empirical insight — that the train-val gap in online map based motion prediction is primarily caused by the map model's near-perfect performance on its own training set (mAP 87.6) versus its much lower performance on unseen data (mAP 50.3) — has direct field-wide implications. This is not a marginal measurement concern but a structural flaw in how a CVPR 2024 best-paper finalist protocol was executed. The second novel insight — that evaluation focused solely on the ego vehicle systematically masks the range-mismatch problem, because the ego vehicle is almost always within the map's coverage — is elegant and makes the metric-correction contribution organically tied to the other findings rather than being a separate standalone concern.

---

## Suggestions

1. **Fix Table 5** by resolving the duplicate row (likely one row is a different ablation or map model); add a centerlines-only row; and ensure the map element conclusions are drawn from an unambiguous table.
2. **Add a statistical reliability section** characterizing result variance across seeds or bootstrap resamples of the 86-scene val set, which is essential for a benchmark paper.
3. **Reframe Table 1** to clearly acknowledge that Split 1 and Split 3 use different validation populations; restrict the quantitative comparison to internally consistent settings or use relative rather than absolute metrics.
4. **Add an ablation separating spatial disjointness from stage separation** (e.g., use the same motion train/val partition as Split 1 but allow spatial overlap, and compare to Split 1) to precisely attribute where the performance gap comes from.

---

## Score and Decision — Calibration Report

**All retrieved anchors:**

| Path | Avg Score | Round | Comparison to OMMP-Bench |
|---|---|---|---|
| pzZjyYee6L.md (trajectory forecasting w/ kinematics) | 2.50 | R1 | Much weaker; rejected; limited contribution |
| 324fOKW1wO.md (SimDT, imitation learning AD) | 3.33 | R1 | Weaker; rejected; limited novelty |
| V1N6MmDY27.md (commonsense reasoning AV) | 2.50 | R1 | Weaker; rejected |
| DCg9r2DKKe.md (STL-Drive formal verification) | 2.50 | R1 | Weaker; rejected |
| sEJYPiVEt4.md (ESDMotion SD maps motion pred) | 5.25 | R1 | Comparable; proposes novel modules + experiments; rejected; similar methodological depth |
| 72MSbSZtHv.md (RedMotion redundancy reduction) | 5.33 | R1 | Comparable; proposes new pretraining; rejected |
| cvGdPXaydP.md (world models planning) | 4.25 | R1 | Slightly weaker |
| ZPCBcR7Drg.md (MapDR benchmark) | 5.00 | R1,R2 | Comparable benchmark paper; more limited execution |
| k3y0oyK7sn.md (BEV uncertainty benchmark) | 5.40 | R2 | Similar benchmark scope; accepted; slightly more methodologically complete |
| DUkYDXqxKp.md (DriveGPT4) | 4.75 | R2 | Weaker; rejected |
| ga1IraEqTE.md (A2Perf benchmark) | 4.75 | R2 | Weaker benchmark; rejected |
| Vv76fCYffN.md (SSR end-to-end AD) | 6.40 | R2 | Stronger; accepted; more novel model design |
| MW8DN8BE3g.md (Uni-Map HD map construction) | 6.25 | R2 | Comparable-to-slightly stronger; rejected; more technical depth |
| efeBC1sQj9.md (SEPT motion prediction SSL) | 7.00 | R2 | Stronger; accepted; more methodological novelty + larger-scale validation |
| E8S5Upr6oO.md (MGMapNet multi-granularity map) | 6.00 | R2 | Comparable; accepted; proposes a novel architectural component |

**Round 1 bracket:** 5.0–7.0.

**Round 2 narrowing:** Within the bracket, the closest topical anchors are ESDMotion (5.25, rejected), the BEV uncertainty benchmark (5.40, accepted), and MGMapNet (6.0, accepted). OMMP-Bench is weaker than SEPT (7.0) and SSR (6.40) in methodological novelty, comparable in scope to the BEV uncertainty benchmark (5.40), and has more genuine field-wide impact than ESDMotion but is hampered by the Table 5 issue, small val set, and Table 1 confound. The paper is better than the weak anchors but does not reach the technical depth of the 6.0–7.0 anchors. Positioning: slightly above the BEV uncertainty benchmark (5.40) given the importance of the problem addressed, but held down by the three Major weaknesses. 

**Final score: 5.5** — The paper makes a genuine and important contribution to correcting field-wide methodology in an emerging protocol, with compelling empirical evidence for the train-val gap. However, the small evaluation set (86 scenes) with no variance reporting, the confounded Table 1 comparison, and the duplicate row in Table 5 collectively reduce confidence in the benchmark's own rigor, which is the paper's primary claim to contribution.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>