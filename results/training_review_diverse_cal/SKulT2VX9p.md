Now I have all the information needed. Let me produce the consolidated review.

## Summary

This paper addresses the limitation of existing causal fairness methods that assume a fully known causal DAG. It proposes a framework for achieving interventional fairness using a maximally partially directed acyclic graph (MPDAG), which can be obtained from observational data and background knowledge but does not require a fully specified DAG. The paper makes three main contributions: (1) a modeling technique proving that augmenting an MPDAG with a predictor node \(\hat{Y}\) yields another MPDAG (Theorem 1), enabling formal causal inference; (2) an identification condition and formula for interventional fairness criteria on MPDAGs (Proposition 1); and (3) a constrained optimization framework (\(\epsilon\)-IFair) that balances accuracy and fairness with a tunable trade-off. The approach is validated on synthetic DAGs of varying size and on two real-world datasets (UCI Student, Credit Risk).

## Strengths

- **Theorem 1 — Augmented MPDAG preservation is a genuine theoretical contribution.** The paper formally proves that adding a predictor node \(\hat{Y}\) (modeled as a function of all observable variables) to an MPDAG \(\mathcal{G}\) yields another MPDAG \(\mathcal{G}^*\) consistent with the given background knowledge (Section 4.1). This result is nontrivial and enables rigorous causal inference on partially known graphs, directly addressing the paper's core goal of relaxing the fully-known-DAG assumption.

- **Proposition 1 gives a principled, testable identification condition.** The necessary and sufficient condition (no undirected edge between intervention set and remaining variables) and the closed-form identification formula (lines 228–244) provide a clear criterion practitioners can verify before applying the method. This moves beyond opaque "identifiability assumed" statements common in the literature.

- **Constrained optimization with tunable trade-off is practically valuable.** The formulation (\(\epsilon\)-approximate interventional fairness, Definition 2, Equation (1)) replaces the rigid "use only definite non-descendants" baseline (IFair, Lemma 1) with a flexible Pareto-style approach, allowing practitioners to navigate the accuracy–fairness trade-off via hyperparameter \(\lambda\). The synthetic experiments (Figures 3, 4) demonstrate that for appropriate \(\lambda\), the method achieves fairness comparable to IFair while retaining accuracy comparable to the Full model.

- **Honest scope discussion.** Section 4.4 clearly states that the method applies to interventional fairness but not yet to path-specific or counterfactual fairness, which is a responsible handling of the method's current limits.

## Weaknesses

### Fatal
None.

### Major

- **Real-data evaluation lacks independent ground truth and the limitation is not acknowledged.** For real datasets (UCI Student, Credit Risk), interventional data are generated from the *same* fitted conditional densities used by the predictor model, creating a circular evaluation: the fairness numbers confirm the optimization was solved, not that predictions are fair in reality. The synthetic experiments (with known ground-truth SCM) provide valid validation of the method, but the real-data results are presented without qualification. The paper should explicitly discuss this limitation and what would be required for meaningful real-data validation (e.g., randomized experiments, sensitivity analysis over plausible alternative MPDAGs). This does not invalidate the core theoretical contributions, but it weakens the claim of empirical effectiveness.

### Minor

- **Construction of MPDAGs for real datasets is not explained.** The paper states "Our experiments are carried out on the MPDAG \(\mathcal{G}\) in Figure 4" (Student data) and "based on the MPDAG \(\mathcal{G}\) in Figure 5" (Credit Risk) without describing how these MPDAGs were obtained — whether through causal discovery, domain knowledge, or both. The figures exist in the original paper but the text provides no summary of the graph structure or justification of the choices. This is a reproducibility gap that should be addressed.

- **Non-identification case is discussed but not implemented or evaluated.** Section 4.2 ("Dealing with non-identification," lines 249–251) briefly proposes averaging unfairness over valid orientations of offending undirected edges, but gives no algorithm, theoretical justification, complexity analysis, or experimental validation. Since all experiments use settings where identification holds, the paper effectively scopes itself to identifiable cases. This is acceptable, but the text should be clearer that the averaging approach is a suggestion for future work, not a validated component of the method.

- **MMD kernel and hyperparameters are unspecified.** The paper uses Maximum Mean Discrepancy to measure distributional unfairness (line 256) but does not specify which kernel was used or how the bandwidth was selected. Since MMD results can be sensitive to these choices, this omission affects reproducibility.

- **No sensitivity analysis to MPDAG errors.** The entire framework assumes the MPDAG contains the true DAG. While this is the standard assumption in causal inference with equivalence classes, the paper's motivation emphasizes that real-world graphs are only partially known. A simple synthetic experiment (e.g., systematically omitting or reversing background knowledge to test how degradation occurs) would have meaningfully strengthened the demonstration of practical utility.

### Trivial

- **The paper uses conditional multivariate normal distributions for \(f(\mathbf{v}_i \mid pa(\mathbf{v}_i, \mathcal{G}))\)** (line 256). This is a parametric assumption, but the paper acknowledges "other conditional density estimation approaches can also be employed." For synthetic data (linear Gaussian) this is consistent; for real data the adequacy is not checked. A minor limitation worth noting.

- **IFair baseline's dependence on identifiability is not explicitly verified in all settings.** The footnote (line 272) explains the condition, and the paper correctly notes IFair is inapplicable for Credit Risk (no non-descendants of Age). For the Student dataset the condition is not explicitly confirmed, but this is a minor point about a baseline rather than the main method.

## Nice-to-Haves

- A pseudo-code summary of the optimization algorithm (sampling from fitted conditionals, MMD computation, neural network training loop) would improve reproducibility.
- Practical guidance on selecting \(\lambda\) (e.g., choose largest \(\lambda\) achieving a target RMSE on a validation set) would increase usability.
- A synthetic experiment with perturbed MPDAGs (missing/reversed background knowledge) to test robustness would strengthen the practical claims.
- For real datasets, reporting whether the identification condition holds (no undirected edges between treatment set and complement) would clarify the method's practical scope.

## Removed Points

- **Criticism that figures (Figures 4, 5 for real-data MPDAGs) are "not described in the text."** These figures are image-based and exist in the original PDF but were not extractable by the text parser. The core concern about *how* the MPDAGs were constructed is kept (see Minor weaknesses above); the complaint about missing figure descriptions is a parser artifact.
- **Criticism that the optimization procedure is not reproducible (exact loss function, gradient computation).** The loss function is given in Equation (1), and the sampling procedure from fitted conditionals is described (lines 255–256, 288–290). The level of detail is standard for a conference paper of this type and is not a structural flaw.
- **Criticism about the parametric assumption (multivariate normal).** The paper already acknowledges alternatives. This is a minor observation, not a weakness requiring action.
- **Criticism about the IFair baseline identifiability.** For synthetic data, identifiability is explicitly ensured (line 286: "background knowledge that is necessary to identify fairness"). The concern is partially correct for Student data but is about a baseline, not the main method.

## Novel Insights

The reviews identify a genuine tension in the paper: the method is theoretically elegant (Theorem 1 + Proposition 1 form a clean pipeline for moving from a partially known graph to a fairness-constrained predictor), but the empirical evaluation on real data cannot escape the fundamental challenge that causal ground truth is unobservable. The most interesting open question raised by the reviews is whether the real-data experiments could be redesigned to avoid circularity — for instance, by using a holdout dataset with known intervention outcomes, or by evaluating fairness claims through domain-expert validation of the MPDAG structure rather than through the generated interventional samples alone. The paper's theoretical apparatus could support such designs, but the current evaluation does not execute them.

## Suggestions

1. **Acknowledge the circularity of real-data evaluation explicitly** and discuss what would constitute a non-circular validation (domain-expert-reviewed MPDAG, sensitivity analysis, or use of datasets with known interventional data).
2. **Describe how the real-data MPDAGs were constructed** — which features were included, what background knowledge or causal discovery algorithm was used, and what the resulting structure looks like (even a brief textual summary or adjacency list).
3. **Specify the MMD kernel and bandwidth selection method** for reproducibility.
4. **Clarify the scope of the non-identification handling** — either implement and validate it, or clearly state that the paper addresses only identifiable cases and relegate the averaging suggestion to future work.

## Score and Decision

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>