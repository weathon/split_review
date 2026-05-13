# A Nearly Optimal and Low-Switching Algorithm for Reinforcement Learning with General Function Approximation

- Decision: Reject
- Scores: 5, 5, 6, 5

## Abstract
The exploration-exploitation dilemma has been a central challenge in reinforcement learning (RL) with complex model classes. In this paper, we propose a new algorithm, Monotonic  Q-Learning with Upper Confidence Bound (MQL-UCB) for RL with general function approximation. Our key algorithmic design includes (1) a general deterministic policy-switching strategy that achieves low switching cost, (2) a monotonic value function structure with carefully controlled function class complexity, and (3) a variance-weighted regression scheme that exploits historical trajectories with high data efficiency. MQL-UCB achieves minimax optimal regret of $\tilde{O}(d\sqrt{HK})$ when $K$ is sufficiently large and near-optimal policy switching cost of $\tilde{O}(dH)$, with $d$ being the eluder dimension of the function class, $H$ being the planning horizon, and $K$ being the number of episodes. 
   Our work sheds light on designing provably sample-efficient and deployment-efficient Q-learning with nonlinear function approximation.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper considers low switching-cost algorithm with general function approximation, with the Bellman operator of the
underlying Markov decision process (MDP) is assumed to map any value functions
into a function class with a bounded eluder dimension. The key algorithmic design
includes a general deterministic policy-switching strategy that achieves low
switching cost, a monotonic value function structure with carefully controlled
function class complexity, and a variance-weighted regression scheme that
exploits historical trajectories with high data efficiency. MQL-UCB achieves
minimax optimal regret of $O(d \sqrt{HK})$ when K is sufficiently large and near-
optimal policy switching cost of $O(dH)$, with d being the eluder dimension of the function class, H being the planning horizon, and K being the number of episodes.

### Strengths
This paper proposes a novel policy-switching strategy based on the cumulative sensitivity of historical data. To the best of our knowledge, this is the first deterministic rare-switching strategy for RL with general function approximation which achieves Oe(dH) switching cost. 

With the novel policy-switching scheme, this paper showcases how to reduce the complexity of value function classes while maintaining a series of monotonic value functions, strictly generalizing the LSVI-UCB++ algorithm to general function class with bounded eluder dimension.

### Weaknesses
1. Why in definition 2.8, it is reasonable to assume a bounded covering class for bonus? Since you assume covering for $\mathcal{F}$ in 1. of Def 2.8, and def. of $D_\mathcal{F}$ is clear, can you derive the covering number of the bonus class rather than assuming it exists?

2.  The update criteria in Line 6 of Algorithm 1 is incomplete and I cannot find it directly. Maybe that corresponds to the last equation in page 5? This is crucial as it will decide the switching cost of the algorithm. 

3. How is policy updated in Algorithm 1 if the "if condition" in line 6 is not satisfied? Without it how do you rollout in Line 21? 

4. The monotonic value function seems to be an interesting idea that can keep the conditional variance on track. However, the explanation is too short. May I ask how could you "ensure that the pessimistic value maintains a monotonically increasing property during updates, while the optimistic value function maintains a monotonically decreasing property"? Also, you say inspired by He et al., is the idea the same or there are some differences?

### Questions
Please answer the questions above.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a new algorithm, Monotonic Q-Learning with Upper Confidence Bound, to solve reinforcement learning with general function approximation.
Specifically, the proposed algorithm is based on a new policy-switching strategy that only requires $\tilde{O}(dH)$ switches, and achieves $O(\sqrt{dim(\mathcal{F}) \log \mathcal{N} HK})$ regret.
The regret is minimax optimal in the special case of linear MDPs.

### Strengths
- This paper generalizes the approach by He et al (2022) to solve general function approximation. The authors extend the technique in He et al (2022) by changing the covariate matrix criterion with the newly proposed $D_{\mathcal{F}_h}^2$ criterion.
- Compared to existing papers studying similar problems, this paper is able to get near-optimal regret with fewer number of switches, and uses a simpler planning strategy.

### Weaknesses
 - A few assumptions look really strong. For example, assuming completeness holds for any function $V$ as well as for second moments is not common in my opinion. Specifically, the assumption that the function class is complete with respect to the Bellman operator and also complete with respect to the variance of the value function seems particularly strong, and it is not clear if this assumption can be satisfied in practice for complex function classes. This assumption is crucial for the theoretical analysis, but its practical implications and limitations should be discussed in more detail.
- The optimality of regret is only for linear MDPs, and the authors prove no lower bound for general function approximation. This limits the impact of the theoretical results, as it is unclear whether the proposed algorithm is truly optimal in the general function approximation setting. The lack of a lower bound makes it difficult to assess the tightness of the derived regret bound.
- Overall, the paper could be better organized, and adding some more intuitive explanations will be helpful for readers. The current presentation makes it difficult to follow the technical details and understand the key ideas behind the proposed algorithm. For example, the motivation behind the specific policy switching strategy and the choice of the $D_{\mathcal{F}_h}^2$ criterion could be explained more clearly.
- There are quite a few typos in the paper. For example, in page 3, $O$ is missing for regrets in table 1. In page 6, a parenthesis is missing in the definition of $b_{k,h}$, and there is an excessive He et al (2022). In page 8, "may differs" should be "may differ".

### Questions
- Please clarify points raised in "weaknesses".
- Can you elaborate more on how to find the bonus oracle $\bar{D}^2_{\mathcal{F}}$?
- Why should we care about the monotonic properties of the value functions?
- Given Theorem 4.4, can you rephrase the regret bound in terms of eluder dimension?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper considers RL setting with general function approximations, and targets at achieving near-optimal regret with only a small number of policy switching.
The authors consider the same Generalized Eluder dimension in (Agarwal et al., 2022) as the complexity measure for function classes, and contribute an algorithm, which only performs policy updates once the collected information goes beyond a threshold from last updating.
The authors also show that their algorithm can achieve sublinear regret (near-optimal when restricted to the linear class) with low policy switching.

### Strengths
The problem studied in this paper is well-motivated. 
The algorithm proposed in this paper indeed achieves some improvement comparing with previous works.
The authors also include several informative discussions, e.g. connection between $D^2_{\mathcal{F}}$-uncertainty and Eluder dimension.

### Weaknesses
1. I have doubts on whether the claim that "MQL-UCB achieves near-optimal policy switching" is true.

   It seems to me this paper only considered the case where the algorithm is only allowed to deploy deterministic policy at each iteration, and the $\Omega(dH)$ policy switching lower bound the authors compared with also only holds for such setting. Intuitively, stochastic policies should have better exploartion ability than deterministic policies and should be preferred more in deployment efficienct learning setting. There are also several closely related works [1] and [2] have reported that when the algorithm can deploy stochastic or even non-Markovian policies at each iteration, the lower bound of deployment complexity would be $\Omega(H)$ and can be matched.

   However, such clarification is missing and those closely related works are also not mentioned in the paper. I would suggest the authors clarify about this issue somewhere in the introduction and include the discussion with those related works in the paper.

2. It is not very clear to me what the main novelty in technique analysis and innovations in algorithm design in this paper. There are lots of places "inspired by ...(some previous work)" in this paper, and it's not clear what are the novel parts and what are ingredients from previous work.

3. The paper writing can be improved.
* In line 6 of Algorithm 1, seems something is missing after "such that".
* It would be better to discuss the main results (section 4) before section 3

### Questions
What are the technical novelty and innovation in algorithm designs? Could you highlight it more clear?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the authors propose an algorithm named MQL-UCB for Reinforcement Learning with general function approximation. The MDP setting satisfies that the Bellman operator could map any value functions into a function class with a bounded Eluder dimension. The algorithm is shown to achieve near optimal regret and switching cost simultaneously.

### Strengths
1. The setting of reinforcement learning with low switching cost and general function approximation is interesting and important.

2. The paper is solid, the proof looks correct to me.

3. Both the regret bound and the switching cost bound is nearly minimax optimal.

### Weaknesses
1. My main concern is about technical novelty. It seems that the only different component compared to LSVI-UCB++ is the policy switching framework. It would be better if the authors could highlight the technical novelty, especially the part that is different from [1]. Specifically, while the idea of switching based on a cumulative sensitivity score is mentioned, the precise mechanism and its theoretical justification in the context of general function approximation are not sufficiently elaborated. The connection to the determinant of the covariance matrix used in linear settings needs to be made more explicit, particularly why the $D^2$ quantity serves as a suitable replacement and how it ensures a tractable covering number for the value function class.

2. It is not very clear how general the function approximation is. It would be better if the authors could discuss more about the relationship between this setting and some other settings, like the linear Bellman complete MDP and the Eluder Condition class. Under these settings, [2] and [3] design algorithms with low switching cost and sub-linear regret bound. The paper should clarify whether the proposed setting strictly contains or is contained within these other settings, and if not, what are the key differences and implications for the applicability of the results. A more detailed comparison of the assumptions and guarantees is needed to understand the scope of the proposed method.

3. The presentation is not very clear. As a paper focused on theory, a proof sketch is expected. In addition, in line 6 of Algorithm 1, the switching condition is replaced by '...', which is very confusing (although it is discussed in the main text). The algorithm description should be self-contained and not rely on the reader to piece together the details from the main text. The lack of a clear proof sketch makes it difficult to assess the correctness and the technical depth of the results.

### Questions
Please see the weakness section.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
