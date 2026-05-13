# Communication-Efficient Algorithm for Asynchronous Multi-Agent Bandits

- Decision: Reject
- Scores: 6, 5, 5, 6

## Abstract
We study the cooperative asynchronous multi-agent multi-armed bandits problem, where the active (arm pulling) decision rounds of each agent are asynchronous. In each round, only a subset of agents is active to pull arms, and this subset is unknown and time-varying. We propose a fully distributed algorithm that relies on novel asynchronous communication protocols. This algorithm attains near-optimal regret with constant (time-independent) communications for adversarial asynchronicity among agents. Furthermore, to protect the privacy of the learning process, we extend our algorithms to achieve local differential privacy with rigorous guarantees. Lastly, we report numerical simulations of our new asynchronous algorithms with other known baselines.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the authors study the cooperative asynchronous multi-agent multi-armed bandits problem, where the active agents in each round are unknown in advance. The authors propose a new algorithm with Accuracy Adaptive Communication (AAC) protocol that achieves near-optimal regret and requires communication rounds that are independent of time. The proposed approach is shown to be superior in terms of communication rounds through synthetic data.

### Strengths
* The paper is well-written, easy to follow, and well-organized.
* Compared to previous work [1], the authors propose a novel and superior Successive Elimination (SE) algorithm with Accuracy Adaptive Communication (AAC) protocol. The proposed algorithm achieves constant communication rounds, which are independent of time complexity. This is a significant advantage for real-world applications.
* The proposed algorithm is easy to implement and has the potential to be applied to a wide range of real-world applications.
* Synthetic data experiments show that the proposed algorithm outperforms existing algorithms in terms of communication rounds.

[1] Yu-Zhen Janice Chen, Lin Yang, Xuchuang Wang, Xutong Liu, Mohammad Hajiesmaili, John C.S.
Lui, and Don Towsley. On-demand communication for asynchronous multi-agent bandits. In
International Conference on Artificial Intelligence and Statistics, pp. 3903–3930. PMLR, 2023.

### Weaknesses
 * The proposed algorithm is not validated with real-world data.
* The authors do not provide a lower bound for the number of communication rounds required, which makes it difficult to assess the performance of the proposed algorithm.

### Questions
Typos:

1.1 Success Elimination -> Successive Elimination

### Soundness
2 fair

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies cooperative asynchronous MABs, such that the arm pulls are asynchronous across the agents. The authors proposed a fully distributed algorithm (called SE-AAC-ODC) which achieves near-optimal regret with the number of communications independent of the time horizon. Furthermore, the algorithms are modified to achieve local differential privacy along with rigorous guarantees. Numerical simulations are also presented to compare the performance of their algorithm with the other known baselines.

### Strengths
Originality
------------------------------------------------------------------------------------------------------------
- N/A
_______________________________________________________________________
Quality
--------------------------------------------------------------------------------------------------------------
- Analysis seems to be correct
__________________________________________________________________________
Clarity
---------------------------------------------------------------------------------------------------------------
- Algorithm and analysis are clearly explained
- The paper is well-written for the most part (minor concerns are mentioned in the Questions)
________________________________________________________________________________
Significance
---------------------------------------------------------------------------------------------------------------
- The multi-agent asynchronous MAB considered in this paper is motivated by real-world applications (covered in detail in the Introduction) and could be of interest to the researchers studying multi-agent bandits

### Weaknesses
 - **Lack of originality:** The algorithm and the analysis are extensions of known works in (Yang et. al. 2023) and (Chen et. al. 2023)

- **Missing details in numerical simulations:** The algorithm AAE-ODC from (Chen et. al. 2023) uses a buffer threshold for messages communicated among the agents. There is no mention of the values of the buffer threshold used in AAE-ODC for the experiments presented in the paper
________________________________________________________________________________________
**Potentially misleading claim about the communication cost of the SE-AAC-ODC:**
---------------------------------------------------------------------------------------------------------------------------------------------------
The authors claim that the communication cost of SE-AAC-ODC, which scales as $O(KM\log \Delta^{-1})$ is much smaller than that of (Chen et. al. 2023), in which the communication cost scales as $O(KM^2 \Delta^{-2}\log T)$ as claimed in this paper. However, the authors haven't mentioned all the details from (Chen et. al. 2023). Recall from the previous bullet that the algorithms in (Chen et. al. 2023) use buffer thresholds.
- The communication cost scaling as $O(KM^2 \Delta^{-2}\log T)$ of the AAE-ODC algorithm in (Chen et. al. 2023) only holds when the buffer thresholds are constant with respect to the number of communications (ref: Corollary 1, part (b) in (Chen et. al. 2023)).
- However, if the buffer thresholds are exponential with respect to the number of communications, the communication cost of the AAE-ODC algorithm in (Chen et. al. 2023) scales as $O\big(M^2 \log \frac{K \log T}{\Delta^2}\big)$ (ref: Corollary 2, part (b) in (Chen et. al. 2023)).

I claim that when $K$ is very large (and $K > M$), the communication cost of the AAE-ODC algorithm in (Chen et. al. 2023) with the exponential buffer threshold is smaller than that of the communication cost of SE-AAC-ODC in this paper, unless the time horizon $T$ scales doubly exponentially in $K$. It can be quickly noticed by taking the ratio of the communication costs $\frac{M^2 \log \frac{K \log T}{\Delta^2}}{KM\log \frac{1}{\Delta}} = \frac{M \log \frac{K \log T}{\Delta^2}}{K\log \frac{1}{\Delta}}$, which is less than some small constant (ignoring other constants in the $O$ notation) for $T=O(\exp (K^{-1}\exp(K)))$ (assuming natural logarithm). This makes the constant communication cost of SE-AAC-ODC algorithm in this paper vacuous.

- The preceding discussion also puts the validity of the numerical experiments into question.

### Questions
- I encourage the authors to address the concerns in the Weaknesses section, in particular about the numerical results and misleading claim about the communication cost.
- Can the authors also provide a lower bound on the communication cost of the asynchronous multi-agent MAB model considered in this paper?

Minor Comments
----------------------------------------------------------------------------------------------------------------------
- In the Introduction, the authors have used $\mathbb{N}^{+}$ for the set of natural numbers. The $+$ in the superscript is redundant, as natural numbers are positive by definition.
- In the Related Work (Section 1.2), (Chawla et. al. 2020) considers gossip-style communication scheme as well, which isn't mentioned.
- In the definition of the confidence radius in eq (1), Section 3.2.1, shouldn't it be $\min (1, \sqrt{\frac{2 \log T}{n}})$?
- In Remark 10, the bound $\frac{e^{\epsilon}+1}{e^{\epsilon}-1} \leq 1 + \frac{1}{\epsilon}$ is incorrect. To check this, set $\epsilon = 1$ and notice that the left hand side $> 2$ and the right hand side $= 2$. The correct bound is $\frac{e^{\epsilon}+1}{e^{\epsilon}-1} \leq 1 + \frac{2}{\epsilon}$. It can be proved by noticing that $\frac{e^{\epsilon}+1}{e^{\epsilon}-1} - 1 = \frac{2}{e^{\epsilon}-1} \leq \frac{2}{\epsilon}$, since $e^{\epsilon}-1 \geq \epsilon$.
________________________________________________________________________________________________________
After detailed discussions with the authors, I have increased my score from 3 to 5.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a distributed asynchronous method for solving the multi-agent multi-armed bandit (MA2B) problem. The authors also extend their algorithms and results to preserve privacy. The main contribution of this paper is the design of the event-trigger-based asynchronous method to achieve higher communication efficiency. Both the theoretical and numerical results demonstrated the higher communication efficiency.

### Strengths
The paper is well written and easy to read. The idea of algorithm design is quite reasonable and sounds promising. They use the idea of "event trigger", namely, a node communicates only when it has enough new information to share. They also quantify the amount of information by something called "confidence radius". They also theoretically and numerically justify their main motivation: lower communication complexity. Their theoretical results show that their algorithm possesses the property of "constant communication", which is attractive to the reviewer.

### Weaknesses
1. Although the order of the regret bound of the proposed algorithm (see Remark 3) is the same as the optimal bound, the constant term before the order can be quite large. For example, when setting $\alpha=6$ as used in the experiments, the constant can be as large as 392, which is a very large number. This large constant significantly impacts the practical performance, especially in scenarios with smaller time horizons. It would be beneficial to see a more detailed analysis of how this constant affects the actual regret, perhaps by comparing the theoretical regret bound with empirical results for different values of T. I suggest the authors provide the regret bound (not only the order) of alternative methods and compare them. It will also be better to plot the regret bounds and the communication complexity bounds of the proposed method and alternative methods.

2. Can the authors clarify what is indeed the most important measurement (time or communication) in the MA2B task? The authors explained that synchronous updates will lead to redundant communication (Section 3.1). This is reasonable, but what is the final purpose of saving communication? Is it to achieve a lower regret within a shorter time horizon? If time is the most important thing, then by Figure 1,2, the performance of the proposed method is not as good as UCB-IBC. The current presentation does not clearly articulate the practical scenarios where communication efficiency is more critical than minimizing regret, and this needs to be better justified.

3. I can see that from Theorem 2, a smaller alpha yields smaller regret. I can also see that from Figure 1,2, the proposed method has a higher regret compared to UCB-IBC. Therefore, I'm interested in the question of when we use smaller $\alpha$ to achieve similar regret as UCB-IBC, will the number of communications of the proposed method still be much smaller? It's unclear how the trade-off between regret and communication, controlled by $\alpha$, plays out in practice, and whether the communication savings are still significant when trying to match the regret performance of UCB-IBC.

### Questions
I'm quite interested in the property of constant communication. By Theorem 2, the authors show that the regret bound is closely related to T, but the number of communications is independent of T. This means that communication between agents is not so important and even if there are only a few communications, smaller $R(T)/T$ can still be achieved by using a large T. Can the authors intuitively explain the philosophy behind this property?

I'm not familiar with this topic, but if the authors can clarify my concerns, then I'm willing to improve my score.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors study the cooperative asynchronous multi-agent multi-armed bandit problem:
- the agents are allowed to communicate for handling the same Bernoulli multi-armed problem, 
- at each time step a subset of agents, which is chosen in advance by an adversary, can play the arms.
The authors designed a new communication protocol: an agent communicates if its new local observations enough reduce the estimation of the global confidence bound of the considered arm. The proposed bandit algorithm is based on Successive Elimination of suboptimal arms. The algorithm is analyzed and then tested versus the state-of-the-art.

### Strengths
The main claim of the paper is to handle cooperative asynchronous multi-agent multi-armed bandits with a constant communication cost, while guarantying a rate optimal regret upper bound.
This study is interesting, notably the fact that agents asynchronously play, which has a significant applicative potential. The constant communication cost can be easily obtained by an explore-then-exploit approach (Hillel et al 2013), but not with an optimal rate regret upper bound. So, it is an interesting result.

### Weaknesses
The paper has some weaknesses:
        - Objective function: the authors wrote that the expectation in the expected regret (actually, the pseudo regret) is taken over the randomness of the algorithm and reward realizations. However, the reviewer did not find where there is randomness in Algorithm 1. So, there is no expectation in the second line of the pseudo regret R(T).

        - Algorithm 1: the reviewer does not understand what lines 21-24 mean.
        - Communication cost: the reviewer is wondering why agents send an elimination message to other agents (line 7), while agents also send their estimates line 15. 
        - Number of agents: in the experiments, the number of agents is lower than the number of arms. 
        - Proof of Lemma 1: equation (a1), M_t is not defined and misleading.
        - Proof of Theorem 2, step 3: the reviewer does not understand where the last equation page 17 comes from. Could you provide more details?
        - Model: the authors assume that there is only on best arm (\mu_1 > \mu_2 \geq …). This is a strong assumption that limits the scope of this study.

### Questions
See above

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
