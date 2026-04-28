# Active Automated Machine Learning with Self-Training

- Decision: Reject
- Avg Score: 3.75
- Scores: 3, 3, 3, 6

## Abstract
Automated Machine Learning (AutoML) aims to automatically select and configure machine learning algorithms for optimal performance on given datasets. In real-world applications, training data oftentimes contain a large amount of unlabeled examples, whereas the amount of labeled examples is limited. However, AutoML tools have so far only focused on supervised learning, i.e., utilizing labeled data for training, leaving the valuable information provided by unlabeled data untapped. To address this limitation, we introduce our augmented AutoML system AutoActiveSelf-Labeling (AutoASL), which combines principles from self-training and active learning to effectively leverage unlabeled data during the training process. AutoASL iteratively self-labels previously unlabeled data instances, which is achieved through a powerful ensemble of AutoML and traditional ML algorithms, resulting in a substantial expansion of the labeled training data. We observe synergetic effects between the incorporated self-training and active learning components, leading to an improvement of the overall accuracy compared to state-of-the-art tools.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents AutoASL, an augmented AutoML system that combines principles from self-training and active learning to effectively leverage unlabeled data. Experimental results on open-source datasets show an improvement in the overall accuracy compared to state-of-the-art tools.

### Strengths
1. The problem this paper tackles is important. This paper explores the synergies between AutoML, SSL, and AL and demonstrates how methods from AutoML can effectively address SSL tasks.

2. This paper is clear and generally well-written.

### Weaknesses
1. The combination of SSL and AL is not new, and the author further introduced AutoML to the combination process. However, the motivation for introducing AutoML is unclear. As shown in Figure 1, it is just used for building the ensemble process, making the method more complex. The specific mechanism by which AutoML contributes to the core SSL/AL loop, beyond simply ensembling, is not well-articulated. It appears that the AutoML component is primarily used to select and combine models trained on different subsets of data, which is a relatively standard practice in ensemble learning, rather than a novel integration of AutoML into the SSL/AL framework.

2. As we know, the AutoML process is time-consuming, so it is better to compare the training time of AutoASL and other tools. The paper lacks a thorough analysis of the computational overhead introduced by the AutoML component. Given that AutoML often involves an extensive search over a large space of models and hyperparameters, it is crucial to quantify the additional training time required by AutoASL compared to other SSL or AL methods. This is particularly important for practical applications where computational resources and time are often limited.

3. The experimental results only show the average accuracy, which is not enough. For example, this paper mentions multiple parameters, but it does not provide a method for determining the optimal values of these parameters, nor does it conduct sensitivity analysis. Besides, since this system is a combination of many techniques, it is better to add an ablation study part to measure the influence of each part. The paper fails to provide a detailed analysis of the impact of various parameters on the performance of AutoASL. Without a sensitivity analysis, it is difficult to understand the robustness of the proposed method and to determine the optimal configuration for different datasets. Furthermore, the absence of an ablation study makes it challenging to isolate the contribution of each component (AutoML, SSL, and AL) to the overall performance gains.

### Questions
See the Weaknesses

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes AutoML system AutoActiveSelf-Labeling (AutoASL), which combines semi-supervised learning and active learning to AutoML. SSL is applied using pseudo-labeling techniques, AL is applied through an ensemble-based uncertainty measure. The proposed system is evaluated against state-of-the-art baselines across a diverse set of real-world datasets.

### Strengths
The paper is well-motivated to combine SSL and AL to AutoML as conventional AutoML methods only focused on supervised learning. 

The proposed system is thoroughly evaluated against state-of-the-art baselines across a diverse set of real-world datasets.

### Weaknesses
Based on my understanding of the experiment description, the main weakness is the comparison lacks fairness. The baseline methods are only provided with 25 labeled instances, while the proposed AutoASL benefits from extra labeled instances obtained from its active learning procedure. For a fairer comparison, the baseline methods should also be provided with a comparable number of randomly selected samples.

In page 6, the equation of DS is not correct. By definition, the DS should also exclude instances for which the probability p(x) falls outside the range of (rho, 1-rho).

### Questions
Why disagreement set should be removed from the unlabeled set? I think labeling them by oracle should also be beneficial? The paper claims that removing these items "prevents them from getting wrongly labeled in future iterations", then why items in unconfident set are kept?

Why in Algorithm 1, line 5, if no models have sufficiently high accuracy score, the algorithm should stop and get classifier from labeled dataset by TabPFN? I think collecting true labels with AL should still be beneficial to improve the classifier .

### Soundness
1 poor

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
**The paper presents AutoActiveSelf-Labeling (AutoASL), a method aiming to bridge the gap in Automated Machine Learning (AutoML) by utilizing unlabeled data by synthesizing self-training and active learning principles.** While the initiative to amalgamate these domains is commendable, the execution and substantiation within the paper leave room for substantial improvement and clarification.

A salient issue emerges in portraying the method as a symbiosis of self-training and active learning. **The integration of active learning, necessitating access to an oracle for true labels, deviates from the inherent autonomy of self-training.** This intersection raises conceptual ambiguities, as the reliance on an oracle for true labels in active learning seems to compromise the self-reliance and intrinsic labeling mechanism characteristic of self-training. Such a blend appears to muddy the clear delineation traditionally maintained between these two methodologies, necessitating a more explicit justification or clarification regarding the algorithm’s classification and operational principles.

Another notable shortcoming lies in the scope of experiments. The authors primarily tailor the AutoASL system to binary classification tasks, which curtails its generalizability and applicability across a broader spectrum of real-world problems. The omission of multi-class settings from the study's purview signifies a missed opportunity to showcase the method's versatility and robustness.

In conclusion, while the paper does introduce a unique perspective within the AutoML domain, it tends to be circumscribed by limited applicability, a lack of rigorous theoretical foundation, and insufficient engagement with contemporary methodologies and advancements. These aspects warrant critical reflection and enhancement to bolster the method's credibility, robustness, and relevance within the evolving landscape of AutoML.

### Strengths
- The paper takes a methodological step forward by attempting to unify self-training and active learning within a semi-supervised learning framework. This combination seeks to utilize both labeled and unlabeled data more effectively, marking an approach to enhancing existing systems.

- Regarding practical application, the proposed AutoASL system has demonstrated promising results in benchmark tests. This indicates a level of competence and potential usefulness in automated machine learning (AutoML), contributing to the ongoing advancements in the field.

### Weaknesses
 - **Conceptual Clarity:** The paper presents a method as a fusion of self-training and active learning, but there seems to be a conceptual misalignment in this integration. The inclusion of an oracle for true labels in the active learning component seems at odds with the autonomous nature of self-training. This amalgamation raises questions regarding the true autonomy of the proposed method and muddles the distinct identities traditionally associated with each methodology. A clearer justification or elaboration on this aspect would be beneficial for understanding the algorithm’s unique operational principles.


- **Experimental Scope:** The current study predominantly focuses on binary classification tasks, limiting the algorithm's demonstrated applicability and generalizability. The absence of experiments involving multi-class settings restricts insights into the versatility and robustness of the proposed AutoASL system. Expanding the range of experiments to encompass diverse classification scenarios would have enriched the evaluation and illustrated the algorithm's adaptability to varied real-world challenges.


- **Hyperparameter Sensitivity:** The method exhibits a pronounced sensitivity to hyperparameters, which poses practical usability challenges. If users cannot ascertain and set hyperparameters effectively a priori, it could hinder the practical deployment and user-friendliness of this framework, making this aspect a significant limitation that needs addressing to bolster the model's utility in real-world applications.


- **Reference to Contemporary Works:** There’s a noticeable lack of engagement with recent advancements and scholarly works in both self-training and active leanring. Incorporating updated references and literature is essential to enhance the paper's contextual depth, comparative analysis, and alignment with contemporary scholarly discourse.

### Questions
- Could the authors elucidate the role of the oracle within the active learning phase of the algorithm? Specifically, is there a reliance on true labels during this step, and if so, to what extent? Understanding the degree of labeling required by the oracle is crucial for a comprehensive evaluation of the model's autonomy and practical applicability in semi-supervised learning contexts. 

- What guidance or strategy does the paper offer regarding the a priori selection of hyperparameters? Clear instructions or criteria for choosing hyperparameters beforehand are crucial for users who aim to apply this framework effectively in practical scenarios. Your elucidation on this aspect would significantly contribute to the model’s usability and overall applicability.

- Could the authors provide an ablation study for AutoASL? It would be insightful to discern which specific components contribute most significantly to the overall performance of the system.

- The authors suggest extending the model to multi-class classification is relatively straightforward. Given this assertion, could you elucidate which components—between self-training and active learning—will likely be more pivotal or influential in a multi-class scenario? A clear delineation of the impact or contribution of each component in multi-class settings would be instrumental in understanding and applying the model effectively in broader contexts.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces an augmented AutoML system AutoActiveSelf-Labeling (AutoASL) for semi-supervised tabular data tasks. AutoASL combines traditional ML and AutoML algorithms and incorporates strategies from Self-training and Active Learning to leverage information from unlabeled data. The method has a certain rationality and feasibility. The paper has a clear structure and clear hierarchy.

### Strengths
This paper creative combinations of existing methods.

### Weaknesses
The contribution lacks novelty creative as the paper only combinations of existing methods. The paper claims to introduce an augmented AutoML system, but the core mechanisms rely on well-established techniques like self-training and active learning. While the combination is presented as novel, the individual components and their integration lack significant innovation. The experimental results, specifically the fact that the proposed method achieves the best results on less than half of the datasets (22 out of 47), raises concerns about the generalizability and robustness of the approach. It is unclear why the method fails to outperform existing methods on the majority of datasets. The description of the Diversity Sampling (DS) method is vague, particularly regarding the definitions of "majority of the predictors" and "minority". This lack of clarity makes it difficult to assess the practical implementation and effectiveness of this component.

### Questions
(1)	Should the line 2 and line 3 in Algorithm 1 be swapped?
(2)	In page 6, the formula of DS does not match the textual description. 
(3)	For DS, what the “majority of the predictors” and the “minority” refer to is unclear.
(4)	In Table 1, out of 47 datasets, only 22 had the best results, which is less than half of the total number of results.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
