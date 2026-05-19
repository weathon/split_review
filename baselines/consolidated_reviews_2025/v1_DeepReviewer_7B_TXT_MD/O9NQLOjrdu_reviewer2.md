### Summary

This paper proposes a simple method for zero-shot image classification. The method leverages a multimodal LLM to generate textual descriptions of the input image and uses these descriptions to enhance the classification process. The method is simple and effective, and the experimental results show that it achieves state-of-the-art performance on several datasets.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow.
2. The method is simple and effective, and the experimental results show that it achieves state-of-the-art performance on several datasets.
3. The method is easy to implement and can be used in real-world applications.

### Weaknesses

#### Some Related Works


#### comment

1. The method relies on a powerful multimodal LLM, which may limit its applicability in resource-constrained environments.
2. The method does not consider the uncertainty of the LLM's predictions, which may lead to incorrect classifications.
3. The method does not consider the diversity of the generated descriptions, which may lead to redundant information.

### Suggestions

The paper should explore methods to reduce the computational cost of the proposed approach, especially when using large multimodal LLMs. One potential direction is to investigate techniques for distilling the knowledge from the large LLM into a smaller, more efficient model. This could involve methods like knowledge distillation or pruning, which have been successfully applied in other areas of deep learning. Another approach could be to explore more efficient LLMs that are specifically designed for text generation tasks, potentially leading to a better trade-off between performance and computational cost. Furthermore, the paper should investigate the impact of different LLM architectures and sizes on the overall performance of the proposed method, providing a more comprehensive understanding of the method's sensitivity to the underlying LLM.

To address the issue of uncertainty in LLM predictions, the paper could explore methods for incorporating uncertainty estimates into the classification process. This could involve using techniques such as Bayesian neural networks or ensemble methods to quantify the uncertainty of the LLM's predictions. The uncertainty estimates could then be used to weight the different input features, giving more importance to features with higher confidence. Additionally, the paper could investigate methods for generating multiple diverse descriptions of the input image, which could help to mitigate the impact of any single, potentially inaccurate, description. This could involve using techniques such as beam search or nucleus sampling to generate a set of diverse text descriptions, which could then be used as input features for the classification model.

Finally, the paper should investigate methods for selecting the most informative descriptions to use as input features. The current approach of using all generated descriptions may lead to redundant information, which could negatively impact the classification performance. One potential approach is to use a feature selection method, such as mutual information or correlation analysis, to identify the most informative descriptions. Another approach is to use a ranking method to prioritize the descriptions based on their relevance to the input image. This would allow the model to focus on the most relevant information, potentially improving the overall performance and reducing computational cost.

### Questions

1. How does the method perform on datasets with highly ambiguous or complex images where textual descriptions may not be easily generated?
2. What is the computational cost of using multimodal LLMs for each image, and how does this scale with the size of the dataset?
3. How sensitive is the method to the choice of LLM or the specific prompt design used for generating textual descriptions?

### Rating

5

### Confidence

4

**********
