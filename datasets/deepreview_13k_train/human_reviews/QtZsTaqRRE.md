# Accelerated Online Reinforcement Learning using Auxiliary Start State Distributions

- Decision: Reject
- Scores: 3, 3, 5

## Abstract
Learning a robust policy that is performant across the state space, in a sample efficient manner, is a long-standing problem in online reinforcement learning (RL). This challenge arises from the inability of algorithms to explore the environment efficiently. Most attempts at efficient exploration tackle this problem in a setting where learning begins from scratch, without prior information available to bootstrap learning. However, such approaches often fail to fully leverage expert demonstrations and simulators that can reset to arbitrary states. These affordances are valuable resources that offer enormous potential to guide exploration and speed up learning. In this paper, we explore how a small number of expert demonstrations and a simulator allowing arbitrary resets can accelerate learning during online RL. We show that by leveraging expert state information to form an auxiliary start state distribution, we significantly improve sample efficiency. Specifically, we show that using a notion of safety to inform the choice of auxiliary distribution significantly accelerates learning. We highlight the effectiveness of our approach by matching or exceeding state-of-the-art performance in sparse reward and dense reward setups, even when competing with algorithms with access to expert actions and rewards. Moreover, we find that the improved exploration ability facilitates learning more robust policies in spare reward, hard exploration environments.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The authors propose an algorithm for selecting start state distributions other than the given start conditions. They introduce a mathematical definition of safety that represents the probability of a policy triggering an early episode termination. And two practical algorithms inspired by this mathematical object. The first algorithm produces a sampling distribution over given offline demonstrations using the length of the episode as a proxy for task success. The second algorithm uses this distribution to sample start states, simulating from the sampled state.

The algorithm is evaluated in the sparse Lava Bridge Environment against Inter-Quartile Learning + Jump Start Reinforcement Learning, an offline reinforcement learning algorithm combined with an exploratory policy learning algorithm and HySAC, a hybrid algorithm that learns online and utilizes offline demonstrations. They are able to beat the provided baselines.

The algorithm is further evaluated in three simple continuous control MuJoCo tasks, matching the performance of HySAC, and with fewer offline data than other algorithms in the Lava Bridge Environment. 

Finally, they compare against sampling uniformly and with a different heuristic in the Lava Bridge Environment.

### Strengths
The introduction of the safety state distribution is quite interesting and the experiments in 5.4 and 5.5 provide useful insight into the benefits of this metric. Because of this, the algorithm is motivated in principle and is quite easy to implement.

### Weaknesses
Unfortunately the baselines in the main experiments are not designed for and do not have access to resetting to arbitrary states and are not directly comparable. JSRL seems to learn a policy that explores, so it will inevitably spend more samples getting to critical states
There are other state of the art baselines that also could have been included like simple behavior cloning or [1].

The MuJoCo experiments could have been augmented to be sparse, like ant maze. Showing that the algorithm matches the performance of HySAC does not provide useful information.

One big concern is the lack of citation of [2]. They study the benefits of uniform simulator resets in terms of sample efficiency and robustness. Findings in 5.1 and 5.2 are somewhat overlapping with the aforementioned work.

### Questions
How does this algorithm perform in a sparse continuous control task like ant maze?

How does this algorithm perform in higher-dimensional systems like humanoid?

In section 5.3, how do the baseline algorithms perform given the same number of samples (0.5k) as given to AuxSS?

### Soundness
2

### Presentation
2

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
This paper proposes AuxSS, aiming to improve sample efficiency in online RL by sampling the initial states from an auxiliary distribution. The distribution is dynamically updated during training using a Monte Carlo-like scheme. With such auxiliary start distribution, the policy can avoid struggling at the start region of the environment, thus enjoying higher sample efficiency and safety.

### Strengths
- The problem discussed in this paper is novel. Low sample efficiency is a long-existing challenge in online RL, and this paper provides a novel perspective to further address this problem.
- The experiments cover various settings, including both sparse- and dense-reward tasks and different common baselines, showing the effectiveness of the auxiliary start distribution.

### Weaknesses
 - What is the formulation of $J_{\mu_{OOD}}$?
- I do not find any reference of Figure 2. Could you please insert it to the proper place to better explain your algorithm? Besides, I wonder what the color of points in the middle of Figure 2 represents.
- The notation in Algorithm 1 is not clear. For example
  - What does $S_{demo} - S_{demo}[i]$ means if $S_{demo}$ is a state sequence while $S_{demo}[i]$ is a single state?
  - Following the previous question, why $\lambda$ is computed by this equation?
  - Is $W[i]$ the $i$-th position of $W$, or a new variable? If it is a part of $W$, Line 3 has changed its value, so the update in Line 5 is meaningless. If it is a new variable, what does Line 5 do by adding a sequence and a single value?
- The description of Lava Bridge appears at the beginning of Section 5, but the illustration is at Figure 8, Section 5.4, which is quite confusing. Could you please move this illustration to the same place of the description?
- AuxSS is based on the early termination of episodes. However, HalfCheetah-v4 will not terminate until it reaches the timestep limitaion, that is, it will not early terminate. Including this environment does not consistent to the motivation of this paper. Could you please use environments with early termination, such as Hopper or Humanoid?
- Is the Lava Bridge environment first proposed in this paper? If it is, could you please provide detailed information about it, especially the reward function? You only mentioned that "The agent only gets a non-zero reward on reaching the goal state or entering a terminal state", but not giving how much reward the agent will get. As a result, I am confused by the relation between the training reward and the success rate.
- In Section 5.3, I think the performance change of AuxSS over the size of expert demonstration should be included. Will increasing the size of demonstration further promote the performance of AuxSS? And will AuxSS work if the demonstrations are expert but half-way trajectories?
- In Section 5.4, the sampling distributions are unclear. What are the specific formulations of $\Omega$-SS and GoalDist-SS?
- Could you please illustrate how $W$ changes during the training process?
- The formulation of the smoothing parameter $\lambda$ in Algorithm 1 is unclear. As a smoothing parameter, $\lambda$ should be within the range $[0,1]$. However, the formulation in Line 4 does not guarantee this. Furthermore, when $S_{demo}[j]$ is far from $S_{demo}[i]$, there is a risk of overflow for $\lambda[j]$. How is this handled?
- The experiments in Sections 5.2, 5.3, and 5.4 appear to be conducted using only one seed. Given the importance of experimental reproducibility and the potential for seed-dependent variability, the conclusions drawn from these results are not fully trustworthy.
- In Figure 15, only the change in episode length using AuxSS is shown, without any comparison to other baseline methods. Including comparisons to other approaches would strengthen the validity of the claims and provide clearer context for the performance of AuxSS.
- It appears that the sum of the sampling probabilities in the right figure of Figure 16 exceeds 1. However, since the sampling distribution $\mathcal{W}$ is discrete, the total sum should be exactly 1. What do the probabilities in Figure 16 actually represent and why is there this discrepancy?

### Questions
- What is the formulation of $J_{\mu_{OOD}}$?
- I do not find any reference of Figure 2. Could you please insert it to the proper place to better explain your algorithm? Besides, I wonder what the color of points in the middle of Figure 2 represents.
- The notation in Algorithm 1 is not clear. For example
  - What does $S_{demo} - S_{demo}[i]$ means if $S_{demo}$ is a state sequence while $S_{demo}[i]$ is a single state?
  - Following the previous question, why $\lambda$ is computed by this equation?
  - Is $W[i]$ the $i$-th position of $W$, or a new variable? If it is a part of $W$, Line 3 has changed its value, so the update in Line 5 is meaningless. If it is a new variable, what does Line 5 do by adding a sequence and a single value?
- The description of Lava Bridge appears at the beginning of Section 5, but the illustration is at Figure 8, Section 5.4, which is quite confusing. Could you please move this illustration to the same place of the description?
- AuxSS is based on the early termination of episodes. However, HalfCheetah-v4 will not terminate until it reaches the timestep limitaion, that is, it will not early terminate. Including this environment does not consistent to the motivation of this paper. Could you please use environments with early termination, such as Hopper or Humanoid?
- Is the Lava Bridge environment first proposed in this paper? If it is, could you please provide detailed information about it, especially the reward function? You only mentioned that "The agent only gets a non-zero reward on reaching the goal state or entering a terminal state", but not giving how much reward the agent will get. As a result, I am confused by the relation between the training reward and the success rate.
- In Section 5.3, I think the performance change of AuxSS over the size of expert demonstration should be included. Will increasing the size of demonstration further promote the performance of AuxSS? And will AuxSS work if the demonstrations are expert but half-way trajectories?
- In Section 5.4, the sampling distributions are unclear. What are the specific formulations of $\Omega$-SS and GoalDist-SS?
- Could you please illustrate how $W$ changes during the training process?

### Soundness
2

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
This paper addresses the issue of sample efficiency in online reinforcement learning (RL). The authors propose a method, Auxiliary Start State Sampling (AuxSS), which leverages a small set of expert demonstrations and a simulator with arbitrary resets to improve exploration and policy robustness. AuxSS uses an auxiliary start state distribution informed by safety cues—essentially prioritizing task-critical states where safety violations, such as early episode terminations, commonly occur. This approach enables better exploration in environments with sparse rewards and difficult exploration tasks, as it targets states crucial for task completion.

### Strengths
Overall, the paper is well-written and easy to follow. The method is presented clearly with sufficient notations. The idea is interesting and straightforward. The algorithm is compatible with many RL algorithms and can be applied to many scenarios.

### Weaknesses
The below paper seems to be highly relevant, but the authors didn't discuss and compare with it:
- Contrastive Initial State Buffer for Reinforcement Learning (https://arxiv.org/abs/2309.09752v3), which comes with open-sourced code (https://github.com/uzh-rpg/cl_initial_buffer).

Besides, the current experiments only covered a 2D discrete env (lava bridge) and 3 Mujoco task. How would the algorithm perform on high-dimensional tasks with sparse rewards? (the hard tasks in MetaWorld for example)

In terms of "the time to termination"(line 252), do you only consider failure episodes or both successful and failure episodes? From line 240, it should consider the cases of "early episode termination", while it doesn't distinguish between successful and failed runs in algorithm 1.

In Figure 7, it would be better to include the baseline algorithms' performance with 0.5K demonstrations as well. Currently, we don't know if the performance of the baseline algorithms drops with fewer demonstrations.

### Questions
1. Is the algorithm applicable to environments with more randomness? For example, a maze task where the start location, the goal, and the map are all randomly generated for each episode. What would be "task-critical states" for such scenarios?
2. In terms of "the time to termination"(line 252), do you only consider failure episodes or both successful and failure episodes? From line 240, it should consider the cases of "early episode termination", while it doesn't distinguish between successful and failed runs in algorithm 1.
3. How is task horizon H determined and how does it influence the algorithm performance? Does the algorithm work for dynamic-horizon tasks?
4. In Figure 7, it would be better to include the baseline algorithms' performance with 0.5K demonstrations as well. Currently, we don't know if the performance of the baseline algorithms drops with fewer demonstrations.

### Soundness
2

### Presentation
3

### Contribution
2
