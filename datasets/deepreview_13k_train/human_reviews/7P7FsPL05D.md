# DuRND: Rewarding from Novelty to Contribution for Reinforcement Learning via Dual Random Networks Distillation

- Decision: Reject
- Scores: 5, 6, 3, 3

## Abstract
Existing reward shaping techniques for sparse-reward tasks in reinforcement learning generally fall into two categories: novelty-based exploration bonuses and value-based rewards. The former encourages agents to explore less visited areas but can divert them from their main objectives, while the latter promotes stable late-stage convergence but often lacks sufficient early exploration. To combine the benefits of both, we propose Dual Random Networks Distillation (DuRND), a novel framework integrating two lightweight random network modules. These modules jointly generate two rewards: a novelty reward to drive exploration and a contribution reward to evaluate progress toward desired behaviors, achieving an efficient balance between exploration and exploitation. With low computational overhead, DuRND excels in high-dimensional environments like Atari, VizDoom, and MiniWorld, outperforming several benchmarks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents an approach to better balance novelty-based exploration and exploitation (performance on the primary task). It introduces Dual Random Network Distillation (or DuRND), an extension of the novelty-based bonus from RND that combines two bonuses based on novelty and contribution to success. Unlike RND,  DuRND aims to focus later exploration behavior on novel states that led to successful trajectories or milestones. Experiments across Atari, Vizdoom, and MiniWorld show that the implementation of DuRND outperforms some novelty-seeking and reward-shaping approaches. Further ablations show that both bonuses are helpful over each bonus considered individually.

### Strengths
S1. The paper explains the DuRND clearly. Algorithms and figures clearly illustrate the steps of the proposed approach. The paper also considers ablations to justify combining two bonuses in their setup.

S2. The authors also explicitly discuss the limitations of their approach, which is a big positive.

S3. The proposed approach can be combined with many popular RL algorithms, such as PPO and SAC.

### Weaknesses
W1. The dependence on using a success criterion for trajectories (or sub-trajectories) for training the predictor networks makes the applicability of this idea beyond goal-reaching tasks difficult. Even with sub-trajectories, the approach relies on strong assumptions of what success/failure means, i.e., if a reward or manually defined milestone is received within $T_{max}$ steps. Both the milestone and $T_{max}$ would require knowledge about the environment. The definition of success as receiving a reward within a fixed number of steps ($T_{max}$) is problematic because it conflates the notion of success with a time-bound constraint. This approach might not generalize well to environments where success is not directly tied to immediate rewards or where the time scale for achieving a goal is highly variable. Furthermore, the reliance on manually defined milestones introduces a significant engineering overhead and limits the method's autonomy. The method's effectiveness is thus highly dependent on the quality of these manually defined milestones, which may not be straightforward to identify in complex environments.

W2. The approach relies on knowledge about the training time to decay the intrinsic reward coefficients. This specific form of decay assumes additional prior knowledge about interactions needed for training, which is an important limitation. It would be interesting to understand how DuRND performs with choices of fixed coefficients, especially since the other considered baselines used fixed values for similar hyperparameters. The decay of intrinsic reward coefficients based on training time introduces a dependency on the total number of training steps, which is a form of prior knowledge about the environment. This approach assumes that the agent's learning progress is directly correlated with the number of training steps, which may not be true in all cases. A fixed coefficient would provide a more consistent baseline for comparison, and it would be valuable to see how the performance of DuRND is affected by this choice. The current approach of decaying the coefficients makes it difficult to isolate the effect of the proposed exploration bonus from the effect of the decaying coefficients.

W3. Some information about baselines seems missing and should be provided in the paper. In Lines 407-408, the authors say, “To keep the comparison fair between off-policy and on-policy methods ..” does this mean that PPO was not the base agent for all considered agents (ExploRS, RND, #Explo, ReLara, ROSA, etc.)? Other details about how baselines were tuned would also be important to know. Was the intrinsic reward coefficient (like $\lambda$ in the proposed approach) for other baselines set to a constant value of 1, or was it held constant at some other value? It might be the case that the agents with only novelty-based bonuses would also naturally focus on the main task (as the novelty wears off) if intrinsic rewards were on a suitably low scale compared to the main task’s reward. The lack of a consistent base agent across all baselines makes it difficult to isolate the effects of the proposed exploration strategy. The performance differences could be attributed to the choice of the base RL algorithm rather than the exploration method itself. It is also unclear how the intrinsic reward coefficients for the baselines were set, which makes it difficult to compare the results fairly. Without this information, it is hard to determine if the performance gains are due to the proposed method or simply due to a more favorable hyperparameter setting.

### Questions
- Wouldn’t it be more natural to use the minimum of $e_s(s)$ and $e_f(s)$ as the novelty intrinsic reward? In the current formulation which uses a sum, the novelty bonus can be high even if one network has seen the state $s$ a large number of times. Were any experiments conducted with alternative formulations of bonuses?

- Do the authors have results for vanilla PPO on the considered environments?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
Random network distillation is an unsupervised technique designed to enhance the exploratory behavior of an agent by fitting a predictor network to the latent outputs of a randomly initialized but fixed target network. The deviation between target and predictor, commonly measured by the mean squared error, is typically higher in underexplored areas of the search space, translating into a higher auxiliary "reward" signal that encourages exploration. The paper "DuRND: Rewarding from Novelty to Contribution for Reinforcement Learning via Dual Random Networks Distillation" proposes an extension to classical RND by introducing two distinct random network modules—one for states deemed "successful" and another for states associated with "failure." This innovation allows for the derivation of both a "novelty" and a "contribution" reward signal, striking a balance between exploratory and exploitative behavior. The proposed method is evaluated on three benchmark environments: Atari, VizDoom, and MiniWorld.

### Strengths
•	The paper is well-written, structured, and easy to follow.

•	The exploration vs. exploitation dilemma remains a core issue in reinforcement learning.

•	The general approach is elegantly simple and lightweight, meaning it can be easily integrated into any online reinforcement learning algorithm without significant overhead.

•	The authors provide a thorough experimental evaluation, reporting results from over 10 different training runs across 10 distinct environments, and comparing DuRND to six baseline methods.

•	The extensive evaluation demonstrates the utility of both the "novelty" and "contribution" reward signals in isolation, and shows their synergy when used together.

### Weaknesses
•	Despite the extensive evaluation in the experiments section, I have a significant concern, which the authors have acknowledged but deferred to future work: the weighting of the shaped reward signals. The paper aims to improve handling of the exploration-exploitation dilemma, and while it achieves this, the shaped rewards rely on additional hyperparameters—λ and ω—which are linearly adjusted in the current implementation. I believe this aspect warrants more in-depth discussion and empirical analysis within the paper itself. Specifically, the paper lacks a sensitivity analysis of how different values of λ and ω affect the agent's exploration behavior. For instance, how does increasing λ impact the agent's tendency to explore novel states versus exploiting known successful trajectories? Similarly, how does varying ω influence the agent's focus on states that contribute to positive rewards? Without this analysis, it is difficult to understand the practical implications of these hyperparameters.

•	In addition, the method relies on success and failure labels to update the respective network modules, but in ambiguous or multi-objective tasks, defining success and failure may not be straightforward. This is particularly concerning in environments where rewards are sparse or delayed, making it challenging to determine if a state is truly contributing to success or is merely a step in a long sequence of actions. For example, in a complex navigation task with multiple sub-goals, a state might appear to be a failure if only considering the immediate reward, but it could be crucial for reaching a later sub-goal. The paper does not address how the method would handle such situations, which could lead to suboptimal learning.

•	While the additional novelty introduced by DuRND is incremental compared to classical RND, I still believe the contribution is valuable and fills a gap in the current literature.

### Questions
•	How should the λ and ω hyperparameters be set in general, and more critically, how can they be set in the absence of prior knowledge about the scaling of the environmental reward (r_env)?

•	The linear scaling approach requires an end point; how should this be determined without resorting to expensive and time-consuming experimental tuning?

•	How robust is the performance of DuRND if the weight scheduler is suboptimal? This question is critical, as real-world applications often cannot afford perfect tuning of hyperparameters, and the performance may degrade substantially if these are not set optimally.

Given the importance of these issues, I feel they should not be relegated to the future work section. Instead, this discussion should be incorporated into the main body of the paper, potentially reducing sections 4.3 and 5.2 to make space for this analysis.

--
Post-rebuttal: After reading all reviews and rebuttals, it is evident that there is a significant overlap in the issues found. While I appreciate the clarifications provided in the rebuttal, the most critical aspect -- a more detailed analysis of λ and ω, including their scaling with respect to environmental rewards, the endpoint of linear scaling, and suboptimal weight scheduling -- remains largely unaddressed. Therefore, I will maintain my current score.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes a novel algorithm DuRND, a refined version of RND (Random Network Distillation), by categorizing the states into successful states and failed states. This allows the agent to obtain a more refined intrinsic reward structure.

### Strengths
1. The method is easy to understand. 
2. Presumably easy to implement from an existing RND implementation.
3*. The results seem to be strong, but I have a number of concerns, which I will elaborate on in the weaknesses section.

### Weaknesses
The idea of splitting the successful and failed states is interesting, but not convincing. My understanding is that the authors try to prevent the exploration algorithms to over-explore by re-weighting the reward based on the success/failure prior, so that the agent would be more exploratory towards successful states, and less towards failed states. However, this can be simply done by computing the intrinsic reward conditional on value [1], which is a more general indicator of the quality of current state.

The proposed algorithm integrates the intuition mentioned above, but significantly increases the complexity of the algorithm compared to RND, araising some of my concerns discussed below.

Despite the results seem strong, there are several concerns raise in terms of the experiment:
1. PPO is missing in the comparison, which is very crucial for experiment of any PPO-based algorithms.

2. The proposed algorithm DuRND introduces two new hyperparameters $\omega$ and $\lambda$ into the formulation, which does not exist in RND. In the original RND experiment, the coefficient of the intrinsic reward is effectively fixed to 0.5 given by $2A_{env} + A_{rnd}$. However, the authors mentioned they gradually decrease $\lambda$ from 1 to 0 and increase $\omega$ from 0 to 1, which drastically different from the choice of RND. I will elaborate on this point:
* RL algorithms are \textbf{VERY} sensitive to the choice of the coefficient like $\omega$ and $\lambda$ in this paper. Hence it is very concerning whether the performance improvement mostly coming from the choice of the hyperparameter. The fact that RL algorithm would prefer a decreasing novelty reward coefficient as the training proceeds, so that the algorithm can start to emphasize exploitation sooner, hence achieves better sample efficiency. I would potentially lift my rating if the authors can show that DuRND can still out-perform other baseline algorithms with same schedule of coefficients.
* Similar to the previous point, it is also crucial to control the speed of the converge rate of the intrinsic reward model, i.e. the learning rate of $f(\dot ; \theta)$. This is not mentioned in the paper.

3. The proposed algorithm DuRND requires a way to determining whether a trajectory is successful or failed. The authors mention that they use the $\sum_{step=1}^{T_{max}} r \geq 1$ condition, to determine whether a sub-trajectory rollout in the current iteration is successful or not. This introduces two problems:
* $T_{max}$ is still a hyperparameter, the value of which is not provided in the paper.
* Intuitively, the suitable choice of such hyperparameter would correlate to the periodicity of the environment. Consider a episodic setting, if the task is a navigation task, like TMaze and ThreeRooms, such $T_{max}$ should be equal to the horizon $H=500$, whereas in the environment like Solaris, the $T_{max}$ should presumably be smaller, otherwise many bad states would be considered as successful state. Hence it would be very difficult to tune when the periodicity of the environment is very hard to know, for example, legged robotics tasks.

Overall, I am not convinced that the improvement of the performance solely coming from the characterization of the successful/failed states, during the design process, the authors introduced three hyperparameters that may not be chosen in a systematic or unified way across all types of environment.

### Questions
1. What is the performance of PPO in this set of environment?
2. What is the performance of algorithms in the set of environment with original reward structure?
3. What is the choice of hyperparameters $\lambda$, the coefficient of intrinsic reward of baseline algorithms?
4. What is the performance of RND, as well as other baseline algorithms, when you also decrease their coefficient $\lambda$ from 1 to 0 linearly?
5. What is the choice of $T_{max}$ used in different environment? How do you choose the $T_{max}$?

### Soundness
1

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper's method is established on the observation that novelty-based reward can divert agents from their main objects and value-based reward lacks sufficient early exploration. The authors then propose a framework (DuRND) integrating 2 groups of lightweight random network pairs that jointly generate novelty and contribution rewards. To balance exploitation and exploration during training, DuRND scales the coefficients for the novelty and contribution rewards throughout the learning process. Finally, the authors integrated DuRND into PPO.

I think the problem this paper tries to solve is important, but some clarifications are needed to help me gauge the contribution of this work.

### Strengths
- Learning in sparse reward tasks is a long-standing problem in RL, the paper is taking on an important challenge.
- The paper's idea is simple and clearly presented.

### Weaknesses
 - It is unclear how challenging the evaluated tasks are. Unlike Montezuma's Revenge, a notoriously hard to solve problem, it is unclear how challenging the tasks in which DuRND is evaluated and thus it is hard to gauge the contribution. For example, the [highest score achieved in Freeway is 34](https://github.com/cshenton/atari-leaderboard) while the best algo in Figure 6 achieves 25.
- Somewhat contradictory findings. While in the abstract and the introduction, the authors say that *"The former [novelty-based reward] encourages agents to explore less visited areas but can divert them from their main objectives, while the latter [value-based reward] promotes stable late-stage convergence but often lacks sufficient early exploration."*, Figure 6 shows that novelty reward can actually achieve descent scores (e.g., Freeway, Frogger and TMaze). This questions the paper's assumption.


### Questions
1. Can the authors provide scores from other model-free RL algos on the tasks? Like PPO? This would also allow a reader to compare the vanilla PPO with DuRND, which is a modified version of PPO in this paper.
2. Is the 2nd point in the Weaknesses section reasonable to the authors?
3. When the reward is sparse, there are few success trajectories. Does it cause a problem for learning the Success RN module? How did you overcome this problem? 
4. Is $T_{max}$ for each task tuned? I don't see it in table 4. If so, did you also tune the HPs for the baselines? 
5. I find the toy task to be comprehensive and a good tool to understand DuRND, how are the states represented? One-hot encoding? Can the authors provide code (it's not in the current supplementary material)? Both training and the learned model would be appreciated.

### Soundness
2

### Presentation
3

### Contribution
2
