# Submodular Reinforcement Learning

- Decision: Accept
- Scores: 6, 8, 6, 8

## Abstract
In reinforcement learning (\RL), rewards of states are typically considered additive, and following the Markov assumption, they are {\em independent} of states visited previously.  In many important applications, such as coverage control, experiment design and informative path planning, rewards naturally have diminishing returns, i.e., their value decreases in light of similar states visited previously. To tackle this, we propose {\em submodular RL} (\subrl), a paradigm which seeks to optimize more general, non-additive (and history-dependent) rewards modelled via submodular set functions which capture diminishing returns. Unfortunately, in general, even in tabular settings, we show that the resulting optimization problem is hard to approximate. On the other hand, motivated by the success of greedy algorithms in classical submodular optimization, we propose \subPO, a simple policy gradient-based algorithm for \subrl that handles non-additive rewards by greedily maximizing marginal gains. Indeed, under some assumptions on the underlying Markov Decision Process (\mdp), \subPO recovers optimal constant factor approximations of submodular bandits. Moreover, we derive a natural policy gradient approach for locally optimizing \subrl instances even in large state- and action- spaces. 
We showcase the versatility of our approach by applying \subPO to several applications such as biodiversity monitoring, Bayesian experiment design, informative path planning, and coverage maximization. Our results demonstrate sample efficiency, as well as scalability to high-dimensional state-action spaces.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies submodular reinforcement learning, i.e. reinforcement learning with submodular set reward function that captures diminishing returns. Specifically, this paper has made the following contributions:

- This paper motivates and develops the framework of submodular reinforcement learning.

- This paper derives a lower bound that establishes hardness of approximation up to log factors in general (Theorem 1, Section 3).

- This paper motivates and develops a general algorithm for the considered problem, referred to as Submodular Policy Optimization (SubPO, Algorithm 1). This is a policy optimization algorithm. Provable guarantees are established in some restricted settings (Section 5).

- Extensive and rigorous experiment results are demonstrated in Section 7.

### Strengths
- The considered problem is interesting and significant.

- Extensive and rigorous experiment results have been presented in Section 7.

- The paper is well-written in general, and easy to read.

### Weaknesses
- The idea behind the proposed algorithm, Submodulr Policy Optimization, is quite straightforward. It is just a relatively straightforward extension of the classical policy optimization algorithm.

- The analysis in Section 5 seems to be very restricted. Could the authors provide a similar analysis in more general settings?

### Questions
- Please try to address the weaknesses listed above.

- It is not clear to me why the authors chose to put the "Related Work" section between an analysis section and the experiment section. Probably the authors should put it after Introduction.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors propose a submodular reinforcement learning (subRL) setting. Different from the existing reinforcement learning settings, they do not assume the rewards are additive. This allows them to work with more general and history-dependent reward models and they characterize these reward models with submodularity. Moreover, they design a policy gradient-based algorithm, called subPO, for  subRL problems by drawing inspiration from the greedy algorithm for classical submodular problems.

### Strengths
Combining submodularity with reinforcement learning in a generalized way seems highly intuitive that I am surprised it has not been proposed before. This emphasizes the significance of the paper's contribution. The main idea of the paper is a simple yet powerful one. Additionally, the paper is well written and the ideas or conveyed clearly.

### Weaknesses
These are more minor suggestions for improvement rather than weaknesses:
- On the last paragraph of page 1, the adverbs firstly, secondly, thirdly can be just replaced with first, second, and third. Also, we after the firstly should be lowercase.
- I think there can be a broader discussion of using submodular functions in reinforcement learning setups in the related work section. I am aware that the introduction also mentions some examples of submodular rewards, but I believe it is interesting enough to have its own paragraph in the related work.

### Questions
- Are there other attempts of incorporating submodular functions to reinforcement learning problems?

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The submission considers a new framework of Submodular Reinforcement Learning (SubRL), where the total reward is given as a submodular function of given trajectories, rather than as an additive sum of rewards from individual time steps. From my understanding, the main applications of interest would have environments where repeated actions (at the same states) are not so much preferred -- this is explicitly embedded in the reward design itself in SubRL. Contributions are the following:

- While the optimal policy can still be Markovian, the authors first show that approximating the optimal value up to any constant factor is computationally hard in polynomial time (that is, planning is computationally hard). 

- Given an additional assumption that the reward function is DR-submodular, AND if the underlying MDP is nearly deterministic, then a constant factor approximation is possible.

- The authors present a policy-gradient type algorithm for SubRL, and demonstrate the effectiveness of the method on several interesting synthetic examples and deep-RL settings.

### Strengths
The submission introduces a novel and "mathematically" interesting framework that accounts for diminishing returns of repeated actions. 

- The view of submodular rewards is fresh. The hardness result is new and interesting. 

- The selected toy examples sound interesting and well-suited for the proposed framework.

### Weaknesses
- I do not see much contribution in positive results. Not only does the assumption sound strong from a practical perspective, but it seems quite contrived only for the sake of analysis. 

- Literature review: I agree with the motivation from diminishing returns, but a submodular reward design is not the only way to address that. For example, there is a blocking-bandit style framework that discourages repeated actions [1]. Maybe good to discuss why the submodular reward design is better. 

I also encourage authors to survey more existing works that explore similar ideas with submodular reward design. For example, can the authors explain the difference between [2] in terms of the problem setting?

[1] Basu et al., Blocking Bandits, NeurIPS 2019.

[2] Chen et al., Contextual Combinatorial Multi-armed Bandits with Volatile Arms and Submodular Reward, NeurIPS 2018. 

- Suggestion: It looks slightly unnatural to have Section 4 (practical algorithms) in between hardness results (Section 3) and positive results (Section 5). A more natural flow would have been having the positive theoretical results first and then presenting practical algorithms, or at least having them connected. 

- Overall, I feel that the framework is well-motivated for the "mathematical" purpose but less sound for the practical purpose or advancing the theory of RL.

### Questions
- I do not understand what it means by $\pi$ is parameterized by $\pi^h(a)$ in Theorem 3. Does this mean $\pi$ does not depend on the state? 

- Definition 2 - why is it named \epsilon-"Bandit" SMDP? 

- The submission focuses on the "planning" side. Any thoughts on the "learning" side? (a.k.a., exploration and sample complexity)

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes and studies submodular MDPs, where the total reward is characterized by a submodular function of the trajectory. The authors first show that computing a logarithmic approximation of the optimal policy is computational intractable. However, there exists a polocy optimization algorithm which gives a (1-c)-approximation where c is the curvature of the submodular function. Specifically, when specified to bandits, this result outperforms existing ones.

### Strengths
1. The model is well-motivated and clearly described. It is also easy to understand.
2. The results contain both upper and lower bounds, which are pretty complete.
3. Empirical evaluations are conducted for the proposed algorithm.

### Weaknesses
1. I'm not sure why this paper considers multiplicative approximations instead of regret/sample complexity, which are common in theory papers studying episodic MDPs.
2. The optimal dependency on curvature remains unspecified. Whether Proposition 3 is (near-)optimal?

### Questions
See weaknesses.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good
