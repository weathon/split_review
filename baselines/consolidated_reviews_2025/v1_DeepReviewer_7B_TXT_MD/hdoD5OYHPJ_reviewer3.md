### Summary

This paper proposes a method for automatic prompt weighting for zero-shot classification. The method is based on the observation that the similarity between an image and a class descriptor determines how the class descriptor should be weighted. The method is evaluated on a variety of vision-language models and datasets, and the results show that the method improves the performance of the zero-shot classification.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The method is simple and easy to implement.
2. The method is evaluated on a variety of vision-language models and datasets, and the results show that the method improves the performance of the zero-shot classification.
3. The method is evaluated on a variety of vision-language models and datasets, and the results show that the method improves the performance of the zero-shot classification.

### Weaknesses

#### Some Related Works


#### comment

1. The method is only evaluated on image classification tasks, and it is unclear how it would perform on other vision-language tasks, such as visual question answering or image captioning.
2. The method requires per-image optimization of the weights, which may be computationally expensive, especially for large-scale datasets.
3. The paper does not provide a detailed analysis of the cases where the method fails to improve performance.

### Suggestions

The paper introduces an interesting approach to zero-shot classification by dynamically weighting prompt templates based on image-text similarity. However, the evaluation is limited to image classification, and it is unclear how the method would perform on other vision-language tasks such as visual question answering (VQA) or image captioning. For VQA, the method could be applied to weight prompts that generate answers, but the evaluation would require a more complex setup with multiple possible answers and a mechanism to determine the correct one. Similarly, for image captioning, the method could be used to weight prompts that generate descriptions, but the evaluation would require a metric that measures the similarity between the generated caption and the ground truth caption. The paper should include experiments on these tasks to demonstrate the generalizability of the proposed method. Furthermore, the paper should provide a more detailed analysis of the computational cost of the per-image optimization, especially for large-scale datasets. The current analysis is limited to a few datasets, and it is unclear how the method would scale to larger datasets. The paper should also provide a more detailed analysis of the cases where the method fails to improve performance. It is important to understand the limitations of the method and the scenarios where it is not effective. This analysis should include a discussion of the types of images and prompts where the method struggles, and it should provide insights into how the method could be improved.

To address the limitations, the authors should consider expanding the evaluation to include VQA and image captioning tasks. For VQA, the method could be applied to weight prompts that generate answers, and the evaluation could involve a multiple-choice setup with several candidate answers. The performance could be measured by the accuracy of selecting the correct answer. For image captioning, the method could be used to weight prompts that generate descriptions, and the evaluation could involve a metric that measures the similarity between the generated caption and the ground truth caption, such as BLEU or CIDEr. This would provide a more comprehensive assessment of the method's capabilities and limitations. Additionally, the authors should investigate the computational cost of the per-image optimization, especially for large-scale datasets. This could involve profiling the code to identify the most time-consuming operations and exploring techniques to optimize the implementation. The authors should also provide a more detailed analysis of the cases where the method fails to improve performance. This analysis should include a discussion of the types of images and prompts where the method struggles, and it should provide insights into how the method could be improved. For example, it would be useful to know if the method performs worse on images with complex scenes or prompts that are semantically ambiguous.

Finally, the authors should consider comparing their method with other prompt tuning methods, such as those that use gradient-based optimization or reinforcement learning. This would provide a more comprehensive assessment of the method's performance and its advantages and disadvantages compared to other approaches. The comparison should include a detailed analysis of the performance of each method on different datasets and vision-language models. This would help to identify the strengths and weaknesses of the proposed method and provide a better understanding of its potential impact. The authors should also consider exploring the use of more sophisticated similarity metrics beyond cosine similarity. While cosine similarity is a common metric, there may be other metrics that are better suited for specific tasks or datasets. For example, metrics that take into account the semantic meaning of the text embeddings or the visual features of the images could be explored. This could potentially lead to further improvements in the performance of the method.

### Questions

1. How does the method perform on datasets with more complex or ambiguous class descriptions?
2. How does the method compare to other prompt tuning methods, such as those that use gradient-based optimization or reinforcement learning?
3. What are the limitations of the proposed method, and in what scenarios does it not perform well?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
