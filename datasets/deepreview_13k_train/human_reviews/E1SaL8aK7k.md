# SafeVision: Efficient Image Guardrail with Robust Policy Adherence and Explainability

- Decision: Reject
- Scores: 5, 6, 5, 6

## Abstract
As image generation models become increasingly prevalent, the need for efficient and transparent guardrails against unsafe content is more critical than ever. Traditional unsafe image classifiers, limited to predefined categories, often misclassify content due to the pure feature-based learning rather than semantic-based reasoning and struggle to adapt to emerging threats. The time and resources required for retraining on new harmful categories further hinder their ability to respond to evolving threats. To address these challenges, we propose SafeVision, a novel image guardrail system that integrates human-like understanding and reasoning with scalability. Within SafeVision, we propose an effective data collection and generation, policy-following training pipeline, and a customized loss function. In particular, we propose an efficient diverse QA generation and training strategy to enhance the effectiveness of the training process.
SafeVision is able to follow given safety policies during inference time to guardrail against new risk categories and thus avoid expensive retraining, provide accurate risky content predictions, and provide precise explanations. SafeVision operates in two modes: 1) rapid classification mode, and 2) comprehension mode that provides both classification and human-readable explanations.  In addition, considering the limitations of existing unsafe image benchmarks, which contain either only binary or limited categories, we provide VisionHARM-500K, a high-quality unsafe image benchmark comprising over 500k images to cover a wide array of risky categories. This dataset significantly broadens the scope and depth of unsafe image benchmarks. Through comprehensive experiments, we show that SafeVision achieves state-of-the-art performance in both efficiency and accuracy, with an accuracy of 91.77% on the VisionHARM-500K test set (17.77% higher than GPT-4O) and an inference time of 0.0979 seconds per image (over 50 times faster than GPT-4O). SafeVision sets a new standard for comprehensive, policy-following, and explainable image guardrail models, delivering state-of-the-art performance while aligning with human reasoning and enabling scalable adaptation to emerging threats.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes an unsafe image classification model, in which it particularly provides several features: 1) the classification results can be coupled with a human-readable explanation (i.e. why such image is classified as unsafe/harmful), 2) zero-shot ability to support user-defined novel classes (i.e. the text description/definition of the novel unsafe class), and 3) the model has fast inference time with having the output in JSON format. Moreover, this paper also proposes a VISIONHARM-500K dataset, which is large-scale, diverse (cover wide range of unsafe categories), and richly-annotated (e.g. explanations and QA-pairs) to support various training objectives.

### Strengths
+ The proposed method is experimentally shown to have superior performance with respect to different baselines (including four VLM guardrails and nine classifier guardrails) across several datasets (three multi-label datasets and six binary label datasets), with having better trade-off between model performance and computational overhead.

### Weaknesses
- The InternVL2-8B itself is already having comparable performance with respect to GPT-4o and the proposed method SafeVision-8B (which takes InternVL2-8B as its backbone) for the novel classes (cf. Figure 5), where the additional training procedure or even the model designs in the proposed method seem to not offer better zero-shot transferability.
- The comparison might be not fair enough, as the proposed SafeVision is trained on the proposed VISIONHARM-500K dataset where its harmful categories are actually the super-set (or union) of all the other multi-label and binary-label datasets. Moreover, the self-refinement training scheme used in the proposed method actually can be treated as an ensemble framework of utilizing the consensus of several strong VLMs (i.e. Qwen-VL-Chat, InternVL2-26B, LLaVA-v1.6-34B, and the continuously-updated SafeVision model). In summary, the proposed method adopts larger training set, leverages the ensemble framework during training, and is built upon a stronger backbone (i.e. InternVL2), it is hence not surprising to have superior performance than the other baselines, leading to potential concern of unfair comparison (perhaps there should be baselines of training the open-source VLM guardrails on the proposed dataset?).
- From the ablation study, it looks like the proposed method is quite sensitive to the hyper-parameter tuning (e.g. critical token weight ratio and the weights of VLMs in the self-refinement training scheme, while the value and the varying schedule of these hyper-parameters are manually set) and the format of few-shot samples.
- The design for the decoder of SafeVision for having fast inference is actually not new (i.e. having a list of special token in the tokenizer to improve the inference efficiency).
- The overall organization seems to be problematic, as the details of dataset collection and proposed method are mostly provided in the supplementary, leading to the concern of self-containment for the main paper.

### Questions
The authors should carefully address the concerns as listed in the weaknesses.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper presents a dataset and model for detecting harmful visual content, with explanation and adaptation capability to new policies. The proposed method creates VisionHARM-500K dataset from LAION dataset, by using VLM filtering and image captioning. Built on the proposed VisionHARM-500K dataset, this paper also presents a model for detecting harmful content, which supports two modes. The first mode simply outputs classification results, and the second mode also generates a textual explanation with the harm score. To demonstrate the effectiveness, this paper compares the proposed method with many other models on binary classification, multi-classification, and new category harm classification. This paper presents stronger results in most settings than previous work. Overall, the paper is clearly written, but I have some concerns on the details, especially in the comparison with other methods. Therefore, I lean to reject this work slightly, even though this paper presents a lot. I could change my mind after rebuttal.

### Strengths
+ This paper presents a new dataset, VisionHARM-500K dataset, which can be used by the community to study vision safety problem. Researchers can also utilize the results presented in this paper as baseline, to move forward and achieve better results.

+ This paper presents better results than many previous work in terms of binary classification and multi-classification tasks. Ablation studies are also presented.

### Weaknesses
- This paper shows fewer novelties or contributions in model architecture for VLM learning and inference. In addition, this paper discusses very few about the network architecture. I prefer to learn more about model details about the proposed method. I cannot see how vision encoder and policy prompt encoder fuse each other.

- The experiments are not very convincing. For the comparing methods, how do those models train? Are those model trained on VisionHARM-500K dataset? It is unclear that the proposed method is significantly better than other methods, because of potential data distribution bias. From Figure 5, I am not convinced that the proposed model is significantly better than other models, as the proposed method trained on VisionHARM-500K and tested on VisionHARM-500K. In new category experiment, we can see GPT-4o is better than this method.

- In Table 1 & 2, citations are necessary for each comparing method.

### Questions
See weakness.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes SafeVision, a novel image guardrail system based on Vision-Language Models to detect and comprehend synthetic images. The system consists of two key modules: fast classification for general filtering scenarios and multimodal comprehension for policy-specified guardrails. The framework is evaluated with multiple safeguard scenarios and compared with diverse models. The proposed dataset is sufficiently scalable compared to existing datasets.

### Strengths
1. The research topic of safeguarding image generators is important and intriguing.
2. The proposed dataset is novel with good contributions.
3. The evaluation of various existing safeguarding methods is fair.

### Weaknesses
1. The proposed self-refinement training involves a testing procedure where the new version of the model is evaluated on the test set and misclassified instances are extracted & analyzed to curate new policies (Line 267 - Line 269). The paper should argue why and how such a procedure avoids **test set leakage**. If the test set information is encoded in the renewed policy, the procedure could lead to inflated performance on the test set because the model has already captured the exact test information during training. Also, the paper should compare how existing works handle misclassified instances in the test set.

2. The paper presentation needs significant improvement. For example, Appendix C.5 refers readers to a null table (Line 1407) and the prompt description on page 20 exceeds the page boundary (Line 1026 - Line 1079). The quotation marks in the prompt description are often monotonously right quotations (page 16, page 19, page 22). The reference list is also not well-curated. For example, the referenced website addresses often far exceed the page boundary and are obscured (Line 665, Line 778). Note that the Llama-Guard Team's paper is referenced as "Team (2024)" in the paper (Line 144, Line 215, ...), which reads strange. Also, there are many lines of unspecified space on page 18 (Line 922 - Line 958). **While a few minor errors in the paper presentation will not affect the rating, **too frequent observation** of them will harm the rating since they are not aligned with the proceeding guidelines and are not beneficial for future readers.**

### Questions
Please address my concerns stated in the weakness section. Although the novelty and presentation are limited, I still appreciate the contribution of this new dataset for image safeguarding. I give this submission an initial rating of borderline reject, and I look forward to the authors' response.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work explores multimodal large models for detecting harmful content. Existing work suffers from low generalization and difficulty in handling new categories of hazards. Therefore, the authors built VISIONHARM-500K, a high-quality unsafe image benchmark comprising over 500k images to cover a wide array of risky categories. Based on this benchmark, the authors proposed SAFEVISION, which supports multiple modes and provides precise explanations. Experiments show the effectiveness and efficiency of the proposed method.

### Strengths
1. This paper constructs VISIONHARM-500K, which is conducive to the further development of image moderation.

2. The proposed SAFEVISION can better distinguish harmful content and has extremely high efficiency.

### Weaknesses
1. The categories defined by the dataset should be reflected in the main body.
2. How does SAFEVISION judge the content of new categories? Is it controlled only by prompts?
3. In Section 4.2, is the improvement to the tokenizer to add category nouns to the vocabulary library?
4. This work declares the contribution of the dataset, but there is no related open-source plan in the text. Will the code and dataset of this paper be released?

### Questions
See Weaknesses.

### Soundness
4

### Presentation
3

### Contribution
4
