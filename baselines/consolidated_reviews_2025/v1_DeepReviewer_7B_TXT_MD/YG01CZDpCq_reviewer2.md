### Summary

This paper proposes Adaptive Prompt Prototype Learning (APPLe) for vision-language models. Specifically, APPLe learns multiple prompts as class prototypes to cover the visual variance of each class. Moreover, an adaptive attention mechanism is designed to weigh the importance of different prototypes. Experiments show the effectiveness of the proposed method.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper is well-written and easy to follow.
2. The motivation of the paper is clear and reasonable.
3. The experiments are comprehensive and well-designed.

### Weaknesses

#### Some Related Works

[1] ProDA: Probabilistic Discriminative Adapters for Vision-Language Models
[2] Learning to Prompt for Visual Recognition

#### comment

1. The novelty of the paper is limited. The proposed method is a simple combination of prompt learning and prototype learning. The idea of learning multiple prompts as class prototypes has been explored in [1][2]. The main difference between the proposed method and [1][2] is that the proposed method uses an attention mechanism to learn the importance of different prototypes. However, the attention mechanism is also widely used in the field of vision-language models. The core idea of using multiple prompts to capture intra-class variance, while effective, lacks significant novelty given existing work in adapter-based methods and prompt learning. The adaptive attention mechanism, while a useful component, is not a fundamentally new concept in the broader context of vision-language models.
2. The paper lacks a detailed analysis of the proposed method. For example, the authors should analyze the effect of the number of prototypes and the effect of the proposed method on different classes. The paper would benefit from a more thorough investigation into the sensitivity of the method to the number of prototypes used. Furthermore, a more granular analysis of performance across different classes, especially those with high intra-class variance, is needed to understand the method's strengths and weaknesses. This analysis should go beyond overall accuracy and delve into specific failure cases.
3. The paper lacks a comparison with some important baselines, such as MaPLe. The absence of a direct comparison with MaPLe, a relevant and state-of-the-art method, makes it difficult to assess the true contribution of the proposed approach. A more comprehensive comparison is needed to contextualize the performance of APPLe.

### Suggestions

The paper should provide a more in-depth analysis of the proposed method's behavior. Specifically, the authors should investigate the impact of varying the number of prototypes on the performance of APPLe. This analysis should include a detailed examination of how the performance changes as the number of prototypes increases or decreases, and whether there is an optimal number of prototypes for different datasets or classes. Furthermore, the authors should analyze the performance of APPLe on a per-class basis, especially for classes with high intra-class variance. This analysis should identify specific classes where the method performs well and classes where it struggles, providing insights into the method's strengths and weaknesses. Such analysis would help to understand the method's ability to capture intra-class variance and its limitations.

To address the lack of comparison with MaPLe, the authors should include a direct comparison with this baseline in the experimental section. This comparison should not only include overall performance metrics but also a detailed analysis of the results. The authors should discuss the differences in performance between APPLe and MaPLe, and explain why one method performs better than the other in specific scenarios. This comparison should also include an analysis of the computational cost of each method, providing a more complete picture of their relative strengths and weaknesses. The authors should also consider including other relevant baselines in the comparison to provide a more comprehensive evaluation of the proposed method.

Finally, the authors should provide a more detailed explanation of the adaptive attention mechanism. While the paper mentions that the attention mechanism is used to learn the importance of different prototypes, it lacks a deeper explanation of how this mechanism works and why it is effective. The authors should provide a more detailed description of the attention mechanism, including the specific mathematical operations involved and the rationale behind their design choices. This explanation should include a discussion of how the attention mechanism adapts to different inputs and how it contributes to the overall performance of the method. A more detailed explanation of the attention mechanism would help to clarify its role in the proposed method and its contribution to the overall performance.

### Questions

1. What is the effect of the number of prototypes?
2. How does the proposed method perform on some classes with high intra-class variance?
3. How does the proposed method perform compared with MaPLe?

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
