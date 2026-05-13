# Communication-efficient Algorithms Under Generalized Smoothness Assumptions

- Decision: Reject
- Scores: 5, 5, 5, 5

## Abstract
We provide the first proof of convergence for normalized error feedback algorithms across a wide range of machine learning problems. 
Despite their popularity and efficiency in training deep neural networks, traditional analyses of error feedback algorithms rely on the smoothness assumption that does not capture the properties of objective functions in these  problems. 
Rather, these problems have recently been shown to satisfy generalized smoothness assumptions, and the theoretical understanding of error feedback algorithms under these assumptions remains largely unexplored. 
Moreover, to the best of our knowledge, all existing analyses under generalized smoothness either i) focus on single-node settings or ii) make unrealistically strong assumptions for distributed settings, such as requiring data heterogeneity, and almost surely bounded stochastic gradient noise variance. 
In this paper, we propose distributed error feedback algorithms that utilize normalization to achieve the $\mathcal{O}(1/\sqrt{K})$ convergence rate for nonconvex problems under generalized smoothness. Our analyses apply for distributed settings without data heterogeneity conditions, and enable stepsize tuning that is independent of problem parameters. 
Additionally, we provide strong convergence guarantees of normalized error feedback algorithms for stochastic settings. 
Finally, we show that normalized EF21, due to its larger allowable stepsizes, outperforms EF21 on various tasks, including the minimization of polynomial functions, logistic regression, and ResNet-20 training.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes normalized error feedback algorithms across a variety of settings and provides convergence guarantees for this family of algorithms. The paper also provides experimental results on various settings such as logistic regression with non-convex regularizer. Notably, the convergence guarantees only rely on the general smoothness condition, which is a generalization of the classical smoothness condition.

### Strengths
The paper relaxes the classical smoothness condition to the generalized smoothness condition. Furthermore, the convergence guarantee is competitive and matches the SOTA.

### Weaknesses
My main concern with this paper is the only notable contribution is the relaxation from the classical smoothness condition to the generalized smoothness condition. While it is indeed an interesting result, the analysis is known from Chen et al. 2023 and various other works. And so, the theoretical analysis is not too impressive.

The empirical settings are a bit limited and not well-motivated but this is only a minor point.

The paper does not present well the communication aspect of the algorithm, nor its proof idea.

Minor comment:
- The word "expectation" should be capitalized in Table 1.

### Questions
- The paper does not present the communication-efficient aspect of the algorithm well, and it is not clear what is the communication protocol. The paper should state this explicitly. Furthermore, there is no analysis on the communication complexity. Is it the same as the sample complexity?

### Soundness
3

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
4

### Summary
**Summary.** The authors present the convergence guarantees for normalized error feedback algorithms for minimizing objectives satisfying generalized smoothness assumption. The proposed algorithm achieves $O(1/\sqrt{K})$ convergence rate for minimizing nonconvex problems. The authors also extend the analysis to stochastic settings. Finally, the authors show via numerical experiments that normalized EF21 outperforms EF21 on various tasks.

### Strengths
**Strengths.** Here, I list the major strengths of the paper. 

- The authors present the first analysis of normalized error feedback algorithms in a distributed setting for minimizing non-convex objectives satisfying generalized smoothness conditions. The proposed algorithm matches the guarantees of the standard error feedback algorithms under classical smoothness assumptions. 

-  The authors also show convergence under the stochastic settings. 
- The authors numerically evaluate the performance of the proposed algorithm.

### Weaknesses
 **Weaknesses.** Here, I list my major concerns and comments. 

- The discussion on the requirement of heterogeneity assumption by the earlier algorithms and the proposed algorithm not requiring the assumption is slightly misleading. In my understanding, heterogeneity assumption is usually needed if the local machines conduct multiple updates while the proposed algorithm, Normalized EF21, only conducts a single local update. So naturally the heterogeneity assumption is not required in contrast to the works of Crawshaw et al. (2024) and Liu et al. (2022) where the local machines conduct multiple local updates.  The authors should clarify the connection between their single local update approach and the lack of heterogeneity assumptions. Additionally, how does the proposed algorithm perform with multiple local updates, and whether heterogeneity assumptions would then become necessary?

- Why both Assumptions 1 and 2 are required? Assumption 2 implies Assumption 1, moreover, I believe it should be possible to conduct analysis only with Assumption 1.  Please justify the inclusion of both assumptions or revise the analysis to rely only on Assumption 1 if possible.

- For the stochastic setting, usually, the speed-up with the number of clients in the performance is desired. However, the presented analysis does not capture the effect of the number of clients on the performance.  Does the proposed algorithm achieve linear speed-up with the number of clients? Please analyze or discuss the scalability of the proposed algorithm with respect to the number of clients.

- In Theorem 1, is there an upper bound on the requirement of $\gamma_0$? Why such a bound is not necessary for Theorem 1 but is required in Theorem 2?
 
- The presented numerical results are very weak. The authors have compared the performance of their algorithm only against the EF21 algorithm. However, there are several federated baselines (with and without compression) against whom the authors should compare their algorithm. For example, the baselines like FedAvg, CHOCO-SGD, Momentum based algorithms, etc.

### Questions
Please see the weaknesses above.

### Soundness
3

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
4

### Summary
This paper presents the first convergence proof for normalized error feedback algorithms under generalized smoothness, a condition more applicable to a range of machine learning problems than traditional smoothness assumptions. Existing analyses either focus on single-node setups or make unrealistic assumptions (e.g., data heterogeneity) for distributed settings. Here, the authors propose distributed error feedback algorithms with normalization, achieving an $\(O(1/\sqrt{K})\) $ convergence rate for nonconvex problems without requiring data heterogeneity. The approach also enables stepsize tuning independent of problem parameters. Empirical results show that normalized EF21, which allows larger stepsizes, outperforms EF21 across tasks like polynomial minimization, logistic regression, and ResNet-20 training.

### Strengths
1 The paper clearly articulates the limitations of previous approaches and their constraints in proof, while explicitly highlighting the improvements and increased generalizability introduced by the proposed method.

2 This paper presents the first convergence proof for normalized error feedback algorithms under generalized smoothness in a decentralized setting, filling an existing theoretical gap on this issue.

3 The proof appears to follow a standard framework for decentralized problems, making it fairly credible.

### Weaknesses
1 The algorithm itself does not present significant innovation, as it primarily combines the standard EF21 with a normalization technique.

### Questions
Could you explain the specific challenges encountered in the proof after changing the assumptions and incorporating the normalization step, and how these challenges were addressed?

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
4

### Summary
This paper mainly considers the normalized EF21 algorithm in distributed settings. It generalizes the existing EF21 algorithm to the $(L_0,L_1)$-smoothness settings and achieves comparable convergence results. In the stochastic settings, the paper incorporates momentum into the algorithm to control the effect of gradient variance. Experimental results are generally consistent with the theoretical claims.

### Strengths
1. The paper is well-written and easy to follow. The notation definitions are clear.

2. The theorems are clear and complete. The theoretical results are novel and seem to be sound.

### Weaknesses
1. This is a technical solid paper, however, the technical novelty appears limited. I briefly went through the proof and my impression is that the proof primarily combines existing tools on $(L_0,L_1)$-smoothness, error feedback, and analysis of normalized gradient descent with momentum. These are well-established techniques, and the results, while solid, are not particularly surprising. It is possible that I overlooked something important, and I would appreciate it if you would point it out and allocate some space to briefly talk about the technical novelty in this case.

2. I am not sure why Theorem 2 implies the results of NSGD-M as the author mentioned in line 406. There is a mismatch that when $\sigma=0$, i.e. the deterministic case, the order of Theorem 2 is still $\mathcal{O}(T^{-1/4})$, while Theorem 1 in (Cutkosky & Mehta, 2020) is $\mathcal{O}(T^{-1/2})$. I think maybe you should follow (Cutkosky & Mehta, 2020) to allow a step size order shift regarding the magnitude of $\sigma$ to fix this.

### Questions
1. In Figure 1, it seems that EF21 (without normalization) converges faster in the first place. Could you provide some explanations or comments for this, as it seems this figure may not be strong enough to prove the efficiency of normalized EF21?

2. I am curious whether clipped EF21 rather than normalized EF21 is also applicable to the $(L_0,L_1)$-smoothness setting in the paper.

### Soundness
3

### Presentation
3

### Contribution
2
