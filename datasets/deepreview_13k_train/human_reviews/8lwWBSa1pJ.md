# Time-aware World Model:  Adaptive Learning of Task Dynamics

- Decision: Reject
- Scores: 6, 3, 5, 8, 6

## Abstract
In this work, we introduce Time-Aware World Model, a model-based approach designed to explicitly incorporate the temporal dynamics of environments. By conditioning on the time step size, $\Delta t$, and training over a diverse range of $\Delta t$ values - rather than relying on a fixed time step size - our model enables learning of both high- and low-frequency task dynamics in real-world control problems. Inspired by the information-theoretic principle that the optimal sampling rate varies depending on the underlying dynamics of different physical systems, our time-aware model enhances both performance and learning efficiency. Empirical evaluations demonstrate that our model consistently outperforms baseline approaches across different observation rates in various control tasks, using the same number of training samples and iterations. We will release our source code on GitHub once the final review decisions are made.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors propose an approach to address the issue of differing time step sizes $\Delta t$ between training and test phases, which can lead to a mismatch in dynamics. They propose a training scheme that randomly samples $\Delta t$ as inputs and update the model that explicitly conditions on $\Delta t$. They show that empirically this approach outperforms the baseline method, which was trained with a fixed time step size, when tested with a different $\Delta t$.

### Strengths
- This paper considers a novel problem setting which is also practically important, especially for robotics control tasks.

- The paper is well written. The motivation is well-stated and the methodology is presented clear.

- The proposed algorithm is evaluated on multiple tasks. And the empirical results are supportive of the main claim of the paper.

### Weaknesses
 - I would suggest to add a comparison between the proposed approach with works about Robust RL (e.g. Pinto, Lerrel, et al. "Robust adversarial reinforcement learning." International conference on machine learning. PMLR, 2017). In my understanding, the mismatch in the time step size is one specific instance of the dynamics mismatch. I wonder if the proposed approach can get better performance by explicitly conditioning on $\Delta t$ only.

- I wonder if the log-uniform distribution is the best way to sample $\Delta t$. A justification for this would be helpful.

### Questions
Please check the above Weaknesses section.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
For model-based RL in continuous time domains, the paper proposes to learn a time-aware world model whose components depend on the sampling frequency. In the training phase, the time-aware world model is trained with randomly varying time steps. In numerical experiments, the proposed method is evaluated under different time steps and show better performance compared with the baseline trained at the fixed time step.

### Strengths
- When approximating a continuous-time dynamical system with a sampled model, having a time-step dependent world model makes a lot of sense to better fit the actual dynamics. The paper proposes such a time-aware world model with the potential to improve model-based RL performance.

### Weaknesses
 - The motivation referring to the Nyquist-Shannon sampling theorem does not seem to be consistent with the observation of numerical experiments. From the sampling theorem, as long as the sampling frequency is high enough, there won't be any information loss. But the numerical experiments suggest that the non time-aware model performs poorly even when the sampling frequency is the highest. This inconsistency makes the connection to the sampling theorem questionable.

- During the training phase, the sampling step is randomly selected from a log-uniform distribution. It is suggested that this distribution helps stabilize the training process, but no theoretical nor numerical analysis is provided. Some ablation studies using different sampling distribution might provide some insights to the choice.

- In the numerical evaluation, performance is compared across different observation rate. Given any time-step, the time-aware model can provide the appropriate prediction by conditioning on the time-step. But for the model trained with a fixed time-step, the information of the observation time-step does not seem to be adjusted. For example, for a model trained with $\Delta t=1$ms, when evaluating at $\Delta t=2$ms, instead of applying the model once, one might want to apply the model twice to have a more accurate prediction given the knowledge of the doubled time-step. Without doing some kind of adjustments for the baseline models make the fairness of comparisons questionable.

- When trained and evaluated with the same time-step, Figure 5 shows similar performance between the baseline model and the time-aware model. This makes the effectiveness of the proposed methods questionable when the goal is just to achieve good performance. Maybe under some scenarios where the training time-step and evaluation time-step are different, the proposed method might make more sense.

### Questions
- It would be great if those points listed in the weaknesses above could be addressed.

### Soundness
2

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
4

### Summary
This paper emphasizes the importance of incorporating temporal information $\Delta t$ into dynamic modeling and introduces a mixture-of-time-step training framework that learns task dynamics across multiple frequencies. The authors' motivation stems from the existence of multi-scale dynamical systems, where each subsystem may operate at a unique frequency, and from the Nyquist-Shannon sampling theorem, which implies that lower sampling frequencies reduce performance, while higher sampling frequencies improve accuracy but increase sample complexity and reduce learning efficiency. Their approach involves conditioning all components of a world model, except the encoder, on $\Delta t$ and using the Euler or RK4 integration method to reformulate the dynamic model. The authors experimentally validate their method on several control tasks from the Meta-World suite, using TD-MPC2 as the baseline. They demonstrate that their time-aware modifications to TD-MPC2 yield superior performance over the baseline when evaluated across varying frequencies at test time, all while maintaining the same sample efficiency.

### Strengths
- The paper is well-written and clear, with strong motivation and thorough explanations of each aspect of their approach.

- The proposed idea is innovative and promising, with potential for significant impact on real-world applications.

### Weaknesses
 - Since the core framework relies heavily on pre-existing world models and the main contribution is incremental, I expected to see larger-scale experiments in more complex environments, such as real robots or video games, to better illustrate the approach's applicability. In its current form, the paper lacks sufficient novelty to fully engage readers. I recommend that the authors either incorporate experiments in more complex environments to demonstrate real-world applicability or create more challenging scenarios, such as those requiring adaptation to varying $\Delta t$ within the same episode.


- The authors claim that smaller frequencies increase sample complexity and are therefore lead to inefficient learning. However, the paper lacks theoretical or experimental evidence to explain why this is true. To strengthen this claim and further support the motivation for time-aware world models, I suggest adding smaller frequencies to the experiment in Figure 4 and comparing their sample complexity with that of the time-aware model. This addition would provide valuable insight into the efficiency benefits of the proposed approach.

### Questions
- Is there a specific reason why lower frequencies are missing in Figure 4? For instance, I was interested in seeing the baseline's performance with $\Delta t =0.1$ ms, as this frequency is used during the training of the time-aware model.

- Section 3.2.3 appears to be a mitigation for the issue described in 3.2.2. Would it be reasonable to combine these sections, or are they based on distinct motivations?

- Since TD-MPC2 assumes an underlying MDP structure, I suggest replacing $o_t$ with $s_t$ in Section 4.1 to avoid confusion with observations in a POMDP setting.

### Soundness
3

### Presentation
4

### Contribution
1

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper proposes time step aware world models for handling real life distribution shifts with lower observation frequencies. It includes the time step as an additional input to the world model and uses log-uniform time step sampling during training to learn the world model for various observation frequencies. It shows impressive results on various control tasks within Meta-World, without any increase in the sample complexity.

### Strengths
The proposed strategy shows impressive performance when combined with TD-MPC2 on a variety of control tasks while using the same number of samples.
The proposed method can be combined with any existing MBRL algorithms such as TD-MPC2.

### Weaknesses
One of the motivations for the TD-MPC2 work was to create generalist agents, which can be trained in a multi-task setup and then can be easily fine tuned on any new task. However, no comparison with TD-MPC2 has been made for a multi-task setup.
A closely related work (as mentioned by the authors) on multi time scale world models (Shaj et al.) is missing as a comparison baseline in the experimental section.

A precise description of how 4th order runge kutta method is used for integration is missing from section 4.1.2 or Algorithm 1. Can the authors please state it here as well as in the main paper for clarity?

### Questions
A precise description of how 4th order runge kutta method is used for integration is missing from section 4.1.2 or Algorithm 1. Can the authors please state it here as well as in the main paper for clarity?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces the Time-Aware World Model (TAWM), which adapts to the temporal dynamics of environments by conditioning on the time step size ($\Delta t$). Different from conventional models that use a fixed time step, TAWM trains across a diverse range of ∆t values, allowing it to capture both high- and low-frequency task dynamics. This approach addresses shortcomings in existing models, such as temporal resolution overfitting and inaccurate system dynamics when applied to real-world scenarios.

### Strengths
The time-aware mechanism significantly improves the emprical results compared to the non time-aware methods. The paper writing is improved and easy to understand.

### Weaknesses
1. The paper writing clearance and correctness should be improved. In Line 140, what does $\eta(\pi)$ mean? policy or expected return? And why $s_i$ could be sampled from a policy $\pi$?
2. What is the advantage of the proposed method compared to directly setting the simulation frequency 2x bigger than the real-world frequency? It seems that your proposed method and baselines all work under small $\Delta t$.
3. As depicted in Fig.5, your proposed method is not significantly superior to the baselines in empirical performance.


### Questions
Could you please provide more results of the comparisons between your proposed method and MTS3?

### Soundness
3

### Presentation
3

### Contribution
2
