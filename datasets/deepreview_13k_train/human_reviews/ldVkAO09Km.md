# Diffusion Actor-Critic: Formulating Constrained Policy Iteration as Diffusion Noise Regression for Offline Reinforcement Learning

- Decision: Accept
- Scores: 6, 8, 6, 6

## Abstract
In offline reinforcement learning (RL), it is necessary to manage out-of-distribution actions to prevent overestimation of value functions. Policy-regularized methods address this problem by constraining the target policy to stay close to the behavior policy. Although several approaches suggest representing the behavior policy as an expressive diffusion model to boost performance, it remains unclear how to regularize the target policy given a diffusion-modeled behavior sampler. In this paper, we propose Diffusion Actor-Critic (DAC) that formulates the Kullback-Leibler (KL) constraint policy iteration as a diffusion noise regression problem, enabling direct representation of target policies as diffusion models. Our approach follows the actor-critic learning paradigm that we alternatively train a diffusion-modeled target policy and a critic network. The actor training loss includes a soft Q-guidance term from the Q-gradient. The soft Q-guidance grounds on the theoretical solution of the KL constraint policy iteration, which prevents the learned policy from taking out-of-distribution actions. For critic training, we train a Q-ensemble to stabilize the estimation of Q-gradient. Additionally, DAC employs lower confidence bound (LCB) to address the overestimation and underestimation of value targets due to function approximation error. Our approach is evaluated on the D4RL benchmarks and outperforms the state-of-the-art in almost all environments.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper integrates the advantage-weighted regression and diffusion model for offline reinforcement learning. This paper introduces the Diffusion Actor-Critic (DAC) framework, which theoretically formulates KL-constrained policy iteration as a diffusion noise regression problem. The experimental results demonstrate the advantages of DAC in terms of performance and stability. However, several concerns are as follows.

### Strengths
Overall the paper is well-written, making readers quickly capture the core idea. There are several advantages of this paper:

1. DAC directly models the target policy as a diffusion model, which is an innovation in the field of offline reinforcement learning.

2. Soft Q guidance adjusts the intensity of Q gradients according to noise scale, encouraging the generation of high-return actions while staying within the behavior support range. This approach effectively prevents actions outside the sampled distribution, enhancing the stability and performance of the algorithm.

### Weaknesses
1. The notation of this paper is complicated. 

2. The translation between Equations 13 and 14 probably is not acceptable. How could you replace the target policy with the offline dataset? Do you mean behavior policy?

3. The design of Q-ensemble makes the results unconvincing. The Q-ensemble methods can solve the offline RL without any extra regularization. Given the design of the Q-ensemble, it's ambiguous whether the improvement comes from the proposed diffusion policy-constrained iteration or the Q-ensemble. The ablation of Fig. 4 seems to approve this. The baseline methods, such as DQL, should add a Q-ensemble to compare what makes it fairer. 

4. Although the paper emphasizes the importance of the LCB objective in stabilizing Q-value estimation, it lacks a deeper analysis of the impact of different pessimism factors, ρ.

5. Insufficient comparison of offline RL, including but not limited to:

[1] RORL: Robust Offline Reinforcement Learning via Conservative Smoothing.

[2] Offline RL with No OOD Actions: In-Sample Learning via Implicit Value Regularization.

Several previous methods using constrained policy learning for offline RL should be discussed at least:

[3] Behavior proximal policy optimization

[4] An Implicit Trust Region Approach to Behavior Regularized Offline Reinforcement Learning

[5] Uni-o4: Unifying online and offline deep reinforcement learning with multi-step on-policy optimization

### Questions
See weaknesses.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper presents the Diffusion Actor-Critic (DAC) framework, aimed at addressing key challenges in offline reinforcement learning, particularly in policy optimization and high-reward action generation. By innovatively transforming the KL-constrained policy iteration problem into a diffusion noise regression problem, DAC introduces a soft Q-guidance mechanism. Through comparative experiments, DAC demonstrates superior performance over existing methods on multiple D4RL benchmark tasks, especially when handling datasets containing a large number of suboptimal trajectories. The experimental results indicate that DAC not only exhibits stable convergence but also surpasses other methods in overall scores, showcasing its potential in the field of offline reinforcement learning.

### Strengths
Originality:

The DAC framework which combines diffusion models with policy optimization in reinforcement learning is novel. By introducing soft Q-guidance, the paper effectively overcomes the problem of overestimating Q-values in offline learning, enhancing the stability of policy improvement. This approach offers a new direction for future research.

Significance:

The authors conduct extensive experiments on D4RL benchmarks, covering a variety of tasks with results that are clear and convincing. The experimental results is strong

Clarity:

The paper is clearly written with illustrative examples

### Weaknesses
The authors should consider evaluate DAC in more offline reinforcement learning tasks, particularly in real-world application areas such as robotic control and atari games. And It would be better to provide specific choice of hyperparameter configuration

The authors mention that soft Q-guidance performs well in handling tasks, but that hard Q-guidance significantly deteriorates in performance when facing a large number of sub-optimal trajectories. It is not clear if the soft Q-guidance is robust to different levels of sub-optimality in the dataset. The paper should explore the sensitivity of the method to the quality of the offline data. Furthermore, the paper should explore combining different guidance strategies to enhance the robustness of the algorithm, and evaluate the introduction of additional regularization methods in specific tasks to prevent the policy from overly relying on sub-optimal trajectories, thereby enhancing the model's stability and generalization ability.

In the antmaze task, the author noted that sparse rewards have a certain impact on the algorithm's performance. In this regard, the paper should investigate more effective reward mechanisms or exploration strategies to address the challenges posed by sparse rewards. In practical applications, if the algorithm encounters sparse rewards, what measures do you anticipate taking to adjust the DAC algorithm to ensure it can still effectively learn and optimize the policy?

The authors mentioned using a lower confidence bound to counteract overly pessimistic estimates. Could this lead to a systematic bias in the Q-values? How significant is this bias in different task settings?

Finally, how does the $\eta$ parameter in the objective function influence the optimization process? In certain scenarios, the choice of $\eta$ might lead to oscillations or divergence of the algorithm. Is there a need for a sensitivity analysis regarding this choice? If gradient vanishing issues arise, particularly when the update frequency of the target policy is high, how should this potential problem be addressed?

### Questions
- Soft Q-guidance relies on the accurate estimation of Q-values. If Q-values are overly optimistic or pessimistic, how does this affect the generated final policy? Have you considered the propagation of such uncertainty in the learning process? If the weight adjustment for soft Q-guidance is improper, could it lead to an over-reliance on Q-values in the generated policy, potentially resulting in overfitting?

- Soft Q-guidance performs well in handling tasks, but that hard Q-guidance significantly deteriorates in performance when facing a large number of sub-optimal trajectories. Have you considered combining different guidance strategies to enhance the robustness of the algorithm? Specifically, have you evaluated the introduction of additional regularization methods in specific tasks to prevent the policy from overly relying on sub-optimal trajectories, thereby enhancing the model's stability and generalization ability?

- In the antmaze task, the author noted that sparse rewards have a certain impact on the algorithm's performance. In this regard, have you designed more effective reward mechanisms or exploration strategies to address the challenges posed by sparse rewards? In practical applications, if the algorithm encounters sparse rewards, what measures do you anticipate taking to adjust the DAC algorithm to ensure it can still effectively learn and optimize the policy?

- The authors mentioned using a lower confidence bound to counteract overly pessimistic estimates. Could this lead to a systematic bias in the Q-values? How significant is this bias in different task settings?

- How does the $\eta$ parameter in the objective function influence the optimization process? In certain scenarios, the choice of $\eta$ might lead to oscillations or divergence of the algorithm. Is there a need for a sensitivity analysis regarding this choice? If gradient vanishing issues arise, particularly when the update frequency of the target policy is high, how should this potential problem be addressed?

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
3

### Summary
This paper presents Diffusion Actor-Critic (DAC), a novel offline reinforcement learning algorithm designed to directly generate target policies using diffusion models. DAC formalizes the policy iteration problem with Kullback-Leibler (KL) constraints as a diffusion noise regression problem, achieving policy constraints through soft Q guidance, thus avoiding the generation of actions outside the offline data distribution. The paper demonstrates the outstanding performance of DAC in D4RL benchmark tests, surpassing current state-of-the-art methods in nearly all environments, while showing stable convergence and robust performance.

### Strengths
Innovativeness: Introduces a new algorithm DAC and proposes the soft Q guidance, addressing several challenges in offline reinforcement learning.

Experimental Performance: Demonstrates outstanding performance in D4RL benchmark tests, especially surpassing current state-of-the-art algorithms in locomotion and antmaze tasks.

Theoretical Support: Provides clear theoretical justification by rigorously transforming the KL constrained policy iteration problem into a diffusion noise regression problem.

### Weaknesses
Lack of presentation: structure of the article is chaotic, failing to highlight key points, which creates some difficulty in reading.

Scope of Application: Although DAC performs well on standard benchmarks, its generalization ability in large-scale or complex real-world tasks has not been fully validated.

The advantages of Soft Q-guidance are not sufficiently pronounced compared to other methods.

### Questions
How does DAC's generalization performance hold up in larger-scale real-world applications, such as autonomous driving or industrial robotics? Is there a plan to further test the scalability of this method?

Does the trade-off in soft Q guidance choice show differences in performance across various environments? Can the specific effects of different weight parameters on model performance be further explored?

### Soundness
3

### Presentation
2

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
The paper proposes DAC, an offline reinforcement learning algorithm that uses diffusion models to manage out-of-distribution actions and prevent the overestimation of value functions. DAC formulates the KL-constrained policy iteration as a diffusion noise regression problem, enabling the direct representation of target policies as diffusion models. The approach includes soft Q-guidance for actor training and a Q-ensemble for critic training, stabilizing Q-gradient estimation. DAC outperforms state-of-the-art methods on the D4RL benchmarks, demonstrating its effectiveness across various environments.

### Strengths
- The paper incorporates diffusion models into constrained policy iteration by using score functions, addressing the issue of the untraceable KL divergence in diffusion policies. 

- The paper also presents extensive experiments and thorough ablation studies, demonstrating the effectiveness and robustness of DAC.

- DAC captures the multimodality of policies using diffusion model.

### Weaknesses
 - There are some 2024 papers missing in the offline RL summaries (existing citations are 2023 at best), and accordingly I would like to see your results against them in the experimental section eg. AlignIQL: Policy Alignment in Implicit Q-Learning through Constrained Optimization (He et al.), Diffusion Policies creating a Trust Region for Offline Reinforcement Learning (Chen et al.). 

 - Recently, there is also a lot of work combining online RL and diffusion modelling, and I think a brief summary is also very necessary. Let me name a few famous works, you can add a paragraph to summarise eg. Policy Representation via Diffusion Probability Model for Reinforcement Learning(Yang et al.), Learning a Diffusion Model Policy from Rewards via Q-Score Matching(Psenka et al.), Diffusion Actor-Critic with Entropy Regulator(Wang et al.).

 - I don't seem to have seen you perform ablation experiments for LCB, as well as ablation experiments for diffusion step size. Especially with the ablation experiments for LCB, I'd like to see the proportionality of the improvement in performance of LCB for your final performance compared to the improvement in performance of your proposed method.

 - Experiments including $\rho$ were not analysed for sensitivity.

### Questions
- line244 or so, did you experiment with estimating entropy in the EDP?
- Why haven't you done experiments with Adroit Tasks and Kitchen Tasks and compared them with the latest algorithms? (It's not enough in the appendix, it's perfectly fine to put it in the body of the text for comparison)
- In Equation 15, the Q-function is well-trained only within the original data distribution. However, the distribution of $x_t$ tends to be more random and can significantly diverge from the dataset distribution. How can we ensure that the Q-function's gradients with respect to $x_t$ remain accurate and avoid substantial extrapolation errors?

### Soundness
3

### Presentation
3

### Contribution
2
