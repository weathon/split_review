Now I have all the information I need. Let me synthesize the final review.

**Round 1 bracket:** The paper is clearly stronger than the weak anchors (<3.5, which are about different topics entirely). Among middle anchors (3.5–7.5), the most comparable are ESDMotion (5.25, reject), Leveraging Semantic Uncertainty (5.0, reject), P-MapNet (5.0, reject), Predictive Uncertainty for BEV (5.4, accept poster), and SEPT (7.0, accept poster). Strong anchors (>7.5) are from different domains. **Initial bracket: 5.0–7.0.**

**Round 2 narrowing:** Reading the full reviews confirms the paper is clearly stronger than ESDMotion, P-MapNet, and Leveraging Uncertainty (all rejected with substantive flaws). It is comparable to the BEV UQ Benchmark (5.4, accepted poster). It is weaker than SEPT (7.0, accepted poster), which achieved SOTA on two major benchmarks. **Finalized score: 6.0.**

Now the full review:

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses

### Fatal

### Major

### Minor

### Trivial

## Nice-to-Haves

## Removed Points

## Novel Insights

## Suggestions

## Score and Decision

Let me write it all out.

Actually, I need to think about what the "Removed Points" section should contain. Let me review the rules:

From the filtering rules:
- REMOVE criticisms about missing appendix, missing proofs in appendix — the parser strips those. But the harsh critic doesn't mention missing appendix specifically.
- REMOVE pure formatting/style nitpicks — no typos mentioned.
- REMOVE nitpicks about reproducibility such as undisclosed hyperparameters — the harsh critic mentions the baseline is under-specified (backbone, projection). The backbone criticism is somewhat valid but the projection criticism is about standard practice.
- REMOVE any criticism about typos, spelling, grammar — none mentioned.
- REMOVE strawman weaknesses — none obvious.

Actually, let me look at each of the harsh critic's weaknesses more carefully:

1. "Evidence for the train-val gap is insufficiently rigorous." — This is a real, substantive criticism. The comparison in Table 1 has confounds. KEEP as Major.

2. "The baseline using image features is under-specified" — 
   a. "Which backbone produces the image features?" — The paper says "image features extracted from a backbone" and Figure 7 shows the map estimation model architecture with CNN → Image Feature. This is clear enough in context — it's the image backbone of the map model. REMOVE — this is nitpicking when the Figure 7 diagram makes it clear.
   
   Actually, let me re-check. The paper says: "We denote the image features extracted from a backbone {I_1, I_2, ..., I_{N_c}}". The paper doesn't explicitly say "this is the CNN backbone of the online mapping model" but Figure 7 shows the architecture and it's clear from the context that these are the intermediate features from the map model's image encoder. Still, it would be better to be explicit. I'll KEEP this as a minor point.

   b. "How are agent coordinates projected onto image features?" — "Using the intrinsic and extrinsic parameters and agent positions, we project each agent onto an image feature." This is standard multi-view geometry. REMOVE — standard practice.

   c. "No comparison to simple alternatives" — The paper compares to "unc" and "bev" which are the SOTA baselines. The critic's suggestion of BEV features from expanded range or dummy token are alternatives but not standard baselines. However, such an ablation would be informative. WEAKEN to minor/nice-to-have.

3. "No error bars or significance tests" — Valid concern but standard practice in this subfield. WEAKEN to minor.

4. "Conclusion is too brief, lacks limitations" — Valid. KEEP as minor.

5. "Setting 2 is not explained in the text" — Actually, looking at Table 1, Setting 2 trains map model on Map Train + Motion Train and motion model on Map Train + Motion Train. The text doesn't explicitly explain Setting 2. This is a minor presentation issue. KEEP as trivial.

Wait, looking more carefully at Setting 2: The table shows "Map Train + Motion Train" for both map and motion model training. This seems to be a control where the map model has seen all the data used for motion model training — so the train-val gap is eliminated at the cost of the map model having seen the evaluation distribution? No, evaluation is still Motion Val which is disjoint. So Setting 2 means the map model was trained on both Map Train and Motion Train — so when it generates maps for motion model training, those maps are on its training set and thus very accurate. But at evaluation (Motion Val), the map model has never seen this set, so there's a similar gap as in default. Actually wait, the rows show:

Setting 2: Train Map Model: Map Train + Motion Train, Train Motion Model: Map Train + Motion Train, Eval: Motion Val → 0.7006

This is confusing. If Map Model is trained on Map Train + Motion Train, and Motion Model is trained on Map Train + Motion Train... but Map Train and Motion Train are different scenes. So the map model is trained on all available training data (Map Train + Motion Train), and when generating maps for motion model training, it generates on Map Train + Motion Train (which includes its own training set). For motion model evaluation, the map model generates maps on Motion Val (unseen). So the train-val gap is reintroduced because the map model performs well on its training distribution (which includes the Motion Train set) but poorly on Motion Val. That actually makes sense as a comparison.

But the harsh critic says "Setting 2 is not explained in the text" — this is correct, the text doesn't explain Setting 2. This is a minor clarity issue.

OK let me finalize.

One more thing — I need to consider whether any of the claimed strengths from the Strength Finder should be filtered out. Let me check:

Strength 1: "Identifies and fixes the train-val gap from two-stage training" — Supported by Figure 3 (maps mAP discrepancy) and Table 1. The claim is somewhat moderated by the confound issue, but the evidence is still there. KEEP but note the caveat.

Strength 2: "Introduces evaluation on moving non-ego agents with close/far stratification" — Clearly supported by Section 3.4 and Table 6. KEEP.

Strength 3: "Proposes a boundary-free baseline using raw image features" — Supported by Section 3.3, Eq 1, Table 4. KEEP.

Supporting Strength 1: "Empirically demonstrates that adding all map element types benefits motion prediction" — Table 5. KEEP.

Supporting Strength 2: "Provides a clean, spatially disjoint dataset split" — Figure 4 shows reduced overlap from 87% to 5%. KEEP.

Supporting Strength 3: "Comprehensive benchmark results across multiple model combinations" — Table 7. KEEP.

All strengths are concrete and specific. None should be dropped.

Now let me write the full review.Now I have everything I need. Let me produce the final consolidated review.

## Summary

This paper systematically identifies three misconceptions in the emerging online map based motion prediction protocol: (1) the default data split creates a train-val gap because the map model sees the same scenes during motion model training but unfamiliar scenes during evaluation, (2) the perception range of online mapping models (e.g., 30×60m) is too small to provide map context for distant agents, and (3) reporting only ego-vehicle metrics masks these issues. The authors propose **OMMP-Bench** with a spatially disjoint three-way data split, refined metrics (moving non-ego agents stratified by close/far), and a boundary-free baseline using Deformable Attention over raw image features. Experiments across two map models and two motion prediction models validate the proposed corrections.

## Strengths

1. **Identifies and demonstrates a real train-val gap in two-stage training.** Figure 3 shows concretely that the default protocol gives the motion model maps at 87.6 mAP during training but only 50.3 mAP during evaluation, while the proposed spatially disjoint split yields similar map accuracy (48.9 vs. 50.3 mAP). Table 1 shows that the proposed split improves minADE over the default split (0.6308 vs. 0.6839).

2. **Introduces evaluation on moving non-ego agents with close/far stratification, fixing a blind spot in prior work.** Section 3.4 and Table 6 show that static agents yield near-zero error (minADE 0.002), confirming they inflate metrics. Stratifying by distance reveals that far agents are substantially harder (minADE 0.6997 vs. 0.5585 for HiVT+MapTR), providing a genuinely discriminative evaluation that prior ego-only protocols could not capture.

3. **Proposes a boundary-free baseline that directly uses image features to mitigate missing map context for distant agents.** Equation 1 and Figure 7 describe Deformable Attention over multi-view image features. Table 4 shows this "img" baseline achieves minADE 0.6163 compared to 0.6272 (unc) and 0.6287 (bev). Table 7 further shows it cuts minADE for far agents by 12.7% (0.6999 → 0.6274 with MapTRv2-CL+HiVT).

4. **Empirically demonstrates that using all map element types benefits motion prediction.** Table 5 shows that combining divider, boundary, pedestrian crossing, and centerline gives the best minADE (0.6308), while centerline alone is second-best (0.6631). This is a concrete insight for online mapping model design.

5. **Provides a clean, spatially disjoint dataset split.** Figure 4 shows the original nuScenes split has 87% spatial overlap between training and validation, while the proposed split reduces overlap to only 5% between map train and motion train sets, enabling fairer evaluation of online mapping generalization.

6. **Comprehensive benchmark results across multiple model combinations.** Table 7 reports nine metrics for two map models (MapTR, MapTRv2-CL) × two motion predictors (HiVT, DenseTNT) × four method variants, enabling systematic comparison.

## Weaknesses

### Fatal
None.

### Major

1. **The train-val gap diagnosis does not perfectly isolate the claimed mechanism.** The comparison in Table 1 between Setting 1 (proposed) and Setting 3 (default) differs along multiple dimensions simultaneously: training set composition, training set size (397 vs. 700 scenes), evaluation split, and map accuracy mismatch. The performance difference (0.6308 vs. 0.6839) could be partially driven by these confounds rather than solely by the train-val gap. The paper would benefit from a controlled experiment that holds the motion model and evaluation set fixed while varying only whether the map model's inference distribution matches evaluation (as Figure 3's mAP values already suggest, but without linking directly to motion prediction). That said, Setting 4 (50/50 split of nuScenes train) partially addresses this concern by also reducing the gap, achieving 0.6373 — close to the proposed 0.6308 — which strengthens the overall case even if the isolation is imperfect.

2. **The boundary-free baseline's mechanism is not analyzed.** The paper shows that the "img" baseline improves performance, but offers no analysis of *why*: is the improvement from raw RGB information, from features from a backbone with a different training objective, or simply from adding any additional signal? An ablation comparing learned image features against a constant learned embedding for out-of-map agents would clarify the source of the 12.7% improvement. Additionally, the paper does not specify which backbone produces the image features (it is implicitly the map model's CNN encoder from Figure 7, but this should be stated explicitly).

### Minor

1. **Results are reported without variance or significance tests.** Table 7 reports single-run point estimates across all model combinations. With only 86 motion validation scenes, variance could be non-negligible. Whether a 0.01 minADE difference is meaningful is unclear without uncertainty quantification.

2. **Conclusion section is too brief and lacks a discussion of limitations.** The paper does not acknowledge that the benchmark is limited to nuScenes, to two motion prediction architectures (HiVT, DenseTNT), and to two mapping models (MapTR, MapTRv2-CL). The new split, while carefully designed, may introduce its own biases. A benchmark paper should explicitly state its scope and limitations.

3. **Setting 2 in Table 1 is not explained in the text.** The table includes four settings but only Settings 1 and 3 are discussed; the reader must infer the intent of Settings 2 and 4 from the table alone.

4. **The baseline description lacks some architectural details.** The paper does not state the number of Deformable Attention points, the dimension D of agent features, or how the projected image feature is resolved when an agent projects onto regions of the image with irrelevant content (e.g., sky). These do not invalidate the results but would help reproducibility without relying on the code release.

### Trivial

- "bey" in Table 4 (line 337) appears to be a typo for "bev".

## Nice-to-Haves

- A cleaner ablation holding the motion model and evaluation set fixed, comparing motion training with maps from the map model's training set vs. maps from a held-out set matched to evaluation quality.
- Oracle baseline using ground-truth maps for all agents, broken down by close/far, to set an upper bound.
- Additional analysis of the image feature baseline: replacing learned image features with a learned constant embedding for out-of-map agents to isolate the source of improvement.

## Removed Points

The following points raised by the reviewers were considered but removed or demoted:

- **"The baseline's agent-to-image projection is not specified"** — The paper states: "Using the intrinsic and extrinsic parameters and agent positions, we project each agent onto an image feature." This is standard multi-view geometry in autonomous driving and requires no further elaboration. **Removed.**
- **"No comparison to BEV features from an expanded range or dummy unknown token"** — The paper compares against "unc" (SOTA uncertainty-based) and "bev" (SOTA BEV feature attention) baselines, which are the relevant published methods on this task. Suggesting additional ad-hoc baselines is scope creep. **Demoted to Nice-to-Have.**
- **"Missing comparison to a simple alternative for image features"** — As above, the paper's empirical contribution is the identification of misconceptions and a benchmark, not a SOTA method. The baseline serves as proof-of-concept. **Demoted to Nice-to-Have.**
- **"Table 1 Setting 2 is not explained"** — This is a valid clarity issue. Kept as Minor, not removed.
- **"The paper only uses nuScenes"** — The paper explicitly explains (Section 3.1) that nuScenes is the only dataset providing raw camera data, HD maps, and agent trajectories in the same scenario; Waymo and Argoverse don't. This is a scoping justification, not an oversight. **Removed.**

## Novel Insights

The most interesting finding that emerges from the reviews is the contrast between the paper's two well-supported claims (range misalignment and non-discriminative metrics) and its weaker claim (train-val gap). The range and metrics claims are convincingly supported with clean experiments (Tables 2, 3, 6), while the train-val gap claim — though plausible and supported by Figure 3's mAP comparison — lacks a perfectly controlled experiment. This unevenness suggests that the paper's most immediately actionable contributions may be the refined metrics and the boundary-free baseline rather than the specific data split, but all three are useful for practitioners.

## Suggestions

1. Add a controlled ablation for the train-val gap: hold the motion model and evaluation set fixed; compare (a) motion training with maps from the map model's training set vs. (b) motion training with maps from a held-out set that matches evaluation quality. This would cleanly attribute the motion prediction improvement to gap elimination rather than to training set size or composition changes.

2. Add a brief limitations paragraph to the conclusion explicitly stating the scope (nuScenes only, two mapping and two motion models) and potential biases in the split.

3. Report at least one measure of variance (e.g., across random seeds or bootstrap resamples) for the main benchmark results in Table 7.

4. Include a simple ablation of the "img" baseline that replaces learned image features with a learned constant embedding for out-of-map agents, to clarify whether the improvement comes from the image features themselves or simply from the additional information dimension.

5. Explicitly state which backbone produces the image features in Section 3.3 (the CNN image encoder of the online mapping model, as shown in Figure 7).

## Score and Decision

**Calibration anchors:**

| Paper | Avg Score | Round | Comparison |
|-------|-----------|-------|------------|
| ESDMotion (reject) | 5.25 | 1, 2 | **Weaker** — had fairness concerns with baselines and unclear novelty. Current paper's contributions (identifying protocol flaws, new split) are more clearly defined. |
| Leveraging Semantic/Positional Uncertainty (reject) | 5.00 | 1, 2 | **Weaker** — simple uncertainty modeling; only one dataset. Current paper makes more substantive protocol-level contributions. |
| P-MapNet (reject) | 5.00 | 2 | **Weaker** — missed recent baselines, lower inference speeds, HDMap prior paradox. Current paper's claims are better supported. |
| Predictive UQ for BEV (accept poster) | 5.40 | 2 | **Comparable** — both are benchmark/analysis papers with methodological contributions. BEV UQ had 3 datasets; current paper has more nuanced protocol analysis. |
| SEPT (accept poster) | 7.00 | 1, 2 | **Stronger** — achieved SOTA on two major benchmarks (Argoverse 1 & 2). Current paper is a benchmark/analysis paper, not a SOTA method paper. |
| MapDR (withdrawn) | 5.00 | 2 | **Comparable genre but weaker** — motivation concerns, limited to Chinese cities. Current paper's claims are more broadly applicable. |

**Round 1 bracket:** 5.0–7.0. The paper is clearly stronger than rejected anchors in the 5.0–5.25 range and clearly weaker than SEPT (7.0).

**Round 2 narrowing:** The paper sits above 5.0–5.4 rejected anchors (which had substantive methodological flaws) and below 7.0 (which had SOTA results on two leaderboards). The most comparable accepted paper is the BEV UQ benchmark at 5.4.

**Final score: 6.0** — The paper makes a solid contribution to an emerging field by identifying genuine protocol misconceptions and providing practical corrections (new split, refined metrics, useful baseline). The main weakness (imperfectly isolated train-val gap evidence) is addressable and does not undermine the paper's core value. The benchmark, with its careful analysis and practical fixes, is likely to be adopted by the community, aligning with the standards of an accept-level benchmark paper.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>