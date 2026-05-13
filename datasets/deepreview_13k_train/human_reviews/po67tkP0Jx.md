# Mitigating Goal Misgeneralization via Minimax Regret

- Decision: Reject
- Scores: 6, 3, 5, 3

## Abstract
Robustness research in reinforcement learning often focuses on ensuring that the policy consistently exhibits capable, goal-driven behavior. However, not every capable behavior is the intended behavior. *Goal misgeneralization* can occur when the policy generalizes capably with respect to a 'proxy goal' whose optimal behavior correlates with the intended goal on the training distribution, but not out of distribution. Though the intended goal would be ambiguous if they were perfectly correlated in training, we show progress can be made if the goals are only *nearly ambiguous*, with the training distribution containing a small proportion of *disambiguating* levels. We observe that the training signal from disambiguating levels could be amplified by regret-based prioritization. We formally show that approximately optimal policies on maximal-regret levels avoid the harmful effects of goal misgeneralization, which may exist without this prioritization. Empirically, we find that current regret-based Unsupervised Environment Design (UED) methods can mitigate the effects of goal misgeneralization, though do not always entirely eliminate it. Our theoretical and empirical results show that as UED methods improve they could further mitigate goal misgeneralization in practice.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper proposes a method to mitigate goal misgeneralization in RL, which occurs when the policy generalizes capably with respect to a proxy goal but not out of distribution. The authors argue that the training signal from disambiguating levels could be amplified by regret-based prioritization. They show that approximately optimal policies on maximal-regret levels avoid the harmful effects of goal misgeneralization. Empirically, they find that current regret-based Unsupervised Environment Design (UED) methods can mitigate the effects of goal misgeneralization.

### Strengths
* The idea of focusing on regret-based prioritization to mitigate goal misgeneralization is novel and promising.
* A clear and well-structured theoretical analysis to support the proposed method.
* The empirical evaluation can demonstrate the effectiveness of the proposed method.

### Weaknesses
 * How does the proposed method handle scenarios where the behavior policy's state distribution is highly sub-optimal or incomplete, potentially leading to poor coverage of desirable states? Specifically, if the behavior policy is far from optimal in the disambiguating levels, the regret estimates will be unreliable. For instance, if the agent is trained to navigate a maze and the proxy reward encourages it to go to a corner, but the true reward is only found in the center, the policy might never explore the center, leading to an underestimation of regret in levels where the true reward is present. This could cause the method to fail to prioritize the correct levels for learning.
* The structure of this paper should be more clear. The logical flow between the theoretical analysis, the proposed method, and the empirical evaluation is not always easy to follow. The connections between different sections could be strengthened to improve the overall clarity.
* While the authors' experiments give algorithmic insights, experiments in complex scenarios can persuade readers more easily. The current experiments are limited to relatively simple environments, which may not fully capture the challenges of real-world applications. Testing the method in more complex environments with higher dimensional state and action spaces would provide stronger evidence of its effectiveness.

### Questions
Please see the Weaknesses.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The papar studies the goal misgeneralization issue in underspecified Markov Decision Processes, where the dynamics is controlled by a set of level parameters.  The paper compares two kinds of solutions to this problem: one is domain randomization, which tries to find a policy that maximize the reward over a distribution of levels, and the other one uses minimax expected regret, which find the policy that maximizes the reward under the worst case level parameter. The paper argues that minimax expected regret mitigates the goal misgeneralization issue, through both theoretical argument and experiments.

### Strengths
1. The paper considers both theory and experiments.
2. The experiments consider several variants of the baselines.

### Weaknesses
1. I am quite confused about the setting that the paper is actually considering: in the preliminary the paper introduces reward-free UMDP, which is reward function is not unknown to the learner or the learner does not observe reward signal at all. Then in the introduction of UED and domain randomization, there is a ground truth reward R that is optimzed by the learner - so seems like we are considering reward-based MDPs again. Both then in section 3 & 4, for example definition 3.1, it says reward-free UMDP again, and it is unclear to me that if the learner only observe R, or the learner does not observe any reward signal, or some other construction. Finally in the experiment section it seems to me that we go back to reward-based setting since the learners receive reward signal again.

2. If the goal for the theory section is to prove that MMER is better than DR in terms of distribution shift (goal misgeneralization), I am not sure if the theoretical result in the paper provides new results. Regardless of whether the paper considers reward-free or reward based UMDP, we can see that reward-free UMDP generalize / is harder than reward-based UMDP. Now if we consider reward based UMDP, and consider horizon=1, and the level parameter only controls the inital state distribution, then we can think of the control parameter is just the (distribution of) covariate in supervised learner. And the difference between optimizing for average case vs. worse case is well-known in distribution/covariate shift literature so it seems to me that the conclusions in section 4 is already implied by previous covariate shift literature, if not already existed in RL?

### Questions
In definition 4.1, are the states part of the trajectory?

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper addresses the important problem of goal misgeneralization in reinforcement learning (RL) and provides formalisms using level ambiguity. The authors propose that level sampling in Unsupervised Environment Design (UED) based on minimax expected regret (MMER) can mitigate the effects of goal misgeneralization by amplifying the training signal from disambiguating levels. The paper theoretically proves that MMER-based methods are more robust to goal misgeneralization than standard domain randomization (DR) methods using the resource-allocation setting. Empirical results in a single grid-world domain validate these claims, and show that regret-based Unsupervised Environment Design (UED) methods significantly outperform DR in avoiding goal misgeneralization.

### Strengths
1. The paper tackles the important problem of goal misgeneralization, which is highly relevant in reinforcement learning, particularly in safety-critical applications. The application of minimax regret to mitigate goal misgeneralization is a novel approach.

2. The paper formalizes the problem of goal misgeneralization using level ambiguity and introduces a framework based on minimax regret. Based on my knowledge on previous works regarding goal misgeneralization in deep RL, the distinction between disambiguating and ambiguating levels is a novel contribution. It is also very intuitive for understanding the goal misgeneralization problem.

3. The paper has strong theoretical rigor and provides a extensive proofs that minimax expected regret policies mitigate goal misgeneralization.

### Weaknesses
 **1. There is a lack of experiments**

Gridworld environments is fine since previous works in deep RL studying "goal misgeneralization" have mainly experimented using those [1,2]. But I am wondering why there isn't more experiments in different domains such as "Keys and Chest" from [1] and especially in domains with denser rewards such as "Tree Gridworld" from [2]. Testing in only one domain makes it difficult to assess whether the observed improvements are due to the MMER strategy itself or are influenced by domain-specific factors, such as the reward structure (e.g., sparse vs. dense rewards). Broader testing across different domains is needed to establish the generality of the MMER approach. Furthermore, the current gridworld experiments are limited to relatively simple configurations. It would be beneficial to see results on more complex gridworlds, perhaps with varying sizes, obstacles, or more intricate reward structures to further validate the robustness of the proposed method.

**2. Results visualizations are very confusing and lack explanations**

The plots are really not intuitive and readers would stuggle to interpret them. In Figures 2C and 2G, the y-axis shows "prop of OOD training levels" and x-axis shows "mixture weight". Correct me if I'm wrong, but there isn't a line in the paper explaining what the mixture weight $\alpha$ is, i.e. whether it is portion of ambiguating or disambiguating levels. Same for prop of OOD training axis. What is the difference between the two axis? As of current, how to interpret both figures is unclear to me. The figures also lack clear explanations of what constitutes an 'ambiguating' versus a 'disambiguating' level, making it difficult to understand the experimental setup. The use of 'OOD' is also not well-defined in the context of the training levels, and the connection to the goal misgeneralization problem is not immediately obvious. 

In lines 412-413, it is stated that "DR is susceptible to goal misgeneralization until there is 3-10% of training levels that are disambiguating" but in line 420, "$\text{ACCEL}_\text{id}$ ... at a very low $\alpha$ = 0.03%". Is the percentage in the latter statement intended? Why does $\alpha$ have a max of 1 in the plots but then it is mentioned in percentages in the explanations. The inconsistent use of percentages and proportions in the text and figures makes it difficult to compare the results across different sections of the paper.

**3. Empirical evidence is not conclusive**

Based on the results, specifically Figure 2D and Figure 4G, it appears that MMER is not primary factor mitigating goal misgeneralization. The performance of most of the regret-based UED approaches closely tracks that of DR, only showing divergence at a mixture weight of around 1e-3 in "Cheese in the corner". This is with the exception of $\text{ACCEL}_\text{id}$. It appears that the mutation method for environment generation has more impact than the minimax regret level sampling, which diminishes the significance of MMER. Also, the use of only 3-4 seeds per experiment is below the typical standard in deep RL research, especially given the inherent variability in RL performance. The lack of statistical significance testing further weakens the claims made based on these limited experiments.

**4. Overcomplicated and confusing theoretical section**

A large part of the paper is devoted towards defining and proving using the "resource-allocation" setting which is arguably a restrictive setting of sequential decision making problems. This proof is also unnecessarily complicated for what it's trying to show. Wouldn't the key point be to bring across that MMER strategy prioritizes levels where the policy has high regret, which would likely be the disambiguating levels (since they are OOD)? It would be much better deferred to the appendix and having more of the paper spent on empirical results (e.g. more domains) and providing clearer interpretations of the effects of MMER. The current theoretical framework, while rigorous, does not provide a clear intuition for why MMER should be effective in mitigating goal misgeneralization beyond the basic idea of prioritizing high-regret levels. The connection between the resource allocation setting and the actual RL environments used in the experiments is also not clearly established.


**5. It is unclear whether only MMER strategy is viable for solving goal misgeneralization or just one of many.**

The MMER strategy is potentially just one of several approaches for mitigating goal misgeneralization. The significance of using MMER to address goal misgeneralization is not established as the paper lacks comparision against other alternatives for level sampling. For instance, it is possible that the maximin reward strategy could similarly target the goal misgeneralization problem. Additionally, novelty-based approaches, where more diverse levels are prioritized (which would potentially contain more disambiguating goals), might be equally effective. Furthermore, the challenge of goal misgeneralization may not solely stem from how levels are sampled, but also from the learning algorithm itself. Improvements in the "inner-loop" mechanisms, such as better exploration through intrinsic curiosity, might be far better at addressing the problem. While the paper demonstrates the impact of MMER, it does not fully establish why this method is superior to other possibly simpler or more intuitive strategies. If several alternative approaches could potentially mitigate goal misgeneralization, the necessity of using MMER in particular is not so important.

### Questions
**1. Why does corner size matter in "Cheese in the corner"?**

Could you explain the corner size $c$ and the plot with x-axis as $c$ is shown in the main body? How is $c$ related to the ambiguity of the level?

**2. Why is there a need for log scale for the vertical axis in figures 2D and 4G?**

Isn't both Gridworld experiments are already in the scale of reward being 0-1, where 1 represents mouse successfully getting the cheese in every run? 

**3. Why is there no robustness result for "Cheese on a dish" in the appendix?**

How does ACCEL and PLR scale with different feature numbers?

**4. Possible reason why max-latest regret estimator has the best result**

From my understanding of minimax-regret UED approaches as in PLR and ACCEL, positive GAE (generalized advantage estimation) has typically been better performing. However, you mentioned that the max-latest regret estimator which does not rely on the policy's value estimate, but rather keeps track of the running max achieved performance on a level, achieved the best result. It could potentially be due to the fact that ambiguating levels causes the policy to overestimate the value in disambiguating levels. Intuitively, within disambiguating levels (which form a low proportion of the training distribution), the agent always overestimate the value of states/trajectory leading to the common location of the cheese, but in reality gets zero reward. This lead to consistently negative GAE values, which are zeroed out under positive GAE, effectively hiding regret information. Therefore using the max attained reward which does not rely on value estimate allows the regret to be in the positive range. If that is true, the approach’s effectiveness may depend heavily on learning rate (LR) and entropy regularization in PPO rather than on the MMER approach alone. A low LR combined with higher entropy (encouraging exploration) would lead the agent to "accidentally" find the goal in disambiguating levels more often, thereby reinforcing positive regret signals under the max-regret estimate. This may suggest that MMER is not entirely reliable in isolation. It might be good to discuss and experiment regarding this in order to establish MMER's significance.

**5. Questions in the "Weaknesses" section**

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
4

### Summary
In this paper, the authors analyse the problem of goal misegeneralization, i.e., the problem that arises when our learning agent optimizes a different reward function (goal, named proxy reward) instead of the true one. While the true rewards induce similar optimal policies during training, good policies under the proxy reward may be arbitrarily bad under the true reward during testing. The authors analyse a sort of constrained problem, in which there are resources (with a budget) associated to reward functions. They show that good policies on environments with large regret can limit goal misgeneralization. They also find that, empirically, unsupervised environment design can mitigate the effects of goal misgeneralization.

### Strengths
- The considered problem of goal misgeneralization is interesting and important for the RL community

### Weaknesses
 - Basically the author consider a constrained RL problem, but do not mention constrained RL nowhere, not even in the related works.
- The paper is difficult to follow because there are some counter-intuitive parts, like the fact that the resources/budget constraints are associated to reward functions instead of state-actions. I think that this formulation is not a model that might be applied in many applications. Instead, I think that remodelling the problem using a cost function as a function of the state/action would be much more meaningful and a much more powerful model.

Moreover, there are many typos:
- 190: missing "is" 
- 191: two "the" 
- Definition 4.1: clarifying that $s_i,s_j$ belong to the trajectory 
- 240: "allocationof"  
- 087,088: the return of a trajectory should not depend on $\theta$
- 241,248: it is wrong notationally to write $\sum\limits_{s_t\in\tau}$, but you have to loop also over $a_t,s_{t+1}$ if you want to use them
- ...

### Questions
- why not modelling the problem with a state with two components, i.e., using one component for the resource?   Or, alternatively, why not modelling the problem using both a reward function and a cost function, with the latter for the budget/resource constraints?  
- definition 4.2: what is G? It has no reward associated with it.  
- I do not understand the meaning of allocating resources to rewards. If the resource is a function of the state (according to your definition 4.1), and since a reward is a function of the state too, why should the resource be allocated to rewards in different manners?

### Soundness
2

### Presentation
2

### Contribution
2
