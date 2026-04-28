# Interpretability-driven active feature acquisition in learning systems

- Decision: Reject
- Avg Score: 3.75
- Scores: 3, 3, 6, 3

## Abstract
In real-world applications like medicine, machine learning models must often work with a limited number of features due to the high cost and time required to acquire all relevant data. While several static feature selection methods exist, they are suboptimal due to their inability to adapt to varying feature importance across different instances. A more flexible approach is active feature acquisition (AFA), which dynamically selects features based on their relevance for each individual case. Here, we introduce an AFA framework that leverages SHapley Additive exPlanations (SHAP) to generate instance-specific feature importance rankings. By reframing the AFA problem as a feature prediction task, we propose a policy network based on a decision transformer architecture, trained to predict the next most informative feature based on SHAP values. This method allows us to sequentially acquire features in order of their predictive significance, resulting in more efficient feature selection and acquisition. Extensive experiments across multiple datasets show that our approach achieves superior performance compared to current state-of-the-art AFA techniques, both in terms of predictive accuracy and feature acquisition efficiency. These results demonstrate the potential of explainability-driven AFA for applications where feature acquisition cost is a critical consideration.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes an active feature acquisition (AFA) framework leveraging Shapley Additive Explanations (SHAP) values to determine feature importance on an instance-by-instance basis. The authors train a decision transformer model to imitate a SHAP-based oracle, intending to optimize the sequential selection of features to maximize predictive accuracy while minimizing acquisition cost. The model's training follows a teacher-forcing-style imitation learning approach, complemented by an on-policy adaptation stage. Experiments are conducted on various image datasets to evaluate the method against existing AFA techniques.

### Strengths


### Weaknesses

### Questions

### Strengths
- The use of SHAP values for feature ranking supervision in AFA is novel, bringing interpretability-focused methods into the AFA setting.
- The two-stage training strategy seems interesting. It combines imitation learning and on-policy adaptation to aligns feature acquisition with SHAP rankings, improving the model’s robustness.
- The authors provide a farily clear description of the model's structure and training pipeline, which facilitates reproducibility.

### Weaknesses
 - Reliance on SHAP values for ranking: The effectiveness of SHAP values as a basis for feature acquisition is questionable. Previous works, such as "Marginal Contribution Feature Importance - an Axiomatic Approach for Explaining Data" (Amnon Catav, et al. ICML 2021), have pointed out that SHAP can dilute the importance of redundant features, while "Problems with Shapley-value-based explanations as feature importance measures" (IE Kumar, et al. ICML 2020) highlights how SHAP’s equal distribution of influence may not suit non-additive models. These limitations challenge the suitability of SHAP-based ranking for supervising feature acquisition policies. Specifically, SHAP values, by design, distribute credit for a prediction among all features, even when some features are highly correlated or redundant. This can lead to a scenario where the model is encouraged to acquire multiple correlated features, even if a single feature would provide most of the relevant information. This is particularly problematic in high-dimensional feature spaces where redundancy is common.
- Baseline: The evaluation lacks an essential baseline where features are acquired based on a global feature importance ranking. Specifically, determining a global ranking from the training dataset and using this static ranking to acquire features for each test instance would offer a valuable comparison, assessing the advantage of instance-specific rankings in this AFA context. The absence of such a baseline makes it difficult to ascertain whether the proposed method's performance gains are due to the instance-specific nature of the feature selection or simply due to a more effective feature ranking method in general. A global ranking approach, such as one derived from a feature selection algorithm applied to the entire training set, would provide a necessary point of comparison.
- Dataset selection: The experiments focus purely on image classification datasets, which are not the most relevant to AFA. In practical applications like healthcare or finance, where feature acquisition is costly, a dynamic approach to selecting features would be more impactful. Without evaluations on these types of datasets, the real-world utility of the proposed method remains unclear. The current evaluation does not adequately address the practical challenges of AFA, such as varying acquisition costs, noisy features, and the need for efficient feature selection in time-sensitive scenarios. Furthermore, the reliance on image data, where features are often spatially correlated, may not generalize well to other data modalities.

### Questions
- How might this model perform on datasets more representative of typical AFA applications, such as those in medical diagnostics, where feature acquisition incurs genuine costs? In such scenarios, I believe that acquisition based on global feature ranking is a strong baseline.
- To increase the evaluation's persuasiveness, consider conducting experiments on various tabular datasets.
- How does the model’s SHAP-based feature selection strategy compare with alternative methods, such as conditional mutual information, especially in scenarios with highly correlated features?

### Soundness
2

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
5

### Summary
The goal of this paper is to sequentially acquire features, for applications where using all features is costly. To do that, the paper first uses SHAp to generate feature rankings for all training data, and then train a policy network to predict the next most important feature.

### Strengths
The problem is interesting and important. The performance of the proposed method is good according to the experiments.

### Weaknesses
There are two main issues with the paper.

1. The main motivation for the method is that acquiring all features can be expensive, time-consuming and sometimes have to be done sequentially. This argument convinced me at the introduction when the authors mention medical settings. However, all experiments were done using image data, except one using email spam data. I cannot think of any realistic settings where one can only query one patch at a time from an image, or one feature at a time from emails. The application of these methods to these datasets are not convincing at all. Since the authors mentioned medical setting, why not using medical datasets to prove the value of the method?

2. Another concern is the use of SHAP to determine the feature importance. For this specific setting, what the authors really need to predict is the feature that will has a big impact on the predictive performance of a model, not features that will make biggest contribution to the output. For example, one feature could make biggest contribution, but if it makes almost the same contribution to every instance, then it will have little impact on the predictive performance because knowing that feature does not increase the accuracy much. I think a more appropriate feature importance should be something like mean decrease in accuracy.

### Questions
Did you try using other importance metrics like mean decrease in accuracy? Why did you use SHAP?

Can you find more convincing and realistic applications of your method?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a new approach to active feature acquisition, particularly for scenarios where gathering all features is expensive or time-consuming, such as in medical applications. They introduce the first AFA framework that leverages SHAP values to determine instance-specific feature importance rankings. They reframe AFA as a feature prediction task rather than a feature exploration problem, using a decision transformer architecture to predict which feature to acquire next based on SHAP values. They propose a novel two-stage training approach: First stage: Training using SHAP value ranking order. Second stage: Training using predicted feature acquisition order to improve real-world performance. Through experiments across multiple datasets they demonstrate their method achieves superior or comparable results to state-of-the-art AFA techniques.

### Strengths
-The paper reframes AFA from an exploration problem to a prediction problem and leverages SHAP values for determining instance-wise feature importance in AFA, which is novel and innovative

### Weaknesses
 - The paper lacks theoretical justification for why predicting SHAP values should lead to optimal feature acquisition
-This method bridges between interpretability methods and feature acquisition, it doesn't provide any interpretability results 
- No evaluation of robustness to: a) Input perturbations, b) Different model architectures beyond those tested, c) Changes in the SHAP value computation approach

### Questions
To improve the paper, I would recommend: Adding detailed analysis of policy network prediction patterns and failure modes, providing thorough ablation studies of the training process

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces a new approach to active feature acquisition (AFA) that uses SHAP to determine which feature to acquire next given instance. The key idea is to use pre-specified SHAP values on the training set obtained using a pretrained classifier, and then use these values to train a policy network to predict the next most informative feature based on these SHAP values. The authors show that their approach outperforms current state-of-the-art AFA techniques on multiple datasets (4 image datasets and 1 tabular dataset).

### Strengths
-	The paper is in general well-written and easy to follow.
-	The authors provide extensive quantitative analysis by thoroughly comparing the proposed method to a wide range of feature selection methods.
-	The two-stage training approach and the use of SHAP values to guide feature acquisition sounds like a promising direction.
-	The proposed method provides state-of-the-art performance.

### Weaknesses
 - The authors don't fully justify why they use SHAP values to guide feature acquisition. Although their "Oracle" method, which uses the ground-truth SHAP, seems effective, SHAP might not be the best way to choose the most informative features. SHAP measures how much each feature contributes to a change in the model's prediction, but this doesn't necessarily mean those features are the best for making accurate predictions with only a few features. Specifically, the underlying assumption that features with the highest SHAP values in a fully trained model will also be the most informative when only a subset of features is available needs further justification. It is not clear that maximizing the change in prediction based on individual features will directly translate to optimal accuracy when only a limited number of features can be acquired. A more rigorous explanation of why SHAP is suitable for guiding feature acquisition in a limited-feature setting is needed.
- The approach might not fully consider how the importance of acquiring a feature can change based on what features are already acquired. The ordering of SHAP value is fixed during training and thus the policy network (even though it takes the sequence of observed features as input) will neglect such dependencies, which could be the key to AFA. This static ordering may not accurately reflect the dynamic nature of feature importance in an active acquisition scenario. For example, a feature that is highly informative on its own might become redundant if a correlated feature has already been acquired. The policy network should ideally be able to re-evaluate feature importance based on the current set of acquired features.
- The authors motivated the impact of AFA on healthcare and medical applications, but only one out of five datasets is healthcare-related. The other datasets are general image datasets where the artificial partitioning into smaller patches doesn't reflect real-world scenarios. Using real-world tabular medical datasets (like MIMIC or METABRIC) would better demonstrate the method's relevance to its stated application. The current evaluation may not fully represent the challenges and complexities of real-world medical data, where feature acquisition often has significant implications.
- The authors do not clearly justify why a decision transformer is used as the policy network and the entire sequence of reward is used as input. It's unclear if performance gains are from this specific architecture or from the SHAP guidance. Ablation studies or comparisons with alternative policy network architectures would help isolate the contribution of the decision transformer. Specifically, it would be valuable to understand whether a simpler model could achieve comparable performance when using the SHAP-based feature ordering.
- More in-depth case studies would strengthen the paper. Showing how and why feature acquisition order varies across different samples would provide valuable insights. For instance, analyzing cases where the proposed method significantly outperforms baselines could reveal specific scenarios where SHAP guidance is particularly effective. Conversely, examining cases where the method struggles could highlight potential limitations and areas for improvement.
- Training Strategy: The details of the training process, especially how the context length ($\ell$) is chosen and how pre-selection is used, could be clearer. Pseudo-code would improve understanding and reproducibility. Specifically, providing more details on the criteria used for selecting the context length and how it impacts the performance of the policy network would be helpful. Additionally, a more detailed description of the pre-selection process, including the rationale behind the chosen pre-selection method, would enhance the clarity of the training strategy.

### Questions
-	Regarding weakness 1, please elaborate the underlying motivation of using the ordering of SHAP value for training the policy network. For instance, why the features that contribute to the model prediction the most should be most discriminative and thus suitable for AFA?
-	The SHAP ordering of features is treated as a fixed ground truth. However, in reality, the order in which features are most informative might shift depending on the information already acquired. For example, if the model already has access to a highly predictive feature, the relative importance of other features might decrease or change. The current approach, by relying on a pre-specified SHAP ordering, could overlook these dynamic interactions between features, potentially leading to suboptimal feature acquisition choices. Could the authors explain why this is not an issue?
-	How does the policy network prevent the selection of an already-chosen feature? I couldn’t identify any explicit architecture design or loss to prevent the re-selection of previously acquired features as the policy network simply provides a softmax output at each instance.
-	To better illustrate the advantages of the proposed SHAP-based AFA method, could the authors provide some case studies? It would be helpful to see examples where traditional AFA methods fail, but the proposed method, guided by SHAP ordering, produces more accurate (discriminative) predictions. Additionally, consider including a subgroup analysis based on similarities in feature acquisition order. This would help to demonstrate the effectiveness of using SHAP values in guiding AFA.

### Soundness
3

### Presentation
3

### Contribution
3
