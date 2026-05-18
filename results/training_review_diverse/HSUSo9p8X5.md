Now I have a thorough understanding of both the paper and the reviewer claims. Let me produce the final consolidated review.

## Summary

This paper introduces a Gaussian Process (GP) based probabilistic subgoal representation for goal-conditioned hierarchical reinforcement learning (HRL). Instead of learning a deterministic mapping from states to subgoal representations (as in prior work like LESSON), the method places a GP prior on the latent subgoal space, producing a posterior distribution over representation functions. This probabilistic treatment is designed to capture uncertainty from environmental stochasticity and unexplored states, leading to more stable subgoal embeddings, improved robustness, and transferable representations. An efficient online inference procedure using state-space GP (Kalman-filter-like updates) enables constant per-step complexity. Experiments on continuous control tasks (Ant Maze variants, 7-DOF robotic arm environments) show consistent advantages over HESS, LESSON, HRAC, and TD3 in sample efficiency, asymptotic performance, and robustness to noise.

## Strengths

- **Novel application of GPs to subgoal representation in HRL**: The paper is the first to use a GP prior over the subgoal representation function, producing a distribution over functions rather than a single deterministic mapping. This is a conceptually clean way to capture uncertainty in the subgoal space, distinct from VAE-based approaches that model distributions over latent variables given a fixed encoder.

- **Strong and consistent empirical results**: Across six diverse environments (Ant Maze, Ant Push, Ant Fall, Ant FourRooms, 7-DOF Reacher, 7-DOF Pusher) with sparse/dense rewards, image observations, and random start/goal positions, HLPS consistently outperforms all baselines (LESSON, HESS, HRAC, TD3) in both sample efficiency and asymptotic performance (Figs. 3, 4). The advantage is most pronounced in the most challenging tasks (Ant Fall, Ant FourRooms with images).

- **Demonstrated robustness to environmental stochasticity**: When Gaussian noise is added to agent positions at σ ∈ {0, 0.1, 0.15}, HLPS shows substantially smaller performance degradation and lower variance than LESSON and HESS (Fig. 7, left). This directly validates the core motivation that probabilistic representations better handle stochastic uncertainties.

- **Stable and reachable subgoal embeddings**: The visualization in Fig. 6 qualitatively shows that HLPS maintains consistent subgoal embeddings across training, with subgoals aligned to low-level trajectories. In contrast, HESS and LESSON produce unstable, shifting embeddings with unreachable subgoals. This stability addresses a key non-stationarity problem in off-policy HRL.

- **Efficient online inference with O(1) complexity**: The state-space GP formulation (Section 3.4) converts batch GP inference into recursive Kalman-filter-like updates, enabling constant per-step computation and memory for online subgoal generation. This makes the probabilistic approach practical for real-time deployment.

## Weaknesses

### Major

1. **Learning objective is heuristic and disconnected from the GP's probabilistic machinery.** The loss in Eq. (4) is a task-designed contrastive-style objective (softplus of differences in latent distances, weighted by a ratio of encoding distances) that does not derive from the GP's marginal likelihood, ELBO, or any standard probabilistic inference principle. The paper states that this loss learns the GP hyperparameters (σ², γ², ℓ), but the objective has no probabilistic interpretation relative to the GP prior or posterior. While training GP hyperparameters with a downstream task loss is a valid engineering approach, the paper overclaims by suggesting this constitutes learning a "posterior distribution over subgoal representation functions" in a principled Bayesian sense. The probabilistic claim would be substantially stronger if the core learning signal came from the GP's own marginal likelihood, with the heuristic loss as a regularizer or auxiliary term.

2. **The batch and online GP formulations are not the same model, and the relationship is under-explained.** The batch GP (Eq. 1-2) defines a kernel over the full multi-dimensional state space, considering all pairs of states. The online formulation (Section 3.4) converts this to a one-dimensional state-space GP where the evolution operator Ψ_i depends only on the scalar distance ΔS_i = D(s_i, s_{i-1}) between consecutive states along a trajectory. The paper acknowledges this as a "relaxation" to a Markov chain (line 172), but does not analyze the approximation error or discuss when it is valid. A GP with a Matérn kernel over a multi-dimensional input is not generally a Markov chain in the trajectory index; the state-space GP form for Matérn kernels is exact only for 1D inputs. The paper relies on this relaxation without justification, and the claim that the online formulation "preserves the GP posterior on the original state space" is misleading.

3. **Missing algorithmic specification of the joint training procedure.** The paper claims that "our method learns φ(s) simultaneously with the hierarchical policy" and that the objective "cohesively integrates" representation and policy learning, but provides no pseudocode or precise description of the training loop. Key questions left unanswered: (a) Are GP hyperparameters updated jointly with policy parameters via gradient sharing, or alternately? (b) How often is batch GP inference (Eq. 2) performed during training—every step, every episode, every k steps? (c) How is the representation loss (Eq. 4) combined with the SAC losses for the two levels? (d) The encoding network that produces f feeds into the GP layer—are its weights trained through the GP posterior, through the heuristic loss, or both? Without these details, the method is difficult to reproduce and it is unclear whether gains come from the probabilistic representation or from specific training choices.

### Minor

1. **Transfer experiments lack baseline comparisons.** Fig. 6 shows that HLPS with transferred subgoal representation and low-level policy outperforms HLPS learning from scratch on the target task. However, there is no comparison showing whether LESSON or HESS (with similar transfer) would also benefit—or whether the probabilistic nature of HLPS specifically facilitates transferability. The claim that probabilistic representations "facilitate transfer relative to deterministic ones" is therefore unsubstantiated by the current experiments.

2. **"First probabilistic subgoal representation" claim needs qualification.** VAE-based approaches (Pere et al., Nasiriany et al., Nair et al.), which the paper cites in related work, produce distributions over latent subgoal variables (encoder outputs distributions over latents). The paper's contribution is a distribution over *functions* rather than over latents *given* a function, which is a meaningful distinction. However, the abstract's phrasing ("the first probabilistic subgoal representation") without acknowledging prior probabilistic approaches is imprecise and could confuse readers.

3. **The learning objective (Eq. 4) uses imprecise notation.** The Δ terms are defined with ∝ (proportional to) symbols and the index ranges are not specified. The reader cannot determine how the loss is computed over a trajectory—whether it averages over all i, samples specific pairs, or uses a fixed window. This obscures an important implementation detail.

4. **No deterministic-environment results for the Maze tasks.** All Maze experiments in the main comparison use added Gaussian noise (σ=0.1, as stated on line 333). While the robotic arm experiments (Reacher, Pusher) appear to be fully deterministic, the core claim of "outperforming baselines in standard benchmarks" would be better supported by also showing results on the fully deterministic variants of the Maze tasks. Without this, it is unclear how much of HLPS's advantage is due to its stochasticity handling vs. other factors.

5. **No wall-clock time or step-count efficiency comparison.** The paper claims "lightweight" and "constant computational complexity" for online inference but does not report training wall-clock time or per-step compute compared to LESSON/HESS. The batch estimation phase uses matrix inversion (cubic in window size T=3), so the overall training cost matters.

### Trivial

- The ∝ notation and missing index ranges in Eq. (4) should be clarified.
- The paper states that baselines were evaluated in settings with random start/goal, but does not specify whether LESSON and HESS were re-tuned for these new conditions.

## Nice-to-Haves

- An ablation comparing the heuristic loss (Eq. 4) against a loss that includes the GP marginal likelihood (even approximately) would greatly strengthen the claim that the method is truly "probabilistic" rather than a GP-smoothed neural network trained with a task loss.
- A comparison on fully deterministic Maze tasks (without added noise) would clarify whether HLPS's advantages extend beyond stochasticity handling.
- Comparison with transferred baselines (LESSON-transfer, HESS-transfer) would substantiate the transferability claims.
- Pseudocode or an algorithm box summarizing the training loop would substantially improve reproducibility.
- A brief analysis of the approximation error introduced by the Markov-chain relaxation of the batch GP would strengthen the theoretical foundation.

## Removed Points

The following criticisms from the harsh reviewer were removed as inaccurate:

- **"Ablation results weaken the contribution... The paper does not comment on this."** — The paper explicitly comments on the ablation at line 417: "HLPS-BL-B exhibits much higher asymptotic performance than HLPS-BL-A but slightly lower performance than HLPS. This empirically demonstrates the effectiveness of our probabilistic subgoal representation and learning objective respectively." The reviewer's claim is contradicted by the paper text.
- **"Model inconsistency... neither stated nor justified."** — The paper does state this is a relaxation at line 172: "our model can be relaxed to a direct graph, i.e., Markov chain." The statement is present; the issue is the level of justification, which is captured in the modified major weakness above.
- **"Deterministic environment results... only shows results with added noise."** — The paper explicitly includes Reacher and Pusher environments (Fig. 4) which do not mention added noise, and the abstract states "both deterministic and stochastic settings." The claim is factually incorrect.
- Generic/non-specific strengths from the Strength Finder (e.g., "novel learning objective" as listed abstractly without specific evidence) have been folded into the properly evidenced strengths above.

## Novel Insights

The reviews reveal an interesting tension: the paper's primary empirical contribution (stable, reachable subgoal embeddings via GPs) is well-supported by the visualization (Fig. 6) and robustness experiments. However, there is a gap between the paper's framing as a "principled probabilistic model" with Bayesian posterior updating and the actual learning procedure, which uses a heuristic contrastive-style loss to train GP hyperparameters. The GP is used more as a structured smoothing mechanism that enforces global (as opposed to local) constraints on the latent space rather than as a fully Bayesian inference machine. This insight suggests that the paper's main advantage may come from the GP's ability to encode long-range correlations in state space (through the Matérn kernel) rather than from the probabilistic computation per se. The strong performance of HLPS-BL-B (GP + LESSON-style contrastive loss) in the ablation supports this interpretation. The reviews collectively suggest that the paper would be stronger if it reframed the contribution around "GP-structured subgoal representations with global constraints" rather than overclaiming Bayesian inference.

## Suggestions

1. **Clarify the learning procedure with pseudocode.** Provide explicit details on: (a) how the GP hyperparameters and the encoding network are updated relative to the policy networks, (b) how often batch estimation occurs, and (c) how the loss in Eq. (4) is computed over mini-batches of transitions.

2. **Acknowledge the heuristic nature of the learning objective.** Reframe the contribution: the GP provides a structured prior with learnable hyperparameters, whose values are set by a task-specific objective. This is a practical design choice, not a fully Bayesian procedure. The phrase "learning a posterior over subgoal representation functions" is technically true of the GP inference step, but the hyperparameter learning is not derived from the posterior—clarify this distinction.

3. **Add baseline comparisons for transfer experiments.** Show whether LESSON and HESS also benefit from transferring subgoal representations, to substantiate the claim that HLPS's probabilistic nature specifically enables transfer.

4. **Analyze the batch-to-online approximation.** Provide a brief discussion of when the Markov-chain relaxation of the GP is faithful to the original model and when errors may arise. This could be a small empirical study or a theoretical statement referencing the relevant GP literature (Särkkä 2013).

5. **Report deterministic Maze results.** Include a version of the Maze experiments without added noise, so readers can distinguish robustness improvements from general performance improvements.

## Score and Decision

The paper introduces a genuinely novel approach to subgoal representation in HRL, with strong empirical results across challenging benchmarks and clear qualitative evidence of the method's benefits (stable embeddings, robustness to noise, transferability). The weaknesses are real but addressable: the learning objective is heuristic rather than derived from the GP's likelihood, the batch/online relationship is underexplained, and training details are underspecified. None of these weaknesses invalidate the core empirical contributions, but they should be addressed to strengthen the paper's theoretical framing and reproducibility. I recommend acceptance with a request for major clarifications.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>