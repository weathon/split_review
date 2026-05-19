Now I have all the information needed. Let me construct the final consolidated review.

---

## Summary

This paper proposes Physics-Informed Normalizing Flows (PINF), which extends continuous normalizing flows to solve Fokker–Planck equations with diffusion. The key idea is to transform the diffusion FP equation into a system of ODEs via the method of characteristics (by defining an effective drift $\boldsymbol{\mu}^* = \boldsymbol{\mu} - (\nabla\log p)\mathbf{D} - \nabla\cdot\mathbf{D}$), then train a neural network in a self-supervised manner by minimizing the MSE between the ODE-integrated log-density and the network-predicted log-density. For steady-state FP equations, Real NVP is used to enforce normalization.

## Strengths

- **Novel reformulation of the diffusion FP equation into ODEs (Section 4.1.2, Eqs. 9–12).** The transformation of the diffusion term into an effective drift that depends on $\nabla\log p$ enables continuous normalizing flows to handle diffusion—this is the central algorithmic contribution that distinguishes PINF from prior flow-based methods that only address the zero-diffusion (Liouville) case.

- **Self-supervised training without labeled data or reference solutions (Algorithm 2, Eq. 13).** The consistency loss between ODE-integrated log-density and network-predicted log-density avoids the need for samples from the target distribution or ground-truth PDE solutions. This is a clean formulation that is conceptually simple.

- **Hard constraint for the initial condition (Eq. 14).** The network architecture $\phi_\theta(\mathbf{x}, t) = \log p_0(\mathbf{x}) + t\,u(\mathbf{x}, t;\theta)$ exactly satisfies the initial PDF by construction, which is more principled than the soft penalty approach used by standard PINNs.

- **Normalization guarantee for steady-state solutions via Real NVP (Section 4.2).** The paper correctly identifies the scale-invariance issue in the steady-state ODEs and uses the change-of-variables formula of Real NVP to ensure the predicted density integrates to one, directly addressing a fundamental challenge that would break a pure ODE-only approach.

## Weaknesses

### Major

- **The experimental validation is far too narrow to support the paper's core claims.** All three test problems have Gaussian exact solutions: the TFP example (d=10) has constant drift and constant diffusion yielding a Gaussian with time-dependent mean and variance; the SFP examples (d=30, d=50) are Ornstein–Uhlenbeck processes with Gaussian stationary distributions. No non-Gaussian, multimodal, or nonlinear drift/diffusion problems are tested. Fitting a single Gaussian in 10–50 dimensions does not constitute evidence that the method "can efficiently solve high dimensional" FP equations as claimed in the abstract. Without at least one nontrivial problem (e.g., a multimodal stationary distribution, a problem with anisotropic diffusion, or nonlinear drift), the contribution remains unvalidated for its intended use case.

- **No baseline comparisons are provided.** The paper mentions that "PINN is effective primarily with the dimension d≤3" (line 356) but does not actually compare against PINNs, KRnet, TNF, or any other method—not even on a low-dimensional problem where PINNs could be run as a sanity check. The claims about PINF's advantages relative to prior work are therefore unsubstantiated.

- **No runtime, convergence, or scalability analysis.** The method requires solving an ODE for each sample in each mini-batch during training, with the ODE right-hand side involving gradients of the neural network and divergences computed via automatic differentiation. Yet the paper provides no wall-clock training time, no ODE solver evaluation counts, and no scaling study as dimensionality increases. Without this information, it is impossible to assess whether the method is practical for the stated target applications.

### Minor

- **Evaluation is confined to 2D slices of the full high-dimensional space.** For the TFP example (d=10), the reported error is computed only on a 2D grid $(\vx_1, \vx_2)$ with all other coordinates fixed to 2 (line 376). For the SFP example (d=30, d=50), test points are $(\vx_1, \vx_2, 0, \ldots, 0)$ (line 397). This is an extremely narrow evaluation that does not measure the method's performance across the full high-dimensional domain.

- **The error metric for the SFP case is underspecified.** The paper states "the relative error remains below 0.2%" (line 397) without clarifying whether this is pointwise relative error, integrated relative L² error, or some other measure. Specification of the exact metric is needed for reproducibility.

- **The claim that PINNs are effective only for d ≤ 3 (line 356) is stated without citation or supporting evidence.** Even if this is a known heuristic in the community, a paper making this claim should provide a reference or a brief experiment to substantiate it.

### Trivial

- The architecture description (Eq. u_net, lines 177–180) imports a quadratic potential + ResNet structure from optimal control work without explaining why simpler alternatives were not explored. This is a presentation gap rather than a technical flaw.

## Nice-to-Haves

- Ablation studies on the key design choices (log-MSE vs. direct MSE loss, hard constraint vs. soft penalty, the effect of the quadratic potential term in the network) would help understand what makes the method work.
- A brief analysis of training dynamics (does the loss converge reliably? are there trivial fixed points?) would strengthen the paper's technical foundation.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *Harsh critic's claim that "the paper repeatedly states that PINNs are effective only for d ≤ 3…" — The paper states this once, not repeatedly. Retained as minor since it is an unsupported assertion, but the "repeatedly" framing is inaccurate.*
- *Harsh critic's speculation that "ODE right-hand side involves both the gradient of the neural network and the divergence of the effective drift… could be prohibitively expensive" — The criticism about missing runtime analysis is valid and retained in Major. The speculative claim about prohibitive cost is grounded in what the method does, but no evidence is presented that it is actually prohibitive. Replaced with the verifiable observation that no runtime data is reported.*
- *Harsh critic's concern about normalization guarantee for SFP — "the training loss (MSE on log-densities) may drive the predicted log-density away from the true normalized distribution." The paper addresses normalization through Real NVP's change-of-variables formula; this concern is speculative without evidence of such drift.*
- *Strength Finder's generic strengths about "addressing an important problem" — these are not specific to the paper's contribution.*
- *Strength Finder's claim about "demonstrated accuracy on high-dimensional steady-state FP equations (d=30 and d=50)" — While the experiments show low error on Gaussian problems, the "high-dimensional" framing is weaker than claimed because the problems are simple Gaussians and evaluation is on 2D slices. However, the actual experimental result (low error on these problems) is a genuine supporting observation, so this is retained in Strengths but framed carefully.*

## Novel Insights

None beyond the paper's own contributions. The reviews surface the known tension between an elegant mathematical derivation and weak empirical support, but this is a standard observation rather than a novel synthesis. One structural insight worth noting: the self-consistency loss (MSE between ODE-integrated and network-predicted log-density) is similar in spirit to the "Picard iteration" or "ODE fixed-point" formulation used in some older PDE-solving frameworks, and the paper could benefit from connecting to this perspective.

## Suggestions

1. **Add at least one non-Gaussian test problem** — a multimodal stationary distribution (e.g., a Gaussian mixture as the stationary solution of an appropriate FP equation) or a problem with nonlinear drift. This would demonstrate that the method can learn more than a single elliptical Gaussian.
2. **Include a baseline comparison** — run a PINN on a low-dimensional version (d=2 or d=3) of the same problem to support the claim that PINNs struggle beyond low dimensions. Even better, compare to KRnet for the SFP case.
3. **Report wall-clock training time and ODE solver evaluations** for the existing experiments, and include a brief scaling study (e.g., how does training time grow with d for the SFP problem?).
4. **Evaluate on full-domain test points** rather than 2D slices, or at minimum explain why the 2D slice evaluation is sufficient (e.g., if the problem symmetry guarantees that error is dominated by the first two dimensions).
5. **Clearly specify the error metric** used for the SFP experiment (pointwise relative error? relative L²?).

## Score and Decision

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>