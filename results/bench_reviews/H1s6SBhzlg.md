Here is my consolidated final review:

---

## Summary

This paper studies aggregation of answers from multiple LLMs, proposing two algorithms: Optimal Weight (OW) — a weighted linear aggregator proven Bayes-optimal under conditional independence — and Inverse Surprising Popularity (ISP) — a second-order method that provably outperforms majority voting (MV) in expectation. The theoretical framework cleanly categorizes aggregation methods by information order (zero/first/second) and provides closed-form expressions for ISP's advantage over MV (Theorem 2) and a finite-sample bound (Theorem 3). Experiments on simulated data, UltraFeedback, MMLU, and a healthcare dataset (ARMMAN) show that the proposed methods often beat MV.

## Strengths

1. **Principled theoretical hierarchy.** The paper formalizes LLM aggregation as an information aggregation problem with clear zero/first/second-order categories, providing a useful conceptual framework for the community.

2. **Bayesian optimality result (Theorem 1).** Proving that OW with weights \(\sigma_K^{-1}(x_i)\) is the Bayes-optimal aggregator under conditional independence is a genuine theoretical contribution, and Corollary 1 connecting the optimal weights to the Bradley-Terry model offers principled justification for BT-style weighting in LLM aggregation.

3. **Closed-form expected advantage of ISP over MV (Theorem 2).** The exact analytic expressions for \(\mathbb{E}[\mathrm{Adv}_{\mathrm{ISP}}(s^*) - \mathrm{Adv}_{\mathrm{MV}}(s^*)]\) are elegant and provide interpretable insight into when and why ISP should outperform MV (e.g., the gap shrinks as \(K\) increases, and vanishes when agents are near-random).

4. **Theoretical explanation for SP's underperformance.** The paper formally shows that MV outperforms SP in expectation in the LLM setting (Theorem 2), and provides a clear intuitive explanation: LLMs lack the systematic biases that SP exploits in human crowds — a genuinely useful insight for the community.

5. **Empirical validation on diverse real-world tasks.** The paper evaluates on three distinct datasets (preference data in UltraFeedback, multi-choice QA in MMLU, and a real healthcare application in ARMMAN) and demonstrates consistent improvements over MV across all settings.

## Weaknesses

### Fatal

- **Unexplained identical results for OW-L and OW-I across all three datasets.** In Table 3, OW-L and OW-I report *exactly* the same accuracy on UltraFeedback (73.66%), MMLU (90.37%), and ARMMAN (85.78%). In Table 4, the per-question discrepancy counts are also identical across all three datasets (2545/1727, 1821/659, 264/195). OW-L estimates accuracies by empirical risk minimization on second-order information (Equation 7), while OW-I uses ISP-derived pseudo-labels — these are fundamentally different estimation procedures. The chance that two different pipelines produce identical accuracy numbers *and* identical per-question decision patterns across three heterogeneous datasets is essentially zero without either a bug, a mathematical equivalence that the paper does not discuss, or an evaluation error. The paper offers no explanation for this finding. This undermines the credibility of the entire real-world experimental evaluation — the central empirical evidence for the paper's claim that "our methods consistently outperform majority voting." Without resolution, the experimental results cannot be trusted.

### Major

- **Core theoretical results rely on conditional independence (Assumption 1), which is acknowledged to be unrealistic for LLMs, with no robustness analysis in the main text.** The paper states that "this assumption may not hold perfectly in the LLM setting" (line 67) and defers extensions to Appendix C (not visible in the main text). However, Theorems 1, 2, and 3 are all derived under this assumption. Given that LLMs share training data, architectures, and reasoning patterns, correlated errors are the norm. While the simulated experiments satisfy the assumption, the real-world experiments — which could serve as a robustness check — are compromised by the OW-L/OW-I issue above. This decouples the theory (which needs the assumption) from the experiments (which should test robustness to its violation), weakening the paper's overall narrative.

- **The comparison to baselines is narrow.** The paper compares only against MV and SP. Standard aggregation baselines such as soft voting (weighted by confidence scores), stacking, or simple averaging of output probabilities (when available) are not included. The text acknowledges accuracy estimation noise as a challenge but does not compare against the clairvoyant optimal (OW with true accuracies) in real data, making it hard to assess how much of the theoretical advantage survives estimation error.

### Minor

- **The finite-sample bound (Theorem 3) uses the vague notation "≳" and suppresses logarithmic factors.** The bound shows that the advantage degrades at rate \(\tilde{O}(\sqrt{\frac{1}{M}\log(1/\delta)})\), but the paper does not investigate at what sample size \(M\) the bound becomes non-vacuous relative to the practical dataset sizes used in experiments. This would help understand when ISP's theoretical advantage is empirically attainable.

- **The random label shuffling step is claimed to be "without information loss" (Appendix B.1) under certain conditions, but the paper does not empirically compare performance with and without shuffling.** While the paper assumes LLMs are insensitive to ordering (citing Guo & Vosoughi, 2024), this is a debated finding and may not hold for all models and tasks.

- **Agent diversity is limited.** All main experiments use \(N=4\) agents (the strongest model from each of 4 families). While 16 combinations are mentioned, the detailed breakdown is relegated to the appendix. The paper does not explore how ISP's advantage scales with group size (e.g., \(N=2, 8, 16\)).

### Trivial

- The "≳" notation in Theorem 3 is imprecise for a formal statement and should be replaced with an explicit bound or big-O notation with a clear constant.
- The paper's abstract claims "Across all cases, our methods consistently outperform majority voting," which is slightly too broad given the small number of datasets and the unresolved identical-results issue.

## Nice-to-Haves

- An ablation study with simulated correlated errors (violating Assumption 1) would demonstrate the robustness of OW and ISP, bridging the gap between theory and practice.
- Varying the number of agents \(N\) and the dataset size \(M\) experimentally would make the empirical evaluation more informative about when each method is preferable.
- A scatter plot comparing estimated vs. true accuracies in OW-L (on simulated data) would help assess how well the learning pipeline recovers the true first-order information.

## Removed Points

These points were flagged by reviewers but are removed or weakened per the meta-review guidelines:

- **Missing related works, e.g., "standard ensemble methods" beyond the paper's scope.** The paper explicitly discusses related work in Section 1.1 and Appendix A.1, and requesting specific additional citations would require external knowledge to verify.
- **"The future directions are generic."** Criticizing a conclusion section for being generic is a minor presentation issue that does not affect the paper's contribution.
- **Request for experiments on open-ended generation tasks.** The paper scopes itself to multiple-choice aggregation; extending to freeform text is outside the stated scope.
- **"The paper overstates the novelty: aggregation with weights based on accuracy is classic."** This conflates the general concept of weighted aggregation with the specific Bayes-optimal weighting scheme derived in Theorem 1, which is novel.
- **Formatting/style nitpicks and comments about reproducibility trivia.** None of the reviewer's comments about missing hyperparameters or trivial implementation details are retained.
- **Complaints that the Appendix C extension is "not reviewed here."** This is a structural observation about where content is placed, not a factual error, and is subsumed by the main Major weakness on conditional independence.
- **Criticism about "the paper does not discuss limitations" (e.g., computational cost).** The paper discusses practical estimation challenges in Section 4.3 and estimation noise in Section 5.2. This is a generic critique.

## Novel Insights

The reviews collectively surface a deeper tension in the paper that extends beyond the individual weaknesses. The paper attempts to simultaneously satisfy two goals: (1) providing a theoretically principled framework for LLM aggregation grounded in classical information aggregation theory, and (2) delivering practical, label-free methods that work on real LLM outputs. The conditional independence assumption perfectly illustrates this tension — it is standard in the information aggregation literature (where it has a natural justification from independent signal structures) but almost certainly violated in the LLM setting. The paper's honest acknowledgment of this violation is commendable, but the resulting gap between the theory (which requires the assumption) and the experiments (which should demonstrate robustness to its violation) is never properly bridged. The identical OW-L/OW-I results suggest that the experimental pipeline may have deeper issues that prevent it from serving as a convincing validation of the theory. A more impactful version of this paper would either (a) develop the theory under weaker assumptions (e.g., bounded correlation), or (b) provide rigorous empirical evidence — including error bars, broader baselines, and ablation studies — showing that the methods work despite assumption violations.

## Suggestions

1. **Investigate and explain the identical OW-L and OW-I results.** This is the single most important issue. If the results are correct, the paper must explain why two fundamentally different estimation procedures yield identical outputs — even a mathematical proof of equivalence under certain conditions would suffice. If there is a bug, correct the results and re-evaluate all claims. If the methods are genuinely equivalent on this data, state this explicitly.

2. **Address the conditional independence gap in the main text.** At minimum, include a robustness simulation where agents have correlated errors (e.g., via a shared latent factor) and show that OW and ISP still outperform MV despite the assumption violation. This would make the paper self-contained.

3. **Expand baselines.** Add soft voting (weighted by model confidence or estimated accuracy) and, where possible, compare against the clairvoyant OW with true accuracies as an oracle upper bound.

4. **Add error bars or confidence intervals.** Especially for the simulated experiments, multiple random seeds would give a sense of variance. For real datasets, the paired t-test is a start, but bootstrapped confidence intervals would be more informative.

## Score and Decision

### Calibration Anchors

| Path | Avg Human Score | Comparison |
|------|----------------|------------|
| `gDxJK8yvZU.md` (Minimax-Optimal Aggregation for DRE) | 7.50 | Stronger paper — tight theory with minimax optimality and thorough experiments with no red flags. Current paper has weaker experiments. |
| `VtN1z92lvu.md` (Decision Aggregation under Quantal Response) | 6.67 | Stronger paper — clean theory plus convincing LLM experiments. Current paper's theory is comparable but experiments are compromised. |
| `x85kiYqL4y.md` (Optimal Aggregation of LLM and PRM Signals) | 5.00 | Comparable in theory quality but that paper's experiments, while limited, had no unexplained artifacts. Current paper has more ambitious theory but a fatal experimental flaw. |
| `f6mDQ7zl4t.md` (RL for solution aggregation) | 4.80 | This paper and the current one are structurally different, but both have limitations that prevent acceptance. The current paper has stronger theory but worse experimental credibility. |
| `Ug1R40CH8Y.md` (RL for Generalized Label Aggregation) | 4.50 | Both papers have interesting ideas undermined by experimental concerns. The current paper has stronger theoretical results but more severe experimental issues. |
| `UKPDpKGXAi.md` (EEG temporal confound) | 2.00 | Not directly comparable — this is a replication study. The current paper is substantially stronger in theoretical contribution. |

The paper has genuine theoretical contributions — the Bayesian optimality proof, closed-form advantage expressions, and the ISP derivation are all solid. However, the identical OW-L/OW-I results across all three datasets constitute a fatal experimental flaw that undermines the central empirical claims. The paper cannot be accepted in its current form. Against the calibration anchors, this paper is weaker than the accepted papers at score 5–6, which had either cleaner experiments or no experimental credibility issues. It is stronger than rejected papers at the 4–5 level in terms of theoretical ambition, but the experimental problem pushes it below the acceptance threshold.

MY FINAL SCORE: <pineapple>3.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>