# Topological Blindspots: Understanding and Extending Topological Deep Learning Through the Lens of Expressivity

- Decision: Accept
- Scores: 8, 8, 8

## Abstract
Topological deep learning (TDL) facilitates learning from data represented by topological structures. The primary model utilized in this setting is higher-order message-passing (HOMP), which extends traditional graph message-passing neural networks (MPNN) to diverse topological domains. Given the significant expressivity limitations of MPNNs, our paper aims to explore both the strengths and weaknesses of HOMP's expressive power and subsequently design novel architectures to address these limitations. We approach this from several perspectives: First, we demonstrate HOMP's inability to distinguish between topological objects based on fundamental topological and metric properties such as diameter, orientability, planarity, and homology. Second, we show HOMP's limitations in fully leveraging the topological structure of objects constructed using common lifting and pooling operators on graphs. Finally, we compare HOMP's expressive power to hypergraph networks, which are the most extensively studied TDL methods. We then develop two new classes of TDL models: multi-cellular networks (\ourmethod) and scalable multi-cellular networks (SMCN). These models draw inspiration from expressive graph architectures. While \ourmethod can reach full expressivity but is highly unscalable, \secondmethod offers a more scalable alternative that still mitigates many of HOMP's expressivity limitations. Finally, we construct a synthetic dataset, where TDL models are tasked with separating pairs of topological objects based on basic topological properties. We demonstrate that while HOMP is unable to distinguish between any of the pairs in the dataset, \secondmethod  successfully distinguishes all pairs, empirically validating our theoretical findings. Our work opens a new design space and new opportunities for TDL, paving the way for more expressive and versatile models.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This work studies the expressivity of Topological Deep Learning (TDL) architectures, particularly focusing on the limitations of Higher-Order Message Passing (HOMP) for distinguishing combinatorial complexes. The first half of the paper extends Bamberger’s (2022) work on the expressivity limitations of message-passing Graph Neural Networks (GNNs), which characterized, using covering maps, graphs that GNNs cannot distinguish. In a similar vein, this paper reveals "topological blindspots" in HOMP frameworks: (1) complexes that share a cover are indistinguishable by HOMP, and (2) HOMP cannot distinguish complexes that differ in important topological and metric properties such as diameter, orientability, planarity, and homology. In the second half, the authors address these limitations by adapting techniques from expressive graph architectures that process features over tuples of nodes. Similarly, the work extends HOMP with multi-cellular feature spaces and equivariant linear updates. This extension, Multi-Cellular Networks (MCN), achieves full expressive power, allowing it to (1) distinguish non-isomorphic complexes and (2) differentiate complexes based on properties like diameter, 0-th homology group, and also distinguish between a Moebius strip and a cylinder (which disagree on planarity). The work also introduces a more computationally scalable version of MCN, aptly called SMCN.  Lastly, the authors empirically validate MCN and SMCN on benchmarks designed to capture topological expressivity, demonstrating the superiority of these architectures over standard HOMP and expressive GNN models.

### Strengths
(++++) **Novelty and Relevance**: This work is new and addresses questions of significant importance and urgency for the Topological Deep Learning (TDL) community.

(++++) **Theoretical Contribution**: The theoretical contribution is strong, rigorous, and sound. The answers provided to the question considered by the work are satisfying.

(++) **Empirical Validation**: The authors validate their models with real-world and synthetic benchmarks designed to capture topological expressivity, demonstrating clear improvements over standard HOMP and expressive GNN models.

(++) **New Benchmarks**: The work introduces benchmarks that test models on topological invariants to assess TDL expressivity, which will serve as a valuable tool for the TDL community.

### Weaknesses
(---) **Presentation**: The architecture descriptions may be opaque for readers unfamiliar with TDL. Section 5 gives examples of CC data that the new multicellular nodes can encode, but it is unclear which nodes and connections should be included and when. For example, the choice of multicellular nodes and connections such as in the example tensor diagrams in Figure 5 would benefit from additional explanation. Specifically, the paper lacks a clear explanation of how to construct the multi-cellular feature spaces and how the equivariant linear updates are applied in practice. The description of the tensor diagrams in Figure 5, which are central to understanding the proposed architecture, is particularly vague. It is not clear how these diagrams translate into concrete computational steps within the MCN and SMCN layers. For instance, the paper does not specify the exact mathematical operations performed on the features based on the connections in these diagrams, making it difficult to reproduce or extend this work.

(---) **Limited Empirical Evaluation**: The proposed architectures are benchmarked on only three-world datasets. This limited scope makes it difficult to assess the generalizability of the proposed models to more complex real-world scenarios. The benchmarks, while novel, do not fully capture the breadth of applications where TDL methods are typically employed. The lack of experiments on larger, more diverse datasets raises concerns about the practical applicability of the proposed methods.

(--) **Related Work**: Although Section 4 extends Bamberger’s (2020) result, this work is only mentioned once in Section 4.1. An earlier mention in Section 2 (Previous Work) would help readers place this work within a broader research context. The connection to the existing literature on the expressivity of graph neural networks and topological deep learning is not sufficiently elaborated. The paper would benefit from a more thorough discussion of how the proposed approach relates to and differs from existing methods, particularly in terms of their theoretical underpinnings and practical performance.

### Questions
1. The authors demonstrate that HOMP can be extended to achieve full or greater expressivity with components that may make the proposed models computationally impractical for large combinatorial complexes. Is this an inherent limitation that comes with achieving full/greater expressivity, or did the authors only intend to demonstrate that such levels of expressivity are achievable and the proposed extensions sufficed for that purpose?
2. Could the authors give recommendations or guidelines for which additional multicellular nodes and connections to include in the MCN and SMCN models? For example, how should a practitioner choose and connect multicellular nodes in the MCN and SMCN layers as in the example in Figure 5?
3. Could the authors expand their real-world benchmarks with some more tasks/datasets? For example, the TUDatasets or trajectory classification tasks from Bodnar et al. (2021).
4. Are the group actions in Section 5 required to be compatible with the underlying complex? For example, are permutations that exchange nodes while fixing higher-dimensional (rank) simplices allowed?
5. Could the authors make their code publicly available?
6. Could the authors provide a brief account of Bamberger (2020) in the main text to help contextualize how earlier methods relate to and may have motivated the approaches developed in the first half of this work?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The paper presents a new way to define expressivity but from a topological perspective. The paper shows that existing Topological Deep Learning (TDL) models have trouble estimating certain important topological properties such as diameter, orientability, planarity, and homology. The authors then propose a new model called MCN and its scalable version SMCN that can capture the topological properties better. The paper also presents new benchmarks focusing on learning topological properties of complexes.

### Strengths
The paper presents a novel essential perspective that differentiates TDL and deep learning on graphs, which used to be compared under the same umbrella previously (in terms of graph expressivity and benchmarks). This work partly bridges the gap between TDL and traditional computational topology methods, which largely focus on homology. The paper also presents theoretical insights showing that higher-order message passing is incapable of capturing certain topological metrics. The experiments also support these insights. The experiments also constrain on parameter budgets to show the effectiveness of the method with respect to the baseline. The paper acknowledges the weakness of MCN if we consider higher-order spaces, so the authors present a scalable version that leverages subgraph GNNs to encode higher-order features. The novel benchmarks are a great contribution which can facilitate a better comparison standard for TDL methods.

### Weaknesses
The paper is hard to follow and the presentation is not good. For example, the authors can be more explicit on lines 309 and 310 and discuss (1), (2), and (3) more instead of stating them. Specifically, the neighborhood functions defined in equations (1), (2), and (3) lack sufficient explanation regarding their practical implications and how they relate to the topological properties being captured. The paper should elaborate on how these functions are implemented and how they influence the construction of the multicellular cochains. The notations involve many upper scripts and lower scripts while not explaining their purposes clearly make the formula confusing (line 319 and 320). For instance, the group action indices are introduced without a clear explanation of their role in the overall framework, making it difficult to understand how they contribute to the topological analysis. The paper isn’t self-contained; for example, the paper can discuss more about IGN as the model itself leverages an architecture similar to IGN. The same thing applies to Subgraph GNNs. A more detailed explanation of how IGN's architecture is adapted and used within the MCN framework is needed. Similarly, the paper should provide more background on Subgraph GNNs, detailing how they are integrated and why they are suitable for encoding higher-order features. Also, even when the paper focuses on expressivity from a topological perspective, I think it would be helpful to include a brief section discussing the proposed method with respect to graph expressivity so that there is a smoother transition between deep learning on graphs and TDL. The paper should explicitly discuss how the proposed method relates to established graph neural network expressivity frameworks, such as the Weisfeiler-Lehman test, to clarify its position within the broader field of graph representation learning. Lastly, please refer to question 3 for experiments on runtime and lifting time.

### Questions
1. For Figure 5, can you elaborate more on colored nodes of SMCN and MCN? I think this part can be improved to make it clearer for the audience.
2. For Figure 7, the superscript for \mathcal{X} and \mathcal{H} isn’t discussed in the main text, so it is confusing.
3. Can the authors comment on the lifting and runtime complexities with respect to CIN? I think the paper only mentions the runtime complexity and neglects the discussion. It is also helpful to include an experiment on wall-clock training/inference time to see the model scalability in practice when comparing with other TDL models.

### Soundness
3

### Presentation
2

### Contribution
4

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper presents an in-depth exploration of Topological Deep Learning (TDL) architectures through the lens of Higher-Order Message Passing (HOMP). The authors investigate HOMP's expressivity limitations in capturing topological invariants (e.g., orientability, planarity, diameter, and homology) in combinatorial complexes and propose two novel architectures: Multi-Cellular Networks (MCN) and Scalable Multi-Cellular Networks (SMCN). These architectures aim to enhance HOMP’s expressivity in distinguishing between topological structures. Empirical evaluations using newly designed benchmarks and real-world graph datasets demonstrate that SMCN outperforms existing models, highlighting the potential of using expressive topological information in TDL.

### Strengths
1.	The authors provide a rigorous examination of HOMP’s expressivity limitations concerning fundamental topological and metric invariants, establishing the groundwork for understanding the weaknesses in current TDL approaches.

2.	The introduction of MCN and SMCN provides new pathways for achieving higher expressivity. The authors demonstrate that MCN can theoretically achieve full expressivity, while SMCN offers a computationally feasible alternative, balancing expressivity with scalability.

3.	SMCN demonstrates substantial improvements over traditional HOMP and GNNs, validating the model's efficacy in capturing and leveraging topological features in learning tasks.

### Weaknesses
1.	While SMCN offers a scalable alternative to MCN, it still encounters significant challenges in managing large and complex combinatorial complexes due to its super-linear scaling with respect to the number of cells. It would be beneficial for the authors to provide a comparative analysis of SMCN’s runtime performance against existing HOMP methods and other GNNs, such as CIN (Bodnar et al., 2021) and the backbone subgraph GNN used in SMCN. Specifically, a detailed breakdown of the computational cost associated with each stage of the SMCN pipeline, including the construction of the cellular complex, the subgraph GNN computations, and the final message passing phase, would be valuable. Furthermore, it is important to understand how the runtime scales with the size and complexity of the input complexes, going beyond just the number of cells, for example, considering the number of faces, edges, and vertices, and the maximum dimension of cells.

2.	The paper would benefit from a more detailed rationale for why topological invariants—such as diameter, orientability, planarity, and homology—are critical for machine learning models to differentiate. Specifically, it would be helpful to address the importance of these invariants in machine learning tasks, either through empirical evidence, theoretical reasoning, or relevant literature. For example, the authors could discuss specific scenarios where the ability to distinguish between graphs with different diameters or homology groups would lead to improved performance in downstream tasks. This discussion should also clarify why these invariants are not already captured by existing GNN architectures, which are known to be powerful in capturing graph structural information.

3.	There appears to be a discrepancy between SMCN’s theoretical expressivity and its empirical accuracy. For instance, it is unclear why SMCN does not achieve full accuracy in predicting cross-diameter and the second Betti number, which warrants further investigation. The authors should explore the potential reasons for this gap, such as limitations in the optimization process, the choice of hyperparameters, or the specific architecture of the subgraph GNN used within SMCN. A more thorough analysis of the model's behavior on these tasks, including error analysis and visualization of the learned representations, would be beneficial.

### Questions
1.	To enhance readability and comprehension, the main paper should be more self-contained by clearly explaining topological invariants—such as diameter, orientability, planarity, and homology. For clarity, consider presenting formulas or examples within the main text (e.g., rather than relying solely on descriptions on line 233).

2.	In the introduction of the concept of CC covering, an illustrative case could help readers grasp this concept more intuitively.

3.	Could the authors discuss the proposed method in relation to relevant research? For instance, [1] proposed a cycle-invariant positional encoding where cell/cycle features are initially encoded using an invariant network and subsequently incorporated into a standard GNN as additional edge features. A comparison would contextualize SMCN’s contributions within the broader landscape of topological GNN methods.

[1] Yan Z, Ma T, Gao L, et al. Cycle invariant positional encoding for graph representation learning. LoG 2024.

### Soundness
3

### Presentation
2

### Contribution
3
