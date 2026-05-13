# Topology-aware Graph Diffusion Model with Persistent Homology

- Decision: Reject
- Scores: 5, 5, 6, 3

## Abstract
Generating realistic graphs presents challenges in estimating accurate distribution of graphs in an embedding space while preserving structural characteristics such as topology. However, existing graph generation methods primarily focus on approximating the joint distribution of graph nodes and edges, overlooking topology-wise similarity hindering accurate representation of global graph structures such as connected components and loops. To address this issue, we propose a topology-aware diffusion-based graph generation method that aims to closely resemble the structural characteristics of the original graph by leveraging persistent homology from topological data analysis (TDA). Specifically, we suggest a novel loss function, Persistence Diagram Matching (PDM) loss, which ensures the generated graphs to closely match the topology of the original graphs, enhancing their fidelity and preserving essential homological properties. Also, we introduce a novel topology-aware attention to enhance the self-attention module in the denoising network. Through comprehensive experiments, we demonstrate the effectiveness of our approach not only by exhibiting high generation performance across various metrics, but also by demonstrating a closer alignment with the distribution of topological features observed in the original graphs. In addition, application to real brain network data showcases its versatility and potential for complex and real graph application.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces a topology-aware diffusion-based method for realistic graph generation, aiming to preserve structural characteristics similar to the original graphs. The authors propose a novel approach that integrates topological data analysis (TDA), specifically using persistent homology, to guide the generation process. They introduce a new loss function Persistence Diagram Matching (PDM) loss that ensures the generated graphs closely align with the topology of the original graphs, thereby improving fidelity and preserving essential homological properties. Additionally, a topology-aware attention mechanism is developed to enhance the self-attention module in the denoising network.

### Strengths
1. This paper addresses the challenge of existing graph generation methods failing to preserve topological information by proposing  a novel topology-aware graph generation method that yields homologically similar graphs with high fidelity.
2. This paper demonstrates the effectiveness of the proposed approach through comprehensive experiments, exhibiting high generation performance across various metrics and aligning better with the distribution of topological features observed in the original graphs.

### Weaknesses
1. The paper does not adequately address the relationship between the Preliminaries and the Methodology, making it challenging to follow. Section 3 introduces many topological concepts, which can be frustrating if understanding them is required to proceed with reading. However, Section 4 did not specifically clarify how to apply these topological concepts. This gives me the feeling that there is no need to understand the various topological concepts mentioned in Section 3.
2. Motivation is not convincing enough. The main contribution of this paper is to maintain the topological features of the original graph during the graph generation process. However, it does not analyze the existing methods' capability in capturing topological invariance characteristics.
3. The paper focuses on graph structure information and proposes a topology-aware diffusion-based graph generation method. However, the generalization ability to small graph data: the performance improvement of the model on small graph datasets (e.g., Ego-small) is not obvious, which may indicate that the generalization ability of the model on small graph data needs to be improved. Although the model aims to recover the original graph structure from noisy graphs, how sensitive and robust it is to noise is not detailed in the text. In practice, different noise types and intensities may have an impact on model performance.

### Questions
Please refer to weaknesses.

### Soundness
3

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
4

### Summary
This paper introduces a novel graph generation method that utilizes persistent homology within a diffusion model, enhancing structural characteristics. The proposed Persistence Diagram Matching (PDM) loss, in conjunction with the 1-Wasserstein distance, significantly improves the model's topological awareness. The approach extends its application to complex brain network data, demonstrating its effectiveness in real-world scenarios.

### Strengths
Pros

1. The proposed method differs from traditional self-attention models by incorporating persistent homology encoding and the use of Q in the forward process, addressing the structural characteristics of graphs.
2. The denoising model integrates the 1-Wasserstein distance to introduce a new loss function (PDM), which is highly versatile and effectively enhances the model's structural awareness.
3. The application range is extended from traditional graphs to brain data with structural features, demonstrating the method's effectiveness on complex real-world datasets.

### Weaknesses
Cons

1. As a self-attention model, the paper does not clarify the costs associated with introducing attention mechanisms with mu and training multiple models.
2. The evaluation lacks diverse metrics for comparing graph properties, limiting a comprehensive assessment of model performance.
3. As a generative model, it should generate similar graphs without prior conditions. Here, mu and Q are given to generate the graph, this would naturally make the graph tend to have those similar mu and Q? If so, how to obtain the mu and Q for the graph to be generated? If mu and Q of the test graph themselves are used during the test process, this will make the generated result naturally close to the original graph. If use training ones this would lead to bias?
4. While the loss function emphasizes degree distribution, this leads to the model showing the most significant improvements in degree metrics, while performance on other indicators is less pronounced.

### Questions
Please refer to Cons.

### Soundness
3

### Presentation
2

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
This work introduces a persistence diagram matching loss, which aligns the generated graphs’ topology with that of the target, and a topology-aware attention mechanism within the denoising network. By capturing homological structures, this work aims to better replicate global structural characteristics like connectivity and loops, making it suitable for complex applications.

### Strengths
1. The proposed idea is interesting.
2. Demonstrated application in real-world brain networks illustrates TAGG’s adaptability to complex, topologically rich datasets.

### Weaknesses
1. A thorough complexity analysis of the graph generation process, including the persistent homology component, is essential. Given that this approach may be computationally intensive, providing a comparative analysis with existing baselines would be highly beneficial. This analysis should include a discussion on both time complexity and resource requirements, considering its practical feasibility for large datasets and real-world applications.

2. The paper’s introduction of the topology-aware diffusion approach is distinct. However, a clearer differentiation from [1] is necessary. The authors should emphasize the conceptual advancements over DiGress in terms of preserving global topological features through persistent homology. It would also strengthen the paper to discuss how this method aligns or contrasts with other homology-based approaches in TDA applications for graphs, which are briefly mentioned in the related work section.

3.  Table 3 provides a quantitative comparison between TAGG and baseline models across multiple datasets using MMD metrics. However, the analysis could benefit from a more detailed interpretation. For instance, while TAGG shows improved performance on various datasets, the significance of the metric differences, especially on small-scale graphs, could be expanded upon. Additionally, a discussion on how TAGG’s improvements in clustering and orbit metrics correlate with enhanced topological fidelity would offer a deeper understanding of the model’s strengths.

### Questions
See Weakness.

### Soundness
3

### Presentation
3

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
The paper introduces a topology-aware graph generation method called TAGG that incorporates persistent homology into diffusion models to preserve structural characteristics of graphs. The authors propose two main technical contributions: a persistence diagram matching (PDM) loss that ensures generated graphs match the topology of original graphs, and a topology-aware attention mechanism that enhances the self-attention module by incorporating homological features. The method is evaluated on various datasets, with a particular emphasis on brain network generation.

### Strengths
The technical execution of the work is solid and thorough. The empirical evaluation is comprehensive, with extensive comparisons against baselines and multiple visualizations. The application to brain network generation is interesting, as it addresses a real-world problem where topological features are crucial. The authors also provide detailed ablation studies.

### Weaknesses
The paper's primary limitation lies in its incremental nature and lack of theoretical depth. The core diffusion framework is heavily based on existing work (Vignac et al., 2023), and the integration of persistent homology, while useful, represents an incremental advance rather than a fundamental breakthrough. The topology-aware attention mechanism is essentially a straightforward modification of standard attention by incorporating topological features. And it is not clear why such topological based representations or vectorizations are differentiable and can be trained in an end-to-end generative model. The paper lacks theoretical analysis of why topology-awareness improves generation and provides no theoretical guarantees about topological preservation. The computational overhead of computing persistent homology is not adequately addressed, which could be significant for larger graphs. Additionally, the novelty is limited as the use of persistent homology in graph analysis has been explored in previous works (e.g., Hofer et al., 2020), and the paper doesn't clearly articulate how their approach fundamentally differs from these previous applications.

### Questions
- How does the computational complexity scale with graph size, particularly considering the overhead of computing persistent homology? How does the method perform on very large graphs, and what are the main scalability challenges?
- The topology-aware attention mechanism uses pre-computed homological features during training, but how sensitive is the performance to the choice of filtration function used to compute these features?
- Are these topology-aware attention and persistence diagram matching loss differentiable or able to be trained end-to-end?
- What new features are learned through proposed methods? Is there any way to illustrate related hidden representations?
- Could this approach be extended to dynamic graphs where topology evolves over time?

### Soundness
2

### Presentation
2

### Contribution
2
