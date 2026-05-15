Now I have all the information needed to produce the final consolidated review.

---

## Summary

WeCAN proposes an end-to-end reinforcement learning framework for heterogeneous DAG scheduling with task-pool compatibility coefficients. The architecture features two key innovations: (1) Weighted Cross-Attention (WeCA) layers that integrate compatibility coefficients as attention biases outside the softmax, enabling adaptive handling of variable numbers of pools and task types; and (2) a Longest Directed Distance GNN (LDDGNN) that encodes DAG structure via learnable biases based on longest directed paths. The paper also provides a theoretical analysis of the optimality gap in list scheduling and introduces a skip-action mechanism within the single-pass setting to close this gap. WeCAN achieves up to 18.1% makespan improvement over the best heuristic on TPC-H while running at heuristic-level speed (0.15s for greedy inference).

## Strengths

- **WeCA architecture is well-designed and well-ablated.** The weighted cross-attention layer places compatibility coefficients outside the softmax, which the paper convincingly argues (and empirically demonstrates in Table 3) better captures overall task compatibility than an inside-softmax variant. The outside placement yields a 3.5 percentage-point higher improvement over Tetris than the inside version on TPC-H-30 (14.0% vs 10.5%). Removing WeCA entirely collapses performance to near-heuristic levels (0.5% improvement), confirming the component is essential.

- **LDDGNN effectively encodes DAG dependencies.** The longest-directed-distance-based attention biases are a well-motivated extension beyond standard GNN message passing. Table 3 shows that replacing LDDGNN with forward GAT or bidirectional GAT degrades makespan by 3-5 percentage points of relative improvement, demonstrating meaningful structural encoding beyond what standard GAT variants provide.

- **Strong and comprehensive empirical results.** Across two distinct benchmarks (TPC-H, a real-world dataset, and Computation Graphs, a synthetic dataset), WeCAN consistently outperforms both strong heuristics (CP, Tetris, HEFT) and neural baselines (PPO-BiHyb, One-Shot). The generalization experiments (Figure 2) show robust performance under environment fluctuations (varying pool count, pool types, task count, task types) with 6.7–20.4% improvement over the best heuristic, substantially exceeding One-Shot's generalization.

- **Single-pass inference achieves practical speed.** WeCAN-Greedy runs in 0.15–1.72s on TPC-H instances, comparable to heuristics (HEFT: 0.18s, Tetris: 0.21s) and orders of magnitude faster than multi-round RL methods (PPO-BiHyb: 20.48s). This combination of solution quality and speed is a genuine practical advantage.

## Weaknesses

### Fatal

None.

### Major

- **Skip action contribution to main benchmark results is unmeasured.** The skip mechanism is presented as a central contribution (closing the optimality gap, "underscoring the importance of skip"). However, the skip action is only ablated on a synthetic "heavy-task" variant (Figure 3) where 1% of tasks are artificially inflated in resource demand and duration. No skip ablation is performed on the standard TPC-H or Computation Graphs benchmarks reported in Tables 1–2. Consequently, it is impossible to determine whether the 18.1% improvement over heuristics on TPC-H derives from the WeCA/LDDGNN architecture, the skip mechanism, or some combination. Given that the abstract and introduction prominently feature the skip contribution, this missing evidence leaves a core claim insufficiently supported.

### Minor

- **Theoretical claims about the skip parameterization are incompletely connected to the implementation.** Theorem 1(iv) asserts the existence of scores (including the 3-parameter skip formula) that yield an optimal solution via greedy selection. The proof is in the appendix and cannot be verified here, but the main text does not provide intuition for why the specific monotonic form \(u_a(1 - k/(2n))^{u_b} + u_c\) is sufficient to represent diverse skip patterns across heterogeneous DAG instances. The theoretical framework in Section 4 (Assumption 1, Theorem 2) establishes that skip actions can make the generation map surjective, which is a clean insight, but the gap between that abstract construction and the implemented 3-parameter formula could be bridged with more explicit discussion. This does not invalidate the contribution but makes the theory-to-practice link harder to assess.

- **PRO-BALM is used as a baseline label in Figure 3 without definition.** The heavy-task ablation figure includes a bar labeled "PRO-BALM" that is never introduced or explained in the paper text, making the results harder to interpret.

- **Heavy-task experiments use a synthetic construction with unclear real-world relevance.** The paper validates the skip mechanism using instances where 1% of tasks are randomly replaced with heavy tasks (inflated resource demand and duration). While this serves as a reasonable stress test for the theoretical claim about the list-scheduling optimality gap, the paper does not establish whether such extreme task distributions arise in the TPC-H or Computation Graphs settings it otherwise evaluates. The paper appropriately scopes this as a validation of the theoretical gap rather than a practical claim, but the leap from this synthetic result to the paper's broader statements about skip importance warrants caution.

### Trivial

- The Figure 3 bar chart has two bars both labeled "WeCAN-S(256)" (one at 8.3% and one at -2.3% on TPC-H-30-heavy), making it unclear which corresponds to the skip-enabled and which to the non-skip variant. The text clarifies but the figure labeling is confusing.

## Nice-to-Haves

- A Gantt chart or trace visualization comparing rollout behavior with and without skip on a concrete TPC-H instance would make the operational effect of skip tangible beyond aggregate numbers.

- Comparing the parametric skip formula against a simpler alternative (e.g., a single learned scalar bias per instance) would test whether the 3-parameter form is necessary or merely incidental.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"The proof is relegated to a stripped appendix" (from Harsh Critic, Issue 1):** The appendix is present in the original submission; its absence here is a parser artifact, not an author error. The paper explicitly states "We provide the details of the proof in Appendix A."

- **"PRO-BALM without definition" treated as a fatal evidential gap (from Harsh Critic, Issue 3):** This is a labeling/presentation issue in Figure 3, not an evidential gap. The text clearly identifies the non-skipping variant comparison; the undefined label is a minor oversight.

- **Harsh Critic's claim that "the abstract promises more than the paper delivers":** The abstract states the method "addresses" and "closes" the optimality gap through skip actions. The paper provides a theoretical framework (Theorem 2, Assumption 1) and synthetic experiments supporting this claim. Whether the evidence is fully sufficient is debatable but the claim is not fabricated.

- **Strength Finder's claim that "Figure 3 directly validates the theoretical gap and the skip action's benefit":** This is partially true for the synthetic setting, but overstated as evidence for the main benchmarks. Retained in weakened form as a minor weakness above.

- **Strength Finder's claim about "skip-score formula prevents degenerate idle behavior while retaining single-pass inference" as a standalone strength:** This is a description of the design, not a validated strength. The formula's effectiveness at preventing degenerate behavior is not independently tested.

## Novel Insights

The paper's theoretical framing of the list-scheduling optimality gap through the lens of surjectivity of the generation map (Assumption 1, Theorem 2) is genuinely novel. The observation that \(S_{\text{list}}\) fails because \(T \circ S_{\text{list}}\) is neither the identity nor surjective, and that adding skip actions can restore surjectivity by enlarging the reduced space, provides a clean conceptual framework for understanding when and why list-scheduling-based methods fall short. This is a useful lens beyond this specific paper.

## Suggestions

- Add a skip ablation on the main TPC-H and Computation Graphs benchmarks (train/evaluate WeCAN with skip probability forced to zero) to isolate the skip mechanism's contribution to the headline results. This is the single most important addition.
- Define PRO-BALM explicitly or remove it from Figure 3; clarify which WeCAN-S(256) bar in Figure 3 corresponds to the skip-enabled vs. non-skip variant.
- Add a paragraph in Section 4 bridging the abstract construction (\(S_n\), Assumption 1) to the specific 3-parameter skip formula, explaining intuitively why this limited parametric family is sufficient.

---

Now, for calibration, here is every anchor returned by the calibration search and how the paper under review compares:

| Anchor | Path | Avg Score | Comparison |
|--------|------|-----------|------------|
| GAA-PtrNet | `/home/wg25r/review_agent/human_reviews_2026/UbWy2QVmke.md` | 4.50 | WeCAN has stronger empirical results, more comprehensive baselines, a theoretical contribution, and better-ablated architectural components. WeCAN is clearly stronger. |
| MACE | `/home/wg25r/review_agent/human_reviews_2026/rnrENwgDsn.md` | 3.50 | WeCAN has broader evaluation (two benchmarks vs. one), larger empirical gains, and a cleaner architecture with better ablations. WeCAN is substantially stronger. |
| ReSched | `/home/wg25r/review_agent/human_reviews_2026/s5pWbwf2tk.md` | 5.00 | Both have well-ablated architectures with strong results and some methodological concerns (ReSched: training data imbalance; WeCAN: missing skip ablation). Comparable quality tier. |
| Smoothness Bounds | `/home/wg25r/review_agent/human_reviews_2026/Zcn4n57lHg.md` | 6.00 | A pure theory paper with tight bounds; different genre. WeCAN is empirical with theoretical elements; the theory is less tight. WeCAN is below this anchor. |
| LaRL | `/home/wg25r/review_agent/human_reviews_2026/Ikjxsa5RHD.md` | 2.50 | Poorly justified LLM integration, unclear contributions. WeCAN is far stronger in both clarity and empirical validation. |
| DEFT | `/home/wg25r/review_agent/human_reviews_2026/yVFOdLjd7V.md` | 5.00 | Mixture-of-experts for cloud workflow scheduling; accepted poster. WeCAN shows larger empirical gains and has a theoretical component. Roughly comparable or slightly stronger. |
| RAISE | `/home/wg25r/review_agent/human_reviews_2026/7gA6ZYii0e.md` | 4.00 | Ensemble-based online RL for DAG scheduling; rejected. WeCAN has cleaner architecture, stronger results, and better ablations. |
| Select and Schedule | `/home/wg25r/review_agent/human_reviews_2026/e1osUquspZ.md` | 3.00 | Hierarchical optimizer for blocking JSSP. WeCAN is substantially stronger in both results and contribution clarity. |

WeCAN sits in the 5.0 band: comparable to ReSched and DEFT (both accepted as posters at 5.0), clearly stronger than GAA-PtrNet (4.50) and MACE (3.50), but below the 6.0 theoretical work. The core architecture is well-validated with strong ablations and results; the primary gap is the unmeasured contribution of the skip mechanism to main benchmarks — a significant but addressable weakness.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>