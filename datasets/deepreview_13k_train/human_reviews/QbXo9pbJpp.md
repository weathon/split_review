# Improved Invariant Learning for Node-level Out-of-distribution Generalization on Graphs

- Decision: Reject
- Scores: 6, 5, 5, 5

## Abstract
Enhancing OOD generalization on graph data is a recent hot research topic. Among this, node-level OOD generalization remains an underexplored and challenging subject. The difficulty of node-level OOD tasks lies in the fact that representations between nodes are coupled through edges, making it difficult go characterize distribution shifts and capture invariant features. Furthermore, environment labels for nodes is typically expensive to obtain in practice, rendering invariant learning strategies based on environment partitioning infeasible. By establishing a theoretical model, we highlight that even with ground-truth environment partitioning, classical invariant learning methods like IRM and VREx designed for independently distributed training data  will still capture spurious features when the depth of the GNN exceeds the width of a node's causal pattern (i.e., the invariant and predictive neighboring subgraph). Intriguingly, however, we theoretically and empirically find that by enforcing Cross-environment Intra-class Alignment (CIA) of node representations, we can remove the reliance on these spurious features. To harness the advantages of CIA and adapt it on graphs, we further propose Localized Reweighting CIA (LoRe-CIA), which does not require environment labels or intricate environment partitioning processes. Leveraging the neighbouring structural information of graphs, LoRe-CIA adaptively select node pairs that exhibit large differences in spurious features but minimal differences in causal features for alignment, enabling more efficient elimination of spurious features. The experiments on GOOD benchmark shows that LoRe-CIA achieves optimal OOD generalization performance on average.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a novel method to improve out-of-distribution (OOD) generalization for node-level tasks on graph data. It introduces a theoretical model to assess OOD techniques in node-level OOD classification and proposes an enhanced invariant learning objective that considers both graph topology and node features. The method is evaluated on benchmark datasets, demonstrating superior OOD detection and classification performance. The paper contributes a theoretical analysis of OOD methods on graphs, an innovative approach for invariant learning, and empirical benchmark evaluations.

### Strengths
- **Motivation**: The paper addresses an important challenge in graph learning: achieving OOD generalization on real-world graphs.

- **Theoretical guarantee**: This approach is grounded in a theoretical model that analyzes the performance of several OOD methods, including V-REx and IRM, in node-level OOD classification problems. The theoretical model presented in the paper also offers insights into the performance of OOD methods, which could inform future research in this area.

- **Statement of intuition**: The paper provides explanations of the theoretical model and the proposed approach. I particularly appreciate the part where the authors discuss the intuitions presented in the main paper.

### Weaknesses
 - **Theoretical model**: In Remark, the authors noted, "In this toy model, the distribution shift is caused by both changes in topological structures (Ae) and node features (Xe2). This represents the general case of real-world OOD graphs." It would be beneficial to see a more detailed analysis of the model's assumptions and limitations. Specifically, what cases are not covered by the model? The model appears to assume a linear relationship between invariant and spurious features, which may not hold in complex real-world scenarios. A discussion of how non-linear relationships might affect the model's conclusions is warranted. Furthermore, the model's assumption that spurious features are solely influenced by node labels and neighbor labels could be too simplistic, ignoring other potential confounding factors.

- **Efficiency explanation**: In the abstract and introduction, the authors mentioned that the proposed approach enables "more efficient elimination of spurious features." However, the paper does not provide an analysis of the computational complexity of this approach, and the experimental section lacks relevant information about its runtime. While the authors claim efficiency, a rigorous analysis of the time and space complexity, especially as it scales with graph size, is missing. A comparison of computational cost against baseline methods would be beneficial.

- **Presentation**: The paper's structure and clarity could be further improved. For instance, in Figures 1 and 2, the shapes representing labels are hard to tell at the first sight. In Section 4.2, the statement "the rate of change of a node’s spurious features with respect to spatial location on the graph is faster than that of the causal feature" could benefit from a more specific explanation of what "rate" means in this context. Additionally, while the content is generally clear, the writing could be further refined. The concept of 'rate' needs to be more precisely defined, possibly in terms of a gradient or distance metric within the graph structure. The lack of a formal definition makes it difficult to assess the validity of this claim.

- **Real-world graph datasets**: Since CBAS is a synthetic dataset, its weight in the study may be smaller than the other two datasets. It might be worthwhile to include more real-world datasets to validate the generalization ability of CIA/LoRe-CIA across a wider range of distributions. The reliance on a synthetic dataset for a substantial part of the evaluation limits the generalizability of the findings. More experiments on diverse real-world graph datasets with varying characteristics are needed to support the robustness of the proposed method.

### Questions
- What are the cases that are not included in the theoretical model?
- What is the evidence that supports the claim about CIA is a more efficient approach?
- In Section 4.2, "...the rate of change of a node’s spurious features with respect to spatial location on the graph is faster than that of the causal feature...", what does "rate" mean specifically?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper studies node-level OOD generalization. It establish cases where invariant learning methods like IRM and VREx given environment labels learn spurious features when the depth of the GNN exceeds the causal depth. Then it shows the cross-environment intra-class alignment of nodes avoid some spurious features. The paper also proposes LoRe-CIA, which does not require environment labels but selects node pairs that exhibit large differences in spurious features but minimal differences in causal features for alignment. Experiments are conducted to evaluate the methods.

### Strengths
1. The paper studies an algorithmic case and clearly analyzes IRM, VREx and CIA from a theoretical perspective.

2. The paper presentation is clear and easy to follow.

3. The proposed method does not require ground-truth environment labels. The conducted experiments look correct.

### Weaknesses
1.  The setting in 3.1 assumes $L > 2k$ and GNNs are sufficiently deep, which is doubtful. Typically graph tasks would not use very deep GNNs due to the well-known fact that deep GNNs have over-smoothing issues and compromise performances. Therefore this assumption may not hold. Moreover, there's no validation for the number of layers of the causal pattern of a node in any real-world dataset, thus no conclusion whether this $L > 2k$ setting is applicable for any graph tasks.

2. From my understanding, CIA's major superiority over other methods using environment labels like VREx roots in its consideration of both class and environment label information at the same time. However, LoRe-CIA does not use environment labels. According to [1], learning invariant/spurious features without environment partition is fundamentally impossible if not given further inductive biases or information. Thus, there appears to be no guarantee that LoRe-CIA can learn the information supporting CIA, i.e., LoRe-CIA might not be able to identify node pairs with significant differences in spurious features and small differences in causal features.

3. Sec 4.2 assumes 1. change rate of node’s spurious features w.r.t spatial location is faster than that of the causal feature; 2. label distribution of node's different-class neighbors reflects the distribution of spurious features. This assumption is quite strong and seems not applicable widely. There are graphs exhibiting various behavior, such as heterogeneous/homogeneous graphs. Further discussions on when these assumptions hold should be included.

### Questions
See weaknesses

### Soundness
3 good

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
This paper studies the out-of-distribution node classification. The authors propose a toy model considering the connections among nodes to demonstrate the limitations of IRMv1 and VREx in learning the underlying invariant features, such that similar frameworks like EERM well as fail. Then the authors incorporate the causal objecting matching objective to contrast intra-class samples across environments, called Cross-environment Intra-class Alignment (CIA). To address the collapse issue of the learned representations, the authors further propose a localized weighting variant of CIGA, called LoRe-CIA, that reweights the contrasting pairs according to the shortest path distance. In experiments with GOOD datasets, LoRe-CIA that does not use environment partitions, demonstrates competitive performance with respect to other methods that uses environment partitions.

### Strengths
(+) The studied problem is important;

(+) The theoretical failure results of IRM and VREx is interesting;

(+) The proposed localized reweighting scheme is new and interesting;

### Weaknesses
(-) The main motivation setting seems to be too hypothetical;

    - Although the proposed toy example seems to be more general than EERM, what are the realistic examples for the proposed data model? Without proper explanation and discussion, it is hard to claim that “This is the general case of real-world OOD graphs.” The model's reliance on a multi-layer structure, while theoretically interesting, lacks clear justification in practical scenarios. The authors do not provide sufficient evidence that real-world graph data necessitates this specific multi-layer generation process, especially when compared to existing models like EERM, which also capture multi-hop dependencies through ego-graph constructions.
    - What does the superscript $e$ means in $A^e$? How environment changes could affect the generation of X?
    - Moreover, the failure proofs seem to heavily rely on the assumption that “GNNs that are sufficiently deep (deeper than the number of layers of the causal pattern of a node) are typically used.”. Is it really true? The claim that a GNN's optimal performance is achieved when its depth matches the 'true generation depth' is vague. Real-world graphs present complex dependencies that are not solely determined by the depth of causal patterns. Factors such as homophily and heterophily can significantly impact the performance of GNNs, making the assumption of a direct correlation between GNN depth and optimal performance questionable.

(-) The novelty of the proposed method is limited and some related works have not been fairly discussed.
    - The proposed method is a simple modification of Mahajan et al. (2021). How does the modification work to make up the environment information? The modification, while incorporating node pair information, seems to take a 'free lunch' that could improve over the original CIA with environment information. A more rigorous justification of this approach is needed to understand why LoRe-CIA could outperform or underperform previous approaches. Without such justification, it is difficult to assess the true contribution of the method.
    - If it’s only for the collapse issue, as already demonstrated in Figure 1, properly tuning the hyperparameter $\lambda$ already solves the problem well. How the $\lambda$ is tuned for CIA?
    - What’s the relation between LoRe-CIA and CIA? Does CIA serve as a upper bound for LoRe-CIA? Why not incorporating LoRe into CIA with environments directly to resolve the collapse issue?
    - What is the exact implementation of LoRe-CIA?
    - The failures of IRM and VRex, and the success of intra-class contrastive learning are not surprising, as they are already shown by Chen et al., (2022). It is desirable to properly discuss the distinctions of the work with respect to previous works, thus the readers could better understand the place of the work in the literature.

(-) The improvements are limited:
    - When comparing to baselines that do not use environments, LoRe-CIA does not show clear advantage, and most of the improvements are within standard deviation.
    - It is unclear how the hyperparameters such as $\lambda$ and hop numbers are tuned.

### Questions
Although I like the idea of the paper, it seems the paper could be improved significantly by clarifying the following points:

1. The main motivation setting seems to be too hypothetical. 
- Although the proposed toy example seems to be more general than EERM, what are the realistic examples for the proposed data model? Without proper explanation and discussion, it is hard to claim that “This is the general case of real-world OOD graphs.”
- What does the superscript $e$ means in $A^e$? How environment changes could affect the generation of X?
- Moreover, the failure proofs seem to heavily rely on the assumption that “GNNs that are sufficiently deep (deeper than the number of layers of the causal pattern of a node) are typically used.”. Is it really true? 

2. The novelty of the proposed method is limited and some related works have not been fairly discussed. 
- The proposed method is a simple modification of Mahajan et al. (2021). How does the modification work to make up the environment information? 
- If it’s only for the collapse issue, as already demonstrated in Figure 1, properly tuning the hyperparameter $\lambda$ already solves the problem well. How the $\lambda$ is tuned for CIA? 
- What’s the relation between LoRe-CIA and CIA? Does CIA serve as a upper bound for LoRe-CIA? Why not incorporating LoRe into CIA with environments directly to resolve the collapse issue?
- What is the exact implementation of LoRe-CIA?
- The failures of IRM and VRex, and the success of intra-class contrastive learning are not surprising, as they are already shown by Chen et al., (2022). It is desirable to properly discuss the distinctions of the work with respect to previous works, thus the readers could better understand the place of the work in the literature.

3. The improvements are limited:
- When comparing to baselines that do not use environments, LoRe-CIA does not show clear advantage, and most of the improvements are within standard deviation.
- It is unclear how the hyperparameters such as $\lambda$ and hop numbers are tuned.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents a method called LoRe-CIA for out-of-distribution (OOD) generalization in graph neural networks (GNNs). The notable contributions of the paper include proposing a novel regularization term called LoRe, which encourages the learning of invariant representations across different environments. The LoRe term is combined with the Contrastive Invariant Alignment (CIA) objective to improve OOD generalization performance. Experimental results on the GOOD benchmark dataset demonstrate that LoRe-CIA outperforms several state-of-the-art methods in terms of OOD generalization accuracy.

### Strengths
The paper innovatively focuses on not fully explored node-level OOD generalization in graphs, revealing limitations of existing methods and introducing a novel approach, LoRe-CIA. High-quality work grounded in both theory. Addresses key challenges in graph-based OOD generalization and offers a robust solution with LoRe-CIA. Well-structured and clearly articulated, the paper provides a logical flow from problem formulation to solution, enhancing readability and comprehension.

### Weaknesses
The paper does not discuss the computational complexity of LoRe-CIA. Given that graph neural networks can be computationally intensive, an analysis of the algorithm's scalability to larger graphs would be beneficial. It would be better to add more recent models in experiments.

### Questions
In Table 2, when examining LoRe-CAI on the CBAS dataset, is there a specific reason why the variance of the results appears to be zero?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
