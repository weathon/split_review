# GITD: Enhancing Medical Classification on Tabular Data with Missing Values via Graph Modeling

- Decision: Reject
- Avg Score: 4.80
- Scores: 3, 5, 5, 5, 6

## Abstract
With the advancement of machine learning, various techniques have been developed to classify patients for disease diagnosis using medical tabular data. Due to the presence of missing values in the medical tabular data, these techniques commonly impute the missing values before applying classifiers. However, most existing techniques classify patients solely based on each patient's individual features despite the advantages of leveraging patients with similar features that can enhance both imputation and classification. To address this issue, we introduce graph data imputation for tabular data (GITD), a novel approach that constructs feature-attentive k-nearest neighbor (kNN) graphs to enable the use of graph data imputation methods on medical tabular data. The key idea of GITD is constructing a kNN graph among patients by prioritizing important features for classification. Our extensive experimental results demonstrate that GITD successfully bridges graph data imputation methods and medical tabular classification, achieving state-of-the-art performance across various medical tabular datasets.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors address the problem of imputing medical (tabular) data by
converting the data to a graph and applying a novel graph-related
imputation approach called GITD to the graph data. They show that GITD
imputation yields better classification performance compared with
previously published imputation methods on six medical datasets.

### Strengths
- important problem with no clear-cut solutions

- intuitively appealing idea

- good experimental analysis using six real datasets

### Weaknesses
The principal weakness is that the results, as presented, do not
adequately support the claim that GITD is the state-of-the-art
imputation method for medical data.

Details:

Weakness 1:

- it is not clear how GITD classification is performed. To be
  specific: do you perform imputation using GITD, and then the
  resulting imputed data can be analyzed using any classifier? Or is
  the classifier part of the combined imputation+classification
  algorithm? I can't tell from the text nor from Figure 2, despite
  searching carefully. This is obviously crucial question for
  understanding and evaluating the manuscript

Weakness 2:

- it is not clear how the performance of GITD is compared with prior
  art. For example, mean imputation method imputes the missing data,
  and then applies standard classifiers to the resulting training
  set. The manuscript does not say how the mean-imputed data is
  classified. This is critical: for fair comparison with GITD, we want
  to optimize a classifier to each imputed dataset.  This is a
  challenging problem, because there are, at a minimum, 2 non-trivial
  components: 1) classifier tuning/optimization (including selection
  of classification algorithm) 2) performance comparison, with GITD
  and other methods. There is no adequate information in the
  manuscript how this is being done, and furthermore we don't know if
  it was done rigorously. Without this, the manuscript cannot be
  properly evaluated.

Weakness 3:

- it is not clear how the GITD would be applied in production, i.e.,
  in a clinical setting. Suppose a patient arrives with missing data
  in their clinical record. It is not clear from the manuscript how
  one would classify that patient using GITD approach.

### Questions
INTRODUCTION

"Recent progress in machine learning technology has led to substantial
strides in the medical domain"

The authors should reference the FDA list of cleared AI/ML devices
because it provides significant evidence - arguably, strongest
available evidence - regarding the strides of ML technology in the
medical domain (note: despite the title, all devices on the list are
ML, not AI):

https://www.fda.gov/medical-devices/software-medical-device-samd/artificial-intelligence-and-machine-learning-aiml-enabled-medical-devices

"Among various types of data in the medical domain, tabular data is
one of the most representative forms, consisting of numerical and
categorical features for each patient."

Please rephrase or drop this. There are only a handful of different
forms of medical data (images, tabular, audio, signal, genomic), so
arguably every form is among the "most representative".

"The main challenge in handling medical tabular data is that it often
contains missing values due to various factors, such as private
concerns or incomplete data collection."

private concerns --> privacy concerns

"To handle medical tabular data containing missing values, imputation
techniques that fill in the missing values must be applied prior to
classifiers."

Not true. XGBoost - a major classification algorithm - does not
require imputation. Also, for other classifiers, imputation is not the
only approach for data containing missing values: one could also drop
the data with missing values. Should be mentioned for completeness.

"This is because most classifiers assume that the data is fully observed."

Inconsistent with previous sentence which claims that imputation is
required.

"We demonstrate that graph data imputation methods using feature-attentive kNN graphs
significantly outperform existing state-of-the-art methods in medical classification."

What does this mean? Graph data imputation methods are not
classification methods - they are imputation methods. How are we
comparing imputation methods with classification methods? Please
clarify.


4.3 EXPERIMENTAL SETUP

"For a fair comparison, we generate five random splits for training,
validation, and test samples with proportions of 0.1, 0.1, and 0.8,
respectively."

Is there a reason for the imbalanced split? In the absense of prior
knowledge, I would probably split evenly.

Please clarify this. How exactly (using what data) is the average
Micro-F1 score calculated:

"To evaluate classification performance, we measure the
average Micro-F1 score across the five splits."


APPENDIX B

Table 10: please add meaning of columns to the caption of Table 10.

### Soundness
1

### Presentation
3

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
The paper proposes a similarity approach to impute missing values for classification tasks in the medical domain. The approach consists in three  main phases: 1) Train a DL model with attention; 2) Using a simple aggregation of  the attention weights, normalize the feature vectors to highlight the importance of the relevant features and then create a graph with the KNN (cosine similarity) to generate the corresponding graph edges.  Then use the graph to impute the missing features based on similar weighted rows. 3) Retrain the model with the imputed values using the graph.

Experiments include comparisons to other imputation methods with different levels of sophistication and empirical results in several medical datasets support  the author's claims about the efficacy of the proposed method.

### Strengths
1) The paper is well written, organized and it is mostly self-contained. Experiments adequate within the topics and scope that the paper presents and focus on.

2) The classification algorithm used seems appropriate, although the authors dont discuss the fine tuning process behind the training phase.  

3) The solutions proposed seems relatively easy to implement.

### Weaknesses
1) What thing that is confusing is that the author's don't discuss much what makes this uniquely  suited for medical data, in my opinion this can be applied to any other domain. Can you please elaborate?
2) Privacy is paramount when doing data science / ML with medical data, privacy is mantioned briefly but but not tackled, I think this is a missing opportunity for the paper. Specially because once the graph is created dependency from the original features (untransformed) is not needed. 
3) There are various relevant references missing, for example: 
https://arxiv.org/abs/2210.08258 to name one.
4) I dont think its fair for the comparisons to have some out of memory failures, specially for the ones that ar every competitive. Based on the times when they did not fail, for some experiments, they were very close to the results achieved by the proposed method. Also adding p-values for significance would be helpful to have. 
5) I wonder why the authors didi not include other ways to obtain the feature importance (and compare). For example you could actually repeat the process using Random forests (with gini scores  for feature importance) as the classification algorithm. 
6) Also a regularization term to enforce sparsity and to drive the sum of the attention weights to zero, Like a L1 regularizer might force the algorithm in the first run to choose and focus in the really important features. You could drop (or reduce the weight) the regularization term for the final training phase.

### Questions
Can you please clarify how to do the imputation once the corresponding graph neighbors have been identified? I missed that in the paper.

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposed GITD, a method that applies graph data imputation to medical tabular data by constructing feature-attentive kNN graphs. Through a three-stage pipeline (preliminary training, graph construction, and final training), GITD can handle missing values while emphasizing class-discriminative features. The authors conducted extensive experimental studies on six medical datasets to show that GITD significantly outperformed existing tabular data imputation methods in classification tasks.

### Strengths
1. The proposed method is presented clearly
2. The experiments are extensive. The GITD is compared with seven imputation methods on six medical datasets
3. This proposed method achieves stronger performance than other baselines, demonstrating its great potential for practical use.

### Weaknesses
1. The technical novelty is relatively incremental. Personally, I do not agree that the proposed method is an imputation method. It's more like a classification solution with missing values, as the proposed method is used for classification rather than generating imputed data.
2. As with most multi-step or multi-stage methods, the proposed method faces challenges of tuning more hyperparameters like k in kNN and α in the graph construction stage.
3. Intuitively, the proposed method starts from zero imputed data, then uses the model trained at the 1st stage to select important features and builds a GNN classification model using the kNN graph constructed on the selected features. The authors may consider comparing the proposed method with some other feature selection baselines.
4. The authors may consider giving some theoretical guarantees or intuitive explanations on how the proposed method work.
5. The authors may consider conducting experiments on larger scale datasets.

### Questions
The main questions and suggestions have been detailed in the 'Weaknesses' section.

### Soundness
2

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
The paper proposed a novel graph data imputation for tabular data (GITD) method for medical classification tasks with missing data, which constructs feature-attentive k-nearest neighbor (kNN) graphs to enable the use of graph data imputation methods on medical tabular data. The proposed method was evaluated on six benchmark medical disease classification datasets and multiple baseline methods.

### Strengths
- Originality: the proposed method is potentially a novel combination of existing methods to bridge graph data imputation and medical classification tasks. 
- Quality: the paper is of good technical soundness in terms of experiment designs, benchmark datasets and comprehensive baseline models. The methods comparison and evaluation also includes multiple perspectives on performance metrics, memory usage and time efficiency.
- Clarity: the paper is well-organized with logical flows and different research questions.

### Weaknesses
- Weak technical soundness in results significance: Performance metrics in Table 1, 2, 3,4 & 7 are reported with standard deviations, instead of confidence intervals. This could be misleading in model comparison since single standard error might only account for 68% confidence of better performance. Pls add confidence intervals and adjust the results conclusion accordingly. Some numbers show very close numbers and the proposed method might not win at a statistically significant level. 
- It seems the difference between ATT_kNN and kNN is in number of selected features for graph construction. If incorporating other feature selection approach with the kNN, will the performance be equivalent to ATT_kNN?  (Also, from Table 2, after confidence interval computation, the advantage of ATT_kNN over kNN might be non-significant. )
- A better way to test the feature difference among different classes for Table 8 and 9 should be a statistical test on distributions and report p-values. Still, standard deviation is not a proper error metric. 
- The paper lacks limitation discussion in conclusion.

### Questions
- The proposed method seems to be applicable to non-medical datasets as well. Is there any particular reason to choose medical data? And also is there any result on non-medical data? 
- Could you pls report the missing percentage of the selected features that construct ATT_kNN graph? It'll be interesting to see whether those features with missing values are chosen or not.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents a novel approach for applying graph data imputation methods to medical tabular data. The key idea involves constructing feature-attentive k-nearest neighbor (kNN) graphs to facilitate graph data imputations. The proposed method is evaluated across several medical tabular datasets, demonstrating state-of-the-art performance. Additionally, the authors conduct extensive experiments to assess the optimality of various components of the proposed approach. Discussions on the time complexity and space complexity are also demonstrated.

### Strengths
- The idea of applying graph data imputation to medical tabular data is novel and interesting.
- This paper exhibits a high level of completeness in the experimental evaluation, including the assessment of various components of the proposed approach.
- The writing in this paper is clear and well-structured, making it easy to follow.

### Weaknesses
**About experiments:**

- The proposal relies highly on the assumption that instances with similar discriminative features tend to have similar labels. While this assumption sounds reasonable, it should be empirically validated.
- No sensitivity of the missing rate is provided. Intuitively, when there lacks a significant amount of discriminative features, a graph reconstruction may not be as effective.

**About contributions:**
- Though the idea of applying graph data imputation to medical tabular data is novel, both of the components are existing techniques. Thus, the technical contribution of this paper is limited.

**Minor Issues:**

1. Figures 1 and 2 are both unclear. Using a vectorized format for the figures would be more beneficial for the readers.
2. Lines 201-209 have many verbose sentences as in Lines 183-189. It is recommended that one of them be shortened.
3. Line 379: OOM denotes an out-of-memory error.
4. Typos: Line 194 "raph" should be "graph"

### Questions
- Can the assumption that instances with similar discriminative features tend to have similar labels be empirically validated? See Weaknesses **About experiments** #1.
- How does the proposed method behave when the missing rate is high? See Weaknesses **About experiments** #2.
- Can an end-to-end learning approach be considered for the proposed method? I have no idea whether it is feasible, but it might be interesting to discuss.

### Soundness
4

### Presentation
4

### Contribution
3
