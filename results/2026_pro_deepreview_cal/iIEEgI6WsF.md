Now I have all the evidence I need. Let me write the consolidated review.

---

## Summary
This paper proposes On-Demand Communication (ODC), a communication scheme that replaces FSDP's per-layer collective operations (all-gather, reduce-scatter) with point-to-point RDMA primitives, effectively turning sharded data parallelism into a decentralized parameter server. By relaxing synchronization from the layer level to the minibatch level, ODC mitigates straggler effects caused by variable sequence lengths in LLM post-training, and enables simpler minibatch-level load balancing (LB-Mini). Evaluated across SFT and RL tasks on models from 1.5B to 32B parameters, ODC achieves up to 36% throughput improvement over standard FSDP on SFT workloads.

## Strengths
- **Novel and well-motivated insight**: The paper makes a clean observation—that collective communication in FSDP creates synchronization barriers that are harmful under imbalanced workloads, and that the older parameter server paradigm is naturally better suited for this regime. The adaptation of PS principles into FSDP via point-to-point RDMA is a creative synthesis that none of the cited prior work has proposed in this exact form (Sections 1, 3.1).

- **Thorough and well-controlled SFT evaluation**: The paper evaluates across two SFT datasets (LongAlign, SWE-Smith), four model scales (1.5B–32B), multiple device counts (8–32 GPUs), and three load-balancing strategies (LocalSort, LB-Micro, LB-Mini). The parametric study in Figure 10 systematically isolates the effects of minibatch size, max sequence length, packing ratio, and device count, providing precise insight into when ODC's benefits are largest (Section 5.3).

- **Transparent about limitations**: The paper honestly reports that ODC's point-to-point primitives underperform collectives in cross-node settings (Figure 11), discusses mitigations (overlap, hybrid sharding), and acknowledges that RL gains are modest (up to 10%) due to framework constraints that prevented LB-Mini deployment (Sections 5.2, 6.1). The communication microbenchmarks strengthen credibility.

- **Enables simplified load balancing**: Section 4 clearly demonstrates that removing per-layer synchronization allows load balancing at the coarser minibatch level rather than the microbatch level, and the empirical results (Figure 8, left portions of curves) confirm that LB-Mini outperforms LB-Micro at small minibatch sizes where microbatch-level packing is most constrained.

- **Open-source release**: The implementation is publicly available, which is essential for a systems contribution.

## Weaknesses

### Major
- **RL evaluation is narrow and the gains are modest**: The RL experiments (AIME/GRPO, Figure 9) show only up to 10% speedup, and the more powerful LB-Mini load-balancing strategy could not be deployed due to implementation constraints in the verl framework (the paper acknowledges this explicitly in Section 5.2). Since RL for LLM reasoning is a prominent post-training workload, the paper's claim that ODC is broadly beneficial for LLM post-training rests primarily on SFT evidence. The authors could substantially strengthen their case by either demonstrating that relaxing the verl constraint would recover the larger SFT-level speedups, or by testing on an RL framework that permits LB-Mini.

### Minor
- **Single model family evaluated**: All experiments use the DeepSeek-R1-Distill-Qwen family. While the parametric study varies model size across an order of magnitude (1.5B to 32B), testing on a different architecture (e.g., Llama) would strengthen the claim that ODC's benefits are architecture-agnostic rather than specific to Qwen-style models. The parametric study partially mitigates this concern.

- **Convergence verification not summarized in main text**: The paper states that convergence validation is in Appendix F but provides no summary in the main body. A single sentence confirming that loss curves match between ODC and collective baselines would provide minimal reassurance to readers who cannot access the stripped appendix.

- **Memory overhead not discussed**: The gradient accumulation daemon and additional communication buffers likely introduce some memory overhead. Given that FSDP is memory-sensitive, even a brief note on the memory footprint would help practitioners assess tradeoffs.

### Trivial
- No measure of variance or number of runs is reported for throughput benchmarks. For systems papers evaluating throughput on fixed hardware, this is a minor omission but worth noting.

## Nice-to-Haves
- A direct measurement of device idle time (bubble/straggler time) for a representative workload in both collective and ODC settings would make the mechanism of speedup concrete. Currently the evaluation relies on throughput alone; a profile showing how ODC shrinks the gap between slowest and fastest device would be compelling.
- Extending the communication microbenchmarks (Figure 11) to include latency measurements and an analysis of how the bandwidth gap changes with the number of outstanding requests would provide deeper insight into ODC's communication characteristics.
- A brief discussion of floating-point sensitivity when gradient accumulation order differs between ODC and collective baselines would preempt concerns about training fidelity, though the Appendix F convergence check likely addresses this.

## Removed Points
These points are flagged to be removed, treat them with caution:

- *"The paper omits important details about the gradient accumulation daemon (e.g., how it ensures atomic updates without stalling parameter reads, how it interacts with CUDA streams)"* — The paper references Appendix B for detailed implementation information and the main text describes the key architectural choices (RDMA via CUDA IPC/NVSHMEM, Triton-Distributed kernels). This is standard practice for a systems paper; the level of detail in the main text is adequate for understanding the design.

- *"The paper does not provide a full problem formulation or analyze the optimality of the proposed [load balancing] algorithm"* — The harsh critic themselves notes this is acceptable since the main contribution is the communication scheme. Changed from a weakness to a removed point.

- *"The abstract and conclusion could be read as claiming that 36% is typical"* — The abstract uses "up to 36% speedup," which is factually accurate. The parametric study (Section 5.3, Figure 10) exhaustively documents how the acceleration ratio varies with all relevant factors. The framing is appropriate.

## Novel Insights
None beyond the paper's own contributions. The paper's core observation—that the PS paradigm is naturally more tolerant of workload imbalance than collective communication, and that this tolerance can be retrofitted into modern sharded DP—is itself the novel insight.

## Suggestions
- Patch the verl framework (or use an alternative RL framework) to enable LB-Mini and report the resulting speedup. Even a minimal patch demonstrating the expected gain would substantially close the most significant evidential gap.
- Add one sentence to the main text summarizing the convergence verification from Appendix F (e.g., "loss curves between ODC and the collective baseline are indistinguishable").
- Add a brief note on memory overhead of the daemon and communication buffers relative to standard FSDP.
- Consider testing on at least one model from a different architecture family (e.g., Llama-7B) to demonstrate architecture independence, even if only for a single representative configuration.

## Score and Decision

### Calibration Anchors

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| GFLAgent (ArJikvI6xo) | 3.40 | 1 (bracket) | Far weaker: poor evaluation, unclear method. ODC is clearly superior. |
| SPD (uoU4ypjAmN) | 4.00 | 1 (bracket) | Weaker: missing end-to-end latency comparison, unclear writing. ODC has much stronger evaluation. |
| DSP (Z3xg3hxdky) | 5.40 | 2 (narrow) | Weaker: related to sequence parallelism but less thorough evaluation. ODC is stronger. |
| BurstAttention (qDKTMjoFbC) | 5.60 | 2 (narrow) | Weaker: similar domain (long-sequence distributed training) but less comprehensive comparison. |
| From Promise to Practice (lo3nlFHOft) | 6.67 | 2 (narrow) | Comparable: both address communication in distributed training with good empirical evaluation. FtPtP has theoretical convergence analysis; ODC has a more novel core idea. |
| CO2 (ZO5cn4IfaN) | 7.00 | 2 (narrow) | Slightly above: CO2 has broader experiments (CV + NLP) and theoretical convergence analysis, but its core idea (local SGD + async) is more incremental. ODC's PS-for-FSDP insight is more creative but evaluation is narrower. |
| NetMoE (1qP3lsatCR) | 7.20 | 2 (narrow) | Above: cleaner optimization formulation (ILP), rigorous problem modeling. ODC is empirically strong but lacks comparable theoretical depth. |
| QSR (yroyhkhWS6) | 6.75 | 2 (narrow) | Comparable: theory-grounded approach to synchronization frequency. Different style; ODC is more systems-focused. |

**Round-1 bracket**: 5.5–7.5. The paper is clearly above the 3–4 range (GFLAgent, SPD) and below the 7.5+ range (anchors like FlexPrefill at 8.0).  
**Round-2 narrowing**: The paper lands between BurstAttention (5.60) and NetMoE (7.20), comparable to "From Promise to Practice" (6.67) and CO2 (7.00). ODC's core idea is more novel than CO2's but it lacks theoretical analysis and the RL evidence is weaker. The single-model-family limitation and sparse convergence reporting in the main text pull the score slightly below CO2. NetMoE (7.20) has stronger theoretical grounding and cleaner problem formulation. **Final score: 6.5**.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>