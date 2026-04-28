# Distribution Shift Resilient GNN via Mixture of Aligned Experts

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 3, 6, 6

## Abstract
The ability of Graph Neural Networks (GNNs) to generalize to diverse and unseen distributions holds paramount importance for real-world applications. However, previous works mostly focus on addressing specific types of distribution shifts, e.g., larger graph size or node degree, which is highly limited when confronted with multiple and nuanced distribution shifts. For example, a node in a social graph may have both increased interactions and features alternation, while its neighbor nodes may see different shifts. Failing to consider such complex distribution shifts will largely hinder the generalization effect in practice. Here we introduce GraphMETRO, a novel framework based on a mixture-of-experts (MoE) architecture, enhancing GNN generalizability for both node- and graph-level tasks. The core concept of GraphMETRO includes the construction of a hierarchical architecture composed of a gating model and multiple expert models that are aligned in a common representation space. Specifically, the gating model identifies the significant mixture components that govern the distribution shift on a node or graph instance. Each aligned expert produces representations invariant to a type of mixture component. Finally, GraphMETRO aggregates the representations from multiple experts to produce an invariant representation w.r.t. the complex distribution shift for the prediction task. Moreover, GraphMETRO provides interpretations on the distribution shift type via the gating model and offers insights into real-world distribution shifts. Through the systematic experiments, we validate the effectiveness of GraphMETRO which outperforms Empirical Risk Minimization (ERM) by 4.6% averagely on synthetic distribution shifts and achieves state-of-the-art performances on four real-world datasets from GOOD benchmark, including a 67% and 4.2% relative improvement over the best previous method on WebKB and Twitch datasets.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studied learning with distribution shifts on graphs, which is an under-explored open challenge in GNN community. The authors propose a mixure-of-expert-based model to learn the invariant representation learning of graph data for out-of-distribution generalization. By theoretical analysis, the authors show that the proposed model can provably capture the invariant patterns. Experiments showcase the efficacy of the model for tackling both node-level and graph-level distribution shifts against several state-of-the-art methods.

### Strengths
1. The problem this paper targets is a significant problem and the paper is well motivated

2. The proposed model seems reasonable and interesting to my knowledge

3. The experiment results are promising and the improvements are solid

### Weaknesses
1. The novelty is not well justified and comparison with recent methosd is not sufficient

2. Some of recent papers on out-of-distribution learning on graphs are not discussed [3-5]

3. The authors argued that "previous works mostly focus on addressing specific types of distribution shifts", which seems inproper and incorrect. E.g., the typical works for graph OOD learning EERM [1] and DIR [2] do not assume the type of distribution shifts in their problem formulation. The claim about previous works focusing on specific shift types is too broad. While some methods might target specific shifts, many OOD methods aim for general robustness without explicit assumptions about the shift type. The paper needs to more carefully position itself with respect to these methods.

### Questions
1. How does the model compare with existing invariant learning-based models for graph OOD generalization, e.g., EERM [1] and DIR [2]? What is the key technical originality of this work?

2. What is the computation cost of this model compared against other peer models?

3. Can the proposed model handle multiple different types of distribution shifts that simultanenously exist in data?

4. Can the proposed model tackle distribution shifts and out-of-distribution generalization on molecular graphs?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces a method to enhance the out-of-distribution performance of graph neural networks (GNN) by learning to understand distribution shifts instead of addressing the assumed ones. To achieve this, the Mixture of Experts architecture is integrated into the GNN, supplemented by an alignment procedure to recognize the shift. Empirical experiments are conducted to validate the theoretical assertion.

On the whole, I believe the proposed method lacks the necessary motivation and its novelty isn't substantial enough to meet the standard.

### Strengths
- The paper aptly addresses OOD as a crucial issue for GNNs, pinpointing graph shift heterogeneity as the core challenge.
- Real-world datasets back the claims through experiments.
- Thorough ablation studies validate the learned graph shifts, a commendable effort.

### Weaknesses
 - The motivation behind the proposed method is not adequately substantiated. The primary basis given is that "previous research has concentrated on addressing specific types of distribution shifts." However, this overlooks a plethora of prior works in the field. Contrary to the suggestion that graph shift heterogeneity is under-explored, numerous studies have delved into learning the "environment generators" for GNNs to detect graph shifts, as exemplified by [https://arxiv.org/abs/2202.02466]. Other works have focused on learning shift-specific transformations, such as [https://arxiv.org/abs/2211.02843]. Consequently, there exists a wide spectrum of approaches to tackle graph shift heterogeneity. The choice of approach in this paper, especially the emphasis on MOE, requires a more detailed and robust justification to elucidate its relevance and significance.

- The presented assumption seems overly broad and lacks specificity. Additionally, the architectural design appears to be somewhat arbitrary. Consequently, it's challenging to discern the functionality, its underlying mechanism, and its improvements over existing methods. The core idea of decomposing distribution shifts into a mixture of stochastic graph transformations, while potentially interesting, is not sufficiently grounded in theory or empirical evidence. The assumption that complex shifts can be accurately represented by a combination of simpler, predefined transformations is a significant leap that requires more rigorous justification. Furthermore, the method lacks a clear explanation of how the mixture components are learned and how they relate to the actual distribution shifts observed in the data. Without a more concrete understanding of these aspects, it remains unclear why this approach should be preferred over other methods.

- The proposal is insufficient in its details, particularly concerning the implementation of specific model architectures, stochastic transformation, and the optimization process. Given the inclusion of shift learning midway and data augmentation initially, one would expect a more intricate optimization strategy than standard routines. The paper does not sufficiently detail how the gating network is trained and how it interacts with the expert networks. The lack of clarity on the training procedure for the mixture components, especially concerning how the alignment procedure is implemented and optimized, makes it difficult to reproduce the results or to assess the practical viability of the method. The description of the stochastic transformations is also too high-level, lacking specific details about the types of transformations used and their parameterization.

### Questions
Please check Weaknesses.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies the distribution shift of graphs caused by a set of stochastic transformations. To obtain an invariant representation under distribution shift, the paper proposes a mixture of experts where each mixture is designed to capture a corresponding transformation. Through the gating mechanism, the model automatically captures the transformation that causes the distribution shift. Experimental results with synthetic and real datasets show the superior performances of the proposed algorithm.

### Strengths
The experimental result on the WebKB dataset is outstanding.

### Weaknesses
 - The proposed approach assumes that the distribution shift on a graph dataset happens due to some underlying transformations. While this assumption looks plausible at first, it seems quite difficult to identify all distribution shifts with the assumption since the transformations are treated independently when combined together.
- In other words, the entire framework requires a set of predefined transformation classes to learn the model, and all necessary transformations need to be identified beforehand. However, it is unclear whether the set of transformations used in the experiments is enough to cover complex distributions causing the distribution shift. For instance, real-world distribution shifts might involve combinations of structural and feature changes, or more subtle, non-stochastic variations, which may not be easily represented by the chosen transformations.
- Moreover, most of the transformation requires a set of hyperparameters, e.g., dropout probability. However, each mixture only models a single instance of the transformation but not the entire class of transformations. Given that the hyperparameters are selected via the validation set, there is no evidence that the same configurations can work for the test set since it may caused by the different hyperparameters of the same transformation type. This raises concerns about the model's robustness to unseen variations within the same transformation class.
- This work only considers the distribution shift in the graph structure but not in the labels. This is a significant limitation as real-world datasets often exhibit shifts in both graph structure and label distributions. Ignoring label shifts could lead to suboptimal performance in practical scenarios.

### Questions
- Which of the results are statistically significant in Table 1? For graph classification tasks, the proposed model seems marginally better than the others.
- Can we say we use ERM for the node classification even if nodes and their labels are not i.i.d.?
- Figure 2 is not easy to digest since there is only a single label along the radial axis. Could you provide the exact numbers?
- The test accuracy for the synthetic dataset for some transformations is relatively lower than the other transformations. Why some transformations is harder to identify than others for some datasets?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents GraphMETRO, a graph neural network with mixture-of-experts architecture for domain generalized graph learning. The idea of GraphMETRO is a two-level design. It first aims to identify the form of graph distribution change with a gating module, and then directs the graph to the corresponding experts that are responsible for the forms of graph distribution change. In addition, the experts should generate invariant features w.r.t to its graph distribution change. The authors design objective functions for each of the goals above. Experiments over real-world and synthetic datasets with distribution shift show the effectiveness of the proposed GraphMETRO.

### Strengths
1. The problem of graph OOD generalization is important in real-world applications. Indeed, in real-world deployment of graph neural networks, we have to deal with shifting data (e.g. caused by temporal dynamics or cross-domain data). I also appreciate that the authors do not view distribution shifts as a whole, but try to decompose a distribution shift into different types of shifts. This brings extra insights to the problem of graph OOD generalization. 

2. The paper is well-presented, well-organized, and very easy to follow. 

3. The solution with mixture-of-experts is simple but sound and provides some interpretability to the distribution change. Indeed, mixture-of-experts is an established technique, but the authors made extra efforts to adapt MoE to the case of OOD generalization. The design that each expert is in charge of one type of distribution shift makes good use of MoE architecture, and a gating module that identifies the type of distribution changes adds interpretability to the whole method. In addition, adequate designs are made to ensure that the gating model recovers the right shift types, and the experts output invariant features.

### Weaknesses
1. It is not clear how well the 5 designed distribution shifts can well cover real-world graph distribution shifts. The authors listed 5 distribution shifts in the paper (add edge, drop edge, feature noise, subgraph, drop nodes), but in fact there may be more graph distribution shifts than that. For example, there may be a systematic change in link preference (i.e. nodes tend to link with a different type of neighbors), adding malicious nodes (e.g. malicious users in a trading system). Maybe the authors can justify how well the 5 designed shifts can cover real-world distribution shifts.  

2. It is not clear how the proposed GraphMETRO can handle imbalanced distribution shifts within the same graph. For example, it may happen that some subgraphs in the graph gets denser, while other subgraphs get sparser (e.g. some topics gain interest, while others lose).  How will GraphMETRO respond to this kind of shifts? 

3. It is not clear how graph pre-training can address the OOD generalization issue. Pre-training trains the model to observe a wide range of graphs and should be helpful in improving generalization. 

4. It may be good to discuss some previous works in graph transfer learning. Graph transfer learning addresses the problem that the source graph has a different distribution with the target graph, but the target graph should be given beforehand and is thus less difficult than the problem in this paper. Nevertheless, it may be good to discuss them and clarify the differences, e.g. (Zhang et al. 2019), (Wu et al. 2020).

Unsupervised Domain Adaptive Graph Convolutional Networks. Wu et al. WWW 2020
DANE: Domain adaptive network embedding. Zhang et al. IJCAI 2019.

### Questions
1 and 2 in weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
