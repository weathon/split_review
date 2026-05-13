# Utilizing Explainable Reinforcement Learning to Improve Reinforcement Learning: A Theoretical and Systematic Framework

- Decision: Accept
- Scores: 6, 6, 8, 8

## Abstract
Reinforcement learning (RL) faces two challenges: (1) The RL agent lacks explainability. (2) The trained RL agent is, in many cases, non-optimal and even far from optimal. To address the first challenge, explainable reinforcement learning (XRL) is proposed to explain the decision-making of the RL agent. In this paper, we demonstrate that XRL can also be used to address the second challenge, i.e., improve RL performance. Our method has two parts. The first part provides a two-level explanation for why the RL agent is not optimal by identifying the mistakes made by the RL agent. Since this explanation includes the mistakes of the RL agent, it has the potential to help correct the mistakes and thus improve RL performance. The second part formulates a constrained bi-level optimization problem to learn how to best utilize the two-level explanation to improve RL performance. In specific, the upper level learns how to use the high-level explanation to shape the reward so that the corresponding policy can maximize the cumulative ground truth reward, and the lower level learns the corresponding policy by solving a constrained RL problem formulated using the low-level explanation. We propose a novel algorithm to solve this constrained bi-level optimization problem, and theoretically guarantee that the algorithm attains global optimality. We use MuJoCo experiments to show that our method outperforms state-of-the-art baselines.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors propose a new approach of using explanations for reinforcement learning developed in the XRL community to improve RL algorithms. The design a two part method – the first part generates the explanations (two levels – learning an implied reward function and identifying ‘misleading’ states) and the second part utilizes this explanation to improve an RL agent’s performance by formulating a constrained bi-level optimization problem. Specifically, these two levels involve learning a reward shaping function and then a policy to optimize for this shaped reward. In addition to providing theoretical guarantees, the authors empirically demonstrate their method on four MuJoCo environments.

### Strengths
1. The authors address an important problem in RL – which is using explainability to improve performance. Their framework “UTILITY” is a novel approach to using XRL to optimize the RL agent’s performance. 
2. The paper is well written. The authors provide a good background literature survey, explain the problem and their motivation well and also clearly describe their solution.
3. The authors provide a detailed theoretical analysis and proofs for their claims. While I am unable to verify these completely, I have not found any error. However, I think it will still be helpful if the authors provide a proof sketch or outline in the main paper itself.

### Weaknesses
1. Can the authors add a discussion on stochastic environments and the impact of the same on their approach? I think the current approach has only been demonstrated in deterministic environments. Specifically, can the authors discuss how their theoretical guarantees and empirical results might change in stochastic environments, and whether any modifications to their approach would be needed?
2. The current method seems to need a lot of environment interaction. Can the authors detail the additional interaction needed for their approach?
3. Can the authors add a discussion on the scalability of their proposed approach, in terms of state/action space size, or computational complexity as the problem size increases?
4. The impact of the error in explanation on approach and final policy has not been covered, i.e., errors in reward learning and Q value error and behavior policy learning error. Can the authors address these with a discussion in the paper? Specifically, can the authors provide a sensitivity analysis showing how errors in each component (reward learning, Q-value estimation, behavior policy learning) impact the final performance with some discussion on potential mitigation strategies for these errors?

### Questions
1. The key idea in this paper of learning an implied reward function of a learned RL agent and also identifying the state-action pairs that cause the agent to be non-optimal to be used in learning a new policy seems novel and interesting. However, wouldn’t this require re-learning? Wouldn’t generating the explanations require either access to the environment for generating additional data or knowledge of the environment parameters such as transition function, maximum attainable reward, goal state etc.? Can the authors add a discussion on this topic detailing what extra data and computation are needed by their method?
2. Can the authors also compare their approach with other RL algorithms from literature where the other algorithms have access to the same total quantity of data used by the authors’ approach? The current comparison in Fig 2, does have total environment interactions, can the authors confirm if these interactions also include the additional data mentioned in Point 1 above?
3. It is known from the literature on inverse RL that learning a reward function from data is a problem that can have multiple solutions. Can the authors describe how they address the non-uniqueness problem and how do they choose a single reward function?
4. Can the authors clarify if different plausible high-level explanations (learned reward functions) can lead to different low-level explanations (misleading states)? If so, how do the authors propose to select the best high-level explanation? What is the authors’ opinion on using feedback from the RL agent’s performance post using their approach as input to improve their explanation generation. i.e., can their approach benefit by making the process of explanation generation and policy improvement iterative? 
5. Can the authors confirm if misleading states are states where the agent does not act optimally as per its own Q-function? Is this definition valid even if the Q-function learned by the RL agent is not accurate, which is often the case in several practical RL problems?
6. The authors state in Line 222 that: “However, our case is different because we only need to learn one precise Q-function, which corresponds to the specific policy $\hat{\pi}_A$”. But won’t the authors need this Q-function to be accurate for also state-action pairs that are not visited or rarely visited under this policy? This is because in defining the $l(s,a)$ metric, the authors use a max over all $Q$ values of a given state $s$. How do the authors propose to learn these values accurately or adjust the definition of their proposed metric to ensure that this does not impact their approach?
7. Can the authors clarify if the shaping reward function requires access to the ground-truth reward function? If so, how do the authors propose to obtain this?
8. Can the authors specify the loss function used for learning the proposed shaping reward function used in equation (1), i.e., can the authors provide a discussion on the gradients proposed in Lemma 2 and its relation to this shaping reward function?
9. When the authors claim uniqueness of solution in Theorems 1 and 2, it would be helpful if they can clarify whether only $J$ value is unique or is $\pi$ also unique?
10. Minor: There is a typo in “RICE+constaint” which occurs twice in the paper (Lines 513 and 514).

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes an explainable reinforcement learning (XRL) based policy update algorithm. The algorithm utilizes notion of "misleading state-action pairs" in the agent's current behavior that lead the agent to perform poorly compared to the optimal policy. These misleading $(s, a)$ pairs are then to be avoided by the agent to be able to act optimally. The criterion for defining misleading $(s, a)$ is whether the advantage of the policy is negative. For these misleading experiences, a positive cost is assigned. Parallely, from the agent's demonstrations with application of inverse RL on top, a reward function $\hat{r}$ is recovered. This reward function is then used to explain agent's current actions, as the reward function explains why a particular action is taken in the demonstration by assigning higher values. The misleading $(s,a)$ constitute the low-level explanations and the IRL reward function $\hat{r}$ the high-level explanation. A bi-level algorithm is then set up, where the agent has to learn a policy such that its low-level cost is bounded, i.e., not many disadvantageous actions are taken while high-level **ground-truth returns** are maximized. The first level includes both the cost $c(s, a)$ and the reward shaping using ground truth reward $r$ and IRL reward $\hat{r}$.

The paper then goes into the details of optimization where a dual approximation of bilevel algorithm is proposed that substitutes reward function with dual variables. Further, theoretical guarantees are provided about the convergence of a practical approach that uses low-level $c$ and high-level $\hat{r}$ and outputs an optimal policy. 


As for the experiments, this paper uses sparser variants of the MuJoCo environments, and tries to answer how much effective improvement their algorithm UTILITY provides against other XRL techniques when combined with standard SAC algorithm. Paper provides ablations for different considerations in the modeling of the algorithm. By removing low-level and high-level explanations, paper shows why both are needed to get superior performance.

### Strengths
1. I find a close connection between the proposed algorithm and algorithms in generalized policy iteration class, because (1) avoiding disadvantageous behavior under current policy is analogous to improving the policy (imagine giving a leeway when taking a greedy action and instead use budget over choosing worse actions), (2) learning a Q-function to understand the policy's performance is analogous to policy evaluation. So, as long as these two steps are implemented properly, the proposed algorithm is bound to improve the policy, and eventually help reach the optimum in state values. Again, I might have skipped the specific details about the convergence constants, learning rates, etc., but the algorithm seems about right.
2. The idea of finding K misleading $(s, a)$ to inform the policy update is very neat. This in itself is valuable as many times a post-hoc policy analysis might be necessary for identification of its limitations. The paper does a great job at also integrating the misleading with policy's current beliefs and using ground truth rewards to rectify those beliefs.
3. The paper is well written, the ideas are well presented, figures are illustrative. I like how authors wrote "challenges" bullet points for every proposed method and then provided solutions for them. The theorems and lemmas are invoked appropriately. Some parts were not clear to me, which I have asked in the following sections. Nevertheless, I enjoyed reading the paper for its theory-grounded explainable RL approach to policy optimization.

### Weaknesses
There are a few weaknesses of the paper: 

1. The notion of l(s, a): The paper assumes access to environment interaction and hence I am considering that there is enough knowledge about the actions per given state. If that is so, the way l(s, a) is defined by the paper in definition 1, is simply negative of advantage function for policy $\pi_A$. 
2. The choice of MuJoCo environment and plausible issues: MuJoCo environments allow the agent to complete an episode for full length while other environments might terminate early if certain states are reached. Subsequently, MuJoCo environments provide correlated "second-chances" to the agent to make similar mistakes and the misleading effect is easy to capture. The algorithm's performance depends highly on the coverage of the demonstrations given by the earlier policy. MuJoCo would end up allowing coverage over optimal state-action visitation distribution and hence the algorithm proposed in the paper would work with single low-level and high-level explanation. However, this will not hold in the other complex environments. Also, in the case of sparse environments, where the agent has not received enough feedback from the environment to capture the "misleading" state-actions, the algorithm might misattribute notion of misleading.
3. Issue with complexity: To me, the bilevel algorithm seems an overkill if explanations are to be used for RL policy improvement. First of all, the idea of low-level optimization is simply to keep the policy improving by ensuring only a budgeted amount of disadvantageous actions are taken. Secondly, solving an IRL problem simply to gather a reward function to compare with ground truth reward function and reshaping it for policy update is again analogous to policy evaluation, done in an unorthodox manner. Why should we not simply assign meanings from XRL literature to the policy iteration or rather generalized policy iteration (GPI) procedural steps and keep training the RL agent. 
I don't see in any way the explanations during the training are helpful for the humans. The complexity of bilevel approach makes it even harder for the human to understand how various non-linear function approximators might be playing their role. Moreover, I am afraid that allowing SAC the same amount of compute as UTITLITY for per-step improvement, i.e., giving access to online rollouts and updating the policy under UTILITY's computational budget, we might end up with performance as good as that of UTILITY, if we are comparing only the extent of improvement to underlying RL policy updates.

### Questions
Suggestion -- I would suggest the authors to use RL-consistent notation and substitute -A(s, a) instead of l(s,a). This will also simplifies elucidation of the technique mentioned in the paper.

Q. Why did you take the dual into consideration? How does that help the algorithm? I mean, please provide description about how the dual forms an upper or a lower bound on the true objective against which this approximation is being taken. Further adding details about how this approximation is still valid with its loosening of the original objective would be helpful too. I find it hard to think that dual formulation for making the lower level optimization unconstrained and convex, and then using the optimal dual solution as reward function is still a valid way.

Suggestion -- To help illustrate UTILITY's explanations during the training iterations, it would be helpful if the authors provided evolution of Figure 1-c to Figure 1-d tracked across policy updates. This would support the utility of the UTILITY.

Q. I tried finding how the cost function is defined for the lower-level optimization. However, I could not find a technical section on definition of $c(s, a)$. Can authors please shed some light on this? Also, how do you decide the top-K misleading state-action pairs? This also was not mentioned anywhere, or I might have missed it.

Q. Can authors please demonstrate UTILITY's execution on a few more gridworld settings with reward variations: sparse, dense, multiple terminal states, etc.?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The paper proposes to solve two problems: 1) the incomprehensibility of reinforcement learning agents and 2) the suboptimal performance of the agents. It introduces a two-level explanation, consisting of a high-level explanation that illustrates the reward function the agent has learned internally. The low-level explanation shows the state-action pairs where an agent chooses suboptimal actions with respect to an optimal policy. The suboptimal state-action pairs are called misleading. They use the low-level explanations to explain when it is infeasible to utilize the high-level explanations, for example, environments with high dimensional features. The misleading state actions pairs and the high-level explanations together are used to improve policy performance via a new loss function. A new algorithm is proposed to solve the loss function introduced to improve policy performance. The proposed method is experimentally tested in several MuJoCo environments.

Note: my expertise lies in explainability, thus my opinion on the second contribution (model performance) should weigh less.

### Strengths
- The paper proposes a new way to utilize misleading state action pairs to improve policy performance. Furthermore, they explain why the policy did not attain optimal performance in the first place.
- The paper has done a great job on covering related work and contrasted to them.
- The method proposed shows better performance in terms of return than all the baseline methods. And has good ablation tests to see which part of the method that contributes most to the results.
- The authors have included code with the paper.

### Weaknesses
 - It is unclear to me why the policy would learn the wrong reward function internally in the first place. I might have misunderstood something.
- It is unclear why theorem 1 is true. I do not see reference to any proof.
- I am unsure how the performance would translate to environments with high-dimensional features. For example, Atari environments. Is there a reason why only MuJoCo environments are chosen for experiments?
- It is unknown how useful these explanations are to human users, and who is the target audience of these explanations.
- The main novelty is on improving model performance using explanations. The explanations themselves are not new to this work.

### Questions
- Definition 1: Why is the Q-function taken with respect to $\pi_A$. Isn't $\pi_A$ the suboptimal policy?
- Line 245: What is the functional form of the reward shaping function?
- Line 249: Why do we not want to visit misleading states? I thought it is where the agent takes a suboptimal action. Can we not fix the problem by just taking the optimal action when we encounter a misleading state?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper proposes to improve an RL policy by using IRL to learn a reward for which the policy is optimal, and then use this IRL reward to shape the original reward by adding two terms: (1) an additional reward proportional to the difference between IRL reward and true reward, and (2) a constraint that the policy does not visit significantly suboptimal states under the Q function of IRL reward. This results in a constrained RL problem, which the authors propose an iterative solution for. The algorithm is shown to improve over SAC and several other baselines that shape SAC on continuous control tasks.

### Strengths
Strengths:
1. The idea of using IRL as a signal for RL is interesting.
2. Figure 1 is very clear and helps understand the method.
3. The experiments and ablation studies seem rather extensive, although I am not familiar enough with the relevant baselines to say if anything important is missing.
4. The theoretical analysis of convergence for the iterative solution of the optimization problem in Section 4.2.3 is nice.

### Weaknesses
Weaknesses:
1. In the problem formulation, the authors formulate the constrained optimization problem in Eq. (1) as the problem that the agent needs tosolve. My biggest concern is that while the authors spend considerable efforts on showing that their solution of Eq. (1) is sound, the derivations leading to Eq. (1) seem very ad hoc to me, and I cannot understand why this method would work in general RL problems (or, for what problems should it work?)
2. The writing and presentation could be improved. For example, the paper talks a lot about explainability, but I did not find explainability to be relevant here so much. At some point, the “explainable RL” idea is replaced by standard IRL. I think the authors should tone down the XRL parts and focus instead on using IRL as a signal in RL.

Details:

1. The derivations leading to Eq. (1), the main objective of the method, are not clear to me. I collect here several unclear passages.
    1. Line 185: “At a low level, the RL agent is not optimal meaning that it visits some critical points that lead to the non-optimality.” - I don’t understand this. It could be that the agent is slightly suboptimal *on all* states. This statement seems very ad hoc. Why should it be suboptimal only on some critical points?
    2. Line 199: \pi* and \pi_A are distributions. What does \pi_A - \pi* mean exactly? Why is it a metric?
    3. Line 209: isn’t this a well known result? I.e., a policy is optimal iff it satisfies the Bellman equation.
    4. Line 215: I’m not sure why Top K “misleading” states make sense. Because changing an action in a state affects the future states the agent will visit, I don’t see how ordering by misleading level makes any sense. For example, consider an agent that at the first step can walk either right or left. If it chooses right, it reaches the goal after some time and obtains reward. If it chooses left, after some time it can either choose to reach the goal, or die and get a huge negative reward. Consider a policy that both takes left in the beginning, and then chooses to die and get the negative reward. Because of discounting, the most misleading state here would be the last state with the negative reward. But if the agent chose right in the beginning, it would not have even reached this state at all, and that would be the state that we want to fix.
    5. Line 240: I don’t understand what the difference r - \hat{r}  really means. Is there any formal result that ties between  \hat{r}  that is the max likelihood IRL solution to the true reward in the system? Is there any formal result that makes this ad hoc choice make sense?
    6. Line 247-257: This whole paragraph seems very ad hoc. Why should we discourage the misleading state-actions? Maybe under a different policy, they are actually necessary for optimal behavior? E.g., consider an agent that *must* cross some “bridge” to get to the goal. Now, because the agent is not optimal, state actions on the bridge are misleading. But if we restrict the agent from visiting them, it will *never* get to the goal! The causal entropy term is also not well motivated - why is exploration crucial here? 

Summary (and explanation for score): I think this paper really needs more work in explaining *why* the approach makes sense. A theoretical result that ties the max-likelihood IRL that the authors build on to Eq. (1) and some optimal policy in the MDP, for example, would go a long way in establishing the soundness of this work, and what MDPs it should work for (the examples I mentioned above hint that for some MDPs we should not expect this approach to work well).

### Questions
see above.

### Soundness
2

### Presentation
2

### Contribution
3
