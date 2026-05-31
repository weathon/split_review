## Summary

This paper presents CORE-3D, a training-free pipeline for open-vocabulary 3D scene understanding that combines three key innovations: (1) progressive multi-granularity mask refinement using SemanticSAM to reduce fragmentation; (2) context-aware CLIP encoding that aggregates embeddings from multiple complementary crops (mask, bounding box, large, huge, surroundings) with a negative weight on the surroundings crop; and (3) multi-view 3D mask merging with a symmetric-balanced volumetric overlap criterion. The method is evaluated on 3D semantic segmentation (Replica, ScanNet) and natural-language object retrieval (SR3D+), outperforming prior open-vocabulary approaches.

## Strengths

- **Principled pipeline addressing known weaknesses of SAM-based open-vocabulary 3D mapping.** The progressive granularity refinement is well-motivated to mitigate over-segmentation while preserving small objects, and the symmetric IoV merging criterion handles multi-view consistency in a geometrically sound way.
- **Innovative context-aware CLIP encoding strategy.** Constructing five distinct crops (mask, bbox, large, huge, surroundings) with a weighted combination that subtracts the surroundings embedding is a clever, training-free way to inject richer visual context beyond the isolated mask crop.
- **Strong quantitative results across multiple benchmarks.** On Replica, the method achieves mIoU 0.29 and fmIoU 0.56, clearly surpassing BBQ-CLIP (0.27, 0.48). On ScanNet, it achieves mIoU 0.36 and fmIoU 0.46 versus BBQ-CLIP's 0.34 and 0.36. On SR3D+ object retrieval, the method outperforms BBQ by 7.6% absolute at A@0.25 (35.6 vs 22.7), a substantial improvement.
- **Ablation studies validate each component.** Tables 3, 4, and 5 systematically demonstrate that progressive granularity, context-aware CLIP encoding, and the mask-size-based extension mechanism each contribute to the final performance.
- **Well-structured retrieval pipeline.** The query structuring, VLM verification, and orientation grounding stages provide a complete, interpretable framework for complex 3D language queries with spatial relations.

## Weaknesses

### Fatal
None.

### Major
1. **Unclear tuning procedure for embedding weights.** The paper states the weights in Section 3.2 are "empirically tuned" without specifying whether this tuning was performed on held-out validation data or on the test datasets themselves. If the weights were optimized to maximize performance on the reported test sets (Replica, ScanNet, SR3D+), this constitutes test-set contamination. The authors must clarify the exact tuning procedure and report validation-set performance to rule out this concern.

2. **No statistical significance or variance reported.** All results in Tables 1–5 are presented as point estimates without error bars, confidence intervals, or scene-level standard deviations. Given that zero-shot methods can exhibit high variance across different scenes, it is essential to assess whether the reported improvements are consistent or driven by a few favorable scenes.

3. **Progressive refinement yields no improvement on ScanNet fmIoU.** Table 3 shows that on ScanNet, single granularity level 4 achieves fmIoU 0.46, identical to the proposed progressive method (0.46). The claimed benefit of progressive granularity is thus not supported on this benchmark. The paper should discuss this discrepancy and under what conditions the progressive strategy is actually beneficial.

4. **Reproducibility concerns for retrieval pipeline.** The retrieval pipeline relies on external VLM/LLM APIs, but the paper does not specify which models were used (e.g., GPT-4V, Gemini, Claude). Different models or API versions could produce different results, and the prompts (relegated to the removed appendix) are critical for understanding and reproducing the approach.

### Minor
5. **DBSCAN parameters not reported.** The method uses DBSCAN clustering in mask refinement (Section 3.1), but the critical hyperparameters (eps, min_samples) are never specified. The sensitivity of results to these choices is unexplored.
6. **Incomplete baseline comparisons.** For training-based methods, many entries in Table 1 are marked "–", making it impossible to compare across all methods on all metrics. The paper should either report available numbers or explain why they are missing.
7. **"Neighbor coverage" ablation is poorly explained.** Table 5 compares "Neighbor coverage" vs "Mask size" extension mechanisms, but the neighbor coverage variant is not clearly defined in the main text.

### Trivial
None significant.

## Nice-to-Haves

- Include error bars or scene-level performance breakdowns to demonstrate statistical reliability.
- Provide a sensitivity analysis of the key hyperparameters (embedding weights, IoV thresholds \(\gamma\) and \(\delta\), DBSCAN parameters).
- Report a failure case analysis to help readers understand the method's limitations.

## Novel Insights

Beyond the paper's own contributions, the idea of using a negative weight on the surroundings crop to create a contrastive embedding is a neat trick that could generalize to other zero-shot recognition pipelines where masked crops lose valuable context. The symmetric-balanced volumetric overlap criterion (IoV) for 3D merging is also a practical improvement over simple intersection-over-union, as it explicitly prevents merging objects with asymmetric containment relationships (e.g., a small object lying on a large surface).

## Suggestions

- Clearly state whether the embedding weights were tuned on held-out validation scenes or on the test datasets, and validate on separate data if not already done.
- Add error bars by reporting per-scene results or bootstrap confidence intervals across scenes.
- Specify the exact VLM and LLM models used (e.g., GPT-4V-2024-05-13, Claude 3.5 Sonnet) and include the full prompts in the paper rather than only in the removed appendix.
- Discuss conditions under which the progressive granularity refinement is most beneficial and when a single granularity suffices.
- Report DBSCAN parameters and test sensitivity to them.

## Score and Decision

The paper makes a solid contribution to open-vocabulary 3D scene understanding with a clever, training-free pipeline and strong empirical results. However, the lack of clarity on empirical tuning, absence of variance estimates, and incomplete ablation analysis (notably the ScanNet fmIoU result) prevent me from recommending a higher score. These issues are addressable and do not fundamentally invalidate the contribution.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>