# Cross-Domain Off-Policy Evaluation and Learning for Contextual Bandits

- Decision: Accept
- Scores: 6, 6, 6, 8

## Abstract
Off-Policy Evaluation and Learning (OPE/L) in contextual bandits is rapidly gaining popularity in real systems because new policies can be evaluated and learned securely using only historical logged data. However, existing methods in OPE/L cannot handle many challenging but prevalent scenarios such as few-shot data, deterministic logging policies, and new actions. In many applications, such as personalized medicine, content recommendations, education, and advertising, we need to evaluate and learn new policies in the presence of these challenges. Existing methods cannot evaluate and optimize effectively in these situations due to the notorious variance issue or limited exploration in the logged data. To enable OPE/L even under these unsolved challenges, we propose a new problem setup of Cross-Domain OPE/L, where we have access not only to the logged data from the target domain in which the new policy will be implemented but also to logged datasets collected from other domains. This novel formulation is widely applicable because we can often use historical data not only from the target hospital, country, device, or user segment but also from other hospitals, countries, devices, or segments. We develop a new estimator and policy gradient method to solve OPE/L by leveraging both target and source datasets, resulting in substantially enhanced OPE/L in the previously unsolved situations in our empirical evaluations.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
Cross-Domain Off-Policy Evaluation and Learning (OPE/L) addresses challenges in contextual bandits, such as few-shot data, deterministic logging, and new actions, by leveraging logged data from multiple domains to evaluate and learn new policies more effectively. This paper introduces a new estimator and policy gradient method that improves OPE/L performance, both theoretical analysis and experimental results are presented.

### Strengths
1. This paper studies an interesting and practical problem, with both theoretical analysis and experimental results.
2. This paper is mostly clearly written, and most parts are easy to understand.
3. A suite of experimental results are provided after the theoretical analysis.

### Weaknesses
1. I feel the theoretical results are a little bit weak:

1a I am curious about the condition 3.2, is this a common and reasonable assumption? It is better to provide more insightful comments on when this assumption will hold in practice.

1b It is hard for me to understand the paragraph in line 314-320. Why is the estimator unbiased when its cluster size is equal to 1? Intuitively, more clusters in the target cluster $\phi(T)$ mean more logged data come from the same cluster as the new data in the target domain, which will help reduce the bias? Please expand the discussion on this paragraph.

1c I also feel curious about using the off-the-shelf clustering algorithm based on empirical average. How does it work in your theoretical analysis? If the rewards are not very symmetrically distributed, i.e. heavy-tailed distributed, then the empirical mean will lead to terrible estimation, so how to deal with this issue in practice?

1d is there a final regret bound in this paper in terms of the magnitude of $T$ like other bandit works. e.g. $O(\sqrt{T})$

2. Since this paper studies a very niche area of contextual bandits, it is better to give more real-world applications to help readers understand its significance.

3. It is better to report the running time of the proposed algorithm along with baselines to validate the efficiency of the proposed method.

Remark: I checked the codes in the supplementary material and most notes are written in non-English (I guess it is Japanese). Please use English for everything in your source codes, since other languages may lead to violation of double-blind reviewing policy.

### Questions
Please refer to the above Weaknesses section.

### Soundness
2

### Presentation
3

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
This work studies off-policy estimation and learning (OPE/OPL) for the cross-domain scenario, where logged bandit feedback for different domains is leveraged to improve the offline estimation and learning for policies on a target domain. The proposed estimator COPE relies on a reward decomposition inspired by previous work. Its bias and variance were studied for OPE and a straightforward policy gradient approach was derived for OPL. Experiments show that the estimator performs well on cross-domain scenarios with support deficiency in both OPE and OPL

### Strengths
- The paper is well written and pleasant to read.
- The experimental section shows favorable results for the proposed solution.

### Weaknesses
 - If the cross-domain application in OPE/OPL is novel, the motivation and contribution of the work is oversold:
   + Hospitals for example rarely share data of patients with centralised entities, and learning on this type of sensitive data is primarily done within the framework of _federated learning_ [3]. The described framework where the learner has access to the data of all hospitals in a centralised manner is far from reality. 
   + The MIPS [1] and OffCEM [2] estimator for example are based on the same reward decomposition, and treat the large action space scenario, where support deficiency happens all the time, as the logging policy cannot cover all the action space. For example, this sentence in the work: "However, our work differs from these studies in motivation, as we formulate the cross-domain OPE/OPL problem to solve non-trivial challenges such as new actions and deterministic logging" lacks support, as MIPS and OffCEM already solve these non-trivial challenges. See for example Section 3 of [1] where one of the main motivations is going beyond the common support assumption.

- The derivation technique of the estimator is not novel. The COPE estimator is based on the same technique of [1, 2], with little adjustment  to the new application. Its bias/variance tradeoff is also studied in the same way as [2], which makes the theoretical contribution unoriginal.


- The work claims to study OPL, which was not done in [1, 2]. Their proposed OPL method is based on the derivation of a policy gradient, which is basically computing the gradient of the proposed estimator and using it in first order optimisation methods. This contribution is also straightforward and lacks studying in the paper.

- The paper omits a large spectrum of OPE/OPL contributions based on the pessimism principle. This principle was heavily studied for OPL specifically and was proven to be optimal, contrary to optimising the estimator directly. The following lines of work should be incorporated to the related work and discussed, the following papers can be a good start:

   + Bayesian Counterfactual Risk Minimization. Ben London, Ted Sandler Proceedings of the 36th International Conference on Machine Learning, PMLR 97:4125-4133, 2019.
   + Confident Off-Policy Evaluation and Selection through Self-Normalized Importance Weighting. Ilja Kuzborskij, Claire Vernade, Andras Gyorgy, Csaba Szepesvari Proceedings of The 24th International Conference on Artificial Intelligence and Statistics, PMLR 130:640-648, 2021.
   + PAC-Bayesian Offline Contextual Bandits With Guarantees. Otmane Sakhi, Pierre Alquier, Nicolas Chopin Proceedings of the 40th International Conference on Machine Learning, PMLR 202:29777-29799, 2023.
   + Importance-Weighted Offline Learning Done Right. Germano Gabbianelli, Gergely Neu, Matteo Papini Proceedings of The 35th International Conference on Algorithmic Learning Theory, PMLR 237:614-634, 2024.
   + Logarithmic Smoothing for Pessimistic Off-Policy Evaluation, Selection and Learning. Otmane Sakhi, Imad Aouali, Pierre Alquier, Nicolas Chopin.


### Questions
- What are the challenges that make the cross-domain application more difficult/particular compared to the large action space scenario? If it is just deterministic policies/deficient support, then it is not different than the case of large action spaces.
- What is the originality of the bias/variance study of the COPE estimator?
- How can you be sure that your OPL method will converge to the right policy?
- Is there a reason why you omit the whole OPL literature based on pessimism?

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
This paper focuses on addressing the problem of OPE/L when the common support assumption is not met. It introduces a new estimator based on the Common Cluster Support assumption and multi-source data to tackle this issue. The proposed approach is validated through semi-simulated experiments.

### Strengths
- The challenges of OPE/L with multi-source data and violations of the common support assumption are significant and relevant in practical contexts.

- The proposed estimator aligns well with the motivations of this paper and provides theoretical support for its unbiasedness.

### Weaknesses
 - This paper does not compare with significant literature focused on the limited overlap problem. For instance, the assumptions in Condition 3.1 and the subsequent proof of unbiasedness are fundamentally similar to those in [1, 2], which also assume that while the original x may not satisfy the overlap assumption, there exists a score or representation that does. The unique contribution of this paper lies in its application to the cross-domain OPE/L setting.

- However, the absence of a real cross-domain experimental validation, relying instead on semi-simulated experiments, limits the contribution of this work.

If the authors clearly outline the unique challenges of limited overlap in the context of multi-source data compared to conventional scenarios, and explain the specific efforts made to address these challenges, I would consider increasing my score.
Additionally, if the authors provide evaluation results of their method in real-world settings, I would also reconsider my score.

### Questions
see above

### Soundness
3

### Presentation
2

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
This paper tackles the challenging problem of Cross-Domain Off-Policy Evaluation and Learning (OPE/L) for contextual bandits. It focuses on addressing practical issues frequently encountered in real-world applications, such as deterministic logging policies, few-shot data in the target domain, and the presence of new actions. The authors propose COPE, a novel estimator that leverages data from multiple source domains to improve evaluation and learning in a target domain. COPE decomposes expected rewards into domain-cluster and domain-specific effects, aiming to reduce bias and variance. The paper includes an empirical evaluation on a real-world dataset and provides the code for reproducibility.

### Strengths
- The paper addresses the important problem in OPE/L for contextual bandits. In particular, the setting where there are deterministic logging policies is often overlooked, despite being a scenario highly relevant to practical deployments. This focus significantly enhances the paper's relevance to real-world applications

- The proposed COPE estimator introduces an interesting approach to leveraging cross-domain data, building upon and extending existing ideas in the field. The connections and distinctions with related estimators, such as OffCEM by Saito et al., are noteworthy

- The empirical evaluation is comprehensive, including ablation studies that provide insights into the contributions of different components of the proposed method. The provided code further strengthens the paper's contribution by ensuring reproducibility

### Weaknesses
 - While the experimental evaluation on the chosen dataset is comprehensive, I believe the paper would benefit from evaluation on an additional dataset. This would improve the paper, evaluating COPE across different data distributions and characteristics.

- The clarity of the paper could be improved, particularly in explaining the technical details of the COPE estimator, the clustering approach, and the underlying assumptions. More precise definitions and a step-by-step explanation of the methodology would enhance understanding and reproducibility.

- The novelty of the approach is present, however COPE is very similar to OffCEM, as also mentioned in the paper 

- The theoretical analysis, which I believe is already interesting, could be strengthened. Specifically, an analysis of the variance of COPE would be valuable. Furthermore, exploring the estimator's bias when the various analyzed conditions are not satisfied would provide a more complete picture of its performance characteristics.

- The theoretical assumptions, such as Conditional Pairwise Correctness (CPC), while providing a foundation for the analysis, might be difficult to verify or guarantee in practice. 

Minor:
typo at line 081: Cross-domain Off-Policy EvaluatOIn (COPE)

### Questions
- Can the authors provide a theoretical comparison of COPE with the existing methods in the setting of deterministic logging policies?

- Can the authors provide a more detailed explanation of the clustering function, its practical implementation, and its impact on the performance of COPE? What guidelines can be offered for choosing appropriate clustering strategies in different domains?

- What are the practical implications and limitations of the theoretical assumptions in real-world scenarios? How can these assumptions be verified in practice?

- Can the authors provide an analysis of the variance of the COPE estimator? How does the variance compare to existing methods?

- What is the bias of COPE when the conditions for unbiasedness are not met? Is it possible to characterize or bound this bias?

### Soundness
3

### Presentation
3

### Contribution
3
