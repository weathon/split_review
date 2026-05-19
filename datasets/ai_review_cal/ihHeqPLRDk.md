- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 5, 3, 6
Now I have all the information needed. Let me produce the consolidated review.

## Summary

This paper proposes SincKAN, a KAN variant that replaces cubic spline activation functions with a learnable linear combination of Sinc basis functions at multiple step sizes, augmented by a normalized coordinate transformation and a linear skip connection. Through experiments on 8 function approximation tasks and 5 PDE benchmarks, the authors show SincKAN achieves competitive accuracy, with particularly striking results on boundary layer problems where other methods fail entirely (e.g., relative L2 error of 5.48×10⁻³ vs. >1.0 for all baselines at ε=1000).

## Strengths

1. **Dramatic advantage on extreme boundary layer PDEs (Table 3, ε=1000).** For the 1D boundary layer problem with ε=1000, SincKAN achieves a relative L2 error of 5.48×10⁻³, while all four baselines (MLP, modified MLP, KAN, ChebyKAN) yield errors above 1.0 (most above 9.87). This is the single strongest result in the paper and directly validates the core motivation that Sinc methods handle sharp gradients well. The convergence curves in Figure 4 substantiate this.

2. **Consistently strong function approximation across diverse cases (Table 1).** SincKAN achieves the best RMSE in 7 out of 8 function approximation tasks (sin-low, sin-high, bl, double exponential, multi-sqrt, piece-wise, spectral-bias), covering low-frequency, high-frequency, singular, discontinuous, and spectral-bias functions. This breadth supports the claim of general-purpose utility.

3. **Well-motivated architectural components with ablation validation (Table 4).** The three design innovations (multi-h interpolation, normalized coordinate transformation, linear skip connection) are each grounded in known challenges of Sinc numerical methods. The ablation study shows that the normalized transformation (γ=tanh) is critical: configurations without it perform poorly (errors >0.07), while the best configuration on Burgers' equation (6.21×10⁻⁴) uses it.

4. **Honest treatment of limitations.** The paper prominently acknowledges the derivative inaccuracy issue (end-point degradation in Sinc derivative approximation) in its own Limitations section, explaining why SincKAN achieves "good results but not the best results for some cases" in PDEs, and discusses the MIM approach as a potential future workaround.

## Weaknesses

### Fatal

None.

### Major

1. **Missing experimental details undermine comparison fairness.** The paper reports no layer counts, width per layer, total parameter counts, optimizer choice, learning rate schedule, number of training iterations, or data split details for any method (SincKAN or baselines). Without these, it is impossible to determine whether SincKAN's wins are due to the proposed mechanism or simply having more parameters, more training, or better-tuned hyperparameters. For a paper introducing a new architecture, reporting at minimum parameter counts and training budgets is standard practice. The paper's core experimental claims rest on comparisons that cannot be independently verified or reproduced as presented.

2. **Derivative inaccuracy is a significant but unaddressed limitation for the PINN contribution.** The paper acknowledges that "approximating derivative by Sinc numerical methods is always inaccurate in the neighborhood of the Sinc end-points" and that this "limits the capability of SincKAN" for PDEs. However, this issue is never quantified: there is no analysis of derivative error across the domain, no demonstration that the degradation does or does not harm PDE solutions in practice, and no workaround is implemented or tested (the MIM suggestion is future work only). Since half the paper's claimed contribution is to PINNs, and the PDE results show SincKAN is best on only 2 of 5 problems (with two cases where modified MLP outperforms it by 30×), the reader cannot assess how severely this limitation undercuts the PINN claims. The authors should at minimum quantify derivative error for a representative PDE and show its spatial distribution.

3. **The multi-h claim is not isolated in the ablation.** The paper claims that combining multiple step sizes yields "a more accurate approximation than the optimal h" (Section 2.3) and that multi-h is "the main reason for SincKANs' superior ability in approximating complex smooth functions" (conclusion). However, the ablation study (Table 4) does not include a single-h baseline. The h-selection experiment (Section 3.1, Figure 2) only compares multi-h configurations against each other, not against a version with one learned/tuned h. Without this control, the unique benefit of the multi-h approach over a well-chosen single h is not substantiated.

### Minor

1. **Theory-practice framing requires more precision.** The convergence theorems in Section 2 (Theorem 1, Theorem 2) are for *classical* Sinc interpolation where coefficients are fixed as function values f(jh). In SincKAN, coefficients are learned parameters. The paper draws motivational connections ("still meets the condition of ψ in Theorem: transformation," line 159), but does not provide a direct analysis of SincKAN's approximation properties as a learned-basis network. This leaves a gap between the theoretical framing and the actual method. The paper would benefit from being transparent that the theorems motivate the architecture choice but do not directly bound SincKAN's error.

2. **Claim of "better results in almost all examples" is overstated for PDEs.** The function approximation results support this (7/8 best), but for the PDE benchmarks (Table 2), SincKAN is best on only 2 of 5 problems. On ns-tg-u and ns-tg-v, modified MLP outperforms SincKAN by roughly 30× (2.14e-5 vs. 6.51e-4 and 1.91e-5 vs. 1.34e-3). The abstract and introduction should qualify this claim accordingly.

3. **No comparison against other learned-basis KANs.** The paper cites WavKAN, FourierKAN, and other KAN variants but only compares against ChebyKAN. While not required, including at least one additional learned-basis KAN would strengthen the case that Sinc functions are specifically beneficial, not just that any non-spline basis helps.

### Trivial

1. No code/data availability statement, which would aid reproducibility.
2. Computational cost (training time, memory usage) of SincKAN vs. baselines is not discussed.
3. The "piece-wise" function is alluded to in Figure 3's caption but the reader must infer its definition.

## Nice-to-Haves

- A single-h SincKAN baseline in the ablation to isolate the multi-h benefit.
- Derivative error quantification for a representative PDE (spatial profile across the domain).
- Parameter counts and training budgets for all methods and all experiments.
- Brief function definitions (sin-low, sin-high, bl, etc.) in the main text for self-contained reading.

## Removed Points

These points were flagged but are removed or downgraded from the main review:

1. **"Theoretical misalignment is a structural flaw that undermines the paper's central claim."** (Harsh Critic, Critical Issue #1) — This is too strong. The paper presents classical Sinc theory as motivation, not as a proof that SincKAN inherits specific bounds. The paper explicitly notes coefficients are learnable (line 147) and that f is unknown in ML (line 97). The theorems are standard background. The point is retained as a Minor weakness (theory-practice precision) rather than a structural flaw.

2. **"Ablation study undermines the conclusion that the linear skip connection is the most stable approach."** (Harsh Critic) — Re-reading the paper, the conclusion "most stable" is about robustness across both test equations: linear gives 2.44e-4 / 3.12e-3 while SiLU gives 1.60e-4 / 8.90e-3 (much worse on Burgers). This claim is reasonable as stated. The criticism is not retained.

3. **"The paper conflates Sinc interpolation with SincKAN throughout."** (Harsh Critic) — The paper uses standard terminology (e.g., "Sinc interpolation" as the broader numerical method) and clearly distinguishes the architecture. The retained Minor weakness #1 above captures the relevant nuance.

4. **Strength: "Theoretical grounding for handling singularities directly supports SincKAN."** (Strength Finder) — This overstates the connection. The theorems are for classical Sinc interpolation with fixed coefficients, not for the learned-basis network. Retained as a partial strength only because the empirical results independently validate the claim.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a consistent pattern: the paper has compelling empirical results (especially on boundary layers) but the evidence is weakened by insufficient experimental transparency. The reviewers agree on the core strengths and the same set of actionable gaps.

## Suggestions

1. **Add a reproducibility appendix** reporting for each experiment: network architecture (layers, width, total parameter counts for all methods), optimizer and learning rate schedule, number of training steps, and data sampling strategy. This is the single highest-impact improvement.

2. **Quantify the derivative degradation** for at least one PDE benchmark (e.g., Burgers' equation). Show the error in the PDE residual and its spatial distribution across the domain, comparing SincKAN against the best baseline. This would clarify whether the acknowledged limitation is practically significant or negligible for the tested problems.

3. **Add a single-h baseline** to the h-selection experiment. Compare multi-h SincKAN against the best attainable single-h version (h tuned per problem) on the same set of functions to substantiate the claim that multi-h is beneficial beyond convenience.

4. **Tighten the scope claims.** Replace "better results in almost all examples" with a more precise statement that reflects the PDE results (excellent on boundary layers, competitive but not always best on other PDEs).
