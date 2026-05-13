# Exact Computation of Any-Order Shapley Interactions for Graph Neural Networks

- Decision: Accept
- Scores: 6, 6, 3, 6

## Abstract
Albeit the ubiquitous use of Graph Neural Networks (GNNs) in machine learning (ML) prediction tasks involving graph-structured data, their interpretability remains challenging. In explainable artificial intelligence (XAI), the Shapley Value (SV) is the predominant method to quantify contributions of individual features to a ML model’s output. Addressing the limitations of SVs in complex prediction models, Shapley Interactions (SIs) extend the SV to groups of features. In this work, we explain single graph predictions of GNNs with SIs that quantify node contributions and interactions among multiple nodes. By exploiting the GNN architecture, we show that the structure of interactions in node embeddings are preserved for graph prediction. As a result, the exponential complexity of SIs depends only on the receptive fields, i.e. the message-passing ranges determined by the connectivity of the graph and the number of convolutional layers. Based on our theoretical results, we introduce GraphSHAP-IQ, an efficient approach to compute any-order SIs exactly. GraphSHAP-IQ is applicable to popular message passing techniques in conjunction with a linear global pooling and output layer. We showcase that GraphSHAP-IQ substantially reduces the exponential complexity of computing exact SIs on multiple benchmark datasets. Beyond exact computation, we evaluate GraphSHAP-IQ’s approximation of SIs on popular GNN architectures and compare with existing baselines. Lastly, we visualize SIs of real-world water distribution networks and molecule structures using a SI-Graph.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper introduces GraphSHAP-IQ, an approach to compute any-order Shapley Interactions exactly. The authors focus on explanations for fro graph classification task. First thing, they introduced GNN-induced Graph and Node Game, they show the invariance of the node game with respect of masking outside its $\ell$ neighbourhood, where $\ell$ is the number of layers of the GNN. 
Exploiting this they also show that for GNN the complexity of MIs depends only linearly in the saize of the graph and exponentialy in the connectivity of the graph. Finally experiments on real world dataset are reported.

### Strengths
-  The mehtod introduced in the paper is novel. 
-  The method is sound  and  the authors provide robust theoretical results. 
- The authors validate their approach with experiments on diverse datasets, including real-world datasets.

### Weaknesses
 - Adding information on the algorithm's running time across different datasets and compare it with the running time of the baselines would provide more information about the applicability of the method. 
- The method's efficiency heavily depends on graph sparsity and the size of receptive fields. For very dense or large graphs, the complexity may still be prohibitive. Specifically, while the method scales linearly with the number of nodes, the exponential dependence on the size of the largest l-hop neighborhood remains a significant limitation for highly connected graphs. 
- The algorithm assumes linear global pooling and output layers, which limits its direct application to non-linear readouts.

### Questions
- The paper addresses the problem for graph classification. Could this approach be extended to node classification? 
- Could we use a different baseline choise intead of the mean.  Such as a random baseline and a learned baseline ?

Typo: 
- Line 421 "ground truth " shold be "Ground truth".

### Soundness
3

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
3

### Summary
This paper identifies an invariance property in node games on graphs and demonstrates that the exponential complexity of Shapley Interactions depends only on the receptive fields of graph neural networks. Leveraging this insight, the authors propose GraphSHAP-IQ, a method for efficiently computing any-order Shapley Interactions for graph neural networks. They also introduce an approximate version of GraphSHAP-IQ, which restricts computation to the highest order of Möbius Interactions. Finally, the authors propose a visualization technique for Shapley Interactions using SI-Graph and validate their approach through experiments on various real-world applications.

### Strengths
- The proposed GraphSHAP-IQ method demonstrates high efficiency.
- The authors provide theoretical guarantees for GraphSHAP-IQ's computational complexity.
- Extensive experiments on real-world applications are conducted, with results clearly illustrated. Notably, the introduction of the WAQ dataset adds valuable tools for evaluating explanation methods on graphs.
- The paper is well-written and easy to follow.

### Weaknesses
 - **Novelty**: The primary contribution of this paper lies in reducing the computational complexity of Shapley Interactions through node game invariance, limiting the calculation of Shapley Interactions within the receptive field of the graph neural network. However, this approach is not entirely novel, as it was previously proposed in other works. For example, Section 5.4 of [1] states:

  > Indeed, for a GNN model with $k$ layers, only $k$-hop neighbors of $v$ can influence the prediction for $v$, and thus receive a non-zero Shapley value. All others are allocated a null importance according to the dummy axiom and can therefore be discarded.

  Extending this approach from model-agnostic to structure-aware approximation may offer limited novelty on its own.

- **Experiments**: In Figure 4, the authors claim that GraphSHAP-IQ achieves better approximation quality than other methods, by comparing their MSE **at the same number of model evaluations**. However, as noted in the previous point, GraphSHAP-IQ’s performance advantage could be attributed simply to disregarding nodes outside the GNN’s receptive field, thereby requiring fewer model evaluations. Thus, the assertion that GraphSHAP-IQ provides superior approximation quality is unconvincing. A more balanced evaluation would involve applying the same efficiency optimization across all methods and comparing results to see if GraphSHAP-IQ still outperforms. Specifically, the comparison should isolate the impact of the receptive field optimization from other factors. The current experimental setup does not adequately demonstrate the unique benefits of the proposed method beyond this optimization.

- **Minor Issues**: The vertical spacing between paragraphs appears missing. Additionally, some capitalized terms (e.g., SV, SI, MI) and the term “BShap” contain hyperlinks that link incorrectly to the first page of the paper.

### Questions
See weaknesses.

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
2

### Summary
The paper studies the interpretability of graph neural networks (GNNs) via Shapley Interactions (SIs). Specifically, it explores quantifying node contributions by computing exact SIs. The paper proposes an any-order SIs computation method named GraphSHAP-IQ, which can significantly reduce the complexity of exact SIs computation. Finally, it conducts extensive experiments to validate the effectiveness of GraphSHAP-IQ and complexity reduction.

### Strengths
- The figures on the paper are well-constructed and clearly convey the intended information.

### Weaknesses
 - The writing in the paper needs significant improvement, as it currently makes it difficult for readers to follow the arguments and content. The issues with the writing can be summarized as follows: (1) The overall logic and flow of the paper are unclear, which hinders comprehension. (2)Several grammatical errors detract from the clarity and professionalism of the manuscript.

- The motivation for the study is not clearly articulated and does not come across as compelling. This appears to be a result of suboptimal writing throughout the paper.

- The review of related work appears to be somewhat disorganized, and it would be beneficial to provide a more detailed comparison with similar methods, such as TreeSHAP.

- The experiments provided do not convincingly demonstrate the effectiveness of the method in reducing complexity. Additional or more targeted experiments may be needed to better support this claim.

### Questions
What is the purpose of showing the performance of GNN vanilla in Table 1?

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a method for efficient calculation of exact and approximate any-order Shapley Interactions by leveraging GNN structure and node receptive fields to filter out trivial interactions, eliminating unnecessary computations and significantly accelerating processing. For highly connected graphs or very deep GNNs, the paper introduces an approximation technique to ensure computational feasibility. Experiments demonstrate substantial acceleration and low error for the approximation method.

### Strengths
1.	The figures are well plotted, particularly Fig. 2.
2.	This paper takes an innovative approach by leveraging the structural characteristics of GNNs to accelerate the computation of any-order Shapley Interactions, while ensuring exact results.
3.	The experiments cover a diverse range of datasets and GNN architectures, providing comprehensive qualitative and quantitative results that demonstrate the method’s efficiency and low approximation error.

### Weaknesses
1. The restriction to a linear readout function may limit the method’s broader applicability. Specifically, many GNN models utilize non-linear activation functions in their readout layers to capture complex relationships between node embeddings and the final prediction. This linear restriction could lead to inaccurate or incomplete explanations for models with non-linear readouts, potentially hindering the method's use in real-world applications where non-linearities are common.
2.	Higher-order interactions could make the interpretations for the visualization more challenging for users. While the paper introduces a method for calculating any-order Shapley Interactions, the complexity of visualizing and understanding these interactions increases exponentially with the order. For example, visualizing 3-way or 4-way interactions can be difficult to interpret, potentially limiting the practical utility of higher-order explanations for end-users who may struggle to extract meaningful insights from such complex visualizations.
3.	The extensive use of varied notations can be difficult to follow without a notation table. The paper introduces several new notations and symbols, which, without a clear and concise notation table, can make the paper difficult to read and understand. This can be especially challenging for readers who are not already familiar with the specific notations used in the field of explainable AI and graph neural networks.

### Questions
1. In Fig.4 right, it seems that we can just plot the top-k most important 2-node group to remove the unimportant ones and get a clearer visualization. And the top relevant groups seem to be the same, i.e, N-O? It would be interesting to compare the top-k most important groups of the exact SHAP and approximated SHAP.
2. Accuracy and computation expense needs trade-off when using SHAP. How much faster/slower is the proposed method than other approximation methods of SHAP? A figure with computation expense as x-axis, MSE as y-axis and each method as a point would be useful for users to decide when to use which method.
3. Is the proposed method extendable to other models? E.g., for CNN, where each input pixel also has receptive fields.

### Soundness
3

### Presentation
3

### Contribution
3
