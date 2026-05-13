# Decoupled Subgraph Federated Learning

- Decision: Accept
- Scores: 6, 6, 6

## Abstract
We address the challenge of federated learning on graph-structured data distributed across multiple clients. Specifically, we focus on the prevalent scenario of interconnected subgraphs, where interconnections between different clients play a critical role.  We present a novel framework for this scenario, named \textsc{FedStruct}, that harnesses deep structural dependencies. To uphold privacy, unlike existing methods, \textsc{FedStruct} eliminates the necessity of sharing or generating sensitive node features or embeddings among clients. Instead, it leverages explicit global graph structure information to capture inter-node dependencies.
We validate the effectiveness of \textsc{FedStruct} through experimental results conducted on six %diverse
datasets for semi-supervised node classification, showcasing performance close to the centralized approach across various scenarios, including different data partitioning methods, varying levels of label availability, and number of clients.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper works on subgraph FL for node classification, where inter-connections between different clients is important. 

It first computes a global L-hop neighborhood matrix before training. During training, it uses GNN for node feature embedding and use L-hop matrix multiplying a trainable matrix to calculate node structure embedding. Both embeddings are concatenated to get the final prediction result. Experiments show the performance.

### Strengths
1. Subgraph FL with inter-connections is an important topic.
2. Completing the missing L-hop features by learning a L-hop node structure embedding is an interesting idea.
3. Experiments show the performance.

### Weaknesses
 1. Privacy leakage. Before training, clients communicate to calculate the L-hop neighborhood matrix $\hat{A}$. In the 2-hop case, since the client knows 1-hop neighbors and the information during the communication, it is still able to reconstruct the 2-hop graph. Pruning cannot guarantee the privacy.
2. FedSage+ and FedGCN can outperform FedStruct.
3. In FedGCN, the server does not require a global adjacency matrix for homomorphic encryption. It only needs to know the node ids for encrypted aggregation and identify which nodes belong to each client for sending the aggregation result back.

### Questions
As in weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents a novel framework, FEDSTRUCT, to tackle the challenge of federated learning on graph-structured data distributed across multiple clients, particularly in scenarios involving interconnected subgraphs, it utilizes explicit global graph structure information to capture inter-node dependencies. The effectiveness of FEDSTRUCT is validated through extensive experiments on six datasets for semi-supervised node classification, demonstrating performance that approaches that of centralized methods across various scenarios, including different data partitioning strategies, levels of label availability, and numbers of clients.

### Strengths
1)	This paper studies a significant and interesting problem, and the method can be used in a wide range of real-world applications. 
2)	The paper is overall well motivated. The proposed model is reasonable and sound. Theoretical analysis is performed.

### Weaknesses
1) The abstract lacks a description of the background. I recommend briefly outlining the context of the issues addressed in this paper before elaborating on the key problems that are solved.

2) Figure 1 has not been cited and its placement is too early in the text; please adjust this detail. Additionally, Figure 2 is unclear; I recommend adjusting the proportions or border thickness of each subfigure.

3) In the Related Work section, you mention that FED-STAR shares structural knowledge, yet in the conclusion, you state, "No work has leveraged explicit structural information in SFL." Are "structural knowledge" and "structural information" the same concept? Please provide more clarification in the conclusion.

4) The formula following (1) is missing a comma; please check for similar issues throughout the paper.

5) Privacy is one of the directions addressed in this paper, yet most references are to other works. I suggest including some original proofs or experiments related to privacy to enhance the completeness of the article.

### Questions
See the weakness.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes a novel SFL method called FEDSTRUCT, which leverages the augmented explicit structure $\bar{A}$ to promote the SFL model performance. Moreover, they propose HOP2VEC to learn local structure embedding. FEDSTRUCT precalculates the $\bar{A}$ with privacy protection and prunes the $\hat{A}$ matrix to decrease the calculation complexity and communication costs, thus balancing the communication-privacy-accuracy trilemma.

### Strengths
1. The proposed method is novel, utilizing augmented explicit structure which can be regarded as global knowledge to promote the performance of the SFL model. 
2. Utilizing pruning skills decrease the calculation complexity and communication costs.
3. Well written and well formulated problem.

### Weaknesses
1. **Focus on Privacy**. How to  obstain the local L-hop combined adjacency matrix while not share the L-hop global Adjacency Matrix maybe play the core role in FEDSTRUCT. In APP D, the equations [30] [31], [32], what does the $\hat{A}^{[K]}_j$ mean? Should be $\hat{A}^{[k]}_j$? If so , the next question, for client $i$, how does it know all $\hat{A}^{[k]}_j$ for $ k \in [K]$ without sharing the global adjacency matrix in all clients.  So another question when computing, the $\tilde{A}^{[i]}_j \in \mathbb{R}^{|\tilde{V}_i| \times |{V}_j|}$, the same to $\hat{A}^{[i]}_j$? So $\hat{A}^{[i]}_k \times \hat{A}^{[k]}_j$ should be $\mathbb{R}^{|\tilde{V}_k| \times |{V}_k|}  \times \mathbb{R}^{|\tilde{V}_k| \times |{V}_j|}$， but according the definition before, the $|\tilde{V}_k| \neq |{V}_k| $, how does the computation continue? Maybe I miss something? I really hope you can explain it for me to understand the feasibility of FEDSTRUCT. That's my main concern about this paper.

2. **About the hyperparameters.** **1)** The analysis of $\beta$ is not enough, an essential parameter in FEDSTRUCT for various homophilic and heterophilic graphs, which directly dominate the performance and affect the  judgment of FEDSTRUCT's contributions. **2)**  It is so strange that the parameter $L_s$ and $L$ is set to1 for heterophilic graph chameleon in table 5. As the author states in lines 297-299, a heterophilic graph should own multi-hop nodes and a high-frequency filter to augment the local graph representation.

### Questions
see weaknesses.

If the first questions can be well explained, the rating should be higher.

### Soundness
3

### Presentation
4

### Contribution
3
