Now I have enough information. Let me write the consolidated final review.

## Summary
This paper identifies three structural misconceptions in the emerging online map-based motion prediction protocol: (1) inappropriate train-val data splits that create a distribution shift in map quality between motion model training and evaluation, (2) misaligned perception ranges between online mapping models and motion prediction needs, and (3) non-discriminative metrics that evaluate only the ego vehicle. The authors propose OMMP-Bench with a spatially disjoint three-way split, refined evaluation metrics (moving non-ego agents stratified by distance), and a simple image-feature baseline to address the range mismatch. Comprehensive experiments on nuScenes with two map models and two motion models validate the proposed fixes.

## Strengths
- **Systematic identification of genuine protocol flaws.** The paper demonstrates convincingly (Table 2, Table 3, Figure 6) that existing online mapping models operate at 30×60m while motion prediction needs information for agents >100m away, and that simply expanding the map range collapses map accuracy (mAP drops from 0.124 to 0.014 for MapTR). This is a concrete, actionable finding.
- **Quantified demonstration of the train-val gap.** Figure 3 shows map mAP of 87.6 on motion training data vs 50.3 on motion validation under the default protocol, while the proposed split yields near-identical accuracy (48.9 vs 50.3). Table 1 confirms motion prediction minADE improves from 0.6839 (default) to 0.6308 (proposed), with the evidence supporting that the train-val gap is the dominant factor (~88% of total improvement, with spatial overlap accounting for ~12%).
- **Meaningful metric refinement.** Table 6 shows that static-agent minADE is near zero (0.002) for both methods, rendering current ego-only metrics uninformative. The proposed moving/non-ego/close/far stratification reveals genuine performance differences (e.g., minADE 0.5585 close vs 0.6997 far for HiVT+MapTR) that existing protocols obscure.
- **Comprehensive benchmark results.** Table 7 reports 32 configurations across two map models, two motion models, and four methods, consistently supporting the paper's conclusions (e.g., stronger map models help, the image baseline improves far-agent prediction by 12.7%).

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
- **The boundary-free baseline is under-analyzed for its billing as a contribution.** The image-feature baseline (Eq. 1, Deformable Attention over projected agent positions) is described in roughly one paragraph with one equation. While it is positioned as a "simple yet effective baseline" and achieves useful results (12.7% minADE improvement for far agents), the paper provides no ablations of design choices — no comparison of different attention mechanisms, no analysis of whether all six cameras are needed, no study of how feature dimension or projection method affects results, and no discussion of failure cases (e.g., agents outside all camera frustums). This is reasonable for a demonstration baseline within a benchmark paper, but the contribution list gives it co-equal billing with the data split and metrics contributions, which are more fully developed.

- **The map element type analysis (Table 5) is thin.** It uses only one motion model (HiVT) and explores element types additively without testing interaction effects (e.g., whether pedestrian crossings help when centerlines are already present, or whether dividers and boundaries are redundant). The conclusion "feed all possible map elements" is unsurprising, and the claim to provide "insights for new designs in the online mapping community" overstates what a single-model additive ablation can support.

- **No uncertainty quantification on metrics.** With only 86 validation scenes, the reported metric differences (especially borderline ones like Setting 1 vs 4 in Table 1: 0.6308 vs 0.6373) would benefit from confidence intervals or variance estimates. This is standard practice for benchmark papers.

### Trivial
None.

## Nice-to-Haves
- An additional experiment that trains the map model on the full nuScenes training set but holds out a random subset for motion model training (maps generated on this held-out subset) would cleanly isolate the train-val gap from spatial overlap effects. The existing data already strongly supports the paper's position, but this would further sharpen the causal story.
- The image baseline could be strengthened by a simple comparison to providing a constant "no map" embedding for out-of-range agents, to quantify how much of the gain comes from image features specifically versus simply not having missing inputs.

## Removed Points
- **Criticism about train-val gap evidence contradicting the narrative (from Harsh Critic).** REMOVED as factually wrong. The critic claimed Setting 4 (0.6373) shows spatial overlap is dominant, but Setting 4 eliminates the train-val gap (map model trained on a different half of the data from the motion model) and retains spatial overlap. The improvement from Setting 3→4 (0.6839→0.6373, gap of 0.0466) measures the train-val gap effect, and the improvement from Setting 4→1 (0.6373→0.6308, gap of 0.0065) measures the additional spatial overlap effect. The train-val gap accounts for ~88% of the total improvement. The evidence supports the paper's narrative, not the critic's.
- **Criticism about duplicate rows in Table 5.** REMOVED as a parser artifact. The PDF extraction garbled the text, producing two rows with identical checkmark patterns but different numerical values. The original paper does not have this issue.
- **Criticism about non-ego evaluation being claimed as novel.** REMOVED as factually wrong. The paper explicitly states "we focused our evaluation on moving vehicles, similar to popular motion prediction benchmarks like Argoverse... and Waymo" (Section 3.4).
- **Criticism that spatial overlap is presented as the paper's own discovery.** WEAKENED and moved here. The paper properly attributes the spatial overlap issue to Yuan et al. (2024) in Section 3.2 ("pointed out in recent online mapping work Yuan et al. (2024)"). The Introduction's phrasing "we identify that the current dataset splits are unsuitable" refers to the combined problem (train-val gap + spatial overlap), which is accurate.
- **Strength Finder strengths about the problem being important.** REMOVED as generic. Kept only concrete, evidence-grounded strengths.

## Novel Insights
The harsh critic's attempted refutation of the train-val gap evidence inadvertently reveals something subtle: the paper could strengthen its causal narrative by explicitly walking through the arithmetic of Table 1 (Setting 3→4 vs Setting 4→1) to attribute the improvement to the two mechanisms. The merged review identifies that, but the paper itself already contains the data needed — it just doesn't do the explicit decomposition. This is a presentation gap, not an evidence gap.

## Suggestions
1. Reframe the contribution list to reflect that the baseline is a demonstration/downstream contribution rather than co-equal with the data split and metrics contributions, which are the paper's primary analytical contributions.
2. Add a brief explicit decomposition in Section 3.2 showing that the train-val gap accounts for ~88% of the minADE improvement and spatial overlap for ~12% (using the Table 1 data).
3. Expand the map element analysis (Table 5) to at minimum acknowledge the single-model limitation, and ideally test at least one interaction (e.g., does centerline + boundary differ from centerline alone?).
4. Add confidence intervals or standard deviations for key comparisons where statistical significance matters.

## Score and Decision

Let me calibrate:

**Round 1 anchoring** (bracketing):
- Weak band (<3.5): Limited relevance  
- Middle band (3.5–7.5): ESDMotion (5.25), P-MapNet (5.00), RedMotion (5.33) — all topically similar AD papers
- Strong band (>7.5): Less relevant (different subfields)  

**Round 1 bracket: 3.5–7.5**  

**Round 2 anchoring** (narrowing):
- BEV Uncertainty Benchmark (5.40, accepted) — similar benchmark paper in AD domain. The paper under review has stronger diagnostic contributions (identifying structural protocol flaws vs evaluating existing methods). Paper is somewhat stronger.
- MapDR (5.00, rejected) — AD benchmark/dataset paper with clarity and motivation concerns. Paper under review is clearly stronger.
- MJ-Bench (6.00, rejected) — comprehensive benchmark in different domain; solid but had completeness concerns. Comparable in quality.
- MONICA (5.75, rejected) — medical benchmark. Paper under review is somewhat stronger.

**Final score: 6.0** — The paper makes a genuinely useful contribution by identifying and fixing real misconceptions in an active research area. The core claims are well-supported by evidence (train-val gap analysis, range mismatch evidence, metric analysis). The weaknesses are minor (under-analyzed baseline, thin element ablation) and do not undermine the main contributions. The paper is meaningfully stronger than the typical 5.0-level benchmark papers in the AD space.

**Decision**: Accept

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>