# Budgeted Online Continual Learning by Adaptive Layer Freezing and Frequency-based Sampling

- Decision: Accept
- Avg Score: 7.50
- Scores: 8, 8, 6, 8

## Abstract
The majority of online continual learning (CL) advocates single-epoch training and imposes restrictions on the size of replay memory.
However, single-epoch training would incur a different amount of computations per CL algorithm, and the additional storage cost to store logit or model in addition to replay memory is largely ignored in calculating the storage budget.
Arguing different computational and storage budgets hinder fair comparison among CL algorithms in practice, we propose to use floating point operations (FLOPs) and total memory size in Byte as a metric for computational and memory budgets, respectively, to compare and develop CL algorithms in the same `total resource budget.'
To improve a CL method in a limited total budget, we propose adaptive layer freezing that does not update the layers for less informative batches to reduce computational costs with a negligible loss of accuracy.
In addition, we propose a memory retrieval method that allows the model to learn the same amount of knowledge as using random retrieval in fewer iterations.
Empirical validations on the CIFAR-10/100, CLEAR-10/100, and ImageNet-1K datasets demonstrate that the proposed approach outperforms the state-of-the-art methods within the same total budget.
\blfootnote{\hspace{-2em}$^*$: Equal contribution. $~~^\dagger$: Corresponding author.}

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes the method *aL-SAR*, which standardizes computational and memory budgets of continual learning (CL) algorithms based on training floating point operations (FLOPs) and total memory size in Byte to address the challenge of fair comparison in online CL algorithms. Besides, this paper introduces adaptive layer freezing to reduce computation costs by selectively freezing layers and frequency-based sampling to prioritize under-learned samples. Experiments on CIFAR-10/100 and ImageNet-1K datasets show that aL-SAR consistently outperforms existing CL methods like ER (Experience Replay), DER++, MIR (Maximally Interfered Retrieval), MEMO, REMIND, EWC, OCS, LiDER, X-DER, CCL-DC, and CAMA by up to 5-10% on average across AAUC and last accuracy, especially under stringent budget constraints.

### Strengths
++ Standardizing computational and memory budgets of continual learning (CL) algorithms is important for evaluating algorithm efficiency and learning system design.

++ The paper provides comprehensive and detailed experimental results.

### Weaknesses
-- Using FLOPs as a metric focuses on raw operations, ignoring algorithm-specific optimizations for training software and hardware systems. See C1.

-- The additional computations required to decide which layers to freeze may introduce overhead that is not directly part of the core training but still contributes to the total computational cost. See C2.

-- The retrieval strategy based on the use-frequency cannot ensure that the model does learn sufficiently by preferring less frequently used samples. See C3.

### Questions
C1:
  - FLOPs served as a direct measure of computational demand across different models, making it possible to compare CL algorithms fairly. However, it doesn’t account for real-world runtime or memory access patterns, which vary based on hardware and software implementations. For instance, two architectures with similar FLOPs might have different inference times on the same hardware due to parallelization or memory bandwidth usage differences.
  
C2:
  - The adaptive layer freezing proposed in this paper can reduce FLOPs but adds complexity. Calculating the full Fisher Information Matrix (FIM) is computationally intensive because it involves second-order derivatives, which can be prohibitive, especially for large neural networks. The paper must explain why calculating FIM does not introduce additional computation costs.
  - Fisher Information (FI) is calculated based on the current mini-batch. However, the calculation results based on the current mini-batch may not generalize across diverse batches in continual learning. For instance, a layer might appear less informative for one mini-batch but could be essential for others due to shifting data distributions, especially under continual learning settings. Hence, the paper needs to justify this.

C3:
  - The strategy might prioritize rare samples in the dataset but may need to be more informative. This overemphasis can lead to inefficient learning, as these rare samples may not enhance generalization and introduce noise. The paper needs to justify that such a retrieval strategy would maintain the acquired knowledge during training.

**Writing Issues**

  1. Line 071: 'ImageNet)' -> 'ImageNet'.
  2. Line 087: 'ER' has no citation and explanation for the abbreviation.
  3. Fig. 1: No explanation of the y-axis.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes a new algorithm for the online CL problem. The authors first explain that a fair comparison between different methods should consider the total number of FLOPs instead of the total number of iterations, as some methods can perform expensive operations each round. Also, it is essential to include all types of memory usage rather than only considering the number of examples in the episodic memory as the actual memory cost. Next they propose an efficient algorithm to address the problems in online continual learning. They use batch fisher information to find the optimal layers that can be frozen while learning from the data. Then, they introduce a new metric, 'appearance frequency,' to measure the contributions of each training example.

### Strengths
* The arguments about the FLOPS and memory costs are critical. To have a fair and meaningful comparison between different methods, we *need* to know the actual cost.

* The idea of having batch-wise and dynamic layer freezing makes the training more suitable for online settings.

* The authors did an excellent job of explaining the motivation and algorithm. All the different components are adequately explained and justified.

### Weaknesses
 * In my opinion, the introduction lacks proper background knowledge, and it jumps to the solutions for the existing problems in online CL. I suggest adding at least one paragraph explaining the background and current state of online continual learning and the current high-level challenges that prior work has attempted to solve, so the readers are on the same page and maybe appreciate your work even more. 

* Have you considered reporting forgetting as an additional metric? This is commonly used in CL papers and could provide further insight into the efficacy of your method.

* What is the memory selection mechanism? In other words, how memory samples are selected, and how does the memory get updated?

* Besides the similarity-aware retrieval, is there any other difference between the in-memory and new samples in the training?

### Questions
* What is the memory selection mechanism? In other words, how memory samples are selected, and how does the memory get updated?

* Besides the similarity-aware retrieval, is there any other difference between the in-memory and new samples in the training?

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
3

### Summary
This paper addresses the challenge of fair comparison in online continual learning (CL) by proposing a total resource budget framework that considers both computational costs (FLOPs) and memory usage (bytes). The authors introduce aL-SAR, which combines two key innovations:

1. Adaptive layer freezing: A method that selectively freezes network layers based on Fisher Information to reduce computational costs while maintaining performance
2. Similarity-aware retrieval: A computationally efficient strategy for retrieving training samples based on usage frequency and gradient similarity

The method is extensively validated on CIFAR-10/100, CLEAR-10/100, and ImageNet-1K datasets, showing superior performance compared to state-of-the-art methods under the same resource constraints.

### Strengths
1. Novel framework for comparing CL methods using total resource budgets including innovative adaptive layer freezing approach based on Fisher Information and computationally efficient memory retrieval strategy.

2. Rigorous empirical validation across multiple datasets and setups containing thorough ablation studies and comparisons with state-of-the-art methods and successful application to large models (LLaVA-1.5-7B).

3. Addresses practical constraints in online CL and shows significant performance improvements while reducing computational costs.

### Weaknesses
1. Using the layer freezing technque for recuding the model params would always block the shallow layers (i.e., layer 1-n) and their representation would be outdated. This would be problematic for frequent distribution shifts.
   
2. The paper's adaptive layer freezing strategy treats layers somewhat independently when making freezing decision. However, neural networks typically have complex inter-layer relationships that this approach might not fully capture.
   
3. The method doesn't address catastrophic forgetting directly, instead focusing on resource efficiency. It's unclear how the method balances the trade-off between resource efficiency and forgetting prevention.
   
4. The computational overhead of maintaining class-wise gradient similarities might become prohibitive for problems with a large number of classes or frequent distribution shifts.

### Questions
1. Could the adaptive layer freezing strategy be extended to handle cross-layer dependencies, potentially leading to more optimal freezing decisions?
2. Although authors have illustrated the process of calculating *Effective Use Frequency* in Sec.3.2 and Sec.A.17, it is still vague for me that how to calculate cosine similarity of the gradients between classes? In A.17, do it that using *0.05% of the model parameters* means that randomly sample params among unfrozen layers?

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
4

### Summary
This paper addresses the challenge of resource constraints in online continual learning (CL) by introducing an efficient method named aL-SAR, which combines adaptive layer freezing and similarity-aware sample retrieval. The adaptive layer freezing component selectively freezes layers to minimize computation based on Fisher Information, while the similarity-aware retrieval component focuses on sampling underused and informative samples from episodic memory to enhance training efficiency. Experiments on CIFAR-10/100, CLEAR-10/100, and ImageNet-1K datasets demonstrate that aL-SAR outperforms several state-of-the-art methods under the same computational and memory budgets.

### Strengths
Pros:

1. The paper introduces a unique approach to online CL by integrating adaptive layer freezing and frequency-based sampling, effectively reducing both computational and memory costs without significant performance trade-offs.

2. The empirical results across multiple datasets comparing to multiple existing SOTA benchmarks show the competitiveness of al-SAR, especially under constrained resource settings.

### Weaknesses
1. Though designed to be efficient by only computing class based gradient, the similarity-aware retrieval approach still requires gradient similarity calculations, which could introduce overhead in large-scale applications. 

2. The experimental setups impose strict memory and computational constraints, limiting the contribution primarily to incremental improvements in the efficiency of existing online continual learning approaches.

3. The authors should compare the method with model based like iCaRL.

### Questions
Please also refer the comments in the strengths and weaknesses sections:

1. Can the authors compare the al-SAR with other methods under the epoch-based setup to show the effectiveness of the method with larger memory constraint? 

2. Can you consider applying aL-SAR on more diverse datasets (e.g., text, multimodal data) to demonstrate the approach’s generalizability?

### Soundness
3

### Presentation
3

### Contribution
2
