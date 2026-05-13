# EvIL: Evolution Strategies for Generalisable Imitation Learning

- Decision: Reject
- Scores: 3, 3, 6, 3

## Abstract
Often times in imitation learning (IL), the environment we collect expert demonstrations in and the environment we want to deploy our learned policy in aren't exactly the same (e.g. demonstrations collected in simulation but deployment in the real world). Compared to policy-centric approaches to IL like behavioural cloning, reward-centric approaches like \textit{inverse reinforcement learning} (IRL) often better replicate expert behaviour in new environments. This transfer is usually performed by optimising the recovered reward under the dynamics of the target environment. However, \textit{(a)} we find that modern deep IL algorithms frequently recover rewards which induce policies far weaker than the expert, \textit{even in the same environment the demonstrations were collected in}. Furthermore, \textit{(b)} these rewards are often quite poorly shaped, necessitating extensive environment interaction to optimise effectively. We provide simple and scalable fixes to both of these concerns. For \textit{(a)}, we find that \textit{reward model ensembles} combined with a slightly different training objective significantly improves re-training and transfer performance. For \textit{(b)}, we propose a novel \textit{evolution-strategies} based method (\acro{}) to optimise for a reward-shaping term that speeds up re-training in the target environment, closing a gap left open by the classical theory of IRL. On a suite of continuous control tasks, we are able to re-train policies in target (and source) environments more interaction-efficiently than prior work.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces Evolutionary Imitation Learning (EvIL), a versatile strategy for imitation learning (IL) that can forecast the behavior of agents in environments across different dynamics.
EvIL employs Evolution Strategies to concurrently meta-optimize the parameters (such as reward functions and dynamics) that are input into a subsequent reinforcement learning process. The authors claim that they are able to inherit some of the benefits of IRL and 
In addition, since they are using a population-based method, the reward or the training process does not need to be differentiable. They validate the robustness and generalization ability through some simple environments.  The results show that they can perform better than BC and classic IRL approaches.

### Strengths
- The ability to predict an expert’s behavior in an environment different from the one where the trajectory data was collected is an important topic
- Able to handle undifferentiable rewards.

### Weaknesses
 - Since the paper only uses experiments to demonstrate the method's effectiveness, I believe that the experiments are too few and too simple. Usually, when someone talks about the generalization of RL regarding the transition function, I will think of more challenging and practical modifications like different gravity, mass, and friction. 
- The method is very slow since it involves multiple rounds of training.
- The authors do not clarify why we should use their design since the method is not the most straightforward way to solve the problem of previous work.  An easy way to focus on only one scenario first and talk about why we need the method in that scenario (e.g., online).

### Questions
- It seems like in expert demonstrations you only use one kind of transition function is that correct?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a way of applying evolutionary optimization to inverse reinforcement learning. The performance of the method is evaluated in some toy problems and compared with AIRL.

### Strengths
It is certain that evolution can provide a solutions to any problem.
Originality of the proposal includes:
• estimating the gradients of policy and transition model parameters with Gaussian mutation and perform gradient decent, rather than usual selection.
• tuning of inner-loop steps to avoid disappearance of the above gradient
• L1 distillation of the estimated reward functions

### Weaknesses
A crucial issue in evolutionary approach is how practically and competitively a real-world problem can be solved.
Figure 1 presents the comparison with AIRL, but the implementation of AIRL is not sufficiently documented. The x axis is the number of outer loops, but how many interactions with the environment happened in each outer loop for EvIL and AIRL?
The basic parameters like the population size N should be reported in the main text.

4.1, 2.: The link between the non-differentiable objectives and potential-based shaping is not clear to me.
Page 2, para. 3: environment dynamics are trained: did you mean dynamics models are trained? You can train your agent but not the environment.
What were the target reward functions of each benchmark? It is not clear even in the supplementary materials. For each goal point, how sparsely was the reward functions set?

### Questions
How does the gradient approach compare with standard selection approach in evolutionary optimization? This can be benchmarked in addition to the ablation study within the EvIL framework.
4.1, 2.: The link between the non-differentiable objectives and potential-based shaping is not clear to me.
Page 2, para. 3: environment dynamics are trained: did you mean dynamics models are trained? You can train your agent but not the environment.
What were the target reward functions of each benchmark? It is not clear even in the supplementary materials. For each goal point, how sparsely was the reward functions set?

### Soundness
2 fair

### Presentation
1 poor

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents an evaluation strategy approach for immitation learning. This meta-learning approach optimizes the parameters of a reward function and environment dynamics in the outer loop, and then uses them in the inner loop to reinforcement learn. The authors show that their approach is able to learn the reward function induced by an expert bot behaviour, also when the dynamics of the environment are not fully known. The method is evaluated on gridworld, reacher, and pointmass environment and compared to a standard behavioural cloning approach and adverserial inverse RL.

### Strengths
- The paper presents an interesting application of ES, taking advantage of the fact that neither the reward nor the training - procedure need
to differentiable. 
- The approach addresses some key limitations of most IL approaches
- Baseline comparisons and ablation tests are sensible
- Promising results in three benchmarks

### Weaknesses
 - Some acronomys are not defined, e.g. AIRL (adverserial inverse reinforcement learning). What are its training setup?
- Approach should be evaluated on more environments and potentially complexer ones. Is the approach generally better to BC or does it
depend on the type of environment?
- It would be useful to test how transferable the learned reward functions are to similar domains
- Hyperparaemters for some of the experiment steps don’t seem to be mentioned (e.g. learning rates, etc.?)
- The environments are not described in the paper. Details should at least be added to the appendix.

Minor comments:
Typo page 3: "the the expert demonstration"

### Questions
- Why were these particular evaluation test environments chosen? 
- What are the parameters for the BC training?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper presents a method of model-based imitation learning based on learning and evolution. Specifically, the proposed method named EvIL is formulated as a bilevel optimization problem. The outer loop optimizes the reward and transition functions that are used to train a policy by reinforcement learning in the inner loop. The objective function of the outer loop is behavioral cloning loss, and CMA-ES is adopted to optimize the reward and transition functions. The evolved reward function is distilled to simplify the network architecture of the reward function, which improves the performance in the test environment. EvIL is evaluated on Gridworld and Reacher and outperforms BC and AIRL.

### Strengths
The proposed method is general and applicable to various policy optimization problems. The finding that using distillation is better than simply adding $\ell_1$ regularization to a loss function seems interesting. The experimental results are promising. In particular, transferability to unseen environments is interesting.

### Weaknesses
The literature review is insufficient. For example, the structure of EvIL is similar to the framework of learning and evolution. For example, Elfwing et al. (2018) optimize hyperparameters of RL by a simple evolutionary algorithm in the outer loop while the policy is trained by RL. In Nielum et al. (2010), the reward function is optimized by genetic programming. Please discuss the relation between EvIL and these classical studies. In addition, a more detailed survey on meta-learning is needed. For example, Evolved Policy Gradient (Houthooft et al., 2018) optimizes a differentiable loss function, where a similar evolutionary strategy is used in the outer loop.
S. Niekum et al. (2010). Genetic Programming for Reward Function Search. IEEE Transactions of Autonomous Mental Development. 2(2): 83-90. 
S. Elfwing et al. (2018). Online Meta-Learning by Parallel Algorithm Competition. In Proc. of GECCO.  
R. Houthooft et al. (2018). Evolved Policy Gradients. NeurIPS. 

My second concern is the scalability of the algorithm. Since a naive evolutionary strategy is adopted to optimize the reward and transition functions, applying the proposed method to problems with a high-dimensional state space is problematic. 

Finally, it would be better to re-organize Section 5 because Figure 3 is explained after Figure 2.

### Questions
1. Figure 1 seems interesting, but I do not fully understand the experimental conditions. The first paragraph of Section 4.1 mentions that the reward function optimized in the training environment is used to train policies in the test environment. However, Figure 1 shows that the reward and transition functions are optimized in the test environment. Please clarify the motivation for the experiments. 
2. Figure 1 shows that the performance of EvIL is worse than that of AIRL in the training environment. However, AIRL failed to improve its performance in the test environment. Does it imply that the initial reward is tuned for the training environment? 
3. Discussions about Figure 2 are needed. For example, in my view, there are no significant differences among EvIL, EvIL with supervised loss, and EvIL with supervised model. In addition, the performance in the online setting is much better than those of other methods. It implies that EvIL failed to find a good transition function even in the Poitmass environment. Would you discuss the quality of the optimized transition function in detail? 
4. Figure 3 is interesting, but I am unsure how the features such as the obstacle position are retrieved from the reward function. As far as I understand, the reward function is represented by a neural network, which is a mapping from a state to a scalar value. Would you clarify the method to retrieve the reward features?

### Soundness
1 poor

### Presentation
2 fair

### Contribution
1 poor
