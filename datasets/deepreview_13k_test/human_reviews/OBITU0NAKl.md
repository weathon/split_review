# How Graph Neural Networks Learn: Lessons from Training Dynamics in Function Space

- Decision: Reject
- Scores: 5, 6, 8

## Abstract
A long-standing goal in deep learning has been to characterize the learning behavior of black-box models in a more interpretable manner. For graph neural networks (GNNs), considerable advances have been made in formalizing what functions they can represent, but whether GNNs will learn desired functions during the optimization process remains less clear. To fill this gap, we study their training dynamics in function space. In particular, we find that the gradient descent optimization of GNNs implicitly leverages the graph structure to update the learned function, as can be quantified by a phenomenon which we call \emph{kernel-graph alignment}. We provide theoretical explanations for the emergence of this phenomenon in the overparameterized regime and empirically validate it on real-world GNNs. This finding offers new interpretable insights into when and why the learned GNN functions generalize, highlighting their limitations in heterophilic graphs. Practically, we propose a parameter-free algorithm that directly uses a sparse matrix (i.e. graph adjacency) to update the learned function. We demonstrate that this embarrassingly simple approach can be as effective as GNNs while being orders-of-magnitude faster.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper investigates the function-space learning dynamics of graph neural networks (GNNs) during gradient descent. The key contributions include:

-   Identifying the similarity between GNN learning dynamics and cross-instance label propagation, facilitated by the neural tangent kernel (NTK).
-   Theoretical insights into why GNNs demonstrate strong generalization on graphs with high homophily, connected to NTK’s natural alignment with graph structure.
-   Development of a Residual Propagation (RP) algorithm inspired by these dynamics, showcasing notable performance improvements over standard GNNs.
-   Examination of GNN limitations on heterophilic graphs, including empirical validation on both synthetic and real-world datasets, revealing misalignments between NTK and the graph structure.

### Strengths
**Originality**: While connecting GNN dynamics to propagation schemes is novel, the paper lacks some innovation in terms of proposing new techniques beyond the basic RP algorithm. Theoretical insights relate to existing works on kernel alignment and generalization.

**Quality**: The theoretical claims rely heavily on assumptions of overparameterization and alignment of NTK with adjacency matrix, which may not perfectly hold in practice. More analysis is needed for finite width GNNs. Empirical evaluation is quite limited.

**Clarity**: The key ideas are reasonably clear, the significance of results is not fully crystallized.

**Significance**: The insights on generalization are incremental on existing theory on kernel alignment. Practical impact is unclear given the simplicity of RP and lack of evaluation on large benchmarks. The limitations of GNNs on heterophily are already well-known.

### Weaknesses
**Strong assumptions**: The study's theoretical framework is built on robust assumptions regarding infinite width and NTK alignment that may not hold across all scenarios. Expanding the analysis to cover finite-width GNNs could substantiate the findings.

**Limited evaluation**: The empirical validation is limited in scope, focusing on smaller datasets and simpler models. Extensive testing involving state-of-the-art GNNs and more diverse benchmarks would be instrumental in corroborating the theoretical claims.

**Significance in theory**:  The theoretical contributions, while valuable, seem to offer only a modest advancement beyond existing studies on kernel alignment. Clarifying the distinctions from previous work would help to highlight the unique contributions of this study.

### Questions
-   How does the theoretical analysis diverge from previous studies on kernel alignment? Clarification of the novel insights would be appreciated.
-   Given the recognized challenges of GNNs in dealing with heterophily, are there any strategies or recommendations proposed by the authors to tackle this issue beyond the current analysis?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies the training dynamics and generalization of graph neural networks (GNNs). The authors theoretically derive the evolution of the residuals of GNNs on training and testing data in several settings and based on this, they explain the generalization ability of GNNs. Some numerical verification is also reported.

### Strengths
1. The analysis of training dynamics and generalization is an extremely important topic in the research of GNNs. This paper has a good scope and is clearly written to connect ideas from different fields.
2. Although I think there are some limitations, the derived theoretical results are technically solid and are pleasing to read. The authors use tools from label propagation and graph neural tangent kernel to characterize the training dynamics of GNNs and they derive explicitly dynamics in several cases.
3. The authors give some reasonable explanation of the GNN generalization by connecting GNN training dynamics and optimal kernel.

### Weaknesses
1. In Section 4.2, the authors only consider two very special $\bar{\mathcal{X}}$, which makes the theory somehow limited.
2. The training dynamics of GNNs should be highly nonlinear. More explicitly, in equation (12), the GNTK $\Theta_t^{(l)}$ depends on $W_t$. However, the derived dynamics in Theorem 5 and Theorem are linear. The authors need to explain how they remove the nonlinearity and why it makes sense.

### Questions
1. This question is related to the second point in the "Weakness". According to your derivations in Section B.4, I think you remove the nonlinearity or the dependence of the kernel on the parameters $W$ by taking the expectation for $W$. Please correct me if I misunderstood something. I am confused as to why you take the expectation -- in my opinion, training dynamics is the evaluation of residuals or parameters for any given/fixed initialization. If you want to take expectation over $W$, I think the equation (14) and (15) should be stated as something like expected residual. Please explain what is happening and why it is reasonable.
2. In Theorem 5, do you have the training dynamics for optimizing $W^{(2)}$? In Theorem 6, is the training dynamics for optimizing all parameters in the GNN, or it is just optimizing parameters in a single layer (as in Theorem 5)?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper analyzes the learning dynamics of GNN in the function space and connects it to label propagation. The link is the residual propagation where the neural tangent kernel matrix is replaced by high order graph adjacency matrix. The authors show that the learning dynamics of infinitely wide two-layer GNN is a special form of residual propagation. The authors then study the generalization of GNN based on kernel-graph alignment.

### Strengths
(1) The connection between the learning dynamics of GNN and label propagation via residual propagation is novel and insightful. 

(2) The theoretical analysis is deep and elegant.

### Weaknesses
(1) The assumption of infinitely wide network is not realistic. It is better to analyze the evolution of the kernel. 

(2) The restriction to two-layer GNN or last-layer feature propagation is not realistic either.

### Questions
Is it possible to go beyond neural tangent kernel and two-layer GNN? What theoretical tools are needed? I assume there are methods developed for MLP.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent
