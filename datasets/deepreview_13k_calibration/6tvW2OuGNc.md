# TopGQ: Post-Training Quantization for GNNs via Topology Based Node Grouping

- Decision: Reject
- Avg Score: 4.50
- Scores: 3, 5, 5, 5

## Abstract
Graph neural networks (GNN) suffer from large computational and memory costs in processing large graph data on resource-constrained devices. One effective solution to reduce costs is neural network quantization, replacing complex high-bit operations with efficient low-bit operations. However, to recover from the error induced by lower precision, existing methods require extensive computational costs for retraining. In this circumstance, we propose TopGQ, the first post-training quantization (PTQ) for GNNs, enabling an order of magnitude faster quantization without backpropagation. We analyze the feature magnitude of vertices and observe that it is correlated to the topology regarding their neighboring vertices. From these findings, TopGQ proposes to group vertices with similar topology information of inward degree and localized Wiener index to share quantization parameters within the group. Then, TopGQ absorbs the group-wise scale into the adjacency matrix for efficient inference by enabling quantized matrix multiplication of node-wise quantized features. The results show that TopGQ outperforms SOTA GNN quantization methods in performance with a significantly faster quantization speed.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper presents a post-training quantization (PTQ) framework tailored for graph neural networks (GNNs) that mitigates the quantization error by grouping nodes based on topology (indegree and local Wiener index) and absorbing group-specific scales into the adjacency matrix, TopGQ enables highly efficient integer matrix multiplication. Experiments demonstrate that TopGQ achieves faster quantization speeds compared to quantization-aware training (QAT) methods.

### Strengths
1-TopGQ introduces a PTQ approach, eliminating the need for gradient computation, which reduces quantization time significantly.

2-Using indegree and local Wiener index to group nodes based on topological similarity seems novel

### Weaknesses
1- Lack of motivation and not providing proper application for the work 

2-Considerable accuracy drop in 4-bit scenarios.

3-Less detailed justification about the obtained results.




### Questions
1- The motivation of the paper is not clear to me. The paper needs to provide applications where fast quantization is urgently needed. From the plots, the QAT takes about 2 hours for large workloads in most cases. Since it needs to be done one time, quantization time cannot be a good motivation to me especially when the proposed method has an accuracy drop. Please provide more applications and cite a few notable references that show quantization time matters. It would be helpful to suggest specific applications or scenarios where fast quantization could be particularly valuable.

2- The motivation behind quantization can be time and storage. However, as Table 5 shows, TOPGQ is not showing any gains in terms of inference time. No results for storage reduction are provided as well. The authors can provide a more comprehensive analysis of the trade-offs between accuracy, quantization time, inference time, and storage requirements.

3- The author didn’t study GAT. Is there any reason behind it?

4- Several studies show that PTQ starts degrading performance when it goes below 4 bits. I think the proposed PTQ technique will not work well compared to QAT in below 4-bit unless the authors show some results that nullify the hypothesis. Even for 4-bit, I can see quite a notable accuracy drop compared to fp32 (e.g., around 7% Reddit GCN and 21% on ogbnproducts GCN). The authors need to provide an application where such drops are acceptable.

5-The author needs to provide detailed justification where PTQ can perform better than QAT and FP32. For example, why in the case of ogbnproteins, TopGQ is better than FP32 by a noticeable margin?

6-How sensitive is TopGQ to changes in group sizes or to variations in the rank used in low-rank approximations?

7- Outliers might still exist within topologically grouped nodes, especially in large-scale graphs. How does this affect quantization quality?

8- Table 5 needs to provide results for 4-bit as well.

9- An ablation study comparing the use of indegree and Wiener index with other centrality measures (e.g., closeness or betweenness) would provide insights into the robustness of TopGQ’s topology-based grouping.

10- An analysis of how changing grouping parameters (e.g., group size, hop count for Wiener index) affects quantization error would clarify the stability and adaptability of TopGQ.

11-The provided code is just .py file without any instructions on how to run and get results. That limits the reproducibility.
The could should provide a README file with setup instructions, example commands, and a requirements.txt file for dependencies.

12-Minor Typos:

A– Consider changing "huge" to " significant, substantial, etc"

B- Change "On the quantization time" to "In terms of quantization time."

C- "a fair comparison, we use fixed-precision quantization" – Add "a" before "fixed-precision quantization"

D. with a significant drop in accuracy of 9.0%p!

### Soundness
1

### Presentation
1

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
This paper proposed a post-training quantization method for graph neural network.  It uses both the degree information and the topological information (localized Wiener index) to efficiently group the node with similar embedding magnitude together.  The paper also employed a fast algorithm for calculating the local Wiener index to reduce the quantization and inference overhead.  Experiments show that the method well maintain the accuracy of the models.

### Strengths
1. This paper uses post-training quantization without backprop, while the related works are mostly quantization-aware training, or requires backpropagating gradients in the quantization procedure.
2. It is novel to consider topology information to group the nodes and performs well.
3. The method has little harm on the accuracy performance.

### Weaknesses
1. The overhead of calculating the topological information is faster compared to other baselines, but it seems still a burden compared with the inference time, especially considering most inference is done in batch. It's not clear how the localized Wiener index calculation scales with larger graphs or deeper k-hop neighborhoods. The paper should provide a more detailed analysis of the computational cost of this step, including memory usage and its impact on overall inference latency, especially when considering batched inference.
2. It looks like that the inference is not done in a batched manner (correct me if I'm wrong), making the inference time for fp32 baseline extremely long.  It would be better if batched inference results can be shown and compared to have a full understanding of the capabilities of this method. The current presentation makes it difficult to assess the true performance benefits of the proposed quantization method. The lack of batched inference for the baseline makes the comparison unfair and the reported speedups less meaningful.
3. There is no discussion of combining this method with sampling methods, like neighbor sampling or subgraph sampling.  Real world graph training for node tasks mostly requires sampling.  And the inference for neighbor sampling is much faster.  I would like to see how the method performs in these cases and how large the overheads are. The method's applicability to real-world scenarios is limited without considering sampling techniques, which are essential for handling large graphs. The paper should explore how the proposed quantization method interacts with common sampling strategies and report the resulting performance and overhead.

### Questions
1. I wonder how the inference is done, because the inference time on ogbn-products is surprisingly long.  Is it done in a batched manner or each single node goes through the network individually?
2. The accuracy of SAGE on ogbn-products Table 1 is abnormally low.  On the ogbn-leaderboard, SAGE on ogbn-products is over 78%.  Why is this happening?
3. Are there any other indexes that may be better than Wiener index, like the spectral information?
4. Can the authors give more information about why quantization for GNN models is important, or in what scenario is it important?  The largest dataset used here (ogbn-products) can be trained and inferred in the full-graph manner in one single card (A6000), which is much faster than the inference time number shown here. 

I would like to raise my score if my concerns are properly addressed.

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
This paper proposes TopGQ, a post-training quantization (PTQ) framework for GNNs. Unlike existing quantization methods that rely on quantization-aware training (QAT), which involves retraining the model with gradient updates, TopGQ achieves efficient quantization by leveraging the topological information of the graph without requiring any retraining. Specifically, TopGQ groups vertices with similar topology information, including inward degree and localized Wiener index, to share quantization parameters within the group, which can quantize GNNs without backpropagation and accelerate the quantization. To further optimize inference efficiency, TopGQ absorbs group-wise scale factors into the adjacency matrix during aggregation steps, which allows for efficient integer matrix multiplication. Experiments show that TopGQ outperforms SOTA GNN quantization methods in performance with a faster quantization speed.

### Strengths
- The proposed method is innovative. Both indegree information and localized Wiener index are used for node grouping to effectively address the high feature magnitude variance issue in GNN quantization.
- Accelerating the quantization process of GNNs is necessary.

### Weaknesses
 - This work may not achieve a wall-clock speedup on graph-level tasks because it requires grouping the nodes of unseen graphs and computing quantization parameters.
- The application of this method is limited. Because of the use of scale absorption, it seems hard to apply this method to GAT models.
- The acceleration of the Accelerated Wiener Index Computation Algorithm is mainly because of parallel computing rather than the proposed algorithm.
- The third method, scale absorption, is commonly used in network quantization. It should not be a key contribution to this paper.

### Questions
- In Table 6, the baseline methods use the SciPy implementation. It is better to compare the Accelerated Wiener Index Computation Algorithm with a parallel Dijkstra method.
- Can this method be applied to GAT models? If so, it is better to add more experiments about GAT quantization to show the generalization of TopGQ.
- In the experiments, the baseline $A^2Q$ method also uses a uniform quantization, but it is a mixed-precision method. So it would be better to compare a mixed-precision version of $A^2Q$ under the same compression or computation constraint.

### Soundness
3

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
3

### Summary
TopGQ proposes a post-training quantization (PTQ) framework for Graph Neural Networks (GNNs), achieving favorable quantization results without the need for backpropagation. To address the challenge of significant diversity in node features, TopGQ introduces a local Wiener index from a grouping perspective, clustering nodes with similar in-degrees and local Wiener indices for quantization. Additionally, TopGQ optimizes the computation of the local Wiener index, enhancing the efficiency of the grouping process. Finally, it employs scale absorption techniques to merge feature scales into the adjacency matrix, resulting in a more uniform feature distribution.

I read the rebuttals and decided to keep my decision. In my eyes, adding too many experiments in the rebuttal should not be encouraged. Besides, this paper still lacks comprehensive discussions on GNN quantization.

### Strengths
1. A framework for GNN post-training quantization (PTQ) without backpropagation is proposed, achieving superior quantization results with reduced calibration time.
2. The concept of grouping is introduced, utilizing the Wiener index as a replacement for the traditional in-degree metric for effective grouping.
3. An accelerated algorithm for computing the Wiener index is presented, enhancing parallelism and reducing overhead during the grouping process.
4. The code is released, and practical deployment is demonstrated on a GPU.

### Weaknesses
1. The literature review is insufficient. Many SOTA works [1-3] are not mentioned and have not been included in the experimental comparisons. In the summary of GNN quantization works, only Degree-Quant, SgQuant, and A2Q (highlighted in red) were compared in the experiments, lacking consideration of newer works.
2. Section 5.1: The rationale for using the Wiener index as the basis for grouping is not explained. As stated in the paper, there are various metrics to describe the topology of graphs. More theoretical derivation or comparative experiments are needed to demonstrate the advantages of using the Wiener index over other metrics. 
3. Section 5.3: The introduction of scale absorption does not clarify its purpose. According to Equation (16), it merges the scale of X into the adjacency matrix A after quantization. However, the results provided in Section 6.6 show that the distribution before quantization is more uniform and is considered easier for quantization, which appears inconsistent with the method presented in Section 5.3.
4. Lack of Training and Without-Training Comparative Experiments: Without-training should only be considered a viable option when training performance is average or shows minimal improvement. It is inappropriate to directly present without-training as a contribution, as it is relatively easy to implement.
5. Section 6.4: The use of Scale Absorption for INT8 generally results in precision loss, which is not explained. The paper should provide a detailed analysis of why scale absorption degrades performance in INT8, especially when it is designed to improve quantization.
6. Section 6.5: Although actual inference speedup is provided, INT8 only achieves 1.25 times acceleration compared to FP32, or even lower. However, reference [2] demonstrates 3-4 times or higher inference speedup. Additionally, while INT4 is mentioned, there is no deployment of INT4, requiring a reasonable explanation. The paper needs to clarify why the observed speedup is so low compared to existing work and why INT4 deployment is not shown.
7. Section 6.5: The presented speed performance of the optimized local Wiener index is compared to very outdated classical methods, which weakens the argument's credibility. The comparison should be made against state-of-the-art parallel implementations of shortest path algorithms on GPUs to provide a fair assessment of the proposed method's efficiency.

### Questions
1. This paper states that TopGQ is the first PTQ framework for GNNs; however, according to the review [1], SGQuant is actually a PTQ work. The paper also claims that SGQuant is a method for Quantization-Aware Training (QAT), which requires verification.
2. The experimental results of [2] and A2Q [3] exhibit fluctuations (e.g., 81.5±0.7%), while the experimental results presented in this paper are fixed values. Is this a normal phenomenon?

[1] A Survey on Graph Neural Network Acceleration: Algorithms, Systems, and Customized Hardware

[2] Low-bit Quantization for Deep Graph Neural Networks with Smoothness-aware Message Propagation [CIKM 2023]

[3] A2Q: Aggregation-Aware Quantization for Graph Neural Networks [ICLR 2022]

### Soundness
2

### Presentation
1

### Contribution
2
