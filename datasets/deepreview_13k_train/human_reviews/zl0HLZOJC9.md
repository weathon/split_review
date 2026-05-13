# Probabilistic Learning to Defer: Handling Missing Expert Annotations and Controlling Workload Distribution

- Decision: Accept
- Scores: 8, 8, 8, 8

## Abstract
Recent progress in machine learning research is gradually shifting its focus towards *human - AI cooperation* due to the advantages of exploiting the reliability of human experts and the efficiency of AI models. One of the promising approaches in human - AI cooperation is *learning to defer* (L2D), where the system analyses the input data and decides to make its own decision or defer to human experts. Although L2D has demonstrated state-of-the-art performance, in its standard setting, L2D entails a severe limitation: all human experts must annotate the whole training dataset of interest, resulting in a slow and expensive annotation process which can subsequently influence the size and diversity of the training set. Moreover, the current L2D does not have a principled way to control workload distribution among human experts and the AI classifier that is important to optimise resource allocation. We, therefore, propose a new probabilistic modelling approach inspired from mixture-of-experts, where the Expectation - Maximisation algorithm is leveraged to address the issue of missing expert's annotations. Furthermore, we introduce a constraint, which can be solved efficiently during the E-step, to control the workload distribution among human experts and the AI classifier. Empirical evaluation on synthetic and real-world datasets show that our proposed probabilistic approach performs competitively, or even surpasses previously proposed methods assessed on the same benchmarks.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper extends the concept of *learning to defer* (L2D) to scenarios with missing expert annotations and balanced expert workloads. The authors propose a formulation that relies on a clever application of the expectation-maximization algorithm, which naturally handles missing data. Additionally, they introduce a constraint within the expectation stage of the algorithm to manage expert workloads. The proposed L2D is tested on both synthetic and real-world datasets, resulting in a higher area under the coverage-accuracy curve compared to the evaluated baselines.

### Strengths
+ The paper addresses a research question relevant to real-world applications by providing a solution for settings where expert annotations are incomplete. 
+ The results show that reducing the workload of highly accurate (and typically overloaded) human experts only slightly decreases overall accuracy and can lead to higher accuracy in scenarios with inconsistent expert performance between the training and test sets. 
+ The proposed controllable workload formulation simplifies the evaluation of accuracy-coverage ratios compared to existing methods, which often require assumptions or post-hoc adjustments to balance learnable models and human experts.

### Weaknesses
 + As acknowledged by the authors, the proposed formulation does not scale well with the number of human (or learnable) experts. While grouping experts into clusters is suggested as potential future research direction, this introduces the number of clusters as a hyperparameter, necessitating additional tuning and potentially hindering scalability. The computational complexity of the expectation-maximization algorithm, particularly the E-step, grows linearly with the number of experts, making it impractical for scenarios with a large pool of annotators. Furthermore, the clustering approach, while potentially mitigating this issue, introduces a new layer of complexity by requiring the selection of an appropriate clustering algorithm and the determination of the optimal number of clusters, which may not be straightforward and could impact the overall performance.
+ Although the paper is concise and generally well-written, the notation is ambiguous in some places (see Q1 and Q2), and the discussion of the results is very brief and could benefit from additional explanations (see Q3 and Q4). Specifically, the relationship between the expert annotations, the ground truth labels, and the model's predictions is not clearly articulated, making it difficult to understand the underlying mechanisms of the proposed approach. The lack of detailed analysis of the experimental results, particularly the reasons behind the performance gains and the impact of different parameters, limits the interpretability and practical applicability of the findings.
+ (Minor comment) I recommend the authors release the source code to reproduce results. While not mandatory, providing the code would help readers understand how to implement the algorithm proposed on page 14, especially the implementation steps required to solve the optimization equation formulated in Eq. 4 on page 4.

### Questions
+ Q1. I found the data training process and the L2D objective on page 3 difficult to understand, possibly due to ambiguous notation. Does $\mathbf{y}$ represent the ground truth label or output prediction? If $\mathbf{y}$ refers to the ground truth, why does it depend on the expert annotations $\mathbf{t}$? Should not $\mathbf{y}$ be dependent on $\mathbf{x}$ but independent of expert selection and annotation? The notation in Eq. 1, where $\mathbf{t}_i$ becomes $\mathbf{y}_i$, is particularly confusing. Revising the notation could improve clarity and help readers understand the logic.
+ Q2. Regarding Eq. 1, if $\mathbf{t}_i$ are deterministic expert annotations from a look-up table and $\mathbf{y}_i$ represents the ground truth label, is it still valid to compute the log-likelihood with *hard labels*?
+ Q3. Could you provide a more detailed explanation of why the accuracy of probabilistic L2D surpasses that of the best human expert (even with a 70% missing rate and especially for low coverages)? This was not explained in the discussion.
+ Q4. Why does the area under the coverage-accuracy curve increase with higher missing rates on the MiceBone dataset? Why does having fewer annotations lead to better performance? It is mentioned that this is due to inconsistent human expert behavior between the training and test sets. How do missing annotations help in this case?
+ Q5. The discussion on balanced workload and inconsistent human performance between training and test sets could benefit from further elaboration (Page 8, Line 423). Would assigning less weight to a particular expert act as a form of regularization?
+ Q6. (Minor suggestion) It would be helpful to present the results in Figure 3 with equal Y-axis scales for subplots corresponding to the same dataset.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The paper studies the problem of learning to defer for a realistic setting where expert annotations can be missing and where workload balancing among experts is crucial. The authors propose a probabilistic modeling approach where EM is used to address the missing annotations, In particular, a constrained optimization during the E step regulates workload balancing among human experts and the AI classifier. The proposed method is evaluated on synthetic and real-world datasets and is shown to perform on par or better than the considered baselines.

### Strengths
The paper is well-written and easy to follow. The proposed probabilistic modeling techniques and the use of EM in this setting seem novel and an interesting contribution. Experimental results show the performance gain of the method compared to the baselines.

### Weaknesses
A key weakness is highlighted by the authors in the paper: Bad dependency on the number of human experts. Although, they discuss potential remedies, e.g., clustering. However, this probably wouldn't work for a setting with diverse human experts (where the number of clusters is large). Are there other dimensionality reduction approaches (e.g., hierarchical clustering) that one could consider for this setting and how would they affect computational cost?

### Questions
I am unsure about the computational cost of the method compared to the considered baseline. Could the authors elaborate more on this? Ideally, by comparing and reporting the runtimes of the proposed method and the baselines across the different datasets.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces a probabilistic framework for “Learning to Defer” (L2D) that enables an AI system to either make decisions independently or defer them to human experts based on confidence levels. The approach addresses the limitations of existing L2D methods by handling cases where not all experts can annotate every data sample. This approach is designed to reduce the annotation burden. The approach is based on the Expectation-Maximization (EM) algorithm to optimize workload distribution between AI and human experts. The proposed method shows promising performance across synthetic and real-world datasets.

### Strengths
- The paper addresses an interesting issue in L2D and proposes a sound solution based on a probabilistic approach. 
- The workload management is particularly promising in many areas where AI is supporting expert decision such as in medicine. 
- This is also relevant in addressing ethical and practical constraints, and possibly even regulations and laws. 
- The ablation study offers an insight on the mechanism that lead to prioritise highest performing humans with the imbalanced approach, with possible overfitting.
-  It is interesting that the study allows for the conclusion that in practice it may be desirable to distribute workload evenly across all human experts.

### Weaknesses
1. Overall, the approach has some limitations, which I acknowledge are also partially discussed. However, it's unclear how well the system can scale given that each expert requires a probabilistic model. It's unclear to me how well the clustering of expert would work and what are the risks associated with that.

2. I would be interested in reading more about the trade-off between the case for fewer deferring cases or deferring cases with the highest uncertainty, which is not much discussed. Clearly, there will be cases, e.g., healthcare, where deferring on uncertain cases would be quite important.

3.  How could the model be adapted to take into consideration fast and slow changing expertise performance? The model assume static performance, however, experts could have fast performance changes, e.g. due to fatigue, or slow performance changes, e.g. due to learning through a period of time. It would be nice to understand how the model could accommodate for such dynamic scenarios.

### Questions
Could the authors answer points/questions 2 and 3 in the list above "weaknesses"?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The paper deals with human - AI cooperation. It presents a modification of the learning to defer technique which can handle incomplete expert annotations and balance the workload of the experts.

### Strengths
* It seems to me that the topic has been addressed very comprehensively
* The comparisons include all the mentioned relevant predecessor methods

### Weaknesses
I can't see any significant weaknesses. However, this may also be because the topic is new to me.

Further comments:

* In the case of “In contrast, machine learning or AI models excel at processing large amounts of information but may be prone to biases (Meehl, 1954)”, the reference chosen cannot be used as evidence for the statement because “machine learning or AI models ... processing large amounts of information” were not available until long after 1954.
* I find statement “Ideally, a perfect balanced workload among experts and the AI model can be expressed as follows” a little strange. After all, you will only strive for an equal distribution if all experts are equally competent.
* I wonder about “slightly-similar”, how can something be slightly similar?
* I find it a bit irritating that there is no section called “Conclusion”.
* “50 %” -> “50%”

### Questions
* Would it make sense to repeat the learning experiments several times in order to be able to estimate the uncertainty of the results?
* Does it make sense to give the results in Table 1 with four valid digits? Are the results really that accurate?

### Soundness
3

### Presentation
3

### Contribution
3
