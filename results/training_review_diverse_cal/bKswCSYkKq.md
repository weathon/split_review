Now I have all the information needed. Let me construct the final review.

## Summary

This paper introduces NBSP (Neuron-level Balance between Stability and Plasticity), a method for addressing the stability-plasticity dilemma in deep reinforcement learning. The core idea is to (1) identify "RL skill neurons" via a goal-oriented method that scores neurons by how well their activation patterns correlate (positively or negatively) with task success, and (2) freeze those neurons via gradient masking while allowing other neurons to adapt to a new task, supplemented by experience replay. Experiments on Meta-World and Atari benchmarks show NBSP achieving near-1.0 success rates on both old and new tasks, outperforming EWC, ANCL, and an importance-based variant.

## Strengths

1. **Novel neuron-level approach to the stability-plasticity problem in DRL.** The paper operationalizes "skill neurons" specifically for DRL via a goal-oriented identification method (Eq. 1–4) that measures correlation between neuron activation and task success, including both positively and negatively correlated neurons. This is the first work to address *both* stability and plasticity simultaneously at the neuron level in DRL — Sokar et al. (2023) addresses plasticity loss only (dormant neuron recycling) and does not target knowledge retention/stability.

2. **Strong empirical results on multiple benchmarks.** On all four Meta-World task pairs, NBSP achieves success rates near 1.0 on both the first and second tasks after sequential learning (Figure 4), while EWC, ANCL, and Importance-based NBSP each fail on at least one task pair. The pattern holds on Atari (Figure 7), demonstrating generalization across both continuous and discrete action spaces.

3. **Ablation studies properly isolate the contribution of gradient masking.** The comparison Base → Replay-Only → NBSP (Figure 5) shows that NBSP (replay + masking) substantially outperforms Replay-Only on both knowledge retention and second-task learning. Since NBSP and Replay-Only share the replay component, the difference directly isolates the value added by gradient masking. This undercuts the harsh critic's claim that masking's contribution is unisolated.

4. **Insightful finding about the critic's critical role.** By applying NBSP to actor-only vs. critic-only (Figure 6), the paper shows that NBSP-Critic retains prior knowledge better than NBSP-Actor, and only full NBSP achieves optimal balance. The explanation — that the critic's recursive update and target network mechanisms make it the bottleneck for stability-plasticity — is well-reasoned and provides actionable insight for future work.

5. **Parameter-free and simple to integrate.** The method adds no extra parameters or complex modules; it only requires computing a neuron score after the first task and applying a binary mask during second-task training — a practical advantage over modularity-based approaches like ANCL.

## Weaknesses

### Fatal
None.

### Major

1. **Missing comparisons against DRL-specific continual learning baselines.** The paper compares against EWC (regularization-based, from supervised continual learning) and ANCL (modularity-based, from supervised continual learning). Neither is designed for DRL specifically. Missing are comparisons against DRL methods that address forgetting or plasticity degradation — e.g., CLEAR (Rolnick et al., 2019), Progress & Compress (Schwarz et al., 2018), or the dormant neuron recycling approach of Sokar et al. (2023) (which is cited but not used as a baseline). While Sokar et al. focuses on plasticity rather than both stability and plasticity, a comparison would clarify what NBSP adds beyond existing DRL-specific techniques. This gap weakens the claim that NBSP "significantly outperforms existing approaches," since the "existing approaches" tested are not from the DRL continual learning literature.

2. **The neuron identification method's validation is incomplete.** The comparison against Importance-based NBSP (Paik et al., 2019) shows that the goal-oriented method outperforms an importance-based alternative — this is helpful but insufficient. The paper does not show:
   - Whether freezing the identified neurons preserves first-task performance more than freezing randomly selected subsets of the same size (a more direct causality test).
   - Whether the identified neurons are consistent across multiple training runs.
   - How many neurons are identified per layer/network (the paper states "the number varies depending on the complexity of the task" but gives no concrete numbers).
   
   These gaps leave the core identification step less rigorously validated than it should be for a method whose novelty rests on it.

### Minor

1. **Limited to SAC.** The method is evaluated only on Soft Actor-Critic. Generalization to other common DRL algorithms (PPO, DQN, TD3) is not demonstrated. Since the gradient masking mechanism is algorithm-agnostic, this is a scope limitation rather than a structural flaw, but it should be noted.

2. **Key hyperparameters are unanalyzed.** The replay interval *k* (Eq. 6) and the size of the prior-task replay buffer are not analyzed or reported. These likely affect the stability-plasticity tradeoff and should at minimum be stated, with some sensitivity analysis.

3. **No computational overhead characterization.** The neuron identification step requires running inference on a batch of prior-task data. The paper should report the additional computation time this introduces, even if it is small.

4. **No pseudocode or algorithm box.** While the method is described textually, a concise algorithm summary would aid reproducibility and clarity.

### Trivial
None that survive filtering.

## Nice-to-Haves
- A "Masking-Only" (no replay) condition in the ablation would further clarify whether masking alone provides any benefit, though the existing ablation already shows masking adds value on top of replay.
- A comparison against standard neuron attribution methods (e.g., integrated gradients, activation maximization) for identifying task-relevant neurons would strengthen the case for the proposed goal-oriented score.
- Statistical significance tests (beyond error bars) would strengthen the claims of superiority over baselines.

## Removed Points
- **"Gradient masking contribution is never isolated"** (Harsh Critic point 2): Removed because it is factually incorrect. The ablation (Figure 5) compares NBSP (masking + replay) against Replay-Only, where the only difference is masking. This *does* isolate masking's contribution. The critic's demand for a "Masking-Only" condition addresses a different question (whether replay adds value on top of masking) and is not required to validate the paper's claims.
- **"Arbitrary thresholding"** (Harsh Critic point 1a): Removed because using the mean as a threshold for binarizing neuron activations is standard practice in the neuron analysis literature (Bau et al., 2020; Wang et al., 2022). The criticism is generic and does not identify a concrete flaw unique to this paper.
- **"Anti-correlated neurons treated identically is a weakness"** (Harsh Critic point 1b): Removed because the paper explicitly addresses this design choice: "it overlooks neurons that exhibit a negative correlation with the goal but still carry valuable task-related knowledge." The decision to include anti-correlated neurons is a reasonable conservative choice, not an oversight.
- **"First work claim conflicts with Sokar et al."** (Harsh Critic "Other Observations"): Removed because the paper's claim is "first work that addresses both stability and plasticity loss simultaneously in DRL at the level of neurons." Sokar et al. (2023) addresses *plasticity loss only* (dormant neuron recycling), not knowledge retention/stability. The claim is accurate with the qualifiers.
- **"Baselines are likely undertuned"** (Harsh Critic point 3): Removed because this is speculation unsupported by evidence. The paper states all methods use identical network architecture and are evaluated on the same task pairs.

## Novel Insights
The paper's core novel insight — that stability and plasticity in DRL can be balanced at the neuron level by identifying goal-correlated neurons and freezing them — is well-supported by the experiments. A genuinely novel secondary finding, not fully anticipated by prior work, is that the *critic* network is the bottleneck for stability-plasticity balance in actor-critic architectures (Figure 6 and accompanying analysis in Section 4.3). This is explained by the recursive update and target network mechanisms of the critic, which the authors connect to insights from Ma et al. (2024). This finding has practical implications beyond the paper's own method: it suggests that future DRL continual learning approaches should prioritize protecting the critic's knowledge.

## Suggestions
1. Add comparisons against at least one DRL-specific continual learning method (e.g., CLEAR, Progress & Compress, or a variant of experience replay tuned for DRL) to substantiate the claim of superiority over existing approaches.
2. Add a causal validation experiment: freeze randomly selected neuron subsets of the same size as the identified RL skill neurons and compare first-task retention. Report overlap/consistency of identified neurons across seeds.
3. Report the number/fraction of neurons identified as RL skill neurons per layer and per task, and provide at least a heuristic for how the threshold is set.
4. Report the replay interval *k* and prior-task buffer size used in experiments. Add a brief sensitivity analysis if practical.
5. Include a pseudocode or algorithm listing for NBSP integration into SAC.
6. Explicitly clarify the novelty differentiation from Sokar et al. (2023) — i.e., that Sokar et al. targets plasticity recovery only, while NBSP targets *both* stability and plasticity.

## Score and Decision

This paper makes a genuine contribution: a novel neuron-level framework for the stability-plasticity dilemma in DRL, with clean empirical results and an interesting finding about the critic's role. The core claims are supported by the evidence, and the ablations are properly designed. The main weaknesses are (1) missing DRL-specific baselines that weaken the "outperforms existing approaches" claim, and (2) incomplete validation of the neuron identification method. These are addressable and do not threaten the paper's contribution, but they prevent it from being a definitive work in its current form.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>