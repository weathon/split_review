Now I have all the information needed. Let me compose the final consolidated review.

## Summary

This paper identifies three core misconceptions in the emerging field of online-map-based motion prediction: (1) inappropriate data splits that cause a train–val distribution gap under two-stage training, (2) misaligned perception ranges between online mapping models (30×60m) and the motion prediction task (agents up to >100m), and (3) non-discriminative metrics that evaluate only the ego vehicle and include trivial static agents. The authors propose **OMMP-Bench**, a benchmark with a spatially disjoint three-way data split, refined metrics that evaluate moving non-ego agents separately at close and far ranges, and a boundary-free baseline that uses Deformable Attention over raw image features to provide environmental context for out-of-range agents. The paper also analyzes how different map element types (divider, boundary, pedestrian crossing, centerline) affect motion prediction performance.

## Strengths

1. **New spatially-disjoint data split that demonstrably eliminates the train–val gap.** Figure 3 quantifies the problem concretely: under the default split, online mapping mAP drops from 87.6 (train) to 50.3 (val), while under the proposed split the gap nearly vanishes (48.9 on motion train → 50.3 on motion val). Table 1 further shows this translates to a substantial motion prediction improvement (minADE improving from 0.6839 under the default protocol to 0.6308 under the proposed split). This is the paper's strongest contribution — a clean, actionable fix to a real benchmarking flaw.

2. **Refined evaluation metrics that are more discriminative and aligned with the purpose of motion prediction.** Table 6 demonstrates that static agents are trivially easy (minADE = 0.002), and that far agents are substantially harder than close ones (0.6997 vs. 0.5585 for HiVT+MapTR). Moving from ego-only to moving-non-ego evaluation, and separating close/far ranges, makes the benchmark more meaningful for assessing collision-relevant predictions — a sensible refinement.

3. **Multi-model evaluation revealing consistent trends.** Table 7 evaluates two online mapping models (MapTR, MapTRv2‑CL) × two motion models (HiVT, DenseTNT) × four methods (base, unc, bev, img), covering 8 combinations. The proposed image-feature baseline improves performance across all 8 combinations for far agents, and the improvement is consistently larger for far agents than for close agents when using HiVT, providing convergent evidence.

4. **Analysis of map element selection provides practical guidance.** Table 5 shows that including all map element types yields the best minADE (0.6308) vs. using only centerlines (0.6631) or only dividers (0.8770), giving the community concrete advice for designing online mapping model outputs.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **The boundary-free baseline is not isolated as a specific remedy for out-of-range agents.** The image-feature injection (Eq. 1) improves performance across *all* agent groups — ego, close non-ego, and far non-ego — not only far agents. For HiVT+MapTR, the minADE improvement on close agents is 5.5% and on far agents is 9.7%; for DenseTNT+MapTR, it is 16.6% on close and 14.2% on far. The paper provides no ablation that restricts image features to out-of-range agents only, nor a capacity-matched control without image features. Consequently, some of the gain could stem from general feature enrichment (the Deformable Attention module adds parameters) rather than specifically from filling missing map coverage for distant agents. This does not invalidate the baseline's usefulness, but the claimed mechanism is not conclusively demonstrated.

2. **The map-element selection analysis is thin.** Table 5 reports minADE for only a single model (HiVT) with no variance or statistical tests. Some adjacent conditions show small differences (e.g., boundary+pedestrian crossing = 0.6500 vs. boundary+centerline = 0.6631). The conclusion "feed all possible map element types" is sensible and likely correct, but the empirical support is a single un-ablated comparison.

3. **The benchmark does not demonstrate that the new metrics change method rankings.** The paper argues that the existing protocol is non-discriminative (Table 6 shows static agents are trivially easy and only the ego is evaluated), which is well-supported. However, it never shows that the relative ranking of methods differs under the old vs. new protocol. If the same models rank the same way under both protocols, the practical value of the metric reform is reduced. Showing ranking changes would strengthen the case.

### Trivial

1. **Numerical discrepancy in the claimed improvement.** The paper states "Applied the method on the MapTRv2-CL+HiVT model, the minADE decreased by 12.7%." From Table 7, the actual reduction for this combination (far agents) is (0.6999 → 0.6274) = 10.4%; the 12.7% figure corresponds instead to MapTRv2-CL+DenseTNT (2.2742 → 1.9836 = 12.8%). This is a minor factual error that should be corrected.

2. **Lack of variance/confidence intervals on main benchmark results.** Table 7 reports single-run metrics without any measure of uncertainty, making it difficult to assess whether small differences (e.g., MapTRv2-CL+HiVT unc vs. base for close agents: 0.5682 vs. 0.5585) are meaningful.

## Nice-to-Haves

- **Ranking correlation analysis between old and new evaluation protocols** (Spearman or Kendall rank correlation). This would directly validate whether the refined metrics change conclusions about which methods are best.
- **Ablation of the image-feature baseline** that isolates the effect for far-only agents (e.g., by masking features for close agents) or a capacity-matched control without image features to disentangle the "out-of-range coverage" mechanism from general feature enrichment.
- **Distributional analysis of far agents** — their typical distances, the amount of map coverage they actually receive under the 30×60m perception range, and how much of the minADE gap is attributable to missing map context vs. inherent prediction difficulty.

## Removed Points

- **"The new data split is not evaluated for whether it actually eliminates the train-val gap"** (Harsh Critic, Critical Issue 2). **Factually wrong.** Figure 3 explicitly reports online mapping mAP on both motion train (48.9) and motion val (50.3) under the proposed split, alongside the default split values (87.6 train → 50.3 val). The paper does verify the claimed reduction in train-val gap.
- **"The claim that stronger online mapping model benefits motion prediction is trivial"** (Harsh Critic, Critical Issue 5). **Overly harsh.** The paper is establishing baseline benchmark results, not claiming a novel scientific insight. The observation serves to validate the benchmark's utility, not to inflate the contribution. It is a reasonable sanity check.
- **"The threshold for close/far is not explicitly stated"** (Harsh Critic, Section 3.4). **Misreads the paper.** Section 3.4 states "close and far are decided by whether within the perception range of online mapping models" and Section 3.3 states MapTR covers 30×60m. The threshold is explicitly defined.
- **Strength Finder's generic strengths** ("addressed an important problem," "timely topic") — removed as lacking specific content. The specific evidentiary strengths are retained in the Strengths section above.

## Novel Insights

The most notable observation from the reviews is a subtle pattern evident in Table 7 that the paper does not discuss: the image-feature baseline helps far agents more than close agents when the motion model is HiVT (9.7% vs. 5.5% for MapTR; 10.4% vs. 7.3% for MapTRv2-CL), but with DenseTNT the pattern *reverses* (far improvement is smaller than close: 14.2% vs. 16.6% for MapTR; 12.8% vs. 15.6% for MapTRv2-CL). This interaction suggests that the benefit of image features depends on the motion model's architecture or its capacity to exploit the additional visual context — a finding that could guide future work on which motion prediction paradigms are most compatible with perception-modality fusion. This pattern is latent in the paper's data but not surfaced in the paper's analysis.

## Suggestions

1. Correct the 12.7% number in Section 4.2 so it matches the table (10.4% for MapTRv2-CL+HiVT, or state the correct value for the DenseTNT combination).
2. Add a simple ablation for the image-feature baseline that restricts it to far agents only, or add a parameter-matched control (e.g., an MLP on agent history with equivalent extra dimensions) to demonstrate that the improvement is specific to the visual context mechanism.
3. Report Spearman rank correlation between method rankings under the old protocol (ego-only, all agents) and the new protocol (moving non-ego close/far) using the 8 combinations in Table 7.
4. Provide confidence intervals or standard deviations for the main benchmark results (Table 7, Table 4), or at minimum state how many seeds were run.

## Score and Decision

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>