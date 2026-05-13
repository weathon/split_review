# A Graph-Theoretic Framework for Joint OOD Generalization and Detection

- Decision: Reject
- Scores: 6, 3, 6

## Abstract
In the context of modern machine learning, models deployed in real-world scenarios often encounter various forms of data shifts, leading to challenges in both out-of-distribution (OOD) generalization and detection. While these two aspects have received significant attention individually, they lack a unified framework for theoretical understanding and practical usage. This paper bridges the gap by formalizing a graph-theoretical framework tailored for both OOD generalization and detection. In particular, based on our graph formulation, we introduce spectral learning with wild data (SLW) and show the equivalence of minimizing the objective and performing spectral decomposition on the graph. This equivalence allows us to derive provable error quantifying OOD generalization and detection performance. Empirically, SLW demonstrates competitive performance against existing baselines, aligning with the theoretical insight.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces an innovative graph-theoretical framework that addresses the dual challenges of OOD generalization and detection. The foundational approach in the paper involves constructing a graph wherein nodes represent image data, and edges are established to connect similar data points. The definition of edges, influenced by both labeled and unlabeled data, lays the groundwork for examining OOD generalization and detection through a spectral lens.

The paper further contributes by proposing a spectral contrastive loss, which facilitates concurrent learning from labeled in-distribution (ID) data and unlabeled wild data. This loss function serves as a key component of the framework, contributing to the overall effectiveness of the method.

Moreover, the paper substantiates its claims through a series of well-conducted experiments that illustrate the capabilities of the framework in the context of OOD generalization and detection. These experiments not only validate the proposed approach but also provide valuable insights into its practical utility.

### Strengths
The author introduces a novel framework aimed at addressing both the challenges of out-of-distribution (OOD) generalization and OOD detection simultaneously. This is achieved through the spectral decomposition of a graph that encompasses in-distribution (ID) data, covariate-shift OOD data, and semantic-shift OOD data.

The paper not only presents this innovative approach but also offers valuable theoretical insights into the learned representations. It is worth noting that the paper claims that the closed-form solution for the representation is equivalent to conducting spectral decomposition of the adjacency matrix.

Furthermore, the experimental results, conducted on various datasets, showcase the impressive performance of the Spectral Learning with Wild data (SLW) framework. The evidence provided through these experiments underscores the framework's competitiveness and potential to make significant contributions to the field of OOD generalization and detection.

The paper's combination of theoretical analysis and empirical validation, along with its innovative approach, suggests that it has the potential to bring valuable advancements to the understanding and application of spectral decomposition in addressing OOD challenges. However, some additional clarifications and refinements may be needed to fully grasp the scope and implications of the proposed framework

### Weaknesses
•	Confusion Between Augmented Graph and Image: The paper appears to introduce both augmented graphs and augmented images, but the relationship and distinction between these concepts are not well-defined. The authors should provide a more comprehensive explanation of how these two augmentation techniques are related and used in conjunction within the paper. A clear rationale for why both augmented graphs and images are necessary should be provided to justify their inclusion. 

•	Model complexity: Constructing the adjacency matrix, which encodes image connectivity, presents challenges in terms of both its creation and computational demands. The difficulty associated with building the adjacency matrix, along with the potential challenges of computation in real-world data, warrants careful consideration.

•	The paper introduces the term \frac{9}{8}\alpha without a clear derivation or explanation of its significance. It is crucial to provide a detailed and step-by-step derivation of this term to enhance the paper's mathematical rigor.

•	Typos, for example, there is not x^+ in equation (1)

### Questions
The paper should engage in a meaningful discussion on the potential for extending the framework to a more diverse dataset. This discussion should touch upon the adaptability and robustness of the proposed methods, models, or techniques.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes to handle out-of-distribution generalization and detection tasks in a unified method. To this end, the authors propose a graph-based approach by constructing a self-supervised graph adjacency and a supervised graph adjacency based on the augmentation views of the data. Theoretical analysis is provided to justify the design from the perspective of feature decomposition and separability evaluation. Experiments on common benchmarks validate the proposed model.

### Strengths
1. The idea seems novel to my knowledge, and the model is reasonable and sound

2. The intuition behind the method is clearly described and the theoretical analysis well justified the model

3. The experimental results look promising and the improvements are significant.

### Weaknesses
1. The major concern for me on this work is the potential overclaim. The paper title describes the method as a "graph-theoretic framework", but instead, the method is purely based on some heuristic ways for constructing a graph from the data. Also, the theoretical analysis has weak connection with graph theory, and is based on linear algebra. Furthermore, the existing experiments fail to show how the method can act as a general "framework" where different models can be applied. From my personal view, I would recognize the method as a graph-based model instead of a "graph-theoretic framework".

2. The second concern is the limited evaluation in comparison with the broad claim in the title and introduction. For out-of-distribution generalization, there are diverse kinds of distirbution shifts in data, and the current work only studies one particular type, covariate shift. It limits the scope of this paper against the claim of "unifying out-of-distribution generalization and detection". Also, the selection for baselines is not that convincing. The baselines for out-of-distribution generalization tasks are published several years ago, and there are plenty of SOTA models that are missing. For OOD detection, the scores appeared in the paper are different from those reported in the paper of baselines. Is this due to that the authors use different protocols?

3. Some of the descriptions are misleading. E.g., the self-supervised graph adjacency and supervised graph adjacency. Also the section tiltle for 3.1 "Graph-theoretic formulation" is misguided. What does the graph theory refer to and how is the problem of OOD learning formulated as a graph problem?

### Questions
See the weakness section

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper consider the OOD generalization and detection at the same time. The authors embed the distance between samples into a graph w.r.t. supervised and self-supervised signals. and extract principle components through the graph spectral analysis. The overall training method is applying contrastive loss on these decomposed components. The authors provide further analysis to illustrate the insights and conduct experiments to demonstrate the prominent performances.

### Strengths
1. The overall method is interesting and novel. Considering both OOD generalization and detection together and using graph to model the sample correlations instead of directly using distribution similarities is intriguing.
2. The organization of the paper and the demonstrations of the theoretical insights are fantastic.
3. The performances of the method is extraordinary good from both OOD generalization and detection aspects.

### Weaknesses
1. The authors state that all distribution types are encapsulated, but I think the paper does not consider concept shifts, where P(y|X) varies. Notably, this shift is not trivial, e.g., if feature $X_c$ is the cause of label $y$ but due to noises, $X_s$ has higher correlation with $y$ during training but not in testing, then the method may fail. In such a case, $X_s$ is a more prominent component during training, thus, it will be extracted by SVD decompositions and mislead model training including the contrastive training.
2. I did not find the OOD generalization theoretical guarantees and the required assumptions. According to my understanding, it is impossible to solve OOD generalization problem using purely observational data without any interventional equivalent information or assumptions. Can the authors clarify what are the assumptions and the guarantees?
3. The method may not be well motivated. I don't see why the authors choose a graph to model the sample correlations.

### Questions
1. May it be possible to analyze without constructing a graph and achieve the same training loss with SVD decompositions?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
