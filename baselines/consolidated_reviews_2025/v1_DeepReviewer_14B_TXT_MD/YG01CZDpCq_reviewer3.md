### Summary

This paper proposes Adaptive Prompt Prototype Learning (APPLe), which introduces multiple prompts as class prototypes to enhance zero-shot CLIP performance. The authors design an adaptive attention mechanism to assign higher confidence to accurate prototypes and introduce a decorrelation loss to suppress the co-occurrence of multiple confident prototypes. The method demonstrates consistent performance gains across various datasets and tasks.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The motivation is clear and the proposed method is simple yet effective.
3. The experiments are comprehensive, and the results are convincing.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method requires fine-tuning new prototypes to optimize performance when adapting to certain new classes, which may limit its applicability in real-world scenarios. The need to retrain or fine-tune the prototype embeddings for each new class introduces a significant computational overhead and dependency on labeled data, which is a major limitation for zero-shot learning scenarios. This fine-tuning process also makes the method less practical for large-scale applications where new classes are frequently encountered.
2. The effectiveness of the method is significantly tethered to the quality of the prompts, as the prototypes may contain flawed keywords that can lead to ambiguous decisions. The reliance on GPT-3 generated prompts, while diverse, introduces a potential bottleneck. If the generated prompts are not semantically representative of the class or contain noisy keywords, the performance of the method will be negatively impacted. This dependence on the quality of the prompts makes the method less robust and reliable.

### Suggestions

The authors should investigate methods to reduce the reliance on fine-tuning the prototype embeddings for new classes. One potential approach could be to explore techniques for generating more robust and generalizable prototypes that can adapt to new classes without requiring extensive retraining. This could involve incorporating techniques from meta-learning or few-shot learning to enable the model to quickly adapt to new classes with minimal fine-tuning. Another direction could be to explore methods for learning disentangled representations of the prompts, which could allow the model to focus on the most relevant aspects of the prompts and ignore noisy or irrelevant keywords. This could improve the robustness of the method to variations in prompt quality.

To address the issue of prompt quality, the authors should explore methods for automatically evaluating and filtering the generated prompts. This could involve using a separate model to assess the semantic relevance of the prompts to the target classes and filtering out prompts that are not semantically aligned. Another approach could be to use a combination of different prompt generation techniques and select the best prompts based on their performance on a validation set. Furthermore, the authors could investigate methods for incorporating uncertainty into the prompt representations, which could allow the model to be more robust to noisy or ambiguous prompts. This could involve using techniques such as Bayesian neural networks or Monte Carlo dropout to model the uncertainty in the prompt embeddings.

Finally, the authors should provide a more detailed analysis of the computational cost of their method, including the time and memory requirements for fine-tuning the prototypes and generating the prompts. This analysis should compare the computational cost of their method to other state-of-the-art methods and should provide insights into the scalability of the method for large-scale applications. The authors should also investigate methods for reducing the computational cost of their method, such as using more efficient prompt generation techniques or using model compression techniques to reduce the size of the model.

### Questions

1. How does the method handle cases where the visual features of a class are highly diverse and do not align well with any single prototype?
2. How does the method perform when the quality of the prompts is poor or when there is a high degree of ambiguity in the prompts?

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
