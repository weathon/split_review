Now let me write the final consolidated review.

## Summary

This paper introduces Physics-Informed Normalizing Flows (PINF), a method that extends continuous normalizing flows to solve the Fokker-Planck (FP) equation with diffusion. The key idea is to rewrite the FP equation using a modified drift \(\boldsymbol{\mu}^* = \boldsymbol{\mu} - (\nabla \log p)\mathbf{D} - \nabla\cdot\mathbf{D}\), transforming it into an ODE system via the method of characteristics. A neural network \(\phi_\theta\) representing \(\log p\) is trained via a self-supervised loss that matches ODE-computed densities against the network's own predictions. The method guarantees the normalization constraint on probability densities by construction, which is a known limitation of PINNs.

## Strengths

- **Principled extension of continuous normalizing flows to diffusion.** The derivation in Section 4.1.2 (equations 151–158) shows how the FP equation with nonzero diffusion can be rewritten as an advection equation and solved along characteristic curves via the modified drift \(\boldsymbol{\mu}^*\). This is a conceptually clean bridge between CNFs (which handle only the zero-diffusion Liouville equation) and the full FP equation.

- **Built-in satisfaction of the normalization constraint.** The paper identifies and addresses a genuine limitation of PINN-based PDE solvers. The change-of-variables formula in normalizing flows guarantees \(\int p(\mathbf{x},t)d\mathbf{x} = 1\) by construction for the time-dependent case (Section 4.2), and the combination of RealNVP + ODE evolution enforces it for the steady-state case (Section 4.3). This is a structurally meaningful advantage over PINNs, which rely on soft penalty terms that are often violated.

- **Self-supervised training without labeled data or target samples.** The loss function (Equation 7) requires only samples from the initial distribution \(p_0\) and Monte Carlo estimates of the log-density along ODE trajectories. This eliminates the need for ground-truth density values or data from the target distribution, which is a practical advantage over likelihood-based approaches.

- **Hard constraint for the initial condition.** The network parameterization \(\phi_\theta(\mathbf{x}, t) = \log p_0(\mathbf{x}) + t\, u(\mathbf{x}, t;\theta)\) (Equation 6) enforces the initial condition exactly rather than via a soft penalty, which is a clean design choice.

## Weaknesses

### Major

- **Experimental evaluation is far too narrow to support the paper's claims.** All three test problems have Gaussian closed-form solutions — a time-dependent Gaussian (d=10) and isotropic Gaussians (d=30, 50). The SFP examples (d=30, d=50) are single isotropic Gaussians, which are the simplest possible distributions and do not test whether the RealNVP component can represent non-trivial densities. No multimodal, double-well, or any non-Gaussian steady-state distribution is attempted, despite the paper claiming PINF "can efficiently solve high dimensional time-dependent and steady-state Fokker-Planck equations." Without a non-Gaussian example, it is impossible to assess whether the method scales beyond unimodal Gaussian targets.

- **No baselines or comparisons of any kind.** The paper makes an unsubstantiated claim that "PINN is effective primarily with the dimension \(d \leq 3\)" (line 356) without running a single PINN experiment or citing supporting work. No comparison is made against PINN, KRnet, TNF, finite-difference methods, or any other baseline. Without baselines, the paper's claims of accuracy, efficiency, and architectural superiority are unverifiable. This is the most critical omission.

- **Quantitative metrics are missing or unverifiable.** For the TFP case (d=10), the MAPE is shown only as a visual panel in Figure 2 with no numerical value reported. For the SFP case, "relative error below 0.2%" is stated without a table, explicit calculation method, error bars across random seeds, or any supporting numbers. Standard practice for deep learning PDE solvers requires reporting quantitative errors (e.g., relative \(L^2\) error, KL divergence) with variance over multiple runs.

- **Claim about PINN limitations is unsupported.** The statement that "the PINN is effective primarily with the dimension \(d \leq 3\)" (line 356) is presented as fact with no citation or experiment. Since this claim frames the motivation for PINF's high-dimensional claims, it should be substantiated.

### Minor

- **No discussion of computational cost or ODE solver details.** The training procedure (Algorithm 2) requires evaluating \(\nabla\phi_\theta\) (and its divergence) at every ODE solver step, which involves repeated gradient computations through the neural network. The paper does not specify the ODE solver type, tolerance settings, step size, or number of function evaluations. No wall-clock time or scaling analysis is reported, despite claims of efficiency.

- **Self-consistency training lacks convergence analysis.** The training is a fixed-point iteration: the ODE solver uses the current network to compute \(\log p_\text{ode}\), which is matched back to the network. The paper provides no argument (contractivity, convexity, or otherwise) that the minimizer of this loss satisfies the FP equation, or that the loss can be driven to zero for nontrivial cases. While theoretical convergence proofs are not standard for deep learning PDE solvers, the lack of any analysis — even empirical validation on a grid-based PDE residual — is a gap that weakens trust in the method's correctness.

- **ODE integration time horizon in Algorithm 3 is unexplained.** The steady-state ODE is integrated from 0 to 1 with no justification. Since the steady-state solution is invariant under time shifts, any positive horizon would suffice, but sensitivity to this choice is not explored.

- **No ablation studies.** The choice of ResNet architecture with quadratic potential terms is borrowed from optimal control literature. No ablation compares this to a standard MLP of similar size to isolate the benefit of these design choices. Hyperparameter sensitivity (learning rate, network width/depth, batch size) is not explored.

### Trivial

- The term "causality-free" is cited to Nakamura (2020) but its specific meaning (time-independent parallel sampling vs. time-marching schemes) could be stated more explicitly.
- In Algorithm 3, the notation \(\phi_\theta^f\) and \(\phi_\theta^b\) for forward/backward RealNVP transformations is used without explicitly linking it to equations (281)-(290); a brief note would improve readability.

## Nice-to-Haves

- A convergence diagnostic showing that as the self-consistency MSE loss approaches zero, the PDE residual on a test grid also approaches zero (e.g., a 1D Ornstein-Uhlenbeck problem).
- A non-Gaussian test problem (e.g., double-well potential, multimodal mixture) to demonstrate that the method handles complex densities.
- Error bars over multiple random seeds for all reported metrics.

## Removed Points

- **"The transformation \(\boldsymbol{\mu}^*\) is not novel"** — The paper presents this as "some necessary transformations" (line 150) and never claims novelty here. This is a strawman criticism.
- **"The zero-diffusion toy problem proves nothing"** — The paper explicitly frames this example as an illustration that "PINF algorithm is the method of characteristics" (line 334), not as a demonstration of the diffusion-handling mechanism. The criticism misreads the paper's own framing.

## Novel Insights

The reviews reveal an interesting tension: the paper's core idea is structurally principled (reformulating the FP equation as ODEs via a modified drift is mathematically sound, and using normalizing flows to guarantee normalization addresses a real limitation of PINNs), but its empirical validation is the weakest possible version of what is needed. All three test problems are Gaussian — meaning they test nothing about the expressive capacity of the normalizing flow component. This creates a situation where the theoretical architecture is more solid than the evidence provided for it, which is the opposite of the typical pattern in deep learning papers (where experiments often outpace theory). The key question for the community is whether the elegant theoretical framing justifies acceptance despite the thin experiments, or whether the evaluation must be commensurate with the claimed generality.

## Suggestions

1. **Add at least one non-Gaussian benchmark** — a double-well potential or multimodal steady-state FP equation — to demonstrate that the RealNVP component can learn complex densities beyond Gaussians.
2. **Run PINN, KRnet, or a finite-difference baseline** on the same problems and report quantitative errors. This is essential for any claim of superiority.
3. **Report quantitative metrics in tabular form** (relative \(L^2\) error, KL divergence) with standard deviations over 5+ random seeds.
4. **Specify the ODE solver** (type, tolerance, step size) and report wall-clock training time and number of ODE function evaluations.
5. **Provide a small-scale convergence check** (e.g., 1D/2D OU process) where the PDE residual can be explicitly evaluated on a grid, to validate that minimizing the self-consistency loss drives the FP residual to zero.

## Score and Decision

The paper presents a methodically sound idea with a clean theoretical derivation and a meaningful advantage (guaranteed normalization) over PINN-based alternatives. However, the experimental evaluation is critically insufficient: only Gaussian targets, no baselines, no quantitative error metrics with error bars, and no ablation studies. The core claims cannot be verified from the evidence presented. The paper needs major revisions — including baselines, non-Gaussian benchmarks, and rigorous quantitative reporting — before it can be accepted.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>