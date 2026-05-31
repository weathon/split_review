## Summary

This paper presents a comparative empirical study arguing that structure-preserving inductive biases reduce the need for large models while improving generalization in dynamical system learning. Two use-cases are investigated: (1) a 2D dissipative heat-transfer system identified using a linear state-space model (LSSM) with symmetric positive definite (SPD) constraints learned via Riemannian optimization (RAdam), and (2) an 18-dimensional conservative Fermi-Pasta-Ulam-Tsingou (FPUT) system modeled using symplectic Hamiltonian neural networks (SHNNs). The paper benchmarks these against structurally naive models (Random Forest, XGBoost, LSTM, NeuralODE), finding that smaller structure-aware models generalize better to unseen initial conditions and maintain lower energy drift over long rollouts.

## Strengths

- **Energy drift visualization on projected Hamiltonian slices**: Figures 2 and 4 provide an intuitively compelling diagnostic. Showing how a trajectory "jumps" across energy level sets on 2D Hamiltonian projections (while all other coordinates are held fixed) is a useful and clear explanatory tool for why structurally-naive models fail at long rollouts. This adds genuine pedagogical insight.
- **Clear quantitative evidence for FPUT**: Table 2 and Figure 3 show that a 1,441-parameter SHNN (L=1, W=72) achieves a roll-out MSE and energy drift that are orders of magnitude better than the best LSTM (97,074 parameters), providing concrete evidence for the paper's central claim.
- **Two complementary paradigms**: The dissipative (Riemannian/SPD) and conservative (symplectic) cases together illustrate that the "structure-preserving" principle generalizes across system classes, not just Hamiltonian mechanics.

## Weaknesses

### Fatal
None.

### Major

1. **Minimal methodological novelty.** Both key components — Riemannian optimization on the SPD manifold (via `geoopt`/RAdam) and SHNNs (David & Méhats, 2023) — are established, off-the-shelf techniques. The paper applies these tools to selected benchmarks without introducing new algorithms, theory, or architectural variants. As a result, it functions primarily as a demonstration study.

2. **Imbalanced and partially unfair experimental design.** For the FPUT comparison, SHNN and NeuralODE are swept over both depth $L$ and width $W$, but the LSTM is swept over width only (no depth). This gives the LSTM fewer chances to find a good configuration and inflates the apparent advantage of the SHNN. The claimed ~65× parameter advantage (1,441 vs 97,074) is therefore not a fully fair comparison.

3. **The dissipative use-case is too simple to carry the argument.** The heat transfer system is 2D and linear. Comparing an appropriately structured linear LSSM against nonlinear models (RF, XGBoost, LSTM) on a fundamentally linear system is not a level playing field — structure-naive nonlinear models are known to perform poorly out-of-distribution for linear systems for reasons unrelated to geometric inductive biases. The more compelling claim (smaller models, better generalization) is really demonstrated only through the FPUT experiment.

4. **Key inconsistency not discussed.** Table 1 shows that XGBoost achieves an MSE of 1.06e-01 on T_ext2 London, substantially better than RieOpt (5.07e-01) and EucOpt (5.80e-01). The paper claims the structure-aware approach wins on generalization but does not acknowledge or explain this result.

5. **No comparison with other structure-aware methods for FPUT.** The paper discusses PINNs and other structure-preserving approaches in the introduction but never includes them as baselines for the FPUT experiment. Comparing only against black-box baselines (LSTM, NeuralODE) does not establish SHNN as the right structure-aware choice.

### Minor

- The NeuralODE drift results vary dramatically across model sizes (e.g., W=36 gives 3.775e+02 while W=72 gives 1.787e+00 at L=1), suggesting training instability that deserves discussion rather than simply being reported.
- The paper does not address how sensitive the SHNN results are to the choice of symplectic integrator (implicit midpoint rule) used during rollout versus during training data generation (Störmer–Verlet). This distinction is methodologically relevant.
- The generality of the thesis ("a case for smaller models") is not examined beyond two narrow use-cases; it is unclear how results would change for chaotic regimes, higher-dimensional systems with partial observability, or noisy data.

### Trivial

- The Figure 1(b) caption references a third axis $T_\text{ext3}$ (°C) which does not appear in the 2D heat-transfer model described in the text, creating confusion about what the 3D SPD manifold is actually plotting.

## Nice-to-Haves

- It would strengthen the argument significantly to show results for the FPUT system at higher values of $\alpha$ (more nonlinear) where structure-preserving matters even more, or in regimes with partial observations.
- A sweep over training set size (not just model size) would directly test the paper's claim about "data-intensive training" for structurally naive models.
- Including the Cholesky parameterization alternative for SPD optimization (mentioned briefly in Section 2.1.2) as an ablation would clarify how much the Riemannian geometry itself helps versus simply imposing the constraint.

## Novel Insights

The most genuinely novel aspect of the paper is the time-evolving visualization of predicted trajectories on sliced 2D Hamiltonian surfaces (Figure 4), showing visually and intuitively that the SHNN trajectory stays on the correct energy level set while the LSTM trajectory drifts across level sets. This provides a geometric, causal explanation of roll-out instability in structurally-naive models that goes beyond simply reporting drift metrics. Beyond this visualization tool, however, the paper's insights are largely the expected confirmation of known properties of these established methods.

## Suggestions

- Redesign the LSTM sweep to include depth variation, matching the design for SHNN and NeuralODE, so that parameter comparisons are fair.
- Explain or discuss the XGBoost outperforming RieOpt on T_ext2 London; if the interpretation is that short-horizon in-distribution MSE is not the right metric and generalization metrics tell a different story, make that argument explicitly.
- Consider increasing the scope of the FPUT experiment (e.g., varying $\alpha$, initial conditions diversity, or training trajectory length) to make the "smaller models" thesis more convincingly general.
- Replace or supplement the 2D linear heat-transfer baseline comparisons with a dissipative system that is nonlinear, where the advantage of geometric priors over black-box baselines would be more meaningful.

## Score and Decision

The paper makes a valid and clearly motivated point — structure-preserving inductive biases do help, and significantly so in the FPUT case. However, both methods applied are entirely existing techniques, the dissipative experiment is insufficiently challenging to carry the thesis, and the experimental design has fairness issues. As an empirical study, the claims are supported but limited in scope. For a top venue like ICLR, the contribution does not offer sufficient novelty or depth relative to the existing literature.

MY FINAL SCORE: <score>3</score>
MY FINAL DECISION: <decision>Reject</decision>