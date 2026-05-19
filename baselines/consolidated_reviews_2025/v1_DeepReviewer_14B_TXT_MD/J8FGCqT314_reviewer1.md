### Summary

The paper first provides a theoretical proposition regarding the success of decision transformers (DTs) in deterministic environments, as well as motivation for why they fail in stochastic environments (increasing variance of the return-to-go). The paper then proposes a method (D2T2) to address this issue by changing the supervision signal for the DT from the return-to-go to a temporal difference (TD) learned value, which is used to select a desired next state. This reduces the variance of the supervision signal, as well as the horizon of the DT. Experiments in various offline RL domains are performed, showing that D2T2 outperforms baselines in stochastic environments.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper is well written, with a clear motivation, and the proposed method is well explained.
- The proposed method is simple and intuitive, and should be relatively easy to implement.
- The proposed method outperforms baselines in the Tailgate and FrozenLake environments, which are (somewhat) representative of the stochastic setting for which the method is proposed.

### Weaknesses

#### Some Related Works


#### comment

 - I am not convinced by the FrozenLake experiments. The performance of all methods is poor (probability of reaching the goal while avoiding the holes). I feel that a different environment, or a different representation, would allow the performance of all methods to increase, resulting in a more fair comparison. It seems that a simple baseline that always moves right would achieve a non-negligible probability of reaching the goal.
- The performance of D2T2 in the deterministic domains is very similar to that of DT, which is expected given the theoretical analysis of deterministic environments. However, I believe that the stochasticity in the environments comes not only from the transition function, but also from the reward function. Therefore, experiments in which the transition function is deterministic, but the reward function is stochastic, would help to better understand the advantages of D2T2 over DT. Specifically, a more controlled experiment where the reward is stochastic but the transitions are deterministic would isolate the effect of reward stochasticity on the performance of both methods. This would provide a more nuanced understanding of the conditions under which D2T2 offers a significant advantage.

### Suggestions

To address the concerns regarding the FrozenLake environment, it would be beneficial to explore alternative state representations or environments that are more conducive to demonstrating the strengths of the proposed method. For instance, using a continuous state space approximation of the FrozenLake environment, or a different grid-world environment with more complex reward structures, could potentially highlight the advantages of D2T2 more clearly. Additionally, it would be helpful to compare the performance of the methods against a simple, yet effective, baseline for the FrozenLake environment, such as an optimal policy derived from dynamic programming. This would provide a clearer understanding of how well each method is performing relative to the optimal solution, and would help to determine if the poor performance is due to the limitations of the methods or the environment itself. Furthermore, it would be useful to investigate the sensitivity of the methods to different levels of stochasticity in the FrozenLake environment, as this could reveal the conditions under which D2T2 truly excels.

To further investigate the advantages of D2T2 in stochastic environments, it is crucial to conduct experiments where the transition function is deterministic, but the reward function is stochastic. This can be achieved by introducing noise to the reward function, such as adding a random variable to the reward at each step. This would allow for a more controlled analysis of the impact of reward stochasticity on the performance of both DT and D2T2. For example, one could consider a scenario where the reward is either +1 or -1 with some probability, or where the reward is a continuous value with some added noise. This would help to isolate the effect of reward stochasticity and provide a more nuanced understanding of the conditions under which D2T2 offers a significant advantage over DT. It would also be beneficial to explore different types of reward stochasticity, such as additive noise versus multiplicative noise, to see how each affects the performance of the methods.

Finally, it would be valuable to investigate the computational cost of D2T2 compared to DT, especially in terms of training time and memory requirements. While the paper mentions that the proposed method is simple and intuitive, it would be helpful to have a more concrete understanding of the computational overhead associated with the TD-learning component. This is particularly important for practical applications where computational resources may be limited. Furthermore, it would be useful to analyze the sensitivity of D2T2 to the choice of hyperparameters, such as the learning rate and the discount factor, as this could affect the performance of the method in different environments. A thorough analysis of these factors would provide a more complete picture of the practical implications of using D2T2.

### Questions

- I would like to hear the authors' opinion regarding my comment on the stochasticity in the reward function. I believe that the proposed method should have a particularly large advantage in environments where the transition function is deterministic, but the reward function is stochastic. Is this true?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
