# Lightweight Graph Neural Network Search with Graph Sparsification

- Decision: Reject
- Avg Score: 5.33
- Scores: 5, 8, 3

## Abstract
Graph Neural Architecture Search (GNAS) has achieved superior performance on various graph-structured tasks. However, existing GNAS studies overlook the applications of GNAS in resource-constraint scenarios. This paper proposes to design a joint graph data and architecture mechanism, which identifies important sub-architectures via the valuable graph data. To search for optimal lightweight Graph Neural Networks (GNNs), we propose Lightweight Graph Neural Architecture Search with Graph SparsIfication and Network Pruning (GASSIP). In particular, GASSIP comprises an operation-pruned architecture search module to enable efficient lightweight GNN search. Meanwhile, we design a novel curriculum graph data sparsification module with an architecture-aware edge-removing difficulty measurement to help select optimal sub-architectures. With the aid of two differentiable masks, we iteratively optimize these two modules to efficiently search for the optimal lightweight architecture. Extensive experiments on five benchmarks demonstrate the effectiveness of GASSIP. Particularly, our method achieves on-par or even higher node classification performance with half or fewer model parameters of searched GNNs and a sparser graph.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposed an lightweight GNAS algorithm. It iteratively optimizes graph data and architecture through curriculum graph sparsification and operation-pruned architecture search.

### Strengths
1. The paper proposes a GNAS method with graph sparification, which is an interesting exploration.
2. The paper applies the method to extensive experiments and shows good results on multiple datasets.

### Weaknesses
 1. GNAS methods nowadays have been expanded to large-scale datasets, while the paper only showed the results on Physics and Ogbn-Arxiv datasets. Could you please give a more overall perfomance comparison with other GNAS methods like GUASS  on large-scale OGB datasets?

   [1] Large-scale graph neural architecture search, ICML 2022.

2. More comparsion on the unified benchmark will be appreciated, such as NAS-Bench-Graph.

   [2] Benchmarking Graph Neural Architecture Search, NIPS 2022.

3. Cited works in Section 2 are mostly before 2022 and the methods compared in Table 1 are all before 2021 which make the work out-dated. I do know there were multiple GNAS and graph sparsification methods proposed in 2022/2023. Maybe more cutting-edge research work as well as comparisions should be added.

4. The first contribution is proprosing a operation-pruned search method with learnable weight mask. However, the work of HM-NAS introduced this hierarchical masking on redundant operations, edges, and even the weights of supernet. It seems like transfering the idea on graphs. Maybe you should add this work and discuss the noble part of the first contribution compared with the learnable weight mask idea on edges in HM-NAS.  

   [3] HM-NAS: Efficient Neural Architecture Search via Hierarchical Masking, ICCV 2019.

6. I feel a little confused about the workflow in Figure 1. I understand that the iterative training process of structure mask is between the gradient update of operations and architectures. However, the training process probably need to point back to the architecture searching part to illustrate the interactive training not directly getting the final sparsed graph and connecting to the pruned architecture. Maybe the training part and the procedures after binarizing masks can be seperated.

### Questions
See weakness.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces a new approach to lightweight graph neural network architecture search called GASSIP. What sets it apart is that during the search process, it jointly considers graph data sparsification and operation pruning, allowing the discovered sub-architectures to achieve better performance with fewer parameters. It also exhibits a degree of robustness. Ultimately, it yields both sparse graphs and lightweight sub-architectures, enhancing search efficiency.

### Strengths
1. First jointly considers operation pruning and graph data sparsification in graph neural architecture search, which can efficiently search lightweight GNNs. 
2. Uses curriculum learning strategy in graph data sparsification, which can more accurately identify redundant edges and obtain a sparse graph structure beneficial for downstream tasks

### Weaknesses
1. Considers graph sparsification and operation pruning at the same time, but does not provide a theoretical analysis of whether this iterative optimization converges.
2. Insufficient experiments on large-scale graph data: The large-scale graph data set used in the experiments of this article only contains OGBN-ARXIV. Therefore, more experiments on large-scale graph data are needed to verify the performance of the GASSIP method.

### Questions
1. Is the search result sensitive to the choice of random seed? 
2. Simultaneous optimization of operation pruning and graph data sparsification may interfere with each other and lead to performance degradation. Could you provide some theoretical analysis on the convergence of the joint optimization process?
3. In equation (3), operation pruning and graph sparsification are combined with a logical OR operation. What is the rationale behind this design choice?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper introduces a novel approach called GASSIP (Lightweight Graph Neural Architecture Search with Graph Sparsification and Network Pruning) for automating the design of efficient Graph Neural Networks (GNNs). It highlights the needs for lightweight GNAS and data sparsification to reduce resource requirements. GASSIP employs operation pruning and curriculum graph data sparsification to iteratively optimize GNN architectures and graph data, resulting in more efficient and accurate lightweight GNNs. Experimental results demonstrate its superiority over traditional GNNs and GNAS, achieving substantial performance improvements with significantly reduced search time.

### Strengths
1.	GASSIP is shown to significantly improve the efficiency of GNAS by reducing search time while maintaining or even enhancing the performance of GNNs.
2.	The writing is easy to follow.

### Weaknesses
1.	The research problem is not novel to the community. There have been a series of work for the co-optimization of neural architecture and data, even at the domain of graph NAS and graph data. 
2.	I am still concerned about the motivation to work on graph NAS. Different to other neural architectures, there are only several layers in GNNs, and the number of candidate operations is limited. I believe if one only applies the popular toolkit of hyperparameter tuning, the much higher performance will be obtained. 
3.	The unstructured pruning of model weights makes no sense in the practical efficiency improvement. Based on the current parallel hardware (with processing of single instruction multiple data), the unstructured matrix multiplication has almost the same cost with the dense matrix multiplication.

### Questions
1.	Please address my concerns listed in the weaknesses. 
2.	It is unscalable to apply a learnable mask with shape of N\timesN in graph data. The node number in most of the graphs are at the scale of millions or even billions. 
3.	Following the last question, I need to check the possibility of applying this work in the benchmark datasets of ogbn-products and paper100m.
4.	Graph sparsification is a very old topic, and there have been many researches being conducted to provide the principle in how to remove edges without affecting the graph structural properties (e.g., adjacency eigenvalues). For example, one can remove edges based on degrees of 1/d_i + 1/d_j, where d_i and d_j are the degrees of node i and j, respectively. It is easy to remove more than 90% of edges but maintain the comparable performance [1].
[1] Lovász, László. "Random walks on graphs." Combinatorics, Paul erdos is eighty 2.1-46 (1993): 4
5.   How many edges can be deleted in the adopted datasets?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
