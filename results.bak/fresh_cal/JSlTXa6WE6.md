Now I have all the information needed to write the consolidated review.

## Summary

This paper introduces ∂-CROWN, a post-training certification framework that computes guaranteed upper bounds on the continuous-domain residual error of Physics-Informed Neural Networks (PINNs). The method formalizes three correctness conditions (initial, boundary, residual), extends CROWN-based linear bound propagation to handle partial derivatives of neural networks with O(L) complexity per derivative via a hybrid back-propagation / forward-substitution scheme, and uses greedy input branching to tighten bounds. Experiments on Burgers', Schrödinger, Allen-Cahn, and Diffusion-Sorption equations demonstrate that ∂-CROWN produces certified residual bounds that are tighter than IBP and LiRPA baselines at matched runtimes.

## Strengths

1. **Formal correctness conditions for PINNs over continuous domains.** Definition 1 explicitly defines three error-based conditions (initial, boundary, residual) that must hold over the *entire* spatio-temporal domain, shifting away from the pointwise empirical evaluations standard in prior PINN work. This gives a principled target for certification.

2. **Efficient O(L) derivative bounding via a hybrid scheme.** Theorems 1 and 2 derive closed-form linear bounds for first and second partial derivatives of a neural network using a hybrid back-propagation/forward-substitution approach, avoiding the O(L²) cost of full LiRPA. Table 2 confirms that under fixed runtime, ∂-CROWN achieves tighter residual bounds than both IBP and LiRPA (e.g., certified residual bound 1.30×10¹ vs. 2.78×10³ for IBP and 1.78×10² for LiRPA for Burgers' equation).

3. **Certification reveals failures naive sampling would miss.** The Diffusion-Sorption example is compelling: 10⁴ Monte Carlo samples estimate the residual max at 1.1×10⁻³, while 10⁶ samples give 21.09—and ∂-CROWN's certified bound (21.34) correctly reports the larger value, demonstrating the practical need for formal certification over finite-point testing.

4. **Greedy input branching concentrates computation effectively.** Algorithm 1 adaptively splits subdomains where the gap between empirical and certified bounds is largest, and the branching density visualizations in Figure 1 confirm that the allocation is non-uniform, concentrating effort where bounds are loosest.

5. **Empirical analysis of the residual-to-solution error correlation.** Figure 2 provides an empirical link (for Burgers' equation) between maximum residual error and maximum solution error across training epochs, supporting the relevance of residual certification as a meaningful—though not formal—proxy.

## Weaknesses

### Major

1. **The certification target is the residual, not the solution error.** The paper certifies that |f_θ| ≤ ε, but this does *not* certify that |u_θ − u| is small. The paper acknowledges this clearly (Section 5.2: "there is no formal guarantee related to |u_θ − u| within our framework"), and this is stated upfront. However, the practical significance of the framework is substantially limited by this gap. Practitioners deploying PINNs care about how far the approximate solution is from the true PDE solution, not directly about the residual. The empirical correlation for Burgers (Figure 2) is a starting point, but no quantitative measure (e.g., R²) is given, and no stability argument linking residual to solution error is provided. This is a real limitation that constrains the framework's impact, even if the paper is transparent about it.

2. **Runtime for residual certification is prohibitive for practical use.** The reported residual verification times are 2.8×10⁵ seconds (~3.2 days) for Burgers, 1.2×10⁶ s (~14 days) for Schrödinger, 6.7×10⁵ s (~7.8 days) for Allen-Cahn, and 2.4×10⁶ s (~27.8 days) for Diffusion-Sorption. While this is a one-time post-training cost, days-to-weeks of computation is a severe limitation that the paper itself characterizes as "unquestionably the running time." Moreover, for Burgers' equation, the residual bound after 10⁴s is 1.30×10¹, which is 130× worse than the bound after 2.8×10⁵s (1.03×10⁻¹), meaning the method requires the full runtime to produce meaningfully tight certificates. The paper does not discuss whether parallelization (branches are independent) or GPU acceleration could reduce these times, nor does it provide a Pareto-style analysis of bound tightness vs. runtime.

3. **Scalability beyond 2D domains is entirely unaddressed.** All four PDEs have a 2D spatio-temporal domain (t + one spatial dimension). The greedy branching splits each subdomain into 2^{d₀} subdomains per branch; for d₀=2 this is N_d=4, but for d₀=3 it becomes 8, and for d₀=4 it becomes 16—and the number of required branches N_b likely increases as well due to looser bounds. The paper mentions higher-dimensional PINNs (Navier-Stokes, Gray-Scott) were excluded due to unavailable code/models, but does not provide any experiment or analysis to establish feasibility beyond 2D. Given that runtime is already in days for 2D, the scalability concern is material and undermines the claim that the method is "general, efficient and scalable."

### Minor

1. **Bound tightness gap for well-trained networks is not quantified.** For Burgers' equation, the certified residual bound (1.03×10⁻¹) is ~5.7× larger than the 10⁶-sample MC estimate (1.80×10⁻²). For Schrödinger, the gap is ~7× (5.55×10⁻³ vs. 7.67×10⁻⁴). For poorly trained networks (Allen-Cahn, Diffusion-Sorption), the bounds are near-tight. The paper claims "tightness" but does not discuss what gap is acceptable for practical certification or whether the method is meaningfully tighter for the best-trained PINNs (where certification matters most). This does not invalidate the contribution but warrants discussion.

2. **Greedy branching relies on empirical min/max estimates that could be inaccurate.** Algorithm 1 uses N_s random samples to estimate the true min/max of the function over each subdomain. These estimates are themselves approximations, and the algorithm's behavior when empirical estimates are inaccurate (e.g., in higher dimensions where N_s may be insufficient) is not discussed.

3. **No confidence intervals or error bars for Monte Carlo estimates.** The MC max estimates in Table 1 are reported as point estimates without any uncertainty quantification. Reporting confidence intervals would help assess whether the certified bound is actually tight or merely close to a noisy empirical estimate.

### Trivial

- The notation for the PDE residual f and the PINN residual f_θ is slightly overloaded (the same symbol f is used for both), though the paper clarifies the distinction.
- Timing results are reported from a single run on a MacBook Pro; it is unclear whether parallelization across branches was used, though the branches are independent.

## Nice-to-Haves

- A Pareto curve of certified bound vs. runtime (varying N_b) for at least one PDE, allowing readers to assess the cost-tightness trade-off.
- An ablation comparing greedy branching against uniform branching at the same total number of subdomains, to quantify the advantage of the adaptive strategy.
- A simple 3D PDE experiment (e.g., 2D diffusion + time) even if the runtime is prohibitive—reporting the boundary of feasibility would itself be informative.
- Discussion of whether parallelization across independent branches or GPU computation could reduce runtime.

## Removed Points

These points were flagged for removal based on filtering rules; treat with caution.

- **Missing σ' and σ'' relaxation details (Critic's Point 4):** The critic claims that the paper "never specifies what these relaxations are" for σ' and σ'', making the method irreproducible. **Removed per instruction:** The parser strips appendix and supplementary material from all papers. These technical details (linear relaxation formulas for σ'(y) and σ''(y) given pre-activation bounds) are standard in the CROWN literature and would expectedly reside in the original appendix. The paper states "we need to be able to linearly relax σ' and σ'' given pre-activation bounds" (Section 5), indicating these exist in the full submission.

- **Table 2 comparison is unfair (sub-point of Critic's Point 2):** The critic claims "the runtime limits are arbitrary (150s, 100s, 10⁴s) and the best method wins by definition on those allocations." **Removed:** This is factually wrong. Table 2 compares all three methods under *identical* runtime budgets. ∂-CROWN achieves bounds 13.0 vs. 2780 (IBP) and 178 (LiRPA) for the residual — a clear win. The experimental design is standard and sound.

- **"The method certifies a poorly trained network" for Diffusion-Sorption (Critic's comment in abstract notes):** The critic notes that the Diffusion-Sorption case "certifies a poorly trained network," implying this is a weakness. **Removed:** This is a finding about the PINN's training quality, not a weakness of the certification method. If anything, it demonstrates the method's value by catching bad networks that sampling-based evaluation would miss.

- **Missing related work:** The critic did not raise this, but the general instruction is to not mention missing related works. Not applicable.

- **Formatting/style nitpicks:** None were raised that warrant removal.

## Novel Insights

The most noteworthy synthesis emerging from the reviews concerns the asymmetric tightness profile across PDEs and training quality: the method produces near-tight certificates for poorly trained networks (Allen-Cahn, Diffusion-Sorption) where the residual is already large, but shows a ~5-7× gap for well-trained networks (Burgers, Schrödinger) where certification would be most valuable for deployment decisions. This suggests that the primary contribution of ∂-CROWN may be in *flagging unreliable PINNs* (where loose bounds would be too optimistic) rather than in providing tight guarantees for already-accurate ones. Combined with the days-long runtime, this positions the method as a diagnostic/validation tool for small-dimensional PINNs rather than a production certification pipeline. The reviewers converge on the view that the technical contribution is real and non-trivial, but its practical significance is substantially narrower than the paper's framing suggests.

## Suggestions

- Provide a Pareto analysis of certified bound vs. runtime for at least one PDE (varying N_b) so users can evaluate the cost-tightness trade-off.
- Add a simple 3D experiment (e.g., 2D diffusion + time), even if it shows the method becomes infeasible—that finding is valuable information.
- Quantify the correlation in Figure 2 (e.g., Spearman rank correlation) and discuss under what PDE conditions a residual certificate translates to a meaningful solution error guarantee.
- Clarify whether the reported runtimes are serial or parallelized across branches, and discuss the potential for GPU acceleration or branch parallelism.
- Add a succinct characterization of which PDE structures ∂-CROWN can handle (order, nonlinear terms, activation types) to help readers assess applicability to their own problems.

## Score and Decision

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>