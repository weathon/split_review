Now let me calibrate the score.Based on my review of the paper and calibration anchors, I have enough information to write the final review.

## Summary
The paper identifies methodological problems in the recently-introduced online-map-based motion prediction protocol (Gu et al. 2024a;b) and proposes OMMP-Bench as a corrected protocol on nuScenes: a new spatially-disjoint three-way split (map train / motion train / motion val), refined metrics that separate moving non-ego agents into close/far groups, an analysis of which map element types help, and a simple "boundary-free" baseline that injects raw image features via deformable attention to help agents outside the online-mapping range.

## Strengths
- **Concrete evidence for a real train–val gap**: Figure 3 and Table 1 demonstrate that under the default Gu et al. (2024a) protocol the map model's mAP drops from 87.6 (train) to 50.3 (val), and that the proposed spatially-disjoint split yields similar map accuracy (48.9 vs 50.3) across train and val. This is a substantive, well-documented protocol observation.
- **Discriminative grouped metrics**: Table 6 shows that ego-only evaluation hides the hard cases — static agents have minADE ≈ 0.002 while moving non-ego far agents reach 0.6997 for HiVT+MapTR. The close/far split is a genuinely useful refinement aligned with how Argoverse/Waymo handle stationary filtering.
- **Empirically supported baseline**: Table 4 and Table 7 show the image-feature baseline consistently improves over `base`, `unc`, and `bev` variants — e.g., MapTRv2-CL+HiVT minADE on Moving Non-Ego Far drops from 0.7242 (bev) to 0.6274 (img), a 12.7% reduction — providing real evidence that out-of-BEV-range agents benefit from raw image features.
- **Reveals trade-offs hidden by ego-only metrics**: Table 7 shows that `unc` and `bev` improve ego prediction but can degrade moving non-ego prediction (e.g., MapTRv2-CL+HiVT `bev`: 0.6738 → 0.7242 on far minADE going from MapTR to MapTRv2-CL), demonstrating the diagnostic value of the proposed evaluation.

## Weaknesses

### Fatal
None. The central observations are sound and the evidence, while limited, supports the core protocol-level claims.

### Major
- **Table 1 partially undercuts the headline split argument.** Setting 4 (random 50/50 split of the official nuScenes train, no spatial disjointness) yields minADE 0.6373 / minFDE 1.2261 / MR 0.1580 — essentially indistinguishable from the proposed spatially-disjoint Setting 1 (0.6308 / 1.2487 / 0.1558). This implies most of the train-val-gap reduction comes from simply not training the map and motion models on the same data, not from the careful spatial partitioning the paper sells as its main split contribution. The two issues — overlap between the map model's training data and the motion model's training data, vs. spatial overlap in nuScenes — are conflated, and the spatial-overlap claim should be defended independently (e.g., does it expose generalization gaps for the *map* model that a random split misses?).
- **Narrow model coverage for a paper framed as a benchmark.** Table 7 evaluates two motion models (HiVT, DenseTNT) crossed with two map models (MapTR, MapTRv2-CL). The related-work section discusses StreamMapNet, LaneSegNet, QCNet, MTR/MTR++, SceneTransformer, LaneGCN, TPCN, none of which are exercised. The protocol-level findings are likely robust, but the *generality* claim ("a well-defined benchmark", "solve the long-standing mis-usage") is materially weakened. At least one query-centric Transformer (e.g., QCNet) would substantially strengthen the benchmark's authority.

### Minor
- **"Boundary-free" framing oversells the baseline.** Equation 1 projects each agent onto an image feature using intrinsics/extrinsics — which requires the agent to be in some camera's FOV. Agents truly out of view get nothing. Calling this "boundary-free" misrepresents the actual coverage; image features have FOV/resolution boundaries even if they lack a hard BEV-range cutoff. The empirical improvement on far agents is real, but the paper should disentangle in-FOV-but-out-of-BEV agents from truly out-of-FOV agents.
- **No variance / seed information for Table 7.** Several deltas the paper highlights are small enough that a reader cannot tell whether they are statistically real. For example, on close non-ego minADE for MapTRv2-CL+HiVT, the `unc`/`bev`/`img` cells span 0.5175–0.5682; these comparisons are meaningful only if seed-level variance is well below that range. This is straightforward to fix and would strengthen the rankings the paper relies on.
- **GT-map-100×100 → image-features argument has a gap.** Table 3 shows that *GT* maps at 100×100 outperform 30×60 for HiVT (minADE 0.6003 vs 0.6154). The paper uses this to motivate the image-feature baseline, but image features and GT lane geometry are different information modalities. The motivational chain ("longer GT-map range helps" → "therefore raw image features help") should be either supported with an analysis that image features approximate the content of longer-range GT maps, or weakened in phrasing.
- **"Moving" threshold (2m in 3s) is unjustified.** Given that Table 6 shows static-agent prediction is trivial (minADE ~0.002), the moving/static partition decisively affects the headline metrics, but the choice of threshold is not motivated or sensitivity-analyzed.

### Trivial
- The phrase "long-standing mis-usage and misunderstanding" in the abstract is overstated for a protocol introduced in 2024.
- Table 5 appears to contain two rows with the same checkmark configuration (Boundary only) but different minADE values (0.6829 vs 0.6558); one of these is likely a "centerline-only" or similar configuration. *Caveat: this may be a parser artifact rather than an author error.*

## Nice-to-Haves
- Add a continuous curve of minADE as a function of agent distance from ego (per method/configuration). This would do more for the paper's "ego-only evaluation hides what matters" claim than the discrete close/far tables.
- Side-by-side ranking table: old ego-only protocol vs. new moving-non-ego protocol. Table 7 already implies that rankings shift; presenting this directly would be the cleanest evidence that the old protocol misleads.
- For the image-feature baseline, report the fraction of "far" agents that are in some camera's FOV at prediction time, and split the improvement accordingly. This would convert an incremental empirical win into a diagnostic finding about the protocol bottleneck.

## Removed Points
*These points are flagged to be removed; treat them with caution:*
- *"'All Map Elements' as a contribution is unsurprising."* — The paper itself acknowledges this in Section 3.5 ("Not surprisingly, feeding all possible map element types..."), so it is not overclaimed.
- *Speculation about an unspecified appendix or Section 3.5 typo as a "headline-claim-affecting" issue.* — The paper's centerline observation is supplemental, and the likely-parser duplicate row should not be treated as a substantive flaw.
- *Generic "evaluation lacks rigor" / "comparisons may not be fair" sweeps that did not anchor to a specific table or claim.*

## Novel Insights
None beyond the paper's own contributions. The reviewer inputs surface useful framings — particularly that Table 1's Setting 4 partially undermines the spatial-split contribution — but these are observations about the paper's evidence rather than novel ideas of their own.

## Suggestions
- Run an orthogonal ablation that varies (a) whether the map and motion models share training data and (b) whether splits are spatially disjoint, to separate the two ingredients now conflated in Table 1.
- Add at least one query-centric Transformer (QCNet or similar) and ideally one additional map model (e.g., StreamMapNet) to Table 7 to strengthen the benchmark's generality claim.
- Report seed variance across all OMMP-Bench cells in Table 7 (3 seeds minimum).
- Reframe the "boundary-free" baseline as "BEV-range-free" and provide an FOV-vs-BEV-range analysis.
- Justify or sensitivity-test the 2m/3s moving threshold.
- Tone down "long-standing mis-usage" — this is an early-stage protocol catch, which is itself valuable.

## Evaluation on the requested axes
- **Originality**: Moderate. The protocol critique is timely and the specific decomposition (split / range / metrics / element-type / baseline) is a reasonable framing, but each individual fix (disjoint splits, moving-agent filtering with close/far bins, image-feature retrieval via deformable attention) is conceptually familiar from other benchmarks (Argoverse/Waymo) and prior BEV-feature work.
- **Importance**: Real. The two-stage protocol introduced by Gu et al. (2024a;b) is gaining attention, and catching evaluation-design flaws now is genuinely useful.
- **Support for claims**: Mixed. The train-val-gap, range-mismatch, and ego-only-hides-failures claims are well supported. The "spatial overlap matters" claim is *weaker* than presented — Table 1 itself suggests random splitting captures most of the gain. The "benchmark" generality claim is undercut by the 2×2 model grid.
- **Soundness of experiments**: Reasonable but thin. Single-seed runs, narrow model coverage, and conflated ablations on the headline split.
- **Clarity**: Acceptable. The four-issue decomposition is easy to follow; the framing overreaches in places.
- **Value to the community**: Real. Researchers building on the Gu et al. protocol would benefit from this critique and the proposed metric refinements, even if the benchmark needs broader population to become authoritative.

## Anchor Comparisons
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/sEJYPiVEt4.md` — ESDMotion (avg 5.25, Round 1+2). Very close topic match: motion prediction on nuScenes with HiVT/DenseTNT, online mapping setting. Reviewers there criticized old baselines, limited novelty of feature-fusion ideas, and reliance on one dataset. The paper under review has analogous coverage limits (same baselines, same dataset) but adds something ESDMotion did not: explicit protocol critique with documentation of a real train-val gap and ego-only evaluation pathology. Roughly comparable.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/72MSbSZtHv.md` — RedMotion (avg 5.33, Round 1+2). Motion prediction method paper with broader baseline comparisons (Waymo Motion Challenge) but narrower contribution scope. The paper under review is broader in protocol scope but narrower in empirical coverage.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/ZPCBcR7Drg.md` — Driving by the Rules / MapDR (avg 5.00, Round 1+2). Benchmark paper for HD map / traffic-sign integration; reviewers asked for more diverse locations and richer ablations. Similar dynamic: useful new evaluation construct with limited coverage. Comparable to the paper under review.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/r125wFo0L3.md` — Large Trajectory Models (avg 5.00, Round 1+2). Different focus (scaling) but similar review pattern: real contributions, evaluation gaps.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/RflvsSxM0u.md` — Entropy-Based Uncertainty (avg 4.50, Round 2). Trajectory-prediction-on-nuScenes paper with narrow empirical contribution; reviewers gave 3/5/5/5. The paper under review has more substantive protocol-level contribution than this anchor.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/UapxTvxB3N.md` — Trajectory-LLM (avg 5.75, Round 2, Accept). Has a clearer "novel direction" (LLM-based generation). The paper under review does not have comparable novelty.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/H6i47PKXSN.md` — GAP planner (avg 5.25, Round 2). Mid-tier AD planning paper.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/9wSWiavGwU.md` — SwapTransformer (avg 5.00, Round 2). Mid-tier AD paper with niche contribution.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/DUkYDXqxKp.md` — DriveGPT4 (avg 4.75, Round 2). LLM-for-driving paper with reviewer skepticism about contributions.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/KyqtKhv6q1.md` — 3D Perception with Differentiable Map Priors (avg 4.25, Round 2). Related but distinct task.

**Round-1 bracket**: 4–6. **Round-2 narrowing**: anchors cluster at 4.5–5.5 with the most topically similar paper (ESDMotion) at 5.25. The paper under review sits a bit *below* ESDMotion because (a) it does not introduce a new method of comparable depth and (b) Table 1 specifically undermines part of its headline; but it sits *above* the 4.25–4.5 anchors because the protocol critique is substantive and timely. I place it at 4.5.

## Score and Decision

The paper makes legitimate, useful observations about a recently-introduced protocol and proposes sensible (if incremental) corrections. The contribution is real but is overclaimed — the benchmark coverage is narrow, the spatial-split argument is partially undermined by the paper's own Table 1, the "boundary-free" framing is imprecise, and no variance is reported. Calibrated against the closest anchors, it lands slightly below the ESDMotion / Driving-by-the-Rules cluster.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>