# Learning From Multi-Expert Demonstrations: A Multi-Objective Inverse Reinforcement Learning Approach

- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 3, 5, 3

## Abstract
Imitation learning (IL) from a single expert's demonstration has reached expert-level performance in many Mujoco environments. However, real-world environments often involve demonstrations from multiple experts, resulting in diverse policies due to varying preferences among demonstrators. We propose a multi-objective inverse reinforcement learning (MOIRL) approach that utilizes demonstrations from multiple experts. This approach shows transferability to different preferences due to the assumption of a common reward among demonstrators. We conducts experimental testing in a discrete environment Deep Sea Treasure (DST) and achieved a promising preliminary result. Unlike IRL algorithms, we demonstrate that this approach is competitive across various preferences in both continuous DST and Mujoco environments, using merely a single model within the SAC framework instead of $n$ models for each distinct preference.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper addresses the challenge of utilizing imitation learning in real-world scenarios, particularly when faced with multiple sources of expert data. The authors frame this issue as a multi-objective inverse reinforcement learning problem and introduce a method that exhibits transferability across various preferences. Their experimental findings demonstrate that this approach not only yields competitive results with baseline but also requires fewer computational resources.

### Strengths
1. The paper's notable strength lies in its dedicated attention to a pivotal problem, with the potential to enhance the effectiveness of imitation learning when applied in real-world scenarios.

### Weaknesses
1. Annotating the preference vector $\omega$ can be cumbersome, especially when dealing with a large expert demonstration dataset collected from multiple human expert sources. This manual annotation process may become a bottleneck, particularly when preferences vary significantly among the human experts.

2. The proposed method primarily addresses the challenge of demonstration diversity stemming from different preferences among experts, but it does not explicitly tackle the diversity arising from multi-modality or stochastic behavior within the same preference category. For instance, some experts might have the same preference but choose different paths, such as passing by a tree on the left or the right.

3. The choice of the baseline method appears to be relatively weak. While multi-expert inverse reinforcement learning algorithms are limited, the authors could have selected more advanced IRL methods as baselines and trained a model for each preference individually. This would have provided a better understanding of the proposed method's capabilities by allowing for a more robust comparison.

### Questions
1. What factors contribute to the notably superior performance of MOIQ and GAIL at the early stages of training, when compared to the expert's performance in the Mo-Ant environment, specifically in the preference setting [0.1, 0.9] as depicted in Figure 2?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces a multi-objective Inverse Reinforcement Learning (IRL) approach within the framework of Alternating Direction Method of Multipliers (ADMM). This novel approach not only converges towards optimal solutions but also attains global solutions. The authors establish a link to Inverse Soft Q-Learning and illustrate the efficacy of their algorithm through experimentation on Mo-Mujoco and DST environments.

### Strengths
* Leveraging the theory of ADMM as a foundational framework for Multi-Objective Markov Decision Processes offers an intriguing perspective. This approach enables authors to train a single model, eliminating the need for multiple models catering to distinct preferences.

* The authors have developed an approach, grounded in the inverse Bellman operator, that can efficiently scale to both discrete and continuous tasks.

### Weaknesses
 * The related works are quite limited. A more thorough review should be presented.

* The experimental results, while valuable, would benefit from a more comprehensive analysis. Currently, the authors only compare their proposed algorithms to Generative Adversarial Imitation Learning (GAIL), and it's worth noting that in the Mo-walker and Mo-Ant environments, the Average Return of MOIQ performs worse than GAIL. Additional analyses are necessary to provide a more complete evaluation of these experiments.

* The author's use of the variable 'w' is somewhat ambiguous as it is defined multiple times in the paper. It is unclear whether 'w' represents the preference of the expert or a d-dimensional probability vector. Clarification is needed on this aspect.

### Questions
* Could the authors provide a clear definition of the symbol $\rho$ in Equation (3), and elaborate on the method for determining its value?"

* The authors impose a constraint that $r_i = r$ even when expert demonstrations exhibit heterogeneity. Does the use of a common reward function imply the treatment of all demonstrations as homogeneous? 

* It would be valuable if the authors could provide a more in-depth explanation regarding the instability observed in the transfer experiments, particularly in the Mo-HalfCheetah and Mo-Walker environments.

* Could the author please illustrate the distinction between the common reward function and the ground-truth reward function?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes an inverse reinforcement learning (IRL) framework when the reward function is a vector quantity and the expert demonstration consists of multiple experts. Using the key assumption that those experts share the common reward function, the authors extend the standard IRL framework into a multi-objective case with a linear scalarization function. This MOIRL adopts either the ADMM method for consensus or the inverse deep soft-q learning technique. Numerical results show that the proposed MOIQ algorithm produces a single model covering various expert demos from different preferences.

### Strengths
- This paper addresses multi-objective inverse reinforcement learning (MOIRL) framework, which seems to provide a new perspective.
- The paper provides some mathematical formula regarding the framework. 
- Based on ADMM and inverse soft-Q learning, the proposed methodology gives technical soundness.

### Weaknesses
There are several fundamental discussions regarding the assumption of the proposed method, most of which is not clarified to me.
1) Is it valid in practice if we assume we know the number of multiple experts which produced the whole demonstration?
2) Is it valid in practice if we assume each multiple experts produced equal contribution to produce the whole given demonstration (since the formulation?
3) Is it valid in practice if we assume we know each preference (omega_i) of each expert? It seems that using 3 expert of [0.1,0.9], [0.5,0.5],[0.9,0.1] is a strong assumption.

4. In related work, two methods of MOIRL are introduced. Should these be encompassed in the baseline algorithm?

5. Can the proposed method applicable to other algorithm than SAC framework?

### Questions
Please check the above weakness part. Additional questions are as follows.

6. Can we use MOIQ for discrete case?

7. In Table 1, how MOIQ sometimes outperform expert?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Summary: The authors propose a multi-objective inverse reinforcement learning approach that can learn from multiple experts. Towards this purpose, the authors formulate an approach that learns the common reward across demonstrators utilizing the alternating direction method of multipliers (ADMM) in the discrete case and build on IQ-Learn in the continuous case. The authors present details regarding their approach and preliminary work. Finally, the authors conclude by presenting an evaluation in several domains by creating varying-preferenced demonstrators as the training data. The results are positive in some domains, with the quality of demonstrator imitation varying given the preference.

### Strengths
This paper has several strengths:
+ To the best of my knowledge, solving for the common reward with consensus ADMM is novel. Further extending the IQ-learn framework to the field of MOIRL is novel.
+ Presenting results on each preference individually is beneficial, paints a picture of the algorithm's full performance, and can display features such as mode collapse.

### Weaknesses
 - The novelty of this paper is not clear with respect to a string of prior works that utilize a very similar approach (inferring a common reward function to learn from heterogeneous demonstrations). Could you clarify how your work differs from the work below?
1. Joint Goal and Strategy Inference across Heterogeneous Demonstrators via Reward Network Distillation (https://arxiv.org/abs/2001.00503)
2. Fast Lifelong Adaptive Inverse Reinforcement Learning from Demonstrations (https://arxiv.org/abs/2209.11908)
3. InfoGAIL
- Further, as learning from heterogeneous demonstrators has been studied for several years, it would be beneficial to compare against a framework that attempts to accomplish this goal. It would be expected that a baseline like GAIL will underperform the proposed approach.
- It isn't clear how the preferences were designed in Section 5 and how the preferences result in different behaviors qualitatively. Specifically, what are the explicit reward function weights used for each preference, and how do these differences manifest in the demonstrated behavior? For example, in a navigation task, does one preference prioritize speed while another prioritizes a shorter path, and how is this reflected in the reward function?
- Justifications should be added for the critic and policy update simplifications in 4.2.2. It is unclear why these simplifications are valid, and how they affect the convergence or performance of the algorithm. For example, what are the implications of using a simplified update rule for the critic, and how does this relate to the theoretical convergence properties of the algorithm?
- The results would benefit from more detail and justification. It is unclear why the proposed approach underperforms GAIL in some instances. For example, in what specific scenarios does GAIL outperform the proposed method, and what characteristics of these scenarios might explain this behavior? Are these cases where the underlying assumptions of the proposed method are violated?
- The paper could benefit from a read-through to improve clarity and grammar.

### Questions
Could you please address the weaknesses mentioned above?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
