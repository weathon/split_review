# When Do MLPs Excel in Node Classification? An Information-Theoretic Perspective

- Decision: Reject
- Scores: 8, 3, 3

## Abstract
Recent research has shed light on the competitiveness of MLP-structured methods in node-level tasks. Nevertheless, there remains a gap in our understanding regarding why MLPs perform well and how their performance varies across different datasets. This paper addresses this lacuna by emphasizing mutual information’s pivotal role in MLPs vs. GNNs performance variations. We first introduce a
tractable metric to quantify the mutual information between node features and graph structure, based on which we observe different characteristics of various datasets, aligning with empirical results. Subsequently, we present InfoMLP, which optimizes node embeddings’ mutual information with the graph’s structure, i.e., the adjacency matrix. Our info-max objective comprises two sub-objectives: the first focuses on non-parametric reprocessing to identify the optimal graph-augmented node feature matrix that encapsulates the most graph-related information. The second sub-objective aims to enhance mutual information between node embeddings derived from the original node features and those from the graph-augmented features. This integration of message-passing during preprocessing maintains the efficiency of InfoMLP, ensuring it remains as efficient as a standard MLP during both training and testing. We validate the effectiveness of our approach through experiments on real-world datasets of varying scales supplemented by comprehensive ablation studies. Our results affirm our analysis and underscore the success of our innovative approach.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies an Information-Theoretic Perspective on node classification on graphs, specifically, it focuses on the problem of when and why MLP can achieve good performances in graph representation learning tasks. The conclusion drawn from this paper is that when there is significant structural information contained within node features, MLP can achieve relatively good performances, since it does not require additional operators to introduce topological information. Motivated by this finding, the authors proposed a solution named InfoMLP, which aims to learn a node embedding that maximizes the mutual information between node feature and graph structure.

### Strengths
1. The most notable contribution of this paper is it explained how and why MLP can achieve relatively good performances in node classification on certain graph datasets, the mutual information justification is intuitive and serves as a strong argument.

2. Based on the observation that, MLP can only achieve good performances when graph structure information is partially contained in node features, authors proposed a mutual-information maximization approach to enhance the performance of MLP on the graph, which is novel and interesting.

3. The proposed method exhibits strong improvements over baselines, notably, this improvement is valid on both homophilous and heterophilic graphs.

### Weaknesses
1. Despite the insights and meaningful findings of this paper, the information-theoretic perspective is still rather empirical. While the mutual information justification is intuitive, the paper lacks a rigorous theoretical framework to support the claim that maximizing mutual information between node features and graph structure leads to improved performance in node classification. A more formalized theoretical analysis, perhaps involving bounds on generalization error or a more detailed study of the relationship between mutual information and downstream task performance, would significantly strengthen the paper's core argument.

2. The distinction between $Z_{aug}$ and $Z_{mlp}$ requires further clarification. While both are outputs of the same MLP encoder, the paper states that $Z_{aug}$ incorporates graph structure information while $Z_{mlp}$ does not. However, the precise mechanism by which this incorporation occurs is not explicitly defined. Furthermore, the term "ideal" node representation is not well defined. A more precise definition should be provided, perhaps specifying the properties that an "ideal" representation should possess in the context of node classification, such as discriminability, smoothness, or alignment with the underlying graph structure.

3. The paper states that the method aims to maximize $H(A|X)$, but the actual implementation involves a non-parametric mapping that fuses $X$ and $A$. The connection between this fusion and the maximization of $H(A|X)$ is not adequately explained. There is no guarantee that the proposed $X_{aug}$ actually maximizes the conditional entropy. If a theoretical justification is not feasible, the authors should provide a more intuitive explanation of how the fusion process relates to the information-theoretic objective. An ablation study that analyzes the information content of $X_{aug}$ by, for instance, visualizing the learned representations or quantifying the ability to reconstruct the adjacency matrix from $X_{aug}$, would provide empirical evidence for the effectiveness of the approach.

### Questions
No questions at the moment.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper addresses the question of how to incorporate structural information to MLPs. 
In other words, the latent question is: How structured must be MLPs? 
Quoting the authors: "In this work, we first aim to understand the reasons behind the successes 
of previous MLP-structured models for learning node representations". 
The main idea is to quantify the overlap between the node features and graph structures (it is 
well known that MLPs perform better than GNNs when the node feaures are uncorrelated with 
the graph structure/adjacency). As a result, the authors propose to maximize the mutual information 
between node embeddings and adjacency as a pre-processing step. 

InfoMLP, the proposed method, works as follows: "1) the generation of a graph-augmented node
feature matrix that encapsulates extensive graph structure information, and 2) the maximization of
mutual information between node representations learned from the original node features and the
generated graph-augmented node features.". 

Conditional probability between existing edges and feature correlations feeds an entropy estimator 
that proves to illustrate the overlap between feature distribution and structure (links) in well-known 
datasets. This leads to an upper bound of the H(A|X): conditional entropy of A given X.  

Then, 1) is addressed in order to facilitate information maximization. This leads to $X_{aug}$ as a 
function of powers of the transition matrix. 2) is addressed through standard MI maximization. 
However, for the sake of efficiency, the MI Loss during training is simply an Euclidean loss. Overall, 
"InfoMLP has the same complexity as a vanilla MLP in both training and testing".

Experiments show that InfoMLP is good in cold-start settings and outperforms significantly 
the state-of-the-art only in Pubmed. It fails in Cora.

### Strengths
* Nice methodology for comparing/integrating MLPs-GNNs.
* Good analysis of mutual information.

### Weaknesses
 * Not good results in standard datasets (e.g. Cora).
* This is probably due to the terse definition of the augmented features. Multi-hop diffusion seems to me not sufficient even when $K$ is adapted properly. The simple linear combination of powers of the transition matrix might not capture complex structural relationships, especially in graphs with intricate connectivity patterns. The method lacks a mechanism to adaptively weigh different hops based on the specific graph structure, potentially limiting its ability to extract relevant information from the graph. A more sophisticated approach, such as using attention mechanisms or learnable weights for each hop, could be beneficial.


### Questions
* How critical is the augmented representation? 
* How critical is the MI simplified Loss? (please see Rényi estimators). 
* Entropy estimation is very terse (positive vs negative distribution). Please, measure the overlap between positive and negative distribution using the Chernoff bound, for instance.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies the problem of node classification given node features and the graph structure information. The author propose a crude estimate on the extent to which node features cover graph structure information. Based on the idea of maximizing the mutual information between node embeddings and the graph structure, the authors introduce a novel regularization-based MLP model termed InfoMLP. InfoMLP consists of a preprocessing step and a learning step. Only the preprocessing step requires utilizing the graph structure information. Once the raw node features are preprocessed, InfoMLP has the same efficiency as a standard MLP during both the training and testing phases. Empirically, the proposed method demonstrates competitive performance over a few small benchmark datasets, while being much more efficient than existing graph neural networks.

### Strengths
- Efficiency is a major problem for the application of conventional GNNs in the industry, where practitioners often have to deal with graphs of massive size. This paper proposes an alternative and efficient method for node classification while utilizing both the raw node features and the graph structure.

- The idea to construct node embeddings during a preprocessing stage by explicitly maximizing the mutual information between node embeddings and the graph structure information is interesting, although not surprising. I liked this perspective.

- The empirical results over the selected benchmark datasets are promising, as shown throughout Section 4 in the paper.  (The additional results in the appendix, however, are on the pessimistic side, more on this later.)

### Weaknesses
 - A number of claims in Section 3.1 are not well justified by either theoretical or empirical evidence. Here are some examples:
  - At the end of page 3, the authors claim that "We hypothesize that this is due to the high degree of overlap between the information conveyed by node features X and the graph structure A", and then proceed with an "analysis" using the cartoons in Figure 1. First of all, I do not think that the hypothesis is correct in general. As a very simple example, consider a balanced stochastic block model with 2 equal-sized classes, inter-class edge probability q=0 and intra-class edge probability p=1. That is, consider a graph that consists of two complete subgraphs, with one subgraph corresponds to class 0 and the other subgraph corresponds to class 1. Furthermore, assign node IDs 1,2,...,N to the nodes uniformly at random, and let the node features be the one-hot encodings of node IDs. This makes I(X;A) = 0 since X and A are independent. However, it should be clear to see that, even in this case, a strong Laplacian regularization would make an MLP to perform nearly as good as, e.g., GCN. In my example above I am omitting details regarding the representation (which concerns with the ability to approximate/represent certain functions)  and generalization (which concerns with sample complexity) capabilities of MLP and GCN. I welcome the authors' feedback on this example. In any case, I would recommend the authors be careful about stating a hypothesis, in particular, when certain assumptions are required for a claim to be true.
  - I found that the authors were very vague in their discussion about comparing MLPs with GNNs. For example, in the second paragraph on page 4, when discussing Figure 1(b), the authors claim that "Thus, MLPs are expected to have the same capacity as GNNs in this context". The term capacity is a very vague term, here, do the authors refer to representational power, or do the authors refer to generalization capability? Note that when an MLP has a worse test accuracy than a GNN, it could be due to either expressiveness or generalization or both. Overall, I really could not appreciate the discussion in Section 3.1. I am not convinced by the authors' conclusion that the performance gap between MLP and GNN is determined by the mutual information. I would recommend the authors constrain the problem context by explicitly stating the required assumptions and focus on specific data generative models. Otherwise, the current claims feel very unsupported.
  - As another example, at the top of page 4, the authors claim that "..., a well-trained MLP model might implicitly derive an estimated graph structure matrix from the outset. It could then implicitly leverage both the estimated graph structure and the raw node features to generate node embeddings, thereby achieving performance similar to that of GNNs." This claim is neither theoretically justified nor empirically verified in this paper. Even in the extreme case where one considers augmented feature matrix X' = [X; A], so that the graph structure is completely covered by X', it is unclear if an MLP acting on X' can achieve similar performance to that of GNNs.
  - To be honest, I think the paper might be better if the authors simply delete Section 3.1. Alternatively, the authors should be very careful in the writing. Clearly state all necessary assumptions on the data/model/architecture, clearly define and use proper technical terms, and avoid using vague terms. Otherwise, I find it very hard to be convinced by the messages which the authors try to convey in Section 3.1.

 - There is a clear gap between $H(A|X)$ and $H(A|\hat{A})$ in equation 1, and the paper does not provide a bound on $|H(A|X)-H(A|\hat{A})|$. Therefore, it is difficult to determine how useful the proposed metric $H(A|\hat{A})$ is. The authors should at least discuss the reason to choose the $\ell_2$ distance for $\hat{A} = f(X)$.

 - Although the empirical results over small datasets in Section 4 look promising, the additional results over larger datasets in the appendix are not very good. Since one of the major advantages of MLPs over GNNs is efficiency, the performance of InfoMLP over larger datasets is more relevant and important. I think the authors should provide results on larger datasets in the main text, and place the results over small datasets in the appendix. However, over larger datasets, InfoMLP is outperformed by simple GNN architectures such as GCN or even SGC which does not suffer from efficiency issues.

### Questions
- In Theorem 1, why do we necessarily have that $H(A|X) = \inf_f H(A|\hat{A})$ (i.e. equality holds)? Based on the proof I think it should be $H(A|X) \le \inf_f H(A|\hat{A})$?

- For training and testing time of SGC reported in Table 5: I think that once preprocessing is done, SGC is basically a liner logistic regression. Why does it have slower training and testing time than InfoMLP?

- At the end of page 6, the authors claim that "Furthermore, the node embeddings $Z_{aug}$ are utilized to predict the node labels." Based on the description of the method, shouldn't $Z_{mlp}$ be utilized to predict the node labels? In any case, I think the authors should report the performance achieved by both $Z_{aug}$ and $Z_{mlp}$ for comparison purposes.

### Soundness
1 poor

### Presentation
2 fair

### Contribution
2 fair
