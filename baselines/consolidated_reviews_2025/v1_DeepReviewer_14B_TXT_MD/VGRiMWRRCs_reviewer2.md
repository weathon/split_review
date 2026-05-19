### Summary

This paper proposes a new method to improve group robustness in machine learning models by unifying existing approaches within an Empirical Bayesian framework. The authors introduce a novel technique called "Learn from Known Unknowns" (LfKU), which leverages epistemic uncertainty to identify and reweight samples that are likely affected by spurious correlations. The method involves a two-phase process: first, training a standard ERM model with evidence regularization to estimate uncertainty, and second, retraining only the last layer of the model using a reweighted loss based on the uncertainty estimates. The authors demonstrate that LfKU improves worst-group accuracy across diverse datasets, including Colored MNIST, Waterbirds, CelebA, MultiNLI, and CivilComments, while reducing the need for extensive hyperparameter tuning.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

1. The paper introduces a novel perspective by framing several existing group robustness methods within an Empirical Bayesian framework, providing a more unified understanding of these techniques.
2. The paper is well-organized, with clear explanations of the problem, related work, and the proposed method. The authors provide a detailed description of the LfKU method, including the mathematical formulation and implementation details.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a rigorous theoretical analysis of the proposed method, particularly regarding the convergence properties of the uncertainty estimation and the reweighting scheme. Specifically, the paper does not provide any theoretical guarantees on how the epistemic uncertainty estimates converge to accurate representations of the true uncertainty, nor does it analyze how the reweighting scheme affects the optimization landscape and the convergence of the last-layer retraining. The absence of such analysis makes it difficult to assess the robustness and reliability of the method, especially in scenarios with complex data distributions or high levels of spurious correlation.
2. The paper does not provide a detailed analysis of the computational cost of the proposed method compared to existing approaches. While the authors mention that only the last layer is retrained, they do not provide a quantitative comparison of the training time and memory requirements with methods like JTT and CnC. This lack of analysis makes it difficult to evaluate the practical applicability of the method, particularly in resource-constrained environments. A more detailed breakdown of the computational overhead, including the cost of uncertainty estimation and reweighting, is needed.
3. The paper could benefit from a more thorough comparison with a wider range of existing group robustness methods, including those that do not rely on group annotations. While the paper compares against several methods, it does not include comparisons with methods such as Invariant Risk Minimization (IRM) or Logit Correction (LC), which are relevant baselines for group robustness. A more comprehensive comparison would provide a better understanding of the strengths and weaknesses of the proposed method relative to the state-of-the-art.

### Suggestions

To strengthen the theoretical foundation of the proposed method, the authors should provide a more detailed analysis of the convergence properties of the uncertainty estimation and the reweighting scheme. This could involve deriving bounds on the estimation error of the epistemic uncertainty and analyzing how the reweighting scheme affects the optimization landscape. Specifically, the authors could investigate whether the reweighting scheme introduces any bias or variance in the gradient estimates, and how this affects the convergence of the last-layer retraining. Furthermore, it would be beneficial to explore the conditions under which the proposed method is guaranteed to improve worst-group accuracy. Such theoretical analysis would provide a more rigorous understanding of the method's behavior and its limitations, and would increase the confidence in its applicability to different scenarios.

To address the lack of detailed computational analysis, the authors should provide a quantitative comparison of the training time and memory requirements of the proposed method with a wider range of existing approaches. This should include a breakdown of the computational cost of each step of the method, such as the initial ERM training, uncertainty estimation, and last-layer retraining. The comparison should also include methods like JTT and CnC, as well as other relevant baselines, to provide a comprehensive understanding of the computational trade-offs. Furthermore, the authors should discuss the scalability of the proposed method to larger datasets and models, and identify any potential bottlenecks that might limit its applicability. This analysis should be presented in a clear and concise manner, with specific numbers and comparisons to support the claims.

To provide a more comprehensive evaluation of the proposed method, the authors should include comparisons with a wider range of existing group robustness methods, including those that do not rely on group annotations. This should include methods such as Invariant Risk Minimization (IRM) and Logit Correction (LC), which are relevant baselines for group robustness. The comparison should be performed on a variety of datasets and metrics, to provide a more complete picture of the method's performance. Furthermore, the authors should provide a detailed analysis of the method's sensitivity to different hyperparameter settings, and discuss how to choose the optimal hyperparameters for different datasets. This would help to ensure that the method is practical and easy to use in different scenarios.

### Questions

1. Could the authors provide more details on the convergence properties of the uncertainty estimation and the reweighting scheme?
2. How does the computational cost of the proposed method compare to existing approaches, especially in terms of training time and memory requirements?
3. Could the authors provide a more detailed comparison with a wider range of existing group robustness methods, including those that do not rely on group annotations?

### Rating

5

### Confidence

3

**********
