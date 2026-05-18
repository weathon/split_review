Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper proposes a Bayesian preference elicitation framework for personalizing algorithmic recourse. The core idea is to learn an individual's cost function (a Mahalanobis weighting matrix) through a small number of strategically chosen pairwise comparisons, then use the learned posterior to recommend graph-based sequential recourse with minimal expected cost. The method contributes: (1) an analytical mutual information expression for question selection using an asymptotic approximation, (2) a variational posterior update restricted to Wishart distributions with a convergence guarantee, and (3) a binary linear programming formulation for recourse over a graph. Experiments on synthetic and three real datasets are reported.

## Strengths

1. **Analytical mutual information for efficient question selection**: The paper derives a closed-form expression for asymptotic mutual information (Proposition 3.1) and a computable probability for the difference of Wishart quadratic forms (Theorem 3.2), reducing the computational complexity from O(L·d²) sampling to O(d²) analytical evaluation (Section 3.1). This is a technically solid result that enables scalable question selection without expensive Monte Carlo simulations.

2. **Principled posterior update with convergence guarantee**: The posterior update formulation (Section 4.1) minimizes KL divergence combined with a response-alignment term. Proposition 4.3 compactifies the feasible set, Lemma 4.4 reduces the projection to a simplex projection on eigenvalues, and Lemma 4.5 proves strong convexity and Lipschitz smoothness, ensuring linear convergence of the projected gradient descent algorithm (Section 4.2). This gives the optimization a rigorous foundation.

3. **Clean integration of elicitation with recourse recommendation**: Section 5 connects the posterior output to a tractable recourse optimization by exploiting the Wishart moment condition (𝔼[A] = m_T Σ_T), converting a stochastic optimization over matrix-valued random variables into a binary linear program solvable by off-the-shelf solvers. The framing of recourse as expected-cost minimization under a learned posterior is conceptually clean.

## Weaknesses

### Fatal

None.

### Major

1. **The linearized likelihood in the posterior update is unvalidated.** The paper approximates the logistic/BTL likelihood by Φ(v) ≈ v (Section 4.1), which is a crude linearization valid only when κΔᵢⱼ is small. When the cost difference is large — i.e., when the response is nearly deterministic — this approximation dramatically overestimates the effect of the response, losing the saturation behavior essential to the BTL model. The paper provides no analysis of the approximation error, no comparison with a more accurate Bayesian update (e.g., probit link or Pólya-Gamma augmentation), and no diagnostic of posterior quality (coverage, calibration). Since the posterior drives recourse recommendation, systematic bias could lead to consistently poor cost estimates. This is the most serious technical gap in the paper.

2. **The graph construction for recourse is critically underspecified.** Section 5 states that a directed graph 𝒢 = (𝒱, ℰ) is constructed to "capture the underlying geometric structure of the available data" and that edges represent "feasible transitions," but provides no description of *how* edges are determined. Are they k-NN edges? ε-radius? Based on feature-space proximity? Do they incorporate actionability constraints (e.g., immutable features)? The paper says it is "inspired by FACE" (Poyiadzi et al., 2020) but does not specify which graph construction was actually used in the experiments. Without this, the recourse recommendation problem is not fully defined, and the experiments cannot be reproduced. Additionally, the flow constraints in problem (6) are displayed as applying to *all* nodes, but the explanatory text says they apply only to negative-class nodes — the mismatch between the mathematical display and the text is confusing and should be resolved.

3. **Experiments lack critical baselines to demonstrate the value of the elicitation framework.** The mean rank plots (Figure 2) show decreasing mean rank with more questions, but there is **no comparison with random question selection** to show that the MI-based selection actually helps, and **no comparison with a prior-only baseline** (T=0, using only the prior without elicitation). Without these controls, the improvement could simply be due to increasing the number of queries rather than the specific MI-based selection strategy. These baselines are essential to support the paper's core claim.

4. **No hyperparameter sensitivity analysis.** The hyperparameter τκ is set to 1 with no justification and no exploration of its effect on the posterior or final recourse quality. Similarly, there is no sensitivity analysis with respect to the initial prior parameters (m₀, Σ₀) or the degrees-of-freedom constraint m ≤ m_{t-1}. These choices could materially affect results, and their effects are not characterized.

### Minor

1. **The asymptotic MI approximation is used for question selection without finite-κ validation in the main text.** Proposition 3.1 derives mutual information in the κ → ∞ (noiseless) limit, but κ is finite in practice (τκ = 1). While the paper claims empirical validation exists (the garbled ".5" reference on line 116 likely refers to an appendix experiment), the main paper provides no theoretical bound on the approximation error and no analysis of how the selected questions differ from those chosen under the exact finite-κ MI. The concern is partially mitigated because MI is used only for question selection (a heuristic), not for inference — even approximate MI-maximization may yield informative questions. Still, this gap should be addressed.

2. **The ground truth in synthetic experiments is well-specified to the model.** The ground truth A₀ is generated as AAᵀ with i.i.d. Gaussian entries, which is essentially a sample from the same Wishart family used as the prior. The ℓ₁ experiments in Table 2 do test misspecification on real data, but the synthetic experiments add limited evidence when the model is perfectly well-specified. Testing with alternative cost structures in the synthetic setting would strengthen the evaluation.

3. **The non-increasing degrees-of-freedom constraint (m ≤ m_{t-1}) is imposed without justification.** This restriction artificially limits the posterior's flexibility — if the data strongly suggest more certainty, it is unclear why the degrees of freedom should only decrease. This warrants at least a brief discussion.

4. **The bound ε in Proposition 4.3 depends on ‖Σ_{t-1}⁻¹ + τκ Rᵢⱼ Mᵢⱼ‖_F**, which could be large, making ε extremely small and potentially causing numerical issues in the projected gradient descent algorithm.

5. **Question selection complexity is O(N²) over the positive dataset**, which could be prohibitive for large N. The paper acknowledges this but does not discuss mitigation strategies (e.g., sampling a subset of candidates).

6. **The claim of O(d²) complexity for the analytical MI** is slightly optimistic — computing the Gauss hypergeometric function ₂F₁ (Theorem 3.2) is generally fast in practice, but the complexity of evaluating it to machine precision is not constant across all parameter regimes. A brief runtime comparison with sampling would be helpful.

### Trivial

- The displayed flow constraints in problem (6) apply to all nodes without restriction, while the explanatory text (line 253) clarifies they are intended only for negative-class nodes. The display should be corrected to match the text.

## Nice-to-Haves

- A comparison of the asymptotic MI-based question selection against exact finite-κ MI (estimated via sampling) on a small-scale problem would validate the approximation.
- Replacing the linearized likelihood with a more principled approximation (e.g., a probit link with Gaussian approximation, or Pólya-Gamma augmentation) would strengthen the inference. At minimum, comparing the posterior from the linearized method against MCMC on a synthetic problem would help assess bias.
- Including the non-graph-based baselines (Wachter, DiCE) in the main results tables rather than deferring them to the appendix would improve the paper's self-containedness.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"No Section 6.5 in the extracted text"** — The garbled reference on line 116 is a parser artifact; the appendix (stripped) likely contains the cited experiment. Removed per the rule that parser-stripped appendix content is not a valid weakness.
- **"Wachter/DiCE results are only in the appendix"** — The comparison methods are declared in Section 6 intro; their result tables likely appear in the stripped appendix. Removed per appendix-strip rule. (The broader point that these results would strengthen the main text is retained as a Nice-to-Have.)
- **"No experiments test misspecification of the cost function form"** — This is factually incorrect. The paper explicitly tests ℓ₁ norm as true cost (Table 2, Section 6.2), which is a misspecification test since the model assumes Mahalanobis. Removed.
- **"Flow formulation may be mathematically inconsistent"** — The explanatory text (line 253) clarifies that the second flow constraint applies only to negative-class nodes. The mathematical display omits this restriction, which is a presentation error, not a mathematical inconsistency. Downgraded to Trivial.
- **Generic formatting/style nitpicks** — Removed per hard rules.

## Novel Insights

The most interesting tension that emerges from the reviews is between the paper's clean mathematical structure (analytical MI, provably convergent posterior update, tractable recourse LP) and the crude approximations required to achieve it (asymptotic MI, linearized likelihood, fixed Wishart family). The paper presents a coherent *framework* that elegantly connects Bayesian elicitation to graph-based recourse, but each step involves an approximation whose error is uncharacterized. The question is whether these approximations degrade performance in practice — the experiments attempt to address this but lack the baselines needed to isolate each component's effect. A systematic ablation study (e.g., replacing each approximation with a gold standard one at a time) would transform this from a promising framework into a validated method.

## Suggestions

1. **Validate or replace the linearized likelihood.** This is the most critical gap. Either analyze the approximation error theoretically, replace it with a more principled variational approximation (probit link, Pólya-Gamma), or at minimum compare against MCMC on a small synthetic problem to assess bias.

2. **Specify the graph construction completely.** Describe exactly how edges are defined in the experiments (k-NN parameters, actionability constraints, node set composition). This is essential for reproducibility.

3. **Add the missing baselines.** A no-elicitation baseline (recourse using the prior mean) and a random-question-selection baseline are needed to isolate the benefit of the elicitation framework.

4. **Add hyperparameter sensitivity analysis** for τκ and the prior parameters.

5. **Add an oracle baseline** (recourse using the true A₀) to show the upper bound on performance.

## Score and Decision

The paper addresses a timely and well-motivated problem with a creative synthesis of Bayesian preference elicitation and algorithmic recourse. The mathematical machinery (analytical MI, provably convergent posterior update, tractable recourse LP) is competently developed. However, the paper's core claims are weakened by unexamined approximations and a lack of critical experimental baselines. The linearized likelihood is used without any error analysis or validation, and the experiments cannot distinguish whether the reported improvements come from the specific MI-based query strategy, the Bayesian framework, or simply asking more questions. The paper also leaves the graph construction critically underspecified, hindering reproducibility. These are significant gaps that prevent the paper from fully delivering on its contribution in its current form.

The strengths are real but the weaknesses are substantive enough that the paper needs major revisions before it can be accepted. I recommend rejection, with encouragement to resubmit after addressing the major issues — particularly validating the linearized likelihood, specifying the graph construction, and adding the missing baselines.

MY FINAL SCORE: 5.0
MY FINAL DECISION: <orange>Reject</orange>