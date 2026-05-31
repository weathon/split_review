## Summary

The paper proposes a joint pixel-token compression method for video large language models (VLLMs). At the pixel level, consecutive frames are pruned based on L1 pixel difference with a threshold. At the token level, tokens at corresponding positions across frames are pruned based on cosine similarity to an anchor frame, with a dynamic pruning ratio. The method is designed as a plug-and-play module and is evaluated on LLaVA-Video and Qwen2.5-VL under both training-free and training settings on MVBench, VideoMME, and NextQA benchmarks.

## Strengths

- **Important and timely problem** – Reducing the computational overhead of visual tokens in VLLMs is a significant bottleneck. The paper targets both frame-level and token-level redundancy, which is a reasonable approach.
- **Simple, intuitive design** – The pixel-level (L1 frame difference) and token-level (cosine similarity between corresponding tokens) compression strategies are easy to understand and implement. The plug-and-play claim is attractive.
- **Ablation studies** – The paper provides ablation on architecture (pixel vs. token vs. joint), compression ratio, and similarity measure, offering insights into the contribution of each component.
- **Comparative experiments** – Comparison with training-free methods (FastV, PruMerge, DyCoke) shows that the proposed method outperforms these baselines on several benchmarks.

## Weaknesses

### Fatal
None.

### Major

1. **No actual efficiency metrics reported** – Despite being an efficiency paper, the experiments only report accuracy. No measurements of wall-clock time, FLOPs, memory consumption, or throughput are provided. Without these, the claimed computational savings are unsubstantiated.
2. **Heuristic thresholds without justification** – The pixel-level threshold (0.1 for L1 pixel difference) and token-level thresholds (cosine similarity 0.5, dynamic range [0.5,0.7]) are chosen arbitrarily. There is no analysis or sensitivity study to motivate these values.
3. **Limited baseline coverage and model-agnostic claim** – The method is tested on only two VLLMs (LLaVA-Video and Qwen2.5-VL). The token-level compression relies on exact spatial correspondence of tokens across frames, which is not guaranteed in all visual encoders. The plug-and-play generality is not convincingly demonstrated.
4. **Small and inconsistent improvements** – Many gains are ≤1% and some results are identical to the baseline (e.g., Table 2: LLaVA-Video Uniform 64 vs Pixel 50% on VideoMME w/ subtitle both 69.6). No error bars or statistical significance tests are provided. The abstract claims a 0.9% gain on MVBench, but the actual observed gain in Table 1 for LLaVA-Video with joint compression is 0.7% (61.7 vs 61.0).
5. **Comparison with other training-free methods is incomplete** – The LLaVA-OV comparison (Table 1) does not include MVBench results for the baselines, making cross-benchmark comparison difficult. Compression ratios differ (75% vs 77%), so the comparison is not controlled.

### Minor
- The description of token-level pruning is somewhat confusing – the anchor frame tokens are fully retained but then also pruned intra-frame (Equation 4). The interplay between inter-frame and intra-frame pruning is not clearly explained.
- The pixel-level compression algorithm is described using a while loop, but the implementation details (normalization of pixel values, the role of threshold 0.1) are missing.
- The paper contains minor phrasing errors (e.g., "plus-and play" instead of "plug-and-play").

### Trivial
- Figure captions appear to be repeated twice in the extracted text (likely a PDF parsing artifact, but the reviewer is instructed to ignore such issues).

## Nice-to-Haves

- Measure and report actual speedup, FLOPs reduction, and memory savings across different compression ratios.
- Evaluate on additional VLLMs with different visual encoder architectures (e.g., Video-LLaVA, LLaMA-VID) to support the plug-and-play claim.
- Include statistical significance (e.g., multiple runs with standard deviation) for key results.
- Provide an analysis of failure cases where compression degrades performance.

## Novel Insights

None beyond the paper’s own contributions. The insight that jointly pruning at both pixel and token levels can preserve or even slightly improve accuracy is empirically demonstrated, but the approach is a straightforward combination of existing ideas (frame selection via pixel difference, token pruning via similarity). The observation that a substantial fraction of visual input is redundant is well known.

## Suggestions

- Add efficiency metrics (inference time, FLOPs, GPU memory) to substantiate the claimed computational savings.
- Clarify the token-level compression algorithm, especially how the anchor frame is handled (inter-frame vs. intra-frame pruning).
- Report performance with multiple random seeds and include confidence intervals.
- Provide justification or a small grid search for the chosen thresholds.

## Score and Decision

**Score:** 4.0

**Decision:** Reject

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>