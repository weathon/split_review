Now I have a thorough understanding of the paper and the calibration anchors. Let me synthesize the final review.

## Summary
2-3 sentence summary of the paper's contribution.

The paper identifies that FSDP's per-layer collective communication (all-gather/reduce-scatter) creates synchronization barriers that are the root cause of inefficiency under the imbalanced workloads characteristic of LLM post-training (where sequence lengths vary widely). It proposes On-Demand Communication (ODC), which replaces these collectives with point-to-point gather/scatter-accumulate primitives, reframing FSDP as a decentralized parameter server and relaxing synchronization from per-layer to per-minibatch. Evaluated on SFT and RL tasks across 1.5B–32B models on up to 32 A100 GPUs, ODC achieves up to 36% throughput improvement over standard FSDP.

## Strengths

1. **Well-motivated and clearly articulated core idea**: The paper identifies a conceptually clean root cause—FSDP's per-layer collectives force tight synchronization that is fundamentally avoidable under imbalanced workloads—and provides a correspondingly clean fix (replacing collectives with point-to-point operations, formalized via Eq. (1) and Figures 1–2). This reframing of FSDP as a decentralized parameter server is both novel and intuitive.

2. **Consistent empirical speedups across diverse settings**: ODC shows throughput improvements over FSDP in nearly all tested configurations—SFT (up to 36%), RL (up to 10%), across model sizes 1.5B–32B, three datasets with very different sequence-length distributions (Figure 7), and both packed and unpacked workloads (Figure 8). The gains are not cherry-picked.

3. **Parametric study examining sensitivity to key factors**: Figure 10 systematically varies minibatch size, max sequence length, packing ratio, and number of devices, showing that ODC's benefits increase with sequence length and device count, and decrease with packing ratio—all consistent with the paper's thesis. This provides practical guidance for practitioners.

4. **Honest treatment of limitations**: The paper acknowledges that ODC's point-to-point primitives are significantly slower than collectives across nodes (~50 GB/s vs. ~140 GB/s for gather at 16 devices, Figure 11), discusses overlap with computation and hybrid sharding as mitigations (Section 6.1), and transparently explains why RL gains are smaller (framework constraints, less long-tailed distributions). This candor increases confidence that the authors are not overclaiming.

## Weaknesses

### Fatal
None.

### Major

1. **No direct profiling of communication/computation overlap**: The paper's central defense against cross-node overhead is that ODC's point-to-point communication can be overlapped with computation, particularly for long sequences where attention cost grows quadratically while communication volume stays constant. However, no time breakdown is provided to confirm this. The end-to-end speedups at up to 32 GPUs are consistent with overlap working, but without a breakdown of compute time vs. communication time vs. idle time for a representative configuration, it is impossible to assess how the method would behave at larger node counts, with shorter sequences, or with smaller models where the computation-to-communication ratio is less favorable. This is the single most significant gap in the evaluation. (This corresponds to Harsh Critic point 1; verified against paper: no profiling of overlap in any section.)

2. **Hybrid sharding (Section 6.1) is discussed but never experimentally evaluated**: The paper proposes hybrid sharding (sharding only within a node) as a remedy for inter-node overhead and states results are in Appendix E, but the extracted text contains no hybrid sharding experiments. Given that inter-node overhead is the primary limitation of the current approach, evaluating this variant is essential to support the claim that ODC can scale to larger clusters. Without it, the paper's conclusions are confined to the tested scale of up to 8 nodes.

### Minor

3. **Evaluation limited to 32 GPUs (4–8 nodes)**: While 32 GPUs is a reasonable scale for a conference paper, the claim that ODC is "a superior fit for the prevalent imbalanced workloads in LLM post-training" would be strengthened by validation at larger scales, especially since inter-node overhead is a known concern. The parametric study shows acceleration increasing with device count (Figure 10), which is encouraging, but this trend may reverse at larger node counts where cross-node communication dominates. A simple analytical model could have addressed this gap without running larger experiments.

4. **RL speedups are modest (≤10%) and domain-specific**: The paper honestly attributes this to framework integration constraints and less long-tailed distributions, but it means the main empirical support for the core claim rests primarily on SFT results. The RL results, while positive, are narrow enough to warrant caution about generalizing to other RL post-training pipelines.

5. **Load-balancing algorithms (LB-Micro, LB-Mini) are only described at a high level in the main text**: Section 4 explains the high-level approach (partition globally at minibatch level, pack locally) but the detailed procedures are relegated to Appendix C (not available in the extracted text). While this is common practice, it makes it harder for readers to attribute observed gains to the communication scheme versus the load-balancing algorithm.

6. **Communication primitive benchmark (Figure 11) is synchronous**: The paper explicitly states that ODC primitives were benchmarked with barriers before and after each operation. While this is a useful bandwidth comparison, it does not reflect the effective communication cost when overlapped with computation in the full training loop, which is the actual claimed advantage.

### Trivial
None.

## Nice-to-Haves

- A simple analytical performance model that estimates the crossover point where ODC's overhead outweighs its benefits (acknowledged as missing by both the harsh critic and the paper's own discussion).
- Discussion of when ODC could be detrimental (e.g., perfect workload balance + high inter-node bandwidth).
- Evaluation on model architectures other than DeepSeek-R1-Distill-Qwen (e.g., Llama, Mistral) to verify architectural generality.

## Removed Points

The following weaknesses were surfaced by reviewers but are removed after verification against the paper:

- **"Implementation details are too brief; appendices are missing"** (from Harsh Critic): The paper describes the high-level implementation (CUDA IPC, NVSHMEM, Triton-Distributed) in Section 3.2 and points to Appendix B for more details and an open-source release. This is standard practice; the parser stripped the appendices. Not a paper flaw.
- **"Load-balancing algorithms are insufficiently specified to assess novelty"** (from Harsh Critic): Section 4 clearly describes the objective (partition samples to balance computational load across devices, then pack locally), which is sufficient to understand the key insight. Detailed algorithms in appendices are normal.
- **"Memory management implications of variable numbers of microbatches not discussed"** (from Harsh Critic): A reasonable scope limitation; the paper does not claim to address memory management beyond FSDP's existing mechanisms.
- **"Missing related works"**: The instructions forbid mentioning missing related works as I cannot verify them externally.
- **"Reproducibility concerns due to missing appendices"**: Parser artifact; the paper states it will open-source.
- **"Formatting/style nitpicks"**: Parser artifacts, not author errors.
- **Generic "evaluation lacks rigor" or "claims not fully supported" sweeps without concrete anchors**: Removed as category-driven noise.

## Novel Insights

None beyond the paper's own contributions. The core insight—that FSDP's per-layer collectives are the fundamental source of inefficiency under imbalance, and that replacing them with point-to-point operations reframes FSDP as a decentralized parameter server—is the paper's main contribution, and the reviews do not surface additional novel observations beyond this framing.

## Suggestions

1. **Provide a communication/computation time breakdown** for at least one representative SFT configuration (e.g., 7B model on 16 GPUs). Show compute time, collective communication time, ODC communication time, and idle time separately. This would directly validate the claim that overlap hides the cross-node penalty.

2. **Evaluate the hybrid-sharding variant** (sharding only within a node) in at least one multi-node setting to demonstrate that the inter-node inefficiency can be eliminated. This is the most impactful missing experiment.

3. **Include a simple analytical model** that estimates the crossover point where ODC's benefits are outweighed by communication overhead, given bandwidth measurements and compute time estimates. This would substantially strengthen the paper's practical guidance.

4. **Specify the LB-Mini algorithm formally** in an appendix with the objective function and procedure, or provide pseudocode that clearly separates the communication scheme's contribution from the load-balancing contribution.

## Score and Decision

### Calibration Anchors

All anchors retrieved across rounds:

**Round 1 — Topic band queries (parameter server / FSDP distributed training):**
- `bntJK4NyIW` (avg 2.00, Reject, topic-low): Decentralized Training of Transformer Models in Heterogeneous Network. Much weaker than the paper under review—unclear contribution, unrealistic assumptions. ODC is clearly stronger.
- `cPZepCZlFW` (avg 3.25, Reject, topic-low): Capturing Gradient Aggregation Errors. Lower quality; ODC has a more coherent contribution.
- `p4RAKZ4oik` (avg 3.00, Reject, topic-low): FedDTPT. Not directly comparable (federated learning domain).
- `b7HOhqXiZs` (avg 2.60, Reject, topic-low): DeMo. Similar exploration of relaxed synchronization but weaker empirical validation.
- `uoU4ypjAmN` (avg 4.00, Reject, topic-mid): SPD. Sync-point dropping in tensor parallelism. Less comprehensive evaluation; ODC is stronger.
- `lo3nlFHOft` (avg 6.67, Accept, topic-mid): From Promise to Practice. Stronger paper—has a runtime model, convergence proof, 64-GPU experiments. ODC lacks this analytical depth.
- `UV1jr2aJ2J` (avg 5.00, Reject, topic-mid): ACCO. Communication-computation overlap with local-updating. ODC has a more novel core idea.
- `0cadcLKbt7` (avg 4.00, Reject, topic-mid): TPI-LLM. Edge inference, not directly comparable.
- `vf5aUZT0Fz` (avg 8.00, Accept, topic-high): DEPT. Much stronger; decoupled embeddings with massive communication reduction.
- `ZuazHmXTns` (avg 7.60, Accept, topic-high): PAdaMFed. Federated learning, not directly comparable.
- `OfjIlbelrT` (avg 8.00, Accept, topic-high): FlexPrefill. Attention mechanism paper, not comparable.
- `OvoCm1gGhN` (avg 8.00, Accept, topic-high): Differential Transformer. Architecture paper, not comparable.

**Round 1 — Weakness-anchored queries:**
- `kC5i5X9xrn` (avg 5.00, Reject, weakness-inter-node): LightSeq. Sequence parallelism for long context. Similar scale limitations; ODC has comparable breadth.
- `oVnfVnwh6y` (avg 4.75, Reject, weakness-inter-node): LASP. Linear attention sequence parallelism. Narrower contribution.
- `JOBokGDcX0` (avg 2.50, Reject, weakness-inter-node): Sequence segmentation. Not relevant.
- `ZO5cn4IfaN` (avg 7.00, Accept, weakness-inter-node): CO2. Stronger—convergence proof, 128 GPUs, comprehensive evaluation. ODC lacks this scale and theory.
- `N80ER2he6l` (avg 5.00, Reject, weakness-load-balancing): OMNIBAL. Load balancing for vision-language models. Similar issue of limited validation.
- `WVmarX0RNd` (avg 3.50, Reject, weakness-load-balancing): Multi-Bin Batching. LLM inference, different setting.
- `bAFVlpFQvT` (avg 6.75, Accept, weakness-load-balancing): CoLM. Memory-efficient training, different focus.
- `eENHKMTOfW` (avg 6.00, Accept, weakness-load-balancing): Training Mice to Compete with Elephants. Tuning strategies for small LLMs, different focus.
- `ic1Z7Qe9xH` (avg 3.67, Reject, weakness-scale): Elastic Load Balancing for Dynamic LLMs. Lower quality eval.
- `bntJK4NyIW` and `N80ER2he6l` repeated from other queries.

**Round 2 — Narrowing queries (score 4.0–6.5):**
- `kC5i5X9xrn` (avg 5.00): Already listed.
- `N80ER2he6l` (avg 5.00): Already listed.
- `oVnfVnwh6y` (avg 4.75): Already listed.
- `WsRHpHH4s0` (avg 5.50, Accept, round2): RingAttention. Comparable quality—useful idea with split reviews on novelty; similar scale of experiments.
- `Z3xg3hxdky` (avg 5.40, Reject, round2): DSP. Dynamic sequence parallelism. Comparable quality but rejected.
- `DUsqifwwf5` (avg 4.75, Reject, round2): SOLOS. Not directly comparable.
- `jhiByZpuIS` (avg 4.67, Reject, round2): MSfusion. Collaborative training, different setting.
- `cZZMC8VFZc` (avg 5.00, Reject, round2): FlashDP. DP-SGD, different focus.
- `UV1jr2aJ2J` (5.00) and `kC5i5X9xrn` (5.00) repeated.

Round-1 bracket: The paper sits between the low-band (<3.5, where papers have unclear contributions or missing evaluations) and the mid-band (3.5–7.5). It is clearly above the low-band anchors. The relevant mid-band comparison papers (ACCO at 5.00, LightSeq at 5.00, RingAttention at 5.50) have comparable experiment scales but the ODC paper has a more novel core idea. Papers with stronger analytical contributions (From Promise to Practice at 6.67, CO2 at 7.00) benchmark what the ODC paper could become with more rigorous analysis.

**Final comparison reasoning:** The low-band anchors failed primarily due to unclear contributions, unrealistic assumptions, or insufficient experimental validation. The ODC paper shares none of these failures—its contribution is clear, the idea is well-motivated, and the experiments are solid for the tested scale. However, the weakness-anchored queries confirm that papers with missing communication/computation profiling and limited scale tend to cluster around 4.5–5.5. The paper under review is at the stronger end of this cluster because its core insight is more novel and its evaluation more comprehensive than e.g., ACCO (5.00) or LightSeq (5.00), but it lacks the analytical depth and larger-scale validation of top mid-band papers like "From Promise to Practice" (6.67) or CO2 (7.00).

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>