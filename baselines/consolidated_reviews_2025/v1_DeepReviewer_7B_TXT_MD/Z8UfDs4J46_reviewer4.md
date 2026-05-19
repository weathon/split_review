### Summary

This paper studies the problem of signal delay in deep reinforcement learning. The authors propose a new framework called Delayed Observation Markov Decision Processes (DOMDP) to model the problem. They also propose a series of methods to mitigate the problem. Experiments on MuJoCo tasks show the effectiveness of the proposed methods.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow. The authors provide a comprehensive review of the related work and clearly explain the motivation of the problem.
2. The authors propose a series of methods to mitigate the problem of signal delay in deep reinforcement learning. These methods are easy to implement and effective.
3. The authors conduct extensive experiments on MuJoCo tasks to validate the effectiveness of the proposed methods.

### Weaknesses

#### Some Related Works


#### comment

1. The authors only consider the case where the delay is fixed. However, in real-world scenarios, the delay may vary over time. It would be better to discuss the limitations of the proposed methods in handling time-varying delays.
2. The authors only consider the case where the delay is known. However, in real-world scenarios, the delay may be unknown or uncertain. It would be better to discuss the limitations of the proposed methods in handling unknown or uncertain delays.
3. The authors only consider the case where the delay is small. It would be better to discuss the limitations of the proposed methods in handling large delays.

### Suggestions

The paper would benefit from a more thorough discussion of the limitations of the proposed methods when applied to time-varying delays. While the current approach assumes a fixed delay, many real-world systems exhibit delays that fluctuate over time due to various factors such as network congestion or sensor noise. The authors should explore how their methods would perform under such conditions. For instance, they could investigate the use of adaptive delay estimation techniques or incorporate a mechanism to detect and adjust to changes in the delay. Furthermore, it would be valuable to analyze the sensitivity of the proposed methods to different types of delay variations, such as linear or non-linear changes in delay over time. This would provide a more comprehensive understanding of the robustness of the proposed framework.

Additionally, the paper should address the challenges associated with unknown or uncertain delays. In practical applications, the exact delay may not be known precisely, and there might be a range of possible delay values. The authors should discuss how their methods would perform under such uncertainty. One potential approach could be to incorporate a delay estimation module that learns the delay from the data, or to use robust optimization techniques that are less sensitive to variations in the delay. It would also be beneficial to analyze the impact of delay uncertainty on the performance of the proposed methods and to provide guidelines for selecting appropriate delay estimation techniques or robust optimization methods based on the expected level of uncertainty. This would enhance the practical applicability of the proposed framework.

Finally, the paper should investigate the performance of the proposed methods under large delays. While the experiments in the paper consider relatively small delays, many real-world systems may experience significant delays that can significantly impact the performance of the proposed methods. The authors should explore how their methods would perform under such conditions and identify the limitations of the proposed methods in handling large delays. For instance, they could investigate the use of delay-aware architectures or incorporate a mechanism to handle large delays. It would also be valuable to analyze the trade-offs between delay accuracy and performance and to provide guidelines for selecting appropriate methods for different delay ranges. This would provide a more comprehensive understanding of the applicability of the proposed framework in real-world scenarios.

### Questions

Please see the weaknesses.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
