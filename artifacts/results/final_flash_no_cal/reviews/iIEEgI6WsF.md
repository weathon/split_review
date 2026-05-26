## Summary

This paper proposes On-Demand Communication (ODC), which replaces FSDP's per-layer collective operations (all-gather, reduce-scatter) with point-to-point RDMA-based gather and scatter-accumulate primitives. This relaxes synchronization from the layer level to the minibatch level, reducing device idle time under the imbalanced workloads that arise from variable sequence lengths in LLM post-training. ODC further enables a minibatch-level load balancing scheme (LB-Mini) that allows devices to process different numbers of microbatches. Experiments on SFT and RL tasks show consistent throughput improvements over standard FSDP, up to 36%.

## Strengths

1. **Root-cause fix of FSDP's synchronization barriers under imbalance.** The paper formally identifies (Eq. 1, §2.2) that per-layer all-gather and reduce-scatter create fine-grained barriers forcing faster devices to wait for slower ones. ODC replaces these collectives with point-to-point operations, relaxing the barrier from per-layer to per-minibatch (Figures 1, 2). This is a principled approach that addresses the problem at its source rather than only mitigating symptoms with complex packing.

2. **Consistent, substantial throughput gains across diverse settings.** In SFT tasks, ODC achieves up to 36% speedup over standard FSDP (Figure 8), and in RL tasks up to 10% (Figure 9). The gains hold across model sizes (1.5B–32B), datasets with different skew characteristics (LongAlign, SWE‑Smith, AIME), and multiple minibatch sizes — providing convergent evidence that the benefit is robust, not a corner case.

3. **Minibatch-level load balancing enabled by ODC's relaxed synchronization.** Because ODC removes the requirement that all devices have the same number of microbatches, it enables LB-Mini, a simpler balancing strategy that operates at the minibatch level (§4). The parametric study (Figure 10) shows LB-Mini consistently outperforms microbatch-level packing (LB-Micro) at small minibatch sizes, demonstrating that the decoupling creates a strictly larger optimization space.

4. **Parametric evidence linking the advantage to the problem's root causes.** The controlled study (§5.3, Figure 10) shows that ODC's acceleration ratio grows with sequence length (from ~25% at 8K to ~35% at 128K) and with device count (from ~25% on 1 device to ~35% on 32). These monotonic trends confirm ODC becomes more valuable precisely where workload imbalance is worst.

5. **Practical, non-intrusive implementation with RDMA primitives.** ODC is built on CUDA IPC, NVSHMEM, and Triton‑Distributed (§3.2), enabling on-demand transfers that do not interrupt the target device's computation. Integration with existing FSDP codebases requires only replacing collective calls, lowering the adoption barrier.

## Weaknesses

### Fatal

None.

### Major

1. **Ambiguous "Collective LB-Mini" baseline in Figure 8.** The paper explicitly states that LB-Mini "can produce different number of microbatches for different devices" and therefore "applies only to ODC" (§5.1). Yet Figure 8 includes a "Collective LB-Mini" curve without any explanation of how LB-Mini's variable-microbatch assignment is reconciled with collective communication's requirement for equal microbatches across devices. The reader cannot determine whether this is an apples-to-apples baseline (e.g., same sample assignment but forced equal microbatches) or something else entirely. This reduces interpretability of a key comparison. The authors should clarify how this baseline is constructed and whether its limitations are systematically biased for or against ODC.

2. **Headline 36% speedup conflates communication and packing effects.** The abstract claims "up to a 36% speedup over standard FSDP." From Figure 8, the maximum gap appears to be between ODC+LB-Mini and Collective+LocalSort — a comparison that changes *both* the communication scheme and the packing algorithm. The paper does not specify which baseline defines "standard FSDP" in this claim, making it impossible to tell how much comes from ODC's communication change vs. LB-Mini's better packing. While the data in Figure 8 does allow a reader to decompose effects (e.g., ODC+LB-Micro vs. Collective+LB-Micro isolates communication), the headline number bundles both. The authors should state explicitly which comparison yields 36% and report communication-only and packing-only gains separately.

### Minor

3. **Scalability validation limited to 32 GPUs.** The cross-node communication benchmark (§5.4, Figure 11) shows that ODC's point-to-point primitives have significantly lower bandwidth than NCCL collectives once communication spans multiple nodes. The paper discusses mitigation strategies (overlapping with computation, hybrid sharding in §6.1), but the end-to-end experimental validation stops at 32 GPUs (≈4 nodes). While the parametric study suggests the acceleration ratio increases with device count (Figure 10(d)), this trend may not hold at much larger scales where cross-node overhead dominates. The authors should either provide larger-scale experiments or more explicitly bound the regime where ODC is beneficial.

4. **Parametric study reports only acceleration ratios, not absolute throughput.** Figure 10 shows acceleration ratios relative to the collective baseline, but does not report absolute throughput (e.g., samples/second). This makes it impossible to tell whether ODC's absolute performance is increasing or decreasing as parameters vary. For example, when the packing ratio is 8, the acceleration ratio drops to ~15%, but absolute throughput could be much higher than at packing ratio 1 — the reader cannot judge. Including absolute numbers would improve interpretability.

5. **RL evaluation does not test LB-Mini's key advantage.** The paper honestly notes that implementation constraints in verl require identical numbers of samples per device, limiting LB-Mini's effectiveness (§5.2). As a result, the RL results (up to 10% speedup) only demonstrate ODC's communication benefit, not its load-balancing flexibility. This is a scope limitation rather than a flaw, but the paper would be strengthened by a small proof-of-concept demonstrating variable microbatches under ODC in an RL setting.

### Trivial

None.

## Nice-to-Haves

- **Bubble rate (idle time) analysis in the main paper.** The introduction motivates ODC with up to 50% device idle time (Table 6), but the main evaluation does not report bubble rate. Adding this (Appendix G covers it) would directly validate the motivation and isolate where ODC helps.
- **Experimental validation of hybrid sharding.** The paper proposes hybrid sharding to mitigate cross-node overhead (§6.1) and references Appendix E, but does not evaluate it in the main experiments. A single ablation would strengthen the scalability story.
- **Dedicated limitations section.** A brief discussion of when ODC may *not* outperform collectives (short sequences, high packing ratios, large cross-node ratios) would be helpful. The parametric study hints at these but they deserve explicit treatment.
- **Communication overhead analysis.** While ODC does not increase communication volume, the number of messages per device scales differently than collectives. A brief discussion of network contention would aid practitioners.

## Removed Points

These points were flagged in the reviews but are removed or demoted under the filtering rules:

- **Section 2.2 model ignores communication–computation overlap:** The paper already acknowledges overlap and correctly notes it does not remove synchronization points. Strawman — the paper already addresses this.
- **LB-Micro description is vague, lacking algorithm:** The paper defers details to Appendix C, which was stripped by the parser. Not a fair criticism of the existing content.
- **Figure 8 y‑axis values not readable:** Parser artifact — original PDF is assumed to be clear.
- **Section 5.4 synchronous launch is worst-case:** The paper intentionally uses synchronous launch "for fairness" in benchmarking. This is methodologically conservative, not a weakness.
- **Reproducibility statement empty:** Likely a parser artifact; the paper states it will open‑source the implementation.
- **Lightweight daemon details missing:** Deferred to Appendix B (stripped by parser).

## Novel Insights

None beyond the paper's own contributions. The central insight — that FSDP's per-layer collectives are the root cause of idle time under imbalance and can be replaced with point-to-point operations while preserving sharding semantics — is well executed and the paper makes it clearly. The reviews did not surface additional novel observations beyond what the paper itself provides.

## Suggestions

1. **Clarify the "Collective LB-Mini" baseline.** Explain what it means, how the assignment of microbatches works, and any approximations involved. If it forces equal microbatches, state this explicitly.
2. **Decompose the headline speedup.** State which baseline comparison yields the 36% figure, and report the communication-only gain (ODC+LB-Micro vs. Collective+LB-Micro) and the packing-only gain (ODC+LB-Mini vs. ODC+LB-Micro) separately.
3. **Add absolute throughput to the parametric study.** A secondary y‑axis or a table with samples/second for the golden setting would resolve the ambiguity in the acceleration-ratio-only plots.
4. **Add a small variable-microbatch RL experiment.** Even a 2‑device demonstration would confirm that LB-Mini's advantage carries over to RL when the verl constraint is relaxed.
5. **Include bubble rate data in the main paper.** This directly links the measured speedup to the claimed mechanism (reduced idle time).

**Score and Decision**

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>