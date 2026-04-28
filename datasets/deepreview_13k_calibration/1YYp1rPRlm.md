# Differentially Private Deep Model-Based Reinforcement Learning

- Decision: Reject
- Avg Score: 5.75
- Scores: 5, 6, 6, 6

## Abstract
We address private deep offline reinforcement learning (RL), where the goal is to train a policy on standard control tasks that is differentially private (DP) with respect to individual trajectories in the dataset. To achieve this, we introduce \textsc{PriMORL}, a model-based RL algorithm with formal differential privacy guarantees.
\textsc{PriMORL} first learns an ensemble of trajectory-level DP models of the environment from offline data.
It then optimizes a policy on the penalized private model, without any further interaction with the system or access to the dataset. 
In addition to offering strong theoretical foundations, we demonstrate empirically that \textsc{PriMORL} enables the training of private RL agents on offline continuous control tasks with deep function approximations, whereas current methods are limited to simpler tabular and linear Markov Decision Processes (MDPs). We furthermore outline the trade-offs involved in achieving privacy in this setting.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work extends model-based offline reinforcement learning, namely MORL, to its differentially private variant, namely PriMORL. The work intends to guarantee trajectory level DP, which means it treats two datasets that differ in at most one (entire) trajectory as neighboring datasets and asks the algorithm to output indistinguishably between them.

The differential privacy is achieved by model privacy, i.e. if the model is learned in a DP way, then by post processing the algorithm is also DP. This though comes with the limitation that the learning algorithm can no longer access the dataset once the model is obtained from the previous phase. To achieve DP model learning, it randomly draws a subset of trajectories and uses this batch of data to estimate a gradient. A clip is then applied to the gradient which bounds the sensitivity of the gradient. The work discusses different clipping techniques which fine tune the clipping threshold. The DP guarantee is then proved by moment accountant.

Once a model is obtained the policy is trained through pessimistic private MDP, which is by the intuition that being aware of the model uncertainty requires pessimisty. This intuition inspires the authors to run soft actor-critic on the  pessimistic variant of MDP, where the reward is reduced by the uncertainty level. This to some extent mitigates the cost of not being able to access the data once the model training is complete.

Many experiments are provided on tasks like pendulum, cartpole, and halfcheetah. The authors didn't seem to compare their algorithms with baseline methods, while there seems to be many. Though, the performance of the proposed algorithm is reasonably good on its own.

### Strengths
As a summary, this work investigates a natural setting and models the problem in a reasonable way. The work guarantees DP through model learning and post processing, which is intuitive. The performance of the algorithm seems decent.

### Weaknesses
1. Model/Techniques are not exciting.
2. No baseline comparison.
3. Limited testbeds

### Questions
N/A

### Soundness
3

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
2

### Summary
This paper studied differentially private model-based offline reinforcement learning (RL). The paper proposed a new algorithm that provide differential privacy for training ensemble models. Besides theoretical guarantees, the experiments also demonstrate the effectiveness of the proposed algorithm.

### Strengths
1. The proposed method that provides privacy guarantees for training ensemble models is novel.
2. The investigation of the problem is thorough.

### Weaknesses
1.  There exist several typos. For example, in line 274, 'it does entirely remove...' I assume it should be 'it does not entirely remove...' because increasing $N$ will degrade the model performance.
2. The major weakness is that there is a lack of a more explicit discussion on each term in the theoretical results, such as $\epsilon_p$ and $\epsilon_p^{DP}$. I would be curious about if these terms depend on privacy parameter or $N$, if so, what should be the approximate dependency.

### Questions
It seems that the number of ensembles $N$ plays a vital role in the results. This work has already reduce the dependency to $\sqrt{N}$ in the sensitivity. I am just curious is it possible to further reduce it in training ensemble models.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces PRIMORL, a differentially private (DP) model-based reinforcement learning algorithm for offline settings. PRIMORL trains policies for continuous control tasks while ensuring trajectory-level privacy by learning an ensemble of DP models from offline data. This approach protects against privacy leaks in RL, especially critical in applications where individual trajectories may contain sensitive information. PRIMORL operates in an offline, infinite-horizon setting, leveraging private models to optimize policies without further interaction with the environment. Empirically, PRIMORL demonstrates competitive performance on deep RL tasks, advancing private RL beyond simpler tabular and linear MDPs and addressing practical privacy-performance trade-offs.

### Strengths
The paper is clearly organized. The authors first introduce the trajectory-level differential privacy framework within the offline RL setting, then explain the method for training private models using a model ensemble approach, covering both implementation details and theoretical guarantees. Finally, they describe how policy optimization is achieved by incorporating uncertainty techniques, with theoretical support provided as well.

### Weaknesses
1.	It is unclear how the private-variant experiments control for \epsilon. In the theoretical guarantees section, \epsilon is presented as a theoretical bound, yet here it seems to be treated as a tunable hyperparameter, with little explanation connecting these two perspectives. Specifically, the paper does not clarify how the noise multiplier `z` directly relates to the reported \epsilon values, nor does it discuss the practical implications of choosing specific `z` values on the resulting privacy guarantees. The experimental results would benefit from a more detailed explanation of how the privacy parameter \epsilon is actually controlled in practice, and how this relates to the theoretical bounds.
2.	While the motivation for the work is compelling, the experimental design is relatively simple and basic. I would have liked to see experiments that address the unique challenges of applying DP frameworks within the RL domain, yet this paper lacks a broader experimental analysis to underscore the real-world relevance of introducing DP into RL. The current experiments do not sufficiently explore the nuances of the privacy-utility trade-off in complex RL tasks, and do not address the practical challenges of implementing DP in high-dimensional state and action spaces. The paper would benefit from a more thorough investigation into the scalability and robustness of the proposed method in more challenging RL environments.

### Questions
1.In Theorem 4.2, a general formula for \epsilon^{MA}(z, q, T, \delta) is presented, but neither the main text nor the appendix provides a complete, detailed expression of this formula. Could you include a full derivation of this formula so we can clearly understand how \epsilon^{MA} is calculated based on inputs like z, q, T, and \delta?
2.In Section 4.3.2, the paper discusses handling model uncertainty under a private setting but appears to apply existing uncertainty-handling techniques from non-private settings directly to the private setting. Could you clarify any special considerations or unique aspects of handling uncertainty in the private setting? Specifically, how might model error and uncertainty differ under a private setting, given its unique constraints? We would appreciate any further insights on this point.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this paper, the authors consider private deep offline reinforcement learning (RL), where the goal is to train a policy on standard control tasks that is differentially private (DP) with respect to individual trajectories in the dataset. To achieve this, they introduce PriMORL, a model-based RL algorithm with formal differential privacy guarantees. PriMORL first learns an ensemble of trajectory-level DP models of the environment from offline data. It then optimizes a policy on the penalized private model, without any further interaction with the system or access to the dataset. In addition to theoretical guarantees, they empirically demonstrate that PriMORL enables the training of private RL agents on offline continuous control tasks with deep function approximations.

### Strengths
1. The problem of offline RL with DP is important and well-motivated.
2. This paper proposes a practical solution to the problem.
3. The authors do experiments to support their algorithm.
4. The paper is well-written in general.

### Weaknesses
1. The main concern is about technical novelty. The definition of Trajectory-level DP is directly adapted from [1]. The first part directly applies DP-FEDAVG, while the second part is about learning from the private model with pessimism. To the best of my knowledge, [1] is based on the same idea of private model + pessimism. The DP guarantee for the private model is from previous results, and the DP guarantee for learning the policy is from standard post-processing. I do not see any technical challenge in the process. It will be better if the authors could discuss about the challenges.

2. Proposition 4.4 only provides an error bound for estimating the value function of $\hat{\pi}$, which is not standard. Is it possible to derive any results about the sub-optimality gap $V^\star-V^{\hat{\pi}}$?

3. In the experiments, the privacy protection is very weak (some $\epsilon$ being close to 100). What will happen for more practical choices of $\epsilon$? E.g. $\epsilon \approx 1$.

### Questions
Please refer to the weaknesses above.

### Soundness
3

### Presentation
3

### Contribution
2
