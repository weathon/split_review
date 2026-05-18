I have thoroughly reviewed the paper against both reviewer inputs. Let me now produce the consolidated review.

---

## Summary

This paper introduces HLPS, a method for goal-conditioned hierarchical reinforcement learning that replaces the deterministic subgoal representations used in prior work (e.g., LESSON, HESS) with a Gaussian Process prior over the latent subgoal space. The GP captures long-range correlations via a Matérn kernel with learnable hyperparameters, and a novel learning objective (Eq. 3) jointly optimizes those hyperparameters alongside hierarchical SAC policies. An efficient online inference scheme is derived using a state-space GP formulation (Kalman-filter-like updates) that avoids cubic batch cost. Experiments on MuJoCo-based continuous control tasks with stochastic dynamics, sparse rewards, and image observations show consistent improvements over LESSON, HESS, HRAC, and TD3 in sample efficiency, asymptotic performance, robustness, and transferability.

## Strengths

- **First application of GP priors to subgoal representation in HRL.** The paper formulates subgoal learning as a GP regression problem (Eq. 1), producing a posterior distribution over representation functions rather than a single deterministic mapping. This is a genuinely novel framing that departs from the slowness/contrastive objectives of LESSON and HESS. The nonparametric GP with a learnable Matérn kernel provides global smoothing that explicitly captures long-range correlations in state space — a capability absent from prior local-constraint methods (Section 3.2, Fig. 5/fig:visual).

- **Strong and consistent empirical results.** HLPS outperforms all baselines across multiple challenging task families (Ant Maze variants, robotic arm tasks), under both sparse and dense rewards, with and without image observations (Fig. 3/fig:comparison, Fig. 4/fig:fetch). The advantage is largest in high-dimensional image-based tasks and stochastic environments, where deterministic representations struggle most. Results are reported with 95% CI over 10 trials.

- **Demonstrated robustness to environmental stochasticity.** A focused experiment (Fig. 6 left) shows HLPS degrades significantly less than LESSON and HESS as Gaussian noise increases from σ=0 to σ=0.15, with lower variance in outcomes — directly supporting the claim that the probabilistic formulation handles uncertainty better.

- **Transfer learning is demonstrated.** Initializing target tasks (Ant Push) with subgoal representations and low-level policies learned on source tasks (Ant Fall) yields clear gains in sample efficiency and asymptotic performance for both state-based and image-based variants (Fig. 7/fig:transfer2).

- **Ablation cleanly isolates the two components.** HLPS-BL-A (no GP, no proposed objective) vs. HLPS-BL-B (GP with LESSON's contrastive objective) vs. full HLPS (GP + proposed objective) shows that (i) the GP framework itself provides a large boost, and (ii) the proposed learning objective adds further improvement (Fig. 8/fig:ablation). This is informative ablation design.

## Weaknesses

### Fatal

None.

### Major

- **The probabilistic machinery is not fully exploited by the policies.** The paper repeatedly frames the key advantage as "probabilistic" — "a continuum of possible subgoal representation functions," "coping with stochastic uncertainties," "capturing the posterior distribution." However, the subgoal actually fed to both the high-level and low-level policies is the *posterior mean* (a deterministic point estimate; line 120: "the subgoal representation, Z can be restored by taking the posterior mean of the GP"). The posterior variance is never propagated into action selection, exploration bonuses, or planning. The observed benefits therefore plausibly stem from the GP's *global kernel-induced smoothing* (which a deterministic nonparametric method could also provide), not from any uncertainty-aware decision-making. The paper should either (a) use the uncertainty (e.g., high-level exploration via predictive variance, uncertainty-penalized intrinsic rewards) or (b) explicitly reframe the contribution as "learning globally smooth subgoal spaces via GP priors" and qualify the "probabilistic" language accordingly. *Evidence: Eq. 2 and surrounding text in Section 3.2; the entire Section 3.4 describes policies receiving the posterior mean; no experiment incorporates the posterior variance into decision-making.*

- **The training procedure is underspecified.** The paper claims Eq. 3 "cohesively integrates the learning of probabilistic subgoal representations and hierarchical policies" and describes "simultaneous" or "joint" learning (abstract, Section 3.3). However, the paper never specifies how the GP hyperparameter objective is optimized relative to the two SAC objectives. Is it an auxiliary loss added to the combined RL loss? Is it optimized in alternating gradient steps? What is the gradient flow from Eq. 3 through the GP posterior mean to the encoder and the policies? Without this information, the paper's central methodological claim — a unified framework — is not reproducible. *Evidence: Section 3.3 provides only the loss expression; no training loop, pseudocode, or optimization schedule is given anywhere in the paper.*

### Minor

- **Scaling of the state-space GP to d-dimensional latent spaces is unclear.** Section 3.4 derives the state-space GP formulation for the Matérn 3/2 kernel, but the derivation (matrices Ψᵢ, h, etc.) corresponds to a *one-dimensional* latent process. The subgoal representation z is d-dimensional (line 87: φ(s) : s ↦ ℝᵈ). The paper does not explain whether d independent 1D GPs are run in parallel, or whether correlations across dimensions are modeled. The claim of "constant computational and memory complexity per state" (line 173) is therefore ambiguous — it is O(1) per state in the number of data points but scales with d. A clarification would also help practitioners understand the practical cost. *Evidence: Section 3.4, Eq. 5–8 show 2×2 matrices and a 2D state vector, consistent only with a 1D latent process.*

- **The tightening of the success criterion (ℓ² distance from 5 to 1.5) may disadvantage baselines that were originally tuned for the easier criterion.** The paper states this tightening (line 334) but does not confirm whether baselines (LESSON, HESS, HRAC) were re-tuned for this harder setting. Since hyperparameters like subgoal tolerance or intrinsic reward scaling may depend on the success threshold, a fair comparison requires either re-tuning or an explicit statement that the default hyperparameters are robust to this change. *Evidence: lines 333–335.*

- **No discussion of limitations, computational overhead, or failure modes.** The paper mentions no scenarios where HLPS might underperform, no comparison of wall-clock time or sample-complexity overhead versus baselines (the batch GP inference has O(N³) cost during training; the paper only discusses the online efficiency), and no discussion of sensitivity to kernel choice or hyperparameters beyond the time-window ablation. While not fatal, this limits the paper's practical usefulness. *Evidence: Entire Section 5 (Conclusion) and no separate limitations section.*

### Trivial

None.

## Nice-to-Haves

- Include a deterministic kernel-based smoothing baseline (e.g., a deterministic RBF network with the same Matérn kernel) to isolate whether the GP's probabilistic nature or its global covariance structure drives the improvements. This would directly address the framing concern.
- Report mean ± std or a table of final asymptotic values for all methods and tasks to complement the learning curves.
- Provide full training pseudocode.
- Report performance on deterministic versions of the tasks alongside the stochastic ones to precisely quantify the robustness benefit.
- A statement about code release would aid reproducibility.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

1. **"Training procedure underspecified — no pseudocode"** → *Kept as Major (merged into weakness #2).*
2. **"The 'lightweight online formulation' is a known technique, presented as a contribution"** → *Removed. The paper explicitly cites Särkkä 2012, 2013 for the state-space GP derivation (line 173). The contribution is the *application* of this technique to HRL subgoal representation, not its invention. The scaling concern is retained as a separate Minor weakness.*
3. **"Missing HIRO comparison"** → *Removed. The paper compares to LESSON (which builds on HIRO's framework) and HRAC (which also uses pre-defined subgoal space like HIRO). Baseline coverage is adequate.*
4. **"First probabilistic subgoal representation claim vs VAE methods"** → *Removed. The paper explicitly distinguishes VAE-based methods as doing unsupervised observation compression "unable to encode the states of hierarchical temporal scales in HRL" (line 300). The claim is specific to subgoal representation in HRL and is defensible.*
5. **"Comparison conflates probabilistic with global smoothing"** → *Downgraded from the harsh critic's framing to a qualified note. The ablation (Fig. 8) already separates GP benefit from objective benefit. The issue is that the "probabilistic" framing is broader than what the empirical comparison strictly shows; this is now part of Major weakness #1.*
6. **"The proposed objective contributes little because HLPS ≈ HLPS-BL-B"** → *Removed. The paper describes HLPS-BL-B as showing "slightly lower performance than HLPS" (line 417). Even a modest gap on challenging tasks is meaningful, and the ablation *does* confirm that the objective contributes. This is not a weakness; rather it confirms both components matter.*
7. **"Ratio term justification is vague"** → *Removed. The paper provides an explicit rationale: "to enhance feature discrimination and the interaction between F and Z, we use the ratio ... focusing on the relative ratio rather than the absolute difference" (line 129). The explanation may be concise but is not absent.*
8. **Generic presentation/style nitpicks** → *Removed per instructions.*

## Novel Insights

Beyond the paper's own contributions, the reviews surface one useful observation not fully articulated in the paper: the ablation structure (BL-A → BL-B → HLPS) reveals that the GP's global smoothing provides the *dominant* performance gain, while the novel learning objective (Eq. 3) confers a secondary but real improvement. This suggests that the most impactful design decision is adopting a nonparametric global prior (GP or a deterministic equivalent) over local-constraint objectives, with the specific objective function being a refinement rather than the primary driver. The paper does not explicitly acknowledge this hierarchy of importance.

## Suggestions

1. Provide a complete training algorithm (pseudocode) showing how the GP hyperparameter loss (Eq. 3) is optimized relative to the two SAC losses — this is the single most important missing detail for reproducibility.
2. Qualify the "probabilistic" claims throughout: explicitly state that the policies use only the posterior mean, and clarify that the probabilistic framing contributes via Bayesian updating and kernel-induced global smoothing rather than uncertainty-propagated decision-making. Consider reframing the contribution as "learning globally smooth subgoal representations via GP priors."
3. Clarify how the state-space GP formulation scales to d-dimensional latent spaces — specifically whether dimensions are modeled independently and how the complexity relates to d.
4. Add a limitations paragraph: discuss computational overhead during training, hyperparameter sensitivity, and scenarios where the GP assumptions (smoothness, stationarity) might not hold.
5. State whether baselines were re-tuned for the tightened success criterion and random start/goal conditions, or include a small study showing hyperparameter robustness.

## Score and Decision

The paper introduces a novel, well-motivated idea (GP-based subgoal representations in HRL), provides an efficient online inference scheme, and presents strong empirical results across diverse and challenging tasks. The weaknesses are real but not structural: the main gap is a mismatch between the "probabilistic" framing and the actual usage of the uncertainty, and the training procedure needs fuller specification. Neither issue invalidates the core contribution. The paper makes a solid contribution to subgoal representation learning in HRL.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>