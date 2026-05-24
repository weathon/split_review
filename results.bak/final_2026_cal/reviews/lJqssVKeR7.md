Now I have all the information needed. Let me write the final consolidated review.

**Calibration summary:**

Round 1 bracket: The paper is clearly stronger than the weak ZO-FL papers (scores 2–4) and below the 8-range papers that aren't topically similar. Initial bracket: [4.5, 7.0].

Round 2 narrowing: Three most comparable anchors read in full:
- **Meerkat** (2DuMBKVbX2, score 5.00, Accept Poster): ZO-FL for LLMs, sparse updates. HiSo has a more novel contribution (generalized framework + Hessian-informed ZO vs. sparsity, which is well-explored) and stronger theory (d-independent rate). HiSo is stronger.
- **FOCUS** (jMzXLsHdnF, score 5.20, Reject): ZO Hessian-informed LLM fine-tuning (single-node, not FL). HiSo is in the FL setting, has a generalized framework, and has better empirical scope. HiSo is stronger.
- **HyperFedZero** (9XkmuBR0r1, score 5.50, Accept Poster): FL personalization with hypernetworks, theory-light. HiSo has stronger theory and comparable experiments.

Final placement: 5.5 — below the 6.00 GH-OFL anchor (which is a cleaner, more self-contained contribution) but above Meerkat (5.00) and FOCUS (5.20).

---

## Summary

This paper proposes **HiSo**, a Hessian-informed zeroth-order federated optimization method that integrates diagonal Hessian preconditioning with the scalar-only (dimension-free) communication framework pioneered by DeComFL. The paper makes three main contributions: (1) a generalized scalar-only communication FL framework that decouples dimension-free communication from vanilla ZO-SGD; (2) a Hessian-informed ZO update (Eqs. 8–10) that preserves scalar-only communication because the curvature information is reconstructed locally from shared seeds and scalars; and (3) convergence theory showing a dimension-independent rate under a well-approximated Hessian condition. Empirically, HiSo achieves 1.4–5.4× speedup over DeComFL on SST-2, QQP, and SQuAD with OPT-350M/1.3B/2.7B at KB-level communication cost.

## Strengths

- **Generalized scalar-only communication framework (Section 3.3, Algorithm 1).** The paper correctly identifies that dimension-free communication requires only scalar representations, not the specific ZO-SGD update. This decoupling enables integrating Hessian-informed optimization while preserving scalar-only uplink/downlink — a genuine conceptual advance beyond DeComFL.

- **Hessian-informed ZO update with zero additional communication cost (Section 4.1, Eqs. 8–10).** The derivation shows that the Hessian-informed ZO gradient estimator decomposes into a scalar term *g* and a direction term *H⁻¹/²u*. Because the direction is determined by a shared random seed and *H* is reconstructed locally, the update requires no additional communication of second-order information. This directly addresses the paper's central tension between acceleration and communication efficiency.

- **Global diagonal Hessian learned without extra communication (Section 4.2, Eq. 12).** The server and clients reconstruct the global diagonal Hessian *H* using the existing scalar-represented update vectors Δx (which are needed for model reconstruction anyway). Since the server knows the scalars *g* and shared seeds, and reconstructs *H* locally, it can compute the squared-update-based Hessian update entirely from already-communicated information. This is a clean design.

- **Convergence rate independent of model dimension *d* and Lipschitz constant *L* (Corollary 1).** Under the well-approximated Hessian and low-effective-rank assumptions, the paper proves a rate of *O*(√(ζ/mR)) for τ=1. This is the first such dimension-independent guarantee for ZO methods in federated learning.

- **Empirical 1.4–5.4× communication-round speedup over DeComFL on LLM tasks (Table 2).** On SST-2, QQP, and SQuAD with OPT-350M/1.3B/2.7B, HiSo reaches DeComFL's best accuracy in consistently fewer rounds, yielding 29%–80% communication savings at identical per-round communication cost. The speedup is purely algorithmic.

## Weaknesses

### Fatal
None.

### Major
None that threaten the paper's core claims.

### Minor

- **The Hessian update rule is not shown to satisfy the well-approximated condition required for the accelerated rate.** The convergence analysis (Corollaries 1–3) assumes *H* satisfies Tr(*H⁻¹/²*Σ*H⁻¹/²*) ≤ ζ ≪ *d*. The practical update (EMA of squared model-diffs) is a heuristic inspired by RMSProp/Adam, and the paper provides no theoretical or direct empirical verification that this *H* actually meets the condition. The paper is transparent about this gap (Section 5.2 Remarks: "Although it is hard to determine if this approximation holds…"; Appendix F.7.1: "if H_r fails… performance degenerates into DeComFL"), and the long-tail distribution of learned *H* entries (Figure 5, right) offers indirect support. Nevertheless, the theory does not *explain* the observed speedup — it describes an idealized algorithm. This weakens the paper's central theoretical claim but does not undermine the empirical contribution, which stands independently.

- **The number of local update steps τ is not reported for the LLM fine-tuning experiments (Tables 2 and 3).** This is a relevant hyperparameter because Corollary 3 shows that DeComFL's convergence rate becomes dimension-dependent again when τ > 1, while HiSo's remains dimension-independent. Without τ, the reader cannot fully assess the fairness of the comparison or reproduce the results. The paper reports *P* = 5 (perturbations per gradient estimate) and the MNIST experiment uses a specific τ, but the LLM experiments omit it.

- **The description of the Hessian update has a minor inconsistency between two formulations.** The main text (Section 4.2) first presents an update using per-client Δx_{r,τ}^{(i)}, while Eq. 12 and the simplified pseudocode (Section 4.3) use the global aggregated Δx_r. Both are reconstructable from scalars (the server computes *g*·*H⁻¹/²u* from the scalar *g* and shared seed), so this is not a communication-budget violation. But the mismatch could confuse readers about the exact algorithm implemented. A clarifying statement would resolve this.

- **Client scale and participation are limited.** The LLM experiments use only 6 clients with 2 sampled per round, which is a small-scale FL setting. The paper acknowledges this indirectly through its experimental design choices but does not discuss how performance would change at larger scales (e.g., 100+ clients with lower participation rates).

### Trivial
None of note.

## Nice-to-Haves

- A comparison to ZO methods with learned preconditioners *without* the scalar-only constraint (e.g., a FedAvg variant where clients run Hessian-informed ZO locally and communicate full updates) would help isolate the benefit of the Hessian information from the communication-saving mechanism.
- An ablation on Hessian update frequency (e.g., updating every local step vs. once per round) would further validate the design choice.
- Reporting downlink communication cost in addition to uplink would give a more complete picture of total client-side communication.

## Removed Points

These points from the inputs are removed as invalid or not applicable:

- **Harsh critic's claim #2** (server cannot reconstruct per-client Δx from scalars): The server knows the scalar *g*, the shared seed (which determines *u*), and reconstructs *H* locally. So the server can compute Δx = *g*·*H⁻¹/²u* entirely from communicated scalars. No extra communication is needed. The criticism is factually incorrect.
- **Harsh critic's claim that "no justification—theoretical or empirical—that the specific update rule yields this property"** is partially addressed by Figure 5 (right), which shows the long-tail distribution of learned *H* entries consistent with the low-effective-rank assumption, and the paper's honest remarks about the assumption's scope. The claim that "the theory does not explain HiSo's convergence" overstates — the theory explains convergence *under the assumption*, and the paper is transparent about this.
- **Strength Finder's strengths about "robustness to ν" and "empirical evidence supporting low-effective-rank assumption"** are kept in modified form within the review but the more generic/superficial claims are dropped.
- **Harsh critic's point about memory cost** (4–8 GB for billion-parameter models): The paper mentions that the appendix discusses memory cost; this is a standard practical consideration, not a flaw.
- **Harsh critic's point about missing comparison to ZO methods without scalar-only constraint**: demoted to Nice-to-Have as it's beyond the paper's stated scope.

## Novel Insights

The most interesting observation in the review inputs that goes beyond the paper's own contributions is the structural tension flagged by the harsh critic: the paper's theoretical acceleration relies on an assumption (the well-approximated condition) that the algorithm's practical Hessian update has not been shown to satisfy. This is a recurring pattern in optimization theory where practical heuristics (EMA of squared updates, akin to RMSProp) are analyzed under idealized conditions. The paper's honest acknowledgment of this gap is commendable, but it means the theoretical contribution is more "what could be achieved with a good Hessian approximation" than "what HiSo provably achieves." The empirical results, however, do not depend on the theory and stand as evidence that the heuristic works in practice. The paper would be strengthened by directly measuring the whitened trace Tr(*H⁻¹/²*Σ*H⁻¹/²*) for a small model and showing it is indeed ≪ *d*.

## Suggestions

1. Report τ (local update steps) for all LLM experiments and ensure the comparison with DeComFL uses the same τ.
2. Clarify whether the Hessian update uses per-client Δx_{r,τ}^{(i)} or the global aggregated Δx_r, and why.
3. Add a small-scale empirical validation of the well-approximated condition by computing Tr(*H⁻¹/²*Σ*H⁻¹/²*) for a small model and comparing it to *Ld*.
4. Discuss scalability to larger client populations and the memory cost of storing the d-dimensional diagonal Hessian.

## Score and Decision

**Calibration anchors used (all rounds):**

| Anchor ID | Score | Round | Comparison to paper |
|-----------|-------|-------|--------------------|
| gVn0FbzvBk | 3.33 | R1 | Much weaker: FedProx-based paper with no ZO contribution |
| H4okZ5imHB | 3.20 | R1 | Much weaker: Hybrid ZO-FO SFL paper, lower clarity |
| DgSpW6JZSK | 3.00 | R1 | Much weaker: ZO VFL privacy paper |
| xzJrPSlMS4 | 2.00 | R1 | Much weaker: DP optimization paper |
| 6aTbJR95Gu | 4.50 | R1 | Weaker: Parameter-free ZO, single-node, no FL |
| wJ8uT3RJKV | 5.50 | R1+R2 | Comparable: Federated RL paper with similar scope/limitations |
| hB8r4cdFTh | 4.00 | R1 | Weaker: Cross-device FL cohort design, no ZO or Hessian |
| 0KXI6lDM9C | 5.50 | R1+R2 | Comparable: Distributed optimization lower bound, strong theory, weaker experiments |
| yRtgZ1K8hO | 8.00 | R1 | Much stronger: Polar decomposition, different topic, oral |
| **2DuMBKVbX2** | **5.00** | **R2** | **Slightly weaker: Meerkat (ZO sparse FL LLM), HiSo more novel** |
| **9XkmuBR0r1** | **5.50** | **R2** | **Comparable: HyperFedZero, HiSo has stronger theory** |
| **qqoQKCulZt** | **6.00** | **R2** | **Slightly stronger: GH-OFL cleaner contribution** |
| **jMzXLsHdnF** | **5.20** | **R2** | **Slightly weaker: FOCUS (ZO LLM, single-node, not FL)** |
| **ve3EzAvMGe** | **6.00** | **R2** | **Slightly stronger: DeepAFL, cleaner analytic approach** |
| NMvIw1Uwm2 | 6.00 | R3 | Stronger: LMO-based momentum, different topic |

Round 1 bracket: [4.5, 7.0]. Round 2 narrowed to 5.0–6.0 by comparing against the most topically similar anchors. Final score: **5.5** — below GH-OFL (6.00) and DeepAFL (6.00), but above Meerkat (5.00) and FOCUS (5.20), and comparable to the 5.50 anchors (HyperFedZero, Non-Convex FedOpt).

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>