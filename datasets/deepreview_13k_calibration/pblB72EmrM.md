# HumanoidOlympics: Sports Environments for Physically Simulated Humanoids

- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 3, 5, 6

## Abstract
\vspace{-4mm}
We present $\name$, a collection of physically simulated environments that allow humanoids to compete in a variety of Olympic sports. Sports simulation offers a rich and standardized testing ground for evaluating and improving the capabilities of learning algorithms due to the diversity and physically demanding nature of athletic activities. As humans have been competing in these sports for many years, there is also a plethora of existing knowledge on the preferred strategy to achieve better performance. To leverage these existing human demonstrations from videos and motion capture, we design our humanoid to be compatible with the widely-used SMPL and SMPL-X human models from the vision and graphics community. We provide a suite of individual sports environments, including golf, javelin throw, high jump, long jump, and hurdling, as well as competitive sports, including both 1v1 and 2v2 games such as table tennis, tennis, fencing, boxing, soccer, and basketball. Our analysis shows that combining strong motion priors with simple rewards can result in human-like behavior in various sports. By providing a unified sports benchmark and baseline implementation of state and reward designs, we hope that $\name$ can help the control and animation communities achieve human-like and performant behaviors.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work presents a collection of environment settings in Isaac Gym and the benchmark for single-person sports and multi-person sports using several reinforcement learning algorithms. Human demonstration data could be obtained from videos using some existing motion reconstruction pipeline.

### Strengths
The tasks in this work are about sport activities. These tasks are not easy and a variety of tasks are included ranging from simple actions to complex competition scenarios. It also shows processed human demonstration data from videos are helpful for the learning tasks and very detailed benchmark results are provided.

### Weaknesses
This work leverages several existing components to build a framework for training simulated humanoids. Although the tasks are interesting, the overall contribution is kind of marginal because most of the work is about implementation and benchmark of existing algorithms. The core novelty is limited, as the paper primarily focuses on integrating existing techniques rather than introducing fundamentally new methodologies or insights into the underlying challenges of humanoid control and reinforcement learning. The selection of tasks, while diverse, does not present a significant departure from existing benchmarks in the field, and the performance gains achieved are incremental rather than transformative.

### Questions
1. What are the challenges to set up the training environment for sports in Issac Gym compared with other tasks? This could be a good motivation and make the work not just about implementation.
2. The reward functions are carefully designed for these tasks which is also claimed to be very important for good simulation results. I am wondering how much better these reward functions could be compared with simple reward functions?

### Soundness
2

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
5

### Summary
This paper aims to provide a simulation environment that includes humanoid robots capable of performing a range of Olympic sports, such as long jump and tennis. However, most or all of the proposed simulation activities are ambitious and likely not feasible for current state-of-the-art humanoid robots (e.g., Unitree H1 and G1).

### Strengths
+ If successful, building a high-fidelity simulation of humanoid robots with diverse tasks could greatly contribute to the research community focused on humanoid robotics.

+ Demonstrating the capabilities of humanoid robots to perform Olympic games sounds fascinating.

### Weaknesses
- The proposed humanoid simulation is overly optimistic and ambitious, and it does not consider or justify the feasibility of deployment on real physical humanoid robots. For example, please explain how a Unitree H1 robot could perform a long jump or high jump. Can the motors provide enough torque for the robot to achieve this? The physical H1 lacks an ankle joint, so how can it perform lateral movements efficiently? Furthermore, the simulation does not account for the limitations of the robot's actuators, such as velocity and acceleration limits, which are critical for dynamic movements like jumping. The paper also fails to address the challenges of impact forces during landing, which could significantly affect the robot's stability and structural integrity. These omissions make the simulation's results questionable for real-world transfer.

- The paper does not show validation of the simulation or methods trained in the simulation on real robots. The significant sim-to-real gap in this simulation due to simplified assumptions on physical constraints (e.g., kinematics, dynamics, and torque capabilities) makes this work less valuable to the robotics community focused on physical humanoid robots. The simulation appears to use idealized models without considering the complexities of real-world sensor noise, actuator backlash, and unmodeled dynamics. This lack of realism makes it difficult to assess the practical applicability of the proposed methods. The absence of any discussion on how the simulation parameters were chosen or validated further weakens the credibility of the results.

- In my opinion, designing a diverse set of activities is not the main bottleneck for humanoid simulation. The real challenge lies in accurately modeling a humanoid's kinematics, dynamics, torque and motion constraints, and physical interactions with the environment. The paper focuses on task diversity but neglects the crucial aspect of accurate physical modeling. For instance, the simulation should incorporate realistic friction models, contact dynamics, and the effects of compliance in the robot's joints. Without these considerations, the simulation will likely produce unrealistic behaviors that cannot be replicated on physical robots.

### Questions
See above.

### Soundness
1

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
4

### Summary
This paper proposes a simulation environment for the simulation and learning of various sports tasks using several humanoid robot designs. Through dense reward design and learning from demonstration schemes, which use two different methods from the literature called PULSE and AMP, the authors show that the RL algorithm PPO can learn more human-like motion for these robots. The humanoids are compatible with SMPL motion, and the SMPL human motion parameterization provides (together with the use of algorithms for the transfer task) a relatively easy way to transfer motion from humans to the humanoids. Various comparisons are made in the Experiments section using PPO, PULSE, AMP and their combinations, showing the effects/contributions coming from the different algorithmic components.

===== POST-REBUTTAL RESPONSE =====

I thank the authors for their rebuttal and for answering my questions. I am not going to raise the score, because after careful reading of other reviews and the general rebuttal, I tend to think that the contribution is a bit marginal. I would have liked to see more effort on the reward design / simulation side to address some of my concerns. 

However I liked the writing style and the presentation of the material, I encourage the authors to continue working on it [if not accepted] and either (i) submit to a non-learning-focused conference as is (or with small modifications) or (ii) expand on the learning contributions (e.g. more RL focus, sim-to-real focus etc.) and submit to a ML conference.

### Strengths
There seems to be a clear, albeit modest, contribution to the literature: having a unified simulation environment for the testing/simulation of various sports tasks for various humanoids is going to be useful for the community, as we try to push current RL methods to higher dimensional systems and more complex scenarios. Moreover, the paper is well written and presents their work clearly.

### Weaknesses
However there are some limitations and weaknesses, some of which could be addressed / improved perhaps in the rebuttals:

- The methods are not introduced adequately, in particular it is not clear what PULSE and AMP are doing. The appendix discusses how the authors used PULSE for their work but it is not enough to form a clear picture of what PULSE is doing, and AMP is not discussed. There needs to be a longer, more self-contained discussion I think, some of which should be streamlined with the main text. Specifically, the paper lacks a clear explanation of how these methods leverage human motion data. For instance, is the human motion data used as a direct imitation target, or is it used to shape the reward function, or both? The precise mechanisms of how these methods incorporate human motion priors are not adequately detailed, making it difficult to assess their contribution.
- Only PPO is used as the baseline RL algorithm in the Experiments but the paper in the introduction and conclusion states that they 'benchmark' the humanoids control algorithms, which is clearly an overstatement. If the authors claim that benchmarking is a contribution of the paper, then we need more careful investigation of different RL (or non-RL) approaches. The paper should explore a wider range of RL algorithms, such as SAC or TD3, to provide a more comprehensive benchmark. The current approach limits the scope of the benchmarking and does not fully explore the potential of different RL algorithms for humanoid control.
- There should be ablations and more experimentation of reward design, especially the effect (of different or varying reward designs) on the human-likeness of the learned motions and the effect on the task success rates should be discussed. See one of the questions below for more details on this point. The paper should include a detailed analysis of how different reward components affect the learned behavior. For example, how does the weighting of the task completion reward versus the human-likeness reward influence the final policy? The lack of such ablations makes it difficult to understand the impact of individual reward components.
- As a more minor point, the experiments use only a three-layer MLP to learn the RL policy, which may be too limiting. The paper should justify the choice of a three-layer MLP and discuss its limitations. It is possible that a more complex network architecture, such as a recurrent neural network or a transformer, could lead to better performance, especially for tasks requiring temporal reasoning.

### Questions
Some questions and minor points/corrections:
- "Embodiement" -> Embodiment
- "Another important challenge of working with simulated humanoids is the ease of obtaining human demonstrations." Is it a challenge, or is it an opportunity not sufficiently exploited (till now)?
- Would be nice to mention why SMPL humanoids have 3DOF actuation per joint.
- "To overcome this, we design dense reward functions to guide the learning process." But wouldn't this be interfering with the original task? Can you toggle them off if needed? It's not necessary to overly-constrain the robots: we might miss out on some interesting strategies if we over-specify the reward.
- A contrary point to the above perhaps with respect to the dense rewards: instead of learning from demonstrations (or in addition to), can you not add dense rewards to encourage more human-like or realistic movement? For instance, you can penalize jerky motion, penalize joint limit violations or apply constrained RL, etc.
- "We modify the humanoid model by replacing its right hand with a 1.4-meter-long golf club." Why not also learn the holding mention, does it make the task too difficult? (similarly for tennis and table tennis, I think there could be an option to add the humanoid hand back)
- p_t^c or c_t^b for the club position?
- terrain height o_t is not changing w.r.t time I guess?
- I suggest removing 1 x notation in eq. (1) and elsewhere for improved readability. (especially so given that you don't discuss scaling)
- is eq. (1) dense meaning that there's a reward generated at each t? (so every 1/30 seconds for a robot operated at 30Hz)
- you don't assume any air friction in eq. (3) it seems.
- check line 304, (1) could come right after "where".
- notation for soccer could be simplified.
- "inhuman behavior" in Figure 4: inhuman has a negative connotation, use e.g. less/not human-like
- what are 'qualitative results' ?
- is PPO not using human demonstrations? That wasn't clear to me from the text initially. Likewise not clear if other methods use PPO as the RL algorithm in the main text (appendix mentions it only).
- "All task policies utilize three-layer MLPs with units [2048, 1024, 512]." How did you decide on this parameterization? What are the inputs to the networks? The observations of the states?
- why only use PPO/AMP/PULSE out of many options? That wasn't clear.
- In general we're lacking critical information about these algorithms to follow the text closely. For instance we have to go to the appendix to: "Notice that AMP and PULSE uses PPO as the optimization method but add respective motion priors (as reward or motion representation)." The main text should be as stand alone / independent as possible from the appendix (I realize it is hard in ML conferences but we should try).
- "PULSE adopts a Fosbury flop technique without specific encouragement" adopts or learns / behaviour emerges?
- Figure 5: "PPO and AMP result in inhuman behavior" What are these "unnatural non-human-like motions" (line 426)? Can you not engineer the rewards easily so that human-like behaviour emerges (or likelihood is increased)?
- "diversifying diverse task difficulties" -> choose one diverse
- Table 3 is not clear, what is the difference between "w/o" vs. "w/"?
- "We find that by combining expert reward design and powerful human motion prior, one can achieve human-like behavior for solving various challenging sports" If this is one of the (and perhaps the strongest, according to the text) contributions of the paper, we'd expect it to be more carefully presented: e.g. by comparing against more RL methods / more investigations on reward design. Moreover, what is the use-case of achieving more human-like behavior? That is not discussed. 
- To continue the point above, one can clearly see for instance that PPO generates ridiculous looking movements, that could never be tried on any hardware. That is because some limits of the robot (jerk limits, or joint limits perhaps) would be exceeded immediately, which can be quite 'dangerous'. So we see that safety can be an important factor, but safety can be achieved through other means than including motion priors, e.g., using constraints, or better reward design. In fact safety may not be achieved merely through human motion priors. 
- task observation (line 160) and goal state seem to be used interchangably in the appendix, making it quite confusing to understand what is the goal of the particular task. For instance in tennis (line 817) only p^{tar} is the goal state whereas the whole task observation is presented as the goal state.

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
4

### Summary
This paper presents reinforcement learning environments for sports by humanoid robot agents. These environments contain some humanoid robot models and designed states and rewards for learning sports. The paper provides the benchmark using a state-of-the-art humanoid control learning method. Learning in the environment uses human demonstrations.

### Strengths
- Reinforcement learning environments for sports by humanoid robot agents are useful for evaluating learning algorithms, understanding human sports, and helping human sports.
- The designed states, designed rewards, and benchmarks enable researchers to use the environments and evaluate their methods. 
- The environments have task difficulty diversity. Thus, the researchers evaluate the performance of their method using the environments.

### Weaknesses
The design of the proposed environments looks straightforward. Highlighting the difficulty of designing the rewards and states could help readers understand the paper's contribution more. Do agents using states and rewards other than the proposed ones fail to solve tasks? Do the environments equipped with states and rewards other than the proposed ones fail to represent real sports? The paper lacks a detailed discussion on the specific challenges encountered when designing the state and reward functions for different sports. For instance, the nuances of capturing the dynamics of a sport like fencing or the complexities of a golf swing are not thoroughly explored. The paper would benefit from a more in-depth analysis of how the chosen state representations and reward structures impact the learning process and the resulting agent behavior. Furthermore, the criteria for selecting the specific sports included in the environment are not clearly justified. A more detailed explanation of why these particular sports were chosen over others, and how they contribute to the overall diversity and challenge of the benchmark, would be beneficial.

### Questions
- How is it challenging to design states and rewards and select sports for the environments? 
- Did the authors face particular challenges in designing states and rewards for any sports?
- What are the criteria for selecting which sports to include? 
- Which unique difficulty did the authors encounter when modeling certain sports compared to others?
- How did the authors balance realism with computational feasibility?

- Do the environments have specific advantages that other environments rarely have?
- How does HumanoidOlympics differ from or improve upon specific existing humanoid or sports simulation environments? 
- Are there particular aspects of human-like motion or sports-specific challenges that these environments capture better than others?

### Soundness
3

### Presentation
3

### Contribution
3
