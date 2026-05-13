# Adaptive $Q$-Network: On-the-fly Target Selection for Deep Reinforcement Learning

- Decision: Accept
- Scores: 8, 6, 6

## Abstract
Deep Reinforcement Learning~(RL) is well known for being highly sensitive to hyperparameters, requiring practitioners substantial efforts to optimize them for the problem at hand. This also limits the applicability of RL in real-world scenarios. In recent years, the field of automated Reinforcement Learning~(AutoRL) has grown in popularity by trying to address this issue. However, these approaches typically hinge on additional samples to select well-performing hyperparameters, hindering sample-efficiency and practicality. Furthermore, most AutoRL methods are heavily based on already existing AutoML methods, which were originally developed neglecting the additional challenges inherent to RL due to its non-stationarities. In this work, we propose a new approach for AutoRL, called Adaptive $Q$-Network~(AdaQN), that is tailored to RL to take into account the non-stationarity of the optimization procedure without requiring additional samples. AdaQN learns several $Q$-functions, each one trained with different hyperparameters, which are updated online using the $Q$-function with the smallest approximation error as a shared target. Our selection scheme simultaneously handles different hyperparameters while coping with the non-stationarity induced by the RL optimization procedure and being orthogonal to any critic-based RL algorithm. We demonstrate that AdaQN is theoretically sound and empirically validate it in MuJoCo control problems and Atari $2600$ games, showing benefits in sample-efficiency, overall performance, robustness to stochasticity and training stability.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors have developed a new AutoRL approach called Adaptive Q-Network (AdaQN), which aims to address the non-stationary optimization procedure in RL without requiring additional samples. The algorithm learns multiple Q-functions with different hyper-parameters while using the smallest approximation error as a shared target. So there's no need for additional samples. The paper also provides theoretical motivation that supports the algorithm and through experiments on Mujoco and Atari, AdaQN is shown to have better performance and sample efficiency.

### Strengths
1. Simple but novel and effective design of training multiple Q functions with different hyper-parameters settings and target selection mechanism which means no additional samples are required for hyper-parameter tuning. 
2. AdaQN is shown to performance better in Mujoco and Atari benchmarks than DQN and other autoRL baselines
3. Theoretical support is also presented to support the motivation of the selection mechanism in AdaQN.
4. AdaQN can be applied to other critic-based algorithms

### Weaknesses
From my understanding, AdaQN's performance is still dependent on the initial range of hyper-parameters considered in the multiple Q setup. If this range is not representative of the optimal settings, AdaQN may not achieve the best possible performance. Specifically, if the hyperparameter space is not sufficiently dense around the true optimal values, the algorithm may converge to a suboptimal solution. Also, it seems error or bias in the calculation of approximation error will affect the selection of the shared target. The method relies on the minimum of the cumulated losses as a proxy for the approximation error, but this might be a noisy estimate, especially in the early stages of training or with limited data. This could lead to the selection of a suboptimal target network, hindering the overall learning process.

### Questions
Can AdaQN effectively be applied on continuous action spaces (actor-critic frameworks) especially in complex high-dim environments? Which Q should be use to derive a policy network (maybe similar as we choose the one for target calculation)?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work proposes a new AutoRL algorithms that constructs an ensemble of Q-networks, each learned with different hyperaparameters (e.g., different learning rates). The main novelty is that during learning, there is an interaction between the different Q-networks; namely, the best performing Q-network is used for the target computation for all networks. This means that the individual performances of the networks will be different, potentially better than the performance obtained by just learning by scratch with a chosen hyperparameter. Moreover, the best performing hyperparameters may also change as learning progresses, highlighting an attractive property of the proposal. Action selection is also performed by picking the best performing Q-network from the previous transition, together with an $\epsilon$ random selection of a Q-network from the ensemble. Experiments are performed on DQN lunar lander as well as SAC on MuJoCo tasks. They compare against other AutoRL algorithms like SEARL and DEHB, and obtain superior performance. The work also includes ablation studies on the components of the algorithm, e.g., the epsilon parameter, and the Q-network selection mechanism. Moreover, they provide other evidence, such as directly plotting which networks were selected. The final performances on the tasks seem reasonable, and the learning speed including hyperparameter selection is good compared to the baselines.

### Strengths
- The main idea is clear, theoretically justified and seems like a good idea.
- The performance improves significantly.
- The experiments are thorough, and look at several metrics, include ablations, etc.
- The exposition is good.

### Weaknesses
 - The evaluation protocol was only briefly discussed, and was not completely clear to me. Particularly, how the baselines results are plotted could have been explained more prominently. I believe these plots include the hyperparameter selection cost on x-axis, but this could be clearer. Moreover, for reference, it would be good to know what the performance would be when running from scratch with the best performing hyperparameters.

In particular, what does this mean:
> Additionally, we focus on sample efficiency; thus, for reporting the grid search results, we multiply the number of interactions of the best achieved performance by the number of individual trials, as advocated by Franke et al. (2021). We also report the average performance over the individual runs as the performance that a random search would obtain in expectation.

This bit seems very important for interpreting the results, but it's only briefly mentioned. I would suggest explaining this with equation notation to make it precise. Moreover, perhaps it would be useful to explain the hyperparameter tuning task setting, what the objective and metrics are in the background. Moreover, the axis labels such as "Env steps" can be confusing, because the same notation is used in standard RL where one just runs the best performing hyperparameters without considering cost of searching the hyperparameters. These points would be good to clarify.

- Around the end of the paper, there was a part about also selecting the $\gamma$ discount parameter, but this seemed unsound to me. The discount parameter affects the Q-function, so different Q-functions would necessarily require different targets, and I don’t think they could be shared. For example setting $\gamma=0$ would probably give good small prediction errors, but would not actually perform well.

### Questions
Can you give more explanation on the evaluation protocol?

What is the performance when running the optimal hyperparameters from the start?

Can you clarify the parts that I listed in the weaknesses, including the discussion on the discount factor?

### Soundness
3

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
3

### Summary
This paper addresses the sensitivity of hyperparameters in deep Reinforcement Learning (RL) and proposes a method to speed up hyperparameter selection compared to previous AutoRL approaches. The authors introduce the Adaptive Q-Network (AdaQN), which learns several Q-functions, each trained with different hyperparameters. These Q-functions are updated online using the one with the smallest approximation error as a shared target. Comprehensive experiments on MuJoCo and Atari environments demonstrate the effectiveness of AdaQN.

### Strengths
This paper addresses the crucial issue of hyperparameter selection in deep RL and provides an effective solution. The proposed method is well written and organized. Comprehensive experiments validate the effectiveness of the method.

### Weaknesses
Theorem 4.1 explains why the empirical Bellman operator in Eq (3) derived from experience replay is unbiased to the true Bellman operator in Eq (2). However, it lacks a theoretical analysis on why the selection scheme from Eq (2) leads to convergence rather than local minima. A formal theoretical analysis would strengthen the paper by explaining the convergence properties of the proposed method. Specifically, the paper does not address whether the dynamic selection of Q-functions based on minimal approximation error guarantees convergence to the optimal policy or if it might converge to a suboptimal solution due to the non-convex nature of the problem. It is also unclear how the frequency of switching between Q-functions affects the overall learning process and whether there are specific conditions under which the proposed method is guaranteed to converge to a global optimum rather than being trapped in a local minimum.

### Questions
Given the motivation to "speed up hyperparameters selection," how can the selected hyperparameters by AdaQN be used effectively? Can the selected hyperparameters by AdaQN be used to train a better DQN? It seems the improvements by AdaQN are due to the use of different Q-functions, similar to ensemble methods, with the difference being the use of various hyperparameters instead of just different initializations. Could the paper be motivated by performance improvement using different hyperparameters rather than speeding up hyperparameter selection?

### Soundness
3

### Presentation
3

### Contribution
3
