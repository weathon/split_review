# QPM: Discrete Optimization for Globally Interpretable Image Classification

- Decision: Accept
- Avg Score: 6.67
- Scores: 6, 6, 8

## Abstract
Understanding the classifications of deep neural networks, e.g. used in safety-critical situations, is becoming increasingly important. While recent models can locally explain a single decision, to provide a faithful global explanation about an accurate model’s general behavior is a more challenging open task. Towards that goal, we introduce the Quadratic Programming Enhanced Model (QPM), which learns globally interpretable class representations. QPM represents every class with a binary assignment of very few, typically 5, features, that are also assigned to other classes, ensuring easily comparable contrastive class representations. This compact binary assignment is found using discrete optimization based on predefined similarity measures and interpretability constraints. The resulting optimal assignment is used to fine-tune the diverse features, so that each of them becomes the shared general concept between the assigned classes. Extensive evaluations show that QPM delivers unprecedented global interpretability across small and large-scale datasets while setting the state of the art for the accuracy of interpretable models.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces the Quadratic Programming Enhanced Model (QPM), an approach for globally interpretable image classification. Unlike traditional models that primarily focus on local explanations, QPM achieves a compact, interpretable global representation of each class by assigning only a few features, typically five, per class through discrete optimization. This binary feature assignment ensures contrastive and general class representations, which allows for clear, globally understandable explanations. The model sets a new benchmark in both interpretability and accuracy for compact, interpretable models across small and large datasets, including ImageNet-1K. The approach shows robust performance by using optimally selected features that enhance global interpretability and structural grounding while maintaining high classification accuracy.

### Strengths
- The paper studies global  an important question in explainable machine learning, providing global interpretation through user defined features.

- The paper motivation is well justified, well-written and easy to understand.

- The results show that QPM achieves superior performance in structure grounding, which signifies that QPM’s learned class representations align with human-understandable features. This is very crucial in explainable machine learning.

### Weaknesses
 - The paper operates on only a few features, which is fine for natural images. However, I think in more complex domain applications such as medical imaging, more features might be required. How would more features affect the model’s optimization of feature selection in terms of time and accuracy? Specifically, how does the computational cost of solving the quadratic program scale with an increasing number of features, and what are the practical limits on the number of features that can be used before optimization becomes intractable?

- On that note, the paper lacks experiments related to high-stake domain applications such as healthcare, autonomous driving, etc. The absence of such experiments limits the assessment of the model's robustness and generalizability in real-world scenarios where interpretability is crucial. It would be beneficial to see how the model performs on datasets with different characteristics and complexities than those used in the current study.

- In QPM, Pearson correlation serves as a fundamental similarity measure that aids in identifying which features are most relevant to each class. By focusing on linear relationships, it allows the model to assign interpretable, contrastive, and compact features to classes. However, because it overlooks non-linear relationships, it may not capture all nuances in complex datasets, potentially impacting accuracy in applications where non-linear patterns are significant. Could the author elaborate on this matter? Specifically, how does the model handle datasets where the relationships between features and classes are highly non-linear, and what are the potential limitations of using Pearson correlation in such cases?

- QPM demonstrates inferior performance on SID@5, Class-Independence, and Contrastiveness compared to state-of-the-art models, suggesting that its compact binary feature assignment strategy, while beneficial for interpretability, may limit the model's ability to capture diverse, independent, and highly contrastive feature representations across classes. This trade-off reflects QPM's focus on simplicity and interpretability at the expense of some nuanced, dataset-specific feature diversity. It would be valuable to understand the specific mechanisms that cause this performance trade-off and whether there are ways to mitigate it without sacrificing interpretability.

### Questions
- Presentation-wise, I think it is better to explicitly show what the features are in human language for the figures, so that it is more friendly to the readers.

- Structure ground is only evaluated on CUB-2011, and the authors also explained why. How much effort would it take to achieve the evaluation metric on a larger dataset, such as ImageNet?

- How long is the optimization of “4 hours for fine-grained datasets, and roughly 11 hours for ImageNet”? Are these times better than previous methods?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
To develop inherently interpretable image classification, the authors propose to use a set of five diverse features for each class to perform classification. Specifically, the proposed method leverages discrete quadratic programming to extract the features that are distinct, contrastive, and generalizable across similar classes from pretrained vision models, e.g., ResNet-50. The paper provides extensive empirical results on prediction accuracy and interpretability metrics.

### Strengths
1. The idea is intuitive and easy to understand.
2. The paper is well-organized and easy to follow.
3. Different from most interpretable models, the proposed method didn’t compromise too much on the prediction accuracy.

### Weaknesses
1. Although the proposed method can provide five different heatmaps to explain the prediction of a class, the semantic meanings of these explanations are subjective. This is different from Concept Bottleneck Models (CBMs) and Testing with Concept Activation Vectors (TCAV) that can provide human-understandable concept explanations with semantic meanings. Although the authors propose structural grounding that uses dense annotations of bird parts from the CUB dataset to interpret some of the heatmaps, the concept coverage might be restrictive and cannot reflect what the model has learned. The reliance on a limited set of pre-defined concepts for grounding restricts the model's ability to capture the full range of features it may be using for classification. This is a significant limitation, as the model might be leveraging more nuanced or abstract features that are not easily mapped to human-understandable concepts.

2. The choice of five features per class might be arbitrary. Some classes might be more complicated than others, while some classes could be very simple. Would it be better to use a different or dynamic number of concepts for each class? This is actually related to the Weakness 1 above. The restricted number of five concepts makes the model learn polysemantic features, which means it might represent different concepts within a single feature. This can make the interpretation of the functionality of the features even harder. For example, as shown in Fig. 12, the green feature can highlight bird beaks on one image and wings on the other image. This might defeat the purpose of making the model more interpretable. The fixed number of features could lead to an under-representation of complex classes and an over-representation of simple ones, potentially hindering the model's overall performance and interpretability. The polysemantic nature of the features further complicates the interpretation, as a single feature might be activated by multiple unrelated concepts, making it difficult to understand the model's reasoning.

3. The proposed method highly relies on the quality of extracted features from the pretrained models, whereas they are not designed to be explainable. Since the base models are normally trained, they can also extract biased features which would significantly affect the performance of the proposed model. The reliance on pre-trained models introduces a potential vulnerability, as these models might have learned biases or irrelevant features that could negatively impact the performance and interpretability of the proposed method. The method does not address how to mitigate the impact of these pre-existing biases, which is a critical concern for real-world applications.

4. Experiments using standard metrics for explanations are missing, such as the explanation fidelity using the deletion/insertion method [1]. The proposed contrastiveness metric cannot fully reflect the explanation quality in terms of faithfulness. The authors propose Scale-Invariant-Diversity@5 (SID@5), however, the proposed method cannot achieve the best or second-best performance on the three datasets. The absence of standard explanation fidelity metrics makes it difficult to compare the proposed method with existing approaches. The contrastiveness metric, while useful, does not fully capture the faithfulness of the explanations. The fact that the proposed method does not achieve top performance on the SID@5 metric raises concerns about the quality of the learned features.

### Questions
See Weakness for details.

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
4

### Summary
With the rise of AI in several high-risk areas such as autonomous driving and medical diagnosis, being able to interpret the decisions of deep neural networks is paramount for safety. The authors focus on providing faithful global explanations as opposed to the simpler task of giving local explanations. This is achieved via their Quadratic Programming Enhanced Model (QPM) via learning interpretable class representations using only 5 features and binary assignment. This simple decision logic makes interpreting classifications feasible by humans. The authors optimize for this representation and predictive power using discrete optimization on diverse pretrained features. They evaluate their method on a variety of datasets and achieve competitive accuracy and interpretability compared to popular interpretability methods. The authors show qualitative results of their model’s interpretability and quantitative for metrics on complexity, spatial diversity, class-indepence of features, contrastiveness of features, and their structural grounding to human given concepts.

### Strengths
- Global explanations are simple and easy for humans to interpret. Weights from features are binary and only positive. Each class only has 5 features (in most experiments).
- Robustness and generalizability of their method is given based on evaluation on a variety of datasets and models
- Good use of discrete optimization and constraints to select diverse, localized, and predictive features from a pre trained set of features. Clever relaxation of constraints for feasible optimization while maintaining accuracy and interpretability.
- Ability for concepts/features to be used for predicting multiple classes.
- Competitive or SOTA accuracy and interpretability compared to other popular methods. Qualitative results show the ease of interpretability of their method.
- Ablation experiments show effectiveness of $Z_B$ and $Z_R$ objectives.

### Weaknesses
Minor:
- Writing can be unclear at times:
  - L282: Are you keeping the entries that are being clipped? Between 0 and epsilon.
  - L127-129: This sentence is unclear. How does the balanced binary assignment cause general binary concepts?
  - L372-273: You say you omit measuring the grounding of features, but provide results…Do you mean that you don’t focus on it since you only do this for CUB & TravelingBird due to lack of part annotations in other datasets?

Worth noting:
- While your method doesn’t use negative reasoning, which makes it more simple, it is a restriction/limitation.
- Your method’s performance isn’t that much above Q-SENN, but you mention the computation limitation on Q-SENN. A comparative analysis, such as a table, that shows the speed of training differences between methods would be desirable.

### Questions
- You provide misclassifications of your model in the Appendix in figure 10, but not the explanation for the classification visually. I think being able to understand the misclassification from your method’s explanation is important to your method’s strength. Could you show the explanation visualization for several misclassified samples? I think image (j) would be interesting plus images from other datasets.
- See weaknesses for other questions.

### Soundness
4

### Presentation
3

### Contribution
3
