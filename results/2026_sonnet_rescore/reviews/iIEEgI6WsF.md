Now I have sufficient information to write the final consolidated meta-review.

---

## Summary

This paper proposes **On-Demand Communication (ODC)**, a communication scheme that replaces FSDP's per-layer collective all-gather/reduce-scatter operations with RDMA-based point-to-point communication, effectively reframing FSDP as a parameter-server architecture. The core insight is that per-layer collective synchronization in FSDP introduces unavoidable straggler-induced idle time under the imbalanced sequence-length distributions common in LLM post-training. ODC relaxes synchronization from per-layer to per-minibatch, and enables a complementary minibatch-level load balancing algorithm (LB-Mini) that was infeasible under collective semantics. Across SFT and RL tasks on 1.5B–32B models, ODC achieves up to 36% throughput improvement over standard FSDP.

---

## Strengths

- **Precise problem formalization.** Equation (1) in Section 2.2 directly formalizes FSDP's synchronization cost as a sum of per-layer per-device maximums: $T(\mathcal{P}_M) = \sum_{m=1}^M \sum_{l=1}^L \max_d T_{m,d,l}(\mathcal{P}_M)$. This grounds the contribution in a clear bottleneck analysis rather than vague motivation.

- **Technically sound mechanism.** The decomposition of all-gather/reduce-scatter into on-demand point-to-point gather and scatter-accumulate (Section 3, Figures 5–6) preserves FSDP's sharded memory layout and synchronous minibatch semantics while removing per-layer barriers. The design rationale (RDMA for transparency and one-sided operation; daemon for gradient accumulation) is well-matched to the architectural requirements.

- **Consistent and diverse empirical evidence.** Figures 8 and 9 show throughput improvements across model scales (1.5B, 7B, 14B, 32B), tasks (SFT on LongAlign/SWE-Smith, RL on AIME), and load-balancing settings. The parametric study (Section 5.3, Figure 10) isolates the effect of minibatch size, sequence length, packing ratio, and device count, confirming that gains are robust and that longer sequences and more devices amplify ODC's advantage.

- **Honest reporting of limitations.** Section 6.1 and Figure 11 explicitly show that ODC's RDMA-based primitives are significantly slower than NCCL collectives in multi-node settings, and the paper discusses concrete mitigations (computation overlap for long sequences, hybrid sharding analogous to ZeRO++). This level of candor strengthens rather than undermines the paper's credibility.

- **Practical load-balancing insight.** The LB-Mini strategy (Section 4) correctly identifies that removing the uniform-microbatch-count constraint enables a strictly larger feasible solution space for load balancing. This is not just a theoretical observation — Figure 8 shows LB-Mini consistently outperforming LB-Micro at smaller minibatch sizes where load variance is highest.

---

## Weaknesses

### Fatal
None.

### Major

- **The "Collective LB-Mini" baseline in Figure 8 contradicts the paper's own constraint.** Section 5.1 explicitly states: *"As LB-Mini can produce different number of microbatches for different devices, it applies only to ODC."* Yet Figure 8 includes "Collective LB-Mini" (purple triangles) as a comparison point. This is an unresolved internal inconsistency. If "Collective LB-Mini" uses a constrained variant that enforces uniform microbatch counts to satisfy collective semantics, then the comparison is between ODC's flexible full LB-Mini and a degraded LB-Mini under collective — which structurally favors ODC regardless of communication scheme. If it is the same algorithm, the constraint stated in Section 5.1 is wrong. The paper does not clarify this, which clouds the fairest possible apples-to-apples comparison in the main results figure. **Why it matters:** The headline speedup figures in Figure 8 directly depend on these comparisons, and the interpretation of how much gain is attributable to the communication scheme alone vs. the load-balancing advantage is left ambiguous.

- **36% headline conflates two separable contributions.** The 36% speedup in the abstract and Section 5.2 arises from ODC+LB-Mini combined. Section 5.3/Figure 10 shows that ODC+LB-Micro (isolating the communication effect while controlling for load-balancing) achieves roughly 15–22% depending on conditions, with the remainder attributable to LB-Mini's variable-microbatch flexibility. Both contributions are genuine and together constitute the system, but the paper's framing does not cleanly attribute how much each component contributes. A reader of the abstract would attribute the full 36% to the communication scheme. **Why it matters:** Understanding which workload characteristics make ODC (as a communication scheme) beneficial, versus which favor LB-Mini (as a load balancing algorithm), is practically relevant for deployment decisions.

### Minor

- **Inter-node scalability evidence stops at 32 devices.** Figure 11 demonstrates that ODC's RDMA-based primitives are substantially slower than NCCL collectives in multi-node configurations, and Figure 10 explores device scaling only up to 32 devices. Production post-training pipelines commonly operate at 64–256+ devices. The interaction between the growing straggler benefit (which the paper shows increases with device count in Figure 10) and the growing per-primitive inter-node bandwidth deficit is nonlinear and is not characterized beyond 32 devices. Hybrid sharding is mentioned as a mitigation but is evaluated only in the appendix (stripped). **Why it matters:** Practitioners considering deploying ODC at scale cannot determine the crossover point without this analysis.

- **The synchronous-semantics claim is stated but not argued.** Section 1 claims ODC "preserv[es] the synchronous optimization semantics." This is intuited correctly — synchronization occurs at the minibatch boundary, and all gradients are accumulated before the optimizer step — but the concurrent scatter-accumulate operations from multiple workers to the same server shard via one-sided RDMA introduce the possibility of non-deterministic accumulation order. The paper does not argue that this is equivalent to reduce-scatter in expectation, and implementation details (daemon serialization, atomicity guarantees) are deferred to the appendix. While practically harmless and empirically verified (Appendix F, per the harsh critic), a brief in-text argument would make the claim self-contained.

### Trivial

- Section 2.2's Equation (1) formally characterizes FSDP's runtime cost but no complementary equation characterizes ODC's runtime. A corresponding expression would make the theoretical comparison self-contained without requiring the reader to reason informally.

---

## Nice-to-Haves

- An ablation on a **balanced workload** (low sequence variance) would verify that ODC incurs minimal overhead when the imbalance problem is absent, reassuring practitioners that ODC is safe to deploy without advance knowledge of workload characteristics.
- The parametric study (Figure 10) is the paper's most analytically valuable section and currently covers only a 1.5B model on LongAlign. Extending it to a 7B or 14B model would reveal whether the acceleration curves shift meaningfully with model size, strengthening the "where to deploy ODC" guidance.
- A brief characterization of the computational overhead of solving the LB-Mini partition problem at minibatch granularity during training would address an unstated but practical concern about amortized overhead.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Reproducibility concern about RDMA atomicity implementation details.** The harsh critic flagged the absence of an in-text atomicity mechanism as a reproducibility gap. Removed per the rule that nitpicks about undisclosed implementation details deferred to the appendix (which exists in the original submission) do not constitute weaknesses. The paper is also open-sourced.
- **"Missing complementary equation for ODC runtime"** — Retained as a Trivial issue; it is a small presentation improvement, not a scientific flaw.
- **Strength: "paper addresses an important problem"** — Removed as generic; the specific problem formalization via Eq. (1) is retained as a concrete strength instead.
- **Strength about "broader significance to distributed training community"** — Generic, removed.

---

## Novel Insights

The central novel insight from synthesizing the reviews is that ODC's real value has two distinct but coupled components: (1) a communication-scheme benefit that relaxes per-layer synchronization barriers, measurable in isolation via ODC+LB-Micro vs. Collective+LB-Micro; and (2) a load-balancing benefit that is only unlocked by ODC's variable-microbatch capability. The paper's presentation does not cleanly separate these, which obscures a deeper point: the communication paradigm choice (collective vs. point-to-point) is not just an engineering tradeoff but a *constraint on the space of feasible scheduling algorithms*. This framing — that ODC's most important contribution may be the scheduling flexibility it enables rather than the raw communication efficiency — is implicit throughout but never stated as the organizing thesis.

---

## Suggestions

1. **Clarify "Collective LB-Mini" in Figure 8.** Add a sentence explaining exactly how LB-Mini is adapted to work with collectives (e.g., uniform-microbatch enforcement, or partition-only with standard packing). If it is a degraded variant, say so explicitly and note this structurally favors ODC — which strengthens rather than weakens the argument.
2. **Decompose the 36% attribution.** Add a column or inset in Figures 8–9 (or in Section 5.3) explicitly showing the ODC communication gain (ODC+LB-Micro vs. Collective+LB-Micro) and the LB-Mini load-balancing gain (ODC+LB-Mini vs. ODC+LB-Micro) as separate contributions, making both claims individually clear.
3. **Scope the recommendation more precisely.** Based on Figure 10, provide explicit guidance: "ODC provides >X% benefit when max sequence length exceeds Y tokens and device count exceeds Z."
4. **Report a balanced-workload baseline.** Even a single data point on a low-variance dataset (e.g., fixed-length samples) would establish that ODC is safe to deploy without prior workload profiling.

---

## Score and Decision

**Originality:** The core idea of applying parameter-server semantics within FSDP is a substantive reuse of a classical paradigm, but the technical realization (RDMA-based primitives, daemon for accumulation, minibatch-level synchronization, LB-Mini) is novel in the LLM post-training context. **4/5**

**Importance of research question:** Straggler-induced inefficiency in LLM post-training at scale is a genuine and pressing practical problem. **4/5**

**Claims well supported:** The 36% speedup claim is empirically consistent but inadequately decomposed (ODC vs. LB-Mini contributions); the Collective LB-Mini comparison is unexplained. Core claims (ODC reduces straggler overhead, gains grow with sequence length and device count) are well supported. **3/5**

**Soundness of experiments:** Diverse tasks, model scales, and metrics; Figure 10 parametric analysis is rigorous; inter-node scalability beyond 32 devices uncharacterized; the Collective LB-Mini comparison inconsistency is a genuine methodological gap. **3/5**

**Clarity of writing:** Generally clear; Section 3 and 6.1 are strong; the LB-Mini constraint/Figure 8 inconsistency is a notable clarity failure. **3/5**

**Value to research community:** Open-sourced implementation, directly applicable to real post-training pipelines, addresses a pain point that grows with model and sequence scale. **4/5**

The paper makes a genuine and practically important contribution with consistent empirical evidence and honest reporting of limitations. The internal inconsistency around "Collective LB-Mini" and the conflation of two separable contributions are the main weaknesses — both addressable in revision. The inter-node scalability gap is a real limitation but is acknowledged and partially mitigated. None of these are fatal, and the core claims are well-supported.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>3</clarity>
<community_value>4</community_value>
</subscores>