# Bayesian Neighborhood Adaptation for Graph Neural Networks

- Decision: Reject
- Scores: 8, 1, 5

## Abstract
The neighborhood scope (i.e., number of hops) where graph neural networks (GNNs) aggregate information to characterize a node's statistical property is critical to GNNs' performance. Two-stage approaches, training and validating GNNs for every pre-specified neighborhood scope to search for the best setting, is a daunting and time-consuming task and tends to be biased due to the search space design. How to adaptively determine proper neighborhood scopes for the aggregation process for both homophilic and heterophilic graphs remains largely unexplored. We thus propose to model the GNNs' message-passing behavior on a graph as a stochastic process by treating the number of hops as a beta process. This Bayesian framework allows us to infer the most plausible neighborhood scope for messsage aggregation simultaneously with the optimization of GNN parameters. Our theoretical analysis show the scope inference improves the expressivity of GNN models. Experiments on benchmark homophilic and heterophilic datasets show that the proposed method is compatible with state-of-the-art GNN variants, improving their performance and providing well-calibrated predictions.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This work considers the problem of determining the neighborhood scope of a problem. In other words, determining the contribution of nodes at different distances from the target. To tackle the inefficiency of the standard train-then-validate approach, a technique called *Bayesian Neighborhood Aggregation* (BNA) is presented, which uses a beta process prior on the contributions of nodes at different distances, and a conjugate Bernoulli distribution over the features dimensions used for message passing. The data likelihood is jointly optimized over the (mean-field) variational distribution and the model weights.

### Strengths
1. The idea of using a Bayesian model for inferring the neighborhood scope is novel.

2. The empirical analysis is quite thorough, with an evaluation of model performance, over-smoothing analysis, performance on homophilic and heterophilic datasets, as well as small and large datasets, and computation time.

3. The model performs well, or at least competitively, in comparison to other baselines, in various aspects like the ones mentioned above.

4. The theoretical analysis of over-smoothing provides good support for BNA's expressivity.

### Weaknesses
1. The literature review in Section 2 looks weak because the description of the works is more about the proposed algorithms, but not their relevance to the current work. As in, the descriptions look like "ABC work does XYZ", but their strengths, weaknesses and/or relevance to BNA are not discussed. For example, near line 137, we have "half-hop adds slow nodes at each edge" - it is neither clear what *slow nodes* are (not that it is relevant for this work), nor is it obvious what context this piece of literature is supposed to add for the current work. In the absence of such an analysis, it is hard to contextualize the position of BNA in the current research landscape. An exception is Section 2.3, which does a good job describing how BNA differs from the rest of the Bayesian GNN frameworks, clarifying that these works target different problems. Another point is that despite the extensive literature review, in Section 5, no comparison is made with the Bayesian GNN methods, only with the architectural changes.

2. A modelling intuition, including strengths and weaknesses, is not presented for the choice of the beta process prior. All I understand is that a low $\nu_j$ reduces the weight of nodes at $j$-hops and further away, so the model assumes that the message importance decays monotonically as distance between nodes increases.

3. I am getting the impression that $\pi_l$ is the probability of receiving messages over each feature dimension from nodes **up to** $l$-hops away, and not exactly $l$-hops away, since the augmented adjacency matrix (with self-loops) is used for message passing at each step.

4. The best and second best models should not be computed across all architectures. Rather, for each architecture, the baseline and should be compared with its +BNA version to show how adding BNA affects model performance. This way, the results in Table 1 are unconvincing, for example, ResGCN is competitive with ResGCN+BNA, especially considering the standard deviations.

5. It takes 3-5x more time to train with BNA (Table 5). The authors claim that this is cheaper than performing CV over model depths, but this should be validated by comparing the methods under the same time budget. For example, set the budget to the time it takes for one BNA run, and perform CV over 3-5 model depth choices and then compare performance on test set.

6. While the performance on benchmarks is competitive with the baselines, I would have been more interested in seeing conclusive evidence for neighborhood scope determination, perhaps using a synthetic dataset, where scope of the underlying ground-truth is known. All the other benefits are well and good, but I don't see compelling empirical evidence for automatic determination of neighborhood scope.

7. Possible typos (correct me if I am wrong; in that case, I may have read the related parts wrongly):
  - I think you are using (\cite{...}) for citing inside parentheses, instead of the standard \citep{...}.
  - Near line 108, *... with ~~a~~ graph convolution layers.*
  - Space after "beta process" in line 178.
  - At the end of Equation 6 and in Equation 8, the beta process samples should be in bold face.
  - At the end of line 239/240, it should be *right-hand* instead of left.
  - In Equation 9, $\leq \lambda^L d_{\mathcal{M}}(\mathbf{H}_0)$ instead of $\mathbf{H}_0$.
  - Line 488, AU-ROC instead of AUC-ROC.

### Questions
1. What is the advantage of using a conjugate Bernoulli-process for the feature masks? Analytical tractability is anyway not available, and the choice of conjugate prior does not exactly help with the variational learning, does it? Can you also use other masks on the feature matrix, maybe like the one in DropMessage, where all elements in the feature matrix are masked iid?

2. The symbol $\otimes$ near line 204 should be defined; it is not obvious from the description. Am I correct to understand that this is not the usual Hadamard product, but rather a node-wise analogue?

3. Kindly add the dimensions of the vectors and the matrices, as well as the spaces they belong to. For example, $\mathbf{H}_l \in \mathbb{R}^{N\times O}$.

4. What is the need for adding residual connections in your model? I understand that they improve the expressivity and performance of GNNs in general, but what is its relevance for your theoretical analysis? I see that Res+BNA has better expressivity than Res alone, but I think you should also show how the expressivity of NoRes+BNA relates with that of NoRes. You do test your method with other message passing schemes, such as GAT and JK-Net, where residual connections are not added, so the residual connections aren't exactly needed in your model.

5. The proof of Theorem 2 relies on feature sampling reducing message passing across the graph (line 854, $\mathbf{H} \leftarrow (\mathbf{A}\pi_L+1)\mathbf{H}$), correct? In that case, does BNA exacerbate the over-squashing problem, making it unsuitable for long-range tasks.

6. Can BNA result in over-fitting? I see that PubMed requires information aggregation over 6-hops, while I was under the impression that it is a short range task that is modelled better by shallow networks.

7. Possible typos (correct me if I am wrong; in that case, I may have read the related parts wrongly):
  - I think you are using (\cite{...}) for citing inside parentheses, instead of the standard \citep{...}.
  - Near line 108, *... with ~~a~~ graph convolution layers.*
  - Space after "beta process" in line 178.
  - At the end of Equation 6 and in Equation 8, the beta process samples should be in bold face.
  - At the end of line 239/240, it should be *right-hand* instead of left.
  - In Equation 9, $\leq \lambda^L d_{\mathcal{M}}(\mathbf{H}_0)$ instead of $\mathbf{H}_0$.
  - Line 488, AU-ROC instead of AUC-ROC.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
3

### Summary
This paper proposes a message aggregation strategy based on Bayesian inference that adaptively selects multi-hop neighbor ranges and estimates the contributions of different nodes.

### Strengths
The method proposed in this paper can adaptively apply to different base GNN models to capture long-range relationships.

### Weaknesses
The performance improvement is quite modest compared to the computational cost.

### Questions
no further concerns

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces Bayesian Neighborhood Adaptation (BNA), a novel framework for automatically determining neighborhood scopes in Graph Neural Networks (GNNs). Rather than relying on a two-stage optimization to select the best number of hops for message aggregation, BNA employs a non-parametric Bayesian method. Specifically, it models the expansion of the neighborhood scope as a beta process and performs feature selection via a Bernoulli process. The proposed method allows GNNs to adapt their neighborhood scope dynamically, thus improving expressivity and performance on both homophilic and heterophilic graphs. The authors provide theoretical guarantees for improved model expressivity and conduct extensive experiments showing that BNA enhances GNN variants without introducing significant computational overhead.

### Strengths
- Originality: The paper presents an original solution to the problem of manually tuning neighborhood scopes in GNNs by framing the task as a Bayesian inference problem, which is a novel approach. This differs from typical HPO&NAS methods and introduces a probabilistic perspective on neighborhood adaptation.

- Quality: The theoretical analysis is rigorous, particularly in terms of expressivity, and the claims are backed by mathematical proofs. The experiments are thorough, spanning both homophilic and heterophilic graphs, and demonstrate consistent improvements across various GNN architectures. The use of a variational inference approach to handle the intractable computation of the beta process prior is well-executed, balancing model complexity and computational efficiency.

- Clarity: The methodology and theoretical sections are detailed, with clear explanations of the model formulation and the beta process. The figures, such as the one illustrating neighborhood adaptation, help clarify key concepts. The empirical results are presented comprehensively, with clear tables and comparisons to baselines, making it easy to follow the improvements brought by BNA.

- Significance: Automatically determining the neighborhood scope for message passing in GNNs is an important contribution, as it addresses a key bottleneck in GNN design. The potential impact of this method is significant, as it could simplify GNN model tuning, leading to more efficient and scalable applications of GNNs in various domains.

### Weaknesses
 - Diversity of baselines: It seems that the proposed method is evaluated as a plug-in trick for improving conventional GNNs. However, there have been lots of previous works that achieve adaptive depth in an efficient way (differentiable in some methods). It is necessary to include such works as the baselines here.

### Questions
Could the authors provide more insights into how the framework performs on significantly larger datasets, such as full ogbn-mag or ogbn-papers100M? How would the computational cost and memory usage scale with larger graphs?

What would be the impact of using low-quality or noisy data on the inferred neighborhood scope? Is the beta process robust enough to handle datasets with significant noise or missing edges?

Can the framework be extended to handle dynamic graphs where the structure evolves over time? What challenges might arise in adapting BNA for such scenarios?

### Soundness
2

### Presentation
3

### Contribution
2
