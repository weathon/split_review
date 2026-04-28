# Perlin Noise for Exploration in Reinforcement Learning

- Decision: Reject
- Avg Score: 4.67
- Scores: 3, 6, 5

## Abstract
Reinforcement Learning (RL) enables agents to solve tasks by autonomously acquiring policies by interacting with the environment receiving sparse or noisy feedback in the form of a reward. However, achieving successful optimization in RL requires efficient exploration, which remains a significant challenge, particularly in continuous action spaces. Existing exploration techniques often exhibit limited state-space reach and fail to overcome local optima, resulting in suboptimal policies. Additionally, these techniques can cause erratic movements, posing risks when applied to real-world robots.
In this work, we introduce a novel exploration strategy leveraging Perlin Noise, a gradient noise function that generates smooth, continuous disturbances, thus enhancing the agent's performance by promoting structured exploration and fluid motions. We quantitatively demonstrate the benefits of our approach compared to state-of-the-art methods, showing that it outperforms both unstructured and structured techniques in thorough experimental evaluations.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes using Perlin noise as a drop-in replacement to other forms of noise for any RL algorithm, and demonstrates improvements in exploration in terms of both final performance and smoothness on various tasks in many domains.

### Strengths
- The paper is well written with extensive evaluations on various tasks and in various domains.
-  Naively sampling perlin noise and applying it to the actions of the policy makes it impossible to use the reparameterization trick to compute gradients as in SAC. The authors propose a novel approach of first applying perlin noise to the actions and then modeling the resulting policy using a gaussian distribution using the “Normalize” trick. I agree with the authors that this approach is novel and makes it fairly straightforward for any RL practitioner to use it as a drop-in replacement for other forms of exploration noise. 
- The authors demonstrate good performance improvements on select difficult exploration tasks such as Ant maze (Fig. 7) and provide empirical evidence that Perlin noise leads to smoother action trajectories (Fig. 6).

### Weaknesses
 - Perhaps my main concern with this paper is that, at a high level, it simply proposes and investigates a different noise function for PPO. While simple solutions especially if they solve major problems are not necessarily bad, the novelty and technical contribution here is quite limited.

- Since the claim is that Perlin noise provides more smooth, structured exploration independent of the algorithm or task, it seems necessary to have at least one more algorithm beyond PPO to validate this claim. 

-  Figure 5 needs some context on what the task is, what kind of policy was used to collect the trajectory (is it a random policy? Trained policy? Hand-engineered one?), etc. For example, PPO has a learnable action standard deviation parameter that generally tends towards 0 i.e. a deterministic policy as the policy converges. I would then expect that the trajectory, regardless of what kind of noise is applied, to look relatively smooth. It is impossible to make any conclusions without further context here. 

- Final minor complaint: On lines 59-60 the authors contrast against intrinsic-motivation and trajectory-level noise methods by saying  *“However, these methods require additional treatment of the underlying optimization method by changing the objectives or introducing higher-level abstractions of the actions.”*.  Why is this a problem? This is similar to saying “PPO does better than REINFORCE, however it requires additional treatment of the underlying optimization method”. If that “underlying treatment” results in a fundamentally better algorithm, then the research community will adopt this new approach. This, in my opinion, is not a bad thing but rather the natural progression of a field. 

### Questions
No questions at this time.

### Soundness
3

### Presentation
4

### Contribution
1

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces Perlin noise to enhance stochastic policy distributions in reinforcement learning (RL) by encouraging smoother exploration. Perlin noise assigns random gradient vectors to points on a grid and interpolates between them, creating continuous transitions across space, a technique commonly used in computer graphics. The paper details the process of sampling Perlin noise and how it can be leveraged to improve RL policies.

### Strengths
The paper leverages the Perlin noise, which is commonly used in computer graphics to generate smooth textures, effectively generate smooth and temporally related noise for RL policies. The Perlin is introduced mainly aiming to generate smoother and more coherent trajectories, thus leading to more nature movements, which is very important in robotics.

### Weaknesses
1. The paper claims that using Perlin noise broadens exploration, but this aspect is neither theoretically justified nor sufficiently demonstrated experimentally.

2. While the paper compares several noise types, all approaches focus on adding noise to stochastic policy distributions. Many other exploration methods exist, such as entropy-regularized exploration, curiosity-driven exploration, intrinsic motivation-based approach, reward shaping, and novelty-guided exploration. I believe comparisons with some other advanced exploration strategies besides the policy noise based approaches are necessary to fully demonstrate the advantages of Perlin noise in RL.

[1] Haarnoja, T., Zhou, A., Abbeel, P., and Levine, S. Soft actor critic: Off-policy maximum entropy deep reinforcement learning with a stochastic actor. In International Conference on Machine Learning, pp. 1861–1870. PMLR, 2018.

[2] Pathak, Deepak, et al. "Curiosity-driven exploration by self-supervised prediction." International conference on machine learning. PMLR, 2017.

[3] Burda, Y., Edwards, H., Storkey, A., and Klimov, O. Exploration by random network distillation. In International Conference on Learning Representations, 2018.
 
[4] Devidze, R., Kamalaruban, P., and Singla, A. Exploration guided reward shaping for reinforcement learning under
 sparse rewards. Advances in Neural Information Processing Systems, 2022.

[5] Tang, H., Houthooft, R., Foote, D., Stooke, A., Xi Chen, O., Duan, Y., Schulman, J., DeTurck, F., and Abbeel, P. #
 exploration: A study of count-based exploration for deep reinforcement learning. Advances in Neural Information Processing Systems, 2017.

### Questions
1. Regarding Figure 5, I understand that the sampled action trajectories are drawn from a fixed underlying distribution, and it is evident that Perlin noise generates much smoother trajectories. However, these smooth trajectories (e.g., over 100 actions) are based on a fixed underlying distribution. In real RL learning or inference, the stochastic policy distribution $\pi(\cdot | s_t)$ is conditioned on the current state, meaning the policy distribution changes at each step. In this scenario, does the sequence smoothness still hold? In other words, would generating Perlin noise for a changing policy trajectory still result in smooth action sequences?

2. Does the use of smooth action trajectories imply that action changes are relatively slow? Could this affect the speed of learning or inference? For instance, in scenarios that require rapid action adjustments (such as emergency braking in autonomous driving), would this smoothness impact the effectiveness of the policy?

3. Besides generating smooth action sequences, does Perlin noise effectively increase the diversity of the sampled actions? In model-free RL, efficient exploration, i.e., collecting more diverse samples, is critical for improving sample efficiency. How does the introduction of Perlin noise influence the breadth of exploration?

I would like to increase the scores if these concerns are addressed.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a new exploration strategy derived from Perlin Noise for Reinforcement Learning tasks. Instead of using classical Gaussian Noise, the authors found that Perlin noise could explore the hard-exploration task more effectively and smoothly. To allow Perlin noise to be used for training the RL algorithms, the authors conduct a theoretical work which shows the asymtotic normality of Perlin noise.  A normalization function is also proposed to map the Perlin noises to be gaussian-like distribution. Experiments are conducted in various task sets.

### Strengths
1. The natural property of Perlin Noise such as smoothness can be particularly helpful for robotics tasks as smoother actions are usually perferred due to safety concern.
2. The authors have an extensive proof of the concepts mentioned in the paper.
3. Experiments are carried out in different tasks.

### Weaknesses
1. Clarity is my biggest concern. Many math symbols, terms and performance criterion are undefined. Such as t and i in line 211 or the Mean squared Jerk are not properly defined. The procedure of the whole scheme is shown in Fig. 4. However, how normalize function is calculated exactly and what hyperparameters are there are not explicitly written.
2. The results produced by the authors are also different from existing work. Pink noise [1] shows that they are outperforming white noise in many tasks and the results are evaluated in a statistical way. But in this work, pink noise seems to be significantly worse than white noise. The overall performance of Perlin noise and white noise in terms of rewards is also very close to each other. 
3. The authors claim that Perlin noise can be used for hard-exploration tasks. But in the selected tasks, there aren't many tasks involving sparse rewards.
4. Smoothness would be the key benefits of using Perlin Noise in robotics. Thus, to fairly compare the benefits, it would be more interesting to compare white/pink noise with a simple PID as the filter.
5. Computational cost is not mentioned. How much extra compute cost would Perlin noise bring?
6. No ablation study has been carried out to show the robustness of Perlin noise

### Questions
Some questiosn are mentioned in the weakness part. 
1. Could you please briefly describe the hyperparameter tuning for Perlin noise and other baselines? This would also help for understanding why Pink noise performs so badly.
2. Could you further elaborate how normalize function is in practice calculated?
3.  How much differences in terms of training wallclock time does perlin and other baselines have?
4. How robust is Perlin noise when different t_offset or t_speed are picked?

### Soundness
2

### Presentation
2

### Contribution
3
