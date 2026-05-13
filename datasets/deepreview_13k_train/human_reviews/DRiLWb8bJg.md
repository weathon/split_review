# Stabilizing Reinforcement Learning in Differentiable Multiphysics Simulation

- Decision: Accept
- Scores: 6, 8, 8, 8

## Abstract
Recent advances in GPU-based parallel simulation have enabled practitioners to collect large amounts of data and train complex control policies using deep reinforcement learning (RL), on commodity GPUs. However, such successes for RL in robotics have been limited to tasks sufficiently simulated by fast rigid-body dynamics. Simulation techniques for soft bodies are comparatively several orders of magnitude slower, thereby limiting the use of RL due to sample complexity requirements. To address this challenge, this paper presents both a novel RL algorithm and a simulation platform to enable scaling RL on tasks involving rigid bodies and deformables. We introduce Soft Analytic Policy Optimization (SAPO), a maximum entropy first-order model-based actor-critic RL algorithm, which uses first-order analytic gradients from differentiable simulation to train a stochastic actor to maximize expected return and entropy. Alongside our approach, we develop Rewarped, a parallel differentiable multiphysics simulation platform that supports simulating various materials beyond rigid bodies. We re-implement challenging manipulation and locomotion tasks in Rewarped, and show that SAPO outperforms baselines over a range of tasks that involve interaction between rigid bodies, articulations, and deformables.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This manuscript introduces Soft Analytic Policy Optimization (SAPO), a learning framework for sequential policy optimization that combines reinforcement learning, particularly maximum entropy reinforcement learning, and differentiable simulation. The authors differentiate the soft state value function estimator and make a set of hyper-parameter and architecture modifications for a better and more stable algorithm with practical implementation. To demonstrate the effectiveness of their method, the authors implement six different simulated environments with highly heterogeneous physics, including elastic bodies, articulated bodies, and fluids. These environments are used for both locomotion and manipulation tasks with a highly efficient GPU-based implementation using Warp.

### Strengths
1. The paper is well-written. I did not find any mathematical mistakes or factual errors.
2. The approach of differentiating the maximum entropy reinforcement learning is valid and I personally found it interesting.
3. The results look promising with good visualizations.
4. The release of nicely implemented simulation environments can be useful for the robotics community.

### Weaknesses
1. The implementation details of the simulated environments are missing. How is the robotic ant simulated and actuated? What are the Young's modulus and Poisson's ratio of the elastic body? And fluid? What about the reward function for each environment?
2. I found the visual encoder part to be extremely confusing. Why a PointNet is used for visual encoder? Does the word "visual" mean point cloud instead of images here? Since the title of appendix A.1 is "Learning Visual Encoders in Differentiable Simulation", I would assume the visual encoder is learned from scratch. Why not use a pre-trained model?

Minor typo:
    Line 50: scaling -> scale

### Questions
1. The authors declare that the design choices have larger impact to SAPO than to SHAC: what is the reason behind it? Could the authors provide some insights?
2. I am confused by the TrajOpt baseline. I would guess that the environments are randomly initialized, which makes the trajectory optimization statistically impossible to work since it only replays the mean of learned actions. However, I found it better than some of the baselines. I might need more explanation here.
3. APG baseline also looks weird to me. Typically my experience with APG gives me impression that it instantly improves in a very short time and plateaus. However, the figures show it constantly improves. Is there a reason behind it? Or my impression is wrong?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces Rewarped, a differentiable multiphysics simulator, and SAPO (Soft Analytic Policy Optimization), a maximum entropy RL method designed to leverage differentiable simulation for efficient policy learning. SAPO uses Rewarped’s capabilities to compute on-policy, first-order policy gradients, maximizing a maximum entropy RL objective. Built on NVIDIA's Warp, Rewarped includes a parallelized Material Point Method (MPM)-based soft body simulator with two-way coupling, providing an advanced simulation environment that supports a variety of rigid and soft body manipulation tasks. Benchmark results show that SAPO outperforms current state-of-the-art methods across challenging locomotion and manipulation environments.

### Strengths
1. The paper is well-written and the ideas are presented clearly, making it accessible and easy to follow.
2. The parallelized soft body simulator in Rewarped is a notable advancement. Integrating soft body manipulation environments within a unified Warp-based framework provides an excellent foundation for further research on differentiable physics and soft body RL.
3.  SAPO's combination of on-policy soft policy learning with an off-policy critic is an effective method for differentiable physics-based RL. This design mitigates the complexity of offline policy gradient evaluation while still benefiting from the simulator’s analytical gradients.
4. SAPO demonstrates strong performance on complex soft body manipulation tasks, such as dexterous hand manipulation, consistently outperforming baseline methods.
5. The authors’ commitment to releasing the dataset and simulation code enhances the reproducibility and accessibility of their work.

### Weaknesses
1. While combining maximum entropy with differentiable physics is a promising approach, it may appear incremental, as similar techniques have been explored in prior RL literature. Specifically, the use of maximum entropy regularization in policy optimization is not novel, and the paper could benefit from a more detailed discussion of how SAPO's approach differs from existing methods that also use entropy regularization in conjunction with differentiable models. The novelty of the specific combination with analytic gradients from a differentiable simulator should be more clearly emphasized.
2. If I understand correctly, only one-way coupling is considered in MPM simulator. It would be nice if two way coupling could be added to allow impact back on the rigid body as in Maniskill2. The current implementation limits the simulation's ability to accurately model scenarios where the soft body significantly affects the rigid body's motion, such as in complex manipulation tasks where the soft body's deformation might exert considerable force back onto the manipulator. This simplification could impact the transferability of policies learned in simulation to real-world scenarios.
3. The paper lacks a discussion of the efficiency gains from the parallelized MPM implementation. Including an analysis of wall-time efficiency or runtime comparisons would provide valuable insight. The paper should include a detailed breakdown of the computational costs associated with the parallelized MPM, such as the time taken for each simulation step, the overhead of parallelization, and how these scale with the number of particles and environments. This information is crucial for assessing the practical applicability of the simulator.

### Questions
1. A comprehensive ablation study would provide valuable insights into the effectiveness of different design choices. For instance, comparing the performance of SAPO with different activation functions (e.g., ELU vs. SiLU).
2. I am curious about the improvements brought by the paralleled MPM. how much acceleration can be achieved with the paralleled MPM, compared with the version in DexDeform? How much GPU memory is required?

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
3

### Summary
This paper releases a new algorithm called SAPO which acts better on Soft rigid body dynamics and also a simulator, with the main contribution being sample efficient RL on these kinds of problems. SAPO is a model-based, actor-critic method that leverages analytic gradients from a differentiable simulator to optimize a stochastic policy with entropy maximization.  Rewarped is the simulator, a  differentiable multi-physics simulation platform capable of simulating soft bodies which usually have slow simulation times. They demonstrate that SAPO with Rewarped achieves superior performance on manipulation and locomotion tasks that require handling interactions between rigid structures and deformables outperforming baseline approaches.

### Strengths
1. The paper is well motivated. The authors take inspiration from max entropy model free RL and extend this to SOTA first order model based RL. 
2. The contribution of a accelerated differentiable simulator for soft body dynamics is welcome.
3. The paper is comprehensive in providing an ablation over components of their method and also provides explanations for their design choices.

### Weaknesses
1. Since this work is inspired by model-based reinforcement learning (MBRL) and maximum entropy RL, and the authors present a first-order MBRL algorithm based on the max-entropy RL framework, they should clearly distinguish their approach from prior work, such as this paper(https://arxiv.org/abs/2112.01195) and this one (https://ieeexplore.ieee.org/document/9892381). While it can be argued that these works use a world model rather than a differentiable simulation, this distinction should be explicitly discussed. A brief discussion on the potential inter-applicability of world model and gradient simulator-based methods could open up promising directions for future research. A comparison of the novelty, applications, and results of these works would strengthen the contribution of the paper. Specifically, the paper should clarify how SAPO's approach to policy optimization via analytic gradients differs from methods that use learned world models and backpropagation for policy updates. The current discussion does not sufficiently highlight the specific advantages and limitations of each approach in the context of soft body dynamics, particularly concerning sample efficiency and computational cost. Furthermore, the paper should address how the choice of a differentiable simulator impacts the generalizability of the learned policies compared to world model-based methods which might be more robust to domain shifts.
2. It is not directly intuitive as to why the review of Zeroth Order Batched Gradient is necessary in the main manuscript in Section 3 Equation 4. It is my understanding that the paper builds on top of first order model based RL methods instead. If this section is indeed required please elaborate on it's importance. The inclusion of ZOBG, while a standard technique in RL, seems misplaced given the focus on first-order methods. The paper should clarify why a discussion of ZOBG is necessary for understanding the FOBG, especially since the paper does not use ZOBG in its algorithm. A more direct explanation of how the analytic gradients derived from the differentiable simulator are used to optimize the policy would be more beneficial than a review of ZOBG. The current explanation does not clearly articulate the connection between ZOBG and the core contribution of the paper, which is the use of first-order gradients from a differentiable simulator.

### Questions
1. How does the simulation speed scale with number of particles in the soft body simulation ? A discussion on this can greatly help in understanding the applicability of Rewarped. A potential experiment of interest can be simulation speed vs number of particles.
2. Similarly, what is the effect of number of parallel environments on the simulation speed ? Similar to the above experiment, a table/plot showing simulation speed vs num of parallel environments on a standard consumer grade GPU (eg. 4090)

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This work proposes a first-order model-based reinforcement learning (FO-MBRL) method that combines differentiable simulation and entropy maximization. It also provides a new parallel differentiable simulator that supports various physical systems. The paper demonstrates the efficacy of its proposed FO-MBRL on typical test environments implemented in the new differentiable simulator and reports its performance gain over several representative baselines from reinforcement learning and differentiable simulation.

### Strengths
- The paper is well-organized and nicely written. In particular, I like the way the paper organizes the background section and the preamble in the experiment section;
-  The discussion on the design decisions (Sec. 4.2) is informative for practitioners. The paper is upfront with these specific choices in the framework, which I really appreciate;
- The quality of the simulation environments seems respectable, and the rendering is well-polished (Fig. 1). I am inclined to believe this differentiable simulator has the potential to be a major player in the future, but I’d like to check a few more details (See weaknesses).
- The experimental results and the ablation study look convincing to me.

### Weaknesses
One contribution claimed by this work is the new differentiable simulator that simultaneously accommodates GPU parallelization, multiphysics, and differentiability.
- I didn’t find detailed specifications of the environments, or maybe I missed them. The claim of this simulator is quite ambitious, and verifying this claim requires scrutinizing many technical details. In particular, I am looking for at least the following information: 1) the simulation problem size, including grid and particle numbers in MPM and the time step sizes; 2) the treatment of multiphysics coupling and their gradients, e.g., rigid-soft contact and solid-fluid coupling as shown in Fig. 1. The provided simulation instances, with fewer than 3000 particles, are significantly smaller than those demonstrated in DiffTaichi (e.g., 30K particles). This difference in scale should be explicitly acknowledged in the main paper to provide a more accurate context for the simulator's capabilities.
- Table 1 and the related work should also discuss DiffTaichi, which I believe supports GPU parallelization, deformable solids and fluids, and gradient computation.
- While I highly appreciate the engineering effort behind Rewarped, I don’t see much technical/algorithmic novelty in Sec. 5: the core simulation algorithms behind rigid/soft/fluids are from existing (differentiable-)MPM papers and GPU parallelization is offered by Warp. Grinding existing differentiable simulators in Table 1 and the related work section is a bit unnecessary :)

### Questions
I am generally happy with this work, and my major concern has been listed in the weakness section. Several very minor questions:
- I am under the impression that there should have been a log function in Eqn. 4 (somewhat similar to Eqn. 2 in Georgiev 24). Could you confirm your Eqn. 4 is correct?
- Eqn 12: where is (sl, al) in the inner expectation sampled from? Does this notation miss a probability distribution?
- How is your simulation gradient backprogagated through the stochastic policy tanh (line 332) exactly?

### Soundness
3

### Presentation
4

### Contribution
3
