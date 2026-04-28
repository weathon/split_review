# GETS: Ensemble Temperature Scaling for Calibration in Graph Neural Networks

- Decision: Accept
- Avg Score: 7.50
- Scores: 8, 8, 6, 8

## Abstract
Graph Neural Networks (GNNs) deliver strong classification results but often suffer from poor calibration performance, leading to overconfidence or underconfidence.
This is particularly problematic in high-stakes applications where accurate uncertainty estimates are essential.
Existing post-hoc methods, such as temperature scaling, fail to effectively utilize graph structures, while current GNN calibration methods often overlook the potential of leveraging diverse input information and model ensembles jointly.
In the paper, we propose Graph Ensemble Temperature Scaling (GETS), a novel calibration framework that combines input and model ensemble strategies within a Graph Mixture-of-Experts (MoE) architecture.
GETS integrates diverse inputs, including logits, node features, and degree embeddings, and adaptively selects the most relevant experts for each node’s calibration procedure.
Our method outperforms state-of-the-art calibration techniques, reducing expected calibration error (ECE) by $\geq 25\%$ across 10 GNN benchmark datasets. 
Additionally, GETS is computationally efficient, scalable, and capable of selecting effective input combinations for improved calibration performance.
Codes are available when published.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper proposes graph ensemble temperature scaling (GETS), a novel calibration technique for node-classification GNNs.
GETS is a parametric calibration method which calibrates the predictions for each node in a graph by predicting a temperature for each node which is used as a factor that is applied to the respective class logits.
GETS predicts node-wise temperatures using a set of GNN-based calibration models trained on different features (predicted logits, node degrees, node features or combinations thereof). The temperatures returned by the GNN calibrators are then combined via a learned gating function which selects a top-k subset of the calibrators for each vertex.

To summarize, GETS combines the previously proposed ensemble temperature scaling (ETS) method with the idea of using a GNN to predict structure-aware temperatures (e.g., CaGCN or GATS).

### Strengths
As reported in the experiments, the combination of structural information and a mixture of calibrators trained on different sets of features seems to clearly outperform previously proposed calibration techniques for node classifiers.

This combination of ideas is well motivated by the paper and the claims regarding the advantages of GETS are supported by the broad range of used datasets.

Presentation-wise, the paper is well structured and the ideas are presented concisely and clearly.

### Weaknesses
As mentioned, the reported advantages of the GETS approach seem to stem from the combination of two ideas:
1. Predicting node-wise temperatures based on class logits, node features and node degrees.
2. Incorporating structural dependencies between vertices to predict temperatures.

Both ideas have (to some extent) been utilized independently in prior work. While the performed experiments show that the combination of both ideas works well in practice, it only gives limited insight into why exactly this is the case.

More specifically, I believe it would have been interesting to investigate the following questions:
1. *What is the influence of the three types of features used by the experts ($z$, $x$ and $d$)?* 
   Figure 3b only partially answers this question by showing how frequently the different experts are selected by the gating function. It does not show to which extent the different features are able to substitute each other, i.e., it would be interesting to investigate ablations of GETS without different subsets of experts/features being part of the pool. For example, it is unclear if the performance gains are due to the combination of all three features or if a subset is sufficient. A more detailed analysis of the feature importance would be beneficial, possibly by evaluating the performance when using only pairs of features or even single features.
2. *How well does a GETS-like MoE approach with a structure-unaware MLP instead of a GNN work?* While the evaluated ETS calibration approach also uses the idea of combining multiple calibrators, those calibrators do not use the combinations of $z$, $x$ and $d$ used by GETS. Isolating the effect of this choice of features on the calibration performance would be interesting. A related work in this direction by Liu et al. (2022) [1] could be considered here. It is not clear if the performance gains are solely due to the GNN architecture or if the specific combination of features is more important. An ablation study replacing the GNN with an MLP would help to clarify this.
3. *Are other structural features than the degree count $d$ also useful for calibration?* There is an overlap in the information provided by the node degree inputs and the graph convolutions performed by each expert. As an addition to the previous point, it would be interesting to investigate whether other structural features (e.g., other node centrality measures or node2vec-like embeddings) can serve as effective surrogates to the structural information that is incorporated via the graph convolutions in each calibrator. The paper does not explore the use of other structural features, such as betweenness centrality or clustering coefficients, which could potentially provide complementary information to the degree count. It is unclear if the degree is the optimal choice or if other structural features could lead to improved performance.

### Questions
Apart from the suggestions/questions described in the weaknesses, I only have two minor questions:
1. You report that the GATS calibration approach suffers from OOM problems not present in the other methods. In Section 5.3 you note that the main difference between CaGCN and GATS, time-complexity-wise, lies in the addition of the attention heads $H$. If all computations are parallelized in memory, I would therefore assume the space complexity to be similar. However, in supplement A1.3, you state that you used $H=2$, which appears to be reasonably small, especially considering the fact that $H$ is only a linear factor in the complexity. Does GATS really require orders of magnitude more memory than the other approaches or were the OOM-issues caused by GATS requiring slightly more memory than available? If the former, do you have an explanation as to why this is the case?
2. As I understand, GETS performs temperature scaling (TS) for each vertex. In your experiments, you also evaluated vector scaling (VS). Have you also considered a variant of GETS that uses VS instead of TS?

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
4

### Summary
This paper addresses a critical challenge in graph node classification: the issue of calibration. The authors propose a  method that integrates a combination of features, logits, and node degree within a framework of expert models, aiming to enhance the calibration performance in graph model. By innovatively focusing on the calibration aspect, the study offers new insights into improving the reliable of graph neural networks.

### Strengths
The authors propose a method that leverages node features, logits, and node degree, combined with a framework of  expert models, to enhance the reliability of node predictions. Through extensive experiments, the authors demonstrate the effectiveness of their method compared to existing baselines.

### Weaknesses
1. This paper lacks adequate theoretical backing for why using features, logits, and degree with experts can effectively address calibration issues. Specifically, the paper does not provide a clear explanation of how these three inputs interact to influence the calibration of the model's predictions. Furthermore, it remains unclear why other potentially relevant node factors, such as different types of node embeddings or structural features beyond degree, are not considered. A more rigorous justification for the chosen inputs is needed, including an analysis of their individual and combined effects on calibration.

2. The paper does not explain the mechanism by which the chosen experts resolve calibration issues. It's unclear how these experts are designed to capture different aspects of the calibration problem, and why a single model cannot achieve the same performance. The lack of a clear rationale for using a mixture of experts, rather than a single, more complex model, raises concerns about the novelty and the theoretical grounding of the approach. The paper also does not discuss the potential limitations of the expert selection process, such as the possibility of suboptimal expert choices for certain nodes.

3. The baseline models used in the experiments, particularly the graph calibration model baselines, are outdated. For instance, CAGCN was published in NeurIPS 2021 and GATS in 2022. The field of graph neural network calibration has progressed significantly since then, and the use of older baselines makes it difficult to assess the true contribution of the proposed method. It is recommended that the authors update their baseline models to include more recent and state-of-the-art calibration techniques to enhance the comparability and validity of their approach.

### Questions
My questions can be found in weakness.

### Soundness
2

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
This work leverages multiple GNNs with different inputs within a Graph Mixture-ofExperts (MoE) architecture for confidence calibration of GNNs.

### Strengths
- Paper is written well and easy to read.

- The proposed framework is intuitional and the design choices are justified. 

- Experimental results are thorough and enough empirical analyses are provided.

- Proposed method seems to perform well compared to the selected baselines.

### Weaknesses
 - More recent baselines can be included to further strengthen experimental results.

- The novelties of the proposed framework seem to be rather limited based on the current presentation. It would be better to clearly emphasize the novelties over the existing solutions in the Related Work.

### Questions
Please see weaknesses.

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces Graph Ensemble Temperature Scaling (GETS), a calibration framework for Graph Neural Network that combines input and model ensemble strategies with a Graph Mixture-of-Experts architecture. GETS integrates multiple types of inputs and adaptively selects relevant experts for calibrating such node's predictions. The framework achieves improvements in calibration performance across 10 benchmark datasets.

### Strengths
* The comprehensive experimental results in Table 2 show consistent improvements across different architectures and datasets.
* The sparse activation mechanism described in Section 4.2 enables efficient scaling to larger graphs. 
* The well-presented analysis of expert selection patterns provides insights into which input combinations are most effective for calibration for each dataset.

### Weaknesses
 * The hyperparameter sensitivity analysis is somewhat limited, say regarding the number of experts, or the expert embedding dimension. For example, 
 (1) How do calibration performance and computation costs scale with the number of experts (M) ?
 (2) What is the impact of expert network capacity (e.g. the number of neurons, the number of layers) on calibration quality?
 (3) How does the choice of top-k in sparse gating affect the trade-off between performance and efficiency? An empirical experiment on synthetic dataset would provide valuable implementation guide. 

* While computational efficiency is emphasize, the need to store multiple expert models could be problematic for resource-constrained settings. This practical limitation deserves more discussion. For instance, computational memory requirements for different types of experts handling various input might be helpful.

### Questions
1. Could the authors provide quantitative analysis of expert specialization during the training? This could be potentially done by 
 (1) Visualization of expert activation patterns (investigation of gating function values) across training epochs, or
 (2) Per-expert contribution to the total calibration loss over training epochs, or
 (3) Show how the preference for certain experts emerges and stabilizes (again through analyzing the gating function G or gating scores Q)
While Figure 3(b) demonstrates the final expert selection patterns through sparse activation, a dynamic analysis of expert contribution to performance would be valuable.

2. How does the architecture of individual experts impact calibration performance? Given that experts process different input types, different architecture may be more suitable for each input modality. Currently, GCN with 2 layers is used for all types except the integer degree. Does the same GCN architecture uniformly reflect the effects across the experts of different types?

3. How does GETS perform on heterogeneous graphs where nodes have different feature types or varying degrees of connectivity?

### Soundness
3

### Presentation
3

### Contribution
3
