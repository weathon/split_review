Now I have sufficient calibration data. Let me write the final review.

---

## Summary

This paper proposes NYRULES, a fully differentiable framework for learning rule lists that jointly optimizes feature discretization (thresholds), conjunctive rule construction, and rule ordering end-to-end. The method uses soft predicates with temperature annealing to converge to strict rule lists, a relaxed logical conjunction (with a slack parameter η) to avoid vanishing gradients that plagued prior neuro-symbolic methods, and Gumbel-Softmax for differentiable rule ordering. Experiments on 20 binary classification datasets show NYRULES achieving the best average rank (2.60) against eight rule-list and neuro-symbolic baselines.

## Strengths

- **End-to-end differentiable rule-list learning.** NYRULES is the first framework to unify predicate discretization, rule conjunction, and rule ordering in a single differentiable architecture that converges to strict interpretable rule lists via temperature annealing (Section 3, Figure 2). This addresses a real bottleneck in the rule-list literature where prior methods required pre-discretized features.

- **Relaxed conjunction resolves vanishing gradients.** The slack parameter η (Eq. 5) ensures non-zero gradients even when a predicate is inactive, a problem that plagued prior neuro-symbolic rule learning (e.g., Dierckx et al., Qiao et al.). The ablation study (Section 5.2, Figure 5c) confirms this is not just a theoretical fix: the relaxed conjunction improves F1 by 0.3 on average and is never worse than the strict counterpart.

- **Strong empirical performance across 20 datasets.** NYRULES achieves the best average rank (2.60) across 20 real-world binary classification datasets (Table 1), outperforming eight baselines including combinatorial (CORELS, SBRL), heuristic (CLASSY, GREEDY), and neuro-symbolic (RLNET, RRL, DRNET) methods. The advantage is especially pronounced on the Ring dataset (all-continuous features), where NYRULES leads by 0.13 F1.

- **Learns discretization without pre-processing.** NYRULES jointly optimizes continuous feature thresholds, eliminating manual binning that restricts prior methods. The ablation shows learned thresholds outperform both uniform and k-means pre-discretization on many datasets.

## Weaknesses

### Major

- **Runtime inconsistency between text and Figure 6.** The text states "NYRULES on average takes 75s per dataset" (Section 5.1, last paragraph). However, Figure 6 shows NYRULES at approximately 1000 seconds—more than 10× higher. The figure caption describes this as "Average runtime over all benchmarked datasets," making the discrepancy direct and irreconcilable from the paper as written. Furthermore, the text claims GREEDY and CLASSY take "below 10s per dataset," yet Figure 6 shows them at ~150s. The text says NYRULES is faster than RLNET, but the figure shows RLNET at ~150s and NYRULES at ~1000s. This inconsistency must be resolved before the paper's claims about scalability can be trusted. Either the text is wrong, the figure labels/scale are wrong, or they report different experimental conditions—the paper does not provide enough information to determine which.

### Minor

- **Hyperparameter tuning protocol for baselines may handicap them.** The paper states: "For all methods, we grid search the best hyperparameter set using 5 hold-out datasets and use that configuration for all datasets" (Section 5.1). Methods like CORELS, SBRL, CLASSY, and RLNET are known to be sensitive to pre-discretization bin counts, pruning parameters, and priors. Fixing hyperparameters across all 20 datasets (rather than per-dataset cross-validated selection, which is standard practice in this literature) likely disadvantages the baselines. Without per-dataset tuning or a demonstration of robustness, it is unclear how much of NYRULES' rank advantage (2.60 vs. next best 4.00) stems from genuine superiority versus a favorable tuning setup. A sensitivity analysis or per-dataset tuning results would strengthen the comparison.

- **No statistical significance testing.** The paper reports average ranks and standard deviations but no paired significance test (e.g., Wilcoxon signed-rank test or critical difference diagram) across the 20 datasets. The sample size (20) is reasonable, and a significance test would straightforwardly demonstrate whether NYRULES' advantage over the next-best methods (e.g., 2.60 vs. 4.00) is statistically reliable. Its absence weakens the evidence, especially given the hyperparameter concern above.

- **Small average benefit from learned thresholds and ordering.** The ablation studies show that removing learned thresholds degrades F1 by only 0.04 on average, and removing learned ordering degrades F1 by 0.03 on average (Section 5.2). While the paper notes the benefit is dataset-dependent, the small average improvement suggests that the main performance gain of NYRULES comes from the relaxed conjunction and the overall end-to-end architecture rather than from learning thresholds or ordering per se. The paper should acknowledge this more explicitly.

### Trivial

- **Contradiction about multi-class in future work.** The Future Work section states "the current rule list model is only designed for binary classification tasks," yet Table 2 already presents multi-class results (with NYRULES achieving rank 1.50 on four datasets). The paper either performed multi-class classification successfully (contradicting the stated limitation) or the future-work sentence is a remnant that should be removed or rephrased.

## Nice-to-Haves

- Including per-dataset dataset characteristics (size, number of features, class balance) in the main paper would help readers assess generalizability.
- Showing an oracle baseline with optimal pre-discretization per dataset would more directly isolate the benefit of learned thresholds.
- Reporting rule complexity metrics (average rule length, number of active features per rule) for baselines would contextualize the interpretability trade-offs.
- Adding pseudocode or a training algorithm box would aid reproducibility.

## Removed Points

These points were raised by reviewers but are removed with justification:

- **Controlled synthetic experiment on Ring dataset (Harsh Critic):** The critic says "a controlled synthetic experiment (which they do have in Appendix E, but we cannot see) would be stronger." The appendix was stripped by the parser; the paper already includes this experiment. Removed per instructions about missing appendix content.

- **Gradient behavior analysis in Appendix A.3 (Harsh Critic):** The critic notes the analysis "relies entirely on Appendix A.3 (removed)." Removed—appendix content was stripped by the parser.

- **Dataset characteristics/hyperparameters referenced as missing (Harsh Critic):** These details are in Appendices B/C, which were stripped by the parser. Removed.

- **Competitive runtime strength (Strength Finder):** This strength claimed NYRULES runs in 75s on average, but Figure 6 shows ~1000s. Since the text and figure contradict each other, this strength is unsupported and removed.

- **Generic strengths about "important problem" (Strength Finder):** Removed as generic/superficial.

- **Speculation about rank computation handling n/a values (Harsh Critic):** Removed as speculation without evidence from the paper.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Resolve the runtime inconsistency immediately.** Determine whether 75s or ~1000s is correct for NYRULES, and whether the figure labels/scale are accurate. Provide error bars and the distribution of runtimes across datasets. If the 75s figure is correct, explain what the ~1000s figure represents. If ~1000s is correct, acknowledge that NYRULES is slower than baselines like RLNET (contrary to the text) and argue why the accuracy gains justify the cost.

2. **Add statistical significance testing.** A Wilcoxon signed-rank test or Nemenyi critical difference diagram for Table 1 would substantially strengthen the evidence for NYRULES' rank advantage.

3. **Clarify the hyperparameter protocol and add a sensitivity analysis.** Either adopt per-dataset hyperparameter selection for baselines (which is standard) or demonstrate that NYRULES' advantage is robust to the chosen protocol.

4. **Fix the multi-class contradiction** in the Future Work section.

5. **Acknowledge the modest average benefit of learned thresholds/ordering more explicitly** in the main text, and clarify that the main mechanism driving performance is the relaxed conjunction.

## Score and Decision

**Round 1 bracketing:** Three queries on "differentiable rule learning neuro-symbolic rule list interpretable ML" returned anchors at:
- Low band (<3.5): 2.50–3.40 (e.g., Neural Probabilistic Logic Learning 3.00, Neural Description Logic 3.40, COOL 2.50, Guided Sketch-Based 2.50)
- Middle band (3.5–7.5): 4.25–6.25 (FUSE-ILP 4.25, LFL 4.40, Predictive Checklists 5.67, NSR 6.25)
- High band (>7.5): 8.00 (Phenomenal Yet Puzzling 8.00, D-TSN 8.00, MILLET 8.00, PTaRL 8.00)

The paper clearly surpasses the low-band anchors and is not at the 8.0 level of the high-band anchors. Initial bracket: **4.5–7.0**.

**Round 2 narrowing:** Queries within (4.5–6.0) and (6.0–7.5) returned:
- Logic-Logit (5.50, Accept Poster): similar rule-based interpretable model with strong empirical evaluation but some methodological questions. NYRULES is comparable in quality — better ablation studies and clearer methodology, but undermined by the runtime inconsistency.
- Differentiable Decision Trees (5.00, Reject): weaker method presentation and limited scope compared to NYRULES.
- Discovering Logic-Informed Rewards (5.75, Reject): tangentially related with some methodological concerns.
- NSR (6.25, Accept Poster): stronger novelty and systematic generalization results; NYRULES is slightly weaker due to the concrete runtime error.

FINAL SCORE: 5.5 — The paper has a genuine contribution (end-to-end differentiable rule-list learning with relaxed conjunction solving vanishing gradients). The empirical evaluation is extensive and the results are promising. However, the runtime inconsistency between text and Figure 6 is a concrete error that undermines an explicit claim until resolved, and the hyperparameter tuning protocol weakens the comparison fairness. These issues are fixable with revision.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>