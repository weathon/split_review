- Decision: Accept
- Avg Score: 6.67
- Scores: 6, 8, 6
Now I have all the evidence I need. Let me produce the consolidated review.

## Summary

The paper proposes the Neural Wave Equation, a non-homogeneous wave equation whose source term is parameterized by a neural network, for sequence labeling on irregularly sampled data. The model evolves hidden states continuously over both time and depth, using the wave equation's analytical solution (d'Alembert's formula) to argue that it provides denser connections across hidden states than the heat-equation-based CDR-NDE. Experiments on four irregular-sequence benchmarks show the method achieves the best results on three of four datasets and is competitive on the fourth, while being faster than Neural CDE on large datasets.

## Strengths

- **Principled theoretical motivation via analytical solution comparison (Section 4.3).** The paper compares d'Alembert's formula for the wave equation with the separation-of-variables solution for the heat equation, demonstrating that the heat equation's negative exponential term suppresses information from lower depths while the wave equation does not. This provides a clear, mathematically grounded reason for preferring the wave equation over the prior CDR-NDE (heat equation) approach.

- **Strong empirical results on multiple benchmarks (Table 1, Sections 5.1–5.3).** Neural Wave variants achieve the highest test accuracy on Person Activity (92.78±0.41), the lowest test MSE on Walker2D, and the best AUC on PhysioNet Sepsis. On each of these datasets, at least one variant outperforms a broad set of baselines including GRU-ODE, ODE-RNN, ODE-LSTM, Neural CDE, and CDR-NDE.

- **Ablation validates the learnable source function (Section 5.5).** Removing the neural-network source term (homogeneous wave equation) causes dramatic performance degradation — Person Activity accuracy drops from ~92% to 51.73%, and Walker2D MSE rises to 0.99 — confirming that the parameterized source is essential for capturing complex dependencies.

- **Computational efficiency advantage over Neural CDE (Sections 5.1, 5.5).** Neural Wave is reported to be an order of magnitude faster than Neural CDE on Person Activity, and Neural CDE could not be run on Walker2D and Stance data due to prohibitively long epoch times. This demonstrates a practical scalability advantage.

## Weaknesses

### Fatal
None.

### Major

- **The FDM scheme assumes uniform time spacing (Δt), but the method is designed for irregularly sampled data, and the paper does not explain how this gap is resolved.** The core finite-difference equations (Eqs. 6–8, Eq. 10) use a fixed Δt for the second temporal derivative term `(1/Δt²)[h_{t+Δt,d} − 2h_{t,d} + h_{t−Δt,d}]`. Irregularly sampled sequences have non-uniform inter-observation gaps, yet the paper provides no explanation of how this discretization is adapted — whether by interpolation onto a uniform grid, by using per-gap Δt values, or by some other mechanism. This is a significant methodological gap for a paper whose central problem is irregular sampling, and it undermines reproducibility of the method.

- **The core claim (wave equation > heat equation) lacks a controlled ablation.** The entire motivation (Section 4.3) contrasts the wave equation's information-preserving property with the heat equation's diffusive decay. However, the comparison to the existing heat-equation baseline (CDR-NDE) is not a controlled experiment — the source function designs, solver choices, and architectural details differ. A proper test would implement a neural heat equation using the same FDM solver, same source function variants, and same training setup, then compare wave vs. heat results directly. Without this, the source of any performance difference is ambiguous (it could stem from source function design, solver differences, or implementation details rather than the PDE type). This leaves the paper's primary theoretical claim under-supported by direct evidence.

### Minor

- **The analytical solution (d'Alembert's formula) motivates non-local connections, but the actual solver is a local FDM scheme, and the paper does not analyze how well the numerical scheme approximates the non-local effects.** The theoretical argument (Section 4.3, Eq. 9) uses the analytical solution to claim "denser connections" as an inherent property of the wave equation, yet the FDM iteration (Eq. 7) only exchanges information with nearest temporal neighbors at each depth step. No analysis is provided of how the solver depth or number of function evaluations relates to the support of the analytical integral, or how many steps are needed to approximate the non-local coupling. This weakens the internal logic connecting the motivation to the implementation, though it does not invalidate the empirical results.

- **Vector-valued hidden states are only tersely explained.** The wave equation is a scalar PDE, but hidden states `h(t,d)` are vectors (dimension 64). Section 4.1 states that "the source terms enable the mixing of information across the latent dimension of the hidden state," implying each component evolves independently under the wave equation with cross-dimensional coupling only through the source network. While this is a valid design choice, the paper would benefit from making this independence explicit and discussing whether the wave speed `c` applies uniformly across all components or is learned per channel. The current description is technically adequate but leaves room for ambiguity.

- **The abstract overclaims relative to the full results.** The abstract states "demonstrate the superior performance of the proposed neural wave equation model." The results show SOTA on 3 of 4 datasets (with different variants working best on different datasets), but on stance classification (Section 5.4) the paper acknowledges "Even if our model does not beat some of the baselines" and describes the result as "competitive." While the overall empirical showing is strong, "superior" oversells a pattern where the best variant varies by dataset and one dataset shows competitive rather than leading results.

### Trivial

- **Typo in the heat equation analytical solution (Section 4.3, Eq. 12).** The exponential term inside the integral is written as `exp^{(-kλ_n(t-τ))}` where the integration variable `τ` ranges over depth (0 to d). This should likely be `exp^{(-kλ_n(d-τ))}` rather than involving `t` (the time index). The paper's qualitative conclusion about exponential decay in the heat equation is unaffected, but the formula as written is inconsistent.

## Nice-to-Haves

- A controlled ablation implementing a neural heat equation variant with the same source functions, solver (Tsit5), and training setup. This would directly test whether the wave equation's information-preserving property yields measurable benefits over diffusion dynamics.
- Reporting statistical significance / confidence intervals for the main comparisons in Table 1, especially where margins are small.
- An explicit statement of whether time gaps are handled by resampling/interpolation onto a uniform grid, by using observation-specific Δt values, or by some other mechanism in the FDM temporal derivative.

## Removed Points

The following points raised by reviewers are removed with justification:

1. **"Missing boundary conditions in time" / references to appendix content** — The paper states "A detailed explanation of boundary condition is provided in A.12." The parser strips appendices; this content exists in the original submission. Removed per hard rule about missing appendix content.
2. **"Figure 2 not visible"** — Parser artifact. The figure exists in the original submission.
3. **"The paper never explains how vector-valued states are handled" (as stated in the original criticism)** — The paper explicitly addresses this in Section 4.1: "since we are solving a 1-dimensional wave equation with vector-valued hidden states, the source terms enable the mixing of information across the latent dimension of the hidden state." Demoted to Minor weakness reflecting that the explanation is terse rather than absent.
4. **"Speculate on the potential benefits" phrasing concern** — Style nitpick. The paper clearly states its contributions; the word "speculate" in item 2 refers to benefits derived from analytical solutions, which are then formally presented.
5. **"Baseline hyperparameter tuning was not controlled"** — Speculative concern without evidence that baselines were disadvantaged. The paper states it follows established guidelines from prior work (Lechner & Hasani, 2020).
6. **"CDR-NDE comparison is not an ablation, so the central thesis is unsupported"** — Overstated. The paper compares against CDR-NDE (the heat-equation baseline), and the empirical results favor the wave equation. The lack of a fully controlled ablation is a genuine gap (retained as Major weakness) but does not render the thesis "unsupported."
7. **"Neural CDE could not be run on two datasets" (framed as a weakness of the paper)** — The paper openly acknowledges this as a practical limitation of the baseline, not of the proposed method. It is a constraint on the completeness of the baseline set, which the authors note.
8. **General category-drive concerns from the harsh critic (e.g., "the evaluation lacks rigor" without specific anchor)** — These are area-of-concern sweeps rather than specific, verifiable weaknesses.

## Novel Insights

Beyond the paper's own contributions, the reviews do not surface any genuinely novel insight that the paper itself does not already contain. The most useful observations from the review process (the irregular-time-gap gap and the need for a controlled wave-vs-heat ablation) are methodological gaps that the authors should address, not new research discoveries.

## Suggestions

1. **Clarify how the FDM temporal derivative is computed for irregularly sampled sequences.** This is the single most important missing detail — without it, readers cannot reproduce the method on data with non-uniform time gaps.
2. **Add a controlled neural heat equation variant** using the same FDM solver, source function designs, and training setup, and compare wave vs. heat on all datasets. This would directly test the paper's core theoretical claim.
3. **Make the vector-state handling explicit** — state that each hidden dimension independently follows the wave equation dynamics, with cross-dimensional mixing only through the source network.
4. **Tone down the abstract** to reflect that performance is strongest on 3 of 4 datasets and competitive on the fourth, rather than claiming uniformly "superior performance."
5. **Fix the variable mismatch** in the heat equation analytical solution (Eq. 12, Section 4.3).
