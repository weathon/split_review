Now let me write the final consolidated review.

## Summary

This paper proposes GAMA, a neural neighborhood search method for the Capacitated Vehicle Routing Problem (CVRP) that models the problem instance and the evolving solution as two distinct modalities, encodes them via a Dual-GCN, and fuses them through stacked self-attention, cross-attention, and a learned gated fusion mechanism. The resulting state representation feeds a PPO-based policy that selects local search operators adaptively. Experiments on CVRP20/50/100 and the Uchoa benchmark show that GAMA achieves competitive or better average costs than several neural baselines (DACT, L2I) and classical solvers (LKH3, HGS), with an ablation study confirming that the cross-attention and gated fusion each contribute to performance.

## Strengths

- **Principled multi-modal encoder design.** GAMA is the first method to treat the distance graph (instance geometry) and the solution graph (current routing topology) as distinct semantic modalities, then model their interaction via stacked self-attention (intra-modality) and cross-attention (inter-modality). This is a clean, well-motivated architectural improvement over prior work like GENIS, which uses dual GCNs without cross-modal communication. The ablation in Table 2 isolates this: on CVRP100, GAMA (15.6510) outperforms GENIS (15.7441) and the cross-attention-free variant GAMA_NG (15.7001).

- **Rigorous ablation with statistical testing.** All ablation experiments are run 30 times independently and tested with the Wilcoxon rank-sum test (α=0.05), with clear notation (↑/↓/≈). This provides solid evidence that the reported improvements from cross-attention and gated fusion are not due to chance—a standard of rigor many concurrent papers lack.

- **Competitive results and strong zero-shot generalization.** On CVRP100 (T=20k), GAMA achieves an average cost of 15.6510, surpassing LKH3 (15.6752), HGS (15.6994), DACT (15.6925), and L2I (15.7334). On the Uchoa benchmark (100–1000 customers, unseen distributions), GAMA achieves an average optimality gap of 4.956%—the best among all neural methods tested (ReLD: 5.018%, DACT: 25.305%, L2I: 13.557%)—without any retraining.

- **Well-motivated problem framing.** The paper clearly identifies two genuine limitations of existing L2I methods: coarse state representations that miss structural detail, and naive concatenation of heterogeneous features. The proposed solution (modality-specific encoding + attention-based fusion) follows naturally from this diagnosis.

## Weaknesses

### Fatal
None.

### Major

- **Uncontrolled comparison in search strategy.** GAMA applies exhaustive best-improvement neighborhood search per operator selection (Section 3.1: "the selected operator is applied exhaustively in the neighborhood of the current solution, the best improving move is then adopted"), while baselines DACT and L2I use different per-step search strategies. The paper reports results by number of steps (T=5k/10k/20k) and wall-clock time but never controls for the *number of solution evaluations* per step. Because GAMA evaluates the entire neighborhood of the chosen operator each step while baselines sample fewer moves, the comparison on step count alone conflates the learned policy's contribution with the search strategy's thoroughness. This does not invalidate the results—wall-clock times are comparable across methods at the same T (e.g., CVRP100 T=20k: GAMA 19m, DACT 19.3m, L2I 18.7m)—but without controlling for evaluation effort, the headline claim "significantly outperforms recent neural baselines" is not fully disentangled from the choice of search procedure. The authors should at minimum report per-step evaluation counts and ideally run a controlled experiment with equivalent search budgets.

- **Missing statistical testing against classical solvers in the main comparison.** Statistical significance (Wilcoxon, Table 2) is reported only in the ablation section comparing GAMA to its ablated variants. The main results (Table 1) report point estimates over 30 runs but do not test whether GAMA's advantage over LKH3/HGS is statistically significant. On CVRP50, the gap between GAMA (10.3533) and HGS (10.3548) is only 0.0015 (≈0.014%), which is well within the noise range of a single standard deviation. The claim "GAMA maintains superior solution quality across all instance sizes" is not supported by statistical evidence for the smaller sizes.

### Minor

- **Very marginal improvements on small instances.** On CVRP20, GAMA's average (6.0810) vs. HGS (6.0812) and DACT (6.0811) represents a ~0.003% improvement. On CVRP50, GAMA (10.3533) vs. HGS (10.3548) is ~0.014%. While statistically significant in the ablation, these differences are so small that they lack practical significance. The paper's framing ("significantly outperforms") should be calibrated to problem size—the contribution is empirically strongest on CVRP100 and larger.

- **Phase-level reward assignment creates temporal credit-assignment ambiguity.** The reward function (Section 3.2) assigns the same reward r_t = f(δ₀) − f(δ*₍ₖ₎) to all transitions within an improvement phase, computed at the end using the best solution found therein. Since the reward for an action at time t depends on outcomes of future actions within the same phase, this is technically non-Markovian. The paper follows the same design as Lu et al. (2019), so this is not a novel flaw, but the paper does not discuss the potential credit-assignment bias or justify why it does not harm learning. A brief discussion would strengthen the methodology section.

- **Missing no-policy (random operator selection) baseline.** The ablation compares GAMA against GENIS (learned encoder without attention fusion) and GAMA_NG (without gated fusion). Both use the same exhaustive search and learned policy. What is missing is a baseline that uses *random operator selection* with the same exhaustive search. This would isolate whether the learned policy contributes anything beyond the search strategy itself. The GENIS comparison already shows the encoder matters, but a random baseline would be the cleanest ablation of the policy's value.

- **Figure 2 y-axis labeling error.** The box plot caption labels the y-axis as "Gap %" but the range shown (10.35–10.41) corresponds to absolute costs, not percentage gaps relative to optimal. On CVRP50, the optimality gap is ~0.3–0.5%, not 10.35–10.41. This is a presentation error that should be corrected.

### Trivial
- The paper does not explicitly state the number of operators in the action space or the exact GCN architecture (number of layers, hidden dimensions) in the main text, deferring architectural details to the appendix. While the appendix exists in the original submission, a brief summary in the main text would improve readability.

## Nice-to-Haves
- **Solution evaluation counts:** Report the number of candidate solutions evaluated per step for all methods, allowing a fair comparison of search effort that separates the policy's contribution from the search strategy's.
- **Random operator baseline:** Add a variant of GAMA with random operator selection (same exhaustive search) to directly measure the learned policy's contribution.
- **Per-operator analysis:** Visualize which operators the learned policy selects at different stages of search, and how the cross-attention weights correlate with structural properties of the solution.

## Removed Points
These points are flagged to be removed, treat them with caution:
- "The paper does not specify the exact set of operators used (only '2-opt, swap, insertion and so on')" — The paper explicitly states "The details of the operators are presented in supplementary material." The appendix exists in the original submission but is stripped by the parser. This is a parser artifact, not an author omission.
- "Missing hyperparameters for baselines beyond a reference to original papers" — The paper states each baseline uses its official implementation with "hyperparameters set according to the original paper's recommendations." This is standard practice.
- "The comparison with classical solvers is unfair because they run without a search budget cap while GAMA runs for fixed steps" — Reporting each method's converged solution quality is a standard experimental design for benchmarking.
- "The paper claims GAMA is a 'neural' method but the actual search is exhaustive local search" — This is a description of the method, not a flaw. The neural component learns which neighborhood to explore; this is clearly stated in the abstract and introduction.
- Criticism about the encoder's inference cost not being reported — This is a reasonable request but is a secondary analysis that does not undermine the core claims.
- Claim that the method's reliance on a fixed-size action space is not discussed as a limitation — The paper discusses future work on operator interactions in the conclusion.
- The criticism that Algorithm 1 pseudo-code is "poorly structured" — The algorithm is functional and follows standard conventions. The phase reward computation is correctly scoped within the no-improvement detection block.

## Novel Insights
None beyond the paper's own contributions. The reviews do not surface a perspective that the paper itself does not already articulate.

## Suggestions
1. **Control for solution evaluations:** Re-run baselines while counting candidate solutions evaluated per step, and report results at equal evaluation budgets to disentangle the policy's contribution from exhaustive search.
2. **Add statistical tests to Table 1:** Report whether GAMA's differences from LKH3/HGS are statistically significant (Wilcoxon, as done in the ablation).
3. **Add a random operator baseline:** Include a variant with random operator selection and exhaustive search to directly measure the policy's value.
4. **Fix Figure 2 y-axis label:** The range 10.35–10.41 corresponds to absolute cost, not Gap %. Correct the label.
5. **Tone down claims on small instances:** The improvements on CVRP20/50 are practically negligible. Acknowledge this explicitly.

## Score and Decision

**Calibration anchors** (all from /home/wg25r/review_agent/human_reviews_2026/):

| Anchor | Avg Score | Comparison to GAMA |
|--------|-----------|-------------------|
| HADES (NLgJcADMtr.md) | 4.00 | Similar neural improvement paper for VRP with marginal gains on small instances and incomplete experimental controls. GAMA has a stronger architectural contribution and more rigorous ablation. |
| AGOF (kivcvgV52Z.md) | 4.50 | 2-Opt neural framework with narrower scope. GAMA's multi-modal encoder is more novel and general. |
| L2R (hAurIMOhOW.md) | 4.00 | Search space reduction paper. Strong generalization but less architectural novelty. GAMA is comparable in rigor. |
| URS (EiEbn6FZsK.md) | 4.50 | Ambitious unified VRP solver with questionable LLM component. GAMA is cleaner and more focused. |
| MoH (tIQZ7pVN6S.md) | 5.00 | LLM heuristic generation. Cleaner experiments and better generalization story. GAMA has a stronger architectural contribution but a weaker evaluation. |
| RRNCO (sKvo9ZZfpe.md) | 5.50 | Real-world routing benchmark with practical contribution. GAMA is less impactful but offers a novel architectural approach. |
| Rethinking Distance Metric (R6np5nEhJo.md) | 2.50 | Weak contribution, insufficient novelty. GAMA is substantially stronger. |

Relative to these anchors, GAMA sits between the rejected papers (4.0–4.5) and the accepted ones (5.0–5.5). Its architectural contribution (multi-modal attention with cross-attention and gated fusion) is genuine and well-validated by ablation. However, the evaluation has two significant shortcomings: (1) the uncontrolled search strategy comparison with baselines conflates the policy's contribution with exhaustive search, and (2) the improvements on small instances are practically negligible. Combined with the missing statistical testing against classical solvers, these issues prevent the paper from reaching the clarity and rigor expected for a clear accept.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>