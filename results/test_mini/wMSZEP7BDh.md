Now I have all the information I need. Let me write the consolidated review.

## Summary

This paper proposes PMP-net, a neural network framework that incorporates Pontryagin's Maximum Principle (PMP) necessary conditions as soft constraints in the loss function, enabling unsupervised learning of optimal control solutions without labeled data. The approach is demonstrated on two classic problems: optimal linear filtering (Kalman filter) and minimum-time control (bang-bang control). Key architectural innovations include a learnable terminal-time parameter for problems with unknown horizon and a P^TP decomposition to enforce symmetry/positive semi-definiteness of the covariance matrix.

## Strengths

- **Unsupervised learning without labeled data**: The paper demonstrates that PMP-net recovers the Kalman filter and bang-bang control using only PMP residuals and boundary conditions as loss, with no ground-truth trajectory data. The baseline supervised NN (trained on 50 ground-truth points) fails to generalize beyond the training interval (Figures 1-2), highlighting the value of the unsupervised approach.

- **Handling unknown terminal time**: The minimum-time problem requires optimizing the final time t_f*. PMP-net introduces a learnable intrinsic parameter t_f and a sigmoid masking mechanism to deactivate control after reaching the target, enabling backpropagation through t_f. Figure 5d shows convergence to the true value t_f* = 2. The paper correctly identifies that forward ODE-based methods (e.g., neural ODEs) cannot straightforwardly handle this case.

- **Architectural inductive biases respecting problem structure**: The P^TP construction for the covariance matrix enforces symmetry and positive semi-definiteness as a hard constraint (Section 3.1). The sigmoid masking for bang-bang control mimics a dead-zone controller (Section 4.2). These are principled design choices that improve training stability.

- **Honest ablation studies**: Figure 6a shows that without pretraining the costate estimator, the loss diverges. Figure 6b shows that additional (x, λ) sampling reduces the discrepancy in the learned switching function. These ablations transparently reveal the method's sensitivity to training procedures.

## Weaknesses

### Major

1. **No comparison to standard numerical optimal control solvers**: The only baseline is a supervised NN trained on 50 ground-truth points — a strawman. Standard numerical methods (direct transcription, multiple shooting, collocation via tools like CasADi, GPOPS, or even a simple ODE solver wrapped in an optimizer) can solve both benchmark problems efficiently and accurately. Without establishing whether PMP-net is competitive with or offers any advantage over these well-established solvers, the paper's claim of a "new approach for addressing general... optimal control problems" is unsubstantiated. The missing comparison is the most serious weakness.

2. **Kalman filter solution is only partially correct**: PMP-net matches the steady-state Kalman gain, but the paper acknowledges a clear discrepancy during the transient phase (Figures 1b, 1c). The claim "replicates the Kalman filter" is overstated for the full time interval — the method reproduces only the steady-state behavior. While the paper notes that steady-state gains are often used in practice, many Kalman filter applications (e.g., tracking, data assimilation) operate in transient regimes where this mismatch matters. Leaving this to future work without diagnosing the cause (loss weighting? network capacity? curriculum schedule?) is a significant gap.

3. **Training fragility and reliance on problem-specific heuristics**: The method requires extensive hand-tuning: (i) curriculum learning with a manually chosen schedule (α factor 1.04), (ii) heuristic pretraining of the costate estimator with non-zero values for bang-bang (the ablation in Figure 6a confirms training diverges without this), (iii) a separate freezing step to train the control estimator on random (x, λ) samples, (iv) a carefully chosen large horizon T for the bang-bang case. The sigmoid approximation of the indicator function introduces systematic error acknowledged as a "discrepancy" (Figure 4c). No sensitivity analysis is performed, and results appear to come from a single run with no error bars or multiple seeds. A method that requires substantial prior knowledge of the solution it claims to discover is not yet a general tool.

4. **Limited scope and overclaimed contribution**: The paper demonstrates PMP-net only on two low-dimensional problems (4-state Kalman, 2-state double integrator) with known analytical solutions. The title "Is Pontryagin's Maximum Principle All You Need?" and the abstract's promise of addressing "general, possibly yet unsolved" optimal control problems dramatically oversell the contribution. No evidence is given for scalability to higher dimensions, nonlinear dynamics, state/control constraints beyond bang-bang bounds, or problems without closed-form solutions. The method's real contribution is a proof-of-concept application of PINN-style residuals to PMP-based optimal control, which does not justify the sweeping claims.

### Minor

- **Use of RK4 for evaluation undermines the "learned solution" claim**: Both experiments evaluate PMP-net by extracting the learned control and integrating it with a standard Runge-Kutta solver (Section 3.2, line 154; Section 4.2, line 269) because "the estimated state by PMP-net might not adhere to the dynamics constraints." This means the network does not produce a dynamically consistent trajectory on its own — the state trajectory is generated by a separate numerical integrator. This weakens the claim that PMP-net learns the full solution.

- **No error bars or multiple seeds**: All results appear to be from a single training run. Without reporting mean/variance across multiple seeds, it is impossible to assess the method's stability and reliability.

### Trivial

- None.

## Nice-to-Haves

- A comparison to a PINN-based direct method (parameterizing state and control with a standard collocation loss but without the costate) would isolate the benefit of including PMP conditions.
- Phase portraits showing the (x₁, x₂) trajectory against the optimal switching curve would visually confirm whether the control switches correctly in the bang-bang problem.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Criticism about "forward ODE methods cannot handle unknown terminal time" being unsupported**: The harsh critic claimed you can use event-triggered integration. While true for general numerical methods, this criticism misses that the paper's contrast is specifically with *neural ODE-based approaches*, where the integration horizon is fixed at training time. The paper's claim is defensible in that context.

- **Criticism about "omitted transversality condition" in the Kalman filter PMP**: The terminal cost is tr(Σ(T)) with fixed T=5.0, so λ(T)=I is the correct boundary condition. The transversality condition for free terminal time does not apply. This criticism reflects a misreading.

- **Criticism about "any model-based optimal control method also does not require labeled data" undercutting the unsupervised claim**: This conflates model-based optimization (solving the ODE directly with numerical methods) with learning a neural representation of the solution. The paper's claim about unsupervised learning is distinct in that it learns a neural network that can be queried at any time t, without solving a new ODE each time.

- **Criticism about citing missing related works**: The paper could discuss direct collocation methods, but per guidelines, I cannot confirm or raise missing related work concerns.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Add comparisons to standard numerical optimal control solvers** (direct transcription, shooting, collocation) on both benchmarks, reporting solve time vs. accuracy trade-offs. Without this, the paper cannot claim PMP-net offers any advantage over existing methods.

2. **Run experiments with multiple random seeds (≥5)** and report means and standard deviations for all metrics.

3. **Diagnose and address the Kalman filter transient mismatch** — investigate whether it stems from loss weighting, network capacity, or curriculum scheduling. At minimum, report the quantitative discrepancy (e.g., integrated absolute error over the transient period).

4. **Test on at least one problem without a known analytical solution** (e.g., a nonlinear system with state constraints) to demonstrate the claimed general applicability.

5. **Tone down the title and claims** to match the actual scope of the paper — e.g., "PMP-net: Learning Optimal Control Solutions from Pontryagin's Maximum Principle."

## Score and Decision

### Anchor Comparison

I reviewed calibration papers with the following avg scores (human reviews) to calibrate:

- **VeMC6Bn0ZB.md (avg 7.33, Accept)** — "Learning to Solve DE Constrained Optimization Problems": Thorough experiments with proper baselines, clear comparisons, and well-motivated case studies. Substantially stronger than the PMP-net paper in execution and validation.
- **5AB33izFxP.md (avg 6.75, Reject)** — "Simultaneous Online System ID and Control": Strong Lyapunov-based theoretical contribution with rigorous proofs. PMP-net lacks the theoretical depth and rigorous validation of this paper.
- **PfaPgIQTul.md (avg 5.25, Reject)** — "Learning HJB Viscosity Solutions with PINNs": Similar PINN-for-control paper but with more comprehensive analysis and multiple experiments. PMP-net's experimental validation is significantly weaker.
- **Ty7xx0pn0a.md (avg 4.60, Reject)** — "DEQ-MPC": Also criticized for limited scope (toy examples) and single-seed evaluation, but at least included proper baselines (Diff-MPC comparison). PMP-net has the additional fatal flaw of missing baselines.
- **A67BCisI3F.md (avg 4.00, Reject)** — "Diffusion-based Control": Weak experiments and limited scope, but included baseline comparisons. PMP-net has a more principled approach but even weaker experimental validation.
- **7sMR09VNKU.md (avg 3.50, Reject)** — "Learning System Dynamics from Sensory Input": Missing baselines, only two simple problems. PMP-net has a stronger conceptual framework but similar experimental deficiencies.
- **Mpp6SakVzl.md (avg 3.33, Reject)** — "DiLQR": Missing related work, limited experiments. PMP-net has a similar level of experimental weakness.

The PMP-net paper has a genuinely interesting idea — integrating PMP conditions as neural network constraints — but the experimental validation is far too weak to support the broad claims. The missing comparison to standard optimal control solvers is a fatal gap: without it, the paper cannot demonstrate that PMP-net offers any practical advantage. The training fragility, partial solution of the Kalman filter (steady-state only), and limited scope (two low-dimensional problems) compound this problem. The core idea has potential, but the paper in its current form does not provide sufficient evidence for its claims.

**Score: 3.5**

**Decision: Reject**

MY FINAL SCORE: <score>3.5</score>
MY FINAL DECISION: <decision>Reject</decision>