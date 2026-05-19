### Summary

This paper studies the heterogeneous treatment effect estimation problem with delayed response. The authors first formalize the problem and prove the identifiability of the potential outcome and response time under certain assumptions. Then, they propose a modified EM algorithm based on the counterfactual regression model to solve this problem. The proposed method is evaluated on both synthetic and real-world datasets.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1.	The paper is well-written and easy to follow.
2.	The proposed method is theoretically sound, and extensive experiments are conducted to evaluate its performance.

### Weaknesses

#### Some Related Works


#### comment

1.  The novelty of this paper is somewhat limited. The counterfactual regression model has been widely studied, and the proposed method is a straightforward application of this model to the delayed feedback problem. The core idea of using an EM algorithm to handle latent variables in causal inference is not new, and the specific adaptation to delayed responses, while practical, does not introduce a fundamentally novel approach. The paper lacks a deep theoretical contribution beyond the application of existing techniques.
2.  The delayed feedback problem is a specific case of the more general problem of treatment effects under interference. The authors should discuss the relationship between these two problems and explain why they focus on the delayed feedback scenario. The current discussion does not adequately address how the proposed method would handle situations where interference effects are present, which is a common scenario in many real-world applications. The paper should clarify the scope of its applicability and limitations in the context of more complex causal structures.
3.  The authors should provide more details on the datasets used in the experiments, such as the number of samples, the number of features, and the specific experimental settings. For example, in the real-world datasets, how are the treatment assignments, potential outcomes, and response times generated? The lack of detail makes it difficult to assess the validity and generalizability of the experimental results. Specifically, the data generation process for the potential outcomes and response times needs to be clearly explained, including any assumptions made about their distributions and dependencies.
4.  The authors should also discuss the sensitivity of their method to the choice of hyperparameters and the potential impact of unobserved confounders. The paper does not provide sufficient analysis of how the performance of the proposed method varies with different hyperparameter settings. Furthermore, the discussion on the impact of unobserved confounders is limited, and the paper should explore how violations of the unconfoundedness assumption would affect the identifiability and estimation of treatment effects.

### Suggestions

The paper would benefit from a more thorough discussion of the novelty of the proposed method. While the application of the counterfactual regression model to the delayed feedback problem is a practical contribution, the paper should clearly articulate what specific challenges are addressed by this adaptation and how it goes beyond a straightforward application of existing techniques. A more detailed comparison with alternative approaches for handling delayed feedback, such as survival analysis or time-to-event models, would also be beneficial. The authors should highlight the unique aspects of their method and its advantages over existing solutions, particularly in terms of theoretical guarantees and empirical performance. Furthermore, the paper should explore the limitations of the proposed method and discuss potential avenues for future research.

To address the issue of interference, the authors should provide a more detailed discussion of the relationship between delayed feedback and treatment effects under interference. The paper should clarify whether the proposed method can be extended to handle interference effects and, if so, under what assumptions. If the method is not directly applicable to interference scenarios, the authors should clearly state the limitations and discuss potential modifications or alternative approaches that could address this more general problem. The discussion should include a clear definition of the interference structure and how it affects the identifiability and estimation of treatment effects. The authors should also consider providing examples of real-world scenarios where interference is likely to be a significant factor and discuss how their method would perform in such cases.

Finally, the paper should provide more detailed information about the experimental setup, including the specific characteristics of the datasets used, the data generation process for potential outcomes and response times, and the hyperparameter settings for the proposed method. The authors should also conduct a sensitivity analysis to evaluate the impact of different hyperparameter choices on the performance of the method. Furthermore, the paper should discuss the potential impact of unobserved confounders on the estimation of treatment effects and explore methods for mitigating this issue. This could include techniques such as instrumental variables or sensitivity analysis. The authors should also consider including experiments with real-world datasets where the treatment assignments, potential outcomes, and response times are not generated but observed, to better demonstrate the practical applicability of their method.

### Questions

Please refer to the weaknesses.

### Rating

5

### Confidence

4

**********
