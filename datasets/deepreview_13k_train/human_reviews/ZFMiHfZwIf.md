# Skill or Luck? Return Decomposition via Advantage Functions

- Decision: Accept
- Scores: 6, 8, 5, 6

## Abstract
Learning from off-policy data is essential for sample-efficient reinforcement learning.
    In the present work, we build on the insight that the advantage function can be understood as the causal effect of an action on the return, and show that this allows us to decompose the return of a trajectory into parts caused by the agent's actions (skill) and parts outside of the agent's control (luck).
    Furthermore, this decomposition enables us to naturally extend Direct Advantage Estimation (DAE) to off-policy settings (Off-policy DAE).
    The resulting method can learn from off-policy trajectories without relying on importance sampling techniques or truncating off-policy actions.
    We draw connections between Off-policy DAE and previous methods to demonstrate how it can speed up learning and when the proposed off-policy corrections are important.
    Finally, we use the MinAtar environments to illustrate how ignoring off-policy corrections can lead to suboptimal policy optimization performance.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper extends Direct Advantage Estimation (DAE), an algorithm designed to improve credit assignment by directly learning the advantage function. The original DAE formulation was limited to the on-policy case and this paper derives an off-policy version. This new algorithm is shown to be beneficial in a toy example and with experiments on the MinAtar environments.

### Strengths
- The decomposition of the return in terms of advantages of both the agent and the environment's "actions" is very intriguing and novel. It also leads to a practical algortihm, which could potentially outperform the standard approaches to learning advantage functions, a crucial part of actor-critic algorithms.

- The paper is well-written and this makes the derivation much easier to follow.
- The toy environments are well-designed to demonstrate the differences between the different approaches, DAE vs. off-policy DAE.
- There's some nice insights into why the uncorrected off-policy n-step return may work well in practice due to certain environmental properties.

### Weaknesses
 - The larger-scale experiments are fairly limited with MinAtar being the most complex domain. Other environments, particularly those with higher dimensional state and action spaces, could be considered to better demonstrate the scalability of the proposed method. The current experiments do not fully explore the method's potential in more challenging scenarios.
- Other baselines could be more appropriate for the MinAtar experiment. Tree Backup, while sharing some similarities with the proposed method, is not a state-of-the-art off-policy algorithm. Comparing against more established methods, such as Retrace or other off-policy actor-critic algorithms, would provide a more rigorous evaluation of the method's performance.
- Off-policy DAE requires an additional neural network to estimate the transition distribution, which introduces a model-learning component to an otherwise model-free approach. This reliance on a learned transition model could be a limitation, especially in complex environments where accurate model learning is difficult. Furthermore, the requirement of summing over all discrete latent states seems restrictive and could hinder scalability to environments with large state spaces.

### Questions
- Off-policy DAE requires an additional neural network to estimate the transition distribution. This seems slightly unelegant since actor-critic algorithms are usually model-free. Is it possible to avoid this by converting the constraint into a loss function instead? i.e. optimize the Lagrangian of the constraint with SGD? Perhaps we would have to use an approximate loss here to make it tractable. 

- If we do learn a model to estimate $B_\pi$, is it possible to adapt the algorithm so the model is sampled-based only? Requiring a sum over all discrete latent states seems a bit restrictive in the choice of model and it seems to prevent easy scaling of the model size.

- Could you clarify how equation (10) reduces to the policy improvement lemma? In particular, what happens to the $B^\pi_t$ term? 

- Why was Tree Backup chosen as the baseline? It seems like a less popular or effective choice compared to, say, Retrace [1] or its successors. 

- It could be interesting to try to incorporate off-policy DAE with model-based RL methods since those algorithms would already have a learned model to use. E.g. Dreamer-v3

Minor point:
- To improve the clarity of the notation, I would suggest using capital letters for the random variables. In certain places, the lowercase letters are used to denote both fixed values and random ones. E.g. below equation (7), in the definition of $B^\pi_t$, $s_{t+1}$ in the expectation should be uppercase.


[1] "Safe and efficient off-policy reinforcement learning" Munos et al.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents Off-policy DAE, a framework for off-policy learning that decomposes returns into two components: 1. those controllable by agents (skills) and 2. those beyond an agent's control (luck). Specifically, "luck" refers to stochastic transitions that the agent can't control. By explicitly modeling the advantage attributed to this luck factor, the agent can more effectively discern the impact of its own actions, leading to quicker generalization through enhanced credit assignment. Evaluations conducted on 5 MinAtar environments demonstrate improvements over baselines, particularly in scenarios with stochastic transitions.

### Strengths
S1: This offers a methodical approach to incorporate the effects of non-controllable factors, leading to enhanced credit assignment in off-policy learning. It's a novel concept, one I haven't encountered in other papers.

S2: The paper is very well-written and straightforward. I'm especially impressed by the intuitive examples provided to make the reader understand the main concept.

S3: Experiments are conducted on a standard benchmark suite using 20 random seeds. The results are notable, demonstrating that in stochastic environments, the agent performs better compared to methods not leveraging the proposed advantage function decomposition.

### Weaknesses
The paper is largely well-composed, with the proposed idea articulately presented. While I couldn't pinpoint any specific areas needing improvement,

W1: Conducting experiments in more domains might bolster the paper's claims even further.

### Questions
Q1: Can the method be directly applied to offline RL, and if so, what additional challenges might arise in that context?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposed a new return decomposition method via advantage functions, which contains the average return, the skill term, and the luck term.

### Strengths
The formulations of the paper are quite clear and easy to follow. Although I didn't get the main idea of the paper through the text, the formulations are quite clear for me to follow.





Generally, I think the paper contributes to giving some insight into the decomposition of the return.

### Weaknesses
Although I can get the main ideas from the formulations of the paper, the writing of the paper is poor.

- The introduction is not quite clear. Although it starts with an intuitive example, it doesn't contribute too much to get the idea of the paper.
- Section 3 lacks motivation, making it kind of hard to follow.


The experimental results are not very convincing.

- For Figure 9, Table 2, Figure 10, 11, 12, are the results in deterministic environments? Are there any results in stochastic environments?  I believe this is very important as the evaluation in stochastic environments is the main contribution of the paper.
- The authors used very large $N$ (8) for Uncorrected. However, in existing literature, it's known 3 or 5 are the best. Therefore, the comparison is unfair.
- What's the performance of 1-step DQN? 
- The paper doesn't compare to other state-of-the-art multi-step off-policy method, such as Retrace($\lambda$) [1].

The below claim is exaggerated. I didn't find a theorem that clearly proves the properties of faster convergence.

> We demonstrate that (Off-policy) DAE can be seen as generalizations of Monte-Carlo (MC) methods that utilize sample trajectories more efficiently to achieve faster convergence.



Minor comments:

- Near eq.7: The second term $E{[V^\pi(s_{t+1})|s_t,a_t]}$. What are the random variables of expectation? If it's $s_{t+1}$, please use another notation to differentiate it from the existing one using $s_{t+1}$.
- The complexity of the method seems very large (15 hours vs. 2 hours, as stated in D.7)

### Questions
- Why the decomposition of the return could benefit learning? Could the author give more insights into it?
- What's the probability of the sticky action for stochastic environments?

### Soundness
3 good

### Presentation
1 poor

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The proposes to decompose the advantage function into two parts: 1) return due to the agent's action selection and 2) return due to transition dynamics of the environment. They then use this decomposition to extend an existing algorithm DAE to the off-policy setting.

### Strengths
1. The proposed decomposition is straightforward, and I think is a useful idea to spark newer ideas.
2. The toy examples and Section 4 is useful.

### Weaknesses
1. It is not clear to me why off-policy corrections are not necessary given that the sequence of rewards was generated by a different policy; it feels like frequency at which the sequences appear must be corrected for. Specifically, if the behavior policy explores a different region of the state-action space, the learned advantage function might be biased towards the behavior policy's distribution, and it's unclear how the proposed method avoids this.
2. Related to above, it appears that the only "off-policyness" in Eqn 5 is the $\pi$-centered constraint. Why is this sufficient for the off-policy correction? It seems that the method relies on the assumption that the learned advantage and transition components are independent of the behavior policy, which is not necessarily true in practice. The constraint alone does not seem to address the distributional shift between the behavior and target policies.
3. The decomposition seems related to exogenous and endogenous stochasticity. Is there a way to phrase the current work in that context? I'd also refer the authors to this paper that seems relevant: https://people.csail.mit.edu/hongzi/var-website/content/iclr-19.pdf
4. I am curious if once the advantage function is decomposed into skill and luck, is there a benefit to weighing each component differently? I would suspect that this leads to some bias in the policy ordering, but I am wonder if say the skill related component is too small, it may get overshadowed by the luck component, and the agent may not learn efficiently. For instance, if the transition dynamics are highly stochastic, the 'luck' component might dominate, making it difficult to discern the impact of the agent's actions.
5. Related to above, I am curious how off-policy DAE performs as a function of environment stochasticity. Specifically, how does the performance vary when the transition probabilities become more or less deterministic? It would be useful to see a systematic study of this effect.
6. In Figure 3 and 4, it is unclear to me why all methods are able to produce similar mean estimates? Of course each is different in terms of their variance, but all are centered around the same mean which is a bit surprising. This suggests that while the variance differs, the bias might be similar across methods, and it would be helpful to understand why.
7. What were the number of trials for the Figure 5 results? These should be mentioned.

### Questions
1. It is not clear to me why off-policy corrections are not necessary given that the sequence of rewards was generated by a different policy; it feels like frequency at which the sequences appear must be corrected for.
2. Related to above, it appears that the only "off-policyness" in Eqn 5 is the $\pi$-centered constraint. Why is this sufficient for the off-policy correction?
3. The decomposition seems related to exogenous and endogenous stochasticity. Is there a way to phrase the current work in that context? I'd also refer the authors to this paper that seems relevant: https://people.csail.mit.edu/hongzi/var-website/content/iclr-19.pdf
4. I am curious if once the advantage function is decomposed into skill and luck, is there a benefit to weighing each component differently? I would suspect that this leads to some bias in the policy ordering, but I am wonder if say the skill related component is too small, it may get overshadowed by the luck component, and the agent may not learn efficiently.
5. Related to above, I am curious how off-policy DAE performs as a function of environment stochasticity. 
6. In Figure 3 and 4, it is unclear to me why all methods are able to produce similar mean estimates? Of course each is different in terms of their variance, but all are centered around the same mean which is a bit surprising.
7. What were the number of trials for the Figure 5 results? These should be mentioned.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
