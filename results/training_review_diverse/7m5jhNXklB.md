Now I have a thorough understanding of the paper and the reviewer inputs. Let me write the consolidated review.

## Summary

This paper proposes VTruST, a data-centric framework for controllable training data subset selection targeting tradeoffs among accuracy, fairness, and robustness. The core idea is to define additive value functions for each trustworthiness metric, pose subset selection as an online sparse approximation problem, and solve it with a novel online variant of Orthogonal Matching Pursuit (OMP). Experiments on social, image, and scientific datasets demonstrate that subsets selected by the method can match or outperform several baselines.

## Strengths

1. **Novel online OMP algorithm for data-centric subset selection.** The paper proposes an online variant of Orthogonal Matching Pursuit (Algorithm 1 + DataReplace, Algorithm 2) that avoids storing features across all epochs by operating on the selected set only. The per-epoch complexity is O(ωM(N−ω)) vs. standard OMP's O(ωMN). This algorithmic adaptation is a genuine contribution to the sparse approximation literature in the context of online training.

2. **Controllable composite value functions enable explicit tradeoffs among trustworthiness metrics.** The paper defines additive value functions for accuracy (V_a), robustness (V_r), and fairness (V_f), and combines them via user-specified weights λ. The Pareto-front curves on Adult Census data (Figure 1) experimentally demonstrate that varying λ produces meaningful tradeoffs (e.g., error rate vs. fairness disparity), validating the core controllable-framework premise.

3. **Empirical results show meaningful improvements over several baselines across diverse domains.** On fairness (Table 1), VTruST-F achieves competitive or better EO/DP disparities while maintaining error rates close to full-data training. On robustness (Table 2), VTruST-R outperforms SSR across datasets and subset sizes (e.g., RA 89.21 vs. 88.0 on CIFAR-10 at 60% selection). On scientific datasets (Table 3), VTruST-R at 40% selection achieves RA 78.36 on Spinodal, exceeding the wholedata's RA of 76.89.

4. **Data-centric explanations connect subset characteristics to model behavior.** The analysis of CF-Gap for fairness and uncertainty/distinctiveness for robustness (Section 4.3) goes beyond metric reporting to provide interpretable rationale for why the selected subsets lead to the observed properties.

## Weaknesses

### Major

1. **The fairness value function lacks a valid theoretical foundation within the framework.** There are two distinct problems:

   (a) **The claim that EO disparity is additive over validation sets (line 96) is mathematically false.** The paper states that "ed(θ,D'_1) + ed(θ,D'_2) = ed(θ,(D'_1+ D'_2))" for the equalized odds disparity, which is defined as max of absolute loss differences. This does *not* hold: the maximum of absolute differences is not additive over disjoint validation subsets. This error suggests a misunderstanding of the additivity requirement.

   (b) **The features used for sparse approximation are derived from a Taylor expansion of the loss (line 68), but the fairness value function involves changes in EO disparity — a non-linear function of per-group losses — not changes in loss itself.** The paper does not discuss how the loss-based Taylor expansion approximates changes in EO disparity, nor does it derive a corresponding expansion for the fairness objective. The composite value functions V_af and V_fb (line 99) add a scalar fairness term to vector-valued accuracy/robustness terms, creating a dimensional mismatch (V_f is a scalar, while V_a is M-dimensional). This gap means the theoretical justification for the fairness component (and by extension V_af and V_rf) is unsupported.

   *Severity assessment*: This is a major weakness because the paper's claim of handling fairness is central to its contribution. However, it may not be fatal: (i) the fairness experiments might still work as a heuristic, (ii) the core contributions (online OMP, accuracy-robustness framework) are not invalidated by this issue, and (iii) the problem could be addressed by defining a truly additive fairness surrogate (e.g., sum of per-group loss differences) or by acknowledging the approximation and relabeling the fairness component as heuristic.

### Minor

2. **Robustness experiments (Table 2) are reported without variance estimates.** Table 1 for fairness includes standard deviations across 3 runs, but Table 2 reports only point estimates. This makes it impossible to assess the reliability of the claimed improvements. The TinyImageNet results in particular show enormous gains over SSR (e.g., SA 60.88 vs. 41.94 at 60% selection) — such large margins warrant variance reporting to rule out a single run.

3. **SSR baseline performs anomalously on TinyImageNet.** SSR at 60% selection (180K augmented samples) achieves SA = 41.94, far below Clean-ST (100K clean samples, SA = 63.98). This is unusual for a data-selection method and suggests SSR may not have been properly tuned for the augmented-data setting on this dataset. Since the largest claimed improvements over SOTA come from this dataset, the paper should explain or control for this discrepancy.

4. **The abstract claims ~10-20% improvement over SOTA, which the experiments do not consistently support.** On fairness (Table 1), improvements over the best baseline are typically fractions of a percent in error rate and small margins in EO/DP disparity (~0.01–0.10). On robustness (Table 2), gains over SSR are modest on MNIST and CIFAR-10 (0.05–1.21 points) and only reach large magnitudes on TinyImageNet where the baseline performs poorly. The claimed range is not representative of the full results.

5. **Theorem 1 (lines 214-218) is not a meaningful theoretical contribution.** It largely restates the logic of the DataReplace algorithm in notation without providing an approximation-quality guarantee, convergence bound, or optimality certificate. The proof is deferred to an appendix (which is stripped, but the main text should offer more substance). The algorithm's design intuition is reasonable, but it is presented as a theorem without delivering the analytical insight the label promises.

### Trivial

6. **The complexity analysis on line 185 omits the O(|S_t|²M) least-squares solve for recomputing β_t at each step, considering only the correlation computation cost.**
7. **Several baselines (FairMixup, FairDummies, SAug) are not subset-selection methods, which slightly muddies the comparison framing, though they are established baselines in their respective literatures.**
8. **The qualitative data-centric explanation analysis (Section 4.3) is interesting but could benefit from quantitative metrics to support the visual/anecdotal evidence.**

## Nice-to-Haves

- A simple gradient-norm or influence-based data valuation baseline for robustness (e.g., selecting top-k points by gradient norm) would help isolate the benefit of the sparse-approximation formulation.
- Sensitivity analysis of results with respect to hyperparameters ω (subset size) and λ (tradeoff weight) would strengthen the controllability claims.
- Wall-clock training times per epoch or total runtime would help assess practicality, especially for large datasets.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh critic's claim that "FairMixup and FairDummies are not data-centric subset selection methods" is noted but kept in Trivial — the paper compares against the SOTA fairness literature, which is a common and defensible choice; this is not a weakness that undermines the paper.**
- **Harsh critic's criticism that "the paper should compare to Shapley-based methods for fairness" — this is a missing-related-work critique that I cannot independently verify, and the paper already engages with the most directly relevant fairness-aware data-centric baseline (SSFR).**
- **Strength Finder's strength "Substantial empirical improvements over SOTA" is downgraded because the improvements are modest overall and the largest gains are on a dataset where the baseline performs poorly.**
- **Harsh critic's complaint that SAug is "not a subset selection method" — the paper includes it as a full-data augmentation baseline, which is standard practice to show that subset selection can approximate full-data performance; this is not a weakness.**

## Novel Insights

None beyond the paper's own contributions. The novel element is the online OMP adaptation for data subset selection with composite value functions; the reviews do not surface additional insights beyond what the paper already claims.

## Suggestions

1. **Address the fairness theoretical gap directly.** Either (a) define a truly additive fairness surrogate (e.g., per-group loss differences summed without the max, which is linear in the loss and thus amenable to the Taylor expansion), (b) show empirically that the loss-based features work as a reasonable heuristic for fairness even though the theory is loose, or (c) scope the paper as an accuracy-robustness framework and position the fairness results as a preliminary extension.

2. **Report standard deviations or confidence intervals for all main experiments, especially Table 2.**

3. **Add an ablation study isolating the online OMP component** (e.g., compare to an offline variant or a simpler greedy selection without the replacement step) to disentangle the contribution of the algorithm from the value function design.

4. **Replace Theorem 1 with a clear, intuitive explanation of the replacement rule's motivation** and, if possible, provide a meaningful approximation-quality bound or convergence guarantee. If no such guarantee exists, label the result as a remark rather than a theorem.

5. **Tone down the "10-20%" claim in the abstract** to accurately reflect the empirical evidence.

## Score and Decision

The paper tackles an important problem — data-centric control over multi-objective trustworthiness — and the online OMP algorithm is a genuine algorithmic contribution. However, the fairness value function has a significant theoretical gap: the derivation of the sparse approximation features from the loss Taylor expansion does not extend to the EO-disparity-based fairness objective, and the paper makes a mathematically incorrect claim about additivity of EO disparity over validation subsets. This undermines the theoretical foundation of the fairness (and fairness-robustness) components. The robustness experiments are more sound but lack variance estimates, and the largest claimed gains come from a dataset where the SSR baseline performs suspiciously poorly. These issues are addressable in revision, but the paper in its current form does not provide a reliable evaluation for its fairness claims.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>