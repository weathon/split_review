# Preference Elicitation for Offline Reinforcement Learning

- Decision: Accept
- Scores: 6, 6, 6, 8, 8

## Abstract
Applying reinforcement learning (RL) to real-world problems is often made challenging by the inability to interact with the environment and the difficulty of designing reward functions. Offline RL addresses the first challenge by considering access to an offline dataset of environment interactions labeled by the reward function. In contrast, Preference-based RL does not assume access to the reward function and learns it from preferences, but typically requires an online interaction with the environment. We bridge the gap between these frameworks by exploring efficient methods for acquiring preference feedback in a fully offline setup. We propose Sim-OPRL, an offline preference-based reinforcement learning algorithm, which leverages a learned environment model to elicit preference feedback on simulated rollouts. Drawing on insights from both the offline RL and the preference-based RL literature, our algorithm employs a pessimistic approach for out-of-distribution data, and an optimistic approach for acquiring informative preferences about the optimal policy. We provide theoretical guarantees regarding the sample complexity of our approach, dependent on how well the offline data covers the optimal policy. Finally, we demonstrate the empirical performance of Sim-OPRL in different environments.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper studies preference-based reinforcement learning (PbRL) in offline setting, in which the agent utilizes a fixed trajectory dataset for policy learning and can query humans for preference feedback. In particular, the authors propose to sample preference queries by rolling out trajectory data using learned models of MDPs. The authors provides theoretical guarantees for the sample complexity of their proposed strategy and verify it on simple control tasks.

### Strengths
The idea of using simulated rollouts in preference queries is a natural but unexplored idea in the literature of PbRL. One strength of this paper is that, the authors show the effectiveness in terms of sample complexity both theoretically and empirically.

### Weaknesses
My concern is about the quality of learned policies. While I agree with the optimality criterion mentioned in 3.2, I think to ensure the practical value of the proposed strategy, it is important to include evaluations for offline dataset of varying optimality. This is because for high-dimensional tasks, under a fixed budget of offline trajectories, the coverage over state-action space and the optimality of the behavior policy, can be conflicting objectives. The state-action space is less covered by good behavior policies, yet this reduced coverage can raise concerns on learned transition model. See detailed question below.

### Questions
1. Based on your theoretical analysis, could you discuss how you expect the performance will change on dataset of varying optimality?
2. Could you present experiment results on other dataset for the Cheetah environment, such as medium, medium-expert and expert, to support your discussion?

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
3

### Summary
This paper uses the offline dataset to learn the environment model. They do not assume they have access to the reward in the offline data set. Such offline datasets contribute to the overall learning by providing an estimation of the transition probability. This paper provides a theoretical analysis of reinforcement learning with offline datasets to achieve preference elicitation. The experiments show their algorithms outperform other algorithms in several environments. They also conducted an ablation test to show the importance of pessimistic with respect to the transition model.

### Strengths
Strengths:
1. This paper provides a good theoretical analysis of preference elicitation with the offline datasets. It bounds the value difference between the optimal policy under the estimated transition model and the true optimal policy. Such bounds are achieved by decomposing the loss from the model estimation and the reward estimation.
2. Experiments show the proposed methods outperform other algorithms in several environments.
3. This paper conducted an ablation study to show the importance of pessimistic with respect to the transition model.

### Weaknesses
Weaknesses:

1. The experiment environments are relatively simple. The grid world is quite small. It is interesting to try to extend this to more challenging reinforcement learning benchmarks.

### Questions
N/A

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
4

### Summary
The paper presents Sim-OPRL, an offline preference-based reinforcement learning algorithm that addresses the challenge of acquiring preference feedback in a fully offline setup. It leverages a learned environment model to elicit preference feedback on simulated rollouts, balancing conservatism and exploration. The main idea is to employ a pessimistic estimation for the transition dynamics (based on the offline dataset) for the OOD issue, and use an optimistic estimation for the reward model (based on the preference elicitation data). The benefit of using simulated rollouts is to avoid wasting preference budget on trajectories with low rewards. The authors provide theoretical guarantees on sample complexity and demonstrate the empirical performance of a practical version of Sim-OPRL across various environments, showing its superiority over previous baseline methods (OPRL and PbOP).

### Strengths
- This paper focuses on the preference elicitation problem on offline RL, which attracts wide attention recently from many fields (such as RLHF for LLMs).
- This paper has theoretical results on the proposed algorithm with some high-level insights (e.g., pessimism for dynamics and optimism for reward modeling).
- This paper has practical algorithm designs and good empirical results.

### Weaknesses
 - **Complexity of Implementation:** The algorithm's reliance on learning several accurate dynamics model might be challenging in practice, especially if the model fails to capture the true dynamics. Moreover, Sim-OPRL requires the trajectory rollouts using the dynamics model and the error may accumulate, which poses higher requirements for the dynamics model. Do the authors have any idea on how to design practical algorithms with less computational overhead (e.g., estimating multiple models) and on more complex environments (e.g., when it is hard to learn an accurate dynamics model).
- **Lack of study on the dependence on quality of offline data and feedback:** The performance of Sim-OPRL may be heavily dependent on the quality and coverage of the offline dataset. For the experiments in on the tasks listed in Table 2, how are the offline datasets are collected? Are they expert datasets (so the concentrability coefficients are small)? How the feedback is generated in the experiments? How would the algorithm perform when we vary the feedback quality?
- Minor: What is ``\hat{R}_\text{inf}``? I can guess it is pessimistic reward, but ``\hat{R}_\text{inf}`` and ``\hat{T}_\text{inf}`` are not formally defined.

### Questions
- I do not quite understand “An advantage of sampling from the offline buffer, however, is that it is not sensitive to the quality of the model” in L346. What does “the model” refer to?
- Should $N_T$ in the second equation in L369 be $N_R$?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper addresses the challenge of applying RL to real-world scenarios where direct interaction with the environment is impractical or unsafe. Traditional learning methods require environment interactions, which can be risky in certain fields (like healthcare applications). The paper proposes an algorithm called Sim-OPRL, an offline PBRL learning algorithm that learns from preferences without needing online interaction. This algorithm uses a learned environment model to simulate rollouts and gather preference feedback, balancing pessimism for out-of-distribution data and optimism for acquiring informative preferences. The paper formalizes the problem of preference elicitation in offline RL, proposes a novel algorithm, and provides theoretical guarantees on its sample complexity.

The paper also demonstrates the effectiveness of Sim-OPRL through empirical validation in various environments, including a gridworld and a sepsis simulation. The results show that Sim-OPRL outperforms an existing baseline algorithm (OPRL) in terms of sample efficiency and policy performance. The paper shows that by leveraging simulated rollouts, their algorithm efficiently learns the optimal policy while minimizing the number of human queries required.

### Strengths
1. The authors provide strong theoretical guarantees on the sample complexity of their approach, ensuring that the algorithm is both efficient and reliable. Additionally, the empirical results across various environments demonstrate the practical effectiveness and scalability of Sim-OPRL, showing it outperforms existing methods in terms of sample efficiency and policy performance.
2. Sim-OPRL incorporates a pessimistic approach to handle out-of-distribution data, ensuring robustness to model uncertainty. This is particularly important in offline settings where the data may not cover the entire state-action space. Being robust to OOD data makes the algorithm far more applicable to ‘real-world’ problems/settings.
3. The paper makes a compelling case due to their incorporation of theoretical and empirical evidence. To back up their theoretical insights, they conduct extensive experiments across two different environments. This provided empirical data confirms the practical applicability and robustness of Sim-OPRL, illustrating its effectiveness in scenarios where direct environment interaction is not feasible.
4. The attached code is well-written and largely self-documenting, with a clear and logical internal structure. This design not only facilitates ease of use for other users looking to implement the Sim-OPRL algorithm but also made the process of reviewing the practical implementation and validating the experiments straightforward and efficient. This made the review process much easier.

### Weaknesses
1. The paper’s empirical section does not properly consider different baseline algorithms to compare theirs with. The only algorithm that the authors use as a baseline is OPRL. This severely limits the ability to fully assess the relative performance and advantages of Sim-OPRL. To rectify this, The authors should consider including a wider array of offline PBRL algorithms/frameworks in their experiments. Specifically, the authors should consider including baselines that explore different preference elicitation strategies, such as those that use active learning techniques to select the most informative queries, or those that incorporate uncertainty estimates in their preference sampling process. This would help to better contextualize the performance of Sim-OPRL.
2. The paper demonstrates promising results in the demonstrated environments, but it lacks validation in more complex and realistic settings. To strengthen the evidence of the algorithm’s practical applicability, the authors should evaluate Sim-OPRL on several different datasets. One example could be MuJoCo style datasets. Other relevant papers in the field construct preference datasets from the D4RL offline benchmark. These datasets provide a more challenging and ‘closer to real world’ testbed. Evaluation on such environments (in conjunction with adding more baseline algorithms) could result in a better assessment of the algorithm’s robustness, scalability, and generalizability. The current results, while promising, do not fully demonstrate the method’s ability to handle the complexities of real-world scenarios.
3. The paper demonstrates the algorithm’s performance in relatively small-scale environments. Empirically, it does not seem to address scalability to larger, more complex environments. Due to the smaller scale test environments (Gridworld & Sepsis), the the actual scalability of the algorithm (particularly in real-world deployments outside of benchmarks) remains unclear. The authors should provide a more thorough analysis of the computational complexity of their algorithm and investigate its performance in larger state and action spaces. This would help to better understand the practical limitations of the method.
4. As the authors state, for the sepsis environment, the requisite number of preference samples is rather large, due to the sparse reward function. This seems like an inherent limitation, which they posit could be solved by warm-starting the reward model. It would be interesting to see this data and how it affects performance. If a sparse reward function is a true limitation of the Sim-OPRL method, the authors should show more experiments demonstrating that this can be 'worked around' by performing warm starts. This could also help to further justify the real world applicability of the algorithm. Furthermore, the authors should also investigate how the performance of Sim-OPRL is affected by the quality of the learned environment model. If the learned model is inaccurate, it could lead to suboptimal preference queries and reduced overall performance.

### Questions
1. How does the complexity of the reward function impact the performance of Sim-OPRL? Have you (or do you plan to) test the algorithm with environments that are characterized by more complex, multi-objective, or non-linear reward functions? If the method is agnostic to the reward function (aside from sparsity) it would help to show that as well.
2. Can you provide more details on the sensitivity of Sim-OPRL to its hyperparameters, such as the pessimism and optimism parameters? How do you recommend tuning these parameters in practice? It may be insightful to include ablation testing in the appendix that demonstrates the sensitivity (or robustness) to hyperparameter selection, especially as this could drastically affect the real-world viability of the algorithm. 
3. Are there any other algorithms that would serve as a effective and informative baseline for Sim-OPRL? If not, would it be possible to run experiments that demonstrate learning performance on naive methods?
4. Could you please clarify the rationale behind limiting the experiments to the selected datasets and environments? Are there specific challenges that restrict the application of the method to a broader range of environments and dataset combinations? If there are no such constraints, additional experimental results would be valuable. Conversely, if limitations do exist, it would be beneficial to outline what they are, the reasons for their existence, and why they do not compromise the method's overall effectiveness and practical utility.
5. Generally speaking could the authors please explain the motivations for the setting further? Specifically, would it be practical to compare the results of Sim-OPRL to running standard offline RL algorithms (CQL, IQL, TD3_BC etc.) on the offline dataset directly? If not, why not?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper delves into offline reinforcement learning from preference feedback and proposes an offline preference elicitation method to simulate trajectories from the learned environment model instead of sampling trajectories directly from the offline dataset. They provide theoretical justification for the previous RL with preference feedback method and show that their proposed method can effectively reduce the sample complexity upper bound. They also propose an empirical algorithm and show it can outperform prior methods and achieve SOTA on offline PbRL setups without access to the ground truth rewarded. They finally iid ablation studies to show the importance of incorporating the principle of pessimism.

### Strengths
1. They delve into very interesting setups: offline RL with preference feedback.

2. Their theoretical results are solid and show he advantage of their proposed preference elicitation algorithm over prior methods.

3. They propose a practical algorithm for implementation and extensive experiments show that their method outperform prior methods in several environment.

### Weaknesses
I do not see any big issues.

### Questions
/

### Soundness
3

### Presentation
3

### Contribution
2
