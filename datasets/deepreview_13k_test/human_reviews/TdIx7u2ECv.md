# Imagine to Ensure Safety in Hierarchical Reinforcement Learning

- Decision: Reject
- Scores: 5, 5, 6, 5

## Abstract
This work investigates the safe exploration problem, where an agent must maximize performance while satisfying safety constraints. To address this problem, we propose a method that includes a learnable world model and two policies, a high-level policy and a low-level policy, that ensure safety at both levels. The high-level policy generates safe subgoals for the low-level policy, which progressively guide the agent towards the final goal. Through trajectory imagination, the low-level policy learns to safely reach these subgoals. The proposed method was evaluated on the standard benchmark, SafetyGym, and demonstrated superior performance quality while maintaining comparable safety violations compared to state-of-the-art approaches. In addition, we investigated an alternative implementation of safety in hierarchical reinforcement learning (HRL) algorithms using Lagrange multipliers, and demonstrated in the custom long-horizon environments SafeAntMaze that our approach achieves comparable performance while more effectively satisfying safety constraints, while the flat safe policy fails to accomplish this task.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a Safe RL algorithm that learns the model of the environment as well as a hierarchical approach to policy learning. In particular, it learns a high-level policy that creates sub-goals and a low-level policy that tries to achieve/reach the sub-goals. The authors claim improved results compared with Safe RL approaches that are based on primal-dual/Lagrangian relaxation.

### Strengths
- well-written and clear
- problem and approach is well-motivated

### Weaknesses
- There are not too many benchmarks on which this algorithm has been tested (only three)
- There are very few Safe RL baselines used for comparison. TD3Lag is the only primal-dual baseline, and it performs decently well but was used only in SafeAntMaze. Consider comparing with more primal-dual/Lagrangian relaxation approaches. 
- It is not clear if any model-based safe RL algorithms were used as baselines, especially when the proposed approach is model-based. How does the proposed approach compare empirically with Jayant & Bhatnagar, 2022?
- It would be nice to have a pseudocode of the algorithm in one place.
- It would also be nice to have the training parameters used for the algorithm.

Minor errors:
- Section 2.1 title typo "constrained"

### Questions
What are the limitations of this approach?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper addresses the challenge of safe exploration in reinforcement learning. To balance performance with constraint satisfaction, the authors use a hierarchical architecture in which the high-level policy outputs safe subgoals and the low-level policy learns to reach these subgoals. Leveraging a learnable world model, the agent is able to fully consider safety before taking actions. The authors test the proposed ITES algorithm in the SafetyGym simulation environment, demonstrating its effectiveness in balancing safety and performance across both short-horizon and long-horizon tasks.

### Strengths
- Using the world model to imagine safety before executing actions is an interesting idea.
- The paper is well-organized, and the hierarchical structure is explained clearly.
- The experimental results demonstrate ITES’s effectiveness in balancing safety with performance across both short- and long-horizon tasks.

### Weaknesses
- The authors state, "ITES is the only one that combines model-based and hierarchy approach." However, the necessity of combining these two approaches is not demonstrated (for instance, if the model-based approach alone sufficiently improves safety, then a hierarchical structure may not be needed). Is this combination simply an “A+B” type of innovation?
- The experiments are limited to simple navigation tasks, raising questions about the method’s effectiveness in more complex, real-world tasks beyond navigation.
- The implementation codes are not provided.

### Questions
- Is this hierarchical structure, in which the high-level policy outputs subgoals, generally applicable, or is it only suited to navigation tasks? Would the high-level policy need to be redesigned for different types of tasks?
- How is the safety cost C_M specifically set? How are the probability labels obtained, especially in real-world tasks outside of simulations?
- How is the interval scale for subgoals determined?
- In Table 2, why is the Final Cost for ITES consistently the highest?
- There are some minor typos, including:
  - In line 116, `r_int` should be `r_in`.
  - The first occurrence of “HRAC” should be expanded in full.
  - The \beta coefficients in Equation (6) and their settings need explanation, as does Equation (9).
  - The quality of Figures 5 and 6 needs improvement; for example, in Figure 5, the shaded area is difficult to distinguish, and “Cost Rate” should not be underlined.
  - The format of the references needs to be standardized and unified.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes ITES (Imagine To Ensure Safety), a hierarchical reinforcement learning (HRL) method that incorporates a world model and dual-level safety policy to address the safe exploration problem. By generating safe subgoals with a high-level policy and optimizing short-horizon safety at the low level, ITES aims to balance performance and safety effectively. The world model enables ITES to "imagine" potential actions, verifying their safety before executing them in the real environment. Experiments on SafetyGym tasks and a more complex SafeAntMaze environment suggest that ITES achieves a safety advantage in long-horizon tasks while maintaining competitive performance in simpler settings.

### Strengths
ITES’s use of dual-level safety with high-level safe subgoal generation and low-level safety checks is a well-conceived approach to enhancing reinforcement learning safety. The method of verifying actions in imagination through a world model adds an innovative layer that may reduce real-world safety violations.

The results show that ITES achieves a reasonable balance between safety and performance, particularly in SafeAntMaze. This structure helps demonstrate ITES’s suitability for scenarios where long-horizon safety is critical, even if it compromises some performance in short-horizon tasks.

ITES introduces a practical approach for managing safety constraints in HRL by embedding safety checks at both the planning and execution levels, which may inspire further hierarchical developments in safe reinforcement learning.

### Weaknesses
Although ITES demonstrates safety advantages in the complex SafeAntMaze environment, it does not consistently provide a safer solution than CUP in simpler SafetyGym tasks. For example, in the PointGoal1 task, ITES sacrifices some safety in favor of performance, resulting in a higher reward but slightly increased safety violations compared to CUP. This suggests that ITES may not consistently prioritize safety over performance across different task types, which could limit its applicability in certain safety-critical environments.

SafeAntMaze is the only complex, long-horizon task tested in the paper, which restricts the evidence supporting ITES’s generalizability to other challenging environments. Without more complex benchmarks, it’s difficult to conclude that ITES is superior to other approaches in handling diverse safety-intensive scenarios.

In the short-horizon SafetyGym tasks, ITES shows a performance advantage over CUP in the CarGoal1 task but lacks consistent improvements in safety. This performance-safety trade-off indicates that ITES may be best suited to tasks where performance can be favored without compromising critical safety constraints, making it less optimal for environments that strictly require safety prioritization.

The hierarchical structure in ITES introduces added complexity, but the benefits of this structure are not consistently clear across all tasks. While ITES demonstrates advantages in SafeAntMaze, the mixed results in SafetyGym suggest that simpler, single-policy methods may sometimes offer comparable or superior performance and safety. A broader range of tests could provide a clearer justification for the added complexity of ITES’s hierarchical approach.

### Questions
Could the authors provide further evidence or analysis supporting ITES’s necessity in complex environments by testing on additional long-horizon tasks?

Given that ITES sacrifices some performance in short-horizon tasks, what are the potential trade-offs in settings where safety constraints are less critical?

Could the authors clarify if ITES could be combined with other model-free or model-based approaches to mitigate the observed performance gaps in simpler environments?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The core innovation of this paper is the proposed method called ITES (Imagine To Ensure Safety in Hierarchical Reinforcement Learning). This method combines model-driven reinforcement learning and hierarchical reinforcement learning to ensure safety. It introduces a high-level policy and a low-level policy to generate safe intermediate subgoals and guide the agent toward the final goal. Through trajectory imagination, the low-level policy learns to reach these subgoals safely. 
Key contributions include:
Using hierarchical reinforcement learning for enhanced safety and performance.
Employing a world model to verify safety in imagination and a cost model for generating safe subgoals.
Demonstrating superior performance on SafetyGym and SafeAntMaze benchmarks compared to state-of-the-art methods, especially in satisfying safety constraints.

### Strengths
Compared to existing methods, ITES (Imagine To Ensure Safety in Hierarchical Reinforcement Learning) achieves better performance quality while maintaining comparable safety violations. Additionally, the paper explores an alternative implementation of safety in hierarchical reinforcement learning using Lagrange multipliers and demonstrates that ITES provides better safety while maintaining comparable performance to traditional safe policies in a custom long-horizon environment called SafeAntMaze.

### Weaknesses
1.The paper claims novelty in integrating safety with hierarchical reinforcement learning (HRL) and a model-based approach, but similar methods have been explored previously. For instance, Safe HIRO [1]  and IAHRL [2] also focuses on hierarchical approaches for safe exploration.  Provide a clearer distinction between ITES and existing approaches. Explicitly state the unique aspects of ITES, such as how the world model or subgoal generation differs from previous methods.
[1] Roza F S, Roscher K, Günnemann S. Safe and efficient operation with constrained hierarchical reinforcement learning[C]//Sixteenth European Workshop on Reinforcement Learning, 2023.
[2] Lee S H, Jung Y, Seo S W. Imagination-augmented hierarchical reinforcement learning for safe and interactive autonomous driving in urban environments[J]. IEEE Transactions on Intelligent Transportation Systems, 2024.
2.The use of a world model for safety verification in imagination depends on the accuracy of the learned model. If the model is imperfect, it may not accurately detect safety violations, potentially leading to unsafe behavior in the real environment. This paper does not address the limitations of model inaccuracies or present any strategies to handle model uncertainty.

### Questions
1.How exactly is the safe region for subgoal generation defined, and how is it updated during the training process? Is it a static boundary, or does it adapt based on the agent's learning progress?
2.Provide a clearer distinction between ITES and existing approaches, such as [1] and [2]. 
[1] Roza F S, Roscher K, Günnemann S. Safe and efficient operation with constrained hierarchical reinforcement learning[C]//Sixteenth European Workshop on Reinforcement Learning, 2023.
[2] Lee S H, Jung Y, Seo S W. Imagination-augmented hierarchical reinforcement learning for safe and interactive autonomous driving in urban environments[J]. IEEE Transactions on Intelligent Transportation Systems, 2024.
3.Have you considered any potential challenges in transferring the proposed ITES method to real-world robotic applications? How would the approach handle noisy sensor data or unexpected changes in the environment?

### Soundness
3

### Presentation
2

### Contribution
2
