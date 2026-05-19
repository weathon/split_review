### Summary

This paper proposes a novel approach for generating human motion from text descriptions by leveraging multi-reward reinforcement learning (RL). The method integrates human perception models with traditional generative models to improve the alignment between generated motions and human preferences. The authors introduce a batch-wise Pareto selection strategy to approximate Pareto optimality, allowing the model to generate motions that balance text adherence, motion quality, and human preferences effectively. The paper demonstrates the effectiveness of the proposed method through extensive experiments, showing superior performance in both traditional metrics and human perceptual evaluations compared to existing approaches.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

- The paper introduces a novel multi-reward RL framework that effectively integrates human perception models to enhance the alignment of generated motions with human preferences. This approach addresses a critical gap in current text-to-motion generation research, where human perception is often overlooked.
- The use of Pareto optimality to balance multiple objectives is innovative and well-suited for the task. The batch-wise Pareto selection strategy allows for flexible control over the trade-offs between different rewards, providing a practical solution for generating motions that meet diverse requirements.
- The experimental results are comprehensive, covering both quantitative metrics and human perceptual evaluations. The method demonstrates significant improvements over existing approaches, particularly in terms of human alignment, which is a critical factor for real-world applications.
- The paper is well-written and organized, with clear explanations of the proposed method and experimental setup. The inclusion of figures and tables enhances the readability and understanding of the content.

### Weaknesses

#### Some Related Works


#### comment

 - The paper could benefit from a more detailed discussion of the limitations of the proposed approach, such as the computational cost of the multi-reward RL framework and the potential biases in the human perception models used. Specifically, the paper should address the computational overhead associated with training and inference, including memory requirements and training time, and how these scale with the complexity of the motion sequences and the number of reward functions. Furthermore, the potential biases inherent in the human perception models, such as those trained on limited datasets or with specific cultural biases, should be explored in more detail, including their impact on the generated motions.
- While the paper demonstrates improvements in human alignment, it would be valuable to see a more in-depth analysis of the types of motions that are better aligned with human preferences and the specific scenarios where the proposed method excels. For instance, the paper could analyze the performance of the method on different motion categories (e.g., walking, running, jumping) and varying levels of motion complexity. This would provide a more nuanced understanding of the strengths and weaknesses of the approach and help identify areas for future improvement. It would also be beneficial to explore the sensitivity of the method to different hyperparameter settings and their impact on human alignment.
- The paper could explore the potential for extending the proposed method to other types of human motion generation tasks, such as motion editing or motion completion. The current framework is primarily focused on generating motions from text descriptions, but it could be adapted to handle other types of input, such as motion sequences with missing or corrupted segments. This would broaden the applicability of the method and demonstrate its versatility. Furthermore, the paper could discuss the challenges associated with extending the method to these other tasks and potential solutions to overcome these challenges.

### Suggestions

The paper would benefit from a more thorough analysis of the computational aspects of the proposed multi-reward reinforcement learning framework. Specifically, the authors should provide a detailed breakdown of the computational cost associated with each component of the pipeline, including the text encoder, the motion generator, and the reward functions. This analysis should include the time and memory requirements for both training and inference, and how these scale with the complexity of the motion sequences and the number of reward functions. Furthermore, the authors should discuss the potential for optimizing the computational efficiency of their approach, such as through model compression or parallelization techniques. This would provide a more complete picture of the practical feasibility of the proposed method and help readers understand its limitations in real-world applications. It would also be valuable to compare the computational cost of the proposed method with existing text-to-motion generation techniques, highlighting the trade-offs between performance and efficiency.

To further strengthen the paper, a more in-depth analysis of the types of motions that are better aligned with human preferences is needed. The authors should conduct a detailed evaluation of the generated motions across different motion categories and varying levels of complexity, such as walking, running, jumping, and complex maneuvers. This analysis should include both quantitative metrics and qualitative assessments by human evaluators. The authors should also explore the sensitivity of the method to different hyperparameter settings and their impact on human alignment. For example, how does the weighting of different reward functions affect the generated motions? Are there specific hyperparameter settings that lead to better alignment with human preferences for certain motion categories? This analysis would provide a more nuanced understanding of the strengths and weaknesses of the approach and help identify areas for future improvement. Furthermore, the authors should discuss the potential for incorporating user-specific preferences into the generation process, allowing for more personalized motion generation.

Finally, the paper should explore the potential for extending the proposed method to other types of human motion generation tasks, such as motion editing and motion completion. The authors should discuss the challenges associated with adapting the current framework to these tasks and potential solutions to overcome these challenges. For example, how can the method be adapted to handle motion sequences with missing or corrupted segments? How can the method be used to refine existing motion sequences? The authors should also discuss the potential for using the proposed method as a component in more complex motion generation pipelines. This would broaden the applicability of the method and demonstrate its versatility. Furthermore, the authors should consider the potential for using the proposed method in real-world applications, such as virtual reality or gaming, and discuss the challenges and opportunities associated with these applications.

### Questions

- How does the proposed method handle the trade-offs between different objectives, such as text adherence, motion quality, and human preference? Are there specific scenarios where the method struggles to balance these objectives effectively?
- What are the limitations of the human perception models used in the framework, and how might these limitations affect the quality and diversity of the generated motions?
- How does the proposed method compare to other state-of-the-art text-to-motion generation techniques in terms of computational efficiency and scalability?

### Rating

6

### Confidence

3

**********
