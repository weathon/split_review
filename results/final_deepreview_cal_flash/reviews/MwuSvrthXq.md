Now I have enough anchors. Let me compile the final review.

**Round 1 bracket**: The paper sits between approximately 5.0 and 7.0. It is clearly stronger than the DRL-PP (4.50) and quantum scheduling (5.00) anchors — those had more severe evaluation gaps and fairness concerns. It is less strong than the JSSP DRL (7.50) paper, which had comprehensive evaluation and clean ablations. The fair scheduling paper (6.80) is in a different sub-area (online non-clairvoyant scheduling with competitive analysis) but comparable in overall quality.

**Round 2 narrowing**: The SSCO HRL (6.00) anchor is the closest comparator — both papers propose novel RL architectures for CO problems, have real contributions but also evaluation gaps (the SSCO paper had weak baselines; this paper has missing heterogeneous SOTA comparisons). The paper under review is slightly stronger because its ablation study is more thorough and it provides theoretical analysis, but the evaluation gaps are real. I place this paper at **6.0**.

Now let me write the full review.

Let me check the greedy vs sampling modes:
- WeCAN-Greedy: deterministic, selects highest probability action
- WeCAN-S(n): generates n samples, picks best

The paper says "For each of 10 test problems, we generate 256 samples, computing mean makespan and relative improvement to the best heuristic (Tetris)" for ablation study.

Let me also check if there's any mention of skip ablation on standard benchmarks in the ablation study - Table 3. Looking at Table 3: "WeCA + LDDGNN", "WeCA-inside + LDDGNN", "WeCA-decoder+ LDDGNN", "WeCA-decoder-inside+ LDDGNN", "WeCA-final-only + LDDGNN", "WeCA + GAT(forward)", "WeCA + GAT(bi-direction)". None of these test a "without skip" variant. So the skip is not ablated on standard benchmarks.

Figure 3 does test on heavy-task datasets but with a different setup (HEFT as baseline, not Tetris). The figure shows "WeCAN-S(256)" (which presumably uses skip) vs "WeCAN-inside-S(256)" (which uses inside placement but also presumably uses skip) vs "PRO-BALM" (some method) vs "WeCAN-S(256)" (green - this might be the no-skip variant, but the label says WeCAN-S(256)). Actually looking at the data table: the bar labeled "WeCAN-S(256)" in green shows -2.3% for TPC-H-30-heavy and 0.0% for TPC-H-50-heavy. This is much worse than the blue "WeCAN-S(256)" at 8.3% and 8.9%. So the green one is likely the one WITHOUT skip but the label is wrong (both called WeCAN-S(256)). So the figure DOES compare with a no-skip variant, confirming the skip helps for heavy tasks. But this is only on the heavy-task dataset, not the standard benchmarks.

So the reviewer is correct: skip ablation is only on heavy tasks, not standard benchmarks.

Now let me write the final review.## Summary

This paper proposes WeCAN, an end-to-end RL framework for heterogeneous DAG scheduling with task-pool compatibility. The framework combines (1) a weighted cross-attention (WeCA) encoder that integrates compatibility coefficients as an external multiplicative bias (outside softmax), allowing flexible adaptation to varying numbers of pools and task types; (2) a longest directed distance GNN (LDDGNN) for encoding DAG dependencies; and (3) a single-pass decoder with a learned skip action that theoretically closes the optimality gap of list scheduling. Empirical results on TPC-H and Computation Graphs datasets show consistent makespan improvements over heuristic baselines (HEFT, Tetris, CP) and two neural baselines (PPO-BiHyb, One-Shot), while maintaining inference speed comparable to heuristics.

## Strengths

1. **Weighted cross-attention with external compatibility bias.** Placing the compatibility coefficient as a multiplicative factor *outside* the softmax (rather than as a log-bias inside) is a clean architectural design that lets the network distinguish tasks that have identical attributes but different compatibility profiles across pools. The ablation study (Table 3) confirms that the outside placement outperforms the inside version by 3.5–1.9 percentage points.

2. **Theoretical analysis of the list-scheduling optimality gap and a constructive fix via skip actions.** The paper proves (Theorem 1) that list scheduling's generation map is not surjective onto the optimal solution, identifies the formal condition for surjectivity (Assumption 1), and shows that augmenting with a skip action in the single-pass setting satisfies this condition (Theorem 2). This is a principled justification for what could otherwise be a heuristic trick.

3. **Consistent empirical performance across diverse datasets with fast inference.** WeCAN-S(256) outperforms all baselines on all six test instances (TPC-H-30/50/100 and three Computation Graph types), with improvements of up to 18.1% over the best heuristic and 9.5% over the best neural baseline. WeCAN-Greedy runs in 0.15–1.72s, comparable to heuristics and *two orders of magnitude faster* than PPO-BiHyb (20–179s). This speed–quality trade-off is the paper's strongest practical claim.

4. **Generalization robustness.** Figure 2 shows that WeCAN maintains its performance advantage over One-Shot under four types of environment perturbation (more pools, more pool types, more tasks, more task types) without retraining, validating that the architecture's flexibility translates to practical robustness.

## Weaknesses

### Fatal
None.

### Major

1. **Missing comparison with dedicated heterogeneous scheduling methods.** The related work section cites several RL methods specifically designed for heterogeneous DAG scheduling (e.g., READYS [Grinsztajn et al., 2021], Zhou et al. 2022, Zhadan et al. 2023, Wang et al. 2025). Yet the experimental evaluation includes none of them as baselines. The paper compares only with PPO-BiHyb and One-Shot (both originally designed for homogeneous or simplified settings) plus classical heuristics. Without a direct comparison against these dedicated heterogeneous schedulers, the claim of "outperforming state-of-the-art methods" in the heterogeneous setting is insufficiently supported. This gap weakens the central empirical claim of the paper.

2. **Skip action is not ablated on the standard benchmarks.** The skip action is presented as a core innovation that closes the optimality gap of list scheduling. However, all standard benchmark results (Tables 1 and 2) are reported using the full WeCAN pipeline that includes skip actions. The only ablation isolating the skip mechanism appears on the heavy-task variant (Figure 3). On the standard TPC-H and Computation Graphs datasets, the reader cannot determine how much of the observed improvement comes from the skip action versus from the WeCA and LDDGNN encoding components. A "WeCAN without skip" row in Tables 1 and 2 would resolve this.

### Minor

1. **Unclear adaptation of One-Shot to the heterogeneous setting.** The paper states that One-Shot "does not consider compatibility coefficients or pool allocation" (Section 1, related work). The baselines description (Section 5.1) lists One-Shot as a baseline without describing how it was adapted to handle compatibility coefficients, pool allocation, and resource constraints. If the authors implemented adaptations themselves, the resulting version may not be a fair representative of the original method. A brief description of the adaptation would improve the evaluation's credibility.

2. **Unsubstantiated claim about variance reduction through clustering.** Section 4.2 asserts that the skip-action design "clusters most poor solutions in the high-\(u_a\), high-\(u_c\) region, ... [reducing] variance." No empirical evidence (histograms of learned skip parameters, variance comparison with a non-skip variant, or learning curves) is provided. This claim is used to argue that the method does not suffer from increased variance, but it remains speculation without supporting analysis.

3. **Figure 3 labeling error.** The figure description lists two bars both labeled "WeCAN-S(256)" in different colors (blue and green). The green bar likely corresponds to a no-skip variant, but the label does not distinguish it. This makes the figure difficult to interpret correctly.

4. **No discussion of limitations.** The conclusion does not discuss limitations: scalability of the pairwise-attention LDDGNN to graphs with thousands of nodes, sensitivity to the REINFORCE baseline choice, or problem instances where the skip action might not help.

### Trivial
None.

## Removed Points

- **Missing proofs / appendix content**: Several criticisms concern proofs deferred to the appendix, which is standard practice. The parser strips the appendix; this is not an author error. **Removed.**
- **Missing hyperparameters and training details**: The harsh critic notes these are "presumably in the appendix." Since the appendix is stripped by the parser, this is not a verifiable weakness. **Removed.**
- **Scope-creep demands** (e.g., adding a larger dataset when current size is sufficient): These are not substantive weaknesses. **Removed.**
- **Generic nitpicks about presentation**: Complaints about Section 3.1 justification being "slightly overstated" are subjective and the paper provides empirical evidence (Table 3) supporting the design choice. **Removed.**

## Nice-to-Haves

- A direct ablation of the skip action on the standard benchmarks (Tables 1 and 2) would substantially strengthen the paper's core claim about skip actions.
- An analysis of the learned skip parameters (e.g., a scatter plot of \(u_a, u_c\) values from trained models) would support the variance-clustering claim in Section 4.2.
- A brief paragraph describing how One-Shot was adapted to the heterogeneous setting would improve experimental transparency.
- A scalability discussion (e.g., runtime breakdown or complexity analysis of LDDGNN's pairwise attention) would help practitioners understand the method's limitations.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface any insight about the method that the paper itself does not already articulate.

## Suggestions

1. **Add at least one dedicated heterogeneous scheduling baseline** (e.g., READYS or a recent variant from the cited works) to the main experiments, or provide a clear justification for why comparison is infeasible (e.g., code not available, different problem formulation).
2. **Add a "WeCAN w/o skip" variant to the standard benchmark tables** (Tables 1 and 2) so readers can directly assess the contribution of the skip action separately from the encoding components.
3. **Fix the Figure 3 labeling** so the two "WeCAN-S(256)" bars are distinguished (e.g., "WeCAN-S(256)" vs. "WeCAN-S(256) no skip").
4. **Add a brief empirical analysis** (e.g., histogram or scatter plot of learned \(u_a, u_c\)) to support the variance-clustering claim, or qualify the claim as speculative.
5. **Describe how One-Shot was adapted** to the heterogeneous environment (compatibility coefficients, pool allocation) in the experimental setup.
6. **Add a limitations paragraph** to the conclusion discussing scalability and potential failure cases.

## Score and Decision

**Calibration anchors used:**

| Path | Avg Score | Round | Comparison |
|---|---|---|---|
| bntJK4NyIW | 2.00 | R1 | Unrelated topic (decentralized training); this paper is far stronger |
| ArJikvI6xo | 3.40 | R1 | Federated learning heterogeneity; this paper is considerably stronger |
| 10eQ4Cfh8p | 3.00 | R1 | FJSP optimization; this paper is stronger |
| b9aCXHhdbv | 4.50 | R1 | Pipeline parallelism DRL; this paper has stronger evaluation and theory |
| 8WtBrv2k2b | 5.00 | R1/R2 | Quantum resource scheduling RL; comparable quality but this paper has broader evaluation |
| CJEBFNBLhO | 4.25 | R1/R2 | Massively parallel CO environments; this paper has more novel architecture |
| jBYQAtzp5Z | 6.80 | R1/R2 | Fair scheduling with predictions; this paper is slightly weaker due to evaluation gaps |
| CFLEIeX7iK | 5.75 | R2 | Neural solver selection; this paper has stronger architecture contributions |
| WszeEzjcq2 | 5.33 | R2 | NAR GNNs for CO; this paper has more complete empirical evaluation |
| jsWCmrsHHs | 7.50 | R2/R3 | DRL for JSSP; this paper is clearly weaker — JSSP paper has comprehensive baselines and clean ablations |
| AloCXPpq54 | 6.00 | R2 | SSCO with HRL; comparable quality — both have a novel architecture with notable but addressable evaluation gaps |

**Round 1 bracket**: 5.0–7.0. The paper is clearly above the 4–5 anchors (b9aCXHhdbv, 8WtBrv2k2b) due to stronger architecture novelty, theory, and evaluation breadth. It is below the 7.5 anchor (jsWCmrsHHs) which had comprehensive baselines, clean ablations, and a linear-complexity proof. **Round 2 narrowing**: Comparison with the SSCO HRL anchor (6.00) — both propose novel RL architectures for CO with real contributions but evaluation gaps; this paper has stronger ablation analysis and theory but the missing heterogeneous SOTA comparison is a real gap. The fair scheduling anchor (6.80) is in a different sub-area but at a comparable rigor level; this paper is slightly weaker due to the two major gaps identified above.

**Final score**: 6.0. The contributions (WeCA design, theoretical optimality-gap analysis, efficient single-pass skip) are genuine and the empirical performance is strong across multiple datasets. However, the missing comparison with dedicated heterogeneous scheduling baselines and the missing skip-action ablation on standard benchmarks are substantive gaps that prevent the paper from being a clean accept at the strongest venues.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>