## Summary
This paper proposes **On-Demand Communication (ODC)**, a communication scheme that adapts the classic Parameter Server (PS) paradigm to modern Fully Sharded Data Parallel (FSDP) training for LLMs. The core insight is that FSDP's per-layer collective operations (*all-gather*, *reduce-scatter*) impose synchronization barriers that waste device time under the highly imbalanced workloads (variable sequence lengths) typical of LLM post-training. ODC replaces these collectives with point-to-point RDMA primitives (*gather*, *scatter-accumulate*), relaxing synchronization from per-layer to per-minibatch. Combined with a complementary minibatch-level load balancing algorithm (LB-Mini), ODC achieves up to 36% throughput improvement over standard FSDP across SFT and RL post-training tasks.

## Strengths
- **Clear diagnosis and elegant fix**: The paper precisely identifies that FSDP's per-layer collective barriers are the root cause of idle time under imbalanced workloads (with formal analysis in Eq. 1). The conceptual reframe of FSDP as a decentralized PS is clean and well-motivated. The math in Section 2.2 makes the synchronization bottleneck explicit.
- **Consistent and substantial empirical gains**: ODC achieves up to 36% speedup across two SFT datasets (LongAlign, SWE-Smith) and three model scales (1.5B–32B) with no dataset-specific tuning. Gains hold in both unpacked (LocalSort) and packed (LB-Micro, LB-Mini) configurations, demonstrating robustness.
- **Principled parametric study**: Figure 10 systematically quantifies how speedup varies with minibatch size, sequence length, packing ratio, and device count. This gives practitioners a clear guide for when ODC is most beneficial (longer sequences, more devices, lower packing ratios).
- **Practical implementation**: Using CUDA IPC and NVSHMEM to enable transparent RDMA without interrupting the target device's computation is a sound engineering choice. The lightweight daemon for gradient accumulation avoids the ordering constraints of MPI/NCCL.
- **Honest limitation disclosure**: The paper openly reports that ODC's inter-node bandwidth is significantly worse than NCCL collectives (Figure 11), and provides credible mitigations (compute-communication overlap, hybrid sharding).

## Weaknesses

### Fatal
None.

### Major
- **Limited scale evaluation**: All experiments are conducted on at most 32 GPUs (4 nodes × 8 GPUs). At larger DP scale (hundreds of nodes), the inter-node communication efficiency gap (Figure 11 shows ODC substantially lags NCCL collectives at 16–32 devices) could become the dominant bottleneck. The paper argues larger scale amplifies straggler effects (Figure 10), but this only helps if the synchronization gain outweighs the slower communication—a claim not empirically verified beyond 32 GPUs. The hybrid sharding mitigation is described but validated only in an appendix (not available for review).
- **RL integration constraints**: The verl integration requires identical number of samples per device, preventing LB-Mini from being fully applied in the RL setting. The resulting speedup is only ~10%, significantly lower than SFT. This constraint is presented as a deliberate simplification, but it raises questions about ODC's real-world RL utility in production pipelines.

### Minor
- **Memory overhead unquantified**: ODC requires persistent gradient accumulator buffers on each device (handled by a daemon). The paper does not report memory overhead compared to baseline FSDP, which is relevant given memory-constrained training scenarios.
- **Single hardware configuration**: All experiments use A100 GPUs with NVSwitch (intra-node) and RoCE RDMA (inter-node). Behavior on other hardware (e.g., H100 with NVLink, InfiniBand) or cloud environments with different interconnect characteristics is not addressed.

### Trivial
- The LB-Mini algorithm details are in the appendix (removed by parser), making the load balancing contribution harder to assess independently.

## Nice-to-Haves
- A memory overhead table comparing ODC vs. baseline FSDP would strengthen the practical case.
- A breakdown of time spent in communication vs. computation under ODC at different scales would clarify when the inter-node bottleneck becomes limiting.
- Evaluation on a third post-training task (e.g., DPO or PPO with longer reward model rollouts) would broaden the coverage.

## Novel Insights
The paper makes a non-obvious but important architectural observation: the classical choice between PS and collective-based data parallelism is not purely a question of bandwidth—it is fundamentally a question of synchronization granularity and tolerance to workload imbalance. By showing that the quadratic compute scaling with sequence length means computation-communication overlap naturally hides ODC's lower bandwidth (Section 6.1), the paper identifies a regime where replacing NCCL collectives with individually-slower RDMA primitives is *net beneficial*. This suggests a broader principle: system-level optimality claims made under uniform workload assumptions may reverse in the regime of high variance, and the LLM post-training era may mark such a regime shift for distributed training infrastructure.

## Suggestions
- Report end-to-end training memory consumption for ODC vs. baseline to allow practitioners to assess trade-offs.
- Extend evaluation to at least 64–128 GPUs (8–16 nodes) to demonstrate that the speedup persists at the scale commonly used in production LLM post-training.
- Provide an empirical validation that the hybrid sharding mitigation (Appendix E) maintains comparable speedups to the single-node results at multi-node scale.
- Discuss whether ODC could be combined with pipeline parallelism or tensor parallelism for even larger models.

## Score and Decision
ODC addresses a timely, practically important problem—straggler effects in FSDP under imbalanced workloads—with a principled solution grounded in classic distributed systems ideas. The empirical results are strong and consistent across model scales and task types, the implementation is practical and open-sourced, and the paper is honest about limitations. The primary concern is the limited scale of evaluation (≤32 GPUs) given that inter-node communication efficiency is a disclosed weakness; this leaves open whether the speedup persists at production-relevant scale. Nevertheless, the contribution is solid and practically valuable for the growing LLM post-training community.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>