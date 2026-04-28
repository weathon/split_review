# Learning Effective Multi-modal Trackers via Modality-Sensitive Tuning

- Decision: Reject
- Avg Score: 5.75
- Scores: 6, 6, 6, 5

## Abstract
This paper tackles the critical issue of constructing multi-modal trackers by effectively adapting the extensive knowledge of pre-trained RGB trackers to auxiliary modalities.To address the challenges, we propose a novel modality sensitivity-aware tuning framework, namely MST, which delicately models the learning process via adaptive tuning of model weights by inherent modality characteristics. Specifically, we first investigate the parameter modality-sensitivity as a criterion for measuring a precise element-wise essentiality for multi-modal adaptation. Then, in the tuning phase, we further leverage such sensitivity to bolster the stability and coherence of multi-modal representations, thereby enhancing generalization capabilities. Extensive experiments showcase the effectiveness of the proposed method, surpassing current state-of-the-art techniques across various multi-modal tracking scenarios and demonstrating remarkable performance even in extreme conditions. The source code will be publicly available.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper addresses the complex task of constructing multi-modal trackers by adapting the capabilities of pre-trained RGB trackers to work effectively with additional modalities. The authors introduce a Modality Sensitivity-Aware Tuning (MST) framework, which leverages modality-specific characteristics to adapt model weights, enhancing the tuning process.

Key contributions include:

Parameter Modality-Sensitivity Analysis: This aspect assesses the element-wise importance of parameters for multi-modal adaptation, providing a foundation for more accurate and adaptable tracking.
Modality-Sensitive Tuning: The framework uses this sensitivity during tuning to stabilize multi-modal representations, thereby improving coherence and generalization.
Experimental results demonstrate that MST surpasses current state-of-the-art techniques across various multi-modal tracking tasks, even in challenging scenarios. The authors also commit to open-sourcing their code, supporting transparency and future research efforts. Overall, this work offers a promising solution for multi-modal tracking, with implications for broader application in tracking systems.

### Strengths
This paper has several strengths that contribute to advancing cross-modal tracking.

1. The authors address the common challenge of overfitting or underfitting in cross-modal tracking by introducing a self-regularized fine-tuning framework that maintains both modal-specific and general representations. This approach supports balanced adaptation and helps prevent the model from degrading in performance.

2. The concept of modality sensitivity is well-utilized here, with parameter-wise sensitivity allowing the model to adaptively tune based on multi-modal variations. This sensitivity-driven adjustment process not only preserves essential pre-trained knowledge but also makes the framework flexible for cross-modal tracking.

3.The method achieves state-of-the-art results across benchmarks, which is further supported by ablation studies that validate the self-regularized fine-tuning’s effectiveness in enhancing stability and performance in multi-modal tracking.

### Weaknesses
1.I suggest that the authors test the OSTrack model at a 384 resolution and the DROPTrack model at a 256 resolution to verify whether the proposed method works effectively across different resolutions.

2. Since this paper proposes a fine-tuning framework, I believe that testing only on OSTrack and DropTrack is insufficient. Testing additional models, particularly those with different architectures (e.g., CNN-based trackers), would provide stronger evidence and make the results more convincing. The current selection, while strong, limits the generalizability claims of the proposed method.

3. This is a solid piece of work; however, I would be more convinced of its effectiveness if the authors conducted additional tests to further validate the proposed method, such as evaluating the sensitivity of the method to different hyperparameter settings or analyzing the computational overhead introduced by the modality sensitivity-aware tuning.

### Questions
See weaknesses

### Soundness
3

### Presentation
3

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
In this paper, the authors propose a new fine-tuning method to adapt pre-trained RGB trackers to auxiliary modalities. Different from the existing full fine-tuning and parameter-efficient fine-tuning, the authors propose a regularized way to fine-tune the backbone network to utilize inherent modality characteristics. The entire training process does not require additional network structure and loss function. Therefore, the proposed method can be trained end-to-end without adding any new parameters.

### Strengths
[1] The proposed method is simple and generalizes well, showing significant improvements on three different multimodal tracking.
[2] Sufficient comparative experiments and ablation experiments well demonstrate the effectiveness of the proposed method.

### Weaknesses
[1] The physical meaning of parameter-wise modality sensitivity is unclear. The author may provide a diagram to illustrate it. Specifically, it's not clear how the sensitivity is quantified and what it represents in terms of the model's learned features. It would be beneficial to understand if this sensitivity is related to the magnitude of the parameter, the gradient during training, or some other measure. Furthermore, the paper lacks a clear explanation of how this sensitivity relates to the actual modality characteristics. [2] There is a lack of comparison with full fine-tuning and other parameter-efficient fine-tuning methods (e.g., lora, adapter) on the same baseline (e.g., OSTrack). The current comparisons are insufficient to demonstrate the superiority of the proposed method. It is crucial to see how the proposed method compares against these baselines under identical experimental conditions, including the same backbone network and training data. The absence of these comparisons makes it difficult to assess the true contribution of the proposed method.

### Questions
[1] How to ensure that the proposed method can transfer the pre-trained knowledge to the auxiliary modality? The author needs to give a detailed explanation.
[2]  What physical meaning does the gradient G represent in Algorithm 1?
[3] Why does the performance of the proposed method (self-reg) degrade on multiple datasets, as shown in Table 5?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper presents a modality sensitivity-aware tuning framework (MST) that improves the fine-tuning process to enhance tracking performance. It primarily introduces the concept of parameter modality sensitivity and utilizes it to standardize parameter updates, serving as a measure for multimodal adaptation. The proposed approach achieves commendable results across multiple multimodal tracking tasks and datasets.

### Strengths
1. A new modality sensitivity-aware framework, MST, is proposed, optimizing the learning dynamics of cross-modal trackers from two key perspectives: modeling parameter modality sensitivity and performing adaptive tuning that is sensitive to modality, introducing a novel fine-tuning method.
2. The use of parameter modality sensitivity to standardize parameter updates is proposed.
3. A self-integrating weight strategy is introduced to enhance the stability and consistency of multimodal representations, contributing to improved model generalization capabilities.

### Weaknesses
1. The approach mentioned in the abstract of using RGB pre-training to adapt to multimodal tasks is a common practice in the field and does not present any challenges. It fails to address the difficulties and new issues encountered in this task. Specifically, the paper does not articulate the limitations of existing RGB pre-training methods when applied to multimodal tracking, such as potential biases introduced by the RGB-centric pre-training or the challenges in effectively transferring knowledge to modalities with different statistical properties. 
2. Some sections are overly complex, and the modeling of modality sensitivity and the derivation of formulas lack readability and comprehensibility. The paper does not clearly define what constitutes modality sensitivity in the context of multimodal tracking. The mathematical formulations are presented without sufficient explanation of their underlying assumptions or the rationale behind their design. The connection between the derived formulas and the practical implementation of the proposed method is also not clearly established, making it difficult to understand how the modality sensitivity is actually modeled and used. 
3. This "parameter tuning" method does not differ fundamentally from approaches like ViPT and SDSTrack, which require task-specific training and fine-tuning. Unlike OneTracker, which can adapt to all tasks with a single fine-tuning, this method does not demonstrate significant advancements or improvements. The paper fails to highlight the specific advantages of the proposed tuning method over existing parameter-efficient fine-tuning techniques. The lack of a clear comparison with methods that achieve task-agnostic adaptation further weakens the claims of novelty and advancement. 
4. What exactly is modality sensitivity modeling in multimodal tracking? What does modality sensitivity-aware tuning for multimodal trackers entail? Although the paper discusses gradient computation and parameter-related formulas, it fails to clarify these concepts, and there is no reference to related research or underlying principles. The paper lacks a clear definition of modality sensitivity, and does not provide a theoretical framework to support the proposed approach. The absence of references to related research makes it difficult to assess the novelty and validity of the proposed method. 
5. Issues in the experimental section: a) The evaluation of tracker speed lacks information on the evaluation platform used. b) For the DepthTrack dataset, the evaluation metrics of precision-recall (pr) and success rate (sr) are unclear, along with the significance of OP0.5 and OP0.75. Moreover, the reported pr values do not match those in the official tracker papers, which state the evaluation metrics as F-score, Recall, and Precision. c) The paper mentions that SDSTrack and ViPT use OSTrack as a pre-training result, but it is known that the official evaluations also use OSTrack for pre-training. The results reported in the paper do not align with the official findings.

### Questions
1. In the section "Computational Cost and Inference Speed," why are the parameters of the trackers obtained from OSTrack and DropTrack identical despite using different pre-training methods?
2. What is Modality Sensitivity, modality sensitivity modeling and modality sensitivity-aware tuning? The definition is vague and lacks explanatory depth.
3. Why does DepthTrack use precision-recall (pr) and success rate (sr) as evaluation metrics, and what do OP0.5 and OP0.75 signify?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper tries to propose a modality-sensitive tuning technique for adapting the RGB pre-trained models to the downstream tasks (multi-modal tracking in this paper). From my perspective, this is an interesting motivation since the current community of multi-modal tracking is focusing on design unifed models. Besides, I believe this paper is well-written and various experimental results are provided to demonstrate its effectiveness.

### Strengths
1. This paper is well-written and easy to follow.
2. The motivation is reasonable and also highly related to recent trend of the multi-modal tracking community.
3. Various experiments present that the proposed technique is working with better performance witnessed on several benchmarks.

### Weaknesses
1.	Where are the results reported in Figure 1 from, LasHeR, DepthTrack, VisEvent or other datasets? In this figure, SDSTrack significantly performs worse than ViPT which against my intuition and the official paper as well. Displaying the results on larger dataset like VisEvent or DepthTrack or LasHeR should be better.
2.	A mistake in Table 3, the title ‘SR” is missed.
3.	In Table 5, when fully finetuning ViPT, the results degrade. But it grows as reported in the official manuscript.
4.	As claimed, the current tuning techniques are over- or under-fitting. But it’s not demonstrated that with the proposed technique, the methods are not over- or under-fitting. If the authors want to clarify this point through figure 1, I will suggest the authors to add this relation in the paper. Additionally, ViPT is officially trained 60 epochs and I would like to see the curves at 60 or even more epochs.
5.	The motivation is smoothing the adaption. For this purpose, the most straightforward way is utilizing smaller learning rates. But it’s not investigated in the current version.
6.	As to the definition of modality sensitivity, the training objective is employed as a criterion, which is more like measuring the model-sensitivity rather than the multi-modal sensitivity. The core issue is that the sensitivity is computed based on the loss function, which is inherently a measure of how the model parameters respond to the training data, not necessarily how sensitive the model is to different modalities. This distinction is crucial because the goal is to understand modality-specific sensitivities, not just general model sensitivities.
7.	In generally, from my perspective, the proposed method seems an adaptive Exponential Moving Average (EMA), where this adaptation is achieved by measuring the model sensitivity. Thus, it has limited relation with multi-modal tracking and does not provide any insight for this task.

### Questions
1.	Where are the results reported in Figure 1 from, LasHeR, DepthTrack, VisEvent or other datasets? In this figure, SDSTrack significantly performs worse than ViPT which against my intuition and the official paper as well. Displaying the results on larger dataset like VisEvent or DepthTrack or LasHeR should be better.
2.	In Table 5, when fully finetuning ViPT, the results degrade. But it grows as reported in the official manuscript.
3.	As claimed, the current tuning techniques are over- or under-fitting. But it’s not demonstrated that with the proposed technique, the methods are not over- or under-fitting. If the authors want to clarify this point through figure 1, I will suggest the authors to add this relation in the paper. Additionally, ViPT is officially trained 60 epochs and I would like to see the curves at 60 or even more epochs.
4.	The motivation is smoothing the adaption. For this purpose, the most straightforward way is utilizing smaller learning rates. But it’s not investigated in the current version.
5.	As to the definition of modality sensitivity, the training objective is employed as a criterion, which is more like measuring the model-sensitivity rather than the multi-modal sensitivity.
6.	In generally, from my perspective, the proposed method seems an adaptive Exponential Moving Average (EMA), where this adaptation is achieved by measuring the model sensitivity. Thus, it has limited relation with multi-modal tracking and does not provide any insight for this task.

### Soundness
2

### Presentation
3

### Contribution
2
