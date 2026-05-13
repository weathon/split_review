# QMP: Q-switch Mixture of Policies for Multi-Task Behavior Sharing

- Decision: Accept
- Scores: 6, 8, 6, 6

## Abstract
Multi-task reinforcement learning (MTRL) aims to learn several tasks simultaneously for better sample efficiency than learning them separately. Traditional methods achieve this by sharing parameters or relabeled data between tasks.
In this work, we introduce a new framework for sharing \textit{behavioral policies} across tasks, which can be used in addition to existing MTRL methods. The key idea is to improve each task's off-policy data collection by employing behaviors from other task policies. Selectively sharing helpful behaviors acquired in one task to collect training data for another task can lead to higher-quality trajectories, leading to more sample-efficient MTRL.
Thus, we introduce a simple and principled framework called Q-switch mixture of policies (QMP) that selectively shares behavior between different task policies by using the task's Q-function to evaluate and select useful shareable behaviors.
We theoretically analyze how QMP improves the sample efficiency of the underlying RL algorithm.
Our experiments show that QMP's behavioral policy sharing provides complementary gains over many popular MTRL algorithms and outperforms alternative ways to share behaviors in various manipulation, locomotion, and navigation environments. 
Videos are available at~\href{https://qmp-mtrl.io/}{https://qmp-mtrl.io/}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces Q-switch Mixture of Policies (QMP), a novel framework for multi-task reinforcement learning that improves sample efficiency through selective behavior sharing between tasks. The key idea is to enhance each task's off-policy data collection by selectively employing behaviors from other task policies, using the task's Q-function to evaluate and select useful shareable behaviors.

### Strengths
- The paper is well-written with clear organization and easy to follow.

- The method is elegantly simple yet theoretically sound, introducing behavior sharing through off-policy data collection rather than policy regularization, which avoids bias in the learning objective while maintaining convergence guarantees.

- The proposed Q-switch mechanism provides a principled approach to selective behavior sharing that is complementary to existing MTRL methods, demonstrating consistent improvements when combined with parameter sharing, data sharing, and gradient-based approaches.

### Weaknesses
1. The Q-switch mechanism requires evaluating all task policies and Q-values at each step. While parallelization helps, this still leads to significant computational costs, especially for large task sets as evidenced by the 7+ days runtime in MT50 experiments.
2. The method heavily relies on accurate Q-function estimation to select appropriate behaviors. This dependency may lead to suboptimal behavior selection during early training or in tasks with sparse rewards where Q-function learning is unstable.

3. The method requires careful tuning of hyperparameters, such as manually setting 70% task-specific policy usage in Meta-World MT10. This tuning requirement may limit practical applicability.

4. The method's effectiveness heavily depends on the existence of shareable behaviors between tasks. Performance gains might be limited for completely unrelated or highly conflicting task sets.

5. The convergence analysis primarily focuses on tabular MDPs. The theoretical guarantees may not fully extend to continuous state-action spaces with function approximation.

### Questions
See above.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces the Q-switch Mixture of Policies (QMP), a framework for multi-task reinforcement learning (MTRL) aimed at enhancing sample efficiency by sharing behaviors selectively across tasks. The approach enables an agent to leverage useful behaviors from other tasks during off-policy data collection, guided by the Q-function of the current task to identify beneficial actions. Unlike traditional MTRL methods that rely on uniform sharing or regularization, QMP avoids biasing policy objectives by only sharing behaviors during data collection rather than directly influencing policy updates. Experimental results across various environments, including manipulation and locomotion tasks, demonstrate QMP's capability to accelerate training and improve performance when integrated with existing MTRL frameworks.

### Strengths
1. QMP is designed to complement existing MTRL frameworks, such as parameter sharing and data relabeling. 
2. The authors provide theoretical analysis showing that QMP’s behavior-sharing mechanism preserves the convergence guarantees of the underlying reinforcement learning algorithm.
3. The paper presents extensive experiments across various multi-task environments (e.g., manipulation, navigation, and locomotion).

### Weaknesses
1. QMP requires evaluating Q-values across multiple task policies at each decision step, which could introduce computational overhead, particularly in settings with a large number of tasks. The paper lacks a detailed comparison of computational costs between QMP and baseline methods, which would be helpful for assessing its scalability. Specifically, the paper does not provide a breakdown of the time spent on Q-function evaluations versus other components of the algorithm, such as policy updates or environment interactions. This makes it difficult to assess the true computational bottleneck introduced by QMP. Furthermore, the analysis should consider the memory footprint of storing and processing multiple Q-values and policies, particularly when using parameter sharing, as this could also impact scalability.


### Questions
1. Could you provide some information regarding the computational overhead of QMP?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces QMP (Q-Switch Mixture of Policies), a novel framework for multi-task reinforcement learning (MTRL) designed to improve sample efficiency by selectively sharing behavioral policies across different tasks. Unlike traditional MTRL methods, which rely on parameter sharing or uniform behavior sharing, QMP identifies and shares beneficial behaviors from other tasks based on a Q-function evaluation. This approach enables each task to benefit from the learning progress in other tasks without introducing bias, as only helpful behaviors are integrated into the data collection phase.

### Strengths
1. The QMP framework introduces a Q-value-based behavior selection mechanism that enables selective behavior sharing in multi-task reinforcement learning (MTRL), enhancing sample efficiency.
2. The extensive experimental results across diverse domains—manipulation, navigation, and locomotion—demonstrate QMP’s performance compared to traditional behavior-sharing baselines, showcasing its practical impact in different tasks.

### Weaknesses
1. This paper only proposes a multi-task data sampling strategy implemented within an off-policy framework, which is limited in scope and shows limited improvement in more complex tasks, such as MT10 and MT50. The method's reliance on off-policy data collection restricts its applicability to on-policy algorithms, potentially limiting its broader impact in the field. Furthermore, the observed performance gains on complex tasks like MT10 and MT50 are marginal, raising concerns about the scalability of the proposed approach.
2. The other algorithms in paper [1] achieved better results with fewer interactions with the environment during training. I think that the method proposed in this paper makes a limited contribution to the field of multi-task reinforcement learning. Specifically, the paper does not adequately address the sample efficiency of the proposed method compared to existing state-of-the-art multi-task reinforcement learning algorithms. The lack of a detailed comparison on the number of environment interactions required to achieve comparable performance makes it difficult to assess the practical benefits of the proposed approach.
3. It is unclear how to ensure avoidance of local optima during complex multi-task transfer processes. The paper lacks a discussion on the potential for negative transfer and how the proposed method mitigates the risk of converging to suboptimal solutions when transferring knowledge across diverse tasks. This is a critical concern, especially in complex multi-task scenarios where tasks may have conflicting objectives.
4. There is a lack of comparison with other MTRL baselines. The paper does not provide a comprehensive comparison with a wide range of multi-task reinforcement learning baselines, making it difficult to assess the relative performance and advantages of the proposed method. The absence of such comparisons limits the ability to contextualize the contribution of this work within the broader landscape of multi-task reinforcement learning.

### Questions
Please see previous section.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a framework for multi-task reinforcement learning (MTRL) called Q-switch Mixture of Policies (QMP), which enables the selective sharing of behaviors between tasks to improve sample efficiency. QMP enhances off-policy data collection by selecting useful behaviors from other task policies based on the task's Q-function. The authors provide theoretical guarantees that QMP improves sample efficiency while preserving the convergence guarantees of reinforcement learning algorithms. Empirical evaluations demonstrate that QMP achieves complementary gains over existing MTRL algorithms in manipulation, locomotion, and navigation environments.

### Strengths
The paper is clearly written with a logical flow. The introduction and problem formulation effectively motivate the need for a new behavior-sharing method, and the diagrams provided help visualize the approach. The results are promising.

### Weaknesses
My impression of this paper is mixed. On the one hand, the authors demonstrate that QMP is effective. However, on the other hand, it's not intuitively clear why QMP works as well as it does. The proposed method is quite simple: it uses the current $Q_i$ function to select the argmax policy $\pi_j^{mix}$. Then, $\pi_j^{mix}$ (rather than $\pi_i$) is used to generate one-step data for training. I have some concerns about the approach of naively taking the maximum over per-task Q-functions—this may not be suitable in general settings, such as more stochastic environments, as it could lead to issues like switching tasks at every step or favoring certain tasks while neglecting others, which is undesirable. If this paper is accepted, it might be perceived as presenting a general framework for MTRL, but I have serious doubts about this claim.

In the introduction section of the paper, it mentions 'These tasks share many similar behaviors, like approaching the tabletop or grasping the object handle.' Therefore, I think 'behavior' refers to an action sequence or subtask that continues for a period of time. However, Algorithm 1 (one-step action sharing) appears to be misaligned with the paper's title and motivation, which emphasizes behavior (action sequence) sharing. The paper's motivation requires significant revision to address this discrepancy.

### Questions
Please refer to the Weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2
