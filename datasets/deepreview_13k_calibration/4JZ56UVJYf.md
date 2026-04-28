# CocoRNA: Collective RNA Design with Cooperative Multi-agent Reinforcement Learning

- Decision: Reject
- Avg Score: 4.75
- Scores: 3, 5, 6, 5

## Abstract
Ribonucleic acid (RNA) plays a crucial role in various biological functions, and designing sequences that reliably fold into specified structures remains a significant challenge in computational biology. Existing methods often struggle with efficiency and scalability, as they require extensive search or optimization to tackle this complex combinatorial problem. In this paper, we propose CocoRNA, a collective RNA design method using cooperative multi-agent reinforcement learning, for the RNA secondary structure design problem. CocoRNA decomposes the RNA design task into multiple sub-tasks, which are assigned to multiple agents to solve collaboratively, alleviating the challenges of the curse of dimensionality as well as the issues of sparse and delayed rewards. By employing a centralized Critic network and leveraging global information during training, we promote cooperation among agents, enabling the distributed policies to cooperatively optimize the joint objective, thereby resulting in a high-quality collective RNA design policy. The trained model is capable of completing RNA secondary structure design with less time and fewer steps, without requiring further training or search on new tasks. We evaluate CocoRNA on the Rfam dataset and the Eterna100 benchmark. Experimental results demonstrate that CocoRNA outperforms existing algorithms in terms of design time and success rate, highlighting its practicality and effectiveness.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper addresses the challenge of efficient and scalable RNA secondary structure design. Designing RNA sequences that reliably fold into specified structures is difficult due to the complexity of the combinatorial search space. The paper proposes a collective RNA design approach called CocoRNA which uses cooperative multi-agent reinforcement learning. CocoRNA designs RNA sequences by decomposing the design task into subtasks assigned to multiple agents.

### Strengths
- The paper presents an efficient RNA secondary structure design method using a collective design approach, with empirical evaluations provided on two RNA design benchmark datasets.
- The paper demonstrates the potential of cooperative MARL approaches to RNA design tasks.
- The proposed approach addresses a real-world problem, validated through experiments on real-world datasets.

### Weaknesses
1. The main contribution of the proposed method is presented as designing RNA secondary structure as a "collective design" problem. However, the contribution is not novel as the recent work [1] already introduces such a collective design idea, that is, efficiently designing biological sequences using cooperative design framed as a cooperative game between players (here it is called agents), and [1] should be cited in the relevant work section. Based on this, it should be further clarified that what is the main source of benefit of using a MARL method, instead of performing collective design directly using combinatorial optimization as in [1]? What are the key differences and advantages of your method over [1]?

2. The paper lacks a discussion or a theoretical analysis of the convergence of the distributed policies to the global optimum. In the abstract and also in lines 126-129, it is stated that CocoRNA enables such a convergence, however, there is no guarantee or analysis that supports this claim. I would suggest that either a theoretical analysis or some clear discussion/intuition should be provided in the paper or the claims should be modified.

3. It would support the empirical performance of CocoRNA better if an analysis of the performance of CocoRNA under sparse and delayed rewards is presented. Instead of using the reward function in equation (12), how would the performance change under sparse reward (e.g., $R_t$ = {$0$ if $H_t > 0$; $C$ otherwise})?

4. While motivating CocoRNA in the Introduction, the authors state that RL-based methods do not exploit learning to generalize across different target structures (line 62). CocoRNA is stated to mitigate problems of (1) the curse of dimensionality and (2) sparse rewards (although not supported enough for (2)). However, the paper does not present how CocoRNA generalizes across (3) different target structures.

5. I think the related work section (2.1) should be restructured. There should be a section for RL-based methods that are used to design biological sequences such as [4,5]. These are potential SOTA baselines for CocoRNA. In addition, a discussion on why MARL is needed over these RL methods would clarify the contribution within RL & biological sequence design context. Instead of providing general MARL works in detail, this section would have provided the flow from RL to MARL within the problem context.

6. An ablation study on the grouping of players would be helpful in showing the effectiveness of CocoRNA regarding the interdependence of nucleotides at different positions. The paper presents only agent per position (n many agents) analysis. How does the performance of CocoRNA change with respect to the agent size?

7. Different than the point above, an ablation study considering the decomposition scheme such as position + structure assigned to an agent would have shown the proposed method's flexibility regarding decomposition choices. This is a more specific decomposition than only structure-based decomposition.

8. Regarding Section 4.4, in Hindsight Experience Replay (HER), additional goals are used to store additional episodes in the replay buffer to deal with sparse reward environments. Hence, the goal influences actions, but not the environment dynamics. In Search-augmented Experience Replay (SAER), how are the goals defined? How are additional goals for the replay sampled? It is not clear to relate SAER to HER and not provide clear explanations.  I think to better motivate CocoRNA's sample efficiency and to build a better connection with HER, SAER should have experimented on a sparse reward environment.

9. The empirical evaluation is done against a limited amount (and type) of baselines. The proposed method is compared only against RL-based methods. The paper only cites antaRNA [2] and MCTS-RNA [3] approaches, however, these search-based fundamental approaches should be included as baselines; which would support CocoRNA's performance against a diverse set of baselines. Furthermore, another valid baseline from literature that combines RL with local search [3] could have been considered.

10. It would have supported the generalizability of the proposed approach better if an empirical analysis on any other biological sequence design domain such as protein design (which has some benchmark datasets e.g. GB1) was presented.

11. For a thorough analysis, training performance could have been provided. Further, an ablation over the trained policy (e.g. under different training steps or hyperparameters) could have demonstrated the effectiveness of CocoRNA under various training settings.

12. There is no clear discussion on the limitations and potential drawbacks of the method.

**Minor:**

- In line 114, the reference (Eastman et al…) is doubled. \cite{} should be corrected to avoid repetition.

- Regarding notations, instead of using the notation k for several places, another symbol could be used. Specifically, it is used both in equation (5) to denote the subsequence of nucleotides and in equations (7), (9) to denote cumulative future rewards.

### Questions
1. Why the proposed method is only applied to RNA design? Can the method be extended to any other biological sequence (DNA, protein, peptide) design? If yes, why restrict its applicability/generalization?

2.  As also stated in the first weakness, what is the main source of benefit of using an RL method, instead of performing collective design for combinatorial optimization as in [1]?

3. How does CocoRNA deal with sparse and/or delayed rewards?

4. How does CocoRNA generalize across different target structures?

5. How is SAER related to/inspired by HER? How the goals are sampled in SAER? How do you gradually reduce the SAER operation, this is not clear in the paper.

6. Can you provide some insight/discussion on how embedding SAER into the training process would not yield a suboptimal solution?

7. In Section 5.3 (and Figure 4), the two ablation studies are done on which dataset? Or is it averaged over replications or datasets-- what do error bars represent? It could have been clarified in the figure caption.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper tackles the RNA secondary structure design problem proposing a novel approach using cooperative multi-agent RL. Multiple policies are jointly trained to design the sequence for parts of the RNA structure and a centralized critic is used to maximize the reward of the entire final sequence. The authors show that this methodology improves sample efficiency and computational efficiency while improving over other traditional RL-based baselines.

### Strengths
1.	A novel and interesting MARL-based methodology is proposed for RNA secondary structure design.
2.	A search-based augmented experience replay technique is proposed inspired by HER.
3.	The use of multiple policies improves sample efficiency issues and, given enough computational resources, also improves computational efficiency.

### Weaknesses
1.	The framework is still model-based and relies on repeatedly applying folding algorithms for reward calculation.
2.	Using the position-based decomposition, it is hard to justify having different local policies and not a shared policy. At least an ablation seems needed for that.
3.	Given the current manuscript, it is hard for readers to reproduce it, code is not available, there are some details that need additional information, and the random dataset splits might leak data.

### Questions
1.	It is not clear to the reviewer what is the output of the actor network. Is it the nucleotide type for 1 position or for all positions associated with that agent?
2.	Is code available for the proposed algorithm at an anonymous link?
3.	The reviewer suggests adding the part highlighting the difference from how the experience replay is applied from Appendix A to the manuscript.
4.	The authors mention two possible decompositions: (i) position-based; (ii) structure-based. In the experiments section, it seems that only position-based is mentioned. Are structure-based decomposition results also shown in the manuscript?
5.	The proposed method is compared with other RL-based baselines. It would be interesting to compare the proposed method to the other generative-based model baseline (Patil et al, 2024) having a small comparison regarding success rates and discussing which sequences can't be predicted by the generative-based model baseline because of their sequence length.
6.	From the reviewer's understanding, with n=4, four individual policies are trained. In this scenario, would not be the case to use four shared policies during training (with shared weights). It would be interesting to also have this ablation study.
7.	For the experiments, a random split of the datasets was performed. Similarly to protein-related tasks, a split based on hamming distances of structures to check the generalization capabilities of the policies would be desired in the reviewer’s opinion.
8.	It would be interesting to discuss the trade-offs between the proposed methodology and other generative-based alternatives such as graph neural networks using graph-based representations. As other parts of the structure might also affect the design of the sequence, having partial observations might not give enough information even with a centralized critic. For this, using a GNN architecture for decoding or a GNN-based policy for the RL methodology could alleviate this issue.

### Soundness
2

### Presentation
2

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
This paper introduces a new approach for RNA secondary structure design by leveraging cooperative MARL. The proposed method, COCORNA, breaks down the RNA design task into multiple sub-tasks managed by individual agents. Through a centralized Critic and decentralized Actor architecture, COCORNA enables these agents to cooperate, aiming to address the combinatorial complexity of RNA sequence folding.

The model was trained on RNA design tasks using a novel Search-Augmented Experience Replay (SAER) mechanism, which improves initial learning efficiency. Experimental results on the Rfam and Eterna100-v2 datasets demonstrate that COCORNA outperforms existing methods in both design time and success rate, highlighting its potential for efficient and scalable RNA sequence design without further task-specific optimization. This study showcases COCORNA as a promising tool for addressing complex biological sequence design challenges through MARL.

### Strengths
1) **Significance of the Problem**: The paper tackles the complex challenge of RNA secondary structure design, which holds significant implications in fields like synthetic biology and gene regulation. By addressing the combinatorial nature of RNA design and the need for efficient, scalable methods, the authors provide a contribution to computational biology.

2) **Clear and Well-Structured Presentation**: The paper is well-organized, with each section logically progressing from the problem statement to methodology and experimental evaluation. The clear exposition of the multi-agent reinforcement learning framework, algorithmic details, and ablation studies makes it easy to understand both the innovation and the practical execution of the proposed approach.

3) **Robust Experimental Results**: The experimental results presented on the Rfam and Eterna100-v2 datasets are comprehensive and demonstrate COCORNA’s superior performance over existing methods in terms of success rate and design time. The ablation studies further substantiate the model's robustness, providing evidence that each component of the method contributes to the overall improvement.

4) **Intuitive and Effective Approach**: The proposed multi-agent reinforcement learning framework is well-suited to the complex, distributed nature of RNA design tasks. The decomposition of the design problem and the centralized training with decentralized execution approach provide a practical and computationally feasible solution. The inclusion of the SAER method to improve initial data quality and learning efficiency is a thoughtful addition that strengthens the model’s effectiveness in this challenging domain.

### Weaknesses
1) **Lack of Visual Aids for Method Explanation**: The paper lacks visual illustrations of the proposed method, which is a drawback given the complexity of multi-agent reinforcement learning and RNA secondary structure design. Effective diagrams and flowcharts could have greatly enhanced the readability and accessibility of the methodology, particularly for readers unfamiliar with MARL frameworks in biological sequence design. Including such visuals would improve the reader's ability to grasp the significance and innovative aspects of this work.

2) **Limited Novelty**: A significant concern lies in the limited novelty of the approach. The paper formulates RNA design as an MARL problem and primarily applies established MARL methods to solve it. The novelty of specific components, such as the reward function and the Search-Augmented Experience Replay (SAER) module, also seems limited. It would strengthen the work if the authors provided more innovative, task-specific adaptations or insights that build on existing methods in a unique way.

3) **Need for Deeper Conceptual Insights**: The paper would benefit from more in-depth conceptual insights into the unique challenges and opportunities specific to RNA design in the context of MARL. For instance, an analysis of how different decomposition approaches (e.g., position-based vs. structure-type-based) impact learning, or a discussion on task-specific challenges in RNA sequence alignment, would offer valuable perspectives. Such insights could highlight the authors’ deep understanding of the problem and provide a stronger foundation for the applicability and potential extensions of COCORNA.

### Questions
please see weaknesses.

### Soundness
2

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
This paper presents a novel collective RNA design method based on cooperative MARL to solve the RNA secondary structure design problem. Empirical results demonstrate the outperformance of the proposed method.

### Strengths
The authors efficiently decompose the complex RNA design problem into mutiple sub-tasks. These tasks are allocated to cooperative agents to solve collaboratively. They introduce a search-augmented experience replay method to improve learning
efficiency, which improves the efficiency of RNA design. The proposed method significantly outperforms existing methods in terms of both design time and success rate.

### Weaknesses
1. This paper is more like an application of MARL in RNA design. The contributions to MARL method to solve the specific issues when applying MARL in RNA design should be stated clearly.
2. Besides the design of observations and reward functions, the authors should provide more explanations on how the agents cooperatively to sovle the RNA design task. 
3. The authors do not discuss the limitations of the proposed method.

### Questions
See the weaknessnes above.

### Soundness
3

### Presentation
3

### Contribution
2
