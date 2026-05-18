Now I have all the information needed. Let me write the final consolidated review.

---

## Summary

This paper proposes "Preference Control RL" (PCRL), a framework for training a single meta-policy conditioned on a user-provided preference vector that controls the trade-off among multiple conflicting objectives in MORL. The core algorithmic contribution is PreCo, a gradient-manipulation method that augments the standard MGDA-style min-norm update with a similarity gradient from a carefully designed similarity function, aiming to produce Pareto-optimal solutions aligned with the input preference. The paper claims theoretical convergence guarantees and presents experiments across four environments (Fruit-Tree, MO-Ant, MO-Hopper, MO-Reacher) with up to 6 objectives, using both TD3 (continuous) and PPO (discrete). Results show PreCo consistently achieves strong hypervolume and cosine similarity, with notably better controllability than linear scalarization baselines.

## Strengths

- **Novel preference-conditioned MORL formulation with a clear motivation.** The paper correctly identifies the limitations of linear scalarization in MORL — inability to reach non-convex Pareto front regions and lack of precise controllability — and frames preference-conditioned meta-policy learning as a solution. The proposed similarity function Ψ(p,v) = -½ || max_i(v_i/p_i)p - v ||² is a principled design that encourages focusing on the least-satisfied objective relative to the preference.

- **Consistent empirical superiority across diverse environments.** PreCo achieves the highest hypervolume (HV) in all Fruit-Tree settings (3–6 objectives, Table 1), the highest HV in MO-Hopper (Fig. 6), and is one of only two methods (alongside EPO) that produce preference-specific state coverages in MO-Reacher (Fig. 8b), directly supporting the central claim of controllability. The 5-seed results with standard deviations provide reasonable statistical evidence.

- **Scalability to many objectives demonstrated.** The Fruit-Tree experiments with up to 6 objectives show that LS collapses to a single solution regardless of preference while PreCo maintains diverse, non-dominated value vectors (Fig. 4). This is a genuine advantage over LS-based approaches.

- **Computational efficiency consideration.** The paper notes that solving the min-norm problem at the policy-output level (size m×B) rather than the parameter level (size m×M) avoids the memory and computational cost of handling high-dimensional parameter gradients — a practical concern for large models.

- **Compatibility with multiple base RL algorithms and MOO methods.** The PCRL scheme is demonstrated with TD3 (continuous control) and PPO (discrete control) and supports plugging in various gradient manipulation methods (EPO, CAGrad, SDMGrad) as alternatives to PreCo.

## Weaknesses

### Major

- **Section 4 (Theoretical Analysis) is substantially incomplete in the main text.** Despite the abstract and introduction explicitly claiming "convergence and controllability are theoretically justified" and "comprehensive convergence analysis for stochastic optimization with non-convex smooth objective functions," Section 4 consists only of Definition 4.1 (the similarity function), a one-sentence intuition, and a brief statement that "we analyze the convergence rate of the proposed PreCo update in the stochastic gradient setting" referencing Algorithm 1. No theorem statements, lemmas, convergence rate bounds, or even informal statements of the guarantees are presented in the main text. Even if all proofs are deferred to a supplementary appendix (which is standard), the paper should state the main theoretical result in the body. As it stands, a reader of the main paper cannot evaluate the strength or validity of the claimed theoretical contribution.

### Minor

- **The computation of ∇_{π_p} v̂^{π_p} is underspecified for stochastic/discrete policies.** The paper asserts that the Jacobian "can be obtained by conventional RL methods, such as the policy gradient and the deterministic policy gradient" and that the method applies to "both discrete action space and continuous action space." However, for PPO-based discrete-action environments (Fruit-Tree, MO-Reacher), the paper does not explain how the gradient with respect to the policy *output* (rather than parameters) is obtained, nor whether reparameterization or another technique is used. The concept is not fundamentally problematic — standard backpropagation through the policy network handles it — but the presentation lacks sufficient detail for reproducibility, and the claimed computational advantage of "policy-level" vs "parameter-level" computation requires clearer justification for stochastic policies.

- **Baseline adaptation descriptions are too vague to assess fairness.** CAGrad is described as "modified to be a common ascent direction not is not too far from the similarity gradient" — a significant departure from original CAGrad (which uses the average gradient as reference), with no details on how the constraint parameter or adaptation procedure differs. EPO's two-mode implementation ("low similarity" vs "high similarity") is described in one sentence. Without precise formulations, it is unclear whether the baselines are implemented in a way that reflects their original design intent.

- **The SDMGrad-vs-PreCo comparison is not a clean ablation for the similarity function.** The paper frames SDMGrad as an ablation case, but SDMGrad replaces the similarity gradient with a convex combination of objective gradients — meaning the two methods differ in more than just the presence of the similarity term (the min-norm objective itself changes). Attributing performance differences solely to the similarity function is not cleanly supported without additional controls.

- **Inconsistency between the preference domain definition and experimental usage.** The paper defines the preference set as 𝒫 = {p ∈ ℝᵐ : pᵀ1 = 1, p ≻ 0} (strictly positive entries). However, the MO-Reacher evaluation uses preferences with zero entries ([0,1,0,0], [0,0.66,0.33,0], [0,0.33,0.66,0], [0,0,1,0]). Since the proposed similarity function involves max_i(v_i/p_i), division by p_i=0 is undefined. The paper does not address how this is handled (e.g., via epsilon smoothing or another mechanism).

- **The underperformance of EPO and CAGrad below the random baseline in MO-Reacher (Fig. 7) receives only a brief explanation.** The paper attributes this to "high variance in the gradients for model update" from uniformly sampling preferences. While plausible, no learning curves, hyperparameter tuning details, or diagnostic analysis are provided to support this interpretation. This weakens confidence that the baselines were properly adapted to this setting.

### Trivial

- Line 163: "LS agent policy is not uncontrollable by p" — appears to be a double negative; the intended meaning is "not controllable."
- Line 48: "The threes plots" → "The three plots"

## Nice-to-Haves

- The paper could briefly explain how the min-norm problem in Equation (6) is solved in practice (e.g., via a linear system, convex QP solver, or iterative method), to support the claimed computational efficiency.
- A discussion of the limitation that preferences must have strictly positive entries (or an epsilon-padded variant) would strengthen the paper's completeness.
- Learning curves for the MO-Reacher environment (and others) would help readers assess convergence behavior and diagnose the baselines' poor performance.
- The related work section could be expanded to more clearly position PreCo against prior preference-conditioned MORL approaches (e.g., conditioned-policy methods by Yang et al., Abels et al.).

## Removed Points

These points from the Harsh Critic were removed for the following reasons:

- **"Gradient computation with respect to the policy output is not adequately justified and may not be well-defined for all settings"** — The gradient IS well-defined via conventional RL methods (policy gradient / DPG) and standard backpropagation. The paper's description is underspecified (kept as a Minor weakness above), but the reviewer's characterization of a "fundamental gap" and claims about non-existence for discrete policies are inaccurate. The gradient exists for all differentiable policy parameterizations.
- **"The definition of similarity is introduced without intuition"** — The paper provides intuition: "Intuitively, the similarity gradient ∇_v Ψ(p,v) encourages to focus on the less optimal objectives to reach the preference p." The reviewer missed this.
- **"A discussion of limitations is missing"** — This is a nice-to-have, not a weakness. Moved to Nice-to-Haves.
- **"Missing related works"** — Removed per instructions (cannot independently verify existence of missing references).
- **"The main paper should include Algorithm 1"** — Removed per instructions about parser-stripped appendix content. The algorithm exists in the original submission.
- **"The paper does not discuss the optimization problem in Equation 6"** — The paper notes it's a min-norm problem similar to MGDA, which is a standard formulation solved via quadratic programming. The computational efficiency discussion is present (m×B vs m×M). This is a nice-to-have elaboration, not a weakness.
- **"No hyperparameter search details"** — Five-seed results with standard deviations are reported. Hyperparameter tuning demands are context-dependent; the paper's level of reporting is within normal practice for MORL conference papers. This is a wishlist item.

## Novel Insights

Beyond the paper's own contributions, the reviews collectively highlight a recurring tension in MORL papers that bridge MOO (multi-objective optimization) and RL: MOO methods typically assume access to exact gradients in a stationary setting, while RL provides noisy, high-variance, non-stationary gradient estimates from policy evaluation. The paper's empirical observation that EPO and CAGrad (which are well-behaved in supervised MOO) degrade badly in MORL settings like MO-Reacher — even below random — suggests that the interaction between non-stationary RL gradients and preference-conditioned training is not yet well understood. PreCo's robustness in these same settings may be as much about the structure of its min-norm+similarity formulation providing a natural regularizer against gradient variance as about achieving preference alignment per se. This distinction is worth deeper investigation.

## Suggestions

1. **Move the main theoretical result into Section 4 of the main text.** At minimum, state a theorem: e.g., "Under Assumptions A1–A3, PreCo with stochastic gradients converges to a Pareto stationary point at rate O(1/T)" or similar. A brief proof sketch (1–2 paragraphs) would greatly improve readability. The full proof can remain in the appendix.

2. **Clarify how ∇_{π_p} v̂^{π_p} is computed for each policy type.** Provide separate explanations for TD3 (deterministic continuous: DPG through Q) and PPO (stochastic/discrete: policy gradient through logits, using the reparameterization trick or score function as appropriate). If the "policy-level" computation requires additional storage (e.g., storing the Jacobian), discuss whether the claimed memory advantage still holds.

3. **Provide full implementation details for adapted baselines.** For CAGrad, specify whether the constraint radius c is tuned and how the reference direction is set. For EPO, describe the similarity threshold and how the two modes are selected. Add a brief justification for any modifications.

4. **Address the preference-zero inconsistency.** If a small epsilon is added to preferences during training, state this explicitly. If the similarity function is only used for training and evaluation uses a different metric, clarify.

5. **Add learning curves.** Convergence plots for at least one environment would help assess whether all methods received adequate training budgets and would strengthen the interpretation of the MO-Reacher results.

6. **Correct typos.** Fix "not uncontrollable" → "not controllable" (line 163) and "the threes plots" → "the three plots" (line 48).

## Score and Decision

**Originality:** Moderate. The preference-conditioned meta-policy direction is not entirely new (building on conditioned policies in MORL), but the PreCo update combining min-norm optimization with a novel similarity function is a specific contribution.

**Importance of research question:** High. Controllable multi-objective RL is practically important for applications requiring trade-off specification at deployment time.

**Claims support:** Moderate. The empirical results support the performance claims, but the theoretical claims are not assessable from the main text, and some experimental details (baseline adaptations, gradient computation) are underspecified.

**Soundness:** Moderate. The experimental methodology (5 seeds, multiple environments, both discrete and continuous) is reasonable, but the underspecification of gradient computation and baseline adaptations creates uncertainty.

**Clarity:** Below average. The paper is readable at a high level but lacks precision in key technical details (gradient computation, baseline implementations, theoretical claims).

**Value to community:** Moderate. If the method holds up, it provides a useful algorithm for preference-conditioned MORL. The current presentation, however, needs revision before it can be reliably built upon.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>