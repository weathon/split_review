### Summary

This paper proposes a new method for imputing missing values in tabular data. The method, called ReMasker, extends the masked autoencoding framework to impute missing values of tabular data. It randomly "re-masks" another set of values, then trains the model to predict the re-masked values. The paper also provides theoretical justification for the effectiveness of the method.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow.
2. The method is simple and easy to implement.
3. The paper provides a theoretical justification for the effectiveness of the method.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a clear explanation of why the proposed method is effective. The paper claims that the method learns missingness-invariant representations, but it does not provide any empirical evidence to support this claim.
2. The paper does not compare the proposed method with other state-of-the-art methods for imputing missing values in tabular data. The paper only compares the proposed method with some basic baselines.
3. The paper does not discuss the limitations of the proposed method. For example, the paper does not discuss how the method performs when the missingness is not random.

### Suggestions

The paper should provide a more detailed explanation of why the proposed method is effective. While the authors claim that the method learns missingness-invariant representations, they do not provide any empirical evidence to support this claim. It would be beneficial to include experiments that specifically test the model's ability to generalize to different missingness mechanisms. For example, the authors could train the model on data with one type of missingness and then evaluate its performance on data with a different type of missingness. This would provide more evidence for the claim that the model learns missingness-invariant representations. Furthermore, the paper should include a more detailed analysis of the learned representations. For example, the authors could visualize the learned representations to see if they are indeed invariant to missingness patterns. This would provide more insight into how the model is able to impute missing values effectively.

The paper should also compare the proposed method with other state-of-the-art methods for imputing missing values in tabular data. The current comparison is limited to basic baselines, which does not provide a clear picture of the method's performance relative to existing techniques. The authors should include comparisons with methods such as MissForest, MissForest++, and other relevant methods. This would provide a more comprehensive evaluation of the proposed method and allow readers to better understand its strengths and weaknesses. The paper should also discuss the computational cost of the proposed method compared to other methods. This would be important for practitioners who need to choose the most appropriate method for their specific application.

Finally, the paper should discuss the limitations of the proposed method. For example, the paper does not discuss how the method performs when the missingness is not random. The authors should acknowledge that the method may not perform well in such cases and discuss potential solutions for addressing this issue. The paper should also discuss the sensitivity of the method to the choice of hyperparameters. It would be beneficial to include experiments that explore the impact of different hyperparameter settings on the performance of the method. This would provide a more complete picture of the method's behavior and allow readers to better understand its limitations.

### Questions

1. How does the proposed method compare to other state-of-the-art methods for imputing missing values in tabular data?
2. How does the proposed method perform when the missingness is not random?

### Rating

5

### Confidence

3

**********
