Now I have a thorough understanding of the paper. Let me compose the consolidated review.

## Summary

This paper introduces ∂-CROWN, a post-training certification framework for Physics-Informed Neural Networks (PINNs) that provides guaranteed upper bounds on the residual, initial condition, and boundary condition errors across the *continuous* spatio-temporal domain — moving beyond the point-wise Monte Carlo estimates standard in prior work. The technical core extends CROWN-style verification to handle partial derivatives of neural network outputs (first and second order) in O(L) time via a hybrid backward-forward scheme, and uses McCormick envelopes to bound nonlinear functions of these derivatives (the PDE residual). Experiments on four PDEs (Burgers', Schrödinger, Allen-Cahn, Diffusion-Sorption) show certified bounds that approach high-density empirical estimates, and the Diffusion-Sorption case dramatically illustrates the need for certification: 10⁴ Monte Carlo samples estimate the max residual at 1.1×10⁻³ while 10⁶ samples reveal it to be 21.09.

## Strengths

- **Formal correctness conditions for PINNs with worst-case guarantees (Definition 1).** The paper defines three global error conditions bounding the residual, initial, and boundary errors over the *continuous* domain, establishing a principled framework beyond the point-wise empirical evaluation standard in prior PINN work. This enables deployment-grade guarantees analogous to residual tolerance in classical numerical solvers.

- **Efficient hybrid bound propagation for partial derivatives.** The ∂-CROWN framework derives linear bounds on first and second partial derivatives of the solution network in O(L) time (Theorems 1–2, Figure 1) using a hybrid backward-forward scheme that avoids the O(L²) complexity of full back-propagation (e.g., LiRPA). This is the core technical contribution and directly enables scalable certification of the PDE residual, which involves nonlinear functions of these derivatives.

- **Compelling empirical motivation for certification.** The paper provides concrete evidence that empirical Monte Carlo bounds are unreliable: for the Diffusion-Sorption PINN, increasing samples from 10⁴ to 10⁶ changes the estimated maximum residual error from 1.1×10⁻³ to 21.09 — a 20,000× discrepancy (Table 1, lines 17, 242). This stark finding validates the paper's core premise that point-wise evaluation is insufficient for deployment decisions.

- **Tight certified bounds across diverse PDEs.** The framework produces certified upper bounds that closely match empirical lower bounds for initial and boundary conditions across all four PDEs (e.g., Burgers initial condition: certified 2.63×10⁻⁶ vs. empirical 1.59×10⁻⁶, Table 1). For residual errors, certified bounds are within roughly one order of magnitude of the 10⁶-sample empirical maxima (Burgers: 1.03×10⁻¹ vs. 1.80×10⁻²; Schrödinger: 5.55×10⁻³ vs. 7.67×10⁻⁴), demonstrating practical tightness given the hardness of worst-case certification.

- **Favorable comparison against general verification baselines.** Under fixed runtime limits (Table 2), ∂-CROWN achieves a residual bound of 1.30×10¹, which is 214× tighter than IBP (2.78×10³) and 13.7× tighter than LiRPA (1.78×10²), showing the advantage of a custom method over off-the-shelf neural network verifiers applied to the PINN residual computation graph.

## Weaknesses

### Fatal

None.

### Major

- **Gap between what is certified and what practitioners care about.** The paper certifies upper bounds on the residual error |f_θ|, initial condition error, and boundary condition error (Definition 1). These do *not* directly bound the solution error |u_θ − u| (the quantity practitioners ultimately care about), because for general nonlinear PDEs a small residual does not guarantee convergence to the correct solution branch. The paper transparently acknowledges this (Section 4.2, line 312: "there is no formal guarantee related to |u_θ − u| within our framework") and provides a correlation experiment on Burgers' equation. Nevertheless, the title, abstract, and framing around "certifying PINNs" create an expectation of solution-level guarantees that the framework does not deliver. The connection between residual and solution error remains PDE-specific and empirical, which undercuts the strongest practical interpretation of the results.

- **Prohibitive absolute runtime for residual verification contradicts the "efficient" claim.** From Table 1: residual verification takes 2.8×10⁵ seconds (~3.2 days) for Burgers, 1.2×10⁶ seconds (~14 days) for Schrödinger, 6.7×10⁵ seconds (~7.8 days) for Allen-Cahn, and 2.4×10⁶ seconds (~28 days) for Diffusion-Sorption, all on a MacBook M1 Max CPU. The paper acknowledges this (Section 6, line 365: "One of the limitations of our method is unquestionably the running time"), and the "efficient" claim in the title is relative to even slower alternatives (LiRPA, IBP). However, for a *post-training* certification step intended for practical deployment verification, runtimes measured in days to weeks are prohibitive. The 2 million greedy splits used for residual cases explain the cost, but the framing does not adequately hedge the efficiency claim.

### Minor

- **No direct comparison between greedy and uniform branching.** The paper states that "a uniform sampling strategy would be significantly more computationally expensive" (Section 4.4, line 342) and shows branching density plots (Figure 2), but provides no runtime or tightness comparison between greedy and uniform splitting. Without a quantitative baseline, this claim is unsupported. A simple comparison on one PDE would strengthen the evidence.

- **Adaptation of baselines (IBP/LiRPA) for the residual comparison is not described.** The efficiency comparison (Table 2) pits ∂-CROWN against IBP and LiRPA for bounding the PINN residual. Since these methods were originally designed for standard network outputs, not for networks whose outputs are nonlinear functions of partial derivatives, the paper should explain how they were extended to handle the computation graph of f_θ (which involves ∂_t u_θ, ∂_x u_θ, ∂_x² u_θ, and their nonlinear combinations). This affects reproducibility of the comparison.

- **The solution-error correlation analysis (Figure 3) is limited.** The scatter plot for Burgers' equation shows correlation between residual and solution errors across training epochs, but (a) covers only one PDE, (b) uses only 95% confidence intervals on noisy empirical estimates, and (c) does not bound the ratio. The paper's conclusion that "a similar correlation holds for |u_θ − u|" (line 315) is appropriate in its caution, but this experiment does not provide a usable guarantee.

### Trivial

- The text contains a few minor issues: "Allan-Cahn" in the abstract/contribution list should read "Allen-Cahn" (the paper uses "Allan" in the introduction and "Allen" in the experiment section — the standard spelling is "Allen-Cahn"). The abstract says "Allan-Cahn" while the experiment section correctly uses "Allen-Cahn."

## Nice-to-Haves

- A direct comparison of greedy vs. uniform branching (same N_b budget) on one PDE would quantitatively validate the claim that greedy is more efficient.
- The relaxation of σ' and σ'' for tanh activations is mentioned (line 270) but the actual relaxation functions are not given in the main text — providing them (or pointing to the appendix) would aid reproducibility.
- Extending the framework to handle cross-derivatives (∂_{x_i x_j} u_θ), which the paper notes would be "trivial to derive" (line 174), would broaden applicability to more complex PDEs.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Missing standard errors / confidence intervals on bounds:** The critic asks for confidence intervals on certification bounds. Certification bounds are deterministic given the relaxation method; this is not standard practice in the verification literature and reflects the wrong class of expectations.
  
- **Dependence on PINN quality:** The critic claims the method "only works if the PINN is already well-trained." The paper certifies residual error — if the PINN is bad, the certified bound will be large, which is itself useful information for rejecting the model. This is a misunderstanding of the contribution.

- **Fully connected network limitation:** The paper explicitly states this scope (line 33: "applicable to any PINN where the solution is modeled by a fully connected network"). Criticizing a stated design choice as a weakness is scope creep.

- **Missing tanh relaxation details:** This is the type of implementation detail that would normally appear in an appendix (stripped by the parsing pipeline) or in the original CROWN literature that already handles tanh relaxations. Not a substantive weakness.

- **Generic formatting/style nitpicks:** Removed per instructions.

## Novel Insights

The most insightful observation across both reviewers is that the paper's fundamental technical contribution (hybrid bound propagation for neural network derivatives) is solid and novel, yet the framing tension between "certification" and "solution error" runs deeper than the paper's own acknowledgment suggests. The Diffusion-Sorption case is particularly instructive: it shows that without certification, one can be misled by orders of magnitude, but with certification, the runtime cost is enormous. This reveals an inherent tension in the PINN verification problem — achieving meaningful guarantees may require either substantially tighter bound propagation (to reduce branching depth) or theoretical advances connecting residual bounds to solution error for broader PDE classes. The paper does the right thing by surfacing both sides of this tension transparently.

## Suggestions

- Re-title to better reflect the scope, e.g., "Residual Certification of Physics-Informed Neural Networks" or "Efficient Bounding of PINN Residual Errors," to avoid the expectation of solution-level guarantees.
- Add a small-scale numerical comparison between greedy and uniform branching on one PDE to support the claim that greedy is more efficient.
- Describe how IBP and LiRPA were adapted for the residual computation graph in the efficiency comparison (Table 2), to ensure reproducibility.
- Consider discussing, even speculatively, which classes of PDEs might admit a theoretical link between the certified residual bound and solution error, building on the work of Ryck et al. (2022) already cited.

## Score and Decision

This paper makes a genuine technical contribution: it is the first to extend neural network verification to bound partial derivatives of PINNs, and it demonstrates the practical necessity of doing so through compelling negative examples (Diffusion-Sorption). The limitations are real — the residual-to-solution gap and the prohibitive runtime — but the paper is transparent about both. The work is well-positioned within the PINN literature, the methodology is sound, and the experiments support the claims with appropriate caveats. This is a solid paper that should be accepted.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>