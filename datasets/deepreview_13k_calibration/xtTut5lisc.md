# Iterative Feature Space Optimization through Incremental Adaptive Evaluation

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5

## Abstract
Iterative feature space optimization involves systematically evaluating and adjusting the feature space to improve downstream task performance. However, existing works suffer from three key limitations: 1) overlooking differences among data samples leads to evaluation bias; 2) tailoring feature spaces to specific machine learning models results in overfitting and poor generalization; 3) requiring
the evaluator to be retrained from scratch during each optimization iteration significantly reduces the overall efficiency of the optimization process. To bridge these gaps, we propose a gEneralized Adaptive feature Space Evaluator (EASE) to efficiently produce optimal and generalized feature spaces. This framework consists of two key components: Feature-Sample Subspace Generator and Contextual Attention Evaluator. The first component aims to decouple the information distribution within the feature space to mitigate evaluation bias. To achieve this, we first identify features most relevant to prediction tasks and samples most challenging for evaluation based on feedback from the subsequent evaluator. These identified feature and samples are then used to construct feature subspaces for next optimization iteration. This decoupling strategy makes the evaluator consistently target the most challenging aspects of the feature space. The second component intends to incrementally capture evolving patterns of the feature space for efficient evaluation. We propose a weighted-sharing multi-head attention mechanism to encode key characteristics of the feature space into an embedding vector for evaluation. Moreover, the evaluator is updated incrementally, retaining prior evaluation knowledge while incorporating new insights, as consecutive feature spaces during the optimization process share partial information. Extensive experiments on twelve real-world datasets demonstrate the effectiveness of the proposed framework. Our code and data are publicly available (https://anonymous.4open.science/r/EASE-1C51).

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a general adaptive feature space evaluator named EASE, designed to optimize feature spaces through incremental updates and a contextual attention mechanism. By generating feature-sample subspaces and conducting incremental evaluations, this framework improves the efficiency and accuracy of feature selection, with its performance validated across multiple real-world datasets.

### Strengths
1. The EASE framework includes two key components: a feature-sample subspace generator and a contextual attention evaluator. The feature-sample subspace generator creates feature subspaces relevant to downstream tasks, allowing the evaluator to focus on the most challenging subspaces in each iteration.
2. An incremental update strategy is introduced in this paper, which retains historical parameter weights and updates only critical parameters when new feature spaces appear, reducing the computational cost of retraining from scratch each time. Additionally, an Elastic Weight Consolidation (EWC) strategy is used to calculate Fisher information.

### Weaknesses
1 The paper presents the innovative EASE framework. However, it provides limited implementation details, such as hyperparameter configurations, optimization strategies, and specific training processes. This lack of detail makes it difficult to assess the practical viability and replicability of the proposed method. For example, the specific learning rates, batch sizes, and regularization parameters used in training are not clearly defined, which are crucial for achieving the reported performance.
2 The paper compares EASE with some common models (such as GBDT and Random Forest) but lacks detailed comparisons with current state-of-the-art feature selection or feature space evaluation methods. This makes it hard to determine whether the proposed method offers a significant improvement over existing techniques. The absence of comparisons with methods specifically designed for feature space evaluation, such as those based on information theory or spectral analysis, is a notable gap.
3 The theoretical analysis of EASE relies on specific assumptions about data distribution and feature relevance, which may not always align with real-world data, especially in datasets where features are weakly related or uncorrelated. The paper does not adequately address how the method would perform under violations of these assumptions, such as in the presence of highly non-linear feature interactions or significant noise.

### Questions
1. The complexity of feature subspace generation and multi-head attention mechanisms still makes the EASE framework computationally intensive during training. Due to the large number of parameters in multi-head attention, which require constant updating, the efficiency of EASE may be suboptimal in large-scale datasets or high-dimensional feature spaces.
2. The regularization parameters mentioned in this paper significantly impact the stability and adaptability of parameters in incremental updates, but detailed tuning strategies for different scenarios are lacking. Additionally, the size and sampling strategy of the feature-sample subspaces generated in different iteration steps could directly affect the accuracy and computational cost of final feature space evaluation.
3. While the EASE framework performs well experimentally, it lacks theoretical analysis to explain its generalizability across different feature spaces and tasks. For instance, the paper does not provide detailed theoretical support for whether incremental updates are effective across all feature space distributions, or whether the contextual attention mechanism is universally applicable.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper designs a new framework (i.e., EASE) to enhance the optimization of feature spaces in machine learning tasks. EASE addresses common limitations in existing methods, such as evaluation bias, poor generalization, and inefficient training. It comprises two main components: the Feature-Sample Subspace Generator and the Contextual Attention Evaluator. The former mitigates evaluation bias by decoupling information within the feature space, while the latter captures evolving patterns incrementally for efficient evaluation. The framework is tested on twelve real-world datasets, demonstrating its effectiveness and efficiency over traditional methods.

### Strengths
1. The paper effectively tackles prevalent issues in feature space optimization, such as bias, generalization, and training inefficiency, providing a more robust evaluation methodology.

2. The combination of Feature-Sample Subspace Generator and Contextual Attention Evaluator offers a comprehensive solution that both decouples complex interactions and captures evolving patterns in feature spaces.

3. The extensive experiments on multiple real-world datasets substantiate the superiority of EASE in terms of both accuracy and efficiency, enhancing the paper's credibility.

### Weaknesses
1. The proposed method conduct the efficiency comparison experiments of different feature space evaluators across various datasets. It would be better to further analyze the time complexity of different feature space evaluators to demonstrate the efficiency of the proposed method. Specifically, a more rigorous analysis of the computational cost, including both theoretical time complexity (e.g., Big O notation) and empirical running time, should be provided for each component of the EASE framework and compared against the baselines. This analysis should consider the impact of different factors, such as the number of features, the number of samples, and the dimensionality of the feature space.

2. The proposed method is applied to two iterative feature selection frameworks to validate its effectiveness and generalization capability, i.e., RFE and FLSR. However, both the two baselines are out-of-date. Are there any recent baselines can be applied to? It would be beneficial to compare the performance of EASE against more recent and state-of-the-art feature selection methods, particularly those that have demonstrated strong performance on similar datasets. This would provide a more robust evaluation of the proposed method's effectiveness and competitiveness.

3. The used several datasets are relatively small, i.e., almost all of their sample sizes are small than 10 thousand. How about applied the proposed method on large-scale datasets? The paper should include experiments on larger datasets to demonstrate the scalability of EASE. It is important to evaluate how the performance of EASE changes as the dataset size increases, and whether it can maintain its efficiency and effectiveness on large-scale datasets.

4. I am a little concerned about the innovativeness of the proposed method, because Section 4.2 contextual attention evaluator seems to simply apply the self-attention mechanism. The paper should provide a more detailed explanation of how the self-attention mechanism is adapted and optimized for the specific task of feature space evaluation. It should also discuss the potential limitations of using self-attention in this context and how these limitations are addressed by the proposed method.

### Questions
See above.

### Soundness
3

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
This paper proposes a method to iteratively find good feature space (specifically, a set of relevant features in the original features) to improve downstream task performance. For this, the authors propose a Feature-sample subspace generator that finds relevant features and difficult samples in each optimization step and a Contextual attention evaluator that evaluates the selected features so that it can improve the prediction performance. The experiments show that the proposed method outperformed existing iterative feature space optimization methods.

### Strengths
- The feature selection is an important task in machine learning.
- The effectiveness of the proposed method was evaluated with many datasets including classification and regression tasks and many evaluation metrics.

### Weaknesses
 - The significance of the task of iterative feature space optimization is not clear. For example, even if you don't find a feature space (specifically, feature selection) iteratively, lasso or neural network-based embedding-based feature selection methods can select features that directly improve the performance of downstream tasks by optimizing a single objective function once. This paper may be trying to solve unnecessarily complex problems.
- The presentation quality and clarity of this paper are low. For example, in Eq. 1, the evaluator $M$ takes the feature space as input and calculates the loss with the label space. What is the loss between spaces? Isn't it correct to say data (feature) matrix and label vector, etc., rather than spaces? The word 'space' is associated with mathematical vector spaces, etc., which can be confusing. I also need help understanding Eq. 3. Is the score a scalar or a vector? Because the specific form of $F^t$ (whether it's a vector, a matrix, or something else) is not described, the output of $M$ is also unclear. Thus, the definition of Eq. 3 is ambiguous.
Also, Eq. 2 in section 3 is different from Eq. 10, which is actually used. What is the intention of introducing a specific formula Eq. 2 at the problem-setting stage? I think that this makes the paper unnecessarily difficult to understand.I think the overall explanation of the proposed method needs to be improved.

### Questions
- Since this paper is considering feature selection, wouldn't it be easier for readers to understand if the authors propose the method as a feature selection method rather than using the abstract term 'feature space optimization'? 
- In Figure 3, why is the proposed method faster than other comparison methods? Since the proposed method is based on neural networks (attention), I think it is more expensive.

### Soundness
2

### Presentation
1

### Contribution
2
