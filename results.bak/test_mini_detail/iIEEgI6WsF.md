Now I have all the information needed. Let me write the final consolidated review.

## Summary

This paper proposes On-Demand Communication (ODC), which replaces FSDP's per-layer collective all-gather/reduce-scatter with point-to-point gather and scatter-accumulate operations. By relaxing synchronization from layer-level to minibatch-level, ODC decouples device progress under imbalanced workloads in LLM post-training. The paper reframes FSDP as a decentralized parameter server, preserves FSDP's memory layout, and enables simpler minibatch-level load balancing (LB-Mini). Experiments on SFT and RL tasks across 1.5B to 32B models show up to 36% throughput improvement over standard FSDP.

## Strengths

- **Clear problem identification and formalization.** Section 2.2 provides Equation (1), which formalizes how per-layer max-over-device synchronization creates a fundamental bound on minibatch runtime under imbalanced workloads. This mathematical framing makes the root cause concrete and motivates the need for coarser synchronization.

- **Clean conceptual contribution.** Replacing FSDP's collectives with point-to-point primitives is a principled idea that directly addresses the identified problem. The reframing of FSDP as a decentralized parameter server (Section 3.1) provides a coherent design lens, and the integration preserves FSDP's memory efficiency and synchronous optimization semantics.

- **Consistent and meaningful empirical gains.** Figure 8 shows ODC outperforming collectives across all model scales (1.5B to 32B), datasets (LongAlign, SWE-Smith), and packing strategies (LocalSort, LB-Micro, LB-Mini). The parametric study (Figure 10) systematically varies minibatch size, sequence length, packing ratio, and device count, confirming that ODC's advantage grows with the factors that exacerbate imbalance (longer sequences, more devices).

- **Honest discussion of limitations.** Section 5.4 and Section 6.1 transparently acknowledge that ODC's point-to-point primitives achieve significantly lower bandwidth than NCCL collectives in multi-node settings (Figure 11). The paper proposes concrete mitigations (overlapping with O(s²) computation, hybrid sharding) rather than ignoring the issue.

- **Open-source implementation.** The code is publicly available, supporting reproducibility.

## Weaknesses

### Major

- **Inter-node communication overhead is acknowledged but not fully resolved.** The primitive benchmarks (Figure 11) show ODC's gather/scatter-accumulate achieving 5–20× lower bandwidth than NCCL collectives at 16–32 devices. While the paper's end-to-end results at 32 devices still show positive speedups, the overlapping argument has limits: the parametric study (Figure 10a) shows acceleration ratio declining at larger minibatch sizes, which is consistent with the communication overhead becoming harder to hide. The paper's claim that "ODC shows no significant slowdown in our long-context evaluations" (Section 6.1) is partially supported by the end-to-end results, but the regime where ODC remains beneficial is not clearly bounded (e.g., what is the minimum sequence length or compute-to-communication ratio needed for ODC to break even?). The hybrid sharding mitigation is mentioned but its evaluation is in the (stripped) appendix, so it cannot be assessed from the main text.

- **Speedup sources are not cleanly decomposed in the headline claim.** The "up to 36% speedup" combines ODC's communication scheme with LB-Mini's minibatch-level load balancing. The paper does show ODC+LB-Micro vs. Collective+LB-Micro in Figure 8 (isolating the communication benefit), and the parametric study (Figure 10) compares ODC+LB-Mini vs. ODC+LB-Micro (isolating the load-balancing benefit). However, these decompositions rely on reading values from figures, and no numerical table is provided in the main text. The reader cannot precisely determine how much of the 36% comes from removing collective barriers versus from the improved load balancing algorithm.

### Minor

- **No error bars or statistical uncertainty.** All reported metrics appear to be single runs. Given that distributed runtime can vary with system noise (especially under RDMA), this is a notable gap. It is unclear whether the observed trends (e.g., the gap between ODC+LB-Mini and ODC+LB-Micro in Figure 8) are reproducible.

- **No quantitative memory usage comparison.** The paper claims ODC preserves FSDP's memory advantages (Section 3.1, line 123), but no actual memory measurements are provided. Replacing collective buffers with per-peer communication might have memory implications, especially as the number of devices grows.

- **Missing baseline comparison against hierarchical/hybrid approaches.** The paper mentions ZeRO++ and hybrid sharding as related mitigations (Section 6.1) but does not include them as baselines. Given that inter-node communication is the main weakness, a comparison against a method that already addresses this dimension would strengthen the evaluation.

- **Uncharacterized overhead of the gradient accumulation daemon.** Section 3.2 mentions a "lightweight daemon" for gradient accumulation on the target device but does not quantify its overhead or discuss whether it introduces GPU kernel overhead.

- **Connection management at scale is not discussed.** ODC's point-to-point approach requires each device to communicate with all others. The paper does not discuss the overhead of managing many peer-to-peer connections (e.g., RDMA QP limits) at larger scales.

### Trivial

- **Minor imprecision in "long-context" characterization.** The AIME dataset has a mean of ~9k tokens (Figure 7), which is moderate rather than "long-context" as claimed in Section 6.1. The parametric study does test up to 128k, but the claim of "no significant slowdown in our long-context evaluations" would benefit from a clearer threshold.

## Nice-to-Haves

- A table of numerical speedup values for all configurations in Figure 8 (not just figures) would make the decomposition of communication vs. load-balancing gains precise.
- A controlled experiment comparing ODC and collectives under a perfectly balanced workload would directly quantify the overhead of ODC's point-to-point primitives.
- A simple analytical model of the break-even point (imbalance level needed for ODC to match collectives given the inter-node bandwidth gap) would help readers understand the deployment regime.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Table 6 not shown, cannot verify 50% idle time claim"** — The appendix containing Table 6 was stripped by the parser; the table exists in the original submission.
- **"LB-Mini algorithm is relegated to Appendix C"** — Appendix C was stripped by the parser; the algorithm exists in the original submission.
- **"Hybrid sharding not evaluated"** — Appendix E (stripped by the parser) contains the hybrid sharding evaluation; the main text references it (Section 6.1).
- **"ODC primitive benchmark caveat (synchronous barriers) not mentioned"** — The paper explicitly states "For fairness, ODC primitives are launched synchronously" (Section 5.4), so this caveat is already present.
- **"ODC primitives benchmark may overstate overhead"** — The paper already acknowledges the synchronous launch methodology.
- **"Collective Native baseline inflates ODC speedup"** — The paper shows both Collective Native and the stronger Collective LB-Micro in Figure 9, so readers can see both comparisons.
- **"Novelty concern about colocated roles in PS"** — The paper explicitly acknowledges precedent (Jiang et al., 2020) and states its novelty is in FSDP integration.
- **"Section-by-section notes about missing details in removed appendices"** — Multiple points about missing appendix content that was stripped by the parser.
- **Generic strengths from Strength Finder that lack specific evidence** — Removed as they were generic or conflicted with verified weaknesses.

## Novel Insights

None beyond the paper's own contributions. The harsh critic's observation about the tension between the inter-node bandwidth gap (Figure 11) and the positive end-to-end results (Figure 8) is worth highlighting: the paper's end-to-end results demonstrate that despite 5–20× slower raw primitives cross-node, ODC still wins overall—this implies that the imbalance-induced idle time in FSDP is a much larger problem than the raw communication bandwidth gap. This is an interesting data point that the paper could have made more explicit.

## Suggestions

1. **Add a decomposition table.** Provide a table with numerical throughput values for ODC+LB-Micro vs. Collective+LB-Micro and ODC+LB-Mini vs. ODC+LB-Micro across all settings, so readers can precisely attribute the speedup to the communication scheme vs. the load balancing algorithm.

2. **Add error bars or multiple-run statistics.** Even 2–3 runs per configuration would significantly increase confidence in the reported trends.

3. **Bound the beneficial regime more clearly.** Provide a controlled experiment under perfectly balanced workloads to quantify ODC's pure overhead, and then show how much imbalance is needed for ODC to break even. This would help practitioners understand when ODC is and is not advantageous.

4. **Include a hybrid sharding or ZeRO++ baseline.** Given that inter-node communication is the main weakness, comparing against a method that already addresses this dimension would significantly strengthen the evaluation.

5. **Provide memory usage measurements.** Quantify the memory footprint of ODC's per-peer communication buffers compared to collective buffers.

## Score and Decision

**Calibration methodology:**

**Round 1 — Bracketing:**
- Weak anchors (< 3.5): Papers on distributed/parallel training at scores 1.67–2.60. These have fundamental issues (e.g., DistPar at 1.67, decentralized training at 2.00). Our paper is clearly much stronger.
- Middle anchors (3.5–7.5): BurstAttention (5.60, Reject), LightSeq (5.00, Reject), MSfusion (4.67, Reject). These are distributed training systems papers with varying degrees of contribution.
- Strong anchors (> 7.5): Federated learning papers at 7.60–8.00. These are very strong theoretical or empirical contributions.

**Bracket:** 5.0–7.0

**Round 2 — Narrowing:**
- Zero Bubble Pipeline Parallelism (7.00, Accept Poster): Both are distributed training systems papers with clean insights. Zero Bubble has more thorough evaluation (including memory analysis, schedule optimization) and a cleaner trade-off (bubble elimination vs. memory). Our paper's evaluation is less thorough (no error bars, no memory numbers, conflation of two contributions). Our paper is weaker than Zero Bubble.
- NetMoE (7.20, Accept Spotlight): Both optimize communication in distributed training. NetMoE has a clearer problem formulation, optimization framework, and more thorough evaluation. Our paper is weaker than NetMoE.
- BurstAttention (5.60, Reject): Both are distributed training systems papers. Our paper has clearer novelty, larger-scale evaluation (up to 32 GPUs vs. 8), and more model scales (1.5B–32B). Our paper is stronger than BurstAttention.
- LightSeq (5.00, Reject): Cleaner novelty and better evaluation than LightSeq, which was criticized for overstatement and limited baselines.

The paper sits between the ~5.0–5.6 rejected systems papers and the ~7.0–7.2 accepted ones. The core idea is well-motivated and the results are directionally positive, but the unresolved inter-node concern and the lack of clean decomposition of speedup sources prevent it from reaching the level of the stronger accepted papers.

**Final score: 6.0**

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>