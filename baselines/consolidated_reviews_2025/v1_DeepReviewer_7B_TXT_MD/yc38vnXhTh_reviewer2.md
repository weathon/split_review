### Summary

This paper proposes a framework for generating human-like behavior in 3D scenes. The framework consists of a perceive-plan-act cycle, where the agent generates a tree of possible actions and selects the best one based on a value function. The authors also introduce a dataset of human behavior in 3D scenes, which is used to train and evaluate their method. The proposed method is evaluated on a benchmark dataset and shows promising results compared to other baselines.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The paper is well-written and easy to follow.
- The proposed method is novel and addresses an important problem in human-computer interaction.
- The authors have made a significant effort to collect and annotate a large-scale dataset of human behavior in 3D scenes.

### Weaknesses

#### Some Related Works


#### comment

 - The proposed method relies on several heuristics and design choices, such as the window size for LLM calls and the value function. The authors should provide more details on how these parameters were chosen and their impact on the performance of the method.
- The evaluation of the proposed method is limited to a single benchmark dataset. It would be beneficial to evaluate the method on other datasets or in more diverse environments to demonstrate its generalizability.
- The paper does not discuss the limitations of the proposed method or potential failure cases. It would be helpful to have a more thorough analysis of the scenarios where the method might fail or produce suboptimal results.

### Suggestions

The paper would benefit from a more thorough investigation into the sensitivity of the proposed method to its hyperparameters. Specifically, the authors should conduct a systematic ablation study to analyze the impact of the window size for LLM calls on the overall performance. This could involve varying the window size and observing the resulting changes in success rate, goal success rate, and other relevant metrics. Furthermore, the authors should provide a more detailed explanation of how the value function is designed and trained. It is unclear how the different components of the value function are weighted and how the model is trained to optimize the overall performance. A more detailed description of the training process, including the loss function and optimization algorithm, would be beneficial. The authors should also discuss the potential limitations of the current value function and suggest possible improvements.

To address the limited evaluation, the authors should consider evaluating their method on additional datasets that capture different types of human behavior and environments. This could include datasets with more complex scenes, different types of human actions, or more diverse goal specifications. For example, evaluating the method on datasets that include more dynamic environments or more complex interactions with objects would provide a more comprehensive assessment of its capabilities. Furthermore, the authors should provide a more detailed analysis of the failure cases of their method. This could involve identifying the specific scenarios where the method fails to produce satisfactory results and analyzing the underlying causes. This analysis would help to identify the limitations of the current approach and suggest directions for future research.

Finally, the authors should provide a more detailed discussion of the computational cost of their method. This should include an analysis of the time and memory requirements of the different components of the framework, as well as the overall computational cost of generating a sequence of actions. This information would be helpful for researchers who are interested in implementing the method in resource-constrained environments. The authors should also discuss potential ways to reduce the computational cost of the method, such as using more efficient algorithms or reducing the number of LLM calls.

### Questions

- How does the proposed method compare to other state-of-the-art methods for human motion generation?
- What are the potential applications of the proposed method beyond the tasks presented in the paper?
- How does the proposed method handle situations where the environment is partially observable or dynamic?

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
