### Summary

This paper proposes a new uncertainty estimation method called Relaxed-EDL, which relaxes two non-essential settings in the model construction and optimization stages of Evidential Deep Learning (EDL). Specifically, the prior weight in the construction stage is treated as an adjustable hyperparameter, and the variance-minimized regularization term in the optimization stage is omitted. Experimental results on various benchmarks for uncertainty estimation tasks, including confidence estimation and out-of-distribution detection, demonstrate the effectiveness of the proposed method.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is simple and easy to implement.
3. The authors provide a comprehensive analysis of the prior weight in evidential deep learning and its impact on uncertainty estimation.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a thorough literature review, particularly regarding related works that address uncertainty estimation in classification tasks. For instance, [1] also utilizes the Dirichlet distribution to estimate uncertainty, and [2] and [3] focus on classification tasks with uncertainty estimation. The authors should discuss these works and clarify how their approach differs from and improves upon these existing methods.

2. The authors claim that the prior weight in EDL is a non-essential setting, but they do not provide a clear explanation of why this is the case. The prior weight plays a crucial role in EDL, and its impact on the model's performance should be thoroughly discussed. The authors should provide a more detailed analysis of the role of the prior weight and why relaxing it is beneficial.

3. The authors remove the variance-minimizing regularization term from the optimization objective, but they do not provide a clear explanation of why this term is important. The authors should discuss the potential drawbacks of removing this term and how it affects the model's performance.

4. The experimental results are not convincing enough to demonstrate the effectiveness of the proposed method. The authors should provide more comprehensive experiments, including comparisons with other state-of-the-art methods and evaluations on more challenging datasets.

5. The authors should provide a more detailed analysis of the computational cost of the proposed method. The authors should discuss the trade-offs between performance and computational cost and how the proposed method compares to other methods in terms of efficiency.

### Suggestions

The paper would benefit significantly from a more thorough literature review that places the proposed method within the context of existing uncertainty estimation techniques. Specifically, the authors should discuss how their approach relates to methods that use Dirichlet distributions for uncertainty estimation, such as those found in the cited works [1,2,3]. A detailed comparison of the proposed method with these existing approaches is necessary to highlight the novelty and contributions of this work. The authors should clarify the differences in methodology, assumptions, and performance characteristics. Furthermore, the authors should provide a more in-depth analysis of the prior weight in EDL. The claim that it is a non-essential setting requires more justification. The authors should explain the role of the prior weight in the EDL framework and why fixing it to the class number might be suboptimal. A theoretical analysis or empirical evidence demonstrating the impact of different prior weight values on the model's performance is needed. The authors should also discuss the potential drawbacks of removing the variance-minimizing regularization term. While the authors claim that this term encourages the Dirichlet distribution to approach a Dirac delta function, which may lead to overconfidence, they do not provide a clear explanation of why this is a desirable property. The authors should discuss the potential trade-offs of removing this term and how it affects the model's performance. For example, they should analyze the impact of the regularization term on the model's ability to detect out-of-distribution samples. The authors should also provide more comprehensive experimental results to demonstrate the effectiveness of the proposed method. The current experiments are not sufficient to convince the reader of the method's superiority. The authors should include comparisons with other state-of-the-art methods on more challenging datasets. The authors should also provide a more detailed analysis of the computational cost of the proposed method. The authors should discuss the trade-offs between performance and computational cost and how the proposed method compares to other methods in terms of efficiency. The authors should also discuss the limitations of the proposed method and suggest future research directions.

### Questions

Please see the weaknesses above.

### Rating

5

### Confidence

4

**********
