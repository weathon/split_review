# GlocalCLIP: Object-agnostic Global-Local Prompt Learning for Zero-shot Anomaly Detection

- Decision: Reject
- Scores: 5, 5, 3, 5

## Abstract
Zero-shot anomaly detection (ZSAD) is crucial for detecting  anomalous patterns in target datasets without using training samples, specifically in scenarios where there are distributional differences between the target domain and training data or where data scarcity arises because of restricted access. Although recently pretrained vision-language models demonstrate strong zero-shot performance across various visual tasks, they focus on learning class semantics, which makes their direct application to ZSAD challenging. To address this scenario, we propose GlocalCLIP, which uniquely separates global and local prompts and jointly optimizes them. This approach enables the object-agnostic glocal semantic prompt to effectively capture general normal and anomalous patterns without dependency on specific objects in the image. We refine the text prompts for more precise adjustments by utilizing deep-text prompt tuning in the text encoder. In the vision encoder, we apply V-V attention layers to capture detailed local image features. Finally, we introduce glocal contrastive learning to improve the complementary learning of global and local prompts, effectively detecting anomalous patterns across various domains. The generalization performance of GlocalCLIP in ZSAD was demonstrated on 15 real-world datasets from both the industrial and medical domains, achieving superior performance compared to existing methods.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a novel method for zero-shot anomaly detection. GlocalCLIP separates global and local prompts and optimize them together, enabling detection of general anomalies without object dependence. Through refined text prompts and a V-V attention layer for detailed image features, GlocalCLIP effectively captures both normal and abnormal patterns. Tested on 15 industrial and medical datasets, it outperforms current ZSAD methods.

### Strengths
+  An object-agnostic global  and local prompts are supposed to learn normal and abnormal patterns.
+ Align visual features and text features by jointly optimizing global and local prompts through contrastive learning to enhance robustness.
+  The proposed method demonstrate excellent performance on multiple datasets.

### Weaknesses
This paper primarily focuses on improvements to AnomalyCLIP, particularly with regard to enhancements in text prompts. The paper has some unclear explanations that can make it difficult to understand. The distinction between global and local prompts, while conceptually introduced, lacks a rigorous explanation of how these prompts are generated and how their specific features contribute to the final anomaly detection performance. The paper also does not provide a clear explanation of why the 'semantic prompt design' performs poorly on single tasks, and why it leads to a decrease in performance in Table 4. The drastic reduction in image-level performance (F3) in medical applications, as shown in Table 3, is not sufficiently analyzed, leaving the reader without a clear understanding of the underlying causes. Furthermore, the role and selection of 'anchor prompts' are not well-defined, making it difficult to assess the impact of this design choice on the overall method.

### Questions
+ How to demonstrate the differences between global prompts $g_n$, $g_a$and local prompts $l_n$, $l_a$?
+ Does 'semantic prompt design' refer to Sec3.3 ? Why does it perform poorly on 'single', and even lead to a decrease in performance in table 4?
+ What causes the F3 to reduce image-level performance so drastically in medical applications in table 3? Could you provide a detailed explanation and analysis?
+ What' s the anchor prompts?
+ Some minor issues, such as line 316.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The authors propose GlocalCLIP, which introduces separable global and local prompts through an object-agnostic glocal semantic prompt design and jointly optimizes them to address the zero-shot anomaly detection task. They also employ contrastive learning to enhance the learning of global and local visual features. The effectiveness of the method is validated on 15 datasets.

### Strengths
The authors propose GlocalCLIP, which introduces separable global and local prompts through an object-agnostic glocal semantic prompt design and jointly optimizes them to address the zero-shot anomaly detection task. They also employ contrastive learning to enhance the learning of global and local visual features.

### Weaknesses
1. The structure of the proposed method appears to be almost identical to AnomalyCLIP, except for improvements in prompt design and contrastive learning. There is no fundamental change at the framework level.
2. The design of the V-V attention layer has already been experimented with and used in AnomalyCLIP.
3. I believe the incremental experiments in Table 3 should be conducted starting from AnomalyCLIP to demonstrate the effectiveness of the newly proposed innovations.
4. In Table 3, adding F4, which corresponds to GCL in Figure 4, does not seem to significantly improve the pixel-level metrics and even shows some decline. However, in Figure 4, adding GCL shows a clear difference in pixel-level performance compared to not adding GCL. Please explain the reason for this discrepancy.

### Questions
1. The structure of the proposed method appears to be almost identical to AnomalyCLIP, except for improvements in prompt design and contrastive learning. There is no fundamental change at the framework level.
2. The design of the V-V attention layer has already been experimented with and used in AnomalyCLIP.
3. I believe the incremental experiments in Table 3 should be conducted starting from AnomalyCLIP to demonstrate the effectiveness of the newly proposed innovations.
4. In Table 3, adding F4, which corresponds to GCL in Figure 4, does not seem to significantly improve the pixel-level metrics and even shows some decline. However, in Figure 4, adding GCL shows a clear difference in pixel-level performance compared to not adding GCL. Please explain the reason for this discrepancy.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This work investigates the task of zero-shot anomaly detection and proposes a model named GlocalCLIP, which employs a dual-branch approach for both global and local modeling of image and text inputs based on CLIP. Results across multiple datasets demonstrate the effectiveness of the proposed method.

### Strengths
- The paper is clearly presented, including both text and images, making it easy to reproduce based on existing work.
- Quantitative and qualitative experiments on multiple datasets.

### Weaknesses
 - The novelty of the method is limited compared to AnomalyCLIP. The framework still follows the standard Winclip framework and subsequent works. The authors' claim of the "first framework" is exaggerated, as prompt tuning and V-V attention have already been used in anomaly detection, particularly in AnomalyCLIP.
- The design of global and local branches is not novel. The authors should provide a more detailed explanation of what the two types of tokens model in zero-shot anomaly detection. Specifically, how do the global tokens capture overall scene context, and how do local tokens pinpoint specific anomalous regions? The current explanation lacks sufficient detail on the feature representations.
- The global loss does not use multi-stage feature fusion, unlike the local loss. Additionally, the novelty of the GCL loss is trivial, lacking any impressive design. The justification for not using multi-stage features in the global loss is unclear, especially given the potential for multi-scale information to improve global context modeling. The GCL loss, while functional, appears to be a straightforward contrastive loss without any unique characteristics.
- The introduction resembles related work, and the motivation is not convincing. The introduction does not adequately differentiate this work from existing approaches, and the motivation for the specific design choices is not clearly articulated. The connection between the identified limitations of existing methods and the proposed solution is weak.
- For Fig. 1, it is unclear whether the authors aim to highlight the novelty of the zero-shot anomaly detection task or the disadvantages of other settings. I disagree with the authors' claim in Sec. 2.4 that few-shot and multi-class models (e.g., UniAD) are unfriendly for practical applications. This claim requires more substantial justification, as few-shot and multi-class models can be quite practical in various scenarios.
- The improvement over AnomalyCLIP is not significant. The reported improvements do not appear substantial enough to justify the introduction of a new method. A more rigorous comparison, including statistical significance tests, is needed to support the claims of improvement.
- Please report the differences in training overhead, computational costs, and efficiency comparisons of different methods.

### Questions
Please refer to the Weaknesses section.

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper aims to adapt CLIP for the challenging task of zero-shot anomaly detection. The authors propose enabling object-agnostic learning to capture both global and local anomaly semantics. Experimental results seem to demonstrate the effectiveness of the proposed method.

### Strengths
1. This paper focuses on a challenging and valuable field that is practical to the real world.
2. The authors conduct experiments across diverse datasets to support their claims.

### Weaknesses
1. This paper presents similar technological contributions and organization to AnomalyCLIP. However, the authors do not provide a comprehensive comparison and discussion with AnomalyCLIP. A detailed analysis in the introduction section is necessary to explicitly tell the main technological differences from AnomalyCLIP.
2. The manuscript lacks proper citations in several sections, notably in 3.2 (Prompt Design) and 3.5 (Training and Inference). The authors should carefully review and appropriately cite previous research to acknowledge foundational work in this field.
3. The illustration in the paper is unclear. For example, it is not evident what the term "anchor" refers to in Eq. 5, and the rationale for using V-V attention instead of other attention mechanisms, such as Q-Q or K-K attention, should be clearly explained.

### Questions
See Weaknesses

### Soundness
2

### Presentation
2

### Contribution
2
