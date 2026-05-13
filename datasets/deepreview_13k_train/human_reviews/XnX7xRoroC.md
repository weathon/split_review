# Distilling Reinforcement Learning into Single-Batch Datasets

- Decision: Reject
- Scores: 3, 8, 6, 8

## Abstract
Dataset distillation compresses a large dataset into a small synthetic dataset such that learning on the synthetic dataset approximates learning on the large dataset. Training on the distilled dataset can be performed in as little as one step of gradient descent. We demonstrate that distillation is generalizable to different tasks by distilling reinforcement learning environments into one-batch supervised learning datasets. This demonstrates not only distillation's ability to compress a reinforcement learning task but also its ability to transform one learning modality (reinforcement learning) into another (supervised learning). We present a novel extension of proximal policy optimization for meta-learning and use it in distillation of a multi-dimensional extension of the classic cart-pole problem, all MuJoCo environments, and several Atari games. We demonstrate distillation's ability to compress complex RL environments into one-step supervised learning, explore RL distillation's generalizability across learner architectures, and demonstrate distilling an environment into the smallest-possible synthetic dataset.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
This paper proposes a PPO-inspired dataset distillation technique.

### Strengths
Distillation seems like an interesting technique to reduce the data requirement of reinforcement learning.

### Weaknesses
I vote to reject primarily because the motivation for the algorithm and it's empirical evaluation is difficult to follow. I had a difficult time understanding the core takeaways of this paper.

1. Many of the contributions listed can be combined. For instance, contributions 1, 3, 5 and 6 are essentially saying the same thing: this works propose a new distillation technique and demonstrates its effectiveness empirically. 
2. Contribution 2 doesn't seem like a contribution; it's simply a task that was created to demonstrate the distillation method. I suggest omitting. 
3. "policy gradient methods such as PPO are more sample-efficient, utilizing the entire experience memory rather than randomly sampling from it as in standard DQN learning." This sentence is unclear to me; PPO does not use experience replay, as it is an on-policy algorithm. Also, off-policy algorithms are often more sample efficient than on-policy algorithms, so this statement seems misleading.
4. First paragraph section 3.1: This paragraph motivates building off of PPO, but I think that's all that needs to be said: you build off PPO because it is a reasonably sample efficient on-policy algorithm and is often the go-to algorithm for RL applications.
4. It's unclear how the experiments extend cartpole to N dimensions. A figure for N=2 would make be informative. 
4. Table 1 is difficult to parse. What exactly are the core takeaways from this table? Why is it informative to consider different model initializations? the experiments would be easier to understand if hypotheses were stated prior to showing results -- what do we expect to see if the method works, and why?
5. If the method works, it would be useful to understand how it distills the dataset -- which samples are ultimately distilled? Can we glean any insights from it?

### Questions
See weaknesses.

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper presents an approach that distills a reinforcement learning environment into a synthetic dataset while allowing agent trained under supervised setting with limited resource to reach a comparable performance vs the direct RL training.
It also presents an generalized algorithm to control the difficulty of distillation for estimating the feasibility of the full distillation.

### Strengths
Overall the paper is well-written. It provides an clearly-defined algorithm with training graph and pseudocode. 
It provides a simple algorithm based on PPO to distill RL environments into a parameterized distiller.
The performance results from an easy task to complex tasks are on par with direct RL training which demonstrates the generalizability and high distillation performance of the algorithm.

### Weaknesses
 * The experiments do not cover the continuous control problems which are also important part of RL environments. Demonstrating distillation on those tasks can greatly benefits to the community as many robot experiments are under continuous action space.
* If I understand correctly, the final baseline RL agent is determined by the time limit and convergence. But I would image using the same amount of training sample as in the distillation's outer loop for a more fair comparison.
* The cost saving part might be better displayed in a graph. Such as the overall time spend/number of parameter updates vs number of agent trained.
* For Q2, is the sentence updated? At line 365, it's still using the old description.
* For the distillation size of continuous settings, how is the 64 being decided? And although the equation 3 might not be applied to the continuous setting, it would still be good to see the graph of performance vs ***k*** given the paper want to demonstrate that distillation could reduce the cost of training.
* OPTIONAL For Q5: What's `one set of baseline features`? Would be good to have some analysis on the reward jump.
* Given the performance of distillation in many environments are not on par with direct RL training and the author claims the distillation is based on the optimal policy. It has to provide some discussion on why is the distillation results are bad. Since the Atari performance is due to convergence, you can provide the analysis on the continuous setting only.
* Nit: The previous comment said the $D_{\theta}$ will be replaced with $\{X_d, Y_d\}_{	heta}$, but the current revision's Fig 1 still uses the old format.

### Questions
* In fig 1: What's $D_{\theta}$, same in fig 2.
* Line 197: Why is the gradient destroyed? Isn't the bound non-zero?
* Can you also clarify the instance in sec 4.2, it's the sample generated from the distiller?
* In table 2, why would some experiments did not exceed the random performance while the full distillation did?
* In fig 3, what happens to the sudden increase in (e) subplot?

### Soundness
3

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
This paper introduces a novel distillation framework for distilling online RL environments to a synthetic dataset, which allows performant agents to be trained with one-step gradient descent. It extends PPO to leverage it to produce synthetic examples. Experiments are conducted on the cart pole environment and its n-dimensional extensions. Moreover, a few atari experiments are also performed to demonstrate its generalizability.

### Strengths
* Work is novel considering it is probably the first to introduce dataset distillation for online RL. However, there is a related work on dataset distillation for offline RL that is missing in related work and I believe should be discussed.(https://arxiv.org/abs/2407.20299)

* Results are promising in both Cartpole and atari experiments

* Framework does not introduce a significant overhead to the wall-time of the PPO.

### Weaknesses
 * One of the main issues of this paper is motivation. Dataset distillation is proposed so that a large dataset can be condensed into a synthetic smaller one however I dont think the same analogy is reasonable for RL. Firstly, when you train a supervised model with large datasets, you would get almost the same accuracy which means that this dataset would have a score equivalence given a model whereas this is not accurate for the RL environments because RL environments are not deterministic. So, RL agents' performance varies across different numbers of runs (Agarwal et al., 2021). All in all, the distilling of a single instance of an environment will only represent the data that has been generated by this specific environment, not the environment itself. I would be very surprised if the policy generated by synthetic examples will generalize to the other instances with different seeds. Lastly, the discussion of runtime and the training of 10-20k agents is problematic due to similar reasons. You should get a unique agent if all are initialized the same however RL agent would be different if the environment is not fixed. I believe the randomness of the agents is due to the randomness of initialization.



* Evaluation setup is vague, in particular in Atari. In table 2(a), you present $\textit{Average End-Episode Reward Achieved at Convergence}$. Is it the average total reward of the last 100 episodes, and also what does the st dev mean for this table, is it the average over multiple runs? I believe the evaluation setup should be clarified to interpret the given results.


* More runs and different environments(could be more atari games, or continuous control env like mujoco) are needed to demonstrate the effectiveness of the proposed method. No need for full distillation for new experiments, l4 is good enough.


* Paper is a bit hard to parse(especially section 3.1), so writing could be improved. I believe Figure 2 is redundant, does not provide any insights, and is not visually appealing. Algorithm 1 is sufficient to get the concept. Lastly, you could import booktabs package for a more used format by the ICLR papers.

### Questions
Q1) How does the policy induced by the synthetic examples preserve the trust region since the policy is not updated by the PPO loss?

Q2) Could you provide visualizations of the learned synthetic examples for 2D cartpole examples?

Q3) Do you have any insights regarding why lower ks are better even in higher dimensional cartpole settings?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper proposes a new method / framework generalizing dataset distillation approaches to the reinforcement learning setting. A network distills the "optimal juice" from an RL environment. During test time, this distilled network can generate a dataset (input-output pairs) such that a supervised learning model trained on this dataset will get optimal rewards. Intuitively, I can think of the distilled network as trying to memorize the state-action stationary distribution of the optimal policy of an environment.

### Strengths
1) I think this paper is tackling a novel problem in a novel way. Its "freshness" is definitely a strength.
2) While the results obtained right now are not ground breaking, it does open up avenues for future work.

### Weaknesses
1) Missing baselines -- As far as I can tell, there are no baselines used in the paper. One fairly obvious (but could be strong) baselines is to train a PPO agent till convergence in the environment and use a diffusion model to learn the state-action distribution of the expert policy. At meta-train time, a newly generated agent can just use the state-actions generated by this model as a training dataset. 

2) Motivation -- The motivation behind why this line of work is important is not clear to me after reading the introduction. Let me elaborate -
    a) Hyper-parameter / architecture tuning - Do you believe that the hyper-parameters tuned using the distilled network will be robust when training on a new environment without distillation. It do not know, nor is there any evidence provided in the paper, that hyper-parameters / architectures that work well using distilled network will work well when training in a new RL environment from scratch.

3) Data anonymity -- I think readers might appreciate of when this is a compelling reason in the RL setting.

### Questions
See Weaknesses section for points / questions to address.

### Soundness
4

### Presentation
4

### Contribution
3
