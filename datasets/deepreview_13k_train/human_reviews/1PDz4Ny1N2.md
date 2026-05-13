# Bridging Jensen Gap for Max-Min Group Fairness Optimization in Recommendation

- Decision: Accept
- Scores: 5, 8, 6, 8, 6

## Abstract
Group max-min fairness (MMF) is commonly used in fairness-aware recommender systems (RS) as an optimization objective, as it aims to protect marginalized item groups and ensures a fair competition platform. However, our theoretical analysis indicates that integrating MMF constraint violates the assumption of sample independence during optimization, causing the loss function to deviate from linear additivity. Such nonlinearity property introduces the Jensen gap between the model's convergence point and the optimal point if mini-batch sampling is applied. Both theoretical and empirical studies show that as the mini-batch size decreases and the group size increases, the Jensen gap will widen accordingly. Some methods using heuristic re-weighting or debiasing strategies have the potential to bridge the Jensen gap. However, they either lack theoretical guarantees or suffer from heavy computational costs. To overcome these limitations, we first theoretically demonstrate that the MMF-constrained objective can be essentially reformulated as a group-weighted optimization objective. Then we present an efficient and effective algorithm named FairDual, which utilizes a dual optimization technique to minimize Jensen gap. Our theoretical analysis demonstrates that FairDual can achieve a sub-linear convergence rate to the globally optimal solution and the Jensen gap can be well bounded under a mini-batch sampling strategy with random shuffle. Extensive experiments conducted using six large-scale RS backbone models on three publicly available datasets demonstrate that FairDual outperforms all baselines in terms of both accuracy and fairness.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper, through theoretical and empirical analysis, argues that existing methods with group max-min fairness (MMF) optimization for fairness-aware recommender systems will introduce Jensen gaps during model convergence when applying mini-batch sampling. It theoretically reformulates the MMF constraint objective as a group-weighted optimization objective and proposes a FairDual algorithm to minimize the Jensen gap. The effectiveness of FairDual is verified on two public datasets combined with three skeleton recommendation models.

### Strengths
S1: Sufficient support is provided for motivation through theoretical and empirical analysis.

S2: A new perspective based on group-weighted optimization is provided for MMF, and some corresponding theoretical insights are provided.

S3: Combining different skeleton models on multiple datasets provides various experimental results.

### Weaknesses
W1: The quality and clarity of the presentation need to be improved. Including some unclear statements that need to be revised, the organization of figures and tables needs to be revised, and some content coherence needs to be further revised. For example,
* For Formula 1, the meaning of the symbol $n_i$ seems missing. Secondly, based on the description in the second paragraph of Section 3, $L_k(u)$ is used to represent the recommendation list, and $K$ identifies the list length. However, in the description in the last paragraph, the statement "following the practice in time-aware RS, there may be users with interactions cu,i greater than the ranking size K, in which case we will only consider the least recent K interactions to represent their recent preferences" is confusing. Why is it emphasized that there are users with more than K interactions? Why must the most recent K interactions be kept instead of other numbers?

* Regarding the first paragraph of Section 4, the statement “In real-world scenarios, the number of users |U| is often large, and a mini-batch sampling strategy is often necessary due to the large computational costs. This involves dividing the |U| users into |U|/B batches and performing gradient descent methods on each batch” is also confusing. In my experience, in practice, grouping users into different batches for optimization is not usually adopted, i.e., each batch only contains a subset of users, and all interactions of each user are included. Secondly, the following description seems to use a random batch sampling. The purpose of emphasizing this aspect here is unclear.

* Regarding the second paragraph of Section 4.2 and Figure 1, as far as I understand, the convergence of the same group should be examined under different batch sizes to obtain the desired observations and conclusions.
* For the last paragraph of Section 5.2.1, the meaning of *P* is missing.

* Based on the current description of Section 5.2.2, I can't find any instructions on handling the first batch since it lacks a pre-batch to compute $g$. Secondly, does the operation of sampling $Q$ items bring noise or instability? This requires more discussion and experimental analysis.

* The current placement of figures and tables does not facilitate reading and needs to be placed as close to the corresponding description as possible.

* I like the first half of this paper. However, I am confused about why fairness must be associated with large recommendation models (especially large language recommendation models) after the methods section. On the one hand, this makes some of the treatments required for large language recommendation models appear abruptly. On the other hand, it is not conducive to evaluating the effectiveness of the proposed solution for fairness in a more general setting.

W2: The proposed FairDual lacks some deeper and more valuable insights. For example,
* Does it have the same performance or properties for other types of loss functions?

* Does it have the same behavior or properties as other fairness optimization constraints?

* How does it compare to existing work regarding storage space, computational complexity, and parameter size? Some static or dynamic group weighting methods discussed in related work seem lightweight. Is the additional overhead worthwhile?

* If it is not just about fairness at the item group level, does it apply to fairness at the user group level or even in situations where both users and items exist in groups?

W3: The current experimental setup and experimental results are not convincing enough.
* Representative datasets adopted by many previous fairness recommendation methods should be included more.

* Related to the previous concerns, the current version's selection criteria for baselines are confusing and not sufficiently representative. Skeleton models should not be constrained to be recommendation models related to large language models, and more research lines of fair recommendation methods mentioned in related work should be included as baselines, especially those aimed at designing group weighting.

* The current description of the implementation details is oversimplified, which is not conducive to reproducibility. Secondly, $\lambda$ is mentioned to range from 0 to 5, but in Figure 3 it is inclusive of 0 to 10.

### Questions
Please see the description in Weaknesses.

### Soundness
2

### Presentation
2

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
This paper analyze the Group max-min fairness (MMF) constrained optimization problem in recommendation. The authors first explain the Group MMF constrained objective as a non-linear polynomial form, indicating that the Jensen gap is non-negligible in mini-batch sampling based optimization (i.e., the gap between the overall loss and the sum of batched loss). To bridge the Jensen gap, this paper propose a dual optimization method called FairDual. Specifically, they rewrite the objective as a group-weighted BCE loss, and utilize the dual mirror gradient descent algorithm to optimize this loss. They further conduct experimental validation of FairDual's effectiveness and provide a detailed analysis of its proposed theoretical advantages.

### Strengths
- The Group MMF studied by the authors is significant for  recommendation fairness research.
- The motivation of the paper is clear, the algorithm introduction is straightforward, and the experimental analysis is detailed.
- The paper employs dual optimization to separate MMF and predicted score, resulting in a simple form of group-weighted BCE loss, and uses the dual mirror gradient descent algorithm for optimization, which is somewhat novel.

### Weaknesses
 - Theoretical proofs contain parts that require clarification, and the writing of the proof needs further improvement.
- The authors' analysis of the proposed group-weighted BCE loss is insufficient.
- In the implementation of FairDual algorithm, sampling-based ranking may introduce bias that is not adequately discussed.
- The authors conducted experiments on only two datasets, which may not be sufficient to demonstrate the algorithm's generalization.

### Questions
**Major Concerns:**

**Questions about Theoretical Analysis and Algorithm.** I have the following questions about the theoretical analysis and algorithm in this paper that need clarification:

- In the proof of Theorem 1 (Appendix A), why is Problem (15), i.e., $\min\mathbf{1}^\top\hat{\boldsymbol{A}}^\top\boldsymbol{w}+\lambda\max_{g\in\mathcal{G}}\gamma_g(\hat{\boldsymbol{A}}^\top\boldsymbol{w})_g$ , equivalent to Problem (2), i.e., $\min\boldsymbol{b}^\top(\hat{\boldsymbol{A}}^\top\boldsymbol{w})^{1+t}$ ? Specifically, considering the limit in the function $g(\cdot; \infty)$ , how is the constant $t$ determined? Providing an explicit solution for $t$ and $\boldsymbol{b}$ is important for Theorems 1 and 2.
- The organization of Lemma 2, Lemma 3, and Theorem 3 (Appendix D-F) is somewhat disorganized. I suggest reorganizing these proofs, e.g.:
  - Place Lemma 3 before Lemma 2, as the conclusion of Lemma 2 depends on Lemma 3.
  - Rewrite the proof of Lemma 2 to explain why the conclusion can be derived from $r(\boldsymbol{\mu} + c\boldsymbol{b}) < \infty$ (i.e., Lemma 3).
- The group-weighted form (4) of the Group MMF-constrained objective in Theorem 3 is concise, but its weight $\boldsymbol{s}_g$ is not. The authors should provide some intuitive explanations for the weight $\boldsymbol{s}_g$ to better elucidate the experimental phenomena (Case study in Section 6.3). For instance, under what circumstances is $\boldsymbol{s}_g$ larger, and when is it smaller?

- In the calculation of $\widetilde{w}$, the authors randomly sample $Q$ items and set $\widetilde{\boldsymbol{w}} _ b=\sum _ {k=1}^K(\boldsymbol{E} ^ j\boldsymbol{e} _ {u _ b}) _ {[k]}$ (cf. line 12 in Algorithm 1, and line 358). I am primarily concerned about the bias caused by sampling-based ranking (although it does not affect the fairness bound given in Theorem 4). Can the authors provide a theoretical analysis of this bias? Alternatively, could the authors change the sampling-based ranking to random sampling of $\boldsymbol{E}^j\boldsymbol{e} _ {u _ b}$ , and test the impact of this bias on the convergence rate of Jensen gap?

**Questions about Experiments.** I have the following concerns about the experiments:

- There are only two datasets utilized in the main results (Tables 1 and 2), which is insufficient. The authors might consider adding one or two widely-used datasets, such as Amazon-Electronic, which can be processed using the same method as in Appendix H.
- In Section 6.3 "Experimental Analysis", the authors find that the accuracy first increases then decreases as $\lambda$ increases, and attribute the phenomenon to the popularity bias. Then, is it possible to apply popularity debias method to the proposed algorithm, e.g., Inverse Propensity Score (IPS)-based reweighting method?

**Minor Concerns:**

- Line 324, $\hat c _{u, i} =  -d(\boldsymbol{e} _u, \boldsymbol{e}  _i)$, should there be $\hat c _{u, i} =  d(\boldsymbol{e} _u, \boldsymbol{e} _i)$ ?
- Line 325, the authors should suppose that $\boldsymbol{e}_u$ and $\boldsymbol{e}_i$ are normalized to make sure $d(\boldsymbol{e}_u, \boldsymbol{e}_i) \leq 1$ , which is relied on by the proof of Theorem 4 (cf. Line 1064).
- Line 357, "The $L$ items’ embeddings are denoted as ...", the $L$ should be $Q$ ?
- Line 979, the minus in $-\mathcal{I}$ should be placed at the loss term.

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
2

### Summary
This paper observes that the MMF-based optimization introduces a Jensen gap, which will become more pronounced when mini-batch size decreases and group size increases. The authors reformulate MMF into a group-weighted optimization, and solve its dual to minimize Jensen gap. Theoretical analysis reveals that the proposed method achieves a sub-linear convergence rate. Experiments are conducted across three recommendation models on two datasets.

### Strengths
1.	The paper provides both theoretical analysis and empirical results for motivation derivation and the effectiveness of the proposed method.
2.	The experiments are conducted across large-scale recommendation models, which aligns well with the stated motivation.
3.	The paper is generally well-written, with a clear structure.

### Weaknesses
1.	The assumption of convexity is too strong and impractical for large-scale recommendation models. The optimization landscape for these models is typically non-convex, with numerous local minima and saddle points. Applying convex optimization techniques, even if the loss function itself is convex, might not be suitable for the overall non-convex problem. This discrepancy between the theoretical assumptions and the practical reality of deep learning-based recommendation models needs to be addressed.
2.	Why can the reported NDCG exceed 1, which is theoretically impossible? Also, please specify the number of items in the truncated list K.

### Questions
Please refer to Weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
In this paper, the authors claimed that current group max-min fairness (MMF) methods would introduce a Jensen gap between the model’s
convergence point and the optimal point. The authors analyzed the existence of Jensen gap theorically and emprically. Then, the authors proposed FairDual, a  dual-optimization approach that guaranteed a bound for the Jesen gap. They conducted comprehensive experiments to show the effectiveness and efficiency of FairDual compared to baselines.

### Strengths
- The motivation is well established with theorical and emprical analysises of the Jesen gap in Section 4.
- The method is solid with a guaranteed bound for Jesen gap, and the experiment also showed that the proposed method indeed has lower gap than other baselines.
- The authors conducted complete and comprehensive evaluations, including the effictiveness, Jensen gap analysis, case study, training efficiency and parameter analysis.

### Weaknesses
 - Baselines. The authors mentioned that there are two types of approaches to bridge the Jensen gap,  re-weighting and optimization-based methods. But the authors mostly compared only re-weighting methods in the experiments, while ignoring optimization-based methods they mentioned in the introduction part, such as  Abernethy et al. 2022, Cousins 2022, Demidovich et al., 2023 and Agarwal et al., 2018. I suggest the authors to add state-of-the-art baselines in optimization-based methods mentioned in the paper.

### Questions
- Can authors explain is there a reason that in some cases the MRR is not statistically significant as shown in Table 1 and 2? For example, the MRR in the top-5 results of RecFormer and BigRec is not significant and no improvement, while the improvement of NDCG and MMF is significant. Can authors give some insights on this observation?

- In the visualization of Figure 3(c), the differences in the patterns of the two figures are not quite obvious. The classification boundary of FairDual also seems to exist. Could the authors provide some quantitative results to distinguish the different patterns, such as divergence in the two distributions?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
In this paper, the authors address the challenge of integrating a max-min fairness constraint, which introduces a Jensen gap between the model’s convergence point and the optimal point. They first demonstrate that using mini-batch sampling optimization strategies leads to a Jensen gap that increases as the mini-batch size decreases. To bridge this gap, the authors propose an algorithm that reformulates the original optimization problem through a re-weighting approach, leveraging dual-optimization techniques to update the weights of each group. They theoretically prove that their approach achieves a sublinear convergence rate and numerically demonstrate its effectiveness.

### Strengths
- The paper is well written and provides interesting insights. 
- The authors well motivated the problem in Section 4 where they established the existence of Jensen gap.
- The theoretical results appear sound. The authors also provided extensive numerical evaluations of their method.

### Weaknesses
 - It'd be helpful if the authors can provide more interpretations for Theorem 4, the main theoretical result and, in particular, comment on their technical contributions. What is the main technical novelty in attaining this theoretical result? A proof sketch could also be helpful. Specifically, it's unclear how the dual formulation directly addresses the Jensen gap, and what specific properties of the dual problem allow for the derivation of the sublinear convergence rate. The connection between the dual gradient updates and the original max-min fairness problem needs further clarification. A more detailed explanation of how the complementary slackness is bounded, and how this bound relates to the convergence rate would be beneficial.
- Following the point above, in the numerical experiments, there appears to be some non-monotonic variation of the Jensen gap w.r.t. the batch size. I wonder if the authors can comment on why this is the case. Is this consistent with the theoretical results? It would be useful to see a more rigorous analysis of the experimental results, particularly regarding the observed non-monotonicity. A discussion on the potential sources of this non-monotonic behavior, such as the interplay between batch size and gradient variance, would be valuable. Furthermore, it would be helpful to see a more detailed analysis of how the Jensen gap changes with respect to both batch size and group size, and whether the observed trends are consistent across different datasets and experimental setups.

### Questions
- Could the results extend to alternative fairness constraints beyond max-min fairness?
- What is the computational complexity of the proposed algorithm and how does it compare with the other baselines?

### Soundness
3

### Presentation
3

### Contribution
2
