### Summary

The paper proposes a training-free adaptation method for CLIP. Specifically, the method utilizes Bayes' formula and the maximum likelihood estimator to derive a linear classifier based on the class means and covariance, which can be estimated from the training data. The method is further extended to base-to-new generalization and unsupervised learning. The experimental results show that the proposed method achieves comparable or superior performance to previous training-free methods.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The proposed method is simple and easy to implement.
2. The paper is well-written and easy to follow.
3. The experimental results show that the proposed method achieves comparable or superior performance to previous training-free methods.

### Weaknesses

#### Some Related Works


#### comment

1. The novelty is limited. The proposed method is a simple combination of existing techniques, including Bayes' formula and the maximum likelihood estimator. The application of these techniques to derive a linear classifier for CLIP is not particularly innovative. The method essentially uses a closed-form solution for the linear classifier parameters, which is a well-established technique in machine learning. The paper does not introduce any novel optimization or regularization strategies that would distinguish it from existing approaches.
2. The performance gain is marginal. The experimental results show only slight improvements over previous training-free methods. While the method achieves comparable performance, the gains are not substantial enough to justify the claim of a significant advancement. The improvements are often within the margin of error or are not consistent across all datasets, which raises questions about the robustness and generalizability of the proposed method.
3. The paper does not discuss the limitations of the proposed method. For example, the method assumes that the class means and covariance are sufficient to represent the data distribution, which may not hold true in complex real-world scenarios. The method also does not address the issue of class imbalance, which is a common problem in many practical applications. The lack of discussion on these limitations makes it difficult to assess the practical applicability of the proposed method.

### Suggestions

The paper should explore more sophisticated methods for deriving the linear classifier, rather than relying on a simple closed-form solution. For instance, the authors could investigate techniques such as kernel methods or non-linear dimensionality reduction to better capture the underlying data structure. This would allow the method to potentially achieve better performance, especially in cases where the data is not linearly separable. Furthermore, the authors should consider incorporating regularization techniques to prevent overfitting and improve the generalization performance of the classifier. This could involve techniques such as L1 or L2 regularization, or more advanced methods like dropout or early stopping. These techniques could help to make the method more robust and less sensitive to the specific characteristics of the training data.

To address the issue of marginal performance gains, the authors should conduct a more thorough analysis of the experimental results. This should include a detailed investigation of the cases where the proposed method performs well and the cases where it does not. This analysis could provide valuable insights into the strengths and weaknesses of the method, and could help to identify areas for improvement. The authors should also consider comparing their method to a wider range of baselines, including both training-free and training-based methods. This would provide a more comprehensive evaluation of the method's performance and would help to contextualize the results. Additionally, the authors should explore the sensitivity of the method to different hyperparameter settings, such as the choice of kernel or the regularization parameters. This would help to ensure that the method is robust and can be easily applied to different datasets.

Finally, the paper should include a more detailed discussion of the limitations of the proposed method. This should include a discussion of the assumptions made by the method, such as the assumption of Gaussian distributions and the assumption of sufficient class means and covariance. The authors should also discuss the limitations of the method in handling class imbalance and other real-world challenges. This would help to provide a more balanced and realistic assessment of the method's practical applicability. The authors should also consider exploring methods for addressing these limitations, such as techniques for handling imbalanced data or methods for learning more robust representations. This would make the paper more impactful and would help to guide future research in this area.

### Questions

1. Why the proposed method can outperform some training-required methods?
2. What is the computational cost of the proposed method compared to training-required methods?

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
