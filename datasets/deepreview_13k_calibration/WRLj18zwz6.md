# A Manifold Perspective on the Statistical Generalization of Graph Neural Networks

- Decision: Reject
- Avg Score: 5.40
- Scores: 5, 6, 5, 6, 5

## Abstract
Graph Neural Networks (GNNs) extend convolutional neural networks to operate on graphs.  Despite their impressive performances in various graph learning tasks, the theoretical understanding of their generalization capability is still lacking. Previous GNN generalization bounds ignore the underlying graph structures, often leading to bounds that increase with the number of nodes -- a behavior contrary to the one experienced in practice. In this paper, we take a manifold perspective to establish the statistical generalization theory of GNNs on graphs sampled from a manifold in the spectral domain. As demonstrated empirically, we prove that the generalization bounds of GNNs decrease linearly with the size of the graphs in the logarithmic scale, and increase linearly with the spectral continuity constants of the filter functions. Notably, our theory explains both node-level and graph-level tasks. Our result has two implications: i) guaranteeing the generalization of GNNs to unseen data over manifolds; ii) providing insights into the practical design of GNNs, i.e., restrictions on the discriminability of GNNs are necessary to obtain a better generalization performance. We demonstrate our generalization bounds of GNNs using synthetic and multiple real-world datasets.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper discusses the generalization of GNNs from a manifold perspective. In this setup, the graph is considered as sampled from an underlying manifold equipped with a Hausdorff probability measure. 

The authors aim to investigate the generalization gap between the following: A **GNN** trained on a sampled instance of the graph, and an **MNN** (Manifold Neural Network) that has the same structure and parameters as the GNN mentioned above.
Here, GNN and MNN specifically refer to low-pass filters.

The core of the paper lies in two theorems, which provide generalization gaps for both node-level and graph-level tasks. The main findings of the theorems are:
- The GNN trained on the sampled graph can generalize to the MNN on the original manifold.
- The trained GNN can generalize to other graphs sampled from the same manifold.
- The generalization error of the GNN is primarily influenced by several **key factors**: the number of nodes, the manifold dimension, and the spectral continuity constants $C_{L}$. Practically, this implies:
  - As the manifold dimension increases, more nodes are required to obtain a model with good generalization.
  - (**Important**) A larger $C_{L}$ represents stronger discriminative power but results in weaker generalization. This is a critical trade-off to consider when choosing a model.

The paper uses experiments to demonstrate the impact of these key factors.

### Strengths
1. The paper is well-structured, and the experiments respond well to each part of the theorem.

2. The paper presents two theorems, which contribute to the study of GNN generalization.

3. The two theorems provide practical guidance for the selection of filters.

### Weaknesses
1. The relationship between the experimental and theoretical settings is not clearly explained. In the appendix, the authors mention that the experiments use a graph convolutional layer (GCN). **Does GCN fall under Definition 4** as required by the theorems? Moreover, does the input used in the experiments meet the requirements of **Definition 1**? Also, GCN does not seem to match the filter structure that is analyzed in the paper.

2. The explanation of MNNs is insufficient for me. Are MNNs implemented by sampling graphs and running GNNs on them?

3. If the answer to (2) is yes, then shouldn't the paper provide a generalization bound between two separate runs of MNNs (effectively GNNs on two different sampled graphs)?

### Questions
Please refer to the Weaknesses section. 

If my questions can be addressed, I will consider increasing the score :)

### Soundness
2

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
This work studies the generalization bound of GNN by comparing the bound of the corresponding manifold neural networks. The results show that the generalization gap decreases as the number of nodes increases or the spectral continuity constant decreases. The experiments justify the theory, especially including the discussion about the regularize of the training.

### Strengths
1. The paper is clear and well-written.

2. The theoretical analysis is solid and correct based on my understanding.

### Weaknesses
1. Some definitions are not clear enough. For example, it is better to relate Eqn 16 to the expectation of Eqn 15 so that the generalization gap definition in Eqn 17 is aligned with the classical definition. Please let me know if my understanding is incorrect.

2. The contribution of the trade-off between discriminability and generalization gap is weak. I find that better discriminability is interpreted as a smaller regularizer, which is indicated by a larger continuity constant. This explanation is quite indirect. A stronger analysis of discriminability could be a discussion based on some quantity to measure the discriminability.

3. The theoretical contribution and the novelty of this work are not very clear. It is better to provide a table or a list to show the comparison between this work and existing theoretical works.

### Questions
In Eqn 7 and 8, there are $K_\epsilon(||x_i-x_j||^2/\epsilon)$ in both first steps. Is it a typo, otherwise isn't it a notation abuse of two different kernel functions?

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
2

### Summary
This paper considers the generalization performance of GNNs when the data lies in a manifold. Consider the problem of predicting target value $g$ from a one-dimensional graph signal $f$ on a compact Riemannian manifold $\mathcal{M}$. Two types of models are considered: the Manifold Neural Networks (MNN) induced from the Laplace-Beltrami operator on $\mathcal{M}$, and the GNN constructed on a finite number of i.i.d. sampled data points using a graph kernel. 
This paper evaluates the generalization performance of GNNs when the similarity graph is a Gaussian kernel-based graph and a $\epsilon$-graph, respectively. Here, the generalization performance is defined as the difference between the statistical risk in the sense of the average risk on $\mathcal{M}$ when applying the MNN and the empirical risk using the GNN on a finite number of points $\{(x_i, y_i)\}$. In particular, the rate of generalization gap with respect to the number of sampled data points and its dependence on the dimension of the underlying manifold $\mathcal{M}$ are derived. Furthermore, the generalization gap for node classification tasks is derived when we assume that data points with different labels are on different manifolds.
In numerical experiments, GNNs are applied to node prediction tasks on synthesis and real networks, and node classification tasks on point clouds. The dependence of generalization on data points and spectral continuity constants is also evaluated.

### Strengths
- A single methodology can be applied to the analyses of both regression and classification tasks. Furthermore, for classification, the analysis can be extended to the case where data points with different labels are on different manifolds.
- This paper provides detailed background knowledge on spectral theory on compact Riemannian manifolds, in particular, the Laplace-Bertlami operator, and MNN based on it. It is intended for those who are not familiar with the field, making it accessible to them.

### Weaknesses
 - I have a question about the significance of Theorem 1, especially about the dependence of the upper bound on the spectral continuity constant.
- If I understand correctly, the definition of generalization performance in theoretical analysis differs from that in the usual statistical learning theory. Specifically, the paper defines it as the difference between the statistical risk of the Manifold Neural Network (MNN) and the empirical risk of the Graph Neural Network (GNN), rather than the difference between empirical and statistical risks of the same model. This distinction needs further justification.
- I have a question about whether the generalization gap in numerical experiments appropriately corresponds to that in the theoretical analyses.
- L.261: Is it correct to assume that the feature vector (input to the first layer of GNN or MNN) at each point $x$ is 1-dimensional because the input signal $f$ belongs to $L^2(\mathcal{M})$. If so, can the theory be extended to high-dimensional feature vectors?
- l.293: I think $GA$ is different from the generalization gap in the usual statistical machine learning theory. Usually, the generalization gap is the difference between the empirical and statistical risks of the same model (i.e., hypothesis). In contrast, this paper uses GNNs for the empirical risk and MNNs for the statistical risk: when a new data point $x$ is sampled, the prediction value for $g(x)$ is computed using MNN $\Phi(\mathbf{H}, \mathcal{L}_\rho, \cdot)$ not GNN $\Phi_G(\mathbf{H}, \mathbf{L}_N, \cdot)$. This setting may be justified if we interpret $\mathcal{H}$ as a hypothesis space. However, I do not think it is a very popular setting. The authors should consider using a different term to describe the quantity $GA$.
- l.308: *Theorem 1 shows that the generalization gap decreases approximately linearly with the number of nodes $N$ in the logarithmic scale.*: I want to clarify what this means mathematically. Does it mean that the main term of $\log (GN)$ is $\tilde{O}(-\log N)$, where $\tilde{O}$ is the O-notation that ignores logarithmic orders. This point requires further explanation and clarification in the main text.
- l.311: *More importantly, we note the bound increases linearly with the spectral continuity constant $C_L$ [...].*: I have a question about this claim. In Theorem 1, the left-hand side $GA$ is uniform with respect to the hypothesis space $\mathcal{H}$, that is, independent of the specific hypothesis $h\in \mathcal{H}$. On the other hand, the upper bound on the right-hand side depends on the specific hypothesis $h$ (or specific MNN/GNN) through spectral continuity constant $C_L$. It is not clear if the spectral continuity constant $C_L$ is assumed to be uniform over the hypothesis space $\mathcal{H}$. If it is assumed, this assumption should be made explicit. Furthermore, the theoretical claim is about the upper bound, not the generalization gap $GA$ itself, and the tightness of the bound is not justified.
- l.378: In Figure 4, the linear fitting is applied only on a region with a training accuracy of over 95%. However, I wonder whether this is justifiable. In fact, since the previous argument for l.311 provides a tighter uniform bound on the hypothesis space $\mathcal{H}$, the inequality holds regardless of the training accuracy. The linear fitting is an approximation of the generalization gap rather than its upper bound, and the gap between the generalization gap and its upper bound is not justified to be small.
- l.378: Related to the previous, as the theoretical analysis applies to untrained GNNs, I suggest conducting numerical experiments using untrained GNNs to see if the implication from the theory is valid numerically for them. The results on untrained GNNs are not clearly presented in the current draft.
- l.474: *In all cases, we vary the number of nodes in the training set by partitioning it in $\{1, 2, [...], 1024 \}$ partitions when possible.*: Does this mean that when the whole dataset is divided into $k$ partitions, the training dataset is one of those partitions? If so, how is the test dataset chosen if the number of partitions is one? I also want to check whether this experiment is a transductive problem, i.e., the test dataset is available during training, and the training data is available during the test. It is not clear how the validation and test sets are chosen when the training set is partitioned.
- l.478: In the theoretical analysis, the generalization gap is defined as the difference in risk between MNN and GNN. However, interpreting the generalization gap in numerical experiments in that way is questionable for the following two reasons: first, numerical experiments use GNN for both training and testing. Second, assuming my understanding of the previous question about l.474 is correct, it is a transductive problem, which is different from the assumption in the theory. I want to ask the authors why it is justifiable to interpret the generalization gap in the numerical experiments as $GA$ in the theoretical analysis. The justification that the graph is low-dimensional does not justify using GNN as a proxy for MNN.
- l.497: If we want to make a statistical claim that there is a linear correlation, it is more appropriate to apply hypothetical testing such as t-test and ANOVA rather than using an arbitrary threshold of 0.95. The methodology for assessing the linear correlation requires more rigorous statistical justification.
- l.506: In the experiment in Figure 7, it is claimed that the relationship between the spectral continuity constant $C_L$ and the generalization gap is verified. However, the experiment does not measure the value of $C_L$ is not directly and assumes that increasing the regularizer reduces $C_L$, which shoulde be verified. The paper lacks a direct measurement of the spectral continuity constant and relies on an assumption about the effect of the regularizer, which is not sufficiently validated.
- l.506: Even if we do not take the tight uniform bound as we discuss in the question about l.311, I still have a question about the validity of Theorem 1 in numerical experiments. In Theorem 1, the dominant term in the upper bound, when $N$ is sufficiently large, is the last term $F^LC_3(\log N/N)^{1/d}$. However, this term is independent of the value of $C_L$. It implies that the generalization gap should be almost independent of $C_L$ when the number of nodes is large; this is not the case in Figure 7. The theoretical result suggests that the generalization gap should be independent of the spectral continuity constant when the number of nodes is large, which contradicts the experimental findings.

### Questions
- L.261: Is it correct to assume that the feature vector (input to the first layer of GNN or MNN) at each point $x$ is 1-dimensional because the input signal $f$ belongs to $L^2(\mathcal{M})$.
- l.293: I think $GA$ is different from the generalization gap in the usual statistical machine learning theory. Usually, the generalization gap is the difference between the empirical and statistical risks of the same model (i.e., hypothesis). In contrast, this paper uses GNNs for the empirical risk and MNNs for the statistical risk: when a new data point $x$ is sampled, the prediction value for $g(x)$ is computed using MNN $\Phi(\mathbf{H}, \mathcal{L}_\rho, \cdot)$ not GNN $\Phi_G(\mathbf{H}, \mathbf{L}_N, \cdot)$. This setting may be justified if we interpret $\mathcal{H}$ as a hypothesis space. However, I do not think it is a very popular setting.
- l.308: *Theorem 1 shows that the generalization gap decreases approximately linearly with the number of nodes $N$ in the logarithmic scale.*: I want to clarify what this means mathematically. Does it mean that the main term of $\log (GN)$ is $\tilde{O}(-\log N)$, where $\tilde{O}$ is the O-notation that ignores logarithmic orders.
- l.311: *More importantly, we note the bound increases linearly with the spectral continuity constant $C_L$ [...].*: I have a question about this claim. In Theorem 1, the left-hand side $GA$ is uniform with respect to the hypothesis space $\mathcal{H}$, that is, independent of the specific hypothesis $h\in \mathcal{H}$. On the other hand, the upper bound on the right-hand side depends on the specific hypothesis $h$ (or specific MNN/GNN) through spectral continuity constant $C_L$. In particular, let $C_\mathcal{H}$ be the infimum of the spectral continuity constant over $\mathcal{H}$: $C_{\mathcal{H}}:= \inf_{h\in \mathcal{H}} C_L$. The inequality replacing $C_L$ with $C_\mathcal{H}$ on the right-hand side must also hold and is a tighter uniform bound independent of specific hypothesis $h$.
- l.378: In Figure 4, the linear fitting is applied only on a region with a training accuracy of over 95%. However, I wonder whether this is justifiable. In fact, since the previous argument for l.311 provides a tighter uniform bound on the hypothesis space $\mathcal{H}$, the inequality holds regardless of the training accuracy.
- l.378: Related to the previous, as the theoretical analysis applies to untrained GNNs, I suggest conducting numerical experiments using untrained GNNs to see if the implication from the theory is valid numerically for them.
- l.474: *In all cases, we vary the number of nodes in the training set by partitioning it in $\\{1, 2, [...], 1024 \\}$ partitions when possible.*: Does this mean that when the whole dataset is divided into $k$ partitions, the training dataset is one of those partitions? If so, how is the test dataset chosen if the number of partitions is one? I also want to check whether this experiment is a transductive problem, i.e., the test dataset is available during training, and the training data is available during the test.
- l.478: In the theoretical analysis, the generalization gap is defined as the difference in risk between MNN and GNN. However, interpreting the generalization gap in numerical experiments in that way is questionable for the following two reasons: first, numerical experiments use GNN for both training and testing. Second, assuming my understanding of the previous question about l.474 is correct, it is a transductive problem, which is different from the assumption in the theory. I want to ask the authors why it is justifiable to interpret the generalization gap in the numerical experiments as $GA$ in the theoretical analysis.
- l.497: If we want to make a statistical claim that there is a linear correlation, it is more appropriate to apply hypothetical testing such as t-test and ANOVA rather than using an arbitrary threshold of 0.95.
- l.506: In the experiment in Figure 7, it is claimed that the relationship between the spectral continuity constant $C_L$ and the generalization gap is verified. However, the experiment does not measure the value of $C_L$ is not directly and assumes that increasing the regularizer reduces $C_L$, which shoulde be verified.
- l.506: Even if we do not take the tight uniform bound as we discuss in the question about l.311, I still have a question about the validity of Theorem 1 in numerical experiments. In Theorem 1, the dominant term in the upper bound, when $N$ is sufficiently large, is the last term $F^LC_3(\log N/N)^{1/d}$. However, this term is independent of the value of $C_L$. It implies that the generalization gap should be almost independent of $C_L$ when the number of nodes is large; this is not the case in Figure 7.

**Minor Comments**
- l.161: $P$ is undefined.
- l.165: $M$ is undefined.
- l.184: I think it is not appropriate for the main text to refer to Equation (23), which appears only in the Appendix.
- l.187: The fact that the Laplacian eigenvalue is discrete and, at most, countable should be proved. We can derive it from the fact that $\mathcal{M}$ is compact.
- l.329: Since $\rho$ indicates the density of the manifold $\mathcal{M}$ in the previous sections, it is not recommended to use $\rho$ as a general symbol for the Laplace operator such as $\mathcal{L}\_{\rho, k}$. The same applies to the graph Laplacian $\mathbf{L}\_{N, k}$ in l.333.
- l.334: Figure 3 is not referenced from the main text.
- l.359: $\epsilon$ is undefined in this section. Also, the dependence of $\epsilon$ on $k$ should be made explicit.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper investigates the statistical generalization capabilities of Graph Neural Networks (GNNs) from a manifold perspective. The authors propose a theoretical framework proving that when graphs are sampled from manifolds, the GNN's generalization error bound decreases logarithmically with the number of nodes and increases linearly with the spectral continuity constants of filter functions. The theory applies to both node-level and graph-level tasks, providing guidance for practical GNN design. The theoretical results are validated through eight real-world datasets.

### Strengths
1.First to analyze GNN generalization from a manifold perspective, providing a new theoretical viewpoint that is more relevant to practical applications compared to previous work.
2. Not only presents theoretical framework and generalization bounds, but also validates theoretical results through extensive experiments and provides practical guidelines for GNN design.

### Weaknesses
 - The paper requires input signals to be bandlimited (Definition 1) and filters to be low-pass (Definition 4). While the authors claim these assumptions are easily met, the practical implications of strictly enforcing these conditions, especially in noisy real-world scenarios, are not fully explored. Specifically, the degree to which real-world signals deviate from perfect bandlimitedness and how this impacts the theoretical guarantees needs further discussion. The paper should also provide more concrete examples of how to ensure low-pass filter conditions are met in practice, beyond simply adding a regularizer. The choice of regularizer and its impact on the filter's frequency response should be analyzed in more detail.

- The proposed Gaussian kernel-based graph construction method (Definition 2) requires computing the full adjacency matrix, which is computationally expensive for large-scale graphs with O(N^2) time complexity. Although the authors state that in practice they work with existing graphs, the theoretical framework is built upon this construction. The paper does not adequately address the discrepancy between the theoretical graph construction and the practical use of pre-existing graphs. It remains unclear how the theoretical results apply when the underlying graph structure does not conform to the Gaussian kernel construction. The paper should include a discussion on the sensitivity of the theoretical results to deviations from the assumed graph structure.

- The theoretical results heavily depend on the choice of spectral continuity constant C_L, but the paper lacks concrete guidance on how to select appropriate C_L values in practice. While the authors mention that a regularizer can reduce this constant, they do not provide a systematic method for determining the optimal value of C_L or the regularizer. The paper should explore the relationship between the choice of C_L, the regularizer, and the resulting generalization performance. A more detailed analysis of how to tune these parameters for different datasets is necessary.

### Questions
Please refer to weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper derives generalization bounds for spectral graph neural networks, based on the assumption that the graphs are obtained from a sampling procedure from an underlying manifold. The obtain generalization bound decreases with the number of nodes, and increases with the number of features and network depth. Experimental results corroborate the dependence of the generalization gap on these factors.

### Strengths
The paper is overall well written, and as far as I have checked the technical details seem to be correct. The experimental evidence that the generalization gap decreases as the number of nodes increases is interesting.

### Weaknesses
I don't like the assumptions made in this paper so much. It feels to me like they make the proof rather straightforward, but are rather far from reality. In particular, how common are the GNNs defined in equation (2)? How related are the GNNs in equation (2) to GCN, for which the experiments were carried out in practice? How likely is the assumption that the graphs are sampled from a manifold, for applications of interest (e.g., for the Cora, citeSeer datasets), and why is this assumption more reasonable than the assumption that the graphs were sampled from graphons as in previous work?

Overall, in comparison with the related work of Levie and Maskey cited in the paper,  I don't feel there is a significant upside. My impression that Maskey and Levie also showed generalization gaps which decrease with the number of node, and increase with model complexity (which can be equated with model complexity and  depth in this paper). True, these results were obtained for different GNNs and with a different limit model, but not clear to me why the manifold model, and spectral GNN, are  any "better"?

Main issue is a more detailed discussion of Maskey and Levie- if you would like to try to convince me what your contribution is over those papers, I will be happy to listen.

In addition, here are some minor points which you don't have to discuss in the rebuttal, but could address in your next version of the paper:

* Line 155 instead of "with" should be "from"

* In definition 4, Is the low-pass filter defined with the same d as the manifold? If so why?

* Line 280 you say assumption I makes sense, you can also explain why assumption II makes sense (e..g I believe it is satisfied by norm-based losses like MAE and RMSE)

* Line 370: not sure I understood your point about a single graph. As far as I recall, an alternative where several graphs were sampled from each manifold was not discussed.

* Mention in main text which GNN you use. I understand from the appendix that it is GCN.

### Questions
Main issue is a more detailed discussion of Maskey and Levie- if you would like to try to convince me what your contribution is over those papers, I will be happy to listen.

In addition, here are some minor points which you don't have to discuss in the rebuttal, but could address in your next version of the paper:

* Line 155 instead of "with" should be "from"

* In definition 4, Is the low-pass filter defined with the same d as the manifold? If so why? 

* Line 280 you say assumption I makes sense, you can also explain why assumption II makes sense (e..g I believe it is satisfied by norm-based losses like MAE and RMSE)

* Line 370: not sure I understood your point about a single graph. As far as I recall, an alternative where several graphs were sampled from each manifold was not discussed.

* Mention in main text which GNN you use. I understand from the appendix that it is GCN.

### Soundness
4

### Presentation
3

### Contribution
2
