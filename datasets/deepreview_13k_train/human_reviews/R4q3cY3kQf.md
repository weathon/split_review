# MaxInfoRL: Boosting exploration in reinforcement learning through information gain maximization

- Decision: Accept
- Scores: 5, 8, 6, 8

## Abstract
Reinforcement learning (RL) algorithms aim to balance exploiting the current best strategy with exploring new options that could lead to higher rewards. Most common RL algorithms use undirected exploration, i.e., select random sequences of actions.
Exploration can also be directed using intrinsic rewards, such as curiosity or model epistemic uncertainty. However, effectively balancing task and intrinsic rewards is challenging and often task-dependent. In this work, we introduce a framework, MaxInfoRL, for balancing intrinsic and extrinsic exploration. MaxInfoRL steers exploration towards informative transitions, by maximizing intrinsic rewards such as the information gain about the underlying task. 
When combined with Boltzmann exploration, this approach naturally trades off maximization of the value function with that of the entropy over states, rewards, and actions. We show that our approach achieves sublinear regret in the simplified setting of multi-armed bandits. We then apply this general formulation to a variety of off-policy model-free RL methods for continuous state-action spaces, yielding novel algorithms that achieve superior performance across hard exploration problems and complex scenarios such as visual control tasks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper addresses the problem of exploration in reinforcement learning (RL). Whereas both randomization of actions (like ϵ-greedy and Boltzmann exploration) and information gain maximization have previously been proposed as methods for exploration in RL, the paper suggest combining both. Furthermore, it adapts a way of automatically balancing the amount of exploration that is usual in random exploration methods to information gain. The method can be combined with a wide range of off-policy RL algorithms such as SAC. The paper provides strong empirical results on several benchmarks including vision-based humanoid locomotion.

### Strengths
- the presentation of the paper is reasonably clear and easy to read
- the paper addresses a broadly important problem
- the idea is simple and sensible
- the empirical performance as presented appears strong
- the authors provide code for their method

### Weaknesses
 - originality: the paper pretty much just combines the ingredients from two approaches already present in the literature: info-gain and Boltzmann exploration as present in SAC
- the weaknesses and limitations of the proposed method are not addressed in the paper
- while the paper provides a theoretical analysis in the bandit setting, the link to the full RL setting is not clearly established
- the computational overhead of maintaining and training the ensemble models is not thoroughly discussed or quantified, which seems crucial - some of the baseline methods are explicitly geared toward speed and scalability, so the paper should address this point

- page 4: the use of upper bound on information gain seems inappropriate -- you're trying to *maximize* information gain, instead shifting towards to maximizing an upper bound on information gain is just methodologically wrong. If you're crudely approximating the information gain of any distribution by the information gain of the independent multivariate normal with the same variances, you should say that you are doing that. 
- p. 5, eq. (7) seems to introduce an arbitrary one-to-one trade off between information (in nats) and the reward, that can have arbitrary scale

### Questions
Questions:
- I would appreciate more insight into when / how the method works, and in particular why keeping the naive exploration element is still important. If you claim that info gain is more directed/principled, why not use just that? Could you provide ablations illustrating the importance of (random-action) Boltzmann exploration?
- page 4: the \epsilon-greedy method seems ill-founded: the exploratory action is taken according to the *optimal* Q-function for the intrinsic reward. However, the optimal policy is not subsequently followed (which is an assumption behind an optimal Q-function). In particular, this can result in taking an exploratory action motivated by information a purely exploratory policy could gain in several steps, while gaining no information in the first few. However, since the actual policy is likely to immediately revert to exploit behaviour, the information is never gained. In light of this, does your epsilon-greedy policy make sense?
- on p. 6, you state that the constraint "(iii) it is tight" - what does that mean?
- just to clarify, are you also planning to make the code public (e.g. on Github) upon publication?

Minor comments and suggestions:
- "c.f. is repeatedly used inappropriately as "see" - it usually means "compare to"
- I think eq. 8 would benefit from more explanation/intermediate steps
- the autotuning at the bottom of page 5 does not describe autotuning per se - as listed in this optimization, alpha would go to 0 or infinity. It becomes "autotuning" only once the optimization is done gradually, e.g. using SGD. I think it would be useful to mention that explicitly.
- p. 6 below eq. (10) - the second sentence implies that we can attain arbitrary policy entropy. This is generally not true.
- eq. (12) - since you do that for the Bellman operator, I'd suggest also making the dependence of V on the policy explicit

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper studies how to balance intrinsic and extrinsic exploration. The author gives a novel framework called MAXINFOR by combining the use of intrinsic rewards and  Boltzmann exploration, provides theoretical results within a simplified setting of stochastic multi-armed bandits, and shows that MAXINFORL outperforms existing algorithms on standard deep RL benchmarks.

### Strengths
1. This paper provides a novel framework for RL exploration. The idea of using intrinsic rewards and  Boltzmann exploration to balance intrinsic and extrinsic exploration is very insightful.

2. I appreciate that the author provides both theoretical and experimental results, effectively demonstrating that the proposed algorithm may actually outperform existing methods.

3. This paper is well-organized and easy to follow.

### Weaknesses
1. It is good to provide study problems form both theoretical and experimental perspectives, however, I think the theoretical result which only gives a convergence result seems to be weak. So is it possible to prove a regret bound for your algorithm under certain conditions?

2. I think it is good to provide more comparisons with existing algorithms.

3. I am also curious whether the method in this paper applies to tabular RL. I think it is easier to get more quantitative theoretical results (like a regret bound) within a tabular setting. Reader can more intuitively see the superiority of your method from a theoretical perspective.

### Questions
See Weakness for questions.

### Soundness
3

### Presentation
4

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
The paper tackles the issue of poor exploration techniques based on dithering (like $\epsilon$-greedy and Boltzmann exploration) that are often used in continuous control algorithms such as SAC and REDQ by adapting them to include an intrinsic reward bonus based on the information gain from observing a particular transition.

### Strengths
The empirical evaluation is extensive in terms of the domains evaluated on. 

The theoretical result in Theorem 3.1 demonstrating convergence of their method is important and I'm pleased the authors included it.

I think the paper is generally well written and easy to follow.

### Weaknesses
 There is significant related work missing from the paper as there is no discussion of the rich literature on Bayesian RL (in particular, methods that achieve deep exploration [2]), which have been tackling the same problem highlighted by the authors since at least 2018. 

 I also have concerns with both the empirical and theoretical justification of the algorithm

Theoretical justification of algorithm:

Issue I: Regret bound is not particularly strong

The authors derive a regret bound in the bandit setting of the order $\mathcal{O}(T^{1-\alpha}\log(T)^k + T^{2\alpha})$ for $\alpha\in(0.25,0.5)$ and some $k$ depending on the GP kernel. Whilst this achieves sub-linear regret in the Bandit setting, this is not a high bar to clear and there are many approaches that achieve much better regret bounds like UCB and Thompson sampling, which achieves Lai and Robbins lower bound of $\log(T)$.

Issue II: Analysis in the bandit setting

Carrying out regret analysis in the bandit setting is not sufficient to make claims about regret in the full MDP setting. For example, as discussed already, it is known that Thompson sampling achieves Lai and Robbins lower bound of $\log(T)$ in the bandit setting, but posterior sampling does not achieve optimal regret in the full MDP setting [1]. 

For this reason, I'm not convinced there is a strong theoretical case for the algorithm 

Empirical Justification:

The authors focus on comparing against algorithms that don't have particularly strong exploration properties and this feels a bit like a straw man to me. Given the focus on exploration, I'd expect an empirical evaluation that compares to, for example, [2][3][4][5] to name a few, which all have better theoretical exploration properties and are known to perform well on challenging exploration continuous control tasks. As an example, an empirical evaluation similar to [6] which compares against state of the art exploration methods would be the evaluation I'd expect from a paper on exploration in model-free continuous control. 

For this reason, I don't think there is a strong empirical case for the algorithm.

### Questions
Can the authors prove a better regret bound for their approach that rivals approaches like posterior sampling? 
Is there a reason to neglect the algorithms highlighted in [6] in favour of their approach?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The paper, titled "MAXINFORL: Boosting Exploration in Reinforcement Learning through Information Gain Maximization," introduces a new approach to exploration in reinforcement learning by focusing on maximizing information gain. The authors propose the MAXINFORL framework, which augments standard exploration techniques, like Boltzmann and ε-greedy, with intrinsic rewards based on information gain to direct exploration toward more informative transitions. 

Key contributions include a method that integrates intrinsic and extrinsic exploration objectives seamlessly, sublinear regret performance in multi-armed bandit settings, and the use of ensemble dynamics models to estimate information gain. The authors validate MAXINFORL across standard benchmarks in state-based and visual control tasks, showing significant performance improvements over baseline algorithms like SAC and DrQ. The approach demonstrates particularly strong results in complex exploration scenarios, such as those with sparse rewards and high-dimensional visual control tasks, indicating MAXINFORL’s potential for enhancing sample efficiency and performance in hard-to-solve RL tasks.

### Strengths
1) **Significance of the Problem**: The paper addresses an essential challenge in reinforcement learning — achieving efficient and directed exploration in environments where rewards are sparse or non-informative. By focusing on maximizing information gain, the proposed method has potential implications for enhancing the performance of RL agents in complex and high-dimensional tasks, which makes the work particularly impactful.

2) **Clear and Well-Organized Structure**: The paper is well-structured, providing a logical progression from the problem introduction through the methodology and experimental validation. The explanations of both theoretical insights and practical implementation are clear, making it easy for readers to understand how the proposed MAXINFORL framework improves upon existing exploration methods.

3) **Robust Experimental Results**: The experimental results across various benchmarks demonstrate that MAXINFORL consistently outperforms baseline methods in terms of sample efficiency and exploration effectiveness. The use of challenging tasks, including both state-based and visual control problems, further strengthens the validity and robustness of the presented results.

4) **Effective and Intuitive Methodology**: The MAXINFORL framework combines intrinsic rewards, specifically information gain, with established exploration strategies like Boltzmann exploration in a theoretically sound and computationally feasible way. The use of ensemble dynamics to estimate information gain and auto-tuning mechanisms to balance exploration objectives adds to the approach's practicality, making it a sensible and valuable contribution to RL research.

### Weaknesses
1) **Clarity on the Importance of Information Gain**: The core insight of using information gain as an intrinsic reward requires further clarification. While the paper emphasizes its role in enhancing exploration, a more illustrative example could demonstrate its unique contribution compared to other intrinsic rewards. Specifically, the paper could benefit from a more detailed explanation of how information gain differs from, for example, prediction error or novelty-based rewards in the context of exploration. It is not immediately clear why maximizing information gain would lead to more effective exploration than these other methods, and a concrete example, perhaps in a simple grid-world environment, would help to illustrate the specific advantages of the proposed approach. This would help readers appreciate the specific novelty and advantage of information gain within this framework.

2) **Limited Novelty in the Trade-off Mechanism**: The method for balancing intrinsic and extrinsic rewards, while effective, lacks substantial novelty. The approach builds on existing auto-tuning and temperature parameter techniques without introducing significant new strategies for trade-off optimization. While the use of these techniques is not a weakness in itself, the paper could be strengthened by exploring alternative or novel mechanisms for managing this balance, particularly in complex environments. For example, the paper could investigate adaptive weighting schemes that dynamically adjust the balance between intrinsic and extrinsic rewards based on the learning progress or the environment's characteristics. An exploration of such alternative or novel mechanisms for managing this balance, particularly in complex environments, would strengthen the paper’s contribution and originality.

### Questions
please see weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3
