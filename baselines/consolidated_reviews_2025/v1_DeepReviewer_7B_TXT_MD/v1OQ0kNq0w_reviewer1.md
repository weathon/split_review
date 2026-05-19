### Summary

The paper proposes a reinforcement learning approach to improve the alignment of generated text-to-motion with human preferences. The proposed method, MotionRL, introduces a multi-objective optimization strategy that approximates Pareto optimality to balance text adherence, motion quality, and human preferences. The method demonstrates superior performance compared to existing approaches across multiple metrics.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is well-motivated and addresses a significant challenge in text-to-motion generation.
3. The use of Pareto optimality to balance multiple objectives is innovative and well-suited for the task.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed analysis of the computational cost associated with the proposed method, which is important for practical applications.
2. The evaluation is limited to a single dataset (HumanML3D), and it would be beneficial to see results on other datasets to assess the generalizability of the approach.
3. The paper does not provide a thorough comparison with existing state-of-the-art methods, making it difficult to fully assess the advantages of the proposed approach.

### Suggestions

The paper should include a more thorough analysis of the computational demands of the MotionRL framework. Specifically, the authors should provide a breakdown of the time and memory requirements for each stage of the pipeline, including the reinforcement learning training phase. This analysis should consider the impact of different batch sizes, sequence lengths, and model architectures on the overall computational cost. Furthermore, it would be beneficial to compare the computational efficiency of MotionRL with existing text-to-motion generation methods. This would allow readers to better understand the trade-offs between performance and computational resources, which is crucial for practical applications. The authors should also discuss potential strategies for optimizing the computational efficiency of their approach, such as model pruning, quantization, or distributed training techniques.

To address the limited evaluation, the authors should extend their experiments to include additional datasets that represent diverse motion styles and complexities. For example, datasets with more varied human actions, such as those found in sports or daily activities, could provide a more comprehensive assessment of the generalizability of the proposed method. The evaluation should also include a more detailed analysis of the performance of MotionRL across different types of motions, identifying any potential biases or limitations. Furthermore, the authors should consider using a wider range of evaluation metrics, including metrics that specifically measure the quality of human motion, such as motion smoothness and naturalness. This would provide a more complete picture of the strengths and weaknesses of the proposed approach.

Finally, the paper needs a more comprehensive comparison with existing state-of-the-art methods. The authors should not only compare the performance of MotionRL with other text-to-motion generation models but also with other reinforcement learning-based approaches for motion generation. This comparison should include a detailed analysis of the advantages and disadvantages of each method, highlighting the specific scenarios where MotionRL outperforms or underperforms other approaches. The authors should also discuss the limitations of their method and identify potential areas for future research. This would provide a more balanced and nuanced perspective on the contributions of the paper and help readers understand the current state of the field.

### Questions

See above.

### Rating

5

### Confidence

3

**********
