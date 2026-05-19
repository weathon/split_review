### Summary

This paper proposes a method to improve zero-shot classification by assigning different weights to different prompts for a given image. The weights are optimized to maximize the similarity between the image and the prompts in the embedding space. The method is evaluated on various image classification datasets and with different vision-language models. The results show that the proposed method improves the zero-shot classification accuracy.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The proposed method is simple and easy to implement, and it does not require additional training or fine-tuning of the vision-language model.

- The evaluation is comprehensive, covering various datasets and vision-language models. The ablation study provides insights into the impact of different components of the method.

- The paper is well-written and easy to follow.

### Weaknesses

#### Some Related Works


#### comment

 - The improvement in accuracy is marginal, and in some cases, the proposed method performs worse than the baseline.

- The method requires per-image optimization of the weights, which may be computationally expensive, especially for large-scale datasets.

- The method is only evaluated on image classification tasks, and it is unclear how it would perform on other vision-language tasks, such as visual question answering or image captioning.

### Suggestions

The paper's primary weakness lies in the marginal improvements achieved over baseline methods. While the simplicity of the approach is appealing, the practical significance of the reported gains is questionable. The authors should consider exploring more challenging datasets or tasks where the benefits of adaptive prompt weighting might be more pronounced. For instance, datasets with finer-grained categories or more ambiguous class descriptions could reveal the true potential of the proposed method. Furthermore, a more detailed analysis of the cases where the method fails to improve performance would be beneficial. Understanding the limitations of the approach is crucial for determining its applicability in real-world scenarios. The authors should also investigate the sensitivity of the method to the choice of optimization parameters and provide guidelines for selecting appropriate values for different datasets.

Another area for improvement is the computational cost associated with per-image optimization. Although the authors claim that the optimization is fast, the need to optimize weights for each image could become a bottleneck for large-scale applications. The authors should provide a more detailed analysis of the computational complexity of the optimization process and compare it with the computational cost of other zero-shot classification methods. It would also be helpful to explore techniques for reducing the computational overhead, such as using a simplified optimization procedure or caching the optimized weights for similar images. The authors should also discuss the memory requirements of the method, especially when dealing with large datasets.

Finally, the evaluation of the method is limited to image classification tasks. While image classification is a fundamental vision-language task, the method's applicability to other vision-language tasks, such as visual question answering or image captioning, remains unclear. The authors should consider extending their evaluation to these tasks to demonstrate the versatility of their approach. For example, in visual question answering, the method could be used to weight prompts that generate answers, and in image captioning, it could be used to weight prompts that generate descriptions. The authors should also discuss the challenges of applying their method to these tasks and propose potential solutions.

### Questions

- How does the proposed method compare to other methods that use prompt tuning or meta-learning for zero-shot classification?

- What is the computational cost of the proposed method compared to other zero-shot classification methods?

- How does the method perform on datasets with more complex or ambiguous class descriptions?

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
