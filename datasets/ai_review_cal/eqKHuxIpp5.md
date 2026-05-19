- Decision: Reject
- Avg Score: 2.50
- Scores: 1, 3, 3, 3
Now I have a thorough understanding of the paper. Let me construct the final consolidated review.

---

## Summary

This paper addresses the problem of selecting a partitioning point in a DNN for on-device transfer learning — i.e., which layers to freeze/quantize and which to retrain. The authors propose a framework that uses NSGA-II multi-objective optimization to explore mixed-precision quantization schemes, using quantization robustness as a signal for layer sensitivity, and then extracts a single contiguous partition point. The method is evaluated on ResNet-18 and SqueezeNetV1.1 across three datasets (Flowers-102, STL-10, OxfordIIITPet), showing that the identified mixed-precision model (int8 bottom, bfloat16 top) matches the accuracy of a full bfloat16 baseline.

## Strengths

- **Algorithm identifies the partitioning layer without exhaustive retraining.** The paper proposes a one-shot approach using quantization robustness and NSGA-II optimization (20 generations, 32 initial samples) rather than iteratively freezing each layer and retraining. The experimental results in Figure 3 show that the identified partition point matches what would be found by the expensive iterative-freezing baseline — a meaningful reduction in computational overhead. (Section 3.3, Definition 5; Section 5, Figure 3)

- **The partitioned mixed-precision model matches full bfloat16 accuracy.** Across all three datasets and both model architectures, the green dots in Figure 3 representing the int8-bottom/bfloat16-top model achieve accuracy comparable to the full bfloat16 baseline. This directly validates the claim that the partition does not degrade transferred knowledge. (Section 5, Figure 3; Section 4.2 experimental procedure)

- **Clear empirical motivation for splitting before the classifier.** Table 1 provides useful grounding by showing that partitioning one layer before the classifier yields higher accuracy than the common practice of splitting at the classifier. This motivates why the algorithm searches within the feature extractor. (Section 2, Table 1)

- **Systematic treatment of DAG architectures.** Section 3.2 explicitly addresses topological ordering for modern DNNs with skip connections (e.g., ResNet), which is necessary for robust partitioning in non-sequential networks. Prior partitioning work often assumes sequential models. (Section 3.2, Definition 3)

## Weaknesses

### Fatal
None.

### Major

- **The mapping from mixed-precision optimization output to a single contiguous partition is not explained.** The NSGA-II exploration (Definitions 5–7) finds Pareto-optimal *mixed-precision quantization schemes* across layers, which could interleave quantized and bfloat16 layers arbitrarily. The optimization objectives (maximize quantized layers, maximize accuracy, minimize bit-width) do not enforce contiguity. Yet Definition 8 and the entire experimental evaluation assume a contiguous partition where layers 1 through *s*−1 are quantized and layers *s* through |L| are bfloat16. The paper never explains how a potentially non-contiguous mixed-precision scheme is reduced to a single contiguous cut. This is not a presentation nitpick — it is a structural gap between what the algorithm actually produces and what is validated. (Section 3.3–3.4, Definitions 4–8)

- **The evaluation bypasses the algorithm's mixed-precision output.** The paper states: "it is possible to keep the mixed-precision quantization for the frozen layers, as our algorithm provides this as well. However, as a general example for the evaluation part, we converted all frozen layers to int8" (Section 4.2). This means the validation tests a *uniform int8* model, not the actual mixed-precision scheme the algorithm outputs. The accuracy of uniform int8 quantization may differ from a scheme where specific layers use 4-, 6-, or 16-bit integer, so the evaluation does not validate what the algorithm produces.

- **No quantitative resource measurements.** The paper's title and motivation center on enabling on-device transfer learning with reduced memory and energy. Yet the paper reports zero measurements of memory footprint, latency, power, or energy — on any hardware or even via analytical estimation (e.g., activation memory for backpropagation, MAC counts). Accuracy preservation is a necessary condition, but without any resource metric, the central claim of enabling efficient on-device training is unsubstantiated. The only evidence offered is that a plausible partition does not hurt accuracy. (Section 5, Section 6)

- **The algorithm's partition choice is validated only visually, not quantitatively.** The core claim — that the algorithm identifies the same "uppermost" partition layer that exhaustive iterative freezing would find — is supported solely by visual inspection of three plots (Figure 3). No table reports which layer the algorithm selected vs. the optimal layer from exhaustive search, no quantitative agreement metric is provided, and no variance or reliability statistics (e.g., multiple runs) are given. Given that the exhaustive baseline itself involves multiple retraining runs whose accuracy curves are shown as individual data points with no error bars, it is impossible to assess whether the match is robust. (Section 5, Figure 3)

### Minor

- **No ablation or analysis of the algorithm's hyperparameters.** The NSGA-II uses 32 initial samples and 20 generations with no justification or sensitivity study showing how these choices affect solution quality or runtime. (Section 3.3)

- **No runtime comparison of the algorithm vs. exhaustive search.** The paper qualitatively argues the algorithm reduces computational overhead (contrasting with Dash et al.'s ~1-hour-per-eigenvector cost), but reports no actual wall-clock or FLOP cost for either the optimization or the exhaustive baseline, so the claimed efficiency gain cannot be assessed. (Section 3.3, Section 5)

- **Limited experimental scope.** The evaluation uses two model families (both relatively small: ResNet-18 and SqueezeNetV1.1) and three small image classification datasets. No experiments on larger models (e.g., ResNet-50, ViT), other modalities (text, audio), or actual edge hardware are provided. (Section 4.1, Section 5)

- **No variance or confidence intervals.** No statistical significance measures, standard deviations, or multi-run results are reported for any accuracy values. The iterative-freezing results in Figure 3 are shown as individual points without error bars. (Section 5)

### Trivial

None.

## Nice-to-Haves

- Memory footprint estimates (e.g., activation memory for backpropagation under different partition points) would substantiate the claimed efficiency benefit without requiring actual hardware deployment.
- A direct comparison with the per-layer convergence method (Li et al., 2024) or sparse-update methods (Lin et al., 2022) on accuracy-resource trade-offs would better position the contribution.
- An ablation study of the NSGA-II hyperparameters (population size, generations, crossover/mutation rates) would strengthen the method description.
- Reporting the actual bit-width assignments produced by the optimization (even for one representative scheme) would clarify the algorithm's output before the simplification to uniform int8.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *"No comparison against any other partitioning or partial-update method"* (Harsh Critic, Issue 3, partial). The paper's primary baseline — exhaustive iterative freezing — is the correct comparison for validating the algorithm's partition identification. Methods like Lin et al. (2022) and Cai et al. (2020) address a different aspect (sparse updates, bias-only updates) and are discussed as complementary in Related Work (Section 7). Demanding experimental comparison against these is scope creep for the paper's core claim.

- *"The role of 'layer robustness to quantization' is claimed but never explained"* (Harsh Critic, Section-by-Section Notes). The paper states this explicitly: "we use the robustness of each layer to quantization as an effective and expedient indicator for identifying sensitive layers" (Section 3.3). The concept is that quantization sensitivity serves as a proxy for layer importance — a standard intuition in the quantization literature.

- *"We remove the classification layers from the exploration — why?"* (Harsh Critic, Section-by-Section Notes). The paper explains this: "According to the results presented in Table 1, we remove the classification layers from the exploration" (Section 3.4). Table 1 shows that splitting at the classifier underperforms splitting at feature extractor layers. The reason is provided.

- *"Figures are low-resolution and nearly impossible to read"* and other formatting complaints. These are parser artifacts from PDF extraction, not author errors. Per instructions, formatting nitpicks are removed.

- *"Code is promised but not referenced"* (Harsh Critic, Missing Parts). The paper states code will be released and that the framework is omitted for blind review (Section 4.2). This is standard for anonymous submissions.

- *Generic "Strengthening the Paper" suggestions that are reconstituted as weaknesses.* Suggestions such as "provide a clear pseudocode" or "discuss more limitations" are moved here as they are not actual flaws but generic advice.

## Novel Insights

None beyond the paper's own contributions. The harsh critic identifies structural gaps in the method description and missing evidence, but does not contribute novel technical insights. The strength finder correctly identifies the paper's core empirical result (accuracy parity) and the motivation value of Table 1, both of which are already presented in the paper.

## Suggestions

1. **Clarify the optimization-to-partition mapping.** Either (a) constrain the NSGA-II search to only consider contiguous quantization schemes (e.g., parameterize by a single cut point *s* with all layers before *s* quantized and all after in bfloat16), or (b) explicitly describe a post-processing step that extracts a contiguous partition from the mixed-precision Pareto front and justify why this step preserves the optimality properties.

2. **Evaluate the actual mixed-precision output.** Test the mixed-precision scheme produced by the algorithm, not a uniform-int8 simplification, so that the evaluation matches what the method produces.

3. **Add a quantitative comparison table.** For each (model, dataset) pair, report: (a) the layer index selected by the algorithm, (b) the optimal layer from exhaustive search, and (c) the accuracy of the mixed-precision model at that layer. This replaces visual inspection with a proper quantitative validation.

4. **Provide at least an analytical resource estimate.** Compute the memory savings (e.g., activation memory for backpropagation under the selected partition) relative to full bfloat16 training. This paper's motivation is resource-constrained training; without any resource metric, the core claim is unsupported.

5. **Report variance.** Run the exhaustive-freezing baseline and/or the mixed-precision model with multiple seeds to establish that the accuracy match is statistically robust, not coincidental for a particular train/val split.
