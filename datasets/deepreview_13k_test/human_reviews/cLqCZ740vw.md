# Benchmarking Smoothness and Reducing High-Frequency Oscillations in Continuous Control Policies

- Decision: Reject
- Scores: 5, 5, 6, 5

## Abstract
Reinforcement learning (RL) policies are prone to high-frequency oscillations, especially undesirable when deploying to hardware in the real-world. In this paper, we identify, categorize, and compare methods from the literature that aim to mitigate high-frequency oscillations in deep RL. We define two broad classes: loss regularization and architectural methods. At their core, these methods incentivize learning a smooth mapping, such that nearby states in the input space produce nearby actions in the output space. We present benchmarks in terms of policy performance and control smoothness on traditional RL environments from the Gymnasium and a complex manipulation task, as well as three robotics locomotion tasks that include deployment and evaluation with real-world hardware. Finally, we also propose hybrid methods that combine elements from both loss regularization and architectural methods. We find that the best-performing hybrid outperforms other methods, and improves control smoothness by $26.8$\% over the baseline, with a worst-case performance degradation of just $2.8$\%.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper addresses the issue of high-frequency oscillations in reinforcement learning policies, especially when applied to real-world hardware. The authors categorize methods to mitigate these oscillations into loss regularization and architectural methods, aiming to smooth the input-output mapping of policies. They benchmark these methods on classic RL environments and robotics locomotion tasks, introducing hybrid methods that combine both approaches. The study finds that hybrid methods, particularly LipsNet combined with CAPS and L2C2, perform well in both simulations and real-world tasks, achieving smoother policies without compromising task performance.

### Strengths
A technically sound paper with theoretical analysis and experimental support of their discoveries. Aims to get a better understanding and address an important problem in robotics, especially in application to sim2real when high-frequency, noisy policies can damage robot hardware. In addition to sim sim-only results demonstrate the advantages of their approach on a quadruped robot.

### Weaknesses
Lack of experiments, especially for more challenging continuous control tasks. In addition would be good to see more detailed comparisons against MLP baseline - see training curves and comparison of reward and variance vs not only a number of samples but also training time.

### Questions
1) Could you share training plots at least for Ant and quadruped robot for the reward vs wall-clock time for LipsNet + CAPS and LipsNet + L2C2 vs vanilla MLP? Are there losses in training (wall-clock time) performance when using these more advanced methods vs MLP or they are computationally comparable to the vanilla MLP?
2) Could you run experiments for more challenging control problems - humanoid, or on of the Allegro (Shadow) Hand dexterous manipulation tasks?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In the paper, the author investigates algorithms aiming to prevent high-frequency oscillations during the RL sim2real transfer process. They conduct a comprehensive benchmark of both the performance and smoothness of the trained policies. Moreover, they devise a hybrid method, which, as per the results, demonstrates superior performance.

### Strengths
1. The author effectively categorizes various smoothing methods, providing an exhaustive understanding of the diverse kinds of policy smoothing techniques.
2. Extensive benchmarks are conducted, further enhancing comprehension of the performance exhibited by differing algorithms in simulation.

### Weaknesses
1. The paper presents a rather incremental contribution. The author proposes a hybrid method that combines architectural methods and regularization techniques, but it remains unclear how these two components interact or how the policy can be further improved.
2. The performance enhancement of the hybrid method, compared to the baseline, appears limited. Moreover, since oscillations occur during the sim2real process, the author only contrasts the hybrid method with the vanilla policy. This means comparisons to other baselines are omitted, making it unclear how the hybrid method measures up against other methodologies.

### Questions
1. In Figure 2, in the disturbance imitation task test, why does the combination of LipsNet + L2C2 underperform compared to the vanilla policy regarding smoothness?
2. As you have exclusively provided the measure of policy smoothness in real-world situations, I'm curious as to how the real-world performance (reward) measures up against other baselines?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors benchmark several recent methods for imposing smoothness on policies. The benchmarks are mainly done in simulation, and one the best performing method is evaluated in a sim2real transfer against a vanilla RL policy.

### Strengths
- Benchmark papers are important for the community, and the sim benchmark evaluation on policy smoothness appears to be carefully constructed 
- Reducing oscillations is important, and a common problem in sim2real as the authors note in their conclusions
- The paper is mostly well-written and easy to read

### Weaknesses
Overall I think this is a useful benchmark paper but it has some issues with framing:
- The authors (and title even) mix the concepts of policy smoothness and reducing high-frequency oscillations, but how these concepts relate and why you get oscillations is not thoroughly defined. The paper also talks about sim2real where oscillations are indeed a common problem, but the authors do not make a convincing argument that this is due to non-smooth policies. Sometimes it might be but this has not been well explored as far as I am aware. Overall the paper does a good job of benchmarking existing approaches to increase policy smoothness, but the sim2real / oscillation connection seems weak.
- More in that vein, the sim2real is only attempted with the best performing method from simulation. If simulation was a good indicator of real-world performance, sim2real would be much easier than it currently is, but this is not the case in my experience. If you want to make this paper about sim2real instead of just policy smoothness, then it would be useful if you had tested all the approaches in the real world to see how the approaches generalized. It would also have been useful to see a video of the experiments as is conventional in robotics. Did the robot actually oscillate or is your smoothness metric just picking up a quick motion (e.g, a simple step function also has high-frequency components)? These can sometimes be desirable. 

As it currently stands, I would consider toning down the sim2real implications a little bit and focus more on smoothness.

Minor: 
typo: hyperaparameter

### Questions
"... but in the open-source code a linear activation is used. In our implementation, we used a softplus activation as in the original paper." - This seems like an arbitrary choice that might degrade the performance of a defacto available option. Maybe the implementation is more up to date, or there was a typo in the paper?  Can you test and confirm that it performs as well, or why not include both versions?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The authors investigate methods for reducing the emergence of high-frequency oscillatory behavior when learning continuous control policies. Such behavior is undesirable in real-world robotics applications, however, explicit regularization introduces complex trade-offs. It is then important to identify approaches that gracefully prevent high-frequency motions while maintaining overall performance. This paper aims to provide a benchmark analysis of various method aiming to address this challenge.

### Strengths
- Investigating methods to reduce high-frequency oscillatory behavior in continuous control is an important research direction with real-world impact
- PPO is a good primary baseline choice due to its recent success in enabling sim-to-real transfer of complex behaviors in robotics
- Results are averaged over 9 seeds to yield statistical significance

### Weaknesses
- The discussion of related work is rather limited and should be expanded by a control theory angle, particularly relating to natural emergence of bang-bang-type controllers [1] or pulse-width modulation. Established benchmarks such as the DeepMind Control Suite can furthermore often be solved with high-frequency bang-bang control as studied in [2] or general discretization in [3] – these works provide further motivation for the need of well-designed benchmarks as this paper aims to provide.
- A very relevant related work that automatically learns regularization trade-offs was presented in [4]
- The majority of cumulative returns as well as smoothness scores in Table 1 have overlapping error bands making performance differences difficult to judge.
- The current evaluation has insufficient breadth to serve as a benchmark for smooth continuous control. The analysis relies on empirical data and as such should cover a large representative range of (robotics) tasks or baseline algorithms, ideally both. 
- Pendulum/Reacher/Lunar Lander are rather toy-ish examples that are not representative of the challenges the paper aims to analyze, while they could provide good illustrative examples if analyzed more in-depth
- The analysis would profit from extension to a broader set of baseline algorithms other than PPO to identify trends in order to serve as an extensive benchmark



[1] R. Bellman, et al. "On the “bang-bang” control problem," Quarterly of Applied Mathematics, 1956.

[2] T. Seyde, et al. "Is Bang-Bang control All You Need? Solving Continuous Control with Bernoulli Policies," NeurIPS, 2021.

[3] Y. Tang, et al. "Discretizing Continuous Action Space for On-Policy Optimization," AAAI, 2020.

[4] S. Bohez, et al. "Value constrained model-free continuous control," arXiv, 2019.

### Questions
- Why did the “Locomotion – Velocity Controller” task not use the action rate penalization of Rudin (2021)?
- What do state and action trajectories of trained policies look like? How do they compare across agents?
- How does policy performance and smoothness compare across agents when simply varying weights of action magnitude/smoothness penalties in the reward function? As this is commonly how practitioners counteract high-frequency behavior, such an analysis would improve insights drawn from a benchmark.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
