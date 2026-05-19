- Decision: Reject
- Avg Score: 5.25
- Scores: 6, 5, 5, 5
Now I have a thorough understanding of the paper. Let me produce the consolidated review.

## Summary

This paper proposes INTP, a training-free method to extend Video-LLMs from processing 8 frames to 32 frames. It combines three components: (1) a video token rearrangement scheme that splits a long video into subsequences, processes each through the frozen encoder, and interleaves tokens by absolute frame position; (2) NTK-aware RoPE interpolation to extend the LLM context window; and (3) post-training KV-cache quantization (INT2) to manage memory. The method is evaluated on Video-LLaVA (Vicuna-7B) across five VQA benchmarks, showing consistent but modest gains (+1.3 to +3.6 accuracy on open-ended VQA, +1.6 to +4.4 on multiple-choice sub-scores).

## Strengths

- **Training-free 4× frame increase with consistent empirical gains**: The method enables a pre-trained Video-LLaVA to jump from 8 frames to 32 frames without any training. Tables 2 and 3 show improvements on all five benchmarks: MSVD-QA (+1.3), MSRVTT-QA (+2.2), ActivityNet-QA (+3.6), NExT-QA average (+2.2), and EgoSchema (+1.6). The gains, while modest, are directionally consistent.

- **Novel token rearrangement for frozen encoders**: Section 3.2 presents a clean technique to bypass the fixed encoder/projector limitation: splitting the long video into m subsequences (each with N frames spaced at stride m), encoding each separately, then interleaving tokens by absolute frame position (Fig. 2). This is the paper's primary algorithmic contribution and is clearly described.

- **First application of NTK-aware RoPE scaling to Video-LLMs**: While the scaling technique itself is adapted from prior LLM work (Chen et al., Liu et al.), Section 3.3 represents the first application to Video-LLMs. The adaptation is straightforward but non-trivial given the multimodal context, and it enables the LLM backbone to handle the increased visual token count.

- **Efficiency analysis with concrete memory/latency numbers**: Table 1 provides a clear breakdown of computation costs, showing that KV-cache storage is the main bottleneck. The INT2 quantization reduces KV-cache memory from 4.3 GB to 0.5 GB for 32 frames and from 8.6 GB to 1.1 GB for 64 frames, making deployment more practical.

- **Honest ablation and limitation disclosure**: Table 4 shows a clean progression (8→16→32 frames improves, 64 frames degrades) and the paper explicitly attributes the 64-frame collapse to NTK scaling limitations rather than overclaiming. This transparency strengthens the credibility of the 32-frame results.

## Weaknesses

### Fatal

None.

### Major

- **Token rearrangement vs. simpler alternatives is not empirically validated**: The paper claims its interleaving strategy preserves temporal consistency better than naive chunk concatenation (Section 3.2, lines 118–120), but provides no direct comparison against this simpler baseline. The claim rests on a verbal argument about "inconsistency between the tokens of the N-th frame and those of the (N+1)-th frame." Without measuring feature similarity, temporal coherence, or at least VQA accuracy of the concatenation baseline at the same frame count, the reader cannot assess whether the rearrangement's complexity is justified. Moreover, the ablation (Table 3) shows mixed results at 8 frames (same frame count as baseline): INTp underperforms on MSVD-QA (69.5 vs. 70.7) and MSRVTT-QA (58.2 vs. 59.2) but dramatically outperforms on ActivityNet-QA (55.3 vs. 45.3). This inconsistent pattern suggests the rearrangement's effect is dataset-dependent and poorly understood.

- **KV-cache quantization is presented without accuracy evaluation**: The paper introduces INT2 quantization as a key contribution (Section 3.4, highlighted in abstract and conclusion) but never measures whether it affects VQA accuracy. Table 1 reports only memory and latency. Without verifying that quantized predictions match FP16 predictions, the reader cannot evaluate the accuracy-efficiency trade-off. The related work's claim that "ZipCache achieves negligible performance degradation" is not a substitute for direct evaluation on this specific model and task. This omission makes the quantization section a standalone efficiency analysis rather than an integrated part of the contribution.

### Minor

- **No statistical significance or variance reported**: Given the modest per-benchmark gains (+1.3 to +3.6 accuracy), single-run results without confidence intervals or standard deviations leave open the question of whether improvements are statistically reliable.

- **No analysis of encoder-side computational overhead**: The method requires m encoder passes (e.g., 4× for 32 frames), multiplying encoder computation. The paper focuses entirely on LLM-side KV-cache costs (Section 3.4) but does not account for the encoder's repeated inference, which is a practical deployment consideration for video processing pipelines.

- **No comparison against training-based long-video methods**: While the paper correctly positions itself as training-free, contextualizing against Chat-UniVi or LLaMA-VID (discussed in related work, lines 65–67) on the same benchmarks would help readers assess the practical gap between training-free and training-based approaches.

- **Hyperparameter m (number of subsequences) is not ablated**: The paper uses m = number-of-frames / N implicitly (N=8, so m=2 for 16 frames, m=4 for 32 frames) but never discusses sensitivity to this choice or whether alternative partitioning strategies could improve results.

- **Qualitative examples are illustrative but cherry-picked**: Figure 3 shows two hand-picked examples where INTP-Video-LLaVA reduces hallucinations. While convincing as demonstrations, a systematic evaluation (e.g., automatic hallucination metrics or human evaluation on a random sample) would strengthen the claim.

### Trivial

- None that are genuine paper problems (formatting artifacts removed per instructions).

## Nice-to-Haves

- Compare token rearrangement against the naive "chunk concatenation" baseline at matched frame counts to isolate its contribution.
- Evaluate VQA accuracy with and without INT2 quantization (at 16, 32, and 64 frames) to validate the KV-cache compression claim.
- Report variance or confidence intervals (e.g., 3 runs with different random frame selections).
- Compare with alternative RoPE scaling strategies (YaRN, linear scaling) to understand why NTK fails at 64 frames and whether alternatives could push further.
- Ablate the choice of m (number of subsequences) to assess sensitivity.

## Removed Points

These points were surfaced by reviewers but are removed from the main evaluation for the reasons stated; they are provided here for completeness but should be treated with caution.

- **"Token rearrangement may undermine temporal consistency because the encoder was pre-trained on consecutive frames"** (Harsh Critic, Critical Issue 1): This is speculative. Many video encoders are trained with various frame sampling strategies and may handle non-consecutive frames without issue. The paper's own ablation shows a +10.0 point gain on ActivityNet-QA at 8 frames (INTp 55.3 vs. baseline 45.3), which directly contradicts the claim that rearrangement "harms quality." The speculation about "artifacts masked by more frames" is not supported by the evidence on the page.

- **"Gains are marginal and inconsistent"** (Harsh Critic, Critical Issue 3): The gains are modest but consistently positive across all five benchmarks. On MSRVTT-QA, the "Score" metric staying at 3.5 is not a regression — it is the same score. The claim of inconsistency is not supported.

- **"The KV-cache compression should achieve negligible performance degradation"** (paraphrasing): The paper does not claim their quantization achieves negligible degradation; they cite prior work (ZipCache) that does. The weakness of not evaluating accuracy is kept; the additional claim about unsubstantiated performance claims is removed.

- **"Related works discussion of Chat-UniVi and LLaMA-VID is superficial"**: The related work section provides a brief, correct summary of these methods and notes they rely on training. This is appropriate for a related work section.

- **"Missing figure/table references" and "typographical issues"**: These are parser artifacts from PDF extraction, not errors in the original submission.

- **"Missing appendix, missing proofs"**: The appendix is stripped by the parser; the original submission contains it.

- **Strength Finder's generic statements** (e.g., "this paper addressed an important problem"): These are removed as they lack specific evidence anchored in the paper's content.

- **"No exploration of failure cases"**: The paper discusses the 64-frame collapse, which is the primary failure case. A broader discussion would be nice but is not a missing essential.

## Novel Insights

The reviews converge on the key tension in this paper: the token rearrangement is the most novel component but also the least validated. The harsh critic correctly identifies that the interleaving strategy feeds the encoder a different frame distribution (non-consecutive frames) than its training distribution, but then over-extrapolates this into a fatal structural flaw — ignoring the ActivityNet-QA result that shows the rearrangement can substantially help even at 8 frames. The more measured observation is that the method's success depends on a poorly understood interaction between frame sampling strategy, encoder robustness, and dataset characteristics. The gains at 32 frames are real but modest, and the 64-frame collapse suggests the NTK scaling hits a hard ceiling. An underexplored opportunity is whether a different RoPE scaling strategy (e.g., YaRN) could push beyond 32 frames, or whether the rearrangement could be combined with token compression to handle more frames within the same token budget.

## Suggestions

- **Provide a direct head-to-head comparison** between the proposed interleaved token rearrangement and the naive "chunk concatenation" baseline at matched frame counts (e.g., 16 and 32 frames) to isolate the rearrangement's value.
- **Add a small experiment table** showing VQA accuracy with and without INT2 quantization for at least one frame count (e.g., 32 frames) to validate that the KV-cache compression preserves accuracy.
- **Report results over multiple runs** (e.g., 3 different frame selections) with mean and standard deviation to establish statistical reliability.
- **Include an additional comparison** with a training-based long-video method (e.g., Chat-UniVi or LLaMA-VID) on at least one shared benchmark to contextualize the training-free gap.
- **Briefly discuss the encoder-side cost** (number of forward passes multiplied by m) in the efficiency analysis to give a complete picture of deployment trade-offs.
