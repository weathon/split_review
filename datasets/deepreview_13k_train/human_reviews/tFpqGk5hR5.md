# A Simple Open-Loop Baseline for Reinforcement Learning Locomotion Tasks

- Decision: Reject
- Scores: 6, 3, 3, 5

## Abstract
In search of a simple baseline for Deep Reinforcement Learning in locomotion tasks, we propose a model-free open-loop strategy.
By leveraging prior knowledge and the elegance of simple oscillators to generate periodic joint motions, it achieves respectable performance in five different locomotion environments, with a number of tunable parameters that is a tiny fraction of the thousands typically required by DRL algorithms.
We conduct two additional experiments using open-loop oscillators to identify current shortcomings of these algorithms.
Our results show that, compared to the baseline, DRL is more prone to performance degradation when exposed to sensor noise or failure.
Furthermore, we demonstrate a successful transfer from simulation to reality using an elastic quadruped, where RL fails without randomization or reward engineering.
Overall, the proposed baseline and associated experiments highlight the existing limitations of DRL for robotic applications, provide insights on how to address them, and encourage reflection on the costs of complexity and generality.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes an open-loop controller baseline that has decent performance on a number of control tasks. The baseline is shown to be robust to noise and can be transferred to a real robot.

### Strengths
The primary strength of the approach is in its simplicity. The authors are careful to argue that the proposed method achieves ‘satisfactory’ performance on a number of tasks without requiring complex models. As the authors point out, there are natural advantages to using simpler pattern generators for robotics which avoid issues of bang-bang control and wear-and-tear that might arise from learnt methods. I also appreciate that the authors are careful with their claims and acknowledge that SAC outperforms their proposed approach in simulation without noise.

The paper is also written in clear and simple language and is easy to follow.

### Weaknesses
I generally support the argument for simplicity that is presented in the paper. The baseline requires far fewer parameters and less computation to train. However, I think the paper is missing a discussion on how RL might still play a role when applied to robotics. 

There are solutions to the issues presented in Section 4.3 for Robustness to sensor noise that RL practitioners would likely implement. For example, noise can be added in simulation during the RL training which would result in a conservative but more robust policy. It would be interesting to see how that compares to an open loop baseline. As the paper argues, domain specific knowledge could help improve algorithm design albeit for the RL algorithms in this case. More generally, the results seem to indicate that if final performance is the key driver being optimised, RL may still be the tool of choice.

Finally, while the paper does a good job of implementing baselines from RL and evolutionary algorithms, there are no pattern generating baselines being compared to. Central pattern generators have been studied for some time so it would be important to know how the proposed open-loop baseline compares against existing ideas in the field.

### Questions
1. The `Contributions` list that the baseline can handle sparse rewards. As far as I know none of the environments used for the evaluation use sparse rewards though. Could the authors clarify this point?
2. Can the authors include another non-learning baseline to understand how much is gained with the specific implementation proposed?
3. For the robustness to sensor noise, can the authors include a baseline where SAC is trained with a subset of the noisy parameters? For instance, if SAC were trained to withstand random noise of say 3N, it seems more likely that it would be able to withstand the 5N noise tested in the paper.
4. For Figure 3, shouldn’t the dot for `Open Loop` sit exactly at 1? It seems that the plot is slightly below 1 which seems off to me.
5. While I like the general evaluation in the Experiments section, I found Table 6 in the Appendix with the actual scores informative. Since there is still space, I would suggest adding that table to the main text - if the authors think it would not affect the narrative flow too much.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes an open-loop control algorithm to solve five different locomotion control tasks. The experiments and video show that a simple control algorithm can achieve better results than RL policy.

### Strengths
- The paper contains the real robot experiments. It shows the real effectiveness of the proposed algorithm.
- The paper considers the advantages of the method from the perspective of runtime.

### Weaknesses
- The proposed method lacks novelty. Simple open-loop controllers have often served as baselines in prior reinforcement learning (RL) research. Notably, the locomotion control results presented here are significantly less sophisticated than those achieved by other works, whether they employed RL exclusively [1] or integrated RL with classical control methods [2, 3].

- The training outcomes for the RL methods in this paper appear considerably weaker than the benchmarks established in other RL-focused locomotion studies. Furthermore, the paper does not adequately address the specific challenges that RL aims to solve in control policy, such as ensuring robustness in previously unseen environments.

- The paper offers limited insights for the machine learning community, which is the primary audience of this conference.

### Questions
- In experiments, why the authers choose speed as the metric of the locomotion task? Can you consider more realistic metrics like stability under the noises or some uneven terrains, as well as show more videos beyond walking in a straight line?
- The method works because the tasks only depend on cyclic movements for joints. Can the proposed method still be used if there are more obstacles in the environment, which need some complex behavior (turn left/right)?
- Is it possible to try more to adjust the parameters of the pd controller and the range of the joint target position generated by the RL policy to improve the results of the RL method? The demo shown by the authors is indeed worse than other RL-based locomotion works recently.

### Soundness
2 fair

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The presented paper introduces a Central Pattern Generators (CPG) controller as a rudimentary open-loop baseline for reinforcement learning (RL) in locomotion tasks. In addition to detailing the method, the authors have exhaustively evaluated their proposed baseline on Mujoco-v4 environments and deployed it in a simple real-world setting.

### Strengths
1. The paper offers a comprehensible open-loop RL baseline, with the technical aspects meticulously described and supplementary implementation details provided in the appendix.
2. The research does not limit itself to simulation; it extends its evaluation of the open-loop controller to a genuine real-world environment.
3. The authors emphasize the significance of leveraging prior knowledge in task formulation, suggesting its equal importance to algorithmic enhancement.
4. Common pitfalls of existing RL techniques are explored, accompanied by results that demonstrate scenarios in which contemporary RL methods are outperformed by the simple open-loop baseline.

### Weaknesses
1. In terms of novelty of the work, central pattern generators have been applied to legged locomotion in different ways in much more realistic and complex setting, for example it’s been used to build a better action space for RL as described in Bellegarda, et al [1].  In this case, it’s hard to see the value of applying CPG to many simple locomotion tasks (Mujoco-v4 in gymnasium). Though Gym contains simple locomotion tasks, no matter whether it’s hard to solve or not, it’s mainly designed for evaluating different RL methods providing a specific manually designed controller for these tasks can hardly address issues in current RL methods. The paper does not adequately justify why a CPG controller, especially in its basic open-loop form, is a relevant baseline for addressing the limitations of current RL methods, given that CPGs have been extensively explored in more sophisticated contexts.
2. Though this work is compared with several RL methods trying to study the robustness of current RL methods, no recent works are compared. The most recent work compared in this work is SAC. The choice of SAC as the most recent comparison is limiting, as there have been significant advancements in RL algorithms since its introduction. The paper fails to engage with more contemporary methods that might offer a more nuanced perspective on the robustness and limitations of RL.
3. Though the proposed simple open-loop baseline controller is robust and provide good sample efficiency, this open-loop baseline can only be applied to locomotion tasks, where current RL method can solve much more complex locomotion tasks (like traverse complex terrain) within one hour [2, 3]. The paper does not acknowledge the limited applicability of the proposed CPG controller to a narrow range of locomotion tasks, while RL methods have demonstrated success in more complex and diverse environments. The comparison is therefore not a fair assessment of the broader capabilities of RL.

### Questions
1. It would be great if authors could further address the contribution of the proposed work.
2. It would be great if this work can provide more comparison with recent RL works if this work is trying to address the issue of existing RL methods, like AWR [1], V-MPO[2] (just example), or some model-based RL methods[3].
3. When it comes to sim2real, many rewards like minimizing the energy consumption, penalize the high frequency action has been well-studied, as well as the domain randomization techniques, when studying sim2real performance, these techniques should be applied to see the actual performance different. It would be great to apply these techniques if this work is trying to claim the performance of proposed method in sim2real transfer. 

Reference:
[1] Peng, et al. Advantage-Weighted Regression: Simple and Scalable Off-Policy Reinforcement Learning

[2] Song, et al. V-MPO: On-Policy Maximum a Posteriori Policy Optimization for Discrete and Continuous Control

[3] Hansen, et al. Temporal Difference Learning for Model Predictive Control

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper presents a simple baseline for locomotion tasks usually used to evaluate RL algorithms. This simple baseline employs oscillators to generate periodic joint motions, providing a open-loop method with ease of reproducibility, a fracion of the parameters of neural network-based approaches, and little use of computational resources.

### Strengths
- One of the paper's notable strengths is the simplicity of the proposed approach. The use of open-loop oscillators to solve locomotion tasks offers an elegant and straightforward solution. This simplicity is in contrast to the increasing complexity of many contemporary deep reinforcement learning (DRL) methods.

- This approach is easily reproducible. It provides a minimal standalone code for solving the swimmer task and includes comprehensive details on the optimization of oscillator parameters.

- I really appreciate the thorough analysis of the proposed approach with a few different RL methods. This analysis provides valuable insights into the performance, efficiency, and robustness of this simple baseline in relation to existing more complex methodologies.

### Weaknesses
 - Although the method requires minimal parameters, a lot of trial-and-error is needed in determining the number of oscillators to use for each environment, which is in direct contrast to RL methods which are general across multiple environments. The need for fine-tuning in each context may limit the method's scalability.

- While this result is really nice, this is also very expected. When maximizing the default reward of these environments, the resulting policy always corresponds to cyclical behavior which suggests that a simple cyclical controller could solve the task. Furthermore, these environments are very simple, and this work further intesifies the importance of moving on from this simple environments and focus on harder tasks.

- While the simplicity and practicality of the approach are strengths, the contribution is minimal. I see this work as better suited for the blog post track rather than a conference paper.

### Questions
No questions. I address my opinions in the fields above. I think this work is somewhat valuable to the community, but I also think that it could easily be more appreciated as a simple blog post as the contribution itself is minimal.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
