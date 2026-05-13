# Be Aware of the Neighborhood Effect: Modeling Selection Bias under Interference

- Decision: Accept
- Scores: 8, 6, 5, 8

## Abstract
Selection bias in recommender system arises from the recommendation process of system filtering and the interactive process of user selection. Many previous studies have focused on addressing selection bias to achieve unbiased learning of the prediction model, but ignore the fact that potential outcomes for a given user-item pair may vary with the treatments assigned to other user-item pairs, named neighborhood effect. To fill the gap, this paper formally formulates the neighborhood effect as an interference problem from the perspective of causal inference and introduces a treatment representation to capture the neighborhood effect. On this basis, we propose a novel ideal loss that 
can be used to deal with selection bias in the presence of neighborhood effect.   
 We further develop two new estimators for estimating the proposed ideal loss. 
  We theoretically establish the connection between the proposed and previous debiasing methods ignoring the neighborhood effect, showing that the proposed methods can achieve unbiased learning when both selection bias and neighborhood effect are present, while the existing methods are biased. Extensive semi-synthetic and real-world experiments are conducted to demonstrate the effectiveness of the proposed methods.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This research investigates the influence of other user-item interactions on their ratings in Recommender Systems (RS). While prior studies concentrated on reducing selection bias, neglecting the neighborhood effect can lead to distorted estimates and subpar predictive model performance. This study introduces a treatment representation to capture the neighborhood effect and suggests a new loss function and estimators to tackle both selection bias and neighborhood effects, resulting in unbiased learning compared to current approaches. The effectiveness of these methods is demonstrated through theoretical assurances and comprehensive experiments.

### Strengths
- The introduction of the neighborhood effect in mitigating bias in Recommender Systems (RS) is innovative. The research addresses a significant issue, and its rationale is evident.

- The paper is well-structured and the method is substantiated by robust theoretical foundations.

### Weaknesses
 - The breach of SUTVA and the presence of interference in debiasing user feedback were previously discussed in [1], where they also examined the interactions between propensity and implicit feedbacks on other items. I would like to see a discussion on it in this manuscript.

- A case study or a real-world example demonstrating the neighborhood effect would be valuable for a clearer comprehension of the underlying motivation.

- To enhance the clarity, it is advisable for the authors to furnish pseudocodes delineating the procedural steps of the proposed estimator and the propensity estimation process.

### Questions
Please see the Weaknesses section.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Selection bias in recommender systems arises from the filtering process and user interactions, with most studies focusing on addressing it for unbiased prediction models. However, these studies often overlook the neighborhood effect, which is the variation in potential outcomes due to treatments assigned to other user-item pairs. This paper formulates the neighborhood effect as an interference problem and proposes a novel ideal loss to deal with selection bias in the presence of this effect. Two new estimators are developed, which are shown to achieve unbiased learning when both selection bias and neighborhood effects are present, unlike existing methods. Extensive experiments confirm the effectiveness of these proposed methods.

### Strengths
1. The studied topic is practical and interesting.
2. The experiments are very detailed for reproducing.

### Weaknesses
1. Too many assumptions made the manuscript hard to follow.

### Questions
n/a

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper addresses the combined impact of selection bias and neighborhood effects in recommender systems.\
It introduces a novel approach to represent neighborhood effects as interference, alongside a treatment representation.\
The paper establishes a theoretical connection with existing methods, showing that their approach achieves unbiased learning in the presence of both selection bias and neighborhood effects.\
Experimental validation is conducted on semi-synthetic and real-world datasets to demonstrate the effectiveness of the proposed methods.

### Strengths
1. The paper is comprehensive and provides a theoretical analysis.
- the paper provides a robust theoretical foundation for its proposed methods. It derives unbiased estimators for the ideal loss, establishes a connection to prior methods that do not account for neighborhood effects, and includes analyses of tail bounds and generalization error bounds for the proposed estimators.

2. The experiment is thorough.
- the paper substantiates its claims with empirical results from experiments conducted on both semi-synthetic and real-world datasets. These experiments demonstrate that the proposed estimators outperform previous methods when neighborhood effects are present, underscoring the practical utility and effectiveness of the proposed approach.

### Weaknesses
1. Motivation is weak
- why do we need to eliminate the neighborhood effect?
- for example, existing recommenders can consider the neighborhood effect in the training phase and make recommendations with the neighborhood effect (e.g., similar users have similar embedding and thus get similar recommendations).
- Therefore, the neighborhood effect can be a rich information source for model training.

2. Assumptions are not realistic.
- why $r_{u,i}$ is affected by $o_{u,i}$? In my opinion, $o_{u,i}$ is just a treatment to observe $r_{u,i}$, and does not affect the 'value' of  $r_{u,i}$. (i.e., the value of $r$ is affected only by $x$ and observed only when $o=1$).
- If $r_{u,i}$ is affected by $o_{u,i}$, i think the assumption 3 is not hold.
- In the paper, g is a scalar (a continuous variable), not a representation vector.

3. Minor concerns
- In the real-world experiment, the authors use 5% MAR test ratings for the propensity estimation. This process is unrealistic.
- In the semi-synthetic experiment, the definition of neighborhood effect is the number of neighbor pairs with $o >= c$. what does it mean? Since $o \in {0,1}$, i cannot understand the c is chosen to be the median of all $g$.

### Questions
Please refer to the weaknesses.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the authors introduce a new debias problem under the causal inference framework for handling selection bias in recommendation systems in the presence of the neighboring effect: when the potential outcome for one user-item pair does vary with the treatments assigned to other user-item pairs. The potential outcome, treatment and a new ideal loss are defined so as to include both the selection bias AND the neighborhood interference effect. Follow two new estimators to estimate the newly designed ideal loss: neighborhood inverse propensity score (N-IPS) and neighborhood doubly robust (N-DR).

### Strengths
The paper is well written and quite enjoyable to read. 

The newly proposed ideal loss and estimators are well theoretically investigated:

-The difference between the two losses with and without neighborhood effect (Theorem 2) is studied. 

-The new ideal loss is shown as identifiable (Theorem 1). 

-The first proposed estimator tackles the case when $\bold{g}_{u,i}$, the treatment representation vector, is a continuous probability density via a smoothing symmetric kernel function (ex: Epanechnikov or Gaussian kernels). The N-DR estimator is derived similarly.  -Bias and variance of both estimators are computed with tail and generalization error bounds provided (Theorem 5). 

Then, it is shown how to estimate the propensity score for the joint effect of the treatment and the treatment representation vector for the neighboring effect.  

The approach is accompanied first with experiments on semi-synthetic data (based on MovieLens 100K) to: 
1) assess whether the proposed estimators provide a more accurate estimation for the ideal loss compared to the state-of-the-art methods when neighboring interference is observed.  
2) measure the influence of the neighborhood effect strength on the estimation accuracy.
On the semi-synthetic dataset, for all interference strengths, N versions of DR or MRDR are giving better accuracy (lower relative error) than DR and MRDR but also are less harmed by the interference strength for 6 different methods of predicting the ratings.  

Real-world experimentation is done on Coat, Yahoo! R3 and KuaiRec for which MSE, AUC and NDCG are evaluated N-* are usually in the 3 best results.

### Weaknesses
I would develop some explanations for the experimental part even in the appendix. Cf. questions. 

Minor, typos:

-p.2: “In addition, we introduces”

-p.3: “... both … leads”

-p.9: “For the methods require propensity”, “the three choice”, “Guassian”, “on the a prior”

-p.10: “Early literature focus”

Also, when Figure 1 is first introduced in Introduction section, we don’t yet have the preliminaries content and all elements are not fully defined such as $\bold{g}_{u,i}$ which can make it difficult to understand at first sight.

### Questions
Q1: In practice, how do you specify the probability density function of $\bold{g}$?

Q2: In practice, what is the best choice between Epanechnikov and Gaussian kernels? Experiments seem to have been done only with the Gaussian kernel.

Q3: Can you please detail again for the semi-synthetic experiments how do you define the set of $\mathcal{N)_{u,i}$ as the set of historical user and item interactions for the neighbors of (u,i) who do have an influence on user u? 

Q4: How does $p_{u,i} = p \alpha^{max(0,4-r_{u, i})}$ account for the neighboring effect too?

Q5: c is chosen to be the median of all g_u,i according to p. 7 but g_u,i is also defined depending on c. Can you please explain?

Q6: Does KuaiRec specify the MAR and MAR watching ratio records? If not, how to measure the neighboring effect?

Q7: How p is defined in $p_{u,i} = p \alpha^{max(0,4-r_{u, i})}$ is explained in p. 28. Can you please elaborate: “we adjust p to ensure the total observed sample is 5% of the entire matrix”?

=== AFTER REBUTTAL ===

I thank the authors for taking the time to answer my questions that are now addressed. Many thanks for the added experiments that show the results are not tight to the choice of the kernel.
Hence, I upgrade my score to Accept.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
