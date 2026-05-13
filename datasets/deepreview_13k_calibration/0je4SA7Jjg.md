# Spatiotemporal Learning on Cell-embedded Graphs

- Decision: Reject
- Avg Score: 6.50
- Scores: 10, 6, 5, 5

## Abstract
Data-driven simulation of physical systems has recently kindled significant attention, where many neural models have been developed. In particular, mesh-based graph neural networks (GNNs) have demonstrated significant potential in predicting spatiotemporal dynamics across arbitrary geometric domains. However, the existing node-edge message passing mechanism in GNNs limits the model's representation learning ability. In this paper, we proposed a cell-embedded GNN model (aka CeGNN) to learn spatiotemporal dynamics with lifted performance. Specifically, we introduce a learnable cell attribution to the node-edge message passing process, which better captures the spatial dependency of regional features. Such a strategy essentially upgrades the local aggregation scheme from the first order (e.g., from edge to node) to a higher order (e.g., from volume to edge and then to node), which takes advantage of volumetric information in message passing. Meanwhile, a novel feature-enhanced block is designed to further improve the performance of CeGNN and relieve the over-smoothness problem, via treating the latent features as basis functions. The extensive experiments on various PDE systems and one real-world dataset demonstrate that CeGNN achieves superior performance compared with other baseline models, particularly reducing the prediction error with up to 1 orders of magnitude on several PDE systems.

## Human Reviews

## Human Reviewer 1

### Rating
10

### Rating Number
10

### Confidence
5

### Summary
In general, this paper tackles interesting and meaningful problems governed by PDE. It is well written and the results are sound.

### Strengths
Ablation study is pretty great to justify the proposed framework.

### Weaknesses
The methodology of feature-enhanced is not sufficient, the authors should write down in the appendix more equations with more explanation. Most importantly, why do authors propose such Algorithm 1, is there any physical or mathmatical meaning/inspiration? or any hypothesis? It would be better to show the train of thoughts of how did author propose this FE instead of just showing its working better.

### Questions
See weaknesses

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The authors proposed a cell-embedded GNN model (aka,CeGNN) to learn spatio-temporal dynamics. They claim that their learnable cell attribution to the node-edge message passing process better captures the spatial dependency of regional features.

### Strengths
1. The paper is easy to follow.
2. We can see detailed description of the technical details
3. This paper touches the core problem in this area.

### Weaknesses
1. The most puzzling aspect of this paper is that the discussion of related work and the selection of baselines are all based on studies from before 2022. In fact, there have been many breakthrough studies on both graph-based methods and other neural operator approaches in recent years [1].

2. This work appears more like a straightforward extension of MP-PDE, both in terms of methodology and experiments. The paper proposes a cell-based method for extracting spatial relationships, but how much improvement could be observed if this feature were integrated into MP-PDE?

3. The main experimental results are somewhat confusing. Since the code is not available, it is unclear whether the training data was generated from the authors' own simulations or from public datasets, and what the training dataset size is. If the data is self-generated, the comparison with a few simple baselines is not convincing. Furthermore, the authors mention long-term simulations, yet all experiments are based on one-step predictions, which is clearly insufficient.

4. Regarding the core innovation of this paper, the cell feature is merely a learnable feature initialized by the distance to the cell center. Can its significance be verified by theoretical analysis or by measuring the distance between cell features and node features? The benefit here might simply be from adding position awareness, which makes the model fit specific data better. It could even be considered to replace the distance to the cell center with the distance to the nearest PDE boundary for each point, which might also yield improvements.

### Questions
See weakness above

### Soundness
2

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
3

### Summary
The paper presents a new model, the Cell-Embedded Graph Neural Network (CeGNN), for simulating spatiotemporal dynamics across different physical domains. CeGNN introduces learnable cell attributions to the traditional node-edge message-passing process, upgrading it to a higher-order scheme that captures volumetric information and improves spatial dependency learning. Additionally, the Feature-Enhanced (FE) block enriches feature representations, tackling the over-smoothness issue common in Graph Neural Networks (GNNs). Extensive experiments demonstrate that CeGNN achieves superior performance and generalization in predicting physical dynamics, particularly for Partial Differential Equations (PDEs) and real-world datasets.

### Strengths
Good empirical results.

### Weaknesses
The main weakness is lack of novelty. The main idea of this paper is the proposal of cell-attribution. In the field of topological learning, there have been several prior works proposing the idea of higher-order message passing, cell / simplicial complex neural networks. Please check the following literature:

(1) Topological Deep Learning: Going Beyond Graph Data (this is a great survey of Topological Deep Learning)
https://arxiv.org/abs/2206.00606

(2) Cell Complex Neural Networks
https://arxiv.org/abs/2010.00743

(2) Weisfeiler and Lehman Go Topological: Message Passing Simplicial Networks (for simplical complexes)
https://arxiv.org/abs/2103.03212

However, application of these topological methods in the domain of learning physical systems is new.

### Questions
Please address the weakness in novelty that I have raised!

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes an end-to-end graph-based framework called CeGNN to address limitations of existing Graph Neural Networks in learning complex spatiotemporal dynamics, particularly the over-smoothing issue, and aims to enhance prediction accuracy and generalization ability. The authors introduce two key components: Cell-embedded MPNN block and Feature-Enhanced (FE) block. Through experiments on several PDE systems, the paper demonstrates that CeGNN outperforms other baseline models.

### Strengths
- The paper is well-organized and easy to follow.

- The authors present abundant experimental results and visualizations to validate their ideas.

- CeGNN achieves superior performance compared to the compared methods.

### Weaknesses
 - The baseline methods are relatively weak. The authors did not include recent advancements in the field from 2023-2024, raising concerns about the effectiveness of the proposed method.

- Modeling with higher-order graphs is a widely studied topic. Can the authors more explicitly summarize the contributions of CellMPNN compared to existing approaches?

- The paper lacks a theoretical discussion on the effectiveness of CeGNN. Can the authors discuss the source of CeGNN's effectiveness from a theoretical perspective?

- FE modules are not clearly defined.

### Questions
Please address the weaknesses mentioned above.

### Soundness
1

### Presentation
3

### Contribution
3
