## Human Reviewer 1

### Summary
This paper proposes an attention-weight-based subgoal extraction method to mitigate the extrapolation error problem in offline preference-based reinforcement learning. The experiments are sufficient, and the framework is clear.

### Strengths
1) The authors cleverly introduce the idea of solving extrapolation error in offline RL into reward model training, which is novel.

2) The authors validate the effectiveness of the proposed method through extensive experiments on multiple tasks.

### Weaknesses
1) The algorithm essentially constrains the reward to focus more on the in-distribution data, which may limit the method's generalization capability to some extent.
2) Training the CVAE introduces additional computational cost. Using cosine similarity as part of the reward lacks theoretical motivation and analysis.

### Questions
1) The true ground truth ($g_t$) is obtained via Eq. (5) - is it ultimately randomly sampled from a set? Providing pseudocode for the algorithm is recommended to improve clarity.

2) When training the CVAE, why is the similarity term added rather than subtracted? Shouldn't the regularization be reduced for samples with high similarity?

3) How stable is the CVAE? Do the generated subgoal states truly hold significant meaning in actual trajectories?

4) For manipulation tasks, success rate is the primary concern. How does the algorithm's success rate compare to PT on these tasks?

### Soundness
2

### Presentation
3

### Contribution
2

### Rating
4

### Confidence
3

---

## Human Reviewer 2

### Summary
This paper aims to address a core challenge in Offline PbRL: extrapolation errors in the reward model. The authors propose Subgoal-based Preference Optimization Through Attention Weight, which utilizes an attention-based preference model to extract subgoals and identify critical states within trajectories. Learning is then conducted via reward shaping.

### Strengths
- The problem is well-defined. Extrapolation error in offline PbRL is a real and critical issue.
- The method is novel and intuitive. Transforming attention weights into subgoals is an intuitive approach that makes additional use of attention information.
- SPOT's approach of filtering subgoals based on confidence is interesting.

### Weaknesses
1. SPOT heavily relies on attention weights. However, with limited feedback (especially noisy feedback), the learning process of this attention-based preference model can become very unstable, failing to provide fine-grained importance signals.
2. The experimental setup primarily follows that of Preference Transformer, but two key points from the paper remain unverified. First, the importance of subgoals could be better validated in tasks with original sparse rewards (e.g., AntMaze or Adroit). Second, the paper mentions that reward extrapolation becomes more difficult with noisy preferences, yet no experiments were conducted in noisy environments. Instead, 100% accurate synthetic feedback was used. For example, real human feedback, such as in Uni-RLHF[1], contains noise.
3. The definition of subgoals depends on hyperparameters and heuristic rules. Despite supporting ablation studies, selecting appropriate hyperparameters for different environments is difficult. Additionally, how was the K=10% value chosen?
4. The visualizations show key subgoals for the Hopper task. However, goal-guidance may not provide significant gains in locomotion tasks. It would be beneficial to see visualizations of key states for manipulation and goal-oriented tasks.

[1] Uni-rlhf: Universal platform and benchmark suite for reinforcement learning with diverse human feedback. ICLR2024.

### Questions
- In Table 1, the scores for lift-ph and can-ph are relatively low. Given that algorithms like diffusion policy[2] can achieve 100% success rate in reward-free (e.g., imitation learning) settings, why is the performance on these tasks low?

[2] Diffusion policy: Visuomotor policy learning via action diffusion. IJRR.

### Soundness
3

### Presentation
3

### Contribution
2

### Rating
4

### Confidence
4

---

## Human Reviewer 3

### Summary
This paper introduces a novel method named SPOT, which addresses reward model extrapolation errors in offline PbRL by using subgoals extracted from high-attention weight points on preferred trajectories to improves reward model reliability.

### Strengths
This paper presents a simple approach for offline PbRL that can improve performance to some extent.

### Weaknesses
It also requires training a CVAE in addition to the preference model, which introduces extra computational cost.

### Questions
I have several questions as following:

1.To be honest, novelty of this work is limited. Involving a CVAE after the PT to compute subgoals does not seem very novel, and it also introduces significant extra computation.

2.The experimental results are not sufficiently solid. PT includes AntMaze experiments, and the paper does not compare against more recent baselines such as DTR[1], SEER[2], CPL [3] and more. Including more baselines and tasks would make the results more convincing.

3.It would be helpful to report the increase in training time compared to PT and IPL. I guess the overhead to be substantial.

[1] In-Dataset Trajectory Return Regularization for Offline Preference-based Reinforcement Learning. AAAI 2025.

[2] Efficient preference-based reinforcement learning via aligned experience estimation. 2024.

[3] Contrastive Preference Learning: Learning from Human Feedback without Reinforcement Learning. 2024.

### Soundness
2

### Presentation
2

### Contribution
2

### Rating
4

### Confidence
4