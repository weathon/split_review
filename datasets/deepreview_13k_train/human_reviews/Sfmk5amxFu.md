# Chimera: State Space Models Beyond Sequences

- Decision: Reject
- Scores: 5, 6, 6, 6

## Abstract
Powerful deep learning methods based on Transformers are used to model diverse data modalities such as sequences, images, and graphs. 
These methods typically use off-the-shelf modules like self-attention, which are domain-agnostic and treat data as an unordered set of elements.
To improve performance, researchers employ inductive biases—such as position embeddings in sequences and images, and random walks in graphs—to inject the domain structure, or *topology*, into the model.
However, these inductive biases are carefully engineered heuristics that must be designed for each modality, requiring significant research effort.
In this work, we propose *Chimera*, a unified framework that mathematically generalizes state space models to incorporate the topological structure of data in a principled way.
We demonstrate that our method achieves state-of-the-art performance across domains including language, vision, and graphs. Chimera outperforms BERT on the GLUE benchmark by 0.7 points, surpasses ViT by 2.6% on ImageNet-1k classification accuracy, and outperforms all baselines on the Long Range Graph Benchmark with a 12% improvement on PascalVOC.
This validates Chimera's methodological improvement, which allows it to directly capture the underlying topology, providing a strong inductive bias across modalities.
Furthermore, being topologically aware enables our method to achieve a linear time complexity for sequences and images, in contrast to the quadratic complexity of attention.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper studies state-space models for data beyond sequences. Starting from an observation that connects the mask matrix in Structured Masked Attention and the resolvent of the adjacency matrix, this paper proposes to utilize this observation to inject the topological structure of data into SSMs such that the SSMs can deal with data structures beyond sequences, e.g., images and graphs. This is done by parametrizing the "adjacency matrix" accordingly for each data structure. Multiple tricks are also proposed to improve the accuracy and efficiency of computing the resolvent, including normalization for better numerical conditions and approximation for faster speed. Experiments have demonstrated its great performance.

### Strengths
1. This paper is well-written and easy to follow.
2. The observation is interesting and makes sense.
3. The implementation (i.e., those tricks for improving Chimera) is straightforward.
4. The empirical results look good.

### Weaknesses
1. I know many experiments have been done since this paper claims contributions over multiple data structures, but I do want to see if Chimera can outperform those SSMs proposed in their respective domains, e.g., mamba2 for NLP tasks, vision mamba for CV tasks, etc.
2. The efficiency analysis is not enough: a detailed speed benchmark and description of the way of computing resolvent in practice are needed.
    - Proposition 4.4 involves the use of Gaussian elimination,  whose efficiency may highly depend on practical cases. Could the author clarify what implementation is used in practice to achieve guaranteed linear complexity?
    - If I'm not mistaken, when dealing with graph-structured data, the claimed SOTA performance is achieved by computing the resolvent exactly, right? Does this take cubic complexity? And when using the approximation trick for better efficiency, actually the performance is largely decayed, which is no better than the previous graph mamba works in most cases.
    - BTW, I'm curious about how things are implemented exactly. I was wondering if the authors plan to release the code.
3. How can the model deal with edge features for graph-structured data?
4. It seems to me this work is similar in spirit to another recent graph SSM work [1], although starting from a different story. For example, 1) their LapPE and the resolvent in Chimera for global dependency; 2) their computation can be written similarly as Eq. (5) in Chimera to achieve linear complexity while capturing global dependency; 3) their local + global module v.s. the global module and the local convolution in Chimera. Their work is so recent, so I believe the comparison is not required. But it would be great if the authors could provide a discussion of this work and Chimera.

My major concern is about the practical efficiency, which I think is not presented comprehensively yet in the current manuscript. I believe at least a speed benchmark is required. Overall, I like this paper and I'm more than willing to increase the score if this concern can be resolved.  

[1] Huang, Yinan, Siqi Miao, and Pan Li. "What Can We Learn from State Space Models for Machine Learning on Graphs?". arXiv preprint arXiv:2406.05815 (2024).

When considering the theoretical complexity, the claims of linear complexity for general DAGs in Proposition 4.4 appear questionable. The proof seems to imply a complexity of O(nnz(A)) for each column, resulting in a total theoretical complexity of O(n * nnz(A)). This would necessitate quadratic algorithms both theoretically and empirically, which is not consistent with the claimed linear complexity. For general graphs, the method would require cubic theoretical complexity, and even with approximation, the theoretical complexity can only be reduced to quadratic. The manuscript also overclaims the contribution by not mentioning its suffering in theoretical and empirical complexity. The abstract claims "Furthermore, being topologically aware enables our method to achieve a linear time complexity for sequences and images", which is misleading since the method cannot be implemented efficiently right now, greatly lowering the contribution of this work. The manuscript needs to be revised to reflect these limitations and overclaims.

### Questions
See above.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes Chimera, a framework that generalizes state space models (SSMs) to handle arbitrary data topologies by reformulating them through resolvent operations on adjacency matrices. The paper introduces a principled mathematical approach to incorporating topology into SSMs, achieving competitive results across various tasks. However, the method faces practical limitations for general topologies where DAG assumption does not hold and approximations are required. In addition, the discussion is lacking if the method can also generalize to more structured topologies such as Lie groups.

### Strengths
1. The paper potentially expands the domain of application of recent state-space models (with SMA form) beyond plain sequences. 
2. Theorem 4.5 and the subsequent sections on optimized forward and backward pass implementation make the proposed method the most efficient for DAG-topologies.
3. The normalization scheme is well-motivated and theoretically grounded. I can see it is an essential ingredient for applying Chimera to the wide range of topologies.
4. Experiments demonstrate clear advantages of the proposed Chimera model in comparison with transformer, mixer, M2 and Hyena architectures.

### Weaknesses
1. The insight of SSMs operating on directed line topology is obvious and I suppose trivially holds for any sequence model.
2. Figure 1 does not contribute much to the narrative in the paper. I suggest the authors make a figure more specific to the method described in the paper.
3. While the proposed method claims to generalize SMA-SSMs to any topology, I am not sure it can handle topological groups such as Lie groups. The paper would benefit from additional discussion on the possible extension of SSMs to group-structured topologies given the rising interest in alternatives to self-attention for group-equivariance [1,2,3 etc].
4. While in theory, the proposed approach applies to a wide range of topologies, the practical application requires either a strong assumption like DAG or approximating L as in Eq.19 which can be costly for large graphs. It limits the practical applicability of the proposed model, especially given the results in Table 5 that demonstrate the exact version to work much better than the approximated one.
5. The paper will benefit from a more detailed discussion on computational complexity in the general case when the DAG assumption does not hold.
6.  While I understand the motivation of setting k=diam(G), the paper would benefit from the ablation study on how the performance depends on k when k < diam(G). This ablation study aims to verify if the method can be optimized for large graphs with large diam(G).

Minor:
 - line 161 footnote typos
 - Notation clash in Proposition 4.1: consider changing A^T to A^{|V|}, otherwise, A^T reads as transposed.

### Questions
Questions:
 - Is it possible to extend the proposed method to incorporate edge features when provided? I realize that the proposed method is a first step towards topology-aware SSMs, a brief discussion on the possibility of incorporating edge features will be useful.
 - Why are the results in Tables 1,2,3 reported only over one data split?

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
This paper introduces an SSM framework that can be adapted to several data topology. Moreover, they propose an efficient way of processing the topology when the structure is in the form of a DAG, together with a technique to decompose common modalities such as images and text into DAG components. The method is tested on 3 different modalities including image, text and graph benchmarks.

### Strengths
- Incorporating the data topology in the SSM architecture via the resolvent of the adjacency matrix is a useful tool for extending SSM models into graph community. While most of the existing approaches are flattening the graphs and rely on the expressivity of positional encodings to directly apply the SSM on a sequence, CHIMERA are efficiently incorporate the graph structure via adjacency matrix masking.
- The fact that, when the structure is constrained to be a line graph,  the model correspond to the existing sequence-based SSM,  guarantees the good performance beyond graph domain.
- The decomposition of existing structure into DAG components improves the efficiency, an important advantage for SSM models over existing architectures.
- The experimental results show competitive performance with reduced complexity.

### Weaknesses
 - The paper claims to propose a method that is able to deal with several types of data. However, the core contribution is integrating a graph structure into the SSM, leveraging the fact that sequences  can be represented as linear graphs, while images can be represented as grid-like graphs. Based on this well-known fact, any graph architecture can be (over)stated as being apliable across modalities.
- The operator proposed in Equation(12) is wildly used in spectral-based graph neural networks. Rediscovering it via an SSM lens and using specific techniques to compute it efficiently is an important contribution. However, discussing its relationship with attention-based GNNs (like GAT and Graph Transformers) or efficient GNN variants would provide a more comprehensive overview of the field, extending the context beyond SSMs
- A key advantage of employing SSMs consist in reducing complexity and creating more efficient computation.  While the paper does a good job on motivating linear complexity (as opposed to the quadratic one used by models such as BERT), it fall short on evaluating the efficiency experimentaly. Reporting the empirical time complexity would help better emphasize the advantages of using CHIMERA compared to existing models.

### Questions
Please see the sections above.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
Chimera is a new framework that generalizes state space models to effectively incorporate the topology of diverse data types, such as sequences, images, and graphs, into its structure. Unlike traditional methods that treat data as an unordered set, Chimera captures the inherent topology of data, leading to methodological improvements and state-of-the-art performance across various domains. It achieves this by using a structured masked attention mechanism that parameterizes the adjacency matrix to accumulate influences between nodes, allowing for linear time complexity and outperforming existing models like BERT and ViT in benchmarks.

### Strengths
This paper introduces a versatile, fundamental model architecture that stands in contrast to the commonly utilized Transformer models. The effectiveness of this architecture is demonstrated through experiments in vision, graph analysis, and natural language processing. This work represents a significant contribution to the ML community. Addressing the minor weaknesses below would strongly support its acceptance.

### Weaknesses
1. The fairness of the configurations in Tables 7 and 8 appears to be questionable. (Question 1)

2. The scalability of the proposed architectures needs to be addressed. (Questions 2, 3, and 4)

   Specifically, while the authors claim linear time complexity, the practical memory and computational costs of Chimera, especially with increasing sequence lengths or graph sizes, are not thoroughly explored. The paper lacks a detailed analysis of how the structured masked attention mechanism scales in terms of memory footprint and actual runtime, compared to established models like Transformers. This is crucial for assessing the real-world applicability of the proposed architecture.

   Furthermore, the paper does not investigate the potential trade-offs between model size and performance. It is unclear whether the observed performance gains are solely due to the architectural innovations or simply a result of increased model capacity. The experiments should include a more detailed analysis of the model's behavior across different parameter counts, which would provide a better understanding of the model's capabilities and limitations.

### Questions
1. In the experiments, the Chimera model possesses approximately twice the depth of the ViT model. It is a well-established fact in CV and NLP that depth contributes more to model power than width. While the comparison between SSMs and Transformers in terms of depth is common, it prompts the question: would the Chimera model maintain its superior performance if it had the same number of layers and parameters as the Transformer models?

2. Memory and computational efficiency are often cited advantages of SSMs over Transformers. The inclusion of both theoretical and empirical comparisons between the two would enhance the contribution of this paper.

3. Previous works involving SSMs and the Mamba model have indicated that larger models do not always outperform smaller ones, possibly due to various factors. Could the authors conduct experiments with smaller models in CV and NLP to investigate this phenomenon?

4. Some previous works show that the optimization landscape of Transformers is better than that of SSMs. Could the authors add a figure on training loss to compare the convergence of ViT/BERT with Chimera?

### Soundness
3

### Presentation
3

### Contribution
3
