### Summary

The paper proposes a novel neural network architecture (DBRNet) for estimating individual treatment effects in the case of continuous treatments. DBRNet assumes that the covariates are generated from three underlying factors: instrumental factors, confounder factors, and adjustment factors. DBRNet learns disentangled representations for each factor and uses a re-weighting function to adjust for selection bias. The paper provides theoretical proofs that the proposed re-weighting function can precisely adjust for selection bias. Experiments on synthetic and semi-synthetic datasets show that DBRNet outperforms state-of-the-art methods and demonstrate the effectiveness of each component in the model.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The paper proposes a novel neural network architecture (DBRNet) for estimating individual treatment effects in the case of continuous treatments.
- DBRNet learns disentangled representations for instrumental, confounder, and adjustment factors, and uses a re-weighting function to precisely adjust for selection bias.
- The paper provides theoretical proofs that the proposed re-weighting function can precisely adjust for selection bias.
- Experiments on synthetic and semi-synthetic datasets show that DBRNet outperforms state-of-the-art methods.

### Weaknesses

#### Some Related Works


#### comment

 - The proposed DBRNet assumes that covariates are generated from three underlying factors: instrumental factors, confounder factors, and adjustment factors. This assumption may not hold in all cases, and the performance of DBRNet may suffer if the assumption is violated. Specifically, the assumption of distinct, disentangled factors is a strong one, and the paper does not provide sufficient justification for its applicability in real-world scenarios. The model's performance could be significantly impacted if these factors are entangled or if the true data generating process does not adhere to this specific decomposition.
- DBRNet requires careful tuning of hyperparameters, such as the number of hidden layers and the learning rate, which can be time-consuming and require expert knowledge. The paper lacks a detailed discussion on the sensitivity of the model to these hyperparameters and does not provide clear guidelines on how to choose them effectively. This makes the model difficult to use in practice, as users may struggle to find the optimal hyperparameter settings.
- The paper does not provide any theoretical guarantees for the generalization performance of DBRNet. Without such guarantees, it is difficult to assess the reliability of the model in unseen data. The lack of bounds on the generalization error makes it hard to determine how well the model will perform on new datasets, especially when the training data is limited or noisy.

### Suggestions

The paper should include a more thorough discussion of the limitations of the assumption that covariates are generated from three distinct underlying factors. It would be beneficial to explore scenarios where this assumption is violated and analyze the impact on the model's performance. For example, the authors could investigate how the model behaves when the instrumental, confounder, and adjustment factors are not perfectly disentangled in the data. Furthermore, the paper should provide empirical evidence to support the claim that the model can still perform well when the generating function for adjustment factors depends on other factors. This could involve experiments on synthetic datasets where the degree of entanglement between factors is systematically varied. A sensitivity analysis of the model's performance with respect to different data generating processes would greatly enhance the robustness of the proposed method.

To address the hyperparameter tuning issue, the authors should conduct a more detailed sensitivity analysis of the model's performance with respect to different hyperparameter settings. This analysis should include a discussion of how the learning rate, the number of hidden layers, and other key hyperparameters affect the model's performance. The paper should also provide practical guidelines on how to choose these hyperparameters effectively, potentially by suggesting a range of values that work well across different datasets. It would be helpful to include a discussion of the trade-offs between model complexity and performance, and to provide recommendations on how to select the optimal model complexity for a given dataset. The authors could also explore techniques for automated hyperparameter tuning, such as grid search or Bayesian optimization, to make the model more user-friendly.

Finally, the paper needs to address the lack of theoretical guarantees for the generalization performance of DBRNet. While the authors provide theoretical proofs for the debiasing ability of the re-weighting function, they do not provide any bounds on the generalization error of the overall model. It would be beneficial to include a discussion of the assumptions under which the model is expected to generalize well, and to provide some empirical evidence of its generalization performance on unseen data. The authors could also explore techniques for improving the generalization performance of the model, such as regularization or early stopping. Without such guarantees, it is difficult to assess the reliability of the model in practical applications, and the paper should acknowledge this limitation.

### Questions

- How does the performance of DBRNet compare to other methods in the case of discrete treatments?
- How does the performance of DBRNet vary with the choice of hyperparameters, such as the number of hidden layers and the learning rate?
- How does the performance of DBRNet vary with the size of the dataset?
- What are the theoretical guarantees for the generalization performance of DBRNet?

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
