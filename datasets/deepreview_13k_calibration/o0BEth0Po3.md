# ExID: Offline RL with Intuitive Expert Insights in Limited-Data Settings

- Decision: Reject
- Avg Score: 4.00
- Scores: 3, 5, 6, 3, 3

## Abstract
With the ability to learn from static datasets, Offline Reinforcement Learning (RL) emerges as a compelling avenue for real-world applications. However, state-of-the-art offline RL algorithms perform sub-optimally when confronted with limited data confined to specific regions within the state space. The performance degradation is attributed to the inability of offline RL algorithms to learn appropriate actions for rare or unseen observations. This paper proposes a novel domain knowledge-based regularization technique and adaptively refines the initial domain knowledge to considerably boost performance in limited data with partially omitted states. The key insight is that the regularization term mitigates erroneous actions for sparse samples and unobserved states covered by domain knowledge. Empirical evaluations on standard offline RL datasets demonstrate a substantial average performance increase compared to ensemble of domain knowledge and existing offline RL algorithms operating on limited data.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper aims to incorporate the domain knowledge in the sparse states where the offline data is not explored much. 
Firstly, the teacher policy $\pi_t^w$ is trained by using the domain knowledge in the heuristic manner. And then, the offline policy is trained using a proposed critic-regularization term to enhance performance.

### Strengths
- The novel concept: It is not easy to incorporate some general domain knowledge to train the policy. They try to put somehow symbolic control in the discrete action offline RL.
Method

- The critic regularization term: To use domain knowledge in the offline RL setting, the proposed regularization term is intuitive and proper.

### Weaknesses
 - The method ‘Training Teacher’ is somehow naive, and Eq. (2) is not clear. (Actually, I don’t understance what it is)

- Limited domain: It is not applicable in the continuous action space.

- The hyperparameter $\lambda$, the coefficient constant for critic regularization. There is no exact way to decide the proper value of $\lambda$.

- Updating the Teacher policy: The explanation for updating the teacher policy, especially after line 226, becomes difficult to follow.

- Writing should be enhanced.

### Questions
In the regularization term, are there any gradient stop or .detach() (in torch) in Q-network? 
Line 128, The definition of target network parameter $\theta'$ is missing.

### Soundness
2

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
This paper presents ExID, an offline RL method that enhances policy learning in limited-data settings by using a domain-knowledge-based regularization technique, significantly improving performance over traditional offline RL approaches across diverse datasets.

### Strengths
1. Innovative to incorporate the domain knowledge. 
2. real-world application in sales promotion dataset and simglucose dataset.

### Weaknesses
1. Training the teacher network highly requires domain knowledge. 
2. The method is heuristic and plug-and-play in different algorithms. 
3. The simulation tasks are simple.

### Questions
1. Can this method be applied to a continuous environment? If yes, should the authors try difficult simulated tasks, such as d4rl? 
2. Can this method be applied to different base algorithms, e.g., BEAR, IQL.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
In this work, the authors propose a new transfer offline RL method ExID, which transfer the learned policy of the source domain into the target domain with a expert system and limit data of target domain.

### Strengths
- This work forces on a new and important setting. This setting is make sence because the less the data is, the more the risk is.
- This work proposes a simple but effect architecture, which update the target network and the teacher at the same time. This architecture let the method can be used with expert systems with different qualities.
- The final result is good especially when the target data is noisy.

### Weaknesses
 - The presentation of this work is limit. For example, in Section 3, there is "(s,a,s')\in B, then s'\in B". What exactly the structure of the buffer is? Also, the Eq. 2 is hard to understand at the first time. 
- The environments used in this work are all simple and visible. Can we propose a useful expert system for more complex environments, such as halfcheetah?

- This work leverages a uncertainty based method to update the teacher network. Is this a stable standard? How many times the teacher network is updated in the learning process?

### Questions
- This work leverages a uncertainty based method to update the teacher network. Is this a stable standard? How many times the teacher network is updated in the learning process?
- How many feasible s of  Proposition 4.3?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper work on incorporating domain knowledge into offline RL to improve OOD performance.
The method appears to be based on DQN, but incorporates a "teacher" policy network which is used to regularize the argmax Q-function policy.

### Strengths
The use of domain knowledge in RL is worthy of study.

The results seem to indicate some empirical advantage of the method over baselines (although not consistently so).

### Weaknesses
 **Unconvincing motivation and contributions**
This seems to be an avenue of work that has received very limited attention, and I would appreciate a more thorough motivation for both the problem setting and the approach proposed.

The environments studied seem pretty simple, and I'm not convinced by the baselines.  
I'm skeptical that this approach can scale, as it is based on strong domain knowledge. 
The practical utility on simple environments is also unclear -- can the authors make a more clear and compelling case of when and why they expect this approach to yield practical value?
I would also expect more discussion of how well this approach can scale to more complicated environments, and what sort of future work might help answer that question.

**Other presentation issues**
- I found the presentation of the algorithm confusing and presentation to be weak overall.
- should use citep
- Definition 4.1 is confusing.
-- I think the notation in the first condition (bullet point) is used incorrectly.
-- The 2nd bullet point seems redundant (being guaranteed to hold if the first condition holds).


**Inadequate treatment of model-based RL**
The work needs a more thorough comparison with model-based offline RL methods.
Currently, there is only one experiment reported (in insufficient detail) in the appendix.
I would expect these baselines to be run for all of the environments and reported in main text.
As such, I'm not convinced the authors have made a fair effort to tune and compare their methods with baselines. 
Furthermore, the point of comparison is MOPO, a method from 2020 -- are there more modern methods which ought to be considered?

The submission also states that for such methods "performance highly depends on the accuracy of the learned dynamics."  But this claim is not supported.  These methods are meant to keep policies from seeking out states where the learning dynamics are inaccurate, and thus, we might expect performance to degrade gracefully in the presence of inaccurate dynamics.  On what basis are the authors claiming otherwise?

### Questions
Are there more modern offline RL methods which ought to be considered?

Can your approach be viewed as a form of actor-critic?  Would an actor-critic method be more performant?

What are some alternative methods for 

Does D specify a complete policy (I.e. does it have support on the entire state space)?  If so, I think the notation should be pi_D.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes an offline RL algorithm, ExID, that can leverage domain knowledge-based heuristic rules to enhance small-sample performance. The proposed algorithm can be seen as combining conservative Q-learning (CQL) and Uncertainty Weighted Actor-Critic (UWAC), and adds a CQL-style domain knowledge-based regularize, i.e., push up Q-values for actions that comply with the domain knowledge and push down Q-values for policy-generated actions. For detailed, comments please refer to strengths and weaknesses.

### Strengths
- Leveraging domain knowledge to enhance sample efficiency in offline RL is meaningful.
- The idea of modeling domain knowledge as tree-based heuristic rules and incorporating them using CQL-style value regularization is interesting. 
- The paper is easy to read. The results show good performance for tasks that have domain knowledge-based rules.

### Weaknesses
 - The literature review is insufficient, missing many recent offline RL works that focus on sample efficiency and OOD generalization.
- The proposed method has very stringent requirements for the domain knowledge input. Although we can design domain knowledge trees for simple tasks, it is not practical for complex tasks. Typically, in many real-world tasks, we might only be able to write very few heuristic rules for a task, which can only sparsely cover the state-action space. This severely limits the applicability of the proposed method for a wide range of problems. In the experiments, the authors are also only able to evaluate their method in very simple task environments.
- When training the teacher policy $\pi_t^w$, a random action is used if a state is not covered by the domain knowledge rules. This can be very problematic, as it will inevitably lead to sub-optimality when regularizing the learned policy. Moreover, if only a small set of domain knowledge rules is given (common in most practical problems), then it will cause the teacher policy to learn lots of random behavior, which could damage policy learning.
- The algorithm is essentially a combination of CQL and UWAC, with an additional value regularization that penalizes the value for actions that are not consistent with the domain knowledge. Since CQL is already very conservative and does not generalize well. Adding additional conservative regularization will further distort the value function, which could impact the optimality of the learned value.
- Propositions 4.2 and 4.3 are meaningless and have huge theory-practice gaps. The proposed method combines both CQL and the uncertainty-based method, which makes it almost impossible to draw any reliable theoretical conclusion on the learned value function and the policy. In the proof of Proposition 4.2, the underlying analytical tools used work for any policy, the only thing related to the proposed method is the **assumptions** $\rho_{\hat{\pi}}=\rho_{\pi_{u}}-\Delta_i$ and $\rho_{\hat{\pi}}=\rho_{\pi_{u}}-\Delta_o$, with $\Delta_i$ and $\Delta_o$ assumed to be positive, as well as $Q^*(s,\hat{\pi}(s))-Q^*(s,\pi_u(s)) \approx 0$ for in distribution actions. First, these assumptions have no guarantees from your algorithm. Second, to prove something, you simply cannot introduce some arbitrary assumptions to achieve your purpose. Proposition 4.3 is also trivial and not very meaningful. It only relates to the optimal value function $Q^*$, rather than the learned value function $Q^{\theta}$. You can only learn $Q^{\theta}$, and the proposition provides no information to tell if the teacher policy indeed helps to improve the learned $Q^{\theta}$.
- There are also some inconsistencies in the symbols used in the paper. For example, the teacher policy is expressed as $\pi_t^w$ in the text, but written as $\pi_w$ in Figure 2. The action value function is written as $Q_s^{\theta}$ in the text, but written as $Q_{\theta}$ in Figure 2.

### Questions
- How can the method be used if only limited domain knowledge rules are provided?
- Is it possible to not use random action for cases that are uncovered by domain knowledge rules?

### Soundness
1

### Presentation
2

### Contribution
2
