# StructComp: Substituting propagation with Structural Compression in Training Graph Contrastive Learning

- Decision: Accept
- Scores: 5, 5, 5, 6

## Abstract
Graph contrastive learning (GCL) has become a powerful tool for learning graph data, but its scalability remains a significant challenge. In this work, we propose a simple  yet  effective training framework called Structural Compression (StructComp) to address this issue. Inspired by a sparse low-rank approximation on the diffusion matrix, \ourmodel~trains the encoder with the compressed nodes. This allows the encoder not to perform any message passing during the training stage, and significantly reduces the number of sample pairs in the contrastive loss. We theoretically prove that the original GCL loss can be approximated with the contrastive loss computed by \ourmodel. Moreover, \ourmodel~can be regarded as an additional regularization term for GCL models, resulting in a more robust encoder. Empirical studies on various datasets show that StructComp greatly reduces the time and memory consumption while improving model performance compared to the vanilla GCL models and scalable training methods.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes Structural Compression (StructComp), a new training framework that improves the scalability of graph contrastive learning (GCL) models. The key idea is to substitute propagation with a sparse, low-rank approximation of the diffusion matrix to compress the nodes. Contrastive learning is performed on these compressed nodes, reducing computation and memory costs. Theoretical analysis shows the compressed loss approximates the original loss and StructComp implicitly regularizes the model.  Experiments on various single-view and multi-view GCL methods demonstrate StructComp's improvements in performance and efficiency.

### Strengths
1.	The paper is well-written and easy to follow. The problem is motivated well, and the method is explained clearly. 

2.	Scalability is a major bottleneck hindering wider adoption of graph neural networks. This work makes an important contribution by enabling efficient training of GCL models.

### Weaknesses
1. Additional experiments could help verify claims on scalability and robustness of StructComp: 

- Evaluating on larger datasets like papers100M and or OGBG-LSC datasets  would better support scalability claims, since the experimented datasets are rather small or medium scale.  

- Would be great to verify the model stability/robustness with the proposed regularization, since it is claimed in the presentation. 


2. Would be great to discuss the approximation quality to the diffusion matrix  of StructComp for more complicated graphs and other models architectures (like GAT, GraphSAGE) .

3. There is a lack of  comparisons with certain related works, such as recent graph contrastive learning methods  [1-2]

### Questions
See the weakness above

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper aim at resolving the scalability issue of graph contrastive learning training. In graph representation learning, the most compiutation  overhead comes from message passing, where its complexity grows exponentially wrt the num of layers in GNN. 

To overcome this scalability issue, the authors propose **StructComp** trains the encoder with the compressed nodes. StructComp allows the encoder not to perform any message passing during the training stage.

### Strengths
I like the idea of using compressing nodes to replace the need of message passing.

### Weaknesses
- The theoritical results only hold in linear-GNN, which over-simplifies the problem. It is well know that deep neural network behave different from linear model in contrastive learning [1]. Without consider non-linearity, the problem in Eq. 4 is simply matrix decomposition problem (e.g., [2] section 3).

- Experiment datasets are too small (even arxiv dataset is small)... please try some large-scale graph datasets (e.g., Yelp, Reddit datasets that previously GraphSaint paper) to validate the effectiveness. Especially when this paper is focussing on improving the scalability issue. 

- Repeat experiment multiple times instead of just once. For example Figure 4.

### Questions
How theoritical results could be generalized to non-linear models?

Does the proposed method work for graphs with multiple node/edge types?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces StructComp, a scalable training framework for Graph Contrastive Learning (GCL). By replacing the message-passing operation in GCL with node-compression, StructComp achieves significant reductions in both time and memory consumption. The authors provide both theoretical analysis and empirical evaluations to underscore the effectiveness and efficiency of StructComp in training GCL models.

### Strengths
1. The storyline is relatively clear, it is easy to follow for the authors.  
2. The experiment results are amazing, especially the time-saving.  
3. The used method is quite simple.

### Weaknesses
1. Lack of discussion of graph partition: The paper lacks a comprehensive discussion on graph partitioning. Given that the efficacy of the method hinges on graph partitioning—a classic NP-hard problem—a detailed exploration of its impact on the proposed method is warranted. A cursory introduction does not suffice.  Specifically, the paper does not explore how different partitioning strategies (e.g., spectral clustering, METIS, random partitioning) affect the quality of the compressed graph and, consequently, the performance of the contrastive learning task. The choice of partitioning algorithm could significantly influence the structure of the compressed graph, leading to variations in the learned representations. A more thorough analysis of this aspect is needed, including a discussion of the trade-offs between different partitioning methods in terms of computational cost and the quality of the resulting compressed graph. 
2. Inadequate theoretical provements: The theoretical justifications provided are somewhat limited. The authors' attempt to establish the equivalence between the compressed loss and the original loss is based solely on the ER model, which may not be representative of real-world datasets. The analysis does not consider the structural properties of real-world graphs, such as power-law degree distributions or community structures, which could affect the validity of the theoretical results. The theoretical analysis should be extended to more general graph models or provide a discussion of the limitations of the current analysis. Furthermore, the paper does not provide a clear explanation of how the approximation gap in the loss function translates to the performance of the contrastive learning task. 
3. Lack of the discussion about the limitations.

### Questions
1. Adding more discussions about graph partition: The authors should delve deeper into the topic of graph partitioning, as highlighted in the first weakness.

2. Considering not over-claiming your work: It's crucial to avoid overstating the contributions. While the authors assert that they have provided theoretical proof, the strong assumptions (like the ER model) limit its applicability. It might be prudent to either temper such claims in the abstract and introduction or offer more exhaustive proof.
In essence, while I acknowledge the novelty and results presented in this paper, I urge the authors to provide a more in-depth rationale behind their impressive outcomes. Without this, the paper leans more toward a technical report than a comprehensive research paper.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies improving efficiency of graph contrastive learning. The authors propose a structural compression framework, StructComp, that adopts a low-rank approximation of the diffusion matrix to obtain compressed node embeddings. They show that the original GCL loss can be approximated with the contrastive loss computed by StructComp, with an additional benefit of the robustness. Experiments on seven benchmark datasets show that StructComp greatly reduces the time and memory consumption while improving model performance compared to the vanilla GCL models and scalable training methods.

### Strengths
(+) The proposed structural compression idea is new and interesting;

(+) The presentation and organization are clear and easy to follow;

### Weaknesses
(-) The applicability of StructComp seems to be limited;

- Theoretically, StructComp has to rely on the approximation of the diffusion matrix for a specific graph and GNN model, as demonstrated in Theorem 4.1. How well StructComp can approximate to more complicated graphs such as heterophilous graphs, and more complicated while commonly used GNNs such as GraphSage, GIN, GAT, or even more interesting variants such as PNA?

- Empirically, what is the exact setting of StructComp for node classification? Can StructComp be applied to both transductive and inductive node classification?

- How well can StructComp approximate different augmentations in GCL?

(-) Several claims have not been verified;

- The paper claims that StructComp can work for large scale graphs, while the benchmarked datasets are rather small or medium scale. Although it’s claimed that ogbn-products and arxiv are large datasets, while they are indeed medium scale datasets according to OGB (https://ogb.stanford.edu/docs/nodeprop/). To support the claim, it’s expected to evaluate StructComp in large datasets such as papers100M, reddit, or OGBG-LSC datasets.

- The paper also claims that StructComp has better robustness and stability with the additional regularization, while no evidence’s been found.

(-) Some related works have not been compared or discussed;

-  Some GCL works have not been discussed in the paper, for example, [1,2,3].

- Why not comparing efficient GCL baselines such as CCA-SSG, and GGD discussed in the paper?

(-) How the time and memory cost are computed? Do they count in the preprocessing steps?

### Questions
1. The applicability of StructComp seems to be limited:

- Theoretically, StructComp has to rely on the approximation of the diffusion matrix for a specific graph and GNN model, as demonstrated in Theorem 4.1. How well StructComp can approximate to more complicated graphs such as heterophilous graphs, and more complicated while commonly used GNNs such as GraphSage, GIN, GAT, or even more interesting variants such as PNA?

- Empirically, what is the exact setting of StructComp for node classification? Can StructComp be applied to both transductive and inductive node classification?

- How well can StructComp approximate different augmentations in GCL?

2. Several claims have not been verified:

- The paper claims that StructComp can work for large scale graphs, while the benchmarked datasets are rather small or medium scale. Although it’s claimed that ogbn-products and arxiv are large datasets, while they are indeed medium scale datasets according to OGB (https://ogb.stanford.edu/docs/nodeprop/). To support the claim, it’s expected to evaluate StructComp in large datasets such as papers100M, reddit, or OGBG-LSC datasets.

- The paper also claims that StructComp has better robustness and stability with the additional regularization, while no evidence’s been found.

3. Some related works have not been compared or discussed:

-  Some GCL works have not been discussed in the paper, for example, [1,2,3].

- Why not comparing efficient GCL baselines such as CCA-SSG, and GGD discussed in the paper?

4. How the time and memory cost are computed? Do they count in the preprocessing steps?


**References**

[1] Calibrating and Improving Graph Contrastive Learning, TMLR’23.

[2] Single-Pass Contrastive Learning Can Work for Both Homophilic and Heterophilic Graph, TMLR’23.

[3] Scaling Up, Scaling Deep: Blockwise Graph Contrastive Learning, arXiv’23.

[4] Structure-free Graph Condensation: From Large-scale Graphs to Condensed Graph-free Data, arXiv’23.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
