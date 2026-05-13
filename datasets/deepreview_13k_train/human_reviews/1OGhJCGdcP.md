# Learning subgoal representations from state graphs in goal-conditioned hierarchical reinforcement learning

- Decision: Reject
- Scores: 3, 3, 3, 5

## Abstract
The integration of graphs with Goal-conditioned Hierarchical Reinforcement Learning (GCHRL) has recently gained attention, as the intermediate goals (subgoals) can be effectively sampled from graphs that naturally represent the overall task structure in most RL tasks. However, some 
existing approaches often rely on domain-specific knowledge to construct these graphs, limiting their applicability to new tasks. 
Other graph-based approaches create graphs dynamically during exploration but struggle to fully utilize them because they have problems passing the information in the graphs to newly visited states. 
Additionally, current GCHRL methods face challenges such as sample inefficiency and poor subgoal representations. In this paper, we present a solution to these issues through the development of a graph encoder-decoder that can evaluate unseen states. 
Our proposed method, Graph-Guided sub-Goal representation Generation RL (G4RL), can be incorporated into any existing GCHRL method to enhance performance. 
We show that the graph encoder-decoder can be effectively implemented using a network trained on the state graph generated during exploration. Empirical results indicate that leveraging high and low-level intrinsic rewards from the graph encoder-decoder significantly enhances the performance of state-of-the-art GCHRL approaches in both dense and sparse reward environments.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper presents a novel approach—Graph-Guided sub-Goal representation Generation RL (G4RL)—aimed at addressing several key issues faced by existing Goal-conditioned Hierarchical Reinforcement Learning (GCHRL) methods, including sample inefficiency and poor subgoal representations. By introducing a graph encoder-decoder architecture, G4RL effectively leverages the state graph generated during exploration to enhance the performance of existing GCHRL methods. Empirical results demonstrate performance improvements in both dense and sparse reward environments.

### Strengths
1.	Innovation: The introduction of a graph encoder-decoder offers a novel perspective on GCHRL, facilitating the online construction of state graphs that yield more effective subgoal representations.
2.	Generalizability: G4RL can be integrated into any existing GCHRL algorithm, making it versatile and applicable across various contexts.

### Weaknesses
1.	Increased Complexity: Although the graph encoder-decoder adds new functionality, the added complexity does not yield a substantial performance improvement over existing HRAC methods. This raises concerns about implementation and debugging challenges without corresponding benefits.
2.	Insufficient Comparisons: The paper lacks comparisons with several recent GCHRL methods, which limits the assessment of the proposed approach's advancements and advantages over established techniques.

### Questions
1. Complexity Management: How do the authors plan to manage the increased complexity introduced by the graph encoder-decoder in practical applications? Are there any proposed strategies to simplify the implementation while retaining performance benefits?
2. Comparison Metrics: What specific metrics do the authors plan to use in future work to compare G4RL against recent GCHRL methods? Will they consider not only performance but also computational efficiency of integration?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper focuses on Goal-conditioned Hierarchical Reinforcement Learning (GCHRL) setting and introduces a graph encoder-decoder that can evaluate unseen states and enhance performance. This encoder-decoder can be trained on data generated during exploration, and by leveraging the high and low-level intrinsic rewards from the graph encoder-decoder improves performance.

### Strengths
1. The paper focuses on an important problem of integrating graphs with Goal-conditioned Hierarchical Reinforcement Learning and improving performance.
2. The work provides a good motivation for the research problem and its importance.

### Weaknesses
1. The paper can benefit from improving the writing and cleaning up the list of their contributions.
2. The set of environments / task settings is limited and it would be beneficial to add more tasks.
3. In some results, the methods are pretty similar. Running more seeds or increasing the difficulty of the experiments could be useful to pull the methods apart.

### Questions
1. The settings and environments considered in the experiments are relatively simple. How does the method scale up?
2. How sensitive is the method to the value of K : the number of timesteps used by the high-level policy to propose a goal? Is it same across different tasks?
3. How many seeds were used for the experiments and how were they chosen?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
This paper presents a novel graph encoder-decoder approach designed to evaluate previously unseen states, which can be integrated with existing GCHRL (Graph-based Hierarchical Reinforcement Learning) methods. The proposed model is trained on state graphs generated during exploration, and the authors demonstrate its effectiveness through empirical evaluation. Results indicate improved performance in both dense and sparse reward environments, driven by multi-level intrinsic rewards derived from the graph encoder-decoder.

### Strengths
* The paper is clearly written and easy to follow.
* The proposed method improves upon baseline methods in the AntMaze and AntGather tasks.

### Weaknesses
* The proposed method does not function as a subgoal representation learning approach but rather predicts state affinity.
* The paper lacks strong positioning within the subgoal representation learning literature. It cites only one relevant work and does not provide adequate motivation or comparison with existing methods in this area.
* The method (G4RL) shares significant similarities with HRAC, raising several concerns: 1. G4RL constructs graphs by hard-thresholding distances in state feature space, while HRAC uses K-step affinity along trajectories. As a result, G4RL is both feature- and hyperparameter-dependent, introducing limitations. 2. HRAC applies a contrastive loss to ensure that the learned subgoal space adheres to a K-step adjacency constraint while preventing subgoals from being too close. How does G4RL regularize representation learning in the latent space? 3. What is the rationale behind combining G4RL with HRAC (i.e., HRAC-G4RL)? Does G4RL require HRAC's regularization in the latent space?
* The evaluation is limited in several respects: 1. The method is only tested on the AntMaze and AntGather tasks. 2. It is only compared to two pre-2020 methods, HIRO and HRAC, without including more recent subgoal representation learning methods such as LESSON, HESS, and HLPS.
* There is insufficient analysis of the method's sensitivity to hyperparameters, such as how \epsilon depends on the environment and state space features.

### Questions
Please address my questions in the weakness section

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a novel architecture that employs a graph encoder-decoder to summarize spatial information into subgoal representations and constructs a world model based on the state graph for the agent to generate auxiliary rewards in both the high-level and low-level policies.

### Strengths
The paper introduces the G4RL approach with a degree of originality, and the presentation is clear, effectively explaining the proposed method in a way that is easy to follow.

### Weaknesses
- The primary experiments are conducted in a limited range of environments.
- The ablation studies are insufficient, lacking a comprehensive analysis of key parameters such as $\epsilon_{d}$, $\alpha_{h}$, $\alpha_{l}$, and $N$. The existing experimental results do not adequately support the significance of these parameters as stated in the methods section.
- There is no comparison with other representation methods to demonstrate the advantages or disadvantages.
- The learned world model is influenced by the current policy distribution, and it may not accurately reflect the actual world model.

### Questions
- How is the state representation function $\phi$ implemented? For example, is it based on neural networks or dimensionality reduction? Please provide specific details of the implementation.    
- What impact do the values of $\epsilon_{d}$ and parameters $\alpha_{h}$, $\alpha_{l}$, and $N$ have on the algorithm's performance?    
- Can it be qualitatively or quantitatively demonstrated that the graph encoder-decoder effectively extracts spatial information?    
- Has the representation of subgoal spatial distance been compared with other methods, such as [1]? Does it show advantages over these approaches?

If the author can address the aforementioned weaknesses and questions, I will consider increasing the score.

[1]Park, Seohong, Tobias Kreiman, and Sergey Levine. "Foundation Policies with Hilbert Representations." Forty-first International Conference on Machine Learning.

### Soundness
2

### Presentation
3

### Contribution
2
