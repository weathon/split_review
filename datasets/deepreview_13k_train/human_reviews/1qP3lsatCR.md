# NetMoE: Accelerating MoE Training through Dynamic Sample Placement

- Decision: Accept
- Scores: 8, 8, 6, 8, 6

## Abstract
Mixture of Experts (MoE) is a widely used technique to expand model sizes for better model quality while maintaining the computation cost constant. In a nutshell, an MoE model consists of multiple experts in each model layer and routes the training tokens to only a fixed number of experts rather than all. In distributed training, as experts are distributed among different GPUs, All-to-All communication is necessary to exchange the training tokens among the GPUs after each time of expert routing. Due to the frequent and voluminous data exchanges, All-to-All communication has become a notable challenge to training efficiency.

In this paper, we manage to accelerate All-to-All communication in MoE models from the training sample perspective, which is unexplored so far. In particular, we put forward the observation that tokens in the same training sample have certain levels of locality in expert routing. Motivated by this, we develop \name, which takes such locality into account and dynamically rearranges the placement of training samples to minimize All-to-All communication costs. Specifically, we model the All-to-All communication given the sample placement and formulate an integer programming problem to deduce the optimal placement in polynomial time. Experiments with 32 GPUs show that NetMoE achieves a maximum efficiency improvement of $1.67 \times$ compared with state-of-the-art MoE training frameworks.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents NetMoE, a novel framework designed to optimize the routing of samples in Mixture of Experts (MoE) models by taking into account the actual inter an intro-node communication bandwidth. The goal is to minimize the *time* the routing process takes, which usually amount to minimize inter-node expert routing in the All-to-All communications, while being mathematically equivalent to the standard routing procedure. This paper formulates the problem as an integer linear programming optimization problem, and relaxes it so that an approximate solution can be found sufficiently fast dynamically at each stage of the MoE. Experimental results demonstrate that NetMoE outperforms existing MoE training systems, achieving up to a 1.67x speedup in training efficiency.

### Strengths
* **The problem is clearly motivated:** The challenges of routing samples in MoE are clearly written, making the goal of this paper feel natural after reading the first two sections.
* **Challenges of ILP solving are made clear, and the proposed solution seem effective:** The building to the final approximate method is clear and well motivated through empirical results in Tab.4. The optimization gap between the optimal and the approximate solution seem reasonable in Fig.6.
* **Non negligible empirical benefits of the method are demonstrated:** The speedup brought by NetMoE compared to Dynamic Expert Placement methods seem significant in the experiments displayed.

### Weaknesses
 * **Notations and problem formulation hard to follow:** Many notations are introduced, making the reading of section 3 a bit cumbersome. Maybe putting some of the mathematical details and ILP formulations in Appendix could help lighten the section and make it more readable?
* **No comparison with methods using a modification in the model definition:** While methods introduced in Sec. 2.2 change the convergence property of the model in terms of iterations, the fact that they allow for more iterations per time unit could counter this. Would it be possible to also compare NetMoE to these methods (e.g., in terms of *"time to reach a certain level of perplexity"*)?

**typo:** In table 1 *"number of of nodes"*.

### Questions
see Weaknesses.

**typo:** In table 1 *"number of of nodes"*.

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The whole idea of NetMoE is that we want to reduce the All-to-All scatter & gather communications by reducing the amount of cross-node/device routing of tokens. To achieve this we will adjust the sample/sequence that would minimize the inter-node & intra-node communication volume. This is (approximately) solvable as a weighted bipartite matching / assignment problem between training samples and machines, as shown in Eqn 9 and 10. 

The authors conduct experiments on GPT pretraining and compare with dynamic expert placement baselines as FasterMoE and SmartMoE. NetMoE generally has higher speedup (Figure 5) and the actual speedup is close to the theoretically optimal speedup (Figure 6).

### Strengths
1. The paper is well motivated and the writing is pretty clear. I have no difficulty on understanding the overall idea of sample adjustment (from Figure 2) and the optimization challenges & solutions (Equation 5, 8, 10) upon the first time of reading. 

2. Clever design: reformulating the ILP to a weighted bipartite matching / assignment problem and using Hungarian algorithm that has shorter solving time than communication time (so we can have actual speedup).

### Weaknesses
I don't have strong opposition to the overall idea of sequence adjustments for MoE but I believe the scope and limitations should be more clearly defined:

1. The authors should provide a summary statistics on how many sequences are actually adjusted across nodes/devices during training and how it is correlated with the MoE specialization / router probability. 

2. A small-scaled ablation experiment is definitely needed to show if this communication volume reduction is robust w.r.t. the choice of dataset mixtures, as the performance of NetMoE might be data dependent.

3. Table 4 is concerning because the limit of KM algorithm to use less time than all-scatter is $I/J \sim 24$ (24 is my scaling extrapolation of Table 4's $I/J = 16$ results as KM's time complexity scales cubically w.r.t. # nodes, and $(24/16)^3 * 1 > (24/16) * 2$). A batch size of 24 per device is not a sufficiently large number.

### Questions
1. The sequence adjustment is done per iteration and per layer and composable of reducing the all-gather communication of this layer and all-scatter of next-layer (Eqn. 7). The reduction from all-gather is clear, but I don't understand how it is even possible to reduce the all-scatter costs of *next-layer* as we even don't know what is the routing probability due to an attention block before the MoE. 

2. I don't understand how does expert inline residual fix the position issues of residual stream (it might be helpful to give a diagram as line 12 in Algorithm 1 is not sufficiently clear)

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
This paper proposes to use a dynamic sample placement to speed up the MoE training. Specifically, this paper adopts a mathematical model to simulate the number of inter-node communication and intra-node communication and solve the integer programming problem to figure out the best sample allocation of the sample to reduce inter-node communication inspired by the locality in networks. This paper successfully reduces the all2all gather communication in training and achieve speed up.

### Strengths
1. This paper tackles the MoE training efficiency from a novel perspective, that is the data locality perspective. It dynamically locates the data to reduce the inter-node communication in all2all gathering. 
2. The results shows improvements compared with baselines, signifying the effectiveness of the method.
3. The modeling of the networking problem is inspiring to the reviewer.

### Weaknesses
1. The scalability of the method is questionable, e.g., the improvements for 32 GPUs is smaller then the improvements for 16 GPUs. This leads to the question that what will happen if we continue increasing the number of GPUs? Will the improve converges to zero? 
2. When there are more GPUs, the communication should take a larger portion in the total time? Why the method here, which primarily focuses on optimizing communication, have less significant improvements.

Moving the sample should incurs more movements compared a subset of the tokens in the sample. Why moving sample gives less communication overhead?

### Questions
See Weaknesses. And

Moving the sample should incurs more movements compared a subset of the tokens in the sample. Why moving sample gives less communication overhead?

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
The paper proposes a topology-aware sample placement scheduling approach to optimize All-to-All communication in MoE training.

### Strengths
•	Theoretical Rigor: This paper is thorough in formulating the communication challenges and solution as an optimization problem, with clear problem modeling and a detailed, polynomial-time solution.

•	Practicality: The method can integrate with existing MoE training systems while enhancing training efficiency.

•	Empirical Validation: Experimental results across various configurations validate NetMoE’s improvements in All-to-All communication and overall training efficiency.

### Weaknesses
•	Experimental Context: The paper could benefit from a more comprehensive discussion on the "data locality" conditions required to achieve the claimed speedups in real-world setups. Also, details on the distribution of data locality across real-world training tasks (and the one used in experiment) would give more insight into NetMoE's practical performance.

•	Discussion on Experiment Setup: Given that inter-node expert parallelism can incur heavy communication costs, it would help if the authors provided reasoning for prioritizing inter-node expert parallelism over potentially less intensive techniques like a hybrid one: intra-node expert parallelism + inter-node pipeline parallelism. 

•	More Baseline Comparisons: Additional baselines, particularly concerning dynamic expert placement, would highlight NetMoE’s comparative advantages and limitations.

### Questions
•	How does the data locality used in the experiment compare to typical training scenarios, and what impact might this have on expected performance?

•	Why is inter-node expert parallelism favored over pipeline or other model parallelism techniques in this context?

•	Is an auxiliary loss mechanism incorporated to mitigate expert selection skew, and if so, does it affect the performance of NetMoE?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
Communication efficiency is a significant challenge for training efficiency in distributed Mixture of Experts (MoE) models. Unlike other papers that address this issue from a model perspective, this paper offers a solution from a data perspective. It introduces NetMoE, a method that reassigns data samples to different nodes based on locality to minimize all-to-all communication costs. The problem is formulated as an integer programming problem, and the authors derive a polynomial-time solution. Experimental results further validate the effectiveness of their approach.

### Strengths
1. The author demonstrates strong writing skills, clearly stating the problem and solution. The system diagram is also very clear.
2. They offer a new perspective on communication efficiency in distributed MoE by exploring how data placement can impact efficiency.
3. Experiments are provided to validate the effectiveness of their approach.

### Weaknesses
1. The motivation is not clearly articulated. In the motivation section, the authors mention that previous works focus on the model perspective and do not explore the data perspective, which does not convey the true motivation. Instead, it should emphasize that in certain scenarios, the model perspective may be insufficient, while a data-focused approach can achieve better efficiency.

2. The problem formulation and subsequent assumptions appear contradictory and I suspect the effectiveness of method. In Equation (1), the communication cost is defined as the maximum of intra-node and inter-node costs. However, in Section 3.2, the authors assume the maximum is the inter-node cost and address it first. This raises questions for the reviewer: if the inter-node assignment is fixed but minimizing intra-node communication results in a higher total cost than inter-node, this may lead an undesirable solution.

3. The authors transform this problem into a weighted bipartite matching problem and solve it using the Kuhn-Munkres (KM) algorithm. However, based on the reviewer's knowledge, KM is sensitive to the sample input and has a time complexity of 
O(N^3) which may not be ideal for large models. The authors should justify their choice of KM as the solver.

4. The experiments do not fully validate the approach. The impact of node and device count on performance is not examined. For instance, if there are very few devices in each node but many nodes overall, inter-node communication may dominate the time. Conversely, if there are numerous devices within fewer nodes, intra-node communication could become the dominant factor in training time.

### Questions
Same as Weaknesses.
Q1. In what scenarios would one choose a data perspective approach over a model perspective approach?

Q2. Please revise your solution to ensure it aligns with the stated assumptions.

Q3. Explain why the Kuhn-Munkres (KM) algorithm with highest time complexity is the best choice for this problem.

Q4. Conduct additional experiments to demonstrate the impact of node and device variables on performance.

### Soundness
3

### Presentation
3

### Contribution
3
