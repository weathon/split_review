# Improving Tabular Generative Models: Loss Functions, Benchmarks, and Iterative Objective Bayesian Approaches

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 5, 5, 6

## Abstract
Access to extensive data is essential for improving model performance and generalization in deep learning (DL). When dealing with sparse datasets, a promising solution is to generate synthetic data using deep generative models (DGMs). However, these models often struggle to capture the complexities of real-world tabular data, including diverse variable types, imbalances, and intricate dependencies.
Additionally, standard Bayesian optimization (SBO), commonly used for hyper-parameter tuning, struggles with aggregating metrics of different units, leading to unreliable averaging and suboptimal decisions.

To address these gaps, we introduce a novel correlation- and distribution-aware loss function that regularizes DGMs, enhancing their ability to generate synthetic tabular data that faithfully represents actual distributions. To aid in evaluating this loss function, we also propose a new multi-objective aggregation method using iterative objective refinement Bayesian optimization (IORBO) and a comprehensive statistical testing framework. While the focus of this paper is on improving the loss function, each contribution stands on its own and can be applied to other DGMs, applications, and hyperparameter optimization techniques.

We validate our approach using a benchmarking framework with twenty real-world datasets and ten established tabular DGM baselines. Results demonstrate that the proposed loss function significantly improves the fidelity of the synthetic data generated with DGMs, leading to better performance in downstream machine learning (ML) tasks. Furthermore, the IORBO consistently outperformed SBO, yielding superior optimization results. This work advances synthetic data generation and optimization techniques, enabling more robust applications in DL.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces two regularization terms for improving the performance of the tabular generative model. The authors further propose to use ranking-based Bayesian Optimization to choose the hyperparameter. They finally evaluate the proposed method in Twenty tabular datasets on 10 base generative models by using TSTR, augmentation.

### Strengths
The experiments are comprehensive. Hyperparameters are chosen reasonably.

### Weaknesses
The proposed method is heuristic. The paper does not provide an optimality or convergence guarantee of the proposed loss. These two proposed losses are reasonable for tabular data but not general enough for other types of data. The hyperparameters are chosen by the new proposed Bayesian Optimization without theoretical guarantees.

### Questions
What will the performance if using Standard Bayesian optimization rather than IORBO proposed by this paper?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
- Introduced a correlation- and distribution-aware loss function designed as a regularizer for DGMs in tabular data synthesis that displays promising results
- Introduced a hyperparameter tuning approach, IORBO, that leverages rank-based aggregation. (concerns of units
- They introduce a benchmarking system evaluating statistical similarity, ML TSTR performance, and ML augmentation performance, with robust statistical tests.

### Strengths
**Originality and Quality**

The correlation- and distribution-aware loss function is new and interesting to me. I have not encountered works that display the effectiveness of enforcing correlation and high-order moments in the loss function to improve generative models. It is nice to see an improvement in existing hyperparameter tuning algorithms such as Standard Bayesian Optimization by adding an iterative refinement process.

**Clarity**

Individual sections of the paper are well written.

**Significance**

Tabular data generation is gaining traction in real-world applications such as electronic health records. This work helps bring progress to tabular data generation.

### Weaknesses
 - I am struggling to find a central theme/research question the paper is trying to answer. It provides solutions from three different perspectives: 1) Loss Function Regularization: Improving generative model outputs by enforcing statistical properties (e.g., correlation, distribution); 2) Hyperparameter Tuning: Using methods like IORBO for iterative optimization; 3) Statistical Tests: Providing a framework for assessing model performance across metrics. I am unable to determine a flow to link the three ideas together/how one idea enforces the other.
- L486: How does IORBA perform against other hyperparameter tuning methods such as [Randomised Optimization, GridSearch etc.](https://scikit-learn.org/1.5/modules/grid_search.html#tuning-the-hyper-parameters-of-an-estimator) in terms of performance? What about the computational cost for IORBA vs. SBO and other mentioned baselines, what is this tradeoff? Additionally, what are the optimized hyperparameters that you obtain from your method? Ablation studies of the aforementioned would make your case stronger.
- In [TabSyn](https://arxiv.org/abs/2310.09656), the authors provided a comprehensive evaluation of synthetic tabular data using over five distinct evaluation metrics. Their metrics are straightforward and easy to comprehend. It will be nice to compare and justify why your metrics are more convincing and better than their proposed benchmark so that users should use your metrics instead of/in addition to TabSyn’s.
- Privacy is also crucial in synthetic tabular generation. How does your proposed loss function affect privacy-preserving metrics such as DCR and C2ST?

### Questions
The individual contributions of the paper are good. However, my main concern is the overall theme of the paper. I am unable to determine the overall research question the paper is trying to address. Please see weaknesses.

### Soundness
2

### Presentation
3

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
**Review of "Improving Tabular Generative Models: Loss Functions, Benchmarks, and Iterative Objective Bayesian Approaches"**

This paper proposes several methods to enhance deep generative models (DGMs) for synthetic data generation with a particular focus on tabular data. While the work presents promising results in experiment, certain aspects need further clarification and further improvement.

### Strengths
The paper presents an approach to enhancing Deep Generative Models (DGMs) for synthetic data generation on tabular data. Introduction of a correlation- and distribution-aware loss function, iterative objective refinement Bayesian optimization, and a detailed benchmarking framework are presented.

### Weaknesses
1. **"Moment Generating Function (MGF)":**
The term "Moment Generating Function (MGF)" appears to be misused. The paper discusses empirical moments themselves rather than the empirical MGF $\hat{M_X}(t)$ from which the $n$-th moments can be obtained by taking $n$-th derivatives wrt $t$ at $t=0$. [See *Casella, Statistical Inference, 1990* (pp61)]

2. **Biased Estimator in Synthetic Data:**
A biased estimator is used to calculate the standard deviation. This includes the estimator on synthetic data sampled at size $B$, which is not enough for the biased estimator to converge to the unbiased one. It would be beneficial for the paper to address or justify this choice. Specifically, the use of a biased sample standard deviation estimator, $s = \sqrt{\frac{1}{N}\sum_{i=1}^{N}(x_i - \bar{x})^2}$, on small synthetic data batches introduces a systematic underestimation of the true standard deviation. This bias is particularly problematic when the batch size $B$ is small, as the estimator's convergence to the unbiased estimator, $s = \sqrt{\frac{1}{N-1}\sum_{i=1}^{N}(x_i - \bar{x})^2}$, is slow. The paper needs to justify this choice, especially given the potential impact on the distribution matching loss.

3. **Hyperparameter $\lambda$:**
Hyperparameter $\lambda$ in Eq.6 scales the $L_{\text{distribution}}$ in a manner the same as $\beta$ in custom losses, since $\lambda$ is 
 proportional to  $L_{\text{distribution}}$ in Eq.6.  Simultaneous inclusion of $\lambda$ and $\beta$ in the hyperparameter search may lead to issues such as multi-collinearity for Bayesian optimization.

### Questions
1. **Significance Levels and Decision-Making:**
   In Table 1, the column for significance levels presents $p$-value ranges. A more detailed description of the decision based on the test statistic (or $p$-value obtained) may be helpful in understanding the experiment since a two-sided test is concerned.

2. **Distribution matching loss:**
It is possible for non-converging distributions to have similar moments, especially in lower orders. And, moment estimators of higher order moments introduce instability in the finite sample sense, and this instability goes up when the moment order goes up. It would be helpful if the author could justify using moments for distribution rather than the usual distance/score-based metrics for distribution similarity.



**Some Suggestions:**
 ***Reordering Loss Components:***
  For clearer presentation, consider swapping the order of the two proposed loss components to explain what $\mu$ and $\sigma$ are before presenting them in Eq.2.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work introduces correlation and moment-matching loss functions to regularize the loss function of different deep generative models for tabular data. Its results show that with proper selection of hyperparameters, its approach consistently improves the baselines. A Bayesian optimization procedure is introduced for hyperparameter tuning.

### Strengths
The added regularizers are described clearly and intuitively, with a well-defined methodology and comprehensive benchmark design. This approach encompasses various generative models and employs Bayesian optimization to identify optimal hyperparameter configurations. Consistent improvements over baseline models are demonstrated.

### Weaknesses
What I miss from the paper is a discussion on how to tune the method in the case of data heterogeneity and its performance and robustness in missing data scenarios.  How do the regularizers formulate in the case of counting distributions (e.g., Poisson likelihood) or ordinal variables? Do they consistently improve the results in the case of large fractions of missing entries in the database? I set my score to 6 since I feel that without a proper discussion on these aspects, the impact of the paper is limited.

### Questions
See above

### Soundness
4

### Presentation
3

### Contribution
3
