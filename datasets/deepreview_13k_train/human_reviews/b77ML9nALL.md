# Tackling Feature and Sample Heterogeneity in Decentralized Multi-Task Learning: A Sheaf-Theoretic Approach

- Decision: Reject
- Scores: 6, 5, 3, 5

## Abstract
Federated multi-task learning (FMTL) aims to simultaneously learn multiple related tasks across clients without sharing sensitive raw data. However, in the decentralized setting, existing FMTL frameworks are limited in their ability to capture complex task relationships and handle feature and sample heterogeneity across clients. To address these challenges, we introduce a novel sheaf-theoretic-based approach for FMTL. By representing client relationships using cellular sheaves, our framework can flexibly model interactions between heterogeneous client models. We formulate the sheaf-based FMTL optimization problem using sheaf Laplacian regularization and propose the Sheaf-FMTL algorithm to solve it. We show that the proposed framework provides a unified view encompassing many existing federated learning (FL) and FMTL approaches. Furthermore, we prove that our proposed algorithm, Sheaf-FMTL, achieves a sublinear convergence rate in line with state-of-the-art decentralized FMTL algorithms. Extensive experiments demonstrate that Sheaf-FMTL exhibits communication savings by sending significantly fewer bits compared to decentralized FMTL baselines.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a novel framework for Federated Multi-Task Learning (FMTL) that addresses the challenges of feature and sample heterogeneity across clients in a decentralized setting. A Sheaf-based approach Sheaf-FMTL is used to model complex interactions between client models, promoting local communication while maintaining performance. Experiments demonstrate that Sheaf-FMTL can support communication with models of different sizes and reduce the communication burden.

Overall, this article gives an effective way of organizing federated clients that achieves good inter-client information communication and could be a direction for federated learning training and development. However, there may be some parts that need to be further described, clarified and supplemented.

### Strengths
Overall, this article gives an effective way to organize federated clients that achieves good inter-client information communication and could be a direction for federated learning training and development.

### Weaknesses
For the theoretical part, the objectives formulation of FMTL in existing scenarios should be clarified before elaborating the methodology Sheaf-FMTL. To support the claimed contribution that the Sheaf-FMTL design unifies PERSONALIZED FL, CONVENTIONAL FMTL, HYBRID FL, and CONVENTIONAL FL, more illustrations combined with formulas in addition to Remark 3.3 are supposed to provide.

On the experimental side, I currently have the following questions and concerns,
(1) the additional time-space costs associated with the training and storage of restriction maps need to be clarified. 
(2) Can Sheaf-FMTL adapt to more general FL training scenarios? The authors are suggested to explain the scalability of the proposed method, especially, with more complex data, and larger parameter space (e.g. more complex neural networks). Also, additional computational costs, time and storage space consumption are the concerns under the complex scenarios.
(3) Since this work aims to address heterogeneity and unify multiple FL scenarios, data partitioning should be made more explicit, either in terms of the amount of data, domains (maybe), and classes (label distribution) between clients, or generalized by some sort of Non-IID metrics or pre-existing partitioning instance.

### Questions
1. Please clarify the additional time-space costs associated with the training and storage of restriction maps.
2. Can Sheaf-FMTL adapt to more general FL training scenarios? Please explain the scalability of the proposed method, especially, with more complex data, and larger parameter space (e.g. more complex neural networks). 
3. Please give more explicit data partitioning.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This work studies the federated multi-task learning (FMTL) problem. It points out that existing FMTL frameworks have limitations in handling feature and sample heterogeneous clients and introduces a sheaf-theoretic-based method. Specifically, the optimization objective leverages a sheaf Laplacian regularization that facilitates the modeling of client model interactions. Theoretically, the proposed algorithm achieves a sublinear convergence rate and experimentally, the proposed algorithm outperforms the dFedU algorithm.

### Strengths
The topic is of great interest to the community. The introduction of sheaf Laplacian regulariztion to the objective function in FL is novel as it helps to model the interactions between heterogenous clients. This is meaningful when clients have different data distributions and/or model architectures.

### Weaknesses
The definition of federated multi-task learning (FMTL) is not clear across the manuscript and it seems that there exists disparity between what the authors claim it can do and what the method actually does in experiments. In the introduction, it is mentioned that "FMTL generalizes the FL framework by allowing the learning of multiple related tasks across several clients simultaneously." In the following texts, however, it seems that the setting is narrowed down to data/model-heterogeneous federated learning. For example, the experiments considers data heterogeneity and model heterogeneity. Then it remains to be discussed how the concept of FMTL differs from personalized FL or heterogeneous FL. To handle both data and model heterogeneity in FL, there have been a series of work leveraging knowledge distillation and in which scenario, should people select the method proposed in this work?

For high-dimensional models where $d_i$ is large, will it add communication cost and storage cost when messages are transmitted among the network? At each iteration $k$, each client needs to communicate twice to update the model and the matrices separately.

In the experimental section, more baseline algorithms should be compared. Currently the only benchmarking algorithm is dFedU algorithm. More personalized FL algorithms should be included here (some are included in the paper of dFedU algorithm). 

The experiments do not adequately reflect the task diversity aspect of FMTL, focusing primarily on data and model heterogeneity. The experimental design should include scenarios that explicitly demonstrate the algorithm's ability to handle diverse tasks, not just variations in data distributions or model architectures. The current setup, while addressing heterogeneity, does not fully capture the essence of multi-task learning where clients might be solving fundamentally different but related problems.

### Questions
1. For high-dimensional models where $d_i$ is large, will it add communication cost and storage cost when messages are transmitted among the network? At each iteration $k$, each client needs to communicate twice to update the model and the matrices separately.

2. In the experimental section, more baseline algorithms should be compared. Currently the only benchmarking algorithm is dFedU algorithm. More personalized FL algorithms should be included here (some are included in the paper of dFedU algorithm). 

3. The difference between FMTL and conventional personalized FL/heterogeneous FL should be elaborated in more details.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper studied federated multi-task learning (FMTL) and presented an approach to incorporate the principles from sheaf theory to understand the interdependencies between the tasks. Given an underlying topology of client relationships, the paper utilizes the notion of a cellular sheaf to model the interactions between clients in a decentralized FMTL setting. The modeling approach considers similarity through the use of a projection operator, which is integrated into the learning process as a regularization term. The paper then introduces an alternating gradient descent algorithm that addresses the unknowns (projection matrices and reward parameters) by iteratively fixing one variable and solving for the other.

### Strengths
The paper addresses federated multi-task learning, a growing area of interest due to its collaborative nature that enhances the effectiveness of the learning process.

### Weaknesses
Given that the proposed solution lacks theoretical guarantees on regret and that there are existing empirical approaches that effectively capture heterogeneous agents, its significance is somewhat limited.

The paper also fails to provide a detailed comparison with benchmark approaches, despite the fact that federated multi-task learning has been extensively studied in the literature.

The theoretical result on bounded gradient is not very significant under the assumptions on smoothness in the paper.

### Questions
1. An alternating gradient descent approach for a regularized cost function is a common technique in constrained learning. With this in mind, could you comment on the primary innovation and challenges addressed of the paper?

2. What are some scenarios where the task similarities are defined in terms of vector spaces as required in the paper? Often task similarities are modeled in the form communication network among the tasks, clustering, or specific structures on the features.

3. Can you provide practical examples and physical interpretations of how the sheaf-theoretic approach is applied to real-world problems? Specifically, could you share examples of graph models with fixed-space node features in practical scenarios?

4. Additionally, how is the sheaf-theoretic approach, specifically the interaction between the tasks, integrated into the experiments involving real-world data?

4. The significance of the proposed approach is unclear in the absence of a regret bound. 

5. What is the rationale for selecting dFedU as the sole benchmark for comparison, especially considering that the area has been extensively explored?

6. If considered for larger rounds, will the performance of solving the problems individually have a similar MSE in Fig 3b? If so, given that this also saves the communication cost, what is the advantage of the proposed approach over the naive approach of solving the tasks separately?

### Soundness
2

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
2

### Summary
Federated multi-task learning is an important framework that deals with multiple tasks simultaneously in federated learning. The authors claim that existing methods fail to capture complex relationships. This paper proposes a so-called "sheaf-theoretic approach".

### Strengths
This method is indeed an interesting work, which provides a different perspective.

### Weaknesses
1. I do not understand the limitations of existing FMTL methods. What do you mean by "without a deeper complex interdependencies between tasks"? What is the impact of such deficiencies?

2. The claimed convergence rate is $O(1/K)$, which lacks comparison with existing methods. Hope that authors can provide detailed comparison with the state-of-the-art FMTL methods.

3. For numerical experiments, more comparison with other FMTL methods are needed.

4. In general, I feel that this paper is hard to follow. I do not understand the sheaf-theoretic approach.

5. How to get eq.(8)? I do not follow. Hope that the authors can provide intuition and step-to-step derivation of eq.(8).

### Questions
How to get eq.(8)? I do not follow. Hope that the authors can provide intuition and step-to-step derivation of eq.(8).

### Soundness
2

### Presentation
1

### Contribution
2
