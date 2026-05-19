### Summary

The paper introduces a synthetic graph navigation task as a framework for studying stepwise inference in transformers. The reasoning gap, diversity-accuracy tradeoff, and simplicity bias in stepwise inference are investigated through this framework. The paper also explores the model's navigation preferences and their controllability through in-context exemplars, and examines length generalization, and responses to longer contexts with conflicting exemplars.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

The paper presents a mechanistic understanding of stepwise inference in transformers, using a synthetic graph navigation task as a framework. The research methodology is well-designed and the results are clearly presented.

### Weaknesses

#### Some Related Works


#### comment

The paper's focus on a synthetic task may limit the generalizability of the findings to real-world scenarios. The paper primarily focuses on the mechanistic understanding of stepwise inference in transformers but does not extensively discuss the practical applications of the findings. The paper acknowledges that the model will fail to generalize to reasoning chains longer than those present in its training data, which is a limitation. The paper also notes that the model has a strong bias toward choosing a path defined by the first chain over the second, which is a limitation.

### Suggestions

The paper would benefit from a more thorough exploration of how the observed simplicity bias and primacy bias could be mitigated in practical applications. While the synthetic graph navigation task provides a controlled environment for studying stepwise inference, the identified biases could significantly hinder the performance of transformers in real-world tasks that require more complex reasoning. For instance, in tasks involving multi-hop reasoning or planning, the tendency to favor shorter paths or the first encountered solution could lead to suboptimal outcomes. The authors should consider investigating techniques such as training-based methods or prompt engineering to reduce the impact of these biases. This could involve incorporating specific training examples that explicitly demonstrate the need for longer or more complex reasoning chains, or designing prompts that encourage the model to explore multiple potential solutions before committing to one. Furthermore, the paper should discuss the potential trade-offs between mitigating these biases and other performance metrics, such as accuracy and efficiency.

To enhance the practical relevance of the study, the authors should consider extending their analysis to include more complex graph structures and navigation tasks. The current focus on relatively simple graph navigation scenarios may not fully capture the challenges encountered in real-world applications. For example, the authors could explore tasks that involve graphs with varying degrees of connectivity, cycles, or hierarchical structures. Additionally, the paper could investigate how the model's performance is affected by the presence of noisy or ambiguous information in the input data. This would provide a more comprehensive understanding of the model's limitations and its ability to generalize to diverse scenarios. The authors could also explore the use of more sophisticated evaluation metrics that capture the quality of the reasoning process, rather than just the correctness of the final answer. This could include metrics that measure the completeness of the explored paths or the efficiency of the navigation strategy.

Finally, the paper should delve deeper into the implications of the observed diversity-accuracy tradeoff for practical applications. While the tradeoff is an interesting finding, the paper does not fully explore how this tradeoff might affect the performance of transformers in different real-world scenarios. For example, in some applications, it may be more important to prioritize accuracy over diversity, while in others, the opposite may be true. The authors should consider investigating how the sampling temperature can be tuned to achieve the desired balance between diversity and accuracy for specific tasks. This could involve developing adaptive sampling strategies that dynamically adjust the temperature based on the characteristics of the input data or the desired outcome. Furthermore, the paper should discuss the potential limitations of using temperature tuning as the sole mechanism for controlling the diversity-accuracy tradeoff, and explore alternative approaches that may be more effective in certain contexts.

### Questions

How can the simplicity bias and primacy bias be mitigated in practical applications? Are there any training-based methods or prompt engineering techniques that can be used to reduce the impact of these biases?
How well do the findings from the synthetic graph navigation task generalize to other stepwise inference protocols and real-world tasks? Are there any plans to extend the study to include more complex graph structures and navigation tasks?

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
