Now I have enough calibration data. Let me produce the final review.

## Summary

This paper identifies and systematically addresses three misconceptions in the emerging protocol of online map-based motion prediction: (1) inappropriate dataset splits causing a train-val gap, (2) misaligned perception ranges between mapping and motion prediction models, and (3) non-discriminative metrics that evaluate only the ego vehicle. The authors propose OMMP-Bench with a geographically disjoint split (map train / motion train / motion val), refined metrics that evaluate all moving non-ego agents separately for close and far ranges, and a boundary-free baseline leveraging raw image features to compensate for missing map context for distant agents. Experiments across two mapping models (MapTR, MapTRv2-CL) and two motion predictors (HiVT, DenseTNT) consistently support the analysis.

## Strengths

- **Identifies and resolves a genuine train-val gap in the two-stage training protocol.** The paper demonstrates that the default split creates a 37% mAP drop for the map model between training (87.6) and evaluation (50.3), and that the proposed spatially disjoint split reduces spatial overlap from 87% to 5%, producing a measurable minADE improvement (0.6308 vs 0.6839, Table 1). This directly validates the new protocol's effectiveness.

- **Systematically reveals and quantifies the range misalignment problem.** The paper shows that simply extending the online mapping range degrades map quality (mAP 0.124→0.014 for MapTR, Table 2) while using a wider GT map barely improves close-agent prediction (minADE 0.6154→0.6003, Table 3). The proposed close/far metrics make this degradation visible — far agents show ~11–26% worse minADE than close agents (Table 6), a problem the old ego-only metrics completely mask.

- **The boundary-free baseline convincingly demonstrates a practical solution.** Using deformable attention on raw image features (which have no perception-range limitations) produces substantial gains for far-agent prediction (e.g., 12.7% minADE reduction for MapTRv2-CL+HiVT, Table 7), concretely showing that the range misalignment is a real bottleneck.

- **Thorough and consistent experiments across multiple model combinations.** Table 7 reports results for 16 method configurations (2 map models × 2 motion models × 4 methods), and the observed trends are consistent throughout: the image baseline helps far agents most, stronger mapping models help motion prediction, and distant agents are systematically harder.

- **Useful analysis of map element types.** Table 5 provides concrete guidance to the community — centerlines are the most valuable single element type, and feeding all elements yields the best performance (minADE 0.6308 vs 0.8770 with dividers only).

## Weaknesses

### Major

- **The motion validation set (86 scenes) is notably smaller than the standard nuScenes validation set (150 scenes), yet the paper reports no variance estimates or confidence intervals.** While the consistent trends across multiple method combinations mitigate the concern somewhat, the lack of any statistical reliability analysis is a methodological gap for a benchmark paper whose primary contribution is an evaluation protocol. Bootstrap confidence intervals or standard deviations across multiple runs would substantially strengthen the benchmark's credibility. This does not invalidate the paper's qualitative conclusions but limits confidence in the precise numerical rankings.

### Minor

- **The boundary-free baseline is presented as achieving "SOTA performance" (Section 3.3) without an explicit qualification that it uses an additional input modality (raw image features) not available to the compared methods (base, unc, bev).** The baseline correctly illustrates how external information can compensate for missing map context, which is the paper's intended use. However, the unqualified "SOTA" framing could mislead a reader into interpreting this as a direct method comparison. The authors should qualify the claim explicitly.

- **Setting 4 in Table 1 (subsampling the training set 50/50 for map and motion models on the overlapping split) also improves over the default split (0.6373 vs 0.6839 minADE), which suggests that part of the gain comes from eliminating the train-val gap through separate data for map and motion training, not just from spatial overlap removal.** The paper does not discuss this nuance. Clarifying the contribution of each factor (spatial disjointness vs. separate-map-data) would strengthen the analysis.

- **No discussion of when or why the image-feature approach might fail.** Cases such as occluded far agents, poor lighting, or agents not visible in any camera view are not addressed, even as qualitative discussion.

### Trivial

- **Table 5 has a formatting issue where rows 2 and 3 appear with identical checkmark patterns (✗, ✓, ✗, ✗) but different scores (0.6829, 0.6558).** This is almost certainly a PDF parser artifact from the table rendering — the original submission likely has the correct alignment. The text confirms that centerlines are the second-best element type.

## Nice-to-Haves

- Report inference time or FLOPs for the image feature module to help practitioners understand its practical cost.
- Aggregate results over multiple geographic folds of the data split, or provide bootstrap confidence intervals for the main metrics.
- Analyze the distribution of agent distances in the motion train/val sets to demonstrate balance across splits.

## Removed Points

- *"The new split could have temporal correlation issues"* — The paper states scenes were manually checked for spatial overlap. Whether temporal correlation exists cannot be evaluated from the paper alone, and the claim is speculative without evidence.
- *"The paper does not use the original nuScenes test set with hidden labels"* — This is scope creep; the paper explicitly defines a new validation benchmark and states its purpose.
- *"Reproducibility concern about code release"* — The paper states code will be open-sourced. Following the hard rules, this cannot be a weakness.
- *Strengths from Strength Finder such as "paper addressed an important problem" or "well-motivated"* — These are generic and not concrete evidence-backed claims.

## Novel Insights

None beyond the paper's own contributions. The key findings — that the existing protocol conflates spatial overlap with generalization, that range misalignment is a real bottleneck masked by ego-only metrics, and that image features can compensate — are all clearly stated by the authors.

## Suggestions

1. Add variance information (e.g., standard deviations over 3 seeds or bootstrap CIs) for the main metrics in Table 7, particularly since the validation set is small.
2. Remove or qualify the unqualified "SOTA" claim for the image baseline (Section 3.3), e.g., "achieves the best performance among the evaluated methods" and note the additional input modality.
3. Discuss the contribution of separate-map-data vs. spatial disjointness by comparing Settings 1 and 4 in Table 1 more explicitly.
4. Add a brief failure analysis of the image-feature baseline: when might agents be unobservable in camera views?

## Score and Decision

### Calibration Report

**Round 1 (bracketing):** Three queries returned anchors across score bands.
- Weak band (scores < 3.5): avg 2.5–3.33 — papers with fundamental flaws; our paper is clearly stronger.
- Middle band (3.5–7.5): ESDMotion (5.25, Reject), RedMotion (5.33, mixed), Large Trajectory Models (5.00, Reject). Our paper is cleaner than ESDMotion and has clearer contributions than these.
- Strong band (> 7.5): avg 8.0 — not directly comparable to this paper's genre.

**Bracket:** 4.5–6.5.

**Round 2 (narrowing):** Queries within (4.5, 6.0) and (6.0, 7.5).
- MapDR (5.00, Reject): Benchmark paper with unclear motivation; our paper is better motivated.
- BEV Uncertainty Benchmark (5.40, Accept): Similar genre (benchmark/analysis); our paper has comparably clear analysis.
- ITPNet (6.75, Reject): Method paper with mixed reviews; not directly comparable genre.
- Round 3 confirms with IntersectionZoo (6.00, Accept), AdaWM (5.75, Accept), DiLu (6.25, Accept) — our paper is comparable in quality to accepted benchmark/analysis papers.

**Final score:** 6.0. The paper is a well-executed benchmark/analysis paper that identifies real problems in an emerging field and proposes well-motivated fixes with consistent experimental support. The weaknesses (small validation set without variance, SOTA framing) are real but do not undermine the core contributions.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>