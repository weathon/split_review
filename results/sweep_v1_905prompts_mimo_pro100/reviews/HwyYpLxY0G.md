Now I have enough data to write the final review. Let me synthesize everything.

## Summary

This paper proposes Aligned Scoring Rules (ASR), an optimization framework for designing proper scoring rules for textual elicitation (specifically peer grading) that align with human preferences. Building on the reduction from Wu & Hartline (2024) that maps textual elicitation to numerical elicitation via LLM oracles, the authors formulate a convex optimization problem over the space of separate (additive) proper scoring rules to minimize MSE between the proper score and a reference score (instructor score or LLM-Judge score). Experiments on a 22-assignment peer grading dataset show improved alignment with reference scores compared to unoptimized baselines.

## Strengths

- **Clean convex optimization formulation with provable guarantees.** The paper formulates alignment of proper scoring rules as a convex optimization problem (Program 2, Corollary 3.4), enabling efficient computation via gradient descent. The separate scoring rule structure (weighted average of single-dimensional proper scoring rules) is a natural and well-motivated restriction that yields convexity where other aggregation classes (e.g., max-over-separate) would not.

- **Substantial quantitative improvement over baselines.** Table 1 shows ASR achieves MSE of 1.730 vs. 9.541 for EGPT(AV) and 18.360 for EGPT(MV) on instructor scores, with Pearson correlation of 0.717 vs. 0.294 and 0.213 respectively. These are roughly 5× improvements in MSE, and the baselines (averaged V-shaped and max-over-separate V-shaped scoring rules from Wu & Hartline 2024) represent the prior state of the art for truthful textual scoring.

- **Near-identity regression confirms effective alignment.** Figure 4 and Section 5.3 show that linear regression of reference scores on ASR scores yields a nearly-identity fit (s ≈ S), providing direct visual and quantitative evidence that ASR faithfully recovers the reference score distribution while maintaining properness by construction.

- **Well-articulated connection to prior theoretical framework.** The paper clearly builds on Wu & Hartline (2024)'s reduction, adopting the computation framework of Li et al. (2022) for optimal scoring rules. Theoretical guarantees (Theorem 3.2 for properness under non-inverting oracle, Theorem 3.3 for adversarial robustness) are clearly stated and inherited cleanly through the optimization.

- **Dual reference score evaluation demonstrating practical flexibility.** The paper optimizes and evaluates against both instructor scores and LLM-Judge scores (Table 1), with high correlation (0.554) between the two references (Figure 3), supporting LLM-Judge as a scalable substitute for costly instructor scores.

## Weaknesses

### Fatal

None

### Major

- **No generalization evaluation.** The paper optimizes ASR per-assignment cluster and evaluates on the same training data. With only 22 assignments (~516 reviews total) and no cross-validation, held-out evaluation, or any form of generalization analysis, the near-perfect fit (Figure 4) and low MSE (Table 1) could simply reflect overfitting within a flexible hypothesis class. The paper provides no evidence that ASR weights transfer across assignments, that performance degrades gracefully with less training data, or that the method generalizes beyond the training distribution. This is the most significant gap: the primary empirical claim is that ASR fits reference scores, but fitting training data is a baseline expectation for any convex optimizer.

- **Experimental evaluation lacks ablations and statistical rigor.** The evaluation reports MSE, Pearson, and Spearman correlations without any confidence intervals, variance estimates, or statistical significance tests. There are no ablations on the number of summary points *m*, the choice of LLM for oracles (GPT-4.1 results are mentioned for Appendix B but not analyzed for oracle impact), the amount of training data per cluster, or the sensitivity of ASR to prompt variation in the summarization pipeline. Given the convexity of the problem (making such experiments computationally cheap), this is a missed opportunity.

### Minor

- **Interpretability claim is unsupported in the main text.** The paper lists interpretability as a contribution ("Our Aligned Scoring Rule (ASR) is simple, provably truthful, and interpretable," line 61), and states that "we show the interpretability of ASR by a case demonstration in the appendix" (lines 73–74). However, the appendix is not included in the reviewed version, and the main text contains no analysis of the learned weights *w_i* or the shape of learned scoring rules *S_i*. This claim cannot be assessed from the paper as presented.

- **Abstract overstates empirical contribution regarding properness.** The abstract states "Our experiments show that our ASR outperforms previous methods in aligning with human preference while maintaining properness." Properness is maintained by construction (it is a hard constraint in Program 2), not demonstrated empirically. The phrasing is misleading as it implies properness is an experimental finding.

### Trivial

None

## Nice-to-Haves

- **Generalization across clusters.** Even a simple leave-one-assignment-out evaluation would substantially strengthen the paper and is computationally inexpensive given the convex formulation.

- **Demonstrating that alignment improves mechanism quality.** A simple simulation showing that strategic agents face better incentive properties under ASR than under non-aligned scoring rules would validate the MSE objective as a meaningful proxy for the actual goal (better peer review incentives).

- **Analysis of learned scoring rules.** Showing the optimized weights and scoring rule shapes for several assignments and discussing what they reveal about grading priorities would make the paper substantively richer and support the interpretability claim.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Harsh critic: "The evaluation does not test the paper's core claim."** Partially valid but overstated. The paper's stated goal is to "align a provably proper textual scoring rule with preferences" (line 54). The experiments test alignment (MSE, correlation). The concern about testing incentive properties in deployment is valid as a nice-to-have but the paper's core technical contribution is the optimization framework, not a deployed mechanism.

- **Harsh critic: "The comparison against EGPT baselines is uninformative because they perform poorly."** The EGPT(AV) and EGPT(MV) baselines are the prior state-of-the-art from Wu & Hartline (2024). Comparing against them is appropriate and informative. The fact that they don't optimize for alignment is precisely the point—the paper demonstrates value of the optimization.

- **Harsh critic: "Assumption 2.2 limits applicability."** The paper acknowledges this is driven by the peer grading dataset (line 169: "In our peer grading dataset, we observe that textual reports either express a state being 0 or 1, or have no information"). This is a reasonable scoping choice, not a weakness.

## Novel Insights

The paper's most genuinely novel observation is that the optimization of proper scoring rules for alignment can be cast as a convex program over separate scoring rules, yielding both computational tractability (gradient descent over samples) and interpretability through the per-dimension scoring rule structure. The near-identity regression result (Figure 4) provides concrete evidence that the MSE objective produces an effectively aligned proper score, which is a non-trivial empirical finding given that properness is a constraint that could in principle conflict with alignment.

## Suggestions

1. Add leave-one-out or k-fold cross-validation across assignment clusters to demonstrate generalization. This is the single most important addition needed.
2. Include ablations on the number of summary points *m*, the choice of LLM for oracles, and the amount of training data.
3. Report confidence intervals or standard errors for all metrics.
4. Present at least one learned scoring rule analysis in the main text (not just appendix) to support the interpretability claim.
5. Correct the abstract phrasing regarding properness being maintained "by construction" rather than as an empirical finding.

## Calibration Report

**Round 1 anchors:**
- Low band: "Learning-based Mechanism Design" (2.50, Reject), "Data Distribution Valuation" (3.00, Reject), "Adaptive Proximal Gradient" (1.67, Reject), "Risk Quadrangle" (3.00, Reject)
- Mid band: "Truthfulness Without Supervision" (4.67, Reject), "Peering Through Preferences" (6.50, Accept), "Win Rate is All that Can Matter" (3.75, Reject), "Automatic Calibration" (5.75, Reject)
- High band: "Rethinking Reward Modeling" (8.00, Accept), "Probabilistic Perspective on Unlearning" (8.00, Accept), "Trust or Escalate" (8.00, Accept), "Spread Preference Annotation" (8.67, Accept)

**Round 1 bracket: 4.5 to 6.5.** The paper has a cleaner theoretical contribution than the ~4.67 anchors and comparable (thin) experiments. It is substantially less comprehensive than the 6.5 anchors.

**Round 2 anchors:**
- "Truthful Aggregation of LLMs" (5.25, Reject) — mechanism design for LLMs with theory but weak experiments, no real-world testing. Comparable to this paper in having sound theory with limited empirical validation.
- "Mechanism Design with Multi-Armed Bandit" (4.67, Reject) — theory-heavy, unclear contribution, limited experiments. Weaker than this paper.
- "Deep RL for Sequential Combinatorial Auctions" (5.75, Reject) — more extensive experiments but similar issues.
- "Private Mechanism Design via Quantile Estimation" (6.50, Accept) — more complete theoretical and empirical contribution.
- "Learning Optimal Contracts" (6.00, Accept) — solid theory with experiments.
- "Reassessing Calibration" (5.67, Accept) — clean methodology but limited experiments.

**Final positioning:** The paper's core contribution (convex optimization for aligned proper scoring rules) is well-motivated and cleanly presented. The experiments demonstrate meaningful improvements over state-of-the-art baselines (5× MSE improvement). However, the complete absence of generalization evaluation and the small scale of experiments (22 assignments, ~516 reviews, no ablations) are significant limitations that prevent confident claims about the method's practical value. Compared to the 5.25 "Truthful Aggregation" anchor, this paper has a tighter connection between theory and experiments. Compared to the 6.00 "Learning Optimal Contracts" anchor, this paper lacks generalization evidence. I position this at **5.5**.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>