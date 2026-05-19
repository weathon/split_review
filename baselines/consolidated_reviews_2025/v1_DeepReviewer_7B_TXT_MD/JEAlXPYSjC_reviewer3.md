### Summary

This paper proposes a simple strategy to improve the performance of CLIP models. The authors first demonstrate that CLIP models trained on smaller datasets saturate after a few epochs and that simply training for longer does not significantly affect accuracy. They then propose a strategy to improve the performance of CLIP models by resetting the learning rate scheduler and training for a few extra epochs. The authors show that this strategy can improve the performance of CLIP models on various downstream tasks.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow.
2. The paper provides a simple and effective strategy to improve the performance of CLIP models.
3. The paper provides empirical evidence to support the effectiveness of the proposed strategy.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a theoretical explanation for why the proposed strategy works.
2. The paper does not compare the proposed strategy with other methods for improving CLIP training, such as those proposed in [1] and [2].
3. The paper does not discuss the limitations of the proposed strategy.
4. The paper does not provide a detailed analysis of the computational cost of the proposed strategy.

### Suggestions

The paper would benefit from a more thorough investigation into the underlying mechanisms that contribute to the observed performance gains. While the empirical results are compelling, a theoretical framework explaining why resetting the learning rate scheduler and training for additional epochs leads to improved performance would significantly strengthen the paper's contribution. Specifically, the authors could explore the connection between the learning rate schedule and the optimization landscape, perhaps by analyzing the trajectory of the model parameters during training. This could involve techniques such as visualizing the loss landscape or analyzing the Hessian of the loss function to understand how the learning rate schedule affects the convergence properties of the model. Furthermore, it would be beneficial to investigate whether the observed improvements are specific to certain types of datasets or model architectures, or if they generalize to a broader range of scenarios. This would require a more diverse set of experiments, including a wider range of datasets and model architectures.

In addition to a theoretical analysis, the paper should include a more comprehensive comparison with existing methods for improving CLIP training. The authors should not only compare their proposed strategy with other methods in terms of final performance, but also in terms of training efficiency and computational cost. For example, the authors could compare their approach with methods that use different optimization algorithms or data augmentation techniques. This would provide a more complete picture of the advantages and disadvantages of the proposed strategy. Furthermore, the authors should discuss the limitations of their approach, such as the potential for overfitting or the sensitivity to hyperparameter settings. This would help to clarify the scope of applicability of the proposed strategy and provide guidance for future research.

Finally, the paper should provide a more detailed analysis of the computational cost of the proposed strategy. While the authors mention that the additional training epochs are relatively small, they do not provide a quantitative analysis of the computational resources required. This is important because the computational cost of training large models can be a significant barrier to adoption. The authors should provide a breakdown of the training time and memory requirements for different model sizes and datasets. They should also discuss the potential for parallelizing the additional training epochs to reduce the overall training time. This would make the proposed strategy more practical and accessible to a wider range of researchers.

### Questions

1. How does the proposed strategy compare to other methods for improving CLIP training?
2. What are the limitations of the proposed strategy?
3. What is the computational cost of the proposed strategy?

### Rating

5

### Confidence

3

**********
