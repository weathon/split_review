### Summary

This paper proposes a method for estimating the individualized dose-response function (IDRF) with continuous treatments. The proposed method, DBRNet, learns disentangled representations of covariates and uses a re-weighting function to eliminate selection bias. The authors provide theoretical proofs for the debiasing properties of their method and conduct extensive experiments on synthetic and semi-synthetic datasets to demonstrate its effectiveness.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper is well-written and easy to follow.
- The proposed method is theoretically grounded and provides debiasing proofs for the re-weighting function.
- The paper includes extensive experiments on multiple datasets, demonstrating the effectiveness of DBRNet compared to existing methods.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not adequately address the identifiability assumptions required for estimating the IDRF with continuous treatments. Specifically, the assumption that the learned adjustment factors do not embed information about the treatment is not sufficiently justified. The paper lacks a discussion on how this assumption is met in practice, and what are the potential consequences if this assumption is violated. The authors should provide a more rigorous analysis of the conditions under which this assumption holds, and discuss the implications of its violation.
- The proposed method relies on several hyperparameters (α, β, γ, λ) that control the weights of different loss terms. The paper lacks a clear strategy for selecting these hyperparameters, and the sensitivity of the results to these choices is not adequately explored. The authors should provide a more detailed analysis of how these hyperparameters affect the performance of the model, and provide guidance on how to choose appropriate values for different datasets.
- The experimental evaluation is limited to relatively simple datasets. The authors should consider evaluating their method on more complex and realistic datasets, such as those used in the literature on causal inference with continuous treatments. The current evaluation does not provide sufficient evidence that the proposed method is effective in real-world settings.
- The paper does not compare the proposed method to some relevant baselines, such as those based on mutual information [1] or debiased learning [2,3,4,5]. The authors should include a more comprehensive comparison to these methods to demonstrate the advantages of their approach.

### Suggestions

The paper would benefit from a more thorough discussion of the identifiability assumptions underlying the proposed method. Specifically, the assumption that the learned adjustment factors do not embed information about the treatment needs further justification. The authors should provide a more detailed analysis of the conditions under which this assumption holds, possibly by relating it to the underlying data generating process or by providing theoretical guarantees. Furthermore, the paper should discuss the potential consequences of violating this assumption, and how it might impact the accuracy of the estimated IDRF. This discussion should include a sensitivity analysis of the method's performance under different violations of this assumption, which would provide a more complete picture of the method's robustness. It would also be beneficial to explore alternative approaches that do not rely on this assumption, or to provide a more robust method that is less sensitive to its violation.

Regarding the hyperparameters, the paper should include a more detailed analysis of their impact on the model's performance. The authors should provide a sensitivity analysis of the model's performance with respect to different values of α, β, γ, and λ. This analysis should include a discussion of how these hyperparameters affect the learned representations and the final IDRF estimates. Furthermore, the authors should provide guidance on how to choose appropriate values for these hyperparameters for different datasets. This could involve providing a set of rules of thumb based on the characteristics of the dataset, or providing a more systematic approach to hyperparameter tuning. The paper should also discuss the computational cost of the proposed method, and how it scales with the size of the dataset and the number of hyperparameters.

Finally, the experimental evaluation should be expanded to include more complex and realistic datasets. The authors should consider evaluating their method on datasets used in the literature on causal inference with continuous treatments. This would provide a more comprehensive evaluation of the method's effectiveness in real-world settings. Additionally, the paper should include a more comprehensive comparison to relevant baselines, such as those based on mutual information and debiased learning. This comparison should include a discussion of the strengths and weaknesses of each method, and a justification for why the proposed method is superior. The authors should also consider including ablation studies to evaluate the contribution of each component of their method. This would provide a more thorough understanding of the method's performance and its limitations.

### Questions

Please see the weaknesses.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
