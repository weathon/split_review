# Global minima, recoverability thresholds, and higher-order structure in GNNs

- Decision: Reject
- Avg Score: 3.50
- Scores: 5, 3, 3, 3

## Abstract
We analyze the performance of graph neural network (GNN) architectures from the perspective of random graph theory. Our approach promises to complement existing lenses on GNN analysis, such as combinatorial expressive power and worst-case adversarial analysis, by connecting the performance of GNNs to typical-case properties of the training data.  First, we theoretically characterize the nodewise accuracy of one- and two-layer GCNs relative to the contextual stochastic block model (cSBM) and related models. We additionally prove that GCNs cannot beat linear models under certain circumstances. Second, we numerically map the recoverability thresholds, in terms of accuracy, of four diverse GNN architectures (GCN, GAT, SAGE, and Graph Transformer) under a variety of assumptions about the data. Sample results of this second analysis include:
heavy-tailed degree distributions enhance GNN performance,
GNNs can work well on strongly heterophilous graphs,
and SAGE and Graph Transformer can perform well on arbitrarily noisy edge data, but no architecture handled sufficiently noisy feature data well.
Finally, we show how both specific higher-order structures in synthetic data and the mix of empirical structures in real data have dramatic effects (usually negative) on GNN performance.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors study the accuracy of GNNs with respect to the contextual stochastic block model (cSBM) for data generation. In Theorem 1, for one-layer GNNs, they prove some formulae for the accuracy under this model, which are derived based on the Gaussian error function, and then they show that a linear classifier can be as good as the best GNN. In Theorem 3, they derive accuracy formulae for two-layer linear networks. The paper is concluded with experiments.

### Strengths
- highly motivated problem
- having many experiments

### Weaknesses
 - the paper is not well-written; extensive revision is required to make the contributions clear
- the setup is limited and it is not clear whether the linear classifier is good beyond the assumptions
- nice theoretical results but I guess they are highly tied to the assumptions (limited)

- Section 4.2 is not well written. It is not clear what the authors want to say and it does not have flow. I strongly recommend rewriting it.

- The definition of $\sigma$ in page 4 is missing. It first seems it is a function, but apparently it is a constant?

### Questions
- I think the theoretical contributions of the paper are nice but unfortunately not enough and limited to particular assumptions 

- Section 4.2 is not well written. It is not clear what the authors want to say and it does not have flow. I strongly recommend rewriting it.

- The definition of $\sigma$ in page 4 is missing. It first seems it is a function, but apparently it is a constant?


-----------------------------------
After the rebuttal: I appreciate the authors for their response and revision; they have made significant changes to enhance the quality of the paper. Since they addressed my questions and comments, I have decided to slightly increase my score.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors analyze GNN architectures performance on different tasks. Theoretically they establish that for contextual Stochastic Block Model, linear GCN up to 2 layers attains maximum accuracy - in a certain sense. Empirically, they test different GNN architectures on a variety of datasets and study the effect of edge feature and higher-order structures. In conclusion, GNNs are shown to be more suited to learn simpler models such as cSBM and struggles with noisy data and higher-order structure information.

### Strengths
Experimental details are interesting and cover a wide range of datasets, both synthetic and from the real world. The conclusion of the paper is thought provoking, in showing that GNN is volatile to higher-order structures, and is more capable of learning simpler, albeit noisy, feature data. 

Theoretical results seem correct and self-contained. The take away from the theorems in this paper, in that there are many regimes where linear GNNs are enough to learn the optimal (in some sense) classifier is interesting and corroborated by other research in the literature. The conclusions drawn from the paper is more or less in-tune with current understanding of GNN performance under cSBM, in that nonlinearities need to be re-thought.

### Weaknesses
Unfortunately, I believe that the author missed a couple of key literature pieces. For instance, Wu, Chen, Wang and Jababaie ‘A non-asymptotic analysis of oversmoothing in GNN’ in ICLR2023. As a result, some key results of the paper have been shown or can be derived from existing results in the literature. For instance, Theorem 1 of the paper is established in Lemma 1 of Wu, Chen, Wang and Jababaie (granted that this paper do not make clear the distinction between homophily and heterophily regime, the results of Theorem 1 is a few lines away from their Lemma). In Wu et al, the authors also noted the ineffectiveness of nonlinearities (in particular ReLU) in Appendix K1, which may also give rise to much of the results of Theorem 2 in the current paper under review. Therefore, much of the theoretical contribution in this paper has already been established elsewhere.

There are also many (for some, major) notational issues with presentation (a few of which that I caught is deferred to the Question section).

### Questions
- Pg 3: n_out “the number of nodes in other classes”, do you mean “the number of neighbors in other classes”? Also, n_in and n_out are very dependent on i - the vertex, so i’d suggest writing n_in(i), for example, to avoid confusion (since you’ve already written \mathcal{N}(i), for example).
- Pg 3: Assuming that the means are of opposite sign does not cause loss of generality only in the case when the number of classes in 2. Can the results be generalized to more than 2 classes?
- Pg 3: First bullet point of Theorem 1. Do you mean “has the same distribution as”? (the equation is a random variable, not a distribution).
- Pg 3: First bullet point of Theorem 1. There seems to be some transpose or dot missing when taking the inner product of vectors (eg - mW should be either m^\top W or m \cdot W).
- Pg 4: Second bullet point of Theorem 1. What is the notation y[X], is it the same as y(X)? 
- Pg 4: Third bullet point of Theorem 1. The term “maximum accuracy” also lacks a clear definition in the main paper. 
- Pg 6: Statement of Theorem 3. The linear model still has a nonlinear sigma written in it. 
- Remark 2: What does “extremely dense” mean? Graphs sampled from SBMs are naturally dense (number of edges of quadratic order of number of vertices). 
- Equation 7 (page 14). The first derivative is also 0 when n_in = n_out (is it possible for some setting of the cSBM such that n_in = n_out with high probability?) Perhaps this is mentioned later on below equation 15 but it’s not clear what is the scope of “we make no claims” and if it’s wide enough, should be reflected in the main statement in the main paper. For instance, there are phase transition results for SBM that suggest that if lambda < 1 then the SBM is not distinguishable from Erdos-Renyi model with average degree d.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper investigates the application of graph neural networks to the Contextual Stochastic Block Model (cSBM).

First, the study begins by examining the accuracy of a single node in a single-layer (simple) graph convolutional network without non-linearities, conditioned on the graph structure.  Subsequently, the paper demonstrates that, under certain conditions (which are satisfied by the cSBM), the expected log-likelihood of a two-layer GCN with ReLU activation is lower-bounded by the expected log-likelihood without the ReLU activation. The accuracy for a two-layer (simple) graph convolutional network without non-linearities is also explored, and the formula for the accuracy conditioned on the graph structure is provided, specifically for a single node.

The paper concludes with an extensive set of numerical simulations, benchmarking various graph neural networks on the contextual stochastic block model and on other standard benchmarks.

### Strengths
The examination of graph neural networks' performance on contextual stochastic block models is an important and ongoing area of research. The theoretical analysis employs some interesting techniques, including the use of symmetry. Additionally, the experiments are quite extensive and could offer motivation for future work,

### Weaknesses
Theoretical results in this paper appear to be somewhat limited, as they focus on computing accuracy at single nodes and rely on fixed GCNs without training. Stronger and more informative findings can already be found in the existing literature, where guarantees for the performance of trained GCNs have been provided (for example, see [1,2])

[1] Wu et al. - A non-asymptotic analysis of oversmoothing in graph neural networks

[2] Baranwal, - Graph convolution for semisupervised classification: Improved linear separability and out-of-distribution generalization

### Questions
- Regarding the notation used, it's unclear whether 'W' is meant to represent a row or column vector. If 'z_i' is also a vector, it appears there might be a dimension mismatch in the final equation on page 3.

- Page 5, is the "i" in the equations " ... [X](i)  " a fixed a priori node i ?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies the performance of Graph Neural Networks (GNN) from three perspective on cSBM datasets.
First, the authors analyze the accuracy performance of GCN on cSBM datasets.
Then, the authors study the empirical performance of four classic GNNs on cSBM datasets with varied properties.
Finally, a discussion of the impact of high-order structure on GNNs is included.

### Strengths
1. The accuracy analysis on cSBM datasets reveal the cases when GCNs perform better, and why GCNs achieve optimality on cSBM graphs.
2. The empirical discussion over GNNs' performance on different data regimes is inspiring.
3. The paper is well written and can be clearly understood.

### Weaknesses
1. Analysis into heterophily on cSBM datasets have been made in [1][2].
2. The theoretical results are limited to 1-2 layer GCNs, and may not be inspiring enough for designing better GNNs. The analysis focuses on simplified scenarios, which limits the insights for more complex architectures or datasets. The theoretical results, while providing some understanding of GCN behavior on cSBMs, do not offer concrete guidance on how to modify or improve existing GNN architectures for better performance in practical applications. Specifically, the analysis does not extend to deeper GNNs or provide insight into the role of specific architectural choices like activation functions or normalization layers.
3. The empirical discussion is mostly restricted to 2-class cSBM datasets, so a gap exists between empirical results and real-world scenarios. The lack of experiments on multi-class datasets, or datasets with more complex structure, limits the generalizability of the conclusions. Moreover, the analysis fails to explore the impact of different feature distributions and their interaction with graph structure on GNN performance. This is a significant limitation since real-world datasets exhibit a wide range of feature characteristics.
4. It would be better if more explanation about how the empirical results are affected by the GNN architecture is provided. The paper does not sufficiently explore how different GNN architectures (e.g., GCN, GraphSAGE, GAT) respond to varying graph properties. It's unclear how the observed performance differences arise from specific architectural choices, such as the aggregation function or the attention mechanism. A more detailed investigation into these aspects would be beneficial.

### Questions
1. What's the physical meaning about Theorem 3? It would be better if more explanation is included.
2. What's the relationship between theoretical and empirical results?
3. Intuitively, the high-order structure will be affected by the one-hop structure. On a homophilic graph, its one-hop and high-order neighbors would both be homophilic.  
How to ensure the high-order impact is completely erased?
Does it suggest that designing high-order GNNs is meaningless?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
