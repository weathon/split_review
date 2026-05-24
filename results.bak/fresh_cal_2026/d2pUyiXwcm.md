Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper introduces SCaSML, a framework that improves pre-trained surrogate models (PINNs, GPs) for high-dimensional semi-linear parabolic PDEs at inference time without retraining. The key idea is to derive a Structural-preserving Law of Defect — a new PDE that exactly characterizes the surrogate's error — and solve it using Multilevel Picard (MLP) simulation, which is efficient because the defect PDE inherits the semi-linear structure of the original problem. The authors prove that the final error is bounded by the product of surrogate and simulation errors, yielding an improved convergence rate. Experiments on several PDEs up to 160 dimensions demonstrate 20–80% error reduction across multiple surrogate architectures.

## Strengths

1. **Novel derivation of the Structural-preserving Law of Defect (Fact 2.3, Section 2.2).** The paper derives an exact PDE governing the surrogate's error that preserves the semi-linear structure of the original problem. This is a principled theoretical contribution that is clearly distinguished from classical defect-correction methods (which rely on mesh-refinement hierarchies unavailable for neural nets) and iterative Newton-type approaches (which suffer from nested Monte Carlo convergence degradation). The paper explicitly explains why these prior approaches are unsuitable and why the proposed exact, single-step correction avoids their pitfalls (Section 2.2, lines 146–151).

2. **Provably accelerated convergence rate (Theorem 2.5, Corollary 2.6).** The paper proves that the global L² error of SCaSML is bounded by the product of the MLP simulation error and the surrogate error. This yields an improved scaling law: if the surrogate achieves O(m^{−γ}) with m training points, SCaSML achieves O(m^{−γ−1/2+o(1)}) with the same total budget — better than both the surrogate alone and a naive MLP solver. This is a clean theoretical result, and Corollary 2.6 is empirically validated in Figure 4, which shows steeper log-log slopes for SCaSML across dimensions 20–80 on the viscous Burgers equation.

3. **Consistent empirical error reduction (20–80%) on PDEs up to 160 dimensions.** Table 1 shows that SCaSML achieves the lowest relative L², L^∞, and L¹ errors across all four problem families (LCD, VB-PINN, VB-GP, LQG, DR) and all tested dimensions. For example, on the 60d VP-PINN, the relative L² error drops from 3.95×10⁻² (surrogate) to 2.88×10⁻² (SCaSML); on 80d VP-GP from 2.66×10⁻¹ to 1.52×10⁻¹. Statistical significance is reported (p ≪ 0.001, Appendix G.4), and inference-time scaling plots (Figure 3b) confirm that accuracy improves with additional Monte Carlo samples.

4. **Versatility across surrogate architectures (PINN and Gaussian Process).** SCaSML is tested with both Physics-Informed Neural Networks (Section 3.1, 3.2) and Gaussian Process regressors (Section 3.2, Table 1 VP-GP rows). In the VB-GP case, error reduction ranges from 42.7% to 57.5% across dimensions, demonstrating that the framework works as a plug-and-play corrector not tied to a specific ML model.

5. **Clear differentiation from prior work and thoughtful framing.** Section 2.2 explicitly contrasts the method with classical finite-element defect correction (no polynomial error expansion for neural nets), iterative Newton/quasi-Newton schemes (nested Monte Carlo causes degraded convergence from O(N^{−1/2}) to O(N^{−1/8})), and the distinction between training (global map) and inference (targeted refinement) is formalized in Remark 2.2.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Strong theoretical assumptions (Assumption 2.4) are not guaranteed for neural network surrogates.** The theoretical analysis relies on the surrogate error being uniformly bounded in L^∞ and W^{1,∞}, and the PDE residual ε being bounded proportionally. For neural network surrogates trained with non-convex losses, such uniform bounds — especially on gradients and second derivatives — are not guaranteed, and in high dimensions they may be particularly fragile. The paper acknowledges that the analysis is under these assumptions (line 191: "For simplicity, we present results for the case μ = 0 and σ = sI_d") and the experiments partially bridge the gap empirically, but there is no discussion of when the assumptions might break (e.g., surrogates with large gradient oscillations) or whether the method would still work in those regimes. This does not invalidate the contribution — the product-form error bound is a clean structural result — but it limits the theoretical certification of the method for the model classes used in practice.

2. **Sensitivity of the correction step to surrogate derivative quality is not characterized.** Computing the residual ε (Equation 6) requires evaluating the surrogate's first- and second-order derivatives (the Laplacian appears in ℒ). If the surrogate is trained primarily to match function values (as GPs often are, or PINNs with imperfect gradient regularization), the derivative estimates may be inaccurate, potentially introducing systematic error into the defect PDE. The paper acknowledges this indirectly by using Hutchinson's method for the HJB problem (sampling d/4 dimensions) and computing the full Laplacian for the DR problem, but does not analyze how errors in ∇û or Hess(û) propagate through the correction. The experiments show net improvement, which provides indirect evidence of robustness, but a controlled ablation varying derivative accuracy would strengthen the evidence.

3. **Corollary 2.6's scaling argument is simplified relative to MLP's actual complexity.** The reasoning in Section 2.4 derives the improved rate O(m^{−γ−1/2}) by assuming the simulation error decays as O(m^{−1/2}), but MLP's true complexity involves multiple levels, sample allocation across levels, and the interaction between levels and dimension. The paper references Appendices F and E for the rigorous treatment, and the empirical verification in Figure 4 supports the qualitative claim. However, the main-text presentation glosses over these nuances, and the independence assumption underlying the product bound (Equation 9) — that the surrogate error and simulation error factor — is asserted rather than discussed in terms of potential coupling (since both involve the same surrogate û).

4. **Runtime comparison in the main text is not cost-controlled.** In Table 1, SCaSML runs 2–6× longer than naive MLP and much longer than the surrogate alone. The paper claims "improved scaling law" and "elastic compute," but the primary tabular comparison does not control for total runtime. The authors reference a fixed-budget comparison in Appendix G.7 (line 247: "fixed-budget efficiency comparisons (Appendix G.7), are shown in the Appendix G"), but this important comparison is not given space in the main paper. Given that the "inference-time scaling" narrative is central to the paper's framing, a time-to-accuracy plot or fixed-budget table in the main text would directly support the claims and preempt fairness concerns. The paper is transparent about the runtime overhead, and the appendix addresses this, but the presentation could be more self-contained.

### Trivial

- The notation alternates between "SCaSML" and "SCA²SM¹" (and "SCa²SM¹") without clear explanation. The superscript notations appear in Table 1 and some equations but are never defined in the body — they seem to be a lab internal shorthand that leaked into the manuscript.

## Nice-to-Haves

- **Surrogate-derivative ablation study.** An experiment where surrogate derivatives are artificially corrupted (or a surrogate is trained without gradient regularization) would show how robust the correction is and make a stronger case for practical use.
- **Fixed-budget comparison in the main paper.** Moving a "time-to-accuracy" plot or fixed-budget table from Appendix G.7 to the main text would directly support the "inference-time scaling" narrative.
- **Concrete example of the defect PDE.** Expanding the definition of \~F in (7) with a concrete F (e.g., F(u) = u²) would improve expository value.
- **Code release.** A public repository would increase reproducibility and impact, given the complexity of MLP implementations.
- **Limitations section.** A brief paragraph acknowledging the smoothness requirements on the surrogate and the computational overhead for very expensive neural network surrogates would improve candor.

## Removed Points

*These points were raised by the reviewers but are removed per the filtering rules. They are recorded here for transparency; treat them with caution.*

- **Missing related work section:** The section was removed by the parser; it exists in the original submission. Per the hard rules, this criticism must be removed.
- **Missing appendix content / proofs:** The parser strips these sections from all papers; they exist in the original submission. Removed per hard rules.
- **"SCA²SM¹" never defined as typo:** The notation appears consistently in Table 1 and some equations; this is a formatting artifact rather than a genuine omission. The paper clearly defines "SCaSML" in the abstract and introduction.
- **Criticism that baselines may be unfair if the asymmetry favors the author's method:** The asymmetry (SCaSML uses more runtime) actually disfavors SCaSML, not the baseline. Per the hard rule on asymmetric comparisons, this is removed.
- **Reproducibility concern about undisclosed hyperparameters or implementation details:** Hyperparameters are provided in the experimental setup sections (3.1–3.4). The paper states it uses JAX and DeepXDE. Per the hard rule, trivial reproducibility nitpicks are removed.
- **Strength Finder's generic strengths** ("this paper addressed an important problem," "the paper targets an interesting question"): Removed as generic/superficial/sycophantic. Only strengths with specific, concrete content are retained.

## Novel Insights

The most interesting insight emerging from the reviews is the subtle interplay between the surrogate's derivative quality and the correction's effectiveness. The method's core hypothesis is that the defect PDE is easier to solve because the residual ε is small — but ε involves second derivatives of the surrogate, which may not be small even when function values are reasonable. This creates a potential failure mode that the paper does not explore: a surrogate that approximates the solution well pointwise but has oscillatory derivatives could produce a large residual ε, negating the variance reduction that the theory depends on. Conversely, if such surrogates still benefit from the correction (as the empirical results across GP and PINN surrogates suggest), then the method may be more robust than the theoretical assumptions would imply. Characterizing this gap — when the method works empirically despite assumptions not being met — would be a valuable direction for future work. Additionally, the parallel between SCaSML and control variate methods (briefly noted in the conclusion) is deeper than the paper acknowledges: the surrogate is effectively a (biased) control variate, and the defect PDE correction is a form of debiasing through simulation. Making this connection explicit could connect the work to a broader statistical literature.

## Suggestions

1. Add a brief discussion in Section 2.4 about the conditions under which Assumption 2.4 might fail and whether the method would still be expected to work.
2. Include a fixed-budget comparison or time-to-accuracy plot in the main text (moving from Appendix G.7) to directly support the inference-time scaling narrative.
3. Add a sentence or footnote explaining the "SCA²SM¹" notation when it first appears in Table 1.
4. Expand the derivation in (7) with a concrete example of F (e.g., F(u) = u²) to illustrate how the defect PDE works.

## Score and Decision

**Calibration anchors:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| J8o0w8WrcE (PDE Hypernetwork PINNs) | 3.00 | R1 | Much weaker — method not well validated |
| 7noPldewfE (Projective Symbolic Regression) | 2.50 | R1 | Much weaker — limited results |
| q97pnOxCZB (SPDEBench) | 3.00 | R1 | Much weaker — benchmark paper, no method |
| ENAfBpMc6y (DRR-Net) | 4.80 | R1 | Weaker — clarity issues, incomplete baselines |
| IDJabw9ri3 (GP Priors for BVPs) | 5.00 | R1 | Weaker — narrower scope, less theory |
| z7ilspv4uH (PDE-PFN) | 5.50 | R1 | Weaker — limited to 2D, weaker theory |
| l01eG3Qikl (DriftLite) | 6.00 | R2 | **Comparable** — similar inference-time scaling idea, similar runtime overhead issues; this paper is stronger empirically (160d vs 30d) and in theoretical depth |
| bj0dcKp9t6 (Multifidelity SBI) | 6.50 | R2 | **Comparable** — similar multi-fidelity spirit; this paper has stronger theory, SBI has better runtime analysis |
| Ahdsg2nkNH (Multilevel Control Functional) | 8.00 | R1 | Stronger — cleaner theory, tighter focus, but tackles a different (easier) problem |

**Round 1 bracket:** 5.0–7.5 (well above the 3.0 weak papers, below the 8.0 top tier)

**Round 2 narrowing:** Compared to DriftLite (6.0), this paper is stronger in empirical scope (up to 160d vs 30d), has more novel theory (product-form error bound), and has better empirical validation across multiple PDE families and surrogate types. Compared to Multifidelity SBI (6.5), the theoretical contribution is deeper but the presentation has similar issues (key comparison deferred to appendix). The paper sits between these two anchors, closer to the upper one.

**Final score: 6.5**

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>