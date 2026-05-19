### Summary

The paper presents a simple method to improve the performance of CLIP models on ImageNet zero-shot classification. The idea is to continue training the model for a few more epochs after the learning rate schedule has decayed to zero. Experiments are conducted on CLIP models trained on CC12M and LAION-400M. The results show that this simple method can improve the zero-shot classification accuracy on ImageNet.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

The method is simple and easy to implement. The paper is well-written and easy to understand.

### Weaknesses

#### Some Related Works


#### comment

The method is ad-hoc and lacks theoretical justification. The experiments are limited to a few CLIP models and do not explore the impact of different hyperparameters or training datasets. The paper does not provide a clear explanation of why continuing training after the learning rate has decayed to zero improves performance, especially since the model should ideally be converging. The lack of ablation studies on the learning rate schedule and the number of additional training epochs makes it difficult to assess the robustness of the method. Furthermore, the experiments are limited to ImageNet zero-shot classification, and it is unclear if the method would generalize to other datasets or tasks.

### Suggestions

The paper should include a more thorough investigation into the effect of the learning rate schedule on the performance of CLIP models. Specifically, it would be beneficial to explore different learning rate schedules and their impact on the final zero-shot classification accuracy. For example, experiments could be conducted with a constant learning rate, a step-wise decay schedule, or a cosine annealing schedule, and the results compared to the proposed method. This would help to understand whether the observed improvement is specific to the learning rate schedule used in the original CLIP training or a more general phenomenon. Additionally, the paper should provide a more detailed analysis of the training dynamics during the additional epochs. It would be useful to visualize the loss landscape and the movement of the model parameters to gain insights into why the model continues to improve after the learning rate has decayed to zero. This could involve techniques such as tracking the norm of the gradient or the distance between the model parameters at different epochs. 

Furthermore, the paper should expand the experimental evaluation to include a wider range of CLIP models and datasets. It is important to assess the generalizability of the proposed method to different model architectures, training datasets, and downstream tasks. For example, experiments could be conducted with CLIP models trained on larger datasets, such as LAION-400M or LAION-5B, and the results compared to the models trained on CC12M. Additionally, the paper should evaluate the performance of the method on other zero-shot classification benchmarks, such as ImageNet-V2, ImageNet-A, or ImageNet-R, to assess its robustness to distribution shifts. It would also be useful to explore the impact of different hyperparameters, such as the batch size, weight decay, and optimizer, on the performance of the method. This would help to identify the optimal settings for the proposed method and to understand its sensitivity to different hyperparameter choices. 

Finally, the paper should provide a more theoretical justification for the observed improvement. While the empirical results are promising, it is important to understand why the model continues to improve after the learning rate has decayed to zero. One possible explanation is that the model is able to escape from a local minimum during the additional training epochs. Another possibility is that the model is able to learn more robust features during the additional training epochs. The paper should explore these possibilities and provide a more rigorous theoretical analysis of the proposed method. This could involve techniques such as analyzing the Hessian matrix of the loss function or studying the convergence properties of the optimization algorithm.

### Questions

1. What is the effect of the proposed method on CLIP models trained on larger datasets, such as LAION-400M or LAION-5B?
2. What is the effect of the proposed method on other zero-shot classification benchmarks, such as ImageNet-V2, ImageNet-A, or ImageNet-R?
3. What is the effect of the proposed method on other downstream tasks, such as image retrieval or image captioning?

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
