### Summary

The paper proposes a novel method for estimating the dose-response function (IDRF) with continuous treatments. The proposed method, DBRNet, learns disentangled representations of the covariates to adjust for selection bias using a re-weighting function and a varying coefficient network. The authors provide theoretical proofs for the debiasing properties of their method and conduct extensive experiments on synthetic and semi-synthetic datasets to demonstrate its effectiveness.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The paper addresses an important problem in causal inference, particularly in settings with continuous treatments.
- The proposed method is theoretically grounded and provides debiasing proofs for the re-weighting function.
- The authors conduct extensive experiments on multiple datasets, demonstrating the effectiveness of DBRNet compared to existing methods.

### Weaknesses

#### Some Related Works

[1] Estimating heterogeneous treatment effects: Mutual information bounds and learning algorithms.
[2] Causal forests for estimating heterogeneous effects.
[3] Generalized random forests.
[4] Automatic Debiased Learning for Causal Effect under the always-observed confounders.
[5] Debiased heterogeneous treatment effects estimation using instrument residual networks.

#### comment

 - The paper does not adequately address the identifiability assumptions required for estimating the IDRF with continuous treatments. Specifically, the assumption that the learned adjustment factors do not embed information about the treatment is not sufficiently justified. The paper lacks a discussion on how this assumption is met in practice, and what are the potential consequences if this assumption is violated. The authors should provide a more rigorous analysis of the conditions under which this assumption holds, and discuss the implications of its violation.
- The proposed method relies on several hyperparameters (α, β, γ, λ) that control the weights of different loss terms. The paper lacks a clear strategy for selecting these hyperparameters, and the sensitivity of the results to these choices is not adequately explored. The authors should provide a more detailed analysis of how these hyperparameters affect the performance of the model, and provide guidance on how to choose appropriate values for different datasets.
- The experimental evaluation is limited to relatively simple datasets. The authors should consider evaluating their method on more complex and realistic datasets, such as those used in the literature on causal inference with continuous treatments. The current evaluation does not provide sufficient evidence that the proposed method is effective in real-world settings.
- The paper does not compare the proposed method to some relevant baselines, such as those based on mutual information [1] or debiased learning [2,3,4,5]. The authors should include a more comprehensive comparison to these methods to demonstrate the advantages of their approach.

### Suggestions

The paper should provide a more detailed discussion of the identifiability assumptions required for estimating the IDRF with continuous treatments. Specifically, the authors should elaborate on the conditions under which the learned adjustment factors do not embed information about the treatment. This could involve a more in-depth analysis of the relationship between the learned representations and the treatment variable, and a discussion of the potential consequences of violating this assumption. The authors should also consider providing a theoretical analysis of the sensitivity of their method to violations of this assumption. Furthermore, the authors should provide a more detailed explanation of how the proposed method addresses the challenges of continuous treatments, and how it differs from existing methods for discrete treatments. This should include a discussion of the specific technical innovations that enable the method to handle continuous treatments, and a comparison to existing methods in terms of their ability to handle continuous treatments.

The authors should provide a more detailed analysis of the hyperparameter selection process, including a sensitivity analysis of the model's performance to different values of α, β, γ, and λ. This analysis should include a discussion of how these hyperparameters affect the learned representations and the final IDRF estimates. The authors should also provide guidance on how to choose appropriate values for these hyperparameters for different datasets. This could involve providing a set of rules of thumb based on the characteristics of the dataset, or providing a more systematic approach to hyperparameter tuning. The authors should also consider using techniques such as cross-validation to select the hyperparameters, and provide a justification for the chosen approach. The paper should also include a discussion of the computational cost of the proposed method, and how it scales with the size of the dataset and the number of hyperparameters.

The experimental evaluation should be expanded to include more complex and realistic datasets, such as those used in the literature on causal inference with continuous treatments. This would provide more evidence that the proposed method is effective in real-world settings. The authors should also compare their method to a wider range of baselines, including methods based on mutual information [1] and debiased learning [2,3,4,5]. This comparison should include a discussion of the strengths and weaknesses of each method, and a justification for why the proposed method is superior. The authors should also consider including ablation studies to evaluate the contribution of each component of their method. This would provide a better understanding of the importance of each component and how they interact with each other. The authors should also provide a more detailed analysis of the results, including a discussion of the statistical significance of the differences between the proposed method and the baselines.

### Questions

- How does the proposed method address the identifiability assumptions required for estimating the IDRF with continuous treatments?
- How are the hyperparameters (α, β, γ, λ) selected in practice, and how sensitive is the model's performance to these choices?
- How does the proposed method compare to existing methods for estimating the IDRF with continuous treatments, such as those based on mutual information [1] or debiased learning [2,3,4,5]?

[1] Singh, Viraj, et al. "Estimating heterogeneous treatment effects: Mutual information bounds and learning algorithms." Advances in Neural Information Processing Systems 36 (2024).

[2] Nie, Xinkun, et al. "Causal forests for estimating heterogeneous effects." Advances in neural information processing systems 33 (2020).

[3] Wager, Stefan, and phenotypeConfounded causal forests for estimating heterogeneous effects. Advances in neural information processing systems, 2021.

[4] Bruns-Smith, Elias, et al. "Automatic Debiased Learning for Causal Effect under the always-observed confounders." arXiv preprint arXiv:2406.05210 (2024).

[5] Schwab, Patrick, et al. "Debiased heterogeneous treatment effects estimation using instrument residual networks." Advances in Neural Information Processing Systems 35 (2022): 20144-20160.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
