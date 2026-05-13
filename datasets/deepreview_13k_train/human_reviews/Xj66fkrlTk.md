# Optimizing Backward Policies in GFlowNets via Trajectory Likelihood Maximization

- Decision: Accept
- Scores: 6, 5, 8, 5

## Abstract
Generative Flow Networks (GFlowNets) are a family of generative models that learn to sample objects with probabilities proportional to a given reward function. The key concept behind GFlowNets is the use of two stochastic policies: a forward policy, which incrementally constructs compositional objects, and a backward policy, which sequentially deconstructs them. Recent results show a close relationship between GFlowNet training and entropy-regularized reinforcement learning (RL) problems with a particular reward design. However, this connection applies only in the setting of a fixed backward policy, which might be a significant limitation. As a remedy to this problem, we introduce a simple backward policy optimization algorithm that involves direct maximization of the value function in an entropy-regularized Markov Decision Process (MDP) over intermediate rewards. We provide an extensive experimental evaluation of the proposed approach across various benchmarks in combination with both RL and GFlowNet algorithms and demonstrate its faster convergence and mode discovery in complex environments.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a novel method to optimize the backward policy of the GFlowNet during training. The proposed method can be combined with any GFlowNet training method, and the experimental results demonstrate that it can bring performance improvement in some tasks.

### Strengths
- This paper is well written. The presentation and structure of this paper are clear.
- The proposed method, which employs an EM-style mechanism to optimize the training objective, is interesting. Theoretical analysis guarantees its convergence, and it can be used in any GFlowNet algorithm.

### Weaknesses
 - The performance improvement is marginal. On the sEH task, the proposed method even harms the performance, as explained in line 485. Moreover, the experiments (e.g., Qm9 and sEH) included in this paper are somewhat toy. I encourage the authors to consider more complex and large-scale benchmarks, such as AMP and RMA generation [1].


[1] Biological Sequence Design with GFlowNets, ICML 2022

### Questions
NA

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a method called Trajectory Likelihood Maximization (TLM) for optimizing backward policies in Generative Flow Networks (GFlowNets). The authors formulate the GFlowNet training problem as a unified objective involving both forward and backward policies and propose an alternating minimization procedure. The method is validated through extensive experimental evaluation across various benchmarks.

### Strengths
- The proposed TLM method is designed to be easily implementable and compatible with existing GFlowNet training algorithms.
- The authors validate their approach across four different tasks, demonstrating its effectiveness in various scenarios.
- The paper is well-structured and clearly written, with careful explanations of technical concepts and methodological choices.

### Weaknesses
 - Limited comparative analysis: While the paper acknowledges recent work by Jang et al. (2024) on pessimistic backward policies, it doesn't provide a direct experimental comparison with this highly relevant approach. Such a comparison would help readers understand the relative advantages of TLM. Though the experiments are extensive, it would be valuable to see more detailed analysis of how TLM performs compared to other backward policy optimization methods across different types of environments.
- Ablation studies: The paper could benefit from more detailed ablation studies to understand the contribution of different components of the proposed method.
- Results presentation: It will be better to combine the last three columns in Figure 1 to a single figure as they are just different variants of GFlowNets training objectives. Including the best-performing loss will better present the results (e.g., row 2).

### Questions
1. Could the authors provide a direct experimental comparison with the pessimistic backward policy approach proposed by Jang et al. (2024)? This would help establish the relative merits of TLM in similar settings.
2. Can the authors provide an explanation for the performance of TLM with different choices of the GFlowNet training objective (TB, DB, SubTB)? Are there certain objectives where TLM shows particularly strong or weak performance?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper studies the connection between GFlowNet training and entropy-regularized reinforcement learning problems–also known as soft RL. It specifically tackles this relationship in the setting of the fixed backward policy which is considered a significant limitation in the literature. For this indeed, they propose a simple backward policy optimization algorithm; Trajectory Likelihood Maximization (TLM)  that primarily involves a direct maximization of the value function in an entropy-regularized Markov Decision Process (MDP) over intermediate rewards. They formulate the GFlowNet training problem as a unified objective involving both forward and backward policies and propose an alternating minimization procedure. Their main contribution is deriving the first unified approach for adaptive backward policy optimization in soft RL-based GFlowNet methods, i.e. the TLM. They carry out an experimental evaluation on Hypergrid and Bit Sequence as well as two molecule design environments: sEH and QM9 to conclude that their algorithm converges faster and that can be integrated with any existing GFlowNet training algorithm. Lastly, there are empirical experiments done to show the performance of TLM under different hyperparameter choices.
In general, this paper could be a good contribution, with the caveat of some clarifications on the theory and experiments. Given these clarifications in an author's response, I would be willing to increase the score.

### Strengths
The authors study a very important problem in the GFlowNets and entropy-regularized RL literature which is backward policy optimization. They propose the TLM method that represents the first unified approach for adaptive backward policy optimization in soft RL-based GFlowNet methods which enhances mode exploration and accelerates convergence in complex GFlowNet environments. They formulate the GFlowNet training problem as a unified objective involving both forward and backward policies, proposing an alternating minimization procedure. For novelty, they approximate these two steps through a single stochastic gradient update and derive an adaptive approach for combining backward policy optimization with any GFlowNet method, including soft RL methods. The significance of their work arises from working on the limitations of two main previous research; Mohammadpour et al. (2024) and Jang et al. (2024). Furthermore, their approach can be connected to cooperative game theory by interpreting the forward policy PF as a forward player and the backward policy PB as a backward player, with both players attempting to minimize KL-divergence between corresponding trajectory distributions. For theory, they introduce a new theorem that shows that stability is essential for theoretical convergence. The quality of the proposed method is shown by their numerical experiments. TLM greatly speeds up mode discovery on the QM9 environment for all GFlowNet algorithms. Their results support the findings of Mohammadpour et al. (2024), where it was also observed that the backward policy optimization enhances GFlowNets on more complex and less structured environments like QM9. As a last note, the math behind their algorithm is neat and well-explained.

The main strengths are as follows:
- Deriving the trajectory likelihood maximization (TLM) method for backward policy optimization.
- The proposed method represents the first unified approach for adaptive backward policy optimization in soft RL-based GFlowNet methods. The method can be integrated with any existing GFlowNet training algorithm.
- Providing an extensive experimental evaluation of TLM in four tasks, confirming the findings of
Mohammadpour et al. (2024), emphasized the benefits of training the backward policy in complex environments with less structure.
- Providing the basis for implementing and extending their approach in different domains such as cooperative game theory.

### Weaknesses
The paper does not do a great job of demonstrating the deficiencies of the proposed algorithm. No section in this paper clearly explains and shows the difference between the proposed algorithm and other related work. In other words, the reader may not understand what specifically the work you are trying to build your work on. The authors point to references to establish closely related work such as Mohammadpour et al. (2024) and Jang et al. (2024), but do not clearly and plainly show what exactly they are improving, and what previous limitations they are trying to overcome. Furthermore, the authors mention that there are some similarities between their algorithm and a celebrated EM-algorithm (Dempster et al., 1977) and Hinton’s Wake-Sleep algorithm (Hinton et al., 1995), but did not mention what aspects those similarities are.

The experiments do not seem well justified, in the Hypergrid environment, Figure 1, the authors do not clearly explain why their method TLM fails to outperform the naive method in the TB training. In the Bit Sequences environment, the authors again do not show a sufficient explanation for the different results shown in Figure 2-Top row such as the improvement in DB and why TLM does not affect the results much in TB and SubTB. In addition, there seems to be no clear reason for producing results using two different metrics: Found Modes, and the Spearman Correlation between R and P_theta in three different environments, Bit sequences, sEH, and QM9. No explanation for Figure 2 (center and bottom) where TLM greatly speeds up mode discovery on QM9 for all GFlowNet algorithms, but shows similar or worse performance when compared to other backward approaches on sEH. There is no justified explanation of the poor performance of TLM on sEH in terms of mode discovery in all four Gflownets training algorithms.

Lastly, in Figure 3, their conclusion “TLM results in better correlations when paired with MunchausenDQN and SubTB, and shows similar results to the baselines when paired with DB and TB.” is not well justified. In what aspects does that affect your method? It would be much better to explain their method’s performance alongside its deficiencies in a more active discussion section.

### Questions
For the related work, I still cannot understand what connections you are trying to make and which research you are trying to use and build upon. More specifically, what limitations are you trying to overcome? What are the similarities between your algorithm and the celebrated EM-algorithm (Dempster et al., 1977) and Hinton’s Wake-Sleep algorithm (Hinton et al., 1995) and how does TLM differ from their algorithm?
The experimental work does not seem well justified, but there is no discussion of the varying performances across the environments; what conclusions are you deriving? Do you have any explanations for the deficiencies your algorithm has which were shown in some parts of the empirical results? Do you have any suggestions in order to overcome those shortages? 
The experiments do not provide convincing evidence of the correctness of the proposed approach or its utility compared to existing approaches. There are so many missing details it is difficult to draw many conclusions:
- Why did you use an online backward policy to compute the loss for the backward policy L_TLM?
- Why did you use a target backward policy to compute the loss for the forward policy L_Alg?
- In Hypergrid, all models are parameterized by MLP with 2 hidden layers, why? There seems no study of the decaying learning rate conducted on the Hypergrid environment, any comments?
- Why did you choose transformers to parameterize your models in the Bit Sequences environment?
- There is no clear rule for choosing your hyperparameters; it appears that you are simply taking the values established in previous related work. Why?
The differences in the “full plots” compared to the original ones are very small when choosing decaying learning rates. Can you provide some context to understand the significance of this difference?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a novel method called Trajectory Likelihood Maximization (TLM) for optimizing the backward policy in Generative Flow Networks (GFlowNets). GFlowNets are a class of generative models, and the TLM method accelerates convergence in complex tasks by directly maximizing the likelihood of trajectories. Additionally, it significantly enhances exploration capabilities in high-dimensional tasks.

### Strengths
1. The TLM method shares a strong theoretical connection with existing reinforcement learning approaches, such as entropy-regularized RL. It introduces a novel joint optimization framework that enhances the efficiency of learning the backward policy. These theoretical connections are validated through experimental results presented in the paper.

2. The method is grounded in the maximum likelihood estimation problem from reinforcement learning and proposes a unified approach for optimizing the backward policy. This provides a robust theoretical basis for addressing the longstanding challenge of backward policy optimization in GFlowNets.

3. The paper is written in a clear and accessible manner, particularly in its detailed explanations of complex theoretical concepts, making it easier for readers to comprehend.

### Weaknesses
1. The paper primarily focuses on the introduction and validation of the TLM method, but provides limited discussion on comparisons with other backward policy methods, such as those proposed by Jang et al. and Mohammadpour et al. Notably, the improvement in backward policy optimization is not significant in more structured tasks, such as the sEH task.

2. While the paper demonstrates the advantages of the TLM method in complex environments, it does not sufficiently explore scenarios where TLM might underperform, particularly in simpler or highly structured tasks.

3. Some of the experimental environments, such as the sEH task, are relatively simple. Although the TLM method performs well in these tasks, validation in more complex or realistic environments would better illustrate the practical value of the approach.

4. Although the paper emphasizes the TLM method, exploring combinations with other backward policy approaches, such as maximum entropy policies, could offer more innovative directions for future research.

5. The paper could further discuss the impact of dynamic reward structures on the TLM method, particularly in handling complex, non-stationary reward distributions.

### Questions
1. The paper highlights the advantages of the TLM method in complex environments, but its performance is suboptimal in simpler environments, such as the sEH task. Can the reasons behind this underperformance in simpler tasks be explored in more depth? Is it due to limitations of the model or characteristics inherent to the environment?

2. The paper notes that TLM struggles to handle non-stationary rewards effectively. Could a variant of TLM be designed specifically for dynamic reward structures to address this issue? How would such an adaptation impact TLM's performance in non-stationary reward environments?

3. Maximum entropy policies are beneficial for enhancing exploration. Could the TLM method be combined with maximum entropy policies to improve exploration capabilities in certain tasks? If so, how might these two approaches be effectively integrated for optimal collaboration?

4. Could the TLM method be integrated with other types of reinforcement learning algorithms, such as hard-constrained RL, to address different task requirements? Would such a combination further improve backward policy optimization and overall performance?

### Soundness
3

### Presentation
3

### Contribution
2
