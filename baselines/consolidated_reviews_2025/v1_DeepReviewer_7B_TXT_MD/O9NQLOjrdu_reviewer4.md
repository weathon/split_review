### Summary

This paper proposes a simple yet effective method for zero-shot image classification. The method leverages a multimodal large language model (LLM) to generate textual descriptions of input images and combines these descriptions with initial class predictions to improve classification accuracy. The approach is straightforward, requires no dataset-specific tuning, and achieves state-of-the-art results on multiple datasets.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The proposed method is simple and easy to implement, requiring no dataset-specific tuning.
2. The method achieves state-of-the-art results on multiple datasets, demonstrating its effectiveness and potential for practical applications.
3. The paper is well-written and easy to follow.

### Weaknesses

#### Some Related Works


#### comment

1. The method relies on a powerful multimodal LLM, which may limit its applicability in resource-constrained environments.
2. The method does not consider the uncertainty of the LLM's predictions, which may lead to incorrect classifications.
3. The method does not consider the diversity of the generated descriptions, which may lead to redundant information.

### Suggestions

The paper introduces an interesting approach by leveraging a multimodal LLM for zero-shot image classification, but there are several areas where the methodology could be strengthened. First, while the simplicity of the approach is a strength, the reliance on a powerful LLM raises concerns about computational cost and accessibility. Future work should explore methods to reduce the computational burden, such as using smaller, more efficient LLMs or employing techniques like knowledge distillation to transfer the knowledge of the LLM to a less resource-intensive model. This would make the method more practical for deployment in resource-constrained environments. Additionally, the paper should investigate the impact of different LLM architectures and sizes on the overall performance, providing a more comprehensive understanding of the method's sensitivity to the underlying LLM.

Second, the method's lack of consideration for the uncertainty in LLM predictions is a significant limitation. While the paper combines initial class predictions with LLM-generated descriptions, it does not explicitly address the confidence or uncertainty associated with the LLM's outputs. This could lead to incorrect classifications if the LLM is overconfident or provides misleading descriptions. Future work should explore methods to quantify and incorporate the uncertainty of the LLM's predictions into the classification process. This could involve using techniques such as Bayesian neural networks or ensemble methods to estimate the confidence of the LLM's outputs. Furthermore, the paper should investigate how the uncertainty of the LLM's predictions affects the overall classification performance and explore strategies to mitigate the impact of high-confidence but incorrect LLM outputs.

Finally, the paper does not adequately address the potential redundancy in the generated descriptions. While the method combines multiple descriptions, it does not explicitly consider the diversity of these descriptions. If the LLM generates highly similar descriptions for different images, the method may not benefit from the additional information. Future work should explore methods to encourage the generation of diverse and informative descriptions. This could involve using techniques such as contrastive learning or diversity-promoting loss functions during the training of the LLM. Additionally, the paper should investigate the impact of different prompting strategies on the diversity and informativeness of the generated descriptions and how this affects the overall classification performance. A more thorough analysis of the generated descriptions, including their semantic content and diversity, would strengthen the paper's findings.

### Questions

1. How does the proposed method perform on datasets with highly complex or ambiguous images where textual descriptions may not be easily generated?
2. What is the computational cost of using large language models (LLMs) for generating textual descriptions of images, and how does this scale with the size of the dataset?
3. How sensitive is the proposed method to the choice of LLM or the specific prompt design used for generating textual descriptions?

### Rating

6

### Confidence

4

**********
