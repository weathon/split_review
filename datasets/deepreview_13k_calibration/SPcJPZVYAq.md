# YOSO: You-Only-Sample-Once via Compressed Sensing for Graph Neural Network Training

- Decision: Reject
- Avg Score: 5.75
- Scores: 5, 6, 6, 6

## Abstract
Graph neural networks (GNNs) have become essential tools for analyzing non-Euclidean data across various domains. During training stage, sampling plays an important role in reducing latency by limiting the number of nodes processed, particularly in large-scale applications. However, as the demand for better prediction performance grows, existing sampling algorithms become increasingly complex, leading to significant overhead. To mitigate this, we propose YOSO (You-Only-Sample-Once), an algorithm designed to achieve efficient training while preserving prediction accuracy. YOSO introduces a compressed sensing (CS)-based sampling and reconstruction framework, where nodes are sampled once at input layer, followed by a lossless reconstruction at the output layer per epoch. By integrating the reconstruction process with the loss function of specific learning tasks, YOSO not only avoids costly computations in traditional compressed sensing (CS) methods, such as orthonormal basis calculations, but also ensures high-probability accuracy retention which equivalent to full node participation. Experimental results on node classification and link prediction demonstrate the effectiveness and efficiency of YOSO, reducing GNN training by an average of 75\% compared to state-of-the-art methods, while maintaining accuracy on par with top-performing baselines.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
Paper is interested in sampling graphs, for the purpose of training graph neural networks, in cases where the input graph is large. Rather than taking gradient-steps using entire graphs, sampling-based training of GNNs can take gradient steps using subgraphs (more compute efficient).

Paper shows while indeed existing graph-sampling methods *can* scale learning onto larger graphs, *however*, they significant time in sampling itself (i.e., data prep) rather than on gradient calculation (i.e., training).

### Strengths
* GNNs are indeed popular architectures, solving problems across many domains. Even though there are many methods are proposes to speed-up training of GNNs, making things even faster, should realize some advantages.

* Their sampling method takes less time than competition, yet reaches SOTA metrics.

* Their sampling is computed only once, whereas competing methods draw subgraph samples for every input example every epoch. Since sampling time is significant (often the dominant), then sampling only once significantly saves resources.

### Weaknesses
# Related Work

*   Paper does not address non-sampling-based methods for speeding-up GNNs. At least, they should be mentioned in related work (IMO). One missed family is historical embeddings (e.g., https://arxiv.org/abs/1710.10568, https://arxiv.org/abs/2106.05609, https://arxiv.org/abs/2305.12322), another family is some "linearization" of models (a.k.a "decoupled" GNNs), e.g., https://arxiv.org/pdf/1902.07153, https://arxiv.org/abs/2004.11198, https://arxiv.org/abs/2111.06312). The related work should also discuss how these methods compare in terms of computational cost and performance trade-offs. For instance, methods that precompute embeddings or decouple message passing could offer different advantages and disadvantages compared to sampling-based approaches, and these should be discussed.

*   Other methods also sample-once. E.g., ClusterGCN. The paper should clearly differentiate its approach from methods like ClusterGCN, which also perform sampling once, and discuss the specific advantages of the proposed method over these existing techniques. This should include a discussion of the computational complexity and memory requirements of each approach.

# Sampling is inherently parallelizable

Paper is founded upon a statement that sampling takes more time than the actual training step. I believe the statement is correct (because the graph may be large and does not fit in memory). However, sampling is trivially distributable -- in fact, many papers, such as, PinSAGE, TFGNN, ..., propose and implement distributed or multi-threaded sampling. I think this could also be mentioned in the related work. The related work should also discuss the scalability of the proposed method in distributed settings, and how it compares to existing distributed sampling techniques.


# Possible Writing Improvements

*   First line of Intro: "analyzing" should probably become "modeling"
*   The abstract says "lossless" compression but line 90 says "nearly lossless". It is better to be consistent.
*   The term "embedding matrix" is used a few times in the first 2 pages, without clear definition of what it is -- is it the node input features? is it the hidden representations (between layers)? Is it the output of the GNN? I feel that it is all of those [but only after reading a couple of more pages]. The paper should explicitly define what the embedding matrix represents in the context of the GNN, and clarify how it is used in the sampling and reconstruction process.


# Missing analysis

The paper talks about bias and variance. This is usually done **either** in the forward pass -- let $\widetilde{z}$ be the latent values obtain via the graph sample and $\mathbf{z}$ be the latent values when full graph is used, the zero-biased analysis should show $\mathbb{E}[\widetilde{z}] = \mathbf{z}$; or in the backward pass e.g. $\mathbb{E}[\frac{\partial loss(\widetilde{z})}{\partial \theta}] = \frac{\partial loss(\mathbf{z})}{\partial \theta}$. This paper does neither of those, nor it shows bounds on the variance of these quantities. I suggest the authors remove bias&variance arguments or else show some analysis to back the arguments. The paper should provide a formal analysis of the bias and variance introduced by the sampling method, including mathematical derivations and bounds. This should include a discussion of how the sampling method affects the convergence of the GNN training process.

# Math inaccuracies
*   Adjacency matrix is square (N x N). How is it multiplied on the right by the model parameter matrix? Are GNN parameters a function of the input graph? This happens in Eq6 and Lines 5&7 in Alg1. The paper should clarify how the adjacency matrix is used in the GNN computation, and how it interacts with the model parameters. The dimensions of all matrices involved in the computation should be clearly defined.

*   Line 1 in Alg1 does not explain the initialization process. Crucially, is $U$ initialized to be a(n orthonormal) basis? The paper should provide a detailed explanation of the initialization process for the matrix $U$, including whether it is initialized as an orthonormal basis or not, and the implications of this choice.

*   line 161 "exists" must be a function of k and/or the rank of $\widehat{H}$ -- for example, what if I choose $k=0$, then there is no orthonormal basis $U$ that can recover $H$. In fact, $rank(\widehat{H})$ must be at least equal the rank of $H$ for recovery to be possible. The paper should clarify the conditions under which the orthonormal basis $U$ exists, and how the rank of $\widehat{H}$ affects the recovery process. The relationship between the sparsity level $k$ and the rank of $\widehat{H}$ should be discussed.

*   The sampling matrix (described below Eq1) can be better described. Can you explain its structure? or its motive? Even a google search on "compressed sensing sampling matrix" does not pull-up the answer immediately. What is its rank? The paper should provide a detailed explanation of the structure and motivation behind the sampling matrix, including its rank and how it is constructed. The connection to compressed sensing should be made more explicit.

*   Most-crucially, Eq2, which the rest of the work is founded upon, reads wrong/incomplete. Most-likely, *there are trivial typos, however, I will not do deductions and I expect all authors to ensure correctness of their **main** equation*. $\widetilde{H}$ reads as a scalar (the minimum norm). The paper should carefully review and correct Equation 2, ensuring that it accurately represents the intended mathematical operation. The meaning of $\widetilde{H}$ should be clearly defined.

*   Line 339: eigenvalues do not correspond to nodes. They correspond to eigenvectors. For instance, one can do a low-rank representation of the adjacency matrix (effectively using few eigenvalues). The paper should clarify the relationship between eigenvalues, eigenvectors, and nodes in the context of graph signal processing, and correct the statement about eigenvalues corresponding to nodes.

### Questions
+ Does the (sparse reconstruction) optimization problem have to be solved at every layer, for every new graph? Or is the assumption that the graph is always fixed (between training and inference)?

+ If the parameters of the model significantly change, isn't the re-sampling necessary? Why not sample with some periodicity (as model drifts), instead of sample only once at-start?

+ Is it at-all possible to think about the GNN in the inductive setting in your framework?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces YOSO, a novel compressed sensing-based sampling approach for Graph Neural Networks (GNNs) that samples nodes only once per training. By performing a one-time sampling at the input layer and a lossless reconstruction at the output layer, YOSO aims to minimize the computational burden associated with repeated sampling in GNN training. The proposed method is evaluated on node classification and link prediction tasks, demonstrating significant training time reduction (up to 75%) while maintaining comparable accuracy to several baselines.

### Strengths
1.	The paper is well-organized and easy to follow. It provides a thorough background on GNNs and compressed sensing, equipping readers with the necessary foundational knowledge. Additionally, the authors offer a detailed discussion on the use of compressed sensing for sampling and the proposed YOSO algorithm.
2.	The compressed sensing-based sampling method is both novel and effective in reducing computational overhead associated with sampling.
3.	The authors present experiments demonstrating YOSO's efficiency on large-scale graph datasets across multiple tasks, supporting the practical impact of their approach.

### Weaknesses
1.	The motivation for using compressed sensing-based sampling is unclear. Graph distillation or condensation methods could also be feasible for generating smaller graph datasets while preserving data distribution. What specific advantages does compressed sensing sampling offer over graph condensation? Furthermore, the paper does not discuss the potential drawbacks of using a one-time sampling approach, such as its inability to adapt to changes in the graph structure or node features during training, which could be a limitation compared to methods that perform sampling at each epoch.
2.	Compressed sensing relies on the Restricted Isometry Property (RIP) for accurate reconstruction. In the context of graph neural networks, it is unclear if RIP holds for the input feature matrix, representation matrix, and output matrix. The paper lacks a theoretical analysis or empirical validation of RIP in this context. Specifically, it's not clear if the graph structure and the GNN operations preserve the sparsity required for RIP to hold. Preliminary experiments would be beneficial to validate RIP applicability within GNNs, perhaps by examining the singular values of the matrices involved.
3.	This paper proposes using an unknown $U^{(l)}$ and an universal $\Phi$ to enhance the efficiency. However, a key question remains: does the universal $\Phi$ really exist? The paper does not provide sufficient justification for the existence of such a universal sampling matrix that works across different graph structures and node features. More justification is needed. Additionally, what’s the disadvantage compared with layer-wise $\Phi$? Is the accuracy loss significant? The paper should provide a comparative analysis of the performance and computational cost of using a universal $\Phi$ versus a layer-specific $\Phi$.
4.	For Line 257, I am confused on the forward propagation. Suppose the shape of $\Phi$ is M*N, the normalized Laplacian matrix is N*N, trainable parameters W is d*d, $T^{(l-1)}$ is M*d. It seems that the forward equation is incorrect with an unmatched shape. Is it like $\Phi A \Phi^\top$ to transform the adjacency matrix? The paper needs to clarify the exact mathematical operations and provide a clear explanation of how the sampling matrix is incorporated into the forward propagation of the GNN.
5.	The limitation discussion of YOSO is missing. (1) is YOSO robust over the initialization of sampling matrix $\Phi$? What’s the performance on a random initialized measurement matrix? Why do the authors design a handcraft sampling matrix? The paper should discuss the sensitivity of the method to the choice of the sampling matrix and provide guidelines for its selection. (2) YOSO requires more memory during GNN training? What’s the memory consumption of YOSO compared with other methods? The paper should include a detailed analysis of the memory footprint of the proposed method and compare it with other sampling techniques.

### Questions
Please see the weakness part.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents YOSO (You-Only-Sample-Once), an efficient algorithm designed to streamline graph neural network (GNN) training while maintaining predictive accuracy in downstream tasks. YOSO addresses the high computational overhead in existing sampling methods by introducing a novel compressed sensing-based framework. In this framework, nodes are sampled once at the input layer and then losslessly reconstructed at the output layer each epoch, eliminating costly operations like orthonormal basis calculations and ensuring high-probability accuracy retention comparable to full-node sampling. Experimental evaluations demonstrate YOSO’s effectiveness in reducing GNN training time by approximately 75% on tasks such as node classification and link prediction, achieving accuracy levels similar to leading baselines. This approach positions YOSO as a resource-efficient alternative with potential for significant performance benefits in large-scale GNN training.

### Strengths
1. The paper introduces a fairly novel method to train the GNNs, which is a significant as per the details provided.
2. The mathematical representation provided is fair enough to make the readers understand.
3. The results and the studies are significant to show the efectiveness of the framework. As per the problem, large-scale datasets are considered for the study, which is also appreciable.

### Weaknesses
1. The work is evaluated for only two tasks, i.e., Node classification and link prediction, in which the link prediction results are also just comparable to the baselines.
2. The performance metrics considered is accuracy and loss only. There should me more like F1-score as there may be data bias in case of such datasets.

### Questions
1. According to the article, YOSO operates on sparse data rather than the original dataset. Could this approach lead to potential information loss?
2. If there is data bias, how will it handle the same?
3. As the framework is tested for just two tasks, will it be generic for all type of graph related downstream tasks?

### Soundness
3

### Presentation
2

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces YOSO, a novel algorithm for efficient GNN training using a compressed sensing approach. GNNs are crucial for analyzing structured data, but existing sampling methods often introduce significant computational overhead. YOSO addresses this by sampling nodes only once at the input layer and using a nearly lossless reconstruction at the output layer for each epoch. This method reduces training time by about 75% compared to state-of-the-art techniques while maintaining high accuracy.

### Strengths
1. The concept of "sampling only once" presented in this paper is really interesting and novel, offering a fresh perspective on GNN sampling.
2. The author provides theoretical support to guarantee the effectiveness of YOSO, which is very convincing.
3. The author provides code to ensure the reproducibility of the paper's results.

### Weaknesses
1. According to Formula 1, the generation of $\mathbf{T}$ is closely related to the feature matrix $\mathbf{H}$. However, in YOSO, $\mathbf{U}$ is randomly initialized, and the generation of $\mathbf{\Phi}$ is only related to the graph structure. Does this approach overlook too much feature information? Specifically, the random initialization of $\mathbf{U}$ seems to disregard potentially valuable feature-specific patterns that could be leveraged for more effective compression and reconstruction. The method's reliance on graph structure alone for $\mathbf{\Phi}$ might not be sufficient to capture the nuances of node features, potentially leading to suboptimal performance in scenarios where feature information is highly informative.

2. The methodology section of the paper lacks a description of critical steps. The resulting representations $\mathbf{Z}$  do not have the scale as the input matrix $\mathbf{X}$. So, how should the nodes in $\mathbf{X}$ correspond to the representations in $\mathbf{Z}$? How can we obtain the representations for all nodes in the entire graph? What nodes' loss does $L_{GNN}(\mathbf{Z})$ calculate? Does this mean that it is necessary to sample nodes from the training set? The paper does not clearly explain how the compressed representation $\mathbf{Z}$ relates back to the original node space, which is crucial for understanding how the method can be applied to the entire graph and how the loss function is computed. The lack of clarity on these points makes it difficult to assess the practical applicability of the proposed approach.

3. Some important related works are missing. The paper only discusses related work on graph sampling, while relevant works on Compressed Sensing are not included. What are the objectives and common practices of this technique? Why can it be applied to the GNN sampling problem? These questions need further discussion. The absence of a thorough discussion on compressed sensing techniques leaves a gap in understanding the theoretical underpinnings of the proposed method. A more detailed explanation of how compressed sensing principles are adapted to the GNN sampling context is needed to fully appreciate the novelty and potential of the approach.

4. The mathematical notation in the paper is confusing, making it difficult to understand. For example, in line 155, $\hat{\mathbf{H}}$ should be $\hat{\mathbf{H}}^{(l)}$; in line 159, $\mathbf{U}^{\top}$ should be ${\mathbf{U}^{(l)}}^{\top}$; and in Equation 2, $\min$ should be $\arg \min$. These inconsistencies in notation create unnecessary confusion and hinder the reader's ability to follow the technical details of the paper. Consistent and accurate mathematical notation is essential for the clarity and credibility of any technical work.

### Questions
Please refer to the points I mentioned in the weakness part.

### Soundness
2

### Presentation
2

### Contribution
2
