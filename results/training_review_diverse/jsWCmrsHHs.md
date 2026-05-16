Now I have a thorough understanding of the paper and all the reviewer claims. Let me produce the final consolidated review.

## Summary

This paper proposes a DRL-guided improvement heuristic for the Job-shop Scheduling Problem (JSSP). The key technical contributions are: (1) a two-module GNN architecture — TPM (GIN-based) for capturing topological differences between disjunctive graphs and CAM (GAT-based) for encoding heterogeneous neighbor contexts (precedence vs. machine-sequence); (2) a learned policy that directly selects operation pairs from the N₅ neighborhood, avoiding the costly full-neighborhood evaluation required by traditional improvement heuristics; and (3) a message-passing evaluator that computes schedules in batch on GPU. Experiments on seven classic benchmarks show large optimality-gap reductions compared to prior DRL-based construction heuristics and hand-crafted improvement rules, and the method generalizes to extremely large instances (up to 1000×40) where it outperforms CP-SAT.

## Strengths

1. **Novel GNN representation for complete JSSP solutions.** The dual-module design (TPM using GIN for graph-isomorphism discrimination, CAM using GAT for heterogeneous neighbor contexts) is well-motivated by the structure of disjunctive graphs in the improvement setting. The paper validates through ablation (Figure 6) that the combination converges to a better reward than either module alone, supporting the design choice.

2. **Strong and consistent empirical performance.** The results in Table 1 are substantive and reproducible from the paper's data. Ours-5000 achieves gaps of 6.2% (Taillard 15×15), 8.3% (20×15), and 9.0% (20×20), while the best DRL baseline (ScheduleNet) achieves 15.3%, 19.4%, and 17.2% respectively. The method also beats CP-SAT on Taillard 100×20 (3.0% vs. 3.9%) — a notable result. These improvements are consistent across nearly all 7 benchmark families and all problem sizes.

3. **Efficient move selection.** The learned policy directly outputs an operation pair, avoiding the full neighborhood evaluation that makes traditional improvement heuristics computationally expensive. The runtime data confirm this: Ours-500 on Taillard 15×15 takes 9.3s vs. 48.2s for GD-500, while achieving a better gap. This is a genuine practical advantage.

4. **Generalization to larger scales.** The policy trained with 500 steps continues to improve when run for 5000 steps (Table 1, lower rows), and generalizes zero-shot to extremely large instances (200×40, 500×60, 1000×40) where it outperforms CP-SAT by large margins (Table 5). This demonstrates that the learned heuristic captures reusable structure rather than overfitting to training sizes.

5. **Message-passing evaluator for batch computation.** The proposed GPU-compatible alternative to CPM is a practical engineering contribution that enables efficient batch training and inference, though its standalone benefit is not separately benchmarked.

## Weaknesses

### Fatal
None.

### Major

- **The claim of linear computational complexity is unsubstantiated for the action-selection step.** Theorem 1 states linear time complexity w.r.t. |𝒥| and |ℳ|. However, the action-selection mechanism (Section 4.2.2) computes a pairwise score matrix SC = h' h'ᵀ, where h' is |𝒪|×q and |𝒪| = |𝒥|·|ℳ| + 2. This matrix multiplication is O(|𝒪|²·q) = O(|𝒥|²·|ℳ|²), which is **quadratic** in the product of the problem dimensions, not linear. The paper does not discuss exploiting sparsity (the feasible action space is at most 2N(s)−2 ≪ |𝒪|²). The practical runtime in Table 1 grows sub-quadratically, which suggests the linear claim may hold in practice due to constant factors, but the theoretical claim as stated is incorrect. This needs either a corrected complexity analysis, a sparse action-scoring mechanism, or a restriction of the linearity claim to the embedding phase only.

### Minor

- **The training procedure is underspecified.** Section 4.3 (the n-step REINFORCE algorithm) contains only a single sentence. Critical details — number of training instances per size, batch size, learning rate schedule, number of episodes/steps, discount factor (if any), baseline for variance reduction, entropy bonus (if any), and the value of "n" in n-step — are absent from the extracted paper. While some of these may have appeared in a stripped "Model and configuration" subsection (line 216–217 is clearly a parser artifact), the REINFORCE section itself is genuinely sparse. This hinders reproducibility.

- **The ablation study is too narrow to fully support the two-module design.** The ablation (Section 5.5) shows training curves only on 10×10 instances. No test-set performance (gaps on benchmarks) is reported for the ablated variants (TPM-only, CAM-only), and no analysis is provided for how the two-module design behaves across different problem sizes. While the training curves support the combination's benefit, the evidence is preliminary.

- **The initial solution generation is unspecified.** The paper states "basic dispatching rules" (line 66) without naming which rule(s) are used (e.g., Most Work Remaining, Shortest Processing Time, or a specific composite rule). Since the initial solution quality affects the improvement process, this should be specified for reproducibility.

- **No statistical variance is reported.** Table 1 reports only point estimates (average gaps). Given the stochastic nature of both the policy and the training, reporting standard deviations or confidence intervals across multiple runs/r trials would strengthen confidence in the results.

### Trivial
None.

## Nice-to-Haves

- The tabu search comparison (Section 5.4) references Tables 3 and 4 which are not present in the extracted text (parser artifact). The paper should ensure these are accessible and include a clear description of the tabu search setup (tabu tenure, aspiration criteria, iterations).
- An analysis comparing the standalone benefit of the message-passing evaluator vs. CPM (e.g., speedup on batch vs. single-instance) would help contextualize this contribution.
- Expanding the ablation study to include test-set performance on a range of benchmark sizes would more convincingly demonstrate the necessity of the two-module design.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Comparison to DRL construction methods is fundamentally unfair."** The paper compares against the best available DRL methods for JSSP, which happen to be construction heuristics. This is a valid comparison of two paradigms. Crucially, the paper *also* includes fair comparisons against hand-crafted improvement heuristics (GD, FI, BI) with the same initial solutions and same step budgets, which directly supports the central claim about *learned* improvement policies. The critic's framing ignores these baselines.

- **"Tables 3, 4 are missing."** These table references in Section 5.4 are parser artifacts — the tables exist in the original submission. Per the review rules, parser-stripped content is not a valid weakness.

- **"Hardware details missing."** Hardware/software details were likely in the stripped "Model and configuration" subsection (line 216). Additionally, this is a standard detail easily provided and not a structural flaw.

- **Various formatting, style, and missing-appendix criticisms.** All are either parser artifacts or matters of taste that do not affect the paper's scientific contribution.

## Novel Insights

The reviews surface an interesting tension: the action-selection mechanism computes a full |𝒪|×|𝒪| score matrix, which is theoretically quadratic, yet the empirical runtime scales sub-quadratically. This suggests that either the matrix multiplication is dominated by other linear-time components in practice, or constant-factor GPU parallelism masks the asymptotic behavior at the tested scales. Understanding this gap between the stated theoretical complexity and the practical implementation would be valuable — either the paper should correct its theoretical claim or the community should recognize that the quadratic step is empirically negligible for problem sizes up to 1000×40. This is a genuine methodological ambiguity worth resolving.

## Suggestions

1. **Clarify or correct the complexity claim.** Either (a) provide a sparse action-scoring mechanism that achieves true linear complexity, or (b) explicitly note that the action-selection step is O(|𝒪|²) and explain why it is dominated by the linear embedding step in practice, or (c) restrict the linearity claim to the GNN embedding phase and characterize the full pipeline's complexity honestly.

2. **Expand Section 4.3 with full training details.** Specify the REINFORCE variant (baseline, discounting, n-step value), learning rate, batch size, training instances (number per size), episode horizon, and any entropy bonus or regularization. This is essential for reproducibility.

3. **Report statistical variance.** Add standard deviations or confidence intervals to Table 1's results. Also specify the number of random seeds/runs used.

4. **Strengthen the ablation study.** Report test-set performance (gaps on benchmarks) for TPM-only and CAM-only variants across multiple problem sizes, not just training curves on 10×10.

5. **Specify the initial dispatching rule(s) used.**

## Score and Decision

This paper makes a solid contribution — a novel GNN architecture purpose-built for encoding complete JSSP solutions in an improvement setting, a learning-based policy that avoids costly full-neighborhood evaluation, and strong empirical results across seven benchmarks. The weaknesses are real but addressable: the complexity claim needs correction, the training details need expansion, and the ablation needs deepening. None of these are fatal — the core claims (the architecture works, performance beats baselines) are well-supported by the data. With the revisions suggested above, this would be a strong paper.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>