# FastCLIP: A Suite of Optimization Techniques to Accelerate CLIP Training with Limited Resources

- Decision: Reject
- Avg Score: 3.67
- Scores: 3, 5, 3

## Abstract
Existing studies of training state-of-the-art Contrastive Language-Image Pretraining (CLIP) models on large-scale data involve hundreds of or even thousands of GPUs due to the requirement of a large batch size. However, such a large amount of resources is not accessible to most people. While advanced compositional optimization techniques for optimizing global contrastive losses have been demonstrated effective for removing the requirement of a large batch size, their performance on large-scale data remains underexplored and not optimized. To bridge the gap, this paper explores several aspects of CLIP training with \textbf{limited resources} (e.g., up to tens of GPUs). First, we introduce FastCLIP, a general CLIP training framework built on advanced compositional optimization techniques while designed and optimized for the {distributed setting}. Our framework is equipped with an efficient gradient reduction strategy to reduce communication overhead. Second, to further boost training efficiency, we investigate three components of the framework from an optimization perspective: the schedule of the inner learning rate, the update rules of the temperature parameter and the model parameters, respectively. Experiments on different strategies for each component shed light on how to conduct CLIP training more efficiently. Finally, we evaluate the performance of FastCLIP and the state-of-the-art training baseline (OpenCLIP) on different compute scales up to 32 GPUs on 8 nodes, and three data scales ranging from 2.7 million, 9.1 million to 315 million image-text pairs to demonstrate the significant improvement of FastCLIP in the resource-limited setting.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper introduces FastCLIP, a distributed training framework designed to optimize CLIP model training using compositional optimization techniques, removing the dependency on large batch sizes for effective model performance. The framework incorporates an efficient gradient reduction strategy to minimize communication overhead and conducts comprehensive ablation studies on various components, including learning rate schedules (constant vs. cosine), temperature parameter update rules, and different optimizers (AdamW, LAMB, Lion, and SGDM).

### Strengths
1. This paper studies an important problem in CLIP training, "how to efficiently and effectively training CLIP models with limited resources". 

2. This paper designs an efficient distributed training framework based on advanced compositional optimization techniques. It conducts ablation studies on the several key components during training, such as the update rule of learning rate, temperature parameter and model papers, providing valuable insights for future work in optimizing large-scale model training.

3. Experimental results across various compute and data scales demonstrate that FastCLIP significantly outperforms existing methods, such as OpenCLIP, enhancing training efficiency on setups with up to 32 GPUs.

### Weaknesses
1. This paper is not designed for general CLIP training but is instead built on the assumptions and techniques from prior work[1]. As a result, its applicability may be limited to scenarios that align with these specific assumptions, restricting its generalizability to broader CLIP training tasks. Specifically, the reliance on the compositional optimization techniques from [1] might not be universally applicable across all CLIP model architectures or datasets, potentially hindering its effectiveness in diverse real-world scenarios. The paper does not adequately explore or address the limitations imposed by this dependency, making it unclear how well FastCLIP would perform outside the specific conditions outlined in [1].

2. The paper primarily builds on existing techniques, such as compositional optimization and gradient reduction strategies, without introducing fundamentally new concepts. While it refines and optimizes these methods for CLIP training, the core ideas themselves are not particularly novel. The incremental improvements over existing methods are not clearly quantified, making it difficult to assess the true impact of the proposed framework. The paper lacks a detailed analysis of the computational trade-offs between the proposed optimizations and existing methods, which is crucial for understanding the practical benefits of FastCLIP.

3. The paper's writing lacks clarity, making it difficult to follow at times. The structure of the paper would benefit from significant revision to improve its readability and logical consistency. The descriptions of the proposed framework and experimental setup are often vague, making it challenging to reproduce the results. The lack of clear definitions for key terms and concepts further contributes to the overall lack of clarity.

4. The experiment compares FastCLIP with OpenCLIP, which is designed for large-scale clusters and requires large batch sizes. In contrast, FastCLIP is tested on a relatively smaller cluster (up to 32 GPUs), violating the original conditions under which OpenCLIP was evaluated. Additionally, the results in experiments 4 and 5 are inconsistent, with different methods showing unstable performance. This lack of stability weakens the conclusions and limits the insights that can be drawn for future work. The paper does not provide a clear explanation for the observed inconsistencies, raising concerns about the robustness of the proposed framework.

### Questions
See the weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces a distributed framework designed to improve the efficiency of CLIP by optimizing resource use and reducing dependency on large batch sizes and numerous GPUs. They use several optimization techniques, including a gradient reduction strategy and a flexible LR schedule, to facilitate efficient CLIP training with limited resources. The study compares FastCLIP to OpenCLIP and demonstrates consistent performance improvements on different scales of data and compute resources.

### Strengths
- Efficient resource utilization for settings with limited computational resources, making CLIP training more accessible.

- Systematic Optimizations: The paper provides a structured approach to optimizing multiple aspects of CLIP training, including LR schedules, temperature parameter updates, and gradient communication strategies.

- Experimental Validation: Comprehensive testing on various datasets and compute scales effectively shows the benefits of FastCLIP compared to OpenCLIP.

### Weaknesses
 - Limited Novelty in Optimization Techniques: The optimization techniques applied, such as learning rate decay and gradient reduction, are well-established and may not contribute novel methodological insights. Specifically, the paper does not provide a detailed analysis of how these techniques are adapted to the specific challenges of CLIP training, nor does it compare their implementation against other existing methods. The lack of a thorough comparison makes it difficult to ascertain the unique contribution of their approach beyond standard practices.

- Resource Comparison Limitations: The paper does not conduct an extensive ablation study for larger datasets due to resource constraints, which may limit the generalizability of results on extremely large data scales. The absence of experiments on datasets beyond the scale of those tested raises concerns about the scalability of the proposed optimizations. It is unclear whether the observed performance gains would hold when training on datasets with billions of samples, which are increasingly common in modern vision-language model training.

- Assumption of Availability of Multiple GPUs: Although designed for resource-limited environments, FastCLIP still requires access to multiple GPUs, which may limit applicability for highly resource-constrained users. While the paper reduces the number of GPUs compared to OpenCLIP, the requirement for multiple GPUs still poses a barrier for researchers with very limited resources or those working in environments with single GPU setups.

### Questions
How does the performance of FastCLIP vary across different types of GPUs or compute environments?

Could other advanced optimization techniques (e.g., adaptive optimizers beyond AdamW) further enhance the framework's efficiency?

Would additional experiments on extremely large datasets (>1 billion samples) align with the current findings for smaller datasets?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduced FastCLIP, which uses data-parallel for CLIP training. It claimed to (1) present an efficient gradient reduction strategy to reduce communication overhead, (2) compare inner LR schedule between constant and cosine schedule, (3) compare temperature param update methods and (4) compare optimizers.

### Strengths
1. This paper compared CLIP training performances with different temperature parameter updating methods and different optimizers.
2. The appendix provides detailed experiment results and parameter settings.
3. An introduced cosine schedule could provide better training accuracy.

### Weaknesses
1. Figure 3 is not so clear about the efficiency improvement. The difference between OpenCLIP and FastCLIP is not significant.
2. Figure 4 (a) does not show convergence on the accuracy curve which could be problematic.
3. Figure 4 (b) (c) do not show a significant difference in scalability.
4. The writing style needs improvement, and some part of this paper needs to be summarized. Also, the experiment part needs more details, the authors use many numbers in Table 3, 4, 5 but there is no information on what do they represent, accuracy, or some other metrics.
5. Lack of novelty. This paper compared multiple combinations of existing CLIP training techniques and proposed using data parallelization to scale up the training process. From this summary, existing techniques do not contribute much to novelty except cosine LR schedule, also, data parallelism mentioned in this paper does not show promising results compared to OpenCLIP.

### Questions
1. See weaknesses.
2. Is there any other significant difference between OpenCLIP and FastCLIP? Seems like they are also using data-parallel.
3. What do the number differences represent in Table 3, 4, 5, and Figure 2? The current comparison is not very straightforward.
4. Should the training accuracy converge?

### Soundness
2

### Presentation
3

### Contribution
2
