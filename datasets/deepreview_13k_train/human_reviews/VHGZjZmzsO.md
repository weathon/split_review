# Memory-Enhanced Neural Solvers for Efficient Adaptation in Combinatorial Optimization

- Decision: Reject
- Scores: 3, 3, 5, 3

## Abstract
Combinatorial Optimization is crucial to numerous real-world applications, yet still presents challenges due to its (NP-)hard nature. Amongst existing approaches, heuristics often offer the best trade-off between quality and scalability, making them suitable for industrial use. While Reinforcement Learning (RL) offers a flexible framework for designing heuristics, its adoption over handcrafted heuristics remains incomplete within industrial solvers. Existing learned methods still lack the ability to adapt to specific instances and fully leverage the available computational budget. The current best methods either rely on a collection of pre-trained policies, or on data-inefficient fine-tuning; hence failing to fully utilize newly available information within the constraints of the budget. In response, we present MEMENTO, an approach that leverages memory to improve the adaptation of neural solvers at inference time. MEMENTO enables updating the action distribution dynamically based on the outcome of previous decisions. We validate its effectiveness on benchmark problems, in particular Traveling Salesman and Capacitated Vehicle Routing, demonstrating its superiority over tree-search and policy-gradient fine-tuning; and showing it can be zero-shot combined with diversity-based solvers. We successfully train all RL auto-regressive solvers on large instances, and show that MEMENTO can scale and is data-efficient. Overall, MEMENTO enables to push the state-of-the-art on \num{11} out of \num{12} evaluated tasks.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes a method (MEMENTO) for online fine-tuning of neural CO models. More concretely, MEMENTO learns the rules for updating the policy parameters at inference time. This is achieved by leveraging a learned residual policy for the base policy, where this residual policy utilizes the past solution predictions to explore the search space. Through experiments on the TSP and the CVRP, the paper demonstrates MEMENTO's efficacy against baseline methods.

### Strengths
- The paper conveys most of the ideas clearly.
- The idea of leveraging a learned residual policy for online fine-tuning of the base policy at inference time is interesting and novel.

### Weaknesses
 - MEMENTO prevents the retrieval step from being too costly by only collecting data from the same node we are currently in. Could the authors elaborate on why this is a good retrieval strategy? Information should somehow be retrieved based on the partial solution constructed, since node-level decisions could be vastly different depending on the overall solutions. The current approach seems overly simplistic and may not capture the nuances of the search space effectively. It's unclear how this node-specific retrieval can generalize across different problem instances or even within the same instance as the solution evolves.
- The experiments do not use augmentation with symmetries in the experiments, which they claim to be not critical by citing just one prior work (COMPASS). Overall, to claim that MEMENTO outperforms EAS, the authors should compare it against EAS with augmentation enabled since EAS has been shown to work better that way. The justification for omitting augmentation based on a single citation is weak, especially given the established benefits of augmentation in similar contexts. The lack of augmentation makes it difficult to assess the true potential of MEMENTO against a fully optimized EAS baseline.
- My main concern with this paper is regarding the runtime of different methods in the experiments (which aren't reported for the major experiments in the main paper and put in the appendices instead). In Appendix A.1, the authors clarify that they report the runtime to solve one instance rather than the entire dataset. Given this, the comparison is fair only if they give each algorithm the same amount of runtime. However, Table 2 in the appendices shows that MEMENTO takes more than 2x the runtime than COMPASS (more than 4x for CVPR-100). The runtime is significantly higher than that for EAS as well (more than 2x) for CVRP-100. This raises serious questions about the practical applicability of MEMENTO, especially if it requires significantly more computational resources to achieve comparable or slightly better results.
- The paper makes a few incorrect statements or claims:
         1. In the definition of $\pi^\star$ on Page 3, if we are taking a max over $i$, why does $i$ appear in the outer expectation? This appears to be a notational inconsistency that needs to be addressed for clarity.
         2. The claim that MEMENTO at least learns the REINFORCE update in the worst case is not exactly correct. In the worst case, the residual policy could output random values. I think the authors wanted to claim that the residual policy has the ability to at least learn the REINFORCE update rule (if nothing better). The current phrasing is misleading and needs to be revised to accurately reflect the capabilities of the residual policy.
        3. The paper claims that MEMENTO  is "designed" to be agnostic to the base policy. While the authors demonstrate empirically that the learned residual policy for POMO could be used with COMPASS, the design of the framework as such makes the residual policy very much dependent on the base policy since they're learned jointly. The claim of base policy agnosticism is overstated, given the joint training procedure.

### Questions
1. Could the authors suggest alternative strategies for retrieval that do consider the partial solution constructed?
2. Could the authors report the results with augmentation enabled?
3. Could the authors report the results with the same runtime allocated to each algorithm in the experiments?

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
This paper introduces a fine-tuning method applied during inference to enhance construction methods for combinatorial optimization. It stores historical trajectories from fine-tuning as memory, which is processed by an MLP to adjust the original action probabilities. New solutions are then sampled from this memory-augmented distribution. The pretrained model and memory network are updated using an improvement reward based on the difference between the current solutions and the best-so-far solutions. Experiments are conducted on TSP and CVRP with problem sizes of 100 (generalizing to 125, 150, and 200) and 500.

### Strengths
1. The source code is provided.
2. This work has the potential to enhance the pre-trained construction methods for TSP and CVRP.
3. The idea of reusing the historical trajectories (i.e. the memory) is interesting.

### Weaknesses
1. Marginal Improvement: The improvement of MEMENTO over EAS appears marginal, especially when generalizing to larger scales (e.g., TSP200 in Figure 3). In the CVRP results, the improvement of MEMENTO is also not significant. The gains, while present, are not substantial enough to justify the added complexity, particularly when considering the computational cost. The reported improvements are close to the performance of EAS, raising questions about the practical significance of the proposed method.
2. Scalability Concerns: In the larger-scale experiment (n=500), MEMENTO only slightly outperforms COMPASS, while introducing higher computational overhead. The computational cost seems to outweigh the marginal performance gains, making it less appealing for large-scale problem instances. The method's scalability is questionable, as the performance difference with COMPASS is minimal, and the added overhead makes it less practical.
3. Incomplete Literature Review: The literature review lacks coverage of works focused on scalability and generalization. There is a need to include works that specifically address the challenges of scaling neural combinatorial optimization methods and their generalization capabilities to different problem distributions and sizes.
4. High Computational Cost of Fine-Tuning: The proposed fine-tuning method introduces additional computational overhead. The fine-tuning process adds a significant computational burden, which is a major concern for practical applications, especially when compared to methods that do not require such extensive fine-tuning.
5. Missing Generalization Experiments: Would be useful to add some generalization experiments on different distributions. The experiments are limited to the standard TSP and CVRP benchmarks, and it would be beneficial to see how the method performs on different problem distributions to assess its robustness.
6. Writing Quality: The writing lacks logical flow, and the table formatting needs improvement. The presentation of the results and the overall structure of the paper could be improved to enhance readability and logical flow. The tables are not well-formatted, making it difficult to extract key information.

### Questions
1. Why does POMO with sampling strategies perform worse than POMO with the greedy rollout when generalizing to N=200 in Figure 3?
2. Would it be feasible to apply MEMENTO to improvement methods as well? If so, are there any considerations that would impact its performance?
3. What's the inference time of the methods displayed in Figure 3? The bar chart results seem to replicate those in the table on the left, making it feel a bit redundant
4. Can MEMENTO be applied to other COPs? For example, I noticed that the code includes a preliminary implementation for the Knapsack Problem. I’d be interested to see the results and understand how MEMENTO might extend to different COPs.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes MEMENTO, a method for fast instance-specific adaptation in CO problems when a certain budget is allowed by utilizing a memory module. The proposed memory module is a lookup table storing information encountered during the online search process that is important for decision-making, such as the outcome of certain actions. This is then fed into an MLP, whose output modifies the action probabilities at each step. The method is evaluated in standard routing problems TSP and CVRP up to 500 nodes where it demonstrates SOTA results against RL-trained autoregressive solvers for CO.

### Strengths
1. The paper is very well written and clear with relevant citations to previous literature.
    
2. The proposed MEMENTO module is novel and simple enough to be applied to a range of autoregressive CO solvers in the future, and thus, I believe it is an available addition to the NCO community.
    
3. Good overall performance (albeit with some concerns about baselines below) and experimental validation, including classical benchmarking, zero-shot combination with new solvers, and scaling to large sizes.
    
4. Code is provided, and authors make an effort to make their checkpoints available to the community.

### Weaknesses
1. My biggest concern is about fairness in comparison with EAS. In particular, the values reported in the paper are worse than the ones in the original paper. For instance, for the Kool et al. (2019) 10k instances with 100 nodes, the value reported is 7.778 vs the original 7.769 for the TSP (MEMENTO: 7.768) and 15.66 vs 15.63 for the CVRP (MEMENTO: 15.65). Compared to the values reported in the original paper, MEMENTO would be worse than EAS. This holds true at larger sizes too. Do the authors have an explanation for this?

2. MEMENTO is only applied to routing problems despite the title appealing to a broader “Combinatorial Optimization”. In this sense, experimenting with differently structured environments such as the Job Shop Scheduling (JSSP) as done in COMPASS and EAS would be beneficial.

3. When computing gaps, it would be best to do so compared to SOTA heuristic methods. For instance: in Figure 7, in Table (b), only LKH3 is reported, while HGS is much more powerful on CVRP. However, the authors do report HGS in the appendix, which obtains much better solutions than LKH. This also applies in particular to Table 1, where the “optimality gap” appears to be negative.

4. Given that only routing problems are considered in this paper, it would be beneficial to mention the additional work [1].

5. Some questions regarding hyperparameters remain, see below questions.

### Questions
1. What is the impact of the MLP in terms of cost? Since this has to be called each time, I wonder whether similar results could be obtained with a simple linear layer as well.
    
2. In Figure 2: MEMENTO’s logit update encourages with higher amplitude high-reward actions rather than low-return ones. Is this due to the `ReLU` applied to the reward, constraining it to be strictly positive? I wonder if this analysis would hold without such constraint.

3. Can your method be applied to broader problems that include e.g. edge features as the JSSP?
    
4. What is the impact of the memory size? Would increasing it be beneficial?

5. MEMENTO appears to be >$2\times$ slower than EAS at larger sizes as seen in Appendix A.1. Would EAS, provided with as much time budget as MEMENTO, eventually surpass the latter?

### Soundness
2

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces MEMENTO, a novel memory-based approach designed to enhance existing constructive solvers for combinatorial optimization problems. MEMENTO leverages information from past solution attempts to improve the construction process, using a multilayer perceptron (MLP) network that takes features such as past actions, log-likelihood, and remaining search budget as input. This information is used to adjust the solution generation policy during inference, leading to higher-quality solutions within the given computational budget. The authors demonstrate that MEMENTO can improve the performance of base constructive models like POMO or COMPASS on problems such as the Traveling Salesman Problem (TSP) and Capacitated Vehicle Routing Problem (CVRP).

### Strengths
Adapting the solution generation process using memory to account for previous attempts is undoubtedly a valuable and significant research direction.

### Weaknesses
This paper introduces a 'meta-learning' approach in building solvers for combinatorial optimization problems, structured around two levels of machine learning. The lower-level learning takes place during inference, where previous solution attempts stored in memory are used to update the node selection policy. The upper-level (meta) learning, referred to as 'training' in the paper, involves training a multilayer perceptron (MLP) to find the optimal parameters that shape the behavior of the lower-level learning.

For the lower-level learning, I find the proposed method overly simplistic, with two primary issues.

First, the method indiscriminately utilizes all data in memory associated with the current node. Past experiences at the same 'current node' should not automatically be considered as occurring in the same 'state.' Although I haven’t thoroughly verified this, I believe the current implementation doesn’t necessitate storing the entire raw history. Instead, it could maintain only the accumulated 'logit correction values' and update them as new data arrives. In this sense, the term 'memory' may be too generous for the proposed approach, which feels closer to a simple bookkeeping method (EAS-tab) or basic active learning, both of which adjust the policy after each trajectory rollout iteration. A more effective memory system would incorporate mechanisms to retrieve the most relevant and important data while discarding irrelevant or potentially harmful data.

Second, the input features chosen for learning appear somewhat arbitrary. While the inclusion of the 'budget' feature is a helpful addition, many of the other features seem to offer limited value (as shown in Figure 9), and there is no clear theoretical basis for their usefulness. Moreover, generalizing these features to other combinatorial problems beyond fixed-sized routing may prove challenging.

Regarding the upper-level learning, the authors should provide a more precise and detailed explanation of their meta-learning approach, as applying meta-learning to combinatorial problems is an especially difficult task. To find a globally optimal solution using a reinforcement learning (RL) approach, an end-to-end method may be more suitable than optimizing over a few grouped trajectories, as done in this paper. To partly address this limitation, the authors manually adjust the learning process by logarithmically increasing the loss weight. An effectively designed RL approach would ideally discover optimal weights autonomously, eliminating the need for manual adjustments.

In addition to these concerns, the proposed method yields only marginal improvements over other baselines. Consequently, I believe the paper does not meet the high standards of ICLR.

### Questions
I would like to understand the MLP structure used by the authors, described in Table 4.

Does "memory size 40, number of layers 2, hidden layers 8" imply the following MLP structure?

1) An input layer with 40 neurons
2) A first hidden layer with 8 neurons
3) A second hidden layer with 8 neurons
4) An output layer with 1 neuron

### Soundness
2

### Presentation
3

### Contribution
2
