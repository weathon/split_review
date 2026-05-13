# ResolvNet: A Graph Convolutional Network with multi-scale Consistency

- Decision: Reject
- Scores: 5, 8, 6, 3

## Abstract
It is by now a well known fact in the graph learning community that the presence of bottlenecks severely limits the ability of graph neural networks to propagate information over long distances. What so far has not been appreciated is that,  counter-intuitively, also the presence of strongly connected sub-graphs may severely restrict information flow in common architectures. Motivated by this observation, we introduce the concept of multi-scale consistency. At the node level this concept refers to the retention of a connected propagation graph even if connectivity varies over a given graph. At the graph-level, multi-scale consistency refers to the fact that distinct graphs describing the same object at different resolutions should be assigned similar feature vectors. As we show, both properties are not satisfied by popular graph neural network architectures. To remedy these shortcomings, we introduce ResolvNet, a flexible  graph neural network based on the mathematical concept of resolvents. We rigorously establish its  multi-scale consistency theoretically and verify it in extensive experiments on real world data: Here networks based on this ResolvNet architecture prove expressive; out-performing baselines significantly on many tasks; in- and outside the multi-scale setting.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper considers graphs with two scales, one in which nodes are strongly connected into clique-like communities and a another scale in which the connections are weaker and uniform over the graph. A distinction is based between the two communities based on spectral analysis: the second eigenvalue of the first scale is much higher than all the eigenvalues of the second scale. The idea of resolvents is proposed to deal with such graphs and two types of filters, type-0 and type-1 are defined to propagate information in a GNN. The ideas are validated empirically. It is shown that the proposed method works well on graphs with high homophily.

### Strengths
The idea of separating a network into multiple scales is nice. The problem is well defined and motivated

The use of resolvents to design filters is novel. A theory is developed to justify the methods.

The experimental results show the usefulness of the method.

### Weaknesses
1. The paper would benefit from experiments on synthetically generated graphs, such as those derived from stochastic block models. This would allow for precise control over all graph parameters and provide a more rigorous evaluation of the proposed method's performance under varying conditions.

2. The integration of Type-0 and Type-1 filters is not clearly articulated. Specifically, it is not clear if a node autonomously determines which filter to employ or if this is a global parameter. The mechanism for combining or selecting between these filters needs further clarification.

3. The paper lacks comparisons with several relevant baselines:
a. A method involving pooling to identify clusters (e.g., diffpool, gpool, eigenpooling) followed by a standard GNN on the coarsened graph.
b. An approach utilizing Gaussian Mixture Models to differentiate between the two network scales, training separate GNNs for each scale, and subsequently merging the representations for node or graph prediction.

4. The abstract is unclear, particularly the sentence: "At the graph level, multi-scale ." This part needs to be rephrased for better clarity. Additionally, the concluding sentence of the abstract appears to make assertions that are not fully substantiated by the experimental results presented in the paper.

### Questions
Please look at the weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper points out a problem in graph neural networks where certain strongly connected parts, like cliques, can limit the spread of information in the graph. To solve this, the authors introduce the idea of multi-scale consistency. This means keeping a connected way of spreading information even if the connection density in the graph changes for the node level tasks. For the graph level tasks, it means graphs generated from the same ground truth, which are at different resolutions,  should be assigned similar feature vectors. The research shows that many popular GNN designs don't have this feature. To fix this, the authors of this work propose ResolvNet, a new Spectral-based GNN design based on a math concept called resolvents. By applying resolvent of the Laplacian, 	ResolvNet is able to have the same effect of projecting the dense connected components in the original graph to a coarsened graph, then efficiently propagating information and finally projecting the embedding back to the original graph node level. Authors have theoretically proved that the proposed method is able to consistently integrate multiple connectivity scales occurring within graphs. Also , extensive experiments have shown that ResolvNet has multi-scale consistency and does better than other baselines in many tasks using various datasets. It is also shown that the proposed method is more stable than the baselines under different resolution scales.

### Strengths
*Originality*: The paper identifies a novel issue in graph neural networks and introduces an effective framework, ResolvNet, to address it. This represents a significant and innovative contribution to the field.

*Quality*: The investigative experiments and primary results presented in the paper are persuasive. Supported by solid theoretical proofs, this work stands out as a high-quality piece of research.

*Clarity*: The paper is exceptionally well-organized. Its straightforward and lucid presentation of both the problem and the proposed solution allows readers to grasp the content quickly and comprehensively.

*Significance*: By highlighting a new issue and offering an effective framework to tackle it, this work holds substantial impact potential for the broader community.

### Weaknesses
*Insufficient Analysis*: The paper could benefit from more extensive ablation studies and parameter analyses. Specifically, the impact of variations in parameters like $\omega$ and $k$, as defined in the ResolvNet Layer, on the final results is not thoroughly investigated. For instance, how does the performance change when $\omega$ is varied across different orders of magnitude? Similarly, how does increasing the value of $k$ affect the model's ability to capture multi-scale information? A more detailed analysis of these parameters would provide deeper insights into the robustness and sensitivity of the proposed method.

*Complexity of Concepts*: The concept of "resolvents" is not a commonly understood mathematical idea within the graph neural network community. While the paper introduces the concept, it lacks sufficient depth and practical examples to facilitate a thorough understanding. Providing more explanations, along with practical application cases in graph analysis or related fields, would greatly aid readers in grasping this concept. For example, illustrating how resolvents are used in spectral graph theory or other related domains could enhance clarity. Additionally, a more intuitive explanation of how the resolvent of the Laplacian relates to multi-scale consistency would be beneficial.

Minor issue:

*Notation Introduction*: The paper occasionally lacks a comprehensive introduction to certain notations. For instance, the notation $T$ in section 3.2 is introduced without adequate context or explanation. It is unclear what $T$ represents and how it relates to the Laplacian operator $\Delta$ used in other parts of the paper. A clearer definition and consistent use of notations throughout the paper would improve readability.

### Questions
The datasets utilized in this study are primarily small to medium-sized. How would ResolvNet perform in terms of accuracy and computational time when applied to larger datasets?

How do learnable filters as polynomials in resolvents achieve similar effects of up-projection operator and down-projection operator. It may need more illustrations and explanations for this in Sec 3.2.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper study multi-scale consistency (distinct graphs describing the same object at different resolutions should be assigned similar feature vectors) of node representation in graph neural network, which is indeed an important topic that is less well explored. 

The authors show existing GNN method lack of multi-scale consistency, then they propose ResolvNet to solve this issue. Experiment shows improvement on GNN performance.

### Strengths
1. This paper study multi-scale consistency (distinct graphs describing the same object at different resolutions should be assigned similar feature vectors) of node representation in graph neural network, which is indeed an important topic that is less well explored. 

2. This paper provide a very clear definition on multi-scale consistency in Definition 2.1, and explain in great details (using both figures, text, and examples) to help readers understand why it is important.

3. The proposed method capture the intuition of multi-scale consistency.

### Weaknesses
1. Experiment dataset is small. This is potentially because the proposed method has very high complexity due to matrix inverse (see feed-forward rule in paragraph **The ResolvNet Layer**. The authors need to conduct experiment on larger datasets (e.g., OGBN) and report complexity in terms of FLOP/Wall-clock time.

2. Part of the discription is not very clear, please refer to Questions.



### Questions
1. I understand the definition of $G_\text{high}$ and $G_\text{reg}$, but I am very clear how two split an original graph into this two graph. This is related to Definiton 2.1.

2. Please elaborate on "we would have a Lipschitz continuity relation that allows to bound the difference in generated feature vector in terms of a judiciously chosen distance". This is the sentense above Eq. 1. I don't understand why.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper first points out that the presence of strongly connected sub-graphs may severely restrict information flow in common GNN architectures. Then, it introduces the concept of multi-scale consistency, which can fit both the node-level and graph-level scenarios. In light of this, the authors introduce ResolvNet, a flexible graph neural network based on the mathematical concept of resolvents. Finally, it conducts some experiments to evaluate the proposed method, showing that the proposed method outperforms state-of-the-art baselines on several tasks across multiple datasets.

### Strengths
1.	It provides some theorical support for the proposed model.
2.	It tests on several widely-used datasets, and the proposed method can sometimes beat the existing methods.
3.	The authors provide their codes.

### Weaknesses
1. SOTA baselines are largely ignored. On three famous datasets Cora, Citeseer and Pubmed, there are only two baselines are considered (in Table 1). Few baselines (like GCNII and GraphMAE2), which after 2022, are considered. As far as I know, GCNII (which is open source) can beat the proposed method on Cora and Pubmed. Moreover, even this, the proposed method cannot get the best performance in Table 3.
2. The work is some kind of hard to follow. Although providing lots of theories will enhance the paper, the readability is also should be considered.
3. Some grammatical errors, like 1) satisfied by poular graph -> “popular”; 2) severly restricts - > “severely”. 3) degree occuring -> “occurring”

### Questions
1.	Why the reported results cannot beat SOTA baselines (like GCNII) in Table 1?
2.	How many hyper-parameters are there in your method? If the proposed method contains too many hyper-parameters, it will be hard to reproduce.
3.	See the weakness in the “*Weaknesses” part.
4.	The work can be largely improved by enhancing its experiments and fixing gram errors.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair
