# Spatiotemporal Backward Inconsistency Learning Gives STGNNs Icing on the Cake

- Decision: Reject
- Scores: 3, 5, 3

## Abstract
Spatiotemporal prediction models facilitate various smart-city applications across various domains,such as traffic and climate. While current advancements in these models emphasize leveraging cutting-edge technologies to enhance spatiotemporal learning, they often operate under the implicit assumption of spatiotemporal feature consistency between inputs and labels, overlooking the critical issue of input-label inconsistency. In this study, we introduce a universal spatiotemporal backward inconsistency learning module capable of seamless integration into a variety of models, offering a notable performance boost by explicitly modeling label features to address input-label inconsistency. Our approach includes the development of a spatiotemporal residual theory, advocating for a holistic spatiotemporal learning that encompasses both forward spatiotemporal learning to capture input data’s spatiotemporal features for generating base predictions, akin to existing STNNs, and a backward process to learn residuals that rectify input-label inconsistency, thereby refining the base predictions. Based on this theory, we design the Spatio-Temporal Backward Inconsistency Learning Module (STBIM) for this backward correction process, comprising a residual learning module for decoupling inconsistency information from input representations and label representations, and a residual propagation module for smoothing residual terms to facilitate stable learning. The generated prediction correction term is used to enhance the prediction accuracy. Experimental results on 11 datasets from the traffic and atmospheric domains, combined with 15 spatiotemporal prediction models, demonstrate the broad positive impact of the proposed STBIM. The code is available at https://anonymous.4open.science/r/ICLR2025-2598.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a spatiotemporal prediction module, the spatiotemporal backward inconsistency learning module (STBIM), to solve the problem of inconsistent input labels in existing spatiotemporal neural networks (STNNs) (i.e., the same input may lead to different outputs, or different inputs may have the same output). By combining label features and integrating spatiotemporal residual theory, STBIM effectively improves the prediction accuracy of the model. Experimental results show that STBIM significantly improves the prediction performance across multiple datasets.

### Strengths
1. The authors introduces an innovative module to capture spatiotemporal inconsistencies between inputs and outputs (labels in this paper).

2. The authors conduct many experiments to show the effectiveness of the proposed model STBIM.

3. The code is given which is helpful to reproduce the experimental results.

### Weaknesses
1. I have significant reservations about the authenticity of the experimental results. For example, on page eight, the findings for the "LargeST-GBA dataset", particularly regarding the BigST model, show that the average improvement is considerably less than the claimed increase of over seventeen percentage points.

2. The model's core concept involves correcting predicted outcomes through spatiotemporal residuals. This notion closely resembles shift learning in spatiotemporal networks, yet there is no discussion of the shifts.

3. Additionally, the writing quality in the article requires improvement, as evidenced by a typographical error in the first line of page five ("to be be") and inconsistencies in tense and capitalization throughout.

### Questions
1. The third subplot in Figure 1 is not mentioned in the text, and the "abnormal signal" it shows is not referenced in the document. Is it necessary to keep it? What is its significance?

2. The text highlights the inconsistency between inputs and outputs, using the prediction label to represent the time series of a later time window. Can this be expressed more clearly? If a label is used, could the specific cases be clarified? Typically, a label is a distinct value, not a continuous range of floating-point numbers.

3. If all results are accurate, why do many fine-tuned results exceed those of joint tuning? Can this be analyzed further?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces a Spatio-Temporal Backward Inconsistency Learning Module (STBIM) designed to enhance spatiotemporal prediction models by addressing input-label inconsistencies. This approach incorporates a residual learning mechanism to refine predictions and improve performance across multiple domains, such as traffic and climate prediction. STBIM’s integration demonstrates significant accuracy improvements in various datasets and model types.

### Strengths
1. The paper presents a novel paradigm for handling "input-label inconsistencies" with residual theory based on spatiotemporal Gaussian Markov Random Field.
2. The proposed STBIM is model-agnostic, allowing easy integration into existing models without extensive modification.
3. Experiments demonstrate versatility through extensive testing across diverse datasets and models.

### Weaknesses
1. The paper lacks a thorough discussion of related works addressing spatiotemporal inconsistency. While the discussion on "Label propagation in GNN," does not directly address the core issue and could be streamlined.
2. The connection between the spatiotemporal residual theory and the proposed STBIM module is somewhat unclear. See questions for details.
3. The paper does not include an ablation study for the individual components of STBIM, such as the retrospect MLP and the propagation kernel for smoothing.
4. The core concept of "input-label inconsistencies" and the proposed residual learning approach are not well-defined. The paper claims to address inconsistencies between input and label features, but the method appears to compute residuals based on the difference between input and predicted label embeddings. This approach is problematic because it does not capture the true discrepancy between input and ground truth label features. The use of predicted label embeddings as a proxy for ground truth label features is not well-justified, and it is unclear how this approach provides meaningful information for learning.
5. The paper claims that the model can handle cases where similar inputs have different labels, but this is not convincing. Given that the model is deterministic, it would struggle to differentiate between two identical inputs with different labels. The paper does not provide a clear explanation of how the proposed method addresses this fundamental limitation.

### Questions
1. The paper introduces the unique concept of "input-label inconsistencies" in spatiotemporal prediction. Could you clarify how this concept differs from other types of spatiotemporal inconsistency, such as spatiotemporal out-of-distribution (OOD) or distribution shift?
2. The current claim regarding differences between input and label features (Line 269) seems ambiguous. While the paper uses hidden embeddings as features for input and label, the original values can also be considered features. Does this imply that the difference between input and label values could serve as the residual (if labels are available)? This seems contradictory to Equation 8, which defines the residual as the difference between prediction and label. Could you clarify?
3. In the case of “similar input data resulting in different labels," if there are two identical inputs with different labels, wouldn’t the method struggle to predict correctly since it is a deterministic model? Can this limitation be addressed?
4. What is STRIP in Figure 4(b)?
5. Can the authors provide insights into the computational overhead introduced by STBIM, particularly in large-scale applications?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes Spatio-Temporal Backward Inconsistency Learning Module (STBIM) designed to enhance Spatiotemporal Neural Networks (STNNs) by addressing the problem of input-label inconsistency in spatiotemporal prediction tasks. STBIM operates by capturing residuals between input data and labels through their spatio-temporal features, smoothing these residuals through a residual propagation kernel, and adding the resulting corrections to the base predictions generated by STNNs. Extensive experiments across multiple datasets and baseline models demonstrate substantial improvements in prediction accuracy.

### Strengths
* The experimental validation across 11 datasets with diverse STNN architectures showcases the generalizability and effectiveness of STBIM. Performance gains up to 21% underscore its practical impact.
* The fact that STBIM is designed to be compatible with a wide range of STNN architectures enhances its potential for broader application and scalability in different domains like traffic and atmospheric forecasting.

### Weaknesses
 * The method for measuring the inconsistency between the input data and labels seems redundant in spatio-temporal methods. Ideally, the spatio-temporal methods such as convolution or transformer and their temporal variants (convLSTM or spatio-temporal transformer) have the inductive biases required to take into account the spatio-temporal features that are mapped to labels. It is just a matter of adding additional layers that anyway this method proposes to use (STBIM is a separate module). I would suggest the authors to provide a more detailed comparison between STBIM and traditional spatiotemporal architectures, specifically addressing how STBIM's approach differs from or improves upon simply adding more layers. Further providing clarification on how STBIM's method of measuring inconsistency provides information that cannot be captured by the inductive biases of existing spatiotemporal methods would help the paper.
* Since, there is no new information added (such as test-time labels), adding just an inconsistency loss should not bring any new information for such impressive performance gains and those gains should be achievable through traditional architectures as well. Conducting an ablation study comparing STBIM to equivalent increases in model complexity for traditional architectures. This would help demonstrate why traditional architectures cannot achieve similar gains. I would suggest the authors explain in more detail how STBIM extracts additional information from the existing data that traditional architectures may miss.
* Although performance gains are highlighted, the computational cost associated with adding STBIM to complex STNN models is not fully explored. An analysis of training and inference times with and without STBIM would clarify its practical feasibility. A detailed computational cost analysis, including training and inference times, for models with and without STBIM across different dataset sizes and model complexities could be provided. Additionally, a breakdown of memory requirements for models with and without STBIM.

### Questions
* Could the authors provide an in-depth breakdown of the computational resources required to train models with and without STBIM? How does this impact its scalability?
* how much of the above performance can be recovered by using additional spatio-temporal layers?
* How will the test-time labels be used if available?
* What extra information is the inconsistency loss bringing/recovering from the input data apart from just maintaining a spatial smoothness, for which convolution / transformer have the right inductive bias?

### Soundness
2

### Presentation
2

### Contribution
2
