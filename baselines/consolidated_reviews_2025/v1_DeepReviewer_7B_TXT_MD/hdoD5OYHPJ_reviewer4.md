### Summary

This paper proposes AutoCLIP, a method for auto-tuning zero-shot classifiers. The authors propose to use a set of prompt templates to compute the class embeddings and then use a weighted average of the class embeddings to compute the image embeddings. The weights are computed using a gradient ascent step on the similarity between the image and the class embeddings. The authors show that this method improves the performance of the zero-shot classifiers.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The idea is simple and easy to understand.
- The method is evaluated on a variety of datasets and models and shows improvement over the baseline.
- The method is efficient and does not require any additional training or inference overhead.

### Weaknesses

#### Some Related Works


#### comment

 - The method requires per-sample optimization, which can be computationally expensive for large-scale datasets.
- The method is only evaluated on image classification tasks, and it is unclear how it would perform on other vision-language tasks, such as visual question answering or image captioning.

### Suggestions

The per-sample optimization is a significant limitation that needs to be addressed. While the authors claim the method is efficient, the per-image optimization step could still be a bottleneck for very large datasets. It would be beneficial to explore techniques to reduce the computational cost of this step. For example, the authors could investigate methods to approximate the gradient ascent or use a more efficient optimization algorithm. Furthermore, the authors should provide a more detailed analysis of the computational cost of their method, including the time and memory requirements for different dataset sizes and model complexities. This would help to better understand the scalability of the proposed approach.

Another limitation is the lack of evaluation on other vision-language tasks. While image classification is a fundamental task, it is important to demonstrate the generalizability of the proposed method to other tasks. The authors should consider evaluating their method on tasks such as visual question answering (VQA) or image captioning. These tasks would provide a more comprehensive assessment of the method's capabilities and limitations. For VQA, the method could be used to weight prompts that generate answers, and the performance could be measured by the accuracy of selecting the correct answer. For image captioning, the method could be used to weight prompts that generate descriptions, and the performance could be measured by metrics such as BLEU or CIDEr. This would provide a more complete picture of the method's potential impact.

Finally, the authors should provide a more detailed analysis of the impact of different prompt templates on the performance of the method. While the authors mention using a set of prompt templates, they do not provide a detailed analysis of how the choice of templates affects the results. It would be beneficial to explore different types of prompt templates and analyze their impact on the performance of the method. This could help to identify the most effective prompt templates for different tasks and datasets. Furthermore, the authors should investigate the sensitivity of the method to the number of prompt templates used. It would be interesting to see how the performance of the method changes as the number of templates increases or decreases.

### Questions

- How does the method perform on datasets with more complex or ambiguous class descriptions?
- How does the method compare to other prompt tuning methods, such as those that use gradient-based optimization or reinforcement learning?
- What are the limitations of the proposed method, and in what scenarios does it not perform well?

### Rating

8: accept, good paper

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
