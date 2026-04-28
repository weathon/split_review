# FocalLens: Instruction Tuning Enables Zero-Shot Conditional Image Representations

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5, 5

## Abstract
Visual feature extraction is fundamental to many vision tasks. Most existing methods extract visual features by encoding an image into a generic feature vector. However, an image naturally contains rich information, and there may be multiple perspectives to describe it. For each application, we might be interested in different aspects of an image and want to prioritize those features over others. For instance, in an image of a dog carrying a toy, if we are primarily interested in the dog, we would expect the extracted features to emphasize the dog over the toy. In this work, we introduce FocalLens, a conditional visual feature extraction method that produces different representations for the same image based on the context of interest, expressed flexibly through natural language. We leverage vision instruction tuning data and contrastively tune a pretrained vision encoder to take natural language instructions as additional inputs and produce conditional image representations. Extensive experiments validate that conditional image representation from FocalLens better pronounce the visual features of interest compared to generic features produced by standard vision encoders like CLIP. In addition, we show FocalLens further leads to performance improvements on a range of downstream tasks including image-image retrieval, image classification, and image-text retrieval, with an average gain of 5 and 10 points on the challenging SugarCrepe and MMVP-VLM benchmarks, respectively.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a method called FocalLens, that is designed to improve the visual representation capability of the vision encoders through instruction tuning. The motivation of this method to focus on the specific part of the images, according to the conditions or instructions given. The authors have presented two variants of this method, (i) FocalLens-MLLM : builds upon LLaVA, and (ii) FocalLens-CLIP : builds upon CLIP encoders. The extensive experiments on retrieval tasks have shown superior performance over baselines.

### Strengths
The paper focuses on the conditional visual representation of the images, through instruction tuning, which is a good motivation.

### Weaknesses
1. The motivation of this paper for retrieval tasks through text instructions, is not a new concept. On the other side, the proposed architectures are similar to LLaVA, with just an addition of contrastive loss, that brings very minor novelty.

2. It is not clear about which instructions are given during the inference of retrieval tasks? It would be better to provide those instructions. 

3. I don't see any difference between the textual conditioning of this work and composed image retrieval (CIR) task. As both are shown differently, what are the reasons behind that? A concrete explanation is preferable. 

      I think Pic2Word [1] and SEARLE [2], which are focused on CIR tasks, should be one of the proper baselines for the retrieval experiments.

4. LLaVA [3] should also be one of the baseline methods with the LLaVA feature variant of FocalLens.

5. The overview of the apporach is easy to understand, but the overall presentation is not good as the paper lacks the clear explanation of technical details and experimental details.

### Questions
See the weakness section. I would like to increase my rating, if the proper justification of my questions will be given.

### Soundness
3

### Presentation
2

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
The authors propose a conditional visual feature extraction method that focuses on the representation of specific aspects of the image described in the given text. Specifically, the authors leverage visual instruction tuning data to tune a pre-trained vision encoder in a contrastive manner, taking natural language instructions as additional inputs to produce conditional image representations. Experimental results on a wide range of downstream tasks demonstrate that the proposed method produces features of interest better than generic features produced by standard vision encoders like CLIP.

### Strengths
-	The proposed method is well-motivated. The idea of using text instructions as conditions to extract features of interest for certain downstream tasks is intuitive and interesting. 
-	The paper is generally well-written and easy to follow.
-	The experiments are extensive, covering a broad range of tasks including image-image retrieval, image classification, and image-text retrieval.

### Weaknesses
 - While most results seem promising, some of them are not. For example, in Table 2, FocalLens performs worse than InstructBLIP on GeneCIS (Attribute). In Table 3, FocalLens performs worse than CLIP on Flower and Aircraft. In Table 7, compared with OpenAI ViT-L-14, FocalLens performs the same on Orientation and significantly worse on Structure. These results make me concerned about the actual effectiveness of FocalLens on certain conditions. Could the authors provide a justification on this?
- The authors use the visual instruction tuning data in LLaVA to train FocalLens models. It would be better to show how the number of visual instruction tuning examples affect the final performance.

### Questions
I am concerned about the questions mentioned above. I am leaning towards borderline accept and hope the authors could address my concerns during the rebuttal.

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
The paper proposes the FocalLens which is a visual feature extraction method that generates different image representations based on the specified context of interest, guided by natural language. By turning a pre-trained vision encoder with vision instruction tuning data, FocalLens emphasizes features relevant to the context, and aims to enhance performance on tasks like image retrieval and classification.

### Strengths
The proposed method is validated on multiple downstream tasks for image representations and achieves consistent performance improvements.

### Weaknesses
1. The proposed model is unlikely to outperform existing models significantly. The authors mentioned in Lines 139-141 that the proposed model is different from other conditioned vision models (e.g., LLaVA [1], also cited in the paper) because the proposed model can be applied in "broad downstream use cases". However, in the training setting, they use similar training data and settings as LLaVA. This is thus no validation for "being able to do broader downstream tasks".

2. This paper misses the baseline that uses LLaVA features. From the reviewer's understanding, the proposed model looks like a submodule of LLaVA (by removing the language branch). That is, LLaVA is equal to the proposed method if including a text decoder. Currently, the advantage of this work compared with the LLaVA encoding features is unclear.

3. The motivation of this paper is not convincing to the reviewer. In the related works (and some parts of the introduction section), the justification of the difference between existing works and this submission is not clear. The reviewer's understanding is that general MLLM aims to learn general representation, and existing conditional visual representation works aim for task-specific conditioning features. While, this submission aims to learn general conditioning features which might be somewhere between general features and task-specific conditioning features. Then, the question is what is the criterion to distinguish these three features? It is quite confusing what is going to be learned given that related works of conditioning features have been obtained in many existing works. In other words, what is the benefits of learning such in-between conditioning features/representations? It seems general but also specific to some conditions which are not clarified in this paper, given the validate datasets are just common ones.

### Questions
1. What is the specific and concrete difference between the proposed method and the existing text-conditioning visual feature exaction method?
2. What kind of broader tasks can be only solved by this proposed method? The contribution (compared with other similar or related works) needs to be highlighted during the rebuttal.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces FocalLens which is able to produce different visual representations of the same image based on different contexts of interest. The authors leverage the instruction tuning data, which is usually in the triplet format of (image, instruction, output), to fine-tune MLLMs and CLIPs in a contrastive manner, resulting in FocalLens-MLLM and FocalLens-CLIP, respectively. Evaluations on various benchmarks demonstrate the effectiveness of the propose method.

### Strengths
1. Extracting visual features according to specific conditions, e.g., text instructions, is worth studying.
2. Overall, this paper is well-written and easy-to-follow.
3. FocalLens-CLIP appears to be effective.
4. The motivation is clear, and the training pipeline of FocalLens-CLIP is reasonable.

### Weaknesses
1. FocalLens-MLLM is somewhat weird. This paper aims to produce context-aware visual features. However, there appears to be a discrepancy in the design, as the visual features produced by FocalLens-MLLM do not seem to be modulated by contextual instructions. Notably, the architecture does not incorporate instructions as inputs to the visual encoder. Consequently, this suggests that the visual features extracted remain invariant across different instructions. Could you explain in more detail how the instruction information modulates the visual features in FocalLens-MLLM? Is there a mechanism that allows the visual encoder to produce different representations based on different instructions?
2. Equipping FocalLens-CLIP with standard MLLM training recipes seems to be an appropriate design. I am curious about the performance. Have you evaluated FocalLens-CLIP's performance on standard multimodal comprehension tasks compared to baseline models? Could you provide results or analysis demonstrating how the context-aware visual features contribute to improved multimodal understanding?

### Questions
1. Does the training of FocalLens-MLLM still have the next-token-prediction loss based on cross-entropy?

### Soundness
3

### Presentation
3

### Contribution
2
