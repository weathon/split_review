# Towards Zero-Shot Generalization in Offline Reinforcement Learning

- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 6, 6, 5

## Abstract
In this work, we study offline reinforcement learning (RL) with zero-shot generalization property (ZSG), where the agent has access to an offline dataset including experiences from different environments, and the goal of the agent is to train a policy over the training environments which performs well on test environments without further interaction. Existing work showed that classical offline RL fails to generalize to new, unseen environments. We propose pessimistic empirical risk minimization (PERM) and pessimistic proximal policy optimization (PPPO), which leverage pessimistic policy evaluation to guide policy learning and enhance generalization. Theoretically, our framework is capable of finding a near-optimal policy with ZSG. Empirically, our framework demonstrates the ability to enhance the performance of the base offline RL methods. Our result serves as a first step in understanding the foundation of the generalization phenomenon in offline reinforcement learning. Our codes are released at [this link](https://anonymous.4open.science/r/ProcgenExp-B5B4).

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper focuses on generalization across contexts in offline RL. The authors prove that their proposed algorithms, pessimistic ERM and pessimistic PPO can achieve good regret bounds in this setting. Inspired by the theory, a modified version of IQL is evaluated on offline ProcGen and showcases the benefits of the approach.

### Strengths
The paper tackles an important problem, generalization in RL with offline datasets, and takes a theoretical perspective. From a look, the derivations seems sound and generally, enough detail is included to understand. 
Also, although the paper has a theoretical focus, it is nice to see some of the principles tried in an empirical setting.

### Weaknesses
 The problem setting requires some clarification. The general setting is contextual MDPs with offline datasets but some key details are unclear.
For example:
- The context information is included in the offline dataset. But when the agent is evaluated (run in the environment), is the context information available then?

- There does not seem to be any assumption on context information or any common structure relating the context to the MDP. So, since the MDP can be arbitrarily different between contexts, it's confusing that the bound given by equation (1) (line 335) does not contain a term related to the number of contexts or a related quantity. How would it be possible to generalize to other contexts without any underlying structure? 

- If the context variable is included in the dataset and we are only interested in Markovian policies, how is this different from augmenting the state with the context variables and using a standard offline RL algorithm? 


There are a few concerns about the empirical results and I have some questions in the next section.


I may be missing some important pieces of information concerning the above points and would be willing to revise my score based upon further clarification.

### questions:
 - Line 385: Why is $V^\pi_{i-1,1}(x_1)$ not achievable? What does this mean?

- The objective chosen is the "suboptimality gap compared to the best Markovian policy" (line 164). The best Markovian policy (without context) can be bad on every environment. When using history-dependent policies, it can be possible to infer the context and do much better. Based on this, it's unclear how meaningful the proposed objective is. Perhaps a worst-case bound over contexts would be a more satisfying choice. 
Alternatively, setting where the context variable is revealed in the offline dataset but hidden during evaluation would be interesting to consider. That is, we want to change the objective so that we compare to history-dependent policies. Some additional modifications may be needed so learning is feasible and is different from POMDPs.

- Line 257: The presence of an oracle for each individual dataset seems like a strong assumption. Could you elaborate on how one could implement the oracle and what kind of estimates would be feasiable for $\Gamma(s,a)$

- For the counterexample CMDP in section 4 (line 235), it seems unreasonable to expect the agent to do well on actions that are never observed ($\mu(a) = 0$). There would be no observed rewards for those actions so the agent has no information. Perhaps the counterexample should be adjusted to account for this and give some positive probability to all actions. 


- Looking at the table 3, the stochastic policy variant is better but this is not the result reported in table 2 (in the row for Miner) 
	In table 2, we see the deterministic policy result is reported which is markedly worse. 
	It would be more fair to report the stochastic policy variant in table 2. Currently, it seems like it is the difference between stochastic and deterministic policies that makes the largest difference and not the additional value networks.

- Is the stochastic policy suggested in this work or is it a variant from previous works?

- When running IQL-nV, there are more parameters and more capacity in the network. It would be more fair to compare to the 1V version which gets additional parameters to roughly match the ones of nV, n>1. 


- Methods making use of ensembles of value networks have indeed been used to combat value overestimation issues in various works e.g. [1] and [2]. Any thoughts on parallels between these lines of work and the current one? 


[1] "Randomized Ensembled Double Q-Learning: Learning Fast Without a Model" Chen et al. 
[2] "Maxmin Q-learning: Controlling the Estimation Bias of Q-learning" Lan et al.

Typos:
- In the algorithm boxes, at the end, should it say "Return" instead of "Ensure"? 

- line 122: "successive feature" -> "successor feature"

### Questions
- Line 385: Why is $V^\pi_{i-1,1}(x_1)$ not achievable? What does this mean?

- The objective chosen is the "suboptimality gap compared to the best Markovian policy" (line 164). The best Markovian policy (without context) can be bad on every environment. When using history-dependent policies, it can be possible to infer the context and do much better. Based on this, it's unclear how meaningful the proposed objective is. Perhaps a worst-case bound over contexts would be a more satisfying choice. \
Alternatively, setting where the context variable is revealed in the offline dataset but hidden during evaluation would be interesting to consider. That is, we want to change the objective so that we compare to history-dependent policies. Some additional modifications may be needed so learning is feasible and is different from POMDPs.

- Line 257: The presence of an oracle for each individual dataset seems like a strong assumption. Could you elaborate on how one could implement the oracle and what kind of estimates would be feasiable for $\Gamma(s,a)$

- For the counterexample CMDP in section 4 (line 235), it seems unreasonable to expect the agent to do well on actions that are never observed ($\mu(a) = 0$). There would be no observed rewards for those actions so the agent has no information. Perhaps the counterexample should be adjusted to account for this and give some positive probability to all actions. 


- Looking at the table 3, the stochastic policy variant is better but this is not the result reported in table 2 (in the row for Miner) 
	In table 2, we see the deterministic policy result is reported which is markedly worse. 
	It would be more fair to report the stochastic policy variant in table 2. Currently, it seems like it is the difference between stochastic and deterministic policies that makes the largest difference and not the additional value networks.

- Is the stochastic policy suggested in this work or is it a variant from previous works?

- When running IQL-nV, there are more parameters and more capacity in the network. It would be more fair to compare to the 1V version which gets additional parameters to roughly match the ones of nV, n>1. 


- Methods making use of ensembles of value networks have indeed been used to combat value overestimation issues in various works e.g. [1] and [2]. Any thoughts on parallels between these lines of work and the current one? 


[1] "Randomized Ensembled Double Q-Learning: Learning Fast Without a Model" Chen et al. \
[2] "Maxmin Q-learning: Controlling the Estimation Bias of Q-learning" Lan et al.

Typos:
- In the algorithm boxes, at the end, should it say "Return" instead of "Ensure"? 

- line 122: "successive feature" -> "successor feature"

### Soundness
3

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
This paper proposes Pessimistic Empirical Risk Minimization (PERM) and Pessimistic Proximal Policy Optimization(PPPO), which they leverage a pessimistic policy evaluation component, aiming to address ZSG by minimizing a "suboptimality gap," that combines supervised learning error (related to policy generalization) and reinforcement learning error (related to dataset coverage).

### Strengths
-  The paper provides theoretical bounds on the suboptimality of both PERM and PPPO. This theoretical rigor is a positive contribution to ZSG.
- The proposed algorithms consider multiple environments separately, potentially improving ZSG by better capturing variations across contexts.

### Weaknesses
 -  Applying a pessimistic bias to counteract distributional shifts can lead to over-conservative policies that might underperform, particularly in environments where high-risk, high-reward actions are necessary. This is a fundamental limitation, as the method may not be suitable for tasks requiring aggressive exploration or where optimal policies involve significant risk-taking.
- Pessimism may sometimes hinder the exploration of higher-reward policies due to its inherent cautious nature. This paper’s methods also assume that each environment's context information and datasets are either directly available or accurately inferable, which limits the use cases from random sampled or mixed quality datasets. Specifically, the requirement for accurate environment labels during training is a strong assumption that may not hold in many real-world scenarios where data is collected without precise context information. The method's reliance on these labels could limit its applicability to settings with noisy or incomplete environment information.
- The suboptimality bounds in the paper rely on having a large number of sufficiently varied environments. These bounds may be loose in situations with fewer or more similar environments, and the policy may perform poorly in unseen contexts. The theoretical analysis does not sufficiently address the sensitivity of the bounds to the diversity and number of environments, which is a critical factor for practical applications. It remains unclear how the method would perform in scenarios with limited environmental diversity.
 - Both PERM and PPPO involve parameters that adjust the degree of pessimism applied, where the sensitivity of them are not fully discussed. The lack of a clear methodology for tuning these parameters makes the method difficult to use in practice, as the optimal level of pessimism may vary significantly across different tasks and environments. This lack of guidance on parameter selection is a significant practical limitation.
- PERM requires maintaining separate models or critic functions for each environment in the training set, which can quickly become computationally expensive as the number of environments grows. PPPO, while model-free, still requires multiple policies for different environments, which limits scalability when working with diverse and high-dimensional data. The computational cost associated with maintaining multiple models or policies can be a significant barrier to the practical application of these methods, especially in complex environments.
- The selection of the baseline methods are not justified, why not compare the proposed methods with SOTA methods?

### Questions
please see weakness

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
3

### Summary
This paper studies zero-shot generalisation (ZSG) to unseen environment contexts in offline RL. The authors perform extensive theoretical analyses to establish why standard offline RL techniques perform poorly in this setting. They propose two idealised algorithms (PPPO and PERM) and provide bounds on the sub-optimality of these methods w.r.t. an optimal policy for ZSG. They conclude by providing a practical instantiation of their idealised algorithms based on IQL and evaluate its ZSG performance on procgen.

### Strengths
- The problem setting is an important, unexplored area. To the best of my knowledge, this is the first work that provides a theoretical analysis of zero-shot generalisation to unseen environments in offline RL.
- The authors' theoretical analysis is meticulous and extensive.
- The authors supplement their theoretical analysis with empirical results on the relevant benchmark provided by Mediretta et al. (2023)

### Weaknesses
 - Mediretta et al. (2023)'s work showed that behaviour cloning (BC) zero-shot generalised to unseen environments better than standard offline RL methods. The goal of this paper, in effect, is to establish the failure mode of offline RL methods in this setting and propose new methods that remedy it. However, the empirical findings in Table 2 and Figure 2 do not leave the reader confident that a solution has been found--BC's median performance is better than (or similar to) IQL-4V's on both the expert and mixed datasets. Presumably this can be explained with reference to the sub-optimality gap of PERM reported in Table 1, but the authors do not discuss this.
- I found the paper difficult to follow. The notation is dense, and in my opinion, overloaded (e.g. the definitions of state, and state-action value functions in Lines 150-153), which made following the analysis difficult. At times the English is poor, but I'm sensitive to the fact that it may not be the authors' first language. After several read-throughs, I'm left unsure what the key contribution is (there are many disparate contributions). If a practitioner wanted to build algorithms based on the theoretical results it is, in my opinion, not clear where they should begin. NB: this is not a value-judgement on the quality of the theoretical analysis, but it does affect how easily others can build upon the authors' findings.

**Minor feedback**
- In Line 19 you say that "our frameworks find the near-optimal policy with ZSG both theoretically and empirically". The findings in Section 6 suggest that you do not find the near-optimal policy in your empirical setting.
- Figure 2 is tricky to read, and lacks a y-axis label.
- Line 122: "successive feature" -> "successor features", and Touati et al. (2023) do study zero-shot generalisation in offline RL, but to unseen reward functions rather than unseen environments. Similar works that are not cited include [1,2]
- Section 3 should be titled "Preliminaries".
- In Line 91 you miss Section 2 from your discussion of the rest of the paper.
- When reporting empirical results I would recommend following the guidance of [3] and use IQMs, confidence intervals obtained via bootstrapping etc.
- Line 355: "becomes" -> "become".
- Line 360: remove "it".
- It would be helpful if the code to reproduce the experiments was linked/provided.

### Questions
- In practice, why does IQL-4V not outperform BC in Section 6? It would be helpful if you could discuss more thoroughly the limitations in translating the theoretical findings to practical application.
- As far as I understand, IQL-nV trains $n$ value functions, and $n$ policies (one w.r.t. each value function), but in practice $n$ is less than the number of test contexts. At test-time, how do you select which of the $n$ policies to use for an arbitrary unseen context?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors address the problem of zero-shot offline generalisation, where an algorithm is provided with a number of datasets from some source environments and aims to train a policy that performs as good as possible in a set of target environments from which it has never seen any data.

### Strengths
The authors propose a model-based (PERM) as well as a model-free algorithm (PPPO), which to the best of my knowledge are the first approaches to exhibit zero-shot generalisation capabilities with a proved bound on their suboptimality. They also provide empirical results on a number of environments & analyse why previous offline algorithms fail in the zero-shot generalisation setting without context. Personally, I believe this area to be crucially important for practical applications and believe it to deserve further investigation as it is so far underexplored, and I thus very much welcome the authors' work.

### Weaknesses
I have some questions about the empirical evaluation:
- could you provide uncertainty estimates also for mean & median performance? Currently it is hard to judge whether the mean improvement from e.g. BC to IQL-4V on expert is significant or not.
- generally, I am surprised that BC performs so well - not only on the expert datasets where it could be expected, but also on the mixed datasets. Do you have a theory about why that is the case? Overall BC seems to outperform the proposed method in terms of median & mean performance (except for mean on expert, but it is unclear whether that is significant). With that in mind, it is questionable whether in practice one would not rather use the much simpler, easier to interpret & implement BC method instead of the proposed solution. Generally, the authors don't comment much on BC in the corresponding section and I think this point needs some further discussion.
- if I am not mistaken, figure 2 shows the differences in performance between IQL baseline and the newly proposed approach (?). Please add that information in the caption, it currently only says difference, but not between what.
- furthermore, I understand that not much prior work in the offline zero-shot area exists, however as far as I understand (please correct if I am mistaken) your baseline IQL is overly simple, i.e. it treats all stages as belonging to the same MDP. An improvement over this behavior should be fairly simple when taking into account context information. I believe you could show the merits of your method in a much more convincing way of you chose a baseline that would do this - e.g. use a meta learning approach and don't allow it to fine-tune on the target task (meta learning does take into account context information but I would still expect your proposed method to outperform it)

### Questions
see weaknesses

### Soundness
3

### Presentation
2

### Contribution
3
