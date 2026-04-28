# Private Learning Fast and Slow: Two Algorithms for Prediction with Expert Advice Under Local Differential Privacy

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 3, 5, 6

## Abstract
We study the classic problem of prediction with expert advice under the constraint of differential privacy (DP). In contrast to earlier work in this area, we are interested in distributed settings with no trusted central curator. In this context, we first show that a classical online learning algorithm naturally satisfies DP and then design two new algorithms that extend and improve it: (1) RW-AdaBatch, which provides a novel form of privacy amplification at negligible utility cost, and (2) RW-Meta, which improves utility on non-adversarial data with zero privacy cost. Our theoretical analysis is supported by an empirical evaluation using real-world data reported by hospitals during the COVID-19 pandemic. RW-Meta outperforms the classical baseline at predicting which hospitals will report a high density of COVID-19 cases by a factor of more than 2$\times$ at realistic privacy levels.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces two algorithms, RW-AdaBatch and RW-Meta, for prediction with expert advice under the constraints of local differential privacy (LDP). The primary objective is to enable prediction in the LDP setting. RW-AdaBatch is designed for static environments and enhances privacy by adaptively batching data points, while RW-Meta uses meta-learning to improve predictions in dynamic environments. The paper validates these algorithms through theoretical analysis and empirical testing on COVID-19 hospitalization data, showing significant improvements in prediction accuracy under realistic privacy constraints.

### Strengths
- The paper is well-motivated, addressing a practical and novel problem. It introduces a classical method for solving privacy-preserving problems and proposes variations to address specific challenges.
- The writing is clear and well-structured.
- Both algorithms achieve near-optimal regret bounds (as claimed) and are supported by detailed privacy analyses.
- The experiment improvements seems significant.

### Weaknesses
 - Can the authors provide specific cases where prediction with expert advice under LDP would be essential?
- The computational cost of RW-AdaBatch and RW-Meta appears substantial due to their batched nature and eigen value operation, potentially limiting scalability to very large datasets. Additionally, the datasets used are moderate in size. Can the authors provide a complexity analysis for computation and memory?
- I am not deeply familiar with prediction with expert advice, so a direct comparison of the regret achieved by these algorithms and previously established ones would be helpful. The bounds claimed to be near-optimal seem to compare with non-private lower bounds that do not involve any privacy parameters ($\varepsilon$, $\delta$, $\mu$). Can the authors comment on that? What are some LDP related lower bounds?

### Questions
- How to tune the hyperparameter $B$?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
The paper considers online learning under local differential privacy (LDP), focusing more specifically on prediction with expert advice under full information setting in the oblivious adversary model. The authors propose 2 LDP algorithms and one that works with centralised DP, and analyze the utility and privacy of the proposed methods. The authors empirically test the proposed LDP methods on a real data example.

### Strengths
i) While the paper continues a well-established line of research on DP continual learning, it focuses on the LDP setting, which has fewer contributions.

ii) The writing is generally good, although there are some major caveats as described in rest of this review.

iv) Relaxing the assumption of having a trusted central party can be important.

### Weaknesses
i) The paper completely brushes over many details of the problem and of the proposed solutions, which makes it unacceptably cumbersome and error prone to read. For example, while the stated focus of the paper is a distributed setting with LDP, this is not easy to notice from the writing: the proposed algorithms and definitions do not explicitly mention any separate parties, nor communication steps or clearly state which party does what. This generally makes it bothersome to try and check how the proposed algorithms actually fit into the stated setting. The description of the distributed setting lacks a clear threat model, and the specifics of how the algorithms operate within this setting are often vague. For instance, the interaction between clients and the server is not precisely defined, making it difficult to understand the flow of information and computation. The paper would benefit from a more rigorous definition of the distributed environment, including the capabilities and limitations of each party involved.

ii) Some of the claimed contributions seem inaccurate and somewhat overstated (see Questions below for details).

iii) The paper omits some empirical comparisons to existing baselines (see Questions below for details)

### Questions
### Update after discussion

I still recommend rejecting the paper as it currently stand: as I have mentioned in the comments, especially after the edits, the paper feels very unfinished to the point of being hard to understand. I therefore cannot recommend accepting the paper, as I am unsure if I have understood the presented work correctly based on the writing. I have lowered my confidence to better reflect this uncertainty.

### Comments before discussion

Questions and comments in decreasing order of importance:

1) Especially Sec2: currently, it is unnecessarily hard to try and figure out some basic assumptions you use. Please explicitly define what are neighbouring distributions and which neighbourhood relation you use, i.e., what do you actually try to protect with DP.
2) On the adaptive batching and resulting privacy: based on the abstract and stated contributions, I find it very surprising that the batching does not actually give any amplification in the LDP setting. Please rewrite the related sections to make this clearer from the beginning.
3) Related to the previous comment, as the adaptive batching algorithm assumes a trusted central party, its empirical performance should be compared to the existing methods that assume the same setting, e.g., Asi et al. 2023 (cited in the current paper).
4) Please explicitly consider your chosen setting when formulating the algorithms and the discussion.
5) As per the [note on arXiv](https://arxiv.org/abs/1802.02638), Ullman 2018 citen in the current paper has been withdrawn by the author. Please check the reference and update to the new version as instructed by the author.
6) Lines 313-14: why is $<x_{t,i}, \tilde g_{t}>$ unbiased estimate? Do you assume something specific on the learners?


## Minor comments etc. (no need to comment or acknowledge)

* Please fix typos: lines 121-22 extra dot after Jain et al.
* Lines 192-93: mention what is $G_{t-1}$ .
* Lines 308-09: should be learner $i$, not each learner?
* Alg 2 seems to be missing $\tilde g_0$.
* Lines 86-87: I would not understand what LDP means from this definition.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper studies the problem of distributed online prediction with expert advice under local DP constraints. They propose two algorithms RW-AdaBatch and RW-Meta. The paper provides a theoretical analysis of the proposed algorithms. Additionally, the paper provides experimental results using real-world data.

### Strengths
1. The paper is well-written. The background and related previous work are clearly explained. The algorithms (RW-AdaBatch and RW-Meta) are described in detail. 


2. The paper includes experiments on real-world data from the COVID-19 pandemic.

### Weaknesses
1. The distributed setting is not fully explained. It is unclear how multiple players cooperate together in this distributed setting. Can they share their observations with others? Is there any communication between them?


2. Recent work on differentially private prediction with expert advice includes results for both pure $\varepsilon$-DP and approximate $(\varepsilon,\delta)$-DP [1,2], which are also cited in this paper. However, this paper only provides privacy guarantees for approximate DP. Can RW-AdaBatch or RW-Meta be extended to pure DP as well? If not, could you elaborate on the challenges involved?


[1] Asi, Hilal, et al. "Private online prediction from experts: Separations and faster rates." The Thirty Sixth Annual Conference on Learning Theory. PMLR, 2023.

[2] Asi, Hilal, et al. "Near-optimal algorithms for private online optimization in the realizable regime." International Conference on Machine Learning. PMLR, 2023.


3. The paper states, *"recent work has shown that very private algorithms can be forced to incur $O(T)$ regret by adaptive adversaries (Asi et al., 2023b). We therefore focus exclusively on oblivious adversaries in this work."* This statement is somewhat misleading and may benefit from clarification. Asi et al. (2023b) show linear regret for the pure DP case, while it is still possible to achieve sub-linear regret for approximate DP.


4. The paper does not provide a regret lower bound for the problem.

### Questions
How should noise scale $\eta$ be set to ensure that RW-AdaBatch or RW-Meta is $(\varepsilon,\delta)$-DP?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper addresses the problem of prediction with expert advice under local differential privacy, proposing two algorithms based on the classical "Prediction by random-walk perturbations" algorithm: (1) RW-AdaBatch, which enhances privacy by batching incoming data; and (2) RW-Meta, which adapts to data shifts by selecting from multiple candidate learners. The authors provide both theoretical analysis and empirical evaluation, demonstrating the advantages of the proposed algorithms.

### Strengths
1. Online prediction with expert advice is a fundamental problem in online learning. The investigation of this problem under local privacy constraints is crucial in both theory and practice due to the sensitive nature of machine learning tasks.
2. The authors substantiate their claims with rigorous theoretical analysis and empirical evaluation, demonstrating the high performance of the proposed algorithms.

### Weaknesses
1. The absence of a main theorem (like Theorem 2 in [1]) summarizing the regret of the proposed algorithms (in terms of $\varepsilon, \delta, n$ and $T$) limits the reader's ability to digest the results and identify the contributions effectively. While the paper presents several lemmas and corollaries, a single, comprehensive theorem that clearly articulates the final regret bound for both RW-AdaBatch and RW-Meta would significantly enhance the paper's clarity and impact. Specifically, it is difficult to quickly grasp the interplay between the privacy parameters, the number of experts, and the time horizon on the final regret without such a theorem.
2. The paper lacks a comparison with existing private online learning algorithms. Though they are not designed for the setting considered here, a comparative analysis with existing private online learning algorithms, particularly those using central differential privacy, could provide valuable insights into the privacy-utility tradeoff. It would be beneficial to see how the proposed local differential privacy approach compares to central differential privacy in terms of regret, especially given the potential for increased noise and reduced utility in the local setting. A discussion of the additional costs incurred when transitioning from central to local differential privacy is needed.
3. It seems the proposed algorithms only improve the privacy/utility by a small constant factor, which may not be significant. While the authors claim a constant factor improvement in privacy for RW-AdaBatch, the practical significance of this improvement needs to be further substantiated. For RW-Meta, although the empirical results show improvement over RW-FTPL, the theoretical analysis does not clearly demonstrate a substantial gain in terms of regret bounds. The improvements should be more clearly quantified and compared to the theoretical limits of what is achievable in the local differential privacy setting.

### Questions
1. It was stated that the regret of RW-Meta in (3) is with respect to the best learner in the candidates (line 355). Could you clarify whether the regret is with respect to the gain of the best learner on non-noisy data (i.e., $g_1,\dots, g_T$) or on noisy data (i.e., $\tilde{g}_1,\dots,\tilde{g}_T$)? 
2. The goal of RW-Meta is to choose a learner and follow its action at each time step. It seems this can be done by running RW-FTPL over the set of learners. Why not just run RW-FTPL over the set of learners?
3. Why did you compare RW-Meta to RW-FTPL in Table 1? I think it would be better to compare RW-Meta to the Linear Models instead of RW-FTPL. As shown in Figure 2, Linear Models outperform RW-FTPL a lot for all $\mu$'s. The performance of RW-Meta should largely rely on these Linear Models. Thus, listing the performance of the linear models would be more meaningful.
4. In line 161, does it mean that $v_{(k)}$ is the $k$-th smallest element? Since the gap $v_{(n)} - v_{(n-1)}$ seems to be the largest value minus the second largest value.
5. In line 195, is the distribution $n$-dimensional Gaussian?
6. What are the functions $\alpha$ and $\beta$ in Corollary 3.2.1?

### Soundness
3

### Presentation
2

### Contribution
3
