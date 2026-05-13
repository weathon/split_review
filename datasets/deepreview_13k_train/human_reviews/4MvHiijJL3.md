# Model Explanation Disparities as a Fairness Diagnostic

- Decision: Reject
- Scores: 8, 6, 5, 3, 5

## Abstract
Recent works on fairness in machine learning have focused on quantifying and eliminating bias against protected subgroups, and extended these results to more complex subgroups beyond simple discrete classes, known as "rich subgroups." Orthogonally, recent works in model interpretability develop local feature importance methods that, given a classifier $h$ and test point $x$, attribute influence for the prediction $h(x)$ to the individual features of $x$. This raises a natural question: Do local feature importance methods attribute different feature importance values on average in protected subgroups versus the whole population, and can we detect these disparities efficiently? In this paper, we formally introduce the notion of feature importance disparity (FID) in the context of rich subgroups, which could be used as a potential indicator of bias in the model or data generation process. We design an oracle-efficient algorithm to identify large FID subgroups and conduct a thorough empirical analysis auditing for these subgroups across $4$ datasets and $4$ common feature importance methods of broad interest to the machine learning community. Our algorithm finds (feature, subgroup) pairs that: (i) have subgroup feature importance that is often an order of magnitude different than the importance on the whole dataset (ii) generalize out of sample, and (iii) yield interesting discussions about potential bias inherent in these common datasets.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The work introduces the problem of quantifying disparities in the output of a feature importance method across groups in the data. It finds subgroups for which the average feature importance for a given feature differs significantly compared to the feature importance in the whole population. The main contribution is that the subgroups need not be enumerated beforehand. The proposed method is able to search for groups represented as functions on an arbitrary set of features, called ‘rich subgroups’ in the fairness literature. To do so, the work formalizes a constrained optimization problem and solves it via online learning algorithms through a reduction that leverages oracle access to cost-sensitive classifiers. Theoretical result shows the solution is close to the maximum disparity group. Experiments on multiple datasets show the applicability of the method for different feature importance methods.

---
Updating the score after the rebuttal which addresses concerns on significance of the problem and presentation of the algorithm.

### Strengths
1. The ideas are presented clearly with adequate explanation and clear notation. 
2. I like the generality of the problem formulation and how it is presented in Section 2 and 3 which can then be readily made specific to different feature importances.
3. Experiments are thorough - multiple explanation methods, datasets, tests on hold-out set - and are presented concisely.

### Weaknesses
1. (Major) Utility of the algorithm outputs could be discussed more thoroughly. As discussed in limitations, all differences in explanation outputs need not imply a discriminatory model. On the contrary, sometimes a model will differ in its logic in the protected group to account for differences in data. For example, the feature of not having a health insurance will be much more predictive of health outcomes in the unhoused population (say, a protected group) in comparison to whole population. So, the model logic and the feature importance will differ in the protected group. Reasons for finding such groups should then be discussed to motivate the utility of the method, along with suggestions for diagnosing the disparities. Introduction and empirical results can be edited to convey the significance of the explanation disparity problem.
2. (Minor) Algorithm for finding maximal group can be described in more detail. Reduction to CSC and the specifics of Algorithm 1 like what is theta, lambda, and so on can be briefly explained, even if this is a standard method for solving constrained optimization.

### Questions
1. Please discuss relation to the work Balagopalan et al. 2022 (The Road to Explainability is Paved with Bias: Measuring the Fairness of Explanations https://dl.acm.org/doi/abs/10.1145/3531146.3533179) which also investigates disparities in explanation outputs. Advantages of the proposed method such as rich subgroups should be highlighted.
2. Please include more discussion on what can be done after observing disparities in explanation output. How can the user interpret the relation between explanation disparities and the underlying social biases, and decide how to update the model?

---
## Minor (no response is requested)

In Definition 1 of FID, consider denoting if the expectation is over different samples of the whole dataset X^n.

The scope of prediction models, sensitive features, and feature importances supported by the method was not clear to me. Describe the assumptions needed on the prediction model (for CSC to give good solution) and sensitive features (mix of categorical, real variables) if any. Consider listing feature importance methods that satisfy separability and any other required conditions for the method, perhaps in a table format.

Consider discussing extensions to non-separable importances other than weights in linear regression such as feature-permutation based importances in decision trees.

Please increase font size in Figures 2-6.

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper formally introduces the notion of feature importance disparity in the context of ``rich'' subgroups, which could be used as a potential indicator of bias in the model/data generation process. The proposed algorithm finds (feature, subgroup) pairs that: (i) have subgroup feature importance that is often an order of magnitude different than the importance on the whole dataset, generalize out of sample.

### Strengths
The paper tackles an important question in machine learning literature on understanding how a specific feature contributes to a model's prediction, focusing on feature importance. The objective is clearly stated, definitions are well defined, and the optimization problem is intuitive and well-defined. Overall it uses existing methods in learning theory to solve an interesting fairness problem.

### Weaknesses
I find algorithm 1 hard to interpret; in particular, it involves in exponential gradient update, but it's not clear to me what certain parameters mean. In addition, it is not clear how this algorithm is related to Kivinen & Warmuth in terms of who is the max player, who is the min player, and what their objectives are.

### Questions
1. In definition 1, what does the expectation over? namely, what is $X$?
2. How should I intuitively understand the notion of ``Locally Separable''? In reality, how easy or hard is it to satisfy this condition?

Others:
1. The citation style is weird; the author might consider changing it.

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
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper explores feature importance methods and their potential for disparities in attributing feature importance values across different subgroups. The authors introduce the concept of Feature Importance Disparity (FID), which measures whether local feature importance methods attribute different feature importance values on average in protected subgroups compared to the entire population as a proxy to indicate bias in the model or data generation process. The paper designs an efficient algorithm to identify subgroups with large FID and provides empirical results across 4 public datasets and 4 common feature importance methods.

### Strengths
- The paper does a good job at motivating the connection between explainability and fairness and why more exploration in this direction is warranted
- The experiments to showcase the results in terms of explainability for FID are extensive
- The convergence proof for Algorithm 1 appears correct to me

### Weaknesses
For completeness, I do not have any experience in explainability, but I do in algorithmic fairness as well as the optimization literature.
The main weaknesses of this paper to me appear to be (a) the presentation of FID and Algorithm 1 and (b) the implications and connections to downstream fairness.

(a) The technical presentation of the optimization algorithm is too abrupt for the reader, and some lingering questions never get addresses fully.
-What is the rich subgroup class we are considering, for practical examples?
-What do the size violations correspond to?
-The notion of CSC being relegated to the appendix really subtract clarity from the work, as the reader struggles to bounce back and forth from the appendix for almost every step of Algorithm 1.
I appreciate the intricacies of presenting an algorithm such as this one, but one could maybe shorten the "Introduction" section to provide either a (i) simple example or (ii) dedicate some space to go through each of the single ingredients of the algorithm. Personally, I think this would go a long way towards improving the understanding of AVG-SEPFID and appreciate why solving it is tricky.

(b) The main drawback of this paper is the lack of connections with fairness metrics (such demographic parity or equalized odds) to connect the results in e.g., Table 1, with the disparities of the classifiers with respect to different subgroups. While pointing out biases in the original data is useful, FID seems to be applicable to a given group or family of classifiers $\mathcal{H}$, while in practice what modelers are interested in is to be able to analyse and find the pathways of discrimination in a given model. I believe that an extra set of experiments where the connection between natural fairness metrics and the proposed FID would make this paper meaningful and interesting to the community. As of now, from an algorithmic fairness standpoint, the paper ends too abruptly.

### Questions
Please see "Weaknesses" section above.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces the notion of feature importance disparity (FID) to capture fairness of a model in terms of whether a feature importance value differs significantly for a subgroup compared to the entire population. Then to assess the fairness of a given model, the authors present an algorithm to find a feature and a subgroup, characterized by a function over the protected features, that exhibits a large FID. The algorithm involves iteratively solving constrained optimization problems using a polynomial number of calls to an oracle for cost-sensitive classification. The proposed method is evaluated empirically on four datasets.

### Strengths
The characterization of fairness in terms of disparities in feature importance scores is novel and interesting.

The proposed approach can be used with many feature importance notions and (somewhat) model-agnostic (for some feature importance scores), and thus can potentially be widely applicable.

The paper is well-written and easy to follow.

### Weaknesses
The proposed method returns real-valued subgroup functions, which are not directly interpretable as indicators of specific population groups. While the authors suggest these functions represent fractional membership in demographic groups, the practical utility of such an interpretation in characterizing bias is unclear. For instance, a binary subgroup function would clearly delineate a group experiencing disparate treatment, whereas a real-valued function requires further interpretation to understand its implications for fairness. This lack of clear interpretability makes it difficult to translate the findings into actionable insights for addressing potential biases.

Algorithm 1, designed to maximize AVG-SEPFID, requires a number of calls to the CSC oracle that is quadratic in the size of the data for a single feature. This poses a significant computational challenge, especially for large datasets with numerous features. The quadratic complexity could severely limit the method's applicability in real-world scenarios where datasets are often massive and computational resources may be constrained. The authors should provide a more detailed analysis of the algorithm's scalability and explore potential optimizations to mitigate this computational burden.

Empirical evaluation lacks comparison with any baseline, making it difficult to assess the effectiveness of the proposed method relative to existing approaches. A crucial question is how the subgroups identified by this method compare to those found by established 'rich subgroup' discovery methods. Without such a comparison, it is hard to gauge the novelty and practical value of the proposed approach in identifying subgroups with significant feature importance disparities.

### Questions
1. How do the subgroups identified by the proposed method compare to existing `rich subgroup’ discovery methods on the four datasets?

2. What were the runtimes for optimizing AVG-SEPFID for the experiments?

3. Given a subgroup (with fractional membership) and a feature with high FID, how do the authors suggest the model or domain expert address this? Moreover, how do you decide what value of AVG-SEPFID is significantly high to signal bias?

4. The approximation bound given by Theorem 1 seems quite weak. Even though the difference between the optimum and the expected FID over the distribution p_g is bounded, the expected difference for each g (E[FID(j,g*)-FID(j,g)]) may still be large. Is it possible to bound such expected difference or give a probabilistic guarantee?

Minor comments / questions: 
- Definition 3: typo: $\frac{1}{n|g|}$ -> $\frac{1}{|g|}$
- What does bound B in Algorithm 1 represent intuitively?
- According to the experimental results regarding coefficients of subgroup functions, it appears that the subgroup functions g are linear functions. Is this a restriction imposed by the proposed algorithm?
- While the FID is useful in the algorithm to optimize for AVG-SEPFID, I don’t think it makes much sense as a fairness notion itself. According to Definitions 1 and 2, separable FID just ends up being $|\sum_X (g(x)-1) F(f_j,X,h)|$, which roughly corresponds to the sum of feature importance of non-group data points.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this work, the authors propose to leverage model interpretability methods to explore fairness problems. Specifically, based on local feature importance methods, they introduced a novel notion, FID (feature importance disparity), as a bias indicator under rich group fairness scenarios. Furthermore, they designed an oracle-efficient algorithm to search the large FID subgroups and claimed the potential utility of the proposed concept in fairness research.

### Strengths
- This paper is informative and well-written.
    
- Combining interpretability with the fairness problem, the idea is interesting.

### Weaknesses
 - Not discussing specific definitions of fairness in the context of rich group fairness can sidestep a certain amount of risk, but does it affect the accuracy of the article and the related discussions?
    
- Section 3 and the proposed algorithm are a little confusing; please refer to the questions.
    
- The main body of the article exceeded the required number of pages.

### Questions
- I'm curious if the assumption about being locally separable is too strong.
    
- In algorithm 1, what is the definition of L?
    
- Are there any specific application scenarios or examples for the proposed FID metrics?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
