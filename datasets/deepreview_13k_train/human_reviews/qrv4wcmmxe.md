# Zero-shot Human-Object Interaction Detection via Conditional Multi-Modal Prompts

- Decision: Reject
- Scores: 5, 8, 6, 5

## Abstract
Human Object Interaction (HOI) detection is the task of locating and inferring the relationships between all possible human-object combinations. One of the most challenging issues is the extensive labor required for the annotation of combinatorial space of possible HOI interactions. Most existing HOI detectors rely on full annotations of all predefined interactions, resulting in a lack of generalisation for unseen combinations and actions. Inspired by the powerful generalisation ability of the large Vision-Language Models (VLM), we propose a Prompt-based zero-shot human-object Interaction Detection framework, namely PID, which can improve alignment between the vision and language representations using conditional multi-modal prompts. Specifically, different from traditional prompt-learning methods, we propose learning decoupled visual and language prompts for spatial-aware visual feature extraction and interaction classification, respectively. Furthermore, we introduce constraints for multi-modal prompts to alleviate the problem of overfitting to seen concepts in prompt learning process, thus improving the suitability for zero-shot settings. Extensive experiments demonstrate the prominence of our detector with conditional multi-modal prompts, outperforming previous state-of-the-art on unseen classes of various zero-shot settings.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper addresses the problem of zero-shot HOI detection with the key idea of using conditional multi-modal prompts. Specifically, the language prompts consist of two parts, human-designed prompts and learned ones, with the former being responsible for guiding the learning of the latter. The vision prompts is learned from instance-level visual priors, including bboxes, confidence scores, and semantic embeddings. The proposed method achieves competitive performance on HICO-DET.

### Strengths
The motivation is reasonable and the results are competitive.

### Weaknesses
 **1. Lack of analysis.**
*1)* The language prompts are initialized as the concatenations of  $C_L^a$ and $U_L$, which are subsequently forced to be close to $C_L$, why? It's unclear why the model doesn't directly use $C_L$ if the goal is to align with it. The justification for this two-step process, involving $C_L^a$ and $U_L$, and then aligning back to $C_L$, needs further clarification. Specifically, what is the benefit of optimizing $C_L^a$ and $U_L$ separately if they are ultimately forced to be close to $C_L$? What specific properties are gained by this approach that a direct use of $C_L$ would not achieve?
*2)* Does $\mathbb{A}$ contain unseen verbs? If that so, can this model recognize HOIs that are not present in HICO-DET? In other words, if I want to detect a HOI using this model, does the corresponding interaction verb have to be included in $\mathbb{A}$? The paper needs to clarify the limitations of the verb vocabulary $\mathbb{A}$ and how it affects the model's zero-shot capabilities. It is not clear whether the model can generalize to completely novel verbs or if it is limited to the verbs included in the training set, even in a zero-shot setting.
*3)* For vision prompts, where do the instance-level visual priors come from? Are they extracted by the pre-trained DETR? The paper should explicitly state how the visual priors are obtained. If they are from DETR, what specific outputs are used (e.g., bounding boxes, confidence scores, class probabilities)? How are these outputs processed to form the vision prompts? The lack of detail makes it difficult to assess the complexity and assumptions of this module.
**2.** Actually, I do not understand why the vision prompts are useful for zero-shot HOI detection. Concretely, the visual feature extracted in this model do not seem to be very sepcial compared to the that in most two-stage based HOI detectors. The paper needs to elaborate on what makes the vision features special for zero-shot detection, beyond standard two-stage methods. What specific properties do the vision prompts induce in the feature maps that enable the model to generalize to unseen interactions?
**3.** It is unclear that how these prompts work?

### Questions
See weakness.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this submission, the authors tackled the problem of zero-shot human-object interaction (HOI) detection, which aims to localize and classify all the potential human-object interactions in a given image. The zero-shot setting for HOI detection further requires the model to detect novel classes of objects and/or actions which are not seen during training. Inspired by the recent trend on leveraging vision foundation models for HOI detection, the authors proposed a novel prompt learning based approach called PID. Specifically, several vision and language prompts are adopted to enhance the visual feature extraction and interaction classification, respectively. Some optimization tricks are also explored to prevent overfitting. Experimental results on HICO-DET partially show the significance of the proposed method.

### Strengths
1. Overall, the manuscript is well-written and easy to follow.
2. The use of prompt learning for HOI problems is a good direction to explore (and also a trend in computer vision).

### Weaknesses
1. The whole framework seems like a combination of multiple existing modules, e.g., DETR, CoOp/CoCoOp style prompts. The novelty and the motivation behind each of the design are unclear. Specifically, the use of conditional vision prompts for region-level interactiveness, while intuitively plausible, lacks a clear explanation of how these prompts are generated and how they specifically capture the nuances of human-object interaction beyond simple object co-occurrence. The motivation for using learnable embeddings as context words for the text encoder also needs further justification. It's not clear why this approach is superior to other methods for adapting the text encoder for HOI tasks.
2. In 4.2, the authors mentioned that the DETR used for detecting all the humans and objects in the first stage is fine-tuned on the whole HICO-DET dataset. Does the 'whole' here mean both training and validation sets? If so, this is a weird setting as previous works (including Bansal et al. 2020 and Hou et al. 2020 that the authors claimed) never fine-tuned their detectors on the validation set, which would lead to extremely unfair comparison since the detector can significantly affect the overall performance.
3. The experiments are only conducted on a single dataset. Why the method is not tested on V-COCO?
4. The conclusion part lacks objective reflections on the deficiencies of this study and future prospects for improvements.

### Questions
See the weaknesses part. I'll consider changing the score after reading the authors' responses.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The manuscript mainly focuses on the generalization of HOI detection, particularly zero-shot HOI detection. They proposed a Prompt-based HOI detection framework to improve the alignment between the visual and language representations with multi-modal prompts. Specifically, the decouple the visual and language prompts to improve spatial-aware feature learning. Meanwhile, they present several strategies to alleviate the overfitting to seen concepts. Effective experiments demonstrate the proposed method achieves a significant improvement on unseen categories.

### Strengths
1. The proposed visual-language decomposition strategy seems reasonable and demonstrates its effectiveness.
2. The proposed method demonstrates a significant improvement in zero-shot HOI detection based on large pre-trained models.
3. Part of the ablation experiment is beneficial for further research on visual relationship understanding. e.g. the effect of backbone networks.

### Weaknesses
Overall, the paper mainly borrows the popular adapt large models and prompt strategy for down-stream tasks. Considering that there are massive similar approaches in other fields, the novelty is limited. However, the reviewer still thinks it is beneficial for the development of zero-shot HOI detection. To some extent, the core idea is similar to CoOp and the following work Co-CoOp, though this paper also incorporates the visual prompts and has made some HOI-specific designs.



### Questions
1. The proposed method achieves smaller gap between seen and unseen category. According to Tab.1, PD is larger in RF-UC setting. Could you explain it? Moreover, do you have any ablation studies to check which module is more important for reducing the PD.
2. The paper aims to achieve verb-agnostic prior knowledge. Could you explain why the verb-agnostic feature is helpful for interactiveness-aware features? By the way, the local spatial structure is actually verb-dependent, e.g., different action pattern demonstrates different relative human-object positions. Thus, capturing local spatial structure seems to contradict to verb-agnostic representations. 


In Table 4, the improvement on Unseen category is clearly better than seen category on RF-UC setting when you use a larger backbone network. Do you have any explanations?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposed a prompt-based zero-shot HOI detector. It splits the detection task into two subtasks: extracting spatial-aware visual features and interaction classification. The vision and text prompts are jointly applied to the detector. Experimental results on the zero-shot settings show its effectiveness.

### Strengths
1. This paper is well written and organized. The vision and text prompts are also clearly explained.
2. Experimental results on the zero-shot settings demonstrate the effectiveness of the proposed method.

### Weaknesses
1. Overall, this work is very similar with the following ICCV2023 paper, including the overall framework, the conditional vision prompts and the learnable modules. What's the difference between the proposed method and the ICCV2023 paper.
A1: Efficient Adaptive Human-Object Interaction Detection with Concept-guided Memory, ICCV2023.
2. For the Lcls in (11), it is not clear how to connect the model with the GT labels. 
3. This work only presents the HOI results using zero-shot settings. What's the result using the typical experimental settings?
4. Some important works from CVPR2023 are missing. Besides, the formats of some references are not consistent.

### Questions
Please see the Weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
