Now I have enough data to calibrate. Let me write the final review.

## Summary
The paper proposes On-Demand Communication (ODC), which replaces FSDP's per-layer collective operations (all-gather, reduce-scatter) with point-to-point gather and scatter-accumulate operations, relaxing synchronization from the layer level to the minibatch level. This reframes FSDP as a decentralized parameter server, decoupling device progress and enabling simpler minibatch-level load balancing. The evaluation demonstrates consistent throughput improvements across SFT and RL tasks with models from 1.5B to 32B parameters.

## Strengths
- **Well-motivated, precise diagnosis of the synchronization bottleneck**: The paper formalizes the problem with Equation 1 (minibatch runtime bounded by slowest device at each layer step) and reports device idle times up to 50% even with state-of-the-art packing (Table 6, referenced in Section 1). The argument that per-layer synchronization is an *artifact of the communication model, not a requirement of the training algorithm* (Section 3, line 101) is a clean, well-articulated insight that gives the ODC design a clear target.

- **Substantial, consistent throughput improvements across diverse settings**: Figure 8 shows up to 36% speedup on SFT tasks across LongAlign and SWE-Smith datasets, four model scales (1.5B–32B), up to 32 GPUs, and multiple minibatch sizes. Figure 9 shows up to 10% on RL tasks. Gains are demonstrated across both packed and unpacked settings, showing robustness.

- **Systematic parametric study isolating key design factors**: Section 5.3 and Figure 10 vary one factor at a time (minibatch size, max sequence length, packing ratio, device count) from a fixed golden setting (Table 1), providing clear practitioner guidance on when and why ODC helps most—for instance, acceleration increases with sequence length (from ~25% at 8K to ~35% at 128K) and device count, both consistent with the theoretical motivation.

- **Novel conceptual reframing of FSDP as decentralized PS**: Section 3.1 and Figure 6 articulate how ODC retains FSDP's memory layout and sharding while gaining PS-style imbalance tolerance through colocated server/worker roles. The direct integration with FSDP's sharding mechanism distinguishes it from prior colocated PS systems (citing Jiang et al., 2020).

- **Transparent characterization of communication bandwidth limitations**: Section 5.4 and Figure 11 honestly report that ODC's point-to-point RDMA lags behind optimized collectives in inter-node settings, combined with concrete mitigation strategies (communication overlap, hybrid sharding) discussed in Section 6.1.

## Weaknesses

### Fatal
None.

### Major
- **The headline 36% speedup is ambiguously scoped and likely conflates two factors**: The abstract and Section 5.2 claim "up to a 36% speedup" without specifying which comparison yields this number. Figure 8 includes five SFT configurations: ODC+LB-Mini, ODC+LB-Micro, Collective+LB-Mini, ODC+LocalSort, and Collective+LocalSort. If the 36% comes from comparing ODC+LB-Mini vs. Collective+LocalSort, it changes *both* the communication scheme and the load-balancing algorithm, conflating two separate improvements. The paper should explicitly decompose the headline figure into (a) the communication-only benefit (e.g., ODC+LB-Mini vs. Collective+LB-Mini) and (b) the additional LB benefit enabled by ODC. This matters because the paper's thesis is that the communication change is the key contribution, so demonstrating its isolated benefit should be central to the evaluation.

- **Missing Collective+LB-Micro comparison in SFT evaluation (Figure 8)**: Collective+LB-Micro is the most natural baseline for isolating the communication effect while using the same packing algorithm. It appears in Figure 9 (RL) but is absent from Figure 8 (SFT), even though SFT is where the largest gains are reported. Its omission makes it harder to understand the isolated contribution of the communication change in the paper's strongest result.

### Minor
- **Internal inconsistency about LB-Mini applicability**: Section 5.1 states "As LB-Mini can produce different number of microbatches for different devices, it applies only to ODC." Yet Figure 8 includes "Collective LB-Mini" as one of the five compared methods. If LB-Mini was tested with collectives as an ablation, the text should explain rather than contradict; if the figure label is a mistake, it should be corrected. This confuses the reader about what is actually being compared.

- **No error bars or variance across runs**: All throughput measurements are reported as single points. Even a few repeated runs with standard deviations would increase confidence in the reported speedup magnitudes, especially for the headline 36% claim.

- **Multi-node mitigation evidence deferred to appendix**: Section 6.1 and Figure 11 acknowledge that ODC's point-to-point primitives have significantly lower bandwidth than NCCL collectives in multi-node settings. Mitigation strategies (overlapping communication with computation, hybrid sharding) are proposed but their results are deferred to Appendix E. Since the main experiments include multi-node configurations (14B on 16 GPUs, 32B on 32 GPUs), showing at least one representative mitigation result in the main text would strengthen the paper's multi-node claims.

### Trivial
None.

## Nice-to-Haves
- A brief analysis or measurement of peak memory usage vs. FSDP would strengthen the practical contribution. The paper claims ODC "preserves FSDP's memory layout" (line 103) but doesn't empirically verify whether the changed timing of parameter materialization affects peak memory.
- Including bubble rate / idle time measurements in the main text (currently referenced as Appendix G) would make the core motivation more directly verifiable by readers.

## Removed Points
These points are flagged to be removed, treat them with caution:
- **Critic's claim about Table 6 being in stripped appendix**: The harsh critic notes Table 6 (idle times up to 50%) is in the stripped appendix. Per rules about missing appendices, this is a parser issue—the table exists in the original submission. Remove.

## Novel Insights
The paper's most genuinely novel insight is the recognition that FSDP's per-layer synchronization barriers are an artifact of the communication model rather than a requirement of the training algorithm—and therefore fundamentally avoidable. This is a clean systems insight that reframes a well-known limitation of collective-based DP as a solvable design choice. The connection to the classical parameter server paradigm (Section 3.1) and the demonstration that PS principles can be retrofitted into FSDP without changing the memory layout or sharding mechanism is a meaningful conceptual contribution to distributed training systems.

## Suggestions
- Add the Collective+LB-Micro comparison to Figure 8 (SFT) and explicitly decompose the 36% headline into communication-only and LB-enabled components.
- Move at least one representative inter-node mitigation result from Appendix E into the main text.
- Resolve the textual inconsistency between Section 5.1 ("LB-Mini applies only to ODC") and Figure 8 (which shows "Collective LB-Mini").

## Calibration Report

### Anchors Retrieved

**Round 1 (Bracketing):**
| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| bntJK4NyIW | 2.00 | 1 | Decentralized training in heterogeneous networks — much weaker contribution, poor evaluation, rejected. |
| b7HOhqXiZs | 2.60 | 1 | DeMo: Decoupled Momentum — rejected, lower quality, less practical. |
| cPZepCZlFW | 3.25 | 1 | Fault-tolerant distributed training — rejected, narrower contribution. |
| cSnbM9SIJJ | 3.00 | 1 | Multi-agent simulation — unrelated, rejected. |
| ic1Z7Qe9xH | 3.67 | 1 | Elastic Load Balancing for Dynamic LLMs — rejected, limited novelty, unclear evaluation. Much weaker than paper under review. |
| lo3nlFHOft | 6.67 | 1 | From Promise to Practice: Decentralized Training — accepted, comparable systems contribution but uses somewhat obsolete setup. Paper under review is more targeted and practically relevant. |
| ZO5cn4IfaN | 7.00 | 1 | CO2: Communication-Computation Overlap — accepted, comparable scope and weaknesses (memory analysis, error bars missing). Paper under review has cleaner, more novel insight. |
| qDKTMjoFbC | 5.60 | 1 | BurstAttention — rejected, related but weaker contribution. |
| vf5aUZT0Fz | 8.00 | 1 | DEPT — accepted but about embedding decoupling, less directly comparable. |
| OfjIlbelrT | 8.00 | 1 | FlexPrefill — accepted, inference-time attention, not comparable. |
| ZuazHmXTns | 7.60 | 1 | Problem-Parameter Free FL — accepted, federated learning, less comparable. |
| f4gF6AIHRy | 8.00 | 1 | DiSF — accepted, data selection, not comparable. |

**Round 2 (Narrowing):**
| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| N80ER2he6l | 5.00 | 2 | OMNIBAL — rejected, workload balancing for VLMs. Weaker evaluation, less clean contribution. |
| Z3xg3hxdky | 5.40 | 2 | DSP: Dynamic Sequence Parallelism — rejected, different focus but weaker evaluation. |
| oVnfVnwh6y | 4.75 | 2 | LASP: Linear Attention Sequence Parallelism — rejected, narrower scope. |
| kC5i5X9xrn | 5.00 | 2 | LightSeq — rejected, sequence-level parallelism. Not novel enough, questionable setups. Paper under review is clearly stronger. |
| ZO5cn4IfaN | 7.00 | 2 | CO2 (retrieved again) — accepted. Paper under review has cleaner insight and more targeted evaluation. |
| lo3nlFHOft | 6.67 | 2 | From Promise to Practice (retrieved again) — accepted. Paper under review is more practically relevant. |
| yroyhkhWS6 | 6.75 | 2 | Quadratic Synchronization Rule — accepted, theory-grounded local SGD. Comparable quality but different focus. |
| tuzTN0eIO5 | 7.00 | 2 | Zero Bubble Pipeline Parallelism — accepted, novel scheduling, good evaluation. Comparable contribution quality. |

### Score Calibration
- **Round 1 bracket**: The paper clearly sits between the rejected papers (~3.5–5.5) and the strong accepted papers (~7.5+), placing it in the **6.0–7.5** range.
- **Round 2 narrowing**: Compared to CO2 (7.00) and Zero Bubble (7.00), the paper under review has a cleaner, more novel insight (reinterpreting FSDP as decentralized PS) and more targeted evaluation (LLM post-training with variable-length sequences). It shares similar weaknesses (missing error bars, memory analysis deferred). Compared to LightSeq and OMNIBAL (5.00, rejected), the paper under review is clearly stronger in contribution clarity and evaluation rigor.
- **Final positioning**: The paper is slightly above CO2 (7.00) in terms of insight novelty and practical relevance, but has a genuine evaluation clarity issue (headline number ambiguity, missing baseline in SFT). I place it at **7.0**, matching CO2 and Zero Bubble.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>