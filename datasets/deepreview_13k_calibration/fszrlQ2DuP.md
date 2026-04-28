# Can We Evaluate Domain Adaptation Models Without Target-Domain Labels?

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
Unsupervised domain adaptation (UDA) involves adapting a model trained on a label-rich source domain to an unlabeled target domain. However, in real-world scenarios, the absence of target-domain labels makes it challenging to evaluate the performance of UDA models. Furthermore, prevailing UDA methods relying on adversarial training and self-training could lead to model degeneration and negative transfer, further exacerbating the evaluation problem. In this paper, we propose a novel metric called the Transfer Score to address these issues. The proposed metric enables the unsupervised evaluation of UDA models by assessing the spatial uniformity of the classifier via model parameters, as well as the transferability and discriminability of deep representations. Based on the metric, we achieve three novel objectives without target-domain labels: (1) selecting the best UDA method from a range of available options, (2) optimizing hyperparameters of UDA models to prevent model degeneration, and (3) identifying which checkpoint of UDA model performs optimally. Our work bridges the gap between data-level UDA research and practical UDA scenarios, enabling a realistic assessment of UDA model performance. We validate the effectiveness of our metric through extensive empirical studies on UDA datasets of different scales and imbalanced distributions. The results demonstrate that our metric robustly achieves the aforementioned goals.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
To evaluate the performance of the Unsupervised Domain Adaptation (UDA) model, this paper proposes a novel metric called “Transfer Score”. Based on this metric, we achieve three novel objectives without target-domain labels: (1) selecting the best UDA method (2) optimizing the hyperparameter of the UDA model (3) selecting the best checkpoint.

### Strengths
1.	Evaluate UDA models in an unsupervised manner is very important, but there is a lack of relevant research in the current community
2.	Experiments demonstrate the effectiveness of “Transfer Score” in method selection, hyperparameter tuning, and checkpoint selection. 
3.	The paper is well-written and easy to understand.

### Weaknesses
1.	“Transfer Score” uses clustering and class balance as the measurement criteria. However, the assumption of clustering and class balance usually may not always hold. Acutally, in many real world tasks, class imbanlance often exists. For example, in cross-domain semantic segmentation, a severe category imbalance is often present [1], which limits the application of this metric. Specifically, the Hopkins statistic, while measuring clustering tendency, does not inherently account for class-specific density variations, which can be significant in imbalanced datasets. Similarly, the uniformity measure, calculated on model weights, may not accurately reflect the classifier's performance across minority classes, where the decision boundaries might be less well-defined. This raises concerns about the reliability of the 'Transfer Score' in scenarios where class imbalance is a dominant factor.
2.	Some methods[2,3] directly adopt Eq. 1 and Eq. 4 as optimization objectives. For these methods, the transfer score may be invalid. Specifically, if a method explicitly optimizes for the mutual information term (Eq. 4) or the clustering criteria (Eq. 1), the transfer score may become a redundant measure, as it is already implicitly being optimized during training. This could lead to a situation where the transfer score is not a good indicator of actual transfer performance, as it is essentially measuring the degree to which the model achieves its own training objective, rather than an independent assessment of its transferability.
3.	The author needs to verify the effectiveness of the “Transfer Score” on more advanced UDA methods[3,4]. The current evaluation lacks experiments on state-of-the-art UDA methods, particularly those that employ more sophisticated adaptation techniques beyond basic feature alignment. The absence of such evaluations makes it difficult to assess the general applicability and robustness of the “Transfer Score” across a wide range of UDA approaches. For example, methods that use adversarial training or self-training may exhibit different behaviors, and it is unclear if the proposed metric can accurately capture their performance.

### Questions
I would like to see authors' response regarding the weaknesses.

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
Targeting at evaluating UDA models without target-domain labels, this paper proposes a new metric called the Transfer Score by assessing the spatial uniformity of the classifier via model parameters as well as the transferability and discriminability of deep representations. Three types of experiments are conducted for model evaluation.

### Strengths
+ The proposed metric is meaningful and intuitive.
+ The proposed metric seems useful in various evaluation settings.

### Weaknesses
 - As the authors stated, “prevailing UDA methods relying on adversarial training and self-training could lead to model degeneration and negative transfer”, How can we prove this viewpoint? Can the proposed metric be applied to these types of methods for performance improvement in regular UDA settings?
- Although the proposed metric is intuitive, it is difficult to validate that it is definitely correct for evaluating a UDA model. In fact, various existing UDA approaches also adopt “Transfer Scores” for guiding the model learning process, such as [a]. A comparison between these metrics should be conducted.
- In figure 1, the correlation analysis is conducted only in one UDA task (Office31 A->W) and one UDA model (DANN), more comprehensive analysis and more comparison (with more metrics) should be conducted.
- In Definition 2, the design of the Score seems handcrafted. How can we ensure this formulation is optimal? Why use this design? The reasons should be analyzed.
- Some SOTA UDA approaches are not employed for experimental analysis [b-c].
- From Table 1, why are the improvements of the last four methods on the DomainNet (p->c) task so small?

### Questions
Please refer to the Weakness.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a method named Transfer Score, which measures the classifier bias and feature discriminability, for the unsupervised validation problem.

### Strengths
- This idea is simple and easy to follow.

### Weaknesses
 - The experiments are weak.
  - Task1 and Task2 are actually unsupervised model evaluation problems, all the unsupervised validation methods such as SND can be employed directly, but the authors do not compare their method with these methods.
  - In the experiments, only six UDA methods were evaluated. In task 2, there are only five candidate hyperparameters. The number is too small to illustrate the effectiveness of the proposed method.
  - The UDA datasets employed in the experiments are not comprehensive. On office-home, only four tasks were selected, and the situation was similar for DomainNet and Office. How do you select these tasks?

- The authors said, "TS is the **first** metric to perform simultaneous model comparison and selection without target-domain labels". As far as I know, the three tasks in experiments are actually unsupervised validation problems, and this is an existing research field. Besides, some out-of-distribution generalization prediction methods also solve the model selection problem without labels.
  > K-Means Clustering Based Feature Consistency Alignment for Label-Free Model Evaluation. 
  > Predicting Out-of-Distribution Error with Confidence Optimal Transport.
  > Leveraging Unlabeled Data to Predict Out-of-Distribution Performance.
  > ...

### Questions
See weakness.

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
This paper studies the performance evaluation problem for unsupervised domain adaptation methods. Authors propose a evaluation metric called the Transfer Score. The propose metric consides both spatial uniformity from the model parameters and the transferability and discriminability calculated from the target samples. The metric can help users to select UDA methods, hyperparameters and checkpoints. Authors provide rich experiments to evalutate the effectiveness of the proposed metric.

### Strengths
1. The proposed Transfer Score is novel and the calculation process is clear.

2. The authors provide code in Supplementary Material, which makes the experiments convincing.

3. The structure of the paper is well organized.

### Weaknesses
1. Experimental results of baseline methods (e.g., DEV, SND) should be provided in the experiment section, there are only Transfer Score results of many dataset in that section.

2. Ablation study of Table 3 is weak, authors should provide the same one like Fig. 2 to evaluation the effectiveness of each term.

3. The representation of Equation 1 is incorrect, especially i*(i-1) and the use of i.

4. Authors should provide the complete results of all tasks from the different datasets * different UDA methods * baseline methods and proposed score, like Fig.3. The experimental results in the paper seem a bit sparse.

### Questions
1. What if the Transfer Score used as a optimization function for UDA task? I am curious about this.

2. Mutual information in Eq.4 is used as a term in the Transfer Score, if some methods (e.g. SHOT) minimize this term during adaptation, will it directly cause mutual information term to become invalid?

3. Because there is no source information used in Transfer Score, can authors provide the results on Source-Free Domain Adaptation methods?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
