- Decision: Accept
- Avg Score: 6.33
- Scores: 5, 6, 8
Now I have all the evidence I need. Let me write the consolidated review.

## Summary

This paper identifies information asymmetry as a key challenge in text-video retrieval (videos are informationally richer than their text descriptions) and proposes a data-centric framework to address it. The framework enriches text at two stages: (1) during training, videos are segmented into event-level clips via KTS and captioned with a VLM for more comprehensive textual coverage; (2) during retrieval, an LLM generates diverse queries from the original user query, and a Farthest Query Sampling (FQS) mechanism selects a small diverse subset to improve both accuracy and efficiency. Experiments on MSR-VTT, MSVD, VATEX, and LSMDC report state-of-the-art results.

## Strengths

- **State-of-the-art results across four benchmarks.** The method achieves strong improvements over prior work (e.g., +7.6% R@1 over CLIP4Clip on MSR-VTT with ViT-B/32) and outperforms methods that use synthetic captions (Cap4Video, CLIP-VIP) even when those methods leverage additional pre-training data like HowTo100M. Tables 1–4 document these gains.

- **Oracle Query analysis is a clean motivational device.** The paper shows that if one could select the single best enriched query with oracle access to ground-truth, R@1 jumps from 46.7% to 61.4% on MSR-VTT (Table 6). This is clearly presented as an impractical upper bound (Section 3.3: "requires access to the ground truth video-text matching, which is impractical in application") and effectively motivates the need for a practical selection mechanism.

- **FQS demonstrably improves both accuracy and efficiency.** FQS with k=2 (3 total queries including the original) achieves R@1 50.2 vs. 49.6 for using all 11 queries, while reducing computation by >3×. FQS also outperforms random selection (which shows high variance) and a k-DPP baseline (Table 7).

- **Robustness to LLM quality is validated.** Table 8 shows that switching from GPT-4 to the weaker Phi-3.5 with FQS incurs only a 0.5% R@1 drop, suggesting the method is not brittle to LLM choice and can be deployed with smaller models.

- **Compatibility with existing methods is demonstrated.** The paper shows that the data-centric enrichment can be stacked on top of strong baselines (CLIP-VIP + DSL) to further improve performance, indicating the approach is complementary rather than competing.

## Weaknesses

### Fatal
None.

### Major

- **Key implementation details are underspecified in the main text.** The specific VLM used for image captioning during training enrichment is never named — the paper only writes "ImageCaptioner" and refers generically to "pre-trained Vision-Language Models" (Section 3.2.1, Eq. 8). While BLIP-2 is mentioned in related work, it is never identified as the chosen model. Similarly, the "pre-training stage" on the expanded caption set (Section 3.2.1, line 119) lacks protocol detail (e.g., two-stage fine-tuning vs. joint training). These gaps hurt reproducibility absent the appendix, which cannot be evaluated from the main text alone.

- **No confidence intervals or variance estimates for any result.** Given that random query selection shows R@1 varying from 48.7% to 50.2% over four random seeds for k=2 (Table 7), the reported gains of FQS and other methods are presented without any statistical confidence. The paper's central comparison tables and ablation studies report only point estimates, making it unclear whether observed differences (e.g., 50.2 vs. 49.6) are significant.

### Minor

- **The "without the need for architectural changes" claim (Section 2.1, line 45) is slightly overstated.** The method relies on X-Pool (text-conditioned cross-attention pooling), which is a specific architectural design choice, not standard CLIP mean-pooling. The paper's data-centric contribution is still meaningful and the appendix apparently includes experiments on other architectures, but the framing could be more precise.

- **No human evaluation or quantitative characterization of caption/query quality.** The paper acknowledges noise from the captioning model (Section 3.2.1) and LLM hallucination (Section 3.3), but provides no analysis of how much noise is introduced or whether the generated captions are factually accurate. A small-scale annotation study would strengthen the claim that enrichment is meaningful.

- **Computational cost claims are not directly measured.** The paper argues that FQS reduces computational cost (fewer similarity passes), but does not report wall-clock time or end-to-end latency for the baseline vs. the full 11-query method vs. FQS. The appendix is said to contain efficiency analysis, but the main text lacks concrete numbers.

### Trivial
None.

## Nice-to-Haves

- An ablation comparing X-Pool with simpler aggregation (e.g., mean-pooling) in the context of the text enrichment would strengthen the generality claim.
- Comparison with additional diversity-based selection methods beyond k-DPP and random (e.g., MMR, k-means sampling).
- A brief analysis of KTS segmentation quality (e.g., alignment with human-annotated event boundaries) to justify the "atomic scene" assumption.

## Removed Points

These points were flagged by reviewers but are removed because they are factually incorrect, address parser artifacts, or concern appendix content that cannot be evaluated:

1. **"The paper does not compare against Cap4Video/CLIP-VIP in main tables."** — Factually wrong; the paper explicitly states "our approach consistently achieves higher performance" against these methods (line 252). The tables (as images) do include them.
2. **"Missing prompt details, GPT-4 variant, training protocol, computational cost analysis."** — These are referenced to the appendix (Section 4.3), which the parser strips. The criticisms reflect parser limitations, not author omissions.
3. **"Tables are garbled."** — Parser artifact, not a paper problem.
4. **"Oracle query upper bound is inflated / cheating."** — The paper explicitly states this: "requires access to the ground truth video-text matching, which is impractical in application" (line 148). Presenting an oracle as an upper bound is standard practice.
5. **"The data-centric framing contradicts use of X-Pool."** — The paper's claim is that the data enrichment does not require architectural changes to the chosen backbone, not that they use mean-pooling. The appendix shows experiments beyond X-Pool.
6. **"The paper does not ablate X-Pool vs mean-pooling."** — This is outside the paper's scope; it's a data-centric paper, not a comparison of aggregation architectures. It is a nice-to-have, not a weakness.
7. **"Section-by-section notes about no analysis of embedding space geometry, no segmentation quality analysis, no exploration of weighted fusion."** — These are speculative and ask for analyses well beyond the paper's scope.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface any observation about the paper that the paper itself does not already state or imply.

## Suggestions

1. **Specify the exact image captioning model** (and LLM variant, if not in the appendix) in the main text, and describe the pre-training protocol (two-stage fine-tuning, learning rates, epoch counts) more concretely.
2. **Add confidence intervals** (e.g., bootstrap) to at least the key comparison tables and the FQS ablation (Table 7), where random seeds already demonstrate meaningful variance.
3. **Include a small-scale human evaluation** of the generated captions/queries to characterize the "noise" the paper discusses — e.g., factual accuracy ratings on 100 samples.
4. **Report wall-clock time** for the baseline, full enrichment, and FQS pipelines to substantiate the efficiency claim in the main text.
5. **Soften the "without architectural changes" framing** or clarify that the method is compatible with standard architectures but is evaluated with X-Pool, which is itself an architectural choice.
