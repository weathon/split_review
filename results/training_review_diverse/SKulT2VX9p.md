Now I have a thorough understanding of the paper. Let me write the consolidated review.

## Summary

This paper addresses the problem of achieving interventional fairness when the causal graph is only partially known (specifically, as a maximally partially directed acyclic graph, or MPDAG). The authors propose: (1) a modeling technique where the predictor Ŷ is treated as a child of all observed variables, proving that the augmented graph remains an MPDAG (Theorem 1); (2) an analysis of identification conditions for the interventional effect P(ŷ | do(A), do(X_ad)) on MPDAGs (Proposition 1); and (3) a constrained optimization framework (ε-IFair) that balances unfairness (measured via MMD) against prediction accuracy, with a tunable hyperparameter λ. Experiments on synthetic linear-Gaussian data and two real-world datasets (UCI Student, Credit Risk) demonstrate trade-off curves where ε-IFair can simultaneously approach the low unfairness of a strictly fair baseline (IFair) and the low error of an unconstrained model.

## Strengths

- **Modeling technique that preserves MPDAG structure after adding the predictor (Theorem 1).** The augmented-𝒢 construction (Definition 4) and the proof that adding Ŷ as a child of all nodes yields a valid MPDAG is a clean theoretical result that enables formal causal reasoning on the predictor. This theorem may be of independent interest beyond fairness applications.

- **Clear integration of MPDAG causal identification into a practical fairness optimization.** The paper connects the partial causal ordering (PCO) framework of Perković et al. (2020) to the fairness setting, showing how to compute the interventional distribution P(ŷ | do(A), do(X_ad)) from observable densities when the graph is partially known, and operationalizing this via Monte Carlo sampling and MMD-based constraints.

- **Demonstrated fairness-accuracy trade-off.** The experimental results (Figures 2–5) show that the ε-IFair method can interpolate between the extremes of the Full model (low error, high unfairness) and the IFair model (near-zero unfairness, high error) by varying λ, supporting the claim that the constrained optimization approach is practically usable.

- **Explicit discussion of non-identification handling.** Section 4.2 discusses averaging over valid orientations of undirected edges when the causal effect is not identifiable — a pragmatic and honest treatment of a real limitation.

## Weaknesses

### Major

1. **Proposition 1's identification condition requires stronger justification.** The paper claims (line 232) that the causal effect P(ŷ | do(S)) is identifiable *iff* there is no undirected edge between any node in V' and any node in S in the original MPDAG 𝒢. This simplified condition deviates from Perković et al. (2020, Theorem 3.6), whose identification criterion for MPDAGs involves checking *proper possibly directed paths* — a more nuanced condition that does not reduce to a simple check of undirected edges between the two sets in general. The paper states the proof is "based on" Perković et al.'s result and in the appendix, but without seeing the derivation, it is unclear whether the "iff" claim holds for all MPDAG structures. If the condition is merely sufficient rather than necessary (or missing additional constraints), the identification formula could be applied incorrectly in cases the authors believe are handled. **This is the most significant concern because the entire objective function depends on computing this causal quantity correctly.** The authors should either provide a complete proof connecting their condition to Perković et al.'s general criterion, or relax to a sufficient condition and characterize when it fails.

2. **Experiments never test the distinctive aspect of interventional fairness: non-empty admissible sets.** The paper explicitly states (line 269): "Here, we focus on the scenario where the admissible variable set is empty." With X_ad = ∅, interventional fairness collapses to total causal effect fairness — the very notion that the IFair baseline already targets. The whole point of the interventional fairness definition (Definition 1) is precisely the ability to allow certain causal pathways through admissible attributes. By never demonstrating the method with X_ad ≠ ∅, the paper fails to validate the capability that distinguishes its approach from simpler causal fairness notions. This is a significant gap between the claimed contribution and the demonstrated evidence.

3. **The synthetic evaluation does not test realistic partial knowledge.** The simulation derives the CPDAG directly from the true DAG (line 284) and adds background knowledge also drawn from the true DAG (line 286). This guarantees the MPDAG always contains the true DAG in its equivalence class and has no estimation errors. In practice, CPDAGs would be learned from finite observational data with statistical noise, and background knowledge may be incomplete or imperfect. Without experiments where the CPDAG is *learned* (e.g., via PC or GES) or where the MPDAG contains misspecified orientations, the claim that the method "handles partially known causal graphs" is only validated under idealized conditions. Additionally, the construction of MPDAGs for the real-world datasets (Student, Credit) is not described — the paper merely references figures without explaining whether these graphs came from domain knowledge, causal discovery, or prior literature.

4. **No error bars or confidence intervals in the trade-off plots.** The synthetic results (Figures 2a–2d) report averages over 10 random graphs but show only point estimates. Given the variance induced by different graph structures and data generation, the reader cannot assess whether observed differences between methods are statistically reliable.

### Minor

1. **Inconsistent unfairness metric in the Credit Risk experiment.** The training objective uses MMD, but the Credit Risk results (line 395) report unfairness as absolute difference in means (because the target is binary). While explained, this disconnect weakens the link between the optimization objective and the reported evaluation.

2. **Only linear-Gaussian synthetic data tested.** The conditional density estimation (multivariate normal) exactly matches the data-generating process, making the identification and estimation steps unrealistically clean. Testing with nonlinear data or misspecified density models would strengthen the evaluation.

3. **No discussion of λ selection.** The paper uses λ ∈ {0, 0.5, 5, 20, 60, 100} but provides no guidance on how practitioners should select λ in a new dataset or how sensitive the results are to this choice.

### Trivial

None.

## Nice-to-Haves

- A comparison against a non-causal fairness method (e.g., adversarial debiasing, reweighting) would help clarify whether the extra complexity of causal identification on MPDAGs provides practical benefit over approaches that do not use causal graph information.
- Non-parametric or more flexible density estimation (e.g., conditional normalizing flows) could be tested to assess robustness beyond the linear-Gaussian setting.

## Removed Points

- **Concern about proofs being relegated to the appendix.** Removed per policy: the appendix exists in the original submission; the parser stripped it.
- **Concern about "no comparison against existing fairness-constrained optimization methods."** Not a core weakness of this paper. The baselines (Full, Unaware, IFair) are appropriate for evaluating the benefit of using causal graph structure; adding non-causal baselines would answer a different question.
- **Concern about Proposition 1 being "not adequately justified" in the sense of missing proof steps.** The paper states the proof is provided in the appendix; the criticism is about correctness (kept above) rather than absence.

## Novel Insights

The most interesting observation across the reviews is the tension between the paper's clean theoretical framing (Theorem 1 ensuring the augmented graph remains an MPDAG) and the practical difficulty of verifying the identification condition in realistic settings. The paper's "no undirected edge" condition for identification is appealingly simple, but the reviewer's challenge reveals a gap between that simplicity and the known complexity of causal identification in MPDAGs. Whether this gap can be closed (the proof exists in the appendix) or represents a real limitation will determine the paper's theoretical contribution. The experimental gap (X_ad = ∅) is a separate but equally important concern: the paper motivates its work with the flexibility of interventional fairness over total effects, then never tests that flexibility.

## Suggestions

1. **Provide a complete proof (or citation-to-condition mapping) for Proposition 1 in the main text** — at minimum, state how the "no undirected edge" condition follows from Perković et al. (2020, Theorem 3.6) for the specific augmented graph structure. If the condition is only sufficient, say so.
2. **Add at least one experiment with a non-empty admissible set** — e.g., a synthetic setting where X_ad is a known descendant of A but considered a fair pathway, and show that the method can be tuned to block only the unfair effect.
3. **Include a robustness experiment where the CPDAG is learned from data** (e.g., via the PC algorithm) rather than derived from the true DAG, to simulate realistic partial knowledge with estimation error.
4. **Describe how the real-world MPDAGs were constructed** — what background knowledge or discovery algorithm was used?
5. **Add error bars** (e.g., standard deviations or bootstrap confidence intervals) to the trade-off plots.

## Score and Decision

The paper tackles an important and timely problem — relaxing the full-DAG assumption for causal fairness. The augmented-𝒢 modeling technique (Theorem 1) is a clean contribution, and the constrained optimization framework is practically motivated. However, the paper has two structural weaknesses: (1) the identification condition in Proposition 1 makes a strong "iff" claim whose correctness relative to the known MPDAG identification literature is not adequately justified in the main text; (2) the experimental evaluation does not demonstrate the method's most distinctive capability (non-empty admissible sets) and tests only under idealized partial-knowledge conditions. These limitations are significant but not fatal — the paper's core framework could become convincing with a corrected/relaxed identification analysis and broader experiments.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>