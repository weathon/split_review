Now I have all the information I need. Let me write the final consolidated review.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses
### Fatal
### Major
- weakness 1 — why it matters
### Minor
- weakness 1 — why it matters
### Trivial
- weakness 1

## Nice-to-Haves
- suggestion that would improve but is not a core flaw

## Removed Points
(weaknesses removed with justification)

## Novel Insights
One paragraph synthesizing genuinely novel observations.

## Suggestions
- specific actionable suggestion

Let me finalize.## Summary

This paper revisits the parameter server (PS) paradigm for LLM post-training, where sequence length variation creates persistent workload imbalance across devices. The authors propose On-Demand Communication (ODC), which replaces FSDP's per-layer collective all-gather and reduce-scatter with point-to-point gather and scatter-accumulate operations, relaxing synchronization from the layer level to the minibatch level. ODC preserves FSDP's memory layout and scaling properties while enabling a simpler minibatch-level load balancing strategy (LB-Mini) that is infeasible under collective communication. Across SFT and RL tasks with models up to 32B parameters on up to 32 GPUs, ODC achieves consistent throughput improvements, with up to 36% speedup on long-sequence SFT tasks.

## Strengths

1. **Well-motivated root-cause analysis of FSDP's inefficiency under imbalance.** The paper formalizes that FSDP's per-layer collectives force devices to wait for the slowest one (Equation 1), and backs this with quantitative evidence of up to 50% idle time even with state-of-the-art packing (Table 6, cited in Section 1). This cleanly motivates a communication-level fix rather than yet another packing heuristic.

2. **Clean conceptual contribution: reframing FSDP as a decentralized parameter server.** ODC replaces all-gather/reduce-scatter with point-to-point gather and scatter-accumulate (Figures 3, 5), implemented via RDMA primitives (CUDA IPC, NVSHMEM, Triton-Distributed). This re-frames FSDP as a decentralized PS with colocated server/worker roles (Figure 6), preserving its memory efficiency and scalability while gaining the imbalance tolerance of a PS. The insight that the per-layer synchronization in FSDP is an artifact of the communication model, not a requirement of the training algorithm, is clearly articulated.

3. **Consistent empirical speedups across diverse post-training tasks and a systematic parametric study.** ODC improves throughput over collective baselines on SFT (LongAlign, SWE-Smith) and RL (AIME/GRPO) tasks, across model sizes from 1.5B to 32B and multiple minibatch sizes. The parametric study (Figure 10) independently varies minibatch size, max sequence length, packing ratio, and device count, showing acceleration increases with longer sequences and more devices—directly confirming the paper's core thesis. The paper is also honest about ODC's inter-node communication weakness (Figure 11) and discusses mitigations.

4. **Enables a simpler, more effective load balancing strategy.** Because ODC decouples device progress, it allows minibatch-level balancing (LB-Mini) where each device can process a different number of microbatches—a strategy that is fundamentally impossible under FSDP's collectives. The paper shows this provides additional gains beyond the communication decoupling alone (Figure 10).

## Weaknesses

### Major

1. **"Collective LB-Mini" baseline is contradictory and unexplained.** The paper explicitly states that "As *LB-Mini* can produce different number of microbatches for different devices, it applies only to ODC" (Section 5.1, line 183). Yet Figure 8 includes "Collective LB-Mini" (purple triangles) as a baseline. The paper does not explain how this baseline was implemented. Since LB-Mini's key mechanism (variable microbatches per device) is stated to be incompatible with collective communication, readers cannot determine whether Collective LB-Mini was implemented by padding to uniform microbatches (which would be a form of LB-Micro, not LB-Mini) or by some other means. This is a concrete inconsistency in the main results figure that needs clarification.

2. **The headline "up to 36% speedup" bundles communication decoupling with load balancing improvements without transparent decomposition.** The 36% claim (abstract, Section 5.2) compares the combined effect of ODC's communication reformulation *and* LB-Mini's more flexible packing against a collective baseline (likely Collective+LocalSort or Collective+LB-Micro). While the paper does present ODC+LB-Micro vs Collective+LB-Micro results (isolating the communication benefit, ~15-22% in the parametric study), the headline number is not decomposed. A reader expecting the 36% to reflect purely communication-driven gains would be misled. The paper should state which specific comparison yields 36% and separately report what fraction comes from ODC vs. from LB-Mini.

### Minor

3. **No statistical significance or variance reporting.** All throughput results are presented as single data points without error bars, confidence intervals, or repeated-run statistics. Given the stochastic nature of sequence packing and GPU execution timing, the magnitude of runtime variance at the reported settings cannot be assessed from the paper. This is a standard practice concern in systems papers, not a fatal issue, but it would strengthen the evaluation to report at least a range or standard deviation for key results.

4. **Training convergence verification is deferred to the appendix.** The paper states "we validate the correctness of ODC by verifying the training convergency in Appendix F" (Section 5.1). Since ODC changes the communication pattern (point-to-point vs. collective), a brief convergence plot in the main body would provide important reassurance that training dynamics are preserved. The current presentation forces the reader to take this on faith.

5. **Under-described daemon implementation for gradient accumulation.** The paper states that gradient accumulation is "handled by a lightweight daemon" (Section 3.2), but does not describe how this daemon is scheduled, whether it consumes GPU cycles, or whether it could cause contention on GPU memory bandwidth. Given that the claim of "non-intrusive" point-to-point transfers is critical to ODC's design, these details matter for assessing implementation soundness.

### Trivial

6. **Equation (1) models per-layer runtime as additive max-over-devices without overlap.** This is an idealized bound that does not account for communication-computation overlap. The paper acknowledges overlap exists but notes it "does not remove the underlying synchronization points." The equation is used for conceptual illustration and is not misleading, but the mismatch between the formal model and actual FSDP behavior could be noted more explicitly.

## Nice-to-Haves

- A breakdown of per-minibatch time into compute, communication, and idle for ODC vs. collective under the same load balancing would directly validate the claim that ODC reduces idle time and show whether communication overhead is hidden by computation. The "bubble rate" mentioned in Appendix G would serve this purpose, but including a representative plot in the main paper would strengthen the mechanism story.
- Evaluating ODC at larger scales (e.g., 64-128 GPUs) would help characterize the regime where inter-node communication penalties eventually outweigh the imbalance-tolerance benefit—an acknowledged limitation the paper discusses but does not quantify.
- Including the same microbatch assignments for both ODC and collective in at least one comparison (leaving only the communication primitive as the variable) would provide a cleaner "apples-to-apples" verification.

## Removed Points

These points were raised by reviewers but are removed for the following reasons:

- *Criticism about missing related work citations*: removed per instructions — I cannot verify literature gaps from the paper alone.
- *Criticism about the RL experiment needing identical microbatch assignments as a control*: downgraded to Nice-to-Have. The paper already compares ODC+LB-Micro vs Collective+LB-Micro in Figure 9, which uses the same packing algorithm. Requesting identical per-device microbatch assignments is a stricter standard that would be informative but is not needed to validate the reported differences.
- *Criticism that the parametric study golden setting is "narrow"*: removed. The methodology of holding all but one factor constant is standard and appropriate for isolating each factor's effect.
- *Criticism about the communication primitive benchmark using synchronous launch*: removed. The paper explicitly states this was intentional ("For fairness, ODC primitives are launched synchronously"). The end-to-end results, which include realistic overlap, are what matter for the paper's claims.
- *Criticism about Equation (1) being an overstatement*: downgraded to Trivial. The paper acknowledges overlap exists, and the equation is used as an idealized bound to motivate the problem, not as a precise model.
- *Criticism about derivations in the appendix*: removed. The appendix was stripped by the paper parser; these exist in the original submission.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Resolve the Collective LB-Mini inconsistency**: either remove this baseline from Figure 8 (it is not essential to the paper's claims, which can be established by comparing ODC+LB-Mini vs Collective+LB-Micro and ODC+LB-Micro vs Collective+LB-Micro) or explicitly describe how it was implemented and why it is a fair comparison given the stated incompatibility.

2. **Decompose the 36% headline**: clearly state which comparison produces the 36% speedup, and separately report the gain attributable to ODC's communication decoupling (ODC+LB-Micro vs Collective+LB-Micro) vs. the additional gain from LB-Mini's flexibility (ODC+LB-Mini vs ODC+LB-Micro). This would make the contribution assessment more transparent.

3. **Add multiple-run statistics** (e.g., range or standard deviation) for at least the flagship result configuration that produces the 36% speedup.

4. **Include a brief convergence comparison** (loss curves for ODC vs. collective with identical microbatches) in the main paper, even as a small figure, to directly validate training correctness.

## Score and Decision

**Round 1 bracketing:** The paper sits between weak anchors (1.67–3.25, largely rejected papers on parameter-server/distributed training topics) and strong anchors (7.60–8.50, accepted papers with convergence theory and larger-scale experiments). The narrowest plausible range from round 1 was **4.5–6.5**.

**Round 2 narrowing:** Comparing against anchors in the 4.5–7.5 range:
- *DynMo* (avg 5.25): addresses load balancing for dynamic LLMs but with less novel solutions; ODC is stronger in motivation clarity and contribution novelty.
- *DSP* (avg 5.40): dynamic sequence parallelism with similar technical depth; ODC is comparable in evaluation thoroughness.
- *Scalable Decentralized Learning with Teleportation* (avg 5.75): decentralized learning with convergence guarantees; ODC lacks convergence theory but has stronger empirical motivation and real-task evaluation.
- *CO2* (avg 7.00): communication-computation overlap with convergence proof, larger-scale experiments (128 GPUs), but addresses a different regime (limited bandwidth vs. workload imbalance); ODC's problem framing is more novel but the evaluation is less extensive.
- *From Promise to Practice* (avg 6.67): decentralized training with runtime modeling; stronger theoretical framing, similar evaluation scale.

ODC is clearly stronger than the 5.0–5.4 anchors (better motivation, cleaner solution, more thorough evaluation) but weaker than the 6.67+ anchors (which have convergence theory, larger-scale experiments, or more rigorous analytical modeling). The paper's main weaknesses—the Collective LB-Mini inconsistency, the muddy 36% headline, and the lack of convergence curves/error bars in the main paper—prevent it from reaching the stronger tier.

**Final score: 5.5** — a solid paper with a genuine contribution. The core idea (replacing collectives with point-to-point communication to relax synchronization barriers) is well-motivated and empirically validated across diverse settings. The evaluation is thorough for its scale, and the parametric study is a strength. However, the presentation of the main results contains an inconsistency (Collective LB-Mini) and the headline speedup conflates two distinct improvements without decomposition, which a strong revision should address.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>