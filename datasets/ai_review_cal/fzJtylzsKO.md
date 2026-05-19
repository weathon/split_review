- Decision: Reject
- Avg Score: 4.00
- Scores: 5, 5, 3, 3
Now I have a thorough understanding of the paper and the reviewer claims. Let me compose the consolidated review.

## Summary
The paper proposes qPO (multipoint Probability of Optimality), a batch acquisition function for discrete Bayesian optimization. qPO maximizes the probability that the acquired batch contains the true global optimum, and this batch-level objective decomposes into a sum of individual acquisition scores, avoiding combinatorial optimization. The paper shows analytically how qPO captures diversity through model covariance (distinguishing it from parallel Thompson sampling) and demonstrates competitive empirical performance on two molecular discovery tasks.

## Strengths
- **Additivity of the batch acquisition function (Eq. 4, Section 2.2)**: The batch-level objective is exactly the sum of per-candidate probabilities of optimality, so optimal batch selection reduces to picking the top-\(k\) candidates by individual score. This avoids the combinatorial optimization required by qEI, qUCB, and other batch methods. (Lines 75–88, 101–106)
- **Analytical differentiation from parallel Thompson sampling**: The toy example (Eq. 6, Section 3.2) concretely demonstrates that qPO selects diverse, uncorrelated candidates \((x_1, x_3)\) while pTS tends to select correlated pairs \((x_1, x_2)\), providing mechanistic insight into how covariance drives diversity without randomness or heuristics. (Lines 183–208)
- **Empirical performance on two realistic tasks**: On the antibiotic discovery task (Fig. 2), qPO achieves the best average performance across all six reported metrics. On the QM9 task (Fig. 3), qPO matches or slightly outperforms the strongest baseline (qEI). Results are averaged over ten runs with error bars. (Lines 226–256)
- **Diversity analysis validating the implicit-diversity claim**: Fig. 4 visualizes batch compositions from one iteration and confirms that qPO and pTS produce the most structurally diverse batches, while UCB produces the least diverse, supporting the claim that model covariance drives diversity in qPO. (Lines 237–245)

## Weaknesses
### Fatal
None.

### Major
- **Candidate preselection step is not fully controlled in the main evaluation.** The paper reduces candidates to 10,000 using an undefined "greedy metric" (Line 221) before applying the acquisition function. If this metric selects by high predicted mean, it enriches the candidate pool for exploitative selections, potentially favoring qPO. The paper acknowledges this concern and includes a "random10k" baseline (Line 222), but **the results of this baseline are not shown in any main figure**. Without seeing whether qPO's advantage persists above random selection from the same preselected pool, the reader cannot fully assess whether the method's reported performance is driven by the acquisition function itself or by the preprocessing pipeline. The results may appear in the appendix (stripped during parsing), but the main paper should present this key control prominently.

### Minor
- **Derivation in Eqs. (2)–(3) is mathematically imprecise.** The paper writes \( \Pr(\text{optimum} \in \text{batch}) = \sum_i \Pr(x^* = x_i \mid \{x_j \neq x^*\}_{j\neq i}) \) (Eq. 2) and then claims mutual exclusivity reduces this to \( \sum_i \Pr(x^* = x_i) \) (Eq. 3). The conditional probability in Eq. 2 is not equal to the marginal in general, and the step from (2) to (3) is not a logical consequence of the stated reasoning. The correct derivation is simpler: because the events \( \{x^* = x_i\} \) are mutually exclusive, \( \Pr(\text{optimum} \in \text{batch}) = \sum_{i\in\text{batch}} \Pr(x^* = x_i) \) directly. The conclusion is correct, but the presentation as-is will confuse readers. (Lines 75–84)
- **No direct evaluation of the stated objective.** The acquisition function maximizes the probability that the batch contains the *single true global optimum*, yet the evaluation focuses entirely on top-\(k\) retrieval metrics (fraction of top 0.01%, 0.5%, 1%, etc.). While top-\(k\) metrics (especially small \(k\)) are reasonable proxies and the paper notes the connection (Line 266: "consistent with the acquisition strategy's goal"), a direct metric—fraction of runs where the single true global optimum is acquired within the batch—would directly validate the stated goal. The absence of this metric creates a gap between the theoretical objective and the empirical evidence.
- **Computational cost is partially acknowledged but not evaluated.** The paper mentions the \(O(N^3)\) cost of Cholesky decomposition and reduces candidates to 10,000 to manage this (Line 221), and notes that the method cannot be computed analytically (Line 269). However, no wall-clock times, memory usage, or runtime comparisons with baselines are provided. The reader cannot judge whether the trade-off between qPO's simplicity and its numerical cost is worthwhile in practice.

### Trivial
- The "greedy metric" used for candidate reduction (Line 221) is not defined in the main text (though it is referenced to the appendix via `\ref{sec:experiment_details}`). A one-sentence description in the main text would improve readability.

## Nice-to-Haves
- A direct optimum-recovery metric (fraction of runs where the single true global optimum is acquired) would close the gap between the stated theoretical objective and the empirical evaluation.
- A runtime/wall-clock comparison between qPO and the cheapest baseline (e.g., UCB or greedy) would help calibrate the practical trade-off.
- A sensitivity analysis for the number of Monte Carlo samples (\(M=10{,}000\)) and the candidate reduction threshold (\(10{,}000\)) would strengthen the paper.
- A synthetic experiment with controlled observation noise could characterize when the method breaks down, as noted in the limitations (Lines 270–273).

## Removed Points
*These points are flagged to be removed; treat them with caution.*
- **Undefined greedy metric in the main text (from Harsh Critic's Critical Issue 1)**: The critic argues the greedy metric is "never described" — but the paper explicitly states that experimental details are in the appendix (Line 222: `\ref{sec:experiment_details}`), which was stripped during parsing. This is a presentation issue, not an omission.
- **"More thorough baseline implementation details"**: The critic asks for qEI implementation details and UCB hyperparameter \(\beta\). The paper states experimental details are in the appendix, where such information is standard.
- **"Hyperparameter sensitivity"**: The critic calls \(M=10{,}000\) and the candidate reduction threshold "arbitrary" and requests sensitivity studies. This is a reasonable suggestion for future work but not a flaw; the paper notes (Line 123) that candidates with high probability of optimality are likely to appear in the batch even with modest \(M\).
- **Criticism about computational cost being "entirely unaddressed"** / The critic's specific claim that Cholesky alone costs \(O(10^{12})\) flops: The paper acknowledges the \(O(N^3)\) cost (Line 221) and describes the candidate reduction mitigation. The critic's framing as "entirely unaddressed" is an overstatement.

## Novel Insights
None beyond the paper's own contributions. Both reviews surface the same substantive concern (preselection control) and the same mathematical imprecision; no novel synthesis emerges beyond what the paper itself provides.

## Suggestions
- Add the random10k baseline results to the main figures (or a supplementary figure in the main paper) so readers can directly assess whether qPO's performance is an artifact of the preselection pipeline.
- Replace Eqs. (2)–(3) with a clean, direct derivation: because events \(\{x^* = x_i\}\) are disjoint, \(\Pr(\text{optimum} \in \text{batch}) = \sum_{i\in\text{batch}} \Pr(x^* = x_i)\).
- Add one panel or table reporting the fraction of runs where the single true optimum is acquired by each method.
- Report wall-clock time per BO iteration for qPO and at least one baseline (e.g., UCB or qEI) to help readers gauge practical feasibility.
