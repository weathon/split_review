Now let me read the rest of the paper for the appendix sections mentioned, then run calibration searches.Now let me run the Round 1 bracketing calibration search across three score bands.Let me read the most topically similar anchors to narrow my bracket.Round 1 bracket: **6.0–7.5**. The paper is clearly stronger than the weak/middle-low anchors (ACCO at 5.0, decentralized training at 6.67), with more specific targeting of a real LLM bottleneck, more diverse evaluation, and concrete implementation. Not at the 8+ tier due to the identified inconsistencies and scalability gaps. Now narrowing.Let me read the most comparable anchors in detail.Now I have sufficient anchor comparisons. Let me write the final review.

**Calibration summary:**
- Round 1 bracket: 6.0–7.5
- Round 2 anchors: CO2 (7.00) and NetMoE (7.20) are the closest topically; "From Promise to Practice" (6.67) and ACCO (5.00) are relevant lower anchors
- The ODC paper is comparable to CO2 (7.00) in scope and empirical diversity, but the "Collective LB-Mini" inconsistency and 32-device ceiling narrow it to **6.5**

---

## Summary

This paper proposes **On-Demand Communication (ODC)**, a new communication scheme for FSDP-based LLM post-training that replaces per-layer collective all-gather/reduce-scatter operations with RDMA-based point-to-point gather and scatter-accumulate primitives. The key insight is that FSDP's fine-grained layer-level synchronization barriers create straggler effects under the variable-sequence-length workloads prevalent in LLM post-training, and these barriers are an artifact of the communication model rather than a requirement of the training algorithm. ODC relaxes synchronization from layer level to minibatch level and enables a simplified, more effective minibatch-level load balancing strategy (LB-Mini). Evaluated across SFT (LongAlign, SWE-Smith) and RL (AIME/GRPO) tasks on 1.5B–32B models, ODC achieves up to 36% throughput improvement over standard FSDP.

---

## Strengths

- **Precisely identified and formalized root cause.** Equation (1) explicitly captures the per-layer synchronization cost under FSDP and Figures 1–4 illustrate it clearly. The argument that the synchronization barrier is an artifact of the communication model — not a requirement of the optimization algorithm — is correct and well-stated.

- **Technically sound and elegant mechanism.** ODC's decomposition of all-gather into targeted gather requests and reduce-scatter into scatter-accumulate operations (Section 3, Figures 5–6), implemented via CUDA IPC (intra-node) and NVSHMEM (inter-node), is a natural fit for the on-demand paradigm and integrates with FSDP's sharding layout with minimal disruption.

- **Empirically diverse and consistent.** Figures 8 and 9 show throughput gains across 1.5B, 7B, 14B, and 32B models on two SFT datasets and one RL benchmark, in both unpacked (LocalSort) and packed (LB-Micro/LB-Mini) settings. The parametric study (Figure 10) isolates four factors (minibatch size, sequence length, packing ratio, device count) and explains when and why gains are most pronounced, which is practically valuable guidance.

- **Honest treatment of limitations.** Section 6.1 and Figure 11 explicitly show that ODC's RDMA-based primitives lag significantly behind NCCL collectives in multi-node (16–32 device) settings, and the paper proposes credible mitigations (computation-communication overlap, hybrid sharding). The RL gains are transparently labeled as lower-bound estimates due to verl implementation constraints.

- **LB-Mini enables a genuinely larger feasible solution space.** Section 4's insight that ODC removes the uniform-microbatch-count constraint, opening minibatch-level (rather than microbatch-level) load balancing, is a concrete and practical consequence of the decoupled execution model, not merely a claimed side-benefit.

---

## Weaknesses

### Fatal
None.

### Major

- **"Collective LB-Mini" baseline contradicts stated constraint.** Section 5.1 explicitly states: *"As LB-Mini can produce different number of microbatches for different devices, it applies only to ODC."* Yet Figure 8 includes "Collective LB-Mini (purple triangles)" as a comparison point. If collective communication requires uniform microbatch counts per device, the "Collective LB-Mini" baseline must be using a *constrained* variant of LB-Mini that pads or truncates to enforce uniformity — making it a different, degraded algorithm from the full LB-Mini applied to ODC. The comparison then becomes ODC+full-LB-Mini vs. Collective+degraded-LB-Mini, which structurally favors ODC regardless of the communication scheme. The paper never explains what "Collective LB-Mini" actually does. This muddies the central evaluation: the fair comparison for isolating the communication-scheme contribution is ODC+LB-Micro vs. Collective+LB-Micro (which does appear in Figures 8 and 10), but the unexplained "Collective LB-Mini" baseline creates ambiguity about the fairness of the headline results. The authors must clarify this baseline's implementation or label it as "Collective+constrained-LB-Mini."

- **Headline 36% speedup conflates two separable contributions.** The 36% figure arises from ODC+LB-Mini combined. The communication-scheme-only contribution, isolable via ODC+LB-Micro vs. Collective+LB-Micro in Figure 10, is 10–22% depending on setting. This is not a flaw — both contributions are real and together constitute the system — but the current framing risks misleading readers about how much of the gain comes from the new communication scheme versus the new load-balancing algorithm. The paper should explicitly disentangle these two effects in its summary claims.

### Minor

- **No evaluation under balanced workloads.** A complete systems contribution should verify that ODC does not regress significantly when the problem it targets (workload imbalance) is absent. A brief experiment on a dataset with low sequence variance (or artificially balanced batches) would confirm ODC is safe to deploy without requiring prior knowledge of workload distribution. This gap is not fatal since the parametric study (packing ratio = 8 in Figure 10) shows gains diminish toward 5–15%, but a direct balanced-workload ablation is missing.

- **Scalability evidence limited to 32 devices.** Section 5.1 states experiments use "up to 32 NVIDIA A100 80G GPUs." Production LLM post-training often spans 64–512 devices, where the interaction between growing straggler benefit (shown growing in Figure 10) and growing inter-node bandwidth deficit (Figure 11) is nonlinear and unexplored. The paper discusses this limitation and proposes hybrid sharding (Appendix E), but the scope of the main claims should be more clearly anchored to the evaluated regime.

### Trivial
None.

---

## Nice-to-Haves

- **Complementary formal expression for ODC's minibatch cost.** Equation (1) formalizes FSDP's minibatch runtime under layer-level synchronization. A companion equation showing how ODC relaxes this to a single minibatch-boundary barrier would make the theoretical argument self-contained rather than relying on prose.

- **Characterization of LB-Mini's computational overhead.** The paper defers the partition algorithm to Appendix C (stripped from review) but does not characterize how long the bin-packing-style optimization takes per minibatch during training. For large minibatch sizes, this overhead could be non-negligible.

- **Parametric study on larger models.** The parametric study (Figure 10) uses only the 1.5B model on LongAlign. Understanding how the tradeoff curve shifts for 7B and 14B models (where communication represents a different fraction of compute) would substantially strengthen the practitioner-guidance value of Section 5.3.

---

## Removed Points

*These points are flagged to be removed, treat them with caution.*

1. **Harsh critic: atomicity/race condition concern for scatter-accumulate.** The critic notes that RDMA writes are non-atomic and that the daemon-based gradient accumulation lacks an explicit atomicity argument in the main text. This is a reproducibility concern about implementation detail that the paper explicitly defers to Appendix B and validates empirically in Appendix F. Removed per the rule against reproducibility nitpicks for details impractical to include in the main text.

2. **Harsh critic: formal proof that ODC "preserves synchronous optimization semantics."** The critic argues the claim needs formal proof. While a formal argument would strengthen the paper, the intuition is correct (synchronization occurs at minibatch boundary; all gradients are accumulated before the optimizer step). Demoting to Nice-to-Have would be appropriate but since it was framed as a missing proof issue for an otherwise verified-empirically claim, it is removed from the weakness list per the rule about missing proofs in appendix/supplementary.

3. **Strength finder: "this paper addresses an important problem."** Removed as a generic strength not tied to concrete content. The problem importance is captured in the more specific Strengths above.

4. **Strength finder: "simplified load balancing enabled by ODC."** Partially kept — this is a concrete contribution (LB-Mini enabling minibatch-level balancing) — but was filtered to ensure it is only claimed for the intra-node / small-minibatch regime where it demonstrably outperforms LB-Micro (Figure 8, LongAlign 1.5B with minibatch=2), not universally.

---

## Novel Insights

The paper's most interesting contribution is the reframing: FSDP's per-layer collective synchronization is not a requirement of synchronous data-parallel optimization — it is a constraint imposed by the collective communication model. This reframing opens the conceptual door to colocated parameter-server semantics within modern sharded DP, without abandoning FSDP's memory layout, optimizer sharding, or training semantics. The observation that communication volume is constant in sequence length while compute grows quadratically (O(s²)) — meaning long sequences self-hide communication cost — is a clean and practically important insight that explains why ODC's inter-node bandwidth penalty does not manifest as a regression in the long-context experiments. This compute-hides-communication argument has broad applicability beyond ODC.

---

## Suggestions

1. **Explain "Collective LB-Mini" precisely.** State exactly how LB-Mini is adapted for collective communication (e.g., what constraint is imposed on microbatch counts, and how this degrades the balancing quality). If it is a constrained variant, label it "Collective LB-Mini (constrained)" and acknowledge the asymmetry explicitly.

2. **Disentangle ODC vs. LB-Mini contributions in the abstract and conclusion.** Report both the combined gain and the communication-only gain (from the ODC+LB-Micro vs. Collective+LB-Micro comparison) so readers can attribute the improvement correctly.

3. **Add one balanced-workload experiment.** A single row in an ablation table showing ODC throughput on a dataset with near-uniform sequence lengths (e.g., truncated to fixed length) would confirm there is no material regression when workload imbalance is absent.

4. **Frame RL results as a lower bound.** The paper currently says the verl implementation constraint "limits the effectiveness of LB-Mini" — it should explicitly state that the ~10% RL speedup is an underestimate of what ODC+full-LB-Mini would achieve in an unconstrained implementation.

---

## Score Calibration

**All anchors retrieved:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| bntJK4NyIW.md | 2.00 | R1 | Decentralized training, much weaker — lacks solid empirical evaluation, has major gaps |
| b7HOhqXiZs.md | 2.60 | R1 | Gradient communication reduction — weak novelty and empirical results |
| E4Fk3YuG56.md | 8.50 | R1 | Cut Cross-Entropy — tighter kernel contribution; stronger than ODC paper |
| cPZepCZlFW.md | 3.25 | R1 | Fault-tolerant training — less specific contribution |
| UV1jr2aJ2J.md | 5.00 | R1 | ACCO — similar domain, weaker: more limited evaluation, novelty concerns |
| lo3nlFHOft.md | 6.67 | R1 | High-performance decentralized training — comparable quality, missed related work |
| 0cadcLKbt7.md | 4.00 | R1 | Edge LLM inference — different scope, weaker contribution |
| N80ER2he6l.md | 5.00 | R1 | VLM computation balance — less specific mechanism |
| t7P5BUKcYv.md | 8.00 | R1 | MoE++ — broader algorithmic contribution, stronger |
| vf5aUZT0Fz.md | 8.00 | R1 | DEPT — different domain; stronger novelty |
| wg1PCg3CUP.md | 8.00 | R1 | Scaling Laws for Precision — different scope, stronger theoretical grounding |
| f4gF6AIHRy.md | 8.00 | R1 | Data selection for LLMs — different domain |
| 7JhGdZvW4T.md | 6.00 | R2 | LLM scheduling — similar domain but narrower scope |
| qDKTMjoFbC.md | 5.60 | R2 | BurstAttention — related distributed attention framework, less diverse evaluation |
| ZO5cn4IfaN.md | 7.00 | R2 | CO2 — most comparable: asynchronous communication-computation overlap, 128 GPUs, accepted; similar quality to ODC |
| yroyhkhWS6.md | 6.75 | R2 | Quadratic Synchronization Rule — theory-heavy; different axis |
| 1qP3lsatCR.md | 7.20 | R2 | NetMoE — elegant ILP formulation, clean methodology; slightly stronger than ODC |
| vMNpv5OBGb.md | 5.67 | R2 | UniAP — auto-parallelism search, weaker empirical evidence |
| tuzTN0eIO5.md | 7.00 | R2 | Zero Bubble Pipeline Parallelism — clean mechanism, elegant contribution; comparable |

**Round 1 bracket:** 6.0–7.5  
**Round 2 narrowing:** The paper sits between CO2 (7.00) and "From Promise to Practice" (6.67). It is comparable to CO2 in practical scope and empirical diversity, but the "Collective LB-Mini" inconsistency — a real evidential problem that CO2 does not have — and the 32-device ceiling drag it slightly below 7.0. The paper is clearly above 6.67 in terms of domain relevance and evaluation thoroughness. Final score: **6.5**.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>