# Consistent Multi-Class Classification from Multiple Unlabeled Datasets

- Decision: Accept
- Scores: 6, 6, 8, 8, 6

## Abstract
Weakly supervised learning aims to construct effective predictive models from imperfectly labeled data. The recent trend of weakly supervised learning has focused on how to learn an accurate classifier from completely unlabeled data, given little supervised information such as class priors. In this paper, we consider a newly proposed weakly supervised learning problem called multi-class classification from multiple unlabeled datasets, where only multiple sets of unlabeled data and their class priors (i.e., the proportions of each class) are provided for training the classifier. To solve this problem, we first propose a classifier-consistent method (CCM) based on a probability transition matrix. However, CCM cannot guarantee risk consistency and lacks of purified supervision information during training. Therefore, we further propose a risk-consistent method (RCM) that progressively purifies supervision information during training by importance weighting. We provide comprehensive theoretical analyses for our methods to demonstrate the statistical consistency. Experimental results on multiple benchmark datasets and various prior matrices demonstrate the superiority of our proposed methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The authors study the challenge of weakly supervised learning with a focus on multi-class classification from multiple unlabeled datasets. They propose two methods: the Classifier-Consistent Method (CCM), which utilizes class priors and a probability transition function for training, and the Risk-Consistent Method (RCM), which aims to enhance the CCM by ensuring risk consistency through importance weighting to refine supervision during training. The study claims the superiority of these methods, supporting them with comprehensive theoretical analyses for statistical consistency and positive experimental results across multiple benchmark datasets.

### Strengths
1. The paper presents a novel approach based on statistical learning theory to solve the problem of multi-class classification from multiple unlabeled datasets and the theoretical guarantees of the estimation error bounds strengthen the claims regarding its effectiveness.
2. The authors provide a clear and comprehensive description of their methodology, which enables other researchers to reproduce their results.

### Weaknesses
1. The methods and the corresponding theory presented in the paper are sound and relevant, but the lack of sufficient originality and novelty compared to a previously published work [1,2] could be a limitation. Therefore, the authors should carefully consider these points and take the necessary steps to distinguish their work and demonstrate its original contributions.

   [1] Feng, L., Lv, J., Han, B., Xu, M., Niu, G., Geng, X., ... & Sugiyama, M. (2020). Provably consistent partial-label learning. Advances in neural information processing systems, 33, 10948-10960.

   [2] Kobayashi, R., Mukuta, Y., & Harada, T. (2022). Learning from Label Proportions with Instance-wise Consistency. *arXiv preprint arXiv:2203.12836*. 

2. Employing the direct outputs of a network to estimate the posterior probabilities $p(y=j∣x)$ can be imprecise, particularly under the extreme weak supervision scenario where only class prior probabilities serve as supervisory signals. In such a setting, the network predictions may not align well with the true posterior distributions, leading to suboptimal performance.

3. In Theorems 3.5 and 3.7, the assumptions regarding the Lipschitz continuity of the loss function present an indeterminable strength which could affect the assessment of the model's robustness. Furthermore, the generalization error bound incorporates a summation over $k$ categories of the Rademacher complexity, which may result in a rather loose bound. 

4. The use of subscripts $i$ and $j$ appears to be somewhat confusing and may lead to difficulty in understanding for the reader. Specifically, the subscripts switch between $i$ and $j$, which could introduce ambiguity in distinguishing between the elements associated with the k-dimensional vector $\eta(x)$ and the m-dimensional vector $\bar{\eta}(x)$. Clarity in the mathematical notation is crucial for the precise communication of such theoretical results.

### Questions
Seen weaknesses.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes two algorithms (CCM and RCM) to classify multiple classes from multiple datasets using only class proportion information. They provide theoretical guarantees on the accuracy of their methods and show some experimental results.

### Strengths
I am not familiar with the related work. e.g. LLP, but the overall proposed method seems interesting and sufficiently novel. The proofs in the appendix seem reasonable and the additional experiments there exhaustive enough.

### Weaknesses
- See questions
-	There is typo / the sentence got broken up here: “where d is a positive integer denotes the input dimension. [k] = “
-	This is not grammatically correct / does not make sense “multiple-instance learning (Zhou et al., 2009)) could usually have access to weakly supervised labels.”

However, the paper is badly written (there is barely any explanation of anything; the appendix in some ways is more clear than the main paper!) and very difficult to understand. This is the biggest flaw of the paper, and makes it difficult to evaluate the paper accurately.

### Questions
-	The author’s state that Section 2.2 that in MCMU has the data generating process P(X|y) P(y|c) P(c) which seems reasonable, but that the generating process of LLP is P(y|X)? That would make sense as the modelling distribution (learning a discriminative function), but not as a data generating process? Also where is the class priors in the data generating process of LLP?
-	What are the class priors? The proportion of y_i for each of the k classes?
-	Section 2.4 is kind of randomly there without any introduction and it could be “cleaned up”. 
-	What is WSL?
-	The proposed method is extremely unclear. The paper needs to explain more of its proposed approach instead of spending large parts of the text comparing to other papers e.g. Lu et al. and describing their approach as an extension / variation of other papers. (Note: this also unintentionally make it sound less novel)
-	The main idea of CCM seems to be that by converting the problem from classifying multiple classes in multiple datasets, it can be simplified into classifying which dataset the X sample comes from? And this equivalency is due to a deterministic transition function T() which is based on \rho the probability a datapoint belongs to a dataset, \theta the proportions of each class for each dataset, and \pi the proportion of each “class” over all datasets? 
-	The problem setup seems very restrictive / artificial. There has to be the same number of classes for each dataset and the classes are “ordered” / aligned across multiple datasets? Also while the problem of classifying which dataset a sample belongs intuitively is “easier”, it is not clear how that solves the problem of which class within which dataset a sample belongs to. Multiplying by the proportions of dataset size and class size will “on average” get you probabilities on the latter problem, but this is just a math trick to achieve a bound. It is not clear how this works practically. The experiments seems to indicate it works, it is just extremely unintuitively how / explained badly.

### Soundness
3 good

### Presentation
1 poor

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper focuses on a newly proposed weakly supervised learning problem called multi-class classification from multiple unlabeled datasets (MCMU), where only multiple sets of unlabeled data and their class priors are provided in the training process. To solve this problem, this paper proposes two methods, including a classifier-consistent method (CCM) based on a probability transition function and a risk-consistent method (RCM) based on importance weighting. Additionally, theoretical analyses of the proposed methods and experimental results on multiple benchmark datasets are provided.

### Strengths
1. This paper studies a newly proposed weakly supervised learning problem called multi-class classification from multiple unlabeled datasets (MCMU), and proposes two effective methods, which could avoid the negative risk issue commonly encountered by previous unbiased risk estimator methods.
2. Theoretical analyses are provided to show the theoretical guarantees of the proposed methods.
3. Comprehensive experimental results on multiple benchmark datasets across various settings demonstrate the effectiveness of the proposed methods.
4. The paper is well organized and well written, which makes it easy to follow.

### Weaknesses
1. There is a lack of descriptions of Theorem 3.5 and Theorem 3.7. Additionally, could we compare RCM and CCM from a theoretical perspective?
2. The analysis in section 4.3 is interesting. However, there is a lack of discussion about the observation from Fig. 1. So, could the authors provide more details of why CCM is more robust when few data points are provided?
3. I noticed that in all experimental settings, the number of sets is greater than or equal to the number of classes. Could the authors provide a discussion where the number of sets is less than the number of classes?

### Questions
I have listed the questions in the weaknesses above. Please address them.

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper investigates an interesting weakly supervised learning problem called multi-class
classification from multiple unlabeled datasets, where only multiple sets of unlabeled data and their
class priors (i.e., the proportions of each class) are provided for training the classifier. To tackle this
problem, this paper first gives a multi-class extension of a previous work on binary classification from
multiple unlabeled datasets. However, this paper says that such a method still has several
disadvantages that limit the performance. So this paper further proposes a risk-consistent method that
can avoid those disadvantages and maintain theoretical guarantees. Experimental results support the
claim of this paper.

### Strengths
- Problem. This paper investigates the problem of multi-class classification from multiple unlabeled
datasets, which is interesting problem.
- Method. To solve the problem, this paper proposes two methods. The first one is a classifierconsistent method, which is a multi-class extension of a previous work on binary classification. The
second one is a risk-consistent method that can address the shortcomings of the first one.
- Theory. This paper gives theoretical analysis for the two methods proposed in this paper.
- Performance. From the experimental results, we can find that the classifier-consistent method can
achieve good performance compared with previous methods, and the risk-consistent method
outperforms all the methods. Some ablation studies also support the risk-consistent method.

### Weaknesses
- This paper has proposed two methods (CCM and RCM) to solve the problem and showed that the
second method is better than the first method. I think that there lacks a separate paragraph that is
specially for describing the difference between RCM and CCM in detail.
- This paper should give more explanations for the theoretical findings. For example, there are no
discussions or descriptions on Theorem 3.5 and Theorem 3.7.

### Questions
- What can we learn from Theorem 3.5 and Theorem 3.7?
- What is the relationship between the studied problem and the unlabeled-unlabeled learning problem
[Lu et al. (2019)]?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces a novel approach to weakly supervised learning, specifically targeting multi-class classification from multiple unlabeled datasets with class priors. It addresses limitations identified in Tang et al., 2022, and offers two distinct approaches: a classifier-consistent method using a probability transition matrix and a risk-consistent approach employing importance weighting. However, certain areas require further clarification and empirical investigation.

### Strengths
- The paper successfully addresses limitations observed in the MCMU method and presents an alternative solution, expanding the landscape of weakly supervised learning.
- The introduction of a novel approach focusing on empirical risk minimization (ERM) at the instance level, treating individual data points, stands out as a significant strength.

### Weaknesses
- The experimental comparison is somewhat limited, primarily featuring methods from Tang et al., 2022. While justified due to MCMU's novelty, including additional weakly supervised methods could provide valuable reference points. Moreover, presenting accuracies for fully supervised learning on the same train/test splits would enhance the evaluation.
- The paper lacks a comprehensive study of the method's limitations, particularly with regards to constraints on parameters such as m (the number of unlabeled sets) and n_i (the number of data points in each set), which are crucial for practical applicability.
- Theoretical results like Theorem 3.5, which establishes an upper bound for the difference between true and empirical risk, would benefit from discussion regarding their practical implications and their relationship to the actual classification task involving class labels.

### Questions
1. The paper could further investigate the impact of small m (few unlabeled sets) and significant variations in label proportions across sets on the generalizability of its results with respect to m and n_i.
   
2. A clarification regarding the difference between Lemma 3.1 in the paper and Theorem 1 in Lu et al., ICML 2021, would be valuable for readers.

3. Given that label proportions in real-world scenarios may only slightly differ, the paper should outline constraints on parameters m and n for practical significance, especially considering that a large m may be necessary for the method's effectiveness.

4. A discussion on the practical relevance of the derived upper bound in Theorem 3.5 and its connection to the actual classification task involving class labels would provide valuable insights.

5. The observation that the proposed approach performs significantly worse under certain settings, such as a random class prior matrix and non-constrained m, should be supported by clearer details on how test accuracies were computed, whether test data were balanced, and if class size variations in datasets played a role.

Other suggestions:

"In MCMU, given the class priors, the data points in the same set are independent from each other, while in LLP, given the label proportions, the data points in
the same set are dependent from each other."

The second part of the sentence should clearly state whether data points are "independent from each other" or "dependent on each other." If it implies independence, it raises a significant ambiguity regarding how MCMU and LLP fundamentally differ, as class priors and label proportions are practically equivalent concepts. Moreover, there appears to be a conceptual misuse in the paragraph. Data points within each class are typically assumed to be independent, conditioned on their class labels. The statement in question uses "class priors" in place of "class labels", which could introduce confusion and should be clarified. Overall, given that label proportions and class priors are practically the same thing in the context studied by the papers it is hard to see any difference from a dependence perspective between the two approaches. 

I think using the term "label proportions" when referring to class priors within each set would be more appropriate. In fact what the paper denotes as the j-th class prior of the i-th unlabeled set can be denoted as the label proportion of class j in dataset i. This would distinguish label proportions from class priors estimated using data from all available unlabeled sets.


In Section 4.1. "The ni data points contained in i-th unlabeled set were randomly generated according to ..." Isn't this supposed to be "randomly sampled" or "drawn".  Data already exists... nothing is supposed to be generated.

It would greatly enhance the paper if, within the related work section, an early explanation were provided regarding the reasons behind the possibility of negative empirical risk in these methods (Lu et al., 2019; Tsai & Lin, 2020; Tang et al., 2022). This proactive approach would help readers anticipate and better understand the issues related to negative empirical risk that the paper seeks to address.

In page 4 i is used for indexing both the sets and data points. It may cause confusions. 

In Theorem 3.6 the paper defines this probability p(y=j|\bar{y},x)as the probability of x in \bar{y}-th unlabeled set whose ground-truth label is j. Isn't this supposed to be the probability of x in \bar{y}-th unlabeled set belonging to class j? x may or may not belong to class j. x's ground truth label is not necessarily j. 

Theorem 3.6 also considers p(x|y=j)=p(x|y=j,\bar{y}) as a fact. However, this is not necessarily true. The first one is the conditional distribution of class j estimated using all data belonging to class j whereas the second one is the conditional distribution of class j estimated using only data from unlabeled set \bar{y}. So, from an empirical standpoint these distributions are not equal. Please clarify.


After Rebuttal:

Thanks for taking the time to do those extra comparisons I mentioned. It’s helpful to see how your method holds up with different 'm' values and varying levels of class imbalance. Based on these new results,  I'm happy to bump up my score by one.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
