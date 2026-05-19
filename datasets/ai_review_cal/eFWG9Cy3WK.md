- Decision: Accept
- Avg Score: 6.33
- Scores: 3, 8, 8
Now I have all the information I need. Let me write the consolidated final review.

## Summary

This paper proposes **MC-SMoE** (Merge, then Compress SMoE), a pipeline that consolidates redundant experts in Sparse Mixture-of-Experts models using routing-policy statistics. The method (M-SMoE) first aligns expert permutations, groups experts via router-logit similarity, and merges groups using activation-frequency weighting. An interesting follow-up observation — that merged experts exhibit lower weight dimensionality — motivates a second compression step (low-rank + structured-sparse decomposition). Experiments on switch-base-32 across eight NLP benchmarks show M-SMoE reduces memory by 60% while matching or exceeding the full SMoE on five of eight tasks, and MC-SMoE achieves up to 80% memory and 20% FLOPs reduction with minimal performance loss.

## Strengths

1. **Routing-guided grouping beats seven alternative similarity measures (Table 4).** The proposed *router-logits* similarity consistently outperforms *random*, *expert-weight*, *expert-gradient*, *router-weight*, and three other variants on MultiRC, COPA, MRPC, and SQuAD (e.g., 75.57 vs. 74.69 for random on MultiRC). This directly validates the paper's core claim that routing policies contain effective signals for expert grouping.

2. **Frequency-weighted merging is superior to uniform and Fisher-weighted averaging (Table 7).** Frequency-weighted merging beats both baselines on all four tasks tested (e.g., COPA 68.00 vs. 64.00 and 65.00). This supports the design choice of using activation frequency as an importance proxy.

3. **Adaptive layer-wise merging ratio yields consistent gains over a uniform ratio (Table 3).** On COPA (68.00 vs. 63.00), MRPC (90.69 vs. 90.44), and SQuAD (85.49 vs. 84.56 F1), the adaptive strategy outperforms uniform, confirming the necessity of accounting for cross-layer variation in expert utilization.

4. **M-SMoE achieves 60% memory reduction with performance matching or exceeding the full SMoE on 5/8 tasks (Table 2).** M-SMoE (733M params vs. 2.0B) matches or surpasses full SMoE on MRPC, COPA, WinoGrande, SQuAD, and HotpotQA. For example, SQuAD F1 is 85.49 vs. 85.81 (full SMoE) — a difference of 0.32 points at 60% fewer parameters.

5. **Post-merging compression (MC-SMoE) outperforms compression alone (C-SMoE) despite using fewer parameters (Table 6).** MC-SMoE (381M) beats C-SMoE (570M) on COPA (67.00 vs. 64.00), MRPC (89.22 vs. 88.97), and SQuAD F1 (85.30 vs. 84.93). This provides causal evidence that merging reduces weight-space dimensionality and thereby improves compressibility, a key insight of the paper.

6. **Expert permutation alignment before merging brings clear improvement (Table 5).** Adding weight-matching raises accuracy on COPA from 66.00 to 68.00 and MRPC from 89.95 to 90.69, confirming the importance of handling different optimization trajectories across experts.

7. **The paper provides a controlled KD ablation (Table 5) that isolates the contribution of merging.** The paper explicitly quantifies KD's impact (e.g., COPA 64.00 without KD vs. 68.00 with KD) and states that KD is used for *all* baselines (Section 4.3), ensuring the claimed improvements are not artifacts of asymmetric post-processing.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
1. **Baseline adaptation details for merging methods are underspecified.** The paper states it "directly adapts" Averaging, ZipIt, REPAIR, and Git Re-basin to the SMoE setting and that all methods reduce to ~8 experts/layer, but does not describe how each method's grouping/merging logic was applied to expert groups (e.g., whether ZipIt's pairwise merging was applied within groups or across the entire layer, or how REPAIR's activation statistics were collected for experts). While the results are reasonable and consistent, this limits reproducibility and makes it harder to assess whether the comparison is fully fair to these baselines.

2. **The knowledge distillation description has a minor ambiguity.** Section 4.1 states "we apply knowledge distillation (KD) to compel the M-SMoE and MC-SMoE models to imitate the outputs," which could be read as KD being applied only to the proposed methods. Section 4.3 later clarifies that "we by default use KD for all merged and compressed SMoEs, including our M-SMoE, MC-SMoE, and all baselines." These statements are not contradictory (the latter resolves the former), but the earlier sentence should be rephrased to avoid confusion about whether pruning baselines also received KD.

3. **Zero-shot results for the second model family (fairseq-moe-15b) are absent from the main text.** The paper claims evaluation on two SMoE families and mentions zero-shot benchmarks (MRPC, WinoGrande, OpenBookQA) but provides no numerical results in the main body. These results may exist in the appendix (which is stripped by the parser), but a summary table or key numbers in the main text would substantiate the claim of general applicability across architectures.

### Trivial
- The caption for Table 1 states M-SMoE "still outperforms all other pruning and merging baselines" on SST-2, MultiRC, and WikiQA. While true on the last two, M-SMoE ties pruning on SST-2 (94.50 vs. 94.50). The phrasing could be slightly more precise.

## Nice-to-Haves
- A brief wall-clock timing comparison (even a single forward-pass latency) would ground the FLOPs savings in a more tangible efficiency metric.
- A discussion of how many samples are needed for collecting routing statistics and whether the procedure is sensitive to this sample size would strengthen reproducibility.

## Removed Points
- **Critic's Issue #1 (KD asymmetry as a "methodological gap" threatening fairness of comparisons):** The paper explicitly states in Section 4.3 that "we by default use KD for all merged and compressed SMoEs, including our M-SMoE, MC-SMoE, and all baselines." The Section 4.1 description is merely incomplete, not contradictory. The critic's characterization of this as a fatal flaw is unsupported.
- **Critic's Issue #3 (pruning being "competitive or better" on SST-2/MultiRC/WikiQA):** Factually inaccurate. M-SMoE ties pruning on SST-2 (94.50), beats it on MultiRC (75.57 vs. 75.13), and beats it on WikiQA (96.34 vs. 96.27). The paper's claim that M-SMoE "outperforms all other pruning and merging baselines" is supported by the data.
- **Critic's Issue #4 (FLOPs vs. speedup):** FLOPs reporting is standard practice in the efficiency literature, and the paper clearly describes how TFLOPs are computed. This is not a weakness.
- **Critic's concern about adaptive ratio being underspecified:** Algorithm 1 clearly shows `top(k, row-normalize(A))` where `k` (the number of remaining experts) is an input parameter. The selection rule is well-defined.
- **Strength Finder's #8 (zero-shot evaluation across two model families):** Removed because the zero-shot numerical results for fairseq-moe-15b are not present in the main text (may exist in the appendix). The strength is aspirational but unsubstantiated in the main body.

## Novel Insights

The most interesting insight emerging from the cross-review is how well the paper's ablations isolate the contribution of each design choice. The finding that *router-logits* similarity (which directly captures routing decisions over input samples) outperforms both *router-weight* (the raw weight matrix rows) and *expert-weight* (the expert network weights themselves) is non-trivial — it suggests that the *behavioral* similarity of experts (which inputs they fire on) is a better signal for grouping than *parametric* similarity (how their weights relate). This behavioral-vs-parametric distinction is worth highlighting and could inform future work on expert consolidation beyond SMoE. Additionally, the stable-rank analysis (Figure 3) offers an empirical bridge between merging and compressibility that is rarely demonstrated so directly.

## Suggestions

1. Clarify in Section 4.1 that KD is applied uniformly to all baselines (pruning and merging methods), not just the proposed methods.
2. Add a small table or paragraph summarizing the fairseq-moe-15b zero-shot results in the main text. Even two or three key numbers would substantially strengthen the claim of general applicability.
3. Provide more detail on how each merging baseline (ZipIt, REPAIR, Git Re-basin) was adapted: e.g., were experts merged pairwise within groups or all at once? Were the same grouping and alignment procedures used?
4. Acknowledge the first-layer skip more prominently as a limitation/discussion point.
