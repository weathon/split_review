# Salutary Labeling with Zero Human Annotation

- Decision: Reject
- Avg Score: 4.25
- Scores: 3, 3, 5, 6

## Abstract
Active learning strategically selects informative unlabeled data points and queries their ground truth labels for model updates. 
The prevailing assumption in the active learning paradigm is that the acquisition of ground truth labels optimally enhances model performance. 
However, this assumption may not always hold or maximize learning capacity. 
Moreover, ground truth annotations incur significant costs due to the need for intensive human labor.
In contrast to traditional active learning, this paper proposes salutary labeling, which automatically assigns the most beneficial labels to the most informative samples without human annotation. Specifically, we utilize the influence function, a tool for estimating sample influence, to select newly added samples and assign their salutary labels by choosing the category that maximizes their positive influence. This process eliminates the need for human annotation. Extensive experiments conducted on nine benchmark datasets demonstrate the superior performance of our salutary labeling approach compared to traditional active learning strategies. Additionally, we provide several in-depth explorations and extend salutary labeling to other practical applications including large language model fine-tuning.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents a novel pseudo-labeling approach for unlabeled data using influence functions. The proposed method estimates the influence of each possible label on the validation loss for a given unlabeled data point and assigns the label with the most significant improvement in loss as its pseudo-label. Subsequently, a subset of the unlabeled data with the highest improvement in validation loss is selected to update the model. Extensive experiments are conducted to validate the effectiveness of the method.

### Strengths
Solid experiments are conducted on both tabular and image datasets, integrating recent data selection methods from AL and SSL. The proposed method demonstrates promising empirical results without the need for human-annotated labels. In addition, the method is validated on a LLM fine-tuning task, which further underscores its potential for application in different domains.

### Weaknesses
While the method is framed in part within the active learning context, its approach—assigning pseudo-labels to unlabeled data via a self-training mechanism—seems more aligned with semi-supervised learning. The introduction could benefit from adjustments to reflect this alignment more accurately. Another concern is the limited technical contributions. It uses the influence function to score and pseudo-labeling the unlabeled data. Although this is an interesting application, it may not represent a substantial methodological advance. Furthermore, in the experiments, a query budget of 10 examples is set, yet only the first 10 rounds of performance are reported. Providing results for additional rounds or scenarios with a larger query budget would offer a more comprehensive evaluation of the method’s long-term effectiveness. In Appendix D, results from querying 1% of the data reveal that the proposed method underperforms relative to other baseline methods. This needs further exploration and explanation. My last concern is that the paper’s approach relies on setting aside 20% of the data for validation, which may be impractical for certain active learning settings, where labeled data is typically scarce. Performances on different sizes of validation set should also be explored.

### Questions
1)	In addition to the logistic regression model used, is the proposed method suitable for more complex models? In Appendix E, a surrogate model is employed to compute the influence, but could the ResNet itself be directly used for influence calculation? 
2)	Since the accuracy of the pseudo-labels depends on the quality of the validation set, how does the performance of the proposed method vary with different validation set sizes?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes salutary labeling, which automatically assigns the most beneficial labels to the most informative samples without human annotation. Specifically, they utilize the influence function, a tool for estimating sample influence, to select newly added samples and assign their salutary labels by choosing the category that maximizes their positive influence.

### Strengths
1. The motivation and paper writing are clear. 
2. The experiment is sufficient 
3. The method is fully automatic without human annotation

### Weaknesses
1. They do not discuss the difference with the unsupervised learning methods, such as 

[1] Self-paced Contrastive Learning with Hybrid Memory for Domain Adaptive Object Re-ID
[2] Mutual Mean-Teaching: Pseudo Label Refinery for Unsupervised Domain Adaptation on Person Re-identification

If the human intervention is removed from active learning, it will be transformed to unsupervised learning that assigns the pseudo labels to the samples. Could you discuss the difference ?

2. How to tackle with the situation that the selected labels are wrong? Could you discuss potential error correction mechanisms, or to analyze the impact of incorrect labels on model performance?

### Questions
My main concern is the weakness 1. I do not understand the value of their new proposed task. I think this setting is similar to the unsupervised learning with the pseudo labels. In my understanding, I think the human annotation is helpful during training. This is the reason why we study active learning. If we fully abandon human intervention, this is totally another area which is unsupervised learning.

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This study defines a task called salutary labeling, which involves selecting a subset of data from an unlabeled data pool predicted to be the most beneficial for training, similar to traditional active learning, and then using this selected data for model training. The key difference in the proposed salutary labeling approach is that, instead of using labels from human annotators, it assigns pseudo labels expected to improve performance on the validation set. Specifically, it measures the influence of each data point and assigns a salutary label that maximizes validation set performance. The data with the highest influence from the assigned salutary labels is then used for training. This method was tested on nine datasets and demonstrated improved results compared to traditional active learning approaches.

### Strengths
- The *Salutary Labeling for Active Learning* framework was new to me. If we can effectively annotate data automatically without human annotator, it could demonstrate remarkable potential for machine learning as a whole.

- Overall, the writing is well-structured and easy to follow, making it straightforward to understand the main concepts.

- The proposed method consistently improved performance across nine datasets. This study also conducted detailed ablation studies to analyze the effectiveness of *salutary labels* through the influence function.

### Weaknesses
 - The motivation behind combining salutary labeling with active learning is not fully clear to me.
   - The core motivation of active learning is to label only a small number of informative data points to reduce annotation costs. If automatic labeling without human annotation costs is feasible, applying salutary labels to all available data without the selection process in active learning should suffice.
   - In Algorithm 1, it seems that salutary labels are generated for the entire unlabeled pool during selection. Figure 5 also suggests that model performance improves as the number of salutary labels increases, so the necessity of sampling is unclear.
   - **Additional explanation on why the active learning framework remains effective despite not requiring human labor for labeling would help clarify my understanding.**

- I am not fully convinced about how the salutary labeling task is novel compared to existing label-efficient tasks.
   - To me, the salutary labeling task appears to combine elements from various existing label-efficient tasks. If the goal is to automatically label training data, this could be viewed as a pseudo-labeling process in semi-supervised or self-supervised learning. On the other hand, methods for correcting label noise align more closely with the learning with label noise task [a, b, c].
   - In Appendix A, a key difference from other label-efficient learning tasks is described as a focus on active learning (line 836). However, as mentioned above, without a clear reason for combining salutary labels with the active learning framework, I remain uncertain about the task’s distinction from others.
   - **A clearer explanation on why salutary labels need to be combined with active learning and how this approach fundamentally differs from other label-efficient learning methods would be helpful.**

- There seem to be potential fairness concerns in the comparative experiments with existing AL baselines.
   - The proposed experimental setup uses 20% of the dataset as a validation set and utilizes this validation set’s annotations for influence function calculations and labeling. If labeled data is essential for the proposed method, it would be fairer to allocate part of the training budget for this purpose.
   - Specifically, in Table 1, the budget sample size is set as low as 10, which makes it impractical to reserve 20% of the dataset as a validation set while only training on about 10 samples. This setup might give the impression that validation set labels are indirectly being used for salutary labeling of the unlabeled data.
   - As shown in Figure 5 of Appendix D, one potential reason for the reduced gain of the proposed method as the budget size increases may be the dilution of the validation set’s supervisory effect.
   - **The following additional experiments might strengthen the justification for salutary labeling:**
       - Using a smaller validation set (e.g., 1% to 5% instead of 20%).
       - Including the validation set size in the training budget for all methods (e.g., allowing AL baselines to train on the validation set or at least part of it).

### Questions
- The proposed approach appears closely related to training with noisy labeled data methods mentioned in the Weakness section. An analysis and comparison with this literature in the related work would be beneficial.
- A detailed analysis of the assigned salutary labels would be interesting. It would be helpful to know if labels different from the ground truth sometimes enhance performance or if performance improvement primarily comes from refining noisy labels.

### Soundness
2

### Presentation
4

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors propose salutary labeling for active learning which is human annotation-free. They adapt the influence function to calculate the sample influence by assessing the impact of each sample across all possible labels and assigning the label that yields the greatest positive influence. The authors conducted experiments on different datasets to verify the effectiveness of the simple idea.

### Strengths
1.The writing is good and the supplementary materials are relatively sufficient.

2.The authors propose a simple-sounding but effective active learning method which eliminates the need for human annotation. Judging from the comparative experimental results provided by the authors, this idea is effective.

### Weaknesses
1.In the last paragraph of Section 4, the authors mentioned that the time complexity of salutary labeling is O(nd). However, the proposed salutary labeling algorithm need to calculate the influence estimation of every data point in each iteration of active learning. How much will this slow down the entire training process? Can the authors provide the running time comparison results of each method in Table 1?

2.In the experiment, the author set active rounds R = 10 and query budget b = 10. When b and R are larger, is it impossible to prove that the proposed salutary labeling is effective?

3.The first paragraph of Section 2 is too long and a little bit difficult to read. It should be adjusted appropriately.

4.The legend in Figure 1 obscures part of the polyline and may need to be further refined.

### Questions
1.In the last paragraph of Section 4, the authors mentioned that the time complexity of salutary labeling is O(nd). However, the proposed salutary labeling algorithm need to calculate the influence estimation of every data point in each iteration of active learning. How much will this slow down the entire training process? Can the authors provide the running time comparison results of each method in Table 1?

2.In the experiment, the author set active rounds R = 10 and query budget b = 10. When b and R are larger, is it impossible to prove that the proposed salutary labeling is effective?

3.The first paragraph of Section 2 is too long and a little bit difficult to read. It should be adjusted appropriately.

4.The legend in Figure 1 obscures part of the polyline and may need to be further refined.

### Soundness
3

### Presentation
3

### Contribution
3
