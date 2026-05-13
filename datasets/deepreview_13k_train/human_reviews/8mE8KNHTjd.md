# UniQA: Unified Vision-Language Pre-training for Image Quality and Aesthetic Assessment

- Decision: Reject
- Scores: 8, 5, 5, 6, 6, 6, 5, 5

## Abstract
Image Quality Assessment (IQA) and Image Aesthetic Assessment (IAA) aim to simulate human subjective perception of image visual quality and aesthetic appeal. Existing methods typically address these tasks independently due to distinct learning objectives. However, they neglect the underlying interconnectedness of both tasks, which hinders the learning of task-agnostic shared representations for human subjective perception. 
  To confront this challenge, we propose \textbf{Uni}fied vision-language pre-training of \textbf{Q}uality and \textbf{A}esthetics (UniQA), to learn general perceptions of two tasks, thereby benefiting them simultaneously.
  Addressing the absence of text in the IQA datasets and the presence of textual noise in the IAA datasets, (1) we utilize multimodal large language models (MLLMs) to generate high-quality text descriptions; (2) the generated text for IAA serves as metadata to purify noisy IAA data. To effectively adapt the pre-trained UniQA to downstream tasks, we further propose a lightweight adapter that utilizes versatile cues to fully exploit the extensive knowledge of the pre-trained model. Extensive experiments demonstrate that our approach attains a new state-of-the-art performance on both IQA and IAA tasks, while concurrently showcasing exceptional zero-shot and few-label image assessment capabilities.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper proposes a unified evaluation model to handle both image quality assessment (IQA) and image aesthetic assessment (IAA) tasks simultaneously. Specifically, the proposed method first leverages the existing multimodal large language model (MLLM) to generate IQA (YIQA), IAA (YIAA) datasets with generated descriptions, and purify IAA dataset (Y+IAA) annotated by human’s comments. Then, the proposed method train the CLIP model based on YIQA, YIAA and Y+IAA. Finally, an multi-cue integration adapter is designed to allow the pre-trained CLIP to adapt to specific datasets.

### Strengths
1. This paper includes comprehensive datasets, encompassing nearly all existing IQA and IAA datasets, providing robust validation for the effectiveness of the proposed method.
2. The methodology of the algorithm is described in a clear and straightforward manner, with concise and easily understandable language.
3. The paper presents an extensive set of experiments and rich visualizations, thoroughly validating each module within the algorithm's design.

### Weaknesses
1. The paper’s motivation appears to lack practical significance or has not been convincingly demonstrated.
2. While the proposed approach is intricate, its actual innovation is minimal.
3. The related work section includes methods that are either outdated or lack representativeness in the current IQA and IAA research.
4. Beyond metric improvements, the proposed method lacks substantial inspirational value for future studies.
5. The paper is missing some essential experiments that could substantiate its motivations.



### Questions
1. Motivation Concerns: The motivation for jointly considering IQA and IAA tasks could be questioned. Is there a urgent or practical need to address IQA and IAA together? Do these tasks mutually benefit each other, or does their combination offer real-world value beyond mere metric improvements?
2. Combined Dataset Training: The authors claim that existing combined dataset training fails to learn mutually beneficial representations shared by both tasks. In fact, the authors construct three datasets (YIQA, YIAA and Y+IAA) to train a CLIP model, which resembles the challenge they raised. This raises questions about the rationality of their motivation and calls for concrete evidence to support it.
3. Noise in human- annotated IAA Datasets: The authors argue that textual noise in IAA datasets negatively impact prediction performance. It would be more convincing if they specified what constitutes " textual noise " and clarified the specific negative impacts. In addition, the claim that MLLM-generated description can purify " textual noise " is unconvincing, as only one MLLM model was used in description generation. The model’s biases and possible overuse of irrelevant words are not addressed, making this assumption lack strong justification.
4. Common feature representation: The authors suggest that the proposed method can extract common representations from IQA and IAA tasks. Visual evidence supporting this claim would strengthen their argument.
5. Informativeness Rank (IR): Using sentence length as the metric for Informativeness Rank might be biased. The number of irrelevant or potentially harmful words within a sentence should not be overlooked. 
6. Related Work: The IQA and IAA methods discussed in the related work section are relatively outdated. Adding more recent and representative algorithms would improve this section.
7. Experimental Comparisons and Visualization Limitations: Some newest comparison methods are required. Additionally, the visualization in Fig. 5 fails to demonstrate that the proposed method focuses more on noisy objects and backgrounds. The examples tend to provide “blurry image”, but the sample mostly depicts a blurred background with clear objects, which does not align with the stated objective.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper aims to leverage unified vision-language pre-training to address quality and aesthetic assessment problems concurrently, and proposes a method named UniQA. On the one hand, this paper constructs a high-quality image-text dataset about quality and aesthetics with the assistance of MLLMs. On the other hand, UniQA learns the shared representations of IQA and IAA tasks by pre-training on the constructed dataset.  Additionally, a Multi-Cue Integration Adapter is proposed in UniQA for downstream assessment tasks.

### Strengths
1. In this paper, a high-quality image-text dataset about image quality and aesthetics is constructed based on the assistance of MLLMs, which is valuable．
2．The organizational structure of the article is clear and the content is complete. The writing is clear and easy to follow.　
3. The motivation to "extract mutually beneficial and effective representations for both IQA and IAA tasks" in this paper is plausible.
4. This paper proposes an effective data purification strategy that refines the raw aesthetic caption dataset, providing valuable insights for data organization and cleaning in the IAA field.

### Weaknesses
1．The authors highlight that the motivation of this paper is to "extract mutually beneficial and effective representations for both IQA and IAA tasks." However, throughout the paper, neither the proposed dataset nor the proposed method fully explore the mutually beneficial representations for IQA and IAA tasks; instead, they only address the creation of effective representations for these tasks. Specifically, the method proposed in this paper learns a shared feature representation for IQA and IAA tasks, without proving how the representation is "mutually beneficial" which is somewhat disappointing. It is suggested to provide specific experiments or analyses that demonstrate how the learned representations benefit both IQA and IAA tasks mutually. 
2．The experiments in this paper are not sufficiently comprehensive. First, the compared methods are relatively outdated, lacking comparisons with more recent works in 2024, such as [1][2]. Additionally, the ablation study only focuses on the IQA task, without any ablation analysis for the IAA task, which makes the conclusions of the ablation study less convincing.
3．The novelty is limited. The pretraining process of UniQA merely applies a standard contrastive learning strategy, a commonly used approach in numerous previous works. Additionally, the Multi-Cue Integration Adapter directly adopts the inference approach of CLIP-IQA, while the visual feature adaptation module functions similarly to a LoRA operation for fine-tuning. This Adapter appears unrelated to the concept of Multi-Cue Integration.  It is not clear how the proposed approach improves upon or differs from standard contrastive learning and existing methods like CLIP-IQA. And  a more detailed explanation of how the Adapter relates to the concept of Multi-Cue Integration is suggested.
4．This paper dedicates extensive sections to describing the dataset construction process but lacks detailed information about the resulting dataset, such as sample size, text length distribution, or word cloud distribution. There is also an absence of detailed statistical analysis and comparison between the IQA and IAA datasets used for training, leaving the relationships and differences between them unexplored.
5. The paper contains minor errors that need careful review. For instance, in Line 365, "supplementary material" should be referred to as the "Appendix."

### Questions
1. In Eq. (5), simply summing AR and IR may not be the optimal approach. Assigning different weights to AR and IR and conducting relevant experiments to determine the best weight parameters could yield better results.
2. In Line 103, the statement "achieving SRCC values of 0.828 (vs. 0.764 on CLIVE) and 0.844 (vs. 0.812 on KonIQ)" is somewhat confusing, as it is unclear which method these results are being compared against.

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
This paper has two main contributions
1) This paper constructs a high-quality image-text dataset about image quality and aesthetics. 
2) This paper proposes UniQA to effectively learn a general perception of image assessment.

### Strengths
1) This paper is well-written. 
2) This paper achieves the SOTA performance on IQA and IAA tasks

### Weaknesses
The overall framework and concept are simple and lack novelty.
1) Directly utilizing MLLMs to generate text is now common practice.
2) The pre-training design is straightforward and typical of MLLMs.
3) This paper reports only the performance on IQA and IAA, offering a limited range of downstream tasks.

### Questions
Could you demonstrate the effectiveness of your design in generating high-quality text and apply UniQA to a broader range of downstream tasks ?

### Soundness
2

### Presentation
2

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
This paper designs a novel UniQA framework to perform IQA tasks on different types of visual content. Contains two key designs: (1) Utilize MLLM to generate high-quality text descriptions; (2) Use the text generated for IAA as metadata to purify noisy IAA data. Experiments show that this method achieves state-of-the-art performance on both IQA and IAA tasks, achieving SRCC/PLCC above 0.9.

### Strengths
The refine module proposed in this paper can transform messy data into a quality-related format, thereby ensuring that the model is highly consistent with the supervised experience of the human eye, and has the potential to be applied in future IQA and IAA tasks. This can achieve the migration of large-scale, general descriptive datasets to quality-related specialized datasets, which can promote progress in the field of IQA.

The method proposed in this paper can be used for both traditional visual content and emerging AIGC quality assessment. It can promote the further application of AIGC, especially the aesthetic aspects of AIGC.

The experimental dataset is relatively sufficient, and the comparison method is complete and advanced.

### Weaknesses
The core implementation of UniQA is to predict the probability of The image quality is {bad, poor, fair, good, perfect} and then fuse them. This is not a completely new paradigm. As far as I know, this first appeared in Q-Align. However, the author only reviewed this article without comparing them in experiments. Considering the similarities between the two, it is necessary for the author to conduct comparative experiments in Table 1 and emphasize the differences between the two.

It is a good point that the UniQA proposed by the author has a significant advantage in evaluating AIGC. However, the verification using AGIQA-1K/3K is slightly outdated. T2I generation models are developing very rapidly, and even the best 3K images (June 2023) are only of average quality compared to the current AIGC. Therefore, the author can verify the performance of UniQA on the AIGIQA-20K (April 2024) database to better prove its applicability to AIGC.

### Questions
I am curious whether the combination of IQA and IAA pipelines makes sense. In the ablation experiment, using only IQA does not seem to be too bad. Therefore, I am not sure whether it is necessary to use a dedicated IAA pipeline. I think the quality in IQA is not purely low-level quality, but also includes aesthetic elements, so removing IAA will not lead to a significant drop in performance. Note that this is not to question weakness, just kindly discuss with the author: Is IAA a subtask of IQA, or an equally important task?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a unified model for assessing both image quality and aesthetics, called UniQA. It uses multimodal large language models (MLLMs) to generate descriptive text for IQA and IAA datasets, which allows for a more detailed and refined training dataset. The model uses these captions for pre-training and employs a lightweight Multi-Cue Integration Adapter to adapt the model for downstream tasks. Experimental results show UniQA achieving state-of-the-art (SOTA) performance across multiple datasets.

### Strengths
1. UniQA effectively combines IQA and IAA tasks, extracting shared representations, leading to efficient and comprehensive visual assessment capabilities.

2. Using MLLMs to generate high-quality text descriptions enriches the dataset.

3. The lightweight Multi-Cue Integration Adapter allows UniQA to adapt efficiently to various downstream IQA and IAA tasks with minimal parameter adjustments.

### Weaknesses
1. Although this paper effectively utilizes MLLM-generated text for dataset construction, the generated descriptions tend to have similar structures and expressions, resulting in limited text diversity. The model's performance heavily depends on the quality of MLLM-generated text, which may introduce noise or bias, especially as MLLMs may produce overly positive or vague evaluations when generating image descriptions.

2. While this method aligns IQA and IAA datasets by unifying them on a common MOS scale to reduce MOS biases between datasets, such direct alignment may overlook the inherent rating standards and subtle differences across datasets. For instance, different datasets may prioritize specific visual features (e.g., sharpness, color balance) in quality assessment, while aesthetic assessment might focus more on composition and emotional impact. In such cases, a unified MOS scale may reduce the model's sensitivity to certain features, potentially compromising its performance precision in specific tasks.

3. The effectiveness of the dataset constructed in this paper largely depends on MLLM-generated text descriptions and data purification strategies. However, it lacks a systematic evaluation of dataset quality. While the data purification process uses Aesthetics-relevance Rank (AR) and Informativeness Rank (IR) to filter out irrelevant content, these subjective criteria may filter out some valuable information, which could affect the dataset's diversity and comprehensiveness.

### Questions
See Weakness

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 6

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a unified vision-language pre-training of quality and aesthetics (UniQA) to tackle both the image quality assessment (IQA) and the image aesthetic assessment (IAA) tasks.
The proposed method first generates quality- and aesthetics-related descriptions by using multimodal large language model (MLLMs) and use them to refine authentic noisy data.
Then the UniQA model is pre-trained with the purified data and finally a lightweight adapter is adapted to each IQA and IAA benchmark.
In the pre-training, two tasks are bridged and the UniQA can learn rich correlated information to enhance the both tasks.

### Strengths
- Effective data generation and refinement using MLLMs and efficient adaptation to each benchmark. 
- Tackles IQA and IAA at the same time.
- Comparisons with a number of previous methods.

### Weaknesses
 - In obtaining IR score, the informativeness of text is measured by the sentence length but it seems sub-optimal and less robust.
- It is not verified that the quality-level keywords, "bad, poor, fair, good, perfect", are reasonable without any intuitions or experiments. In addition, they are linked to score values (fig 3 b) "0.2, 0.4, 0.6, 0.8, 1.0", respectively, but it is an arbitrary matching. Likewise, the reason using a prompt ensemble with keywords "extremely blurry, blurry, fair, sharp, extremely sharp" have not been verified.
- The results of the prompt ensemble, which gives a major improvement, are not reported in table 1-3.
- It is unclear how can the UniQA handle real-world images.

### Questions
- How the MOS-based text guidance G is obtained? Have the authors try several other attempts?
- What exactly does multi-cue mean in the multi-cue integration adapter.
- How much will performance improve if replace the backbone CLIP-B/16 to other MLLMs such as LLaVA or more latest models? If it improves then why not use it?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 7

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
To learn mutually beneficial representations shared by both tasks explicitly, this paper proposes Unified vision-language pre-training of Quality and Aesthetics (UniQA), which can extract useful and common representations from two tasks. Specifically, an image-text dataset about image quality and aesthetics is constructed by MLLMs, which is used to train the UniQA based on contrastive learning. Then a lightweight adapter is used to fine-tune the specific dataset of two tasks.

### Strengths
1.This paper includes extensive visualization experiments that provide a clear and intuitive demonstration of the experimental results of the proposed method.

2.Addressing the current scarcity of high-quality text-image datasets in IAA and the low quality of text descriptions, this study uses MLLM for data cleaning, constructing a higher-quality text-image IAA dataset to support future training.

### Weaknesses
1.Although the premise of this paper is intriguing (aiming to address both IQA and IAA problems simultaneously), similar approaches have already been proposed and with better outcomes. For example, [1] tackles IQA and IAA as well as VQA, surpassing this paper in scope and effectiveness. Additionally, this paper lacks a comparison with [1], making its experimental results less convincing.

2.The proposed method lacks substantial innovation. Overall, UniQA uses CLIP and a LoRA-like fine-tuning approach, with minimal improvements in training paradigms or network architecture.

3.Due to limited innovation in the training method, this work resembles more of a dataset paper, as its main contribution is the MLLM-based text-image IQA and IAA dataset. While the authors dedicate considerable detail to the dataset construction process, they fail to provide specifics on dataset content (e.g., image sources, dataset size, data distribution).

4.The writing structure is somewhat disorganized. For instance, in the introduction, the authors first introduce their UniQA method, then critique existing work, and return to explaining their method, which disrupts the flow. In the related work section, each subsection is extremely brief; more comprehensive discussion of recent work and analysis of similarities and distinctions between this method and others are needed.

5.The experiments are insufficiently comprehensive. The comparison covers only a single 2024 method, which is far from adequate. As far as I know, several new methods were introduced in 2024, such as [1], [2], [3], [4], [5], etc. Additionally, it would be beneficial if Table 1 reported variance for the experimental results.

### Questions
1.The meaning of "versatile cues" in Line 99 is unclear. Where in the Methods section is this concept demonstrated? Additionally, what exactly does "Multi-Cue" refer to in Line 111?

2.What is the motivation for using sentence length as a score to represent information quantity in Lines 254–255?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 8

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper propose a Unified vision-language pre-training for Image Quality Assessment (IQA) and Image Aesthetic Assessment (IAA) tasks, which breaks down the barrier between quality-, and aesthetic-related features.  The authors construct a high-quality image-text dataset about image quality and aesthetics. Using their collected data, they develop UniQA, which learns a general perception of image assessment. Experiments show that the proposed method achieves SOTA performance across multiple IQA and IAA datasets.

### Strengths
1. The idea of developing a foundational model with robust visual assessment perceptions consistent with human to benefit both IQA and IAA tasks is novel.
2. The idea of using text descriptions as a bridge to integrate the two tasks is innovative
3. The paper provides a thorough evaluation of existing IQA and IAA models on respective IQA and IAA datasets.

### Weaknesses
1. The coarse image retrieval results in Fig. 4 may not sufficient. Adding the corresponding MOSs can increase its readability.
2. The assessment appear to be thorough and sound. However, the paper does not have any p-values or confidence intervals to support their comparisons of methods (especially for Tab. 1, 5, and 6).
3. The performance gain compared to other MOS regression-based models is limited, but introduce more efforts in collecting textual description, which poses challenge for the subjective study. I think this problem should be discussed further.
4. Line41-42: “high-quality images tend to possess a higher aesthetic appeal compared to their low-quality counterparts.” This conclusion may not true since an aesthetically pleasing old photo may have some noise in it. Besides, some AI-generated images are over smooth which may exhibits high technical quality but with low aesthetic.
5. Is there any word limit in generating captions for images? Since the accuracy of description largely affect the performance. 
6. What is the version of Qwen in Tab. 6 (Ablation on different MLLMs). Please include more information of parameter quantity. In addition, currently, the evaluated MLLMs are all open-source models, the performance difference between them is not significant, it is necessary to evaluate on proprietary MLLMs, such as GPT-4o, Gemini 1.5 Pro, and Qwen-VL-MAX, which owns better visual perception abilities. Experiments on Whether better description can enhance the performance is valuable.
7. When two images (for example, the right two good images of CLIVE in Fig. 4) have similar technical quality and semantic, the generated caption could be very close. In this case, the MOS-based text guidance may not reflect their true quality or aesthetics differences. 
8. In line210-212: The author divide images into 5 levels based on MOS to obtain G, If an image’s MOS ranks in the top 20% of the score range, its level is assigned to perfect. The question is whether there is some loss in performance by quantifying the otherwise continuous scale scores back to a 5-level evaluation criterion, since the MOS distribution in the IQA dataset is almost inhomogeneous, sometimes showing left-skewed or right-skewed. In other words, does the granularity of the evaluation scale affect the model performance?
9. Another question is that the MOS of an image is collected from human study. The quality- and aesthetics-related captioning is completed by MLLMs. Whether the MLLMs can perceive as human remains an problem especially in some aesthetics judgments.
10. Using the length of a sentence as informativeness score may introduce large bias since it may contain some useless words. Why don’t you use Information relevance metrics to measure the informativeness of text?
11. It seems that the proposed method performs well on mainstream IQA datasets. The author further evaluate the generalization capability on AGIQA-3K. Since the naturalness problem [1] (consists of both technical quality and rationality (images which own similar technical quality with NSIs but could contain irrational contents) distortions) appears more easier in AI-generated images than pure quality problem. Is it possible to test on the AGIN dataset [1] ? This may demonstrate a significant benefit of this method in the era of generative AI.

### Questions
1. Line41-42: “high-quality images tend to possess a higher aesthetic appeal compared to their low-quality counterparts.” This conclusion may not true since an aesthetically pleasing old photo may have some noise in it. Besides, some AI-generated images are over smooth which may exhibits high technical quality but with low aesthetic.
2. Is there any word limit in generating captions for images? Since the accuracy of description largely affect the performance. 
3. What is the version of Qwen in Tab. 6 (Ablation on different MLLMs). Please include more information of parameter quantity. In addition, currently, the evaluated MLLMs are all open-source models, the performance difference between them is not significant, it is necessary to evaluate on proprietary MLLMs, such as GPT-4o, Gemini 1.5 Pro, and Qwen-VL-MAX, which owns better visual perception abilities. Experiments on Whether better description can enhance the performance is valuable.
4. When two images (for example, the right two good images of CLIVE in Fig. 4) have similar technical quality and semantic, the generated caption could be very close. In this case, the MOS-based text guidance may not reflect their true quality or aesthetics differences. 
5. In line210-212: The author divide images into 5 levels based on MOS to obtain G, If an image’s MOS ranks in the top 20% of the score range, its level is assigned to perfect. The question is whether there is some loss in performance by quantifying the otherwise continuous scale scores back to a 5-level evaluation criterion, since the MOS distribution in the IQA dataset is almost inhomogeneous, sometimes showing left-skewed or right-skewed. In other words, does the granularity of the evaluation scale affect the model performance?
6. Another question is that the MOS of an image is collected from human study. The quality- and aesthetics-related captioning is completed by MLLMs. Whether the MLLMs can perceive as human remains an problem especially in some aesthetics judgments.
7. Using the length of a sentence as informativeness score may introduce large bias since it may contain some useless words. Why don’t you use Information relevance metrics to measure the informativeness of text?
8. It seems that the proposed method performs well on mainstream IQA datasets. The author further evaluate the generalization capability on AGIQA-3K. Since the naturalness problem [1] (consists of both technical quality and rationality (images which own similar technical quality with NSIs but could contain irrational contents) distortions) appears more easier in AI-generated images than pure quality problem. Is it possible to test on the AGIN dataset [1]? This may demonstrate a significant benefit of this method in the era of generative AI.

[1] Chen, Z., Sun, W., Wu, H., Zhang, Z., Jia, J., Ji, Z., ... & Zhang, W. (2023). Exploring the naturalness of ai-generated images. *arXiv preprint arXiv:2312.05476*.

### Soundness
3

### Presentation
3

### Contribution
3
