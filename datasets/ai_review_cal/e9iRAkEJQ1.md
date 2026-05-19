- Decision: Reject
- Avg Score: 4.75
- Scores: 3, 5, 8, 3
I now have a thorough understanding of the paper and all reviewer claims. Let me construct the final consolidated review.

## Summary

This paper identifies solutions to the eikonal equation as a target space for flow-map approximation, proves a dimension-independent approximation rate (Theorem 2.1), and develops the finite flow method—a learning-based solver that implements this hypothesis space numerically. The rate estimate avoids an explicit curse of dimensionality in the depth parameter \(T\), contrasting with prior flow-map results. Experiments demonstrate advantages in spatial-resolution robustness, transferability among similar problems, and robustness to solution regularity compared to FMM and PINN baselines.

## Strengths

- **Theorem 2.1: Dimension-independent approximation rate.** The bound \(\inf_{\hat u\in\mathcal{H}_T^u(\mathcal{W},\varepsilon)}\|u-\hat u\|_{L^1(B(x_s,1))} \leq C_1\max\{C_u-T,0\}^2 + C_2(4E_{\mathcal{W}}(\tilde V_u))^{\frac{1}{C_u(L+1)+2}} + C_3\varepsilon\) has no explicit dependence on the ambient dimension \(d\), which is a genuine advance over prior flow-map rates (e.g., Ruiz-Balet & Zuazua 2023 with \(\mathcal{O}(T^{-C/d^2})\)). The constants are explicit, and the proof sketch is coherent.

- **Demonstration that flow-map complexity differs from classical smoothness-based measures.** The paper shows concretely (Section 2.3) that the approximation rate depends on dynamical structure (through \(C_u = \inf|\nabla u|\) and the smoothness of \(\tilde V_u = -|x-x_s|\nabla u/|\nabla u|\)) rather than on the smoothness of \(u\) itself. The radial-function example and Proposition B.3 provide evidence that functions with arbitrarily low higher-order smoothness can have smooth \(\tilde V_u\), directly contrasting Jackson-type estimates.

- **Effective algorithm with clear experimental advantages.** The finite flow method (Section 3) is a clean algorithmic consequence of the representation. Experiments show: (i) robustness to spatial resolution—MAE nearly constant across grid sizes while FMM error grows linearly (Figure 3a); (ii) transferability—pre-trained networks reduce training steps by more than half for small perturbations while FMM cost stays constant (Figure 4); (iii) better regularity robustness than PINN methods on a sharply oscillatory cost function (Table 1: best MAE \(2.1\times10^{-3}\) vs PINNeik \(9.2\times10^{-3}\) and NES-OP \(9.8\times10^{-3}\) for \(f_2\)).

- **Empirical validation of the quadratic error-depth relation.** Figure 1 shows log-log plots between \((\tau_{\max}-T)\) and empirical approximation error for three cost functions; slopes align with the quadratic law predicted by Theorem 2.1.

- **Principled handling of the source-point singularity.** The auxiliary parameter \(\varepsilon\) and modified vector field \(\chi_\varepsilon V_u\) (Section 2.2) provide a well-motivated way to avoid the singularity while maintaining the flow-based representation, with Condition (9) ensuring the scheme is controlled.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Loss function justification contains a confusing non-sequitur.** The paper states (line 170): *"Intuitively, as long as the learning rate is small, the flow of \(u_\theta\) will keep converging to a small neighborhood of \(x_s\) during training; otherwise, \(L(\theta)\) will increase during the training steps."* This conflates gradient descent dynamics with the property of the loss landscape and refers to "the flow of \(u_\theta\)" where \(u_\theta\) is a scalar function, not a vector field. The correct justification—available from the paper's own variational formulation (Equation 11 and Proposition A.1)—is that \(u_\theta(x) \geq u(x)\) for all \(x\) (the flow-based representation using any vector field is an upper bound on the true solution), so minimizing \(\|u_\theta\|_p\) drives it toward the true solution from above. This is a clean argument that should replace the confusing sentence. The core idea is correct, but the exposition undermines the method's credibility as stated.

- **Hypothesis space depends on \(f_u\) without sufficient framing.** Definition 2.1 defines \(\mathcal{H}_T^u(\mathcal{W},\varepsilon)\) using \(f_u = |\nabla u|\)—the gradient norm of the specific target function—in the integrand of \(\Gamma_u^{T,\varepsilon}(V)\). In standard approximation theory, the hypothesis class is fixed across targets. The paper acknowledges (line 154) that \(f_u\) is the known right-hand side in the PDE setting, making this dependence natural for the application. However, the theoretical section (Section 2.2) could more explicitly distinguish this setting from classical approximation theory and justify why the dependence on \(f_u\) is appropriate. This is a framing concern, not a technical flaw.

### Trivial
None.

## Nice-to-Haves

- **Wall-clock runtime comparison.** The transferability experiment measures fine-tuning steps vs FMM computation time (Figure 4), but a direct wall-clock comparison between finite flow and FMM (or PINN) for matched accuracy on the same problem would help practitioners gauge practical trade-offs.
- **Higher-dimensional validation.** A small-scale 3D experiment (e.g., radial solution on \(32^3\) vs \(128^3\) grids) would strengthen the scalability claim, which is currently supported only by 2D results.
- **Loss convergence visualization.** Showing loss curves or the evolution of \(u_\theta\) during training would build confidence that the optimization is well-behaved.
- **Discussion of practical choices for Condition (9).** The theorem requires \((2C_u^2+C_u)(4E_{\mathcal{W}}(\tilde V_u))^{1/(C_u(L+1)+2)} < \varepsilon\). Guidance on how to select \(\varepsilon\) and network capacity to satisfy this in practice would aid reproducibility.

## Removed Points

*These points are flagged for removal; treat with caution.*

- **"References missing or incomplete (e.g., Chenghao et al.)"** — The full citation appears in the reference list (line 243). The incomplete appearance is a PDF-extraction artifact. Remove per hard rules.
- **"Missing hyperparameters (architecture, learning rate schedule)"** — Per soft rules, remove nitpicks about trivial implementation details. The paper states batch size (10000) and ODE step size ranges; full architectural details are standard to include but their absence here does not threaten the core claims.
- **Criticisms about the theory being under "Related Work" (section numbering)** — A formatting/style choice, not a substantive weakness.
- **"Could the metric be measuring a proxy?" type speculation** — The harsh critic's notes on this were not substantive; the paper's claims are well-anchored to specific experiments.
- **Several of the "Strengthening the Paper on Its Own Terms" suggestions** — These are absorbed into Nice-to-Haves above or into Minor weaknesses.
- **Strength Finder strength about "this paper addressed an important problem"** — Generic; removed. All other strengths are specific and grounded.

## Novel Insights

The key insight emerging from the reviews is that the paper identifies a fundamental distinction between two notions of complexity for flow-map approximation: classical smoothness (which determines polynomial/neural-network approximation rates) and *dynamical simplicity* (the smoothness of the unit vector field \(\tilde V_u\), which determines flow-map approximation rates). The eikonal equation provides a natural setting where these two measures diverge—solutions with rough \(u\) but smooth \(\tilde V_u\) exist and are approximated efficiently by flows but not by PINNs. This suggests that for PDEs with dynamical structure (characteristic flows), the right measure of "approximability" is not the smoothness of the solution but the smoothness of its characteristic vector field.

## Suggestions

1. Replace the confusing sentence about "learning rate" and "flow of \(u_\theta\)" (line 170) with a clear variational argument: the flow-based representation is an upper bound on the true solution (by the variational principle), so minimizing \(\|u_\theta\|_p\) drives it toward the true solution from above. This single change would substantially improve the paper's clarity.
2. In Section 2.2, add a brief paragraph explicitly stating that \(\mathcal{H}_T^u\) depends on \(f_u\) because \(f_u\) is the known PDE right-hand side, and contrast this with classical approximation theory where the hypothesis class is function-independent.
3. Add a brief discussion of how one might choose \(\varepsilon\) and network capacity in practice to approximately satisfy Condition (9).
