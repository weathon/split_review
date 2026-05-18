Now I have all the information needed. Let me synthesize the final review.

## Summary

This paper formalizes Online Continual Graph Learning (OCGL), a framework that bridges Online Continual Learning and Continual Graph Learning by defining node-streaming with bounded per-batch compute/memory constraints and graph topology awareness. It contributes a benchmark of four datasets adapted to the class-incremental streaming setting, evaluates six CL methods (regularization and replay-based) under an online-appropriate hyperparameter selection protocol, and identifies the neighborhood expansion problem in GNNs, proposing neighbor sampling as a bounded-complexity solution. The main empirical finding is that replay-based methods (especially A-GEM) consistently outperform regularization-based approaches.

## Strengths

- **Formal definition of OCGL (Section 3).** The paper provides a clear, self-contained problem statement specifying the evolving graph model, mini-batching constraints, bounded compute/memory requirements, and task-free streaming — filling a gap between the OCL and CGL literatures. This gives the community a grounded framework that prior CGL benchmarks (e.g., Zhang et al., 2022) did not address.

- **Comprehensive benchmarking with fair evaluation (Sections 5–7).** The paper constructs class-incremental node streams from four diverse datasets (CoraFull, Arxiv, Reddit, Amazon Computer), adapts six CL methods to the task-free online setting, and uses the Chaudhry et al. (2018b) hyperparameter selection protocol that respects the online constraint. Tables 1–4 and 5–8 provide the first systematic comparison of multiple CL techniques under the same OCGL protocol, with results averaged over 5 runs.

- **Identification and quantification of the neighborhood expansion problem (Section 3.2, Figure 2).** The paper clearly demonstrates how multi-hop neighborhoods can grow to cover nearly the entire graph (e.g., Reddit's 2-hop neighborhood engulfs most nodes), making standard full-neighborhood GNN training incompatible with online bounded-compute requirements. This is a genuine graph-specific challenge that prior CGL work did not surface in the online context.

- **Neighbor sampling as a practical bounded-complexity strategy (Section 7).** The paper shows that fixed-size neighbor sampling (5–15 neighbors) enables feasible OCGL training across all datasets while preserving meaningful performance for several methods — establishing a simple baseline for future research on efficient OCGL.

- **Insightful stability-plasticity analysis (Figure 1, Section 6).** The per-task accuracy breakdown reveals that regularization methods (e.g., MAS) yield more stable anytime accuracy but fail to acquire new classes, while A-GEM achieves higher overall accuracy with greater variance, giving practitioners actionable guidance.

## Weaknesses

### Major

- **Tension between the OCGL definition and full-neighborhood experiments (Section 6).** The paper defines OCGL with the requirement that "training on each mini-batch [has] bounded compute and memory budgets" (Section 3), yet the full-neighborhood experiments in Section 6 — especially on Reddit (avg degree ~984, batch size 250) — require processing neighborhoods of size comparable to the entire graph per batch. While the paper acknowledges this ("although the neighboring expansion problem ... is present" and uses 1-layer GCN on Reddit as mitigation), the results in Tables 1–4 are presented as main findings without clearly labeling the cost they incur. For Reddit in particular, the 1-hop full neighborhood of a batch-250 already covers most of the graph, which is inconsistent with the bounded-compute framing. The paper would be stronger if the full-neighborhood results were explicitly repositioned as an unconstrained upper bound (e.g., moved to an appendix), with the sampling-based results (Section 7) presented as the primary OCGL-compliant evaluation. As it stands, a reader may over-interpret Tables 1–4 as evidence from the claimed setting.

### Minor

- **Limited differentiation from existing streaming/online graph learning.** The paper correctly notes that existing "streaming" CGL (Wang et al., 2020; Perini et al., 2022) operates on graph snapshots with offline multi-epoch training, not online mini-batches. However, the discussion is brief (one paragraph in Section 2). A more explicit comparison — e.g., showing how OCGL's mini-batch constraint changes the problem compared to per-task subgraph training — would sharpen the claimed novelty. Adding even one simple non-CL streaming baseline (e.g., a GCN trained on each batch independently with sampled neighborhoods, no replay) would help isolate whether the CL strategies themselves drive the observed gains.

- **Memory buffer size for replay methods is not reported.** ER and A-GEM both rely on a memory buffer with reservoir sampling, but the paper never states the buffer capacity used across experiments. Since buffer size is a critical hyperparameter in replay-based CL, this omission makes the results less reproducible and harder to compare against future work.

- **Node ordering within each task is unspecified.** The paper says "we fix an ordering on the nodes of each task" (Section 5) but does not specify what ordering (random? by degree? by timestamp?). Node ordering can affect neighborhood expansion and forgetting patterns, especially for replay-based methods.

- **Only GCN evaluated as backbone.** While GCN is a reasonable choice, including a non-graph baseline (e.g., MLP on node features alone) would isolate how much graph structure matters under the online constraint versus the CL strategy itself.

- **Adaptations of EWC, TWP, and LwF to the task-free online setting are reasonable but unvalidated.** For example, EWC uses a running-average Fisher instead of the original per-task computation. No ablation is provided to confirm these adaptations preserve the intended behavior of the original methods.

### Trivial

- Multiple passes (up to 5) on each mini-batch are used as a tuned hyperparameter. While this is standard practice in the OCL literature (Aljundi et al., 2019) and the paper is transparent about it, it slightly weakens the strict "seen once" claim. Worth an explicit footnote acknowledging the trade-off.

## Nice-to-Haves

- Move the full-neighborhood results (Section 6) to an appendix as an "unconstrained upper bound" and present the sampling results (Section 7) as the main OCGL-compliant experiments. This would resolve the framing inconsistency cleanly.
- Provide wall-time or complexity measurements for the sampling experiments to make the bounded-cost claim empirically verifiable.
- A systematic ablation of buffer size for ER and A-GEM would increase confidence in the replay-based findings.
- A more detailed hyperparameter sensitivity analysis (beyond the brief anecdotal report in Section 6) would strengthen reliability, given that only 20% of tasks are used for validation.

## Removed Points

These points are flagged to be removed; treat them with caution:

1. **"The paper does not engage substantively with streaming GNN literature (Wu et al., 2020; Yao et al., 2020)."** — The paper explicitly discusses existing "streaming" CGL works (Wang et al., 2020; Perini et al., 2022) and explains why they are offline, not online (Section 2, final paragraph). The specific references Wu et al., 2020 and Yao et al., 2020 are not cited in the paper, so their relevance cannot be verified from the paper itself. The weaker version of this critique (insufficient differentiation) is kept in Minor.

2. **"The results in Tables 1–4 are essentially offline-in-disguise numbers."** — Overstated. For CoraFull (avg degree ~4) and Amazon Computer (avg degree ~8), full 2-hop neighborhoods are bounded and manageable. The issue primarily affects Reddit, and the paper acknowledges this by using 1-layer GCN and flagging the neighborhood expansion problem. The weaker version is kept in Major.

## Novel Insights

Beyond the paper's own contributions, an interesting observation emerges from cross-referencing the harsh critic's and strength finder's analyses: both agree that the paper's main value is as a benchmark/framework contribution rather than a methodological advance. The harsh critic's primary complaint (the Section 6 vs. Section 7 framing tension) actually reinforces this — the benchmark is most useful when its constraints are well-defined, and the paper's own presentation undermines that clarity. The strength finder's emphasis on the neighborhood expansion analysis (Section 3.2) stands out as the most novel technical insight; by contrast, the benchmarking itself is a valuable but straightforward engineering contribution. This suggests the paper's strongest lasting impact may be the OCGL problem formalization and the neighborhood expansion warning, rather than any specific method result.

## Suggestions

1. Restructure the experimental presentation: move Tables 1–4 to an appendix labeled "unconstrained full-neighborhood upper bound," make Tables 5–8 the primary results, and clarify in Section 1 that Section 6 serves to demonstrate why sampling is necessary rather than to establish OCGL baselines.
2. Report the memory buffer size used for ER and A-GEM, and the node ordering strategy within each task.
3. Add a simple non-CL streaming baseline (e.g., GCN on current batch only, with sampled neighborhoods, no replay) to establish a lower bound and clarify whether CL methods provide benefits beyond having more data through replay.

## Score and Decision

The paper makes a genuine contribution by formalizing OCGL and providing a first systematic benchmark. The main structural flaw (inconsistency between the OCGL definition and Section 6 experiments) is acknowledged by the authors but not fully resolved in the current presentation, which weakens the narrative coherence. The novelty is moderate — the core contribution is the problem formalization and benchmark, not new algorithms. The experiments are thorough within their scope, and the neighborhood expansion analysis is useful. Overall, the paper is on the borderline: it has clear value for the community but would be significantly strengthened by restructuring the experimental framing as suggested.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>