Now I have all the information I need. Let me write the consolidated review.

## Summary

This paper introduces a Gaussian Process (GP) based approach to learning probabilistic subgoal representations for goal-conditioned hierarchical RL (HRL), marking the first use of probabilistic (rather than deterministic) subgoal representations in this setting. The method places a GP prior over the latent subgoal space, learns kernel hyperparameters and an encoding network through a custom loss, and uses a state-space GP formulation for efficient online inference. Experiments across six continuous control tasks (standard and stochastic, dense and sparse reward, with and without image observations) show consistent improvements over deterministic baselines (LESSON, HESS, HRAC) and a flat RL baseline (TD3).

## Strengths

1. **First probabilistic subgoal representation in HRL**: The paper introduces GP priors over the latent subgoal space, which is a genuinely novel direction relative to the deterministic representations used in prior work (LESSON, HESS). The probabilistic framing provides a posterior distribution over subgoal functions rather than a single deterministic mapping. This is empirically validated: HLPS maintains more stable subgoal representations across training (Fig. 5), degrades less under increasing environmental stochasticity (Fig. 8 left), and shows lower variance in outcomes compared to deterministic approaches.

2. **Consistent empirical superiority across diverse challenging benchmarks**: The method outperforms four baselines on six environments under both deterministic and stochastic conditions, with dense and sparse rewards, and with low-resolution image inputs (Fig. 2, 3). The gains are largest in the hardest tasks (Ant Fall, Ant FourRooms, 7-DOF Reacher, 7-DOF Pusher) — precisely where deterministic representations struggle most. Experiments use 10 independent trials with 95% confidence intervals, giving reasonable statistical rigor.

3. **Lightweight online inference via state-space GP**: Section 3.4 derives a constant-memory, constant-computation sequential update (analogous to Kalman filtering) for online subgoal generation, using the Matérn kernel's Markovian structure. This is a practical contribution: it makes the GP formulation tractable for online HRL deployment, avoiding the cubic cost of batch GP inference.

4. **Demonstrated transfer learning**: The paper shows that the GP-based subgoal representation and low-level policy can be transferred between tasks (Ant Fall → Ant Push), yielding improved sample efficiency and asymptotic performance in the target task (Fig. 7). This supports the claim that the learned representation generalizes across related environments.

## Weaknesses

### Major

1. **The state-space GP formulation is claimed to be exact, but this claim is not technically accurate as stated.** The paper says the state-space formulation "can be solved exactly without approximations by state-space form GP" (Sec. 3.4). However, the original GP (Eq. 1) is defined on the high-dimensional state space with kernel κ(s_i, s_j) depending on the ℓ2-norm of the full state vectors. The state-space formulation instead operates on a one-dimensional "step" ΔS_i = D(s_i, s_{i-1}), a scalar. These are not equivalent in general: the state-space GP models a 1D process where correlation depends on *cumulative path distance*, while the original GP's kernel depends on *straight-line Euclidean distance* between states. These differ unless the trajectory is straight (by the triangle inequality, the cumulative path distance ≥ the straight-line distance). The method from Särkkä et al. is exact for Matérn kernels on a *1D input space*, but the paper is using it on a 1D *transformation* (cumulative distance) of the original high-dimensional inputs. This is an approximation, and claiming exactness without clarification is misleading. The core online inference method is still practically useful, but the claim needs to be corrected and the approximation characterized.

2. **The training objective (Eq. 4) is a heuristic with no principled connection to the GP probabilistic model, weakening the "probabilistic" framing.** The hyperparameters of the GP (γ², ℓ, σ²) and the encoding network are learned by minimizing a custom loss: L = (Δ_f¹/Δ_f^k)·log(1+exp(Δ_z¹-Δ_z^k)). The paper states this is for learning "the hyperparameters of our probabilistic subgoal representation" (Sec. 3.3). However, this loss is not derived from the GP marginal likelihood, an ELBO, or any other standard GP training criterion. It is a task-specific ratio-of-distances objective with a softplus hinge. The quantities Δ_f¹, Δ_f^k, Δ_z¹, Δ_z^k are only defined up to a proportionality constant (∝), leaving the loss underspecified — the actual scale matters when these appear in a ratio and difference within the same equation. The GP posterior is computed correctly *given* the learned parameters, but because those parameters are learned through a heuristic rather than a probabilistic criterion, the claim that the method provides a principled "probabilistic subgoal representation" is overstated. The paper would benefit from either grounding the objective in the GP's marginal likelihood or being more precise about what "probabilistic" means in this context.

### Minor

3. **The posterior variance from the GP is never leveraged.** The subgoal is taken as the posterior mean; the uncertainty estimates (posterior variance) are computed but not used — for example, as exploration bonuses, for uncertainty-aware subgoal sampling, or to modulate the high-level policy. This limits the practical benefit of the "probabilistic" aspect. While the GP mean still provides useful smoothing and long-range integration, a key distinguishing feature of the probabilistic approach remains unused. This is not a fatal issue but reduces the gap between this method and a deterministic approach with similar architecture.

4. **The T=3 time window choice is presented with an overstrong claim.** The ablation (Fig. 8 right) shows that larger time windows improve *early* performance, while final performance is similar. The paper reports all results with T=3 and says this is "without loss of generality." Since the paper's own data show a meaningful early-training disadvantage for T=3, "without loss of generality" overstates the case. The final asymptotic performance is similar, so this is not a fatal concern, but the claim should be qualified.

5. **The role of the proposed objective vs. the probabilistic formulation is not fully disentangled.** The ablation (Fig. 9) shows that HLPS-BL-B (probabilistic subgoal representation with a contrastive learning objective) achieves performance close to the full HLPS. The paper correctly notes that HLPS outperforms HLPS-BL-B, but the difference appears modest in the reported curves. This suggests that much of the gain comes from the GP framework itself rather than the specific proposed objective (Eq. 4), which the paper does not comment on. A clearer discussion of what each component contributes would strengthen the paper's contribution claims.

### Trivial

6. The quantities Δ_f¹, Δ_f^k, Δ_z¹, Δ_z^k are defined with "∝" (proportional to) but the proportionality constant is never specified. Since these appear in a ratio (Δ_f¹/Δ_f^k) and a softplus difference (Δ_z¹-Δ_z^k), the actual scale of the norms matters. The paper should either state that these are simply the Euclidean norms (Δ = ‖·‖) or define any rescaling explicitly.

## Nice-to-Haves

- The training objective could be grounded in the GP's marginal likelihood (or a variational approximation) to make the probabilistic machinery work end-to-end. This would sharpen the differentiation from deterministic alternatives.
- The posterior variance could be used as an exploration bonus or for uncertainty-aware subgoal generation, which would more fully leverage the probabilistic formulation.
- The paper tests only on MuJoCo-based continuous control tasks. Results on at least one additional domain would strengthen generality claims, though this is scope creep from the paper's current focus.

## Removed Points

- *Criticism about "no principled Bayesian training" being a fatal/structural flaw*: Removed to **Major** tier. The paper is transparent about proposing the loss in Eq. 4 as a learning objective. The GP posterior is still correctly computed given the learned parameters. The issue is one of overclaim in the "probabilistic" framing rather than a fatal invalidation of the method.
- *Criticism about the GP being "decorative"*: Removed to Minor. The GP still provides long-range correlation through the kernel and the posterior mean integrates information across states. The robustness to stochasticity shown empirically (Fig. 8 left) suggests the GP formulation provides real benefits even if only the mean is used.
- *Criticism that HLPS-BL-B performing "nearly as well" is a weakness*: This is an accurate description of the ablation results, but the paper correctly acknowledges it ("slightly lower performance"). It is an informative ablation finding, not a weakness of the paper.
- *Demand for tasks beyond MuJoCo*: Moved to Nice-to-Haves. The paper already tests on six diverse environments with image-based variants, which is a reasonable evaluation scope for a paper introducing a new method.

## Novel Insights

None beyond the paper's own contributions. The reviews largely converge on the same observations: the paper proposes a genuinely novel direction (GP-based probabilistic subgoal representations) with strong empirical results, but overstates the technical precision of its claims — particularly regarding the exactness of the state-space GP formulation and the principled connection between the training objective and the probabilistic model.

## Suggestions

1. **Correct the exactness claim for the state-space GP.** Explicitly state that the state-space formulation is exact for a 1D Matérn process along the cumulative path distance, and that this is an approximation to the original GP defined on the high-dimensional state space. Discuss when this approximation is reasonable (e.g., smooth trajectories on a manifold).

2. **Either ground the training objective in the GP marginal likelihood, or recalibrate the claims.** If retaining the heuristic objective, replace "∝" with explicit definitions and clarify that the hyperparameters are learned through a task-specific loss rather than Bayesian training. This would not diminish the contribution but would make the framing more accurate.

3. **Leverage the posterior variance** — even a simple exploration bonus based on GP uncertainty would demonstrate a concrete advantage of the probabilistic formulation over deterministic alternatives.

4. **Qualify the T=3 claim** — replace "without loss of generality" with a statement that T=3 was chosen for simplicity and yields comparable asymptotic performance, noting the early-training advantage of larger windows.

## Score and Decision

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>