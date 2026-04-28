# Zero-Shot Generalization of GNNs over Distinct Attribute Domains

- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 5, 5, 6

## Abstract
Inductive GNNs are able to generalize across graphs with the same set of node attributes. However, zero-shot generalization across attributed graphs with disparate node attribute domains remains a fundamental challenge in graph machine learning. Existing methods are unable to effectively make use of node attributes when transferring to unseen attribute domains, frequently performing no better than models that ignore attributes entirely. This limitation stems from the fact that models trained on one set of attributes (e.g., biographical data in social networks) fail to capture relational dependencies that extend to new attributes in unseen test graphs (e.g., TV and movies preferences). Here, we introduce STAGE, a method that learns representations of _statistical dependencies_ between attributes rather than the attribute values themselves, which can then be applied to completely unseen test-time attributes, generalizing by identifying analogous dependencies between features in test. STAGE leverages the theoretical link between maximal invariants and measures of statistical dependencies, enabling it to provably generalize to unseen feature domains for a family of domain shifts. Our empirical results show that when STAGE is pretrained on multiple graph datasets with unrelated feature spaces (distinct feature types and dimensions) and evaluated zero-shot on graphs with yet new feature types and dimensions, it achieves a relative improvement in Hits@1 between 40% to 103% for link prediction, and an 10% improvement in node classification against state-of-the-art baselines.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper studies how to use a pre-trained graph model in any new domain with unseen attributes, enhancing the zero-shot generalization. The authors propose a new model STAGE by learning the representations of statistical dependency between attributes, instead of the attribute values themselves. They also conduct experiments to validate the performance of STAGE across several benchmark datasets.

### Strengths
1.	The paper is well written and easy-to-follow.
2.	Extensive results validate the effectiveness of the proposed model.

### Weaknesses
1.	More discussions on the variants on LLM should be made.

### Questions
N/A

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces STAGE, a method designed for zero-shot generalization across attributed graphs with distinct attribute domains. STAGE constructs what it calls STAGE-edge-graphs for each edge in a graph, embedding statistical dependencies between attributes at each node pair. The model achieves significant performance gains in zero-shot settings for tasks like link prediction and node classification on various datasets.

### Strengths
1. This paper achieves SOTA results by embedding statistical dependencies rather than raw features.
2. The STAGE is a domain-agnostic framework, which can generalize across disparate attribute spaces.

### Weaknesses
1. The STAGE-edge-graph is a fully connected weighted graph, so I am concerned about the complexity. Specifically, the construction of these graphs for each edge, involving all pairwise attribute combinations, seems computationally expensive, especially with a large number of attributes. The paper lacks a detailed analysis of how this scales with increasing graph size and attribute dimensionality.
2. Edge-based embeddings may limit its ability to capture high-order interactions in graphs. The method focuses on pairwise relationships between nodes connected by an edge, potentially missing more complex, multi-hop dependencies that might be crucial for certain tasks. For example, a pattern involving a chain of three or more nodes and their attributes might not be effectively captured by edge-centric embeddings.
3. The motivation in the introduction is not presented well. The authors didn't analyze why their proposed method can address the limitations they mentioned before, so it's hard to understand the intrinsic research thinking. The connection between the identified limitations of existing methods and the proposed STAGE framework is not clearly established. It's unclear how embedding statistical dependencies directly addresses the challenges of domain generalization across different attribute spaces.
4. The experiments are a little weak. For example, I believe the 4.2 and 4.3 belong to the same type of experiment, they didn't analyze the complexity and the ablation study, and they didn't include the limited research papers they mentioned in the introduction into baselines,  which weakens the convincing. The lack of ablation studies on the STAGE-edge-graph construction and the choice of statistical dependency measures makes it difficult to assess the contribution of each component. Furthermore, the experiments in sections 4.2 and 4.3, while distinct in task, seem to evaluate similar aspects of the model's generalization capability, and could benefit from a more unified analysis. The absence of comparisons with the specific methods mentioned in the introduction also makes it harder to contextualize the performance gains.
5. I noticed this paper was submitted to ICML workshop so there is authors' information leakage. Both papers present STAGE for zero-shot generalization of GNNs across different attribute domains, and this paper just extends some real-world testing datasets. 
6. The authors didn't release their code although this is not compulsory, which may limit their reproducibility.

### Questions
Please see the weaknesses

### Soundness
3

### Presentation
2

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
The paper presents STAGE, a method that enables zero-shot generalization of graph neural networks (GNNs) across graphs with different attribute domains. STAGE constructs STAGE-edge-graphs to capture statistical dependencies between attributes instead of absolute values, facilitating transferability to unseen domains. The method shows substantial improvement in zero-shot tasks like link prediction and node classification on graphs with entirely new feature spaces.

### Strengths
1. STAGE's strategy to use statistical dependencies rather than raw attribute values to enhance zero-shot generalization in GNNs is novel for graph machine learning.
2. The theoretical basis for STAGE, connecting maximal invariants and statistical dependencies, is well-articulated and provides a sound foundation for the empirical results.
3. STAGE is shown to be adaptable across domains of varied attribute types and dimensions, a crucial quality for real-world applicability.

### Weaknesses
1. STAGE's two-stage process involving STAGE-edge-graphs, conditional probability matrices, and subsequent embeddings may be challenging to implement or optimize in practice. Details on computational overhead compared to baselines would enhance clarity. The provided experiments do not adequately address the computational cost on larger graphs, as the E-Commerce Stores dataset, with only 17,463 nodes, is not sufficiently large to demonstrate the scalability of the method. This raises concerns about its applicability to real-world graphs with millions of nodes and edges.
2. While STAGE is effective for pairwise dependencies, it is unclear how it handles more complex dependencies in highly interconnected graphs. The theoretical justification, while mentioning higher-order conditional independence tests, does not provide concrete examples or empirical evidence of how STAGE captures these complex interactions in practice. The reliance on rank tests, while theoretically sound, needs further validation in complex graph structures.
3. The success of STAGE appears dependent on the architecture and expressivity of the underlying GNNs (M1 and M2). Sensitivity analysis on different GNN backbones might clarify robustness across architectures. While the authors provide some results with GCN, a more comprehensive analysis across diverse GNN architectures, including those with different message-passing mechanisms, is needed to fully understand the generalizability of STAGE.
4. The evaluation focuses on e-commerce and social network datasets; examining STAGE’s generalizability on domains like biomedical or geospatial networks would strengthen claims of universality. The current datasets do not fully represent the diversity of graph structures and attribute types found in real-world applications. The lack of evaluation on domains with different characteristics limits the generalizability of the findings.

### Questions
1. How does STAGE handle attribute domains with highly heterogeneous data types, such as unstructured or mixed media data?
2. Could the authors elaborate on the computational cost associated with STAGE compared to baselines, especially in large-scale graphs?
3. Does STAGE's reliance on GNN backbones like NBFNet affect its generalizability? Could alternative GNN architectures be equally effective?
4. Has STAGE been evaluated in terms of the interpretability of the learned dependencies? If so, what methods were used?

### Soundness
2

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
The paper introduces STAGE, a novel approach designed to enable zero-shot generalization for Graph Neural Networks (GNNs) across graphs with varying node attribute domains. STAGE aims to learn representation of statistical dependencies between attributes rather than their absolute values. This allows the model to transfer knowledge to unseen domains by leveraging analogous dependencies. Through experiments on multiple datasets, the paper demonstrates STAGE's superior performance in link prediction and node classification tasks, especially in terms of zero-shot cross-domain generalization.

### Strengths
- Generalization from a node attributes view and the two stages for processing graph representation are interesting.
- The paper provides a theoretical analysis, linking STAGE with maximal invariants and statistical dependency measures, which provides theoretical support for the model's generalization capabilities.
- The paper shows STAGE's robustness when facing different attribute domains, which is a very important characteristic in the varied real-world data

### Weaknesses
 - Although the paper presents some quantitative results and shows good performance in different link prediction and node classification domains, it lacks some qualitative analysis. For example, it could demonstrate how the model learns that "income level is positively correlated to phone price" from the training set and then discovers that "height is positively correlated with clothing size" in a new domain, thus generalizing to the new domain.
- STAGE is capable of capturing and leveraging feature dependencies in graph data, rather than relying on specific attribute values. The article can illustrate which feature dependencies are effective on the test set after pre-training the model.

### Questions
How well does this model handle larger graph datasets.

### Soundness
3

### Presentation
3

### Contribution
3
