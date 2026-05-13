# Motion Control of High-Dimensional Musculoskeletal System with Hierarchical Model-Based Planning

- Decision: Accept
- Scores: 6, 8, 6, 5

## Abstract
Controlling high-dimensional nonlinear systems presents significant challenges in biological and robotic applications due to the large state and action spaces. While deep reinforcement learning has emerged as the leading approach, it suffers from computationally-intensive and time-consuming, and are not scalable to wide varieties of tasks that each require significant manual tuning. This paper introduces Model Predictive Control with Morphology-aware Proportional Control (MPC$^2$), a novel hierarchical model-based algorithm that addresses these challenges. By integrating a sampling-based model predictive controller for target posture planning with a morphology-aware proportional controller for actuator coordination, our algorithm achieves stable movement control of a 700-actuator musculoskeletal model without training. We show that MPC$^2$ enables zero-shot high-dimensional motion control across diverse movement tasks, such as standing, walking on varying terrains, and sports motion imitation. It can be incorporated into optimal cost function design to automatically optimize the objective, reducing the reliance on traditional reward engineering methods. This work presents a major advancement in (near) real-time control for complex dynamical systems.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents a hierarchical model predictive control approach for a  700-dimensional musculoskeletal system, where a modified version of MPPI is used as a higher-level controller to output target postures that are tracked by a lower-level proportional controller. The gains of the lower-level proportional controller are set using a morphology-aware function based on the Jacobian matrices of the current state and the target posture. The method is evaluated on several tasks and the paper reports ablations of the method.

### Strengths
- The presented method is simple, can handle the high dimensionality of the action space associated with muscle-actuated systems, and performs well on several challenging tasks, such as walking on rough terrain, walking on slopes, or over stairs. 
- Fast cost-design iteration time to evaluate/generate new controllers compared to Deep RL methods.
- The paper is well-written overall and the ablation studies justify different parts of the proposed method.

### Weaknesses
 - I have concerns that the conference might not be a good fit for the paper. I struggle to classify the presented hierarchical sampling-based approach for control as an area or subfield of machine learning. Especially, considering that MPPI and many of its variants have been traditionally presented in robotics conferences. If the authors can clarify, how the conference is a good fit for the paper or if this is not a concern for any other reviewer, I will not oppose the acceptance of this paper in an exercise of  " broadening definitions of originality and significance".

- The paper would benefit from making a clear distinction between the iteration time to create a controller and the time needed to execute a controller at test time. L121 states “Compared to DRL, model predictive control allows for real-time control”.  It is well known that training DRL policies can be time-consuming, however, after the training stage, most DRL policies can be queried/executed in the order of milliseconds thus effectively allowing for real-time control, unlike the presented method which is only suitable for near real-time deployment/execution.


- Probably due to the challenging nature of the setting, only a few baselines are provided and the performance of the baselines is not very competitive.  AHAC [1] might provide a stronger baseline for the comparisons.  AHAC has also been tested on a muscle-actuated humanoid task and has better performance than SAC and PPO on such tasks.
   - [1] Ignat Georgiev et al.  Adaptive Horizon Actor-Critic for Policy Learning in Contact-Rich Differentiable Simulation.

### Questions
- Apart from only being near real-time at execution time? what are other limitations of the method?
- Is the method robust to perturbations? Can the humanoid keep walking when unknown external forces are applied? 
- Is a different cost function used to obtain a controller for each task? If so, is there a systematic way to unify/merge cost functions to obtain a controller that can perform multiple tasks at the same time? 
- One of the motivations for musculoskeletal systems is its robustness in case of actuator failure. How does the method’s performance degrade in the presence of actuator failures  (when only a subset of tendons can be actuated)? Such evaluation would further highlight the benefits of the presented approach.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
## Summary:
The paper introduces a control algorithm called Model Predictive Control with Morphology-aware Proportional Control (MPC2) to address
 challenges associated with the real-time control of high-dimensional musculoskeletal systems. The problem is complex due to the inherent complexity of over-actuated nature involving large state and action spaces. The authors proposed a Sampling based MPC with Morphology-aware Proportional Controller for actuator co-ordination (MPC2). They show that the methodology can produce stable motions without any training/data-driven steps, resulting in zero-shot motion control. They used Deep learning based approach as a baseline to compare their method for various tasks such as standing, walking on flat/rough surface, slope, stairs and kicking a ball.   

## Methodology:
MPC2 combines two main strategies:
1. High-Level Planning via Model Predictive Control (MPC): This component of MPC2 uses a sampling-based model predictive controller to plan target postures for the system. It operates by forecasting the desired postures over a finite horizon and computing optimal control actions to achieve these postures.
2. Low-Level Control via Morphology-aware Proportional Control: This controller works at the actuator level, coordinating the actuators to reach the target joint positions determined by the high-level planner. It adjusts the actuators dynamically based on the morphology of the system, ensuring efficient and effective movement control.

## Key Contributions and Findings:
1. Training-Free Control: Unlike Deep Reinforcement Learning based methods that require extensive training, MPC2 enables zero-shot control, meaning it can control the system effectively without any prior training on specific tasks.
2. Adaptability to Diverse Tasks: The algorithm was tested on various movement tasks, including standing, walking on different terrains, and sports motion imitation. These experiments demonstrated its capability to adapt to a wide range of activities without the need for manual tuning or reward engineering.
3. Real-Time Performance: One of the significant advancements of MPC2 is its ability to perform near real-time control. This is due to their Hierarchical control strategy, reducing of the action space for MPC (dz = 37) instead of the full control over all 700 tendons.
4. Efficient Optimization: The paper shows that MPC2 can optimize its cost function design automatically through Bayesian optimization. This feature significantly reduces the manual effort typically needed in traditional control systems.

## Experimental Validation:
The effectiveness of MPC2 was validated through a series of experiments conducted on a simulated 700-actuator musculoskeletal model. The model was tested across various scenarios that require high levels of coordination and control precision. Results from these experiments confirm the robustness and versatility of MPC2, outperforming existing deep reinforcement learning-based methods in terms of speed and adaptability. Their website provides video demonstrations of MPC2’s real-time control capabilities across various movement tasks. These videos effectively illustrate the adaptability and robustness of the proposed algorithm. They show MPC2 handling complex movements like walking on uneven terrain, climbing stairs, and executing sports motions (e.g., kicking a ball) with stable, smooth coordination across multiple actuators. These visual results add strong qualitative evidence to the paper’s claims about MPC2’s ability to perform zero-shot control without training and adapt to different motion tasks with high precision and reliability.

## Conclusion:
The development of MPC2 marks a significant step forward in the field of robotics and biomechanics, offering a powerful tool for the high-dimensional control of complex systems. This method holds potential not only for improving robotic system performance but also for advancing human-related applications such as prosthetics and rehabilitation robotics, where adaptive, real-time control is crucial.

### Strengths
The paper definitely presents some key strengths:
1. Originality: While breaking down the high-dimensional control/planning problem into multiple stages is a very know concept, the paper presented first of its kind to integrate MPPI with Morphology Aware controller. The paper thus provides a new solution for high dimensional motion control.
2. Quality: The paper provides a thorough experimental validation in Mujoco simulation. On technical aspect, the use of Bayesian optimization for automated cost function tuning streamlined the traditionally labor-intensive process of reward engineering. 
3. Clarity: The paper is a very well written providing curriculum approach to MPC. The provided code is well structured and documented.
4. Significance: Though the results were presented only in simulation and qualitatively seemed far from applicable to real applications, the approach presented has significant practical impact on real-time controls.

### Weaknesses
 I found several weak points in relation to the experiments and validation of the proposed method (it could be also a result of my background from classical control theory). 

1. Lack of quantitative stability metrics: The paper lacks in presenting the performance of their approach on key stability metrics used across the humanoids community like centre of mass polygon support, energy efficiency, etc. Additionally, integrating these metrics into the MPC cost function could enhance the results significantly. (De Viragh, Yvain, et al. "Trajectory optimization for wheeled-legged quadrupedal robots using linearized zmp constraints." IEEE Robotics and Automation Letters 4.2 (2019): 1633-1640.)

2. Experimental results: 
    1. Lacks quantitative discussion in comparison with RL based methods (the stability/energy metrics would have helped here).
    2. The paper’s comparative analysis primarily uses a DRL-based baseline, but the implementation quality of this baseline appears to be lacking. The RL approach (Learning with Muscles: Benefits for Data-Efficiency and Robustness in Anthropomorphic Tasks) should have been compared. 

3. Figure 5.a. mentions "Best Objective Value" but it isnt discussed in the paper, what that means and why it is significant.

### Questions
1. Could the authors provide additional insights into the computational requirements for real-time applications of MPC2?
2. Could you make the experimental more elaborative towards quantitative results ?

### Soundness
2

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
This paper proposes a sampling based hierarchical MPC controller that uses the known model of a simulated high dimensional musculoskeletal humanoid system and achieves good control performance across various tasks without learning a policy representation. This is to be contrasted with deep RL methods that would require a lot of time to train a policy for each task. The hierarchical MPC controller samples target positions that are then used by a morphology aware proportional controller to compute control signals for each DoF. Simulations show that the proposed method works well in various control tasks, where other MPC controllers are claimed to fail invariably.

===== POST-REBUTTAL EDIT =====

I thank the authors for their hard work and the comprehensive rebuttal. The rebuttal has answered some of my concerns and I think the paper could be accepted, it does present a contribution to the simulation/control of high dimensional systems, albeit in a modest way. I raised my score to six as a result. 

Here are some more comments based on the rebuttal:
- The github page with extensive results was quite interesting, I am hoping that the authors will integrate the results with the main paper, as I think the main paper lacks the wide coverage of results that the github page presents.
- The gait that is learned with MPC^2 also does not seem very natural. Is that the reason why MPC^2 also fails to stabilize after some time I wonder? How would you learn more natural gaits (from a human walking perspective) with e.g. black-box optimization? This could be mentioned in the discussion/conclusions.
- The paper in the end does not present a learning component. I think the discussion/conclusions should discuss ways to incorporate learning to improve some of the failure modes (gait is not natural, model too complex, MPC not fast enough for real time, more complex scenarios not covered etc.)
- I am still confused about the 'instant rollout' feature, if I understand instant rollout correctly, every MPC algorithm should incorporate instant rollout at some frequency (maybe different from the control frequency) otherwise it wouldn't be corrective. This means that MPC algorithm (running in parallel to the simulation) should always get current states of the robot from the simulation. However from the paper it seems like that is not the default, any reason why that is so? Is it because in simulation you know the model exactly so you can refrain from doing so?

### Strengths
The paper shows that a hierarchical and sampling-based implementation of a model-based predictive controller (MPC) can control in simulation a high-dimensional musculoskeletal system for the first time. This is to be contrasted with DRL methods that take a very long time to optimize policies, moreover they need to typically be re-run for each task. In that sense there's a clear contribution to the simulation literature on how to control such high dimensional systems.

### Weaknesses
I think the paper has some good contributions to control and simulation of high-dimensional systems as mentioned above, yet there are several weaknesses (some of which can be addressed in the rebuttal phase hopefully):

- There is a very extensive literature on MPC algorithms and analysis, yet the paper does not compare the proposed approach to any other MPC algorithm. Would all of the MPC methods proposed in the literature fail for this complex dynamics case? It is not clear from the text. The tradeoffs of using sampling as opposed to non-sampling based methods are also not discussed. Specifically, the paper lacks a discussion on the computational cost of sampling-based methods compared to gradient-based approaches, and how this impacts the feasibility of real-time control for high-dimensional systems. Furthermore, the paper does not explore the sensitivity of the proposed method to the number of samples used, which is a crucial parameter for sampling-based MPC.
- I'm not sure if ICLR is the right venue for this paper. Even if we agree that restricting ICLR to papers that 'learn representations' would be too strict, still we're missing a more learning-focus to the paper. This doesn't mean the paper is not well-written or that it is not sound, but I think the paper could benefit more from being targeted to a more controls conference. As of now the learning in the paper is restricted to 'inverting' (without a negative connotation) a known-and-very-complex model. However it would be more interesting for the ML community if the paper would consider not only learning a policy in this particular case, but also extending learning to cover e.g. learning the lower-level policy, learning the higher level policy (if we treat MPPI as a learning method) for different robots, etc.

See also the comments in the Questions section below for more details and questions. Overall I think the paper needs a significant extension of the experiments and ablations in order to justify its conclusions. The heuristic nature of their design decisions (low-level controller, sampling vs non-sampling, effect of sampling size, effect of horizon size, etc.) need to be discussed in more detail and compared against various alternatives. Experiments should also be presented together more concisely, more comprehensively in a table or in a figure (e.g. replacing half-page illustrations of skeletons).


### Questions
Some questions and minor comments are given below:

- Missing word in Abstract: e.g. 'it suffers from being computationally-intensive ...'
- Figure 2 is not self explanatory. Also I am confused by the boxes, the 'rollout' box inside big gray box is the access to simulator, which actually replaces the 'reality' of the leftmost box with the skeleton. A more detailed explanation would be appropriate here to ease the introduction.
- From the introduction or the abstract it is not clear how you acquire the 'model' for the Model Predictive Controller that you use. It should be mentioned that you're considering the simulated environment where you have access to / know the model of the robot. In general DRL does not need a model, so the statements should be modified accordingly (RL methods are more general, although sometimes less sample-efficient etc.)
- There does not seem to be any 'learning' in the proposed method, hence it is not clear how to use it in uncertain scenarios, where, e.g., we need to learn a model (or a policy, or both).
- "thus poses a significant bottleneck on the iteration speed of reward engineering." It is not clear up till the sentence what reward engineering is (or what it can be used for) from the introduction, nor the connections of the paper to reward engineering clear.
- Zakka et al. includes DRL in the title, so may not be the right reference for MPC methods vs. DRL in section 2.2.
- Are torque-driven humanoids (Meser et al.) less complex than your system? Section 2.2 does not mention the relation. In fact a 'musculoskeletal' system is not defined.
- notation f is used both for dynamics and for forces (which are part of dynamics, so it's a bit problematic).
- line 160: the cost function used to update MPPI does not seem to be 'cumulative' but only over the horizon of size H.
- line 170: NOT always a local approximation: when H is small, the optimized commands can even cause some systems to be unstable. Moreover you claim f_hat is not equal to f (which is typically the case) hence I think the term "local approximation" is not precise here.
- asynchronized -> asynchronous?
- missing reference for sampling-based MPC methods (there is one reference for an application paper to humanoids)
- again for MPPI, I think the paper is missing a more general reference that introduces the method (the reference is again an application paper it seems)
- \hat{u}^{\theta} notation conflicts with the previous notation where n was used to refer to rollout number.
- I failed to get Algorithm 1, although the text leading up to it was fairly clear. Some terms are not explained, like M_pos, R_MP etc., it's not clear how the initial sigma plays a role, etc.
- The distinction between the terms planning iteration vs. rollout becomes confusing at times, would be nice to define them or illustrate them over the figures.
- the need to introduce instant rollout is not clear to me. why shouldn't the rollout always start from the current state (hence \mu_0 = M_pos(s_0) in your notation). M_pos was explained later in line 276 [and in fact I would simply use p_t as the pose rather than introducing a mask notation, which conflicts with the mass matrix M(q)]. In general this seems to be an re-occurring problem in the paper: properties of certain features of the method are mentioned *before* introducing that feature.
- "While the original Model Predictive Path Integral (MPPI) can be directly employed as a high-level planner for target positions, we find that it lacks the ability to respond quickly to rapidly changing states, such as when the agent is falling. " It wasn't clear to me if this is an argument for the low-level proportional controller? If so why not mention it *after* introducing the low level controller?
- the low level controller seems to be state dependent in eq (11). Hence strictly speaking, it is not a (constant-gain) proportional controller.
- where is the standard error shown in Figure 4?
- shouldn't it be max instead of min in eq. 9?
- it is not clear how eq. (11) resolves the problem of tuning of the gain vector K.
- the design of the low-level controller seems to be very heuristics-driven: one cannot conclude that it will work for arbitrary morphologies/robots, especially given that the results are only given for a particular robot. This seems to be part of a bigger problem, in that, the paper does not propose any learning components to replace DRL or any other state of the art method. This potential lack of generality is worrying, and should be improved.
- "While no previous control methods have demonstrated success in whole-body musculoskeletal systems for these tasks, MPC2 exhibits consistent and stable control performance across various tasks, enabling navigation over different terrain conditions." It would be nice to support this claim by comparing against various MPC/control approaches.
- What are the "DRL-based methods" compared against in section 5.2?
- what are the actual values of the "weights of the position error terms for different body parts" that are optimized? is there an interesting trend, such as significant deviation from uniform values? does it correspond to the last figure in the appendix?
- it's not clear to me what the 'instant rollout' means
- "Figure 6(b) shows that MPC2 significantly outperforms both the constant gain and PD control variants." How are these variants computed? Can you not tune/learn the parameters of the PD (or PID) controller such that it improves the walking distance significantly in Figure 6b?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents a system for using a sampling-based model predictive controller to control a musculoskeletal character with a large number of actuators. Key components include: (1) reducing the number of variables using only a single posture target as the control signal. (2) A modification to the sampling strategy that also samples around the current pose.

### Strengths
The method is easy to understand and is shown to efficiently generate control signals to do various tasks on a high-dimensional simulated humanoid. 

The method allows for the rapid iteration of reward/cost function design.

It is surprising to me that MPPI works well when the sampling signal is just a fixed repeated pose. It could be an interesting observation to the control community.

### Weaknesses
There are no videos of the result, so it is hard to judge the quality of the synthesized controller.

There is not much contribution related to machine learning methodology or insights.

Morphology typically means sizes and shapes of the character, so I was originally expecting to see the controller can adapt to different shapes or sizes, but it seems not the case. I suggest changing the word morphology to something more accurate, e.g., configuration.

I don't think it is fair to compare it to a reinforcement learning method when the action space used is different. It would be better if both algorithms used the same action space.

It seems like instant rollout is only useful for the one very specific scenario discussed. Is it necessary for other scenarios?

### Questions
Morphology typically means sizes and shapes of the character, so I was originally expecting to see the controller can adapt to different shapes or sizes, but it seems not the case. I suggest changing the word morphology to something more accurate, e.g., configuration.

I don't think it is fair to compare it to a reinforcement learning method when the action space used is different. It would be better if both algorithms used the same action space.

It seems like instant rollout is only useful for the one very specific scenario discussed. Is it necessary for other scenarios?

It would be great if videos of the results can be shared.

### Soundness
3

### Presentation
3

### Contribution
2
