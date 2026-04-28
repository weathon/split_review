# DOPL: Direct Online Preference Learning for Restless Bandits with Preference Feedback

- Decision: Accept
- Avg Score: 5.75
- Scores: 5, 6, 6, 6

## Abstract
Restless multi-armed bandits (RMAB) has been widely used to model constrained sequential decision making problems, where the state of each restless arm evolves according to a Markov chain and each state transition generates a scalar reward. However, the success of RMAB crucially relies on the availability and quality of reward signals. Unfortunately, specifying an exact reward function in practice can be challenging and even infeasible. In this paper, we introduce \RMABPF,  a new RMAB model in the presence of \textit{preference} signals, where the decision maker only observes pairwise preference feedback rather than scalar reward from the activated arms at each decision epoch. Preference feedback, however, arguably contains less information than the scalar reward, which makes \RMABPF seemingly more difficult. To address this challenge, we present a direct online preference learning (\DOPL) algorithm for \RMABPF to efficiently explore the unknown environments, adaptively collect preference data in an online manner, and directly leverage the preference feedback for decision-makings. We prove that \DOPL yields a sublinear regret. To our best knowledge, this is the first algorithm to ensure $\tilde{\mathcal{O}}(\sqrt{T\ln T})$ regret for RMAB with preference feedback. Experimental results further demonstrate the effectiveness of \DOPL.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This work studies a new problem set-up, PREF-RMAB.
For me, the problem set-up is very incremental. It is quite similar to duelling bandits. The proposed set-up is more like duelling bandits with state transitions. 

The writing needs to be improved. 

The writing for the intro is too wordy. I wish to see more literature work discussions.

I suggest putting the main theorem (Theorem 1) earlier. I can only see the theoretical result at Page 8. So, the structures for sections 4 and 5 are suggested to re-arrange. 

A minor thing: usually, RL or bandit theory works use $\delta$ to be the failure probability. The greek letter $\epsilon$ is for something else, like the error rate.

I went through the proofs and some steps are novel, not that typical in bandit/RL literature. But I did not check the correctness of the proofs.

### Strengths
see the first box

### Weaknesses
This work studies a new problem set-up, PREF-RMAB.
For me, the problem set-up is very incremental. It is quite similar to duelling bandits. The proposed set-up is more like duelling bandits with state transitions.

The writing needs to be improved.

The writing for the intro is too wordy. I wish to see more literature work discussions.

I suggest putting the main theorem (Theorem 1) earlier. I can only see the theoretical result at Page 8. So, the structures for sections 4 and 5 are suggested to re-arrange.

A minor thing: usually, RL or bandit theory works use $\delta$ to be the failure probability. The greek letter $\epsilon$ is for something else, like the error rate.

I went through the proofs and some steps are novel, not that typical in bandit/RL literature. But I did not check the correctness of the proofs.

### Questions
see the first box

### Soundness
2

### Presentation
2

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
The paper studies the Restless Multi-Armed Bandits with preference feedback named PREF-RMAB. The authors propose the Direct Online Preference Learning (DOPL) algorithm achieving an $\tilde{O}(\sqrt{T \ln T})$ regret, which is the first to give the theoretical regret upper bound for PREF-RMAB. Moreover, the paper presents numerical experiments which further validate the efficacy of DOPL against various baselines.

### Strengths
1.	The paper successfully integrates preference feedback within the RMAB framework, a novel approach that shifts away from traditional scalar reward dependency. Moreover, the presented algorithm DOPL achieves $\tilde{O}(\sqrt{T \ln T})$ regret with theoretical analysis.
2.	The relaxed LP-based direct index policy of DOPL is also given to tackle the limitations of computational intractability.
3.	The writing is clean and easy to follow.

### Weaknesses
1.	Estimating the whole preference matrix $F$ in DOPL algorithm requires large computational cost. Moreover, it would be beneficial to involve a thorough discussion on computational complexity of DOPL.
2.	In experiments, the existing algorithms like MLE_WIBQL, MLE_LP fail to achieve sublinear regret. A detailed discussion on why these algorithms underperform in achieving sublinear regret would provide valuable insights.

### Questions
1.	Estimating the whole preference matrix $F$ in DOPL algorithm requires large computational cost. Moreover, it would be beneficial to involve a thorough discussion on computational complexity of DOPL.
2.	In experiments, the existing algorithms like MLE_WIBQL, MLE_LP fail to achieve sublinear regret. A detailed discussion on why these algorithms underperform in achieving sublinear regret would provide valuable insights.

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes the PREF-RMAB model, which observes only the preference between two arms rather than the exact reward of each arm in the restless multi-armed bandit problem. By expressing the reward function of any arm n  in any state as the sum of a reference reward and a function related to the preference probability between arm n in state s and a reference arm in a reference state, the authors develop a direct index policy based on preference data to choose which arms to activate in the online manner. They establish an O (√(NT|S|ln⁡〖(|S||A|NT)〗 )) regret bound for the proposed algorithm.

### Strengths
1. Although RLHF has recently gained significant attention due to its applications in large language models and robotics, this work is the first to consider a preference-based reward model in the restless bandit problem, opening the door for RLHF to be applied much more broadly.

2. By establishing a connection between pairwise preferences and reward values, the authors transform the reward value of each arm and state into a measure based on the preference probability between this state and a reference arm and state, which is intriguing. Additionally, the algorithm can infer the preference between the element j in the preference matrix \(\mathbf{F}\) and the reference elements \(s_*\) without directly comparing them, but rather through an intermediate comparator. This clever design reduces the complexity to that of directly observing the reward.

### Weaknesses
•	1. A question remains as to whether a preference-based model can outperform direct reward estimation, and whether we really need the preference-base model in RMAB problem. In the first two examples presented in the paper, APP MARKETING and CPAP TREATMENT, while reward data is challenging to estimate accurately and may contain substantial noise, it can still be estimated in some form. Conversely, since preference data inherently provides less information, it is unclear whether incorporating preference data can improve performance over direct reward estimation. Most papers on RLHF use preference feedback to shape the reward for different trajectories in robotics or large language models (LLMs), where trajectory rewards are inherently complex and require function approximation methods to estimate the reward function. However, the RMAB model studied in this paper is a tabular MDP, where rewards can be estimated through multiple sampling.

•	2. In Algorithm 3 of Section C.3, at each step \( h \), the algorithm performs \( (B-1) \) random duels to obtain the preference data. Then, when constructing the preference between \(s_n\) and the reference \(s_*\), only the preference between \(s_n\) and \( j \) and \(s_*\) is used. It appears that \( s_n \) could be compared with many other columns \( i \) in the \( F \) matrix, but the algorithm does not leverage this data. Consequently, Algorithm 3 makes inefficient use of the available information. Specifically, after selecting \( B \) arms at each step, the duels are conducted randomly, resulting in many comparison data points beyond \( j \) that are not used in the inference process. This raises concerns about whether the preference data between \( s_n \) and other states \( i \) is wasted at each step \( k \).

•	3. The MDP considered in the paper is essentially a tabular MDP, and the regret scales with the square root of \( |S| \) (the size of the state space), which may be inefficient for large state spaces.

### Questions
•	1. In the 11th step of Algorithm 3 in Section C.3, when inferring \(\hat{\mathbf{F}}_n^{*,k+1,\text{inf}}(\sigma_{s_n}, \sigma_{s_*})\), only one intermediate column \( j \) in \(\mathbf{F}\) is selected to compute \(\hat{\mathbf{F}}_n^{*,k+1,\text{inf}}(\sigma_{s_n}, \sigma_{s_*})\) based on \(\hat{\mathbf{F}}_n^{*,k}(\sigma_{s_n}, j)\) and \(\hat{\mathbf{F}}_n^{*,k}(j, ((*-1)|S|+\sigma_{s_*}))\). However, after selecting \( B \) arms at each step, the duels are conducted randomly, resulting in many comparison data points beyond \( j \) that are not used in the inference process. Could this lead to substantial unutilized information? Could more comparison data, beyond just \( j \), be leveraged to infer the preference between \( s_n \) and \( s_* \)? Alternatively, rather than performing duels randomly, might strategically choosing duel pairs improve performance?

•	2. In Eq. (3), the authors define \(\pi^{opt}\) as the solution of (1) with scalar rewards, but the footnote states that the regret is with respect to preference feedback, which seems contradictory. This part is unclear to me.

•	3. In Eq. (46), the suboptimality is accumulated over \( K \) episodes. However, since \( \omega^k_n \) is a probability measure and \( Q_n(s) \) represents the relative reward of arm \( n \) in state \( s \), which involves the reward incurred at a specific step \( h \) within episode \( k \), why doesn’t \( h \) appear in this decomposition?

•	4. In Lemma 6, the authors use Lemma 11 to argue that term0 is negative. However, I find this reasoning unclear, as \({\pi^*}\) does not appear to align with \(\tilde{\pi}\) as defined in Lemma 6. Specifically, \(\mu_{\pi^*}\) represents the optimal solution of Eq. (6)-(9), while \(\tilde{\pi}\) is the index policy developed from \(\mu_{\pi^*}\) to satisfy the hard constraint. Therefore, I am uncertain that Lemma 11 can indeed be used to prove Lemma 6, and concluding that term0 is negative is not straightforward.

•	5. In the proof procedure following Eq. (49), from the fourth to the fifth line, the inequality \(\sum_{k=1}^K\sqrt{\frac{1}{Z^k_n(s,a)}} \leq \sqrt{Z^K_n(s,a)}\) appears incorrect. For instance, if the algorithm visits arm \( a \) at state \( s \) once at the beginning and never revisits this state, it would hold that \( Z^1_n(s,a) = \dots = Z^K_n(s,a) = 1 \), yielding \(\sum_{k=1}^K\sqrt{\frac{1}{Z^k_n(s,a)}} = K\), which is indeed greater than \( \sqrt{Z^K_n(s,a)} = 1\). If I have misunderstood this part, please clarify.

•	6. In the sentence between lines 1398 and 1399, I think the statement \(\sum_{n=1}^N\sum_{(s,a)}Z^T_n(s,a) \leq NT\) should instead be \(\sum_{n=1}^N\sum_{(s,a)}Z^T_n(s,a) = T\), as the total visits across all arms and states should sum to \(T\). In fact, only under this revised statement can the inequality (c) above this sentence be satisfied, otherwise it should be \(\sum_{n=1}^N\sqrt{\sum_{(s,a)}Z_n^K(s,a)}\leq N\sqrt{T}\). This confusion also appears in the sentence from 1503 to 1505. If I have misunderstood this part, please clarify.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper studies the restless multi-armed bandit (RMAB) problem with preference feedback (PREF-RMAB) rather than direct reward estimation, motivated by real-world applications like app marketing and CPAP treatment. To address the problem that some arms in some states may not be visited frequently, the authors propose a new method to infer the empirical average of arm preference via the other arms’ empirical preference estimations. Additionally, the authors transform the original reward-based optimization problem into another one in terms of preference feedback directly. Using this transformation, the authors develop a low-complexity index policy for decision making. They also provide theoretical analysis of the regret bound, establishing a regret bound of $\tilde{\mathcal{O}}(\sqrt{T\ln T})$. Finally, the authors conduct experiments to verify the performance of their proposed DOPL algorithm.

### Strengths
1.	The authors present novel approaches to address the PREF-RMAB problem. The results in Lemmas 4 and 5 are particularly interesting and have the potential to inform future algorithmic design.
2.	The propose DOPL algorithm works well on the PREF-RMAB problem.
3.	I understand that analyzing the regret bound of the RMAB problem with preference feedback is challenging, so the inclusion of this theoretical bound is commendable.

### Weaknesses
1.	Although the authors make a strong effort to illustrate potential real-world applications of the PREF-RMAB problem, the justification remains unconvincing. For instance, in the app marketing scenario, users’ state transitions do not satisfy the memoryless Markov chain property, as a user currently in state $s_4$  cannot directly transition to $s_1$, and time tracking is ambiguous. Similar concerns apply to the other examples.
2.	The writing can be further improved. For example, 

    (a) Adding more detail on the composition of the preference matrix $\mathbf{F}$ would improve clarity.

    (b) Eq. (2) needs to be improved, as the notation is confusing. 

    (c) The objective function (6) is not easy to follow. Please define $\mu^{\pi}$ and $\mu_n$ first. I misunderstood it as a myopic problem until I saw the definition of mu^pi. 

    (d) I think Lemmas 4 and 5 are more important than Lemmas 1 and 2. The authors can change them into propositions. 

    (e) Lemma 2 can be improved by defining $Q_n(s)$ first and then present the result in Lemma 2.

3.	The important results Lemmas 4 and 5 are based on Lemma 1. However, it is unclear why there is only a single reference arm * and a single reference state in Lemma 1. In the RMAB setting, DM selects B arms at each time slot, so the use of a single reference arm seems inconsistent.
4.	In Eq. (4), if $\epsilon=o(1)$, the confidence width becomes arbitrarily large. While if $\epsilon=\Theta(1)$, the probability becomes very small. How do the authors balance this trade-off? A more detailed discussion of the setting for $\epsilon$ would be helpful.

### Questions
1.	The important results Lemmas 4 and 5 are based on Lemma 1. However, it is unclear why there is only a single reference arm * and a single reference state in Lemma 1. In the RMAB setting, DM selects B arms at each time slot, so the use of a single reference arm seems inconsistent.
2.	In Eq. (4), if $\epsilon=o(1)$, the confidence width becomes arbitrarily large. While if $\epsilon=\Theta(1)$, the probability becomes very small. How do the authors balance this trade-off? A more detailed discussion of the setting for $\epsilon$ would be helpful.

### Soundness
3

### Presentation
2

### Contribution
3
