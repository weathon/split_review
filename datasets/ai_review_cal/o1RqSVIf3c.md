- Decision: Reject
- Avg Score: 4.25
- Scores: 3, 6, 5, 3
Now I have a thorough understanding of the paper. Let me compose the final consolidated review.

## Summary

This paper proposes a Bayesian preference elicitation framework for personalizing algorithmic recourse (prefactual recommendations). The framework has three components: (1) selecting pairwise comparison questions by maximizing an analytically-computed asymptotic mutual information between the response and the Wishart-distributed cost matrix; (2) updating a Wishart posterior via an optimization combining reverse KL divergence with a linearized response-likelihood term, solved by projected gradient descent with convergence guarantees; and (3) recommending a graph-based sequential recourse path minimizing expected cost under the posterior. Experiments on synthetic and real-world datasets show that the method reduces path cost relative to FACE and other baselines.

## Strengths

- **Analytical mutual information for efficient question selection (Proposition 3.1, Theorem 3.2):** The paper derives a closed-form expression for mutual information in the asymptotic (κ→∞) limit, reducing the per-pair complexity from O(Ld²) for sampling-based estimates to O(d²). The derivation is technically sound and provides a genuine computational advantage for the question-selection step.

- **Posterior update with provable convergence guarantees (Lemma 4.5, Algorithm 1):** The optimization in Eq. (5) is shown to be strongly convex (parameter m_{t-1}/(m d²)) with a Lipschitz-continuous gradient (constant m_{t-1}/(m ε²)) on the compactified feasible set. The projection operator is reduced to a simplex projection (Lemma 4.4), and linear convergence of projected gradient descent follows from standard results. This provides rigorous algorithmic guarantees.

- **Clean recourse reformulation using Wishart moment property (Section 5):** The expected-cost minimization (Eq. 7a) reduces to a deterministic binary linear program (Eq. 7b) because 𝔼[A] = m_T Σ_T for the Wishart distribution. This makes the recourse recommendation solvable by off-the-shelf solvers and is a clean application of the distributional assumptions.

- **Empirical validation on multiple datasets (Tables 1, 2; Figure 2):** Results are reported on German, Bank, Student, and Synthetic datasets. Under correct cost specification (Mahalanobis), Bayesian PR achieves lower path cost than FACE on all four datasets. Under misspecified cost (ℓ₁ norm), Bayesian PR is competitive or better on two of four datasets. The mean rank experiment (Figure 2) shows a consistent downward trend as more questions are asked, directly validating that the posterior mean moves toward the true ordering.

## Weaknesses

### Fatal
None.

### Major

- **Unjustified linear approximation of the sigmoid in the posterior update (Section 4.1, Eq. 3):** The paper approximates the BTL sigmoid Φ(v) by the identity function v↦v (line 148) to obtain a tractable objective. This is a coarse approximation: the slope of Φ at zero is 1/4, not 1, and the linear function is unbounded while Φ is bounded in [0,1], so the approximated "probability" can exceed 1. The paper neither analyzes the approximation error nor discusses its regime of validity, provides no comparison with a sampling-based or variational alternative, and does not justify why this specific linearization is reasonable. The resulting objective in Eq. (3) does not correspond to a proper Bayesian posterior under any standard likelihood model. While the method may work as a heuristic (the empirical results suggest it does), the paper consistently calls the result a "posterior" without caveating the severity of this approximation. This undermines the "Bayesian" framing of the core contribution.

### Minor

- **Asymptotic MI used without validation under finite κ (Section 3.1–3.2):** The question-selection criterion is derived in the noiseless limit κ→∞, but in practice κ is finite. The paper claims "experiments show that our framework performs effectively with finite κ" (line 116) but provides no experiment that isolates whether the asymptotic MI selects informative questions under finite κ, nor compares against a sampling-based MI estimator or random selection. The gap between the asymptotic selection criterion and the actual finite-κ response model could lead to suboptimal question choices, especially for small κ (high noise).

- **Evaluation lacks direct posterior quality metric:** The paper evaluates the posterior indirectly through mean rank (Figure 2) and downstream path cost (Tables 1, 2). A more direct metric — such as the Frobenius distance between the posterior mean m_T Σ_T and the ground truth A₀ — is never reported. This would provide a cleaner signal about whether the elicitation actually learns the cost matrix or only incidentally improves rank ordering.

- **FACE comparison does not cleanly isolate preference elicitation:** In Table 1 (Mahalanobis true cost), Bayesian PR is correctly specified while FACE is misspecified, and the two methods likely use different graph constructions. The paper says "we adhere to the setups outlined in their respective papers" (line 273) but does not confirm that the underlying graphs are comparable. In Table 2 (ℓ₁ true cost), the situation is reversed. This makes it difficult to attribute the cost differences solely to the preference elicitation component vs. structural differences in graph connectivity or path-finding logic.

- **Small validity gaps not discussed:** On Bank (Table 1) and Synthetic (Table 2), Bayesian PR achieves slightly lower validity than FACE (0.94 vs 1.00 and 0.96 vs 1.00, respectively). Lower cost with lower validity may not be a clear win, and this trade-off is not analyzed.

### Trivial
None.

## Nice-to-Haves

- Report statistical significance (standard deviations or confidence intervals) for the cost and validity metrics.
- Include runtime measurements to substantiate the claimed computational efficiency of the analytical MI and the projected gradient descent algorithm.
- Specify graph construction details (connectivity criteria, number of edges) to improve reproducibility.
- Discuss what happens when the "not parallel" condition (Theorem 3.2) is nearly violated — are near-parallel vectors pathological?

## Removed Points

- **Criticism about the "not parallel" assumption not being discussed further:** This was raised by the harsh critic but is a standard technical assumption in such derivations and does not merit inclusion as a weakness. The paper states it clearly.
- **Criticism about no comparison with Yadav et al. (2021):** The paper cites this work in the introduction but does not compare experimentally. While an additional baseline would strengthen the evaluation, this is better classified as a nice-to-have than a weakness, and the reviewer's framing of it as a missing comparison is somewhat scope-creeping.
- **Criticism about the ground truth A₀ being generated randomly:** This is standard practice in metric learning evaluations and does not constitute a weakness; the paper's goal is to test whether the framework recovers a known cost structure, for which a random ground truth is appropriate.
- **Generic criticisms about "the evaluation lacks rigor" without specific anchors:** These were filtered per the instructions.
- **Strength Finder's generic/superficial strengths:** The strength about "addressing an important problem" was removed as it is generic and applies to any paper on recourse.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a tension worth noting: the paper's methodological weaknesses (particularly the ad-hoc posterior approximation) and its empirical strengths (consistent cost reduction across datasets) point in opposite directions. This pattern — a heuristic that works well empirically despite a theory-practice gap in its derivation — is common in applied ML but deserves explicit acknowledgment rather than silent framing as Bayesian inference.

## Suggestions

1. **Either rigorously justify the posterior update or reframe it.** Provide error bounds on the linear approximation, or replace it with a proper variational bound (e.g., a quadratic bound on the logistic log-likelihood). At minimum, explicitly characterize the approximation as a regularized cost-learning heuristic and evaluate its sensitivity to the approximation quality (e.g., by comparing against MCMC on small problems).

2. **Validate question selection under finite κ.** Run an ablation comparing the asymptotic MI selection against (a) random selection and (b) a sample-based MI estimator on a small problem to confirm that the analytical criterion does not degrade informativeness.

3. **Add a direct posterior quality metric.** Report the Frobenius distance (or similar) between the posterior mean m_T Σ_T and the true A₀ as a function of T, alongside the existing mean rank metric.

4. **Control for graph structure in baselines.** Either use the same graph for both FACE and Bayesian PR (varying only the edge cost), or explicitly document the graph construction differences and discuss their impact on the comparison.
