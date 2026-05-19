- Decision: Accept
- Avg Score: 7.50
- Scores: 6, 8, 8, 8
Now I have a thorough understanding of the paper and both reviews. Let me produce the consolidated review.

## Summary

This paper proposes a DRL-based *improvement* heuristic for job shop scheduling, which differs from prior DRL work that focuses on *construction* heuristics. The method encodes complete solutions as disjunctive graphs, learns a GNN-based policy (TPM+CAM modules) to select local moves from the N₅ neighborhood, and uses a message-passing evaluator for batch GPU computation. Results on seven classic benchmarks show large improvements over prior DRL methods and competitive performance with CP-SAT and tabu search, including impressive zero-shot generalization to very large instances (up to 1000×40).

## Strengths

- **Novel dual-module GNN representation for improvement heuristics.** The paper proposes TPM (topological, using GIN) and CAM (context-aware, using GAT on separate job/machine subgraphs) to jointly capture structural differences and heterogeneous neighbor types in disjunctive graphs. The ablation study (Section 4.6, Figures 6:sub2/6:sub3) confirms that the combined model outperforms either module alone, providing clear evidence that the design is more expressive than prior single-module approaches (L2D, RL-GNN, ScheduleNet).

- **Strong empirical results on classic benchmarks, often by a large margin.** In Table 1, Ours-5000 achieves the best (or tied best) gap on 10 out of 15 benchmark groups, outperforming all DRL baselines (e.g., on Taillard 15×15: 6.2% vs. ScheduleNet 15.3%) and hand-crafted rules (GD, FI, BI). On Taillard 100×20, Ours-5000 (3.0% gap) is the only method to surpass CP-SAT (3.9%). The runtime is also competitive — Ours-5000 on 100×20 runs in 8.4 minutes vs. 1 hour for CP-SAT.

- **Impressive zero-shot generalization to extremely large instances.** Table 5 shows that a model trained on 20×15 achieves negative gaps (outperforming CP-SAT) on 200×40 (−24.31%), 500×60 (−20.56%), and 1000×40 (−15.99%) with only 500 improvement steps. This demonstrates size-agnostic generalization far beyond the training distribution, which is notable for a learned scheduler.

- **Message-passing evaluator for batched GPU computation.** Section 3.4 introduces a novel message-passing variant of CPM that can evaluate multiple solutions simultaneously on GPU (Theorem 2 proves equivalence). This is a practical contribution for improving training efficiency and could be useful beyond this specific method.

- **MDP formulation tailored to improvement heuristics.** The state representation uses the complete disjunctive graph (avoiding the partial-solution representation issues of construction methods), actions are operation pairs from N₅, and the reward function directly rewards incumbent improvement. This enables the policy to learn longer-sighted search behavior that can escape cycling (demonstrated in Section 4.3, where greedy rules stall after 500 steps while the learned policy continues improving).

## Weaknesses

### Fatal
None.

### Major

- **The linear complexity claim (abstract, Theorem 1) is inconsistent with the described action-selection mechanism.** The action selection procedure (Section 3.2.2) explicitly computes `h' × h'^T` — a matrix of dimension `|O| × |O|` where `|O| = |J|×|M| + 2`. This is an O(|J|²|M|²) operation. The abstract states "We prove that the computational complexity of our method scales linearly with problem size," and Theorem 1 claims the policy network has "linear time complexity w.r.t both |J| and |M|." The paper does not explain how the quadratic matrix multiplication is reconciled with this claim. While a proof may appear in the appendix (which was stripped by the parser), the main-text description of the algorithm contradicts the headline claim as written. This is not fatal to the contribution — the practical runtimes are clearly competitive — but it misrepresents a core advertised property and must be corrected. The authors should either (a) revise the action selection to only compute scores for the O(|M|) feasible pairs (which would restore linear complexity), (b) provide the proof that reconciles the computation, or (c) remove the linearity claim and accurately state the empirical complexity.

- **No statistical significance or variance reported for any experimental result.** Table 1 reports single-point gap values for all methods on all benchmarks. There is no mention of multiple runs, random seeds, confidence intervals, or standard deviations. Section 4.6 states "we can confirm that our method is fairly reliable and stable for various problem sizes and different random seeds" but provides no supporting numerical data. For a stochastic policy trained with REINFORCE, variance matters; without it, the reader cannot assess whether observed improvements are robust. This is a standard expectation for empirical ML papers and should be addressed for at least a representative subset of results.

### Minor

- **The batch-processing advantage of the message-passing evaluator is claimed but not demonstrated.** The paper introduces the evaluator as a way to "evaluate multiple solutions simultaneously" (Section 3.4, abstract), and the message-passing formulation is a nice theoretical contribution. However, the main experiments run single instances without batching (Section 4.1 states results are "without batching"). There is no wall-clock comparison of sequential vs. batched evaluation. Demonstrating this would strengthen a claimed practical benefit.

- **The initial solution generation method is underspecified.** The paper states "The initial solution is generated by basic dispatching rules" (Section 3) and that hand-crafted rules start from "the same initial solutions as ours" (Section 4.1), but does not specify which dispatching rules are used (e.g., SPT, EDD, MWKR). This affects reproducibility and the fairness of the comparison with hand-crafted rules (since those rules are sensitive to the starting solution). The authors should specify the rule(s) used.

- **No runtime breakdown between policy inference, graph embedding, and evaluation.** The paper reports total solve times but does not decompose them. A breakdown would help the community understand where the computational savings come from and which component dominates, particularly for scaling to larger instances.

### Trivial
None.

## Nice-to-Haves

- A brief discussion of why N₅ was chosen over other neighborhood structures (e.g., N₄, N₆) and whether the method could generalize to other neighborhoods.
- A more detailed analysis of the CP-SAT comparison: how CP-SAT was configured (default settings?), whether its 1-hour limit was always reached, and whether the observed gaps on large instances are typical for CP-SAT at those sizes.
- Ablation results for the number of GNN layers K and embedding dimensions p, q to justify the chosen values.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Tabu search comparison tables are missing."** Tables 3 and 4 are referenced in the text (Section 4.5) but not present in the extracted file. The parser strips appendices and some table environments; these tables exist in the original submission. Per the hard rules, this criticism should not be held against the paper.
- **"Missing hyperparameters (learning rate, batch size, etc.)."** The "Model and configuration" section appears truncated in the extraction (`\textbf{Model and configuration.}}`), and hyperparameter details are likely in the full version or appendix. Per the hard rules, nitpicks about implementation details not present due to parser stripping are removed.
- **"Missing related work."** As the reviewer has no external sources to confirm the existence of missing citations, this is excluded per the hard rules.
- **Strength: "Linear-time policy network with a formal complexity proof."** This strength conflicts with a verified major weakness (the action selection is quadratic as described in the main text). Per the soft rule that "when a strength and weakness disagree, the weakness wins," this strength is dropped.
- **"Reward is sparse."** This is noted by the harsh critic as an observation, not a weakness. The sparsity is intentional and aligned with the goal of maximizing final improvement.

## Novel Insights

The harsh critic correctly identifies the tension between the claimed linear complexity and the described quadratic action selection — this is the single most substantive finding from the reviews, as it goes to a core advertised property of the method. Beyond this, the reviews surface the expected concerns about variance reporting that apply to most empirical DRL papers. A more subtle observation is that the paper's strongest evidence (zero-shot generalization to 1000×40 instances outperforming CP-SAT by 15–24%) is remarkably compelling but also raises a question the paper does not fully address: why does a policy trained on 20×15 transfer so effectively to 1000×40? The answer is likely the GNN's size-agnostic property plus the N₅ neighborhood's structure, but the paper does not analyze the mechanism behind this generalization. None of these observations are fully novel beyond what the paper and reviews surface collectively.

## Suggestions

1. **Resolve the complexity claim.** Either modify the action selection to compute scores only for the O(|M|) feasible pairs (which would restore linear complexity), or revise the claim to be empirically qualified (e.g., "near-linear in practice given sparsity" or "linear in the GNN embedding step"). This is the most critical fix.

2. **Add variance reporting.** Report standard deviations or interquartile ranges for at least the Ours-* methods on a representative subset of benchmarks (e.g., Taillard 15×15, 30×20, 50×20, 100×20) across 3–5 random seeds. This directly addresses the reliability concern.

3. **Specify the initial dispatching rule(s)** used to generate starting solutions.

4. **Include a runtime breakdown** for at least one large instance size to clarify where computational time is spent.

5. **Demonstrate the batch-processing advantage** of the message-passing evaluator with a wall-clock comparison (sequential vs. batched evaluation of N solutions).
