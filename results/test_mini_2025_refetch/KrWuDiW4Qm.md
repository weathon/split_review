Now I have a strong calibration picture. Let me write the final consolidated review.

**Round 1 bracket**: Based on comparisons with weak anchors (scores 2–3.4), middle anchors (scores 4–7), and strong anchors (scores 8+), I initially bracketed this paper between **5.5 and 7.5**.

**Round 2 narrowing**: Reading CAMEL (6.33, Accept Poster), PoDiNNs (6.6, Accept Poster), PIED (7.0, Accept Poster), and DIF (5.0, Reject), the paper is stronger than CAMEL and DIF (better theory, more dramatic results, clearer writing) and comparable to PoDiNNs, while slightly below PIED (which has real-world validation). This narrows to **6.0–7.0**.

**Final score: 6.5**.

---

## Summary

This paper addresses out-of-distribution (OOD) robustness for forecasting parametric ODE systems. It proposes **MetaPhysiCa**, a meta-learning framework that combines causal structure discovery (via ℓ₁-regularized continuous optimization with a V-REx invariance penalty) with test-time task-specific parameter adaptation. The method is evaluated on three synthetic dynamical systems (damped pendulum, predator-prey, epidemic model) under OOD initial conditions and/or ODE parameters, and achieves 2× to 28× lower OOD NRMSE than a suite of strong baselines (NeuralODE, DyAd, CoDA, APHYNITY, SINDy, EQL). A theoretical identifiability result (Theorem 1) guarantees that the proposed objective recovers the true causal structure under appropriate assumptions.

## Strengths

1. **Large and consistent OOD error reductions across all tasks**: On the epidemic task (Table 1), MetaPhysiCa achieves OOD NRMSE of 0.019 vs. the next best baseline at 0.544 (a ~28× improvement under shifted initial conditions) and 0.100 vs. 0.898 (a ~9× improvement under shifts in both initial conditions and ODE parameters). Similar large margins are reported for the damped pendulum and predator-prey systems. Critically, these gains hold against *all* baselines including NeuralODE, DyAd, and CoDA which themselves have excellent in-distribution performance — so the OOD improvement is not an artifact of a single weak comparator.

2. **Theoretical identifiability guarantee for causal structure**: Theorem 1 (with proof in Appendix A) establishes that under Assumption 1, the bi-level optimization with ℓ₁ regularization uniquely recovers the true causal structure Φ of the SCM in Figure 4. This formal assurance that the method can discover the correct governing equation — not merely fit training data — is a non-trivial and well-motivated theoretical contribution.

3. **Systematic diagnosis of why existing PIML methods fail OOD**: Section 3 provides a clean taxonomy of transductive vs. inductive PIML methods, with concrete failure-mode illustrations (Figure 2). This diagnostic analysis (algorithmic alignment deficit for neural networks, parameter-sharing assumptions of transductive methods, neural network extrapolation failures in inductive methods) directly motivates each design choice (basis functions for algorithmic alignment, meta-learning across tasks, causal structure discovery), giving the method a principled foundation rather than an ad-hoc architecture.

4. **Ablation studies confirm the necessity of each design component**: Appendix D.2 shows OOD performance degrades significantly without ℓ₁ regularization or test-time adaptation; Appendix D.2.2 reports that omitting the V-REx penalty raises OOD NRMSE by 24×. These controlled experiments directly link each component (sparsity, adaptation, invariant risk) to the method's success. The paper also verifies that MetaPhysiCa recovers the ground-truth ODE structure across all three systems (Appendix D.1, Table 5).

5. **Principled hyperparameter selection without OOD validation**: Hyperparameters are chosen using only in-distribution validation loss (sparsest model within 5% of best ID validation loss). This respects the OOD setting where the test distribution is unknown, making the reported gains credible rather than artifacts of test-set leakage.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
1. **Derivative estimation for the training loss is underspecified**: The paper states (paragraph before Eq. 4) that it uses squared loss between predicted and "estimated ground truth derivatives" for stable learning. For the damped pendulum dataset (1% Gaussian noise added), numerical differentiation can amplify noise substantially. The paper does not specify which derivative estimation method is used (finite differences, total variation regularization, etc.) or how noisy data are handled. Since the method still achieves good ID error (0.009 for epidemic), this suggests care was taken — but the absence of a clear description affects reproducibility, particularly for practitioners applying the method to new noisy datasets. This is a genuine gap in the paper's empirical methodology description.

2. **APHYNITY baseline comparison would benefit from clarification**: APHYNITY's ID NRMSE on the epidemic task is 0.151 (±0.150) compared to NeuralODE's 0.005 and DyAd's 0.006 — an order of magnitude worse with high variance. APHYNITY is designed to augment an *incomplete physics model* with a neural network, so its poorer ID performance is partially inherent to the method, but the paper does not specify how the incomplete model was chosen for each system or whether APHYNITY's hyperparameters were tuned to give competitive ID results. Since the headline "28× improvement" is computed against APHYNITY as the best OOD baseline, the paper would be strengthened by clarifying this configuration. Importantly, this does *not* invalidate the core claim — MetaPhysiCa also dramatically outperforms NeuralODE (ID error 0.005, OOD error 1.139 vs. 0.019) and DyAd/CoDA — so the concern is about framing precision, not a fatal flaw.

3. **No discussion of computational cost**: MetaPhysiCa involves an ODE solver during training and test-time adaptation, which can be expensive. A brief note on training/adaptation runtimes relative to baselines would help practitioners assess trade-offs, especially since the method uses a bi-level optimization (or joint optimization) scheme.

4. **No sensitivity analysis for the test-time adaptation window**: The test-time adaptation uses the first r = T/3 or T/10 observations. The paper does not ablate over different values of r, which would help characterize robustness of the approach to varying amounts of initial observations.

### Trivial
None that survive filtering.

## Nice-to-Haves
- An experiment where the basis function dictionary is intentionally mismatched (missing a necessary basis function or containing many spurious ones) would further test the method's robustness. Appendix D.7 partially addresses varying dictionary size, but a dictionary-mismatch case (where a necessary function is absent) would strengthen the claims about causal discovery under model misspecification.
- Reporting the specific λ_Φ and λ_REx values used for each dataset would improve reproducibility.
- Including a table of the discovered structure Φ in the main text (rather than only in Appendix D.1) would strengthen the paper's core claim about causal structure recovery.

## Removed Points
- **APHYNITY is poorly configured / comparison is unfair**: The paper explains that APHYNITY uses an incomplete physics model by design — this is not a misconfiguration. Moreover, MetaPhysiCa's improvements hold against NeuralODE (60× on epidemic OOD X_t₀), DyAd, and CoDA, which have excellent ID performance. The concern about inflated claims is valid only if one ignores the other baselines, which the paper clearly reports.
- **Missing variance across seeds**: Standard deviations are reported in Table 1 (in parentheses).
- **Theorem 1 assumptions not in main text**: The paper explicitly states "Under Assumption 1 (Appendix A)" and provides a proof sketch. The appendix is stripped by the parser; the original submission contains it.
- **IRM connection is loose**: The paper provides strong empirical evidence (24× worse OOD without V-REx) that the penalty is necessary; the theoretical framing is acknowledged as approximate.
- **Qualitative analysis should be in main text**: A presentation preference, not a weakness in the science.
- **Missing related works**: Not allowed to flag per protocol.
- **Formatting/presentation nitpicks**: These are parser artifacts, not author errors.
- **Limited evaluation scope (as a major weakness)** : The paper honestly acknowledges this limitation. Evaluating on three synthetic systems is standard for PIML work of this type. Demanding PDEs or chaotic systems goes beyond the stated scope.
- **Various speculative criticisms** (e.g., "could the metric be measuring a proxy?", "assumptions may be too restrictive") from the harsh critic that lack concrete anchors in the paper text.

## Novel Insights
None beyond the paper's own contributions. The synthesis across reviews does not surface any new insight about the method or problem that the authors have not already identified.

## Suggestions
1. **Specify the derivative estimation method** used for the training loss, particularly for the noisy pendulum dataset. This is critical for reproducibility.
2. **Clarify APHYNITY's incomplete physics model configuration** for each system. Show that APHYNITY's hyperparameters were reasonably tuned. Alternatively, reframe the "best baseline" claim to reference NeuralODE/DyAd as well, or show the improvement factors both including and excluding APHYNITY.
3. **Add a table of the discovered structure Φ in the main text** (not just the appendix) to directly support the causal discovery claim.
4. **Include a brief computational cost comparison** (training + adaptation wall-clock time relative to baselines).
5. **Add a sensitivity analysis** on the length of the test-time observation window r.

## Score and Decision

**Calibration anchors used** (all rounds):

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| fzZfju8y0g.md | 3.40 | R1 | Weak paper; MetaPhysiCa is clearly stronger |
| SQl6T4dfs8.md | 3.25 | R1 | Weak paper; MetaPhysiCa is clearly stronger |
| 3sOE3MFepx.md | 2.20 | R1 | Weak paper; MetaPhysiCa is clearly stronger |
| aAI92OHA4t.md | 2.33 | R1 | Weak paper; MetaPhysiCa is clearly stronger |
| TwMLUpPg8G.md | 5.00 | R1 | DIF — clarity issues, theoretical concerns; MetaPhysiCa is stronger |
| SXj1qjFEpQ.md | 5.75 | R1 | FNSDA — incremental over FNO/CoDA; MetaPhysiCa is stronger |
| QMkYEau02q.md | 4.25 | R1 | Weather forecasting paper — weak baselines, unclear writing; MetaPhysiCa is stronger |
| w7P92BEsb2.md | 7.00 | R1 | PIED — real-world validation, broader scope; MetaPhysiCa is slightly weaker |
| xuY33XhEGR.md | 8.00 | R1 | ClimODE — real-world climate forecasting; MetaPhysiCa is clearly weaker |
| uKZdlihDDn.md | 7.60 | R1 | Fluid simulation — real-world scope; MetaPhysiCa is weaker |
| fU8H4lzkIm.md | 8.00 | R1 | PhyMPGN — real-world PDE systems; MetaPhysiCa is weaker |
| gQlxd3Mtru.md | 8.67 | R1 | Stochastic dynamics — strong theory and real data; MetaPhysiCa is weaker |
| eeJz7eDWKO.md | 6.00 | R2 | Bayesian causal discovery — different task, similar quality tier |
| 7VVGO0kuuY.md | 5.80 | R2 | Causal dynamics in RL — narrower scope; MetaPhysiCa is slightly stronger |
| nnicaG5xiH.md | 6.33 | R2 | CAMEL — most similar topic (meta-learning physical systems); MetaPhysiCa ≈ slightly stronger |
| U1DjXQeJRx.md | 6.60 | R2 | PoDiNNs — strong theoretical grounding, similar quality tier |
| GrDne4055L.md | 6.25 | R2 | OOD detection, different task; comparable quality |
| 4VIgNuQ1pY.md | 6.67 | R2 | Neural SDEs, different task; comparable quality |

**Final bracket**: After R1, the bracket was 5.5–7.5. After R2 narrowing (comparing against CAMEL at 6.33, PoDiNNs at 6.6, PIED at 7.0), MetaPhysiCa is slightly stronger than CAMEL (better theory, more dramatic results) and comparable to PoDiNNs, placing it at **6.5**.

**Summary**: MetaPhysiCa makes a genuine contribution to OOD robustness in physics-informed ML. The problem is well-motivated, the proposed meta-learning + causal structure discovery approach is principled, the theoretical guarantee is non-trivial, and the empirical results are striking across three systems. The main limitations are the synthetic-only evaluation (honestly acknowledged) and a few underspecified implementation details (derivative estimation, APHYNITY configuration). These are addressable and do not undermine the core contribution.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>