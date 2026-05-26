Now I have all the information I need. Let me construct the final review.

## Summary

The paper identifies three key misconceptions in the emerging online-map-based motion prediction protocol: (1) inappropriate data splits that create a train-validation gap in map accuracy, (2) misaligned perception ranges between mapping models (30×60m) and motion prediction needs (up to 100m), and (3) non-discriminative metrics that focus on the ego vehicle and static agents. The authors propose OMMP-Bench, featuring a spatially disjoint three-way split (map train / motion train / motion val) that eliminates the train-val gap, refined metrics that evaluate moving non-ego agents with separate close/far reporting, and a boundary-free baseline that uses deformable attention on raw image features to provide environmental context for out-of-range agents. The benchmark is validated across multiple mapping models (MapTR, MapTRv2-CL) and motion models (HiVT, DenseTNT), with additional analysis of how different map element types affect prediction quality.

## Strengths

1. **Clear identification and visualization of the train-val gap, with a principled solution.** The paper demonstrates (Figure 3) that under the default split, online map mAP drops from 87.6 (training scenes) to 50.3 (validation scenes), while the proposed split yields similar mAP (48.9 vs. 50.3). Table 1 shows that the proposed split (0.6308 minADE) outperforms the default split (0.6839 minADE), and the spatial overlap between train and validation scenes is reduced from 87% to 5% (Figure 4). This is a well-motivated, concrete fix to a real protocol flaw.

2. **Discovery of a fundamental perception range mismatch and a simple, effective baseline.** Tables 2 and 3 show that extending the online mapping range degrades map quality without improving motion prediction, while using image features via deformable attention (Eq. 1) improves performance, especially for far-away agents (12.7% minADE reduction on MapTRv2-CL+HiVT, Table 7). The insight that image features are naturally boundary-free whereas BEV features inherit the map model's range limitation is clearly articulated.

3. **Meaningful metric reformulation.** The paper demonstrates (Table 6) that static agents are trivially predictable (minADE 0.002 vs. 0.6307 for moving agents), justifying the exclusion of static agents and the separate reporting of close/far moving non-ego agents. This aligns the evaluation with motion prediction's actual purpose (collision avoidance with other agents) rather than just ego trajectory prediction.

4. **Systematic analysis of map element types.** Table 5 (modulo the labeling issue noted below) provides a useful comparison of how different map elements (dividers, boundaries, pedestrian crossings, centerlines) affect motion prediction quality, offering guidance for co-designing mapping and prediction models.

5. **Comprehensive benchmarking suite.** Table 7 provides results across 2 map models × 2 motion models × 4 methods (base, unc, bev, img), with separate columns for ego, close non-ego, and far non-ego agents. This enables direct comparison and yields actionable insights (e.g., stronger map models benefit downstream prediction; image features help far agents the most).

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Table 5 has a data integrity issue.** Rows 2 and 3 show the identical input pattern (only Boundary: ✗ ✓ ✗ ✗) but report different minADE values (0.6829 vs. 0.6558). Based on the paper's narrative ("centerlines are most helpful and centerlines only achieve the second best performance"), Row 3 was almost certainly intended to show a different configuration — most likely only Centerline (✗ ✗ ✗ ✓). This mislabeling undermines confidence in the specific numeric takeaways from the map-element analysis, though the paper's main conclusion (using all elements together is best) remains robust.

2. **The train-val gap evidence in Table 1 is confounded.** The comparison between Setting 1 (proposed split, 0.6308) and Setting 3 (default split, 0.6839) differs in multiple factors simultaneously: map model training set size (367 vs. 700+ scenes), scene composition, and spatial overlap. The improvement could partly stem from the cleaner spatial split rather than (or in addition to) gap elimination. Figure 3 directly verifies the mAP gap itself, so the core claim is not threatened, but a cleaner ablation (e.g., training the map model on a fixed set and varying only whether the motion model's training maps match the evaluation distribution) would strengthen the causal story.

3. **The image-feature baseline's improvement on close agents clouds the narrative.** In Table 7, the "img" baseline improves minADE even for in-range (close) agents versus the "bev" and "unc" baselines (e.g., 0.5275 vs. 0.5328 for MapTR+HiVT). This suggests the benefit is partly due to image features being a richer representation generally, not solely due to range extension. The paper frames the baseline as addressing the "out-of-map issue" (Section 3.3), but the in-range improvements indicate a broader advantage. An ablation that uses image features only for out-of-range agents would better isolate the range-extension effect.

4. **Several implementation details are underspecified.** The paper does not state whether the image backbone used for the "img" baseline is frozen or fine-tuned during motion model training, nor how agents that are not visible in any camera view are handled (the projection in Eq. 1 assumes visibility). These details are important for reproducibility, though the promised code release will partially address this.

5. **No discussion of limitations.** The benchmark is restricted to nuScenes (the only dataset with all required modalities), and the two-stage paradigm itself is a design choice that excludes end-to-end models. A brief limitations paragraph acknowledging these scope boundaries and discussing how findings might transfer to other sensor setups or geographic regions would strengthen the paper.

6. **Missing agent-distance distribution statistics.** The paper defines close/far categories based on the mapping perception range but does not report what fraction of moving non-ego agents fall into each group. This would help readers gauge the practical relevance of the range-mismatch issue.

### Trivial
None (minor presentation issues are addressed in Nice-to-Haves below).

## Nice-to-Haves

- Provide an ablation of the image baseline that uses image features only for out-of-range agents (and online map features for in-range agents), to disentangle the range-extension benefit from general feature-quality benefits.
- Include a controlled experiment for the train-val gap where the map model is trained on a fixed set and only the match/mismatch of motion-model training maps is varied.
- Report the proportion of moving non-ego agents in the close vs. far categories.
- The labels "bey" and "ing" in Table 4 appear to be abbreviated forms of "bev" and "img" — clarifying them would improve readability (these are likely parser artifacts).

## Removed Points

- **Criticism about the image backbone not specifying query/key/value dimensions for Eq. (1):** Removed as an unreasonably granular implementation detail for a benchmark paper.
- **Requests for confidence intervals / variance measures:** Removed as non-standard for single-run deterministic benchmarks in this subfield.
- **Criticism about missing quantification of spatial overlap's impact on motion prediction:** Removed as the paper already provides the overlap percentage (87% → 5%) and a new split; the requested additional experiment is beyond what a benchmark paper needs to establish.
- **Criticism that the train-val gap claim requires isolating the gap from all confounds:** Downgraded from the critic's framing to Minor (weakness #2 above), since Figure 3 provides direct, non-confounded evidence of the mAP gap itself.
- **Strength Finder's generic framing of the problem importance:** Removed strengths that merely state "the paper addresses an important problem" without concrete evidence. All retained strengths cite specific tables/figures.

## Novel Insights

The synthesis of the reviews surfaces one observation that goes slightly beyond what the paper states explicitly: the image-feature baseline's improvement on *in-range* agents suggests that the bottleneck in online-map-based motion prediction may not only be about map *absence* for far agents, but also about map *quality* (i.e., even in-range maps reconstructed by online mapping models are less informative than direct image features). This implies that jointly reasoning over image features and map elements — rather than treating the map as a complete bottleneck — could be a productive research direction irrespective of the range-mismatch problem. The paper's own framing focuses on range extension, but the data supports a broader interpretation.

## Suggestions

- **Fix Table 5.** Correct the checkmark pattern for Row 3 (almost certainly Centerline-only, ✗ ✗ ✗ ✓) and ensure all values are accurate. Consider adding a row showing only Centerline if it is missing.
- **Add a short limitations paragraph** discussing scope boundaries (nuScenes-only, two-stage paradigm) and possible transfer to other settings.
- **Specify in the text** whether the image backbone used by the "img" baseline is frozen or fine-tuned, and how invisible agents are handled.
- **Report close/far agent count statistics** to contextualize the practical severity of the range mismatch.

## Score and Decision

The paper makes a solid, well-motivated contribution to an emerging area. The identified misconceptions are real and clearly demonstrated. The proposed benchmark, split, and refined metrics are useful resources for the community. Weaknesses are limited to presentation issues (Table 5 labeling error) and the desire for slightly cleaner ablations, none of which threaten the core claims. The paper will improve the rigor of evaluation in online-map-based motion prediction.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>