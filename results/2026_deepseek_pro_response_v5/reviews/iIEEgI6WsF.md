Now I have a clear picture of where this paper sits relative to anchors. Let me compile the final review.

## Summary
This paper proposes On-Demand Communication (ODC), a communication scheme that replaces FSDP's per-layer collective all-gather and reduce-scatter with point-to-point RDMA primitives (gather, scatter-accumulate). The key insight is that LLM post-training workloads are imbalanced due to variable sequence lengths, and FSDP's fine-grained synchronization barriers cause substantial device idle time. ODC reframes FSDP as a decentralized parameter server by colocating server/worker roles within FSDP's sharded memory layout, relaxing synchronization from the layer level to the minibatch level. This also enables a simpler minibatch-level load-balancing strategy (LB-Mini). Across SFT and RL benchmarks on 1.5B–32B models, ODC achieves up to 36% throughput improvement over standard FSDP with consistent gains across all tested settings.

## Strengths
- **Formal characterization of the synchronization bottleneck**: Equation (1) in Section 2.2 captures minibatch runtime as bounded by the per-layer slowest device: \(T(\mathcal{P}_M) = \sum_{m=1}^M \sum_{l=1}^L \max_d T_{m,d,l}(\mathcal{P}_M)\). This directly motivates relaxing synchronization to the minibatch level.
- **Novel conceptual synthesis of PS and FSDP**: Section 3.1 reframes FSDP as a decentralized PS by colocating server and worker roles within FSDP's existing sharded memory layout. The paper explicitly acknowledges precedent (Jiang et al., 2020) but correctly claims novelty in directly integrating with FSDP's sharding mechanism. This insight is the paper's core intellectual contribution and is genuinely original.
- **Consistent and substantial empirical throughput gains**: Figures 8–9 demonstrate ODC never underperforms collectives and delivers meaningful speedups across three datasets (LongAlign, SWE-Smith, AIME), four model scales (1.5B–32B), two training paradigms (SFT and RL), and multiple load-balancing strategies. Gains reach 36% on packed SFT workloads. Crucially, ODC+LocalSort (no packing) still outperforms Collective+LocalSort, isolating the communication scheme's benefit from packing.
- **Informative parametric study**: Section 5.3 and Figure 10 systematically isolate four factors (minibatch size, max sequence length, packing ratio, device count) from a fixed golden setting (Table 1). Trends are intuitive and actionable: ODC's acceleration grows with sequence length and device count (factors that amplify imbalance) and shrinks with packing ratio — giving practitioners clear deployment guidance.
- **Transparent accounting of communication overhead**: Section 5.4 and Section 6.1 honestly report that ODC's point-to-point primitives underperform NCCL collectives in cross-node settings, and discuss concrete mitigations (computation-communication overlap exploiting \(O(s^2)\) compute vs. constant communication, hybrid sharding à la ZeRO++).

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
- **Gradient accumulation under heterogeneous microbatch counts could be more explicit**: LB-Mini allows different devices to process different numbers of microbatches, which drives the largest speedups. The paper mentions weighted aggregation in Section 2.1 (\(\bar{g} = \sum w_m g^{(m)}\) with \(w_m\) encoding the aggregation policy), and the scatter-accumulate mechanism naturally handles this. However, a concise paragraph in the main text confirming how correct training semantics are preserved (e.g., weighting by token counts when different devices contribute different numbers of gradient steps) would strengthen confidence in the paper's strongest results, given that detailed algorithms are deferred to Appendix C.
- **Transport-vs-pattern confound partially addressed but not explicitly discussed**: Section 5.4 benchmarks ODC primitives against NCCL collectives under synchronized conditions, showing comparable intra-node bandwidth. The parametric study (Figure 10) further shows ODC's advantage grows with factors that amplify imbalance rather than raw bandwidth differences. However, the paper does not explicitly discuss the extent to which RDMA transport characteristics (CUDA IPC / NVSHMEM) vs. the relaxed synchronization pattern contribute to observed speedups. A brief discussion would sharpen the causal argument.

### Trivial
- **Possible figure legend discrepancy in Figure 8**: The parser-extracted figure description lists "Collective LB-Mini" among the five compared methods, but Section 5.1 explicitly states LB-Mini applies only to ODC (line 179–180). This is likely a parser artifact (the actual figure caption likely shows "Collective LB-Micro"), but the authors should verify the original figure legend is correct.

## Nice-to-Haves
- Moving a summary convergence plot and timing breakdown (currently in Appendices F and G) into the main text would strengthen the evidence presentation.
- Quantifying how much faster LB-Micro is than the native verl implementation (mentioned qualitatively on line 179) would contextualize baseline strength.
- A brief discussion of how ODC interacts with FSDP features like mixed precision and activation checkpointing would help practitioners.

## Removed Points
These points are flagged to be removed, treat them with caution.

- **"Gradient accumulation across heterogeneous microbatch counts is under-specified (evidential gap)" — downgraded from the harsh critic's fatal framing**: The paper does address gradient weighting in Section 2.1 (weighted accumulation formula). The mechanism (scatter-accumulate to the parameter-owning device, with proper weighting) is straightforward and consistent with standard gradient accumulation. The harsh critic framed this as a potentially fatal evidential gap, but the paper's description covers the essential correctness argument; more detail would help but its absence does not undermine the core claims.
- **"Transport and communication pattern are conflated" — downgraded from harsh critic's major framing**: Section 5.4 explicitly benchmarks primitives under synchronized conditions, and the parametric study isolates imbalance-dependent factors. The paper honestly reports comparable intra-node bandwidth. The harsh critic's demand for a completely isolated experiment (same transport for both patterns) misunderstands that NCCL p2p may not support the non-intrusive RDMA semantics ODC requires.
- **"Integration is straightforward undersells complexity" — removed**: This is a subjective stylistic concern. The paper describes the implementation stack (CUDA IPC, NVSHMEM, Triton-Distributed) in sufficient detail for a conference submission.
- **"Appendix G bubble rate data is stripped" — removed**: Parser artifact; the appendix exists in the original submission.
- **"Missing related work" from harsh critic — removed per hard rules**: No specific missing works identified, and this falls under the rule to not mention missing related works.
- **Generic formatting/style concerns — removed**: These are parser artifacts, not author errors.
- **Strength Finder sycophantic/non-specific strengths removed**: Dropped "pragmatic, low-friction implementation" (too generic without concrete quantification) and partially qualifying statements that overstate contribution scope.

## Novel Insights
The paper's reframing of FSDP as a decentralized parameter server (Section 3.1) is genuinely novel: by recognizing that FSDP's sharded memory layout already mirrors a PS with colocated server/worker roles, the paper shows that only the communication primitive needs to change — from collectives to point-to-point — to gain workload-imbalance tolerance. This is a clean conceptual insight that bridges two historically separate paradigms in distributed training and directly motivates a minimal, practical implementation change rather than a complete system redesign. The observation that minibatch-level synchronization is sufficient for correctness while layer-level synchronization is merely an artifact of the collective communication pattern is both simple and deep.

## Suggestions
- Add a short paragraph in the main text (Section 4 or 5.1) explicitly confirming that LB-Mini's gradient accumulation preserves correct training semantics via weighted aggregation, as already noted in Section 2.1. This would preempt the most likely reviewer concern.
- Add a sentence in Section 5.4 or the discussion explicitly noting that the parametric study results (acceleration grows with sequence length and device count) provide evidence that synchronization reduction, not transport differences, is the primary driver of ODC's speedup.
- Verify the Figure 8 legend does not include "Collective LB-Mini" given LB-Mini is ODC-only.

## Calibration and Score

**Round 1 bracket**: Based on comparison with anchors across all score bands, the paper clearly falls in the 6.0–7.5 range. It is substantially stronger than ACCO (5.00, rejected for limited novelty and weak experiments) and comparable to the accept-tier papers in the 6.5–7.0 range.

**Round 2 narrowing**: Comparing against specific anchors:
- **vs. "From Promise to Practice" (6.67)**: Both are well-executed systems papers on distributed training. ODC has a cleaner and more novel core insight (decentralized PS reframing), while "From Promise to Practice" has a convergence proof. ODC's empirical evaluation is comparably thorough. ODC is slightly stronger on novelty, similar on empirical quality. **ODC ≥ 6.67.**
- **vs. CO2 (7.00)**: CO2 has theoretical convergence guarantees and broader experiments (CV + NLP, 128 GPUs). ODC's insight is more conceptually novel but lacks theoretical depth. CO2 has a stronger paper overall. **ODC < 7.00.**
- **vs. Zero Bubble (7.00)**: Both have a "splitting/reorganizing" insight that yields practical gains. Zero Bubble has tighter mathematical analysis and a more complete story. **ODC ≈ Zero Bubble on insight quality, slightly weaker on theoretical depth.**
- **vs. QSR (6.75)**: Both have a clean idea with solid empirical validation and some scope limitations. QSR has theoretical backing but is somewhat incremental on prior work. ODC is more original but lacks theory. **Comparable quality.**

**Final score**: ODC sits at approximately 6.5. It is a solid accept with a genuinely novel contribution, strong empirical results, and honest limitations. It falls short of the 7.0 tier primarily due to the absence of theoretical analysis and the modest scope of RL results. The weaknesses are minor and addressable.

### Anchor Papers Summary
| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| CO2 (ZO5cn4IfaN) | 7.00 | R1/R2 | Stronger: has convergence proof, broader experiments |
| Zero Bubble (tuzTN0eIO5) | 7.00 | R2 | Slightly stronger: tighter analysis, comparable insight |
| QSR (yroyhkhWS6) | 6.75 | R2 | Comparable: clean idea, good experiments, some scope limits |
| From Promise to Practice (lo3nlFHOft) | 6.67 | R1/R2 | Comparable: ODC more novel, FPTP has theory |
| SEPARATE (8HuLgtjqOD) | 6.00 | R1 | ODC is stronger: more novel, better evaluation |
| BurstAttention (qDKTMjoFbC) | 5.60 | R2 | ODC is clearly stronger |
| ACCO (UV1jr2aJ2J) | 5.00 | R1 | ODC is clearly stronger |
| DynMo (hzQcilRe2v) | 5.25 | R2 | ODC is clearly stronger |
| LEGACY (Xxpt66OgHI) | 4.33 | R1 | ODC is clearly stronger |
| Compressed Decentralized (zqXANcFO9T) | 1.67 | R1 | ODC is clearly stronger |

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>