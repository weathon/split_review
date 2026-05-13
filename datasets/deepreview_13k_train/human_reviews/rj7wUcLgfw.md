# Explaining Black-box Model Predictions via Two-level Nested Feature Attributions with Consistency Property

- Decision: Reject
- Scores: 5, 3, 3

## Abstract
Techniques that explain the predictions of black-box machine learning models are crucial to make the models transparent, thereby increasing trust in AI systems. 
The input features to the models often have a nested structure that consists of high- and low-level features, and each high-level feature is decomposed into multiple low-level features.
For such inputs, both high-level feature attributions (HiFAs) and low-level feature attributions (LoFAs) are important for better understanding the model's decision.
In this paper, we propose a model-agnostic local explanation method that effectively exploits the nested structure of the input to estimate the two-level feature attributions simultaneously.
A key idea of the proposed method is to introduce the consistency property that should exist between the HiFAs and LoFAs, thereby bridging the separate optimization problems for estimating them.
Thanks to this consistency property, the proposed method can produce HiFAs and LoFAs that are both faithful to the black-box models and consistent with each other, using a smaller number of queries to the models.
In experiments on image classification in multiple instance learning and text classification using language models, we demonstrate that the HiFAs and LoFAs estimated by the proposed method are accurate, faithful to the behaviors of the black-box models, and provide consistent explanations.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors propose a method to get high level and low level feature attributions for image classification in multiple instance learning and text classification with multiple sentences using language models. They use a local surrogate model in a LIME-like style, while optimizing for aggregating both high-level and low-level features for prediction. They also include a consistency constraint to enforce that all the attribution scores of low-level features that belong to a high-level feature sum up to that feature. They evaluate on Pascal VOC for image and Amazon reviews for text datasets, using faithfulness, correctness, and consistency metrics, and show that their method outperform baselines.

### Strengths
- The paper proposes to estimate HiFAs and LoFAs simultaneously, while previous works have only estimated them separately.
- The consistency property proposed by the authors is a reasonable property for HiFAs and LoFAs.
- The paper does experiments that ablate different important properties on both image and text datasets.
- The proposed method performed better than all baselines in all the metrics, and can get better attributions with a smaller number of perturbations.
- The method can be used in both text classification with multiple sentences (inputing as one input) and MIL where there are multiple input images.

### Weaknesses
 - The high-level features are constrained to predefined image/sentence and cannot be dynamically chosen by the method.
- With the bottom-up baselines, we can actually convert any feature attribution method to the BU version of it. The paper only compare with different versions of LIME and MILLI. It would be more convincing that faithfulness and consistency cannot be achieved together with more baselines such as (BU-)SHAP, (BU-)RISE[1], IntGrad[2].
- Insertion and deletion are only proxy metrics for faithfulness. Although there is no absolute best metric for faithfulness, it would be good to clarify that they are proxies.
- The object segments in VOC dataset are ground truths for the objects, but not necessarily the model explanation. The model can be using the unintended features to make the prediction. For example, if the wolf always appear with snow in the dataset, the model can be wrongly using the snow for predicting the class fox, but it doesn't mean that attributing to the snow is a wrong attribution. It can be the correct attribution for a model that uses spurious correlation.

### Questions
- line 237. Why does ADMM have the advantage of estimating $\mathcal{\alpha}$ and $\mathcal{\beta}$ independently even though there is the interdependence?
- line 301-303. Does it mean the LoFAs for their higher level feature attribution are just randomly selected based on the corresponding HiFA? What if you take the independently computed LoFA (without the constraint), and distribute each HiFA  proportional to the independently computed LoFA?
- How do bottom-up version of other methods like BU-SHAP, BU-RISE, BU-IntGrad do?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
- Existing studies have primarily focused on estimating either HiFAs or LoFAs, without addressing both levels simultaneously. Current naive approaches either generate a large number of queries or produce inconsistent HiFA and LoFA estimations.
- This paper introduces a model-agnostic local explanation method that effectively leverages the nested structure of input data to estimate both levels of feature attributions simultaneously.
- Experimental results in image and text classification demonstrate that the HiFAs and LoFAs estimated by the proposed method are accurate, faithful to the behavior of black-box models, and provide consistent explanations.

### Strengths
- Overall, the paper is well-written and well-organized, allowing readers to follow the narrative easily.
- The HiFAs and LoFAs estimated by the proposed method in this paper are consistent.

### Weaknesses
 - Lines 297-305: The settings of TD-LIME and TD-MILLI are unclear. Specifically, the choice of perturbation strategy, the number of samples used for local approximation, and the kernel width for LIME are not specified, making it difficult to reproduce the results and assess the fairness of the comparison. Additional explanation is needed to help readers understand their significance.
- This paper lacks a formal introduction to the evaluation metrics NDCG (line 327) and HIML (line 339). The paper should define these metrics clearly, including the specific ranking task for NDCG and the interpretation of the HIML score in the context of hierarchical explanations. Without these definitions, it is hard to understand the quantitative results.
- Figure 3 lacks an introduction to "IA," and the font size should be enlarged. The meaning of "IA" should be explicitly defined in the caption or the surrounding text. Additionally, the font size of the axis labels and the data points in the figure are too small, making it difficult to read and interpret the results.
- The experiments in this paper are conducted solely on synthetic datasets and lack results on real datasets, such as medical imaging data. The absence of real-world data limits the generalizability of the findings and raises concerns about the practical applicability of the proposed method. The synthetic data may not capture the complexity and nuances of real-world scenarios, such as those found in medical imaging, where the feature space is often high-dimensional and noisy.
- In Figure 5, BU-LIME demonstrates a higher level of consistency between LoFAs and HiFAs compared to C2FA. This observation raises questions about the effectiveness of C2FA in maintaining consistency, and the paper should provide a more detailed analysis of why BU-LIME performs better in this specific aspect.

### Questions
- Lines 89-91: The paper states that estimating HiFAs and LoFAs separately can lead to inconsistent explanations between them. How might this mismatch reduce users' trust in the model?
- Section 4.1: What would the explanation be if a bag contains more than two images featuring "cats"?

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes a technique for extracting both high-level and low-level feature attributions from black-box machine learning models. The key idea is to simultaneously estimate high-level and low-level feature attributions while enforcing consistency between them through constraints, although they have not validated the assumption that high-level and low-level feature attributions show consistency for sure. The authors evaluate the method on image classification and text classification tasks, showing improvements over baselines in terms of attribution quality and query efficiency.

### Strengths
**Originality:**
- The idea of jointly estimating high-level and low-level feature attributions with consistency constraints is novel and well-motivated.

**Quality:**
- Experiments are comprehensive, evaluating on both CV and NLP tasks.
- Quantitative metrics assess different aspects like correctness, faithfulness, and consistency of the attributions.

**Clarity:**
- The paper is generally well-written with clear visualization.

**Significance:**  
- The method enables more coherent explanations for nested input structures, which are common in many real-world ML applications.
- The approach is model-agnostic and can be applied to various types of nested inputs and black-box models.

### Weaknesses
 - One foundamental assumption of this paper is that “ the input features have a nested structure that consists of high- and low-level features, and each high-level feature is decomposed into multiple low-level features. ” 

 - Another important assumption is that there is consistency between low and high level features. However, what if conflicting attributions between high and low levels? For instance, when a high-level feature is deemed important, but none of its constituent low-level features appear significant. As the paper mentions that C2FA may perform worse when the consistency property is inherently not satisfied, I feel this is a more realistic consideration, that there is no consistency.

 - The paper lacks a formal theoretical analysis of the properties and guarantees of the proposed method. For instance, there is no discussion on convergence properties of the optimization algorithm or bounds on the estimation error, or discussion on the robustness, the robustness of C2FA to different types of perturbations or variations in the input structure.

 - It's unclear how the choice of hyperparameters (e.g., λ_H, λ_L, μ) affects the trade-off between consistency and individual attribution accuracy. Specifically, the paper does not provide a sensitivity analysis of these parameters, nor does it offer any guidance on how to choose them for different datasets or tasks. This lack of clarity makes the method less practical for real-world applications.

 - The experiments are limited to relatively small-scale problems (e.g., classifying a few images or sentences). It's not clear how well C2FA would scale to larger, more complex nested structures like full documents or large image collections. The computational cost associated with the optimization process is also not discussed, which is a crucial factor when dealing with large datasets.

 - The comparison with MILLI seems unfair, as MILLI is designed only for high-level attributions. A more appropriate baseline would be to combine MILLI with a low-level attribution method. This would provide a more direct comparison and better highlight the advantages of the proposed method.

 - There's no comparison with more recent explanation methods like SHAP-based approaches or gradient-based methods adapted for nested structures. This makes it difficult to assess the relative performance of C2FA compared to state-of-the-art techniques.

 - The image classification experiments use a synthetic MIL dataset. It would be more convincing to see results on standard MIL benchmarks or real-world applications. The use of synthetic data raises concerns about the generalizability of the results.

 - For text classification, only sentiment analysis is considered. Evaluating on more diverse NLP tasks would strengthen the claims of generalizability. Tasks like question answering, text summarization, or named entity recognition would provide a more comprehensive evaluation.

### Questions
- Just a brainfart thought, why 2 levels? How does the performance of C2FA change as the depth of the nested structure increases (e.g., to 3 or more levels)? Are there theoretical or practical limitations to extending beyond two levels? C3FA can make sense in an NLP context,  Word-level to sentence level to paragraph level.

- The paper mentions that C2FA may perform worse when the consistency property is inherently not satisfied. I feel this can be a more realistic setup, which makes C2FA less pragmatic, any justification here? 

- The current formulation assumes a fixed nested structure. How might C2FA be adapted to handle variable-length or dynamic nested structures, such as those often encountered in NLP tasks?

- The experiments focus on classification tasks. How well do you expect C2FA to generalize to regression problems or other types of model outputs?

### Soundness
2

### Presentation
3

### Contribution
2
