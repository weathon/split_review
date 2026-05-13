# Causal Information Prioritization for Efficient Reinforcement Learning

- Decision: Accept
- Scores: 5, 6, 8

## Abstract
Current Reinforcement Learning (RL) methods often suffer from sample-inefficiency, resulting from blind exploration strategies that neglect causal relationships among states, actions, and rewards. Although recent causal approaches aim to address this problem, they lack grounded modeling of reward-guided causal understanding of states and actions for goal-orientation, thus impairing learning efficiency. To tackle this issue, we propose a novel method named Causal Information Prioritization (CIP) that improves sample efficiency by leveraging factored MDPs to infer causal relationships between different dimensions of states and actions with respect to rewards, enabling the prioritization of causal information. Specifically, CIP identifies and leverages causal relationships between states and rewards to execute counterfactual data augmentation to prioritize high-impact state features under the causal understanding of the environments. Moreover, CIP integrates a causality-aware empowerment learning objective, which significantly enhances the agent's execution of reward-guided actions for more efficient exploration in complex environments. 
To fully assess the effectiveness of CIP, we conduct extensive experiments across $39$ tasks in $5$ diverse continuous control environments, encompassing both locomotion and manipulation skills learning with pixel-based and sparse reward settings. Experimental results demonstrate that CIP consistently outperforms existing RL methods across a wide range of scenarios.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces Causal Information Prioritization (CIP) to address sample inefficiency in reinforcement learning by leveraging causal relationships between states, actions, and rewards. CIP uses factored Markov Decision Processes (MDPs) to model these causal relationships and employs techniques like counterfactual data augmentation to improve sample efficiency. The framework is tested across various tasks, including manipulation and locomotion, to showcase its effectiveness in different environments.

### Strengths
- The paper presents an interesting approach by integrating causal reasoning with reinforcement learning (RL), which could potentially lead to better sample efficiency by filtering out irrelevant features.
- The focus on causality and counterfactual augmentation aligns with a growing area in RL, aiming to make models more effective with fewer interactions by prioritizing meaningful features.
- The experiments cover diverse environments and tasks, which is valuable for assessing the generalizability of the approach.

### Weaknesses
 - The paper seems to need more references and discussion around object-centric MDPs and related works in object-centric world modeling and MDP homomorphism, which are relevant areas given the nature of CIP.
- The proposed framework appears to require considerable task-specific engineering, as it doesn’t seem to inherently learn the causal structure but rather relies on manually provided task structures. This may limit its scalability and adaptability to new tasks without re-engineering.
- Empirical results, especially in Table 1, show limited improvement over baselines like ACE and BAC. The gains aren’t always significant, especially given the complexity and additional engineering that CIP requires. The benefits may not justify the added complexity in some cases.
- Some results in Table 1 indicate the CIP approach performs on par with or even below baselines for certain tasks, suggesting that the improvements might not generalize strongly across all evaluated environments.

### Questions
- How does CIP address the need for task-specific causal structure input? Is it possible to reduce the engineering effort required for this, or is the approach dependent on manual structure provision?
- Were there specific reasons for the chosen baselines (ACE, BAC)? Would other baselines, particularly those that handle causality differently, add more context to the results?
- What are the plans for integrating 3D world understanding or extending CIP to work more naturally with object-centric or high-dimensional MDPs without predefined causal structures?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces CIP, the causal information prioritization method that leverages causal information in reinforcement learning to improve learning efficiency. Comprehensive experiments are conducted to verify the proposed method.

### Strengths
The paper is well-organized. The presentation is mostly clear. The experiment section is comprehensive.

### Weaknesses
1. Several related works are missed:

[1] Sun, Yuewen, et al. "ACAMDA: Improving Data Efficiency in Reinforcement Learning Through Guided Counterfactual Data Augmentation." Proceedings of the AAAI Conference on Artificial Intelligence. Vol. 38. No. 14. 2024.

[2] Sun, Hao, and Taiyi Wang. "Toward Causal-Aware RL: State-Wise Action-Refined Temporal Difference." arXiv preprint arXiv:2201.00354 (2022).

2. The limitation section in the current paper is not really a discussion of the limitations of the proposed method.

### Questions
Will the proposed method be suitable for offline RL or has it to be applied with online explorations?

Can the authors provide more analysis on the pitfalls of the proposed method? What is the trade-off of the proposed method, and under what cases would this method face challenge? e.g. computational burden, can not handle highly stochastic environments? 

I appreciate the authors' efforts in their large-scale experiments, yet I have concerns about the statistical significance of the performance. On some of the tasks, the performance seems to have large variances. I wonder what would be the recommended hyper-parameter setups from the authors, and is the proposed method stable/robust to different hyper-parameter settings?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The paper proposes a novel reinforcement learning (RL) approach called Causal Information Prioritization (**CIP**), designed to address sample inefficiency by leveraging causal reasoning. CIP focuses on prioritizing causal relationships between states, actions, and rewards in reinforcement learning tasks, thus guiding the agent to focus on the most impactful behaviors. CIP improves sample efficiency by leveraging factored Markov Decision Processes (MDPs) to infer causal relationships and using counterfactual data augmentation. It integrates a causality-aware empowerment learning objective that enhances goal-directed action execution, leading to more efficient exploration. The approach is validated experimentally across 39 tasks in five diverse environments involving continuous control, demonstrating superior performance over existing RL techniques in terms of both sample efficiency and task success rates.

### Strengths
Integrating the causality-aware empowerment objective into the policy optimization objective alongside strong, extensive experimental results - demonstrating its ability to outperform several state-of-the-art RL methods, particularly in challenging environments with sparse rewards and high-dimensional action spaces - makes the paper a valuable contribution to the RL community.

**Originality**: The combination of causal reasoning with empowerment learning for reinforcement learning is a novel and creative approach.

**Quality**: The paper is well-researched and technically rigorous, with solid theoretical foundations and thorough experimental validation.

**Clarity**: The motivation and design of CIP are well-explained, with intuitive examples such as the robot-arm manipulation scenarios. The illustrations help make abstract concepts more accessible.

**Significance**: CIP addresses an important issue in reinforcement learning—sample inefficiency—by leveraging causal relationships, which has the potential for broad applicability in complex environments.

### Weaknesses
 **Complexity of Empowerment Calculation**: The use of empowerment as part of the learning objective, though promising, involves additional computational complexity. The paper would benefit from a more in-depth discussion of how computational costs compare to the gains in sample efficiency, especially for tasks with very high-dimensional action spaces. Specifically, the paper should analyze the time complexity of the empowerment calculation, considering the number of state and action dimensions, and how this scales with the size of the environment. A comparison of the wall-clock time for training with and without the empowerment objective would provide a more concrete understanding of the computational overhead.

**Generalizability and Assumptions**: The reliance on the DirectLiNGAM method for causal discovery may limit generalizability in real-world environments where non-linear relationships are common. Exploring alternative causal discovery methods could enhance robustness. The paper should discuss the limitations of DirectLiNGAM, such as its assumption of acyclic graphs and linear relationships, and how these assumptions might affect the performance of CIP in more complex environments. It would be beneficial to see experiments with datasets that violate these assumptions to understand the sensitivity of the method.

**Empirical Comparisons**: While CIP is compared to standard baselines like SAC and ACE, further empirical comparisons to model-based RL approaches or hybrid methods would strengthen claims regarding sample efficiency and generalization capabilities. The paper should include comparisons to model-based methods that also leverage causal reasoning or latent dynamics models. This would help to better contextualize the performance of CIP and highlight its unique advantages or limitations compared to these alternative approaches.

### Questions
**Questions**

1. Could the authors elaborate on how CIP could be adapted or extended to discrete action spaces, where causal dependencies may be more rigid?

2. How does CIP handle potential **inaccuracies in causal discovery** during the learning process? Is there a mechanism in place to correct or adapt the causal models if they are misaligned with the environment dynamics?

3. **Causal Discovery**: Could the authors elaborate on the choice of DirectLiNGAM for causal discovery? Have other causal discovery techniques been tested, and if so, how do they compare in terms of performance and sample efficiency?

4. Assumptions of DirectLiNGAM: How sensitive is CIP to the assumptions required for the DirectLiNGAM method (e.g., linearity and Gaussian noise)? Would non-linear extensions of causal discovery alter CIP's effectiveness?

5. **Computational Overhead**: Could you provide a more detailed analysis of the computational costs associated with empowerment calculations compared to traditional entropy regularization approaches?

### Soundness
4

### Presentation
3

### Contribution
4
