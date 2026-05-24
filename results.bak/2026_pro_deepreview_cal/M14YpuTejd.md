Now I have a good calibration picture. Let me write the final consolidated review.

**Bracketing**: Round 1 placed the paper between approximately 5.0 (MapDR) and 7.0 (SEPT). Round 2 narrowed to ESDMotion (5.25) and SEPT (7.0) / SmartPretrain (6.75). The paper is clearly stronger than ESDMotion (which had limited novelty, older baselines, more questionable claims) but not as polished as SEPT (which had SOTA leaderboard results, extensive ablations, cleaner execution). I'd place it around 6.0 — a solid contribution with some execution gaps that keep it from being a clear-cut strong accept.

Now let me produce the final review.

---

## Summary
This paper identifies three practical misconceptions in the emerging two-stage protocol for online-map-based motion prediction: (1) inappropriate dataset splits that create a train-validation gap for the downstream motion model, (2) mismatched perception ranges between online mapping models and motion prediction, and (3) non-discriminative metrics that overemphasize easy cases (static agents, ego-only). The authors propose OMMP-Bench, which introduces a spatially disjoint three-way data split for nuScenes, refined evaluation metrics (moving non-ego agents, close/far stratification), and a boundary-free baseline that fuses image features via deformable attention to aid agents beyond the map's coverage. Experiments across multiple map-model and motion-model combinations demonstrate consistent trends validating the identified issues.

## Strengths
- **Convincing identification of the train-validation gap**: The paper clearly demonstrates that the default two-stage protocol trains the motion model on high-accuracy maps (from the mapping model's own training set) but evaluates on low-accuracy maps (from unseen data), creating a harmful distribution shift. The proposed three-way split eliminates this gap, yielding improved motion prediction (Table 1: minADE 0.6308 vs. 0.6839 for the default split, and 0.7006 for the split that retains the gap).
- **Rigorous documentation of the range-mismatch problem with an effective mitigation**: Tables 2-3 show that online map models degrade severely when extended to 100×100m range (MapTRv2-CL mAP drops from 0.164 to 0.002), yet wider GT maps do improve motion prediction. The boundary-free baseline using image features via deformable attention yields consistent improvements, especially for far agents (Table 7: e.g., HiVT+MapTRv2-CL far minADE drops from 0.7071 to 0.6274), providing evidence that image features can compensate for missing map context.
- **Useful metric redesign that reveals hidden difficulty stratification**: Table 6 shows static agents are trivially easy (minADE 0.002) while distant agents are much harder (minADE 0.6997 vs. 0.5585 for close agents), justifying the focus on moving non-ego agents and close/far stratification. This exposes real challenges that ego-only evaluation obscures.
- **Actionable map-element analysis**: Table 5 provides practical guidance that all map element types yield the best motion prediction and that centerlines are the single most valuable element type — directly useful for co-design of mapping and prediction models.

## Weaknesses

### Fatal
None.

### Major
- **Lack of statistical reliability measures for a benchmark contribution**: The motion validation set contains only 86 scenes (Sec. 4.1), and all results in Tables 1, 4, 6, 7 are point estimates without confidence intervals, standard deviations, or seed-level variance. For a paper whose primary contribution is a benchmark intended to replace existing evaluation protocols, this is a significant evidential gap. Differences as small as 0.003–0.01 in minADE between methods (e.g., base vs. unc for close non-ego agents in Table 7) are discussed as meaningful patterns without any indication of whether they are distinguishable from noise. A benchmark must demonstrate that its metrics are stable enough to support the comparisons it enables; the current presentation does not establish this.

### Minor
- **Spatial split not clearly justified against simpler alternatives**: Table 1 shows that a simple random 50-50 hold-out of the nuScenes training set (Split 4, minADE 0.6373) yields metrics close to the proposed spatial split (Split 1, minADE 0.6308), though evaluated on different sets. The paper's argument for spatial disjointness — preventing overlap-based overestimation of the online mapping model's generalization — is plausible but not directly tested. An experiment showing whether spatial overlap inflates downstream motion prediction metrics would substantially strengthen the case for the labor-intensive manual spatial split.
- **Boundary-free baseline is under-specified**: The description of image-feature integration (Sec. 3.3, Eq. 1) is brief: it states that deformable attention aggregates features per agent using camera parameters and agent positions, but does not specify how these features are injected into HiVT/DenseTNT, whether the image backbone is frozen or fine-tuned, or how multi-view handling works. While the appendix (stripped from this copy) may contain additional details, the main-paper description alone is insufficient for a baseline that the benchmark presents as a fixed reference point.
- **Table 5 lacks clarity on the map model used**: The element-type ablation reports "Performance of HiVT under Different Online Map Element Types" but does not clearly state which online mapping model generated the maps. This limits the generalizability of the finding and makes it unclear whether the ranking of element importance is model-specific.

### Trivial
- The comparison of training mAP (87.6) to validation mAP (50.3) in Fig. 3 illustrates the train-val gap directionally, but training-set mAP is not a realistic proxy for map quality during motion-model training — a held-out map accuracy comparison would be more rigorous. This does not undermine the core argument, which is validated by the downstream motion prediction results in Table 1.

## Nice-to-Haves
- Reporting separate ego metrics alongside the moving non-ego metrics (as the paper already does in Tables 6-7 with ego columns) with a brief discussion of why ego prediction may not always track improvements in non-ego prediction would add depth.
- Adding qualitative visualizations of image-feature attention for far agents to probe what information the boundary-free baseline actually provides.
- Adopting a reproducible algorithmic method for the spatial split (e.g., gridding the map and assigning logs by cell) rather than the current "manually checked" description.

## Removed Points
These points are flagged to be removed, treat them with caution.

- **"Ego vehicle removed entirely from primary evaluation" (Harsh Critic #4)**: REMOVED. The paper DOES report ego metrics in both Table 6 and Table 7. The harsh critic's claim is factually incorrect — the paper simply shifts primary focus to moving non-ego agents while still providing ego results.
- **"Novelty of each individual observation is low" (Harsh Critic, Introduction note)**: REMOVED as a standalone weakness. The paper explicitly positions itself as identifying and systematizing known practical challenges in a new protocol context, not as claiming novel discoveries. The contribution is the synthesis and benchmark, which is a legitimate scope for a benchmark paper.
- **Strength about "practical significance" (Strength Finder #3 under Supporting)**: REMOVED as too generic. While true, this is not a concrete strength — most papers claim practical significance.

## Novel Insights
The review process reveals an interesting tension: the paper's strongest evidence comes from Table 1's demonstration of the train-validation gap, but the spatial-overlap component of the split (the more labor-intensive part) has weaker justification. A random hold-out could address the train-val gap with less data loss, while spatial disjointness primarily benefits the evaluation of the mapping model's generalization, not the motion model's performance. The paper would be strengthened by disentangling these two motivations more explicitly.

## Suggestions
- **Add statistical reliability**: Report at minimum standard deviation across 3+ training seeds for the main results, or adopt cross-validation over the motion partition. This is the single most important improvement for the benchmark's credibility.
- **Include a direct comparison** between the spatial split and a same-sized random hold-out evaluated on the same motion validation set, to isolate (and justify) the contribution of spatial disjointness.
- **Specify the image-feature integration architecture** for both HiVT and DenseTNT in the main text, including feature injection point, training procedure (frozen vs. fine-tuned backbone), and multi-view fusion details.

## Score and Decision

**Calibration anchors referenced:**

| Paper | Avg Score | Round | Comparison |
|-------|-----------|-------|------------|
| Don't Reinvent the Steering Wheel (pzZjyYee6L) | 2.50 | 1 | Much weaker: limited novelty, bare-bones experiments, unclear baselines |
| MapDR (ZPCBcR7Drg) | 5.00 | 1 | Weaker: motivation less clear, diversity concerns, our experiments more comprehensive |
| ESDMotion (sEJYPiVEt4) | 5.25 | 2 | Weaker: more limited scope, older baselines, some misleading framing. Our paper has broader analysis |
| RedMotion (72MSbSZtHv) | 5.33 | 2 | Not directly comparable (method paper); our contribution is more clearly scoped |
| SmartPretrain (Bmzv2Gch9v) | 6.75 | 1 | Stronger: more polished execution, SOTA results, but our paper's protocol analysis is more novel |
| SEPT (efeBC1sQj9) | 7.00 | 2 | Stronger: SOTA leaderboard results, extensive ablations, cleaner methodology |

**Round 1 bracket**: Between ~5.0 and ~7.0.  
**Round 2 narrowing**: The paper is clearly stronger than ESDMotion (5.25) but not as well-executed as SEPT (7.0) or SmartPretrain (6.75). The core contribution (identifying protocol-level misconceptions) is valuable and well-motivated, but the benchmark execution lacks statistical rigor. This places the paper around 6.0.

The paper makes a genuine and useful contribution by systematically identifying and correcting protocol flaws in an emerging research area. The experiments are comprehensive in coverage (multiple model combinations) and the insights are actionable. However, the small validation set (86 scenes) with no variance reporting substantially weakens the benchmark's claim to serve as a "well-defined" replacement for existing protocols. The other weaknesses are addressable through revisions. On balance, this is a borderline accept that would benefit from strengthening the statistical foundation of its benchmark claims.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>