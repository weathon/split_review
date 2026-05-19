### Summary

This paper proposes a novel approach to improve the performance of Vision Language Models (VLMs) on downstream tasks. The authors identify a critical issue with existing methods that use a single embedding for each class, which fails to capture the visual variance within a class. To address this, they introduce Adaptive Prompt Prototype Learning (APPLe), which builds multiple prompts as class prototypes to cover the visual variance. Additionally, an adaptive attention mechanism is designed to weigh the importance of different prototypes, assigning higher scores to representative prototypes and lower scores to less representative ones. The effectiveness of APPLe is evaluated on three representative tasks: generalization to unseen classes, new target datasets, and unseen domain shifts. The results show a consistent performance improvement of 3.66% on new classes and 2.79% on the harmonic mean.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is simple yet effective, achieving consistent performance improvements across various datasets and tasks.
3. The authors provide a comprehensive experimental evaluation, demonstrating the effectiveness of their approach on different tasks and datasets.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method requires fine-tuning new prototypes to optimize performance when adapting to certain new classes, which may limit its applicability in real-world scenarios.
2. The effectiveness of the method is significantly tethered to the quality of the prompts, as the prototypes may contain flawed keywords that can lead to ambiguous decisions.

### Suggestions

The paper introduces an interesting approach to address the limitations of single-embedding class representations in Vision Language Models (VLMs) by using multiple prompts as class prototypes. However, the reliance on fine-tuning these prototypes for new classes presents a practical challenge. While the authors demonstrate improvements on several benchmarks, the need for fine-tuning could hinder the method's applicability in scenarios where labeled data for new classes is scarce or unavailable. Future work should explore methods to generate more robust and generalizable prototypes that require minimal or no fine-tuning for new classes. This could involve techniques such as meta-learning or leveraging large language models to generate more diverse and representative prompts. Furthermore, the computational cost associated with fine-tuning multiple prototypes should be thoroughly analyzed and compared to existing methods.

Another area for improvement is the sensitivity of the method to prompt quality. The paper acknowledges that flawed keywords in prototypes can lead to ambiguous decisions, but it does not provide a detailed analysis of how to mitigate this issue. The authors should investigate methods for automatically evaluating and filtering out low-quality prompts. This could involve using techniques such as prompt ensembling or incorporating uncertainty estimates into the prototype selection process. Additionally, exploring the use of more sophisticated prompt generation techniques, beyond simple keyword replacement, could lead to more robust and reliable prototypes. For example, using large language models to generate more semantically rich and diverse prompts could improve the overall performance and reduce the impact of individual flawed keywords.

Finally, while the paper presents a comprehensive experimental evaluation, it would be beneficial to include a more detailed analysis of the method's performance on different types of visual variance. For example, how does the method perform when the visual variance is due to changes in lighting, viewpoint, or background? Understanding the method's strengths and weaknesses in different scenarios would provide a more complete picture of its capabilities and limitations. Furthermore, it would be valuable to compare the proposed method with other techniques that aim to address the same problem, such as methods that use multiple visual embeddings or attention mechanisms to capture visual variance. This would help to better position the proposed method within the existing literature and highlight its unique contributions.

### Questions

Please refer to the weakness.

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
