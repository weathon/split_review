# Estimating Conditional Mutual Information for Dynamic Feature Selection

- Decision: Accept
- Avg Score: 7.33
- Scores: 8, 6, 8

## Abstract
Dynamic feature selection, where we sequentially query features to make accurate predictions with a
minimal budget,
is a promising paradigm to reduce feature acquisition costs and provide transparency into a model's predictions.
The problem is challenging, however, as it requires both predicting
with arbitrary feature sets and learning a policy to identify
valuable selections. Here, we take an information-theoretic perspective and prioritize features based on their mutual information with the response variable.
The main challenge is implementing this 
policy,
and we design a
new
approach that estimates the
mutual information
in a discriminative
rather than generative
fashion.
Building on our approach,
we then introduce several further improvements: allowing variable feature budgets across samples, enabling non-uniform feature costs,
incorporating prior information, and exploring modern architectures to
handle partial inputs.
Our experiments show that
our method provides consistent gains over recent
methods across a variety of datasets.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper studies the problem of dynamic feature selection (i.e., adaptively acquire features based on previously acquired ones), where the ultimate goal is to classify each data instance using a small subset of the available features. A greedy approach, termed DIME, is proposed, where feature selection is based on the conditional mutual information (CMI) with the response variable. The paper focuses on estimating CMI in a discriminative fashion, and then trains two networks to implement the feature selection policy. Furthermore, the paper discusses how to handle non-uniform costs across features, prior information and variable feature budgets. A number of experiments on tabular and image datasets are provided that showcase the performance of DIME in contrast to prior work on the area of dynamic feature selection.

### Strengths
+ The paper studies a very important and timely problem, i.e., dynamic feature selection with a minimal budget.
+ A new greedy algorithm is proposed that estimates CMI in a discriminative fashion.
+ The paper discusses how to handle common issues happening in practice, e.g., non-uniform costs, variable feature budgets, etc.
+ Theoretical results are provided that lead to an unbiased estimator of CMI.
+ The paper is well-written and effort has been put to clarify its contributions.
+ The performance of the proposed algorithm is illustrated on a number of datasets and compared with existing methods.

### Weaknesses
 - I believe that some relevant wont on dynamic feature selection that is neither RL-based nor greedy-based is missing (see references below)
- The performance improvement of DIME wrt to one of the baselines (i.e., Argmax Direct) is small (especially for the tabular datasets).
- The paper claims that DIME only accounts for non-uniform costs and variable feature budgets, but I am pretty sure that some of the RL-based methods handle such settings too.
- The really bad performance of the RL-based methods compared to the greedy methods, including DIME, is quite surprising to me and I am wondering if this is some kind of typo.
- The introduction of the paper strongly suggests that RL-based methods are not good alternatives for the problem studied in the paper. However, it seems that there is limited work to suggest that in addition to the fact that it is not for sure that RL is worse, since there are many factors that can influence the final result (e.g., the objective a method optimizes or even the datasets selected for the experiments).


### Questions
(1) I believe that the following set of references also study dynamic feature selection, but from a different perspective than the references presented in the paper. Specifically, they formulate the problem as POMDP and study the theoretical properties of the optimum solution, which enables them to design fast algorithms for dynamic feature selection. They also give bounds on the expected number of features needed to achieve a specific accuracy level. Finally, the latter paper uses mutual information to also drive dynamic feature selection. I think that after reviewing these papers, the authors would agree with me that this is relevant work and they should consider citing them for completeness.
 
- Liyanage, Y.W., Zois, D.S. and Chelmis, C., 2021. Dynamic instance-wise joint feature selection and classification. IEEE Transactions on Artificial Intelligence, 2(2), pp.169-184. 

- Liyanage, Y.W., Zois, D.S. and Chelmis, C., 2021. Dynamic Instance-Wise Classification in Correlated Feature Spaces. IEEE Transactions on Artificial Intelligence, 2(6), pp.537-548. 

(2) I also believe that the algorithms proposed in the previous references as well as (Janisch et al; 2019) are designed to handle non-uniform costs and variable feature budgets. I think this need to be clearly stated in the paper, since at the moment, it is suggested that only DIME can accommodate such settings.

(3) The performance of DIME is very close to Argmax Direct. What is the benefit of using DIME instead of Argmax Direct in that sense?

(4) My major concern is the really surprisingly bad performance of RL-based methods compared to the greedy methods, including DIME. The reason is that I see the RL-based methods as a way of implementing dynamic programming, which is the optimal thing to do, and should be better than greedy methods. Of course, RL has its own issues, but I am still wondering if the performance improvement observed in the experiments is due to using more powerful neural networks to approximate the selection process and not the greedy nature of the method. In addition, it may be because the RL-based methods that DIME is compared with use different criteria than mutual information (excluding the missing references above). Finally, I believe that the RL-based methods consider the cost of features during their decision making process. Is it possible that the results presented in the paper have misspecified this parameter? May be an ablation study  would help me better justify the above surprising behavior of RL-based methods compared to DIME

(5) I noticed in the Appendix that features are in groups. Does DIME use the group structure somehow?

(6) It is unclear to me from the description in the paper if DIME uses a hard feature budget constraint for each data instance or an average constraint or something else. May be you can clarify this?

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The work is devoted to the problem of dynamic feature selection. The authors propose to estimate – learn – Conditional Mutual Information (CMI) of the next feature given the past selected ones. The learning is based on the incremental loss improvements of a given predictor (simultaneously learned with the CMI). It is proven that, for cross entropy loss, the optimal learning point will be CMI. The paper also contains experiments on several datasets that demonstrate better performance of the proposed method in comparison to several baselines.

### Strengths
-	Clear problem setup
-	Large volume of experiments

### Weaknesses
 - Comparison with baselines (see questions)
- It looks like incorporating prior information and variable feature selection constitute 2/3 of the overall work contribution, but they seem more-or-less incremental things (i.e., given such a task a practitioner would easily reproduce Sections 4.2 and 4.3 having Section 4.1). More non-trivial insights would be nice to see in the main contribution.

### Questions
1.	As far as I understand, the authors propose a method to learn CMI improvement. It would be nice to compare this method to the ones, where CMI is approximated in the direct statistical way. For instance, there is a lot of approaches like MIM, MIFS, mRMR, JMI, CMICOT, etc. See for a brief overview of them in [Shishkin, A., et al. “Efficient high-order interaction-aware feature selection based on conditional mutual information”, NeurIPS 2016]. Could you please compare your approach with such statistical methods? Including, in experiments. Is it true that the gain we obtain from learning CMI improvement over statistical methods is cost effective? (learning consumes more computation => on the same level of computation costs, we can get more from statistical methods, right?)


2.	Returning back to [Shishkin, A., et al. “Efficient high-order interaction-aware feature selection based on conditional mutual information”, NeurIPS 2016], we can see that greedy approach of selecting features one by one is not the best way. The ideal approach is to select the best subset of features (which is computationally and dimensionally infeasible). But we at least can select features not one-by-one, but taking into account interactions between selecting features (like in CMICOT). Is there any way to incorporate that approach into the work of the authors?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose DIME a dynamic feature selection (DFS) method that is based on two neural networks, aiming to maximize prediction accuracy while balancing the cost of acquiring features. Specifically, a value network is designed to estimate the conditional mutual information (CMI), $I(y;x_i∣x_S)$, and a prediction network is used to make predictions based on the currently selected features. Both networks are jointly trained. If the acquisition costs for features are known, the objective aims to select the feature that maximizes $I(y;x_i∣x_S)/c_i$, where $c_i$ is the acquisition cost of $i$'th feature. In the experiments, DIME is compared against both static and dynamic feature selection methods on various (tabular and image) datasets. The results show that DIME outperforms the competitors in terms of predictive performance and effectiveness (i.e., number of selected features).

### Strengths
1.) The research investigates various policies for feature selection, such as RL, imitation learning, and a greedy policy based on CMI.

2.) The introduction of the Predictor Network and Value Network, which jointly work to estimate Conditional Mutual Information (CMI) is interesting and represents a novel approach.

3.) The theoretical parts of the paper provide a solid foundation for the approach.

4.) The experimental evaluation is quite comprehensive.

### Weaknesses
1.) While the incorporation of acquisition costs with CMI estimates is straight-forward, the acquisition costs appear to be an artificial supplementary add-on to the methodology.

2.) Some related approaches should be mentioned in the related work section and could have been considered as competitors

Incremental permutation feature importance (iPFI): towards online explanations on data streams (Machine Learning 2023)
F Fumagalli, M Muschalik, E Hüllermeier, B Hammer

Leveraging model inherent variable importance for stable online feature selection (KDD 2020)
J Haug, M Pawelczyk, K Broelemann, G Kasneci

3.) It is not quite clear how prior information is factored into and affects the feature selection policy; this part should be better explained.

4.) An exact algorithmic representation should be used to provide clarity on the interplay between the networks, the CMI estimation, the use of prior information, and how the features are finally selected in various scenarios.

### Questions
See weaknesses 3.) and 4.) from above.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
