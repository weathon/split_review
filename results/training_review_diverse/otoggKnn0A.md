Now I have all the evidence I need. Let me write the final consolidated review.

---

## Summary

FHA-Kitchens is a dataset for fine-grained hand action recognition in kitchen scenes, offering 2,377 video clips (30,047 frames) sourced from Kinetics 700_2020. Its core contribution is a rich 9-dimensional annotation scheme: each frame has bounding boxes for three sub-interaction regions (left-hand/object, right-hand/object, object-object), action triplets `<subject, verb, object>` with active-passive role assignment and contact areas, totaling 878 action triplets (131 verbs, 384 nouns). The paper benchmarks models across three tracks: detection (SL-D), action recognition (SL-AR), and domain generalization (DG), showing that even strong video models struggle on this fine-grained task.

## Strengths

- **High-dimensional action annotation with regional interaction detail.** The dataset annotates three sub-interaction regions (L-O, R-O, O-O) with bounding boxes, active-passive object relationships, and contact areas, yielding 9-dimensional action representations. This is evidenced by 198,839 bounding boxes across 9 annotation types and 878 action triplets (Section 3.2, Table 1). This goes well beyond existing datasets like EPIC-KITCHENS, which lack regional localization and relationship information.

- **Comprehensive benchmarking revealing genuine challenges.** The paper evaluates 8+ models across three tracks and shows that even large models (VideoMAE V2, Hiera) achieve substantially lower accuracy on FHA-Kitchens than on coarse-grained benchmarks like Kinetics 400. Detection models suffer a minimum 15 mAP drop on unseen sub-categories in the intra-class DG track (Section 4.4.1). These results empirically validate the difficulty of fine-grained hand action recognition and establish clear baselines.

- **Rigorous data cleaning process.** From an initial 113,436 frames, only 30,047 high-quality frames were retained based on occlusion, blur, subtitles, logos, and meaningful hand action criteria. Three rounds of cross-checking were conducted for annotations (Sections 3.1–3.2), supporting the claim of annotation quality.

## Weaknesses

### Fatal
None.

### Major

- **Ambiguous clip construction undermines the SL-AR (video action recognition) benchmark.** The paper states: "First, we split the collected video data into individual frames, as our annotated units are frames… Finally, we organized the video frames based on the action triplet classes, ultimately generating 2,377 clips that represent distinct hand action triplet classes" (Section 3.1). This phrasing is ambiguous: it could mean that clips are temporally contiguous segments from the original videos (each depicting one action), or that frames sharing the same action triplet were grouped regardless of temporal continuity, producing non-temporal collections. The SL-AR track evaluates video-level models (SlowFast, VideoSwin, VideoMAE V2, Hiera) that rely on temporal structure — 3D convolutions, spatio-temporal attention, and temporal aggregation. If clips are non-temporal, those results are not interpretable as action recognition. The paper must unambiguously state how clips were constructed, report average clip length, and confirm temporal continuity. This is the single most important issue to resolve. (Note: the tables referenced in Section 4.3 are present in the original submission as embedded images — the table contents are not missing despite parser artifacts.)

- **No inter-annotator agreement statistics.** The annotation scheme is complex (9 dimensions, three sub-regions, active-passive roles, contact areas) and the paper claims "high-quality annotations" with three rounds of cross-checking. However, no quantitative agreement metric (e.g., Krippendorff's alpha for triplets, IoU for bounding boxes) is reported. For a dataset paper with this annotation complexity, the absence of IAA metrics makes it difficult for readers to assess the reliability of the annotations. A small-scale IAA study on a random subset of 100–200 frames would substantially strengthen confidence.

### Minor

- **Dataset derived from only 30 source videos.** While the annotation granularity is a strength, the underlying source diversity is limited: 30 videos (84.22 min) from Kinetics 700_2020, covering 8 dish types. The paper partially acknowledges this in the Discussion ("Our dataset may be slightly smaller in terms of the number of videos") but still makes broad claims about diversity. Intra- and inter-class DG experiments are conducted entirely within this narrow scope, so their results may reflect dataset-specific idiosyncrasies. The paper should more transparently discuss how this limited source diversity affects generalization claims.

- **No analysis of discarded frames and potential bias.** 113,436 frames (~79% of the initial collection) were discarded due to occlusion, blur, "meaningless hand actions," etc. (Section 3.1). No analysis is provided of what types of frames were preferentially discarded or what biases this aggressive filtering might introduce (e.g., biasing toward simple, unoccluded actions). For a small dataset, this could skew the distribution significantly.

- **No dataset license or terms of use mentioned.** The paper says the dataset "will be released on the FHA-Kitchens project website" but does not specify a license. Since the data is derived from Kinetics 700_2020 (which has a non-commercial license), the paper should clarify whether annotations alone will be released, whether source video URLs/identifiers will be provided, and what usage restrictions apply.

- **No discussion of ethical considerations.** Kitchen scenes in Kinetics-derived videos may contain identifiable individuals, private spaces, or branded products. The paper does not address whether faces were blurred, whether personal information was handled, or consent considerations. This is increasingly expected for dataset papers.

### Trivial
None.

## Nice-to-Haves

- The paper provides SAM-generated object masks for all frames (Section 3.2) but does not use them in experiments or evaluate their quality. While this is an offered additional resource, a brief quality assessment (e.g., comparison to human annotations on a subset) would be helpful.
- Hyperparameter details are sparse ("recommended optimization strategy" without specific values). While standard for dataset papers benchmarking existing methods, including full training configurations in supplementary material would improve reproducibility.
- The triplet subject labeling (e.g., "hand_left" as subject in `<hand_left, hold-in, carrot>`) is a design choice for modeling the interaction region, but the paper could clarify that "subject" in L-O/R-O regions refers to the body part performing the action, whereas in O-O regions it refers to the active tool. This is a presentational clarification, not an error.

## Removed Points

The following points from the harsh review are removed because they either reflect parser artifacts or are factually incorrect when checked against the paper:

- *"The SL-AR track results table (Table 4) is missing from the text"* and *"The SL-D track results (Table 2) are also not visible"* — **Removed.** Both tables are present in the paper as embedded images (see `![](images/...)` markers at lines 126 and 141). The parser strips images but the original submission includes them.
- *"The paper should include complete training logs"* — **Removed** as an impractically large artifact.
- *Complaints about "1.1" and "1.2" references* — **Removed.** These are cross-references to an appendix/supplementary that was stripped by the parser, not missing content in the original submission.
- *Criticism that the dataset does not "correspond to currently available systems"* — **Removed** per hard rule: cited references are assumed real.

## Novel Insights

The most interesting observation from the reviews is that the paper's core value may be somewhat decoupled from the SL-AR track. The annotation scheme (9 dimensions, regional interactions, active-passive roles) and the detection/DG benchmarks could stand as a contribution even if the temporal structure of the clips needed redesign. This suggests the paper should consider reframing its emphasis: the truly novel contribution is the annotation granularity and the detection/domain generalization experiments, not the video-level action recognition benchmark per se (which faces standard dataset-scale limitations). The DG track's finding that models drop 15+ mAP on unseen sub-categories within the same parent action is a genuinely informative result that deserves more prominence.

## Suggestions

1. **Clarify clip construction unambiguously.** Provide an explicit example showing how a single source video is split into temporal clips at action boundaries. Report average clip length (in frames and seconds), and confirm that frames within each clip are temporally contiguous and properly ordered. If clips are non-temporal, redesign the SL-AR track.

2. **Add inter-annotator agreement statistics.** Even a small-scale study (100–200 frames with 2–3 annotators) using appropriate metrics (Krippendorff's alpha for categorical labels, IoU/F1 for bounding boxes) would greatly strengthen confidence in the annotation quality.

3. **Discuss dataset limitations more transparently.** Acknowledge the limited number of source videos (30), the aggressive filtering (79% discarded), and what biases these may introduce. This is already partially done in the Discussion but could be more explicit.

4. **Specify the dataset license and address basic ethical considerations.** Clarify what will be released (annotations only? video IDs? frame images?) and under what terms. Briefly note whether identifiable information (faces, brands) was handled.

## Score and Decision

**Originality:** The annotation scheme (9 dimensions, three sub-interaction regions, active-passive roles) is novel and more detailed than existing kitchen hand-action datasets.  
**Importance:** Fine-grained hand action recognition is an under-addressed problem with practical relevance. The dataset fills a genuine gap.  
**Claims support:** The core claims about annotation richness and benchmark challenge are supported. However, the SL-AR track's validity depends on resolving the clip construction ambiguity.  
**Soundness:** The detection and DG experiments are sound. The SL-AR experiments may need to be re-evaluated after clarification.  
**Clarity:** Generally clear, except for the critical ambiguity in clip construction.  
**Value to community:** Positive, assuming the temporal ambiguity is resolved and IAA metrics are provided.

The paper's core contributions (annotation scheme + detection/DG benchmarks) are real, but the critical temporal ambiguity and missing IAA metrics prevent full assessment. A revision that clarifies the clip structure and adds basic quality metrics would significantly strengthen the paper.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>