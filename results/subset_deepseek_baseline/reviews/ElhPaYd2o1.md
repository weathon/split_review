## Summary

This paper proposes a joint pixel-token compression strategy for Video Large Language Models (VLLMs) that reduces computational costs by pruning redundant visual information at two levels: pixel-level frame selection based on inter-frame L1 distance, and token-level pruning based on cosine similarity between corresponding tokens across frames. The method is designed as a plug-and-play module and is evaluated on LLaVA-Video and Qwen2.5-VL under both training-free and fine-tuning settings across MVBench, VideoMME, and NextQA benchmarks.

## Strengths

- **Practical problem with clear motivation**: The paper addresses a genuine and important bottleneck in VLLMs—the computational overhead from processing many frames and tokens. The two-stage compression (pixel then token) is a natural and well-motivated decomposition of the redundancy problem.
- **Comprehensive experimental setup**: The authors evaluate under both training-free and training-based settings, across two strong baseline models (LLaVA-Video and Qwen2.5-VL), and on three diverse benchmarks. Ablation studies on compression ratio, similarity measure, and architecture components provide useful insights.
- **Plug-and-play design**: The method requires no architectural changes to the base VLLM, making it practical and easy to adopt. The training-free results are particularly valuable for deployment scenarios where fine-tuning is infeasible.
- **Consistent improvements despite aggressive pruning**: The method achieves performance gains (e.g., 0.9% on MVBench) even after discarding >50% of visual tokens, which is a non-trivial and practically useful result.

## Weaknesses

### Fatal
None.

### Major
- **Lack of comparison to state-of-the-art compression methods**: The training-free comparison in Table 1 only includes FastV, PruMerge, and DyCoke on LLaVA-OV 7B. Missing comparisons to more recent or stronger baselines like LongVU, Video-XL-Pro, or HiCom (all cited in related work) significantly weakens the claim of effectiveness. The paper does not explain why these were excluded.
- **No latency or throughput measurements**: The paper claims to reduce "computational costs" and "computational overhead" but provides no actual runtime measurements, FLOPs counts, or memory usage data. The only reported metric is accuracy. Without efficiency metrics, the core claim of the paper is unsubstantiated.
- **Inconsistent and potentially misleading reporting**: In Table 1, the "Pixel (50%)" and "Token (50%)" rows for LLaVA-Video show identical numbers to the training-based Table 2 for the same methods (e.g., VideoMME w/o subtitle: 61.0 for both). This suggests the training-free and training-based results may be identical or copied, which is suspicious. The paper should clarify whether these are the same experiments or different.
- **Missing details on the training-based setup**: The paper states "a single epoch of fine-tuning" but does not specify learning rate, batch size, optimizer, or whether the compression modules themselves are trained or only the base model. The training data mixture (120K videos from multiple sources) is described but not analyzed for potential distribution shift or overfitting.

### Minor
- **Threshold selection is not justified**: The pixel-level threshold τ=0.1 and token-level threshold 0.5 are given without any sensitivity analysis or justification. The dynamic pruning range [0.5, 0.7] is similarly arbitrary.
- **The anchor frame token pruning (Eq. 3-4) is under-explained**: The paper describes pruning tokens within the anchor frame based on intra-frame redundancy, but the interaction between this intra-frame pruning and the inter-frame pruning is not clearly described. It is unclear whether both are applied simultaneously or sequentially.
- **Algorithm 1 is incomplete**: The algorithm shows iterative frame pruning but does not specify the distance function d(·,·) used. The text mentions L1 distance, but the algorithm pseudocode is generic.

### Trivial
- The paper uses "plus-and play" instead of "plug-and-play" in multiple places (abstract, Section 3.1, conclusion). This appears to be a typo.
- Figure 2 is referenced but the caption is duplicated and the layout is difficult to parse.

## Nice-to-Haves

- Reporting wall-clock time or FLOPs for the compressed vs. uncompressed models would greatly strengthen the practical claims.
- A comparison to random frame/token dropping would help isolate the benefit of the proposed similarity-based selection from mere subsampling.
- Analysis of which types of videos (e.g., static scenes vs. fast action) benefit most from the compression would provide deeper insight.

## Novel Insights

The paper's key insight—that redundancy exists at both pixel and token levels and that joint compression can be more effective than either alone—is not entirely novel but is practically validated. The more interesting finding is that aggressive pruning (75% removal) can sometimes improve performance, suggesting that VLLMs may be distracted by redundant visual information. This echoes findings in image-based VLMs but is less explored in video. However, the paper does not deeply analyze *why* this happens (e.g., does pruning reduce attention dilution? does it remove misleading tokens?). The insight remains at the observational level.

## Suggestions

1. **Add efficiency metrics**: Report inference time (or throughput) and peak memory usage for the compressed vs. uncompressed models. Without these, the paper's central claim is unverifiable.
2. **Expand baseline comparisons**: Include LongVU, Video-XL-Pro, or HiCom in the training-free comparison. If they are not directly comparable, explain why.
3. **Clarify the training-based results**: Explain whether the numbers in Table 2 are from the same experiments as Table 1 or different. If different, provide the training-free results for the same models in a consistent format.
4. **Provide threshold sensitivity analysis**: Show how performance varies with τ (pixel) and the token-level threshold across a range of values.
5. **Describe the intra-frame pruning more clearly**: Explain whether Eq. 3-4 is applied to all frames or only the anchor, and how it interacts with the inter-frame pruning.

## Score and Decision

The paper addresses a relevant problem and provides a simple, practical solution with reasonable empirical support. However, the lack of efficiency metrics and the incomplete comparison to state-of-the-art methods are significant gaps that prevent a strong acceptance. The suspicious overlap between training-free and training-based results also raises concerns. The paper has merit but needs substantial revision to fully substantiate its claims.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>