Now I have enough calibration information. Let me write the consolidated review.

**Calibration synthesis:**

**Round 1 bracket:** Weak anchors (2.0–3.33) → Middle anchors (4.0–5.5) → Strong anchors (8.0–8.5). The paper clearly sits in the middle band.

**Round 2 narrowing within bracket:** 
- RO-HNN (4.00, reject): Very similar topic (structure-preserving Hamiltonian learning); both papers have limited novelty concerns and incomplete baselines. Our paper is slightly stronger empirically (cleaner FPUT experiments) but has similar-level flaws.
- Mesh Field Theory (5.50, reject): More comprehensive framework but rejected for weak benchmarks. Our paper has cleaner individual experiments but less theoretical depth.
- DGNet (5.00, accept): Had a clear methodological contribution (Green's function theory). Our paper lacks this kind of technical novelty.
- Operator learning with domain decomposition (5.00, accept): Solid empirical work with a well-scoped contribution.

**Final score: 5.0.** The FPUT experiments are strong and well-designed, the geometric exposition is clear, and the motivation is sensible. However, the dissipative case has mixed results not adequately discussed, size-controlled comparisons are missing in the heat transfer study, and Eq. (7) contains a typo. The paper is borderline but the issues are concrete and fixable; in its current form it does not fully deliver on its central claim.

---

## Summary

This paper presents two case studies — a 2D heat transfer system learned with a SPD-constrained linear state-space model via Riemannian optimization, and an 18D Fermi-Pasta-Ulam-Tsingou (FPUT) system learned with symplectic Hamiltonian neural networks (SHNNs) — to argue that geometry-informed inductive biases allow for smaller models with better generalization than structure-naive baselines (RF, XGBoost, LSTM, NeuralODE). The paper is a comparative empirical study rather than a new-method paper.

## Strengths

1. **SHNN outperforms much larger LSTMs on long-horizon rollout and energy drift by orders of magnitude.** Table 2 shows SHNN with 1,441 parameters achieves rollout MSE 1.322×10⁻³ and drift RMS 8.876×10⁻⁹, while the best LSTM (97,074 params) achieves 5.914×10⁰ and 1.694×10⁻⁶ — five orders of magnitude worse in drift. Figure 3 confirms this gap across all swept model sizes. This directly supports the claim that structure-preserving models can be far smaller yet generalize better.

2. **Riemannian optimization (RieOpt) achieves the lowest MSE on the out-of-distribution Chicago test set.** Table 1 shows RieOpt at 1.36×10⁰ (Text1) and 1.79×10⁰ (Text2) versus the best naive baseline at 22.3×10⁰ and 7.85×10⁰ respectively. This demonstrates that SPD-constrained learning generalizes to unseen climatic forcing where unconstrained models fail qualitatively.

3. **Systematic hyperparameter sweep with parameter counts enables fair comparison across model sizes.** Table 2 reports 15 configurations each of SHNN, NeuralODE, and LSTM with parameter counts from 361 to 149,041, allowing the reader to verify that the structure-preserving advantage holds across the complexity spectrum.

4. **Qualitative phase-space visualizations (Figures 4a–c) directly illustrate the energy-drift mechanism.** The 2D projected energy surface diagnostic makes the abstract concept of "crossing energy levels" tangible: the SHNN trajectory stays on the correct energy contour while the LSTM visibly drifts across levels.

## Weaknesses

### Fatal
None.

### Major

1. **Mixed results in the dissipative case are not adequately discussed.** The paper claims that structure-naive approaches "demonstrate instability" while RieOpt shows "global stability," but Table 1 shows that on the London test set, XGBoost achieves lower MSE than RieOpt on Text2 (0.106 vs 0.507). The London Text1 result favors RieOpt (0.400 vs 0.502), so the overall picture for in-distribution performance is mixed. The Chicago (OOD) results strongly favor RieOpt, but the paper glosses over the London result rather than explaining it (e.g., is XGBoost better at one-step but worse at rollout? Is this a fluke of the train/test split?).

2. **Size-controlled baselines are missing in the dissipative case.** RieOpt has ~5 parameters (a 2×2 symmetric Φ_A and 2×1 Φ_B), while RF, XGBoost, and LSTM have orders of magnitude more. The paper never tests what happens when naive baselines are forced to be similarly small (e.g., a linear autoregressive model, a tiny MLP, or a single-neuron LSTM). Without these controls, the observed wins could partly reflect the fact that the correctly-specified linear model is the right model for a linear system — interesting but not a clean test of "smaller models via structure preservation." (The EucOpt baseline partially addresses this since it has the same size, but it is also linear.)

3. **Equation (7) contains a substantive typo.** The loss function writes ‖Φ_A T_i + Φ_B **T_i** − T_{i+1}‖². Based on the dynamics in Eq. (4) (T_{t+1} = Φ_A T_t + Φ_B **U**_t), the term should read Φ_B **U**_i, not Φ_B T_i. This is not a formatting artifact — it is a real error in a central equation that damages reproducibility.

### Minor

4. **No measures of variance or statistical significance.** All MSE values in Tables 1 and 2 are reported as single numbers without confidence intervals, error bars, or multiple runs. With synthetic data one could easily bootstrap the test sample or rerun with different seeds, and the absence of any such measure makes it impossible to assess whether the reported differences are reliable.

5. **The eigenvalue analysis in Section 2.1.1 is confusingly written.** The text mixes conditions for positive definiteness (Re(λᵢ) > 0, needed for SPD) with discrete-time stability (eigenvalues within the unit circle). The underlying technical content is correct, but the presentation is likely to confuse readers unfamiliar with the mapping between continuous-time negative-real-part stability and discrete-time unit-circle stability.

6. **The RF and XGBoost baselines are not fully described for multi-step rollout.** The paper does not specify whether these models predict one-step-ahead using a sliding window or are applied autoregressively for multi-step prediction. This makes the comparison somewhat opaque.

### Trivial

7. **The paper does not specify which exact Riemannian parametrization was used.** It mentions Cholesky decomposition as an alternative but does not state what was actually implemented (e.g., whether geoopt's default SPD parametrization or a custom Cholesky parameterization was used).

## Nice-to-Haves

- The paper's "smaller models" claim would be significantly strengthened by adding a controlled experiment in the dissipative case: learn an unconstrained linear LSSM and a tiny MLP (~5–10 parameters) as baselines of matched size against RieOpt.
- An honest discussion of the London Text2 result (XGBoost beating RieOpt) with analysis of whether it holds for rollout versus one-step prediction would improve credibility.
- Reporting computational cost (training time, convergence speed) would complement the "smaller models" argument.
- Testing generalization to different material properties or boundary conditions (beyond unseen forcing) would be a stronger test of "structural generalization."

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Naive baselines (RF, XGBoost, LSTM) are not well-motivated for this task."** The paper includes EucOpt (unconstrained linear state-space model), which is exactly the standard structure-naive system identification baseline. The additional baselines are conventional ML models; their inclusion, while imperfect, is not a flaw.
- **"The paper does not test generalization to unseen dynamics (different material properties, boundary conditions)."** This is scope creep — the paper explicitly tests generalization to unseen forcing, which is within its stated scope.
- **"Code and data are promised but not provided."** The ethics statement promises public release. Code/data sharing at submission is not standard practice for ICLR.
- **"Missing related works."** Unable to verify from available information.
- **"The paper does not discuss computational cost or training time."** This is a nice-to-have, not a weakness.

## Novel Insights

None beyond the paper's own contributions. The reviews collectively surface a useful observation: the mixed London results in the dissipative case create a tension with the paper's clean narrative, and addressing this honestly would strengthen rather than weaken the paper. This is an actionable insight for revision but not a novel analytical finding.

## Suggestions

1. Fix the typo in Eq. (7) (replace Φ_B T_i with Φ_B U_i).
2. Add size-controlled baselines to the heat transfer experiments: an unconstrained linear LSSM and a tiny MLP (~5 parameters).
3. Discuss the London Text2 result explicitly — explain whether XGBoost's advantage is only on one-step MSE, or whether it also holds for multi-step rollout.
4. Add error bars or confidence intervals to all reported metrics.
5. Clarify the description of how RF and XGBoost baselines are set up for multi-step prediction.
6. Specify the exact Riemannian parametrization used (e.g., which geoopt SPD manifold and retraction).

## Score and Decision

**Calibration details:**

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| Learning Generalized Hamiltonian Dynamics | 20PqWPr4aL | 3.00 | R1 | Weaker paper that proposed a GP method with soft constraints; criticized for limited novelty and small experiments. Our paper has clearer empirical evidence. |
| ECO | SA5XBWOoZr | 3.00 | R1 | Chaotic dynamics paper with boundedness guarantees; less directly comparable. Our paper is stronger. |
| Learning Hamiltonian Dynamics at Scale (RO-HNN) | JfNkiril3c | 4.00 | R1,R2 | Most topically similar. Both deal with structure-preserving learning. RO-HNN was rejected for combining existing components and missing baselines. Our paper is comparable in quality — cleaner FPUT experiments but similar issues in the dissipative case. |
| Dynamics of learning when learning dynamics | T65jHpSX7i | 4.50 | R1,R2 | Theoretical analysis of linear dynamics; criticized for being too simple and lacking experiments. Our paper has stronger empirical validation. Slightly stronger than this anchor. |
| Equilibrium flow | TkhPnmP4GS | 4.80 | R2 | Interesting framework for learning dynamics from snapshots; had high score variance. Our paper is comparable. |
| Mesh Field Theory | dWtJXHZkFy | 5.50 | R2 | More comprehensive structure-preserving framework but rejected for weak benchmarks and missing context. Our paper has clearer experiments but less theoretical depth. Slightly weaker than this anchor. |
| DGNet | EJ8HnNTEAv | 5.00 | R2 | Green's function-based PDE learning; accepted as poster. Had a clearer methodological contribution. Similar experimental quality. |
| Operator learning with domain decomposition | IxAnL4PRsg | 5.00 | R2 | Accepted as poster. Solid empirical work with well-scoped contribution. Our paper is comparable. |

**Round 1 bracket:** Between 3.0 and 8.0; clearly in the middle band (4.0–5.5).

**Round 2 narrowing:** Compared against RO-HNN (4.00), Equilibrium flow (4.80), Mesh Field Theory (5.50), DGNet (5.00), and operator learning with domain decomposition (5.00). The paper sits between the 4.0 and 5.5 anchors — stronger than RO-HNN due to cleaner FPUT experiments, but weaker than Mesh Field Theory in terms of theoretical framing. The FPUT experiments are genuinely strong, but the dissipative case issues (mixed results, no size-controlled comparisons, Eq. 7 typo) prevent the paper from being a clear accept.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>