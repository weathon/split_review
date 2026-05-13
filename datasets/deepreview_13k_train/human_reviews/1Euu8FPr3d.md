# Unsupervised Multi-Agent Diversity With Wasserstein Distance

- Decision: Reject
- Scores: 5, 6, 5, 5

## Abstract
In cooperative Multi-Agent Reinforcement Learning (MARL), agents sharing policy network parameters are observed to learn similar behaviors, which impedes efficient exploration and easily results in the local optimum of cooperative policies. In order to encourage multi-agent diversity, many recent efforts have contributed to distinguishing different trajectories by maximizing the mutual information objective, given agent identities. Despite their successes, these mutual information-based methods do not necessarily promote exploration. To encourage multi-agent diversity and sufficient exploration, we propose a novel Wasserstein Multi-Agent Diversity (WMAD) exploration method that maximizes the Wasserstein distance between the trajectory distributions of different agents in a latent representation space. Since the Wasserstein distance is defined over two distributions, we further extend it to learn diverse policies for multiple agents. We empirically evaluate our method in various challenging multi-agent tasks and demonstrate its superior performance and sufficient exploration compared to existing state-of-the-art methods.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposes a novel approach to multi-agent policy diversity within the MARL domain. Firstly, the paper provides a detailed analysis of the shortcomings of current diversity methods based on mutual information. Subsequently, it leverages a CPC-based next-step prediction method to facilitate the learning of distinguishable representations of agent trajectories. Furthermore, it introduces a method for rapidly calculating the Wasserstein distance in multi-agent systems, which is integrated into practical MARL algorithms in the form of intrinsic rewards. Finally, the effectiveness of the proposed method is validated on the Pac-Men, SMAC/SMACv2 environments.

### Strengths
1. The paper is clearly articulated and well-structured, with the discussion on MI-based methods being particularly enlightening.
2. The discussion in the experimental section is comprehensive, with a thorough design of ablation studies.

### Weaknesses
Although the paper is well-written, I have major concerns regarding the novelty of the paper. 
1. The first is the introduction of Wasserstein Distance (WD) to quantify the policy diversity (as represented by trajectories) among agents, where there has already been related work in the MARL domain, which may not represent a significant innovation. For example, work [1] introduces the concept of system neural Diversity based on WD, and work [2] proposes a policy distance concept also based on WD by learning representations of policy distributions. 
2. The second concern is about translating the diversity's WD into intrinsic rewards to encourage diversity. In fact, methods purely encouraging diversity are not limited to intrinsic rewards or objective functions but also include controlling the network structure. Work [3] has even gone beyond merely encouraging diversity to being able to control the diversity of a multi-agent system to a specific value. Therefore, this work might not be novel enough to match the ICLR community. 
3. Correspondingly, there are concerns regarding the selection of baselines. Since this is a method encouraging multi-agent diversity, why has it only been compared with MI-based methods? Baselines should include MARL diversity-related but MI-unrelated methods. For example, RODE [4], ADMN[5], and the previously mentioned methods?

*I hope the authors can understand my concerns and address them together with the following questions.*

### Questions
Beyond the major concerns I have listed, there are the following questions: 
1. Can this method be applied to agents in continuous action spaces, and to multi-agents with different action spaces? 
2. Regarding the discussion in lines 171-173 of the paper, can the authors provide an example to illustrate this point, and why wouldn't the WD directly become zero?
3. Compared to vanilla methods like QMIX and QTRAN, WMAD will undoubtedly introduce additional computational overhead. If WMAD appears to require fewer timesteps to achieve comparable performance levels, but demands more CPU/GPU computation time （or real time）, could this impact its practical use? Have there been any experiments conducted to assess the extent of this additional computational load?

4. WMAD chooses the Euclidean distance as the cost function to compute the Wasserstein distance. I am curious about the results if the Euclidean distance were used directly as the intrinsic reward.

### Soundness
2

### Presentation
4

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
In order to promote exploration in multi-agent reinforcement learning, the authors propose a method WMAD to maximize the difference in agents’ trajectories. The difference in trajectories is represented by Wasserstein distance, which is calculated with latent variables. Extensive experiments are conducted to show the superiority of WMAD in tasks including Pac-Men and SMAC.

### Strengths
1. The authors propose SMAC to promote exploration by using Wasserstein distance to evaluate the difference in trajectories of different agents, which is more reasonable than mutual information.
2. Experimental results show that the proposed algorithm WMAD is much better than baseline algorithms.

### Weaknesses
1. Although the use of Wasserstein distance is better than mutual information, it seems that the idea of using Wasserstein distance to enhance the difference in trajectories of agents has been proposed, such as “Controlling Behavioral Diversity in Multi-Agent Reinforcement Learning”.
2. The authors claim that the proposed algorithm WMAD achieve SOTA with better exploration, while the baseline algorithms in experiments are not specifically designed for exploration. Baselines are fundamental MARL algorithms and mutual information-based exploration algorithms. Other kinds of exploration methods are missing, such as “Episodic multi-agent reinforcement learning with curiosity-driven exploration”.
3. It seems that the results of baselines are much worse than those in original papers, such as MAVEN in 6h_vs_8z (super hard) and corridor (super hard).

### Questions
See the weaknesses. Look forward to more explanation.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper focuses on the issue of diversity in cooperative multi-agent reinforcement learning (MARL). As parameter sharing in MARL often leads to homogeneous behaviors and limited exploration, some previous methods promote identity-aware multi-agent diversity by mutual information (MI). The authors point out the drawbacks of MI and replace it with Wasserstein Distance. The Wasserstein Multi-Agent Diversity (WMAD) uses the Wasserstein distance between the trajectory distributions of different agents as an intrinsic reward to facilitate exploration. The authors conducted experiments on Pac-Men, SMAC and SMACv2 to test the proposed method.

### Strengths
1. The authors describe the framework and implementation of WMAD in detail, which makes the method easy to understand.
2. The motivation of this paper is very clear: First, promote multi-agent diversity for exploration; Second, improve previous mutual-information-based approaches.
3. The visualization of the visited area strongly demonstrates the effectiveness of WMAD in promoting diversity.

### Weaknesses
1. The novelty is relatively limited. As the authors mentioned, there are already many works about promoting diversity for enhanced exploration. WMAD follows them and replaces the metric of diversity with Wasserstein distance.
2. According to Figure 4(d), the diversity of agents' trajectories is improved significantly. However, how would WMAD perform in scenarios that require homogeneous behaviors (e.g., focus fire on the same enemy in SMAC)? I think the authors need to include results or discussion on WMAD's performance in such scenarios.
3. The experiment results in SMAC and SMACv2 are very significant. However, it is worth noting that the learning rate is set to 0.005 and the batch size is 128. The exploration rate is also tuned. These settings are proven to significantly improve the performance of QMIX in *pymarl2* [1]. Therefore, I wonder how the other baselines are implemented, and I'm concerned about the fairness of the experiments. Maybe the authors could clarify the implementation and hyperparameter settings of other baselines. Furthermore, It would be better to provide the results of WMAD under the hyperparameter settings in *pymarl* and *pymarl2*, respectively.

### Questions
1. I hope the authors can provide comparison results between WMAD and baselines in terms of the number of parameters and training costs.
2. Please see Weaknesses 3.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes Wasserstein Multi-Agent Diversity (WMAD), a new method for promoting exploration in Multi-Agent Reinforcement Learning (MARL). Unlike mutual information-based approaches, WMAD maximizes the Wasserstein distance between agents' trajectory distributions to encourage diverse behaviors. The method leverages Contrastive Predictive Coding (CPC) to learn trajectory representations and introduces a nearest neighbor intrinsic reward based on the Wasserstein distance. WMAD achieves more diverse policies and better exploration, outperforming state-of-the-art methods in complex multi-agent tasks.

### Strengths
- The paper introduces a new approach by using the Wasserstein distance to promote agent diversity, addressing the limitations of mutual information-based methods in encouraging effective exploration.

- Using contrastive predictive coding for learning distinguishable trajectory representations enhances the ability to measure differences between agents’ behaviors.

- The method is evaluated across multiple challenging multi-agent environments (like Pac-Men, SMAC, and SMACv2), demonstrating consistent outperformance over baseline methods. The proposed approach is integrated with MARL algorithms like QMIX, showing its practical applicability and potential to improve real-world cooperative learning tasks.

- The paper is organized clearly and it is easy to follow its core idea.

### Weaknesses
 - The Wasserstein distance relies on an appropriate cost function to measure trajectory differences, and the paper uses a simple Euclidean distance without exploring task-specific alternatives, which may limit the method’s adaptability.

- Although the paper employs kernel-based techniques to reduce costs, computing the Wasserstein distance for every pair of agents in large-scale multi-agent systems can still be computationally intensive, making the system not scalable.  

- The paper does not thoroughly explore the sensitivity of the method to key parameters, such as the choice of kernel or the weighting of intrinsic rewards, which could affect generalizability.

### Questions
- Have you explored alternative cost functions tailored to specific tasks, and if so, how did they impact the results?

- Although you adopted a kernel-based method to reduce computational costs, what challenges did you face in scaling the method to larger multi-agent systems? Will this limit the proposed method's scalability?

- How sensitive is your method to the selection of hyperparameters, such as the kernel width or the coefficient for intrinsic rewards? Did you conduct any sensitivity analysis to understand their impact?

- Since the effectiveness of your method heavily relies on CPC for trajectory representation, how robust is the learned representation to noise or perturbations in agent observations?

### Soundness
3

### Presentation
2

### Contribution
3
