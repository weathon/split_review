# Bypassing Skip-Gram Negative Sampling: Dimension Regularization as a More Efficient Alternative for Graph Embeddings

- Decision: Reject
- Scores: 5, 5, 5

## Abstract
A wide range of graph embedding objectives decompose into two components: one that attracts the embeddings of nodes that are perceived as similar, and another that repels embeddings of nodes that are perceived as dissimilar. Without repulsion, the embeddings would collapse into trivial solutions. Skip-Gram Negative Sampling (SGNS) is a popular and efficient repulsion approach that prevents collapse by repelling each node from a sample of dissimilar nodes. In this work, we show that when repulsion is most needed and the embeddings approach collapse, SGNS node-wise repulsion is, in the aggregate, an approximate re-centering of the node embedding dimensions. Such dimension operations are much more scalable than node operations and yield a simpler geometric interpretation of the repulsion. Our result extends findings from self-supervised learning to the skip-gram model, establishing a connection between skip-gram node contrast and dimension regularization. We use this observation to propose a flexible algorithm augmentation framework that improves the scalability of any existing algorithm using SGNS. The framework prioritizes node attraction and replaces SGNS with dimension regularization. We instantiate this generic framework for LINE and node2vec and show that the augmented algorithms preserve downstream link-prediction performance while reducing GPU memory usage by up to $33.3$% and training time by $22.1$%. Further, for graphs that are globally sparse but locally dense, we show that removing repulsion altogether can improve performance, but, when repulsion is otherwise needed, dimension regularization provides an effective and efficient alternative to SGNS.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes a regularization approach over embedding dimensions as an alternative to the conventional negative sampling strategy (i.e. noise contrastive estimation) adapted in the skip-gram-based graph representation learning methods. The authors apply the approach to the objectives of Node2Vec and LINE and evaluate the performance across multiple real-world datasets. The results demonstrate improvements in both computational efficiency, including reduced runtime and lower GPU memory requirements during optimization.

### Strengths
- Proposes a novel framework aimed at reducing running time and GPU memory requirements.
- Supports the proposed framework with theoretical analysis.

### Weaknesses
 - Given the current dominance of Graph Neural Networks (GNNs) in the graph representation learning domain, the practical relevance of the proposed framework may be limited.
- Application of the framework to Node2Vec and LINE results in significant performance drops (notably for Node2Vec), raising concerns about its practical effectiveness.
- The theoretical analysis provided lacks detail, making some claims difficult to follow.

- - For instance, in the proof of Proposition 2.2, it is not clear how we obtain the equation given in Line 730 from Equation 27. Although $C$ is defined as the minimum of the inner product of embedding vectors, $C$ is considered a constant, but embeddings depend on time and vary at every step, so I think $C$ also should depend on time. In Lines 731-732, the authors state that the constriction is monotonically increasing, since it remains positive. But this argument doesn’t guarantee that we will obtain $C\geq c$ for any given $c$. The series of the reciprocals of powers of 2 is monotonically increasing as well and convergent, so it can be given as a counter-example. The learning rate is also assumed to be convergent to 0 in Proposition, but it is ignored in the proof.

- - In Lines 257-259, the authors state that we can approximate $N_{SG}$ with the objection $N_{SG}^{’}$ for large sparse graphs, and then they provide Proposition 2.3 to validate this point. However, Equation 11 holds since the denominator term goes to infinity so it does not establish the convergence of the gradients of $N_{SG}$ and $N_{SG}^{’}$. The numerator term in Proposition 2.3 is upper bounded by the term $m\beta_{max}$ where $\beta_{max} \geq 1$ is a constant and $m$ is the number of non-zero entries in the sparse (assumption) similarity matrix $S$. Therefore, having an upper bound on the numerator term doesn't guarantee that it will "remain small". $m$ can be a very big number so the difference $|| \nabla N^{′}_{SG} − \nabla N_{SG} ||$ can still be large.
- - The derivation from Equation 37 to Equation 35 is not clearly explained.
- - A more detailed explanation in proofs and theoretical analysis would enhance the paper's quality.

- Applying the proposed method to additional approaches like VERSE [1] could strengthen the experimental validation.

- The notation in Defn. 2.1, $min_{i,j \in n x n}$ might be replaced by $min_{i,j \in [n] x [n]}$ to represent $[n]$ as a set of integers from $1$ to $n$.
- In Line 357, $j$ is the index representing batch, but it is overwritten in Line 358.
- In Equation 30, there should be a delta before $N_{SG}$.

### Questions
**Comments**

**Theoretical Analysis:**
- The provided theoretical analysis lacks rigor and clarity in certain parts:

- - For instance, in the proof of Proposition 2.2, it is not clear how we obtain the equation given in Line 730 from Equation 27. Although $C$ is defined as the minimum of the inner product of embedding vectors, $C$ is considered a constant, but embeddings depend on time and vary at every step, so I think $C$ also should depend on time. In Lines 731-732, the authors state that the constriction is monotonically increasing, since it remains positive. But this argument doesn’t guarantee that we will obtain $C\geq c$ for any given $c$. The series of the reciprocals of powers of 2 is monotonically increasing as well and convergent, so it can be given as a counter-example. The learning rate is also assumed to be convergent to 0 in Proposition, but it is ignored in the proof.

- - In Lines 257-259, the authors state that we can approximate $N_{SG}$ with the objection $N_{SG}^{’}$ for large sparse graphs, and then they provide Proposition 2.3 to validate this point. However, Equation 11 holds since the denominator term goes to infinity so it does not establish the convergence of the gradients of $N_{SG}$ and $N_{SG}^{’}$
- - The derivation from Equation 37 to Equation 35 is not clearly explained.
- - A more detailed explanation in proofs and theoretical analysis would enhance the paper's quality.

**Experimental Validation:**
- Applying the proposed method to additional approaches like VERSE [1] could strengthen the experimental validation.

*[1] Tsitsulin, Anton, et al. "Verse: Versatile graph embeddings from similarity measures." Proceedings of the 2018 world wide web conference. 2018.*

**Notations and Clarity:**
- The notation in Defn. 2.1, $min_{i,j \in n x n}$ might be replaced by $min_{i,j \in [n] x [n]}$ to represent $[n]$ as a set of integers from $1$ to $n$.
- In Line 357, $j$ is the index representing batch, but it is overwritten in Line 358.
- In Equation 30, there should be a delta before $N_{SG}$.


**Questions:**
- Given that only positive samples are used (i.e. $II^0$), it is interesting that embeddings do not collapse and that models (especially LINE) achieve comparable performance to vanilla versions. Could this be related to the choice of a small number of epochs?
- Since the approach assumes unweighted edges, could the authors discuss its applicability to weighted networks?

I vote for a score of 3 because of my concerns regarding the originality of the proposed approach, theoretical contributions, and experimental evaluation.

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
4

### Summary
This paper proposes an alternate repulsive force for skipgram (instead of negative sampling) based on dimension regularization.  At its core, it takes results from self-supervised learning (dimension mean regularization) and applies them to skip gram (but mostly graph embedding).  The authors argue that the proposed negative loss is more efficient (and therefore more scalable) than skipgram with negative sampling.  Experiments to evaluate the proposed regularization are performed on a handful of mostly citation datasets.

### Strengths
+  The proposed method's formalization seems nice, especially in terms of how it performs in the presence of dimensional collapse.
+  The paper's writing is generally good, and the author's methods are clear.

### Weaknesses
 -  There are some questions about novelty - in that the proposed regularization perhaps "already exists" in the SSL community and replacing SGNS is a seemingly obvious application.  However I'm not aware of work that actually does this (... but have not extensively looked for it).
- The core argument of the paper is that the proposed method is more efficient than SGNS and therefore "more scalable".   While the efficiency of the method is definitely better, its not obvious that it's an "online" loss, and the true scalability of SGNS comes from the fact that the loss can be computed (and parallelized) online.  Specifically, the method requires a full pass over the data to compute the mean for centering, which is not online. This is a significant limitation for large-scale graph embedding tasks where data arrives sequentially or is too large to fit in memory.
- There are not many (or really any) baselines used in the paper's experiments.  Since skipgram is well studied, it seems like more modifications of negative sampling or other related work might aide in understanding the proposed method better. For example, comparing against different negative sampling strategies (e.g., uniform, degree-based) or other contrastive losses would be beneficial. The lack of these comparisons makes it difficult to assess the true advantages and disadvantages of the proposed method.
- Finally, there is an apparent performance loss that comes from the proposed method.  This is present in the SBM experiments (Figure 2).  This is discussed some in the paper, but it seems like its the most important part and should be investigated more. The authors should provide a more in-depth analysis of why this performance degradation occurs and under what conditions it is most pronounced. It's crucial to understand the trade-offs between efficiency and accuracy.

### Questions
Please see weaknesses.  In addition, here are some more thoughts/questions.

- What's the primary draw of the proposed method?  If its truly efficiency, then we need to see how an online version of your method performs vs SGNS.

- Using downstream tasks (especially just a handful of graphs (4 of which are citation networks)) to prove the goodness of an embedding method just doesn't cut it these days.

- I would love extra experiments in the vein of Figure 2d.  Especially, how does SGNS compare to the full gradient solution (which presumably is better than SGNS, since it is itself an efficiency play).  What can we say about when each loss is better, worse, etc.

### Soundness
3

### Presentation
3

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
This paper presents a theoretical reinvestigation of skip-gram models, with particular focus on their dimensional properties. The authors demonstrate that while the skip-gram negative sampling (SGNS) loss function itself does not act as a dimension regularization technique, the preservation of dissimilarity between embeddings can be effectively achieved through dimensionality reduction methods. Building on these theoretical insights, the authors propose two key modifications to existing SGNS-based algorithms: (1) a mechanism to balance the trade-off between similarity and dissimilarity preservation, and (2) a strategic approach to introducing dimensionality regularization only after detecting embedding collapse.

### Strengths
1. The paper has a pretty solid mathematical interpretation (section 2). The proof flow is very good  and quite makes sense. 
2. The paper is pretty well-written and easy to understand.

### Weaknesses
1. Limited practical impact. The proposed augmentation shows consistent performance degradation in node2vec embeddings by approximately 5% (Table 2).  The authors also fail to present potential use cases where their modifications would be beneficial for graph embedding algorithms nowadays.
2. Dataset selection is inadequate: while the key point of proposed modifications lies in potentials in scalability, the dataset selection is Limited to small and medium-scale datasets and misses evaluation on large-scale datasets. 
3. Limited experiments: the experiments is mostly done on LINE and node2vec, which are pretty old graph embedding methods. It would be great if authors can provide some experiment results to justify how this can be potentially useful for  skip-gram based language models.

### Questions
1. Could you clarify the intended use cases for your proposed augmentation algorithm? The practical applications seem limited if the primary goal is scaling up LINE/node2vec. What other potential applications could benefit from this approach?
2. Could the proposed algorithm be used to scale up skip-gram based language models? 
3. Why in table 2 and 3, the key performance metric is AUROC instead of MRR/Hits@K? Given that link prediction tasks typically rely on ranking metrics, wouldn't MRR/Hits@K be more appropriate?

### Soundness
3

### Presentation
2

### Contribution
2
