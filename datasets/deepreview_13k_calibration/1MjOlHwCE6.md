# Reducing Complexity of Force-Directed Graph Embedding

- Decision: Reject
- Avg Score: 2.50
- Scores: 3, 3, 3, 1

## Abstract
Graph embedding is a critical pre-processing step that maps elements of a graph network, such as its nodes or edges, to coordinates in a $d$-dimensional space. The primary goal of the embedding process is to capture and preserve various features of the graph network, including its topology and node attributes, in the generated embedding. Maintaining these graph features in the embedding can significantly enhance the performance of the downstream machine learning tasks. In this work, we introduce a novel family of graph embedding methods that leverage kinematics principles within a spring model and $n$-body simulation framework to generate the graph embedding. The proposed method differs substantially from state-of-the-art (SOTA) methods, as it does not attempt to fit a model (such as neural networks) and eliminates the need for functions such as message passing or back-propagation. Instead, it aims to position the nodes in the embedding space such that the total net force of the system is reduced to a minimal threshold, resulting in the system reaching an equilibrium state. The spring model is designed as a linear summation of non-linear force functions, with the shortest-path distance serving as the adjusting parameter for the force factor between each node pair, and therefore, inducing the graph topology in the force functions. In this work, we attempted to reduce the complexity of the original algorithm from $\log(n^2)$ to $n\log(n)$, while maintaining the performance metrics at a competitive level.
The proposed method is intuitive, parallelizable, and highly scalable. While the primary focus of this work is on the feasibility of the Force-Directed approach, the results in unsupervised graph embeddings are comparable to or better than SOTA methods, demonstrating its potential for practical applications.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The short review is as follows: the paper proposes a new set of graph embedding methods which instead of using message passing or back propagation, it uses spring model to construct graph embedding. Each nodes' positional embedding is the equilibrium state. I think there are quite a lot of paper that proposes new graph embedding methods, and in order to make a proposed method to work it needs to capture (1) global and local structure information (2) able to be learned and proactively adapted, otherwise no one would ever use the newly proposed embedding methods. From a brief walkthrough of the paper, I don't think the proposed method can be used as a way that proactively learns embeddings for nodes and graphs, which are useful for downstream tasks.

### Strengths
NA

### Weaknesses
NA

### Questions
NA

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper presents a novel method for computing graph embeddings using a spring model without any neural network/model.

### Strengths
The overall idea is interesting and offers a complimentary perspective.

### Weaknesses
The paper seems incomplete.

### Questions
N/A

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
While this paper presents an interesting force-directed graph embedding approach, the manuscript feels incomplete. I recommend that the authors include more powerful baselines (e.g., DGI [1], GraphZoom [2]) and conduct evaluations on larger graphs (with over 1M nodes) to better demonstrate improvements in accuracy and scalability for their next submission.

[1] Veličković et al., "Deep graph infomax", ICLR'19 \
[2] Deng et al., "GraphZoom: A Multi-level Spectral Approach for Accurate and Scalable Graph Embedding", ICLR'20

### Strengths
NA

### Weaknesses
NA

### Questions
NA

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
The paper presents a force-directed graph embedding method that reduces the computational complexity of an earlier approach proposed by Lotfalizadeh et al. The authors introduce a modification to limit the force computations to $k$-hop neighborhoods and a few randomly sampled nodes, resulting in a reduction from $O(n^2)$ to $O(n \log(n))$ complexity. This makes the proposed method potentially more scalable for large graphs while maintaining competitive performance in unsupervised graph embedding tasks like link prediction and node classification.

### Strengths
(++) **Scalability Improvement**: The proposed complexity reduction from $O(n^2)$ to $O(n \log(n))$ is a notable improvement.

(++) **Practical Utility**: The paper demonstrates comparable or slightly better performance to some state-of-the-art graph embedding methods while offering scalability improvements, which suggests that the proposed approach has practical utility for large graph datasets.

### Weaknesses
(----) **Limited Novelty**: The main contribution is an incremental improvement to the original method by Lotfalizadeh et al. The use of $k$-hop neighborhoods and stochastic sampling for complexity reduction, while useful, does not represent a fundamentally new idea in the context of graph representation learning. The paper offers no new theoretical contributions, insights, or analyses.

(----) **Relationship to Previous Work**: The relationship to previous work, by Lotfalizadeh et al. (2023, 2024) is ambiguous. It is not clear how this work fundamentally extends the original force-directed embedding approach from these works.

(--) **Limited Evaluation and Analysis**: The paper only evaluates the quality of the proposed embeddings using two downstream tasks: link prediction and node classification.

(---) **Presentation Issues**: There are multiple signs that the paper is incomplete. Some examples:
* Placeholders such as "!!! A PICTURE TO BE INSERTED for CAMERA READY !!!" at Line 239 and "!!! TO BE ELABORATED ON for CAMERA READY !!!" at Line 452. The Discussion section is empty!
* Typographical errors such as "topolofy" on Line 234 and starting the sentences on Line 186 with lowercase letters.
* Broken reference on Line 301.
* $\log(n^2)$ in Line 027 in the abstract should be $O(n^2)$.
* The notation $\mathbf{z}_{uv} = \mathbf{z}_v - \mathbf{z}_u$ was introduced on Line 140 to facilitate brevity, then used in equation 3, not used in equations 8 and 9, then used again in equations 13 and 14.
* The paper mentions several well-known graph embedding techniques on Line 273, such as LINE, SDNE, DeepWalk, and Node2vec, but does not provide proper inline citations for them.

(--) **Marginal Performance Improvement**: While not a deal breaker, the downstream task performance improvement on previous methods is marginal at best, as can be seen in Figures 3 and 5.

### Questions
1. Could you clarify the differences between this paper and the previous work by Lotfalizadeh et al.?
2. Could you expand the empirical analysis and evaluation with more downstream tasks, e.g., multilabel classification or clustering?
3. Besides improved performance on downstream tasks, what desirable qualities do the FD embeddings have? E.g., the paper mentions reflecting the topology of the graph on Line 234 as a rationale for some of your choices. Would it be possible to evaluate that with metrics such as mean average precision?
4. Could you make your code available for reproducibility purposes?

### Soundness
3

### Presentation
2

### Contribution
2
