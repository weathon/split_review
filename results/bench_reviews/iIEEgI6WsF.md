Now I have a thorough understanding of the paper and the review inputs. Let me synthesize the final review.

---

## Summary

This paper proposes On-Demand Communication (ODC), which replaces FSDP's per-layer collective operations (all-gather and reduce-scatter) with RDMA-based point-to-point communication, effectively reframing FSDP as a decentralized parameter server. By relaxing synchronization from the layer level to the minibatch level, ODC mitigates straggler effects caused by sequence-length imbalance in LLM post-training. The approach also enables LB-Mini, a simpler minibatch-level load balancing strategy. Experiments on SFT (LongAlign, SWE-Smith) and RL (AIME/GRPO) across 1.5B–32B models demonstrate up to 36% throughput improvement over collective FSDP.

## Strengths

- **Elegant conceptual reframing with practical impact**: The paper identifies that FSDP's per-layer collectives create synchronization barriers that are an artifact of the communication model, not a training requirement. By decomposing all-gather into targeted gather requests and reduce-scatter into scatter-accumulate operations (Section 3.1, Figure 6), ODC retains FSDP's memory layout while inheriting PS-style workload tolerance. This is a clean, well-motivated design.

- **Strong empirical evidence for SFT**: The throughput results on LongAlign and SWE-Smith (Figure 8, Table 5) show substantial and consistent gains across model sizes. At 14B LongAlign minibatch 4, ODC LB-Mini achieves a 36% speedup over collective LB-Micro, and even ODC LB-Micro (without the new load balancer) achieves 28%. The bubble-rate data (Tables 4 and 6) directly quantify the idle-time reduction, e.g., 14B LongAlign collective LB-Micro shows 57% bubble rate at minibatch 4, reduced to 14% under ODC LB-Mini.

- **Well-designed parametric study**: The controlled experiments in Section 5.3 isolate how minibatch size, max sequence length, packing ratio, and device count modulate ODC's effectiveness. The finding that acceleration ratio grows with device count (more devices → more heterogeneity → more benefit) and with sequence length (quadratic compute cost hides communication) provides actionable guidance.

- **LB-Mini is a genuine contribution enabled by ODC**: By removing per-layer synchronization, ODC allows devices to process different numbers of microbatches. LB-Mini exploits this to balance at the minibatch level rather than the microbatch level, yielding up to 27% additional gain over ODC LB-Micro at small minibatch sizes (SWE-Smith 1.5B, minibatch 2).

- **Convergence verification and open-source release**: The learning curves in Appendix F confirm ODC matches collective FSDP's optimization trajectory, and the code is publicly available, supporting reproducibility and adoption.

## Weaknesses

### Fatal

None.

### Major

- **The "consistently improves" claim is too strong given negative RL results**: The abstract and conclusion state that ODC "consistently improves device utilization and training throughput" across tasks including RL. However, Table 3 shows that for the 14B model on AIME at minibatch size 2, ODC LB-Micro achieves 101.0 samples/s vs. 106.4 for collective LB-Micro, a **−5% regression**. ODC LB-Mini similarly shows −4%. The main text (Section 5.2) only says "gains are less pronounced" without acknowledging these throughput regressions. While the method shows clear benefits in the vast majority of configurations tested, the blanket "consistently improves" claim is incorrect as stated and should be narrowed. The paper should discuss when and why ODC can underperform.

- **No decomposition of communication overhead vs. idle-time reduction**: Tables 4 and 6 show ODC dramatically reduces idle time in all configurations, including the 14B RL minibatch-2 case where bubble rate drops from 28.35% to 22.89%. Yet throughput still regresses, implying that ODC's point-to-point communication pattern imposes higher overhead than collectives in that regime. The paper never directly measures or decomposes communication versus computation time, leaving the reader unable to understand the trade-off or predict when ODC will help. Section 6 acknowledges inter-node inefficiency and proposes hybrid sharding, but this analysis is not connected back to the actual regressions observed. This gap prevents the paper from establishing a clear operational envelope for ODC.

### Minor

- **Headline speedup conflates ODC with LB-Mini without clear attribution**: The abstract credits ODC for "up to a 36% speedup" without clarifying that this number comes from ODC + LB-Mini combined. The 36% figure (14B LongAlign, minibatch 4) compares ODC LB-Mini against collective LB-Micro, so it reflects gains from both the communication change and the new load-balancing algorithm. While LB-Mini is enabled by ODC and the paper does separately report ODC LB-Micro results (e.g., +28% on the same setting), the abstract should clearly separate the two contributions to avoid misleading readers about where the gains come from.

- **Non-intrusive claim lacks empirical validation**: Section 3.2 asserts that ODC's RDMA transfers are non-intrusive and do not interrupt server-side computation, with a daemon handling gradient accumulation without occupying GPU SMs. The paper mentions "no observable slowdown" (Appendix B) but provides no quantitative measurement of RDMA interference on memory bandwidth or compute throughput. While the overall throughput gains implicitly suggest interference is manageable, a direct measurement would strengthen this critical implementation claim.

### Trivial

- The paper refers to Figure 11 (communication primitive bandwidth benchmarking) from Section 5.3, but the figure contains content not directly discussed until Section 6.

## Nice-to-Haves

- A direct measurement or profiled timeline trace comparing communication time, computation time, and idle time for a beneficial vs. detrimental configuration would help readers understand the trade-off.
- Testing on heterogeneous hardware (mixed GPU types) would strengthen the "revisiting PS" narrative, though this is outside the paper's stated scope.
- An explicit characterization of the break-even sequence length or compute-to-communication ratio below which ODC becomes slower than collectives would provide practical guidance for practitioners.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Missing comparison with asynchronous allreduce baseline"**: The paper explicitly scopes itself to synchronous semantics (Section 6.2 discusses async as future work). Demanding this comparison is scope creep.
- **"Evaluation needed at 128+ GPUs"**: The parametric study already shows trends with device count; demanding a specific larger scale is a generic one-size-fits-all criticism.
- **"Network contention analysis needed"**: The paper already provides communication bandwidth benchmarks (Figure 11) and discusses inter-node inefficiency (Section 6). Additional microbenchmarks would be nice but are not a gap.
- **"Memory overhead quantification"**: The paper describes ODC's memory layout (M/N per client, total M) which matches FSDP's sharding. The criticism is speculative without evidence of a problem.
- **"The PS motivation oversimplifies history"**: This is a subjective stylistic complaint, not a substantive weakness.
- **Strength Finder generic strengths dropped**: "The paper addresses an important problem" and similar generic statements removed as superficial.

## Novel Insights

The most interesting insight emerging from this work — beyond the paper's own claims — is the framing of FSDP as a decentralized PS where colocated server/worker roles preserve memory efficiency. This reframing reveals that the efficiency advantage of collectives over PS in homogeneous clusters was always contingent on balanced workloads, and that the post-training regime (with its inherent sequence-length variance) tips the balance back toward PS-style architectures. The parametric study's finding that ODC's advantage grows with device count (more heterogeneity at scale) while collective overhead also grows suggests a potentially fundamental scalability advantage for PS-style communication in imbalanced settings.

## Suggestions

- Revise the abstract and conclusion to replace "consistently improves" with more precise language, e.g., "improves throughput in the large majority of configurations" or "substantially improves throughput on SFT tasks."
- Add a paragraph in Section 5.2 explicitly discussing the 14B RL minibatch-2 regression, connecting it to the inter-node communication analysis in Section 6, and characterizing when ODC may not help.
- Consider adding a simple decomposition of the 14B minibatch-2 RL case: show that bubble rate was reduced (Table 4 already shows 28% → 23%) but point-to-point communication cost increased enough to offset the gain. Even a brief analysis would substantially strengthen the paper.
- Clarify in the abstract that the 36% headline number includes the LB-Mini contribution, and state the ODC-only (LB-Micro) gain separately.
- Add a brief note in Section 5.3 (or the parametric study caption) indicating whether the acceleration ratio ever drops below 1.0 in the controlled experiments, for completeness.

## Score and Decision

### Calibration Anchors

- `/home/wg25r/review_agent/human_reviews_2026/vU7pcaDypQ.md` — avg score 4.00 (Reject): A method for partial parameter updates to reduce communication. Incremental extension of DiLoCo; marginal improvements over prior work. The current paper is substantially stronger: it has a more novel technical contribution, broader empirical validation across multiple tasks and scales, and addresses a more clearly identified bottleneck.

- `/home/wg25r/review_agent/human_reviews_2026/ddf7XdLtNO.md` — avg score 4.00 (Reject): Data scheduling based on sequence length for LLM pretraining. Addresses a related problem but with narrower scope and less compelling evidence. The current paper has stronger experimental validation and a more principled systems contribution.

- `/home/wg25r/review_agent/human_reviews_2026/1VgUoPfl3z.md` — avg score 4.50 (Reject): KnapFormer for load balancing in DiT training. Addresses a similar problem (workload imbalance) with a knapsack-based solution. Achieves 2-3x speedups but reviewers flagged limited novelty and baseline comparisons. The current paper has a more novel core idea (PS reframing of FSDP) and better ablation studies, though KnapFormer's raw speedup numbers are larger.

- `/home/wg25r/review_agent/human_reviews_2026/lWWaBbFPw4.md` — avg score 4.00 (Reject): DCP for variable-length sequence training. Similar problem domain. Has substantial speedups but reviewers flagged limited novelty, small models, and weak baselines. The current paper tests larger models (up to 32B), has stronger baselines, and provides a more principled communication redesign rather than a scheduling heuristic.

- `/home/wg25r/review_agent/human_reviews_2026/HZYuyNkBdD.md` — avg score 5.50 (Accept Poster): Decentralized ADMM optimization with theoretical guarantees. Strong theory but limited experiments (small datasets, fixed network size). The current paper is a systems contribution with complementary strengths: strong empirical evidence but no theoretical analysis. Both have concrete but addressable weaknesses. Comparable quality level.

- `/home/wg25r/review_agent/human_reviews_2026/0KXI6lDM9C.md` — avg score 5.50 (Accept Poster): Theoretical lower bounds for distributed optimization. More theoretical than the current paper; different subfield.

- `/home/wg25r/review_agent/human_reviews_2026/cEkVJeMwSd.md` — avg score 4.50 (Reject): Activation quantization for pipeline parallelism. Similar systems flavor but narrower scope.

The current paper sits above the 4.0–4.5 anchors due to stronger novelty (the PS reframing is genuinely insightful), more comprehensive experiments, and clear practical value. It falls short of an outstanding contribution (7+) due to the overclaimed consistency, the missing decomposition analysis for the RL regression, and the conflation of ODC and LB-Mini contributions. These weaknesses are addressable in a rebuttal. The paper is comparable to the 5.5 anchors in overall quality — a solid systems contribution with well-identified, fixable weaknesses.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>