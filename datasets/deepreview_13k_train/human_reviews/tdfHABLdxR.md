# Constrained Skill Discovery: Quadruped Locomotion with Unsupervised Reinforcement Learning

- Decision: Reject
- Scores: 5, 5, 5, 6

## Abstract
Representation learning and unsupervised skill discovery can allow robots to acquire diverse and reusable behaviors without the need for task-specific rewards.
In this work, we use unsupervised reinforcement learning to learn a latent representation by maximizing the mutual information between skills and states subject to a distance constraint. Our method improves upon prior constrained skill discovery methods by replacing the latent transition maximization with a norm-matching objective. This not only results in a much a richer state space coverage compared to baseline methods, but allows the robot to learn more stable and easily controllable locomotive behaviors.  We successfully deploy the learned policy on a real ANYmal quadruped robot and demonstrate that the robot can accurately reach arbitrary points of the Cartesian state space in a zero-shot manner, using only an intrinsic skill discovery and standard regularization rewards.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper extends the Lipschitz-constrained Skill Discovery (LSD) framework by Park et al. (2022) to enable the learning of stable and controllable locomotion skills with broader state-space coverage. The proposed approach learns a skill-conditioned policy, where each skill is represented by a 2D continuous vector. This method allows robots to navigate at varying velocities without relying on task-specific rewards, instead using intrinsic mutual information and extrinsic regularization rewards. The authors further demonstrate that the policy can achieve effective zero-shot goal-tracking performance in quadruped locomotion tasks involving the ANYmal robot.

### Strengths
- The figures are well-illustrated and nicely done. I especially like Figures 1 & 4, which show a representation of skills in the 2D space.
- Real robot experiments using an ANYmal quadruped

### Weaknesses
1. The contributions are unclear. Could the authors clarify how this work improves upon LSD (Park et al., 2022)? Specifically, could you present a side-by-side comparison of the two objectives, highlighting what has been added or removed, and explain the rationale behind these changes?
2. It appears that this approach may not perform well in environments with obstacles. Based on the illustration of the sampled skills, it seems that the quadruped is capable of reaching any 2D location on a plane, but only in the absence of obstacles.
3. The authors overlook many relevant works related to skill discovery, including references [1-7]. Note that these works may use different terminology, such as 'options,' to achieve similar objectives.
4. The term 'skill' is not clearly defined. What is the duration of a skill? Does a skill have a termination condition? What constitutes a skill?
5. While I appreciate the demonstration of results on a real robot, it would also be valuable to see results on simulated benchmarks to better illustrate the efficacy of the proposed approach compared to LSD and Metra.

### Questions
1. In Equation 10, it seems there may be a misuse of notation. Is \( N \) a scalar rather than a function? If so, is this simply a multiplication?
2. How does this approach handle practical environments with obstacles?
3. What is the rationale behind restricting the latent space to a 2D vector? Could you provide some intuition on when this restriction might be beneficial and when it might need to be extended?
4. In Figure 3, the density distribution of the proposed method appears similar to a uniform random distribution. Why is this desirable? Does it indicate greater coverage of the state space?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents a method for constrained skill discovery applied to quadrupedal robot locomotion using unsupervised reinforcement learning. The proposed approach builds upon previous works that use mutual information between skills and states. In contrast to existing works, this paper introduces a norm-matching objective so as to achieve broader state space coverage with stable, controllable movements. This enables a quadruped robot to reach arbitrary points in its environment without requiring task-specific rewards. The proposed method was evaluated on the ANYmal robot.

### Strengths
- Based on the results, the norm-matching objective allows the robot to cover a broader range of states compared to previous approaches.
- It eliminates the need for task-specific rewards by using intrinsic motivation through skill discovery.
- The paper includes successful experiments with an actual robot.

### Weaknesses
 - The novelty of the paper is questionable. It is obvious from the results that the norm-matching objective is indeed helpful, but this is just a simple regularization applied on top of existing methods. It is also the straightforward / obvious solution to the problem the paper talks about. Thus, it may not attract much interest.
- The paper is sometimes very difficult to follow. To me, this is a major concern that is sufficient for my rejection rating, because I believe the paper needs a major rewrite which is beyond a rebuttal. Starting from the second section, it uses a lot of notation and assumes some prior knowledge about skill discovery methods. This makes the paper inaccessible for people who are not working on this topic. A proper notation definition is missing, e.g., the variable z is used for skills starting from Section II but they are not given a formal definition as a mathematical object in the paper.

### Questions
I understand the problem the norm-matching objective is trying to solve. Did existing works try other approaches to solve the same problem and fail? Why is norm-matching interesting / novel? To me, it seemed like the most obvious solution.

### Soundness
4

### Presentation
2

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
This paper proposes a novel unsupervised reinforcement learning method for skill discovery, which improves upon previous constrained skill discovery methods (LSD[1], METRA[2]) by introducing a norm-matching objective. This norm-matching objective replaces latent transition maximization, achieving the following goals: (1) enabling the agent to learn a broader range of skills and reliably cover a larger portion of the state space; (2) addressing the issue of overly aggressive, high-speed movements resulting from the previous maximization objective, which are challenging to deploy on most robotic hardware. Experiments demonstrate that, compared to baseline methods, this approach allows for more accurate target-tracking in quadruped robots and enables zero-shot deployment on actual quadruped hardware.

### Strengths
1. The paper is clearly written, with Sections 2 and 3 providing a well-articulated motivation and a strong connection to prior work. Both the method and empirical studies are explained with considerable detail.

2. The proposed approach allows for skill control in terms of both magnitude and direction, enabling the robot to navigate the environment at different speeds.

3. The experimental results are impressive, particularly the position-tracking comparisons. Compared to previous methods, this approach appears to achieve more accurate position and velocity tracking without relying on task-specific domain knowledge.

### Weaknesses
 - Previous methods [1][2] conducted comparative experiments on multiple benchmark tasks (e.g., Ant, HalfCheetah) and validated their effectiveness across various downstream tasks. This paper, however, only conducts experiments on the ANYmal quadruped robot, focusing primarily on velocity tracking. (If this paper aims to demonstrate the broad applicability of the proposed method, comparison experiments should be conducted on datasets like Ant and HalfCheetah. If the focus is on quadruped robots, it is necessary to compare the method with other controllers designed for quadruped robots.)

- The derivation in Equations 6-7 of the paper contains errors; the coefficients after expanding the squared difference formula are incorrect. What is the purpose of comparing the magnitudes of \( L \) and \( L^{LSD} \)? Compared to \( L \), \( L^{LSD} \) is a simplified result. Does choosing the unsimplified \( L \) as the optimization function make the optimization more complex?
- Figure 7 shows that the ANYmal robot can accurately track velocity commands in the x and y directions. What specific performance criteria were used to evaluate tracking in this experiment? (e.g., The experiment can provide quantitative metrics, such as the mean squared error of position or velocity over time, and compare the performance with controllers that include velocity tracking rewards or controllers from previous methods.)
- In the final 30 seconds of the supplementary video, the test results on the ANYmal robot are demonstrated. However, this section lacks textual and verbal explanations, making it unclear what the paper intends to convey. (e.g., The unannotated parts of the video could include annotations displaying the target position or velocity, or show comparative content.)

### Questions
- The derivation in Equations 6-7 of the paper contains errors; the coefficients after expanding the squared difference formula are incorrect. What is the purpose of comparing the magnitudes of \( L \) and \( L^{LSD} \)? Compared to \( L \), \( L^{LSD} \) is a simplified result. Does choosing the unsimplified \( L \) as the optimization function make the optimization more complex?
- Figure 7 shows that the ANYmal robot can accurately track velocity commands in the x and y directions. What specific performance criteria were used to evaluate tracking in this experiment? (e.g., The experiment can provide quantitative metrics, such as the mean squared error of position or velocity over time, and compare the performance with controllers that include velocity tracking rewards or controllers from previous methods.)
- In the final 30 seconds of the supplementary video, the test results on the ANYmal robot are demonstrated. However, this section lacks textual and verbal explanations, making it unclear what the paper intends to convey. (e.g., The unannotated parts of the video could include annotations displaying the target position or velocity, or show comparative content.)

[1] Seohong Park, Jongwook Choi, Jaekyeom Kim, Honglak Lee, and Gunhee Kim. Lipschitzconstrained Unsupervised Skill Discovery. October 2021.
[2] Seohong Park, Oleh Rybkin, and Sergey Levine. METRA: Scalable Unsupervised RL with Metric-Aware Abstraction. October 2023.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper proposes a method for unsupervised reinforcement learning to enable quadruped robots to autonomously learn diverse locomotion skills. The key idea is to maximize the mutual information between the robot's skills and states while constraining the distance covered, replacing the previous latent transition maximization with a norm-matching objective. This allows for richer state space coverage and more controllable and stable locomotive behaviors than prior approaches. The method demonstrates successful deployment on the ANYmal quadruped robot, where the robot can accurately perform zero-shot goal tracking without any task-specific rewards, relying solely on intrinsic skill discovery.

### Strengths
- The paper is clearly presented, with abundant ablation studies and various baseline methods. The analysis in the experiment part explains well how the introduced constraint can help improve the state space coverage intuitively.
- The experimental setup is thorough, with comparisons against state-of-the-art methods like Lipschitz-constrained skill discovery (LSD) and Metric-aware abstraction (METRA). The paper presents extensive performance evaluations in both simulated and real environments using the ANYmal robot, showing robust results in real-world conditions.

### Weaknesses
 - The proposed method additionally imposes a norm matching constraint on the original LSD formulation to regularize the agent from maximizing the latent space transition. In Eq.9, using L2 norm on the original state space makes sense in the simplified setting where only euclidian distance is considered and XY plan coverage is focused on. It may fail to generalize to more complex state space to diversity skills in to justify the choice of this bound. Think of diversifying in a joint space; it is not reasonable to impose such a bound with the difference between two consecutive joint positions since similar joint states can represent completely different robot gaits.
- Limited experiments on a simplified setting with euclidian space coverage. It would be super helpful and make the proposed method much stronger to show results in style/gait diversification on quadruped, or simulated settings such as maze navigation, where the state space euclidian distance does not reflect the adjacency in the latent space.
- For a fair comparison with ASE and CASSI, one should select encoder input with the same features as in the proposed method. As the authors pointed out, if joint information is considered, the diversity on the XY plane coverage will deteriorate. And the encoder input should consider states of consecutive steps to match the usage in the proposed method, such as (pos_xy, pos_xy', ...).

### Questions
- Regarding weakness 1: if LSD fails to regularize the norm of the latent space transition, why not simply add it back or normalize it to a unit vector maintaining only directional information? Alternatively, why not consider selecting state space such that it encodes \phi(s_t, s_{t+1}) or \phi(s_{t+1}-s_t) where you process the directional information before encoding?
- It would be helpful to demonstrate the applicability of the proposed method with experiments on more complex settings other than the single simplified euclidian space coverage presented in the paper.
- For a fair comparison with ASE and CASSI, one should select encoder input with the same features as in the proposed method. As the authors pointed out, if joint information is considered, the diversity on the XY plane coverage will deteriorate. And the encoder input should consider states of consecutive steps to match the usage in the proposed method, such as (pos_xy, pos_xy', ...).

### Soundness
3

### Presentation
4

### Contribution
3
