Now I have all the information I need. Let me produce the consolidated review.

## Summary

This paper identifies a real problem in LLM post-training: workload imbalance from sequence length variance causes synchronization overhead in FSDP's per-layer collectives. The authors propose On-Demand Communication (ODC), which replaces collective all-gather/reduce-scatter with point-to-point gather/scatter-accumulate, reframing FSDP as a decentralized parameter server. ODC decouples device progress by relaxing synchronization from per-layer to per-minibatch, and enables simpler minibatch-level load balancing (LB-Mini). Evaluated across models from 1.5B to 32B on SFT and RL tasks, ODC achieves up to 36% throughput improvement over standard FSDP (SFT, 32B model) with consistent gains across diverse settings.

## Strengths

- **ODC directly addresses the root cause of straggler idle time — per-layer synchronization barriers — by replacing collectives with point-to-point communication.** Section 3 and Figures 2 and 5 clearly show how ODC replaces all-gather/reduce-scatter with gather/scatter-accumulate, eliminating the per-layer max-over-devices bottleneck formalized in Equation (1). This is a structurally clean solution that tackles the problem at the communication level rather than the packing/batching level.

- **Up to 36% throughput improvement over standard FSDP, demonstrated across multiple model sizes (1.5B–32B), datasets (LongAlign, SWE-Smith), and minibatch sizes.** Figure 8 provides a comprehensive evaluation with consistent ODC advantages over Collective baselines across both packed (LB-Micro, LB-Mini) and unpacked (LocalSort) settings. The speedup is largest under packing, precisely where the paper's core argument (collective synchronization punishes imbalance) predicts it should be.

- **ODC enables minibatch-level load balancing (LB-Mini) that is both simpler and more effective than microbatch-level packing under imbalance.** Section 4 makes a crisp argument: FSDP's per-layer collectives force uniform microbatches across devices, constraining packing. ODC's decoupling removes this constraint, allowing different devices to process different numbers of microbatches. Figure 8 confirms that ODC+LB-Mini outperforms ODC+LB-Micro at small minibatch sizes, directly demonstrating the benefit of coarser balancing granularity.

- **ODC preserves FSDP's memory efficiency while adding imbalance tolerance.** The decentralized parameter server design (Section 3.1, Figure 6) colocates server and worker roles by sharding parameters, gradients, and optimizer states across devices — inheriting FSDP's memory footprint while gaining the straggler tolerance of a PS architecture.

- **Parametric study (Figure 10) systematically isolates factors affecting ODC's relative advantage.** Trends are informative and internally consistent: acceleration grows with sequence length and device count (where imbalance is most severe), and declines with packing ratio (where the baseline's packing efficiency improves). This strengthens confidence that the mechanism aligns with the stated cause.

## Weaknesses

### Fatal

None.

### Major

- **The claim that ODC's RDMA point-to-point transfers are "non-intrusive" and do not interrupt target-device computation is asserted without supporting evidence.** The paper states (Section 3.2, Section 3) that RDMA reads/writes to GPU memory are transparent to the target GPU's ongoing computation. However, RDMA memory accesses do compete with compute kernels for HBM bandwidth. The paper provides no microbenchmark measuring whether this contention slows concurrent compute kernels on the target device, nor does it measure how much communication latency is hidden by overlap in the end-to-end runs. The primitive benchmark (Figure 11) measures isolated bandwidth with barriers before and after — deliberately not overlapping with compute — so it does not address this question. The authors should provide either a microbenchmark of concurrent compute+RDMA (showing that contention is negligible) or a communication-computation overlap efficiency measurement from the training runs. Without this, the mechanism by which ODC achieves its speedups is partially unverified, even though the end-to-end results themselves are not in question.

### Minor

- **No statistical variance or error bars reported on throughput measurements.** Given that sequence length distributions are stochastic and packing algorithms may produce variable outcomes, reporting single-run or averaged throughput without variance makes it impossible to gauge the stability of the reported gains. This does not undermine the main results, which are consistent across many settings, but it would increase confidence.

- **RL evaluation is limited to models up to 14B.** The paper notes this is due to inference time constraints (Section 5.1), which is understandable, but the claim that ODC benefits RL training would be stronger with evidence at 32B scale. The paper should clearly state this as a limitation affecting generalizability of the RL results.

- **"Collective LB-Mini" baseline in Figure 8 is ambiguously defined relative to the text.** Section 5.1 states that LB-Mini "applies only to ODC" because it produces different numbers of microbatches per device, yet Figure 8 reports a "Collective LB-Mini" curve. The paper should clarify how this baseline is constructed (e.g., does it pad devices to equal microbatches, or use a different mechanism?). The comparative ordering is sensible regardless, but the ambiguity should be resolved.

- **The RL speedup explanation ("less long-tailed distribution, implementation constraints in verl") is plausible but not quantified.** The paper cites Appendix G for bubble rate data (stripped from this review), but the main text would benefit from a brief quantification, e.g., showing that RL has lower sequence-length coefficient of variation on AIME compared to SFT datasets.

### Trivial

- Figure captions are repeated verbatim as alt-text and again as standalone captions; this is a formatting artifact, not author error.

## Nice-to-Haves

- Reporting a timing breakdown (compute time vs. communication time vs. idle time) for the main SFT and RL runs would help separate the contribution of ODC's decoupled progress from its communication overhead, and directly validate the mechanism.
- A microbenchmark explicitly measuring the slowdown (if any) on compute kernels running concurrently with RDMA reads/writes on the same GPU would strengthen the "non-intrusive" claim.
- A brief 1–2 paragraph description of the gradient accumulation daemon's execution model (CPU thread vs. GPU kernel, contention handling) in the main text would improve Section 3.2's clarity.

## Removed Points

- **"Synchronous optimization semantics not justified"** (Harsh Critic): The paper clearly states that gradients are accumulated on owning devices before the optimizer step, and Appendix F validates convergence. The semantic equivalence is straightforward and adequately addressed. REMOVED as factually incorrect.

- **"No comparison to best possible FSDP packing baseline"** (Harsh Critic): The paper provides the fair comparison (ODC+LB-Micro vs Collective+LB-Micro) to isolate the communication benefit. The critic acknowledges the point still stands. REMOVED as not a real weakness.

- **"Daemon description too vague"** (Harsh Critic, part): The paper references Appendix B for implementation details; the parser strips appendices. The main text description is brief, but this is typical for system papers that defer low-level details. WEAKENED to Nice-to-Have rather than a weakness.

- **"Hybrid sharding results in appendix"** (Harsh Critic): The appendix is stripped by the parser; the reference to Appendix E is present in the original submission. REMOVED as parser artifact.

## Novel Insights

None beyond the paper's own contributions. The paper is a well-executed systems contribution, and the reviewers' input does not surface a higher-level synthesis beyond what the paper already states: that the PS paradigm's straggler tolerance, long abandoned in favor of collectives for balanced workloads, is a natural fit for the imbalanced workloads of LLM post-training.

## Suggestions

1. Add a microbenchmark showing that concurrent RDMA reads/writes do not meaningfully degrade compute kernel performance on the target GPU, or alternatively, measure communication-computation overlap efficiency in the end-to-end training runs.
2. Add error bars or variance reporting on the throughput measurements in Figures 8 and 9.
3. Clarify how the "Collective LB-Mini" baseline is implemented in the main text.
4. State the 36% speedup figure with its conditioning context (SFT, 32B model, minibatch size 4, SWE-Smith dataset) explicitly in the abstract.

## Score and Decision

### Calibration Report

**Round 1 — Bracketing:**
- Weak anchors (avg ≤ 3.5): RHJVkaIYYa (3.00, withdrawn) — decentralized LLM pretraining with memory constraints; hzikvjtIj4 (3.33, reject) — async optimization for data/pipeline parallelism; yOkek71cG5 (3.00, reject) — pipeline-parallel communication compression; DVfaLBUc2s (2.40, reject) — dynamic compression for distributed communications. These papers have fundamental flaws (loss divergence, limited evaluation, unsupported claims) that clearly place them below the target paper.
- Middle anchors (3.5–7.5): vU7pcaDypQ (4.00, reject) — partial parameter updates, limited to one model size; Ej1DYLYzFU (4.00, reject) — NoLoCo, loss divergence issues; on9jR4Dx2L (4.00, withdrawn) — subnetwork data parallelism; 6N2qFixxYZ (6.00, accept poster) — DES-LOC, desynced optimizer communication with theory + 1.7B experiments. The target paper is clearly stronger than the 4.0 rejects (broader evaluation, cleaner contribution, no divergence issues) and comparable to DES-LOC.
- Strong anchors (≥ 7.5): qOyF214xmg (8.00), VKGTGGcwl6 (8.00), oBXfPyi47m (8.00), yRtgZ1K8hO (8.00) — all are language model capability papers, not distributed systems papers. Not directly comparable.

**Round 1 bracket:** 5.0 – 6.5

**Round 2 — Narrowing:**
- MSHPrMpIHZ (5.33, accept poster) — Semantic Parallelism for MoE inference; aa14rlfR6k (5.33, accept poster) — FlexRL, VLM RL load balancing; cfZNOO6ZHf (5.50, reject) — AMDP async pipeline parallelism; 6N2qFixxYZ (6.00, accept poster) — DES-LOC (re-read in full). All address related distributed training/system problems.

**Round 2 comparison:**
The paper is stronger than the 5.33 anchors (FlexRL lacks ablation, Semantic Parallelism has limited evaluation). It is comparable to DES-LOC (6.0): DES-LOC has theory + 1.7B experiments with 1.3–2.1× speedup; ODC has broader model scaling (up to 32B) with up to 36% speedup and a more fundamental contribution (revisiting PS paradigm), but lacks theoretical analysis and has an evidential gap in the non-intrusive RDMA claim.

**Final score:** 6.0

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>