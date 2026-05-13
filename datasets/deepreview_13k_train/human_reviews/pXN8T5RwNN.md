# Explanations of GNN on Evolving Graphs via Axiomatic  Layer edges

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
Graphs are ubiquitous in social networks, chemical molecules, and financial data, where Graph Neural Networks (GNNs) achieve superior predictive accuracy. Graphs can be
evolving, while understanding how GNN predictions respond to the evolution provides significant insight and trust. 
We explore the problem of explaining evolving GNN predictions due to continuously changing edge weights.
We first propose a layer edge-based explanation to balance
explanation fidelity and interpretability, as opposed to message flow and input edge.
Then we propose a novel framework to address the challenges of axiomatic attribution and the entanglement of multiple computational graph paths due to continuous change of edge weights. We first design an axiomatic attribution of the evolution of the model prediction to message flows, then develop Shapley value to fairly map message flow contributions to layer edges.
We formulate a novel optimization problem to find the critical layer edges based on KL-divergence minimization. Extensive experiments on eight datasets for node classification, link prediction, and graph classification tasks with evolving graphs demonstrate the better fidelity and interpretability of the proposed method over the baseline methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents Axiom Layer Edge, a novel explanation framework designed for dynamic graph learning models, particularly focusing on Graph Neural Networks (GNNs). The framework aims to identify the most influential "layer edges" — connections within the GNN layers that have a significant impact on the model’s predictions. This approach is based on the use of Shapley values to fairly attribute contribution scores to individual layer edges and provides a principled and interpretable explanation for prediction shifts that occur as the graph changes over time. The results on several datasets and graph task show that method outperforms other existing baseline methods.

### Strengths
- The work focuses on problem of explainability in evolving/dynamic graphs which is an important task
- Extending concepts of shapley value to many dynamic graphs is also key contribution of the work
- The work aims to focus on the trade-offs between quality of interpretablity and fidelity

### Weaknesses
 - Applying shapley value and KL divergence to large or highly dynamic graphs can be challenge especially due to combinatorial nature of computation
- No theoretical analysis on computation complexity is provided for evolving graphs
- There are several limitations with Shapley such as the lack of robustness, stability etc [1]. It is unclear what are the limitations of Shapley in this setting.

### Questions
- It would be helpful if the authors can justify the use of Shapley value instead of other game-theoretic methods  (e.g., core, Banzhaf etc)?
- How can we approximate the calculations of shapley and KL divergence in large/dynamic graphs?

- Can we have a discussion on the usefulness of the explanations from the point of view domain experts? Also, are the explanations stable to graph operations like attention, pooling, etc.?

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
2

### Summary
This paper works on the problem of explaining challenges in GNNs' predictions when the weights of the input edges are continuously changing. Prior work has weaknesses in axiomatic attribution of message flows, unfair distribution, and optimality. The proposed algorithm from the authors addresses the challenges by decomposing the changes in the message flow and introducing the Shapley value for fair attribution. Extensive experiments have been conducted to show the effectiveness of the proposed method. The paper is well-written and organized.

### Strengths
The intuition behind this paper is interesting and novel. The design of the framework is feasible and detailed explained. There are also sufficient experiments to demonstrate the effectiveness of the proposed methods.

### Weaknesses
The goal of this paper is to address the challenges of explanation on GNN in evolving graphs. Thus, it should include more dynamic graph baselines instead of simply using static GNNs. The current evaluation primarily focuses on static GNNs applied to evolving graphs, which does not fully validate the method's effectiveness in truly dynamic scenarios. The paper lacks a thorough analysis of how the proposed evaluator behaves across the temporal dimension. Specifically, it's unclear how the Shapley values change over time and whether these changes accurately reflect the evolving importance of different edges. The experimental section should include a more detailed analysis of the temporal dynamics of the explanations.

### Questions
1. There are typos in line 221. Please carefully check them.
2. As the goal of this paper is to understand how GNN predictions respond to the evolution of graphs. However, in this paper, the GNNs are all static GNNs. What is the effectiveness of the proposed method in explaining the dynamic GNN methods? For example, TGN or TGAT?
3. What is the relationship between the Shapley value through temporal dimension? Does the proposed method capture the influence of evolving nature in dynamic graphs?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a method for the explainability of evolving graphs, where edge weights of a graph changes over time. The authors explore this problem across three tasks of node classification, link prediction, and graph classification and show that their approach demonstrates superior performance compared to other baselines. Furthermore, in their problem setting Pr(Y |G0; θ) will evolve to Pr(Y |G1; θ), and they aim to explain the evolution of Pr(Y |G; θ) with respect to G0 → G1. They formulate the changes in hidden vectors on G0 and G1 and apply chain rule of DeepLIFT to assign the changes in logits to message flows. Finally, they show that their approach outperforms other baselines on KL divergence metric.

### Strengths
- The problem of explainability for Graph Neural Networks (GNNs) in the context of evolving graphs is both interesting and novel. 

- The proposed model demonstrates superior performance compared to other baseline methods.

### Weaknesses
 - The metric used for evaluation is not clearly justified. There are standard metrics, such as fidelity, that could provide a better understanding of the method's performance. Specifically, the paper lacks a clear explanation of why KL divergence is suitable for evaluating the explanation of evolving graphs, and how it relates to the actual changes in the graph structure and node features. It is unclear how the KL divergence captures the quality of the explanations in terms of identifying the most influential edges that cause the change in prediction.
- For an explainability method, it is crucial to include at least one visualization of a dataset. This would allow readers to visually assess the method's effectiveness. The absence of visualizations makes it difficult to understand the practical implications of the proposed method and how well it can identify the important changes in the graph. For example, visualizing the changes in edge weights and their corresponding impact on node classification or link prediction would be very helpful.
- It would be beneficial to experimentally demonstrate that this method works with different Graph Neural Networks (GNNs). Additionally, including a table that shows the performance of the pre-trained GNNs across various datasets would be helpful. The current evaluation is limited to a single GNN architecture, and it is unclear whether the proposed method can generalize to other GNN models, such as GAT or GraphSAGE. Furthermore, the lack of a detailed performance table for the pre-trained GNNs makes it difficult to assess the overall quality of the base models used for evaluation.

### Questions
- What pre-trained GNN has been used in this work?
- Could you provide visualizations of your results for datasets such as MUTAG?
- What is the rational behind choosing KL divergence as the evaluation metric?

### Soundness
3

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
4

### Summary
This paper provides explanations for predictions on evolving graphs. In the case of continuously changing edge weights, the authors propose an explanation method based on Axiomatic Layer Edges, mapping the contribution of message flows to layer edges using Shapley values, and selecting key layer edges by minimizing the KL divergence optimization problem. Experimental results show that this method outperforms existing baseline methods across multiple datasets and tasks.

### Strengths
1. The paper presents an explanation method based on layer edges, which can more accurately capture the variations in message passing, thereby improving the fidelity of the explanations. The method is innovative.
2. The authors explain prediction changes by selecting a small number of key layer edges at multiple scales through a KL divergence-based optimization problem.
3. The paper conducts experiments on multiple datasets and tasks, including node classification, link prediction, and graph classification tasks.

### Weaknesses
1. The authors should conduct a complexity analysis, as the computation of Shapley values generally has a high complexity. Additionally, since the authors select a small number of key layer edges in their method, will this impact the complexity of the model? Specifically, how does the selection of a subset of layer edges affect the convergence rate of the optimization process, and what are the implications for scalability to larger graphs with more complex edge dynamics?
2. In this paper, the authors use a series of carefully designed methods to balance the fidelity and interpretability of explanations. However, I still have a question: is there an optimal balance point (for example, the optimal point reached in Figure 2(b))? It is unclear how this balance is achieved in practice, especially when the number of layer edges becomes very large. The paper should provide more insight into how the method adapts to varying levels of graph complexity and the trade-offs involved in selecting the number of key layer edges.
3. The paper assumes that changes in edge weights are continuous; however, could the authors also explore sudden or discontinuous changes (such as the addition or deletion of nodes or edges)? Changes in graph structure can be quite complex and unpredictable, which may affect the robustness of the method. The paper needs to address the limitations of the approach when dealing with non-continuous changes, and how the method would handle the introduction of new nodes or edges that were not present in the original graph.

### Questions
See Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
4
