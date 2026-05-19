### Summary

This paper proposes an agent that can generate human-like behaviors in 3D scenes. The agent consists of a perceive-plan-act cycle. The agent is evaluated on a newly created dataset, BEHAVIORHUB.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

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

The authors should provide a more detailed analysis of the hyperparameter selection process, particularly for the window size of the LLM calls and the value function. For the window size, it would be beneficial to show how different window sizes affect the performance metrics, such as the success rate and the quality of the generated plans. This could involve a sensitivity analysis where the window size is varied systematically, and the resulting performance is plotted. For the value function, the authors should provide more details on how the different components are weighted and how the model is trained to optimize the overall performance. This could include a discussion of the specific loss functions used and the optimization algorithms employed. Furthermore, the authors should discuss the potential limitations of the current value function and suggest possible improvements.

To address the limited evaluation, the authors should consider evaluating their method on additional datasets that capture different types of human behavior and environments. This could include datasets with more complex scenes, different types of human actions, or more diverse goal specifications. For example, evaluating the method on datasets that include more dynamic environments or more complex interactions with objects would provide a more comprehensive assessment of its capabilities. Additionally, the authors should consider comparing their method to other state-of-the-art methods for human motion generation, even if those methods are not directly comparable. This would help to contextualize the performance of their method and identify areas for improvement. The authors should also discuss the computational cost of their method and how it scales with the complexity of the environment and the length of the generated plans.

Finally, the authors should provide a more thorough analysis of the limitations of their method and potential failure cases. This could include identifying the specific scenarios where the method fails to produce satisfactory results and analyzing the underlying causes. For example, the authors could investigate the performance of the method in scenarios with occlusions, dynamic objects, or unexpected events. This analysis would help to identify the limitations of the current approach and suggest directions for future research. The authors should also discuss the potential impact of the limitations on the real-world applicability of their method. This would provide a more balanced and realistic assessment of the proposed approach.

### Questions

Please see the weaknesses.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
