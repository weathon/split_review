Now I have all the information needed. Let me write the final consolidated review.

## Summary

This paper introduces a Bayesian preference elicitation framework for personalizing algorithmic recourse (prefactual recommendations). The key idea is to learn an individual's cost weighting matrix (Mahalanobis distance) through pairwise comparison questions, using an analytical asymptotic mutual information formula for efficient question selection and a compactified posterior update procedure. The learned posterior is then used to recommend graph-based sequential recourse with minimal expected cost (solved as a binary linear program). Experiments on synthetic and real-world datasets show that increasing the number of questions reduces the mean rank of recommended recourses and that the method is competitive with FACE even under cost-function misspecification.

## Strengths

- **Analytical closed-form for asymptotic mutual information (Theorem 3.2).** By deriving an explicit expression for ℙ(Δ_ij ≤ 0) under a Wishart prior using properties of correlated gamma variables and the Gauss hypergeometric function, the paper avoids expensive sampling (O(Ld²)) and reduces question-selection computation to O(d²) per pair. This is a technically clean contribution that could be useful beyond this paper.

- **Principled convergence guarantee for posterior update.** The paper compactifies the feasible set (Proposition 4.3), reduces the projection onto the trace-constrained PSD cone to a simplex projection (Lemma 4.4), and proves strong convexity and Lipschitz smoothness (Lemma 4.5), yielding linear convergence for the projected gradient descent algorithm. This provides a rigorous optimization foundation for the belief-updating step.

- **Tractable recourse as a binary linear program.** By exploiting the Wishart moment condition 𝔼[A] = m_T Σ_T, the stochastic recourse problem reduces to a deterministic binary program solvable with off-the-shelf optimizers (Mosek, GUROBI). This clean reduction is a practically useful contribution.

- **Robustness under cost misspecification (Table 2).** When the true cost is ℓ₁ (so Bayesian PR's Mahalanobis assumption is misspecified, while FACE correctly uses ℓ₁), Bayesian PR achieves comparable or lower cost on the Synthetic and Student datasets. This empirically demonstrates the framework's adaptability beyond its assumed cost class — a stronger result than the more obvious Table 1 comparison where Mahalanobis is the true cost.

- **Validation of elicitation via mean rank decay (Figure 2).** The mean rank of recommended recourses (relative to the true cost) consistently decreases as the number of questions T increases across all four datasets, confirming that the sequential questioning progressively refines the posterior toward the ground truth.

## Weaknesses

### Fatal
None.

### Major

1. **Unvalidated linear approximation in posterior update (Section 4.1).** The paper replaces the logistic function Φ(v) = 1/(1+e^{−v}) with the linear map v ↦ v to obtain tractability in the response-likelihood term. This approximation is unjustified: Φ(v) is bounded between 0 and 1, while v is unbounded, so the approximation can produce arbitrarily poor estimates, especially when |κΔ_ij| is large (which occurs early in learning). The resulting objective (3) is an ad hoc combination of a reverse-KL divergence with an unbounded linear penalty that does not correspond to any principled variational bound. Crucially, **no diagnostic experiments are provided** to validate this approximation — e.g., comparing the learned posterior to a sampling-based posterior (MCMC) on synthetic data with known ground truth. The paper sets τκ = 1 in all experiments, further masking the behavior of this term. Without validation, the fidelity of the entire posterior inference pipeline is uncertain. This is the most substantive methodological gap in the paper.

2. **No ablation of the question-selection strategy.** The paper uses asymptotic (κ → ∞) mutual information for query selection but provides **no comparison to simpler baselines** such as random question pairs, uniform sampling, or a sampling-based finite-κ mutual information estimate. Figure 2 shows that the overall elicitation pipeline reduces mean rank with more questions, but this conflates the effect of the MI-based selection strategy with the effect of simply asking more questions. Without an ablation, claims about "efficient, near-optimal question selection" are unsubstantiated — the observed improvement could come entirely from the quantity of feedback rather than the quality of selected pairs.

### Minor

1. **Number of questions T is not reported in the main cost-comparison tables (Tables 1 and 2).** The paper's sample efficiency is a central advertised contribution, but the tables comparing Bayesian PR to FACE do not state how many questions were asked. If T is small, the improvement may be due to the cost-function specification rather than effective learning; if T is large, the comparison is in a different regime. This omission makes it impossible to assess sample efficiency from the primary comparison tables. (Figure 2 does show T ∈ [1,10], but it is a different experiment with a different metric.)

2. **The baseline comparison in Table 1 is predictably asymmetric.** When the true cost is Mahalanobis (Table 1), Bayesian PR correctly assumes this form while FACE uses its default (L2/L1) cost — so Bayesian PR unsurprisingly achieves lower Mahalanobis cost. The paper transparently acknowledges this asymmetry. Table 2 partially addresses the concern by flipping the advantage to FACE. Still, the headline interpretation of "outperforms" is mostly supported by the misspecification-robustness result (Table 2), not by Table 1. A cleaner experimental design would include a version of FACE using the same Mahalanobis cost.

3. **The graph construction and edge-connectivity criteria are underspecified.** Section 5 describes the recourse graph as "inspired by FACE" but does not define how edges are determined (e.g., k-nearest-neighbor threshold, epsilon-ball, density-based connectivity). This makes the recourse-recommendation component difficult to reproduce independently, even though the binary LP formulation itself is clear.

4. **Figure 2 lacks error bars or variance information.** The plot shows mean rank decreasing with T, which is encouraging, but without confidence intervals or per-dataset variance, it is unclear whether the improvement is statistically significant, especially given that each "user" has a randomly generated ground truth A₀.

### Trivial

- The ground truth A₀ is generated as A₀ = AA^T with i.i.d. standard normal entries, which produces matrices with no particular structure. This is reasonable for synthetic experiments but may not reflect realistic cost preferences.
- The hyperparameter setting τκ = 1 is stated without justification or sensitivity analysis.

## Nice-to-Haves

- Sensitivity analysis for τκ and κ (the noise parameter) to understand when the linear approximation degrades.
- A comparison with random question selection as a baseline in the mean-rank experiment (Figure 2) to isolate the benefit of the analytic MI formulation.
- Validation of the posterior update against a sampling-based posterior (e.g., MCMC or importance sampling) on synthetic data with known A₀, reporting KL divergence or Frobenius norm error of the mean.
- Reporting T explicitly in Tables 1 and 2, or showing a trade-off curve as T varies.
- A qualitative example showing the actual graph path recommended by Bayesian PR vs. FACE vs. the true minimum-cost path for one user.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Lemma 4.5 (strong convexity and Lipschitz gradient)... no proof is provided."** Proofs for theoretical claims are standardly deferred to the appendix, which the PDF parser strips. This is a known artifact of the review process, not an author omission.

- **"The garbled notation [in Algorithm 1] is a parser issue."** Correct — this is a PDF-to-text artifact, not an author error. Removed per guidelines.

- **"Wishart quadratic forms not being independent... derivation appears to use the property of difference of correlated gamma variables."** This is a technical observation about the derivation of Theorem 3.2, but the critic acknowledges it is "not a fatal flaw." The paper's math is standard; the critic is pointing out complexity (correlation) that the paper already accounts for in the formula.

- **"The paper overstates novelty: Bayesian preference elicitation for pairwise comparisons is well-established."** The paper's novelty is the *application to recourse* and the *specific technical pipeline* (Wishart prior + analytic MI + compactified posterior + graph-based recourse). The critic's claim that "the technical components are mostly re-used" ignores the non-trivial integration and new derivations (Theorem 3.2, Proposition 4.3, Lemma 4.4–4.5). The paper's contribution claims are appropriately scoped.

- **"O(N²d²) complexity... becomes prohibitive when N is large."** The paper already acknowledges O(N²) complexity. This is a known limitation of pairwise-comparison elicitation, not an oversight. The paper does not claim scalability to millions of points.

- **"Numerical instability of Gauss hypergeometric function for certain parameter ranges."** This is a speculative concern about implementation details common to many papers using special functions. No evidence of actual instability is provided.

## Novel Insights

The most striking observation emerging from this review is the disconnect between the paper's clean theoretical scaffolding (analytic MI in Theorem 3.2, compactification in Proposition 4.3, convergence guarantee in Lemma 4.5, tractable binary LP for recourse) and the brittleness of its core posterior update, which relies on an unvalidated and likely poor linear approximation to the logistic likelihood. The paper has the right high-level architecture for personalized recourse — elicit preferences via queries, update beliefs, recommend paths — but the weakest link is the very step that connects responses to beliefs. The mean rank results in Figure 2 suggest the overall pipeline does learn something useful, but whether a tighter variational approximation or a sampling-based posterior would substantially improve performance remains unknown. This also means the ablation studies the community would need (random vs. MI-based queries, sampling-based vs. approximate posterior) are exactly the ones missing from the paper.

## Suggestions

1. **Validate the linear approximation.** Add a synthetic experiment with known A₀ where the posterior mean m_TΣ_T from the approximate method is compared to a sampling-based posterior (e.g., MCMC). Report the Frobenius norm error ‖m_TΣ_T − A₀‖_F and KL divergence as functions of T. This is the single most important missing experiment.

2. **Add a random-question baseline.** In the mean-rank experiment (Figure 2), compare the analytic MI selection against random pair selection at the same number of questions. This isolates the benefit of the question-selection component from the overall elicitation effect.

3. **Report T in Tables 1 and 2.** Either fix T across all methods and datasets and report it, or show a sweep over T with the cost/validity trade-off. Without this, the reader cannot assess sample efficiency from the primary cost comparison.

4. **Specify the graph-construction details** (neighborhood connectivity criteria, edge feasibility constraints) to enable reproduction of the recourse recommendation.

## Score and Decision

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>