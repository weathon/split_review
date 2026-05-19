### Summary

This paper proposes a new method for merging multiple task-specific models into a single multi-task model without access to the original training data. The key idea is to learn adaptive merging coefficients for each task vector (or layer within each task vector) using entropy minimization on unlabeled test samples as a surrogate objective. The authors demonstrate the effectiveness of their approach on eight image classification tasks, showing significant performance gains over existing model merging techniques. They also show improved generalization to unseen tasks and robustness to test data distribution shifts.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper is well-written and easy to follow. The motivation for adaptive model merging is clearly explained, and the proposed method is presented in a logical manner.

- The experimental evaluation is comprehensive, covering multiple tasks, model architectures, and evaluation scenarios (generalization and robustness). The results are compelling, demonstrating consistent improvements over existing methods.

- The idea of using entropy minimization on unlabeled test samples as a surrogate objective for learning merging coefficients is novel and well-motivated. The authors provide a clear explanation of their approach and justify its effectiveness through empirical analysis.

- The proposed method is simple yet effective, requiring only a small amount of unlabeled test data and minimal additional training time. This makes it practical for real-world applications where access to original training data is limited.

### Weaknesses

#### Some Related Works


#### comment

 - The paper lacks a detailed analysis of the computational cost associated with the proposed method. While the authors mention that the optimization process is efficient, they do not provide a quantitative comparison of the training time and memory requirements of AdaMerging with existing task vector-based merging methods. Specifically, it is unclear how the iterative entropy minimization affects the overall training time, especially when considering the need for multiple iterations to converge. A detailed breakdown of the computational complexity, including the number of forward and backward passes required per iteration, would be beneficial.

- The paper does not explore the sensitivity of AdaMerging to the choice of hyperparameters, such as the learning rate and the number of iterations for coefficient optimization. It is important to understand how these parameters affect the performance of the method and whether the reported results are robust across different settings. For example, how does the performance vary with different learning rates for the coefficient optimization, and what is the impact of using a fixed number of iterations versus a convergence-based stopping criterion?

- The paper does not provide a theoretical analysis of why entropy minimization works well as a surrogate objective for learning merging coefficients. While the empirical results are promising, a theoretical justification would strengthen the paper's contribution. It would be helpful to understand the relationship between entropy minimization and the underlying optimization problem of finding optimal merging coefficients. For instance, is there a connection between minimizing entropy and maximizing the mutual information between the merged model's output and the target labels?

### Suggestions

To address the lack of computational cost analysis, the authors should include a detailed comparison of the training time and memory requirements of AdaMerging with existing methods. This should include a breakdown of the computational complexity of each step in the optimization process, such as the number of forward and backward passes required per iteration. Furthermore, the authors should provide a quantitative analysis of the wall-clock time required for training, as well as the memory footprint of the method. This analysis should be performed on a standard hardware setup and should include a comparison with other task vector-based merging methods. This would allow readers to better understand the practical implications of using AdaMerging in resource-constrained environments.

To address the sensitivity to hyperparameters, the authors should conduct a thorough ablation study on the impact of different hyperparameter settings on the performance of AdaMerging. This should include a systematic exploration of the learning rate and the number of iterations for coefficient optimization. The authors should also investigate the impact of using different optimization algorithms for the coefficient updates. Furthermore, the authors should provide a clear explanation of how these hyperparameters should be chosen in practice. This would help readers to understand the robustness of the method and to apply it effectively in different settings. The authors should also consider using a convergence-based stopping criterion for the coefficient optimization, rather than a fixed number of iterations, to ensure that the method converges to a stable solution.

To provide a theoretical analysis of why entropy minimization works well as a surrogate objective, the authors should explore the connection between entropy minimization and the underlying optimization problem of finding optimal merging coefficients. This could involve analyzing the properties of the loss landscape and the relationship between entropy and the model's generalization performance. The authors could also investigate whether entropy minimization is related to maximizing the mutual information between the merged model's output and the target labels. A theoretical analysis would provide a deeper understanding of the method and would strengthen the paper's contribution. This analysis could also provide insights into the limitations of the method and suggest potential avenues for future research.

### Questions

- How does the performance of AdaMerging vary with different choices of hyperparameters, such as the learning rate and the number of iterations for coefficient optimization?

- What is the computational cost of AdaMerging compared to existing task vector-based merging methods? Can the authors provide a detailed analysis of the training time and memory requirements?

- Is there a theoretical justification for using entropy minimization as a surrogate objective for learning merging coefficients? How does it relate to the underlying optimization problem?

### Rating

8

### Confidence

3

**********
