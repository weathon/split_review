# Finally Rank-Breaking Conquers MNL Bandits: Optimal and Efficient Algorithms for MNL Assortment

- Decision: Accept
- Avg Score: 5.75
- Scores: 6, 6, 6, 5

## Abstract
We address the problem of active online assortment optimization problem with preference feedback, which is a framework for modeling user choices and subsetwise utility maximization. The framework is useful in various real-world applications including ad placement, online retail, recommender systems, and fine-tuning language models, amongst many others. The problem, although has been studied in the past, lacks an intuitive and practical solution approach with simultaneously efficient algorithm and optimal regret guarantee. E.g., popularly used assortment selection algorithms often require the presence of a ``strong reference" which is always included in the choice sets, further they are also designed to offer the same assortments repeatedly until the reference item gets selected---all such requirements are quite unrealistic for practical applications. In this paper, we designed efficient algorithms for the problem of regret minimization in assortment selection with \emph{Plackett Luce} (PL) based user choices. We designed a novel concentration guarantee for estimating the score parameters of the PL model using `\emph{Pairwise Rank-Breaking}', which builds the foundation of our proposed algorithms. Moreover, our methods are practical, provably optimal, and devoid of the aforementioned limitations of the existing methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper revisits the Active Optimal Assortment (AOA) problem, and proposes two algorithms: $\mathrm{AOA-RB_{PL}}$ (Algorithm 1) and $\mathrm{AOA-RB_{PL}-Adaptive}$ (Section 4). Regret bounds have been established (Theorem 3, 4, 5) and preliminary experiment results have been demonstrated in Section 5.

### Strengths
- To the best of my knowledge, the proposed algorithms in this paper are novel, and they are based on some new insights like Rank-Breaking (proposed in Khetan & Oh (2016)) and Adaptive Pivot Selection (proposed in this paper).

- The analyses in this paper seem to be rigorous and highly non-trivial. I have not checked the analyses line by line, but the derived regret bounds make sense to me.

- The authors have done a good job of literature review and have well positioned this paper with respect to relevant literature.

### Weaknesses
 - The writing of this paper can be further improved. Section 3 and Section 4 are too technical and a little bit hard to read.

- All the experiments in this paper are synthetic. Might the authors add some experiment results based on real-world datasets?

- [typo] for Arith50 environment, $\theta_i = 1-(i-1) \times 0.2$ for $i \in [50]$. This seems to be a typo since $\theta_i$ can be negative.

### Questions
Please address the weaknesses above.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper revisits MNL bandit problems, and designs efficient algorithms for the problem of regret minimization in assortment selection. The authors propose a novel concentration guarantee for estimating the score parameters of the model using ‘Pairwise Rank-Breaking’, which builds the foundation of the proposed algorithm. The provided regret upper bound is quite comparable with state-of-the-art, with numerical simulations verifying their theoretical results.

### Strengths
* The paper proposed a new perspective to tackle the MNL bandit problem, which is interesting in the literature while sharing a quite comparable regret performance as Agrawal et al. 2019.

### Weaknesses
 * In Line 315, I'm not sure if a regret bound of $\tilde{O}(\sqrt{KT})$ is optimal in the proposed model setting, as the lower bound of stochastic bandit is known as $\Omega(\log T)$ from Lai & Robbins (1985) [1], while $\Omega(T^{1/2})$ is known as the regret lower bound of adversarial bandit setting. The provided bound seems to conflate these two scenarios, and it's unclear why a $\sqrt{T}$ dependence is justified in a stochastic setting. The authors should clarify the specific assumptions under which their regret bound is derived and why it deviates from the standard logarithmic bound for stochastic bandits.
* How does the regret result relate to the maximum of assortment size $m$? In extreme case where $m=1$, the problem reduces to a standard bandit problem with a "no choice" action. How to understand the impact of $m$ on the regret? It is not clear how the algorithm's performance scales with the number of items in each assortment, and whether there is a trade-off between the size of the assortment and the regret. The paper should provide a more detailed analysis of the impact of $m$ on the regret bound, especially in the context of the algorithm's exploration-exploitation strategy.

### Questions
* In Line 315, I'm not sure if a regret bound of $\tilde{O}(\sqrt{KT})$ is optimal in the proposed model setting, as the lower bound of stochastic bandit is known as $\Omega(\log T)$ from Lai & Robbins (1985) [1], while $\Omega(T^{1/2})$ is known as the regret lower bound of adversarial bandit setting.
* How does the regret result relate to the maximum of assortment size $m$? In extreme case where $m=1$, the problem reduces to a standard bandit problem with a "no choice" action. How to understand the impact of $m$ on the regret?

[1] https://core.ac.uk/download/pdf/82425825.pdf

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
5

### Summary
This paper considers the problem of online assortment optimization from bandit feedback. More specifically, they assume a setting where there are k arms or items (along with a special item corresponding to the no-selection option), each associated with an unknown quality, and the learner can select m items in each trial to present to the user. Feedback is received in the form of a single choice or selection from the presented set of arms, which is assumed to be drawn from the classical MNL model where the probability of an item selection is proportional to the underlying item quality. In this framework, they consider two main objectives: a top-m selection objective where the per-round regret is defined as the difference in the total quality of the set of m arms with the highest quality (optimal action in hindsight), and the set of arms presented to the user by the learner in that round, and a weighted top-m objective (revenue maximization), where each arm is additionally associated with a revenue, and the corresponding regret is the difference between the expected revenue of the set of arms with the highest expected revenue, and the expected revenue of the presented subset. This general problem is commonly studied in both the machine learning and operations research literature, but prior work has some notable limitations, such as assuming the arm corresponding to the no choice option has the highest weight/quality, and is present in every set of arms presented. This work resolves some of these deficiencies by proposing a relatively simple and intuitive algorithm based on rank breaking, which is a common idea explored in the past for breaking multiway comparisons into multiple pairwise comparisons to compute estimates of the qualities of the underlying items. The authors show that rank breaking is able to obtain sharp estimates of the underlying qualities, and as a consequence, are able to show that their approach theoretically obtains a regret bound that scales as roughly $O(\sqrt{T})$ for both settings - top-m and revenue maximization, and has improved dependence on certain parameters such as the quality of the best item. They corroborate the theory with experiments on synthetic data.

### Strengths
I think the paper is very well written. The exposition is clear, and the authors do a good job of placing their work relative to other related research. The claims are accompanied with technical proofs, which I have verified to be correct. The algorithm is also very intuitive, and simple enough to be used in practice.

### Weaknesses
Despite the strengths, I do not believe this result is very novel. While some of the limitations of existing works are legitimate, such as assuming that the no choice option has the highest weight, and removing this assumption is an important contribution, other points made, such as existing work requiring the same set to be probed multiple times to get a good estimate of the item qualities are not. Practically, you are not playing this online learning game with a single user, but rather a huge number of users, in which case it is perfectly reasonable to be able to display the same set multiple times. Moreover, there is value in repeatability and predictability: for example being shown the same set of options or at least a similar set of options every time a user queries something. For example, imagine a user is comparing between different offerings for a particular kind of product across different websites, and eventually deciding to pick one after comparing all their options. Now if they return to a website to select something they think to be best after comparing all their options, but the website shows them a completely different set of options this time around, it is reasonable to expect the user would get annoyed, since they would have to restart their comparison process all over again. Therefore, an argument can be made in either direction, and I don’t believe “not repeating options” is a strength. Moreover, the other limitation which you pointed out where some results require you to converge to the top arm being duplicated m times is not really a limitation. It is due to the notion of regret used in their work and not an algorithmic limitation. It is perfectly reasonable when your arms are really higher level categories, which can contain multiple different instances of that arm type instead of duplicates (e.g. an arm might be a particular brand or service provider, and the ‘m’ copies might be different offerings by the same brand or provider).

On a more technical front, I am fairly certain this result can be obtained via a combination of Accelerated Spectral Ranking (Agarwal et al, ICML 18), and the batching idea for bandits with limited adaptivity (Esfandiari et al, AAAI 21, Gao et al Neurips 19, Perchet et al, Annals of Statistics 16). Basically, break the set of items into subsets of size m each, and play these batches in epochs of geometrically increasing lengths, using the ASR algorithm to compute estimates of the item qualities at the end of each epoch. Since we can select which arms are in each subset, we can force a reference arm to be placed in all subsets (either no-choice arm if it has sufficiently high weight, or some other arm of your choice that has weight comparable to the highest weight arm). The estimation guarantees of ASR are in terms of TV norm, but due to the nature of that bound, you can simply use it as an L_\infty bound instead, and use it to eliminate arms that have a clear separation from the top m arms, and repeat this process with the surviving arms, doubling the epoch length in each round. I am fairly certain this will give essentially the same regret bound, if not a better one. I will try to work out the proof when I can find some time to verify my suspicion.

### Questions
Look at the last point in my weaknesses. To me, it seems like this problem should be solvable via known results in bandits + parameter estimation for MNL.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
In this paper, the authors addressed the problem of active online assortment optimization with preference feedback. The authors worked with a general AOA model where the no-choice item does not necessarily have the highest preference score. They then designed an algorithm using rank-breaking MNL-parameter estimation, and provided theoretical guarantees for their algorithm for both Top-m and Wtd-Top-m objectives. The authors also numerically evaluated the effectiveness of their algorithm.

### Strengths
Overall, the paper is well structured. The theoretical results appear sound and the authors provided detailed proof sketches. The authors have also provided a comprehensive overview of the existing literature and summarized their limitations.

### Weaknesses
1. I'm not sure what's the main motivation behind the model studied. In MNL bandits, the assumption of having a no-choice item with the highest preference score is usually well justified. For example, in an e-commerce setting where multiple items are present, the majority of the customers are simply browsing the pages before making the purchase. In what kind of applications would this new AOA model be helpful?
2. Following the point above, if the rank-breaking algorithm is applied to a setting where the no-choice item does dominate, how does the algorithm compare to MNL-bandits? It seems that MNL-bandit should achieve a better regret bound in that case, and from Fig 2. it seems that the performance is also somewhat similar. 
3. In terms of practicality, I am wondering if the authors could also comment on how the rank breaking algorithm can be applied in real-world settings. The authors suggest that the proposed model can be potentially helpful in "web search, language models, online shopping, recommender systems". I wonder if the authors can comment more on how the proposed model can assist these applications. Experiments on real-world data could also be helpful here, as only synthetic experiments have been conducted so far.

### Questions
See weaknesses.

### Soundness
3

### Presentation
2

### Contribution
2
