### Summary

This paper proposes MotionRL, a reinforcement learning-based approach for text-to-motion generation that optimizes for multiple objectives, including text adherence, motion quality, and human preferences. The key contributions are:

- A novel multi-reward optimization strategy using Pareto optimality to balance different objectives.
- Incorporation of human perceptual priors through a computational perception model.
- Reward-specific identifiers to control trade-offs during inference.

The method is evaluated on the HumanML3D dataset and demonstrates superior performance compared to baselines in terms of both quantitative metrics and human evaluations.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- Novelty: The paper makes a valuable contribution by being the first to apply reinforcement learning to incorporate human perception in text-to-motion generation. The proposed multi-reward optimization strategy using Pareto optimality is a creative solution to balancing multiple objectives.
- Quality: The methodology is well-grounded in existing techniques like PPO and VQ-VAE, with clear mathematical formulations and a thorough experimental evaluation. The use of a pre-trained perception model and the design of reward functions demonstrate technical rigor.
- Clarity: The paper is generally well-written and easy to follow, with clear explanations of the proposed method and experimental setup. The figures and tables effectively illustrate the results.
- Significance: The work addresses an important gap in the field by explicitly considering human perception, which has been largely overlooked in previous text-to-motion generation methods. The ability to control the trade-offs between different objectives during inference adds practical value.

### Weaknesses

#### Some Related Works


#### comment

 - The paper could benefit from a more detailed discussion of the limitations of the proposed approach, such as potential biases in the human preference data or challenges in scaling to more complex motion sequences.
- While the use of a pre-trained perception model is a strength, the paper could explore the impact of different perception models or the possibility of fine-tuning the perception model jointly with the motion generator.
- The ablation study could be more comprehensive, for example by analyzing the impact of different components of the reward function or the sensitivity to hyperparameters.
- The paper mentions using reward-specific tokens to control trade-offs during inference but doesn't provide much detail on how these tokens are designed or how users would specify their preferences. More practical details on the inference process would be helpful.
- The paper could also benefit from a discussion of the computational cost of the proposed method compared to baselines, especially given the use of reinforcement learning.

### Suggestions

The paper should delve deeper into the potential biases inherent in the human preference data used to train the perception model. Specifically, it would be beneficial to analyze the demographics of the human raters and discuss how their subjective preferences might influence the model's behavior. For example, if the raters primarily come from a specific cultural background, the model might learn to favor motions that align with that culture's norms, potentially limiting its generalizability. Furthermore, the paper should explore methods to mitigate these biases, such as using a more diverse dataset or employing techniques to debias the preference data. A detailed analysis of the types of motions that are consistently preferred or dispreferred by the human raters could also provide valuable insights into the limitations of the perception model and guide future improvements.

Further investigation into the impact of different perception models is crucial. The paper should not only compare the performance of the chosen model with other existing models but also explore the possibility of fine-tuning the perception model jointly with the motion generator. This could potentially lead to a more tightly coupled system where the perception model is better aligned with the motion generation process. The paper should also discuss the trade-offs between using a pre-trained perception model and training one from scratch, considering factors such as computational cost, data requirements, and potential for overfitting. It would be beneficial to analyze the sensitivity of the overall system to the performance of the perception model, and explore methods to make the system more robust to variations in perception model accuracy. For example, the authors could investigate the use of an ensemble of perception models or techniques to regularize the perception model's output.

The ablation study should be significantly expanded to provide a more thorough understanding of the proposed method. The paper should analyze the impact of each component of the reward function individually, as well as in different combinations. This would help to identify which rewards are most important for achieving the desired motion quality and human preference alignment. The study should also explore the sensitivity of the method to different hyperparameter settings, such as the learning rate, batch size, and the weights assigned to different rewards. A detailed analysis of the training process, including the convergence behavior and the stability of the results, would also be valuable. Furthermore, the paper should provide more practical details on the design of the reward-specific tokens and how users can specify their preferences during inference. This should include examples of how different tokens affect the generated motions and a discussion of the limitations of this approach.

### Questions

- How does the performance of MotionRL scale to more complex or longer motion sequences?
- What is the computational cost of the proposed method compared to baselines?
- How sensitive is the method to the choice of hyperparameters, such as the learning rate and reward weights?
- How do you ensure that the human preference reward doesn't negatively impact other metrics like text adherence?
- Can you provide more details on the design of the reward-specific tokens and how users can specify their preferences during inference?

### Rating

6

### Confidence

4

**********
