Now I have all the information I need. Let me synthesize the final review.

## Summary

The paper introduces the Spacetime E(n)-Transformer (SET), an architecture that enforces E(n)-equivariance (rotation, translation, permutation) in both the spatial and temporal dimensions for spatio-temporal graph data. It uses E(n)-equivariant graph convolutional layers (EGCL) for spatial processing followed by an Equivariant Temporal Attention Layer (ETAL) for temporal aggregation, with weight sharing across time steps. The method is evaluated on the charged N-body problem, predicting particle positions and velocities far into the future from a short history window.

## Strengths

1. **Ablation study cleanly isolates the benefit of equivariance.** Table 1 directly compares Equiv=True vs Equiv=False with all other components held fixed (same spatio-temporal attention structure, same parameter count). Test MSE increases from 1.25e-10 to 2.03e-10 (1.57× worse), providing clear evidence that the E(n)-equivariant inductive bias is the driver of the model's performance — not just the spatio-temporal attention architecture.

2. **Orders-of-magnitude improvement over baselines on a standard benchmark.** SET achieves test MSE of 1.25e-10 on the charged N-body problem (N=5), outperforming LSTM (2.03e-08), EGNN (2.05e-06), MLP (3.48e-06), and Linear (3.04) by 2–7 orders of magnitude. These gaps are far too large to be explained by variance alone, lending strong support to the central claim.

3. **Parameter efficiency independent of graph size.** Figure 2 shows SET's parameter count remains constant as N increases from 5 to 30, while the LSTM baseline grows from ~800K to ~1.8M parameters. This is a genuine practical advantage for scaling to larger systems, explained by the architecture's reliance on feature/coordinate dimensions rather than node count.

## Weaknesses

### Fatal
None.

### Major

1. **Missing experimental details undermine reproducibility.** No training configuration is reported — no optimizer, learning rate, batch size, number of epochs, or early stopping criterion. The hyperparameter α in the loss function (Eq. 8) is stated only as ∈(0,1) with no specific value. No confidence intervals, standard deviations, or number of random seeds are reported. The MSE differences between some configurations (e.g., best model vs. adjacency variant on test MSE) are so small that variance estimates are essential to assess significance. These omissions are the most significant barrier to accepting the paper at a conference venue.

2. **No sequential/rollout evaluation.** The model predicts a single time point (t = L+H where H=10,000) directly from a history of L=10 steps, via mean pooling across the temporal dimension. While this is a long-horizon prediction, it does not test the model's ability to roll out predictions autoregressively over many steps. The paper frames its contribution as "long-term spatio-temporal graph modeling" (line 4, line 18), which typically implies sequential prediction. Without rollout evaluation, the claim about long-term modeling is only partially supported. Adding cumulative error over a multi-step rollout would substantially strengthen the evaluation.

3. **Adjacency attention component is net zero or harmful, yet presented as part of the method.** The ablation (Table 1) shows that including temporal adjacency attention (Adj=True) yields test MSE of 1.29e-10 vs. 1.25e-10 for Adj=False — essentially no improvement — while validation MSE degrades substantially (1.12e-09 vs. 1.21e-10). The paper hypothesizes this is because edge attributes are already captured by coordinates, which is a reasonable explanation. However, the component is presented as a core architectural contribution (Eqs. 18–20, Algorithm 1) with no caveat until the ablation section. The framing should either de-emphasize this component or provide a setting where it is actually beneficial.

### Minor

1. **Noise experiment is underinformative.** The noisy observations experiment (Table 3) tests only one noise level (σ²=0.5), where all models reach MSE ≈ 0.497 — the irreducible noise floor. This shows SET does not overfit to noise, but it does not test whether equivariance provides any advantage in moderate-noise regimes (e.g., σ²=0.01, 0.05, 0.1). A single noise level at saturation is insufficient to draw conclusions about robustness. This experiment neither confirms nor refutes the value of equivariance under noise.

2. **Missing external non-equivariant STGNN baseline.** While the ablation (Equiv=False) controls for the architecture, a standard spatio-temporal GNN (e.g., GCN+LSTM, DCRNN) as an external baseline would help contextualize SET's performance against the broader STGNN literature. The gap over LSTM could partially reflect the benefit of spatial graph structure rather than equivariance per se. The Equiv=False ablation addresses this internally, but an external STGNN baseline would be more informative for readers unfamiliar with equivariant methods.

3. **Limited evaluation to one dataset.** The method is evaluated only on the charged N-body problem. While this is a standard benchmark for equivariant methods, demonstrating results on at least one additional dynamical system (e.g., a molecular dynamics simulation or a spring system) would substantially increase confidence in the method's generality.

### Trivial

1. The MSE Ratio column in Table 1 appears to use validation MSE rather than test MSE for the Adjacency row (test ratio would be ~1.03×, not 8.96×), creating an inconsistency with the table caption. The authors should clarify which metric the ratio is based on.

2. The correspondence between the symbolic equations (Eqs. 2–7) and the algorithmic description (Algorithm 1) — particularly how coordinate/velocity updates interact with feature and adjacency updates within a single layer — could be clearer.

## Nice-to-Haves

- A multi-step rollout experiment where the model predicts multiple future time steps sequentially (using its own predictions as inputs) would directly test the "long-term modeling" claim.
- Testing at additional noise levels (σ²=0.01, 0.05, 0.1) would provide a more informative picture of robustness.
- A comparison against Hamiltonian/Lagrangian neural networks (HNNs/LNNs), which the paper discusses in related work, would strengthen the positioning against physics-informed approaches.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Adjacency attention increases test MSE by 8.96×"** — This is factually incorrect. The paper's Table 1 shows Adj=True test MSE = 1.29e-10 vs. best model 1.25e-10 (≈3% increase). The 8.96× figure corresponds to validation MSE or a miscalculation. The symptom (adjacency doesn't help) is real but the severity claimed by the reviewer is wrong.
- **"The experimental evaluation does not support the paper's core claims"** (in its strongest form) — The paper does predict at horizon H=10,000 from L=10 steps, which is genuinely far into the future. The ablation (Equiv=False) directly tests the benefit of equivariance. The reviewer's claim that "predicting one future state from a trajectory segment is a regression task, not a test of long-term temporal modeling" understates the long-horizon nature of the prediction task. This point has been downgraded and reframed as Major #2 (lack of rollout evaluation).
- **"The noise experiment shows equivariance provides no benefit under realistic noise"** — The experiment tests only one noise level at the noise floor (σ²=0.5). No single noise level at saturation disproves equivariance's usefulness across all noise regimes. The point has been retained as Minor #1 in a more measured form.
- **"Minimal research has been done on preserving group symmetries in a spatio-temporal fashion" is an overstatement"** — Since I cannot verify the existence of the cited works (Gerken et al., etc.) without external sources, and per the hard rules on related work, this point is removed. The paper's claim about existing work is a matter of degree.
- **Strength: "Robustness under observational noise"** — SET ties with MLP at the noise floor. This is not evidence of robustness. Dropping this as a claimed strength since it conflicts with the verified weakness that the noise experiment is underinformative.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective on the paper that the authors' own discussion misses.

## Suggestions

1. Report full training details: optimizer, learning rate (and schedule if any), batch size, number of epochs/early stopping criterion, hardware, training time, and the specific value of α used.
2. Report results with error bars (at least 3 random seeds with mean ± std) for all experiments.
3. Add a rollout evaluation: use the model autoregressively to predict multiple future time steps and report cumulative MSE over the rollout horizon.
4. Either remove the adjacency attention component or move it to an appendix with a clear caveat that it was not beneficial in this setting, and explain the discrepancy in the MSE ratio column of Table 1.
5. Add at least one additional dynamical system (e.g., spring system, molecular dynamics) to evaluate generalization.

## Score and Decision

The paper proposes a well-motivated architecture that combines E(n)-equivariance with temporal attention. The core claim — that preserving group symmetries in both space and time improves spatio-temporal graph modeling — is supported by a clean ablation. The performance gains over baselines are large and convincing. However, the paper is significantly weakened by missing experimental details essential for reproducibility, a single-data evaluation, and the absence of rollout evaluation for a paper that claims "long-term" modeling. The contributions are real, but the experimental presentation does not yet meet the standards expected at a top conference.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>