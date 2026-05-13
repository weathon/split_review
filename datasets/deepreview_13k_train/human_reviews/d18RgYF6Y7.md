# Fair Classifiers Without Fair Training: An Influence-Guided Data Sampling Approach

- Decision: Reject
- Scores: 5, 6, 5, 5, 5

## Abstract
A fair classifier should ensure the benefit of people from different groups, while the group information is often sensitive and unsuitable for model training. Therefore, learning a fair classifier but excluding sensitive attributes in the training dataset is important. In this paper, we study learning fair classifiers without implementing fair training algorithms to avoid possible leakage of sensitive information. Our theoretical analyses validate the possibility of this approach, that traditional training on a dataset with an appropriate distribution shift can reduce both the upper bound for fairness disparity and model generalization error, indicating that fairness and accuracy can be improved simultaneously with simply traditional training. We then propose a tractable solution to progressively shift the original training data during training by sampling influential data, where the sensitive attribute of new data is not accessed in sampling or used in training. Extensive experiments on real-world data demonstrate the effectiveness of our proposed algorithm.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies learning fair classifiers without implementing fair training algorithms to avoid possible leakage of sensitive information. Its analysis indicates that training on datasets with a strategically implemented distribution shift can effectively reduce both the upper bound for fairness disparity and model generalization error. It also proposes the sampling algorithm FIS to sample influential examples from an unlabeled dataset.

### Strengths
1. Sampling influential examples from an unlabeled dataset based on the combined influences of prediction and fairness is interesting. 
2. The theoretical analysis on the upper bound of the fairness disparity is provided.
3. The experiments on three datasets demonstrate the proposed algorithm is useful.

### Weaknesses
1. The definition 3.1's symbolism is not clear, are $P$ and $Q$ the same as preliminaries? Why use the model trained on P instead of that trained on Q? Could you give more explanation?
2. Assumption 3.2 seems a bit strong. The assumption before Lemma 3.1 that the loss is bounded is not common. Could you give more justification to these assumptions?
3. In the first paragraph in Sec 4.1.1, the assumption of an auxiliary hold-out validation dataset is too strong. For my understanding, test data means that we don’t know the distribution of the data. So I am not sure the reasonability of the assumption.
4. Although it states the computation cost of the proposed algorithm is low, it seems the algorithm needs to pre-calculate the loss for testing the performance of a sample, which is costly.
5. It lacks discussion of how to select the initial training dataset for the warm start (influence when applying different proportions or distributions), and how to determine the solicitation budget $r$ which is the declared a small number of sampling data to gain a better result (both accuracy and fairness).
6. Regarding the experiments, the baselines are not sufficient.

Minors:
1. The symbol used in paper should be unified. Notion of Q and P are not used consistently in Sec 3 and 4.
2. In the proposed algorithm section, the proposed strategy I or II should be in Line 6, and the calculation of prediction's and fairness's influences should be in Line 7, 8.
3. Typo: That -> that in paragraph before Def. 3.2

### Questions
1.	It is not clear about the statement "an appropriate distribution shift can reduce both the upper bound for fairness disparity and model generalization error". I think the Theorem 3.2 tells us that no distribution shifts will help lead to the smaller generalization error bound, and a smaller shift leads to smaller error (straightforward). 
2.	In Eq. 1, if $f$ is a classifier, then $x$ seems to be the feature instead of original data.

### Soundness
2 fair

### Presentation
2 fair

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
The paper proposes a new fair training method when the sensitive attributes are missing. The paper first provides theoretical analyses to show the upper bounds for the generalization error and fairness disparity of the model. For example, their theoretical observations show that the upper bound of the fairness disparity is affected by both distribution shifts and group bias in the data. Based on such analyses, the paper proposes a new sampling strategy that utilizes the influence information of each unlabeled sample to improve the fairness and accuracy of the model. The proposed algorithm is tested on several datasets, including image and tabular datasets.

### Strengths
- The paper focuses on a realistic setting in model fairness, where the sensitive attribute labels are unavailable during the training.
- The paper provides interesting theoretical analyses, including the upper bounds of generalization error and fairness disparity. 
- The paper uses various benchmark datasets, including both image and tabular scenarios, helping to show the multiple applications of the proposed algorithm.

### Weaknesses
 - The paper needs to clarify the connection between this paper and other related works in the fairness literature.
  - For example, one of the important discussions in the paper is about the accuracy-fairness tradeoff, which also affects the main proposed algorithm. However, such a tradeoff between accuracy and fairness has been widely studied (e.g., [1]), so it would be better if the paper could clarify what is the difference between this paper’s analysis and previous discussions in the fairness literature. Specifically, the paper should discuss how the proposed method addresses the inherent accuracy-fairness trade-off, especially given that the method operates without sensitive attribute information during training. It is unclear whether the proposed method simply shifts the trade-off curve or if it offers a fundamentally different approach to balancing accuracy and fairness. The paper should also discuss how the theoretical bounds derived in the paper relate to the existing literature on accuracy-fairness trade-offs.
  - Also, the paper uses the concept of distribution shifts, which is recently extensively studied in the fairness literature, but the paper does not discuss those works (e.g., [2, 3, 4]). It seems the setups of this paper and recent distribution shifts studies in fairness literature are a bit different, as this paper aims to ‘utilize’ an appropriate distribution shift for sampling, while many recent studies focus on ‘solving’ the distribution shifts between training and target distributions for fair training. Thus, it would be much better if the paper could clarify the connection and differences between this work and other distribution shifts studies. The paper should explicitly address how the proposed sampling strategy differs from methods that aim to mitigate distribution shifts, and how the theoretical analysis accounts for the specific type of distribution shift being utilized.
- The paper does not compare with enough baselines in their experiments. For example, there are various algorithms for training fair models without using sensitive attribute information (e.g., [5, 6]), but the paper does not include clear comparisons with those works. The paper should include more baselines that also aim to achieve fairness without sensitive attribute information, and it should also discuss the differences in the underlying assumptions and methodologies between the proposed approach and these baselines.

### Questions
The key questions are included in the above weakness section.

-------------------
[After rebuttal] I read both the responses and the revised paper. As most of my concerns have been resolved, I raised my score.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper studies the fairness problem with a sampling strategy. From the motivation that changing the data distribution would help with the fairness issue, the authors propose to estimation the influence of sample via first-order gradient approach, and re-weight samples individually. Experiments are conducted on images, tabular data, and language to demonstrate their approach.

### Strengths
1. The proposed algorithm is technically sound and straightforward. No access to the sensitive attribute of training data is a good property to have.

2. The presentation is clear and easy to follow.

3. The experimental datasets cover multiple types of data, which is good to have.

### Weaknesses
1. Key reference missing. In [1], the authors also proposed a sampling/reweighing strategy to select good samples based on influence estimation. The algorithm has no access to the sensitive attributes of training data. The two paradigms seem conceptually and technically similar to me. Some discussions are needed in this paper.

2. Weak connection between the theorem and algorithm. I understand the theorem served as a very high-level motivation to change the distribution shift, but from my perspective, it has limited connections to the specific algorithm later on. Also the theorem is closely related to the theorems in domain adaptation established several years ago, so that somehow to be incremental.

3. Since the influence is based on first-order estimation, if there any chance to validate the estimation of influence per sample? Maybe show the actual influence and its estimation would be helpful.

4. The authors consider the accuracy in the algorithm. However, in the experimental section, I didn't see any numerical evaluation for model accuracy. Given the context, involving the model's accuracy and show the tradeoffs between fairness and accuracy make more sense to me.

### Questions
N/A

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper focuses on addressing the challenge of training fair classifiers with limited number of labeled training samples (without access to sensitive attributes) and an unlabelled dataset. Instead of relying on in-processing fairness constraints due to the lack of sensitive attributes and to avoid accuracy-fairness tradeoff, the authors make a theoretical observation that traditional training on dataset with carefully induced distribution shift can decrease the upper bound of fairness disparity and model error. Based on this observation, the authors propose Fair Influential Sampling (FIS) algorithm. FIS leverages the unlabeled dataset to query examples that help in shifting the training data distribution to maximize fairness without compromising accuracy. The effectiveness of FIS is demonstrated empirically using four datasets.

### Strengths
- The problem setting is relevant and interesting.
- The paper addresses the issue of mitigating unfairness without access to sensitive information on the training dataset.

### Weaknesses
 - There is a large body of work to improve fairness without sensitive attributes on training data [1, 2] and also on validation data [3, 4, 5]. Is there a reason why the authors did not compare the performance of FIS against such methods? 
- The related works section lacks discussion about fair active learning frameworks like [6]. In addition, the authors should distinguish the proposed framework from existing fair active learning frameworks and perform an empirical comparison. 
- The paper is missing a comparison with in-processing fairness training algorithms, such as MinDiff [7]. Such a comparison would provide a clearer perspective on any accuracy-fairness trade-offs advantages that FIS may entail.
- How are the hyper-parameters, such as number of new examples in each round r, number of rounds T, tolerance $\epsilon$, etc., of the training algorithm determined? This question arises because the selection of hyper-parameters appears to be a significant challenge when training fair models, as reported in [2, 4].
- To gain a comprehensive understanding into the effectiveness of the proposed algorithm, it is imperative to conduct a sensitivity analysis that explores the relationship between the labeling budget and the (accuracy, fairness).

### Questions
Please see above

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In fair classification, researchers tend to intervene during pre-processing, training or post-processing. The paper examines how to develop a fair classifier when sensitive attributes are not included in training data and fairness constraints are not employed. The main contributions are theoretical. The theory shows that implementing a distribution shift during pre-processing improves model generalization on average as well as fairness. Building on previous work employing influence functions, the paper suggests sampling influential examples during training.

### Strengths
(1) The idea that better generalization error might also improves fairness performance is an important area of theoretical fairness. There are recent and upcoming papers in a similar vein in applied ML but not as many theory papers

(2) Theorem 3.2 on the upper bound of "fairness disparity" is mathematically interesting and seems to be the main result

### Weaknesses
 (1) Implementing distribution shift as a way to improve generalization is already known in studies of adversarial training and reliable deep learning, but the paper does not engage with this existing literature. Specifically, the paper does not discuss how the proposed distribution shift method compares to adversarial training techniques that also modify the input distribution to improve robustness and generalization. A more thorough discussion of the similarities and differences with methods such as Projected Gradient Descent (PGD) based adversarial training would be beneficial.

(2) Exposition needs improvement throughout for clarity. For instance, the paper states "Our theoretical analysis indicates that training on datasets with a strategically implemented distribution shift can effectively reduce both the upper bound for fairness disparity and model generalization error (Lemma 3.1, Theorem 3.2). This gives us a key insight that fairness and accuracy can be improved simultaneously even with simply traditional training. [Section 3]" How is training on datasets with a strategic distribution shift simple traditional training? And for the second bullet in contributions, the paper states "we sample influential examples" but does not clarify what influence function is used throughout the paper. I see section 4.1.2 but it is not clear to me how this is distinct from the previous definitions in the literature. The paper needs to more clearly define what it means by 'influence' and how it differs from standard influence functions used in areas such as robust learning or data poisoning.

(3) The paper over-emphasizes that sensitive attributes are not used during training, which is pretty standard practice in fair classification. Sure, maybe for post-processing techniques but this particular paper is presenting a technique for pre-processing/during training adjustments. Further, even in work on leave-one-out fairness or influence functions and fairness (analysis of perturbing training data in some way), sensitive attributes are not typically used in training. I notice that these are also areas of related work that the paper does not engage with. The paper should acknowledge that many existing methods also operate without sensitive attributes during training and clarify the specific novelty of their approach in this context.

(4) Related work section needs improvement. The section splits into pre-processing methods and post-processing methods which is not helpful for the main contribution of the paper. The related work should be organized to highlight the similarities and differences with other methods that use distribution shifts, influence functions, or training without sensitive attributes, rather than simply categorizing by pre- or post-processing.

### Questions
1. What is the relationship between the strategic distribution shifts and adversarial training?

2. What is the novelty in section 4? Which parts are restating results from the literature and what parts are new?

3. What is the motivation for employing the distribution shift for this reason? Why is a particular type of shift used? And again, how is this different from adversarial or influence function informed training?

minor:
4. Why are there no captions in the tables?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
