Now I have thoroughly analyzed the paper against all reviewer claims. Let me produce the consolidated review.

---

## Summary

This paper proposes a DRL-guided **improvement** heuristic for Job Shop Scheduling (JSSP), departing from the prevalent construction-heuristic paradigm. It introduces a dual-module GNN policy network (TPM for topology, CAM for node-type context) that directly selects local moves (operation swaps in the N5 neighborhood) without evaluating the full neighborhood. A message-passing evaluator reformulates the Critical Path Method (CPM) as a batched GPU-compatible computation. Experiments on seven classic benchmarks show strong performance against prior DRL-based methods, hand-crafted improvement rules, and CP-SAT, with notable generalization to much larger instances.

## Strengths

- **Novel dual-module GNN architecture (TPM + CAM) for JSSP improvement heuristics.** The paper is the first to combine a GIN-based topological module with a GAT-based context-aware module for disjunctive graphs in an improvement setting. The ablation study (Figure 6) confirms that the combination converges faster and achieves lower makespan than either module alone, validating the design.

- **Consistent and substantial improvements over prior DRL-based methods on seven classic benchmarks.** Across all benchmark collections (Taillard, ABZ, FT, LA, SWV, ORB, YN), Ours-500 achieves significantly lower gaps than L2D, RL-GNN, and ScheduleNet (e.g., 9.3% vs 15.3% on Taillard 15×15; 2.1% vs 12.1% on LA 10×5 in Table 1). The advantage persists or grows with more steps (Ours-5000), and the method is also faster or competitive in runtime.

- **Generalization to larger horizons and unseen instance sizes.** The learned policy trained for 500 steps continues to improve when run for 5000 steps (e.g., 9.3% → 6.2% on Taillard 15×15), whereas hand-crafted rules stagnate due to cycling. More strikingly, a model trained on 20×15 instances generalizes zero-shot to 200×40, 500×60, and 1000×40 instances and outperforms CP-SAT with 1h time limits (Table 5), demonstrating size-agnostic representation learning.

- **Practical message-passing evaluator for batched makespan computation.** The reformulation of CPM as a GPU-compatible message-passing operation (Theorem 2) enables simultaneous evaluation of multiple solutions, addressing a real bottleneck in improvement heuristics. The method's wall-clock times in Table 1 (e.g., 9.3s vs GD-500's 48.2s on 15×15) confirm the practical benefit, even without a direct CPM-vs-MP ablation.

## Weaknesses

### Fatal
None. The paper's core claims — that a learned improvement policy outperforms construction heuristics and hand-crafted rules — are supported by the empirical evidence. The issues below are serious but fixable and do not invalidate the central contribution.

### Major

1. **The claimed linear complexity (Theorem 1) is inconsistent with the action-selection mechanism.** The paper asserts that the policy network has linear time complexity w.r.t. both |𝒥| and |ℳ|. However, the action selection (Section 4.2.2) computes a full |𝒪|×|𝒪| score matrix *SC* = h'·h'^T (where |𝒪| = |𝒥|×|ℳ| + 2), which is O(N²·q) — quadratic, not linear — before masking to feasible pairs. For the 1000×40 instance (N=40,000), this would involve billions of scalar operations per step. No proof, informal argument, or empirical complexity breakdown is provided to reconcile this discrepancy. This is not a nitpick: the linearity claim appears in the abstract, introduction, and a dedicated theorem, making it a central advertised property. **Either the action selection must be changed to avoid the quadratic bottleneck, or the complexity claim must be corrected and the empirical wall-clock times reconciled with the actual scaling.** The paper's practical efficiency is not in doubt, but the formal claim is wrong as stated.

2. **Training methodology is critically underspecified.** The "n-step REINFORCE algorithm" (Section 4.3) consists of a subsection heading and a single sentence — no equations, no pseudocode, no value of *n*, no baseline specification, no reward normalization, no entropy regularization. The "Model and configuration" subsection (Section 5.1) is similarly empty (heading followed only by a closing brace). The number of GNN layers *K*, hidden dimension *p*, number of attention heads *n_h*, MLP sizes, learning rate, optimizer, batch size, number of training episodes, and training time are all absent from the main text. **This makes the method impossible to reproduce and undermines confidence in the reported results.** Even if some of these details appear in the (stripped) appendix, the main text should summarize the essential choices — a standard practice followed by virtually all papers in this area.

### Minor

3. **The framing of construction-heuristic baselines inflates the perceived contribution.** The abstract and introduction repeatedly emphasize outperforming "state-of-the-art DRL-based methods" (L2D, RL-GNN, ScheduleNet), which are **construction** heuristics producing a single solution in one pass. An improvement heuristic running 500–5000 local moves should naturally dominate one-shot construction methods. The paper does include proper improvement baselines (GD, FI, BI, tabu search) where the advantage is real but narrower. Relegating the construction-heuristic comparison to a secondary role and centering the narrative on improvement-vs-improvement comparisons would better reflect the actual contribution.

4. **Extremely large-instance results (Table 5) lack error bars and diagnostic information.** The reported −24.31% gap against CP-SAT on 200×40 instances is striking but presented without variance across the 100 random instances, without indicating how many CP-SAT runs timed out before finding a feasible solution, and without discussion of whether CP-SAT's hour-long time limit is proportionally reasonable for instances of this scale. These results are plausible but need more scrutiny.

5. **The message-passing evaluator's novelty is modest and unbenchmarked against a baselined CPM.** The evaluator reformulates CPM as a fixed-point message-passing iteration, which is a straightforward re-expression. While practically useful for GPU batching, the paper provides no runtime comparison against an optimized batched CPM implementation — only against a serial CPM implied to be slower. Without this baseline, it is unclear how much of the speed advantage comes from the new formulation versus simply using GPU parallelism.

6. **Ablation study (Figure 6) is only shown for 10×10 instances.** Reporting final test performance across multiple sizes would strengthen the claim that the TPM + CAM combination generalizes.

### Trivial

- The scaling analysis in Section 5.2 ("the run time of our model is linear w.r.t the number of improvement steps *T* for any problem size") conflates scaling with *T* with the Theorem 1 claim about scaling with problem size. These are distinct claims and should be presented separately.
- The hand-crafted rule baselines' restart strategy ("restart to escape local minimum") is vague; the exact criterion (e.g., random restart after *L* non-improving steps) should be specified.

## Nice-to-Haves

- A direct runtime comparison of the message-passing evaluator against an optimized batched CPM on GPU would substantiate the claimed efficiency advantage.
- Reward shaping or denser reward alternatives could be briefly discussed, since the current sparse reward (positive only on incumbent improvement) gives the agent no learning signal on the majority of steps.
- The tabu search comparison could be strengthened by reporting the specific hyperparameters of the Zhang 2007 variant used.

## Removed Points

- **Strength #4 from Strength Finder** ("Theoretical guarantee of linear computational complexity"): Removed because it conflicts with verified Weakness #1 (quadratic action selection contradicts the linearity claim).
- **Generic strengths from Strength Finder**: The Strength Finder's descriptions of "novel dual-module GNN" and "large performance improvements" were kept (they are specific and evidence-backed). No generic or conflicting strengths remain.
- **Harsh critic's point about missing appendix/proofs**: Removed per instructions (parser strips appendix content from all papers; the proofs and training details likely exist in the original submission's appendix).
- **Harsh critic's point about "no formal argument" for Theorem 1**: The specific criticism is kept but subsumed into the broader verified weakness about the quadratic action selection contradicting the linearity claim.
- **Criticism about comparing against methods with unreleased code** ("reproduce RL-GNN and ScheduleNet since their models and code are not publicly available"): Removed per instructions (cited works are assumed to exist).

## Novel Insights

The reviews collectively reveal a tension between the paper's ambitious theoretical framing (linear complexity, formal theorems) and its actual strength, which lies in the **empirical demonstration** that a learned improvement policy can beat both construction heuristics and hand-crafted improvement rules across diverse benchmarks, including impressive zero-shot generalization. The claim that "our method has linear complexity" is the paper's weakest link — it is formally unsupported, architecturally contradicted by the quadratic action selection, and unnecessary for the paper's empirical contributions. The paper would be stronger by substantially dialing back this claim and instead providing an honest empirical complexity characterization. Similarly, the "n-step REINFORCE" subsection is a placeholder rather than a specification; readers and reviewers cannot evaluate whether the training methodology is sound without knowing even basic hyperparameters. These two issues — an overclaimed theorem and a missing algorithm specification — are the gatekeeping problems that prevent the paper's otherwise solid empirical work from being accepted in its current form.

## Suggestions

1. **Correct or remove the linear complexity claim (Theorem 1).** Provide a factual asymptotic analysis of each component (TPM message-passing: O(K·|𝒪|·degree); CAM: O(K·|𝒪|·degree·n_h); action selection: O(|𝒪|²·q)). If the quadratic term is practically dominated (e.g., q is very small or the feasible action set is small), explain why with empirical wall-clock breakdowns.

2. **Fill in the training methodology.** Add a table with all architecture dimensions (K, p, n_h, MLP sizes, q) and training hyperparameters (learning rate, optimizer, batch size, training instances/episodes, n in n-step REINFORCE, baseline type, entropy weight, reward normalization, training time to convergence).

3. **Reframe the narrative.** Center the main results on the comparison with improvement heuristics (GD, FI, BI, tabu search) and present the construction-heuristic baselines (L2D, RL-GNN, ScheduleNet) as a lightweight supplementary comparison — the interesting result is that learned improvement beats hand-crafted improvement, not that a multi-step method beats one-shot methods.

4. **Add error bars and diagnostic commentary for the large-instance experiments (Table 5).** Report standard deviation or min/max across the 100 instances, note how many CP-SAT runs timed out without feasible solutions, and discuss whether the 1h CP-SAT limit is proportionally fair.

5. **Provide a small runtime ablation** comparing the message-passing evaluator against a batched CPM implementation on GPU for various instance sizes and batch sizes, to isolate the speedup attributable to the new formulation vs. GPU parallelism.

## Score and Decision

**Score: 5.0**

The paper proposes a well-motivated approach with a genuinely novel GNN architecture for JSSP improvement heuristics and backs it with strong empirical results across multiple benchmarks. However, it suffers from two major issues that prevent acceptance in its current form: an incorrect/unsupported central complexity claim (Theorem 1) that is contradicted by the quadratic action-selection mechanism, and a critically underspecified training methodology that precludes reproducibility and verification. These issues are fixable with major revision, and the core contributions are worth preserving. A resubmission that honestly characterizes complexity, fills in training details, and adjusts the framing would be competitive.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>