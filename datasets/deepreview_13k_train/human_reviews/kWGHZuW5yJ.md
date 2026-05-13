# Enhancing Descriptive Image Quality Assessment with a Large-scale Multi-modal Dataset

- Decision: Reject
- Scores: 3, 6, 8, 6

## Abstract
With the rapid advancement of Vision Language Models (VLMs), VLM-based Image Quality Assessment (IQA) seeks to describe image quality linguistically to align with human expression and capture the multifaceted nature of IQA tasks. However, current methods are still far from practical usage. First, prior works focus narrowly on specific sub-tasks or settings, which do not align with diverse real-world applications. Second, their performance is sub-optimal due to limitations in dataset coverage, scale, and quality. To overcome these challenges, we introduce Enhanced Descriptive image Quality Assessment (EDQA). Our method includes a multi-functional IQA task paradigm that encompasses both assessment and comparison tasks, brief and detailed responses, full-reference and non-reference scenarios. We introduce a ground-truth-informed dataset construction approach to enhance data quality, and scale up the dataset to 495K under the brief-detail joint framework. Consequently, we construct a comprehensive, large-scale, and high-quality dataset, named EDQA-495K. We also retain image resolution during training to better handle resolution-related quality issues, and estimate a confidence score that is helpful to filter out low-quality responses. Experimental results demonstrate that EDQA significantly outperforms traditional score-based methods, prior VLM-based IQA models, and proprietary GPT-4V in distortion identification, instant rating, and reasoning tasks. Our advantages are further confirmed by real-world applications including assessing the web-downloaded images and ranking model-processed images. Datasets and codes will be released publicly.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
In this paper, a large-scale EDQA-495K dataset is proposed to fine-tune VLMs as multi-functional image quality assessors that can handle both quality assessment and comparison tasks. In specific, they use a ground-truth-informed approach and retain image resolution during training to construct the dataset. Experimental results demonstrate the superiority of DepictQA-Wild over traditional score-based methods, prior VLM-based IQA models, and GPT-4V across various tasks and settings.

### Strengths
The introduction of the DQ-495K dataset represents a significant contribution by providing a large-scale, high-quality dataset for Image Quality Assessment (IQA). The paper discusses various IQA tasks within both full-reference and no-reference frameworks, including assessments of single images and comparisons between paired images. Additionally, the incorporation of confidence estimation for responses is an interesting enhancement that could potentially improve the reliability of the assessments.

### Weaknesses
Although this paper contributes a comprehensive dataset and a multi-functional model for descriptive image quality assessment, the major weakness is the limited novelty and contribution, with some consideration that it is somewhat a data extension of the existing dataset and pipeline. Specifically, the pair-wise quality assessment and reasoning issue has been well addressed in the previous work Co-Instruct, while the performance gain of the proposed model basically comes from the augmented instruction data, which is somehow not a considerable contribution.  Besides, CoInstruct can also handle the quality comparison between multiple images, which is a harder task compared to image pairs, while the proposed model can only handle the latter one. Therefore, while the formulation of the augmented dataset is potentially useful, neither new perspectives nor new techniques are raised in this paper that can warrant a high score compared to previous work.

### Questions
See my comments above.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The authors propose a method called Enhanced Descriptive Image Quality Assessment (EDQA), which aims to leverage a large-scale multi-modal dataset (EDQA-495K) for improved IQA. The methodology includes both single-image assessments and paired-image comparisons, supported by an extensive distortion library. The paper claims significant performance improvements over existing models.

### Strengths
Strengths

1. The use of VLMs for IQA is new and aligns with current trends in AI research.
2. The authors propose a comprehensive and large-scale dataset, EDQA-495K, which could be a valuable resource for the research community.
3. The paper presents a clear and well-organized structure.

### Weaknesses
1. More detailed information is needed regarding the testing of the OOD settings presented in Table 3. Additionally, some non-reference IQA models, such as LIQE, are capable of identifying distortion types as well. It is recommended that these methods be included in the comparison.

2. Table 4 should incorporate IQA datasets that feature realistic distortions, such as KonIQ-10k and SPAQ. Including these datasets will allow for a more robust evaluation of the model's generalization capabilities.

3. The provided examples indicate that the model consistently generates template-like responses. It is important to investigate whether the model can effectively address open-ended questions. If so, results from the Q-Bench benchmark, which includes questions for both single and paired image inputs, should be provided.

4.  The methodology for computing quality score regression results in the full-reference setting (Table A3) is not clearly defined. Please elaborate on this aspect.

5.  Are there any specific fine-tuning procedures employed to obtain the results presented in Table A4?

6. Given that the model supports a maximum of two images as input, this limitation may lead to cumbersome and time-consuming comparisons when analyzing model-processed images across a larger variety of contents and algorithms. Suggestions for addressing this issue would be appreciated.

7. The results of Q-Instruct and Co-Instruct should also be included in Table 6. 

8. Are there any inherent limitations associated with this model? A detailed discussion on this topic would enhance understanding.

### Questions
See weaknesses.

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
5

### Summary
This paper proposes an Enhanced Descriptive image Quality Assessment method based on the VLM, and constructs a large-scale multimodal dataset. Compared with the existing VLMs-based IQA algorithms and the traditional score-based IQA algorithms, the authors adopt a general method to achieve multi-functional quality assessment, which can obtain brief and detailed responses. The authors conducted sufficient comparative experiments and ablation experiments to illustrate the superiority of the proposed method. From the experimental results, the proposed method is capable of coping with a variety of IQA tasks and can generate reasonable quality descriptions. This work is innovative and inspiring and the paper is well organized.

### Strengths
The authors have achieved multi-functional quality assessment through a general method, including quantitative indicators and qualitative language descriptions. The proposed method can adapt to a variety of practical application scenarios. The authors have achieved the purpose of multifunctional quality assessment based on VLM by reasonably designing data tags and prompts. The proposed multi-functional IQA task paradigm can provide support for subsequent work. The proposed model has achieved good performance on a variety of evaluation tasks, which shows its effectiveness.

### Weaknesses
As shown in the experimental results，the proposed method shows good multi-functional IQA performance. However, the model size of the proposed model is much larger than that of the traditional IQA models, and the model training requires more computing resources. In particular, for the classic quantitative quality assessment task, the cross-modal training adopted by the proposed model does not seem to achieve significant improvement compared with the SOTA single-modal IQA model.

### Questions
The reviewers want to know the training resource consumption of the proposed model, as well as the inference efficiency. In addition, whether cross-modal and multi-functional IQA tasks are beneficial to classic instant rating IQA task.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
In this paper, the authors propose Enhanced Descriptive image Quality Assessment (EDQA), a multi-functional IQA paradigm that addresses limitations in current VLM-based IQA methods. EDQA supports diverse tasks, including both full-reference and non-reference IQA scenarios and incorporates EDQA-495K—a large, high-quality dataset informed by ground-truth data. With image resolution retained, EDQA can handle resolution-dependent quality issues effectively, and it offers confidence scores to filter low-quality outputs.

### Strengths
1. The proposed model supports both full-reference and non-reference IQA tasks.
2. A large-scale dataset with 495k images and annotations is constructed, which will benefit VLM-based IQA model training.
3. Key tokens are analyzed for confidence score estimation, indicating the model’s uncertainty in its responses.

### Weaknesses
1. Only synthetic distortion types are included in the dataset construction. Although the authors test performance on the SPAQ dataset, inferior results compared to existing VLM models (e.g., Q-Align) raise concerns about the model’s functionality. Additional testing on authentic distortions is recommended to verify performance. Specifically, the lack of diverse real-world distortions, such as those arising from camera lens imperfections, varying lighting conditions, and sensor noise, limits the applicability of the model to practical scenarios. The model's ability to generalize beyond the synthetic distortions it was trained on remains questionable.
2. The paper lacks an investigation of comparison order effects. In full-reference IQA, the order of images (e.g., reference first, then distorted, or vice versa) significantly impacts model performance, and it’s crucial to verify model robustness in this scenario. The authors could consider using a small set of existing datasets or testing on the datasets released in [2AFC Prompting of Large Multimodal Models for Image Quality Assessment, TCSVT 2024] to strengthen performance validation. The absence of such analysis makes it difficult to assess the reliability of the model in practical applications where the order of input images may vary.
3. While the authors state that image resolution is retained, the appendix reveals that images larger than 672 pixels are resized bilinearly, potentially diminishing the claimed resolution advantage. It is recommended that the authors refine this claim for accuracy. This discrepancy between the main text and the appendix creates confusion about the actual resolution handling capabilities of the model. The bilinear resizing could introduce artifacts and impact the model's ability to accurately assess quality based on fine details.
4. Distortion severity in the constructed dataset appears limited. In real scenarios, distortion can be more severe (e.g., extreme low-light conditions), raising concerns about the model's generalization capability to such challenging, real-world conditions. It would be beneficial for the authors to test the model in real-world scenarios, including severe compression, low-light conditions, and adverse weather such as fog and rain, to better evaluate its practical applicability. The limited range of distortion severities in the training data may lead to poor performance when the model encounters more extreme degradations.

### Questions
1. An investigation into comparison order effects should be conducted to verify the model’s robustness.
2. The model’s generalization capacity on distorted images in the wild should be examined.

### Soundness
2

### Presentation
3

### Contribution
2
