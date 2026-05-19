### Summary

This paper proposes a method to improve zero-shot classification by assigning different weights to different prompt templates for each image. The weights are determined by the cosine similarity between the image and the class descriptor embeddings. The proposed method is evaluated on various vision-language models and datasets, demonstrating its effectiveness in improving zero-shot classification performance.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The proposed method is simple and easy to implement, requiring only a few lines of code.
2. The method is evaluated on various vision-language models and datasets, demonstrating its effectiveness in improving zero-shot classification performance.
3. The paper is well-written and easy to follow.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method is only evaluated on image classification tasks, and it is unclear how it would perform on other vision-language tasks, such as visual question answering or image captioning.
2. The method requires per-image optimization of the weights, which may be computationally expensive, especially for large-scale datasets.
3. The paper does not provide a detailed analysis of the cases where the method fails to improve performance.

### Suggestions

The paper introduces an interesting approach to zero-shot classification by dynamically weighting prompt templates based on image-text similarity. However, the evaluation is limited to image classification, and it is unclear how the method would perform on other vision-language tasks such as visual question answering (VQA) or image captioning. For VQA, the method could be applied to weight prompts that generate answers, but the evaluation would require a more complex setup with multiple possible answers and a mechanism to determine the correct one. Similarly, for image captioning, the method could be used to weight prompts that generate descriptions, but the evaluation would require a metric that measures the similarity between the generated caption and the ground truth caption. The paper should include experiments on these tasks to demonstrate the generalizability of the proposed method. Furthermore, the paper should provide a more detailed analysis of the computational cost of the per-image optimization, especially for large-scale datasets. The current analysis is limited to a few datasets, and it is unclear how the method would scale to larger datasets. The paper should also provide a more detailed analysis of the cases where the method fails to improve performance. It is important to understand the limitations of the method and the scenarios where it is not effective. This analysis should include a discussion of the types of images and prompts where the method struggles, and it should provide insights into how the method could be improved.

To improve the paper, the authors should consider the following: First, expand the evaluation to include VQA and image captioning tasks. This would provide a more comprehensive assessment of the method's capabilities and limitations. Second, provide a more detailed analysis of the computational cost of the per-image optimization, especially for large-scale datasets. This analysis should include a comparison with other zero-shot classification methods. Third, provide a more detailed analysis of the cases where the method fails to improve performance. This analysis should include a discussion of the types of images and prompts where the method struggles, and it should provide insights into how the method could be improved. Finally, the authors should consider comparing their method with other prompt tuning methods, such as those that use gradient-based optimization or reinforcement learning. This would provide a more comprehensive assessment of the method's performance and its advantages and disadvantages compared to other approaches.

### Questions

1. How does the proposed method compare to other prompt tuning methods, such as those that use gradient-based optimization or reinforcement learning?
2. What are the limitations of the proposed method, and in what scenarios does it not perform well?
3. How does the method perform on datasets with more complex or ambiguous class descriptions?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
