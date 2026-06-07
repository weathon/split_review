Now I have a good set of anchors to calibrate against. Let me compile the final review.

## Summary of Calibration

**Round 1 (Bracketing):**
- Low band anchors: ~2.5-3.0 range (EPINN, PINN with trSQP, etc.) — clearly much weaker than the paper under review
- Middle band anchors: Neural Metriplectic Systems (7.00), PoDiNNs (6.60), Chaotic Dynamics (4.67), Port-Hamiltonian GNN (7.00)
- High band anchors: ~7.6-8.0 range — clearly much stronger

My round-1 bracket: **~4.5-6.5**. The paper sits above 4.67 (Chaotic Dynamics) but below 6.60 (PoDiNNs) and 7.00 (Neural Metriplectic).

**Round 2 (Narrowing):**
- Projected Neural DEs (4.75): Novel method, theory, FPUT experiments. Split scores (8,1,5,5). Rejected. The paper under review has no novel method but better-organized experiments with OOD testing.
- Helmholtz-Hodge GP (5.80): Novel method + theory, simple experiments. Rejected. Scores (6,3,6,6,8).
- Learning Chaotic Dynamics (4.67): Novel method with theoretical guarantees, limited experiments. Rejected.

The paper under review is a comparative empirical study with no novel method, but it has compelling results (especially FPUT) and clear geometric exposition. Compared to PNDEs (4.75): similar experimental quality but no novel method. Compared to HH-GP (5.80): weaker on novelty/theory but stronger on experimental scope. Score: **5.0**.

---

## Final Review

## Summary

This paper presents a comparative empirical study arguing that geometric inductive biases — Riemannian optimization on the SPD manifold for dissipative systems and symplectic integration for conservative Hamiltonian systems — enable smaller models to generalize more robustly than larger structurally-naive alternatives. It demonstrates this through two case studies: (1) system identification of a 2D heat-transfer system with an SPD-constrained linear state-space model, and (2) modeling of an 18D FPUT system using symplectic Hamiltonian neural networks (SHNNs), compared against LSTMs and NeuralODEs across a sweep of model sizes.

## Strengths

- **Compelling quantitative size-efficiency result on the FPUT conservative system**: Table 2 and Figure 3 show that a compact SHNN with 1,441 parameters (L=1, W=72) achieves roll-out test MSE of ~8.9×10⁻⁹ and energy drift RMS of 1.3×10⁻³, while the best LSTM requires 97,074 parameters yet achieves drift RMS of 5.9. This directly substantiates the central claim that structure-aware models can dramatically outperform much larger structure-naive baselines on long-horizon prediction.

- **Energy drift RMS as an insightful diagnostic metric**: The paper introduces drift RMS (ΔHₖ = H(ẑ_{t+k}) − H(ẑ_t), Section 3.2) as an evaluation metric that goes beyond MSE. Table 2 shows NeuralODEs and LSTMs exhibit drift RMS on the order of 1–10², while SHNNs stay at 10⁻⁴–10⁻³, explaining *why* structurally-naive models fail at long roll-outs despite reasonable one-step accuracy. This connects model behavior directly to violation of the underlying Hamiltonian structure.

- **RieOpt demonstrates improved OOD generalization over EucOpt**: Table 1 shows that under the Chicago climate (unseen forcing distribution), RieOpt achieves MSE of 1.36 on T_ext1 versus 3.35 for EucOpt, while RF (24.1) and XGBoost (22.3) degrade catastrophically. This provides evidence that constraining the state matrix to the SPD manifold adds value beyond merely using the LSSM architectural form.

- **Effective phase-space visualization**: Figure 4 makes energy drift interpretable by showing the LSTM trajectory visibly crossing energy level sets on the projected Hamiltonian surface, while the SHNN trajectory remains on the correct energy level, providing an intuitive geometric explanation for the quantitative drift metrics.

## Weaknesses

### Fatal

None.

### Major

- **FPUT evaluation uses a chronological train/test split from a single trajectory, conflating interpolation with generalization**: The paper simulates one 30,000-step FPUT trajectory from a single initial condition and splits it chronologically 80/20. For a continuous dynamical system, temporally adjacent states are highly correlated, meaning the reported roll-out MSE on the test set primarily measures interpolation rather than generalization to new dynamical regimes. The paper includes qualitative "unseen initial condition" rollouts (Figures 4b/c), but only for one SHNN and one LSTM configuration, and only visually — no quantitative metrics are reported for these OOD evaluations. The headline quantitative results in Table 2 and Figure 3 are all based on the chronological split, which weakens the paper's generalization claims.

- **No statistical rigor across any experiment**: Every model configuration across both use cases is trained exactly once. There are no error bars, standard deviations, or seed-based variance reported anywhere. For the dissipative case in particular, where several MSE values are within the same order of magnitude (e.g., London T_ext2: XGBoost 0.106 vs RieOpt 0.507 vs EucOpt 0.580), the ranking could shift under different random initializations. This undermines the reliability of the quantitative comparisons, especially for the dissipative use-case where performance margins are narrower.

### Minor

- **Missing plain HNN baseline for the FPUT case**: The paper compares SHNN against LSTM and NeuralODE but omits a standard Hamiltonian neural network (HNN) that parameterizes H_θ and uses a non-symplectic integrator. This is the most direct ablation for distinguishing whether the benefit comes from the Hamiltonian parameterization (learning a scalar energy) or specifically from the symplectic integrator. Without it, the paper cannot cleanly attribute the performance gain to symplectic integration specifically.

- **Dissipative-case comparison is partially confounded between model class and structure**: The paper compares a linear state-space model (LSSM, with or without SPD constraint) against fundamentally different model classes (RF, XGBoost, LSTM). While the EucOpt vs RieOpt comparison within the LSSM class does isolate the SPD constraint, the large OOD gap between black-box models and both LSSM variants (e.g., Chicago T_ext1: RF 24.1 vs EucOpt 3.35 vs RieOpt 1.36) leaves unclear how much of the OOD benefit comes from the LSSM's linear structure versus the SPD constraint specifically.

- **Asymmetric LSTM sweep**: The LSTM architecture sweep varies only width W, while SHNN and NeuralODE sweeps vary both width and depth (L). This asymmetry in the model-size comparison weakens the fairness of cross-architecture comparisons.

### Trivial

- **Equation 7 notation inconsistency**: The loss function in equation 7 uses Φ_B T_i, but the system dynamics in equation 4 use Φ_B U_t. Unless T_i is being overloaded to include the input, this appears to be a notation error that should be corrected for clarity.

## Nice-to-Haves

- Redesigning the FPUT data split using multiple independent trajectories from different initial conditions, with quantitative OOD metrics across all model configurations, would substantially strengthen the generalization claims.
- Adding a plain HNN baseline (Hamiltonian parameterization without symplectic integrator) would cleanly isolate the contribution of the symplectic integrator.
- Extending the dissipative case to a higher-dimensional system would make the "smaller models" thesis more compelling, since a 2D system with ~6 learnable parameters trivially satisfies "small."

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Harsh critic: "Missing figures and tables (Figures 5-8, Table 3)"** — REMOVED. The parser strips figures and appendix material from submissions; these exist in the original paper. Flagging them as missing would be a parser artifact, not an author error.

- **Harsh critic: "The training convergence speed claims depend on Figures 7 and 8 which are not accessible"** — REMOVED for the same reason; figures exist in the original submission.

- **Harsh critic: "Equation 7 could be a bug that would invalidate the dissipative results"** — REMOVED as speculative. The notation is likely a typo (T_i instead of U_i) rather than an implementation error; claiming this could invalidate results is not warranted from the paper text alone.

- **Harsh critic: "The EucOpt baseline already shows the LSSM structure alone provides *most* of the generalization benefit"** — WEAKENED and kept as a minor weakness about confounded comparison. The numbers in Table 1 show RieOpt substantially outperforms EucOpt on Chicago T_ext1 (1.36 vs 3.35), so the claim that the LSSM structure alone provides "most" of the benefit is not supported by the data.

- **Strength Finder: "Dual-use-case design spanning dissipative and conservative physical regimes"** — REMOVED. Generic and superficial; covering two use cases is not inherently a strength.

- **Strength Finder: "Clear pedagogical development linking physical stability to manifold geometry"** — REMOVED. Generic; any well-written paper should explain its foundations clearly. Not a distinguishing contribution.

- **Harsh critic: "The NeuralODE results show extreme instability for some configurations (drift RMS of 377 or 1803), suggesting training instability rather than a fundamental limitation"** — REMOVED. The paper does not claim NeuralODEs are fundamentally limited; it shows they are unstable in practice, which is consistent with the paper's thesis. Whether the cause is training instability or architectural limitation does not change the empirical observation.

## Novel Insights

The paper's most genuinely novel insight is operationalizing energy drift RMS as a diagnostic that cleanly separates structural from capacity-driven generalization. While energy conservation diagnostics exist in the Hamiltonian ML literature, the paper's explicit framing — showing that drift RMS explains *why* one-step MSE alone is misleading for model selection (a structurally-naive model can have good one-step accuracy but catastrophic drift) — provides a useful evaluative lens. The connection between this metric and the "smaller models" thesis (structure substitutes for capacity specifically because it prevents drift accumulation) is a worthwhile framing.

## Suggestions

- Redesign the FPUT evaluation to use multiple independent trajectories from distinct initial conditions for training and testing, and report quantitative OOD metrics across all model configurations. This would directly address the most significant evidential gap.
- Run at least 3 seeds per configuration and report mean ± std, particularly for the dissipative case where performance margins are narrower.
- Add a plain HNN baseline (Hamiltonian parameterization, non-symplectic integrator) to isolate the contribution of the symplectic integrator from the Hamiltonian inductive bias.
- Fix the notation in equation 7 (Φ_B T_i appears to be a typo; should likely be Φ_B U_i).

## Calibration Anchors

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| EPINN for Stiff ODEs | SYiOxXWlKU | 2.50 | R1 | Weaker — narrow method, limited scope |
| PINN with trSQP | GkJCgUmIqA | 3.00 | R1 | Weaker — methodological contribution to PINN training |
| Beyond Dynamics (conservation discovery) | NRRHkJE03w | 3.00 | R1 | Weaker — less systematic, weaker experiments |
| Mamba Neural Operator | VtP7CamOR5 | 3.00 | R1 | Weaker — less mature contribution |
| Learning Chaotic Dynamics with Dissipativity | XqDM97DtMf | 4.67 | R1/R2 | Comparable — novel method but limited experiments, rejected |
| Projected Neural DEs | 2AWZTv6kgV | 4.75 | R2 | Comparable — novel method, split scores, similar FPUT evaluation, rejected |
| Helmholtz-Hodge Decomposition + GP | qKf0tZtF6B | 5.80 | R2 | Stronger — has novelty and theory, but weaker experiments; rejected |
| PoDiNNs | U1DjXQeJRx | 6.60 | R1 | Stronger — novel architecture, theoretical depth, extensive experiments; accepted |
| Neural Metriplectic Systems | uL1H29dM0c | 7.00 | R1 | Stronger — novel parameterization, theoretical results, extensive experiments; accepted |
| Oscillatory State-Space Models | GRMfXcAAFh | 8.00 | R1 | Much stronger — novel method, theory proofs, comprehensive evaluation |

The paper sits between Projected Neural DEs (4.75) and Helmholtz-Hodge GP (5.80). It lacks the novelty and theory of HH-GP but has more compelling experimental design (model size sweep, OOD evaluation). It is comparable to or slightly better than Projected Neural DEs (4.75), which had similar FPUT experiments but was split by a strong novelty challenge. The paper's core results (especially FPUT size-efficiency) are clear and its geometric exposition is well-done, but the chronological split and lack of statistical rigor are significant methodological gaps. Score: **5.0**.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>