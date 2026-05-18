Now I have all the evidence I need. Let me produce the consolidated review.

## Summary

This paper identifies a confound in prior safe SSL evaluations of unseen-class impact: prior work fixed the total unlabeled set size while varying unseen-class proportion, which simultaneously changes seen-class data volume. The authors propose RE-SSL, an evaluation framework that holds seen-class data constant while only varying unseen-class data, and systematically evaluate 15 SSL methods across five factors (sample count, category count, category index, nearness, label distribution) using five robustness metrics. The paper is an evaluation/benchmark contribution — its primary value is the corrected evaluation protocol and the empirical findings it produces.

## Strengths

- **Identifies and addresses a genuine confounding issue in prior safe SSL evaluations.** The paper correctly observes that when total unlabeled set size is fixed and unseen-class proportion varies, seen-class data quantity changes simultaneously, making it impossible to attribute performance changes solely to unseen classes. The structural causal model in Figure 1 clearly illustrates this confound, and RE-SSL's design (fixing $r_s$ while varying $r_u$) is a principled correction. This is the paper's central methodological contribution and is well-motivated.

- **Systematically evaluates SSL methods across five distinct factors.** Beyond sample quantity ($r$), the paper studies category number ($C_n$), category index ($C_i$), nearness (near vs. far OOD), and label distribution ($C_{ib}$). This multi-factor scope is genuinely broader than prior work and generates useful comparative insights — e.g., that models are most sensitive to unseen-class sample quantity and relatively robust to label distribution changes (Table 6). The GM summary table clearly condenses this cross-factor analysis.

- **Introduces a set of five complementary robustness metrics.** The metrics ($R_{slope}$, GM, WAD, BAD, $P_{AD\geq0}$) go beyond single-point accuracy comparisons and capture both global trends and local fluctuations. The distinction between global robustness (Definition 1) and local robustness (Definition 2) provides a reusable analytical vocabulary for the field.

- **Broad method coverage with consistent methodology.** Evaluating 10 classic + 5 robust SSL methods on two datasets (CIFAR10 and CIFAR100) under identical conditions (ResNet50, LAMDA-SSL, 3 seeds) enables meaningful cross-algorithm comparisons. The finding that PseudoLabel, ICT, UASD, and CAFA are robust across both datasets, while FixMatch is consistently fragile, is empirically grounded.

## Weaknesses

### Fatal

None. The paper's core claims are supported by evidence, and no errors invalidate the central contribution.

### Major

None. The weaknesses identified are genuine but fixable and do not undermine the paper's overall contribution.

### Minor

- **Overstated critique of prior work.** The paper frames prior safe-SSL evaluations as categorically "flawed" (Sections 1, 3, 8) and "unfair." While the confounding critique is scientifically valid, prior work's design (fixing total $D_U$ size while varying composition) answers a different but legitimate question: "given a fixed pool of unlabeled data, how does its composition affect performance?" RE-SSL answers a complementary question: "what is the marginal effect of adding unseen-class samples to a fixed seen-class pool?" The paper would be more defensible by acknowledging this complementarity rather than dismissing prior work as categorically wrong. As written, the strong language invites unnecessary pushback against what is otherwise a valid methodological contribution.

- **Unjustified threshold in robustness definition.** Definition 1 classifies methods as globally robust if $R_{slope} \geq \delta_g$, and $\delta_g = -0.020$ is set without any justification. The paper says "assume that $\sigma_g$ equals -0.020" (line 128) — the same value is applied to both CIFAR10 and CIFAR100 without explanation of why -0.02 (rather than -0.01 or -0.05) is meaningful or how it relates to practical deployment tolerances. This choice affects which methods are labeled "robust" and could shift conclusions. The paper's relative ranking approach (using GM, $F_{avg}$) is more principled and should be foregrounded.

- **Linearity assumption in $R_{slope}$ not discussed.** The $R_{slope}$ metric fits a linear regression to accuracy at discrete $r$ values (0, 0.2, 0.4, 0.5, 0.6, 0.8, 1.0), which assumes the accuracy-vs-unseen-class relationship is linear. Visual inspection of Tables 1-2 suggests some methods exhibit nonlinear patterns (e.g., plateauing then dropping). The paper does not acknowledge this assumption or test its sensitivity. The GM metric avoids this issue and should be treated as the more reliable global measure.

- **Missing variance estimates.** The paper reports averages from three seeds (line 119) but provides no standard deviations, confidence intervals, or individual run results. Given the known variability in SSL training, this omission makes it difficult to assess whether observed differences between methods or across conditions are statistically meaningful. At minimum, standard deviations should be reported in the tables or an appendix.

- **Nearness analysis could be deeper.** The comparison of near OOD (CIFAR unseen classes) vs. far OOD (MNIST) is valuable, but the analysis (lines 161-163) is somewhat superficial. The paper notes that far OOD yields lower GM (more robust) but does not explore why — e.g., whether far OOD data is simply easier for the model to ignore, has simpler features, or triggers different failure modes. A more mechanistic discussion would strengthen this experiment.

### Trivial

- The paper uses the notation $\sigma_g$ on line 128 where Definition 1 uses $\delta_g$. Minor inconsistency.
- Some figure references (e.g., Figure 3 on line 166) appear before Table 6 (line 176) without clear ordering in the extracted text, though this may be a parser artifact.

## Nice-to-Haves

- A concrete example where the prior confounded evaluation would suggest harm while RE-SSL shows no harm or benefit would dramatically strengthen the claim that the confound matters in practice.
- Justifying $\delta_g$ via practical significance (e.g., "a slope of $-0.02$ corresponds to at most a 2% accuracy drop at $r=1$, which is negligible in deployment") would resolve the arbitrariness concern.
- Reporting standard deviations or individual seed results in an appendix.
- A brief sensitivity analysis comparing $R_{slope}$ results to a non-parametric trend measure (e.g., average derivative) would address the linearity concern transparently.

## Removed Points

*These points are flagged to be removed — treat them with caution.*

- **Criticism that the SCM is "not used analytically" (Harsh Critic, Other Observations).** The paper presents the SCM in Figure 1 as a conceptual motivation for the confounding issue, not as a causal inference framework requiring do-calculus. This is appropriate for an evaluation/benchmark paper. The paper does not over-promise on this front, and the criticism is a mismatch of expectations.

- **Demand for additional datasets (CIFAR-only limitation).** CIFAR10 and CIFAR100 are the standard evaluation benchmarks in SSL research. Expecting ImageNet-scale evaluation is a scope-creep demand that does not match standard practice in this subfield.

- **"Modest novelty of the core empirical finding" treated as a major weakness (Harsh Critic, Point 2).** While individual SSL methods (e.g., MixMatch, ICT) were previously known to handle unseen classes reasonably well, the paper's contribution is the *systematic multi-factor evaluation framework* and the *corrected experimental design* — not just the headline finding. The reviewer's critique conflates "some methods are robust" with "the systematic analysis of 15 methods across 5 factors using a corrected protocol is novel." The latter remains a meaningful contribution. The criticism is kept but downgraded to minor.

## Novel Insights

The reviewers collectively surface a productive tension: the paper's core methodological critique (prior evaluations confound seen-class and unseen-class variation) is well-founded and important, yet the paper's own threshold-dependent robustness classification ($\delta_g = -0.02$) introduces a different kind of arbitrariness. This suggests that the field's real need may not be a single "robust vs. non-robust" binary per method, but rather relative rankings across multiple metrics (GM, $F_{avg}$) that do not require threshold choices. The paper's own Table 6 is arguably its strongest contribution precisely because it avoids threshold-based dichotomies. A second insight from the cross-review: the paper's value proposition shifts substantially depending on framing — if positioned as "correcting a flaw in prior work," the bar for novelty is higher and invites pushback; if positioned as "providing a complementary, more granular evaluation protocol," the contribution is cleaner and harder to dispute. The paper as written straddles these two framings uneasily.

## Suggestions

1. **Reframe the critique of prior work.** Acknowledge that prior evaluations answered a different (but also valid) question, then position RE-SSL as a complementary design that isolates the marginal effect of unseen classes. This makes the paper more constructive and reduces unnecessary pushback without weakening the contribution.

2. **Either justify $\delta_g$ or deprecate it.** If the threshold is retained, provide a practical rationale (e.g., "a slope $\geq -0.02$ corresponds to less than 2% accuracy loss at full unseen-class contamination, which is negligible in most deployment scenarios"). Better yet, foreground relative rankings (GM, $F_{avg}$) and use the threshold-based classification only as supplementary material.

3. **Add variance information.** Report standard deviations for at least the main results (Tables 1-2) or provide individual seed results in a supplement. This would substantially improve the paper's scientific rigor.

4. **Acknowledge the linearity assumption** behind $R_{slope}$ and note that GM is the assumption-free alternative. A brief sensitivity check comparing $R_{slope}$ rankings to those from GM would strengthen confidence in the conclusions.

5. **Deepen the nearness analysis.** The MNIST vs. CIFAR comparison is interesting but under-analyzed. A few additional sentences speculating on *why* far OOD yields greater robustness (e.g., feature-level separability, model's ability to ignore simpler data) would add value.

## Score and Decision

**Score:** 6.5/10 — a solid paper with a valid methodological contribution and extensive experiments. The weaknesses are real but fixable and do not invalidate the core claims.

**Decision:** Accept

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>