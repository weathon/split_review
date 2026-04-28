# Learning with User-Level Local Differential Privacy

- Decision: Reject
- Avg Score: 4.67
- Scores: 5, 6, 3

## Abstract
User-level privacy is important in distributed systems. Previous research primarily focuses on the central model, while the local models have received much less attention. Under the central model, user-level DP is strictly stronger than the item-level one. However, under the local model, the relationship between user-level and item-level LDP becomes more complex, thus the analysis is crucially different. In this paper, we first analyze the mean estimation problem and then apply it to stochastic optimization, classification, and regression. In particular, we propose adaptive strategies to achieve optimal performance at all privacy levels. Moreover, we also obtain information-theoretic lower bounds, which show that the proposed methods are minimax optimal up to logarithmic factors. Unlike the central DP model, where user-level DP always leads to slower convergence, our result shows that under the local model, the convergence rates are nearly the same between user-level and item-level cases for distributions with bounded support. For heavy-tailed distributions, the user-level rate is even faster than the item-level one.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper first analyzes the mean estimation problem and then extends the findings to stochastic optimization, classification, and regression. Specifically, the authors propose adaptive strategies to achieve optimal performance across all privacy levels. They also derive information-theoretic lower bounds, demonstrating that the proposed methods are minimax optimal up to logarithmic factors. Notably, unlike the central DP model, where user-level DP generally leads to slower convergence, the results show that, under the local DP model, convergence rates are nearly identical between user-level and item-level cases for distributions with bounded support. For heavy-tailed distributions, the user-level rate is even faster than the item-level rate.

### Strengths
The paper tackles significant learning problems under user-level local differential privacy (LDP) constraints and establishes several tight lower and upper bounds.

### Weaknesses
Some statements throughout the paper are somewhat unclear, which can make parts of the presentation difficult to follow.

For the stochastic optimization problem, only the bounded gradient case and strongly convex objective functions are considered, which may not be sufficiently practical for broader applications.

### Questions
1. Why is the case of $\epsilon > 1$ considered interesting for LDP studies?

2. In Proposition 1 (2), to ensure user-level $\epsilon$-LDP from item-level $\epsilon$-LDP, if we randomly pick a sample from each user, why is it stated as ''$n$ users with $m$ samples per user'' instead of ''$n$ users with $1$ sample per user''?

3. For Definition 1, could you explain in detail why the definition of user-level $\epsilon$-LDP does not ensure item-level $\epsilon$-LDP?

4. For Theorem~1, I am unable to understand why is it said that the mean squared error will never converge to zero with increasing $m$ if $n$ is fixed.

5. What does $n_0$ represent in Equation (6)?

6. For the stochastic optimization problem, why is only the bounded gradient case considered? Why can't the private mean estimation over unbounded support developed in the paper be used for the unbounded gradient case, which seems more interesting and important in practice?

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
4

### Summary
This paper examines user-level privacy in a distributed setting, particularly in user-level local differential privacy (ULDP). The authors analyze mean estimation and its applications in stochastic optimization, classification, and regression, proposing adaptive strategies that optimize performance across various privacy levels. The authors claim that unlike in the central model, the convergence rates for user-level and item-level privacy are nearly equivalent in local models, with user-level privacy yielding even faster rates for heavy-tailed distributions.

### Strengths
1. The paper is very organized and presents its results in a clear manner.

2. Matching information-theoretic lower bounds are also derived which enhances the completeness of this work.

### Weaknesses
This paper studies ULDP on various problem settings: mean estimation, stochastic optimization, classification and regression. It is clear from Table 1 how the proposed rates in ULDP is different from the rates in item-level LDP.  However, some relevant papers appear to be missing from the references. For example, [1], [2] and [3]

[1]: Li, Bo, Wei Wang, and Peng Ye. "Improved Bounds for Pure Private Agnostic Learning: Item-Level and User-Level Privacy." arXiv preprint arXiv:2407.20640 (2024).

[2]: Cummings, Rachel, et al. "Mean estimation with user-level privacy under data heterogeneity." Advances in Neural Information Processing Systems 35 (2022): 29139-29151.

[3]: Charles, Zachary, et al. "Fine-tuning large language models with user-level differential privacy." arXiv preprint arXiv:2407.07737 (2024).


Besides, on line 132 and 133" Moreover, we also provide the first analysis on nonparametric classification and regression problems under user-level ϵ-LDP" is not accurate. To the best of my knowledge, [4] also studies regression in the ULDP setting under sparsity constraint. From my perspective, sparse estimation problem in LDP model ([5], [6]) might also could also be a valuable addition to the related work section.

[4]: Ma, Yuheng, Ke Jia, and Hanfang Yang. "Better Locally Private Sparse Estimation Given Multiple Samples Per User." arXiv preprint arXiv:2408.04313 (2024).

[5]: Zhu, Liyang, et al. "Improved Analysis of Sparse Linear Regression in Local Differential Privacy Model." arXiv preprint arXiv:2310.07367 (2023).

[6]: Zhou, Mingxun, et al. "Locally differentially private sparse vector aggregation." 2022 IEEE Symposium on Security and Privacy (SP). IEEE, 2022.

### Questions
Please see above.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper addresses the problem of achieving user-level local differential privacy (LDP) across various statistical tasks, including mean estimation, stochastic optimization, classification, and regression. By tailoring privacy mechanisms to different privacy levels, the authors propose algorithms that attain optimal performance rates under user-level LDP, achieving minimax optimality up to logarithmic factors. Unlike the central model, where user-level privacy often implies slower convergence, the local model yields convergence rates comparable to item-level LDP, with even faster rates in heavy-tailed distributions. This work provides both theoretical bounds and adaptive strategies, expanding the scope of user-level LDP applications in distributed systems.

### Strengths
+ It addressed user-level DP, which is a relatively less explored but extremely relevant area
+ It studied a wide variety of tasks (mean estimation, stochastic optimization, nonparametric classification and regression)

### Weaknesses
 - Technical novelty is unclear
- Some proof is unclear

### Questions
1. The authors highlight the regime where \eps > 1 in the introduction. Yet, it is unclear how this regime is handled in the proof of the lower bound. For example, in the proof of Theorem 2, how do we get from Eq. 62 to Eq. 64, if \eps > 1? I understand that the current proof holds for \eps < 1. Similar questions exist in the proof of Theorems 6 and 7. 

2. Following the above, it would be useful to highlight the difference in the lower bound proof for item-level and user-level LDP, especially the regime when \eps >1. 

3. It seems to me that the current local model is **non-interactive**? Can the authors comment on the **interactive** model? That is, can the proposed algorithms be easily extended to the interactive model?

### Soundness
2

### Presentation
3

### Contribution
2
