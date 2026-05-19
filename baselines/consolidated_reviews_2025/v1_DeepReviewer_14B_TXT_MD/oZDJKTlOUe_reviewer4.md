### Summary

The paper introduces LVLM Hallucination Revisor (LURE), a post-hoc method to reduce object hallucination in large vision-language models (LVLMs). LURE is based on a statistical analysis of the key factors contributing to object hallucination, including co-occurrence, uncertainty, and object position. The authors evaluate LURE on six open-source LVLMs and demonstrate its effectiveness in reducing object hallucination compared to existing methods. The results show that LURE outperforms the previous best approach in both general object hallucination evaluation metrics and human evaluations.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow. The authors provide a clear and concise explanation of the problem, their proposed solution, and the experimental results.
2. The authors conduct a comprehensive evaluation of LURE on six open-source LVLMs, demonstrating its effectiveness in reducing object hallucinations. The results show that LURE outperforms the previous best approach in both general object hallucination evaluation metrics and human evaluations.
3. The paper provides a theoretical explanation for the effectiveness of LURE, which helps to understand the underlying principles of the method.
4. The authors make their code and data publicly available, which promotes reproducibility and allows other researchers to build upon their work.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational cost of LURE. It would be helpful to understand the computational resources required to train and deploy the method, especially in comparison to other approaches. Specifically, the paper lacks information on the training time, inference time, and memory requirements for the hallucination revisor, making it difficult to assess the practical applicability of the method. A comparison of these metrics against the baseline methods would be crucial for a comprehensive evaluation.
2. The paper does not discuss the potential limitations of LURE. For example, it is not clear how the method would perform on more complex or ambiguous images, or how it would handle cases where the hallucinated objects are actually present in the image but are difficult to detect. The paper should also address the sensitivity of LURE to the quality of the initial captions, and whether the method can handle cases where the initial captions are already noisy or contain errors. Furthermore, the paper does not explore the potential for LURE to introduce new errors or biases during the hallucination mitigation process.

### Suggestions

The paper should include a detailed analysis of the computational cost associated with LURE. This analysis should include the training time, inference time, and memory requirements for the hallucination revisor. It would be beneficial to compare these metrics against the baseline methods to provide a clear understanding of the computational overhead introduced by LURE. For example, the authors could report the GPU hours required for training, the time taken to process a single image-text pair during inference, and the memory footprint of the model. This information is crucial for assessing the practical applicability of the method, especially in resource-constrained environments. Furthermore, the authors should investigate the scalability of LURE with respect to the size of the input images and the length of the text descriptions.

To address the limitations of LURE, the authors should conduct experiments on more complex and ambiguous images. This could involve using datasets that contain images with multiple objects, occlusions, or unusual viewpoints. The paper should also analyze the performance of LURE on images where the hallucinated objects are actually present but are difficult to detect. This could be achieved by creating a subset of the evaluation data where the ground truth contains objects that are often missed by object detectors. Additionally, the authors should investigate the sensitivity of LURE to the quality of the initial captions. This could be done by introducing noise into the initial captions and evaluating the performance of LURE under these conditions. The paper should also explore the potential for LURE to introduce new errors or biases during the hallucination mitigation process. This could be done by analyzing the types of errors introduced by LURE and comparing them to the original hallucinations.

Finally, the authors should consider exploring alternative methods for generating the hallucinatory descriptions used to train the revisor. While GPT-3.5 is a powerful language model, it may introduce biases or artifacts into the training data. Exploring other methods, such as using a combination of different language models or incorporating human-generated hallucinations, could potentially improve the robustness and generalizability of LURE. The authors should also investigate the impact of the size and diversity of the training data on the performance of LURE. It would be beneficial to explore whether increasing the size of the training data or using a more diverse set of images and captions can further improve the performance of the method.

### Questions

1. How does LURE perform on more complex or ambiguous images?
2. How does LURE handle cases where the hallucinated objects are actually present in the image but are difficult to detect?
3. How does the quality of the initial captions affect the performance of LURE?
4. Are there any potential limitations or drawbacks of LURE that the authors have not discussed in the paper?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
