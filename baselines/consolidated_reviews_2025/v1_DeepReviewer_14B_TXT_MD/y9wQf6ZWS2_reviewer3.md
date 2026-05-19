### Summary

The paper proposes a new Q-learning algorithm with linear function approximation. The proposed algorithm adds an L2 regularization term to the standard Q-learning update. The authors prove the convergence of the proposed algorithm using the ODE analysis framework and the switching system model. The authors also provide experimental results to show the performance of the proposed algorithm.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper is well-written and easy to follow.
2. The authors provide a detailed convergence analysis of the proposed algorithm.
3. The authors provide experimental results to show the performance of the proposed algorithm.

### Weaknesses

#### Some Related Works


#### comment

1. The main theorem (Theorem 5.2) of this paper is built on a very strong and unrealistic assumption (13), which makes the theoretical contribution of this paper very limited. Specifically, the assumption requires the regularization parameter to scale with the square root of the state and action space size, which is impractical for large or continuous spaces. This scaling makes it difficult to apply the algorithm in real-world scenarios where the state and action spaces are often very large or even continuous. 
2. The authors do not make it clear why the state space and action space are assumed to be both finite in this paper, while in most of the literature, only the state space is assumed to be finite while the action space is finite or infinite (but with bounded immediate reward). This assumption significantly limits the applicability of the proposed algorithm, as many real-world problems involve continuous or very large action spaces. The authors should justify this assumption and discuss its implications for the practical use of their algorithm.
3. The proposed algorithm is very similar to the algorithm in Diddigi et al., 2019, and the difference is that the former one applies the regularization to Q-function while the latter one applies the regularization to V-function. However, the authors do not discuss this similarity and do not show the difference in terms of performance. It is crucial to understand the practical implications of this difference and whether the proposed approach offers any advantages over the existing method.
4. The proposed algorithm is single time-scale, but the authors do not explain why single time-scale can perform better than double time-scale. The authors should provide a more detailed discussion of the trade-offs between single and double time-scale algorithms, and justify their choice of a single time-scale approach.
5. The experiments only show that the proposed algorithm, RegQ, performs faster than other algorithms, but the authors do not show that the error bound (Lemma 3.2) is valid. The authors should provide empirical evidence to support their theoretical claims, such as by plotting the error as a function of the number of iterations and showing that it converges to a small value. It is also important to compare the performance of the proposed algorithm with other algorithms in terms of the final error, not just the convergence speed.
6. The authors do not compare the proposed algorithm with other algorithms on large-scale problems, and do not show that the proposed algorithm can be applied to large-scale problems (with large state and action spaces or continuous state and action spaces) or not. The lack of experiments on large-scale problems makes it difficult to assess the practical applicability of the proposed algorithm. The authors should provide more extensive experiments on a variety of problems with different state and action space sizes to demonstrate the robustness and scalability of their approach.

### Suggestions

The paper's primary weakness lies in the strong theoretical assumptions, particularly the one concerning the regularization parameter, which limits the practical applicability of the proposed algorithm. The authors should provide a more detailed analysis of the sensitivity of the algorithm to the choice of the regularization parameter and how the performance degrades when this condition is not met. It would be beneficial to include experiments that explore the behavior of the algorithm under different regularization parameter values, including those that do not satisfy the theoretical condition. Furthermore, the authors should investigate alternative regularization techniques that do not rely on such strong assumptions, or provide a more practical method for selecting the regularization parameter. The current theoretical analysis, while technically sound, does not provide sufficient guidance for practical implementation. The authors should also consider providing a more detailed discussion on the implications of the finite state and action space assumption, and how their approach might be extended to handle continuous or very large action spaces. This could involve exploring the use of function approximation techniques that are suitable for continuous action spaces, such as neural networks or kernel methods. 

Another significant concern is the lack of a thorough comparison with existing methods, particularly the one in Diddigi et al., 2019. The authors should provide a detailed analysis of the differences between applying regularization to the Q-function versus the V-function, and discuss the potential advantages and disadvantages of each approach. This should include both theoretical considerations and empirical evidence. Furthermore, the authors should provide a more detailed discussion of the trade-offs between single and double time-scale algorithms, and justify their choice of a single time-scale approach. This should include a discussion of the potential benefits and drawbacks of each approach, and how they relate to the specific problem being addressed in the paper. The authors should also provide a more detailed analysis of the convergence properties of their algorithm, and provide empirical evidence to support their theoretical claims. This should include plotting the error as a function of the number of iterations and showing that it converges to a small value. It is also important to compare the performance of the proposed algorithm with other algorithms in terms of the final error, not just the convergence speed.

Finally, the experimental evaluation of the proposed algorithm is insufficient. The authors should include more extensive experiments on a variety of problems with different state and action space sizes. It is crucial to compare the performance of the proposed algorithm with other algorithms in terms of the final error, not just the convergence speed. The authors should also provide empirical evidence to support their theoretical claims, such as by plotting the error as a function of the number of iterations and showing that it converges to a small value. The current experiments do not provide sufficient evidence to demonstrate the practical applicability of the proposed algorithm. The authors should also investigate the performance of the algorithm on large-scale problems and provide a more detailed analysis of its scalability. This could involve using benchmark problems with larger state and action spaces, or even continuous state and action spaces. The authors should also consider comparing their algorithm with other state-of-the-art algorithms, and provide a detailed analysis of the results.

### Questions

1. Can you give some comments on Assumption 2.2? Is it a common assumption to make in the literature? What if the feature matrix does not satisfy Assumption 2.2?
2. Can you explain why the state space and action space are assumed to be both finite? Is it a common assumption to make in the literature?
3. Can you explain why (13) is a sufficient condition for -(A_{\pi_{X{\theta}_k}}+nI) to be negative definite? And can you give some comments on Lemma 3.1? Is it a common way to choose \eta in the literature?
4. Can you explain why \theta_k converges to \theta_e where \theta_e satisfies (9)?
5. Can you explain why the proposed algorithm performs faster than other algorithms? Is it because of the difference in the algorithms or just the difference in the parameter selection?

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
