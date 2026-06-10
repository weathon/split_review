Now let me produce the final review.

## Summary

This paper introduces a new "atypical" video dataset (5,486 videos across sci-fi, animation, unintentional, and abnormal categories) and uses Outlier Exposure (OE) to study whether training on unconventional video data improves OOD detection for video action recognition. The main finding is that the smaller atypical dataset outperforms the much larger Kinetics400 as an OE source, and OOD performance improves as more atypical categories are included. The paper is framed as an exploratory study.

## Strengths

1. **Novel, purpose-built atypical video dataset**: The paper collects and releases the first dataset explicitly designed to study atypical video content for OOD detection, spanning four categories (sci-fi, animation, unintentional, abnormal) that qualitatively differ from standard action recognition benchmarks (Section 3, Table 1).

2. **Atypical data outperforms large-scale typical data (Kinetics400) as OE source**: Table 2 reports that the much smaller atypical dataset (~5.5K videos) yields better OOD detection on real OOD datasets (HMDB51, MiT-v2) than Kinetics400 (~240K videos). This is a non-obvious result that directly supports the paper's core hypothesis and has practical implications (Section 4.4, line 178).

3. **t-SNE feature-space analysis provides mechanistic insight**: Figure 6 visualizes that atypical OE data produces more dispersed feature distributions than Kinetics400 OE data, supporting the explanation that diverse atypical samples expand decision boundaries and improve OOD discrimination (Section 5, lines 203–208, Figure 6).

4. **Rigorous category-orthogonality preprocessing**: The paper explicitly removes 93 overlapping action categories between Kinetics400 and UCF101/HMDB51, plus 6 overlapping categories between HMDB51 and UCF101, ensuring no information leakage between ID, OOD, and OE datasets (Section 4.2.3, lines 158–160).

## Weaknesses

### Major

1. **No variance or reliability estimates reported for any experiment**: Every metric in Tables 2 and 3, and every point in Figures 4 and 5, is reported as a single number with no multiple runs, random seeds, or confidence intervals. Given that SGD training with data augmentation is inherently stochastic, the reader cannot assess whether the reported differences between methods are reliable or within the noise of a single run. This is a significant methodological gap for a top-venue paper and makes it impossible to evaluate the robustness of the claimed improvements.

2. **The central claim about categorical diversity is not properly controlled**: The paper argues that "increasing the categorical diversity of the atypical samples further boosts OOD detection performance" (abstract), but Figures 4 and 5 add entire categories (along with all their videos) without holding total OE data volume constant. The observed improvement could reflect simply having more OE data in absolute terms rather than diversity *per se*. A controlled experiment — comparing N videos from one category vs. N videos spread across multiple categories — is needed to substantiate the diversity claim and is absent.

3. **Noise OOD test sets conflate evaluation and inflate aggregate metrics**: The evaluation includes Gaussian noise and Bernoulli noise as OOD test sets alongside realistic sets (HMDB51, MiT-v2). As the paper itself acknowledges (line 178), these noise sets are trivially easy to detect. By averaging metrics across all four sets, the noise sets inflate apparent performance, and the reported mean comparisons between OE methods may be driven more by noise-set performance than by behavior on realistic OOD scenarios. The paper should report and prioritize results on the realistic OOD sets.

4. **Comparison between atypical data and Kinetics400 is confounded by multiple uncontrolled factors**: The finding that atypical data (~5.5K videos) outperforms Kinetics400 (~240K videos) is potentially interesting, but the comparison involves many uncontrolled differences beyond "atypicality": dataset size, number of categories, video source characteristics, production quality, and visual features. Without controlling for these (e.g., matching training set sizes, ablating by content type), the comparison is suggestive but not diagnostic of *why* atypical data helps.

### Minor

1. **Equation 2 does not match the implemented objective**: The formal OE objective in Equation 2 (line 127) writes L_OE as a function of *both* ID variables (f(x), y) and the OE sample (f(x')), nesting the OE expectation inside the ID expectation. The actual implementation (line 134) uses the standard decoupled OE formulation from Hendrycks et al. (2019), where the OE term is simply H(U; f(x')) on OE samples independently, with no dependence on ID variables. This inconsistency is confusing and suggests the equation was not proofread against the implementation.

2. **Single backbone limits generalizability**: All experiments use only ResNet3D-50. It is unclear whether the findings generalize to other video architectures (e.g., VideoMAE, SlowFast), limiting the strength of the claimed findings.

3. **"Abnormal" subset composition dilutes the "atypical" characterization**: The abnormal subset draws from classic video anomaly detection datasets (Ped2, CUHK Avenue, ShanghaiTech, UCF Crime). Many events in these datasets (e.g., someone riding a bike in a pedestrian zone) are deviations from a narrow scene-specific normal rather than genuinely "atypical" content, which may dilute the distinctiveness of this category relative to what the paper claims.

### Trivial

1. Missing implementation details: batch size is not reported, which is relevant for video training with 3D convolutions.
2. The title references "Harry Potter" but the paper itself never mentions Harry Potter — this is a thematic disconnect.

## Nice-to-Haves

- To strengthen the diversity claim, hold total OE video count constant and compare: all videos from one category vs. equal split across two categories vs. equal split across all four. This is the cleanest test of the central claim.
- Report variance across at least 3–5 runs with different random seeds.
- Restructure evaluation to foreground per-dataset results on HMDB51 and MiT-v2; relegate noise-set results to an appendix or report separately without aggregation.
- Control for additional fine-tuning: the baseline is trained for 100 epochs while OE models get 100 + 5. A control fine-tuning the baseline on ID data for 5 more epochs without the OE term would isolate the OE effect.
- A quantitative analysis (e.g., nearest-neighbor distance or semantic similarity) demonstrating that the atypical dataset is categorically different from ID/OOD datasets would strengthen the paper's motivation.

## Removed Points

- Harsh Critic's claim that "the smaller dataset permits more passes over each sample" is factually incorrect: both atypical data and Kinetics400 are fine-tuned for 5 epochs, so each sample in either dataset is seen exactly 5 times. Removed.
- Harsh Critic's characterization of ResNet3D-50 as a "dated choice" — removed as a subjective characterization; the single-backbone limitation is retained as a minor weakness.
- Harsh Critic's criticism of the conclusion introducing unmotivated future directions — removed as this is standard paper-writing practice and not a substantive weakness.
- Harsh Critic's concern that the paper "over-claims" the relationship to open-world discovery — the paper defines OOD detection as a specific task within open-world learning in Section 2.1, making this a matter of degree rather than a factual error.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add statistical grounding: report results over multiple seeds with confidence intervals for all experiments.
2. Design a controlled diversity experiment holding total OE video count constant.
3. Restructure the evaluation to foreground realistic OOD datasets (HMDB51, MiT-v2) and move noise sets to an appendix.
4. Fix the inconsistency between Equation 2 and the actual fine-tuning objective.
5. Report omitted implementation details (batch size, clip sampling strategy).
6. Discuss the practical implication that a small, curated atypical dataset can outperform a massive standard dataset — this is a compelling narrative point currently underdeveloped.

## Score and Decision

This paper offers a useful new dataset and asks an interesting question, but the experimental evidence is not rigorous enough for a top venue. The absence of any variance estimation, the uncontrolled diversity analysis, the conflated evaluation (noise sets inflating aggregate metrics), and the confounded comparison with Kinetics400 all undermine confidence in the paper's central claims. The core idea has merit, but the current evidence is preliminary. Substantial additional experimentation and controls would be needed to meet the bar for ICLR.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>