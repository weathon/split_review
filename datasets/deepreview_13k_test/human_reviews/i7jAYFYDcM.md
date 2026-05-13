# Bootstrapped Model Predictive Control

- Decision: Accept
- Scores: 6, 8, 8, 6

## Abstract
Model Predictive Control (MPC) has been demonstrated to be effective in continuous control tasks. When a world model and a value function are available, planning a sequence of actions ahead of time leads to a better policy. Existing methods typically obtain the value function and the corresponding policy in a model-free manner. However, we find that such an approach struggles with complex tasks, resulting in poor policy learning and inaccurate value estimation. To address this problem, we leverage the strengths of MPC itself. In this work, we introduce Bootstrapped Model Predictive Control (BMPC), a novel algorithm that performs policy learning in a bootstrapped manner. BMPC learns a network policy by imitating an MPC expert, and in turn, uses this policy to guide the MPC process. Combined with model-based TD-learning, our policy learning yields better value estimation and further boosts the efficiency of MPC. We also introduce a lazy reanalyze mechanism, which enables computationally efficient imitation learning. Our method achieves superior performance over prior works on diverse continuous control tasks. In particular, on challenging high-dimensional locomotion tasks, BMPC significantly improves data efficiency while also enhancing asymptotic performance and training stability, with comparable training time and smaller network sizes. Code is available at https://github.com/bmpc-anonymous/bmpc.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes Bootstrapped Model Predictive Control (BMPC), a model-based RL method that combines MPC with a policy, where the policy gives MPC better prior distribution of action to sample over, while the MPC uses a refined plan to train this policy. The authors propose lazy reanalyze method to make imitation of MPC policy more efficient, by eliminating the frequency of replanning & immediate update. The authors study the performance of proposed BMPC on a variety of continuous control tasks, compared against SOTA MBRL methods as well as model-free methods.

### Strengths
The paper is clearly written and the method is well-motivated: the policy can make MPC search more efficient while MPC's high-quality results can help with policy learning. 

The result and analysis are solid and convincing. The authors benchmarked on a good number of environments & standard benchmarks.

The good ablations answer a lot of my questions, and I expect all readers to find them very informative.

### Weaknesses
The outstanding concern is the legitimacy of letting MPC & policy bootstrapping each other. For example, it's unclear what influence this has on exploration. Will the added policy hurt the exploration of MPC? Could you highlight how exploration is achieved in your model or is it just like in TD-MPC2?

The authors chose Dreamer v3 as the MBRL baseline in the main evaluations. Since Dreamer v3 is specifically designed for visual observation & multi-tasking, I wonder whether the authors tried tuned it for state-based evaluations.

### Questions
In terms of the trade-off between exploration & exploitation, do you have to carefully tune/have a curriculum on the sigma std for the MPC?

What's the effect of EMA in Eqn(7)? Is it mainly for stabilization? How grounded is this design choice?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper proposes Boostrapped Model Predictive Control (BMPC), a model-based RL method that improves upon TD-MPC. TD-MPC consists of two policies: a network policy trained with RL, and an MPC policy guided by the network policy and its value function. The authors found the network policy in TD-MPC to perform much worse than the MPC policy. This is attributed to the network policy being trained in a model-free manner, which is less sample-efficient than MPC. The poor network policy then seeps into the value function, which in turn impacts the performance of the MPC policy. To mitigate this issue, the authors propose to train the network policy by directly imitating the MPC policy, while still using the network policy and its value function to guide the MPC policy. This effectively "distills" the MPC policy into a neural network, avoiding the policy mismatch in TD-MPC. However, this kind of imitation introduces significant overhead into policy learning, as each training step requires replanning on all samples. To address this, the authors propose Lazy Reanalyze, which replans on a small set of transitions every few training steps. With Expert Imitation and Lazy Reanaylze, BMPC achieves better asymptotic performance in fewer number of environment steps compared to TD-MPC on high-dimension DM Control tasks, all without introducing significant overhead.

### Strengths
1. The paper is motivated by a thorough analysis of the TD-MPC algorithm, which crystalizes into a key insight: the performance of TD-MPC is impacted by a mismatch between the network policy and the MPC policy. The proposed algorithm then follows as an intuitive solution. The overall flow of the paper is excellent, making it a pleasant read.
2. The empirical results of BMPC demonstrate a significant performance gain over TD-MPC, especially in complex high-dimensional locomotion tasks. In most tasks, BMPC is more sample-efficient than TD-MPC. And in a few tasks, it also achieves higher asymptotic performance.
3. The ablation experiments supplement the main experiment well, providing insights into the effect of hyperparameters and key design decisions. This adds to the credibility of the method
4. Overall, I believe this paper proposes a simple method that brings a new perspective to model-based RL. Therefore, I recommend acceptance.

### Weaknesses
1. The expert imitation procedure introduces overhead into the training pipeline, as each training step requires replanning. Although this is sidestepped by Lazy Reanalyze, it remains a fundamental limitation of the method.
2. The experiments are run with a small number of seeds (3 seeds). 
3. The experiments succinctly prove the point that the authors try to make. That said, it would strengthen the paper to include experiments across more diverse domains (those in TD-MPC 2).

### Questions
1. Are there other reasons behind TD-MPC's bad value function? If it's just the sample inefficiency model-free policy optimization, then the network policy should eventually catch up to the MPC policy. But this is not the case as shown in Figure 2 -- the asymptotic performance of the network policy is worse.
2. What is the tradeoff of pure MPC policy distillation compared to model-free policy optimization? Are there domains or settings where BMPC performs worse than TD-MPC? If so, what are the reasons?
3. Can you describe the three variants in Figure 6 (a) in more detail? I would also suggest adding the details of the variants in the appendix.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
Current state-of-the-art in MBRL learn a policy and Q-function in a model-free manner, then couple it with online planning via MPC to improve the policy. However, the authors of this paper find that on complex tasks, there is a substantial gap between the policy and policy+MPC performance. They propose a number of modifications, including an expert iteration-like scheme, for improving the final policy. This involves alternating between improving the policy with MPC online and imitating the updated policy as an expert offline. They find that not only does this improve performance, but it also closes the gap between the network policy and combining it with MPC. With their algorithm, BMPC, the policy learned via expert iteration actually nearly matches the performance of coupling it with online re-planning. Therefore, it is a viable final policy which amortizes the online planning with MPC.

### Strengths
- Improving the performance of MBRL algorithms by combining model-based and model-free components is a timely and important problem.
- The paper is well organized and overall clearly written. It does a good job explaining the novelty and results and provides enough information to support its claims.
- The analysis of the performance gap between the model-free policy and bootstraped MPC policy in TD-MPC2 is particularly thorough and very informative, doing a good job to motivate the paper.
- The evaluations are very thorough, considering all 28 environments in the DMControl benchmark tasks and an adequate selection of baselines, such as SAC, DreamerV3, and TD-MPC2. There is also a nice outline of questions to be considered in the evaluation section. And the results do indicate that BMPC can outperform these baselines, suggesting it is a promising method for combining the advantages of model-free and model-based RL.
- The lazy reanalyze method proposed in the paper is a nice solution to recomputing expert actions while still making use of a replay buffer. It's also nice that this reanalyze interval is a free hyperparameter rather than coupled directly to the number of updates to the policy.

### Weaknesses
- Some details are missing from the exposition, such as how the MPC policy is computed each batch without having to re-run the planning algorithm. One possibility is that the mean and covariance of the Gaussian is stored in the replay buffer. However, the paper would benefit from making this more concrete.
- It would be worth mentioning other work which attempt to imitate an expert MPC controller [1-4]. Alternatively, there are also approaches which attempt to learn residual on MPC [5-6], which is another way of bootstrapping MPC. And there are approaches which attempt to improve MPC via learned sampling distributions [7, 8]. Although not expert iteration, they are definitely related approaches which are important to mention.

References:
[1] Pan et al., "Agile Autonomous Driving using End-to-End Deep Imitation Learning," RSS 2018.
[2] Pan et al., "Imitation learning for agile autonomous driving," IJRR 2020.
[3] Sacks et al., "Learning to optimize in model predictive control," ICRA 2022.
[4] Fishman et al., "Motion policy networks," CoRL 2023.
[5] Sacks et al., "Deep Model Predictive Optimization," ICRA 2024.
[6] Silver et al., "Residual Policy Learning," arXiv 2018.
[7] Power et al., "Variational Inference MPC using Normalizing Flows and Out-of-Distribution Projection," RSS 2022.
[8] Sacks et al., "Learning Sampling Distributions for Model Predictive Control,"  CoRL 2022.

### Questions
- How is the MPC policy computed for imitation learning without rerunning the planning algorithm every batch? Is the mean and covariance of the MPC policy stored in the replay buffer as well?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents BMPC, a plan-based MBRL algorithm that integrates expert imitation for policy learning, performs model-based TD-learning for value learning, and introduces lazy reanalyze to utilize re-planning results better.

### Strengths
The paper is well-written and easy to follow.

For high-dimensional locomotion tasks, the paper presents ablation experiments comparing MPC policy with network policy. The results indicate that learning a network policy through expert imitation significantly enhances the performance of MPC.

The approach is evaluated against several baseline agents on DeepMind Control Suite environments.

### Weaknesses
1. The paper relies on TD-MPC2 and introduces modifications such as expert imitation and lazy reanalysis. However, these improvements seem overly engineering-focused and do not provide significant insights into the research direction.

2. It is unclear how the expert policy π is initially established as the prior policy. Could you describe how expert policy π evolves during training?

3. In the experimental section, the authors use only 3 seeds as following TD-MPC2. However, I believe that this is not enough. Could you provide additional results with more seeds as DreamerV3 if possible?

4. The related work section provides a rather simplistic overview of MPC research. I recommend enhancing this section for greater comprehensiveness.

### Questions
1. The paper replaces the Q-network with a V-network. What are the specific implications of using either Q or V for the training of the algorithm?

2. In line 260, the paper states that "setting N too large would lead to excessive compounding errors," yet it seems that increasing N would be less biased for the V-value estimation. Could you clarify this contradiction?

3. In line 325, could you provide a detailed explanation of "environment step"?

### Soundness
3

### Presentation
3

### Contribution
2
