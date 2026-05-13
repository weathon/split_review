# Demonstration-Regularized RL

- Decision: Accept
- Scores: 6, 8, 6, 6

## Abstract
Incorporating expert demonstrations has empirically helped to improve the sample efficiency of reinforcement learning (RL). This paper quantifies theoretically to what extent this extra information reduces RL's sample complexity. In particular, we study the demonstration-regularized reinforcement learning that leverages the expert demonstrations by $\KL$-regularization for a policy learned by behavior cloning. Our findings reveal that using $\Nexp$ expert demonstrations enables the identification of an optimal policy at a sample complexity of order {\small$\tcO(\mathrm{Poly}(S,A,H)/(\epsilon^2 \Nexp))$} in finite and {\small$\tcO(\mathrm{Poly}(d,H)/(\epsilon^2 \Nexp))$} in linear Markov decision processes, where $\epsilon$ is the target precision, $H$ the horizon, $A$ the number of action, $S$ the number of states in the finite case and $d$ the dimension of the feature space in the linear case. As a by-product, we provide tight convergence guarantees for the behavior cloning procedure under general assumptions on the policy classes. Additionally, we establish that demonstration-regularized methods are provably efficient for reinforcement learning from human feedback (RLHF). In this respect, we provide theoretical evidence showing the benefits of KL-regularization for RLHF  in tabular and linear MDPs. 
Interestingly, we avoid pessimism injection by employing computationally feasible regularization to handle reward estimation uncertainty, thus setting our approach apart from the prior works.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose KL-regularized online RL algorithms and provide an upper bound on the sample complexity of this algorithm in tabular MDP and linear MDP settings.

### Strengths
The authors provide a thorough analysis of the algorithms, to justify the efficiency of the RL algorithms with access to an expert dataset.

### Weaknesses
1. There is limited discussion on the relationship between the pure online learning version of LSVI-UCB and UCBVI+. Specifically, the paper does not clearly articulate the differences in their exploration strategies, how the KL-regularization impacts their performance, and under what conditions one might be preferred over the other. A more detailed comparison, including a discussion of their respective advantages and disadvantages in different scenarios, would greatly benefit the reader.
2. The paper can be better organized, there are too many references pointing towards the appendix. This makes it difficult to follow the main line of argument and to assess the significance of the results. Key definitions, proofs, and intermediate results should be more accessible within the main body of the paper to improve readability and flow.

### Questions
I am not an expert in RL theory, I am a bit confused by the results presented in Corollary3 and Theorem6, where the bound presented in Corollary3 depends on $N^E$, whereas the bound in Theorem6 does not. Intuitively, I suppose the sample complexity would eventually depend on the size of the expert dataset. Can authors explain this?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper studied demonstration-regularized reinforcement learning (RL), where the learner first performs behavioral cloning on expert-generated demonstrations using maximum likelihood estimation. Then during the online interaction with the underlying environment, the learner penalizes deviation of the learned policy from the one learned in the behavioral cloning phase. The paper provided a theoretical analysis of these two phases. For behavioral cloning, the authors show that the KL divergence between the learned policy and the expert policy decreases linearly as the number of demonstrations grows. This holds for both tabular MDPs and linear MDPs under certain assumptions. Then based on this result, the authors further studied the regularized online learning scenario and the RLHF setting. In both cases, the authors are able to prove a fast convergence rate for the proposed algorithms.

### Strengths
(1) The paper performed a strong and solid theoretical study of behavioral cloning for both tabular and linear MDPs. The authors proved that the KL-divergence between the learner policy and the expert policy decreases linearly as the number of demonstrations grows. The authors also complemented the above positive results with a lower bound on the convergence rate. In terms of the dependency on the number of demonstrates, the upper bound and lower bound match. This is a nice and great result. Based on that, the authors further performed analysis on their proposed demonstration-regularized RL algorithms and the RLHF algorithms, and both achieved surprisingly fast convergence rates. Overall, the paper has made significant technical contributions.

(2) The paper studied a very novel, interesting, yet challenging problem. The topic is of particular interest to the theoretical RL community, and I can forsee that the results of this paper significantly push the frontiers of RL theory and will drive more research along this line.

### Weaknesses
(1) It would be great to include some empirical studies, although this is purely a theory paper.

### Questions
(1) Can you provide some empirical results to validate the theoretical findings of this paper?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies demonstration-regularized RL where an agent is supposed to find a near optimal policy given an offline dataset that is collected from an expert policy. The paper theoretically shows that given $N^E$ expert samples, the sample complexity of finding a $\epsilon$-optimal policy reduces by a factor of $1/N^E$ in both tabular and linear MDPs. Moreover, the paper extends the proposed method to RLHF and theoretically justify the efficiency of it.

### Strengths
1. The paper provides comprehensive theoretical results on various settings in demonstration-regularized RL.
2. The results are nice and show a strong benefit using expert demonstrations.

### Weaknesses
1. I prefer that there is a separated "related works" section such that the presentation is clear.
2. The contributions from the algorithm design part seem not significant. The algorithm is a combination of imitation learning and regularized RL.
3. The results highly depends on the performance of the expert policy. However, in real life applications, obtaining expert demonstrations is usually expensive, and there might be far less offline demonstrations that that considered in this paper. Specifically, from Corollary 3, it seems that the benefit occurs when $N^E>H^3SA$, which is close to the typical sample complexity in standard RL, which might be too much in real applications.

### Questions
While the paper provides the lower bound for the imitation learning, is there any lower bound for the regularized RL?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies two new hybrid setting which are novel/uncommon in the literature: (i) demonstration regularized RL and (ii) Demonstration Regularized RLHF.

In (i) both expert demonstrations from an $\epsilon$-optimal policy and online access to an MDP with reward function are possible. In (ii) the reward function is not available but it can be inferred thanks to a Preference Based Model introduced in Assumption 4.

### Strengths
Both the newly introduced settings are interesting and matches practical situations.

### Weaknesses
There are several technical weaknesses in my opinion.

The main weakness is in my opinion that the setting seems 

1) The lower bound in Theorem 2 turns unfortunately vacuous in the limit of $\gamma \rightarrow 0$.

2) It is unclear why the class of linear policies at the third line of Section 3.2 is considered to be not learnable. In fact, under this choice [1] proves in their Theorem 5 that it is possible to recover an $\epsilon$-suboptimal policy compared to the expert with behavioural cloning.

3) Corollary 3 requires the expert to be $\mathcal{O}(\epsilon)$ optimal but I would expect that, given the reward knowledge, it should be possible to prove a sample complexity bound without the assumption on the $\mathcal{O}(\epsilon)$ optimality of the expert.
To see this think to the case of any BPI algorithm which requires no expert at all to learn an $\epsilon$-optimal policy.

4) I think that Lemma 11 should be referred as the standard performance difference lemma.

5) Just before Corollary 3, it is said  that "UCBVI-Ent+ algorithm for regularized BPI. It is a modification of the algorithm UCBVI-Ent by
Tiapkin et al. (2023) with improvement sample complexity". However, it is not explained which is the crucial difference between the two algorithms. In particular, also the settings are different because UCBVI-Ent+ uses reward information while UCBVI-Ent can be used only for maximum entropy exploration and not to solve Regularized MDPs but this difference is not explained in the main text.

### Questions
Q1) Is it possible to prove a bound which does not require the assumption that the expert is $\epsilon$ optimal ?

Q2) Why the regularization is needed in the tabular case but not in the linear one ? I am referring to Section 3.2

Q3) How can UCBVI-Ent+ achieve $\mathcal{O}(\epsilon^{-1})$ sample complexity according to Theorem 5 while UCBVI-Ent achieves a worst sample complexity of $\mathcal{O}(\epsilon^{-2})$ ?

Q4) What are the definitions of $\pi^{t,(h)}$ and $\tilde{\pi}^t$ in Algorithm 3?

Q5) In the setting of Demonstration Regularized RLHF is it necessary to have the coefficients defined in equation 3 in the bound ?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
