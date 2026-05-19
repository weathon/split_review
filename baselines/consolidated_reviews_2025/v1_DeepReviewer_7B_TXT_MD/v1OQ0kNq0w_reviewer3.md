### Summary

This paper proposes a novel approach to text-to-motion generation by leveraging multi-reward reinforcement learning (RL). The authors address the challenge of aligning generated motions with human preferences, which is often overlooked in traditional generative models. The method employs a multi-objective optimization strategy to balance text adherence, motion quality, and human preferences. The authors introduce a batch-wise Pareto optimality selection strategy, which approximates Pareto optimality within each batch of samples. This allows the model to generate motions that effectively balance the trade-offs between the three objectives. The method is evaluated on the HumanML3D dataset, demonstrating superior performance in terms of both traditional metrics and human perceptual model scores.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper introduces a novel approach to text-to-motion generation by leveraging multi-reward reinforcement learning (RL). This is a significant departure from traditional generative models that primarily focus on optimizing for motion quality and text alignment, often neglecting the crucial aspect of human perception.

2. The authors propose a batch-wise Pareto optimality selection strategy, which approximates Pareto optimality within each batch of samples. This is a creative solution to the challenge of balancing multiple objectives, allowing the model to generate motions that effectively balance text adherence, motion quality, and human preferences.

3. The paper is well-structured and clearly written, making it easy to follow the proposed methodology and understand the experimental setup.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed analysis of the computational cost associated with the proposed method. While the authors mention the use of reinforcement learning, they do not provide a thorough discussion of the computational resources required for training and inference. This is a critical aspect, especially when dealing with complex tasks like text-to-motion generation, where computational efficiency can significantly impact the practicality of the approach. Specifically, the paper should include details on training time, memory usage, and the hardware requirements, which are essential for reproducibility and for assessing the feasibility of the method in real-world applications.

2. The evaluation is limited to a single dataset (HumanML3D), which may not be sufficient to demonstrate the generalizability of the proposed method. While HumanML3D is a widely used dataset for text-to-motion generation, it may not capture the full range of human motion complexities and variations. Evaluating the method on additional datasets, such as those with more diverse motion styles or different types of human actions, would provide a more comprehensive assessment of its performance. This is important to ensure that the method is not overfitting to the specific characteristics of HumanML3D and can generalize well to other scenarios.

3. The paper does not provide a detailed comparison with existing state-of-the-art methods. While the authors mention that their method outperforms existing approaches, they do not provide a comprehensive analysis of the strengths and weaknesses of their method compared to other techniques. A more detailed comparison, including quantitative results and qualitative analysis, would help to better position the proposed method within the existing literature and highlight its unique contributions. This should include a discussion of the specific advantages and disadvantages of the proposed approach compared to other methods, such as GPT-based models or other reinforcement learning approaches for motion generation.

4. The paper does not discuss the potential limitations of the proposed method. For example, it would be helpful to discuss the sensitivity of the method to the choice of hyperparameters, the potential for mode collapse, or the challenges of generating motions that are both diverse and aligned with human preferences. A thorough discussion of these limitations would provide a more balanced view of the method and help to identify areas for future research. This should include an analysis of the potential failure modes of the method and how these could be addressed.

### Suggestions

To address the lack of computational cost analysis, the authors should include a detailed breakdown of the resources required for both training and inference. This should include specific information on training time, memory usage, and the hardware specifications used. Furthermore, it would be beneficial to provide a comparison of the computational cost of their method with other state-of-the-art text-to-motion generation techniques. This would allow readers to better understand the trade-offs between performance and computational efficiency. The authors should also discuss the scalability of their method, including how the computational cost scales with the size of the input text and the length of the generated motion sequences. This analysis should be presented in a clear and concise manner, possibly using tables or graphs to illustrate the computational requirements.

To improve the generalizability of the method, the authors should evaluate their approach on additional datasets that capture a wider range of human motion complexities and variations. This could include datasets with more diverse motion styles, different types of human actions, or even datasets from different domains. The evaluation should include a quantitative analysis of the performance of the method on these new datasets, as well as a qualitative analysis of the generated motions. This would help to demonstrate the robustness of the method and its ability to generalize to new scenarios. The authors should also discuss any challenges they encountered when adapting their method to these new datasets and how they addressed these challenges. This would provide valuable insights into the limitations of the method and potential areas for improvement.

Finally, the authors should provide a more detailed comparison with existing state-of-the-art methods, including a discussion of the specific advantages and disadvantages of their approach. This comparison should include both quantitative results and qualitative analysis, and should be presented in a clear and concise manner. The authors should also discuss the limitations of their method, including the sensitivity to hyperparameters, the potential for mode collapse, and the challenges of generating motions that are both diverse and aligned with human preferences. This discussion should be supported by empirical evidence and should provide a balanced view of the method. The authors should also suggest potential avenues for future research to address these limitations and further improve the performance of their method.

### Questions

1. How does the proposed method handle the trade-offs between text adherence, motion quality, and human preference? Are there specific scenarios where the method struggles to balance these objectives effectively?

2. What are the limitations of the human perception models used in the framework, and how might these limitations affect the quality and diversity of the generated motions?

3. How does the proposed method compare to other state-of-the-art text-to-motion generation techniques in terms of computational efficiency and scalability?

### Rating

6

### Confidence

4

**********
