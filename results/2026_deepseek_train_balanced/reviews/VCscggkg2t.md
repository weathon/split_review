## Summary
Goal2FlowNets (G2FN) proposes using goal-conditioned Generative Flow Networks (GFlowNets) as policies in goal-conditioned RL. The key idea is that GFlowNets, by design, learn a diverse set of trajectories proportional to reward, which yields a "policy cover" — multiple distinct ways to reach each goal. The paper claims this improves sample efficiency, zero-shot generalization to distribution shifts, and few-shot adaptation. Experiments are conducted on MiniGrid/BabyAI gridworld environments with comparisons against PPO, SAC, and DEIR.

## Strengths
- **Timestep-augmented state representation to satisfy the GFlowNet DAG requirement in RL MDPs**: The paper identifies that GFlowNets require a DAG, which is violated by cyclic RL MDPs, and resolves this by augmenting states with the current timestep (Section 4, lines 99–101). This is a concrete technical adaptation necessary to use GFlowNets as online policies in standard RL environments, and is clearly articulated.
- **Zero-shot generalization across substantial distribution shifts with behavioral comparison**: Policies trained on Empty-5x5 and evaluated zero-shot on Empty-16x16 show that G2FN successfully navigates to goals many steps away while PPO "doesn't travel much beyond the environment length it has been trained on" (lines 139–140). The paper provides both quantitative success rates (Table 2) and trajectory visualizations (Figure 4). The shift from 5×5 to 16×16 is non-trivial.
- **Comparison against DEIR distinguishing trajectory diversity from state diversity**: The paper contrasts G2FN with DEIR (Wan et al., 2023), a recent exploration method, and notes that "although DEIR explores the state space very well, the resulting policy does not maintain diversity and also collapses" under distribution shift (line 123). This sharpens the paper's argument that trajectory-level diversity (not merely state coverage) is what matters.
- **Learning-free few-shot generalization diagnostic**: Using simulated rollouts in the ground-truth simulator, G2FN achieves near-perfect performance under hard distribution shifts (e.g., empty room → lava), while baseline methods do not improve (Table 3, line 147). This diagnostic experiment isolates whether the policy's trajectory coverage is practically useful.

## Weaknesses

### Fatal
None.

### Major
- **No quantitative diversity analysis for the central policy-cover claim**: The paper argues that GFlowNets learn a diverse "policy cover" and claims that on Empty-5x5 "a trained G2FN agent traverses all the possible paths to reach the goal" (line 143). However, the paper provides zero numerical evidence for this — no trajectory counts, no comparison of unique trajectories discovered by G2FN vs. baselines, no entropy measurements, no comparison against the combinatorially determined total number of possible paths. The supporting reference (Fig. 6 / Fig. 5(b)) shows only three example trajectories qualitatively. Since the entire method is motivated by diversity, the lack of any quantitative diversity metric is a significant gap that undermines the paper's core argument.
- **Missing critical baseline: Hindsight Experience Replay (HER)**: The paper evaluates against PPO, SAC, and DEIR, but omits HER (Andrychowicz et al., 2017), the standard baseline for sparse-reward goal-conditioned RL. Without HER, the paper cannot demonstrate that the benefit comes from GFlowNets' diversity properties rather than simply from being a more sample-efficient off-policy method. This is especially important given that SAC (the main off-policy baseline included) is not designed for goal-conditioned sparse-reward settings.
- **No GFlowNet ablations**: The paper makes several design choices (SubTB(λ) objective, conditioning P_F/P_B/F on goals and timesteps, timestep augmentation, uniform vs. learned P_B) but never ablates any of them. For instance, the paper states that "by using the right P_B we can induce maximum entropy over successful trajectories" and suggests using a uniform P_B (line 97), but never clarifies whether the experiments actually use uniform P_B or a learned one. Without ablations, the contribution of individual components is unknown.

### Minor
- **Novelty overclaiming inconsistent with cited prior work**: The paper claims "As far as we know, we are the first to use GFlowNets as policies in a typical RL setting, and one more complex than gridworlds" (lines 30–31), yet also cites Pan et al. (2023; 2022) who "used GFlowNets to train reinforcement learning agents in a sparse-reward setting" (line 95). The paper does not explain how its use differs from Pan et al., creating an unresolved contradiction. Furthermore, all experiments are conducted on MiniGrid/BabyAI environments, which are gridworlds — contradicting the "more complex than gridworlds" assertion.
- **Missing implementation details critical for reproducibility**: The paper does not specify network architectures (layers, hidden sizes, activation functions), observation encoding for MiniGrid's partial egocentric views, hyperparameters (learning rate, batch size, replay buffer size if used), or how training trajectories are collected (on-policy from P_F vs. from a replay buffer). These omissions make it difficult to reproduce or assess the method.
- **No inline numerical results**: All quantitative results (Tables 1–3, Figure 3) are presented only as images with no numerical values reported in the accessible text. The text provides only qualitative descriptions ("G2FN performs better than PPO," "nearly perfect"). For a paper making strong comparative claims, inline numbers would allow the reader to assess effect sizes directly.
- **Conclusion makes unsupported causal claim**: The conclusion states "We have shown that a lack of diversity in the learned goal-conditioned policies is a major cause of these failures" (line 161), but the paper never compares G2FN against a non-diverse variant of itself to isolate diversity as the causal mechanism.

### Trivial
- **Numerical inconsistency about rollout count**: The method description says K=100 rollouts (line 141) but Table 3 says "10 simulated rollouts."

## Nice-to-Haves
- A causal analysis comparing G2FN against a non-diverse GFlowNet variant (e.g., using trajectory balance or a different P_B) to directly test whether diversity is the mechanism behind the observed improvements.
- Analysis of failure cases: the paper mentions G2FN "is often still imperfect in some of the harder cases of distribution shift" (line 141) but never analyzes when or why it fails.
- Reporting wall-clock time or sample throughput to help assess the practical cost of learning three networks (P_F, P_B, F) vs. one policy network.

## Removed Points
These points were flagged during review merging and are reported for transparency:
- *"The experimental evaluation is fundamentally insufficient and makes claims entirely unverifiable"* — REMOVED (overstated). The paper does present results in tables (as images); inability to read images is a text-extraction limitation. However, the lack of inline numbers is retained as a Minor weakness.
- *"The few-shot experiment gives G2FN access to a perfect simulator that baselines don't benefit from"* — REMOVED (factually incorrect). The paper explicitly states "rollout an equal number of samples (such as K=100) with each of the proposed methods" (line 141).
- *Strength: "Empirical verification of a full policy cover on Empty-5x5 providing direct quantitative evidence"* — REMOVED. The paper claims "all possible paths" but provides no numerical evidence (trajectory counts, entropy values). The cited reference shows three example trajectories qualitatively only. The absence of quantitative evidence is itself a weakness, not a strength.
- *Strength: "The paper addressed an important problem"* — REMOVED (generic, not specific to this paper).

## Novel Insights
None beyond the paper's own contributions. The two reviews largely agree on the paper's strengths (timestep augmentation for DAG, interesting few-shot diagnostic) and on its weaknesses (no quantitative diversity metrics, missing HER baseline, overclaiming). No novel synthesis insight emerged beyond what the paper itself proposes.

## Suggestions
1. Add trajectory count / entropy measurements on the Empty-5x5 environment to substantiate the policy-cover claim quantitatively.
2. Include HER as a baseline across all experiments.
3. Add GFlowNet ablations: compare SubTB with uniform P_B vs. learned P_B, and compare against a trajectory-balance variant.
4. Report all key numerical results inline in the text (e.g., "G2FN achieves 87% ± 3% success vs. 42% ± 5% for PPO on Empty-8x8 zero-shot to Empty-16x16").
5. Clarify the novelty claim with respect to Pan et al. — explain explicitly how the proposed use of GFlowNets differs from that prior work.
6. Provide hyperparameters and network architecture details in a reproducibility statement.

## Score and Decision
MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>