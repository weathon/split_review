# SynHING: Synthetic Heterogeneous Information Network Generation for Graph Learning and Explanation

- Decision: Reject
- Scores: 5, 5, 6, 6

## Abstract
Graph Neural Networks (GNNs) excel in delineating graph structures in diverse domains, including community analysis and recommendation systems. 
As the interpretation of GNNs becomes increasingly important, the demand for robust baselines and expansive graph datasets is accentuated, particularly in the context of Heterogeneous Information Networks (HIN). Addressing this, we introduce SynHING, a novel framework for Synthetic Heterogeneous Information Network Generation aimed at enhancing graph learning and explanation. SynHING systematically identifies major motifs in a target HIN and employs a bottom-up generation process with intra-cluster and inter-cluster merge modules. This process, supplemented by post-pruning techniques, ensures the synthetic HIN closely mirrors the original graph’s structural and statistical properties. Crucially, SynHING provides ground-truth motifs for evaluating GNN explainer models, setting a new standard for explainable, synthetic HIN generation and contributing to the advancement of interpretable machine learning in complex networks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces SynHING, the first framework designed for generating synthetic heterogeneous graphs with ground-truth explanations. SynHING designed to advance graph learning and explanation. The effectiveness of SynHING is validated using four datasets. This paper establishing a new benchmark for explainable

### Strengths
S1:  This paper is well-written, and the method is presented clearly.
S2: The article proposes a novel framework for generating synthetic heterogeneous information networks, which is an important contribution to the study of the interpretability and generalization capabilities of Graph Neural Networks
S3: The SynHING framework is capable of generating synthetic graphs with practical application backgrounds, such as community analysis and recommendation systems

### Weaknesses
S1: The document mentions some existing synthetic graph generation techniques, why not include them for comparison?
S2: In heterogeneous graphs, nodes typically have node types and node attributes. Why does the paper only generate attribute information for the target nodes?

### Questions
Seen Weaknesses

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
The paper presents SynHING, a framework for generating synthetic heterogeneous information networks (HINs) designed to support graph neural network (GNN) learning and model interpretability. The framework synthesizes HINs by identifying and replicating core structural motifs from real-world graphs, creating diverse subgraphs, and merging them through controlled intra-cluster and inter-cluster methods to ensure realistic structure and statistical alignment with reference datasets.

### Strengths
-	The paper presents SynHING, which generates synthetic heterogeneous information networks specifically designed to support graph learning and GNN explainability.
-	SynHING’s modular design (e.g., motif generation, intra-cluster and inter-cluster merging) allows flexible control over the network structure, making it possible to model complex HIN characteristics.

### Weaknesses
-	While SynHING’s computational complexity is discussed, an empirical evaluation of scalability and runtime efficiency on large-scale datasets is not provided. The author mentions in line 339 that "the overall time complexity of SynHING is O(N)," which seems efficient. However, the largest graph size used in the experiments is only 53,428, which is insufficient to demonstrate the scalability of the method. Specifically, the paper lacks experiments that systematically vary the size of the generated graphs to analyze the runtime scaling behavior. It is unclear how the motif generation, intra-cluster merging, and inter-cluster merging steps contribute to the overall runtime, and whether the O(N) complexity holds in practice for much larger graphs.
-	The purpose of SynHING is to generate HINs. To evaluate the effectiveness of SynHING, the author selects only three different HGNNs as baselines, which is insufficient to fully demonstrate the generalization capability of SynHING in generating HINs. The choice of baselines is also limited in terms of the diversity of HGNN architectures. For example, the selected models may not fully represent the spectrum of approaches, such as attention-based models, message-passing models, or models that explicitly consider higher-order relations. A more comprehensive evaluation should include a wider range of HGNN models with different underlying mechanisms to ensure the robustness of the generated HINs.
-	Evaluating how similar the synthetic graphs are to real graphs is a meaningful experiment. The author addresses this question through pre-training and fine-tuning, which seems reasonable. However, the author only reports the results for HGT. Reporting results for more baselines, with consistent performance trends, would be necessary to support the experimental conclusions. The pre-training and fine-tuning approach, while valid, only indirectly measures the similarity between synthetic and real graphs. It would be beneficial to also include direct structural similarity metrics, such as graph edit distance or other measures of graph isomorphism, to quantify the structural differences between the generated and real-world graphs.
-	The presentation of the paper has some formatting inconsistencies that require a thorough review: (1) The caption of Figure 5 ends with a period, while other figures do not. Normally, if a caption is a complete sentence, it should end with a period. (2) Different formats are used when referencing figures, such as "Fig. 3(a)," "Figure 4a," and "Fig. 5a.".

### Questions
See the weaknesses part.

### Soundness
2

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
4

### Summary
This paper proposes a new method for synthesizing heterogeneous graphs called SynHING. SynHING generates synthetic heterogeneous graphs through modules such as Major Motif Generation, Base Subgraph Generation, Intra-Cluster Merge, Inter-Cluster Merge, and Node Feature Generation, allowing for flexible adjustment of the size of the HIN. Multiple experiments validate the effectiveness and scalability of the synthetic heterogeneous graphs.

### Strengths
1. This paper proposes a new direction for creating synthetic datasets for heterogeneous graphs, which is scarce in this area.
2. The methods in the paper are innovative, and each module is necessary and effective.
3. The experiments in the paper are sufficient and validate the effectiveness of the proposed synthetic graphs.

### Weaknesses
1. The images in the paper are too small and difficult to see clearly, especially Figure 2.
2. The authors should provide a detailed introduction of when synthetic graphs need to approximate reference graphs and when they should differ from them. In my view, synthetic graphs should address some of the shortcomings of the reference graphs; otherwise, Section 5.4 lacks significance.
3. I believe the authors need to conduct explainable experiments on the synthetic graphs to validate their effectiveness and to verify whether the ground truth is accurate. Potential models include: xPath[1] and HENCE-X[2].
4. The proposed synthetic dataset seems targeted at node classification tasks; can it also be applied to graph classification tasks?

### Questions
See Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper focuses on the scarcity of heterogeneous graph datasets and overcomes the need for such datasets in the domain of GNN explanations. In particular, it proposes a novel SynHING framework for generating synthetic HINs. This method leverages the real-world HINs as references and systematically generates the major motifs for explanations. Extensive experiments have demonstrated its generality and practicality.

### Strengths
1. Originality: This paper introduces the first framework for generating synthetic heterogeneous graphs with ground-truth explanations.

2. Clarity: The paper's writing in the methodology section is logically clear.  The reason behind each step of the method design is also explained in detail.

3. Significance: The framework for generating diverse synthetic HINs that can be flexibly adjusted will provide a solid foundation for future research on heterogeneous GNN explanations.

### Weaknesses
1. The size of many figures in this paper needs to be adjusted. For example, Figure 2 is too small, which is not conducive to reading.

2.  The writing of this paper could be improved. For instance, there is a significant gap between the first and second paragraphs of the introduction.

3.  The techniques used in this paper for generating synthetic HINs are relatively normal, focusing only on the degree of nodes in the graph to consider the relationship with real graphs. 

4.  This paper only validates the methods on node-level tasks, and it is unclear whether this method can be transferred to graph-level explanation task scenarios.

5. The design of the paper's experimental section needs improvement. First, more tabular types of experiments should be used to conduct a more intuitive quantitative analysis. Second, important experimental results should be presented at the forefront.

### Questions
1. I would like to know if this method can assist with graph-level explanation tasks in heterogeneous graphs.

### Soundness
3

### Presentation
3

### Contribution
3
