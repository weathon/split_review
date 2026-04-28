# Highly Efficient Self-Adaptive Reward Shaping for Reinforcement Learning

- Decision: Accept
- Avg Score: 6.50
- Scores: 8, 6, 6, 6

## Abstract
\noindent Reward shaping is a technique in reinforcement learning that addresses the sparse-reward problem by providing more frequent and informative rewards. We introduce a self-adaptive and highly efficient reward shaping mechanism that incorporates success rates derived from historical experiences as shaped rewards. The success rates are sampled from Beta distributions, which dynamically evolve from uncertain to reliable values as data accumulates. Initially, the shaped rewards exhibit more randomness to encourage exploration, while over time, the increasing certainty enhances exploitation, naturally balancing exploration and exploitation. Our approach employs Kernel Density Estimation (KDE) combined with Random Fourier Features (RFF) to derive the Beta distributions, providing a computationally efficient, non-parametric, and learning-free solution for high-dimensional continuous state spaces. Our method is validated on various tasks with extremely sparse rewards, demonstrating notable improvements in sample efficiency and convergence stability over relevant baselines.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper proposes SASR, a novel method for adaptive reward shaping in RL with sparse binary rewards, based on the idea that states that belong to trajectories ending in success are more valuable than states that belong in a trajectories that end in failure, so visiting such states should be encouraged by increasing the immediate stage reward leading to them. This mechanism is a form of temporal credit assignment, a central question in RL with sparse rewards, and appears to be very effective in speeding up learning in multiple test problems.

### Strengths
The main strength of the paper is perhaps the principled approach in augmenting the reward function of RL with sparse rewards with a component that encourages visiting states that have proven to be useful in completing a sequential decision making task in past trials. The proposed method of using beta distributions to model the probability that a state is useful avoids overconfidence in this probability from very few samples, and is helpful in encouraging exploration in the early stages of learning. The proposed use of kernel density estimation combined with random Fourier features solves the problem of keeping tally of which states are successful in continuous state spaces. The experimental verification is rigorous and of high quality and leaves no doubt in the effectiveness of the method on representative benchmark problems of significant complexity. The paper is well written and easy to follow, and the related work section is thorough and informative.

### Weaknesses
The method still needs at least some trajectories with successful outcomes, so it cannot speed up the initial discovery of such trajectories, which is perhaps the most difficult problem in RL with sparse rewards. 

A claim has been made that the method for estimating the beta distributions of expected success of individual states is parameter-free and learning-free, and I am not sure I agree with that. At the very minimum, the KDE estimator depends on the bandwidth parameter h, and the ablation study in Section 5.3 clearly shows that its value does matter a lot as regards the accuracy of estimation and the overall success of the algorithm. Usually, the bandwidth of KDE schemes is determined by a search routing of some kind, either grid search or cross-validation, which is a form of learning. Other parameters that matter are M, the number of RFF, and lambda, the weight of the additional reward term, and they must be determined somehow, preferably automated by some form of learning.

A minor typo:
P. 8. L. 427: "broadens" -> "broadening"

### Questions
The use of a state's success rate reminds me of the use of eligibility traces, whose purpose is also to assign credit to states and actions taken in them. Eligibility traces typically depend on how far in the future success happened, whereas in this paper, the success of a state does not depend on the time horizon of a positive reward. Have the authors considered time-dependent or other variable weights depending on distance to the goal state, similar to eligibility traces? 

Could the authors clarify what they mean by "parameter-free" and "learning-free" in the context of KDE estimation? Could the authors discuss potential automated methods for selecting parameters like bandwidth h, number of RFF M, and reward weight λ?

Regarding getting to successful outcomes earlier rather than later, does SASR provide any benefits in the very early stages of learning before successful trajectories are found?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents a method called Self-Adaptive Success Rate based Reward Shaping (SASR) aimed at addressing the sparse-reward problem in reinforcement learning. SASR uses success rates from past interactions to construct a shaped reward functions. Success rates are sampled from an evolving Beta distribution, estimated via Kernel Density Estimation with Random Fourier Features to improve efficiency. The authors experimentally validate SASR and ablate their design choices.

### Strengths
- The use of Beta distributions to manage exploration-exploitation trade-offs in sparse-reward environments seems to be simple yet effective.
- The use of KDE with RFF makes the estimation of Beta distributions more efficient. Moreover, the success rates based method is more computationally efficient than similar previous work (ReLara), which uses a neural network to learn shaping rewards.
- SASR shows improved convergence stability in sparse-reward settings compared to several baselines.

### Weaknesses
1. **Inconsistent Notation.** The notation is inconsistent in some parts of the paper.
	1. Equation 6 uses boldface notation for state variables, while the rest of the paper does not.
	2. Similarly, in Algorithm 1, in lines 12 and 13 the states and states buffers are bolded, when they are not everywhere else.
	3. In Section 4.3, the environmental reward uses a different notation from Equation 3. The authors should choose to either use $R^E(s_{t})$ or $r_t^E$.
2. The retention rate $\phi$ in line 265 has not been introduced yet. It can be helpful to introduce it before using it in presenting the space complexity of SASR.
3. Section 4.3 seems to be partially copied from the ReLara paper.
	1. The $\mathcal A_P$ in the Q-function is redundant.
	2. The notation for the policy should be made consistent. At the moment, the policy appears with three different notations.
4. This method was only tested for state-only reward functions. In contrast, ReLara can also work for state-action reward functions. Why is the reward function considered in SASR state-only? Can the authors also show the efficacy of SASR for state-action reward functions or provide arguments as to why this is not necessary?
5. Montezuma Revenge is know to be a hard exploration problem. It would be insightful to have a comparison of SASR with other exploration algorithms, such as RND.
6. SASR appears to be quite similar to ReLara, except it is restricted to using a Beta distribution for success rates, rather than a more expressive neural network to propose shaping rewards. The paper would benefit from a more thorough discussion on why ReLara seems to perform worse, despite using an overparametrized neural network, which should in theory be able to learn a Beta distribution.

### Questions
See **Weaknesses**. Additionally:
1. Does the method require to know $R_\min$ and $R_\max$? If not, are they estimated? How?
2. In line 305, it is stated that "if a reward is obtained within a pre-defined maximum number of steps, the corresponding sub-sequence is classified as a success". How is the threshold for the reward and number of steps decided? Is the algorithm sensitive to how these are chosen?
3. In the following grid-world environment, where B is a bad state with very low reward, O is an empty state, G is the goal state, W is a wall and A is the agent, would SASR encourage the agent A to encourage the agent to take the longer path that goes down, right and then up because the state between B and G would be counted in many successful and failure trajectories, so it would be deemed a bad state? How could you make sure that in this case, the agent still takes the shortest path?
```
| B | O | G | O |
| W | A | W | O |
| W | O | W | O |
| W | O | O | O |
```

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduced Self-Adaptive Success Rate based reward shaping (SASR) for reward-sparse RL problems. SASR incorporates success rates, defined as the ratio of a state's presence in successful trajectories to its total occurrences, as auxiliary rewards. Further, SASR adopt Kernel Density Estimation (KDE) and Random Fourier Features (RFF) to derive Beta distributions and sample success rates from that distribution.

### Strengths
- The idea of using success rate as auxiliary reward is interesting.
- The writing is clear and the paper is easy to follow.
- SASR shows promising results in the experiments.

### Weaknesses
 - Some of the selected environments are simple toy tasks. For example, the authors select the simpler Reach and Push tasks instead of the more challenging PickAndPlace and Slide tasks. It's still unclear if SASR is effective for hard-exploration tasks from the current experiment results.
- Many baselines are old. The paper should compare to more recent baselines in exploration. For example,
    - DRND (https://github.com/yk7333/DRND)
    - RLE (https://github.com/Improbable-AI/random-latent-exploration)
    - GFA-RFE (https://github.com/uclaml/GFA-RFE)
- There are no pixel-based experiments, i.e., Atari games. It's unclear how would SASR perform with pixel-based inputs?
- Typos: (Line 296) "The motivations behind this are"

### Questions
- How would SASR perform on some famous hard exploration tasks, i.e., Montezuma's Revenge and DM-Hard-8?
- Can SASR solve difficult maze tasks with sparse reward, i.e., `AntMaze_HardestMaze-v5` from https://robotics.farama.org/envs/maze/ant_maze/?
- For a hard exploration task where we only receive nonzero reward when the task is solved. If it's very difficult to collect the first successful trajectories. How will SASR perform when the success rates for all states are zero? Will the beta distribution be accurate enough to solve such problems?

### Soundness
2

### Presentation
2

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
The paper proposes a reward shaping method, SASR, for deep reinforcement learning by incorporating success rates derived from historical experiences. These success rates are sampled from Beta distributions with decreasing uncertainty. Kernel Density Estimation (KDE) and Random Fourier Features (RFF) are used to derive the Beta distributions. The method is evaluated on sparse reward tasks and compared with eight baseline methods. The results demonstrate that the proposed method outperforms the baseline methods on the chosen tasks.

### Strengths
- The paper is well-organized and easy to follow. 
- The idea makes sense. The method is original and the authors provide a clear explanation of the method.
- The authors compare their method with 8 baseline methods, which is a good practice.

### Weaknesses
 - The scope of the proposed method is unclear. Although the authors mention "sparse reward tasks" several times, it remains uncertain whether the method is exclusively suitable for sparse reward tasks. If so, this should be clearly stated [1].

- The authors motivate the method by mentioning that "most real-world environments involve high-dimensional state spaces". However, the tasks chosen for the experiments appear to involve vectors with only tens of dimensions.

- The chosen tasks are not standard in the RL community. The authors compare their method with 8 baseline methods, but 7 of these were not tested on the chosen tasks in the original papers. Additionally, there are no implementation details or results of hyperparameter searches for these baseline methods, making it unconvincing that the proposed method outperforms them. I recommend testing the proposed method on standard tasks used in the chosen baselines, such as sparse reward Atari games like Montezuma's revenge and Gravitar chosen by ROSA, #Explo, RND and PPO, or mujoco tasks (though they may not be sparse reward tasks) chosen by #Explo, SAC, TD3, and PPO. In addition, if the proposed method is intended for sparse-reward, high-dimensional, continuous control tasks, dmcontrol conld be a good choice [2,3].

- The method introduces many parameters to tune, such as the weighting factor $\lambda$, the bandwidth of the Gaussian kernel $h$, the retention rate $\phi$, and the Fourier features dimension $M$. These parameters are sensitive to performance, as shown in the ablation study (Figure 6). Additionally, some functions need to be predefined, such as the scaling function $f$ and the kernel function $K$. The interaction between these parameters and functions is complex, making it difficult to understand how they influence each other and how can the method be tuned for other tasks.

- The method introduces additional computational costs (reward computation) and memory costs (three buffers). It is unfair to compare it with other methods without considering these costs. A comprehensive comparison with other methods in terms of computational and memory costs, in addition to performance, would be more appropriate.

### Questions
- What is the formula for the scaling function $f$ in Equation 4?

- In sparse reward tasks, the most challenging part is at the beginning of the learning process when all the trajectories fail or have zero rewards. How does the proposed method handle this situation? What advantage does it offer over other methods in this situation?

- It seems Table 1 computes the average reward over the entire learning process. Why not use the final reward as the metric?

- RND achieves the best performance on MountainCar. Why is it not included in Figure 5?

- What are the dimensions of the chosen tasks? It appears that the state space is a vector of tens of dimensions. How does the method perform on tasks with high-dimensional state space or images-based tasks like Atari games or dmcontrol tasks?

- Since all tasks provide extremely sparse rewards, is the proposed method only suitable for sparse reward tasks? If not, how does it perform on tasks with dense rewards?

- Given that 7 out of 8 baseline methods were not tested on these chosen tasks in the original papers, how did you finetune the hyperparameters of these baseline methods? Did you compare their performance on the tasks reported in the original papers?

- See Weaknesses.

I am willing to increase my score if all my concerns are addressed.

### Soundness
2

### Presentation
2

### Contribution
3
