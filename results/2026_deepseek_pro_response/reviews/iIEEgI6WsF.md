Now let me finalize my analysis and write the complete review.

**Calibration comparison:**

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| `b7HOhqXiZs` (DeMo) | 2.60 | R1 | Different domain, weaker contribution |
| `bntJK4NyIW` (Decentralized Heterogeneous) | 2.00 | R1 | Different domain, clearly weaker |
| `cPZepCZlFW` (PAFT) | 3.25 | R1 | Different domain, weaker |
| `Jl0aEFrp11` (FedBNLACA) | 2.75 | R1 | Federated learning, not comparable |
| `N80ER2he6l` (OMNIBAL) | 5.00 | R1 | Incremental contributions; our paper is technically deeper |
| `ic1Z7Qe9xH` (DYNPIPE) | 3.67 | R1 | Related but weaker contribution |
| `hzQcilRe2v` (DynMo) | 5.25 | R1 | Limited technical innovation; our paper has clearer novelty |
| `7JhGdZvW4T` (TRAIL) | 6.00 | R1/R2 | Similar quality but different domain; our paper has a labeling issue TRAIL doesn't |
| `oVnfVnwh6y` (LASP) | 4.75 | R2 | Weaker contribution, rejected |
| `UV1jr2aJ2J` (ACCO) | 5.00 | R2 | Lacks novelty, weaker experiments; our paper stronger |
| `Z3xg3hxdky` (DSP) | 5.40 | R2 | Communication optimization, rejected; our paper stronger |
| `qDKTMjoFbC` (BurstAttention) | 5.60 | R2 | Limited novelty, insufficient analysis; our paper stronger |
| `lo3nlFHOft` (Decentralized Training) | 6.67 | R2 | Has theoretical analysis we lack; our empirical analysis is better but we sit below this |
| `pAkQhhn4vB` (Micro-batch clipping) | 6.00 | R2 | Not comparable (different domain) |

**Round 1 bracket**: 5.0–6.5
**Round 2 narrowing**: The paper is clearly stronger than ACCO (5.00), OMNIBAL (5.00), DSP (5.40), and BurstAttention (5.60). It is somewhat weaker than the Decentralized Training paper (6.67) due to lacking theoretical analysis and having the Figure 8 labeling issue. It is comparable to TRAIL (6.00) but the Figure 8 contradiction pulls it down slightly. **Final score: 5.5**.

---

## Summary
This paper proposes On-Demand Communication (ODC), which replaces FSDP's per-layer collective operations (all-gather, reduce-scatter) with point-to-point RDMA primitives (gather, scatter-accumulate), relaxing synchronization from per-layer to per-minibatch granularity. ODC enables a simplified minibatch-level load balancing strategy (LB-Mini) that allows different devices to process different numbers of microbatches. Experiments on SFT and RL tasks across model scales 1.5B–32B show up to 36% throughput improvement over standard FSDP.

## Strengths
- **Real problem with clear diagnosis**: The paper identifies that per-layer collective operations in FSDP create synchronization barriers that are "an artifact of the communication model, not a requirement of the training algorithm itself" (Section 3, line 101). The formal model in Equation (1) makes the diagnosis precise and falsifiable.
- **Well-designed parametric study**: Section 5.3 systematically isolates factors (minibatch size, max sequence length, packing ratio, device count) and shows ODC's acceleration ratio tracks theoretical predictions — growing with longer sequences and more devices, shrinking with higher packing ratios. This provides strong evidence that gains come from the claimed mechanism rather than from confounds.
- **Honest treatment of limitations**: Section 5.4 openly benchmarks ODC primitives against NCCL collectives and reports that cross-node bandwidth "lags significantly behind." Section 6.1 discusses practical mitigations (computation-communication overlap, hybrid sharding) rather than overselling.
- **Practical RDMA-based implementation**: The use of CUDA IPC (intra-node) and NVSHMEM (inter-node) via Triton-Distributed for non-intrusive point-to-point transfers avoids the scheduling problems of message-based libraries (MPI, NCCL p2p). The key property — that transfers don't interrupt ongoing computation on the target device — is what makes decoupled execution work in practice.
- **Multi-dimensional evaluation**: Spans two task types (SFT, RL), three datasets with distinct length distributions (LongAlign mean ~16K, SWE-Smith mean ~35K, AIME mean ~9K), four model scales (1.5B–32B), and up to 32 GPUs.

## Weaknesses

### Fatal
None.

### Major
- **Figure 8 labeling contradiction**: The paper states that "LB-Mini can produce different number of microbatches for different devices, it applies only to ODC" (Section 5.1, line 179-180). Yet Figure 8's legend explicitly includes "Collective LB-Mini (purple triangles)" as a plotted method across all eight SFT subplots. This is a direct internal contradiction. Figure 9 (RL) does not have this issue — there the purple triangles are correctly labeled "Collective LB-Micro." The most likely explanation is a figure labeling error (purple triangles = Collective + LB-Micro), but until clarified, the experimental results cannot be taken at face value. If the purple triangles were mislabeled, the natural packed baseline comparison (Collective + LB-Micro vs. ODC + LB-Micro) is obscured. This needs resolution in rebuttal.

### Minor
- **Incomplete synchronization analysis**: The paper claims ODC relaxes synchronization from per-layer to per-minibatch, but the minibatch-end barrier remains and is still governed by the slowest device (line 253: "intentionally preserves a synchronous update at the minibatch boundary"). The paper never quantifies what fraction of idle time comes from within-minibatch barriers (eliminated) vs. the end-of-minibatch barrier (retained). Without this breakdown, it is difficult to assess whether ODC addresses the dominant source of idle time or merely defers it. The throughput gains are real, but the explanatory story is incomplete.

- **PS framing inflates novelty**: The paper markets itself as "revisiting parameter server" and claims ODC "adapts PS into FSDP." But ODC is fundamentally a point-to-point communication scheme within FSDP — there are no separate servers, no asynchrony (it is synchronous at minibatch boundaries), and elasticity is listed as future work. While the decentralized PS analogy provides useful intuition about workload tolerance, the repeated PS branding (abstract, introduction, Section 3.1, conclusion) overstates what the method actually does. The paper would be stronger presenting itself honestly as a point-to-point communication scheme.

- **No comparison to non-packing straggler-mitigation approaches**: The only baselines are FSDP collectives with different packing strategies. Alternative approaches to straggler tolerance (pipeline parallelism schedules, dynamic micro-batching, asynchronous training) are not discussed or compared. Positioning ODC relative to at least one such approach would contextualize the contribution more clearly.

- **Gradient accumulation daemon is underspecified in main text**: Section 3.2 mentions a "lightweight daemon" for gradient accumulation but provides no description of how atomicity is guaranteed when multiple devices push gradients to the same shard concurrently via RDMA. Given that correctness hinges on this mechanism, the main text should at minimum characterize the approach.

### Trivial
- The "device idle times of up to 50%" claim (line 23) references Table 6 in Appendix G; a claim of this magnitude should be supported by data visible in the main text.

## Nice-to-Haves
- Quantify the breakdown of idle time into within-minibatch vs. minibatch-boundary components to strengthen the explanatory story.
- Include abbreviated convergence validation (e.g., a single loss curve) in the main text.
- Discuss the memory overhead of ODC's additional RDMA-exposed buffers relative to standard FSDP.
- Demonstrate at least one inter-node mitigation (e.g., hybrid sharding results) in the main evaluation rather than deferring entirely to appendix.

## Removed Points
These points were considered but removed:

- **"Convergence data in Appendix F is unavailable"** — Removed per hard rule: the appendix exists in the original submission; we cannot penalize the paper for parser-stripped content.
- **"50% idle time claim references Appendix G which is unavailable"** — Removed per hard rule about appendix-deferred content. Retained as Trivial since the claim magnitude warrants main-text support.
- **Demand for ZeRO++ as a baseline** — ZeRO++ addresses communication volume reduction (quantization, hierarchical all-gather), which is orthogonal to ODC's synchronization relaxation via point-to-point primitives. Not a direct baseline, though the paper could discuss the relationship more clearly.
- **"The inter-node communication weakness is not experimentally addressed in main results"** — The paper openly acknowledges this in Section 5.4 and discusses mitigations in Section 6.1. This is honest engineering discussion, not a hidden flaw. Moved to Nice-to-Haves.
- **Typos, formatting issues, parser artifacts** — Removed per hard rules; not present in original submission.
- **"Missing related work" claims** — Removed per hard rules; we cannot verify missing citations.
- **"Implementation details deferred to Appendix B" as a general complaint** — Only the gradient accumulation daemon correctness concern is retained (as Minor) since it is a specific correctness issue. Other implementation details being in appendix is standard practice.
- **"Larger dataset needed / more models needed"** — Generic scale complaint; the dataset variety and model range (1.5B–32B, four scales) is adequate for the paper's claims.
- **"The synchronization model is underspecified" at the level of claiming it's fatal** — Demoted: the paper does describe the synchronization model (line 253 confirms synchronous minibatch boundary), and the throughput measurements demonstrate real gains. The gap is in analysis completeness, not in correctness.

## Novel Insights
The paper's key insight — that per-layer synchronization barriers are an artifact of the communication model (collectives), not a requirement of the training algorithm — is genuinely sharp and shifts the framing from symptom mitigation (packing heuristics) to root-cause elimination (communication primitive swap). The observation that RDMA enables non-intrusive point-to-point transfers where the target device's computation is not interrupted is the technical enabler that makes this insight practical, and it is not obvious from prior work. The parametric study's methodology of fixing a golden setting and varying one factor at a time to isolate causal factors is a model for how systems papers should validate their claims.

## Suggestions
- **Top priority**: Resolve the Figure 8 labeling contradiction. If the purple triangles represent Collective + LB-Micro, relabel them accordingly and explicitly compare Collective + LB-Micro vs. ODC + LB-Micro as the natural packed baseline comparison.
- Add a brief analysis (even a single paragraph with back-of-envelope estimates) of where idle time originates — within-minibatch vs. minibatch-boundary — to strengthen the paper's explanatory story.
- Tone down the PS branding throughout. Lead with the technical mechanism (non-intrusive RDMA point-to-point replacing collectives) and use PS only as an analogy for intuition about workload tolerance, not as a claimed contribution.
- Add a short characterization of the gradient accumulation daemon's atomicity mechanism in the main text.

---

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>