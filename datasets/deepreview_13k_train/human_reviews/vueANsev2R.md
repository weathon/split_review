# Investigating the chaotic dynamics produced by deep reinforcement learning controllers

- Decision: Reject
- Scores: 3, 6, 3, 3

## Abstract
In recent years, deep Reinforcement Learning (RL) has demonstrated remarkable performance in simulated control tasks however there have been significantly fewer applications to real-world problems. While there are several reasons for this dichotomy, one key limitation is a need for theoretical stability guarantees in real-world applications, a property which cannot be provided by Deep Neural Network controllers. In this work, we investigate the stability of trained RL policies for continuous control tasks and identify the types of dynamics produced by the Markov Decision Process (MDP). We find the solutions produced by this interaction are deterministically chaotic with small initial inaccuracies in sensor readings or actuator movements compounding over time producing significantly different long-term outcomes, despite intervention in intermediate steps. The presence of these chaotic dynamics in the MDP provides evidence that RL controllers produce unstable solutions, limiting their application to real-world problems.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Paper proposes a technique for measuring the stability of reinforcement learning policies, demonstrates that standard algorithms tend to be unstable for high dimensional environments, and proposes a modification to the reward function to improve the stability of RL policies.

### Strengths
Significance
- Paper studies an interesting and important problem -- RL policies tend to be sensitive to initial conditions. 

Clarity
- Figures and tables look nice, paper is written nicely and easy to understand.

### Weaknesses
It seems like the main contribution of the paper is in identifying a reason for policy instability (only a subset of the system state is used in the reward) and proposing a solution to enable more stable policies (constraining all system states in the reward function). However, *it is not clear whether stability, in the way it is defined in the paper, is actually a desirable characteristic of RL policies*. 

As a concrete example, let us consider walker stand. In the default version of the environment, the system state include features such as the agent's angle of the foot joint. which is not used the the reward function (reward is only dependent on torso height and angle). As a result, RL policies, given different initial conditions, may control the agent to position its foot joint in different angles while maintaining a standing position. This behavior will lead to consistently high reward across different initial conditions, while yielding a low stability score (as defined by the Maximal Lyapunov Exponent), because the stability score will punish the policy for putting the agent's foot at different angles in different trajectories. Moreover, the paper's proposed method of modifying the reward function will minimize this behavior by incentivizing the policy to always put the agent's foot in the same angle, which will lead to a higher stability score. However, it is not clear that this "stable" behavior is actually desirable. In the example of walker stand, the angle of the foot joint is not part of the reward function, because it *doesn't matter* for the performance of the task. In the current results in the paper, improving stability via the modified reward function does not consistently lead to better performance (in terms of the reward), so it is not clear why measuring and improving stability is meaningful or significant.

### Questions
Is there a scenario where improving the stability of a policy will improve the return of the policy, e.g. by providing a more shaped reward signal?

### Soundness
1 poor

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper explored the dynamics of controllers that have been trained using various reinforcement learning techniques. It analyses the MDP solutions by attempting to quantify their stability. The authors' analyses suggest that these tend to be chaotic for complex environments and agents. The work concludes with a practical guideline to mitigate these instabilities using modified reward functions.

### Strengths
The paper is well written, with a clear structure and suitable diagrams.

A main strength of the paper is the interesting problem that it tackles, which represents solution stability, and is part of a wider field dedicated to understanding and perfecting the process of embodying real-life agents, using policies trained in virtual environment.

Another strength of the work is the analysis of a range of RL algorithms, suggesting that the problem the author's identified is present in many systems.

### Weaknesses
A weakness of the paper is that only one environment is used, the Walker Walk, to show that a modified reward function can increase the stability of the solutions.

Another weakness is that while a range of RL algorithms are considered, they are not as varied as they could be. The authors should consider other algorithms types and show their dynamics. For example dynamics in off vs on-policy algorithms, or value vs policy based algorithms.

### Questions
1. What would be the results of section 5 if the walker stand and run would be considered?
2. Please define the co-domain A of the function/policy \pi in section 3.
3. What are the precise states s that were used to compute the dynamics characteristics in the experiments?
4. From figure 2, it seems like PPO has difficulties solving CR. Is this why in figure 4 we see PPO having an unusually high MLE for CR? If so, this needs to be addressed in the paper.
5. Please expand figure 5 to include the other tasks as well.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work investigates the chaotic dynamics of some continuous control tasks with the policy produced by deep reinforcement learning methods. By calculating the maximal Lyapunov exponent (MLE) numerically, they show that simple environments with low dimensions are more robust with respect to the small perturbations to the initial conditions, while complex environments with high dimensions are prone to produce unstable chaotic dynamics. To solve this issue, the authors propose to redesign the reward function such that it counts all the system states. Experiment study shows that such modification reduces the MLE but sacrifices the agent performance.

### Strengths
This paper is well-presented and easy to follow. The motivation for this work is strong. The stability of DRL controllers is indeed an important topic, especially when we want to apply such learning-based controllers to real-time systems. 

This paper contributes to this topic by investigating the chaotic dynamics produced by DRL controllers, and through several numerical studies, they show that learned controllers are indeed sensitive to the small perturbations of initial conditions. In addition, they propose to redesign the reward function to mitigate such issues.

### Weaknesses
The authors quantify the instability of the system by using the sensitivity of a dynamical system to the initial condition. However, a sensitive controller does not necessarily mean unstable from a control performance perspective. For example, Fig 1 shows sensitive dynamics, but it is hardly to be recognized as unstable. In addition, under the definition of sensitivity in this paper (Definition 1), a system seems very easy to be sensitive to since $\beta$ is only assumed to be positive (can be arbitrarily close to zero), and they only require there exist a time step $k$ such that $|| ^k u(s) - ^k u(\hat{s}) || > \beta$. A more rigorous definition of stability, potentially incorporating metrics like settling time or overshoot within a defined acceptable range, would be more informative.

Furthermore, the modification of the reward function (2) appears to be impractical. In order to obtain reference value $\bar{s}$, one has to run the standard problem first, this is rather inefficient. The need to pre-compute a reference value for each policy undermines the adaptability and generalizability of the proposed solution. I believe such a method is not practical, especially in scenarios where the optimal trajectory is unknown or computationally expensive to obtain.

### Questions
1. In Fig 5, how to compute the MLE during the training phase?
2. The MLE of the walker walk problem shown in Fig 5 seems inconsistent with the ones in Table 2, are they different sets of experiments?

I would also appreciate the authors to comment on my concerns in the Weakness section.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper established that small changes in the system state compound to produce significantly different long-term outcomes for RL algorithms and proposed a novel method for improving the stability of RL policies for continuous control environments via reward function modification.

### Strengths
This simulation in this paper illustrates that small initial inaccuracies in sensor readings or actuator movements compounding over time can produce significantly different long-term outcomes

### Weaknesses
1. The paper introduces several unfamiliar terms such as "TRAJECTORY STABILITY," "Sensitivity," and "Chaotic," without providing sufficient context or clarification. It is imperative for the author to offer clear definitions of these terms and elaborate on how they relate to Lyapunov stability, which readers might be more acquainted with. Specifically, the paper should define what constitutes a 'small change' in the system state, and how this relates to the sensitivity of the system. Furthermore, the concept of 'chaotic' needs to be rigorously defined in the context of dynamical systems, possibly referencing established measures like Lyapunov exponents, rather than just being used qualitatively.

2. The paper repeatedly emphasizes that the MDP framework can be reinterpreted as a controllable dynamical system. However, this assertion is widely acknowledged and lacks the novelty; therefore, continually highlighting it does not contribute significantly to the paper's academic value. The paper would benefit from a more nuanced discussion of how this specific interpretation is leveraged in the context of the proposed method, rather than simply stating the equivalence.

3. The paper is marred by poor writing and grammatical errors, an issue that is evident in sentences like, "One key property of a trajectory which a paramount to dynamical systems theory is it’s stability." Additionally, the results presented in Figure 5 are convoluted, suggesting that the author needs to refine their writing and data presentation skills. The figure lacks clear labeling, and the method for generating the data is not sufficiently explained, making it difficult to interpret the results.

4. The proposed method of "constraining all system states in the reward function" is perplexing. The paper fails to articulate the intuition and logic behind this approach, making it difficult for readers to comprehend its purpose and effectiveness. The paper needs to provide a clear rationale for why constraining all states in the reward function would lead to more stable policies. It is unclear how this method relates to existing techniques for shaping reward functions or ensuring stability in RL.

5. There is a conspicuous absence of discussion concerning the existing body of research on the stability of reinforcement learning (RL) policies. The author neglects to reference any prior studies in this area, indicating a need for more comprehensive literature review and research on the topic. The paper should discuss how the proposed method relates to or differs from existing approaches for stable RL, and it should clarify the limitations of existing methods that the proposed approach aims to address.

### Questions
No

### Soundness
1 poor

### Presentation
2 fair

### Contribution
2 fair
