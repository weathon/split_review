## Summary

This paper proposes a mixed-precision partitioning framework for on-device transfer learning. The core idea is to use multi-objective optimization (NSGA-II) to analyze layer-level quantization robustness on the pre-trained model (ImageNet), then derive a partition point where bottom layers are frozen-and-quantized (int8) while upper layers are retrained in bfloat16. Experiments on ResNet-18 and SqueezeNetV1.1 over Flowers-102, STL-10, and OxfordIIITPet are presented, with the claim that the mixed-precision model matches full bfloat16 accuracy.

## Strengths

1. **Explicitly contrasts per-layer robustness analysis with expensive per-parameter sensitivity methods, providing a clear efficiency argument.** Section 3.3 (lines 90–91) benchmarks against Dash et al. (2022), which requires "approximately an hour per eigenvector on two NVIDIA GTX1080 Ti GPUs for a ResNet-18." The proposed approach replaces per-parameter sensitivity with layer-level quantization robustness as a proxy and combines it with NSGA-II over 20 generations (32 initial samples), achieving O(N) complexity. This is a concrete claimed efficiency improvement over a prior method.

2. **Empirically demonstrates that splitting within the feature extractor (not just at the classifier head) consistently yields higher accuracy than classifier-only transfer learning.** Figure 3 (lines 165–166) shows dotted blue lines indicating the accuracy if split before the classifier. In all 6 model–dataset combinations, retraining from a feature-extractor layer produces higher accuracy. This provides a useful, targeted challenge to the common practice of freezing all feature-extractor layers (e.g., Chiang et al., 2023).

3. **Visual evidence that the mixed-precision partitioned model (int8 bottom, bfloat16 top) achieves accuracy comparable to the full bfloat16 baseline.** Figure 3 shows green dots (mixed-precision) closely overlaying orange dots (full bfloat16) across all conditions. This suggests that quantizing frozen bottom layers to int8 does not cause accuracy degradation relative to the bfloat16 baseline.

4. **Commitment to open-source release.** The paper states that both the framework and code will be made publicly available (lines 24, 138), supporting reproducibility.

## Weaknesses

### Major

1. **The algorithm's output is never quantitatively compared to the brute-force optimum, despite the paper claiming they match.** The central contribution is the partitioning algorithm. Section 4.2 describes a validation procedure where the brute-force result (iteratively freezing layers one-by-one and retraining subsequent layers) and the algorithm's output are obtained "in parallel," and line 147 states the algorithm found "the same layer." However, Section 5 presents only visual plots (Figure 3) with a single red vertical line per plot. No table or text reports: (a) which layer index each method selected for each model–dataset pair, (b) whether the selections match, or (c) the accuracy gap if they diverge. Without this comparison, the paper does not demonstrate that the algorithm works — it demonstrates only that *some* partition (found by exhaustive search) yields good accuracy with int8 quantization. This is a structurally different claim from validating the proposed algorithm.

2. **No numerical accuracy values are reported anywhere; all quantitative evidence is visual.** Section 5 relies entirely on Figure 3 (embedded images). No accuracy numbers, standard deviations, or tables appear in the text. Assertions such as "without losing accuracy compared to the baseline" (lines 167–168) cannot be verified — the reader cannot tell whether the gap is 0.1% or 1% or whether it varies across datasets. This is a critical evidential and reproducibility concern.

3. **Zero on-device measurements despite "on-device" being the paper's central framing.** The abstract, introduction, and motivation repeatedly invoke the constraints of embedded devices (NVIDIA Jetson Nano, Raspberry Pi 4, limited memory, energy efficiency, backpropagation memory footprint). Yet the paper reports no measurements of memory usage, latency, power consumption, or energy efficiency on any actual device or even simulated proxy. The hardware platform used for experiments is never stated. The evaluation delivers only accuracy comparisons, not the resource measurements needed to substantiate the "on-device" claim.

4. **The mapping from the NSGA-II quantization scheme to a single contiguous partition point is unexplained.** The NSGA-II search (Section 3.3, Definitions 5–6) produces a quantization scheme assigning individual bit-widths (4, 6, 8, 16-bit integer) to each layer. Definition 7 selects one scheme minimizing total bit-width subject to accuracy constraint. Definition 8 then defines a contiguous split into quantized bottom layers (Ω) and bfloat16 upper layers (Θ). The paper never explains how a potentially non-contiguous per-layer quantization scheme is reduced to a single contiguous partition point. The "sensitivity factor" mentioned at line 90 as the basis for the search-space reduction is never formally defined or computed.

5. **No experimental comparison against any baseline method from the related work.** Section 7 discusses classifier-only fine-tuning (Chiang et al., 2023), dynamic layer freezing (Li et al., 2024; Wang et al., 2023), and partial-update methods (Lin et al., 2022; Cai et al., 2020). None of these are compared experimentally. The related-work discussion is aspirational rather than evidence-based.

### Minor

6. **Training hyperparameters and experimental configuration are not provided.** Line 138 reads: "The details, such as learning rates, number of epochs, etc." with no values following. This prevents reproducibility. No optimizer, learning rate schedule, batch size, or number of training epochs is specified.

7. **The core assumption linking quantization robustness on ImageNet to optimal TL partitioning on a different target dataset is unstated and unvalidated.** The algorithm analyzes the pre-trained model on ImageNet to determine where to partition for TL on Flowers-102, STL-10, or OxfordIIITPet. This assumes that layers robust to quantization on ImageNet are the same layers that can be safely frozen and quantized when fine-tuning on a different dataset. The paper provides no theoretical justification and does not test this assumption. (Note: the brute-force validation in Section 5 bypasses this assumption by measuring TL accuracy directly, so it does not validate the algorithm's design premise.)

### Trivial

8. **Definition 1 ("A layer l is a layer of a DNN with bfloat16 computational precision") is a vacuous formal definition.** It states an assumption rather than defining a concept. This does not affect technical content but detracts from the claimed formality.

## Nice-to-Haves

- An ablation separating the effect of (a) choosing a deeper partition point from (b) using int8 quantization for frozen layers would clarify each factor's contribution.
- Estimated memory savings (e.g., MAC counts for backpropagation, peak memory at the chosen partition vs. full fine-tuning) would substantiate the on-device claims even without physical deployment.
- Reporting the computational cost of the NSGA-II search (wall-clock time, number of forward passes) would support the efficiency claim.
- A comparison where the same frozen layers are kept in bfloat16 (without quantization) would isolate the benefit of quantization vs. the benefit of deeper partitioning.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Table 1 is referenced but not present in the text (only an image placeholder)"** — This is a PDF-parser artifact. The original submission contains Table 1 as an embedded image. Not a paper weakness.
- **"The second motivation contradicts the later finding that the optimal partition point is within the feature extractor"** — This misreads the paper. Line 32 says "bottom layers cannot be considered viable candidates for use as a partitioning point," meaning the partition cannot be placed at the very first layers (which would mean retraining almost the entire network). This does not conflict with finding the optimal partition somewhere in the feature extractor.
- **"Definition 6 states two objectives that are partly redundant ('maximize the number of integer quantized layers' and 'minimize q-bit integer computational precision' are the same thing)"** — These are related but not identical (e.g., quantizing all layers to 16-bit vs. quantizing a subset to 4-bit). This is not a substantive weakness.
- **"Formal problem definitions provide a rigorous framework" (from Strength Finder)** — Definition 1 is vacuous, and the framework is not notably more rigorous than typical method descriptions. This claimed strength is exaggerated and removed.
- **Criticisms about missing appendix content** — The parser strips appendices from all papers; these sections exist in the original submission.

## Novel Insights

None beyond the paper's own contributions. The reviews identify evidential gaps rather than providing novel synthesis.

## Suggestions

1. Add a table comparing the algorithm's predicted partition layer to the brute-force optimum for each model–dataset pair, reporting the layer index and the accuracy of both choices.
2. Report numerical top-1 accuracy values for all configurations (full bfloat16, mixed-precision, classifier-only split) with standard deviations or confidence intervals.
3. Provide on-device resource measurements (peak memory for backpropagation, number of trainable parameters, estimated latency) or add simulated estimates to support the on-device claims.
4. Specify training hyperparameters (learning rate, optimizer, batch size, epochs).
5. Compare experimentally against at least one baseline from the related work (e.g., classifier-only fine-tuning, dynamic freezing).
6. Clarify the mapping from the NSGA-II quantization scheme to the contiguous partition point, including how the "sensitivity factor" is computed and used.

## Score and Decision

The paper addresses a well-motivated and practically relevant problem. However, the central algorithmic contribution is not validated: the paper claims the algorithm matches brute-force but provides no quantitative comparison. The evaluation relies entirely on visual evidence with no numerical results, omits the on-device measurements implied by the title and framing, and compares against no baselines from the large related-work section. These are not minor omissions — they are evidential gaps that prevent the paper from supporting its core claims. While the approach is plausible, the evidence as presented does not meet the standard required for a top-tier venue.

MY FINAL SCORE: <score>2.5</score>
MY FINAL DECISION: <decision>Reject</decision>