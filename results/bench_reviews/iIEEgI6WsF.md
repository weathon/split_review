Now I have all the information needed. Let me write the consolidated review.

---

## Summary

This paper proposes On-Demand Communication (ODC), which replaces FSDP's per-layer collective operations (*all-gather* and *reduce-scatter*) with point-to-point RDMA primitives (*gather* and *scatter-accumulate*). The key insight is that per-layer collectives create unnecessary synchronization barriers that amplify straggler effects under variable-length sequence workloads common in LLM post-training. By relaxing synchronization from the layer level to the minibatch level, ODC decouples device progress and enables simpler, minibatch-level load balancing. Experiments across SFT and RL tasks, model sizes from 1.5B to 32B, and up to 32 GPUs show consistent throughput improvements up to 36% over standard FSDP with packing.

## Strengths

- **Clear problem identification with empirical grounding**: The paper convincingly demonstrates that per-layer FSDP collectives create synchronization barriers (Section 2, Figure 1) that cause up to 50% device idle time under imbalanced workloads (Table 6). The formal bound in Equation (1) captures why packing alone cannot solve the problem — both are well-motivated.

- **Technically sound system contribution**: Replacing collectives with point-to-point RDMA operations is a clean, principled solution that preserves FSDP's memory layout and synchronous optimization semantics while relaxing synchronization granularity. The implementation using CUDA IPC / NVSHMEM with a lightweight daemon for gradient accumulation (Section 3.2) is practical and well-described.

- **Comprehensive empirical evaluation**: The paper evaluates across two post-training tasks (SFT on LongAlign and SWE-Smith, RL on AIME), model sizes from 1.5B to 32B, and up to 32 GPUs. Multiple load-balancing baselines are included, including an optimized verl packing that is substantially stronger than the native implementation. Speedups are consistent across settings, reaching up to 36%.

- **Honest discussion of limitations**: Section 6 directly confronts inter-node communication challenges, provides per-client volume analysis (Appendix D), and presents hybrid sharding as a mitigation with empirical evaluation (Appendix E). Training convergence is validated (Appendix F).

- **Practical value**: The authors commit to open-sourcing their implementation with FSDP integration patches. The approach is simple to integrate (replacing collective calls with ODC primitives), making it adoptable by practitioners.

## Weaknesses

### Fatal

None.

### Major

- **Multi-node scaling evidence is limited**: The main experiments use at most 32 GPUs (4 nodes), and the hybrid sharding mitigation is evaluated only with truncated sequences (max 8K, Appendix E). Figure 11 shows point-to-point primitives have significantly lower inter-node bandwidth than NCCL collectives. While the paper argues that overlap with computation hides this cost for long sequences, direct evidence with full-length sequences at larger node counts (e.g., 8 nodes with a 32B+ model) is missing. This limits confidence that ODC's benefits persist at the scales typical of production LLM training.

### Minor

- **Mechanism evidence is indirect**: The paper attributes throughput gains to reduced synchronization idle time, supported by "bubble rate" estimates computed from packing algorithms (Tables 4, 6). The paper is transparent that these are estimates ("as estimated by the packing algorithm," line 1509), and the correlation with speedup is consistent. However, direct GPU profiling traces would substantially strengthen the causal claim. This does not undermine the practical throughput results but leaves some uncertainty about the precise mechanism.

- **RL gains are modest**: The RL experiments show only up to 10% speedup. The paper explains this honestly (verl constraints limiting LB-Mini, less long-tailed sequence distributions), but it means the strongest case for ODC is made for SFT workloads specifically. The parametric study also uses only a 1.5B model, limiting insight into how the factors interact at larger scales.

- **Parameter-server framing adds limited conceptual value**: Reframing FSDP as a "decentralized parameter server" is a reasonable analogy, and the paper acknowledges precedent for co-located roles (Jiang et al., 2020). However, the paper does not engage deeply with the PS design space (consistency models, staleness, comparison with RDMA-based PS implementations). The conceptual contribution is more of a reinterpretation than a technical insight — the real contribution is the communication scheme itself.

### Trivial

- Equation (1) formalizes the per-layer stall bound but is never used quantitatively in later analysis — it serves only as motivation.
- No error bars or variance estimates are reported for throughput numbers (though run-to-run variance is typically low in this setting).

## Nice-to-Haves

- GPU profiling traces (e.g., PyTorch profiler timelines) showing side-by-side FSDP vs. ODC activity on an imbalanced minibatch would make the mechanism visually compelling.
- Larger-scale multi-node experiments with full-length sequences (e.g., 32B model on 8 nodes) to validate that overlap effectively hides inter-node communication costs.
- End-to-end model quality evaluation (e.g., LongAlign benchmark scores) to complement the throughput results.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"The paper does not directly measure or profile GPU idle time" — from Harsh Critic #1**: While true that GPU traces are absent, the paper is transparent about its bubble rate estimation methodology and uses it to show correlation between predicted idle time and throughput gains. The throughput gains themselves are directly measured. Demanding GPU profiler traces is a methodological preference, not a requirement for validity. Moved because the bubble rate analysis is a reasonable analytical substitute, though not as strong as direct measurement.

- **"The framing as a 'parameter server' is overclaimed and adds little" — from Harsh Critic #3**: The paper explicitly cites prior work with co-located roles (Jiang et al., 2020) and frames its contribution as the integration with FSDP's sharding. The PS analogy is a legitimate conceptual framework. The criticism that it doesn't engage with PS design space (consistency models, bounded staleness) is scope creep — the paper explicitly preserves synchronous semantics and discusses async extensions only as future work (Section 6.2). Moved because the paper is honest about what it does and doesn't claim, and the PS framing helps readers understand the architecture.

- **"Claim that point-to-point transfers are 'non-intrusive' is asserted without supporting measurements" — from Harsh Critic #1**: RDMA (CUDA IPC, NVSHMEM) inherently enables non-intrusive transfers — this is a defining property of RDMA, not something requiring novel proof. The daemon handles gradient accumulation on the server side. This is standard systems knowledge.

- **"No variance or error bars reported for throughput numbers" — from Harsh Critic #1**: Throughput measurements on homogeneous GPU clusters with dedicated hardware typically exhibit negligible run-to-run variance. This is a generic criticism that carries little weight in systems benchmarking.

- **"Parametric study only examines a 1.5B model" — from Harsh Critic #2**: The purpose of a parametric study is to isolate factors; using a single model size is standard methodology. The main results already cover multiple model sizes.

## Novel Insights

None beyond the paper's own contributions. The paper's core insight — that per-layer collectives create avoidable synchronization barriers and that replacing them with point-to-point communication relaxes these barriers to the minibatch level — is itself the novel contribution.

## Suggestions

- Add a small-scale validation of the idle-time mechanism with PyTorch profiler traces for one representative configuration (e.g., 1.5B model, 8 GPUs, LongAlign with minibatch size 4). This would directly link the bubble rate estimates to measured behavior and substantially strengthen the paper.
- For the camera-ready version, extend the hybrid sharding experiments to include at least one full-length sequence setting, or explicitly discuss what prevents doing so (e.g., memory constraints making it infeasible).
- Consider toning down the PS framing slightly and instead emphasizing the core insight more directly: "relaxing synchronization granularity from layer to minibatch by replacing collectives with point-to-point communication."

## Score and Decision

### Anchor comparison:

| Anchor Paper | Path | Avg Score | Comparison |
|---|---|---|---|
| Scaling with Collapse | `3YKeB9R1g9.md` | 8.00 | More complete contribution with clear applications and theoretical grounding; ODC is less polished and has acknowledged limitations around multi-node scaling. |
| MT-DAO | `5yPP238v4c.md` | 6.50 | Similar quality tier. MT-DAO has theoretical convergence guarantees but smaller-scale experiments (max 720M). ODC has broader empirical scope (up to 32B, multiple tasks) but no theory. |
| DES-LOC | `6N2qFixxYZ.md` | 6.00 | Similar quality tier. DES-LOC has theory + experiments up to 1.7B. ODC has broader empirical evaluation and a more clearly motivated practical problem. |
| Partial Parameter Updates | `vU7pcaDypQ.md` | 4.00 | ODC is substantially stronger: better baselines, broader evaluation, clearer contribution. |
| Sequence Length Matters | `ddf7XdLtNO.md` | 4.00 | ODC has stronger baselines, clearer mechanism insight, and more thorough evaluation. |
| DCP | `lWWaBbFPw4.md` | 4.00 | ODC has clearer novelty, better baselines, and more transparent discussion of limitations. |
| AsyncMesh | `hzikvjtIj4.md` | 3.33 | ODC is substantially stronger with larger-scale experiments and more practical integration. |
| SortedRL | `5v3Gzuic8i.md` | 3.00 | ODC is substantially stronger with clearer methodology and more consistent results. |
| GCT | `RRtwIvoYoh.md` | 2.50 | ODC is much stronger across all dimensions. |

ODC is clearly above the 4.0-tier papers (stronger baselines, broader evaluation, clearer contribution) and comparable to the 6.0-6.5 tier (DES-LOC, MT-DAO). It does not reach the 8.0 tier due to limitations in multi-node scaling evidence and indirect mechanism validation. The paper addresses an important practical problem with a technically sound solution, provides thorough empirical evaluation, and is honest about its limitations.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>