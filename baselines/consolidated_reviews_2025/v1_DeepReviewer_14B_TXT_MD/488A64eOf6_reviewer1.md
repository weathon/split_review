### Summary

This paper proposes a new decoding method called DAEEMON (Decoding As Direct Metrics OptimizatiOn). The method aims to generate text that aligns with human texts on multiple aspects simultaneously. The authors formulate decoding as an optimization problem that minimizes the reverse KL divergence between the model distribution and the human text distribution, subject to constraints on expected metric scores. They prove that this approach improves perplexity on human texts and derive an analytical solution for the decoding distribution. Experiments on Wikipedia and News domains demonstrate DAEEMON's superiority over baselines in metrics alignment and human evaluation.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

* The paper frames decoding as a constrained optimization problem with a proof of improved perplexity on human texts, providing theoretical grounding for the approach.
* The proposed method, DAEEMON, optimizes multiple metrics simultaneously, addressing the limitations of existing decoding methods that focus on individual aspects.

### Weaknesses

#### Some Related Works


#### comment

 * The paper does not discuss the computational cost of the proposed method in detail. It would be helpful to understand the practical implications of the method's complexity. Specifically, the paper lacks a detailed analysis of the time and memory requirements for the optimization process, especially concerning the number of samples needed for accurate estimation of the expectation terms and the impact of the dimensionality of the metric space on the computational burden. Furthermore, the paper does not discuss how the computational cost scales with the length of the generated text, which is a critical factor for practical applications.
* The paper's choice of metrics and constraints is not thoroughly justified. It is unclear how the specific metrics were chosen and whether they are sufficient to capture the desired properties of human-like text. The paper does not provide a clear rationale for why the chosen metrics (repetition, coherence, diversity, and information content) are the most appropriate for evaluating human-like text generation. It also lacks a discussion of the potential limitations of these metrics and whether they might introduce biases or unintended consequences. For example, optimizing for diversity might lead to less coherent text, and the paper does not fully address how these trade-offs are managed.

### Suggestions

The paper should include a more detailed analysis of the computational cost of the DAEEMON method. This analysis should include a breakdown of the time and memory requirements for each step of the algorithm, such as sampling, metric calculation, and optimization. The authors should also discuss how the computational cost scales with the number of samples, the dimensionality of the metric space, and the length of the generated text. It would be beneficial to provide empirical results on the computational cost of the method for different parameter settings and to compare it with the computational cost of baseline methods. Furthermore, the authors should discuss potential strategies for reducing the computational cost of the method, such as using more efficient optimization algorithms or approximating the expectation terms.

The paper should provide a more thorough justification for the choice of metrics and constraints. The authors should discuss the rationale behind selecting repetition, coherence, diversity, and information content as the primary metrics for evaluating human-like text generation. They should also discuss the limitations of these metrics and how they might interact with each other. For example, the paper should address the potential trade-off between diversity and coherence and explain how the DAEEMON method manages this trade-off. It would be helpful to include a discussion of alternative metrics that could be used to evaluate human-like text generation and why they were not chosen. The authors should also discuss the potential for unintended consequences when optimizing for specific metrics and how they can be mitigated.

Finally, the paper should provide more details on the practical implementation of the method. This includes a discussion of the specific algorithms used for sampling and optimization, as well as the hyperparameter settings used in the experiments. The authors should also discuss the sensitivity of the method to different hyperparameter settings and provide guidelines for choosing appropriate values. It would be beneficial to include a discussion of the potential challenges in implementing the method and how they can be addressed. The paper should also include a more detailed analysis of the convergence properties of the optimization algorithm and provide empirical results on the convergence behavior of the method.

### Questions

* How sensitive is the method to the choice of metrics and their corresponding weights? Are there any guidelines for selecting appropriate metrics and weights for different tasks?
* What is the computational cost of the proposed method compared to baseline methods? How does the cost scale with the number of metrics being optimized?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
