# Tractable Probabilistic Graph Representation Learning with Graph-Induced Sum-Product Networks

- Decision: Accept
- Scores: 5, 6, 6

## Abstract
We introduce Graph-Induced Sum-Product Networks (GSPNs), a new probabilistic framework for graph representation learning that can tractably answer probabilistic queries. Inspired by the computational trees induced by vertices in the context of message-passing neural networks, we build hierarchies of sum-product networks (SPNs) where the parameters of a parent SPN are learnable transformations of the a-posterior mixing probabilities of its children's sum units. Due to weight sharing and the tree-shaped computation graphs of GSPNs, we obtain the efficiency and efficacy of deep graph networks with the additional advantages of a probabilistic model. We show the model's competitiveness on scarce supervision scenarios, under missing data, and for graph classification in comparison to popular neural models. We complement the experiments with qualitative analyses on hyper-parameters and the model's ability to answer probabilistic queries.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
While sum-product networks have been well-studied and proven to be efficient in tractable learning and answering probabilistic queries, all previous studies focus on data in the standard forms (e.g. numerical values or discrete classes). However, it has not been well-studied for graph representation learning and related areas. This paper introduces a new probabilistic framework Graph-Induced Sum-Product Networks (GSPNs), which achieves efficiency and efficacy by utilizing hierarchies of SPNs that allow transferable parameters. Extensive experiments are conducted to analyze the role of hyper-parameters and the model's ability to answer probabilisitic queries.

### Strengths
This paper studies an interesting and important problem, which is probabilistic queries for graph learning. Like standard sum-product networks, GSPNs can properly marginalize out missing data in graphs and provide more interpretability, in contrast to deep graph neural networks.

The construction of the networks (page 4 to 6) is detailed, and the hierarchical relationship is well-described. The optimization objective (Equation 1) is expected.

Section 4.2 emphasizes a major advantage of GSPNs, or probabilistic circuits in general, which is the ability to infer with incomplete data. The content in the section also provides the justifications on why certain operations are chosen (summing the average predictions of each mixture in the top SPN).

### Weaknesses
The writing of the beginning of Chapter 4 and Section 4.1 could be improved to a reasonable extent. The construction of the tree is highly technical and such a compact text makes the understanding difficult. The authors may consider the following two improvements: 1) write the process in a more rigorous way like a mathematics or TCS paper, i.e. formal definitions of the function $m(\cdot)$ and the heights $\ell$ of the tree; 2) add more figures to illustrate the construction process.

The subject of sum-product networks has a rich theoretical background, while this paper has little theoretical justifications, unless I missed anything. Many operations (such as the construction of the tree, transforming parameters, and summing top SPNs for inference with incomplete data in Section 4.2) are only justified in the hand-wavy way. Although ML is a highly empirical subject, probabilistic circuits are involved for interpretable inference and therefore, a reasonable amount of theoretical justifications may be necessary.

### Questions
1. Please refer to the second paragraph in the weakness section in case I missed any substantial theoretical justifications.

2. For Equation 1 on page 4, what exactly is the function $m_v(\cdot)$? Also, since $n_1$ is the root, it makes sense so that all other nodes are conditioned. However, when we infer other nodes, e.g. $m_v(n_2)$, do we try to optimize $\log \prod_{v \in V} P_{\Theta} (x_{m_v(n_2)} | x_{m_v(n_2)}, \cdots ) $?

3. In Section 4.2, how is the equation $x_v^{mis} = \sum_{i}^{C} \mathbb{E} [X_1^{mis} | Q_1^L = i] \times h_1^L(i) $ derived?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper suggests a framework for using Sum-Product Networks (SPNs) as Deep Graph Networks (DGNs). That is, the framework establish methods for representing a computation graph, such as the ones used in neural network architectures, as an SPN. The practical motivations for the work comes from DGNs, in general: (i) having overconfident predictions due to lack of uncertainty consideration, (ii) ad-hoc imputation method of missing data due to lack of probabilistic queries.
The authors suggest solving these issues by representing a DGN as a hierarchy of interconnected SPN and, therefore, being capable of answering probabilistic queries in a tractable manner.

### Strengths
* Tractable inference in DGNs: the tractable assumption over input distributions and SPN graphical properties enforcement allows for tractable probabilistic inference. This feature allows for a sound way of dealing with missing data.
* Probabilistic modeling of distributions over vertexes is beneficial in some specific applications, as it seems to be the case in the chemical domain. These are encouraging results for graph-based solutions in downstream tasks.
* Throughout and convincing experiments while exploiting well-established deep learning techniques such as residual connections.

### Weaknesses
* The manuscript would benefit from a theoretical discussion on the implications of generating tree SPNs from induced graphs, for instance, when capturing cyclic information.
* The paper does a good job motivating the work from the DGN perspective by bringing tractable probabilistic inference capabilities. However, the manuscript's relevance could be improved by highlighting the other way around: novel theoretical results to SPNs.
* Please fix the "Scarce Supervision" paragraph under Section 6: it currently contains a "Lorem ipsum" placeholder.

### Questions
* How do imputation methods compare with the formal way of dealing with missing data through probabilistic inference?
* Could you comment on the empirical convergence of the model? Was the model susceptible to variations on parameter initialization? And how did hyper-parameters were tuned?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper suggests utilizing tractable probabilistic models (TPMs) in graph representation learning. More precisely, the proposed graph-induced sum-product networks (GSPNs) are a class of hierarchies of sum-product networks (SPNs) that are capable of answering many types of probabilistic queries in a polynomial time in the size of the model. Further, the authors show that GSPNs are capable of dealing with missing data in the graph. The theoretical results are complemented by empirical experiments, where the authors show that are GSPNs are competitive on the tasks of scarce supervision, modeling data distributions with missing values, and graph classification.

### Strengths
I was unable to grasp every detail of the paper due to my limited knowledge of some of the topics, so please take my review with a grain of salt.

The main contribution of the paper is introducing the GSPN framework on the active area of graph representation learning with the following important properties:
- Efficiently computable probabilistic queries
- The ability to deal with missing data
- The ability to approximate the joint distribution over the random variables, where the graph can have arbitrary structure

Further, the empirical experiments demonstrate that the proposed class of structures is not only theoretically interesting but also in practice.

### Weaknesses
The paper could be more polished:
- As per formatting instructions, the citations should be in parenthesis when they are not part of a sentence.
- "The neighborhood of a vertex $v$ is the set $N_v = \lbrace u \in V | (u, v) \in E\rbrace$ of incoming edges": the neighborhood is not a set of edges but vertices.
- Section 6 starts with a lorem ipsum paragraph

### Questions
If I understood correctly, a small height L of the trees for graphs with a large diameter (consider, e.g., an n-cycle) would result in the trees containing only few of the vertices of the graph. On the other hand, a large L leads to an exponential blowup in the size of the trees, which is computationally infeasible. Is having the trees contain only few of the vertices of the graph detrimental, and if yes, then how harmful is it?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
