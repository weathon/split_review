### Summary

This paper introduces a novel Disentangled and Balanced Representation Network (DBRNet) for estimating the individualized dose-response function (IDRF) in continuous treatment settings. The proposed method learns disentangled representations for instrumental, confounder, and adjustment factors, and precisely adjusts for selection bias using a re-weighting function. The authors provide theoretical proofs for the debiasing ability of the re-weighting function and demonstrate the effectiveness of DBRNet on synthetic and semi-synthetic datasets. The main contributions of the paper include a new method for continuous treatment effect estimation, the first model to precisely adjust for selection bias in continuous treatment settings with theoretical proofs, and extensive experiments validating the effectiveness and disentangling ability of the model.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper proposes a novel method, DBRNet, which learns disentangled and balanced representations for continuous treatment effect estimation at the individual level. This is a significant contribution to the field of causal inference, as existing methods are limited to discrete treatment settings or rely on simplistic approaches for balancing representations.
2. The authors provide theoretical proofs that the proposed re-weighting function can precisely adjust for selection bias in continuous treatment settings. This is a valuable contribution, as it provides a rigorous justification for the debiasing ability of the proposed method.
3. The paper includes extensive experiments on synthetic and semi-synthetic datasets to validate the effectiveness and disentangling ability of DBRNet. The results show that DBRNet outperforms state-of-the-art methods in estimating the individualized dose-response function (IDRF) and adjusting for selection bias.

### Weaknesses

#### Some Related Works


#### comment

1. The paper assumes that covariates are generated from three underlying factors: instrumental factors, confounder factors, and adjustment factors. This assumption may not hold in all cases, and the performance of DBRNet may suffer if the assumption is violated. Specifically, the assumption of distinct, disentangled factors is a strong one, and the paper does not provide sufficient justification for its applicability in real-world scenarios. The model's performance could be significantly impacted if these factors are entangled or if the true data generating process does not adhere to this specific decomposition. Furthermore, the paper does not discuss how to assess the validity of this assumption in practice, which limits the practical applicability of the method.
2. DBRNet requires careful tuning of hyperparameters, such as the number of hidden layers and the learning rate, which can be time-consuming and require expert knowledge. The paper lacks a detailed discussion on the sensitivity of the model to these hyperparameters and does not provide clear guidelines on how to choose them effectively. This makes the model difficult to use in practice, as users may struggle to find the optimal hyperparameter settings. The absence of a systematic approach to hyperparameter selection, such as a grid search or Bayesian optimization, further exacerbates this issue.
3. The paper does not provide any theoretical guarantees for the generalization performance of DBRNet. Without such guarantees, it is difficult to assess the reliability of the model in unseen data. The lack of bounds on the generalization error makes it hard to determine how well the model will perform on new datasets, especially when the training data is limited or noisy. This is a significant limitation, as it is crucial to understand the conditions under which the model is expected to perform well and when it might fail.

### Suggestions

The paper would benefit from a more thorough discussion of the assumptions underlying the proposed method. Specifically, the assumption that covariates are generated from three distinct factors (instrumental, confounder, and adjustment) needs further justification. The authors should explore the implications of violating this assumption and provide guidance on how to assess its validity in real-world applications. For example, they could discuss how to diagnose potential issues when the factors are entangled or when the data generating process deviates from the assumed structure. Furthermore, it would be beneficial to include experiments on datasets where this assumption is violated to demonstrate the robustness (or lack thereof) of the method. This would provide a more complete picture of the method's applicability and limitations.

To address the hyperparameter tuning issue, the authors should conduct a more detailed sensitivity analysis of the model's performance with respect to different hyperparameter settings. This analysis should include a discussion of how the learning rate, the number of hidden layers, and other key hyperparameters affect the model's performance. The paper should also provide practical guidelines on how to choose these hyperparameters effectively, potentially by suggesting a range of values that work well across different datasets. It would be helpful to include a discussion of the trade-offs between model complexity and performance, and to provide recommendations on how to select the optimal model complexity for a given dataset. The authors could also explore techniques for automated hyperparameter tuning, such as grid search or Bayesian optimization, to make the model more user-friendly. This would significantly improve the practical usability of the proposed method.

Finally, the paper needs to address the lack of theoretical guarantees for the generalization performance of DBRNet. While the authors provide theoretical proofs for the debiasing ability of the re-weighting function, they do not provide any bounds on the generalization error of the overall model. It would be beneficial to include a discussion of the assumptions under which the model is expected to generalize well, and to provide some empirical evidence of its generalization performance on unseen data. The authors could also explore techniques for improving the generalization performance of the model, such as regularization or early stopping. Without such guarantees, it is difficult to assess the reliability of the model in practical applications, and the paper should acknowledge this limitation.

### Questions

1. How does the performance of DBRNet compare to other methods in the case of discrete treatments?
2. How does the performance of DBRNet vary with the choice of hyperparameters, such as the number of hidden layers and the learning rate?
3. How does the performance of DBRNet vary with the size of the dataset?
4. What are the theoretical guarantees for the generalization performance of DBRNet?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
