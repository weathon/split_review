I have now verified all the key claims in the paper against the reviewer's comments. Let me construct the final review.

---

## Summary

EffoVPR introduces an effective approach to leverage DINOv2 for Visual Place Recognition (VPR) by exploiting features from intermediate self-attention layers. The method has two key components: (1) a global stage that uses the [CLS] token trained with classification loss (CosFace) to produce compact global descriptors, eliminating the need for external pooling like NetVLAD or GeM; and (2) a re-ranking stage that uses internal Value features filtered by attention scores and mutual nearest neighbor matching. The approach achieves state-of-the-art results across a large number of VPR benchmarks (including challenging day/night, seasonal, and occlusion scenarios) with remarkably compact feature dimensions, and also demonstrates strong zero-shot performance surpassing prior zero-shot methods by large margins.

## Strengths

1. **State-of-the-art performance on multiple challenging benchmarks** — Tables 3 and 4 show large margins over prior methods on datasets with severe appearance change: e.g., +4.3% R@1 on Nordland over CricaVPR, +15% on SF-XL Night over SALAD, +7.9% on SF-Occlusion over SALAD. These results directly support the claim of strong robustness and generalization.

2. **Zero-shot method significantly outperforms prior zero-shot approaches** — Table 1 shows EffoVPR-ZS surpasses AnyLoc and vanilla DINOv2 on all four benchmarks, with dramatic gains on challenging sets: +30.2 R@1 on Nordland over AnyLoc, +28.6 on Tokyo24/7. This validates the claim that internal self-attention features can serve as a powerful re-ranker in a zero-shot setting.

3. **High performance with extremely compact global features** — Figure 1 (bottom) and Table 2 show competitive or state-of-the-art results with feature dimensions as low as 128D, a 66× reduction versus SALAD's 8,448D. This is practically significant for real-world large-scale deployment.

4. **Comprehensive ablation studies** — Tables 5–8 (in the main paper) systematically ablate layer selection (n−1 is optimal), feature facet (Value outperforms Query/Key), thresholds (both T₁ and T₂ are necessary), and number of trainable layers (five layers is optimal). These provide clear evidence that each design choice contributes to overall performance.

5. **Demonstrated generalization across diverse conditions** — The method is evaluated on a large set of benchmarks covering multiple cities, day/night, seasonal changes, occlusion, and multi-decade temporal gaps (AmsterTime) without dataset-specific adaptation, showing consistent top-tier performance.

## Weaknesses

### Fatal
None.

### Major

1. **Re-ranking reduces performance on Pitts30k without acknowledgment or explanation.** The paper's central claim is that the two-stage approach improves over the global stage. However, comparing Table 2 (global stage, 94.8% R@1 on Pitts30k) with Table 3 (reranked, 93.9% R@1 on Pitts30k) reveals a 0.9 percentage point drop. The paper states that "\ours-R achieves top performance across all datasets, taking the second place only on Pitts30K-R@1, with very close result" — this phrasing elides the fact that the global stage itself achieved 94.8% (second place, essentially tied with CricaVPR's 94.9%), and re-ranking actively widened the gap. The paper's contribution (line 48) claims re-ranking "significantly boosts performance," but on a major benchmark the opposite occurs. This inconsistency weakens the claim that the re-ranking stage is uniformly beneficial and requires either explanation (threshold mismatch? systematic disruption of correct top-1 matches?) or adjustment of claims. The ablation on K values (Table S) confirms the issue persists across all K choices on Pitts30k, so it is not simply a K=100 artifact.

2. **Missing controlled ablation separating architectural contribution from training recipe.** The paper claims that eliminating external aggregation methods (NetVLAD, GeM) in favor of the [CLS] token with classification loss is a key contribution (line 25–26, 47). However, it does not ablate this choice against alternatives. Is the strong performance due to the [CLS]-with-classification-loss design, or simply because DINOv2 responds well to fine-tuning with CosFace on SF-XL? An experiment that trains the same DINOv2 backbone (last 5 layers) with a GeM pooling head and contrastive loss — keeping dataset, dimensionality, and training protocol otherwise identical — would disentangle these factors. Without this, the architectural claim is underdetermined; the results could be attributed primarily to the training recipe rather than the proposed pooling-free design.

### Minor

1. **Zero-shot gains lack per-query diagnostic analysis.** The improvement from vanilla DINOv2 (62.2% → 90.8% on Tokyo24/7; 33.0% → 57.9% on Nordland) is dramatic and attributed entirely to the re-ranking mechanism. The paper provides extensive ablations on thresholds, facets, and layers, which are helpful, but does not include per-query analysis (e.g., how many queries are corrected by re-ranking vs. disrupted; distribution of MNN counts for correct vs. incorrect candidates; fraction of queries where the correct match is not in the top-100 and thus unrecoverable). A single qualitative example (Figure 2b) is insufficient to fully characterize when and why the mechanism succeeds or fails. While this does not invalidate the results, adding such analysis would substantiate the claim that the re-ranking mechanism is robustly selecting correct matches across diverse conditions.

### Trivial

1. **Dagger ($^\dag$) marker inconsistency in Table 2.** The caption states "Two-stage methods are marked with \dag, and present 1st-stage performance," yet \ours-G (a single-stage method) is also daggered. This is confusing when compared to Table 3 where \ours-R is correctly daggered.

2. **"CricaVPR" vs. "CircaVPR" typo in Table 4** (line 288). The method is referred to as "CircaVPR" once, while the correct name "CricaVPR" is used everywhere else in the paper and in the citation.

## Nice-to-Haves

- **Threshold sensitivity in main text**: The paper references the appendix for threshold ablations. A brief note in the main text on how robust the method is to T₁ and T₂ values (e.g., a range over which performance is stable) would improve practical applicability.
- **More complete runtime analysis**: The paper reports "1 millisecond per match" for re-ranking. Including global feature extraction time, database search time, and end-to-end latency — especially for larger galleries — would better contextualize practicality.
- **Full recall curves for zero-shot**: Table 1 only reports R@1 for zero-shot methods, while trained methods are compared at R@1, R@5, R@10. Providing R@5 and R@10 for zero-shot would allow fairer comparison with trained methods in Figure 1(a).
- **Controlled comparison with standard pooling**: As noted in Weakness #2 (Major), an ablation comparing [CLS]+classification vs. GeM+contrastive under otherwise identical conditions would resolve the architectural claim.

## Removed Points

The following points from the reviewer inputs were removed per the review synthesis rules:

- **Criticism about missing appendix analyses / threshold sensitivity tables**: The appendix exists in the original submission (stripped by parser). The paper explicitly references the relevant appendix tables.
- **Criticism about "suspiciously high" zero-shot numbers with no evidence of error**: The numbers are supported by ablations on thresholds, facets, layers, and K values across multiple datasets. The reviewer's suspicion is not grounded in any identified methodological flaw.
- **Formatting/style nitpicks** (parser artifacts, line breaks, capitalization): These are parser issues, not author errors.
- **Demands for broader scope (adding Y, covering Z domain)** that would turn the paper into a different paper.
- **Accusation that AnyLoc or other baselines are not properly cited/exist**: All cited references are treated as real.

## Novel Insights

The key insight that emerges from the reviews — beyond what the paper itself states — is that the internal Value features of ViT, filtered by the [CLS] attention scores, provide a surprisingly effective local descriptor for re-ranking without any learned aggregation. This is notable because prior work (AnyLoc, SelaVPR, CricaVPR) either used output-layer features with external pooling or learned adapters. The paper shows that the attention mechanism itself can serve as a natural feature selector, and that combining attention-filtered Value features with MNN matching yields strong results in both zero-shot and fine-tuned settings. The fact that this works with a single set of fixed thresholds across 20 diverse datasets suggests the DINOv2's internal representations have a degree of invariance that prior methods did not fully exploit.

## Suggestions

1. **Acknowledge and analyze the Pitts30k re-ranking regression.** Provide a brief discussion of why re-ranking reduces performance on this dataset (e.g., threshold sensitivity, the nature of viewpoint variations in Pitts30k, or characteristics of the correct matches that get disrupted). If thresholds or other parameters are suboptimal for this dataset, state this explicitly. Consider reporting both global-only and reranked results in the same table to allow direct comparison.

2. **Add a controlled ablation of the global feature design.** Train the same DINOv2 backbone with a GeM pooling head (or NetVLAD) under identical conditions (same dataset SF-XL, same trainable layers, same dimensionality) to isolate whether the [CLS]-with-classification-loss strategy is responsible for the gains, or whether the fine-tuning recipe itself is the dominant factor.

3. **Include per-query analysis for zero-shot.** On a representative dataset (e.g., Tokyo24/7), show the fraction of queries corrected vs. disrupted by re-ranking, and the distribution of MNN counts for correct vs. incorrect matches. This would build trust in the mechanism's robustness.

## Score and Decision

This paper presents a well-motivated and empirically strong approach to VPR that achieves state-of-the-art results across many benchmarks with compact features. The methodology is clearly described and the ablation studies are generally thorough. The two major weaknesses — the unexplained Pitts30k re-ranking regression and the missing controlled ablation for the architectural claim — are real but addressable and do not invalidate the paper's core contributions. With appropriate revisions, this paper would represent a meaningful advance in foundation-model-based VPR.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>