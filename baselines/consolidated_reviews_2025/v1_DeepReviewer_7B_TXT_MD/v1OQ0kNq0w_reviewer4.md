### Summary

The paper introduces MotionRL, a novel approach to text-to-motion generation that leverages multi-reward reinforcement learning (RL) to optimize for human preferences, text adherence, and motion quality. Unlike existing methods that focus on optimizing for motion quality and text alignment, MotionRL incorporates human perception models to capture nuanced human preferences, enabling more natural and human-like motions. The method employs a batch-wise Pareto optimality selection strategy to approximate Pareto optimality, allowing for flexible control over the trade-offs between different rewards. The authors evaluate MotionRL on the HumanML3D dataset, demonstrating its superiority over other algorithms in terms of both traditional metrics and human perceptual model scores.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow, with clear explanations of the proposed method and experimental setup.
2. The authors provide a comprehensive evaluation of MotionRL, including both quantitative metrics and human perceptual model scores, demonstrating its effectiveness in generating human-like motions.
3. The use of multi-reward RL to balance text adherence, motion quality, and human preferences is a novel contribution that addresses a critical gap in text-to-motion generation research.
4. The paper includes a thorough ablation study, which helps to understand the contribution of each component of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

1. The paper primarily evaluates MotionRL on the HumanML3D dataset, which may not fully represent the diversity of human motion. It would be beneficial to see results on other datasets to assess the generalizability of the approach.
2. The computational cost of the proposed method is not discussed in detail, which could be a concern for practical applications.
3. The paper could benefit from a more detailed analysis of the limitations of the human perception models used in the framework and how these limitations might affect the quality and diversity of the generated motions.

### Suggestions

The authors should consider expanding their evaluation to include datasets with more diverse human motion types, such as those found in sports or daily activities. This would provide a more comprehensive assessment of the method's generalizability and robustness. For example, datasets like the HumanAct or CMU Mocap dataset could be used to evaluate the model's performance on a wider range of motion styles and complexities. Furthermore, it would be beneficial to analyze the performance of MotionRL on motions with varying levels of difficulty, such as those involving complex interactions or rapid changes in direction. This would help to identify potential limitations of the approach and guide future improvements.

Regarding the computational cost, the authors should provide a more detailed analysis of the resources required for training and inference. This should include a breakdown of the time and memory requirements for each stage of the pipeline, as well as a comparison with existing text-to-motion generation methods. It would be helpful to discuss the scalability of the method and identify potential bottlenecks that could limit its practical applicability. For example, the authors could analyze the impact of different batch sizes and sequence lengths on the computational cost and provide recommendations for optimizing the method for resource-constrained environments. Additionally, the authors should discuss the potential for parallelizing the computation to reduce the overall training time.

Finally, the authors should provide a more detailed analysis of the limitations of the human perception models used in the framework. This should include a discussion of the potential biases and inaccuracies of these models and how they might affect the quality and diversity of the generated motions. For example, the authors could analyze the performance of the human perception model on different types of motions and identify potential failure cases. It would also be beneficial to explore alternative human perception models and compare their performance with the current model. Furthermore, the authors should discuss the potential for incorporating user feedback into the human perception model to improve its accuracy and relevance.

### Questions

1. How does the proposed method handle the trade-offs between text adherence, motion quality, and human preference? Are there specific scenarios where the method struggles to balance these objectives effectively?
2. What are the limitations of the human perception models used in the framework, and how might these limitations affect the quality and diversity of the generated motions?
3. How does the proposed method compare to other state-of-the-art text-to-motion generation techniques in terms of computational efficiency and scalability?

### Rating

8

### Confidence

4

**********
