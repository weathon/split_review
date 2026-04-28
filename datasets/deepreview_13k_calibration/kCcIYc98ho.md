# Mixing Corrupted Preferences for Robust and Feedback-Efficient Preference-Based Reinforcement Learning

- Decision: Reject
- Avg Score: 5.67
- Scores: 5, 6, 6

## Abstract
Preference-based reinforcement learning (RL) trains agents using non-expert feedback without the need for detailed reward design. In this approach, a human teacher provides feedback to the agent by comparing two behavior trajectories and labeling the preference. Although recent studies have improved feedback efficiency through methods like unsupervised exploration to collect various trajectories and combined self- or semi-supervised learning for unlabeled queries, they often assume flawless human annotation. In practice, human teachers might make mistakes or have conflicting opinions about trajectory preferences. The potential negative impact of such corrupted preferences on capturing user intent remains an underexplored challenge. To address this challenge, we introduce mixing corrupted preferences (MCP) for robust and feedback-efficient preference-based RL. Mixup has shown robustness against corrupted labels by reducing the influence of faulty instances. By generating new preference data through the component-wise mixing of two labeled preferences, our method lessens the impact of corrupted feedback, thereby enhancing robustness. Furthermore, MCP improves feedback efficiency: even with limited labeled feedback, it can generate unlimited new data. We evaluate our method on three locomotion and six robotic manipulation tasks in B-Pref benchmark, comparing it with PEBBLE in contexts with both perfectly rational and imperfect teachers. Our results show that MCP significantly outperforms PEBBLE, requiring fewer feedback instances and a shorter training period, highlighting its superior feedback efficiency.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a new preference-based RL method that utilizes mix-up to augment the preference labels. Specifically it samples two pairs of data and mixes up the state and actions with a linear combination and also the label for two segments. The method is mainly evaluated on B-Pref benchmark, showing that the method can improve the performance of baseline methods such as PEBBLE and SURF.

### Strengths
- Tackles an interesting and important problem of preference-based RL
- Clear and easy writing
- Extensive experiments

### Weaknesses
 - The main weakness of the method is it's not clear how exactly this method improves the performance, given that it's not clear what exactly the linear combination of state and action would mean and how using them for learning rewards could improve the robustness. Mixed-up values in each dimension could lie in *valid* state and action space because their value would lie between the min and max value of spaces, but as a whole, it's very unlikely that the state and action would be valid state and actions. For instance, linear combination of two proprioceptive states of 7-dof arm is very likely to lead to physically infeasible joint positions, and there's no guarantee that it'll be meaningfully connected to linear combination of labels. Without thorough investigation and support in this point, it's very difficult to justify the usage of method in many cases.
- Also the main weakness is that a lot of experimental results are not statistically significant, and the improvements over PEBBLE and SURF are very weak. At least the number of seed should be significantly increased and also other metrics from [rliable](https://github.com/google-research/rliable) could be considered.

### Questions
Please address my concerns in Weaknesses. The paper is well written and clear so that I don't have a lot of questions. But two main weaknesses are so crucial that I want them to be addressed.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work introduces Mixed Corrupted Preferences (MCP), a form of mixup for trajectories and preferences for Preference-based Reinforcement Learning (PbRL). 

Through experiments with MetaWorld and DeepMind Control Suite (DMC), the paper shows MCP leads to increased feedback robustness, measured by higher final policy performance when training PbRL with highly noisy preferences.

### Strengths
* The paper is well-written and easy-to-follow.
* The results are both thorough (multiple tasks with different amounts of feedback) and compelling (with MCP trained with a mistake labeller usually reaching or even beating the performance of PEBBLE trained with an oracle labeller).
* The authors show that MCP is beneficial in combination with other PbRL algorithms that improve sample efficiency.

### Weaknesses
 * _W1_: No analysis with actual humans-in-the-loop. Given that the main goal of MCP is to increase the robustness of PbRL, verifying whether MCP is indeed beneficial is an important ablation. 
* _W2_: The assumption of convex states and actions seems pretty strong, and it is hard to gauge whether it has an actual effect on training.

### Questions
* _Q1_: [Followup from _W2_] Could you provide an analysis of what proportion of states end up being invalid for MetaWorld and DMC? For instance, by randomly mixing up states and actions, and using a simulator to verify whether the interpolated states are valid.
* _Q2_: In equation (8),  what happens if only interpolated trajectories are used? 
* _Q3_: How are the initial trajectories that are used for mixup selected? Is it based on uncertainty like in PEBBLE? Does the initial selection affect performance of MCP?
* _Q4_: The authors do not provide any intuition about the role of the beta distribution. Could you explain how you arrived to the values used in the experiments?

**Nitpicks and suggestions (will not affect rating)**

* Please use vector graphics for figures, they are currently very blurry when zoomed in.
* Figure 1's caption needs to be expanded upon. I would also use the extra space could also be used to indicate that the trajectories and the labels are used for reward-learning.
* The description of the plots in Section 4 (page 5), is far away from the actual plots.
* Could you add final performance tables for all the experiments. Sometimes it is hard to see which of the methods does better and by how much.
* For figure 4, could you use a boxplot or a violin plot? It would be interesting to see if there are any spearman correlation outliers in each of the tasks and algorithms.
* In the Related Work section, I suggest changing "discovered" to "investigated", to avoid a debate whether algorithms are discovered or invented.
* In the Related work section, I would incorporate the use of mixup in representation learning and computer vision.
* The limitations of the method are currently stated as future work. I suggest to write them as limitations, since it is clearer to the readers.


**[[Post-rebuttal update]]**

All questions were addressed in the rebuttal. Please refer to the discussion for details.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper investigates a critical issue within existing PbRL techniques, particularly focusing on the potential adverse effects stemming from corrupted preferences provided by non-expert human labelers. To address this problem, the authors propose a novel approach called Mixing Corrupted Preferences (MCP). This method involves applying a Mixup technique to augment the data, enhancing the model's robustness against faulty instances and improving feedback efficiency, even when working with limited data. The effectiveness of this method is evaluated against state-of-the-art techniques in a standard PbRL benchmark. The results demonstrate that the proposed MCP method outperforms PEBBLE in terms of both robustness and feedback efficiency, while also effectively complementing SURF. A key contribution of this work lies in introducing the Mixup technique into the PbRL framework, thereby bolstering its robustness and feedback efficiency, particularly when dealing with corrupted preference data.

### Strengths
While most recent works concentrate on enhancing the feedback efficiency of PbRL, the authors focus on the challenges stemming from the data quality of collected human preferences, a factor that can profoundly influence the learning process and the performance of the RL agent. This issue is relatively underexplored but holds great significance within the PbRL framework. I appreciate the authors for dedicating their efforts to address this crucial topic.

Furthermore, the idea of the proposed method is elegantly straightforward. It requires only data processing and doesn't necessitate the introduction of complex learning algorithms. This simplicity renders it easily implementable and adaptable to nearly all existing state-of-the-art methods within the conventional PbRL frameworks. In terms of presentation, I feel the paper is well-organized and easy to read.

### Weaknesses
In section 3, a strong assumption is made regarding the state and action space, specifically assuming convexity. While the authors briefly mention limitations in the future work section, a more comprehensive discussion of the implications of this assumption is necessary. For instance, the linear interpolation of states and actions may lead to physically implausible or infeasible transitions, especially in complex environments with non-linear dynamics. This could introduce biases in the learning process, potentially hindering the agent's ability to generalize to real-world scenarios. The paper should include a more detailed analysis of how this assumption affects the validity of the generated mixed trajectories and the overall performance of the method. For the experimental design, I think it could benefit from a more thorough comparison with state-of-the-art PbRL methods, particularly SURF, which also employs data augmentation for PbRL. The current comparison is not sufficient to demonstrate the superiority of the proposed method. Additionally, it may be pertinent to consider the paper on RL from diverse humans [1] as a closely related work that approaches the issue of corrupted human preferences as well in a distinct manner. This comparison would be crucial for evaluating the robustness in handling corrupted preferences. However, the authors may not be aware of this work, and they are not the first to address the issue of corrupted preferences. Furthermore, I recommend introducing the Mixup techniques in the preliminary section to enhance the paper's flow. Finally, while I acknowledge the challenges in conducting real human experiments for PbRL in complex control tasks, this work could be further strengthened with user studies conducted with a diverse group of non-expert human labelers. The absence of such experiments limits the practical relevance of the findings.

### Questions
1. What are the potential negative impact of corrupted preference? What might the newly generated trajectory look like? How do they mitigate the negative impacts? Could you provide some concrete examples for illustration? It is a bit vague to me.

2. Could you briefly explain in which cases the proposed MCP approach may not work effectively?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
