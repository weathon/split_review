Now I have enough information to write a thorough meta-review. Let me assess each rebuttal claim against the paper.

## Summary

This paper proposes **On-Demand Communication (ODC)**, which adapts parameter server semantics into FSDP-based LLM post-training by replacing per-layer collective all-gather/reduce-scatter operations with RDMA-based point-to-point gather and scatter-accumulate primitives. The key insight is that FSDP's per-layer synchronization barriers are an artifact of the collective communication model — not a requirement of the optimization algorithm — and can be relaxed to minibatch-level barriers under workload-imbalanced settings (variable-sequence-length LLM post-training). This also enables a minibatch-level load balancing strategy (LB-Mini) that is infeasible under collective communication. Evaluated on SFT and RL tasks across 1.5B–32B models, ODC achieves up to 36% throughput improvement over standard FSDP.

---

## Rebuttal Assessment

---

**Weakness:** "Collective LB-Mini" baseline contradicts stated constraint
- **Author's response:** Partially address
- **Assessment:** Partially convincing — The authors reveal that "Collective LB-Mini" enforces uniform microbatch counts via padding, which is a reasonable and technically coherent design that would explain what the baseline does. This explanation is plausible: padding shorter device assignments to the maximum microbatch count is how you would adapt a variable-microbatch strategy to collective requirements. **However**, this explanation is entirely absent from the paper. Section 5.1 states only that "LB-Mini applies only to ODC" — it does not describe what "Collective LB-Mini" actually does. The paper includes this baseline in Figure 8 without explaining its implementation, making the "major" concern in the original review factually grounded. The promised fix ("we will rename it 'Collective LB-Mini (uniform padded)' and add a one-sentence explanation") is a revision promise, not evidence already in the paper. The authors are correct that the clean communication-scheme-only comparison (ODC+LB-Micro vs. Collective+LB-Micro) is present in Figure 10. Given the plausible explanation, the weakness is **downgraded from major to minor** — it is a presentation gap rather than a methodological flaw — but the paper in its current form still contains the unexplained baseline.
- **Score impact:** Weakness downgraded (major → minor)

---

**Weakness:** Headline 36% speedup conflates two separable contributions
- **Author's response:** Partially address
- **Assessment:** Partially convincing — The authors correctly note that the communication-only contribution (10–22%) is already isolated in Figure 10 (ODC+LB-Micro vs. Collective+LB-Micro). Verified in the paper: Figure 10 caption reads "Acceleration ratio of ODC compared to collective with LB-Micro in parametric study" and the chart description confirms 10–22% gains for ODC+LB-Micro. This data is indeed present in the paper. The issue is entirely about prominence — the abstract and conclusion report only the 36% combined figure without decomposing contributions. The promised abstract/conclusion revision would resolve this, but it does not exist in the current paper. The concern is a presentation weakness, not a methodological flaw.
- **Score impact:** Weakness downgraded (major → minor)

---

**Weakness:** No evaluation under balanced workloads
- **Author's response:** Partially address
- **Assessment:** Partially convincing — The authors point to Figure 10's packing ratio sweep. Verified: Figure 10 shows that at packing ratio 8, ODC+LB-Mini achieves ~15% and ODC+LB-Micro achieves ~5% gains. This is diminishing but nonzero improvement — it does not constitute a "balanced workload" experiment since even packing ratio 8 doesn't eliminate imbalance. The within-node bandwidth parity (Figure 11, ≤8 devices) implies no regression for intra-node settings, but this is indirect. The promised balanced-workload ablation ("we will add this if accepted") does not count. The weakness is real but the indirect evidence is at least suggestive of no regression.
- **Score impact:** Weakness unchanged

---

**Weakness:** Scalability evidence limited to 32 devices
- **Author's response:** Acknowledge
- **Assessment:** Unconvincing as a resolution — The authors honestly acknowledge this is a valid limitation and commit to clearer scope language. Section 6.1 and Appendix E (hybrid sharding) are already in the paper as the reviewer noted. The authors confirm the 32-device ceiling is genuine. Acknowledgment is honest but does not remove the gap. The hybrid sharding proposal is not demonstrated empirically in the main paper.
- **Score impact:** Weakness unchanged

---

## Strengths

- **Precisely identified root cause.** Equation (1) explicitly formalizes per-layer synchronization cost; Figure 1–4 illustrate the straggler mechanism clearly. The argument that synchronization barriers are artifacts of the collective communication model — not requirements of the optimization algorithm — is correct and well-stated.
- **Technically sound mechanism.** ODC's decomposition of all-gather into targeted gather requests and reduce-scatter into scatter-accumulate (Section 3, Figures 5–6), implemented via CUDA IPC and NVSHMEM through Triton-Distributed, integrates cleanly with FSDP's sharding layout. The daemon-based gradient accumulation for non-interruptive server operation is a credible engineering solution.
- **Empirically diverse and consistent.** Figures 8 and 9 show consistent throughput gains across 1.5B, 7B, 14B, and 32B models on two SFT datasets and one RL benchmark. The parametric study (Figure 10) isolates four factors and gives actionable practitioner guidance.
- **Honest treatment of limitations.** Section 6.1 and Figure 11 explicitly reveal the inter-node bandwidth deficit and propose credible mitigations. The RL gains are transparently labeled as constrained by verl implementation rather than fundamental ODC limits.
- **LB-Mini enables a genuinely larger feasible solution space.** Section 4 correctly identifies that ODC removes the uniform microbatch count constraint, enabling minibatch-level balancing. Verified: Figure 8 shows LB-Mini consistently outperforms LB-Micro at small minibatch sizes (minibatch=2) where variable microbatch counts matter most.

---

## Weaknesses

### Fatal
None.

### Major
None. (Original major weaknesses are both downgraded: the "Collective LB-Mini" issue is a labeling/explanation gap with a plausible implementation; the headline conflation has the supporting data already in Figure 10.)

### Minor

- **"Collective LB-Mini" baseline is unlabeled and unexplained in the paper.** Section 5.1 states LB-Mini "applies only to ODC" but Figure 8 includes "Collective LB-Mini" without explaining how it was adapted. The rebuttal explains it uses padded uniform microbatch counts, which is plausible, but this explanation is missing from the submitted paper. The comparison between ODC+full-LB-Mini and Collective+padded-LB-Mini structurally favors ODC even if the minibatch-assignment strategy is equivalent. The headline comparison should be relabeled in the revision.

- **Abstract and conclusion conflate ODC and LB-Mini contributions.** The 36% headline bundles two separable contributions. The communication-only gain (10–22%) is isolated in Figure 10 but not surfaced in the abstract or conclusion. Readers cannot correctly attribute the improvement without reading the parametric study.

- **No balanced-workload experiment.** The packing ratio sweep (Figure 10, packing ratio=8: ~5% ODC+LB-Micro gain) provides indirect evidence of no regression, but a single fixed-length dataset experiment would confirm this definitively. The 32-device evaluation ceiling means claims should be explicitly scoped.

### Trivial

- Parametric study uses only the 1.5B model on LongAlign; it is unclear how the tradeoff curve shifts for 7B+ models.
- LB-Mini's bin-packing computational overhead per minibatch is uncharacterized.

---

## Nice-to-Haves

- A companion equation to Equation (1) formalizing ODC's minibatch runtime (single boundary barrier) would make the theoretical argument self-contained.
- A brief fixed-length (balanced workload) experiment would confirm ODC's safe deployment without prior knowledge of workload distribution.
- Explicit quantification of both contributions in the abstract: "10–22% from relaxed synchronization alone, and up to 36% combined with LB-Mini."

---

## Novel Insights

The paper's most important reframing is that FSDP's per-layer collective synchronization is not a requirement of synchronous data-parallel optimization — it is a constraint imposed by the collective communication model. This opens the conceptual door to colocated parameter-server semantics within sharded DP, without abandoning FSDP's memory layout, optimizer sharding, or training semantics. The compute-hides-communication argument (communication volume is O(1) in sequence length; attention compute is O(s²)) is a clean and practically important insight explaining why ODC's inter-node bandwidth penalty does not manifest as regression in long-context experiments. This insight has broad applicability to other communication-computation overlap analyses beyond ODC.

---

## Suggestions

1. **Relabel and explain "Collective LB-Mini"** as "Collective LB-Mini (padded uniform)" with a one-sentence description of the uniform microbatch constraint in Section 5.1.
2. **Revise the abstract and conclusion** to report both the combined gain (up to 36%) and the communication-scheme-only gain (10–22% from ODC+LB-Micro vs. Collective+LB-Micro) so readers can correctly attribute contributions.
3. **Add one balanced-workload experiment** — a single ablation row on a truncated fixed-length dataset would confirm no material regression when imbalance is absent.
4. **Anchor scope language** in Section 5.1 and the conclusion to the 8–32 device regime; frame hybrid sharding as a required engineering step for larger deployments rather than a validated solution.

---

## Score and Decision

**Rebuttal effect summary:** The rebuttal is partially convincing overall. The two original major weaknesses are downgraded to minor: the "Collective LB-Mini" inconsistency is a labeling and explanation gap rather than a methodological flaw (the padded implementation is plausible and the clean comparison is already in Figure 10), and the headline conflation is a presentation issue with the supporting data already present in Figure 10. The two minor weaknesses (no balanced-workload experiment, 32-device ceiling) are unchanged — the authors acknowledge them honestly but propose only future fixes. No new problems are revealed by the rebuttal; no author claims are contradicted by the paper.

The paper's core technical contribution is sound and the evaluation is empirically honest. The remaining weaknesses are all presentation/scope issues that a revision can address. Anchoring relative to the original 6.5: the major weaknesses being downgraded to minor moves the paper slightly upward, but the fixes are all in future revisions, not in the submitted paper. The score moves modestly from 6.5 to 6.5 — the rebuttal provides clarity that the problems are smaller than the original assessment but does not resolve them in the submitted version.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>