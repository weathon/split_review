### Summary

This paper proposes a method to improve the zero-shot performance of vision-language models (VLMs) by tuning the weights of prompt templates for each image. The method, called AutoCLIP, uses a single step of gradient ascent to optimize the weights of the prompt templates based on the similarity between the class descriptors and the image embedding. The authors show that AutoCLIP improves the performance of zero-shot classifiers across a range of datasets, VLMs, and prompt templates, with an average improvement of 0.45 percentage points in accuracy. The method is fully unsupervised, has minimal additional computation overhead, and can be easily implemented in a few lines of code.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper introduces a novel method, AutoCLIP, for improving the zero-shot performance of vision-language models. The method is fully unsupervised, has minimal additional computation overhead, and can be easily implemented in a few lines of code.
2. The paper provides a comprehensive evaluation of AutoCLIP across a range of datasets, VLMs, and prompt templates. The results show that AutoCLIP improves the performance of zero-shot classifiers on the vast majority of settings, with an average improvement of 0.45 percentage points in accuracy.
3. The paper is well-written and easy to understand. The authors provide a clear explanation of the method and the experimental setup. The results are presented in a clear and concise manner, and the paper is well-organized.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational cost of AutoCLIP. While the authors claim that the method has minimal additional computation overhead, it would be helpful to provide a quantitative analysis of the runtime and memory usage of the method.
2. The paper does not explore the potential of combining AutoCLIP with other methods for improving zero-shot performance, such as prompt ensembling or knowledge distillation. It would be interesting to see if combining AutoCLIP with other methods can lead to further improvements in performance.

### Suggestions

The paper would benefit from a more thorough analysis of the computational overhead introduced by AutoCLIP. While the authors mention minimal overhead, a quantitative analysis is crucial for practical applications. Specifically, the paper should include a breakdown of the time spent on each step of the AutoCLIP process, such as the gradient ascent optimization and the similarity calculations. This analysis should be performed on different hardware configurations and with varying input image sizes to provide a comprehensive understanding of the method's scalability. Furthermore, the memory footprint of the method should be analyzed, especially when dealing with large batch sizes or high-resolution images. This would allow readers to assess the feasibility of using AutoCLIP in resource-constrained environments. A comparison with the computational cost of other zero-shot classification methods would also be valuable.

Exploring the combination of AutoCLIP with other techniques could significantly enhance the paper's impact. For instance, the authors could investigate how AutoCLIP interacts with prompt ensembling methods, where multiple prompts are used to improve the robustness of zero-shot classification. It would be interesting to see if AutoCLIP can be used to dynamically select or weight the prompts in an ensemble, potentially leading to further performance gains. Similarly, the authors could explore the potential of combining AutoCLIP with knowledge distillation techniques, where a larger, more complex model is used to train a smaller, more efficient model. This could lead to a more efficient zero-shot classification method that retains the performance benefits of AutoCLIP. The paper should also discuss the potential challenges and limitations of combining AutoCLIP with these other methods.

Finally, the paper should delve deeper into the theoretical underpinnings of AutoCLIP. While the empirical results are promising, a more rigorous analysis of why the method works would be beneficial. For example, the authors could investigate the relationship between the optimized prompt weights and the underlying feature representations learned by the vision-language model. This could provide insights into the types of images and classes for which AutoCLIP is most effective. Furthermore, the authors could explore the sensitivity of AutoCLIP to the choice of optimization parameters, such as the learning rate and the number of gradient ascent steps. A more thorough theoretical analysis would strengthen the paper's contribution and provide a deeper understanding of the method's behavior.

### Questions

1. Can you provide a more detailed analysis of the computational cost of AutoCLIP, including the runtime and memory usage of the method?
2. Have you explored the potential of combining AutoCLIP with other methods for improving zero-shot performance, such as prompt ensembling or knowledge distillation? If so, what were the results?
3. Can you provide a more detailed analysis of the cases where AutoCLIP does not improve performance? What are the common characteristics of these cases, and what are the potential reasons for the lack of improvement?

### Rating

8: accept, good paper

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
