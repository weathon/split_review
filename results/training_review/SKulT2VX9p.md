Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper proposes a framework for achieving interventional fairness when the causal graph is only partially known, represented as a maximally partially directed acyclic graph (MPDAG). The contributions are: (i) modeling the predictor as a child of all observed variables, proving the resulting augmented graph remains an MPDAG (Theorem 1); (ii) adapting identification results from the causal inference literature to express the interventional fairness constraint in terms of observable densities (Proposition 1); and (iii) formulating a constrained optimization problem with an ε-approximate fairness penalty that trades off accuracy and fairness. Experiments on synthetic linear-Gaussian data and two real datasets are presented.

## Strengths

- **Relaxes the fully-known DAG assumption by working with MPDAGs.** Most prior causal fairness methods assume access to the true causal DAG. This paper targets the more realistic setting where only an equivalence class (MPDAG) is available, learned from data and domain knowledge. This is a well-motivated and practically important direction.

- **Theorem 1 (augmented MPDAG) is a clean theoretical contribution.** Proving that adding a deterministic prediction node as a child of all observed variables preserves the MPDAG structure is nontrivial and may be of independent interest for other causal inference problems on MPDAGs. It enables rigorous reasoning about interventional distributions on the augmented graph.

- **Proposition 1 provides identification conditions adapted to the fairness setting.** The paper correctly adapts existing MPDAG identification results (Perković et al.) to express the interventional fairness constraint in closed form using observable conditional densities, making the constrained optimization problem computationally tractable.

- **The ε-approximate fairness formulation with a tunable λ is principled.** The constrained optimization framework (Eq. 2) directly connects the interventional fairness definition to a differentiable objective, allowing explicit control over the accuracy–fairness trade-off, which the experiments show can be effective.

## Weaknesses

### Fatal
None.

### Major

- **The paper never tests robustness to MPDAG misspecification — the central practical challenge it claims to address.** The entire motivation is that the true causal DAG is unknown and only an MPDAG is available. Yet in the synthetic experiments, the CPDAG is derived directly from the true DAG (Section 5.1: "As the simulated DAG is known, the CPDAG can be obtained from the true DAG without running the causal discovery algorithms"), and background knowledge is drawn from the true DAG's edges. This bypasses the primary source of error that the paper's framing emphasizes: real causal discovery from finite samples will produce an MPDAG that may be incorrect (missing edges, wrong orientations). The paper provides a brief footnote appealing to "ample sample size" but no analysis, sensitivity experiment, or even discussion of what happens when the MPDAG contains errors. Since the fairness guarantees depend entirely on the correctness of this graph, the practical usefulness of the method for the stated problem is unsubstantiated.

- **Experiments lack statistical rigor.** The synthetic results report average RMSE and unfairness over 10 random graphs but provide no error bars, confidence intervals, standard deviations, or any measure of variance. The reader cannot assess whether the observed trade-off improvements of ε-IFair over baselines are reliable or due to chance. This is a basic expectation for reproducibility-oriented experimental reporting.

- **Real-data MPDAG construction is not described.** The paper references MPDAG figures for the UCI Student and Credit Risk datasets (Figures referenced at lines 345 and 376) but provides no explanation of how these MPDAGs were obtained — whether from expert knowledge, causal discovery algorithms, or a combination. This makes the real-data experiments unreproducible and prevents assessment of whether the MPDAGs are plausible.

### Minor

- **Experiments are limited to a best-case scenario.** The synthetic data uses linear Gaussian structural equation models with Gaussian conditional density estimation — an ideal case for the Gaussian approximation employed. Nonlinear SEMs, heteroscedastic noise, or non-Gaussian conditionals are not tested. The paper also focuses exclusively on the empty admissible set (line 269), leaving the handling of non-empty admissible sets unevaluated.

- **Limited scope of real-data evaluation.** Only two real datasets are used, with no comparisons to any existing interventional fairness methods from the literature (only the authors' own baselines Full, Unaware, and IFair). While the baselines are appropriate for the paper's framing, a comparison to e.g., an adaptation of Zuo et al. (2022) or a DAG-based interventional fairness approach would help position the contribution. The UCI Student test set contains only 19 and 20 interventional data points — the paper acknowledges this limitation but still presents the test-set trade-off plots as primary evidence.

- **Non-identification handling is discussed but never implemented.** The "Dealing with non-identification" paragraph (line 249) sketches an averaging strategy over possible MPDAG orientations, but this is not implemented or tested in any experiment. This gap is notable because non-identification may occur in practice and the proposed remedy is unvalidated.

- **Deterministic predictor versus sampling-based evaluation.** The paper models \(\hat{Y} = h_\theta(\mathbf{x}, \mathbf{a})\) as a deterministic function of the inputs, yet the fairness estimation procedure samples from \(f(\hat{y}|\mathbf{v})\) via Monte Carlo using MMD. While not contradictory, the paper could be more explicit about how the deterministic nature of the predictor interacts with the density estimation and Monte Carlo integration.

### Trivial

- The λ grid for synthetic experiments is relatively coarse ([0, 0.5, 5, 20, 60, 100]) and no analysis of the sensitivity of the trade-off to the choice of λ is given.

## Nice-to-Haves

- A sensitivity analysis where the MPDAG is deliberately perturbed (edge deletions, wrong orientations) to measure degradation in fairness and accuracy would substantially strengthen the paper's claim of handling "partially known" graphs.
- Adding error bars to all reported experimental results.
- Describing how the real-data MPDAGs were obtained (causal discovery algorithm, expert knowledge, or both) would make the experiments reproducible.
- Testing non-linear SEMs and non-empty admissible sets would broaden the evaluation.

## Removed Points

These points are flagged to be removed; treat them with caution:

1. **Criticism about IFair baseline being under-defined due to missing theorem reference.** The harsh critic claimed that the "definite non-descendants" concept and the referenced theorem (\cref{theo: definite ancestral relationship}) do not appear in the text. Per instructions, the parser strips appendix/supplementary material from all papers; these sections exist in the original submission. The Lemma 1 (line 94) already provides the core idea: a function of X_ad and non-descendants of A is interventionally fair.

2. **Criticism that Lemma 1 fails to condition on X_ad for non-empty admissible sets.** The lemma explicitly states: "if it is a function of the admissible set X_ad and non-descendants of A" — it already conditions on X_ad. The critic misread the lemma.

3. **Criticism that the paper's "no selection bias, no latent confounders" assumption is "not revisited in the conclusion."** The conclusion (line 402) explicitly states: "The limitation of this work is that it assumes no selection bias or latent confounders." The assumption is also stated clearly in the introduction and the paper acknowledges it as a limitation.

4. **Formatting/style nitpicks, and any criticisms about "missing appendix" or "missing proofs."** These are parser artifacts.

5. **Strength Finder's claim that the evaluation is "comprehensive."** This conflicts with verified weaknesses (no error bars, no robustness tests, limited datasets, no external baselines). The evaluation has significant gaps, so calling it "comprehensive" is inaccurate.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a new perspective that the paper itself does not already articulate.

## Suggestions

1. **Add robustness experiments against MPDAG misspecification.** This is the single most important addition. Randomly flip/delete/add edges to the MPDAG and measure degradation in fairness guarantees and accuracy. Without this, the paper's central claim — that it handles partially known graphs — is untested in the regime where the partial knowledge is imperfect.

2. **Report error bars** (standard deviations or confidence intervals) for all experimental results, especially the synthetic trade-off plots over the 10 random graphs.

3. **Describe how the real-data MPDAGs were obtained** (discovery algorithm? expert knowledge? both?) to enable reproducibility.

4. **Consider at least one comparison to an existing causal fairness method** that assumes a fully known DAG, to quantify the cost of partial knowledge and empirically motivate the MPDAG setting.

5. **Implement and evaluate the non-identification handling** (averaging over possible MPDAGs) on at least one synthetic scenario where identification fails, to demonstrate that the proposed remedy works.

## Score and Decision

The paper makes a real theoretical contribution — the augmented MPDAG result (Theorem 1) and the adaptation of identification conditions to the fairness setting (Proposition 1) are technically sound and address an important problem. However, the experimental evaluation has a critical gap: it never tests robustness to errors in the MPDAG, which is the central practical challenge the paper claims to address. The CPDAG is derived from the true DAG in synthetic experiments, bypassing the causal discovery errors that motivate the work. Combined with the lack of error bars, opaque real-data MPDAG construction, and limited scope of evaluation, the empirical support for the method's practical effectiveness is insufficient. The theoretical core is promising, but the paper as submitted does not substantiate its central claim that interventional fairness can be reliably achieved when the causal graph is only partially known (and therefore potentially incorrect). Major revisions are needed.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>