# S$^2$MAM: Semi-supervised Meta Additive Model for Robust Estimation and Variable Selection

- Decision: Reject
- Scores: 5, 6, 3, 5

## Abstract
Semi-supervised learning with manifold regularization is a classical family for learning from the labeled and unlabeled data jointly, where the key requirement is the support of unknown marginal distribution enjoys the geometric structure of a Riemannian manifold. Usually, the Laplace-Beltrami operator-based manifold regularization can be approximated empirically by the Laplacian regularization associated with the whole training data and its graph Laplacian matrix. However, the graph Laplacian matrix depends heavily on the pre-specifying similarity metric and may result in inappropriate penalties when facing redundant and noisy input variables. In order to address the above issues, this paper proposes a new semi-supervised meta additive model (S$^2$MAM) under a bilevel optimization scheme to automatically identify the informative variables, update the similarity matrix, and achieve the interpretable prediction simultaneously. Theoretical guarantees are provided for S$^2$MAM including the computing convergence and the statistical generalization bound. Experimental assessments on synthetic and real-world datasets validate the robustness and interpretability of the proposed approach.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper introduces a new Semi-Supervised Meta Additive Model (S2MAM) that aims to improve the robustness and interpretability of semi-supervised learning through bilevel optimization. The proposed model combines manifold regularization, meta-learning, and sparse additive modeling to automatically identify informative features while simultaneously performing semi-supervised learning tasks. Unlike existing methods that rely on pre-specified similarity matrices, S2MAM leverages probabilistic bilevel optimization to adaptively update both the similarity matrix and decision functions. The authors provide theoretical guarantees regarding convergence and generalization, and they validate the proposed model using synthetic and real-world datasets, demonstrating its robustness and interpretability against noisy and redundant variables.

### Strengths
(1) The paper introduces an innovative bilevel optimization framework for manifold regularization that addresses key limitations of existing semi-supervised learning models, particularly those involving noisy and redundant input variables. 
(2) The paper offers a rigorous theoretical foundation, including proofs for optimization convergence and bounds for generalization error. These theoretical results provide assurance about the robustness and applicability of S2MAM in different learning scenarios.
(3) Extensive experiments on both synthetic and real-world datasets show that S2MAM outperforms other state-of-the-art semi-supervised learning models, particularly in scenarios with noisy and redundant features. The robustness and interpretability claims are supported by competitive performance results.

### Weaknesses
 (1) While the paper provides a novel framework, the bilevel optimization procedure can be computationally expensive, especially for large-scale datasets. Despite the probabilistic bilevel framework simplifying the optimization process, the overall complexity might still be a limitation in practical applications. The computational cost stems from the nested optimization loops required to update both the feature masks and the model parameters. This is further exacerbated by the need to compute the Laplacian matrix, which can be a bottleneck for high-dimensional data. The paper lacks a detailed analysis of the computational scaling with respect to the number of samples and features, making it difficult to assess the practical applicability of the method for large datasets.
(2) The proposed method involves both Laplacian matrix computation and optimization over probabilistic masks, which may not scale efficiently to very high-dimensional datasets or very large sample sizes. Although theoretical guarantees are provided, the lack of a discussion on practical scalability leaves questions about how S2MAM would handle real-world big data scenarios. Specifically, the paper does not address how the method would perform with datasets containing millions of samples or features, which are common in many real-world applications. The memory requirements for storing the Laplacian matrix and the computational overhead of the bilevel optimization could become prohibitive in such cases.
(3) While the paper compares S2MAM against a wide variety of baselines, some comparisons (especially against modern deep learning-based semi-supervised models) are limited. This is particularly important since deep learning approaches have become dominant in semi-supervised learning tasks. The paper needs to include more comparisons with state-of-the-art deep learning models, such as those based on variational autoencoders or graph neural networks, to fully demonstrate the competitiveness of the proposed method. The current comparisons are insufficient to establish the superiority of S2MAM over modern deep learning-based approaches.

### Questions
(1) Could the authors clarify the learning dynamics of the probabilistic mask variables? Specifically, how does the model ensure convergence of these masks to truly informative features, and is there a risk of instability in mask selection during the optimization?
(2) How does S2MAM's computational complexity compare to models like LapSVM or AWSSL? Specifically, can the authors clarify its scalability for high-dimensional datasets and large sample sizes?
(3) The paper compares S2MAM with several established baselines, including LapSVM, AWSSL. However, the comparisons with recent deep learning-based semi-supervised learning methods are limited. Could the authors provide additional experimental comparisons with state-of-the-art deep learning-based SSL methods to better evaluate S2MAM's competitive performance?
(4) The datasets used in the experiments appear relatively small. Could the authors evaluate S2MAM on larger, more complex datasets to demonstrate its scalability and robustness in real-world scenarios?

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
5

### Summary
This paper proposes a novel semi-supervised meta additive model where a bilevel optimization scheme is employed to identify the informative features. The authors analyze the properties of the model including the convergence and statistical generalization   bound. Experimental results on toy and real-world data sets demonstrate promising improvements over previous methods.

### Strengths
1. The paper is well-organized.
2. This paper proposes a bilevel optimization scheme to select informative features.
3. The authors provided theoretical guarantees for the proposed model.

### Weaknesses
1. The authors employed a sampling strategy from Bernoulli distributions to select informative features. It is unclear whether this strategy can effectively prevent the selection of noisy features. While the probability parameter of the Bernoulli distribution is learned, the inherent randomness of the sampling process could still lead to the inclusion of irrelevant features. How does the method explicitly address the potential for selecting features that do not contribute to the model's performance, and what mechanisms are in place to remove such noisy features after they have been sampled?
2. Hyperparameter C, which controls the size of the selected feature subset, significantly impacts the selection of informative features. The paper lacks a detailed discussion on how to choose this hyperparameter. A sensitivity analysis demonstrating the effect of different C values on the model's performance and feature selection would be beneficial. Furthermore, specific guidance on selecting appropriate C values for different datasets should be provided.
3. The authors use mini-batches during training. Given that unlabeled samples typically dominate semi-supervised datasets, it is crucial to understand the proportion of labeled samples within each batch. The paper should specify how this proportion is determined and whether it is kept consistent across batches. The impact of varying this proportion on training stability and convergence should also be discussed.
4. The assumption that $\Phi(s)$ is L-smooth is critical for the convergence analysis. However, the paper does not provide a clear method for computing or estimating this smoothness constant L for the specific model. Without a concrete way to determine L, it is difficult to assess the practical implications of the theoretical convergence results. A detailed explanation of how to calculate or approximate L for the proposed model is needed.
5. The authors use dimension reduction techniques before applying their feature selection method to high-dimensional data. It is not clear whether the proposed method is effective for directly selecting features from high-dimensional data, such as gene expression data, without prior dimension reduction. The paper should discuss the limitations of the method when applied directly to such data and provide insights into its scalability and computational cost for high-dimensional feature spaces.

### Questions
Please refer to the weakness.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents a model named S2MAM, which aims to improve classical graph-based semi-supervised learning (GSSL) by combining bilevel optimization with manifold regularization to select relevant features and adapt similarity matrices in noisy and redundant data settings. S2MAM addresses issues in traditional manifold regularization, where fixed similarity metrics can perform poorly with uninformative features. The authors propose a probabilistic bilevel optimization framework to apply adaptive variable masking and provide theoretical proofs of convergence and generalization bounds. Empirical evaluations on synthetic and small real-world data suggest that S2MAM performs well in both regression and classification tasks, particularly under noisy conditions.

### Strengths
* The method partially solves the issue of poor similarity matrix in the graph-based SSL methods
* The authors provided convergence and generalization bounds, which enhances the model's credibility
* The proposed method outperforms the other GSSL methods of the same kind

### Weaknesses
The method still has many limitations of the graph-based GSSL methods. Therefore the impact of the method is very limited.
* It is expensive. The W or L matrix is infeasible when l is large. The method involves multiple kernel matrices, which is even more expensive.
* The assumption of a single bandwidth mu is unrealistic.
* The construction of W is problematic for many data types, e.g., images, text documents, and biology sequences.
* The experiments are not convincing because all tested datasets are very small.

### Questions
* The computational complexity is not ananlyzed.
* The prediction function requires all training samples. This is rather infeasible in practice. If changed to other prediction functions, does the theoretical guarantee still hold?

### Soundness
3

### Presentation
2

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
This paper proposes a new semi-supervised meta additive model (S2MAM) under a bilevel optimization scheme to automatically identify the informative variables, update the similarity matrix, and achieve the interpretable prediction simultaneously. Theoretical guarantees are provided for S2MAM including the computing convergence and the statistical generalization bound. Experimental assessments on synthetic and real-world datasets validate the robustness and interpretability of the proposed approach.

### Strengths
This paper inject the meta learning strategy and sparse additive models into manifold regularized SSL framework, and formulate a new semi-supervised meta additive model (S2MAM) to realize automatic variable masking and sparse approximation for high-dimensional inputs even with noisy variables.

There are no technical errors, and the presentation and writing are clear.

An efficient implementation is employed here to solve the bilevel optimization problem, which avoids the heavy computing burden on the implicit hypergradient calculation.

### Weaknesses
I am absolutely not in this field and the comments from me are not relatively professional. The comments in the following are just raised from the presentation or organization.                       

The authors propose the manifold regularized semi-supervised additive model. However, the authors do not analyze the important part "manifold regularized" in deepth for the presentation of the whole paper, making the paper inevitably lacks the novelty, i.e., the formulation of the manifold regularized sparse additive model is built by the combination of the existing works and the rationality behind this combination and the related theoretical analysis are not clearly given.

I wonder why the authors give many parts in presenting the semi-supervised additive model, i.e., Manifold Regularized Sparse Additive Model, Discrete Bilevel Framework for S2MAM, and Probabilistic Bilevel Framework for S2MAM. These parts seem to be all needed to be presented. However, the limited space in the paper seem to be the combination of these parts and the novelty of each part is dispersed to some degree. The definition of upper level and the lower level of discrete bilevel framework lack clear definition and the realted analysis in Eq. (3) and Eq. (4). The rationality of just using Bernoulli random variable to denote mi should be given, i.e., why it it simple and wheter the other types of random variables can be better in probalisitic bilevel framework.

The authors should add more recent methods for comparison in Table 3 and Table 5 to better show the effectiveness of the proposed method.

The authors just perform evaluations of S2MAM on eight real-world datasets from UCI repository. I think the authors can add other datasets for comparison in the experiment, which is not limited to UCI repository.

### Questions
1. Can the authors analysis the extreme cases when the fixed label percentages are high, i.e., r=50% and the noisy variables are high in the experiment, i.e., 100 noisy variables.

2. The authors can further analyze why the average accuracy on Breast Cancer achieve such high performance on Breast Cancer, i.e., the proposed method on unlabeled case is about 88 and the second best performance is just 77.197.

### Soundness
2

### Presentation
2

### Contribution
2
