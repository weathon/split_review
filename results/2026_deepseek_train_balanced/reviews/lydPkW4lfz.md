## Summary

This paper analyzes Local GD variants for distributed logistic regression with heterogeneous, separable data. The main contribution is proving that a Two-Stage Local GD algorithm (which uses a small learning rate in a warmup phase and then a large Θ(1) learning rate in the second phase) achieves an O(1/(γ²KR)) convergence rate, where increasing local steps K directly reduces communication rounds — a result that all prior worst-case guarantees of Local GD had failed to establish. The key technical insight is the vanishing Hessian property of the logistic loss: ‖∇²F(w)‖ ≤ F(w), which allows a large stepsize η₂ independent of K once the objective is sufficiently small.

## Strengths

- **First convergence guarantee showing local steps reduce communication rounds for a variant of Local GD on any problem**: Theorem 1 proves that Two-Stage Local GD converges at rate O(1/(γ²KR)), with K appearing in the denominator of the dominant ε-dependent term (line 102). Corollary 3 shows that with K = Θ(γ/√(Mε)), the round complexity improves from 1/ε to 1/√ε in ε-dependence (lines 124-127). This is a genuine advance over all prior analyses that cannot show K helps.

- **Novel proof technique exploiting the logistic loss's structure**: The paper identifies and leverages ℓ''(z) < |ℓ'(z)| < ℓ(z) for the logistic loss (Lemma 24), yielding ‖∇²F(w)‖ ≤ F(w) (Lemma 25). This means when the objective is small, the Hessian is also small, enabling η₂ = Θ(1) independent of K (line 116). Prior analyses required η ≤ 1/K. This is the paper's most elegant and technically novel contribution.

- **Carefully derived baselines adapted to the no-minimizer setting**: Corollaries 1 and 2 concretely instantiate the rates implied by existing analyses (Woodworth et al., Koloskova et al.) for the logistic regression setting where no global minimizer exists (lines 66-82). The dominating terms do not depend on K, making the comparison to Theorem 1 rigorous.

- **Last-iterate guarantee**: Theorem 1 provides a last-iterate guarantee for the second stage output (line 130), which is strictly stronger than the average-iterate guarantees given by the baseline analyses.

- **Novel Lyapunov function for the Local GF analysis**: The construction of L_r = max_m ρ_r^m using surrogate losses involving the Lambert W function (line 246) is a technically interesting approach for handling the non-monotonic convergence behavior observed when large ηK creates instability across heterogeneous clients.

## Weaknesses

### Major
None.

### Minor

- **The main result applies to a two-stage variant, not vanilla Local GD**: Theorem 1 analyzes Two-Stage Local GD (Algorithm 2), which requires two carefully tuned learning rates η₁ and η₂ and a transition round r₀ that itself depends on K, M, and γ. The paper's Limitations section (line 287) acknowledges this: "our results do not apply for the vanilla Local GD algorithm." While the paper is transparent about this, the title "Local Steps Speed Up Local GD" and the abstract's framing imply a broader result. The contribution is narrower than a first reading suggests.

- **The warmup requirement substantially constrains the practical benefit**: The second-stage rate improves with K, but the warmup rounds satisfy r₀ = Ω(KM/γ⁴ + (KM)^{3/4}/γ^{5/2}) (Theorem 1). So K helps the second-stage term but hurts the first-stage term. The optimal choice K = Θ(γ/√(Mε)) (Corollary 3) yields total rounds R ≥ Õ(M^{1/2}/(γ³ε^{1/2}) + 1/(γ^{7/4}ε^{3/8})). This requires knowing ε, γ, and M in advance to set K optimally, and the γ⁻³ and γ^{-7/4} dependence is worse than the γ⁻² dependence of baselines — which matters when the margin γ is small in practice. The paper mentions the warmup cost at line 130 but does not discuss these practical tuning difficulties.

- **The Local GF result (Section 5) is too preliminary to carry significant weight**: Theorem 2 analyzes Local GF for M=2 clients and n=1 data point per client. The transition time τ has bounds involving exp(1/γ_min) and exp(1/(1+c)) (line 229), which are enormous for small margins or nearly orthogonal client data. The paper acknowledges this candidly (line 287: "these results are preliminary in that they require strong assumptions"), but the section still reads as a proof-of-concept rather than a meaningful convergence guarantee. The impressive ε-dependence improvement (to ε^{-(1-α)}) comes at the cost of constants that would dominate in any practical regime.

- **Abstract imprecision about Ω(1/R) vs O(1/R)**: The abstract claims "all existing convergence guarantees for Local GD applied to any problem are at least Ω(1/R)." But Corollaries 1 and 2 give O(1/R) *upper bounds* on the existing guarantees, not Ω(1/R) lower bounds. The intended point (that existing guarantees don't improve with K) is correct, but the wording conflates an upper bound on the rate with a lower bound on the problem.

- **Experiments are purely illustrative and do not validate the claimed rates**: Figure 1 shows loss curves for two datasets under three stepsize choices, but there are no measured convergence rates, no error bars, no ablation of K, and no comparison to baselines beyond different stepsize choices (line 276-281). For a paper whose central claim is about convergence rates, directly measuring and displaying the empirical rate (loss vs. rounds for various K) would substantially strengthen the paper. As it stands, the experiments show qualitative behavior but do not confirm the O(1/(KR)) rate.

- **MNIST experimental setup is underspecified**: The paper provides no details on how the MNIST data was partitioned across clients to create heterogeneity (number of clients, partition strategy). This makes the experiment difficult to assess or reproduce.

### Trivial
- Abstract's "at least Ω(1/R)" should read "at most O(1/R)" or "no better than O(1/R)" for technical precision.

## Nice-to-Haves
- A lower bound showing Ω(1/(KR)) is necessary would strengthen the theoretical contribution.
- Discussion of robustness to misspecified hyperparameters (γ is typically unknown in practice).
- Empirical demonstration of the O(1/(KR)) scaling slope for various K in the second stage of Algorithm 2 would bridge the theory-experiment gap.

## Removed Points
The following points from the input reviews were removed after verification:
- *Harsh critic's point about no comparison to SCAFFOLD*: Not required for a theory paper focused on Local GD analysis; the paper never claims to outperform variance-reduced methods.
- *Harsh critic's point about "baselines are derived by modifying existing analyses, not by proving a matching lower bound"*: This is not a weakness; establishing baseline upper bounds is standard practice.
- *Strength Finder's more generic formulations of "addressed an important problem"* (which were not present in the final strength list).
- Any speculative weaknesses about what the appendix "may" contain or assumptions about missing supplementary material.

## Novel Insights
The most insightful cross-cutting observation across the reviews is the tension between the paper's clean theoretical story (vanishing Hessian → large ηK → K reduces rounds) and the practical complexity of actually deploying that result. The vanishing Hessian analysis is elegant and technically sound, but it requires the warmup phase to reach a threshold F(w̄₀) ≤ γ²/(42η₂KM), which itself scales with K and inversely with γ⁴. The paper shows that K helps asymptotically, but the parameter regime where this benefit materializes — where γ is not too small, M is not too large, and the practitioner can estimate γ, M, and ε to set K — is narrower than a headline reading suggests. This is not a flaw in the mathematics but an important caveat for interpreting the result's significance.

## Suggestions
1. Tune the title and abstract to more precisely reflect that the main result applies to Two-Stage Local GD, not vanilla Local GD.
2. Add a concrete illustration or discussion of when the warmup cost is dominated by the second-stage benefit (e.g., regime plots showing where the trade-off favors larger K).
3. Strengthen the experiments by measuring and plotting the empirical convergence rate (loss × K vs. rounds) for different K values in the second stage of Algorithm 2, to provide direct validation of Theorem 1.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>