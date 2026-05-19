### Summary

The paper proposes a novel gradient regularization-based cross-prompt attack method for vision-language models (VLMs). The authors identify the non-stationary phenomenon in the optimization process of VLMs and propose a gradient regularization method to improve the transferability of adversarial attacks. The paper provides extensive experiments on models such as Flamingo, BLIP-2, LLaVA-1.5, and InstructBLIP, demonstrating the effectiveness of the proposed method in enhancing the transferability of adversarial attacks across different prompts.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow. The authors clearly present their ideas and methods, making it easy for readers to understand the proposed approach.
2. The authors conduct extensive experiments on multiple models and tasks, demonstrating the effectiveness of the proposed method in enhancing the transferability of adversarial attacks across different prompts.
3. The authors provide a detailed analysis of the experimental results, including the impact of the number of prompts on attack performance, the convergence of the proposed method, and the transferability of adversarial examples.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed discussion on the limitations of the proposed method and potential future directions. While the authors demonstrate the effectiveness of their method, they do not address potential weaknesses or scenarios where the method may not perform optimally. For example, the paper does not discuss the computational cost of the gradient regularization, especially when applied to large-scale models, or the sensitivity of the method to the choice of regularization parameters. Furthermore, the paper does not explore the potential for the method to be circumvented by adaptive defenses.
2. The paper could benefit from a more comprehensive comparison with existing adversarial attack methods for VLMs. While the authors compare their method with some baselines, they do not provide a detailed analysis of the differences and similarities between their method and other state-of-the-art approaches. For instance, the paper does not compare against methods that use different optimization strategies or those that focus on specific types of adversarial examples. A more thorough comparison would help to better contextualize the contributions of the proposed method and highlight its advantages and disadvantages compared to existing approaches.

### Suggestions

The authors should provide a more in-depth analysis of the limitations of their proposed gradient regularization method. Specifically, they should investigate the computational overhead associated with the regularization, especially when applied to large vision-language models. This analysis should include a breakdown of the time and memory requirements for different components of the method, such as the gradient calculation and the regularization step. Furthermore, the authors should explore the sensitivity of the method to the choice of regularization parameters, such as the regularization strength and the frequency of regularization. A detailed sensitivity analysis would help to understand the robustness of the method and provide guidance on how to choose appropriate parameter values for different scenarios. The authors should also discuss the potential for the method to be circumvented by adaptive defenses, and propose strategies to mitigate these risks. This could include exploring techniques such as adversarial training or defensive distillation.

To strengthen the paper, the authors should conduct a more comprehensive comparison with existing adversarial attack methods for vision-language models. This comparison should not only focus on the performance of the methods but also on their computational cost, robustness, and transferability. The authors should compare their method with a wider range of baselines, including methods that use different optimization strategies, such as gradient-based or gradient-free methods. They should also compare against methods that focus on specific types of adversarial examples, such as those that are designed to fool the model on specific tasks or with specific input types. This comparison should be done on a variety of datasets and model architectures to provide a more comprehensive evaluation of the proposed method. The authors should also discuss the advantages and disadvantages of their method compared to existing approaches, highlighting the specific scenarios where their method is most effective.

Finally, the authors should provide a more detailed discussion of the potential future directions for their research. This could include exploring the application of their method to other types of vision-language models, such as those that are trained on different datasets or with different architectures. They could also investigate the use of their method for other tasks, such as image captioning or visual question answering. The authors should also consider exploring the use of more advanced regularization techniques, such as adaptive regularization or regularization based on the geometry of the loss landscape. Furthermore, the authors should discuss the potential for combining their method with other techniques, such as adversarial training or defensive distillation, to further improve the robustness of vision-language models.

### Questions

1. How does the proposed method perform on other vision-language models, such as those trained on different datasets or with different architectures?
2. How does the proposed method compare to other state-of-the-art adversarial attack methods for VLMs, in terms of performance, computational cost, and transferability?
3. What are the potential limitations of the proposed method, and how can they be addressed in future work?

### Rating

6

### Confidence

3

**********
