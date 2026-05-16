Now I have all the verification I need. Let me write the final consolidated review.

## Summary

This paper introduces a Gaussian Process (GP) based probabilistic subgoal representation for goal-conditioned hierarchical reinforcement learning. Instead of a deterministic mapping from state space to latent subgoal space, the method places a GP prior over subgoal representations, yielding a posterior distribution that can capture stochastic uncertainties. The paper also proposes a novel learning objective for jointly training the GP hyperparameters and hierarchical policies, and presents a lightweight online inference scheme via state-space GP that achieves constant memory and computational complexity per state. Experiments across challenging continuous control tasks with stochasticity, sparse rewards, and image observations show consistent improvements over deterministic-representation baselines (LESSON, HESS, HRAC).

## Strengths

- **First probabilistic subgoal representation in HRL.** The paper introduces a genuinely novel approach by using GP priors to model a distribution over subgoal representation functions, moving beyond the deterministic mappings of prior work (LESSON, HESS). This is directly supported by experimental evidence showing HLPS consistently outperforms baselines in stochastic environments (Fig. 3, Ant Fall, Ant FourRooms, with sparse/dense rewards, with/without images) and degrades less as environmental noise increases (Fig. 5 Left).

- **Lightweight online inference via state-space GP.** Section 3.4 presents a technically sound transformation of the batch GP inference into a state-space form (resembling Kalman Filter updates) that achieves constant memory and computational complexity per state, making the probabilistic approach practical for real-time deployment. This is a nontrivial engineering contribution that distinguishes the work from naive GP applications that scale cubically with trajectory length.

- **Demonstrated transferability of learned representations.** The paper shows that the learned subgoal representation and low-level policy can be transferred between tasks (Ant Fall → Ant Push, with and without images) with improved sample efficiency and asymptotic performance (Fig. 6), indicating that the probabilistic representation captures reusable structure.

- **Qualitative evidence of stable subgoal representations.** The visual analysis (Fig. 4) shows that HLPS produces stable latent embeddings where distances correlate with global transition counts, unlike HESS and LESSON which exhibit unstable and locally-optimal representations. This provides direct evidence for improved stationarity in high-level transitions and low-level reward functions.

## Weaknesses

### Fatal

None.

### Major

- **The learning objective (Eq. 3) is heuristic and not derived from the GP probabilistic model.** The hyperparameters σ², γ², ℓ are learned via a task-specific distance-based loss (ratio of distances in f-space combined with a softplus penalty on z-space distances) rather than through principled GP training procedures such as marginal likelihood maximization or variational inference. The paper explicitly states this objective is "specifically designed for modeling the stochasticity of subgoal space" and provides no justification connecting it to the probabilistic GP model. This means the GP is used as a smooth interpolation layer whose parameters are fitted to a heuristic geometric constraint rather than through Bayesian principles. While the method still produces a legitimate posterior *given* the fitted hyperparameters, the "probabilistic" framing is weakened because the hyperparameters that define the prior are themselves tuned to a heuristic task loss rather than inferred from data. This is a structural concern — the contribution statement promises probabilistic subgoal representations, but the learning procedure is not probabilistic.

- **Baseline configurations are not justified for the modified evaluation protocol.** The paper makes environments substantially more challenging than those in prior work: stochastic action noise (σ=0.1), stricter success criteria (ℓ² distance 1.5 vs. 5), sparse external rewards alongside dense, and random start/goal positions (Sec. 5.1). The baselines (LESSON, HESS, HRAC) were originally designed and tuned for simpler settings — notably, HESS assumes fixed start and goal positions. The paper does not report whether these baselines were re-tuned for the new conditions, nor does it include experiments on the original (simpler) task configurations to verify the baselines are still competitive. This introduces uncertainty about whether the observed improvements stem from HLPS's design or from task modifications that disadvantage the prior methods.

- **Ablation does not isolate the GP component from the loss function.** The ablation study (Fig. 8) compares HLPS against: (a) HLPS-A which omits both the probabilistic representation and the proposed objective, and (b) HLPS-B which adds the probabilistic representation back but uses a contrastive objective from LESSON. This design confounds two factors — the GP layer and the proposed objective — because HLPS-B differs from HLPS in both the objective *and* the hyperparameter learning procedure. A cleaner ablation would compare against a version that uses the same encoding network and the same learning objective but replaces the GP layer with a feed-forward network that outputs z directly, isolating whether the GP structure itself provides benefit beyond the loss function.

### Minor

- **The probabilistic nature is not leveraged during execution.** The subgoal representation used at test time is the posterior mean of the GP (line 120: "Z can be restored by taking the posterior mean"). The posterior covariance is computed but never exploited for exploration bonuses, uncertainty-aware planning, or modulating intrinsic rewards. The practical benefit of the probabilistic formulation therefore reduces to a learning-time regularization effect. While this does not invalidate the method, it narrows the gap between the claimed contribution ("probabilistic subgoal representation") and what is actually used at inference time.

- **The ∝ notation in the learning objective is underspecified.** In Eq. 3, the quantities Δᶠ¹, Δᶠᵏ, Δᶻ¹, Δᶻᵏ are defined as "proportional to" Euclidean distances in their respective spaces, with no proportionality constants or scaling specified. This makes the objective partially ill-defined and harms reproducibility. In practice, they are presumably set to 1 (i.e., the distances themselves), but this should be stated explicitly.

- **Missing training procedure details.** The paper does not describe the optimization schedule for the GP hyperparameters (σ², γ², ℓ), how the encoding network and GP layer are trained jointly (alternating updates vs. shared gradients through the posterior mean), or any regularization/normalization in the latent space. These details affect reproducibility.

### Trivial

None.

## Nice-to-Haves

- **Use of posterior variance during execution:** Even a simple experiment using posterior variance as an exploration bonus for the high-level policy would demonstrate the probabilistic nature serves a concrete purpose beyond training regularization.
- **Quantitative stability metric:** Computing correlation or distance between latent representations of the same state across training checkpoints would strengthen the stability claim beyond visual inspection.
- **Ablation replacing GP layer with a deterministic network:** Comparing HLPS against a version with the same loss but a feed-forward network instead of the GP layer would directly test whether the GP structure matters beyond the loss.
- **Discussion of limitations:** The paper does not address sensitivity to kernel choice, the stationarity assumption, or potential unstable gradients when backpropagating through the GP posterior mean.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Harsh critic's claim that the method "does not actually learn a posterior distribution over subgoal representation functions."** This is an overstatement. The method *does* compute a GP posterior distribution P(Z|S, F) given the learned hyperparameters. The issue is that hyperparameters are learned via a heuristic rather than marginal likelihood — but the posterior computation itself is legitimate. The representation *is* probabilistic; the weakness is about how the prior's parameters are obtained, not about whether a distribution exists.

- **Harsh critic's claim that "the practical benefit reduces to a learning-time regularization effect which could perhaps be achieved by other means."** The latter speculation about alternative methods is not a valid weakness. The learning-time benefit of probabilistic representations is genuine and demonstrated.

- **Strength Finder's output about HLPS showing "significantly smaller performance degradation as stochasticity increases"** — this conflicts with the verified baseline-tuning concern. I keep the strength because it is a genuine empirical observation, but note the caveat about baseline tuning in the major weaknesses.

## Novel Insights

The most interesting observation from synthesizing the reviews is that the paper's core technical achievement — the state-space GP formulation for constant-complexity online inference in HRL — is actually its strongest and most defensible contribution, rather than the "probabilistic" framing per se. The online inference method (Sec. 3.4) is genuinely novel and practically valuable, while the probabilistic claim is significantly diluted by the heuristic hyperparameter learning objective. If the authors were to reframe the contribution around "GP-regularized subgoal representations with efficient online inference" rather than "probabilistic subgoal representations," many of the harsh critic's concerns would be addressed. The experimental results are genuinely promising, but the baseline comparison is the main threat to validity.

## Suggestions

1. **Address the baseline tuning concern.** Re-run baselines on the original (simpler) task configurations to verify they achieve their reported performance, and document the hyperparameter search for the modified tasks. If resources permit, include a controlled comparison where baselines are tuned on the same random-start, stochastic environment configurations.
2. **Principled GP hyperparameter learning.** Either (a) adopt a proper marginal likelihood maximization for the GP hyperparameters and justify the task-specific loss as an auxiliary objective, or (b) reframe the contribution to de-emphasize "probabilistic" and focus on "GP-regularized smooth interpolation with a task-specific distance metric." Option (b) is less work and more honest to what the method actually does.
3. **Isolate the GP layer in ablations.** Compare against a variant with the same learning objective but a feed-forward network replacing the GP layer, to demonstrate the value of the GP structure itself.
4. **Document training details.** Specify how the encoding network and GP layer are optimized jointly, the learning rate schedule for GP hyperparameters, and any normalization in the latent space.

## Score and Decision

The paper identifies a real limitation of deterministic subgoal representations in HRL and proposes a novel GP-based approach with a clever online inference scheme. The experimental results are suggestive and the qualitative analysis is informative. However, two significant concerns prevent acceptance: (1) the heuristic learning objective undercuts the "probabilistic" framing that is central to the paper's contribution claim, and (2) the experimental comparison to baselines is weakened by unverified tuning for the modified evaluation protocol. These issues require substantial revision to resolve. The core ideas have merit, but the paper as presented does not fully deliver what it promises.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>