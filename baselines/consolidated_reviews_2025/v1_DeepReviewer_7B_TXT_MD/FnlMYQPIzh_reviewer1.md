### Summary

This paper proposes a novel framework called ConvINT, which aims to enhance the understanding of user intentions by organizing them into four key aspects: situation, emotion, action, and knowledge. The authors introduce a Weakly-supervised Reinforced Generation (WeRG) method to efficiently expand the ConvINT annotated dataset. The WeRG method combines coarse-to-fine labels to improve the quality and scalability of ConvINT annotations. Experimental results demonstrate that integrating ConvINT with WeRG significantly improves downstream tasks, such as response generation and task completion, highlighting the framework’s potential as a comprehensive solution for conversational AI.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The paper is well-structured and easy to follow.
2. The motivation behind the ConvINT framework is well-articulated, addressing the limitations of existing structured methods in capturing the complexity of user intentions.
3. The WeRG method effectively leverages weak supervision to expand ConvINT annotations, making the approach scalable and practical for real-world applications.

### Weaknesses

#### Some Related Works


#### comment

1. The paper’s novelty is somewhat limited, as it primarily builds on existing frameworks for conversational understanding and weakly supervised learning. The proposed ConvINT framework, while innovative in its four-aspect structure, does not introduce a fundamentally new approach to conversational understanding. The method essentially combines existing techniques, such as structured output prediction and weak supervision, without a significant departure from prior work.
2. The paper lacks a detailed comparison with other conversational understanding frameworks, particularly those that also use structured output prediction or weak supervision. This makes it difficult to assess the relative advantages and disadvantages of the proposed approach. A more thorough comparison with existing methods, including a discussion of their strengths and weaknesses, is needed to properly contextualize the contributions of this work.
3. The paper does not provide a comprehensive analysis of the computational cost and efficiency of the WeRG method, which is crucial for practical applications. The paper should include a detailed analysis of the time and memory requirements of the proposed method, as well as a comparison with other methods in terms of computational efficiency. This analysis should include metrics such as training time, inference time, and memory usage.
4. The paper lacks a thorough discussion of the limitations of the WeRG method and potential areas for future research. The paper should include a more detailed discussion of the potential biases in the weak supervision signals and how these biases might affect the performance of the proposed method. Additionally, the paper should discuss potential areas for future research, such as exploring alternative weak supervision techniques or incorporating more sophisticated models for conversational understanding.

### Suggestions

The paper would benefit from a more detailed discussion of the specific challenges in conversational understanding that the ConvINT framework is designed to address. While the four-aspect structure is a good starting point, the paper should elaborate on why existing methods are insufficient and how the ConvINT framework overcomes these limitations. For example, the paper could discuss the specific types of user intentions that are difficult to capture with existing methods and how the situation, emotion, action, and knowledge aspects of ConvINT provide a more comprehensive representation. This discussion should include concrete examples of how the framework handles complex or ambiguous user utterances. Furthermore, the paper should provide a more detailed explanation of the weak supervision signals used in the WeRG method. The paper should clarify how these signals are generated, what types of annotations are used, and how the reward function is designed to optimize the model's performance. A more detailed explanation of the reward function, including the specific metrics used and the rationale behind their selection, would be beneficial.

To address the lack of comparison with other conversational understanding frameworks, the paper should include a more comprehensive literature review and a detailed comparison with existing methods. This comparison should not only focus on the performance of the methods but also on their strengths and weaknesses. The paper should discuss how the proposed approach compares to other methods in terms of the types of user intentions it can capture, the computational cost, and the scalability. This comparison should include a discussion of the specific types of conversational tasks that each method is designed for and how the proposed method compares to these tasks. The paper should also discuss the limitations of the proposed method and how these limitations might affect its performance in real-world applications. For example, the paper should discuss the potential biases in the weak supervision signals and how these biases might affect the performance of the proposed method. 

Finally, the paper should include a more detailed analysis of the computational cost and efficiency of the WeRG method. This analysis should include a breakdown of the time and memory requirements of the proposed method, as well as a comparison with other methods in terms of computational efficiency. The paper should also discuss the scalability of the proposed method and how it can be applied to large-scale datasets. This analysis should include metrics such as training time, inference time, and memory usage. The paper should also discuss the potential for parallelization and other optimization techniques to improve the efficiency of the proposed method. Additionally, the paper should discuss potential areas for future research, such as exploring alternative weak supervision techniques or incorporating more sophisticated models for conversational understanding.

### Questions

1. How does the WeRG method ensure the quality of the weak supervision signals, especially when dealing with noisy or ambiguous data?
2. What are the specific computational costs associated with the WeRG method, and how does it compare to other weakly supervised learning approaches?
3. How does the ConvINT framework handle cases where user intentions are ambiguous or contradictory, and what mechanisms are in place to resolve such conflicts?

### Rating

3

### Confidence

4

**********
