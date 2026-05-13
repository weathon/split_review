# DyGNeX : Efficient Distributed Training of Dynamic Graph Neural Networks with Cross-Time-Window Scheduling

- Decision: Reject
- Scores: 6, 6, 3, 5, 3, 3

## Abstract
Dynamic Graph Neural Networks (DGNNs) are advanced methods for processing evolving graph data, capturing both structural and temporal dependencies efficiently. However, existing distributed DGNN training methods face challenges in achieving load balance across GPUs and minimizing communication overhead, which limits their efficiency.  In this paper, we introduce DyGNeX, a distributed training system designed to address this issue. DyGNeX utilizes a cross-time-window snapshot group scheduling algorithm that balances computational loads across GPUs without introducing additional cross-GPU feature aggregation or hidden state communication. Based on the specific scenario, the scheduling algorithm is applied using greedy or Integer Linear Programming (ILP) methods, referred to as DyGNeX-G and DyGNeX-L, respectively. DyGNeX-L and DyGNeX-G achieve average reductions of 28\% and 24\% in per-epoch training time compared to state-of-the-art methods, maintaining load imbalance across GPUs at approximately 4\% and 8\%, while preserving model convergence across various DGNN models and datasets. In simulation experiments, as the number of GPUs increases, DyGNeX-G shows good scalability, efficiently handling clusters with up to 512 GPUs while maintaining 95\% efficiency.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
DyGNeX is a distributed training system for dynamic GNN. It achieves minimal communication and balanced workload. 
- To achieve (1), data parallelism is adopted so that only model weights/gradients need to be synchrnoized
- To achieve (2), workload distribution is formulated and is optimized via ILP.

### Strengths
- This paper studies an important research topic
- The system-level performance is promising.
- Experimental results show that DyGNeX boosts the efficiency of 4 popular dynamic GNN architecture.

### Weaknesses
 - Insufficient experiments.

 - My major concern is the test accuracy of the proposed method. Only one dataset is used for evaluating accuracy. It's not clear whether the proposed method hurts model performance significantly.

 - Memory consumption of DyGNeX is not reported. However, this overhead might be significant as all node features are stored in each GPU (line 104).

### Questions
- My major concern is the test accuracy of the proposed method. Only one dataset is used for evaluating accuracy. It's not clear whether the proposed method hurts model performance significantly.
- Memory consumption of DyGNeX is not reported. However, this overhead might be significant as all node features are stored in each GPU (line 104).

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This work describes a method, DYGNEX, to improve the load balance and reduce the communication overhead of dynamic GNN training by distributing group-based snapshots of tasks between a collection of compute resources. DYGENEX first measures the training time required by each task then dynamically combines tasks for different time windows to improve load balance across all compute resources. The task groupings are computing using two different strategies, the first utilizes integer linear programming solvers to find a near-optimal assignment, at the expense of longer latency to find a solution, and a greedy method that finds a reasonable solution but not optimal considerably faster. Support for the performance of DYGNEX compared to other methods is provided in the evaluation section for different architectures, datasets, and data-partitioning strategies. The ILP solver reduces the training time per epoch considerably across different architectures and datasets while the greedy method outperforms competing methods but still underperforms the ILP approach. The merits of the greedy approach are analyzed using a distributed simulation for a larger cluster of devices where the time to compute the solution in the ILP approach becomes prohibitively expensive.

### Strengths
- The proposed method outperforms comparable approaches for a range of different architectures, datasets, and data-partitioning approaches. The evaluation of the methods across all these hyperparameters is sufficient to draw out the novelty and innovations of the proposed method and the additional notes in the Appendix help to clarify some of the details missing in the main body of the text. 
- The tradeoff between the ILP and greedy methods is an interesting comparison and highlights the overhead associated with the near-optimal ILP solution and a greedy alternative. Table 3 is especially interesting for comparing the proposed method to previous approaches and between the 2 variations described in the text.
- The main text, along with the Appendix, is generally well-written and provides enough details to follow the implementation of the analysis of DYGNEX.

### Weaknesses
 - While the gains compared to ESDG and BLAD are substantial the improvement compared with PSG is marginal in many cases, especially in comparison with the greedy variation.
- The ILP solver is computationally expensive but it is unclear if loosening the optimality constraint would allow the solver to work faster and achieve results on par or better than the greedy variation. It may be beneficial to provide a cost analysis of the ILP solver vs the greedy variation as the optimality constraint is increased from 1% to 10%.
- The use of a simulator instead of the actual runs is not ideal but does provide sufficient evidence that the ILP solve time and complexity would grow prohibitively with the number of compute resources.

### Questions
- How does varying the number of snapshots impact the training time per epoch and the task scheduling overhead? It seems to be fixed at 30 in section 4.3.
- How quickly does the dynamic connectivity of the graph change between epochs? I wonder if starting from a solution in a previous epoch would be informative to seed the solution in the current epoch and lower the time to compute a solution.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
The authors introduce DYGNEX, a distributed graph neural network (GNN) training system designed to address the issue of  inefficient resource utilization across GPUs.
DYGNEX utilizes a cross-timewindow snapshot group scheduling algorithm that balances computational loads.
They integrate the scheduling algorithm into DYGNEX based on the specific scenario,  using greedy or Integer Linear Programming (ILP) methods.
From the evaluation, DYGNEX achieves an impressive performance in per-epoch training compared to ESDG, BLAD, and PSG, while preserving model convergence across various DGNN models and datasets. 
In conclusion, the paper presents a novel distributed dynamic GNN training system, that could help us better understand the challenges coming from load balance across GPUs and inter-GPU communication.

### Strengths
* Scheduling DGNN snapshot groups from different time windows using Integer Linear Programming (ILP) or a greedy algorithm is an interesting idea. This approach effectively solve the load balance and inter-GPU communication problem, making it an intuitive and efficient solution.
* The paper has good coherence, and is well-structured. 
* The paper is also very clear with thorough experiments and analysis.

### Weaknesses
 * The primary optimization objective of DYGNEX is to reduce the total training time per epoch to a minimum. However, the training time is influenced by both the number of GPUs in use and the size of the workload. Consequently, a key consideration is the construction of the load from snapshot groups across different time windows. It is evident that varying snapshot sizes and diverse time intervals can significantly affect the load. As such, the overall performance of DYGNEX could be influenced. Please elucidate the effects of snapshot configuration on performance and explain how these configurations are managed.
* The sparsity of dynamic graphs can have a considerable impact on load distribution. How does DYGNEX mitigate the overhead associated with synchronization, especially given the potential variance between spectral and spatial work? My second concern is how DYGNEX achieves a balance between different Graph Neural Network (GNN) architectures and scales effectively with various types of dynamic graphs. Specifically, the paper does not detail how the system adapts to different graph structures, such as those with varying degrees of node connectivity or edge density, which could significantly impact the performance of the scheduling algorithm.
* In Figure 3, only a comparison of accuracy rates on the arXiv dataset is presented. However, the arXiv dataset does not clearly highlight the advantages of the method, as the training time per epoch is only reduced by about 0.1 seconds. This indicates that there is no significant improvement in training efficiency. Could you provide the impact on accuracy for other datasets? Could provide a further data illustrating the changes in accuracy rates across other datasets, such as the Reddit dataset?
* The scalability experiment in section 5.4 is somewhat misleading. At line 310, the author mentions that the experimental cluster consists of only 4 A100 GPUs. How were test data from other clusters obtained? Moreover, the paper does not clarify whether there is a linear relationship between throughput and the number of nodes, nor does it address whether using linear regression for prediction holds any practical value. The use of a linear regression model to predict training times for unseen snapshots, while potentially useful, lacks a rigorous justification. The paper should provide a more detailed analysis of the model's accuracy and its sensitivity to variations in graph characteristics.
* There is no mention of the limitations of DYGNEX. Please include a subsection to address this point.

### Questions
* Please see the weakness section.

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
2

### Summary
This paper introduces DyGNex, a distributed training system for Dynamic GNN (DGNN) that balances the workload across GPUs while minimizing the inter-GPU communication. It proposes a cross-time-window snapshot group scheduling algorithm for load balances. DyGNex profiles the timing for each task on GPUs, and use a CPU to schedule using a cross-time-window group combination, which combines tasks across different time windows. To find the optimal scheduling, it uses two methods: 1) ILP; 2) greedy algorithm. The evaluation shows that DyGNex reduces the epoch training time by 2x.

### Strengths
* Discuss the difference between prior works (ESDG, BLAD) with DyGNex in Table 1, and Figure 1 shows the motivation (load imbalance) clearly.
* The results show that it reduces the training time per epoch and reduce the imbalance ratio.

### Weaknesses
 * Profiling at runtime to estimate the time spent on training snapshot groups is time consuming. 
* Use ILP at runtime to solve the optimal scheduling problem is also time consuming. What if it takes too long and no solution is given. How would the system proceed in such a case.
* The general idea of using runtime profiling data from different GPUs and using heuristics to schedule is not a new idea. It has been widely used in all distributed systems, like federated learning, LLM training stragglers, etc.

### Questions
* In line 298, what is n in the time complexity? Is it the number of snapshots for number of GPUs? 
* How frequently do you need to do profiling and algorithm solving during the overall training process?
* Do you think there may be other metrics (some features in the snapshots) to estimate the runtime on each snapshot rather than doing runtime profiling? 
* Table 3 shows that DyGNex reduces the training time per epoch by more than 2x, but in Figure 4, DyGNex  reduces the imbalance ratio from 1.5x to 1.0x, which is less than 2x. Could you explain why

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper introduces DyGNeX, a multi-GPU distributed training system for dynamic graph neural networks (DGNNs) designed to handle discrete-time dynamic graphs (DTDGs). DyGNeX employs a cross-time-window snapshot group scheduling algorithm to balance computational workloads across GPUs during training by distributing mini-batches and sub-mini-batches. The paper presents two variants of this algorithm, using either greedy or integer linear programming (ILP) methods for scheduling. Experimental results demonstrate promising speedup compared to the state-of-the-art approach.

### Strengths
S1: This paper presents an effective scheduling algorithm that addresses a crucial load balancing issue across GPUs for each training epoch—a problem previously overlooked in the DGNN literature. 

S2: The proposed method is well-motivated, and its effectiveness is compelling. 

S3: Experimental results demonstrate promising speedup compared to the state-of-the-art approach, BLAD.

### Weaknesses
W1: This paper is not self-contained. It fails to clearly and comprehensively define and discuss the research problem, technical challenges, and the proposed method.  
1. Section 2 includes multiple concepts but without any figure illustrations or equations. Without reading the referenced papers, readers cannot know what the standard distributed DGNN training pipeline is, what are the current challenges, and what the contribution of this paper is. The authors should also clearly state what the dimensions in Table 1 specifically refer to (there’s a Typo in Table 1, where the caption says there are four dimensions, but the table only shows three).
2. Section 3 presents an overview of the entire system with multiple components, but the entire paper only gets into detail of the group strategy. What is the difference between other components with previous work BLAD?
3. Section 4.3 is hard to understand where a lot of symbols are not defined or explained in advance.

W2: One critical technical issue is that the proposed scheduling algorithm limits the randomness of training batches in each epoch. However, this paper does not provide rigorous theoretical analysis and requires more empirical evidence to justify how it ensures training quality. Figure 3, Figure 7, and Figure 8 show some extent of performance drop when training some DGNNs. The paper should also show how the scheduling algorithm affects training on other datasets. 

W3: This paper evaluates the proposed method by comparing it with one SOTA baseline (BLAD) and another weak baseline (ESDG). The paper also introduces a strong method called PSG, which represents a naive solution with uncompromised accuracy. However, PSG lacks a detailed definition, and the differences between PSG, NyGNeX, and BLAD are not clearly stated. Clearly discussing these differences would help more accurately identify which components of the system are effective.

### Questions
Please see the weaknesses.

### Soundness
1

### Presentation
1

### Contribution
2

---

## Human Reviewer 6

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper proposes a load balancing technique for training dynamic graph neural networks on multiple GPUs. The authors evaluated their technique on a four-GPU machine and showed good scalability with simulation.

### Strengths
1. The proposed technique (collecting the execution time of different tasks with profiling, formalizing the task grouping problem as an optimization, and solving the optimization problem using ILP) is reasonable.

### Weaknesses
1. I don't see much challenge in the problem. Grouping the tasks according to the profiled execution time is straightforward.

2. Related to the first point, I don't see new insight/contribution in this paper. Load balancing has been studied extensively in many graph algorithm settings. Even for the specific task considered in this paper (distributed training of DGNNs), this paper is not the first to propose a solution. 

3. While the paper targets GNNs, I don't see many ML components. The main problem it studies is the tradeoff between load balance and inter-GPU communication. This topic is more commonly studied in computer systems or high-performance computing conferences, which might be more suitable venues for the paper. 

4. Evaluation with larger graphs are needed. Currently, all of the graphs used in the evaluation fit in one single A100 GPU. To show the real contribution of the proposed technique, the authors need to evaluate with graphs large enough to require distributed training.

### Questions
Please address my comments above.

### Soundness
3

### Presentation
2

### Contribution
2
