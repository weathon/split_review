# Unsupervised graph neural networks with recurrent features for solving combinatorial optimization problems

- Decision: Reject
- Scores: 3, 3, 6, 5

## Abstract
In recent years, graph neural networks (GNNs) have gained considerable attention as a promising approach to tackle combinatorial optimization problems.
We introduce a novel algorithm, dubbed QRF-GNN in the following, that leverages the power of GNNs to efficiently solve combinatorial problems which have quadratic unconstrained binary optimization (QUBO) formulation.
It relies on unsupervised learning and minimizes the loss function derived from QUBO relaxation.
The key components of the architecture are the recurrent use of intermediate GNN predictions, parallel convolutional layers and combination of artificial node features as input.
The performance of the algorithm was evaluated on benchmark datasets for maximum cut and graph coloring problems.
Results of experiments show that QRF-GNN surpasses existing graph neural network based approaches and is comparable to the state-of-the-art conventional heuristics.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper leverages the GNNs to solve the quadratic unconstrained binary optimization problems, especially for the maximum cut and graph coloring problems.  Experimental results demonstrate the effectiveness of the proposed method.

### Strengths
1. Using Neural Networks to solve combinatorial optimization problems is an interesting topic.
2. The proposed QRF-GNN can outperform existing GNNs in solving Max-Cut and graph coloring problems.
3. The paper is well-written and easy to follow.

### Weaknesses
1. The paper's novelty appears constrained, utilizing a GNN with QUBO's continuous relaxation as a loss function for combinatorial optimization. Clarification on how this differs from prior work would be beneficial.

2. The motivation behind the specific design of the GNN, particularly the use of two different convolutional layers (SAGEConv Pool and SAGEConv mean) in the first layer, is not explained. A rationale for these choices should be provided.

3. An ablation study is needed to substantiate the proposed GNN's superiority over existing methods. Without this, the advantage of the proposed model remains unclear.

### Questions
Please refer to the weaknesses.

### Soundness
2 fair

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces an unsupervised QRF-GNN method for solving CO problems, characterized by two fundamental attributes: the general quadratic unconstrained binary optimization (QUBO) formulation and its recurrent design. Built upon the QUBO formulation, the proposed method compromises various CO problems including the maximum cut problem and graph coloring problem. Compared to the previous baseline PI-GNN, the main improvements lie in the refinement of the message-passing paradigm within graph neural networks, including introducing the recurrent feature, artificial input features, and parallel graph convolutional layers. Empirical results show that the proposed method outperforms existing unsupervised learning methods and is competitive with conventional heuristics.

### Strengths
1.The empirical results show advantages over previous methods built on QUBO formulation and are competitive with conventional heuristics.

2.The framework provides a general solution to a range of CO problems, though this property is derived from the existing QUBO formulation.

### Weaknesses
1.The novelty appears to be somewhat limited. It builds upon the foundation laid by PI-GNN [1], inheriting similarities in terms of problem formulation and experimental design. The primary enhancements are centered around the refinement of the message-passing mechanism within the graph neural networks. Moreover, the key characteristics of the proposed QRF-GNN, i.e., the unsupervised approach based on QUBO and the recurrent design, have previously been explored in methods like PI-GNN and RUN-CSP [2]. The methodological innovations do not appear compelling enough to warrant my vote for acceptance. Specifically, while the authors introduce a recurrent message-passing scheme, the core idea of using previous states to influence current decisions is already present in RUN-CSP, even if the specific implementation differs. The incremental nature of the changes, such as adding artificial input features and parallel graph convolutional layers, does not fundamentally alter the approach's novelty. The paper lacks a clear explanation of why these specific modifications are superior to other possible architectural choices, particularly given the existing work in recurrent GNNs for combinatorial optimization.

2.The rationale behind certain design choices remains unclear. Questions arise regarding the decision to incorporate the recurrent feature, artificial input features, and parallel graph convolutional layers in lieu of the raw GNN. If the objective is to enhance representation capacity, why not consider a more advanced GNN or GraphFormer design? It is also necessary to establish the relationship between these design choices and their relevance to CO problems. The paper does not provide a strong justification for why these particular architectural choices were made over alternatives, nor does it offer a clear analysis of how these choices impact the model's performance on different types of combinatorial optimization problems. For instance, the use of parallel graph convolutional layers is not well-motivated, and the paper lacks an ablation study to demonstrate the individual contribution of each component.

3.The evaluation presented in this paper does not convincingly demonstrate QRF-GNN's superiority over heuristic methods. In PI-GNN, Fig. 4 and 5 show its advantages in scalability and computational complexity. Yet these properties are not well verified in this paper. While the paper compares against some heuristics, it does not provide a comprehensive analysis of the scalability and computational complexity of QRF-GNN compared to these methods. The paper should include a more detailed analysis of how QRF-GNN scales with increasing problem size and how its computational cost compares to that of the heuristics, particularly in terms of both training and inference time. The lack of such analysis makes it difficult to assess the practical applicability of the proposed method.

### Questions
1.Why are recurrent features important for solving CO problems?

2.Since the methodology mainly focuses on the design of the graph networks, have you tried other advanced GNNs or GraphFormers in hand for better performance of this formulation?

3.In Table. 5, why is QRF-GNN more efficient than PI-GNN [1] while the main algorithm pipelines seem similar? It probably comes from the setting of PI-GNN in experiments: "In order to obtain the results of PI-GNN, the authors applied hyperparameter optimization for each graph." However, in my understanding, hyperparameter optimization is not a mandatory request of PI-GNN. It is worth investigating the performance of PI-GNN under the same conditions as QRF-GNN to determine if there is still a speed advantage.

4.In Section 5, the statement mentions, "...considering that most of the mentioned methods are specialized for solving specific problems...". In fact, many methods try to propose a general solving framework for solving broad CO problems, such as [2] [3] [4]. Additionally, solving algorithms for NP-complete (NPC) problems inherently possess the potential to solve other CO problems since any NP problem can be reduced to an NPC problem.

[1] Combinatorial Optimization with Physics-Inspired Graph Neural Networks. Nature Machine Intelligence 2022.

[2] Revisiting Sampling for Combinatorial Optimization. ICML 2023.

[3] DIFUSCO: Graph-based Diffusion Solvers for Combinatorial Optimization. NeurIPS 2023.

[4] From Distribution Learning in Training to Gradient Search in Testing for Combinatorial Optimization. NeurIPS 2023.

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
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors introduce QRF-GNN to efficiently solve problems that have a quadratic unconstrained binary optimization (QUBO) formulation.
The relaxed QUBO objective can be used to perform unsupervised learning for the GNNs. 

Further the GNN can be applied repeatedly by including the output probabilities from the previous round as node features in the next round.

### Strengths
The method is simple - relax the QUBO formulation with probability predictions and then use these to augment the node features in the next GNN step. Finally repeat until convergence.

For the loss simply minimize (or maximize) the QUBO formulation itself wrt the parameters.

To the best of my knowledge, this is the first time a QUBO probelm has been solved like this.

The results are competitive against other benchmarks algorithms to solve max cut and coloring problems.

### Weaknesses
Minor nit - The authors could have elaborated a little on the QUBO formulation and the training details before section 3.

### Questions
Did you'll try to solve QUBO problems other than max cut and coloring?

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
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper discusses the emergence of graph neural networks (GNNs) as a solution for combinatorial optimization problems. The authors introduce a new algorithm called QRF-GNN, which employs GNNs to efficiently address problems with quadratic unconstrained binary optimization (QUBO) formulations. QRF-GNN employs unsupervised learning and minimizes a loss function derived from QUBO relaxation. Its architecture includes recurrent use of intermediate GNN predictions, parallel convolutional layers, and a combination of artificial node features as input.

### Strengths
1. The paper is well written and well presented. 

2. The paper also focuses on an important problem QUBO problems via unsupervised learning (which may have certain benefits)

3. The paper shows experimental evidence that suggests that their method indeed works well.

### Weaknesses
1. I'm uncertain about the primary contributions of the paper. Are the key contributions limited to the QRF-GNN architecture and the incorporation of random node features combined with pagerank? Or do they also encompass the formulation of the problem as an unsupervised learning approach?

2. If the primary contributions are solely related to the architecture and node features, it's worth noting that while the results appear promising, the method might be viewed as somewhat incremental, especially when compared to existing methods like spectral clustering, which can be considered a basic form of unsupervised learning. In such a case, could you provide insights into any theoretical guarantees, if any exist for your work?

3. I have concerns about the reproducibility of this work, as it appears the authors haven't made the code base available. Additionally, they mention that the method lacks stability. How do you determine the best run under these circumstances?

### Questions
1. I'm uncertain about the primary contributions of the paper. Are the key contributions limited to the QRF-GNN architecture and the incorporation of random node features combined with pagerank? Or do they also encompass the formulation of the problem as an unsupervised learning approach?

2. If the primary contributions are solely related to the architecture and node features, it's worth noting that while the results appear promising, the method might be viewed as somewhat incremental, especially when compared to existing methods like spectral clustering, which can be considered a basic form of unsupervised learning. In such a case, could you provide insights into any theoretical guarantees, if any exist for your work?

3. I have concerns about the reproducibility of this work, as it appears the authors haven't made the code base available. Additionally, they mention that the method lacks stability. How do you determine the best run under these circumstances?

As it stands, I am inclined to recommend rejecting this paper. However, since I am not an expert in this field, I am open to revising my evaluation if the authors address these questions or if other reviewers support the work.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
