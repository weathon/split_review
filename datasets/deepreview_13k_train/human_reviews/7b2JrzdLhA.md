# Graph Neural Ricci Flow: Evolving Feature from a Curvature Perspective

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
Differential equations provide a dynamical perspective for understanding and designing graph neural networks (GNNs). By generalizing the discrete Ricci flow (DRF) to attributed graphs, we can leverage a new paradigm for the evolution of node features with the help of curvature. We show that in the attributed graphs, DRF guarantees a vital property: The curvature of each edge concentrates toward zero over time. This property leads to two interesting consequences: 1) graph Dirichlet energy with bilateral bounds and 2) data-independent curvature decay rate. Based on these theoretical results, we propose the Graph Neural Ricci Flow (GNRF), a novel curvature-aware continuous-depth GNN. Compared to traditional curvature-based graph learning methods, GNRF is not limited to a specific curvature definition. It computes and adjusts time-varying curvature efficiently in linear time. We also empirically illustrate the operating mechanism of GNRF and verify that it performs excellently on diverse datasets.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper introduces the dynamical system Attribute Discrete Ricci Flow (Attri-DRF) and incorporates this to propose the Graph Neural Ricci Flow (GNRF), a curvature-aware continuous GNN. This ensures that the graph Dirichlet energy can be bilaterally bounded and that the curvature decay to 0 independent of data. Using an auxiliary network (EdgeNet), the model can theoretically incorporate different types of curvature definition. GNRF has excellent performance on many data sets against a variety of discrete and continuous GNNs.

### Strengths
Theoretically, the paper provide several interesting results. 
1. Section 3 provides guarantees on the curvature decay rate and the stable curvature limit of Attri-DRF when certain conditions are met, along with providing a bound on the Dirichlet energy when the curvature stabilizes. This indicates it may be able to avoid over-smoothing/over-squashing. 
2. Incorporating recent results, the paper uses an auxiliary network (EdgeNet), which is capable of approximating arbitrary edge curvature with high precision.

Experimentally, the paper performs well on a variety of popular node classification tasks against a number of old and new discrete and continuous GNN architectures. Section 5.2 and 5.1 provides good evidence that theoretical guarantees hold in reality.

### Weaknesses
1. It is not clear to the reviewer how the theoretical results tie together/what assumptions are made at each step of the way.
2. The design of EdgeNet is glossed over within the paper, with only a few formulas mentioned within either the main paper or the appendix to explain it. There's also no comparison between EdgeNet's curvature values compared against any other type of curvature that it supposedly can approximate.
3. The datasets used in the experiments are relatively small datasets.

### Questions
1) Why does having a data-independent curvature decay rate a good thing?
2) Where does equation (3) come from? I checked the Ollivier paper and I can't find this equation there.
3) Does GNRF satisfy the theoretical results in Section 3. If it does, it would be great if the authors can clarify this a bit more within the paper.
4) Over-smoothing and over-squashing are problems caused by the message-passing design in GNNs. Considering that GNRF does not strictly adhere to the message passing design, is it appropriate to mention these problems in this work?
5) Does GNRF work on larger datasets?

### Soundness
3

### Presentation
2

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
his paper introduces Graph Neural Ricci Flow (GNRF), designed to model a dynamic system called Attribute Discrete Ricci Flow (Attri-DRF) on graph.
Unlike traditional GNNs, which use multiple layers and pass outputs from one layer as inputs to the next, the model in this work employs only a single layer.  Instead, it iteratively updates node features and curvatures—treated similarly to edge weights—over discrete time steps according to the Attri-DRF ODE.

### Strengths
1. The model dynamically learns the curvature instead of relying on precomputed values, enabling it to adapt in response to both internal hidden features and the graph’s topology. 
2. This approach is closely aligned with the heat flow equation.
3. As shown in Figure 3, the proposed framework achieves stable curvature over sufficient time steps. At the same time, the curvature concentrates around zero that can facilitate smoother information flow across the graph.

### Weaknesses
1. The network architecture used in this framework is relatively general. And it would be valuable to discuss the potential benefits of using more complex GNN architectures, such as Graph Transformers, which have shown strong performance on various graph tasks. Moreover, exploring the motivation behind the proposed framework with other related works that focus on graph curvatures could provide additional insights. Specifically, a discussion of how this method relates to curvature-based edge sampling techniques and weighted aggregation methods would be beneficial.

2. The experiment primarily focuses on node classification tasks on small-scale graphs. To better validate the effectiveness of the proposed framework, applying it to larger graphs would be beneficial. For example, the ogbn-arxiv dataset could serve as a graph classification dataset with GNNs as baselines. Additionally, for non-homophilous graph datasets, larger datasets and relevant baselines are available in [4]. It would also be valuable to evaluate the performance on datasets with varying graph sizes and structures to understand the scalability of the proposed method.

3. An efficiency study would be helpful. The computational cost of applying the ODE method should be explicitly discussed so readers can better understand its applicability. For instance, comparing parameters, training time, and GPU memory usage between this approach and other GNNs, such as GCN and GAT, would clarify its potential advantages and trade-offs. Furthermore, it is important to analyze the computational complexity of the proposed method in comparison to standard GNN models, considering both time and space complexity.

### Questions
1. Could you share your thoughts on the relationship and differences between the curvature predicted in this architecture and edge attention mechanisms? And do you think it is possible to apply attention mechanism in the framework?

2. In EdgeNet, are the edge features from the previous time step used as input for the current time step? Equation 13 suggests that the previous edge features should be used, but the code appears to rely only on the previous node features without incorporating the prior edge features.

3. What is the formulation for updating node features at each subsequent time step? As a suggestion, including an illustrative figure or a pseudo-algorithm would help readers gain a clearer understanding of the overall framework.

4. While there is only one layer in the implementation, is it possible to apply a multiple layer GNN? And is it possible to connect layers with time steps in this case?

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
3

### Summary
The paper proposes a continuous GNN dynamics, namely GNRF by incorporating curvature based on the Ricci flow. In particular, by expressing edge weights as a function of node features, GNRF propagate features following a discrete (graph) Ricci flow. In order to avoid the costly computation of Ricci curvature on graphs, the paper proposes an auxiliary network for modeling curvature and learned end-to-end.  The paper provides several theoretical guarantees in terms of bounded Dirichlet energy and fast curvature decay. The experiments support the effectiveness of the method.

### Strengths
1. Compared to curvature-based graph rewiring, it is interesting and natural to incorporate Ricci curvature into the propagation of node features.

2. Theoretical developments are supportive of the claims.

### Weaknesses
1. It is unclear how EdgeNet approximates edge curvatures? In particular, given there are trainable parameters and in the experiments, EdgeNet is trained end-to-end with supervision only from the task, instead of actual curvature. How to ensure EdgeNet approximates the curvature in this case? It seems that the learned edge weights are only implicitly related to curvature, making it difficult to interpret the model's behavior in terms of the underlying geometric structure.

2. Theorem 5 is unclear. Does this mean there exists some network \phi_1, \phi_2 such that the network can approximate any curvature? Please give more explanations. The statement lacks precision regarding the specific properties of the network architecture that enable this approximation. It is not clear if the approximation holds for all possible graph structures and feature distributions.

3. Even though the theory is well-developed, the main GNN algorithm in (14) seems to resemble GRAND, especially the EdgeNet seems to act like a re-weighting term as in graph attention. How does EdgeNet differ to the graph attention module? Can you add experiments to verify the difference? The current explanation does not provide a clear distinction between the proposed approach and existing attention mechanisms, and the lack of comparative experiments makes it difficult to assess the novelty of the approach.

### Questions
1. In Line 285, the paper claims the sign of EdgeNet_ij aligns with the sign of k_ij. I am not sure how this is achieved without the supervision from the actual curvature. 

2. In Line 175 of Theorem 2, w_ij should be changed to k_ij?

3. In Section 5.1, the curvature seems to be computed from the EdgeNet? What about the actual curvature?

4. I am also curious whether there could be improvements when EdgeNet is replaced with actual curvature? This could be part of ablation study.

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
The paper introduces Graph Neural Ricci Flow (GNRF), a novel method for evolving node features in Graph Neural Networks (GNNs) using a differential equation-inspired approach based on the Ricci flow. The authors generalize the Discrete Ricci Flow to attributed graphs, where each edge's curvature converges toward zero over time. This has two key consequences: it bounds the graph's Dirichlet energy and provides a data-independent curvature decay rate. GNRF is unique because it computes time-varying curvature efficiently in linear time, unlike traditional curvature-based methods, which are typically precomputed and limited to specific curvature definitions. 

The motivation behind the GNRF stems from the limitations of existing GNNs that rely on heat diffusion equations, which often lead to over-smoothing. Instead, the paper explores an alternative differential equation—Ricci flow—to mitigate over-smoothing and create more stable, non-smooth node representations. This innovative approach contrasts with traditional methods that view curvature as a static, precomputed property tied only to graph topology. By allowing curvature to evolve with node features, GNRF enables more dynamic and flexible graph learning.

### Strengths
- Novelty: The paper introduces an interesting and innovative approach with GNRF, applying Discrete Ricci Flow to attributed graphs in a novel way. By allowing edge curvature to evolve dynamically with node attributes, GNRF moves beyond the limitations of traditional methods that rely on static, precomputed curvature. Its ability to work with any curvature definition and to compute curvature in linear time addresses key concerns around scalability and efficiency. This flexibility offers a practical and effective way to handle common challenges such as over-smoothing and over-squashing in graph neural networks. Overall, GNRF presents a meaningful advancement in curvature-aware graph learning.
- Theoretical results: The paper offers solid theoretical contributions that help establish the soundness of the Attribute Discrete Ricci Flow framework. One key result is the demonstration that edge curvature naturally converges toward zero, ensuring a stable evolution of node features and addressing potential issues like over-smoothing and over-squashing. The bounding of the Dirichlet energy provides additional assurance that node representations maintain a balance between being too homogeneous or too distinct.

### Weaknesses
 - Limited experimental results: The paper's experimental evaluation has some limitations. The focus is exclusively on node classification tasks, raising the question of why the method wasn't tested on other common tasks like graph classification or regression, which would provide a broader view of its applicability. Additionally, of the seven node classification datasets used, three (Cornell, Wisconsin, and Texas) are notably small, making it difficult to draw definitive conclusions about the method’s performance on more challenging or larger-scale data. Furthermore, on two of the larger datasets (Cora_Full and PubMed), the proposed method performs only within the statistical margin of error compared to the baselines, which limits its ability to demonstrate a clear and significant improvement over existing methods. Overall, I believe the paper would benefit significantly if the authors added some experimental results on graph classification/ regressions tasks, for example the LRGB datasets.
- Baseline comparisons: The paper’s comparison with baseline methods raises some concerns regarding its evaluation methodology. Specifically, on the Tolokers and Roman Empire datasets, the authors use a 60/20/20 train/validation/test split, but the results reported for baseline models like GCN are significantly lower than what is found in the original work, which used a 50/25/25 split. When compared with the results in “A Critical Look at the Evaluation of GNNs under Heterophily” (2023), the proposed method (82.55 on Tolokers) does not seem to outperform a simple baseline like GCN on Tolokers (83.64), raising questions about whether the method truly offers improvements in these settings.

### Questions
Could the authors explain why they are only using the Tolokers and Roman Empire datasets from “A Critical Look at the Evaluation of GNNs under Heterophily” and not the three other node classification datasets?

### Soundness
3

### Presentation
2

### Contribution
3
