- Decision: Reject
- Avg Score: 3.00
- Scores: 3, 3, 3
Now I have a comprehensive understanding of the paper and can verify each review claim against the actual text. Let me produce the final consolidated review.

## Summary

This paper proposes Goal2FlowNets (G2FN), which applies Generative Flow Networks (GFlowNets) to goal-conditioned RL. The key idea is to learn a diverse set of trajectories to each goal by conditioning the GFlowNet's forward policy, backward policy, and state flow function on the goal and timestep, using a uniform backward policy to encourage maximum entropy over successful trajectories. Experiments on MiniGrid and BabyAI environments show promising results in sample efficiency, zero-shot generalization to larger/complex environments, and learning-free few-shot adaptation via simulated rollouts.

## Strengths

- **Novel application of GFlowNets to goal-conditioned RL.** The paper is the first to use GFlowNets directly as policies in a typical RL setting (as opposed to object generation), conditioning the entire GFlowNet on goals and timesteps. This is a genuine methodological contribution that opens a new direction for connecting GFlowNet theory with RL exploration.

- **Impressive zero-shot generalization reported across several distribution shifts.** Table 2 (verified from the paper's text and captions) shows G2FN trained on Empty-5×5 achieving substantial success when tested zero-shot on much larger environments like Empty-16×16 and on environments with obstacles (LavaGapS7), while PPO and SAC collapse to near 0%. The paper provides standard deviations over 3 seeds for these results. This provides concrete evidence that learning a diverse trajectory distribution can transfer to unseen configurations.

- **Evidence of trajectory diversity (policy cover) on a simple grid.** The paper demonstrates via combinatorial analysis on Empty-5×5 (with direction removed) that a converged G2FN agent traverses all possible paths to the goal, while a PPO agent follows a deterministic path. Figure 5(b) visualizes this diversity, directly supporting the claim that G2FN learns a policy cover rather than a single route. The few-shot adaptation results (Table 3) further validate that this diversity has practical utility — diverse trajectories already contain behaviors useful in new environments.

- **The exploration mechanisms are principled and do not require hand-crafted heuristics.** As explained in Section 4, GFlowNets naturally put probability mass on all terminal states and learn off-policy, providing exploration without separate curiosity modules, count-based bonuses, or prediction error models. The uniform P_B design choice is well-motivated by the maximum-entropy-over-trajectories argument from Zhang et al. (2022).

## Weaknesses

### Fatal
None.

### Major

- **Missing comparisons to standard goal-conditioned RL baselines (HER, GCSL).** The paper compares against PPO, SAC, and DEIR, but does not compare to Hindsight Experience Replay (HER) or Goal-Conditioned Supervised Learning (GCSL), which are the most natural and widely-used baselines for the goal-conditioned RL setting. Without these comparisons, it is impossible to attribute the reported gains to trajectory diversity via GFlowNets rather than to basic off-policy learning or goal conditioning. The paper's central claim — that GFlowNet-based diversity is the driver of performance — requires a comparison against methods that share other features (off-policy learning, goal conditioning) but lack trajectory-level diversity.

- **No ablation of the uniform backward policy, which is the key design choice driving diversity.** The paper states (line 97) that a uniform P_B is used to "induce maximum entropy over successful trajectories," but never compares against: (a) a GFlowNet with a learned P_B, or (b) a GFlowNet where P_B is fixed to a different distribution. Without this ablation, the reader cannot determine whether the observed benefits come from the GFlowNet framework itself or from this specific design choice. This is the central mechanism claimed to produce diversity, and it is left untested.

- **The method is underspecified to the point of being non-reproducible.** The paper provides no neural network architecture details (number of layers, hidden sizes, whether separate heads are used for P_F, P_B, and F), no hyperparameter values (learning rate, batch size, replay buffer size, exploration schedule), no λ value for the SubTB(λ) objective, and no details on how the uniform backward policy is enforced (fixed or learned with stop-gradient). As stated in Section 4: "This is achieved by concatenating the goal and the timestep to the state" — this single sentence is the entirety of the architectural description. Reproducibility requires substantially more detail.

- **The policy cover analysis is limited to a single toy environment (Empty-5×5 with agent direction removed) and lacks quantitative diversity metrics for the main experiments.** The paper makes strong claims about learning a policy cover but only provides a combinatorial analysis after stripping the agent's direction from observations (a significant simplification). For the main environments (LavaGap, SimpleDoorKey, etc.), no quantitative measures of trajectory diversity are reported (e.g., number of unique successful trajectories, entropy over trajectories, coverage of the state space). Table 2 provides strong results, but without diversity metrics on these same environments, the connection between the claimed mechanism (trajectory diversity) and the observed outcomes (good generalization) is circumstantial.

### Minor

- **It is unclear whether the PPO and SAC baselines are goal-conditioned.** The paper describes goal-conditioned RL formally (Section 3.1: "the policy input is augmented π(a_t | s_t, g_t)") but never states whether the baselines receive goal information. If the baselines operate without goal conditioning, the comparison is structurally unfair. Similarly, DEIR is described only as "a recent exploration baseline" with no specification of which base RL algorithm it is combined with or how it was adapted for goal-conditioned tasks, making the DEIR results difficult to interpret.

- **Table 1 only compares G2FN to PPO, omitting SAC and DEIR.** The goal-position-robustness experiment (Table 1) compares only against PPO. Including SAC and DEIR would strengthen the claim that G2FN's robustness to goal shifts is unique rather than shared by any off-policy or exploration-augmented method.

- **Limited statistical reporting.** Only Table 2 explicitly reports standard deviations over 3 seeds. Figure 3 (sample efficiency curves) and Table 1 (goal position changes) do not report confidence intervals or number of seeds. Three seeds is a minimal standard; 5+ seeds would provide more reliable estimates, especially for the zero-shot generalization results where variance is high.

### Trivial
- Line 97: "benefit of GFlowNets" — small typo ("benefit").
- The method section (Section 4) is notably brief (under one page) for a paper whose primary contribution is a new method; expanding it with concrete details would substantially improve clarity.

## Nice-to-Haves
- A comparison to a maximum-entropy variant of SAC (which already maximizes policy entropy at the state level) would help isolate whether the benefit is from trajectory-level diversity (unique to G2FN) or could be achieved with state-level entropy maximization.
- The claim that GFlowNets "implicitly capture epistemic uncertainty" (Introduction) is intriguing but never elaborated or tested. A brief discussion or simple diagnostic would strengthen the paper's framing.
- A limitations paragraph discussing failure cases (very long horizons, continuous state spaces, non-terminal rewards) would improve completeness.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *"The use of a perfect environment model for rollouts is unrealistic and not a fair comparison. If baselines were also given the ability to simulate in the perfect model, they might similarly improve"* — **REMOVED.** The paper explicitly states (line 141) that all methods receive an equal number of simulated rollouts in the perfect model ("rollout an equal number of samples... with each of the proposed methods"). The comparison is symmetric; this criticism is factually incorrect.
- *"Figures 3, 5, 6 are referenced but the descriptions... are absent"* and *"Tables are embedded as image placeholders"* — **REMOVED.** These are PDF parsing artifacts; the original submission has actual figures and tables.
- *"No standard deviations for Figure 3"* — **REMOVED as unsupported.** Figures are image placeholders in the extracted text; the actual figure likely includes error bars/shading. The paper does report standard deviations for Table 2.
- *"The paper does not discuss potential failure cases"* — **REMOVED as minor/scope-creep.** Listing all failure modes is not standard for a paper of this length; this is a nice-to-have, not a weakness.
- *"Missing related works"* — **REMOVED per instructions** (cannot verify existence of missing references).
- *"Reproducibility concerns about large artifacts"* — **REMOVED.** The core reproducibility concern (architecture, hyperparameters) is retained as a Major weakness. Nitpicks about trivial details are removed.
- *"Harsh critic's section-by-section notes about 'Introduction unsupported claims about epistemic uncertainty'"* — **WEAKENED and moved to Nice-to-Haves** since it is a minor, non-central point.

## Novel Insights

None beyond the paper's own contributions. The reviews surface useful weaknesses but do not identify unexpected connections or implications that the paper itself does not articulate.

## Suggestions

1. **Add HER and GCSL baselines.** These are the standard comparators for goal-conditioned RL. Without them, the reader cannot attribute gains to trajectory-level diversity versus basic off-policy goal conditioning.
2. **Ablate the uniform backward policy.** Compare G2FN with a learned P_B and with a fixed non-uniform P_B to isolate whether the uniform P_B is responsible for the diversity benefits claimed.
3. **Provide full implementation details:** architecture (layer sizes, whether separate heads), hyperparameters (learning rate, batch size, λ), and training procedure in a table or appendix.
4. **Report trajectory diversity metrics** (number of unique successful trajectories, trajectory entropy) on at least one non-trivial environment (e.g., Empty-8×8 or LavaGap) to directly connect the claimed mechanism to the observed outcomes.
5. **Specify baseline configurations clearly.** State whether PPO/SAC receive goal-augmented states, and describe how DEIR was adapted (base algorithm, hyperparameters).
6. **Increase the number of seeds** to at least 5 for all experiments, and report standard deviations or confidence intervals for the sample efficiency curves (Fig. 3) and goal-position-robustness experiment (Table 1).
