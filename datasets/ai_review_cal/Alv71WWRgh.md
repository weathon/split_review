- Decision: Reject
- Avg Score: 4.50
- Scores: 3, 5, 5, 5
Now I have a thorough understanding of the paper. Let me compose the consolidated review.

## Summary
The paper identifies a real problem — MLLM-driven image editing methods fail on spatial instructions — and proposes SpatialEdit, which includes (1) a data engine that extracts 3D spatial info from 2D images to generate spatial VQA and editing data, and (2) a two-stage training method with "attention tuning" (unfreezing attention layers) to improve spatial understanding. It also introduces SpatialEval, a benchmark for spatial editing. Results show a 7B model beating larger models on spatial editing and achieving SOTA on four zero-shot general editing benchmarks.

## Strengths

1. **Attention score analysis provides a concrete, testable insight.** Equation (5) in Section 4.2 shows that under embedding tuning (only trainable embeddings, frozen MLLM), attention scores for any token are scaled by a common factor, preserving the relative ranking of token importance. This formally explains why existing methods cannot learn to re-weight spatial-relevant tokens — e.g., making "leftmost" attend to the correct visual region. This is the paper's most specific and defensible theoretical contribution.

2. **Data engine for spatial training data.** Section 5.1 (Figure 2) describes a multi-stage pipeline (LLaVA → GroundSAM → Depth Anything → RANSAC) that extracts position, contour, volume, and relative distance from 2D images to automatically generate spatial VQA pairs (62K) and spatial editing tuples (25K). This addresses a genuine bottleneck identified qualitatively by the paper: existing training datasets lack spatial information.

3. **Two-stage training with attention tuning directly targets the identified bottleneck.** Stage I uses the generated VQA data with attention layers unfrozen to improve spatial understanding; Stage II trains on spatial editing data end-to-end. The ablation variants (w/o S1, w/o S2, w/o DE) allow isolating the contribution of each component. The approach is conceptually clean.

4. **SpatialEval benchmark fills a gap.** The paper constructs a benchmark of 90 images from OpenImages, COCO2017, and DAQUAR with human-written instructions targeting spatial perception, reasoning, and visualization. This provides a standardized test bed that was missing, enabling the first systematic comparison on spatial instruction following.

5. **Empirical results are promising if confirmed.** The paper reports that a 7B SpatialEdit model outperforms larger models (Seed-X 17B, GPT4V+Dalle3) on SpatialEval and achieves SOTA on four zero-shot general editing benchmarks (MagicBrush, EVR, MA5k, GIER). The ablation variants are described, allowing readers to assess the contribution of each component.

## Weaknesses

### Major

1. **Theorem 2 is not a valid proof; the logical chain is absent.** Theorem 2 (Section 6) assumes "it is easier to approximate distribution q(x|c) than q(x) by only adjusting the embedding E" and then directly concludes that models trained on spatial conditions outperform on both general and spatial tasks. The paper states the assumption and then states the conclusion with no derivation connecting them. The conclusion does not logically follow from the assumption as presented — there is no reasoning about how training on spatial data optimizes parameters to yield the claimed inequalities. This is an assertion, not a theorem. The paper repeatedly claims "theoretical proof" (e.g., line 35, abstract), which overstates the contribution. This weakens the paper's framing significantly.

2. **The main experimental comparison is confounded by additional training data.** The paper's method is trained on IPr2Pr *plus* the data engine's 25K spatial editing tuples and 62K VQA pairs, while baselines are trained on IPr2Pr only. Although an ablation "SpatialEdit w/o DE" (trained on 25K IPr2Pr data with attention tuning) partially controls for data volume, the main results tables (Tables 1, 2) do not include a baseline trained on an equivalent *supplement* of augmented data. Without isolating whether the improvement comes from the data engine's data quality, the data volume, or the attention tuning, the SOTA claim is not fully supported.

3. **SpatialEval's evaluation protocol lacks validation and detail.** The benchmark uses GPT-4V and GPT-3.5 as evaluation metrics (Section 5.3), yet the paper's own motivation (Figure 1, abstract) demonstrates that GPT-4V performs poorly on spatial editing tasks. The paper does not justify why GPT-4V would be a reliable *evaluator* of spatial editing quality despite being an unreliable *performer*. Additionally: (a) no ground-truth edited images are provided, making the benchmark entirely dependent on LLM-as-judge or human evaluation; (b) the human evaluation protocol is unspecified — no number of annotators, inter-annotator agreement, or instructions are given; (c) at 90 images × 3 instructions, the benchmark is relatively small. These issues make the central claim of "SOTA spatial editing" difficult to verify.

4. **Data quality analysis (Section 7.5) is asserted without evidence.** The paper states: "We found that the quality of our automatically generated data is higher than most datasets, especially showing an advantage in spatial information." No numerical results, annotation protocol, comparison numbers, or evaluation criteria are provided. This is a central claim about the data engine's value, left entirely unsubstantiated.

### Minor

1. **Theorem 1 (Rademacher complexity) is generic.** The bound that stacking Lipschitz function classes increases Rademacher complexity is a generic property that applies to any deep stacked architecture, not specifically to MLLM-driven editing. The paper does not make the connection concrete (e.g., by computing or estimating Lipschitz constants for the specific components). It is more of a plausibility argument than a novel theoretical insight about spatial editing.

2. **Attention score derivation's generality depends on an unverified assumption.** Equation (5) decomposes the attention score such that the scaling factor is shown to be equal for all tokens. The paper asserts this follows because "only embeddings are trainable" but does not verify that the normalization terms collapse to a single common factor in the multi-head, multi-layer setting. The extension to multi-head and multi-layer cases is stated without argument (line 137).

3. **Data engine failure modes are not discussed.** The pipeline chains LLaVA, GroundSAM, Depth Anything, and RANSAC. Each component can produce errors (segmentation failures, depth estimation inaccuracies, RANSAC outliers). The paper does not describe how such failures are detected, filtered, or how they affect the quality of the 62K VQA and 25K editing samples. A quality filter or validation step may exist but is not described.

4. **Loss balance in Stage II is not discussed.** The Stage II loss is L = L_condition + L_edit with no weighting terms (line 208). The paper does not discuss whether these losses are naturally on the same scale or how the balance was determined, which could affect training dynamics.

5. **The SpatialEval benchmark instructions are described only generically.** The paper states instructions relate to "spatial perception, spatial reasoning, and spatial visualization capabilities" (line 220) but provides no examples, breakdown, or analysis of what types of spatial reasoning are covered and whether the distribution is balanced.

### Trivial

None that survived filtering.

## Nice-to-Haves

- Provide a controlled experiment where a baseline (e.g., MGIE) is fine-tuned on an equivalent amount of the data engine's spatial editing data to isolate the benefit of the data content from the training strategy. The w/o DE ablation partially addresses this but uses IPr2Pr data, not the data engine's data.
- Validate the GPT-4V-as-evaluator on SpatialEval by showing correlation with human judgments or replacing it with a task-specific automatic metric.
- Report variance or confidence intervals for the main experimental results.
- De-emphasize or restructure Sections 4 and 6 as intuitive motivation and heuristic reasoning rather than claimed formal proofs.

## Removed Points

- **"Theoretical proof not given in main text"** (Theorem 1 derivation, appendix-deferred proofs): Removed per rule that the parser strips appendix content; these likely exist in the original submission.
- **"Table 4 and Figure 4 not present"**: Removed per rule about parser-stripped tables/figures.
- **"Implementation details unspecified"** (hyperparameters, learning rates, GPU count): Removed per rule about reproducibility nitpicks for trivial implementation details.
- **"Typography/formatting issues"** (braces, equation rendering): Removed per rule about parser artifacts.
- **"No ground-truth edited images in SpatialEval"**: The paper explicitly states this is by design for zero-shot evaluation (line 220). This is standard practice; the criticism misunderstands the benchmark design.
- **Strength finder's generic strengths** ("this paper addresses an important problem"): Removed as generic/superficial; dropped per rule about strengths lacking specific content.
- **"Missing related work"**: Removed per rule about not mentioning missing related works without external sources.
- **"Unfair comparison — baselines not trained on augmented data"**: WEAKENED rather than removed. The criticism has merit but the paper includes a relevant ablation (w/o DE) that partially addresses it, so it was downgraded from what the harsh critic framed as a fatal issue to a major concern.

## Novel Insights

The most notable observation that emerges from the reviews is that **the paper's theoretical framing (Sections 4 and 6) is substantially weaker than its empirical contribution.** The attention score analysis (Section 4.2) is a genuinely useful insight about why embedding tuning fails for spatial tasks, but it is sandwiched between Theorem 1 (a generic Rademacher bound with no editing-specific content) and Theorem 2 (an assumption stated as a theorem with no logical derivation). The paper would be stronger if it dropped the pretense of formal proofs for Theorem 2 and instead presented the attention score analysis as the core theoretical motivation, supported by the empirical ablation study. Another insight: the data engine pipeline, while ambitious, is evaluated only through downstream editing results, not independently validated — the Section 7.5 claim of "higher quality than most datasets" needs specific evidence before the community can rely on it.

## Suggestions

1. **Remove or restructure Theorem 2.** It is currently presented as a "theoretical proof" but is logically incomplete. Either provide a full derivation showing how the assumption leads to the conclusion, or reframe it as an intuitive justification / hypothesis.
2. **Provide a fully controlled comparison.** Train a strong baseline (e.g., MGIE) on IPr2Pr + the data engine's 25K spatial editing data and compare against SpatialEdit trained on the same data. This isolates the benefit of the training strategy from the data.
3. **Validate and document SpatialEval's evaluation protocol.** Report inter-annotator agreement for human evaluation, show correlation between GPT-4V scores and human scores, and provide example instructions by category. Without this, the benchmark results are not reproducible.
4. **Substantiate Section 7.5 (data quality) with concrete numbers.** Report human evaluation scores for data quality (accuracy of spatial information, correctness of ground-truth images) compared against IPr2Pr and other datasets, with annotation protocol details.
5. **Discuss failure handling in the data engine pipeline.** How many samples were discarded? What quality threshold was applied? What is the estimated false positive rate for spatial information extraction?
6. **Report the loss balance and training hyperparameters** for Stage II (or confirm they were on the same scale naturally).
