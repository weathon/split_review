## Summary
WeCAN is an end-to-end reinforcement learning framework for heterogeneous DAG scheduling that addresses task-pool compatibility coefficients. The paper makes three interrelated contributions: (1) a Weighted Cross-Attention (WeCA) layer that incorporates compatibility coefficients directly into the attention mechanism, enabling adaptability to varying environment sizes; (2) a Longest Directed Distance Graph Neural Network (LDDGNN) for encoding DAG dependencies; and (3) a formal analysis of the optimality gap in list-scheduling-based generation maps, with a skip-action mechanism that theoretically closes this gap in the single-pass setting.

---

## Strengths

- **Novel and well-motivated architecture:** Placing compatibility coefficients *outside* the softmax normalization (rather than in log-form inside) is a principled design choice with concrete motivation: it preserves a task's overall compatibility information across the environment. The paper illustrates this with a clean example where the inside placement fails to distinguish between a task compatible with one pool vs. two pools, despite identical task attributes. This distinction is both novel and non-trivial.

- **Formal analysis of the optimality gap:** The paper formalizes a concept that is often acknowledged informally: that list scheduling cannot guarantee optimal solutions. The paper constructs the reduced space *B*, introduces Assumption 1 on generation maps, and proves (Theorem 2) that any map satisfying these conditions can reach optimal solutions. Theorem 1(iii) shows the optimality gap specifically requires skip actions to close—this is a meaningful theoretical result for the neural CO community that goes beyond just reporting empirical gains.

- **Strong empirical results with speed-quality trade-off:** WeCAN-Greedy matches heuristic inference speed while delivering 14–18% improvement over the best heuristic on TPC-H and up to 13.4% on Computation Graphs. WeCAN-S(256) outperforms One-Shot-S(256) substantially with comparable runtime, and both dominate PPO-BiHyb by 2-3× speedup while retaining better makespan. This is a favorable Pareto improvement.

- **Generalization experiments:** Figure 2 shows WeCAN trained in a fixed environment generalizes robustly to more pools, more pool types, more tasks, and more task types—often double the improvement rate of One-Shot under the same environment shifts. This directly validates the adaptability claim and is not merely a restatement of standard test performance.

- **Comprehensive ablation:** Table 3 systematically evaluates WeCA placement (encoder+decoder vs. decoder-only vs. final-only), inside vs. outside normalization, and LDDGNN vs. GAT variants. Each ablation is informative and the degradation is monotone and interpretable.

---

## Weaknesses

### Fatal
None.

### Major

- **Figure 3 (skip ablation) is ambiguous:** The table shows two rows labeled "WeCAN-S(256)" with different values (8.3% vs. −2.3% for TPC-H-30-heavy). One is clearly intended to be "WeCAN-no-skip-S(256)" or similar, but the labeling is not recovered from the alt-text either. This ambiguity is serious because the skip ablation is a core empirical claim. Without knowing which bar corresponds to which variant, it is impossible to assess the magnitude of the skip benefit independently.

- **Monotone skip score is asserted but not tightly analyzed:** The skip score $u_{\pi_{skip}} = u_a(1 - k/2n)^{u_b} + u_c$ is argued to prevent endless idling. However, neither a formal bound on how many skip actions can occur, nor a proof that it prevents idling in the worst case when $u_c > 0$ is large, is given. The claim that this "prevents endless idling" while "remaining the single-pass efficiency" is stated as informal intuition. Since this is presented as a solution to the gap, some tighter analysis—even if deferred to an appendix—is needed.

- **Evaluation scope for skip action is narrow:** The skip benefit is demonstrated only for a dataset with 1% heavy tasks added artificially to TPC-H. The paper claims skip "benefits more when the percentage of heavy tasks increases" but the main experiments in Tables 1–2 do not separate heavy-task vs. non-heavy-task problem instances, making it unclear how much of the overall makespan gain comes from the skip mechanism on standard instances.

### Minor

- **Algorithm 1 framing:** The algorithm is presented as a loop, but the key property—that the neural network is called only *once* (before the loop)—is not made visually prominent. Readers may miss that the loop only executes the generation map, not re-invokes the network.

- **PPO-BiHyb comparison nuance:** PPO-BiHyb uses beam search (a beam-width sampling). When WeCAN-S(256) is compared to PPO-BiHyb, the sample counts and computational budgets are not equalized, which could slightly overstate the efficiency advantage.

### Trivial
- The figure caption for Figure 1 is repeated three times in the parsed text, presumably a parser artifact.

---

## Nice-to-Haves

- An ablation comparing skip-enabled WeCAN vs. non-skip WeCAN on the full TPC-H and Computation Graphs benchmarks (not just the artificial heavy-task variant) would clarify the skip contribution in normal operating regimes.
- A scaling experiment showing how inference time grows with $n$ (number of tasks) would quantify the single-pass claim more concretely.
- Including an example or visualization of when $S_{list}$ fails to reach the optimum (a concrete DAG where no priority ordering in list scheduling yields the optimal schedule) would make Section 4 much more accessible to readers unfamiliar with scheduling theory.

---

## Novel Insights

The paper's most genuinely novel insight is the formal treatment of the optimality gap via the notion of a *generation map*. By showing that $TS_{list}$ is neither the identity nor surjective onto $B_f$, the paper provides a concrete structural reason—not just empirical evidence—for why list-scheduling-based neural schedulers have an intrinsic ceiling. The construction of skip actions as an *enlargement* of the reduced space $B_f$ (rather than a modification of the network) is an elegant abstraction: skip actions lift $S_{list}$ to a surjective map without requiring multi-round inference. The further insight that poor solutions cluster in the high-$u_a$, high-$u_c$ region (making them easier to avoid during training) adds a practical training-stability dimension to what could otherwise be a purely theoretical construction.

---

## Suggestions

- Clarify Figure 3's labeling explicitly: identify which bar is WeCAN with skip and which is without.
- Provide at minimum an informal bound (e.g., maximum number of consecutive skip actions) to support the endless-idling prevention claim.
- Add a comparison showing WeCAN (no-skip) vs. WeCAN (with-skip) on the standard TPC-H/Computation Graphs benchmarks to quantify how much the skip contributes in typical (non-heavy-task) settings.

---

## Score and Decision

WeCAN is a well-executed paper that combines a principled architectural innovation (WeCA), a novel theoretical analysis of list-scheduling's optimality gap, and strong empirical results across diverse benchmarks. The theoretical framing of generation maps and surjectivity is a genuine contribution to the neural combinatorial optimization literature. The ambiguity in Figure 3 and the informal treatment of skip-action bounding are real gaps, but they weaken rather than invalidate the core claims. The paper is suitable for acceptance with these clarifications.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>