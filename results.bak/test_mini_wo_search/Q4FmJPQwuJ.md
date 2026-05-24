Now I have all the information I need. Let me write the consolidated review.

## Summary

This paper proposes CrossTVR, a two-stage text-video retrieval system. Stage 1 uses an off-the-shelf cosine-similarity retriever. Stage 2 introduces a multi-grained re-ranker that computes cross-attention between text and video tokens at both the frame (spatial) level and the video (temporal) level, while keeping the vision encoder frozen. The frozen-encoder design allows scaling to very large backbones (e.g., ViT-G) with modest memory cost. The method is evaluated on five standard benchmarks (MSRVTT, ActivityNet, LSMDC, DiDeMo, VATEX) with two base retrievers (TS2Net, CLIP-ViP), reporting consistent improvements.

## Strengths

1. **Multi-grained cross-attention design is validated by careful ablation.** Table 6 (described in text at lines 164, 188) shows that adding video-level cross-attention yields +1.4% T2V R@1, hierarchical addition of frame-level attention yields another +2.6%, and parameter sharing adds +0.2% — totaling a 3.0% improvement. This directly confirms the paper's central claim that both frame-level (spatial) and video-level (temporal) cross-attention are necessary and complementary.

2. **Frozen encoder strategy provides a genuine practical scalability advantage.** Table 9 (described at line 192) shows that moving from ViT-B to ViT-G increases GPU memory by only 22% for CrossTVR, versus >10× for end-to-end finetuning (CLIP4Clip). With ViT-G, CrossTVR reduces memory by 91% and training time by 58% compared to the finetuned baseline, while still improving R@1 by 7.0% on MSRVTT. This is a concrete, well-documented practical benefit.

3. **Consistent gains across five diverse benchmarks and two base retrievers.** Improvements are reported on every dataset (e.g., +8.0% T2V R@1 on ActivityNet with TS2Net, +1.4–5.3% on other datasets), demonstrating that the re-ranker generalizes beyond a single dataset or base method rather than exploiting dataset-specific artifacts.

4. **Plug-and-play compatibility with four different first-stage methods.** Table 8 (described at line 190) shows that CrossTVR boosts CLIP4Clip by +2.5%, X-pool by +1.2%, TS2Net by +3.0%, and CLIP-ViP by +1.8% T2V R@1 on MSRVTT, supporting the claim that it is a general re-ranking module.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Missing architectural hyperparameters (L and N_Q).** The method description (Equations at line 66–69) defines L (number of cross-attention layers) and N_Q (number of learnable query embeddings), and the frame-text attention module (line 63) relies on these. The implementation details (line 120) specify M=4, K=15, batch size, learning rate, and optimizer, but never state the values of L or N_Q. Since the cross-attention module is the paper's core contribution, omitting these parameters hinders reproducibility. These are easily stated values (likely L ∈ {1,2}, N_Q ∈ {4,8,16}) and should be provided.

2. **Hard negative sampling distribution is ambiguous.** The training description (line 91) says negatives are sampled "following the contrastive similarity distribution" but does not specify whether this distribution comes from stage 1's cosine similarity scores or from the current model's cross-attention scores during stage 2 training. The paper cites ALBEF, which uses the model's own scores, but this should be explicitly stated to avoid ambiguity.

3. **No variance or confidence intervals reported.** Given that some improvements are modest (e.g., +1.4% R@1 on LSMDC with CLIP-ViP), it would strengthen the evidence to know whether these gains are stable across multiple runs. This is standard practice for re-ranking methods and would take little space.

### Trivial

1. **Notation inconsistency.** The equation defining the frame-text attention output (line 66) uses N_Q as the count of learnable queries, but the accompanying text (line 69) writes "selects and averages the first N tokens" — where N is overloaded (previously denoting vision tokens per frame, line 19). The text should read N_Q for clarity.

## Nice-to-Haves

- A breakdown of inference time into (a) first-stage cosine similarity, (b) feature extraction for top-K candidates, (c) frame-level cross-attention, and (d) video-level cross-attention would make the efficiency claim more informative and easier to verify.
- A brief analysis of sensitivity to K (number of re-ranked candidates) and M (token selector count) would strengthen the robustness claims.

## Removed Points

These points are flagged for removal; treat them with caution.

- **Inference speed implausibility (from Harsh Critic):** The critic asserts that the Table 8 inference times (stated as 0.08 ms for TS2Net and 0.09 ms for CrossTVR indexing 1000 videos) are "implausible" and that 0.08 ms for 1000 cosine similarities is unrealistic. **Reason for removal:** The specific numbers are embedded in a rasterized table image and cannot be independently verified from the available text. More importantly, even if the numbers are as claimed, they are actually plausible on an A100 GPU — a batched [1×512]×[512×1000] cosine similarity on an A100 (~312 TFLOPS) can complete in microseconds, and the re-ranker only processes K=15 of the 1000 videos. The paper's claim (line 190) is modest ("virtually unchanged"), and the critic's objection rests on a miscalculation of GPU throughput. This criticism is removed as it does not hold up under scrutiny.

## Novel Insights

The multi-reviewer analysis reveals a productive tension: both reviewers agree on the paper's core strengths (validated ablation, frozen-encoder scalability, consistent gains) but the Harsh Critic's most prominent issue (implausible inference speed) dissolves under quantitative scrutiny. The real gap is not implausibility but incompleteness — missing hyperparameter values (L, N_Q). This suggests that the paper is fundamentally sound but should prioritize filling in architectural specifications over defending its efficiency claims.

## Suggestions

1. **Specify L and N_Q explicitly** in the Implementation Details paragraph (Section 4.1). If these values differ per dataset, provide a table.
2. **Clarify the hard negative sampling distribution:** state explicitly whether it uses stage-1 cosine similarity scores or the re-ranker's own scores during training.
3. **Add error bars** (at least 3 runs) for the main results, especially where gains are modest, to demonstrate stability.
4. **Fix the notation** in line 69: change "first N tokens" to "first N_Q tokens" to avoid confusion with the vision-token count N.

## Score and Decision

This paper makes a solid contribution to text-video retrieval. The multi-grained cross-attention re-ranker is well-motivated, the ablation studies convincingly validate the design choices, and the frozen-encoder strategy offers a real practical advantage for scaling. The experimental evaluation is extensive (five datasets, two base retrievers). The identified weaknesses (missing hyperparameters, notational ambiguities) are addressable and do not threaten the core claims. No fatal or major flaws were found upon verification against the paper text.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>