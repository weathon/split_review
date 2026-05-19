- Decision: Reject
- Avg Score: 4.80
- Scores: 3, 6, 3, 6, 6
Now I have a thorough understanding of the paper. Let me write the final consolidated review.

## Summary

The paper proposes PDETime, a model for long-term multivariate time series forecasting that reinterprets the task as solving an initial value problem for a PDE. The architecture follows an encoding-integration-decoding pipeline: the encoder estimates the partial derivative in latent space, a patch-based numerical solver integrates it, and a decoder maps back to the original space using meta-optimization. The paper claims state-of-the-art results on 33 of 33 settings across seven benchmarks.

## Strengths

- **Novel PDE-based conceptual framing.** Reconceptualizing LMTF as an initial value problem for a PDE (Eq. 1–2) and showing that historical-value and time-index models correspond to restricted cases of this formulation (Section 1) is a genuinely novel perspective that opens a new direction for the field.

- **Strong empirical results with clear long-term robustness advantages.** PDETime achieves the best or near-best results across most settings in Table 1. Notably, PDETime's error degrades more slowly with horizon length than baselines — e.g., on Traffic, MSE increases 10.6% (0.330→0.365) vs. PatchTST's 20.0% (0.360→0.432) — suggesting genuine architectural advantages for long horizons.

- **Well-designed patch-based numerical solver with continuity loss.** The solver divides the sequence into non-overlapping patches, using a neural network at patch boundaries and Euler steps within patches, with an auxiliary continuity loss (Eq. 10). The ablation showing that setting S=H (no patching) degrades performance (Figure 4c) validates this design choice.

- **Detailed hyperparameter analysis.** Section 4.3 provides sensitivity studies for look-back multiplier μ, INR layers k, aggregation layers N, and patch length S on ETTh1/ETTh2, giving practical guidance and demonstrating stability across settings. The μ analysis (Table "mu") is particularly informative.

- **Transparent discussion of limitations.** The ablation discussion (Section 4.2) explicitly acknowledges that the spatial feature contribution is limited and that temporal feature impact varies by dataset — this honesty is a strength even though it undercuts part of the narrative.

## Weaknesses

### Fatal
None.

### Major

- **Asymmetric look-back window inflates apparent advantage on shorter horizons.** PDETime uses L=μ×H with μ ∈ {1,3,5,7,9} selected per setting, while baselines are capped at fixed look-backs (96 for most, 336/512 for DLinear/PatchTST). For H=96, PDETime uses L up to 672 (μ=7) vs. baselines' 96 — a 7× advantage. This is especially problematic because the μ sensitivity table (Table "mu") shows that larger μ helps most on shorter horizons (e.g., ETTh1 H=96: μ=1→0.378, μ=7→0.354). While PDETime still outperforms on long horizons where μ=1 is optimal (L=720 vs. baselines' 96–512), the headline "33 first-place counts" conflates results obtained under different resource budgets. **The paper's core claim of SOTA performance is not invalidated, but it is overstated, and the advantage cannot be cleanly attributed to the PDE mechanism.**

- **Ablation undermines the PDE motivation.** Removing the spatial component (x_his) yields performance virtually identical to or slightly better than the full model on 3 of 8 settings (Traffic H=96: 0.329 vs. 0.330; Weather H=192: 0.198 vs. 0.200; Weather H=720: 0.290 vs. 0.291). Removing the temporal component on Weather H=336 also improves results (0.240 vs. 0.241). The paper acknowledges this but does not reckon with how it undercuts the central thesis — that the PDE perspective with explicit spatial and temporal domains is driving performance. The model appears to function primarily as a time-index-based predictor with a learned derivative estimator, and the spatial domain encoder is at best weakly exploited. If the PDE-inspired components are not causally responsible for the gains, the novelty of the approach is substantially reduced.

### Minor

- **No statistical significance or meaningful variance estimates.** "All experiments are repeated 3 times with fixed seed 2024" — a fixed seed produces deterministic results; repeating is non-informative. No confidence intervals or standard deviations are reported anywhere. Given that PDETime and the best competitor are within 0.001 MSE on several settings (ETTm1 H=96: 0.292 vs. PatchTST 0.293; ECL H=96: tied at 0.129), the absence of any variance estimate makes it impossible to assess whether differences are meaningful.

- **Baselines not tuned on these datasets.** The paper uses fixed look-backs and "original settings" for baselines while searching over μ, N, S, and learning rate for PDETime. This asymmetry in tuning budget inflates PDETime's apparent advantage, especially on settings where baselines were not optimized.

- **Missing ablation of auxiliary losses.** The continuity loss ℒ_c and first-difference loss ℒ_f are introduced but never individually ablated. Their contribution to the reported performance is unknown, making it hard to assess whether the solver or these auxiliary losses drive improvements.

- **No comparison with ODE-based methods (Neural ODE, Latent ODE).** Given the method's lineage — predicting a derivative and integrating — ODE-based models are the most natural competitors. Their omission is a gap, even if they are slower or harder to train.

- **Decoder substantially overlaps with DeepTime.** The meta-optimization framework with ridge regression for D_φ is directly adopted from DeepTime (cited). The ablation does not isolate whether PDETime's advantage over DeepTime comes from the encoder/solver or simply from different hyperparameter choices.

### Trivial

- The phrase "repeated 3 times with fixed seed 2024" is self-contradictory — a fixed seed makes repetition meaningless. The authors should either run multiple seeds and report mean±std, or report a single run.

## Nice-to-Haves

- Visualizing the learned derivative α_τ to show it corresponds to interpretable quantities (trends, periodicity) would provide qualitative evidence for the PDE analogy.
- Reporting wall-clock time and parameter counts would clarify the practical trade-off.
- A controlled experiment where baselines are given the same look-back as PDETime would cleanly separate the contribution of the method from the contribution of additional history.

## Removed Points

The following points from the inputs were removed or demoted, with justification:

1. **"Paper ignores that PatchTST is better on Weather H=96"** (from Harsh Critic). Factually wrong: the paper clearly shows PatchTST bold (first) and PDETime underlined (second) for Weather H=96. The paper acknowledges this placement.

2. **"Eq. (2)–(3) are mathematically imprecise — time-index models are pointwise, not integrals"** (from Harsh Critic). The paper presents these as *reinterpretations* ("can be seen as", "can be interpreted as"), not as claims about how these models actually compute. This is a conceptual reframing, not a formal reduction claim.

3. **Strength Finder claim: "Removing the temporal feature, spatial feature, or initial condition each degrades performance on Traffic and Weather."** Factually wrong: removing the spatial component *improves* performance on multiple settings (Traffic H=96, Weather H=192, Weather H=720). This strength was removed.

4. **"No hyperparameter tuning for baselines"** as a standalone point (from Harsh Critic). Partially merged into the look-back asymmetry weakness. Using published settings is standard practice, but the combination of PDETime's search over μ + fixed baselines is worth noting; this is now folded into the Major weakness.

5. **"Missing runtime and parameter count"** (from Harsh Critic). Demoted to Nice-to-Have since this is standard for a methodology paper and the lack doesn't threaten the core claims.

## Novel Insights

The harsh critic raises a non-obvious point that the paper's experimental setup conflates two distinct advantages: the PDE-based architecture and the flexibility to use more historical data. This is a genuinely important insight that the paper's own μ sensitivity table partially supports (performance often peaks at moderate μ and degrades at large μ for long horizons). The interaction between look-back length and model architecture is a dimension that even the paper's careful hyperparameter analysis does not fully disentangle. Separately, both reviews together highlight an uncomfortable tension: the paper's claimed innovation is the PDE framing, yet the ablation suggests the model reduces to something close to a time-index predictor with a learned derivative estimator — raising the question of whether the PDE vocabulary is being applied as a genuine structural contribution or as a post-hoc interpretation.

## Suggestions

1. **Run controlled look-back experiments.** Report results where all baselines are given the same look-back as PDETime at each setting, and also run PDETime with the short look-backs used by baselines. This would cleanly separate architectural gains from data advantage.

2. **Add statistical significance.** Run experiments with at least 3–5 random seeds and report mean ± std. This is critical given the small performance gaps on several settings.

3. **Ablate individual auxiliary losses** (ℒ_c and ℒ_f) and the decoder's meta-learning component to isolate what drives performance.

4. **Compare against at least one ODE-based baseline** (e.g., Neural ODE or Latent ODE) to ground the PDE/ODE lineage.

5. **Either strengthen the PDE motivation** by showing that learned derivatives correspond to interpretable quantities, or **downgrade the framing** to avoid overclaiming. The current gap between the ambitious narrative and the ablation evidence weakens the paper.
