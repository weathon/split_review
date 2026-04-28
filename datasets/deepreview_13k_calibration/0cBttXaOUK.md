# Multi-aspect Knowledge Distillation with Large Language Model

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5, 5

## Abstract
Recent advancements in deep learning have significantly improved performance on computer vision tasks. Previous image classification methods primarily modify model architectures or add features, and they optimize models using cross-entropy loss on class logits. Since they focus on classifying images with considering class labels, these methods may struggle to learn various aspects of classes (e.g., natural positions and shape changes). In contrast, humans classify images by naturally referring to multi-aspects such as context, shape, color, and other features. Inspired by this, rethinking the previous approach from a novel view, we propose a multi-aspect knowledge distillation method using Multimodal Large Language Models (MLLMs). Our approach involves: 1) querying Large Language Model with multi-aspect questions relevant to the knowledge we want to transfer to the model, 2) extracting corresponding logits from MLLM, and 3) expanding the model's output dimensions to distill these multi-aspect logits. We then apply cross-entropy loss to class logits and binary cross-entropy loss to multi-aspect logits. Through our method, the model can learn not only the knowledge about visual aspects but also the abstract and complex aspects that require a deeper understanding. We primarily apply our method to image classification, and to explore the potential for extending our model, we expand it to other tasks, such as object detection. In all experimental results, our method improves the performance of the baselines. Additionally, we analyze the effect of multi-aspect knowledge distillation. These results demonstrate that our method can transfer knowledge about various aspects to the model and the aspect knowledge can enhance model performance in computer vision tasks. This paper demonstrates the great potential of multi-aspect knowledge distillation, and we believe it offers a promising direction for future research in computer vision and beyond.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper starts from the perspective of how humans classify images, where humans typically consider multi-aspects such as context, shape, color, and other features. Motivated by this, the author proposes a multi-aspect knowledge distillation method that utilizes Multimodal Large Language Models (MLLMs) to improve image classification performance. By querying, extracting relevant logits, and expanding the model's output dimensions, the method achieves the knowledge learning of visual aspects and abstract knowledge. This method enhances the performance of baseline models across lots of experiments, demonstrating the potential of multi-aspect knowledge distillation in computer vision and other tasks.

### Strengths
1.This paper is written in a clear and straightforward manner, making it easy to quickly grasp the method's approach.
2.The paper conducted a lot of experiments, and the figures and tables are well-organized.
3.The authors claimed they are the first to offer a novel perspective on distilling multi-aspect knowledge regarding abstract and complex concepts. I have seen the author's efforts in the design of knowledge transfer.

### Weaknesses
1. The proposed method shows some improvement on some classic CNN-based models but lacks experiments on ViT-based models. 
2. In the knowledge distillation task, the comparison is only done with KD, lacking comparisons with other knowledge distillation methods [1,2].
3. The improvement in object detection tasks is very limited in Tab7, and there is no comparison done on currently well-performing object detection methods. Object detection is inherently a more fine-grained visual task than classification. Still, the experiments in this paper do not demonstrate the method's effectiveness of multi-aspect knowledge distillation in detection.
4. The explanation for the poor zero-shot classification performance of MLLMs is missing in Tab 1. Incorrect knowledge could also be distilled to the student model.
5. Missing the training curve of MaKD Loss with the number of iterations. The visualization of t-SNE embeddings and the model's multi-aspect responses to a single image are presented in Fig 4 and 5. There is no overall evaluation of the model's responses to multi-aspect on the test dataset.

### Questions
The paper develops a simple way to distill the multi-aspect knowledge of MLLM to perform image classification using a student model. The experiments show some improvements however I still believe that the contributions of this paper are quite limited. Additionally, the baseline models selected in this paper are quite outdated. In summary, the overall technical novelty of the direct injection of knowledge from large models seems incremental.

1. As shown in Tab 1, MLLMs perform badly in zero-shot classification on fine-grained image test datasets, how do we ensure that MLLMs provide correct answers across multiple aspects? 
2. There are questions regarding the task details when extending to object detection: should the input to the MLLM be the object within the box or the entire image? The entire image may contain multiple objects, and the MLLM's response may not be accurate.

### Soundness
2

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
4

### Summary
This paper proposes a new knowledge distillation method. It performs multi-aspect knowledge distillation with the LLM and the MLLM. LLM is utilized to generate multi-aspect questions by using the class and prompt. It further adopts the MLLM to extract the logit for multi-aspect questions and obtain the probabilities corresponding to yes token. The student is optimized by the original cross-entropy loss and the distilled binary cross-entropy loss. Extensive experiments are conducted to demonstrates the effectiveness of the proposed method. It also extends to object detection task to evaluate the great potential.

### Strengths
The paper is well-written, with a clear and logical flow from the introduction through to the conclusion. The authors present simple ideas in a straightforward manner, making the paper accessible to readers from diverse backgrounds. The experimental setup is meticulously organized, with each step of the process described in a way that facilitates reproducibility. The authors outline the methodologies, datasets, and evaluation metrics in clear subsections, allowing readers to follow the experimental design intuitively.

### Weaknesses
1、	Limited Experimental Setting：The experimental setting is narrow, which restricts the generalizability of the findings. The scale of datasets is small and may not be sufficient to demonstrate the robustness of the proposed method across different scenarios. Expanding the experimental scope to include more varied or challenging datasets such as the full ImageNet would significantly strengthen the paper.

2、	Lack of novelty: The proposed method directly adopts the MLLM’s output logit to perform distillation. The principle behind this design is not fully demonstrated. Why MLLM can help improve the performance of student and what features support this? 

3、	Some details are missing, and some experimental comparisons are not fair. The parameter number of the MLLM is larger than the teacher model in the traditional KD. It is questionable whether the improvement is due to the large number of parameters or the inherent properties of the MLLM itself. What will happen to the performance of the student model if only adopting the large vision encoder in MLLM. Some comparison to the traditional methods is not fair. The basic KD adopted in experiment in classification is too old and many improved versions should be used.

4、	There is not the comparison to SOTA KD method in object detection and the baseline should also adopt the powerful setting.

### Questions
I hope the author can better explain the novelty of the paper and the principle of how the algorithm is really effective.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents a multi-aspect knowledge distillation framework that uses MLLMs to improve model performance in visual understanding and detection tasks. By expanding the model’s output dimensions, the method distills multi-aspect logits that encapsulate diverse visual and contextual features beyond standard class labels. Extensive experiments on various image classification datasets, complemented by thorough ablation studies, underscore the framework's effectiveness and robustness.

### Strengths
1. The core idea is simple but looks effective.
2. The paper writing is fluent and easy to follow.
3. The paper conducts experiments on six different fine-grained datasets and two different coarse-grained datasets. The results show that the proposed method achieves stable performance improvement, especially on the fine-grained datasets.
4. The ablation studies and related visualization are comprehensive and insightful.

### Weaknesses
 1. The evaluation datasets in the paper are relatively small, and the model parameters appear insufficient in 2024 . Using ResNet18/34 as the primary model limits the assessment of the framework’s scalability. It would be valuable to test the framework on a larger dataset, such as ImageNet, and with a more complex model like ResNet101, to assess its effectiveness in a more challenging setting.

2. The paper lacks comparisons with other knowledge distillation (KD) baselines, which would provide a clearer benchmark for evaluating the proposed method’s relative performance.

3. The framework could explore additional ways to leverage the knowledge in MLLMs. For instance, distilling logits from the last token output by the MLLM after processing the input image may capture different aspects of visual representation.

4. While Section 5.5 discusses training time and computational cost, the analysis might be incomplete. The time required for MLLMs to annotate the training dataset should also be considered to provide a more comprehensive assessment of computational demands.

### Questions
1. I noticed that even using random logits leads to performance improvements (Table 3(b)). Could you clarify the underlying reason for this result?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a novel approach to solving computer vision tasks, such as image classification and object detection, by enhancing conventional models' classification capabilities through knowledge distillation from Multimodal Large Language Models (MLLMs). The method involves expanding the dimensionality of the model's original logits, which improves classification accuracy. The paper provides numerous ablation experiments and conducts a thorough analysis of the results.

### Strengths
1. The paper combines traditional network models, such as ResNet, with MLLMs to enhance accuracy in classification and detection tasks. 

2. It uses multi-aspect questions to extract knowledge from MLLMs, leveraging this knowledge to support classification. 

3. The experiments are comprehensive.

### Weaknesses
The approach to utilizing knowledge distillation is a bit unclear—are you applying this strategy during training, or is it only used in inference? Additionally, there seems to be a lack of consideration for hallucination issues that may arise with GPT-4o during the generation of questions and responses.

The approach to utilizing knowledge distillation is somewhat unclear. When are the multi-aspect logits extracted from the MLLM, and how are they incorporated into the model's training or inference objective?

Given that GPT-4o generates the multi-aspect questions and that the MLLM has not seen images from each category, especially considering these categories are often long-tailed and fine-grained. Do you have any validation or filtering steps in place for the generated questions and responses, or have you considered comparing the generated questions to human-curated ones? Which types of generated questions contribute most to performance improvements.

When generating responses to the multi-aspect questions for each image, has the potential hallucination issue within the MLLM been considered? How accurately can the MLLM (InternVL) answer these generated questions, and to what extent does the hallucination issue in InternVL affect the accuracy of its responses?

For the object detection task, have you attempted to use other datasets, such as the larger-scale LVIS?

### Questions
1. The approach to utilizing knowledge distillation is somewhat unclear. When are the multi-aspect logits extracted from the MLLM, and how are they incorporated into the model's training or inference objective?

2. Given that GPT-4o generates the multi-aspect questions and that the MLLM has not seen images from each category, especially considering these categories are often long-tailed and fine-grained. Do you have any validation or filtering steps in place for the generated questions and responses, or have you considered comparing the generated questions to human-curated ones? Which types of generated questions contribute most to performance improvements.

3. When generating responses to the multi-aspect questions for each image, has the potential hallucination issue within the MLLM been considered? How accurately can the MLLM (InternVL) answer these generated questions, and to what extent does the hallucination issue in InternVL affect the accuracy of its responses?

4. For the object detection task, have you attempted to use other datasets, such as the larger-scale LVIS?

I may reconsider my score based on your response to these issues.

### Soundness
3

### Presentation
3

### Contribution
2
