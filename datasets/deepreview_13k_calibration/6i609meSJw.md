# Tri-Comparison Expertise Decision for Drug-Target Interaction Mechanism Prediction

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 6, 5, 3, 5

## Abstract
Machine-learned interactions between drugs and human protein targets play a crucial role in efficient and accurate drug discovery. However, the drug-target interaction (DTI) mechanism prediction is actually a multi-class classification problem, which follows a long-tailed class distribution. Existing methods simply address whether interactions can occur and rarely consider the long-tailed DTI mechanism classes. In this paper, we introduce TED-DTI, a novel DTI prediction framework incorporating the divide-and-conquer strategy with tri-comparison options. Specifically, to reduce the learning difficulty of tail classes, we propose an expertise-based divide-and-conquer decision approach that combines the results of multiple independent expertise models for sub-tasks decomposed from the original prediction task. In addition, to enhance the discrimination of similar mechanism classes, we devise a tri-comparison learning strategy that defines the sub-task as the classification of triple options, such as expanding the classification task for classes A and B to include an extra “Neither of them” option. Extensive experiments conducted on various DTI mechanism datasets quantitatively demonstrate the proposed method achieves an approximately 13% performance improvement compared with the other state-of-the-art methods. Moreover, out method exhibits an obvious superiority on the tail classes. Further analysis about the evolvability and generalization of the proposed method reveals the significant potential to be deployed in real-world scenes. Our data and code is included in the Supplementary Materials and will be publicly released after the paper acceptance.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors address the problem of predicting DTI mechanisms by developing a decision method called TED-DTI using deep learning in the following way:
1. for every pair of mechanisms, training a "two-vs-rest" classifier for the mechanisms plus an "other" class made up of examples from the rest of the mechanisms, and
1. at inference time, ensembling the predictions by a novel class-balanced voting mechanism.

### Strengths
- novel two-vs-rest pairwise classifier and class-balanced penalization for voting
- performance improvements over many baselines in Table 1
- demonstrated improvements over both one-vs-one classification and standard voting in Table 2

### Weaknesses
 - Makes comparisons to older (ca. 2020) DTI prediction models, there are many newer ones in the 
- Except for the F1 score on ChEMBL, the gains of TED-DTI over the next best model are very modest.
- Table 1 inaccurately reports the lift $\Delta$, e.g. the ChEMBL F1 score should be $12.88\%$ since $0.789/0.699 = 1.1288$
- one-vs-one (a.k.a. all-vs-all) classification is a long-standing technique in multi-class classification, and is covered in classic ML texts like Bishop's Pattern Recognition and Machine Learning. Authors should have cited this and other earlier papers, e.g. [1] and [2]. I'm also surprised by the claim that two-vs-rest classification hasn't been reported in the literature before, but after a bit of searching I also couldn't find a reference.

### Questions
- How did you choose the baselines models used for comparison? There are many newer DTI prediction models that could have been used.
- Why wasn't the data in Fig 4a and 4c presented as a table like Table 1, along with stdevs and lift? It looks like TED-DTI might have achieved roughly 1.5% improvement over LADE and DrugBAN, which is again modest.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper introduces TED-DTI, a novel framework for drug-target interaction (DTI) mechanism prediction that addresses the challenge of long-tailed class distributions. The key innovation is a tri-comparison expertise decision approach that (1) decomposes the multi-class problem into pairwise sub-tasks using divide-and-conquer, (2) introduces a third "Neither" class for enhanced discrimination between similar mechanism classes, and (3) employs a class-balanced decision voting module for final predictions. The method is extensively evaluated on three datasets and demonstrates significant improvements over state-of-the-art methods, particularly for tail classes.

### Strengths
- A novel tri-comparison expertise training strategy
- A class-balanced decision voting module that effectively combines expertise predictions with weighted rewards/penalties
- Comprehensive empirical validation and thorough ablation studies demonstrating the importance of key components

### Weaknesses
 - The paper would benefit from stronger theoretical justification for why the tri-comparison approach works better than binary classification. Specifically, a more rigorous analysis of how the introduction of the 'Neither' class affects the decision boundaries and error rates is needed. It is not clear how this approach inherently addresses the long-tailed distribution problem beyond simply adding another class. A deeper dive into the mathematical properties of the decision boundaries and the resulting error decomposition would be beneficial.
- How generalizable it is when dealing with less or more classes? The paper lacks a clear discussion on the scalability of the proposed method. While the authors claim it can be adapted to different scales, there is no theoretical or empirical analysis to support this. How does the performance change when the number of classes is significantly reduced or increased? What are the limitations of the tri-comparison strategy in such scenarios? For instance, with fewer classes, the 'Neither' class might become redundant, and with more classes, the number of pairwise comparisons could become computationally prohibitive.
- Additional evaluation/analysis on empirical and theoretical computational costs. Specifically, since each sub-task requires a separate model, potentially making the overall system resource-intensive. The paper does not provide a detailed analysis of the computational complexity of the proposed method. The training and inference time for each sub-task, as well as the overall resource consumption, should be discussed. It is crucial to understand how the computational cost scales with the number of classes and the size of the dataset. A comparison with existing multi-class classification methods in terms of computational efficiency is also missing.

### Questions
See above.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper addresses the multi-class problem of Drug-Target Interaction (DTI) under long-tail distribution and proposes an algorithm based on the divide-and-conquer strategy—Tri-Comparison Expertise Decision (TED-DTI). Compared to other DTI methods and long-tailed learning-based methods, TED-DTI achieves better accuracy and F1 score on the DTI task, particularly with the AUROC metric for long-tail categories being higher than that of other algorithms. The TED-DTI algorithm is an innovative upgrade based on the One-vs-One algorithm, with the core idea of extending the classification task from A/B to A/B/Neither. The authors demonstrate through ablation experiments that this approach effectively improves the model's performance on the test set.

### Strengths
The TED-DTI algorithm is an innovative upgrade based on the One-vs-One algorithm, with the core idea of extending the classification task from A/B to A/B/Neither. The authors demonstrate through ablation experiments that this approach effectively improves the model's performance on the test set.And the authors explain that the introduction of 'Neither' may enhance model performance for the following reasons:(1) The design of class N⊗ improves the discrimination between mechanism classes and provides more expressive representations. (2)Supplementing a large number of samples from the 'Neither' class aids in feature learning.  The multi-class problem under long-tail distribution is a common issue, not only in the DTI context. It is expected that applying this algorithm to other scenarios should also lead to improved model performance, particularly in making more accurate predictions for minority classes. However, this paper focuses solely on the DTI problem and does not provide experimental applications in other scenarios, which is a regrettable omission.

### Weaknesses
I believe that the TED-DTI algorithm can enhance the model's performance on long-tail categories in the DTI multi-class problem. However, the innovation of TED is not significant; it appears to be a minor modification of the One-vs-One approach, essentially changing the original binary classification problem into a three-class problem. Additionally, the introduction of 'Neither' is similar to the 'Rest' in One-vs-Rest, suggesting that TED seems to be a combination of One-vs-One and One-vs-Rest. From this perspective, the authors should briefly introduce One-vs-Rest in the related work section and discuss the connections and differences among the three approaches in subsequent sections. Furthermore, One-vs-Rest should be included in the method comparison (Table-1).

The paper has some imprecise parts; here are a few:

1. As stated in line 244, the loss function formula for each tri-comparison expertise model shows that the loss is the mean of the cross-entropy for N categories. However, each tri-comparison expertise model is a three-class model and is trained separately. Therefore, its loss should be the mean of the cross-entropy for the three categories, not N. Although both 3 and N are constants and do not actually affect the model training, correcting this would make the paper more precise. I recommend that the authors to clarify if N should be replaced with 3 in the formula, or if there is some other reason for using N that is not explained in the current text.

2. Table 1 (lines 342 and 343) presents a comparison between two OvO methods and TED-DTI. However, the backbone models of these two OvO methods are SVM-based and GCN-based, respectively, which are not strictly consistent with the backbone model of the TED-DTI method. Therefore, the conclusion stated in lines 413-415, "Compared with OvO methods which also adopt the divide-and-conquer strategy, TED-DTI significantly exceeds all the OvO baselines," cannot be drawn from this comparison. However, this conclusion can be supported by the ablation experiments described in Table 2.  So I suggest that the authors either use consistent backbone models across all compared OvO methods, or explicitly acknowledge and discuss the impact of different backbones on the performance comparison.

3. The authors selected 829 samples from the ChEMBL dataset as an independent test set. However, it should be analyzed whether there is any overlap between these samples and the training set (GtoPdb). If  overlap exists, the overlapping samples should be removed. The authors should explicitly state in the paper whether they checked for and removed any overlapping samples, and if so, describe the process they used.

Additionally, for the experiments, the following should be addressed:

1. The GtoPdb-GPCRs dataset has a total of 5,111 samples, while the GtoPdb dataset has a total of 13,381 samples. Is the GtoPdb-GPCRs (5,111 samples) included within the 13,381 samples of GtoPdb, or is it additional? Is is suggested that the authors clarify in the paper the relationship between the GtoPdb and GtoPdb-GPCRs datasets, specifically whether GtoPdb-GPCRs is a subset of GtoPdb or a separate dataset.
2. As mentioned in line 354, the authors performed 5-fold cross-validation on the training set. So, i'm confused and would appreciate it if the authors could explicitly describe in the paper how the metrics for the ChEBML dataset in Table 1 were calculated. Are the metrics for various algorithms on the ChEBML dataset the mean values of the metrics from the five models obtained through 5-fold cross-validation on GtoPdb, or were they derived in another way?

Finally, providing open-source code and data would be beneficial.

### Questions
The paper has some imprecise parts; here are a few:

1. As stated in line 244, the loss function formula for each tri-comparison expertise model shows that the loss is the mean of the cross-entropy for N categories. However, each tri-comparison expertise model is a three-class model and is trained separately. Therefore, its loss should be the mean of the cross-entropy for the three categories, not N. Although both 3 and N are constants and do not actually affect the model training, correcting this would make the paper more precise. I recommend that the authors to clarify if N should be replaced with 3 in the formula, or if there is some other reason for using N that is not explained in the current text.

2. Table 1 (lines 342 and 343) presents a comparison between two OvO methods and TED-DTI. However, the backbone models of these two OvO methods are SVM-based and GCN-based, respectively, which are not strictly consistent with the backbone model of the TED-DTI method. Therefore, the conclusion stated in lines 413-415, "Compared with OvO methods which also adopt the divide-and-conquer strategy, TED-DTI significantly exceeds all the OvO baselines," cannot be drawn from this comparison. However, this conclusion can be supported by the ablation experiments described in Table 2.  So I suggest that the authors either use consistent backbone models across all compared OvO methods, or explicitly acknowledge and discuss the impact of different backbones on the performance comparison.

3. The authors selected 829 samples from the ChEMBL dataset as an independent test set. However, it should be analyzed whether there is any overlap between these samples and the training set (GtoPdb). If  overlap exists, the overlapping samples should be removed. The authors should explicitly state in the paper whether they checked for and removed any overlapping samples, and if so, describe the process they used.

Additionally, for the experiments, the following should be addressed:

1. The GtoPdb-GPCRs dataset has a total of 5,111 samples, while the GtoPdb dataset has a total of 13,381 samples. Is the GtoPdb-GPCRs (5,111 samples) included within the 13,381 samples of GtoPdb, or is it additional? Is is suggested that the authors clarify in the paper the relationship between the GtoPdb and GtoPdb-GPCRs datasets, specifically whether GtoPdb-GPCRs is a subset of GtoPdb or a separate dataset.
2. As mentioned in line 354, the authors performed 5-fold cross-validation on the training set. So, i'm confused and would appreciate it if the authors could explicitly describe in the paper how the metrics for the ChEBML dataset in Table 1 were calculated. Are the metrics for various algorithms on the ChEBML dataset the mean values of the metrics from the five models obtained through 5-fold cross-validation on GtoPdb, or were they derived in another way?

Finally, providing open-source code and data would be beneficial.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper improves the one-vs-one method on long-tailed multi-class classification problem by expanding the sub-tasks from binary classification to tri-comparison, with an additional ``neither" class. The method is evaluated on both internal and external dataset, and shown better performance. Noticeable improvement is seen especially on extremely tail class.

### Strengths
What this paper focuses is an important but long-been-overlooked problem. In my opinion, performance on tail classes can easily be overwhelmed in common metrics, such as micro-averaging ones. I am glad to see this paper makes some analysis on extremely tail class, thus highlighting the problem.

The experimental design is solid, especially including external dataset evaluation and generalization validation. The dataset size is relatively small, but I understand it is limited by available public data.

The paper is well organized and presented. It is generally easy to understand, but you should try to make things more concise, to avoid put important information in supplementary.

### Weaknesses
I think adding an additional "neither" class is somewhat rough. You are using more data compared with binary classification, but it is still imbalanced in each sub-tasks. The imbalance is not resolved but only alleviated by the proposed method. Besides, classes have complex relationships between them, so simply putting a highly-correlated class into "neither" may not seem a good idea. For example, if two classes are mechanistically similar, placing them in "neither" for a given sub-task could obscure important distinctions and lead to misclassification. Also from a practical perspective, both the proposed method and one-vs-one generates too many sub-tasks. It is expensive to train all these models, and makes it infeasible to scale to larger number of classes. The computational overhead of training a separate model for each sub-task is a significant concern, especially given the potential for a quadratic increase in the number of sub-tasks with the number of classes.

Also, the method seems not highly coupled with DTI. Actually the only things related to DTI is the two encoders, but the architecture is widely used. So instead of limiting to DTI, authors should try to apply their method to more domains. This also solves the problem of limited dataset size.

### Questions
The paper trains one GCN(for Drug), one CNN(for Target), and one MLP for each sub-task, which incurs a significant additional computational overhead. Have the authors considered using a shared Drug Encoder and a shared Target Encoder for each sub-task? Can you discuss the tradeoffs between using separate vs shared encoders, including any potential impacts on performance or training time?

How the authors obtained the class-balanced weight vector H.

In line 302, how the authors performed the pre-processing. Specifically, how do you handle the missing data? Are they simply been filtering out? Is there any else filtering criteria?

In the experimental section, only the results for the Gating inhibitor are presented. However, data for Allosteric modulators, Channel blockers, and Activators are also limited and should be analyzed as well.

In Table 2, the addition of class “neither” leads to a notable increase in the F1 score only in ChEMBL, rising from 0.648 to 0.789. Can you explain the reason? Also, the accuracy only improves from 0.955 to 0.961. Why is the difference between these two metrics? Can you discuss the implications of these differences for the model's performance on different datasets or class distributions?

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces TED-DTI, a novel framework for predicting drug-target interaction (DTI) mechanisms that addresses the challenge of long-tailed class distribution in real-world drug discovery applications. The authors propose an innovative divide-and-conquer approach by decomposing the multi-class prediction task into pairwise sub-tasks, each handled by independent expertise models. A key contribution is the introduction of a tri-comparison expertise training strategy that adds a "Neither" class option to enhance discrimination between mechanism classes. The framework leverages graph neural networks for drug encoding and CNN for protein sequence encoding, combined with a class-balanced decision voting module to integrate predictions from multiple expertise models. 
    
    The method demonstrates performance improvements on the GtoPdb and ChEMBL datasets compared to state-of-the-art methods. The approach shows special promise in handling tail classes, as evidenced by superior AUROC scores for rare mechanism classes like Gating Inhibitor.
    
    While the technical innovation and empirical results are compelling, there are some important limitations to consider. The computational complexity increases quadratically with the number of classes, potentially limiting scalability for larger mechanism sets. Additionally, while the "Neither" class addition is clever from a machine learning perspective, its biological significance and practical implications could be better justified.

### Strengths
-Novel tri-comparison strategy that effectively addresses long-tailed distribution challenges
-Strong theoretical foundation with clear connections to  neuroscience-inspired design
-Superior handling of tail classes with demonstrated improvements in rare mechanism prediction
-Potential for generalization to other interaction domains

### Weaknesses
 - Marginal performance improvement (<1% on accuracy for both datasets)
- Limited evaluation metrics - lack of AUROC, AUPRC, and MCC metrics which are crucial for imbalanced datasets
- No comparison with 2024 state-of-the-art methods
- The "Neither" class addition lacks biological significance and may not be truly innovative
- OvO method comparisons use overly simple backbones, making the comparative experiments less meaningful
- No comparison with popular multimodal large biological models (e.g., OpenBioMed, BioMedGPT, xTrimo) in DTI prediction
- Insufficient description of important parameters and their tuning process
- Computational complexity scales quadratically with mechanism classes (O(N²)), raising scalability concerns

### Questions
- Why is the balanced penalty weight vector H defined for each mechanism class rather than for each sub-task?
- Is the dataset used in the study newly constructed? Is it publicly available (Will it be released)?
- For DTI baseline comparisons, were the same task decomposition and model ensemble strategies applied as in TED-DTI? This would ensure a fair comparison.
- Has the model been tested in virtual screening scenarios?
- What strategies could be employed to address the quadratic computational complexity?
- How sensitive is the model to different "Neither" class sampling strategies?

### Soundness
4

### Presentation
3

### Contribution
2
