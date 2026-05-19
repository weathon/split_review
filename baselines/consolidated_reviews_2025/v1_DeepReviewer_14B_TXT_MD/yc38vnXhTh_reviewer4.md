### Summary

This paper introduces ACTOR, an agent that can perform high-level, long-horizon, abstract goals in 3D households, guided by its internal value similar to those of humans. ACTOR operates in a perceive-plan-act cycle, extending the ungrounded, scene-agnostic LLM controller with deliberate goal decomposition and decision-making through actively searching the behavior space, generating activity choices based on a hierarchical prior, and evaluating these choices using customizable value functions to determine the subsequent steps. Furthermore, the authors introduce BehaviorHub, a large-scale human behavior simulation dataset in scene-aware, complicated tasks.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The proposed method is technically sound and well-motivated. The proposed dataset is large-scale and can be useful for the community.
2. The paper is well-organized and easy to follow.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method is not fully autonomous. The authors need to provide more details about the perception module, including how the perception module is implemented and what kind of information it can perceive. Specifically, it's unclear what sensors are simulated, how the raw sensor data is processed, and what kind of scene understanding is achieved. For example, can the agent perceive object affordances, or is it limited to basic object recognition? The lack of detail makes it difficult to assess the limitations of the perception module and its impact on the overall system.
2. The authors should provide more details about the motion generation module, including how the motion is generated and what kind of motion quality can be achieved. It is not clear what kind of motion primitives are used, how they are combined to form complex actions, and how the system ensures smooth and realistic transitions between different motions. Furthermore, the paper lacks a quantitative evaluation of the motion quality, such as metrics for naturalness or smoothness. The absence of such metrics makes it hard to compare the proposed method with other motion generation techniques.

### Suggestions

To address the lack of detail regarding the perception module, the authors should provide a more thorough description of its implementation. This should include a detailed explanation of the simulated sensors, the data processing pipeline, and the specific scene understanding capabilities. For example, the authors could describe how the agent perceives object affordances, such as whether a chair is suitable for sitting or a table for placing objects. It would be beneficial to include a discussion of the limitations of the perception module, such as its sensitivity to lighting conditions or occlusions. Furthermore, the authors should provide a quantitative evaluation of the perception module, such as metrics for object recognition accuracy or scene understanding completeness. This would allow for a more objective assessment of the module's performance and its impact on the overall system.

Regarding the motion generation module, the authors should provide a more detailed explanation of the motion primitives used and how they are combined to form complex actions. This should include a description of the motion representation, the control mechanism, and the techniques used to ensure smooth and realistic transitions between different motions. For example, the authors could describe how the system handles transitions between standing, walking, and sitting motions. It would be beneficial to include a quantitative evaluation of the motion quality, such as metrics for naturalness or smoothness. This could involve comparing the generated motions with human motion capture data or using metrics such as the Fréchet Inception Distance (FID) or action recognition accuracy. The authors should also discuss the limitations of the motion generation module, such as its ability to handle complex environments or its sensitivity to changes in the environment.

Finally, the authors should consider providing a more detailed analysis of the overall system's performance, including the impact of the perception and motion generation modules on the agent's ability to achieve its goals. This could involve a series of experiments that systematically vary the complexity of the environment and the tasks, and evaluate the agent's performance under different conditions. This would provide a more comprehensive understanding of the system's capabilities and limitations, and help to identify areas for future improvement.

### Questions

Please see the weaknesses.

### Rating

8

### Confidence

3

**********
