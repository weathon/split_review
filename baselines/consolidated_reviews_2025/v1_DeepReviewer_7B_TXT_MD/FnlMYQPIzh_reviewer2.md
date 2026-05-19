### Summary

This paper proposes a novel framework called ConvINT, which aims to enhance the understanding of user intentions by organizing them into four key aspects: situation, emotion, action, and knowledge. The authors introduce a Weakly-supervised Reinforced Generation (WeRG) method to efficiently expand the ConvINT annotated dataset. The WeRG method combines coarse-to-fine labels to improve the quality and scalability of ConvINT annotations. Experimental results demonstrate that integrating ConvINT with WeRG significantly improves downstream tasks, such as response generation and task completion, highlighting the framework’s potential as a comprehensive solution for conversational AI.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-structured and easy to follow.
2. The motivation behind the ConvINT framework is well-articulated, addressing the limitations of existing structured methods in capturing the complexity of user intentions.
3. The WeRG method effectively leverages weak supervision to expand ConvINT annotations, making the approach scalable and practical for real-world applications.

### Weaknesses

#### Some Related Works


#### comment

1. The novelty of the proposed method is limited. The paper primarily combines existing techniques, such as structured output prediction and weak supervision, without introducing fundamentally new approaches to conversational understanding or weakly supervised learning. The core idea of using a four-aspect framework is not novel, and the application of weak reinforcement learning for data expansion, while practical, does not represent a significant conceptual leap. The paper lacks a clear explanation of how the specific combination of these techniques leads to a substantial improvement over existing methods.
2. The paper lacks a detailed comparison with other conversational understanding frameworks, particularly those that also use structured output prediction or weak supervision. This makes it difficult to assess the relative advantages and disadvantages of the proposed approach. The paper does not adequately discuss how the proposed method compares to existing techniques in terms of performance, computational cost, and scalability. A more thorough comparison is needed to contextualize the contributions of this work.
3. The paper does not provide a comprehensive analysis of the computational cost and efficiency of the WeRG method, which is crucial for practical applications. The paper should include a detailed analysis of the time and memory requirements of the proposed method, as well as a comparison with other methods in terms of computational efficiency. This analysis should include metrics such as training time, inference time, and memory usage. The lack of such analysis makes it difficult to assess the practical viability of the proposed method.
4. The paper lacks a thorough discussion of the limitations of the WeRG method and potential areas for future research. The paper should include a more detailed discussion of the potential biases in the weak supervision signals and how these biases might affect the performance of the proposed method. Additionally, the paper should discuss potential areas for future research, such as exploring alternative weak supervision techniques or incorporating more sophisticated models for conversational understanding.

### Suggestions

The paper would benefit from a more detailed explanation of the specific mechanisms by which the WeRG method leverages weak supervision to expand the ConvINT annotations. The authors should provide a more in-depth analysis of how the coarse-to-fine labeling process is implemented and how it contributes to the overall quality of the annotations. For example, the paper could include a discussion of the specific criteria used to determine the coarse-level labels, the mid-level labels, and the fine-level labels. Furthermore, the paper should provide a more detailed explanation of the reward function used in the reinforcement learning process, including the specific metrics used to evaluate the quality of the generated annotations. This would help to clarify the technical details of the proposed method and make it easier for other researchers to reproduce the results.

To address the lack of comparison with other conversational understanding frameworks, the authors should include a more comprehensive analysis of the performance of the proposed method in comparison to existing techniques. This analysis should include a comparison of the performance of the proposed method on a variety of benchmark datasets, as well as a comparison of the computational cost and scalability of the proposed method with other techniques. The paper should also include a discussion of the limitations of the proposed method and how these limitations might be addressed in future work. For example, the paper could discuss the potential biases in the weak supervision signals and how these biases might affect the performance of the proposed method. The authors should also discuss the potential for the proposed method to be applied to other types of conversational tasks, such as dialogue summarization or dialogue generation.

Finally, the paper should include a more detailed analysis of the computational cost and efficiency of the WeRG method. This analysis should include a breakdown of the time and memory requirements of the proposed method, as well as a comparison with other methods in terms of computational efficiency. The paper should also discuss the potential for parallelization and other optimization techniques to improve the efficiency of the proposed method. The authors should also discuss the potential for the proposed method to be applied to large-scale datasets, and how the computational cost of the method might scale with the size of the dataset. This analysis would help to assess the practical viability of the proposed method and make it easier for other researchers to apply the method to their own problems.

### Questions

1. How does the WeRG method ensure the quality of the weak supervision signals, especially when dealing with noisy or ambiguous data?
2. What are the specific computational costs associated with the WeRG method, and how does it compare to other weakly supervised learning approaches?
3. How does the ConvINT framework handle cases where user intentions are ambiguous or contradictory, and what mechanisms are in place to resolve such conflicts?

### Rating

5

### Confidence

4

**********
