# Do not Start with Trembling Hands: Improving Multi-agent Reinforcement Learning with Stable Prefix Policy

- Decision: Reject
- Scores: 5, 5, 5

## Abstract
In multi-agent reinforcement learning (MARL), the $\epsilon$-greedy method plays an important role in balancing exploration and exploitation during the decision-making process in value-based algorithms. However, we find that $\epsilon$-greedy can be deemed as the concept of "trembling hands" in game theory when the agents are more in need of exploitation, which may result in the Trembling Hands Nash Equilibrium solution, a suboptimal policy convergence. Besides, eliminating the $\epsilon$-greedy algorithm leaves no exploration and may lead to unacceptable local optimal policies. To address this dilemma, we use the previously collected trajectories to plan an existing optimal template as candidate policy, which we call \textbf{Stable Prefix Policy}, in contrast to trembling hands. When the policy is close to the optimal policy, the agents follow the planned template, and when the policy still needs exploration, the agents will adaptively dropout. We scale our approach to various value-based MARL methods and empirically verify our method in a cooperative MARL task, SMAC benchmarks. Experimental results demonstrate that our method achieves not only better performance but also faster convergence speed than baseline algorithms within 2M time steps.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In order to balance between exploration and exploitation during the training process, the authors encourage the policy to follow the optimal trajectory as planned by a Monte-Carlo Trajectory Tree (MCT²). The MCT² is built upon historical trajectories, wherein states are organized into clusters via KMeans clustering. Within the MCT² framework, state values within the same cluster node are concurrently updated. The authors leverage PUCB values to find the optimal path across these clusters. During the rollout, when the actual state (cluster) diverges from the predicted state (cluster), the policy adopts an ε-greedy approach to facilitate exploration.
Experiments conducted within the SMAC benchmark show that the proposed method accelerates training and can be integrated into various MARL algorithms, including QMIX, QPLEX, and OW_QMIX.

### Strengths
The authors innovatively apply Monte-Carlo Tree structure into MARL context, leading to increased training speed. The proposed method may be applied to various existing MARL algorithms, thereby potentially contributes to the field of MARL research.

### Weaknesses
The experiment results do not conclusively demonstrate the effectiveness of the proposed method. In Figure 8, the performance of the proposed policy closely mirrors that of the original QMIX implementation. I would suggest the authors to test on more challenging MARL benchmarks, though those benchmarks often require more exploration, which may pose challenges for the proposed method.

Also, many MARL algorithms already suffer from a lack of exploration. The proposed method, in its pursuit of faster convergence, makes the additional trade-off of further diminishing exploration in favor of exploitation. This strategy necessitates careful consideration due to the potential consequences it may have on the algorithm's overall effectiveness.

### Questions
- In Section 6, the authors claim that the proposed method can be applied to the critic training in Actor-Critic MARL alrogithms. Can you briefly describe how to implement the proposed method in, say, MAPPO? And what is the performance improvement when applying to MAPPO?
- In the matrix game presented in Section 1, should the $epsilon$ for player 1 be 0.1?
- Can the proposed method be applied to scenarios with continuous action spaces?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In order to alleviate the Trembling Hands Nash Equilibrium solution caused by the $\varepsilon$-greedy method in multi-agent reinforcement learning, this paper proposes a Stable Prefix Policy (SPP). SPP can rebalance the exploration and exploitation process when the policy of agents is close to the optimal policy during the training process. The specific method is to implement a Monte-Carlo Trajectory Tree (MCT$^2$) to preserve the structure of previous trajectories, which can plan the existing optimal trajectory template. When agents follow this template during rollouts, the target value is assembled with other target values with the same trajectories. When the agents drop out from the template, the $\varepsilon$-greedy method is activated afterward. SPP can be applied to any value decomposition framework, and experimental results in SMAC and MPE show that it can improve the performance of the basic algorithm.

### Strengths
1. This paper introduces the concept of the trembling hands into cooperative multi-agent reinforcement learning, which is reasonable and novel. The two didactic tasks in the introduction section fully demonstrate that the Trembling Hand Perfect Nash Equilibrium does exist in multi-agent tasks, which provides sufficient reasons for the proposal of the Stable Prefix Policy.
2. This paper implements MCT$^2$, which can plan an existing optimal trajectory (EOT) based on the trajectories in the replay buffer. SPP calculates the target value for TD update by comparing the actual trajectory of the agent with EOT, which is indeed a very novel approach.
3. Key resources (proofs, code, and replay videos) are available, and sufficient details are described such that an expert should be able to reproduce the main results.
4. The experimental results are thoroughly analyzed. For example, The dropout time step ratio in Figure 7 illustrates the working mechanism of SPP and is intuitive.

### Weaknesses
1. The proposed method is based on the premise that agents should be capable of finding a policy toward success from historical interactions. In other words, SPP relies heavily on the performance of the underlying algorithm. This reliance is a significant limitation, as SPP's effectiveness is directly tied to the quality of the initial policies discovered by the base algorithm. If the base algorithm struggles to find even a moderately successful policy, SPP's ability to refine and stabilize behavior will be severely hampered. The paper does not adequately address scenarios where the underlying algorithm fails to produce a reasonable initial policy.
2. The trembling hands is a concept in multi-agent games, but this paper only provides solutions in cooperative scenarios (Dec-POMDP problems). At the same time, SPP is only applied to value decomposition methods. This narrow focus limits the general applicability of the proposed method. The paper does not explore how SPP might be adapted to competitive or mixed cooperative-competitive environments, nor does it discuss its potential integration with other MARL paradigms beyond value decomposition. This raises questions about the method's robustness and versatility.
3. MCT$^2$ introduces more hyperparameters, which increases the difficulty and workload of hyperparameter tuning. The paper acknowledges this but does not provide sufficient guidance on how to efficiently tune these parameters. The lack of a systematic approach to hyperparameter optimization makes it difficult to apply the method in practice. Furthermore, the paper does not analyze the sensitivity of the method to these hyperparameters, which is crucial for understanding its robustness.
4. The proposed method was only evaluated on SMAC (the description of the experimental results in MPE is skimpy and unconvincing). SMAC is a popular multi-agent experimental platform but has been pointed out to have many shortcomings [1]. More and more researchers in the MARL community advocate conducting experiments in multiple different domains to evaluate the proposed algorithm comprehensively [2]. The lack of experiments on diverse environments makes it difficult to assess the generalizability of the proposed method. The paper should include experiments on more challenging and varied environments to demonstrate the robustness of SPP.

### Questions
1. What is the value of the hyperparameter $t_{inter}$? How does its value affect the performance?
2. The target value $y_t$ in vanilla QMIX is $y_t = r_t+\gamma\max_{a^{t+1}}Q_{tot}(s^{t+1}, a^{t+1} )$, which is related to $s^{t+1}$. Why is $y^t$ still related to $s^t$ in Eq. (3)?
3. Is there any theoretical basis to prove that $Q^t_{assem}$ is more accurate than the original $Q_{tot}$?
4. I think that in some scenarios, the SPP variant may be more likely to fall into a local optimal solution. Suppose that in such a scenario, agents can easily access the state corresponding to the suboptimal solution, while the state corresponding to the global optimal solution is in the opposite direction and relatively difficult to access (for example, further away from the initial position of the agents). The SPP variant may directly give up early exploration and find it difficult to converge to the global optimal solution. Of course, the above issue can be alleviated by adjusting $c_{ucb}$, but this requires sufficient prior knowledge.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper addresses the problem of trembling hands in multi-agent systems, namely the negative effect that exploration has on the coordination between agents. This effect is particularly evident when $\espilon$-greedy policies are used as template policies. This work proposes a method to compute a template policy to be followed, instead of greedy policies, and offers some empirical evidence that the proposed method can be competitive on some experimental settings.

### Strengths
The trembling hands problem plays a central role in multi-agent coordination and the idea to follow specifically designed policies instead of more standard policies might lead to original results.

### Weaknesses
Unfortunately, the limitations of this work are extensive and I believe structural. The exposition is the main factor concerning this feedback, both from the point of view of the rhetorics and for the clarification of the original contributions. Here is a (non-exhaustive) list of points:
- In the abstract it is claimed that [you] " find that $\epsilon$- greedy policies can be deemed...", it is unclear how and why this was not already known. In its second part unclear. How do you compute such policies? What do you mean by "plan an existing optimal policy"? The description of what was done is unclear to me, and how this was done is absent.
- The related works section addresses the background rather than the related works, and the background is insufficient in the exposition to provide tools to understand what will be done later. Trembling Hands Nash Equilibria are never defined, for example. This leads to the fact that in the proposed method, it was unclear to me what portions of the whole regime are proper contributions of the work and what are not. 
- The Theoretical Analysis is absent, meaning that in the way it is done is mostly unclear what it should suggest. 
- The Experimental Evaluation suggests some cases of competitiveness but does not compare the methods from a computational point of view, which I believe would help understand the pros and cons of the proposed method. Finally, it was not clear to me how the hyper-optimization of the Sota algorithms used as baselines was done, both in the standard case and in the SDD-augmented case.
- A scientific analysis of the limitations would be needed.

Finally, some English phrasing is wrong and some typos are present (for example there should be an $\epsilon$ at the 9th line of the first page I believe)

### Questions
Unfortunately, the limitations seem extensive, and I believe a refactoring of the work is needed, I hope the comments suggest the portions of the work to be addressed, but I am open to further provide insights and discuss.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair
