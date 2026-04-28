# Latent Trajectory: A New Framework for Actor-Critic Reinforcement Learning with Uncertainty Quantification

- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 5, 3, 3

## Abstract
Uncertainty quantification for deep neural networks is crucial for building reliable modern AI models. This challenge is particularly pronounced in deep reinforcement learning, where agents continuously learn from their interactions with stochastic environments, and the uncertainty of the value function is a key concern for ensuring reliable and robust RL applications. The complexity increases in actor-critic methods, as the training process alternates between optimizing the actor and critic networks, whose optimization nature makes the uncertainty of the value function hard to be quantified. 
To address this issue, we introduce a novel approach to RL training that conceptualizes transition trajectories as latent variables. Building on this framework, we propose an adaptive Stochastic Gradient Markov Chain Monte Carlo (SGMCMC) algorithm for training deep actor-critic models. This new training method allows for the implicit integration of latent transition trajectories, resulting in a trajectory-independent training process. We provide theoretical guarantees for the convergence of our algorithm and offer empirical evidence showing improvements in both performance and robustness of the deep actor-critic model under our Latent Trajectory Framework (LTF). Furthermore, this framework enables accurate uncertainty quantification for the value function of the RL system, paving the way for more reliable and robust RL applications.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
This paper introduces the latent trajectory framework (LTF) that implicitly models the uncertainty of Q-functions by drawing multiple samples of critic parameters, essentially forming a distribution over Q-values.

### Strengths
- The paper provides theroretical justification for the convergence of the proposed method.
- The insight of conditional independence between the critic parameters and past actor parameters given the current state trajectory is particularly interesting.

### Weaknesses
## Lack of related works and comparison
It is hard to position this paper in the context of prior work as it lacks a discussion of how this work relates to existing RL algorithms that model the uncertainty of Q-values. The paper should discuss how this work is different from distributional RL methods, which also model the uncertainty of Q-values. The paper should also discuss why SGMCMC is the suitable method for the problem at hand, in contrast to prior work. This made the paper particularly hard to understand as a reader.

## The problem of uncertainty quantification is not well-motivated
The paper does not provide a clear motivation for why it is important to model the uncertainty of Q-values. It mentions "accurately quantifying the uncertainty of the value function has been a critical concern for ensuring reliable and robust RL applications", but does not provide any concrete examples of why this is the case or precisely in what scenarios this is important. Ideally, the paper should analyze the limitations of existing RL algorithms that do not model the uncertainty of Q-values and provide examples of scenarios where this leads to suboptimal performance, and how the proposed method addresses these limitations in experiments.

## No results on PPO
The paper mentions that PPO suffers from severe miscalibration issues in both the actor and critic, but does not provide any results on PPO to demonstrate this.

## Connecting uncertainty quantification to performance
While the escape environment discusses the relationship of how LTF leads to better MSE of value functions, how this translates to better performance in the escape environment is not clear. Conversely, on other environments, the paper does not provide a clear analysis of how the uncertainty quantification of Q-values leads to better performance.

It is also not so clearly apparent that LT-A2C has smaller seed variability than A2C, as the paper claims. The performance difference is largely imperceptible in the plots, considering the confidence intervals.

### Questions
Can you build a connection to prior works in uncertainty quantification?

How would you make this paper more approachable to a wider audience? Currently, it requires knowing a lot of prior work to make sense of the motivation, algorithm, and convergence proofs. The paper should be largely self-sufficient when reading.

### Soundness
3

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
Uncertainty quantification of the value function is crucial for a robust reinforcement learning algorithm. This work considers the challenging actor-critic setting. The introduced latent trajectory framework (LTF) is built upon the adaptive Stochastic Gradient Markov chain Monte Carlo (SGMCMC) by treating the transition trajectory and the value function parameter as latent variables for policy optimization. The proposed method is theoretically proved to be able to converge under mild conditions. The experiments on indoor escape environments  and PyBullet environment show that the proposed method has better performance compared with baseline A2C algorithms.

### Strengths
- Theoretical results: The proposed LTF is grounded by theoretical convergence results. The paper contains most of the proof details, and the logic in the writing is easy to follow. 
- Experiments: The experiments show multiple metrics for evaluating the performance of the proposed LTF. For instance, the KL and MSE can help evaluate the performance from different perspectives. The results in HalfCheetah show that the proposed method can effectively improve the performance compared with A2C.

### Weaknesses
 - The proposed LTF only compares with the vanilla A2C method, while there have been many  AC-based methods proposed, such as [W1,W2]. I recognize that the proposed LTF introduces a new perspective by treating the value parameters as a latent variable, while the experiments are lacking. In particular, the experiments in Section 4.1 are conducted on rather new environments (by Liang et al.). The lack of comparison with other AC methods (e.g., in experiments and/or related works section) makes the results and performance gain less convincing. If the comparison is not possible or not necessary, please clarify the reasons. 
- The proposed LTF is largely based on SGMCMC algorithms that are proposed in Liang et al., 2022a; Deng et al.,2019, while the major contribution of the LTF is less clear. From my understanding, the main contribution is on the A2C settings, which pose unique challenges for uncertainty quantification. It will be very beneficial for the authors to explicitly state the key challenges of applying SGMCMC to A2C settings and how their approach addresses these challenges.

### Questions
- What is the parameter $\delta_j$ in Eqn. 10?
- What are the relation between $\epsilon_{k,l}$ and $\epsilon_{k} $ in Algorithm 1
- How to select $\mathcal{N}$ in practice?
- Why the variance in Figure 7 for LT-A2C is not significantly reduced if the uncertainty is effectively evaluated during update (e.g., HopperBullet, Evaluation reward)?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors propose a novel method for characterising uncertainty in value functions using a stochastic gradient MCMC algorithm. They carry out a convergence analysis of their method before evaluating PyBullet and Gridworld environments.

### Strengths
The theoretical analysis of the proposed algorithm seems sounds from a cursory readying. Convergence guarantees are always welcome in papers.

### Weaknesses
My main concern relates to lack of positioning of the paper. Bayesian RL offers a precise way to characterise uncertainty in an MDP. At every timestep, the posterior over uncertain variables updates according to a Bayesian Bellman operator. Uncertainty can be characterised in the state-reward transitions as in model-based approaches or other sufficient variables like value functions or Bellman operators as in model-free approaches[4].  There is already a wealth of literature in uncertainty quantification in value functions. See my question below to authors.

The authors claim `Notably, uncertainty quantification for value-functions is generally beyond the reach of conventional iterative optimization algorithms used to train actor-critic models'. This is not true. Methods such optimistic actor-critic [1], BBAC[2] and EVE[3] (to name but a few) have been able to quantify uncertainty in value functions when used in continuous control for some time now as uncertainty quantification is essential to their exploration methods. There also exist analyses of the various approximate inference tools used to quantify uncertainty [5]. See [6] for a recent comparison of state of the art continuous control using uncertainty quantification evaluated in a variety of domains. 

Empirical weaknesses:

There is a significant lack of comparison to other methods that quantify uncertainty in value functions. A comparison of these methods seems essential to evaluate the contribution of the proposed method. Moreover, the authors don't indicate number of timesteps in their evaluations so it is difficult to gauge the worth of their approach in comparison to similar Bayesian methods.

### Questions
How does the proposed method fit into the general model-free Bayesian RL framework that precisely characterises uncertainty in value functions? How does $\pi_\mathcal{N}(\psi\vert \theta)$ relate to the posterior over $g_\psi$ under these frameworks? If it differs from existing characterisations, ie [1]-[4], what theoretical, algorithmic or empirical advantages does it offer over a full Bayesian approach for characterising uncertainty in value functions? 

Can the authors approach be used to derived Bayes-optimal policies? If not, why does their uncertainty quantification prevent this? 

Can the authors extend their empirical evaluation to include other methods that quantify uncertainty in their value functions?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
This paper introduces a Latent Trajectory Framework (LTF) to improve uncertainty quantification in deep actor-critic reinforcement learning, addressing the challenge of value function uncertainty in stochastic environments. Using an adaptive Stochastic Gradient Markov Chain Monte Carlo (SGMCMC) algorithm, the method enables trajectory-independent training, backed by theoretical convergence guarantees and empirical performance improvements. This approach enhances both the robustness and reliability of RL applications by integrating latent transition trajectories.

### Strengths
Theoretical Analysis: The paper provides a theoretical analysis of the Latent Trajectory Framework, attempting to establish convergence and benefits for uncertainty quantification in RL.

### Weaknesses
 **$.1**
- L47: Why is the actor considered "unknown"? We can access its weights during training, so we should be able to evaluate it on any state-action pair. Even if the actor were unknown, how does that affect uncertainty quantification? Specifically, is the concern that the actor's parameters are changing during training, thus introducing a non-stationarity that confounds uncertainty estimation of the critic? What type of uncertainty is being addressed: aleatoric or epistemic?

**$.2**
- L100: What is π(x∣θ)? It's unclear how this relates to the policy, which is a distribution over actions, not states. Is this the stationary distribution of states induced by the policy? If so, this should be explicitly stated. 
- L103: What is π(ψ∣θ)? It is not clear what this conditional distribution represents. Is it a distribution over the critic's parameters given the actor's parameters? This needs further clarification.
- L105: What does "pseudo-population size" mean? Is N not equal to the batch size n? This term is not standard and requires a precise definition. How does this pseudo-population size relate to the actual number of samples used in the SGMCMC algorithm?
- L107: Similar to above, this line is unclear. It is not clear how the pseudo-population size prevents the degeneration of the conditional distribution. 
- Eq(3): Could you provide the intuition behind this learning objective? What is the motivation for integrating out the critic network parameter ψ? How does this relate to the overall goal of uncertainty quantification?

**$.3**
- How does this approach differ from the SGMCMC method discussed in Shih & Liang (2024)? The paper should clearly articulate the novel contributions beyond existing SGMCMC methods, especially in the context of actor-critic methods.

**$.4**
- $4.1: The writing lacks organization. For instance, metrics are introduced at L323, but the computation details are only explained two paragraphs later. Why is coverage rate the chosen metric for uncertainty quantification? What are the limitations of using coverage rate as the sole metric?
- $4.2: Since actor-critic methods are typically used for continuous action spaces, why not use Mujoco benchmarks for Fig. 7? Additionally, can LT be extended to SAC or other recent methods? What are the challenges in extending this approach to more complex RL algorithms?

### Questions
none

### Soundness
1

### Presentation
1

### Contribution
2
