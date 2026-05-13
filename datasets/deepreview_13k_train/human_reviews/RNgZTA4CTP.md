# Best Possible Q-Learning

- Decision: Reject
- Scores: 6, 5, 3, 8

## Abstract
Fully decentralized learning, where the global information, \textit{i.e.}, the actions of other agents, is inaccessible, is a fundamental challenge in cooperative multi-agent reinforcement learning. However, the convergence and optimality of most decentralized algorithms are not theoretically guaranteed, since the transition probabilities are non-stationary as all agents are updating policies simultaneously. To tackle this challenge, we propose \textit{best possible operator}, a novel decentralized operator, and prove that the policies of agents will converge to the optimal joint policy if each agent independently updates its individual state-action value by the operator. Further, to make the update more efficient and practical, we simplify the operator and prove that the convergence and optimality still hold with the simplified one. By instantiating the simplified operator, the derived fully decentralized algorithm, \textit{best possible Q-learning} (BQL), does not suffer from non-stationarity. Empirically, we show that BQL achieves remarkable improvement over baselines in a variety of cooperative multi-agent tasks. %Due to the convergence and optimality, we believe BQL will be a new paradigm for fully decentralized learning.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes an alternate update strategy for Multi-Agent Q-Learning in the "fully decentralized" setting, i.e., where individual agents only have access to their own actions. This update uses the "best possible operator" to update individual agents' Q-values based on an optimistic estimate of the other agents' Q-values using a 2-step update. On the theoretical front, the paper justifies this choice of update strategy by showing the optimality of this update strategy in ideal conditions (i.e., in the asymptotic limit and with access to $\boldsymbol{\pi}^*_{-i}$). The paper evaluates the performance of BQL on 4 domains and shows improved performance in each.

### Strengths
- **The experiments are extensive:** The paper compares BQL against reasonable baselines on four reasonable "domains". I am not well-versed in the MARL literature, so it's possible that these are cherry-picked, but there is enough evidence to convince me that BQL is doing something useful, esp., that BQL uses the batch data $\mathcal{D}$ in a more useful way than baseline methods in the fully decentralized setting. Minor nitpicks:
  1. The experiments are often not run till convergence, e.g., 3(c), 4(a,b), 5(b,d).
  1. It would be nice to have upper bounds like Joint Q-Learning in the Tabular Case and a CTDE baseline in the NN-case.
- **The paper is reasonably well-written:** I think the descriptions of the methods and experiments are good. It's not clear to me (as someone who doesn't actively work in RL) how novel the theory is, but it is quite clean and has some interesting ideas. Minor nitpicks:
  1. It seems like the theory is mostly a reduction of the "fully decentralized setting" to the "joint Q-learning"/CTDE setting. However, the actual connection is quite obfuscated; could you clarify how these two are related (and what is different)? It also seems like BQL can be seen as an extension of I2Q to the stochastic setting. Is this a fair comparison?
  1. I did not follow the last couple of steps in the proof of Lemma 4. Specifically, how are you combining the various expressions to get the second last equation, and how are you unrolling it to get the last one?

### Weaknesses
 - **BQL is not "fully decentralized"?** In the tabular setting, Algorithm 1 assumes that you can ensure that agents independently explore, but it's not clear that's a realistic assumption in this "fully decentralized setting". Specifically, the algorithm requires each agent to explore all actions in each state infinitely often, which is difficult to guarantee without some form of coordination or centralized control. BQL- is more realistic and still seems to outperform baselines, but it seems like the key ingredient to getting BQL- to work is ensuring enough exploration. It would be useful to compare how well BQL does based on how much exploration is allowed (e.g., by changing the distance of the initialization to an equilibrium, or by explicitly varying the exploration rate). It would also be useful to talk about whether sufficient exploration is a realistic assumption in practice, and if not, how the performance of BQL degrades in the absence of such exploration.
- **No intuition for the 2-step update when the theoretical assumptions are broken:** The paper leans heavily on asymptotic intuitions, but a lot of the wins in 4.3 and 4.4 seem to come from sample efficiency. Is there any intuition for this? For example, in the single replay buffer setting, the theoretical guarantees are not directly applicable, yet BQL still shows improved performance. It would be helpful to understand why the 2-step update provides a benefit in this setting. More generally, there seems to be a gap between theory and practice, esp., the improved performance of BQL when there is only a single replay buffer $\mathcal{D}$. Are there any intuitions for why BQL works in this case? Is it simply that the 2-step update provides a more stable target, or is there something more fundamental happening?

### Questions
The things that it would be most useful to clarify are:
1. Are the theoretical proofs a reduction of the "fully decentralized setting" to the CTDE setting? If so, what are the assumptions required? If not, what is the gap?
1. How does the performance of BQL change as you modify the amount of exploration that is performed by the agents?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work proposes Best Possible Q-Learning. They introduce the best possible operator, which is like the standard Bellman operator, but because the actions of the other players are unknown, the operator also includes a maximization over all marginal transition probabilities under other players' policies. The computation of the best possible operator is heavy since it involves searching over all possible transition probabilities. Therefore, the work further proposes the simplified best possible operator and use it to design the algorithm. In the algorithm, every player, with some probability, will execute some random policy in order to explore possible transition probabilities.

### Strengths
- The proposed algorithm looks promising in achieving decentralization in cooperative reinforcement learning.
- The experimental part looks extensive and has covered many different environments. Though due to my unfamiliarity with previous algorithms, I cannot confidently say whether the comparison is fair or not.

### Weaknesses
 - For the explanation on the algorithm and theoretical justification, the writing is unclear in general. There are several arguments I cannot verify, and I suspect that there are flaws in the proof of the convergence. Please see Questions below.  This also largely hinders my understanding of the algorithm. 
- The figure for experiments are too small.

- In the Equation in Lemma 1 (the definition of $Q_i(s,a_i)$), should the $r$ be $r_i(s,a_i)$? If it should, should we also include $\max_{r_i(s,a_i)}$ in the definition of $Q_i(s,a_i)$? It's a bit strange if the reward does not depend on the current state and the action chosen by the player. 
- Again, in the definition of $Q_i(s,a_i)$, what is the search space of $P_i(\cdot|s,a_i)$? Do you search for "all possible transitions probabilities" from $(s,a_i)$?  If it is, then why not the solution simply be $Q_i(s,a_i)=r + \max_{s', a_i'} Q_i(s', a_i')$? That is, the optimal solution of $P_i(\cdot|s,a_i)$ should put all probability to the state $s'$ that has the highest value of $\max_{a_i'}Q_i(s',a_i')$. 
- I have difficulty understanding the first inequality in the equation series in Lemma 2, i.e., the step that replaces $P_{\text{env}}$ with $P_i^\star$ with a $\geq$ inequality. Can you explain that inequality? 
- I don't understand the following sentence in Page 5: "As $P_i$ depends on $\pi_{-i}$ and agents act deterministic policies, $D^m_i$ contains one $P_i$ under a deterministic $\pi_{-i}$. " I thought $D^m_i$ only contains tuples of the form $(s,a,r,s')$, why would it contain $P_i$? 
- In Page 5, it is said that "When M is sufficiently large, given any $(s,a')$ pair, any $P_i(s,a_i)$ can be found in a replay buffer. " I thought the set of $P_i(s,a_i)$ is infinitely large since these are continuous values, how is it possible that a finite set can contain all possible values of $P_i(s,a_i)$?  Again, it's unclear what you mean by $P_i(s,a_i)$ can be found in replay buffer, since replay buffer only contains $(s,a,r,s')$ tuples. 
- I don't understand the following sentence in page 5: "Simplified best possible operator ... does not care about the relation between transition probabilities of different state-action pairs in the same buffer. "
- In Page 5, it is said that "BQL ideally needs only $|A|$ buffers.. which is very efficient" Suppose that every player has $K$ actions, is $|A|=K^N$? I'm not sure one can call this very efficient, given that this is exponentially large, and running a centralized Q-learning (so the number of joint action is K^N) should also just incur the same amount of computation.

### Questions
- In the Equation in Lemma 1 (the definition of $Q_i(s,a_i)$), should the $r$ be $r_i(s,a_i)$? If it should, should we also include $\max_{r_i(s,a_i)}$ in the definition of $Q_i(s,a_i)$? It's a bit strange if the reward does not depend on the current state and the action chosen by the player. 
- Again, in the definition of $Q_i(s,a_i)$, what is the search space of $P_i(\cdot|s,a_i)$? Do you search for "all possible transitions probabilities" from $(s,a_i)$?  If it is, then why not the solution simply be $Q_i(s,a_i)=r + \max_{s', a_i'} Q_i(s', a_i')$? That is, the optimal solution of $P_i(\cdot|s,a_i)$ should put all probability to the state $s'$ that has the highest value of $\max_{a_i'}Q_i(s',a_i')$. 
- I have difficulty understanding the first inequality in the equation series in Lemma 2, i.e., the step that replaces $P_{\text{env}}$ with $P_i^\star$ with a $\geq$ inequality. Can you explain that inequality? 
- I don't understand the following sentence in Page 5: "As $P_i$ depends on $\pi_{-i}$ and agents act deterministic policies, $D^m_i$ contains one $P_i$ under a deterministic $\pi_{-i}$. " I thought $D^m_i$ only contains tuples of the form $(s,a,r,s')$, why would it contain $P_i$? 
- In Page 5, it is said that "When M is sufficiently large, given any $(s,a')$ pair, any $P_i(s,a_i)$ can be found in a replay buffer. " I thought the set of $P_i(s,a_i)$ is infinitely large since these are continuous values, how is it possible that a finite set can contain all possible values of $P_i(s,a_i)$?  Again, it's unclear what you mean by $P_i(s,a_i)$ can be found in replay buffer, since replay buffer only contains $(s,a,r,s')$ tuples. 
- I don't understand the following sentence in page 5: "Simplified best possible operator ... does not care about the relation between transition probabilities of different state-action pairs in the same buffer. "
- In Page 5, it is said that "BQL ideally needs only $|A|$ buffers.. which is very efficient" Suppose that every player has $K$ actions, is $|A|=K^N$? I'm not sure one can call this very efficient, given that this is exponentially large, and running a centralized Q-learning (so the number of joint action is K^N) should also just incur the same amount of computation.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies decentralized multi-agent reinforcement learning (RL). It proposes a new operator called best possible operator in updating the Q-values, along with a computationally efficient variation called simplified best possible operator.

Analytically, both operators are shown to converge to the optimal joint policy.

Empirically, Q-learning based on such operator is shown to achieve good performance across a number of tasks.

### Strengths
- Good empirical performance on a variety of tasks

- A systematic method for updating Q-values in a decentralized multi-agent setting

### Weaknesses
1. The proofs have inaccuracies which impede a clear understanding of the underlying logic.

a.Lemma 2:

this line appears to be incorrect: 

$=\gamma  P_i^*(s^′|s, a_i)  \max_{a_i^′} (\max_{a_{-i}^′} Q(s^′, a_i^′ , a^′_{-i} ) − Q^{k−1}(s^′, a_i^′ ))$

: the $\max_{a_i}$ cannot be factored out here since the maximum actions can be different for the two Q value terms inside the parenthesis and there is a minor sign. Apart from this, the remainder of the lemma appears to be correct.

b.Lemma 3:

In the proof of Lemma 3, the second inequality appears to be valid. However, it seems to omit intermediate steps. The absence of these steps makes it challenging to follow the reasoning.
Elaborating on these steps would enhance the clarity of the proof.

c.Lemma 4: 

“Similar to the proof of Lemma 2, we can easily prove $\max_{a_{−i}} Q(s, a_i, a_{−i}) \leq Q^k_i (s, a_i)$”

While the result seems valid, it may not be as straightforward as implied, especially considering the nuances in this context. In particular, the simplified operator incorporates an additional max operator (8), when compared to the operator (6) used in Lemma 2. A more detailed elaboration of the steps involved in this proof would be beneficial.

2. As I will detail in the following, the conditions in the convergence proof for both operators seem too strong to hold in practice. There seems to be lack of sufficient attention to how these conditions might be met, thus leading to doubts around the practical relevance of the operators.

Both operators implicitly assume that the expectation w.r.t. the transition probabilities in (6, 7) can be computed exactly, at every step of the value update (i.e., $\forall k$). This is a significant limitation, as in practice, these expectations are typically approximated using samples.

Although the simplified operator is “simpler” due to not requiring the computation of expectations for every $\tilde{P_i}$, it still poses practical challenges. The need to compute the expectation for even one $\tilde{P_i}$ at every update step seems impractical. This requirement of exact expectation calculation at every step is not aligned with standard reinforcement learning practice, where expectations are approximated from samples.

In fact, an approximation error in computing the expectations, when combined with the max operation, could cause the over estimation of Q values. This issue, briefly mentioned in the text following Eq. (10), lacks a clear explanation in my opinion. The paper does not adequately address how the proposed method mitigates the overestimation bias, which is a well-known problem in Q-learning. The approximation error would also lead to the violation of the Q value upper bound, undermining the convergence guarantees for both operators.



### Questions
Can the authors please comment on my concerns listed in the weaknesses?

### Soundness
1 poor

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose a strategy called best possible Q-learning for agents learning the optimal joint policy in fully decentralized learning. Under this strategy, when learning the Q function, each agent assumes that after choosing the action, the transition of the $N$-agent environment will be the ``best case" so that the expected return is maximized. The authors prove the convergence of such an elegant strategy to global optimal joint policy (under some assumptions). The authors also provide a simplified version of this strategy that is more computationally attractive.

### Strengths
The writing is clear, which makes it enjoyable to read. Even restricted by the assumption of deterministic policies and the uniqueness of optimal joint policy, it is still impressive that with such an elegant best possible Q-learning, the global optimal policy can be computed.

### Weaknesses
Lemma 2 is a crucial lemma for justifying the best possible operator. However, the second equality appears to be incorrect. Specifically, the maximization over $a_i$ seems to be misapplied, as it should not distribute over the summation. The current formulation incorrectly suggests that each agent's action $a_i$ can independently maximize both the immediate reward and the discounted future reward, which is not generally true. This needs clarification.

I think (3) (where $Q(s,\boldsymbol{a})$ is equipped with some arbitrary $\boldsymbol{a}$) is not the expected return of the optimal joint policy. The definition of $Q(s,\boldsymbol{a})$ seems to imply that after taking an arbitrary joint action $\boldsymbol{a}$, the agents will then follow the optimal joint policy. However, the value function under the optimal joint policy should be defined as the expected return when starting from state $s$ and following the optimal policy from the beginning, not after taking an arbitrary action.

In the proof of lemma 1, I notice that there is an underlying assumption that the actions taken by other agents do not restrict the allowable actions of each agent. This assumption is not always realistic in multi-agent systems. If there are constraints on the joint action space, such as certain actions being unavailable to an agent depending on the actions of others, does the best possible learning strategy still apply? This needs to be addressed, as it limits the applicability of the proposed method.

### Questions
- Is it a common setting that the reward function is only dependent on the current state and the next state (without the dependency on the action)? To me this is not commonly seen.

- I think (3) (where $Q(s,\boldsymbol{a})$ is equipped with some arbitrary $\boldsymbol{a}$) is not the expected return of the optimal joint policy.

- In the proof of lemma 1, I notice that there is an underlying assumption that the actions taken by other agents do not restrict the allowable actions of each agent. If this restriction is considered, does the best possible learning strategy still apply?

- The 3rd line under problem (6), could the authors provide exactly where is the reference in (Puterman, 1994)?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
