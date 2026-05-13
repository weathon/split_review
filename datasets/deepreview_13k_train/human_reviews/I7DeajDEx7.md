# Episodic Novelty Through Temporal Distance

- Decision: Accept
- Scores: 8, 6, 8, 5

## Abstract
Exploration in sparse reward environments remains a significant challenge in reinforcement learning, particularly in Contextual Markov Decision Processes (CMDPs), where environments differ across episodes. Existing episodic intrinsic motivation methods for CMDPs primarily rely on count-based approaches, which are ineffective in large state spaces, or on similarity-based methods that lack appropriate metrics for state comparison. To address these shortcomings, we propose Episodic Novelty Through Temporal Distance (ETD), a novel approach that introduces temporal distance as a robust metric for state similarity and intrinsic reward computation. By employing contrastive learning, ETD accurately estimates temporal distances and derives intrinsic rewards based on the novelty of states within the current episode. Extensive experiments on various benchmark tasks demonstrate that ETD significantly outperforms state-of-the-art methods, highlighting its effectiveness in enhancing exploration in sparse reward CMDPs.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces Episodic Novelty through Temporal Distance (ETD), a new approach for exploration in Contextual Markov Decision Processes (CMDPs) with sparse rewards. ETD uses temporal distance as a metric for state similarity to compute intrinsic rewards, encouraging agents to explore states that are temporally distant from their episodic history. The authors employ contrastive learning to design a quasimetric that estimates episodic temporal distances. They evaluate  ETD when combined with PPO on various CMDP benchmarks, i.e., MiniGrid, and Crafter (pixel-based observations), and MiniWorld (pixel-based observations).

### Strengths
1. The paper introduces a novel method to use temporal distance as a (quasi)metric for state similarity.
2. The paper conducts extensive experiments across multiple CMDP environments, comparing ETD to several baseline methods.
3. ETD + PPO demonstrates robust performance improvements, especially in challenging sparse reward scenarios.
4. Results on extensive experiments across multiple CMDP environments, comparing ETD to several baseline methods have been reported.
5. The paper is well-structured, with clear explanations of the motivation, methods, and results.

### Weaknesses
1. The proposed ETD doesn’t take into consideration extrinsic rewards to compute similarity. Intuitively, states with similar rewards could be considered similar in terms of the task objective [1]. This is a significant limitation, especially in environments where reward signals, even if sparse, provide critical information about the task's progress. The current approach risks treating states that are functionally very different (in terms of achieving the goal) as similar if they happen to be close in temporal distance, and vice-versa.
2. The approach has been primarily tested on discrete action spaces, and its effectiveness in continuous action domains such as MuJoCo [2], DeepMind Control Suite [3], or Fetch [4] environments remains unexplored. This limits the generalizability of the method, as many real-world robotic tasks operate in continuous action spaces. The absence of experiments in these environments makes it difficult to assess the practical applicability of ETD in more complex settings.

### Questions
1. Could the authors shed light on why PPO, an on-policy algorithm, was chosen to be combined with ETD instead of off-policy algorithms such as DQN or SAC? Prior work has used off-policy algorithms extensively for sparse-reward tasks [2] [3].
2. Is ETD straightforward to be extended to continuous action spaces? If so, did the authors run any experiments? If not, what could be possible bottlenecks?
3. Did the authors consider combining temporal distance with reward-based similarity, or explore weighting the temporal distance based on extrinsic rewards? Are there any potential trade-offs or challenges in incorporating extrinsic rewards into the similarity metric that the authors anticipate?

[2] Andrychowicz, Marcin, et al. "Hindsight experience replay." Advances in neural information processing systems 30 (2017).

[3] Co-Reyes, John D., et al. "Evolving reinforcement learning algorithms." arXiv preprint arXiv:2101.03958 (2021).

### Soundness
3

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
3

### Summary
This paper presents a novel reinforcement learning approach to measure similarities between visited states, using the resulting state distances as a reward bonus to encourage exploration in tasks with sparse rewards. The methodology is technically sound, and the results are promising.

### Strengths
- The paper is well-written, with a clear and cohesive narrative. Most technical details are effectively conveyed through illustrative figures and results from intuitive toy tasks.
- The experimental tasks are appropriately chosen, providing sufficient complexity to evaluate the approach.
- The experimental results, along with ablation studies, clearly demonstrate the advantages of the proposed method over other baselines.
- The paper offers a comprehensive analysis and comparison of different technical approaches used by the proposed method and baseline methods, providing valuable insights for readers.

### Weaknesses
## MDP assumption
The definition of the intrinsic bonus reward violates the MDP assumption. In section 2, the total reward $r(s_t, a_t, s_{t+1})$ is a decomposed as the environment reward $r_t^e$ plus the weighted bonus $\beta b_t$. However, $b_t$ is a function that depends on the visited states within the episode, which disrupts the definition of total reward and violates the MDP assumption. In this case, the visited states influences the intrinsic reward, potentially harming the policy built upon MDP, as the actions are solely selected by $\pi(a_t|s_t)$ without knowledge of the states' visiting history. Consequently, the same action $a_t$ may yield completely different rewards $r_{t+1}$, depending on whether the $s_{t+1}$ has been visited in the history or not. This introduces a non-Markovian element into the reward structure, as the reward at time $t$ is not solely determined by the current state and action, but also by the history of visited states within the episode. This deviation from the Markov property can lead to instability and suboptimal learning, as the core assumptions of many RL algorithms are violated. I believe this is a critical technical issue in this paper, and should be explained thoroughly. At the same time, do other related works using reward bonuses also encounter the same issue?

## Unclear content
The content between lines 186 and 208 is challenging to follow. I suggest the authors restructure this section, providing additional explanations and intuitions. Specifically:
- The meaning of the sentence, "Contrastive learning can estimate the successor distance when positive samples are drawn from the discounted state occupancy measure," is unclear. What does it mean to draw samples from a measure? The concept of sampling from a discounted state occupancy measure needs further clarification. It is not immediately obvious how this sampling process is implemented in practice and what its implications are for the learned distance metric.
- The motivation for using the energy function and its decomposition into the potential net and quasimetric net in practice is unclear. What is this energy function, and why is it applied here? The connection between the energy function and the desired distance metric is not well-established. The specific form of the energy function and its relationship to the contrastive loss should be explained more clearly. Furthermore, the rationale behind decomposing it into potential and quasimetric networks requires more justification.
- The rationale behind using the infoNCE loss also needs further explanation. While infoNCE is a common contrastive loss, its specific suitability for this task and its connection to the desired distance metric should be made more explicit. The relationship between the loss function and the properties of the learned distance metric is not clearly articulated.

## Minor issues
- The SpiralMaze in Figure 2 appears to have a linear structure, which may not effectively demonstrate ETD's advantage in distance learning. A more complex example could better illustrate the method's strengths. The current example does not adequately showcase the method's ability to learn meaningful distances in complex environments. A more challenging environment with multiple paths and loops would be more appropriate.
- What is the best practice of choosing the $\beta$? I think it depends on the specific task and is therefore a HP. The paper should provide more guidance on how to select the $\beta$ parameter. While it is acknowledged that this parameter is task-specific, some general guidelines or heuristics would be helpful for practitioners.
- Line 188, there should be a $ds$ in the integral.

### Questions
Please address the issues listed in the weaknesses section.

### Soundness
3

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
4

### Summary
The paper presents a new intrinsic reward for novelty-based reinforcement learning. The intrinsic reward is based on the estimated temporal distance between two states, which estimates the probability that one state can be reached from another state in multiple time steps. Here, discounting is used to give preference for shorter transitions. The temporal distance is learned by a contrastive loss based on the infoNCE loss. The algorithm is compared against several baseline methods on a wide variety of discrete action exploration tasks and shows promising performance.

### Strengths
- A well motivated new intrinsic reward signal for RL
- The concept is simple and provides a strong performance
- Exhaustive evaluations, good comparisons the baseline methods as well as nice ablations
- Good insights why baseline methods fail

### Weaknesses
the paper is already of high quality and I could not find major weaknesses. Minor weaknesses are given in the questions section.

- a more detailed discussion on the successor distance and its assumptions would be insightful. E.g., what happens if the MDP does not allow for loops (which is the case we have to deal with real dynamics, e.g. velocities). Then this distance would be infinite, wouldnt it?
- More insights on the parametrization of the energy function. Why do we need separate networks for  the potential and the assymetric distance? Could we also ablate removing the potential here?
- Why do we need to "symmetrize" the infoNCE loss? Does this imply that transitions are "invertible"? Also here, a ablation and more discussion would be nice.

### Questions
- a more detailed discussion on the successor distance and its assumptions would be insightful. E.g., what happens if the MDP does not allow for loops (which is the case we have to deal with real dynamics, e.g. velocities). Then this distance would be infinite, wouldnt it?
- More insights on the parametrization of the energy function. Why do we need separate networks for  the potential and the assymetric distance? Could we also ablate removing the potential here?
- Why do we need to "symmetrize" the infoNCE loss? Does this imply that transitions are "invertible"? Also here, a ablation and more discussion would be nice.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper addresses the challenge of exploration in sparse reward environments within Contextual Markov Decision Processes (CMDPs), where environments vary between episodes. The authors propose Episodic Novelty Through Temporal Distance (ETD), a method that leverages temporal distance as a metric for state similarity and intrinsic reward computation. Using contrastive learning, ETD estimates temporal distances to assign intrinsic rewards based on the novelty of states within an episode. Experimental results on diverse benchmark tasks show that ETD outperforms state-of-the-art methods, enhancing exploration in sparse reward CMDPs. The paper is well-structured and detailed, and the ETD method is well-described.

### Strengths
The paper compares the proposed method with various existing approaches (including DEIR, NovelD, E3B, EC, NGU, RND, and the Count-based method), covering many classical and common algorithms in the exploration field. By testing these methods across multiple benchmark environments, the paper demonstrates the advantages of the ETD method in sparse reward and high-dimensional pixel environments, validating its applicability across different exploration demands and tasks.

### Weaknesses
1. The core approach of ETD primarily builds upon the main idea of "Learning Temporal Distances: Contrastive Successor Features Can Provide a Metric Structure for Decision-Making," using contrastive learning to estimate temporal distance. It lacks substantial algorithmic innovation.
The innovation of the ETD (Episodic Temporal Distance) method primarily lies in its approach to learning temporal distances. However, this method closely follows key aspects of the referenced work, "Learning Temporal Distances: Contrastive Successor Features Can Provide a Metric Structure for Decision-Making," in several crucial areas:
1) Discounted State Occupancy Measure: In the ETD method, the discounted state occupancy measure p^\pi_\gamma(s_f = y | s_0 = x) is used to estimate the transition probability from state x to y . The formula is as follows: p^\pi_\gamma(s_f = y | s_0 = x) = (1 - \gamma) \sum_{k=0}^{\infty} \gamma^k p^\pi(s_k = y | s_0 = x) This formula originates from "Learning Temporal Distances," where the discounted state occupancy measure p^{\pi}_{\gamma} is defined as the discounted distribution over future states s^{+} : p^{\pi}_{\gamma}(s^{+} = s' | s_0 = s) = (1 - \gamma) \sum_{k=0}^{\infty} \gamma^k p^{\pi}(s_k = s' | s_0 = s)
2) Successor Distance: The successor distance formula used in ETD is also directly derived from the referenced work, "Learning Temporal Distances."
3) Loss Function: Both works adopt a symmetrized InfoNCE loss function to train the model through contrastive learning, which is a critical component of the approach.
4) Energy Function: The energy function utilized in ETD, f_{\theta = (\phi, \psi)}(x, y) = c_{\psi}(y) - d_{\phi}(x, y) , is also sourced from "Learning Temporal Distances," where it is presented as: f_{\phi, \psi}(s, a, g) = c_{\psi}(g) - d_{\phi}(s, a, g)


2. Experiments are conducted solely on discrete control tasks, with no tests on continuous control tasks (e.g., robot control tasks in Meta-World and Mujoco). State spaces in discrete control tasks are relatively small, allowing agents to explore enough states within a shorter timeframe. In contrast, continuous control tasks present larger state spaces and greater exploration challenges, making it essential to validate the method’s effectiveness in these scenarios. Given that many real-world tasks involve continuous control, this omission limits the method's persuasiveness for broader application scenarios.
3. The absence of publicly available code restricts the ability to independently verify the method's effectiveness.

### Questions
1. Please test the performance of ETD on continuous control tasks.
To evaluate the ETD method in continuous control tasks, the authors could consider tasks in environments such as Meta-World (or Panda-Gym) and Mujoco. Examples of basic tasks include "Push," "Reach," and "Pick-Place" in Meta-World (or Panda-Gym), which offer high environmental complexity and sparse reward settings, making them suitable for assessing ETD's exploratory capabilities. Additionally, Mujoco environments like "Cheetah-Vel-Sparse," which have high-dimensional state spaces, could further validate ETD’s performance in high-dimensional continuous spaces. By plotting and comparing learning curves across environments—such as average episode rewards or success rates over training steps—the authors could demonstrate whether ETD converges faster or more stably in sparse reward continuous control tasks compared to other methods.

2. Please provide code.

### Soundness
3

### Presentation
3

### Contribution
2
