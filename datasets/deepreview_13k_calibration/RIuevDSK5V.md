# ConR: Contrastive Regularizer for Deep Imbalanced Regression

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 8, 6

## Abstract
Imbalanced distributions are ubiquitous in real-world data. They create constraints on Deep Neural Networks to represent the minority labels and avoid bias towards majority labels.
The extensive body of imbalanced approaches address categorical label spaces but fail to effectively extend to regression problems where the label space is continuous. 
Local and global correlations among continuous labels provide valuable insights towards effectively modelling relationships in feature space. 
In this work, we propose \Pn{}, a contrastive regularizer that models global and local label similarities in feature space and prevents the features of minority samples from being collapsed into their majority neighbours. 
\Pn{} discerns the disagreements between the label space and feature space, and imposes a penalty on these disagreements. \Pn{} addresses the continuous nature of label space with two main strategies in a contrastive manner: incorrect proximities are penalized proportionate to the label similarities and the correct ones are encouraged to model local similarities.
\Pn{} consolidates essential considerations into a generic, easy-to-integrate, and efficient method that effectively addresses deep imbalanced regression.
Moreover, \Pn{} is orthogonal to existing approaches and smoothly extends to uni- and multi-dimensional label spaces. Our comprehensive experiments show that \Pn{} significantly boosts the performance of all the state-of-the-art methods on four large-scale deep imbalanced regression benchmarks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces a contrastive learning approach to address the issue of imbalanced regression. This method is orthogonal to existing solutions and has demonstrated promising experimental results.

### Strengths
1. Data imbalance and the fairness of machine learning algorithms are practical issues that warrant significant attention.
2. The method is reasonably designed and has shown good experimental results.

### Weaknesses
1. While the paper presents a contrastive learning paradigm adapted for regression, it does not appear to directly address the issue of data imbalance. It would enhance the paper if the authors could clarify how the method specifically tackles this challenge or consider adapting the technique to more explicitly focus on imbalanced datasets. The current approach seems to apply contrastive learning to regression, but the connection to imbalanced data is not clearly established. For example, it's unclear how the proposed method handles the under-representation of minority classes during the contrastive learning process, and whether it introduces any bias towards majority classes.
2. Comparisons should be made with other contrastive regression learning methods (e.g., [a]). Specifically, the paper should compare against methods that also use contrastive learning for regression, to understand the relative advantages and disadvantages of the proposed method. The current comparison is insufficient to demonstrate the novelty and effectiveness of the proposed method.
3. The manuscript could be strengthened by providing some theoretical analysis and insights to support the empirical findings. The lack of theoretical analysis makes it difficult to understand the underlying mechanisms of the proposed method and its convergence properties. For instance, it would be beneficial to see an analysis of how the contrastive loss function affects the feature space and how it specifically helps with imbalanced regression.
4. It would be beneficial if the authors could provide the pseudocode for the algorithm to facilitate the readers' comprehension of the algorithm's details. Without the pseudocode, it's difficult to understand the precise implementation of the proposed method, including the anchor selection process and the negative pair selection strategy.

### Questions
Given the distinct advantages of data augmentation under the contrastive learning framework, are the baseline methods utilizing their typical data augmentation strategies, or those consistent with contrastive learning? If it's the former, a comparison showcasing results after aligning the augmentation techniques would be valuable.

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper addresses the imbalanced regression problems where the label space is continuous. The proposed contrastive regularizer is to model global and local label similarities in feature space and prevent the features of minority samples from being collapsed into their majority neighbours. The proposed ConR consolidates essential considerations into a generic, easy-to-integrate, and efficient method that effectively addresses deep imbalanced regression. The empirical study shows that ConR significantly boosts the performance of SoTA methods on four large-scale deep imbalanced regression benchmarks.

### Strengths
1. This paper is well-written and easy to understand.
2. The novelty of this paper is good. To my knowledge, applying contrastive learning to imbalance regression is novel.
3. The authors provide a new dataset with 2-dimentional label space by using MPIIGaze, which could be useful to the imbalance regression community.

### Weaknesses
1. The proposed objective in Eq. (4) is relative hasty, without the reason of introducing the ordinary regression loss. Also, the definition of the introduced loss should be clearly provided.
2. No deviation measure in the experimental results.
3. No experimental result for the ConR-only case. All the results for the proposed ConR are with respect to the combination with existing methods as a regularized. Due to supervised information is already used in the loss of ConR, its preformation should be provided as a baseline.
4. Some references are missing, e.g., Page 16.

### Questions
1. In the selection of anchor, if an example without any negative example, it will not be chosen as an anchor. What is the main reason for this selection? Do you consider the contrastive learning method without negative pairs, such as BYOL and SimSiam?
2. The empirical label distribution is needed to determine the pushing weight for the negative pair. In addition, the authors suggest using the inverse frequency to compute the pushing weight, so that the minority samples will obtain harder force to be repelled from the anchor. How can we determine the continuous weight with the discrete frequency? Do we need any kernel density estimation technique?
3. Please explain the specific reason for combining the proposed loss with the ordinary regression loss in Eq. (4) with more details and evidence.
4. I notice some failure case in Table 1, Table 2, and Table 3, when adding the ConR loss as the regularization term. It is strange that you can down-weight of $\beta$ to avoid this situation. I understand that the main goal is to improve the performance on *Few* case, however, there are still some cases that the performance on *Few* case drops. Also, there are some cases that the performance on *All* case drops. Hence, please provide the explanation for this phenomenon and what is the specific metric for a good imbalanced regression in your paper. I think the *Few* case should be much more important.
5. Why the results on the *Few* case of Balanced MSE in Figure 3 is inconsistent to that in Table 3?

### Soundness
3 good

### Presentation
3 good

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
The paper addresses the problem of imbalanced problem in real-world data. To tackle the imbalance in continuous label spaces, the authors introduce a contrastive regularization technique named ConR, which is based on infoNCE. This technique simulates both global and local similarities between labels in the feature space, preventing the features of minority samples from being overshadowed by those of majority samples. ConR primarily focuses on discrepancies between the label space and the feature space and penalizes these differences. Indeed, this is also an augmentation method rather than re-weighted method in DIR.

However, this work contains several weakness, which is discussed below.

### Strengths
1. ConR presents a novel auggmentation approach to handle the imbalanced problem in continuous label spaces, whose problem is important.

2. The methods of regularizing process of **ConR** by pulling together positive pairs and relatively repelling negative pairs seems solid.

3. The results seem to indicate that the proposed method can be seamlessly integrated with other models and exhibits improvements over existing baselines.

### Weaknesses
1. While the author claims that **ConR** reduces prediction error, are there any theoretical insights or guarantees supporting the idea that **ConR** can achieve a lower generalization bound? Relying solely on empirical results might not suffice to attest to the superiority of the proposed methods.

2. I am curious about complexity. When performing augmentation on large-scale datasets, sampling might increase the complexity. This leads to a prevalent question: Why not leverage reweighting methods which can attain comparable (or potentially superior) results without the significant memory and time overhead associated with the augmentation step? [1,2]

3. While AgeDB-DIR, IMDB-WIKI-DIR, and NYUD2-DIR are structured in DIR [3], and MPIIGaze-DIR is a creation of the authors, a comprehensive description of each dataset should be included in the Appendix. Moreover, given the variety of metrics in NYUD2-DIR, the rationale behind selecting only two needs clarification.

4. The experiments did not surpass all baselines. For instance, in Table 2, the combination of **LDS + FDS + RankSim** posts the best results in terms of GM in few-shot case.

5. For larger datasets like IMDB and NYUD2, **ConR** doesn't consistently outperform other models. However, it seems to excel with smaller datasets such as AgeDB and MPIIGaze.

6. Examining Table 1, the reported results are as follows:

| model | few |
| :---------: | :------: |
|FDS + RankSim|  9.68 |
|FDS + RankSim + **ConR**| 9.43 |
|LDS + FDS + RankSim| 9.92 |
|LDS + FDS + RankSim + **ConR**| 9.21 |
|||

Further analysis is warranted. For instance, why does **LDS + FDS+RankSim** underperform compared to **FDS + RankSim**? Yet, with the addition of **ConR**, it achieves superior results. This observation hints that **ConR** might enhance outcomes when paired with **LDS + FDS + RankSim**. However, this theory doesn't hold when assessed on IMDB-WIKI-DIR. A more detailed analysis of the experimental results is recommended.

### Questions
See Above. Overall, this work is novel, and interesting. The problem they try to solve is imporant, and results seems good. Nonetheless, I strongly recommend the authors to delve deeper by: 

(1) **theoretical insights or guarantees** supporting the efficacy of the proposed method, and 

(2) **thorough empirical analysis of the experimental outcomes**.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
For imbalanced regression, the authors propose ConR, which uses
supervised contrastive loss as part of the loss function.  They define
Sim(label1,label2) > omega, a threshold hyperparameter, as similar
labels.  For each of the input instances, it generates two augmented
instances.  If the actual labels of two augmented instances are
similar, they form a positive pair.  If the predicted labels of two
instances are similar, but the actual labels are not, they form a
negative pair.  For an augmented instance, a set of positive samples
and a set of negative samples are found.  Augmented instances with at
least one negative sample are called anchors, which participate in
contrastive loss.  For each anchor, the fraction in the regular
contrastive loss is summed over all positive samples.  For the
negative samples in the denominator, they have a "pushing weight" S,
which is a function of the density-based weight of the anchor and the
Sim(anchor_label, negative_sample_label).  L_conR is an average of the
contrastive loss of up to 2N anchors. The overall loss is a weighted
sum of the regular regression loss and L_conR.

ConR was evaluated on 4 datasets, one of which has
multi-dimensional labels, and compared with 4 recent techniques.
Empirical results indicate adding ConR generally improves performance.

### Strengths
Imbalanced regression is an interesting problem.
The proposed technique adapts supervised contrastive loss from
classification to regression.  Particularly, they added a pushing
factor for the negative samples based on similarity in labels and density, 
which is interesting.  Also, negative samples have not just
different labels but also similar predictions.  Empirical results
indicate adding ConR generally improves performance.

### Weaknesses
The proposed contrastive loss, Eq 1, could be further explained and
justified.  Empirical evaluation could be improved by adding "ConR
only" and representations of RankSim and Balanced MSE, which are more
recent techniques.  The similarity threshold omega seems to be an
important parameter, further insights could be explored.

More details are in questions below.

1. Eq 1, the outermost summation: Summing over i's implies j's with more
   positive samples would have more contribution.  Is that desirable?  If so,
   what is the main reason?

2. L_R is on the original instances, while L_conR is on 2
   augmentations of each of the original instances.  That is, the
   original instances are not directly involved in L_conR--is that
   correct?  If so, what is the main reason?

3. Similarity threshold omega between labels dependent on
   applications and range of the labels (1-100 vs 1-10^6), any
   further insights?  It seems to be trial and error as a
   hyperparameter.

4. How does ConR alone, not inconjunction with another technique,
   perform?  Including it in Tables 1-3, would be beneficial.

5. How do the representations from Balanced MSE and RankSim, which are
   more recent, compare with ConR.  Including them in Fig 4 would be
   important.

6. In Fig 5, why 1/omega, instead of omega, is used?  In the approach
   section, 1/omega was not discussed. "Fig. 5b, choosing a higher
   similarity threshold"--it seems similarity threshold omega is
   smaller at 1 (1/omega is higher).

7. p9: Could you further explain: "sharing feature statistics to an
   extent that is not in correspondence with the heterogeneous
   dynamics in the feature space"?

8. Sec 3.2.1: how are the instances augmented?  It seems to be not
   discussed in the approach or experiments.

Comments:

Sec 3.2.2: for completeness, f_S could have more description (it seems
to be a simple product in the appendix)

minor:

Eq 3: 1/2N assumes all 2N augmented instances are anchors, but some
might not be anchors (if I understand correctly).

Kang et al. 21 and Khosla et al. 20 have duplicated entries in
References.

### Questions
1. Eq 1, the outermost summation: Summing over i's implies j's with more
   positive samples would have more contribution.  Is that desirable?  If so,
   what is the main reason?

2. L_R is on the original instances, while L_conR is on 2
   augmentations of each of the original instances.  That is, the
   original instances are not directly involved in L_conR--is that
   correct?  If so, what is the main reason?

3. Similarity threshold omega between labels dependent on
   applications and range of the labels (1-100 vs 1-10^6), any
   further insights?  It seems to be trial and error as a
   hyperparameter.

4. How does ConR alone, not inconjunction with another technique,
   perform?  Including it in Tables 1-3, would be beneficial.

5. How do the representations from Balanced MSE and RankSim, which are
   more recent, compare with ConR.  Including them in Fig 4 would be
   important.

6. In Fig 5, why 1/omega, instead of omega, is used?  In the approach
   section, 1/omega was not discussed. "Fig. 5b, choosing a higher
   similarity threshold"--it seems similarity threshold omega is
   smaller at 1 (1/omega is higher).

7. p9: Could you further explain: "sharing feature statistics to an
   extent that is not in correspondence with the heterogeneous
   dynamics in the feature space"?

8. Sec 3.2.1: how are the instances augmented?  It seems to be not
   discussed in the approach or experiments.

Comments:

Sec 3.2.2: for completeness, f_S could have more description (it seems
to be a simple product in the appendix)

minor:

Eq 3: 1/2N assumes all 2N augmented instances are anchors, but some
might not be anchors (if I understand correctly).

Kang et al. 21 and Khosla et al. 20 have duplicated entries in
References.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
