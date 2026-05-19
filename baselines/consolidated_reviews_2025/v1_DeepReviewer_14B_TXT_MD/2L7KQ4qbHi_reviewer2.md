### Summary

This paper proposes a method for "concept unlearning", which the authors define as modifying a model trained on a concept so that it is independent of the concept in its predictions. This is distinct from machine unlearning, which is to remove the effect of certain training examples from the model. 

The goal is to minimize a concept violation metric that measures how much the model remains neutral towards a concept for its predictions, while minimizing accuracy loss on the overall task. The proposed method, Label Annealing (LAN), iteratively assigns psuedo-labels to training examples by redistributing the labels to match the model's predicted class distribution, then fine-tunes on these psuedo-labels. Theoretical analysis shows that if the original model has low concept violation, the performance of the new model will not degrade significantly. Experimental results show that the method outperforms fairness baselines at forgetting concepts while maintaining accuracy.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

* The problem formulation of "concept unlearning" is novel and interesting. It is distinct from the more popular "machine unlearning" idea, and has some interesting applications, such as removing spurious correlations or biases in the model.
* The proposed LAN method is simple and intuitive. The theoretical analysis provides some justification for the method. The experimental results are promising, showing that the method can effectively forget concepts while maintaining accuracy.
* The paper is well-written and easy to understand.

### Weaknesses

#### Some Related Works


#### comment

 * The proposed method is very similar to iterative class label restoration methods, such as those used in semi-supervised learning or noisy label cleaning. The core idea of reassigning labels based on model predictions and retraining is a common paradigm. The paper does not adequately differentiate its approach from these existing techniques, especially in terms of the specific algorithmic steps and the underlying assumptions. For example, methods like self-training or label propagation also iteratively refine labels based on model confidence, and the paper needs to clarify how LAN's label annealing process is distinct.
* The experimental results are limited to small-scale datasets and relatively simple models. It is unclear how the method would perform on larger, more complex datasets and models. The paper lacks experiments on datasets like ImageNet or with models like ResNet-50, which are standard benchmarks for image classification. This makes it difficult to assess the scalability and robustness of the proposed method. Furthermore, the paper does not explore the computational cost of the iterative label annealing process, which could be a limiting factor for larger datasets and models.
* The baselines are primarily from the fairness domain, which may not be the most relevant comparison for concept unlearning. While the authors argue that concept unlearning is distinct from machine unlearning, the connection to fairness is not fully justified. The paper should include comparisons to methods that are more directly related to label noise correction or semi-supervised learning, as these areas also deal with issues of label quality and model robustness. The current baselines do not provide a strong enough comparison to demonstrate the effectiveness of LAN in a broader context.

### Suggestions

The paper should more clearly articulate the novelty of the proposed method compared to existing techniques in semi-supervised learning and noisy label correction. A detailed comparison of the algorithmic steps, including the specific differences in how labels are reassigned and how the model is updated, would be beneficial. For example, the paper could discuss how the label annealing process differs from standard self-training or label propagation methods, and what specific advantages it offers in the context of concept unlearning. It would also be helpful to analyze the theoretical properties of the proposed method, such as convergence guarantees or bounds on the error, and compare these properties to existing methods. This would provide a more rigorous justification for the proposed approach and highlight its unique contributions.

To address the limitations in the experimental evaluation, the paper should include results on larger, more complex datasets and models. Experiments on ImageNet with models like ResNet-50 would provide a more realistic assessment of the method's scalability and robustness. The paper should also analyze the computational cost of the iterative label annealing process, and discuss how this cost scales with the size of the dataset and the complexity of the model. Furthermore, the paper should explore the sensitivity of the method to different hyperparameters, such as the number of iterations and the learning rate, and provide guidelines for selecting appropriate values. This would make the method more practical and easier to use in different settings.

Finally, the paper should include comparisons to more relevant baselines, such as methods for label noise correction or semi-supervised learning. This would provide a more comprehensive evaluation of the method's performance and demonstrate its effectiveness in a broader context. For example, the paper could compare LAN to methods like reweighted training or robust optimization, which are designed to handle noisy labels. It could also compare to methods like virtual adversarial training or consistency regularization, which are commonly used in semi-supervised learning. These comparisons would help to clarify the strengths and weaknesses of the proposed method and highlight its unique contributions to the field.

### Questions

* How is the proposed method different from iterative class label restoration methods in semi-supervised learning or noisy label cleaning?
* How does the method scale to larger datasets and more complex models?
* What is the computational cost of the iterative label annealing process?
* How sensitive is the method to different hyperparameters, such as the number of iterations and the learning rate?
* Are there other baselines that would be more relevant for comparison, such as methods for label noise correction or semi-supervised learning?

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
