Now I have all the evidence I need. Let me compile the final review.

## Summary

This paper identifies a genuine inefficiency in FSDP for LLM post-training: the per-layer collective synchronization barriers create idle time under imbalanced workloads (caused by variable sequence lengths). The proposed solution, On-Demand Communication (ODC), replaces collective all-gather/reduce-scatter with point-to-point gather/scatter-accumulate primitives adapted from the parameter-server paradigm. The key idea is sound and well-motivated: ODC relaxes synchronization from per-layer to per-minibatch, decouples device progress, and enables simpler minibatch-level load balancing (LB-Mini) that is infeasible under collectives. Experiments on SFT and RL tasks across model sizes 1.5B–32B show consistent throughput improvements over standard FSDP, with up to 36% speedup.

## Strengths

1. **Clear identification of a real problem with a principled solution.** The paper formalizes (Eq. 1) how per-layer collectives in FSDP create synchronization barriers under imbalanced workloads, and ODC directly addresses the root cause by replacing them with point-to-point operations. The framing of ODC as a decentralized parameter server colocated within FSDP's sharding layout is both elegant and practical (Section 3.1, Figure 6).

2. **Consistent throughput gains across diverse tasks and scales.** Figure 8 shows ODC outperforming collective baselines in every configuration on SFT (LongAlign, SWE-Smith) across 1.5B–32B models with up to 36% speedup. Figure 9 extends this to RL (GRPO on AIME), achieving up to 10% speedup over the best collective baseline. The parametric study in Figure 10 systematically validates the conditions under which ODC's advantage grows (longer sequences, more devices, moderate minibatch sizes), substantiating the claimed mechanism.

3. **Enables a simpler and more effective load-balancing strategy (LB-Mini)** that is infeasible under collective communication (Section 4). Because ODC decouples device execution, workloads can be balanced at the minibatch level rather than the microbatch level, allowing devices to process different numbers of microbatches. Figure 8 shows this yields meaningful gains at small minibatch sizes (e.g., ≈20% over ODC+LB-Micro at minibatch=2 on 1.5B).

4. **Practical implementation and open-source release.** The implementation leverages CUDA IPC and NVSHMEM for RDMA-based point-to-point communication, built on Triton-Distributed. Figure 11 shows that within a single node, ODC primitives achieve bandwidth comparable to NCCL collectives. The code is open-sourced at the provided repository.

5. **Well-structured parametric study** (Figure 10) that isolates the impact of minibatch size, sequence length, packing ratio, and device count, confirming that ODC's advantage grows exactly in the regimes where imbalance is worst.

## Weaknesses

### Fatal
None.

### Major

1. **Unexplained "Collective LB-Mini" baseline in Figure 8.** Section 5.1 explicitly states: "As *LB-Mini* can produce different number of microbatches for different devices, it applies only to ODC." Yet Figure 8 plots a method labeled "Collective LB-Mini" (purple triangles) and compares it against ODC variants. The paper provides no explanation of how this baseline was constructed, what guarantees its validity, or even whether it represents a real collective-compatible variant of minibatch-level balancing. Given that the paper itself argues LB-Mini is fundamentally incompatible with collectives, the presence of this baseline without clarification is confusing and undermines reader confidence in the experimental design. **The core claim (ODC outperforms collectives) does not collapse without this baseline** — the comparisons ODC+LB-Micro vs Collective+LB-Micro and ODC+LocalSort vs Collective+LocalSort already show consistent improvements — but the ambiguity must be resolved.

### Minor

1. **Unmeasured daemon overhead.** The paper mentions a "lightweight daemon" (Section 3.2) that handles gradient accumulation on each device, but provides no measurement of its CPU/GPU overhead, memory bandwidth impact, or potential to become a contention bottleneck. The end-to-end throughput results implicitly include the daemon's cost, so this does not invalidate the main claims, but characterizing the daemon's overhead would strengthen the paper and aid reproducibility.

2. **No variance estimates for throughput measurements.** Workload imbalance is inherently stochastic due to variable sequence lengths, yet all reported throughput numbers appear to come from single runs. While single-run throughput benchmarks are common practice in systems papers at this scale, reporting variance would help assess the reliability of the reported speedups.

3. **Limited implementation detail on daemon concurrency.** Section 3.2 describes the daemon but does not explain how it handles simultaneous gradient pushes from multiple peers (e.g., whether it uses atomic operations, locks, or a ring-buffer). This is relevant since the daemon is a core component for gradient accumulation correctness and performance.

4. **RL evaluation at limited scale.** The RL experiments are restricted to ≤14B models on ≤16 GPUs, with modest speedups (≤10%). The paper acknowledges this honestly due to inference time constraints, and the results are directionally consistent with the SFT experiments. However, the limited scope makes it harder to assess whether ODC's benefits persist in RL at scale.

### Trivial
None.

## Nice-to-Haves

- **Ablation of cross-node overhead mitigation.** Section 6 discusses overlapping communication with computation and hybrid sharding as solutions to ODC's cross-node bandwidth disadvantage (Figure 11), but no controlled experiment validates their effectiveness. An ablation comparing ODC with and without hybrid sharding would strengthen the discussion.
- **Comparison with ZeRO++** (mentioned in Section 6.1) as an alternative approach to reducing cross-node communication would be informative, though not required for the paper's core contribution.
- **Gradient accumulation correctness diagnostic.** The paper could strengthen confidence by showing that minibatch-level gradients under ODC match those under collective FSDP (e.g., weight comparison after a fixed number of steps).

## Removed Points

- **Training convergence not verified in main paper:** The Harsh Critic claimed this is an "evidential gap," but the paper explicitly states convergence verification is deferred to Appendix F (line 182). The parser strips appendix content from all papers; the appendix exists in the original submission. This is a known parser artifact, not an author error. **Removed per hard rule.**

- **Concern about "Collective LB-Mini" being an invalid baseline:** The Harsh Critic claims this is a "structural flaw" that "undermines the fairness of the main experimental comparison." While the unexplained baseline IS a real concern (kept as a Major weakness above), the critic's stronger claim that it is a fatal flaw is overstated. The core evidence for ODC's benefits does not depend on this baseline alone — the comparisons that use LB-Micro and LocalSort (which are clearly defined for both collective and ODC) already show consistent improvements. **Downgraded from fatal to major.**

- **Speculation about gradient accumulation semantics:** The Harsh Critic's "Strengthening the Paper" section asks for verification that gradients are correctly accumulated when microbatches complete at different times. This is addressed by the convergence verification in Appendix F (which exists in the original submission). **Removed as moot per hard rule.**

- **Missing related work (ZeRO++) comparison:** The Harsh Critic claims the paper should have compared against ZeRO++. The paper discusses ZeRO++ in Section 6.1 as context for hybrid sharding. This is a reasonable suggestion but not a required comparison for evaluating ODC on its own terms. **Moved to Nice-to-Haves.**

- **"Reproducibility details" about code not being available:** The Harsh Critic states "the code patch is not yet available." The paper states it is open-sourced at the provided repository (line 271). The reviewer cannot verify this, but the paper claims availability. **Removed per hard rule about questioning cited availability.**

- **Strength Finder's generic strengths** (e.g., "the paper addresses an important problem") — these are removed as they are generic/superficial and not specific to the paper's content.

## Novel Insights

The most interesting observation that emerges from the reviews is that ODC's core contribution is not just a performance optimization but a **conceptual reframing**: the paper argues that the dominance of collective communication in modern DP training has caused the field to implicitly accept synchronization patterns that are suboptimal under the workload conditions now prevalent in LLM post-training. By revisiting the parameter-server paradigm — long considered obsolete for homogeneous GPU clusters — the paper demonstrates that PS-style point-to-point communication is actually *better suited* than collectives to the imbalanced workloads created by variable sequence lengths. This insight reframes the historical PS→collective trajectory not as a one-way progression but as a design tradeoff that should be re-evaluated when workload assumptions change. The parametric study (Figure 10) and the analysis of why LB-Mini is only feasible under ODC together provide systematic evidence supporting this reframing.

## Suggestions

1. **Clarify the "Collective LB-Mini" baseline immediately.** Explain how it was implemented given the stated incompatibility between LB-Mini and collectives, or rename/remove it if it is misleading. This is the single most important fix for the camera-ready version.

2. **Add a brief measurement of the daemon's overhead** (e.g., CPU utilization, GPU kernel time, or memory footprint) to substantiate the "lightweight" claim. Even a short paragraph would suffice.

3. **Include error bars or min/max ranges** for at least the key throughput comparisons (Figure 8), particularly since workload imbalance is stochastic.

4. **Move the convergence verification from Appendix F into the main paper** or at least reference it more prominently in Section 5. Since the appendix exists in the original submission, the main text should clearly state the key finding (e.g., "loss curves match within noise").

## Score and Decision

**Round 1 (Bracketing):** The paper sits in the 4.5–7.5 range. Weak anchors (avg ≤3.4) are clearly below this paper's quality (scored papers on federated learning, heterogeneous training, and basic optimizers with fatal novelty/completeness issues). Strong anchors at 8.0 are above (scored papers on scaling laws, pre-training data selection, and specialized training frameworks with broader empirical or theoretical scope).

**Round 2 (Narrowing):** I examined four anchors in detail:
- **ACCO (5.0, rejected):** Similar domain (communication in distributed LLM training), but novelty concerns dominate — reviewers noted the core technique (1-step delay + compensation) overlaps heavily with prior work. ODC has stronger novelty.
- **DynMo (5.25, rejected):** Load balancing for dynamic LLMs. Solid experiments but limited algorithmic novelty. ODC's point-to-point PS reframing is more original.
- **CO2 (7.0, accepted):** Communication-computation overlap via local SGD + async communication. Stronger theoretical depth (convergence proof) and larger-scale experiments (128 GPUs). ODC has comparable clarity and more novel conceptual framing but lacks theoretical analysis and has the LB-Mini baseline ambiguity.
- **"From Promise to Practice" (6.67, accepted):** Decentralized training runtime model. Solid analysis but criticized for missing related work. ODC has a cleaner contribution narrative.

**Final Score:** 6.0. This is positioned above the 5.0–5.25 cluster (clearer novelty, better experiments) but below CO2 at 7.0 (weaker theoretical depth, smaller scale, unresolved baseline ambiguity). The "Collective LB-Mini" issue is the main factor preventing a higher score — once resolved, the paper could reasonably be assessed at 6.5–7.0. **Decision: Accept**. The paper makes a genuinely novel and well-supported contribution to an important practical problem. The main weakness is a presentational inconsistency that can be fixed in camera-ready, not a fundamental flaw in the approach.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>