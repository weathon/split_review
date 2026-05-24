Now I have a thorough understanding of the paper and all reviewer claims. Let me construct the final consolidated review.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses
### Fatal
### Major
### Minor
### Trivial

## Nice-to-Haves

## Removed Points

## Novel Insights

## Suggestions

## Score and Decision

Let me write the review:

## Summary

This paper identifies that per-layer collective communication (all-gather/reduce-scatter) in FSDP creates synchronization barriers that are harmful under imbalanced workloads common in LLM post-training, where sequence lengths vary widely. The authors propose On-Demand Communication (ODC), which replaces collectives with point-to-point gather/scatter-accumulate primitives, reframing FSDP as a decentralized parameter server. ODC relaxes synchronization from the layer level to the minibatch level, decouples device progress, and enables simpler minibatch-level load balancing. Experiments across SFT and RL tasks show consistent throughput improvements of up to 36% over standard FSDP.

## Strengths

1. **Formal model identifies the root cause of inefficiency**: Equation (1) expresses minibatch runtime as the sum over layers of the maximum device time per layer, formally proving that per-layer collectives force faster devices to wait for the slowest one at every layer. This analytical grounding is stronger than prior work that treated imbalance purely as a packing problem.

2. **Consistent throughput gains across diverse settings**: Figure 8 shows ODC achieving up to 36% speedup over collective FSDP on the SWE-Smith dataset with a 7B model, and the benefit holds across model sizes from 1.5B to 32B, two SFT datasets, and RL tasks (up to 10% speedup in Figure 9). The improvements are systematic, not cherry-picked.

3. **Parametric study convincingly characterizes when ODC helps**: Figure 10 systematically varies minibatch size, sequence length, packing ratio, and device count. The acceleration ratio grows with sequence length (from ~25% at 8K to ~35% at 128K) and device count (from ~25% on 1 device to ~35% on 32), confirming that ODC's benefit increases precisely where workload imbalance is worst.

4. **Principled architectural contribution**: The reframing of FSDP as a decentralized parameter server (Section 3.1, Figure 6) provides a clean conceptual bridge between classic PS ideas and modern sharded DP. The design is simple: replace collective calls with point-to-point operations without changing FSDP's memory layout or computational graph. Implementation on Triton-Distributed avoids low-level CUDA code, lowering the adoption barrier.

5. **Intra-node bandwidth comparable to NCCL collectives**: Figure 11 shows that ODC's point-to-point primitives achieve bandwidth on par with all-gather and reduce-scatter within a single node, demonstrating that performance gains come from workload decoupling, not from faster raw communication. The paper honestly acknowledges the cross-node bandwidth disadvantage (Section 5.4, Section 6.1) and discusses mitigation strategies.

## Weaknesses

### Fatal
None.

### Major

- **Communication-computation overlap is asserted but not directly validated**: The paper argues (Section 6.1) that ODC's slower cross-node point-to-point communication is hidden by overlap with computation, because communication volume per microbatch is constant in sequence length while computation scales as O(s²). However, no per-device timeline traces, Nsight profiles, or other direct evidence of this overlap is provided in the main text. The paper references bubble rates in Appendix G and claims "ODC shows no significant slowdown in our long-context evaluations," but without profiling data, the mechanism by which ODC overcomes its 3× cross-node bandwidth disadvantage (Figure 11) remains an untested hypothesis. This is the single largest gap in the evidence: the end-to-end speedups are measured, but the paper's explanation for *why* they hold despite slower cross-node primitives is not empirically supported. Providing timeline traces would substantially strengthen the paper.

### Minor

- **LB-Micro is an author-designed packing baseline**: The primary packing baseline (LB-Micro) is a heuristic designed by the authors. While they demonstrate it outperforms the native verl implementation, and the key comparison (ODC+LB-Micro vs Collective+LB-Micro) isolates the communication effect cleanly, the paper does not compare against more sophisticated packing algorithms from recent work. Since the core contribution is the communication scheme rather than the packing algorithm, this does not threaten the main claims but limits the characterization of how much the improved load balancing alone contributes.

- **Single-run results without variance reporting**: Throughput results in Figures 8-10 are from single runs without confidence intervals or error bars. At the scale of these experiments (up to 32 A100 GPUs), multiple runs are expensive, and single-run reporting is common in systems papers. However, given the stochastic nature of system performance (communication latencies, memory bandwidth contention), this limits the reader's ability to assess the stability of the reported speedups.

### Trivial
None.

## Nice-to-Haves

- **Timeline profiling (Nsight Systems or Chrome tracing)** for a representative minibatch under both FSDP and ODC would directly validate that communication is overlapped and show exactly how much idle time is eliminated.
- **Convergence curves** from Appendix F (training loss/validation accuracy over a full run) would address the theoretical concern about non-deterministic gradient accumulation order, if not already present in the appendix.
- **Sensitivity experiments with shorter sequences** (e.g., 2K-4K tokens) where the quadratic compute advantage is minimal, to show the boundary condition where ODC breaks even or loses.

## Removed Points

These points are flagged to be removed, treat them with caution:

1. **"Gradient accumulation order changes and potential convergence impact not addressed"** — The paper explicitly states (line 181) "we validate the correctness of ODC by verifying the training convergency in Appendix F." The claim "preserves synchronous optimization semantics" refers to the minibatch-level synchronization boundary (Section 3, line 107: "without altering the training semantics"), not to bitwise-identical gradients. Gradient non-determinism already exists in standard NCCL all-reduce across different runs. Convergence validation exists in the original appendix (Appendix F), which the parser has stripped.

2. **"No comparison against state-of-the-art packing from LongAlign"** — Factually incorrect. The paper's LocalSort baseline is explicitly "adapted from Bai et al. (2024)" (line 183), which is the LongAlign paper. The paper also cites LongAlign for its dataset and packing context (line 155).

3. **"Synchronous benchmark may overestimate real-world performance"** — The synchronous benchmark in Figure 11 provides a conservative (lower-bound) estimate of raw bandwidth. If ODC overlaps communication with computation, effective communication overhead would be lower than the benchmark suggests, making this criticism directionally wrong.

4. **"Overstates degree to which prior work ignored imbalance"** — Subjective opinion, not a verifiable weakness.

5. **"Implementation details from Appendix B stripped"** and similar appendix-related complaints — Parser artifact; appendices exist in the original submission.

6. **"Insufficient comparison to packing methods"** — The paper's primary contribution is the communication scheme (ODC). The comparison that matters most is ODC+LB-Micro vs Collective+LB-Micro (same packing, different communication), which is provided. Improved load balancing (LB-Mini) is a secondary benefit, not the core claim.

7. **"No statistical significance or variance reporting"** — Single-run evaluation is standard practice for systems papers at this scale (32 GPUs, large models). Moved to Minor weakness for completeness.

## Novel Insights

None beyond the paper's own contributions. The core insight — that per-layer collectives are the wrong abstraction for imbalanced workloads and that replacing them with point-to-point PS-style communication is a clean solution — is the paper's main contribution and is well-articulated.

## Suggestions

1. **Add a timeline trace figure** (e.g., Nsight Systems profile) for one representative setting showing per-device activity over time under FSDP vs. ODC. This single addition would directly validate the communication-computation overlap claim and make the paper much stronger.

2. **Report bubble rates or idle time percentages** in the main text (these are referenced as being in Appendix G) to give readers a concrete quantitative sense of how much idle time ODC eliminates.

3. **Include error bars or min/max ranges for key results** if practical. Even two runs per setting would help establish stability.

4. **Add a brief note in Section 6.1** clarifying that the numerical differences from non-deterministic gradient accumulation order are bounded and standard in distributed training (e.g., NCCL also has non-deterministic accumulation order), and reference the convergence validation in Appendix F.

## Score and Decision

This paper presents a clean, well-motivated contribution with a principled architectural insight and consistently positive experimental results across multiple tasks, model sizes, and datasets. The main weakness — absence of direct profiling evidence for the communication-computation overlap claim — is real but not fatal; the end-to-end throughput measurements are valid, and the parametric study convincingly shows the benefit scales with the factors that drive imbalance. The paper is above the acceptance threshold for a venue like ICLR.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>