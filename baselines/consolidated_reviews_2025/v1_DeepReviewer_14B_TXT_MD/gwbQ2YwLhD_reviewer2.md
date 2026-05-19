### Summary

The paper investigates the sensitivity of score-based structure learning algorithms to the scale of the variables in the data. The authors demonstrate that the well-known mean squared error (MSE) is heavily influenced by the scale of the variables, and that this can lead to incorrect graph structures being recovered. They provide theoretical proofs that show that minimizing the MSE can result in the selection of a graph that is not the true underlying graph, and that this can occur even when the data is generated from a linear Gaussian model. The authors also propose a new score, the Scale Robust Loss (SRL), that is less sensitive to the scale of the variables. They show that the SRL can be used to recover the true graph structure in a variety of settings, and that it is more robust to the scale of the variables than the MSE. The paper's main contributions are:

1. Theoretical analysis of the scale sensitivity of score-based structure learning algorithms
2. Proof that minimizing the MSE can result in the selection of an incorrect graph structure
3. Proposal of a new score, the SRL, that is less sensitive to the scale of the variables
4. Empirical validation of the SRL on both synthetic and real-world data

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper provides a rigorous theoretical analysis of the scale sensitivity of score-based structure learning algorithms, and shows that minimizing the MSE can result in the selection of an incorrect graph structure. This is a significant contribution to the field, as it highlights a potential pitfall of using score-based methods for structure learning.

2. The authors propose a new score, the SRL, that is less sensitive to the scale of the variables. They show that the SRL can be used to recover the true graph structure in a variety of settings, and that it is more robust to the scale of the variables than the MSE. This is a valuable contribution, as it provides a practical solution to the problem of scale sensitivity.

3. The paper is well-written and easy to follow. The authors provide clear explanations of their theoretical results and empirical findings, and use illustrative examples to help the reader understand the key concepts.

### Weaknesses

#### Some Related Works


#### comment

1. The paper focuses primarily on the theoretical analysis of the scale sensitivity of score-based structure learning algorithms, and does not provide a comprehensive empirical evaluation of the SRL. While the authors do provide some empirical results on synthetic and real-world data, these are limited in scope and do not fully demonstrate the effectiveness of the SRL in a variety of settings. Specifically, the synthetic data experiments do not explore a wide range of graph structures, edge densities, or noise levels. The real-world data experiments are also limited, and it is unclear how the SRL would perform on other types of data.

2. The paper's analysis is limited to linear Gaussian models, and it is unclear how the results would generalize to other types of models. While the authors mention that their results may extend to other models, they do not provide any theoretical or empirical evidence to support this claim. The assumption of linearity is particularly restrictive, as many real-world systems exhibit non-linear relationships between variables. The paper does not address how the SRL would perform in the presence of non-linear dependencies, or how the scale sensitivity of score-based methods might change under non-linear conditions.

3. The paper does not provide a detailed discussion of the computational complexity of the SRL, or how it compares to other structure learning algorithms. This is an important consideration for practical applications, as the computational cost of an algorithm can be a major factor in its usability. It is unclear whether the SRL introduces any additional computational overhead compared to the MSE, and how this overhead scales with the size of the graph and the number of samples.

### Suggestions

The paper would benefit from a more extensive empirical evaluation of the Scale Robust Loss (SRL). The current experiments, while demonstrating the core concept, are limited in scope. Specifically, the synthetic data experiments should explore a wider range of graph structures, including sparse and dense graphs, as well as different edge density distributions. It would also be beneficial to vary the noise levels and the sample sizes to assess the robustness of the SRL under different conditions. Furthermore, the real-world data experiments should be expanded to include a more diverse set of datasets, representing different domains and characteristics. This would provide a more comprehensive understanding of the practical applicability of the SRL and its performance compared to existing methods. The authors should also consider comparing the SRL to other scale-invariant scoring functions, if they exist, to better contextualize its performance.

To address the limitation of focusing solely on linear Gaussian models, the authors should investigate the behavior of the SRL under non-linear relationships. This could involve generating synthetic data with non-linear dependencies and evaluating the performance of the SRL in these settings. It would also be valuable to explore how the scale sensitivity of score-based methods changes under non-linear conditions, and whether the SRL remains effective in mitigating this sensitivity. The authors could consider using techniques such as kernel methods or neural networks to model non-linear relationships and assess the performance of the SRL in these more complex scenarios. Additionally, a theoretical analysis of the SRL's behavior under non-linear conditions would be a valuable contribution, even if it is limited to specific classes of non-linear functions. This would provide a more complete understanding of the limitations and applicability of the SRL.

Finally, the paper should include a detailed discussion of the computational complexity of the SRL. This should include an analysis of the time and space complexity of the algorithm, as well as a comparison to the computational cost of other structure learning algorithms, such as those based on the MSE. The authors should also provide empirical results on the runtime of the SRL on different datasets and graph sizes. This would help to assess the practical feasibility of the SRL and its suitability for different applications. It would also be useful to discuss any potential optimizations that could be used to improve the computational efficiency of the SRL, such as parallelization or approximation techniques.

### Questions

1. How does the SRL compare to other scale-invariant scoring functions, if they exist?

2. How does the SRL perform on other types of data, such as time series data or data with non-Gaussian noise?

3. What is the computational complexity of the SRL, and how does it compare to other structure learning algorithms?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
