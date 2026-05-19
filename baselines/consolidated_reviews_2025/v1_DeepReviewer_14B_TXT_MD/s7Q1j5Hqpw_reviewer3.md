### Summary

This paper proposes a Shift-Resilient Diffusive Imputation (SRDI) framework to address the Variable Subset Forecasting (VSF) problem, which involves forecasting with incomplete data due to sensor failures or limited data collection. The authors identify two types of distribution shifts in VSF: inter-series shift (changes in correlations between variables) and intra-series shift (distribution differences within the same series over time). SRDI integrates a divide-conquer strategy with a denoising process to decompose time series data into invariant and variant patterns, effectively mitigating inter-series shift. Additionally, SRDI employs a meta-learning paradigm to address intra-series shift by treating different time windows as tasks, enabling rapid adaptation to new distributions. Extensive experiments on four datasets demonstrate that SRDI outperforms state-of-the-art methods in VSF tasks.

### Soundness

2

### Presentation

3

### Contribution

3

### Strengths

1. The authors introduce a novel Shift-Resilient Diffusive Imputation (SRDI) framework specifically designed for Variable Subset Forecasting (VSF), which is a significant advancement in handling incomplete time series data due to sensor failures or limited data collection.
2. SRDI effectively addresses both inter-series and intra-series distribution shifts, which are common challenges in VSF tasks. The divide-conquer strategy and meta-learning paradigm are innovative solutions to these problems.
3. The paper is well-organized, with a clear problem formulation, detailed methodology, and extensive experimental results that support the claims made by the authors.

### Weaknesses

#### Some Related Works


#### comment

1. The authors should provide a more detailed explanation of the meta-learning strategy, including the specific algorithms used and the rationale behind their choices. The current description lacks sufficient detail to fully understand the implementation and effectiveness of this component. For instance, it is unclear how the meta-learning algorithm is adapted to the specific characteristics of the time series data, and how the task definition (different time windows) is operationalized within the meta-learning framework. Furthermore, the choice of meta-learning algorithm should be justified in the context of the VSF problem, considering alternatives and their potential limitations.
2. The paper could benefit from a more in-depth discussion of the limitations of the proposed SRDI framework and potential directions for future research. While the authors mention the challenges of VSF, they do not fully explore the scenarios where SRDI might struggle, such as highly non-stationary time series or cases with extremely sparse data. A discussion of the computational complexity of the proposed method, especially in comparison to simpler imputation techniques, would also be valuable. Additionally, the paper should consider the sensitivity of the method to hyperparameter settings and how these parameters should be tuned for different datasets.
3. The experimental section should include a wider range of datasets and real-world scenarios to further validate the effectiveness of SRDI. The current evaluation, while demonstrating the method's potential, is limited in its scope. The inclusion of datasets with varying characteristics, such as different sampling rates, noise levels, and types of distribution shifts, would provide a more comprehensive assessment of the method's robustness and generalizability. Furthermore, the paper should consider evaluating the method's performance in more complex real-world scenarios, such as those involving multiple interacting time series or those with abrupt changes in the underlying data distribution.

### Suggestions

To address the lack of detail regarding the meta-learning strategy, the authors should provide a more thorough explanation of the specific meta-learning algorithm used, including the choice of the algorithm and its adaptation to the VSF problem. This should include a detailed description of how the time series data is preprocessed and fed into the meta-learning framework, how the tasks are defined (e.g., using different time windows), and how the meta-learner is trained to adapt to new tasks. The authors should also discuss the rationale behind their choice of meta-learning algorithm, considering alternatives such as MAML or Reptile, and explain why their chosen approach is particularly well-suited for the VSF problem. Furthermore, the authors should provide a clear explanation of the loss function used for meta-learning and how it is optimized. This would greatly enhance the clarity and reproducibility of the proposed method.

To improve the discussion of limitations and future directions, the authors should explicitly address the scenarios where the SRDI framework might struggle. This should include a discussion of the method's performance under highly non-stationary time series, extreme data sparsity, and abrupt changes in the underlying data distribution. The authors should also analyze the computational complexity of the proposed method, comparing it to simpler imputation techniques, and discuss the sensitivity of the method to hyperparameter settings. Furthermore, the authors should explore potential avenues for future research, such as incorporating domain knowledge into the imputation process, developing more robust meta-learning strategies, or extending the method to handle more complex time series data. This would provide a more balanced and comprehensive view of the proposed method's capabilities and limitations.

To enhance the experimental evaluation, the authors should include a wider range of datasets with varying characteristics, such as different sampling rates, noise levels, and types of distribution shifts. This would provide a more comprehensive assessment of the method's robustness and generalizability. The authors should also consider evaluating the method's performance in more complex real-world scenarios, such as those involving multiple interacting time series or those with abrupt changes in the underlying data distribution. Additionally, the authors should provide a more detailed analysis of the experimental results, including a discussion of the statistical significance of the observed improvements and a comparison of the method's performance across different datasets and scenarios. This would strengthen the empirical validation of the proposed method and provide a more convincing argument for its effectiveness.

### Questions

1. Could the authors elaborate on the specific meta-learning algorithms used in SRDI and the rationale behind their choices?
2. What are the computational complexities of the proposed SRDI framework, and how do they compare to existing methods?
3. How does the performance of SRDI vary with different sizes of the variable subset, and what is the minimum number of variables required for effective forecasting?
4. Can the authors discuss the potential limitations of SRDI and suggest directions for future research in this area?

### Rating

6

### Confidence

3

**********
