## Summary
The paper introduces a joint Pixel-Token (P-T) compression strategy to improve the efficiency of Video Large Language Models (VLLMs). The method operates in two stages: (1) Pixel-level compression, which uses $L_1$ distance between consecutive frames to prune visually redundant frames before encoding, and (2) Token-level compression, which uses cosine similarity to prune redundant visual tokens both across frames (inter-frame) and within the same frame (intra-frame). The authors demonstrate that their "plug-and-play" module can reduce visual tokens by over 50% while maintaining or even slightly improving performance on benchmarks like MVBench, VideoMME, and NextQA using LLaVA-Video and Qwen2.5-VL baselines.

## Strengths
- **Comprehensive Compression Pipeline:** Unlike many existing works that focus solely on frame sampling or token pruning, this paper addresses redundancy at both the raw pixel level and the high-level feature (token) level.
- **Strong Empirical Results:** The method demonstrates a "less is more" effect, where pruning redundant information leads to performance gains (e.g., +0.9% on MVBench with >50% tokens removed). This suggests the compression effectively acts as a denoiser for the LLM.
- **Versatility:** The approach is validated in both training-free (inference-only) and training-based (fine-tuning) scenarios across two state-of-the-art VLLM architectures (LLaVA-Video and Qwen2.5-VL).
- **Ablation Rigor:** The paper provides clear comparisons of different similarity metrics (Cosine vs. $L_1$ vs. Attention) and analyzes the impact of various compression ratios, providing useful heuristics for practitioners.

## Weaknesses
### Major
- **Novelty of Components:** The individual components of the strategy are relatively standard. Pixel-wise difference for frame selection is a classic video processing technique, and similarity-based token pruning/merging has been explored in works like ToMe (Bolya et al.) and FastV. While the *joint* application is beneficial, the technical novelty of the underlying algorithms is incremental.
- **Computational Overhead of Compression:** The paper emphasizes efficiency but does not provide a detailed analysis of the wall-clock time or FLOPs required to compute the pixel-wise differences and the token-wise cosine similarity matrices. If the cost of calculating similarities for thousands of tokens is high, it might offset the savings gained from reducing the LLM's context window.

### Minor
- **Threshold Sensitivity:** The pixel-level compression relies on a predefined threshold $\tau$. The paper does not sufficiently discuss how sensitive the performance is to this threshold across different video domains (e.g., high-motion sports vs. static talking heads).
- **Anchor Frame Dependency:** In token-level compression, the first frame of a window is used as an anchor. If the first frame is an outlier or contains motion blur, it might lead to suboptimal pruning of the subsequent frames in that window.

## Nice-to-Haves
- A visualization of which tokens are pruned (e.g., heatmaps) would help confirm if the model is correctly identifying "background" or "static" tokens versus "action" tokens.
- Comparison of wall-clock inference latency (ms/video) to quantify the actual speedup on standard hardware.

## Novel Insights
The most significant insight is the empirical validation that joint compression at different granularities (pixel and token) is complementary rather than redundant. The ablation study in Table 3 shows that the joint strategy outperforms either pixel-only or token-only pruning at the same compression ratio. This suggests that pixel-level pruning handles temporal redundancy that the visual encoder might still pass through, while token-level pruning handles spatial and semantic redundancy that raw pixel differences cannot capture.

## Suggestions
- Include a table or graph showing the trade-off between the time spent on the compression computation itself versus the time saved during the LLM forward pass.
- Test the robustness of the pixel-level threshold $\tau$ across different video types to see if a dynamic threshold (based on global video variance) would be more effective than a fixed one.

## Score and Decision
The paper presents a well-executed empirical study on a highly relevant problem for the ICLR community. While the individual techniques are not groundbreaking, the joint framework is effective, easy to implement, and supported by solid experimental evidence across multiple benchmarks and models.

MY FINAL SCORE: 6.5
MY FINAL DECISION: Accept

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: Accept