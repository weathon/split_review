Now I have all the information needed. Let me synthesize the final review.

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

Let me draft this carefully now.

---

Based on my analysis:

**Cross-checking Harsh Critic Issue 1 (Data split / training size):** The paper's Table 1 Row 4 already subsamples the default split (50% each for map and motion training), which partially addresses this concern. Row 4 gives 0.6373 vs Row 1 (Ours) 0.6308 — a much smaller gap than Row 3 (Default, full trainset) at 0.6839 vs Row 1. The paper does not discuss Row 4 in the text, which is a weakness, but the control exists. **WEAKEN to minor.**

**Cross-checking Harsh Critic Issue 2 (Close/far definition):** The paper defines close/far as "whether within the perception range of online mapping models" (line 496-497). This is operationalized per-model (e.g., MapTR uses 30×60m). It's workable but ambiguous for reproducibility across different models. **WEAKEN to minor.**

**Cross-checking Harsh Critic Issue 3 (Ego-only claim):** The paper's claim that Gu et al. (2024a) only evaluates ego is stated multiple times. This is well-established knowledge about that paper (it's a CVPR 2024 Best Paper Finalist known for this protocol design). The reviewer's demand for "quotation or reproduction" is excessive. **REMOVE.**

**Cross-checking Harsh Critic Issue 4 (Image baseline under-specified):** The description is indeed sparse — two sentences and one equation (lines 434-448). No backbone details, no mention of frozen/fine-tuned, no variance reported. Valid minor weakness. **KEEP as minor.**

**Cross-checking Harsh Critic Issue 5 (Narrow scope):** 2 motion models + 2 mapping models = 16 configurations. This is reasonable for a benchmark paper establishing a new protocol. **WEAKEN to nice-to-have.**

**Strength Finder check:** The strengths are grounded and backed by evidence from the paper. No generic nonsense here. All KEEP.

Now let me determine the score.

Comparing to anchors:
- **mxz5RqhCMe.md (HD Mapping Stability Benchmark, avg 4.67, accept):** Both benchmark papers in online HD mapping. The mapping stability paper evaluates 42 model variants — far more comprehensive. But the paper under review identifies more fundamental protocol problems (split, range, metrics). Similar quality tier — the under-review paper is slightly less comprehensive in experiments but has stronger problem identification.
- **aqwtK0OIGs.md (SD Map Motion Prediction, avg 4.50, withdrawn/reject):** Similar domain. The SD map paper was seen as incremental/heuristic. The paper under review has stronger motivation and identifies genuine community-wide problems. Slightly stronger.
- **OrgL5DsU0f.md (DrivingGen, avg 6.50, accept):** Much more comprehensive benchmark with thorough evaluations. The paper under review is significantly less comprehensive. Weaker.
- **j3960MwHQn.md (VCBench, avg 2.50, reject):** Weak benchmark with limited novelty. The paper under review has clearer contributions. Stronger.

I place this paper around 3.5-4.0. The main concerns: the training data size confound is not properly discussed/controlled, the image baseline is under-validated, and no statistical significance is reported. These are fixable issues, but they weaken the current submission.

Let me go with 4.0.Now I have thoroughly read the paper and cross-checked every claim against the actual content. Here is my consolidated final review.

---

## Summary

This paper identifies three genuine misconceptions in the emerging online map based motion prediction protocol: (1) inappropriate data splits that create a train-val gap, (2) misaligned perception ranges between online mapping and motion prediction, and (3) non-discriminative ego-only metrics. To address these, the paper proposes OMMP-Bench with a new spatially-disjoint split, refined metrics evaluating all moving non-ego agents with close/far stratification, an analysis of map element formulations, and a boundary-free image-feature baseline for out-of-range agents.

## Strengths

- **Spatially-disjoint data split eliminates the train-val gap.** The paper correctly identifies that the standard nuScenes split causes motion prediction models to train on highly accurate online maps (from the map model's training set) but evaluate on much less accurate maps, creating a severe distribution shift. The proposed three-way split (map train, motion train, motion val) ensures the map model has never seen motion subsets, and Table 1 shows the split yields minADE 0.6308 vs. 0.6839 under the default split — a tangible improvement. Figure 4 further documents that 87% of the default validation scenes overlap spatially with the training set, confirming the problem is real.

- **Refined evaluation metrics that actually test motion prediction.** Prior work evaluates only the ego vehicle, which contradicts the purpose of motion prediction (predicting other agents to avoid collisions). The paper proposes evaluating all moving non-ego vehicles and stratifying by close/far distance relative to the map model's perception range. Table 6 demonstrates that static agents are trivial (minADE ≈ 0.002) and that far agents are substantially harder (0.6997 vs. 0.5585 for close), making the metrics more discriminative and realistic.

- **Systematic analysis of online map element formulations.** Table 5 compares the influence of different map element types (divider, boundary, pedestrian crossing, centerline). Using all elements together yields the best performance (0.6308 minADE), centerline-only is second best (0.6500), and divider-only is worst (0.8770). This provides concrete guidance for the community on which map outputs are most valuable for downstream motion prediction.

- **Image-feature baseline for out-of-range agents provides a promising direction.** The paper observes that online mapping models have limited perception ranges (e.g., 30×60m for MapTR) while agents can be >100m away, and proposes extracting raw image features via deformable attention. Table 7 shows the largest gains on far agents — e.g., MapTRv2-CL+HiVT reduces far-agent minADE by 12.7% (from 0.6999 to 0.6274).

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Table 1's split comparison is confounded by training data size, and the paper does not discuss this.** Row 4 in Table 1 (nuScenes Train subsampled to ~50% each for map and motion training) achieves minADE 0.6373 — much closer to the proposed split's 0.6308 than the default full-train split's 0.6839. This suggests that much of the observed improvement comes from reducing the training set size rather than from the spatial disjointness of the split. The paper claims "the split of OMMP-Bench leads to an explicit performance enhancement compared to the default split" but does not discuss Row 4 or disentangle the two factors. A controlled ablation that isolates spatial disjointness from training data quantity is needed.

- **The "close" vs. "far" agent definition is operationalized relative to each map model's perception range but not specified as a fixed, model-independent threshold.** The paper writes that "close" and "far" are "decided by whether within the perception range of online mapping models" (line 496-497). Since different models have different ranges, this makes comparisons across map models imprecise — an agent considered "close" under one model might be "far" under another. A fixed geometric threshold (e.g., distance from ego) would improve reproducibility, even if the primary analysis also reports per-model results.

- **The image-feature baseline is under-specified and lacks statistical validation.** The method is described in only two sentences and one equation (lines 434-448). The paper does not specify which image backbone is used, whether it is frozen or fine-tuned, or whether image features are applied to all agents or only out-of-range ones. The overall minADE improvement is modest (0.6375→0.6163, ~3.3%) and no standard deviations or confidence intervals are reported for any result in the paper, making it impossible to assess whether the improvements are statistically significant. Some configurations in Table 7 even show small degradations on close agents (e.g., MapTR+HiVT "unc" and "bev" methods sometimes hurt close-agent performance), which the paper does not analyze.

- **The narrow experimental scope limits the strength of some conclusions.** Only two motion prediction models (HiVT, DenseTNT) and two online mapping models (MapTR, MapTRv2-CL) are evaluated. The claim that "stronger online mapping models benefit motion prediction" rests on a single comparison (MapTR vs. MapTRv2-CL). Broader coverage (e.g., QCNet, MTR++) would strengthen the benchmark's conclusions.

### Trivial
- Lines 494-497 could be explicitly numbered with the exact distance thresholds used for the specific map models in the experiments.

## Nice-to-Haves
- Report standard deviations or confidence intervals over multiple seeds for the main results (Tables 1, 4, 7) to establish statistical significance.
- Compare the image-feature baseline against simpler alternatives such as zero-padding or a learned NULL token for out-of-range agents, to quantify the specific benefit of the image features.
- Add at least one more modern motion prediction model (e.g., QCNet, MTR++) to broaden the conclusions.
- Include qualitative visualizations (e.g., a far-away agent where the online map provides nothing vs. the image feature adding useful cues).

## Removed Points
- **Criticism that the paper's claim about ego-only evaluation in Gu et al. (2024a) is "insufficiently supported."** This is a well-established fact about the cited work (a CVPR 2024 Best Paper Finalist), and the reviewer's demand for direct quotation or reproduction is disproportionate. The paper's characterization is standard and reasonable. *[Removed: factually incorrect reading of how citations work in the field]*
- **Criticism about "missing appendix" / "missing proofs."** The parser strips appendix content from the extracted text; the original submission contains it. *[Removed: parser artifact, not author error]*
- **Criticism from Harsh Critic about "selective emphasis" of the 12.7% improvement while ignoring smaller/negative gains.** The paper explicitly states "Integrating image feature helps to predict agents far away" which is factually correct — the 12.7% gain is on far agents specifically, and the paper also notes negative results (e.g., "unc" and "bev" methods sometimes hurt close agents on lines 581-588). *[Removed: the paper already discusses the nuanced results]*

## Novel Insights
None beyond the paper's own contributions. The reviewers did not identify any pattern that the paper itself does not already articulate.

## Suggestions
1. **Disentangle the split design from training data size.** Add an ablation that compares the proposed spatially-disjoint split against a version of the default split that uses the same number of training scenes (e.g., randomly subsample nuScenes Train to 367 scenes for map training and 397 for motion training while keeping the default evaluation on nuScenes Val). This would cleanly isolate the effect of removing spatial overlap from the effect of reduced data.
2. **Define close/far with a fixed geometric threshold** (e.g., Euclidean distance from ego > 50m) in addition to the per-model operational definition, to improve cross-model comparability and reproducibility.
3. **Specify image backbone details** (which architecture, frozen or fine-tuned) and report results with variance across at least 3 random seeds.
4. **Add a "zero-padding" or "learned NULL token" baseline** for out-of-range agents to quantify the specific value added by the image features.

## Score and Decision

**Calibration anchors (from human-review corpus):**

| Path | Avg Score | Comparison to this paper |
|------|-----------|------------------------|
| `mxz5RqhCMe.md` (HD Mapping Stability Benchmark) | 4.67 | Both are benchmark papers in online HD mapping. The stability paper evaluates 42 model variants (more comprehensive) but has metric-design concerns. This paper identifies more fundamental protocol problems. Comparable quality. |
| `aqwtK0OIGs.md` (SD Map Motion Prediction) | 4.50 | Similar domain. The SD map paper was seen as incremental/heuristic. This paper has stronger problem identification and clearer motivation. Slightly stronger. |
| `OrgL5DsU0f.md` (DrivingGen Benchmark) | 6.50 | Much more comprehensive benchmark with thorough evaluations across 14 models. This paper is significantly less comprehensive. Weaker. |
| `j3960MwHQn.md` (VCBench) | 2.50 | Weak benchmark with limited novelty and missing details. This paper has clearer contributions and more rigorous analysis. Stronger. |
| `NrSx6J6IZk.md` (Benchmark of Benchmarks) | 5.00 | Meta-analysis, different domain. Mixed reviews on its methodology. Hard to compare directly. |
| `INy8guZqrm.md` (HUMOF Motion Forecasting) | 6.00 | Method paper, not benchmark. Strong empirical results with clear SOTA claims. This paper is not directly comparable. |

The paper identifies important and timely problems and proposes reasonable fixes, but the experimental validation has gaps: the training data size confound in the split comparison is not discussed, the image baseline is under-validated with no statistical significance, and the scope is narrow. These are fixable issues that would substantially strengthen the submission. Relative to the anchors, this paper sits between the weak benchmarks (~2.5) and the strong comprehensive ones (~6.5), comparable to the mid-tier benchmark papers (~4-5).

MY FINAL SCORE: <pineapple>4.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>