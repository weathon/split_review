### Summary

This paper proposes a new method for label DP. The main idea is to use the public information of the data to denoise the differentially private gradient. They propose several denoisers and analyze their performances. Empirically, they show that their method outperforms existing baselines by a large margin.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

This paper is well-written. The idea of using public information to denoise the DP gradient is interesting. The empirical results look promising.

### Weaknesses

#### Some Related Works


#### comment

The proposed method still requires access to the full dataset to construct the denoiser, which can be a limitation in some settings. 
- The theoretical analysis does not fully explain the empirical results, particularly the discrepancy between the expected excess error bounds and the actual performance of SELFSPAN. The current analysis does not account for the variance of the gradient estimator, which is a crucial factor in the convergence of stochastic gradient descent. The analysis also assumes convexity of the loss function, which does not hold for neural networks, further limiting the applicability of the theoretical results.
- The paper lacks a detailed discussion of the computational cost associated with the projection operation, particularly the number of iterations required for convergence and the memory footprint of the gradient matrices. This is a critical aspect for practical implementation, especially when dealing with large datasets and complex models.

### Suggestions

The paper should provide a more detailed analysis of the computational cost associated with the projection operation. This should include a breakdown of the time and memory requirements for each step of the algorithm, including the computation of the Jacobian-vector product, the vector-Jacobian product, and the projection onto the convex hull. The authors should also discuss the trade-offs between the number of projection iterations, the accuracy of the projection, and the overall runtime of the algorithm. Furthermore, it would be beneficial to explore alternative projection methods that may be more computationally efficient or have better convergence properties. For example, iterative methods such as conjugate gradient or stochastic gradient descent could be considered for solving the projection problem, and their performance should be compared to the current approach. The authors should also provide a more detailed analysis of the memory requirements for storing the gradient matrices, and discuss strategies for reducing the memory footprint, such as using sparse matrix representations or low-rank approximations.

To strengthen the theoretical analysis, the authors should consider incorporating the variance of the gradient estimator into their error bounds. This could be done by using techniques from stochastic optimization theory, such as the analysis of stochastic gradient descent with noisy gradients. The authors should also discuss the limitations of their theoretical results, particularly the assumption of convexity, and explore alternative theoretical frameworks that may be more suitable for analyzing the convergence of their method on non-convex loss functions. For example, they could consider using techniques from non-convex optimization theory, such as the analysis of gradient descent on smooth non-convex functions. Furthermore, the authors should provide a more detailed explanation of the discrepancy between the theoretical bounds and the empirical results, and discuss the factors that may contribute to this discrepancy. This could include a discussion of the impact of the data distribution, the model architecture, and the choice of hyperparameters on the performance of the method.

Finally, the paper should include a more thorough evaluation of the proposed method on a wider range of datasets and models. This should include experiments on larger datasets, such as ImageNet, and more complex models, such as ResNets or Transformers. The authors should also compare their method to a wider range of baselines, including other label differential privacy methods and non-private methods. This would provide a more comprehensive assessment of the strengths and weaknesses of their method, and help to identify the settings in which it performs best. The authors should also provide a more detailed analysis of the sensitivity of their method to the choice of hyperparameters, such as the privacy parameter, the learning rate, and the number of projection iterations. This would help to provide practical guidance for users of their method.

### Questions

1.	Is it possible to use a subset of the dataset to compute the denoiser? What’s the trade-off between accuracy and efficiency?
2.	Can you provide a more detailed analysis of the time and memory cost for the projection? How long does it take to run on large datasets like ImageNet?
3.	Can you provide more explanation on why the excess error bound of ALTCONV is better than SELFCONV? 
4.	Why is the noise multiplier of SELFSPAN larger than ALTCONV in Table 3? 
5.	Can you provide some intuition on why the error bound of SELFSPAN does not have a dependence on dimension but the other ones do? 
6.	Can you provide some intuition on why the rate of SELFCONV is better than SELFSPAN? 
7.	In Lemma 4, why do you assume $I^P$ and $I^G$ are random? In the actual algorithm, aren’t both of them fixed?
8.	Can you provide some explanation on why the theoretical results in Table 4 do not match the empirical results in Table 3? In particular, based on Table 4, the error of DP-SGD should be better than SELFCONV but this is not the case in Table 3. 
9.	Can you provide some explanation on why DP-SGD works so poorly in the high privacy regime in Table 3?
10.	In Table 3, for a small epsilon, can you explain why DP-SGD is better than all the other methods except LabelDP-Pro?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
