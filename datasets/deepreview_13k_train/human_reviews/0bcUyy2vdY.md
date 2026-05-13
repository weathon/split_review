# Multi-play Multi-armed Bandit Model with Scarce Sharable Arm Capacities

- Decision: Reject
- Scores: 6, 8, 5, 3

## Abstract
This paper revisits multi-play multi-armed bandit with shareable arm capacities problem (MP-MAB-SAC), for the purpose of 
revealing fundamental insights on the statistical limits and data efficient learning. The MP-MAB-SAC is tailored for resource allocation problems arising from LLM inference serving, edge intelligence, etc. It consists of $K$ arms and each arm $k$ is associated with an unknown but deterministic capacity $m_k$ and per-unit capacity reward with mean $\mu_k$ and $\sigma$ sub-Gaussian noise.  The aggregate reward mean of an arm scales linearly with the number of plays assigned to it until the number of plays hit the capacity limit $m_k$, and then the aggregate reward mean is fixed to $m_k \mu_k$. At each round only the aggregate reward is revealed to the learner. 
Our contributions are three folds.   1) \textit{Sample complexity:} we prove a minmax lower bound for the sample complexity of learning the arm capacity  $\Omega(\frac{\sigma^2}{\mu^2_k} \log \delta^{-1})$, and propose an algorithm to exactly match this lower bound. 
This result closes the sample complexity gap of Wang et al. (2022a), whose lower and upper bounds are $\Omega(\log \delta^{-1})$ and  $O (\frac{m^2_k \sigma^2}{\mu^2_k} \log \delta^{-1})$ respectively.  2) \textit{Regret lower bounds:}  we prove an instance-independent regret lower bound   $\Omega( \sigma \sqrt{TK} )$  and instance-dependent regret lower bound $\Omega(\sum_{k=1}^K\frac{c\sigma^2}{\mu_k^2} \log T)$.  This result provides the first instance-independent regret lower bound and strengths the instance-dependent regret lower bound of Wang et al. (2022a) $\Omega(\sum_{k=1}^K \log T)$.   3) \textit{Data efficient exploration:}we propose an algorithm named \texttt{PC-CapUL}, in which we use prioritized coordination of arm capacities upper/lower confidence bound (UCB/LCB) to efficiently balance the exploration vs. exploitation trade-off.  We prove both instance-dependent and instance-independent upper bounds for \texttt{PC-CapUL}, which match the lower bounds up to some acceptable model-dependent factors. This result provides the first instance-independent upper bound, and has the same dependency on $m_k$ and $\mu_k$ as Wang et al. (2022a) with respect to instance-dependent upper bound.But there is less information about arm capacity in our aggregate reward setting.  Numerical experiments validate the data efficiency of \texttt{PC-CapUL}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper revisits multi-play multi-armed bandit with shareable arm capacities problem. Improved on previous work Wang et al. (2022a), the paper proposes refined lower and upper bounds for both sample complexity and regret. For sample complexity, the authors propose a minmax lower bound, and give an algorithm that matches the bound. For regret, the authors provide both instance dependent and instance independent regret lower bounds, and find algorithms that match the bounds up to some model-dependent factors.

### Strengths
1. The work closes the sample complexity gap and narrow the regret gap for the MP-MAB problem. Although the techniques used in the proof are not particularly unique (mostly based on regular UCB and LCB), the conclusions are still very interesting and make sense.
2. The work propose numerical simulation to show the advantages of their algorithms.

### Weaknesses
1. The writing is a bit poor. The paper contains many colloquial expressions, i.e., line 383 "But if", line 390, 403, 405 "And furthermore" "And this". The lack of precise language detracts from the technical rigor of the paper. For example, the use of "But if" to start a sentence is generally discouraged in formal writing, and phrases like "And furthermore" and "And this" are often redundant and can be replaced with more concise alternatives. These instances, while seemingly minor, accumulate to create a less professional tone.
2. The author states in the introduction that the algorithm has applications to LLM inference serving. I believe it’s necessary to provide some LLM-related experiments to support this statement. The connection between the proposed algorithm and LLM inference serving is not clearly demonstrated. While the problem formulation might conceptually align with resource allocation in LLM serving, the paper lacks empirical evidence to validate this claim. Without specific experiments or simulations involving LLM workloads, the application to LLM inference serving remains speculative.
3. should we assume that $\mu_k\ge c$ for all $k$? The authors state that the optimal action is always $(m_1,\dots, m_K)$ in line 211. It seems that this only holds when $\mu_k\ge c$ for all $k$. This assumption is not explicitly stated, and its absence creates ambiguity in the problem formulation. It's crucial to clarify whether the per-unit reward of each arm is assumed to be greater than or equal to the cost of using the arm. The optimal action stated in line 211 only holds under this condition, and without this assumption, the analysis and conclusions may not be valid.
4. what is \mu in Theorem 1. I did not find the definition. The lack of a clear definition for \mu in Theorem 1 is a significant oversight. The symbol \mu is used without prior definition, making it difficult to understand the theorem's statement and implications. This lack of clarity undermines the rigor of the theoretical analysis. It's essential to define all symbols and notations before they are used in theorems and proofs.
5. I am curious about how could the sample complexity in Theorem 2 gets rid of the dependence of N. Intuitively, even there is no noise (sigma = 0), for any algorithm, it still need at least $\log N$ rounds to find the true $m_k$ by binary search. Is the dependence on $N$ hidden in $\xi$? The intuition that at least $\log N$ rounds are needed to find the true $m_k$ even without noise is valid. The absence of $N$ in the sample complexity of Theorem 2 is counterintuitive. It's important to clarify how the algorithm achieves this independence from $N$, especially given that the search space for $m_k$ is implicitly bounded by $N$. The dependence on $N$ may be hidden in $\xi$, but this needs to be explicitly stated and justified.

### Questions
1. should we assume that $\mu_k\ge c$ for all $k$? The authors state that the optimal action is always $(m_1,\dots, m_K)$ in line 211. It seems that this only holds when $\mu_k\ge c$ for all $k$.
2. what is \mu in Theorem 1. I did not find the definition.
3. I am curious about how could the sample complexity in Theorem 2 gets rid of the dependence of N. Intuitively, even there is no noise (sigma = 0), for any algorithm, it still need at least $\log N$ rounds to find the true $m_k$ by binary search. Is the dependence on $N$ hidden in $\xi$?


Typos:
line 224: $a_{k,t}$ instead of $a_k$
line 289: for large probability -> with high probability
line 383: to played with -> to play with

### Soundness
3

### Presentation
1

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper studies the multi play multi-armed bandit problem having shared arm capacity where the in each round, the learner gets to select the arm for a number of pulls capped by the capacity limit with the goal of maximizing the total reward at the end of the play. The authors propose a new reward function and develop a new algorithm PC-CapUL for this problem setting. The developed algorithm provides tighter bounds on sample complexity and regret in comparison to the existing works, efficiently balances exploration and exploitation. The work is applicable in resource allocation problem with capacity constraint scenarios such as LLM inference and many other real world scenarios.

### Strengths
•	The problem of Multi play multi-armed bandit problem is an interesting setting to study and improve the foundation of it as it pertains to main real-world settings including LLM inference serving. The work re-establishes that with emphasis on theoretical guarantees.

•	The work provides theoretical improvements in sample complexity compared to the existing work on  MP-MAB-SAC. It tends to close the sample complexity gap found in the previous work in Reference A

•	The authors also provide a new Improved algorithm, PC-CapUL that performs much better than other existing algorithms and have a solid theoretical backing to it with proved theoretical Regret bound guarantees.

•	The experiments cover the regimes where the number of arms is larger which predominantly requires more exploration to take place. The developed algorithm provides much better performance in terms of regret compared to other existing algorithms in this experimental setting.

Reference:
 [A] Xuchuang Wang, Hong Xie, and John C. S. Lui. Multiple-play stochastic bandits with shareable finite-capacity arms. International Conference on Machine Learning, ICML 2022.

### Weaknesses
•	The experimentation design could have been done much better with the inclusion of better baseline comparison in addition to the algorithm found in Reference A . Also, utilizing a real-world dataset for evaluation would have further complemented these theoretical results.

•	The readability of the paper could be much improved. Also, a brief intuitive explanation like a proof sketch could be added in the main text to help the reader get the intuitive logic and understanding of the proof techniques. 

•	A more detailed theoretical comparative analysis like how regret fares against the regret of other algorithms would make the argument much stronger for the developed PC-CapUL algorithm. Moreover, having such a discussion would also help us uncover insights like how the regret bound behaves in different regimes.

### Questions
1.	$m_k$ is deterministic and well known beforehand as to how many pulls can be made in a round. However, there is a constant movement cost $c$ associated to an arm. In case of LLM query, the number of pulls is associated to the amount of query a server instance can handle.

Are $m_k$ and moving cost $c$ dependent in this scenario? If so, how do this implication sit with all the theoretical proof, or do they have to be independent? A clarification on this would help the readers utilize the developed algorithms on many scenarios where the dependencies are crucial. 

2.	Why is ordering of plays of arm selection important in $a_t$, providing some details on it will avoid ambiguity around its objective of whether to maximize the resource utilization or to maximum capacity of the arm?

3.	Also, with respect to movement cost, in the experiment setting, it has been assigned to an arbitrary value of 0.1 .  Is there any fundamental reason for that? Also, how can they be evaluated in a practical scenario when they are also coupled with reward formulation? Adding some details around them can greatly improve the clarity of the work.  

4.	It would be nice to see how the experiments scale up with varying parameters like changing the $m_k$ and changing the movement cost etc ? This will help us understand the empirical performance of the algorithm much better.

Reference:
 [A] Xuchuang Wang, Hong Xie, and John C. S. Lui. Multiple-play stochastic bandits with shareable finite-capacity arms. International Conference on Machine Learning, ICML 2022.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper considers the problem of multi-play multi-armed bandits with scarce shareable arm capacities. Specifically, different from [Wang et al., 2022a], this paper considers the problem where $N\geq \sum_k m_k$ where $m_k$ is the capacity of action $k$. With a modification on the reward function, this paper proposes new sample complexity lower/upper bound that is tight as well as regret lower/upper bound for this problem. Specifically, the author claims that the sample complexity lower bound proven in this paper improves upon the one shown in [Wang et al., 2022a]. Empirical results are also shown to strengthen their theoretical findings.

### Strengths
- This paper first considers this problem with scarce shareable arm capacities and proposes both lower and upper bound for both sample complexity and the regret bound.
- Based on the parts that I checked, the proofs look correct to me.
- The experiments are also conducted to show superior performance compared to the previous work.

### Weaknesses
 - One main concern is the motivation of this paper to consider the case where $N\geq \sum m_k$. In this case, the problem seems to be easier (in the sense of algorithm design) since you will definitely explore each action sufficiently enough to figure out the exact $m_k$ while in the opposite case $N< \sum m_k$, the problem seems to be harder since you need to decide the exploration amount for the suboptimal $k$. Can the authors explicitly justify the choice of studying the $N\geq \sum m_k$ case and why it is challenging compared to the previous case?
- This also leads to the question about the comparison between the lower/upper bound shown in this paper and [Wang et al., 2022a]. While the authors claim better lower bound, I wonder whether the upper/lower bound are comparable in these two cases? Can the algorithm that is derived in this setting adapted to the other? Moreover, I am not sure why equation (5) is more reasonable since it makes sense to me to have the noise's variance larger when $m_k$ or $a_k$ is large.
- As for the upper bound, the bounds in Theorem 5 seems to be suboptimal since it seems to be dependent on $\frac{\max_i \mu_i}{\min_i \mu_i}$, which can be large.
- I do not understand the lower bound argument shown in Theorem 4. When the cost $c=0$, then this ratio becomes 0, which is surely not informative. In addition, why is the ratio independent of $m_k$? Can the authors explain more on this?
- Typos:
  - Line 223: it -> if
  - Line 224: a_k -> a_{t,k}?
  - Line 471: depended -> dependent 
  - Line 751: missing lemma reference.
  - missing periods at the end of many theorem statements (e.g. Theorem 4,5,6..)

### Questions
See "Weakness" Section for questions.

- I wonder whether the dependency on the cost parameter $c$ can be improved for the regret lower bound.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper discusses the problem of the Multi-play Multi-armed Bandit Model with Shareable Arm Capacities (MP-MAB-SAC). It tightens the lower bounds for both sample complexity and the cumulative regret compared to the previous work. Besides, this paper proposes corresponding algorithms to match the lower bounds. Finally, the numerical experiments show that the proposed algorithms outperform the existing ones.

### Strengths
The theoretical contributions are nontrivial. This paper shows tighter lower bounds, and then proposes new algorithms to match them. Furthermore, the experiments verified the theories.

### Weaknesses
I have the following concerns:

1. The writing quality of this paper falls below the standards required for publication in ICLR. Issues such as clarity, rigor, and basic grammatical correctness are prevalent. It appears that the authors did not thoroughly review the paper before submission. From a writing perspective, the paper remains in draft form: numerous typos, confusing notations, and grammatical errors hinder readability. For example,  (1) in Lemma 2, $\epsilon^{uE}$ should be $\epsilon^{UE}$; (2) in the proof of Lemma 2 “Bourel et al., 2020” is even not cited; (3) in the proof of Theorem 1, which lemma is used here? Besides, this theorem should be proved more formally; (4) What is the first baseline “MP-MAB-SA” in the experiments?

2. The explanations provided in the paper are insufficient. (1) In Section 1, more concrete examples of the model's practical applications are needed. (2) The claim that certain changes in settings make the model more suitable for LLMs requires stronger evidence. For instance, the movement cost $c$ (which is known to the learner) seems irrelevant. (3) The paper should provide a more in-depth analysis of the experimental results, going beyond mere statements of fact.

3. The comparison with the previous work seems not fair. (1) Since $N \ge M$ makes the learner only need to learn the capacity $m_k$, without needing to learn the rank of the arms, the learning task seems easier. (2) In lines 307~310, is there any evidence to show stability is getting better? Besides, I’m kind of confused about this result because the robustness v.s. regret usually has some trade-off, which means the increasing of stability may (not always) lead to the decreasing of performance.

### Questions
Please try to solve the problems in weaknesses. In addition, since the improvement in results achieved in this paper mainly comes from the careful selection of UCB, I would like to know what kind of inspiration it will bring to future work? This is not necessary as the theoretical improvement itself is interesting.

### Soundness
3

### Presentation
2

### Contribution
3
