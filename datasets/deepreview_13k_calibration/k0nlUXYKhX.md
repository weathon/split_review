# A Fault Forecasting Approach Using Two-Dimensional Optimization (TDO)

- Decision: Reject
- Avg Score: 2.50
- Scores: 3, 3, 1, 3

## Abstract
Data preparation plays a pivotal role in every machine learning-based approach, and this holds true for the task of detecting claims in the automotive industry as well. Handling high-dimensional feature spaces, especially when dealing with imbalanced data, poses a significant challenge in sectors where a vast amount of data accumulates over time. Machine learning models trained on highly imbalanced data often result in unreliable and untrustworthy predictions. Therefore, addressing the aforementioned issues is essential during the data pre-processing phase. In this paper, we propose an innovative two-dimensional optimization approach to effectively address the challenge of highly imbalanced data in the context of fault detection. We employ a heuristic optimization algorithm called Genetic Algorithm to concurrently reduce both the data point tuples and the feature space. Furthermore, we constructed and evaluated two-dimensional reduction using particle swarm optimization (PSO) and Whale optimization algorithms. The empirical results of the proposed techniques on the data collected from thousands of vehicles show promise.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Interesting paper that focuses on developing specialised techniques for tackling the challenge of high-dimensionality in real-world industrial data on the face of class-imbalance. The authors use popular algorithms like GA, PSO etc. and integrate it with common ML models to evaluate it on a sensors and repairs dataset from China. The paper has limited novelty and the proposed methodology does not consider the explainability and trustworthiness aspects to a sufficient level for a safety-critical industrial application.

### Strengths
The topic is interesting, the use of real-world dataset for experiments is promising. This reviewer appreciates the utilisation of simpler ML models like XGBoost for experimental purposes.

### Weaknesses
Lack of baseline models is one of the major weaknesses of the paper. The authors only consider XGBoost for classification purposes and do not compare it with any other ML model. The dataset under consideration (about 10k samples) is quite small and the authors do not clearly mention the rationale behind specifically using XGBoost and not any other model for classification task. Another major issue this reviewer spotted is the lack of focus on explainability in the paper - GA+XGBoost or PSO+XGBoost is mentioned in the paper and a graph shown with the AUC, however, it is clearly not enough to be convinced of how the GA+XGBoost framework is actually working and learning in the background on the face of high dimensional data with high class imbalance.

### Questions
It would have been nice to see the authors to have performed additional experiments with more traditional and popular algorithms like SMOTE (which the paper does mention of in the introduction section), however, lack of comparison with any kind of baseline dimensionality reduction or class-balancing/synthetic data augmentation algorithm or ML model (other than XGBoost) makes the paper lack novelty and has limited contribution.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper presents the relevant issue of training data imbalance and poses it as an optimization problem. A comprehensive set of heuristic techniques have been employed and results on XGboost are presented. The paper examines the GA, PSO,and WOA algorithms with the aim of simultaneously reducing both the tuple andf eature space to facilitate the construction of predictive models.

### Strengths
The comparison with several metaheusristics on a particular data set.

### Weaknesses
The importance of the fat-shattering dimension in explaining the beneficial effect of a large margin on generalization performance is discussed in existing literature (John Shawe-Taylor, Algorithmica, 22,157-172,1998; J John Shawe-Taylor, Peter Bartlett, Robert Williamson and Martin Anthony, IEEE Trans. Inf. Theory, 44 (5) 1926-1940, 1998. ). In the past, adaboost and thetaboost have been proposed to tackle this problem with theoretical results on maximum margin likelihood estimation under class imbalance. The problem statement is therefore not novel. Weighted loss functions are also proposed to solve this kind of optimization problems. The experimentation is not diverse. A carefully chosen data set is used. Since there is no theoretical guarantee of the method, it is difficult to ascertain the efficacy unless the experimentation net is widened to include some anomaly detection data sets.

### Questions
My question is how different is this approach except for superior performance on some some chosen data sets. Will this approach work if there is heavy imbalance (<1% in one class, rest in other classes) or SVM ensemble training?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper present a fault prediction method in automotives that uses optimizations on the recorded data of a vehicle and associate features. The selectionof the most appropriate data and features results in better predictions. For the data selection these optimization algorithms are used: Genetic Algorithm (GA) Whitley (1994), Particle Swarm Optimization (PSO) Marini & Walczak (2015), and Whale Optimization Algorithm (WOA) Mirjalili & Lewis (2016). The main ideas to to findout the relevant data that provides the better performance. Therefore, the above optimization algorithms are compared for that purpose.

### Strengths
a. The details of the use of GA for selection of data for fault prediction
b. Experiments comparing GA, PSO and WOA algorithms.

### Weaknesses
 a. The details about optimization algorithms are not necessary, rather good references should be enough. 
b. No details are provide on how the PSA and WOA are used in the proposed methods
c. No comparisons ar shown with state of the art (SOA)methods.
d. Nor the Data used is described neither the data source.

### Questions
a. Why only the details of GA applications are give but not the PSA and WOA?
b. Why the propsoed methods is not comapred with SOA methods?
c. What is the source of the data used?
d. What is an example of the data?

### Soundness
2 fair

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
In this paper, the authors address data preparation for fault detection within the automotive industry. Confronted with the challenge of high-dimensional feature spaces and imbalanced data, they introduce a two-dimensional optimization technique. Utilizing the Genetic Algorithm, they aim to concurrently reduce both data point tuples and the feature space. Additionally, the paper explores Particle Swarm Optimization (PSO) and Whale Optimization Algorithms (WOA).

Evaluating the GA, PSO, and WOA algorithms, they simplify tuple and feature space. The experimental results showed the method's capabilities in enhancing the classification performance.

### Strengths
Originality:
The paper introduces a two-dimensional optimization method for the application of fault detection in the automotive sector, by integrating the Genetic Algorithm with PSO and WOA. This approach offers the handling of high-dimensional data and imbalances.

Quality:
The paper is well-structured and methodologically sound clear, it presents the optimization techniques applied in the context of automotive fault detection. 

Clarity:
paper is generally well written.

Significance:
The study achieves promising results. Observations regarding GA's speed compared to WOA have practical implications.

### Weaknesses
 * **Lack of Comparative Analysis:**
While the paper does explore GA, PSO, and WOA for the automotive fault detection problem, it lacks a comparison with other existing methods or state-of-the-art techniques. Providing such a comparative study would have offered more context to the results. Also, adding references to the previous works/results in the domain would add to the paper results validation.

* **Dataset Concerns:**
The paper could have benefited from a more comprehensive analysis using multiple datasets or a more diversified dataset. Relying on a single dataset might limit the generalizability of the method and findings. Moreover, the paper lacks in describing the stats of the dataset in findings, it didn't provide comprehensive results that include the percentage/number of useful/selected features/tuples.


* **Parameterization Details:**
The authors mention parameterizing the three optimization algorithms as per values shown in "Table 1", yet they didn't explain how these optimal values were derived. Understanding the selection process for these parameters is essential for reproducibility and validation of the results.

### Questions
1- Could you elaborate on the reason that the paper lacks a comparison with existing methods or state-of-the-art techniques related to fault detection in the automotive industry?

2- Could you elaborate on the reason that only a singular dataset was chosen for this study, especially given its number of features?

3- In the results section, there seems to be limited detailed statistics about the dataset. Could you provide more statistics, especially the percentage/number of useful features/tuples?

4- How were the optimal parameter values of the three optimization algorithms determined?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor
