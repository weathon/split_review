Now I have a thorough understanding of the paper. Let me compose the final consolidated review.

## Final Review

## Summary
AtlasKV proposes a parametric knowledge augmentation method that converts KG triples into Q-K-V data (KG2KV) and uses hierarchical key-value pruning (HiKVP) to achieve sub-linear inference complexity. The key claims are (1) enabling billion-scale KG augmentation within 20GB VRAM through HiKVP's sub-linear memory scaling, and (2) strong OOD generalization through diverse KG2KV training data.

## Strengths

- **Principled sub-linear GPU memory scaling via hierarchical pruning.** HiKVP reduces both time and memory complexity from O(M) to O(∛M) (Table 2). Figure 4 shows AtlasKV's GPU memory usage staying near 20GB across KG sizes up to 1B triples, while KBLaM exceeds 40GB at only 10⁵ triples. This is the most compelling evidence for the paper's central scalability claim.

- **KG2KV data construction is well-motivated and shows clear benefits.** Converting KG triples into Q-K-V data yields substantially higher query diversity (7.864% vs 0.003%) with lower token costs (165.7 vs 349.9, Table 1). This directly addresses the limited-diversity limitation of the prior Synthetic data approach used in KBLaM.

- **Strong accuracy at tested scales on challenging OOD datasets.** On ATLAS-Pes2o-QKV and ATLAS-CC-QKV, AtlasKV achieves 82.3% and 89.1% ACC@1 at 100 triples, compared to KBLaM's 16.4% and 21.8% (Table 3). Even with HiKVP pruning (k_R=128, k_I=64, k_L=16), AtlasKV retains a large advantage over KBLaM, demonstrating that the learned query heads enable effective fuzzy retrieval under pruning.

- **Ablation studies validate design choices.** Table 4 shows that removing either named or event entities from KG2KV systematically degrades accuracy, confirming the importance of both entity types. This provides concrete evidence for the design decisions in the data construction pipeline.

## Weaknesses

### Major

- **Accuracy evaluation maxes out at 10³ triples — six orders of magnitude below the claimed billion-scale capability.** The paper's title and abstract highlight augmenting LLMs with 1B-triple KGs, but the accuracy experiments in Table 3 only go up to 1,000 triples. The pruning hyperparameters (k_R=128, k_I=64, k_L=16) are tested exclusively on this tiny scale. There is no accuracy evaluation at, e.g., 10⁴, 10⁵, or 10⁶ triples to demonstrate that HiKVP's hierarchical retrieval remains effective as M grows. The GPU memory plot (Figure 4) supports the scalability of the memory footprint, but accuracy at scale is the binding constraint for practical use. This is a fundamental mismatch between the paper's ambition and its evidence.

- **CPU memory requirements for billion-scale operation are not addressed, making the practical feasibility claim incomplete.** During HiKVP inference, leaf-layer key and value vectors "remain in the CPU memory" (Section 4.2, Step 1). For 1B triples with 384-dim sentence embeddings (all-MiniLM-L6-v2), storing both base key and value embeddings at 32-bit precision requires roughly 3 TB of CPU RAM (if storing projected D-dim embeddings, this balloons further). The paper focuses on the 20GB VRAM budget but provides no discussion of CPU memory constraints, compression strategies, quantization, disk offloading, or alternative storage hierarchies. For a paper whose headline claim involves practical billion-scale deployment, this is a significant blind spot.

- **The comparison with KBLaM confounds methodological contributions with data differences.** AtlasKV is trained on KG2KV-constructed ATLAS-Wiki-QKV data, while KBLaM uses the Synthetic dataset from the original KBLaM paper. The substantial improvements in Table 3 (e.g., 82.3% vs 16.4% at 100 triples on Pes2o) could be driven largely by the higher-diversity training data rather than the hierarchical attention or pruning innovations. A controlled comparison — training KBLaM on KG2KV data or AtlasKV on Synthetic data — is needed to attribute improvement to method versus data. Without this, the paper's claim that AtlasKV is "more accurate and generalizable" conflates two independent variables.

### Minor

- **Generation quality (GPTScore) is not reported for the HiKVP-pruned variant.** Figure 5 evaluates GPTScore only for "AtlasKV w/o HiKVP" (full attention over all triples). The effect of the central algorithmic contribution (HiKVP) on answer relevance is not measured. Table 3 does show that HiKVP preserves knowledge grounding accuracy (ACC@1/ACC@5), which partially addresses this, but the generation quality dimension remains unexamined for the pruned variant.

- **The methodology for generating Figure 4 (GPU memory scaling up to 1B triples) is not described.** The main text does not explain whether this plot was produced via actual measurement on constructed embeddings at each scale, analytical calculation from the complexity formulas, or extrapolation. Given the centrality of this figure to the paper's main claim, the experimental or analytical procedure should be stated explicitly.

- **Clustering hyperparameters and pooling method are underspecified.** The hierarchical clustering uses UMAP and GMM (Section 4.2), but the specific parameters (e.g., number of GMM components, UMAP settings, distance metric) and the method for pooling child keys into parent keys (e.g., mean pooling, learned aggregation) are not reported. This reduces reproducibility.

- **No end-to-end wall-time or latency measurements.** The analysis focuses on FLOPs and memory complexity, but HiKVP requires multiple rounds of CPU→GPU transfers (upload root keys, offload; upload inter keys, offload; upload leaf keys/values). The latency of these transfers could dominate inference time at scale and is not evaluated.

### Trivial

- The complexity notation in Table 2 uses C_t and C_m as "much smaller than M" without expressing them in terms of the actual operational constants (k_R, k_I, k_L, S). Expressing the complexity directly in terms of these constants would be more informative.

- The computational cost of the relation rewriting step (LLM calls for each triple) for billion-scale KGs is not discussed. This is a preprocessing concern but relevant to the overall practical picture.

## Nice-to-Haves

- Evaluation on standard KGQA benchmarks (e.g., WebQuestionsSP, CSQA) would help the community calibrate AtlasKV's performance against established methods.
- A discussion of the offline hierarchical clustering cost (UMAP + GMM) for billion-scale KGs would improve transparency.
- Ablation of the relation rewriting step (comparing with vs. without rewriting) would strengthen the motivation, though the paper claims this is in the (stripped) appendix.

## Removed Points

The following points from the input reviews were filtered per the review guidelines:

- **Criticisms about missing appendix content (e.g., "the paper references Appendix H... which are stripped")**: Per guidelines, appendix material exists in the original submission and parser stripping should not be treated as a flaw of the paper.
- **Speculative claims about Figure 4 being "extrapolated" or "faked"**: No evidence in the paper supports this; the methodology is simply underspecified, which is addressed in Minor weaknesses above.
- **Nitpick about ICL complexity in Table 2 being a "straw-man baseline"**: The paper's ICL complexity assumes all triples are placed in context, which is the standard worst-case analysis for ICL; this is not a flaw.
- **Generic concern about relation rewriting not being ablated**: The paper states this analysis is in Appendix B.2 (stripped), so it cannot be confirmed as missing.
- **Strength finder's generic/superficial claims** (e.g., "this paper addressed an important problem"): Removed as unsubstantiated.

## Novel Insights

None beyond the paper's own contributions. The key insight — that KG triples can be naturally decomposed into Q-K-V structures matching the attention mechanism, and that hierarchical clustering of the key embeddings enables sub-linear pruning — is well articulated by the paper itself. The reviews did surface the important observation that the KG2KV data construction is a separable contribution whose impact is not cleanly isolated from the architectural innovations, but this is a critique of the evaluation design rather than a novel insight.

## Suggestions

1. **Run accuracy experiments at progressively larger KG sizes (10³ → 10⁴ → 10⁵ → 10⁶ triples)** on a fixed evaluation set, with the same HiKVP hyperparameters. This would directly bridge the gap between the current small-scale accuracy results and the billion-scale claim. Even if constructing evaluation data at massive scales is challenging, intermediate scales would provide strong evidence that pruning effectiveness does not degrade as M grows.

2. **Perform controlled comparison experiments**: train KBLaM on KG2KV data and/or train AtlasKV on Synthetic data. This would cleanly separate the contribution of the data construction (KG2KV) from the contribution of the architecture and pruning (HiKVP).

3. **Directly address the CPU memory bottleneck.** Discuss possible strategies: quantizing leaf embeddings to 2-bit or 4-bit precision, storing them on disk with a memory-mapped cache, or using a different hierarchy design that avoids storing all leaf keys in CPU RAM. Even a brief analysis of the trade-offs would significantly strengthen the practical feasibility claim.

4. **Report GPTScore for AtlasKV with HiKVP** using the same configuration as in Table 3 (128-64-16), so the effect of pruning on generation quality is directly visible.

5. **Explicitly describe the methodology for Figure 4** — whether it was measured, computed analytically, or extrapolated — and include the derivation or measurement setup.

6. **Add wall-time measurements** at one or two moderate scales (e.g., 10⁴ and 10⁵ triples) to quantify the overhead of CPU-GPU transfers in the hierarchical pruning pipeline.

## Score and Decision

The paper presents a genuinely interesting approach to parametric KG augmentation, with a well-designed hierarchical pruning mechanism and a principled data construction pipeline. The GPU memory scaling results are compelling. However, the evaluation has significant gaps: accuracy is only demonstrated up to 1,000 triples despite billion-scale claims, the CPU memory bottleneck is not addressed, and the comparison with KBLaM confounds method and data. These gaps are substantial enough that the evidence does not yet fully support the paper's central claims.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>