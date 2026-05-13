# Edge Importance Inference Towards Neighborhood Aware GNNs

- Decision: Reject
- Scores: 5, 6, 5, 5

## Abstract
Comprehensive model tuning and meticulous training for determining proper scope of neighborhood where graph neural networks (GNNs) aggregate information requires high computation overhead and significant human effort. We propose a probabilistic GNN model that captures the expansion of neighborhood scope as a stochastic process and adaptively sample edges to identify critical pathways contributing to generating informative node features. We develop a novel variational inference algorithm to jointly approximate the posterior of the count of neighborhood hops and learn GNN weights while accounting for edge importance. Experiments on multiple benchmarks demonstrate that by adapting the neighborhood scope to a given dataset our model outperforms GNN variants that require grid search or heuristics for neighborhood scope selection.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In this paper, the authors propose a probabilistic GNN model to address the challenge of determining the optimal neighborhood scope for information aggregation, which is crucial for enhancing GNN performance. The model utilises a beta process to represent neighborhood expansion as a stochastic process, enabling dynamic adaptation of the neighborhood scope. A variational inference mechanism approximates the posterior distribution over neighborhood hops, balancing the neighborhood scope and edge activation for a given dataset. The model adaptively samples edges, identifies significant pathways, and uses feature similarity to evaluate edge importance.

### Strengths
- The proposed model introduces a probabilistic approach to neighborhood expansion, which allows for flexible adaptation.
- The use of variational inference to approximate posterior distributions over neighborhood hops is novel.
- The model adaptively samples edges and identifies important pathways, which could potentially improve the quality of information aggregation.

### Weaknesses
Overall, my primary concern with this paper is the insufficiency and lack of convincing experimental validation. The primary experimental validation is conducted on small-scale datasets (e.g., Cora, Citeseer, Pubmed), which are known to be too limited for drawing strong conclusions in GNN research. These datasets are also prone to high variability due to different model initialisations, making the results less convincing. More experiments on large-scale datasets, such as those in "OGB" or "benchmarking graph neural networks", are needed to support the claims.

Also, the authors refer to ogbn-arxiv and ogbn-mag as "large-scale" datasets, but these are officially classified as "small-scale" and "medium-scale" in the OGB benchmark. Furthermore, these datasets are only used in a limited portion of the experiments (Tab. 3).

While the authors discuss over-smoothing measurements, Dirichlet energy is, in fact, more widely adopted in the literature compared to the total variation (TV).

In terms of methodologies, the paper misses the discussion of related work on path-based aggregation in GNNs, which addresses similar challenges (e.g., "Path Neural Networks: Expressive and Accurate Graph Neural Networks", ICML 2023).

Furthermore, the use of feature similarity to assess edge importance is straightforward, and it is unclear whether this approach is effective for larger datasets. This raises doubts about whether feature similarity alone can indeed accurately represent edge importance. It would be great if the authors could provide more insights on this point.

(Minor) Line 142: The sentence "Since GNN layer l aggregate information within l-th neighborhood" contains a grammatical issue.

### Questions
1. Could the authors provide more insights into the limitations of using feature similarity as the sole metric for edge importance, especially for large-scale datasets?
2. How does the proposed method compare with the related path-based aggregation methods, such as those described in the ICML 2023 paper mentioned?

### Soundness
2

### Presentation
3

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
This work considers the problem of determining the neighborhood scope of a problem. In other words, determining the contribution of nodes at different distances from the target. To tackle the inefficiency of the standard train-then-validate approach, a technique called *Bayesian Neighborhood Aggregation* (BNA) is presented, which uses a beta process prior on the contributions of nodes at different distances, and a conjugate Bernoulli distribution over the features dimensions used for message passing. The data likelihood is jointly optimized over the (mean-field) variational distribution and the model weights.

### Strengths
1. The idea of using a Bayesian model for inferring the neighborhood scope is novel.

2. The empirical analysis is quite thorough, with an evaluation of model performance, over-smoothing analysis, effect of kernel choice, performance on small and large datasets, and time and memory costs.

3. The model performs well, or at least competitively, in comparison to other baselines, in various aspects like the ones mentioned above.

### Weaknesses
1. The literature review in Section 2 looks weak because the description of the works is more about the proposed algorithms, but not their relevance to the current work. As in, the descriptions look like "ABC work does XYZ", but their strengths, weaknesses and/or relevance to BNA are not discussed. Another point is that despite the extensive literature review, in Section 4, no comparison is made with the Bayesian GNN methods, only with the architectural changes.

2. A modelling intuition, including strengths and weaknesses, is not presented for the choice of the beta process prior. All I understand is that a low $\nu_j$ reduces the weight of nodes at $j$-hops and further away, so the model assumes that the message importance decays monotonically as distance between nodes increases.

3. I am getting the impression that $\pi_l$ is the probability of receiving messages over each feature dimension from nodes **up to** $l$-hops away, and not exactly $l$-hops away, since the augmented adjacency matrix (with self-loops) is used for message passing at each step.

4. While the performance on benchmarks is competitive with the baselines, I would have been more interested in seeing conclusive evidence for neighborhood scope determination, perhaps using a synthetic dataset, where scope of the underlying ground-truth is known. All the other benefits are well and good, but I don't see compelling empirical evidence for automatic determination of neighborhood scope.

5. The manuscript claims that "The beta process induces hopwise activation probabilities and its conjugate Bernoulli process enables us to adaptively sample the edges in the neighborhood." This suggests that there is an inherent advantage in using the conjugate prior, when there doesn't seem to be one. Also, if not implemented in this work, I would appreciate a remark about the possible extension of this method to DropMessage-like dropping.

6. The degree matrix defined near line 132 should be in bold.

7. Kindly add the dimensions of the vectors and the matrices, as well as the spaces they belong to. For example, $\mathbf{H}_l \in \mathbb{R}^{N\times O}$.

8. How do the results in Figure 4 change, when the residual connections are not used? I am hoping to isolate the effect of BNA.

9. What does "Ours" correspond to in Table 2? Which kernel is being used, which architecture?

10. Possible typos (correct me if I am wrong; in that case, I may have read the related parts wrongly):
  - I think you are using \cite{...} everywhere, even where \citep{...} is more appropriate.
  - In Equation 9, the beta process samples should be in bold face.
  - At the end of line 203/204, it should be RHS instead of LHS.

### Questions
1. What is the advantage of using a conjugate Bernoulli-process for the feature masks? Analytical tractability is anyway not available, and the choice of conjugate prior does not exactly help with the variational learning, does it? Can you also use other masks on the feature matrix, maybe like the one in DropMessage, where all elements in the feature matrix are masked iid?

2. The degree matrix defined near line 132 should be in bold.

3. Kindly add the dimensions of the vectors and the matrices, as well as the spaces they belong to. For example, $\mathbf{H}_l \in \mathbb{R}^{N\times O}$.

4. How do the results in Figure 4 change, when the residual connections are not used? I am hoping to isolate the effect of BNA.

5. What does "Ours" correspond to in Table 2? Which kernel is being used, which architecture?

6. Possible typos (correct me if I am wrong; in that case, I may have read the related parts wrongly):
  - I think you are using \cite{...} everywhere, even where \citep{...} is more appropriate.
  - In Equation 9, the beta process samples should be in bold face.
  - At the end of line 203/204, it should be RHS instead of LHS.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces a framework that optimizes neighborhood scope selection in GNNs. This method adaptively samples edges within the neighborhood, allowing for the identification of critical pathways that contribute to effective node encoding. It is claimed to reduce computational overhead while also enhancing the GNN’s ability to capture relevant structural information.

### Strengths
The idea is novel, with a clear and reasonable motivation. The experiment structure is appropriate, and the results are solid.

### Weaknesses
The paper has several presentation issues, including inconsistent citation formatting (e.g., not using \citep) and a lack of uniformity in text font and size across figures. Additionally, the methods section is difficult to follow, making it challenging to fully understand the motivation and logic behind the proposed approach. Consistency among baselines is also needed across relevant methods; for instance, the time complexity table should include all over-smoothing methods to provide a complete comparison. It’s unclear why the method requires both $\mathbf{Z}$ and $\mathbf{\nu}$ to capture the importance of an edge.

### Questions
- See weaknesses.
- It’s unclear why the method requires both $\mathbf{Z}$ and $\mathbf{\nu}$ to capture the importance of an edge.

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
4

### Summary
In this paper, the authors propose a neighborhood-aware GNN model with adaptive edge sampling. Specifically, they use a variational inference to jointly infer the count of neighborhood hops and learn GNN weights. Experiments conducted on the node classification task showcase the effectiveness of their method.

### Strengths
1. Multi-dimensional model evaluation (effect, time, uncertainty, over-smoothing);
2. The principled approach;
3. The paper is well-organized.

### Weaknesses
1. The experimental comparison is insufficient. First, there is no introduction to the comparison method, and baselines are not new enough. Consider adding a recent method comparison. In addition, as an improvement to the basic GNN model, it is not enough to experiment only on node classification. The lack of comparison with more recent methods, especially those that also focus on adaptive neighborhood aggregation or sampling, makes it difficult to assess the true novelty and performance gains of the proposed approach. Furthermore, limiting the evaluation to node classification neglects the potential of the method for other graph-related tasks, such as graph classification or link prediction, where adaptive edge sampling could be particularly beneficial.
2. Does this method work effectively for heterophilic graphs? The performance of GNNs on heterophilic graphs is known to be challenging due to the mismatch between node features and labels across edges. The proposed method's reliance on neighborhood-aware mechanisms might be particularly sensitive to this issue, and it is crucial to evaluate its robustness in such scenarios. It is unclear how the adaptive edge sampling strategy interacts with the heterophily, and whether it exacerbates or mitigates the performance degradation typically observed on these graphs.
3. Consider adding further theoretical support or more visualization results of neighbor modeling. While the paper proposes a variational inference approach for learning neighborhood hops, the theoretical underpinnings of this approach could be strengthened. Specifically, it would be beneficial to provide more insights into the convergence properties of the proposed learning algorithm and the conditions under which it can guarantee optimal neighborhood selection. Additionally, more visualization results of the inferred neighborhood scope would help to understand the behavior of the model and validate the effectiveness of the adaptive sampling strategy.

### Questions
Please see the weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2
