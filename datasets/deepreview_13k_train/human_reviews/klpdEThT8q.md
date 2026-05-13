# MA$^2$E: Addressing Partial Observability in Multi-Agent Reinforcement Learning with Masked Auto-Encoder

- Decision: Accept
- Scores: 8, 6, 6, 5

## Abstract
Centralized Training and Decentralized Execution (CTDE) is a widely adopted paradigm to solve cooperative multi-agent reinforcement learning (MARL) problems. Despite the successes achieved with CTDE, partial observability still limits cooperation among agents. While previous studies have attempted to overcome this challenge through communication, direct information exchanges could be restricted and introduce additional constraints. Alternatively, if an agent can infer the global information solely from local observations, it can obtain a global view without the need for communication. To this end, we propose the Multi-Agent Masked Auto-Encoder (MA$^2$E), which utilizes the masked auto-encoder architecture to infer the information of other agents from partial observations. By employing masking to learn to reconstruct global information, MA$^2$E serves as an inference module for individual agents within the CTDE framework. MA$^2$E can be easily integrated into existing MARL algorithms and has been experimentally proven to be effective across a wide range of environments and algorithms.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
Despite the advancements achieved with CTDE, partial observability remains a barrier to effective cooperation among agents. This paper's approach is to enable each agent to infer global information solely from its local observations, allowing it to gain a comprehensive view without relying on communication. To achieve this, the authors introduce the Multi-Agent Masked Auto-Encoder, which leverages the masked auto-encoder architecture to infer the information of other agents from partial observations. By using masking to learn how to reconstruct global information, the method functions as an inference module for individual agents within the CTDE framework. The method can be integrated into existing multi-agent reinforcement learning (MARL) algorithms and has been experimentally shown to enhance performance across a variety of environments.

### Strengths
- The paper addresses an important problem in cooperative MARL, that is dealing with partial observability without communication.
- The paper proposes an interesting, novel method which achieves very good performance in challenging SMAC and SMACv2 tasks, outperforming well-known MARL baselines, such as QMIX, QPLEX, using a relatively small number of training timesteps.
- The proposed method outperforms methods based on similar approaches, such as MAC2L [1].
- Interestingly, the proposed method can achieve comparable performance, or even outperform state-of-the-art communication-based methods.

[1] Song, Haolin, et al. "MA2CL: masked attentive contrastive learning for multi-agent reinforcement learning." Proceedings of the Thirty-Second International Joint Conference on Artificial Intelligence. 2023.

### Weaknesses
 - The framework requires a pre-training stage, which can be impractical for certain scenarios. How much pre-training is needed? How extra wall-clock time is needed for the pre-training?
- The paper conducts a limited number of experiments in GRF (that is, only for a comparison with VDN). 
- The presentation in the incorporation of the method into the MARL backbone algorithm can be improved.

The authors have addressed my concerns.

### Questions
- CDS [1], a well-known MARL paper, has reported a better performance (than MA$^2$E), using the same number of training time steps, in super-hard corridor, MMM2 and 6h vs 8z tasks, in which this paper reports a "more pronounced improvement" over baselines. Therefore, it would be beneficial if the authors included in the comparison a few exploration-based state-of-the-art methods (such as CDS) which have shown remarkable performance in SMAC tasks.
- In execution time, for agent $i$, the paper says that MA$^2$E takes only the local information of agent $i$. However, in Fig. 2, it is illustrated that the model should take as input information of all agents. So, in execution time, does the model simply masks the positions (trajectories) of the other agents?
- Considering the strong performance of the proposed method, as compared with the communication-based methods, have the authors compared the method with the communication-based baselines in Traffic Junction benchmark (which provides very challenging tasks aiming to test the effectiveness of agent communication)?

[1] Li, Chenghao, et al. "Celebrating diversity in shared multi-agent reinforcement learning." Advances in Neural Information Processing Systems 34 (2021): 3991-4002.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper introduces the Multi-Agent Masked Auto-Encoder (MA$^2$E), which leverages the masked auto-encoder architecture to infer information about other agents from partial observations. Specifically, MA$^2$E masks out the trajectories of other agents at random, enabling the agent to non-centrally reconstruct information about other agents based solely on its own local observations. This approach enhances sample efficiency and final performance during training in Dec-POMDP settings. The authors conducted extensive experiments in the SMAC, SMACv2, and GRF environments, demonstrating the outstanding performance of MA$^2$E.

### Strengths
1. The authors provide the necessary code and hyperparameter details. A preliminary review did not reveal any issues. Sharing the original code significantly enhances the credibility of the experimental results presented in the paper.

2. The motivation behind the paper is clearly articulated: the goal is to non-centrally reconstruct information about other agents using only the local observations of the agent itself, thereby improving sample efficiency in training. Although the method is straightforward, the experimental results reveal significant performance differences between MA$^2$E and other algorithms, particularly in super hard scenarios.

3. The selection of baselines in the experimental section is representative, incorporating many classic and relevant algorithms. Additionally, the experimental environments are diverse, including SMAC, SMACv2, and GRF.

4. The ablation studies are comprehensive, covering nearly all relevant variations. Furthermore, the visualization of observation inference accuracy is effectively executed.

### Weaknesses
1. There are several typos throughout the paper. For instance, a sentence is repeated in line 255, and there is an unnumbered figure in line 907.

2. MA$^2$E employs a two-stage rather than an end-to-end training approach, which contrasts with many existing works. While the authors demonstrate through ablation experiments that end-to-end training could lead to decreased performance, the pre-training aspect of the masked auto-encoder should still be factored into the algorithm's sample efficiency. Specifically, the computational cost and data requirements of the pre-training phase need to be more clearly addressed in the context of overall sample efficiency, as this pre-training phase adds to the total training time and data needed.

3. Based on the experiments, MA$^2$E still shows a significant correlation with observation overlap, indicating that communication-based methods cannot yet be fully replaced by MA$^2$E. The paper should more clearly articulate the limitations of MA$^2$E in scenarios with minimal or no observation overlap, and discuss how this impacts the applicability of the method in different multi-agent settings. The reliance on observation overlap suggests that MA$^2$E might not be suitable for environments where agents have very distinct and non-overlapping views of the world.

### Questions
1. Why did you choose to use trajectories from multiple time steps as input for the masked auto-encoder instead of the hidden states outputted by the RNN in the agent network?

2. SMAC has many representative scenarios, such as 8m_vs_9m, 10m_vs_11m, 27m_vs_30m, and 3s5z_vs_3s6z. Why were these scenarios not included or showcased in the experimental section?

3. Table 2 only presents the final convergence results of communication-based methods. Could you also provide their learning curves?

4. Similarly, regarding SMACv2, the paper only displays results for 10gen_terran (Terran_5_vs_5) and Protoss_5_vs_5. Can you include additional results from other scenarios?

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
3

### Summary
This paper presents Multi-Agent Masked Auto-Encoder (MA2E), which utilizes the masked auto-encoder architecture to infer the global state from partial observations for MARL. MA2E is trained by masking the agent-level information to recover the entire trajectories. Experiments on SMAC, SMACv2, and Google Research Football environments show that MA2E achieves superior performance when compared with representative MARL methods.

### Strengths
1.	The motivation for using MAE to infer the global state from agent observations is straightforward and well-motivated.
2.	The performance of the proposed MA2E is superior across different environments.
3.	The authors compare MA2E with other works using masked modeling such as MA2CL.

### Weaknesses
1.	Although it is claimed that MA2E can be easily integrated into existing MARL algorithms. Only QMIX-style algorithms are tested.
2.	MA2E is difficult to scale to a varying number of agents.

### Questions
1.	Why the results of COLA and MA2CL are missing in 10gen_terran and 10gen_protoss in Figure 4?
2.	Could the authors also compare with MaskMA? Could MA2E be extended into MAPPO and MADDPG?
3.	How does the sight range of each agent affect the performance of MA2E?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper focuses on multi-agent reinforcement learning under partial observability and proposes to reconstruct the agents' trajectory information through a Multi-Agent Masked AutoEncoder (MA$^2$E). During execution, the agent inputs its trajectory into MA$^2$E to infer other agents' trajectories, which is then processed by a self-attention layer. Finally, the agent aggregates the information from its observation and the inference to produce the action. The authors conducted experiments on SMAC and GRF to assess the effect of MA$^2$E.

### Strengths
1. This paper is easy to follow. The motivation is clear, and the presentation is of good quality.
2. The authors conducted sufficient experiments, which provide a comprehensive demonstration of MA$^2$E. 
3. The proposed method can be applied to various multi-agent reinforcement learning algorithms, including value-based and policy-based.

### Weaknesses
1. The novelty of this paper is relatively limited. It simply integrates a masked autoencoder into the decision-making process of agents, which is more oriented to engineering and makes little theoretical contribution. It
2. Some ablation studies are conducted on only a single scenario (e.g., 3s_vs_5z). The results may be contingent.
3. The selected baselines are not strong enough. Many MARL algorithms also modify the decision-making process of agents while keeping the constraints in observability and communication, such as RODE [1], LDSA [2], and SORA [3]. The authors should compare MA$^2$E with these methods to make the results more convincing.
4. Compared to the baselines, the training of MA$^2$E is more complex and computationally expensive, but the performance is not significant enough. In other words, this method is not cost-effective.

### Questions
1. The official code of COLA is implemented based on the original *pymarl*, while MA$^2$E is implemented based on *pymarl2*. Is there any issue of fairness?
2. How does the training cost (measured in GPU hours) of MA$^2$E compare to that of other methods?

### Soundness
3

### Presentation
3

### Contribution
2
