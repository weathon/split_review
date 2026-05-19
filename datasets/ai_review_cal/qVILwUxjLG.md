- Decision: Reject
- Avg Score: 3.75
- Scores: 3, 3, 3, 6
Now I have all the information I need. Let me produce the final consolidated review.

## Summary

This paper introduces NeuralPES (Neural Predictive Ensemble Sampling), a scalable deep-neural-network-based algorithm for non-stationary contextual bandits. The key innovation is a three-model architecture (reward model, sequence model, and predictive model) that biases exploration toward information with lasting value. The paper provides theoretical regret bounds for a linearized variant (LinPS) and evaluates NeuralPES on three tasks: a synthetic AR(1) logistic bandit and two real-world recommendation datasets (MIND over 1 week, KuaiRec over 2 months), showing consistent improvements over stationary neural bandit algorithms and their sliding-window non-stationary variants.

## Strengths

- **Novel algorithmic design integrating predictive modeling for lasting-information prioritization.** The three-model architecture (reward → sequence → predictive) is clearly specified with pseudocode. The predictive model conditions on a two-step-ahead predicted future reward-model representation (ŵ_{m,t+2} ⊙ b(ψ_m; c, a)), which structurally differs from prior non-stationary methods that merely discount or window past data. This is a concrete architectural contribution.

- **Empirical superiority across all three tasks.** Table 1 reports consistent improvements: AR(1) 0.5850 vs next-best 0.5741, MIND CTR 0.1552 vs 0.1513, KuaiRec rating 1.3421 vs 1.3172. Results are reported over 20 seeds with standard errors, and the comparison set includes both stationary neural bandit algorithms and their sliding-window non-stationary variants.

- **Ablation studies isolate the predictive model's role.** Figure 2(e) shows that removing the predictive model (Neural Sequence Ensemble) causes a severe performance collapse on KuaiRec. This provides causal evidence that the predictive model — the core component — is responsible for the observed gains, not just the ensemble or sequence modeling alone.

- **Theoretical analysis provides intuition.** Theorem 1 and Corollaries 2–3 bound the regret of LinPS (a linear variant), showing it achieves zero regret when information is maximally transient (i.i.d. θ_t) and sublinear regret when information is more lasting. The bounds depend explicitly on transition parameters (q_i, γ_i), supporting the claim that the algorithm prioritizes lasting information.

## Weaknesses

### Fatal
None.

### Major

- **Training/inference mismatch in the predictive model is unaddressed.** During training (Eq. 7, Algorithm TrainPredictiveNN), the predictive model receives the *actual* future reward-model weights w_{m,j+2} as input. At test time (Algorithm NeuralPES, line 265–266), it receives the *predicted* weights ŵ_{m,t+2} from the sequence model. This creates a distribution shift the paper does not acknowledge or analyze. The predictive model never sees predicted weights during training, so errors or biases in the sequence model's predictions could degrade performance arbitrarily. While this teacher-forcing-to-free-running gap is a common pattern in ML (e.g., autoregressive generation), the paper should at minimum discuss the issue, analyze how prediction errors propagate, or experiment with training the predictive model on predicted weights (e.g., with a stop-gradient). As written, readers cannot assess how sensitive the method is to sequence model accuracy.

- **Missing critical hyperparameter: sliding-window size.** The paper compares against sliding-window baselines but never reports the window size used, nor describes a tuning procedure for it. Since sliding-window performance is highly sensitive to this parameter, this omission undermines the fairness of the comparison — the baselines may be operating with a suboptimal window while NeuralPES has an advantage.

### Minor

- **Theory analyzes LinPS, not NeuralPES.** The regret bounds (Theorem 1, Corollaries 2–3) are for a linear contextual bandit with known features and known action sets — a highly idealized version of the algorithm. The paper only argues by analogy (e.g., the ensemble approximates the posterior) that NeuralPES inherits these properties. No analysis bridges the gap between the linear model and the neural implementation (nonlinear features, ensemble approximation error, training noise, loss of plasticity). The theory provides intuition but not a guarantee for the claimed algorithm.

- **Text-pseudocode inconsistency in NeuralPES action selection.** The text description (Section 4.3, step 3) says the agent uses the *m*-th predictive model, but the pseudocode (Algorithm NeuralPES, line 266) sums over *all i=1..M* predictive models while using only the *m*-th base network ψ_m and *m*-th predicted weight ŵ_{m,t+2}. This is confusing: is the intent to ensemble-average over predictive models while using a single sampled particle for the base network? The discrepancy should be resolved and the design choice explained.

- **Improvements on real datasets are modest and no significance tests.** The relative gains on MIND (~2.6%) and KuaiRec (~1.9%) are positive but small relative to the reported error bars. Standard errors are reported but no significance tests (e.g., paired bootstrap) are provided, making it hard to assess whether the improvements are statistically reliable across trial conditions.

### Trivial
None.

## Nice-to-Haves

- An experiment training the predictive model with predicted weights (possibly with stop-gradient on the sequence model) to assess the impact of the distribution mismatch.
- Regularized versions of at least one baseline (e.g., Window Neural Ensemble + ℓ₂ regularization toward initial weights) to isolate whether gains come from the predictive architecture or simply from plasticity-preserving regularization.
- Error-over-time plots (regret curves with confidence bands) for the main experiments, rather than only aggregate average reward.
- Specific hyperparameter values used in experiments (M, K, L, learning rates, sequence model architecture) to improve reproducibility.

## Removed Points

*These points from the reviews are removed with brief justification:*

- **"Cherry-picked baselines"** — The paper includes the standard neural bandit baselines (Neural Ensemble, Neural LinUCB, Neural Linear) and their sliding-window variants, which are the appropriate non-stationary extensions. The critic's mention of DUAL, Neural UCB, and Neural TS is either out of scope (computational cost justification is provided) or not clearly established as a state-of-the-art neural non-stationary method. The comparison set is reasonable.
- **"The method is likely broken" / "fatal flaw" framing of the training mismatch** — The teacher-forcing design is a standard ML pattern. It is a genuine concern worth addressing but not a fatal design error. Demoted to Major.
- **"Sliding-window variants sometimes harm performance"** — On AR(1), the window variant of Neural Ensemble goes from 0.5683 to 0.5688, a negligible change but not a decrease. Other baselines (e.g., Neural LinUCB) show clear improvement with windows. This criticism is not substantiated by the data.
- **"No comparison to original predictive sampling (Liu et al. 2023)"** — Liu et al. 2023 is a linear algorithm that does not scale, which is exactly the limitation the paper is trying to address. Running it on a linearized version of the environments would not be a meaningful comparison for a neural algorithm.
- **"The ablation shows predictive model is essential but the overall gain is modest — contradictory"** — These facts are not contradictory. A component can be essential for the few-percent improvement observed without causing a total collapse when combined with other components. The ablation shows that without the predictive model performance is terrible; with it, NeuralPES outperforms baselines. This is consistent.
- **Generic reproducibility nitpicks** (undisclosed hyperparameters, learning rates, architecture details) — The paper lists all hyperparameter names in algorithm inputs (M, K, L, τ, τ_seq, τ_pred, α, α_seq, α_pred, K', K''). The specific numeric values, while helpful, are standard implementation details that can be deferred to an appendix. The critic's characterization of the pseudocode as "missing" these details is inaccurate.
- **Formatting/style criticism** about Figure 1 axis labels and figure size — parser artifact.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Acknowledge and address the training/test mismatch** for the predictive model. Either provide a justification for why the mismatch is benign (e.g., show empirically that the predictive model's output is robust to small perturbations in the future-weight input) or modify the training procedure (e.g., train with predicted weights using a stop-gradient on the sequence model).
2. **Report the sliding-window size** used for window baselines and describe how it was selected (tuned on a validation set, or provide a sensitivity analysis).
3. **Resolve the text-pseudocode inconsistency** in NeuralPES action selection: clarify whether all M predictive models are averaged or only the m-th is used.
4. **Add significance tests** (e.g., paired bootstrap over seeds) for the main results in Table 1.
5. **Include regret-over-time plots** with confidence bands to show whether NeuralPES's advantage is consistent across the entire horizon or concentrated in specific phases.
