# Enhancing Video Understanding with Vision and Language Collaboration

- Decision: Reject
- Scores: 5, 5, 6, 3

## Abstract
Leveraging video pre-trained models has led to significant advancements in video understanding tasks. However, due to the inherent bias towards temporal learning in video pre-training, these models fail to capture comprehensive spatial cues. Additionally, the widely-used supervised adaption methods lack fine-grained semantic guidance as single action labels cannot precisely depict the intra-class diversity. To address these challenges, we incorporate the general capabilities of large Vision Language Models (VLMs) and propose a cross-modal collaborative knowledge transfer method to enhance video understanding. First, we propose an attentive spatial knowledge transfer method that distills spatial knowledge from the VLM's image encoder, enabling the precise capture of spatial information. Next, we design a contrastive textual knowledge transfer approach that achieves detailed video representations through fine-grained text-video alignment. Owing to the cross-modal knowledge transfer, the video representations are capable of attending to informative spatial regions and aligning with fine-grained texts that carry rich semantics. Extensive experiments demonstrate that our method achieves state-of-the-art performance across various datasets, validating its effectiveness.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper aims to improve the spatial understanding of the existing video-language model for the classification task. This is implemented with three different optimization losses, including the classification task (classify the video into predefined classes), contrastive loss (aligning the video with the text descriptions associated with the video) and spatial knowledge transfer task. The spatial knowledge transfer task utilizes the frozen large vision language model to guide the learning of video encoder, by aligning the video token with the image token. Extensive experiments and ablation are conducted on different video datasets and backbones to demonstrate the effectiveness of the proposed training strategies.

### Strengths
1.	Figure 2 is well designed and fully captured the overall training pipeline. 
2.	The paper is well written and simple to follow.
3.	The motivation of this work is strong and interesting.

### Weaknesses
1.	The main contribution of this work is unclear. The classification loss and contrastive loss are common in video pretraining and video classification. Moreover, the alignment with L1 loss between the image token and the video token is also not considered novel. 
2.	The most interesting section in this work is the cross attention section in Eq 6-8, which leverages the segmentation model to guide the alignment. However, while the author shows that the result is not performing well, the explanation in L258-260 is not sound and solid. It will be interesting if the author can provide more study and in-depth discussion.
3.	L297-L299 is unclear. What does it mean by “dissimilar description would be less linked to the action”?
4.	The conclusion from the negative test sampling ablation is unclear. Figure 3 shows a reflection point where the performance of the model has a minimum. Is there any reason why this is happening? What is the variance of each data point in Figure 3?

### Questions
While the motivation of this work is strong and interesting, not much novelty is observed in the study. The gain of this work is also minor compared to the previous work and the variance is not reported. Furthermore, some of the ablation study (like the number of negative text) seems to be very sensitive to the variance. It is unclear whether the gain in Table 1 and the ablation in Table 3 are due to the variance.

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
This work addresses the limitations of current video pre-trained models by integrating large VLMs into a cross-modal collaborative knowledge transfer framework. This method includes an attentive spatial knowledge transfer method that enhances spatial understanding and a contrastive textual knowledge transfer method for improved video-text alignment.

### Strengths
+ The writing is very good, relatively easy to understand, and easy to follow as well.
+ Using VLM to enhance video understanding is a very meaningful issue, and the results of this paper are good.

### Weaknesses
 - It is insufficient to prove the core motivation using only one figure (Fig. 1 c).
- the article lacks an analysis of the consumption of training costs.

- In lines 42-44, the author points out the "emphasis on capturing temporal information" and illustrates how this is a common phenomenon through the heatmap in Fig. 1(c). How does this demonstrate that the method proposed in this paper can address this issue, and what is the specific principle behind the solution?
- The description of the experimental results is quite imprecise. The performance of existing methods for Top-1 has exceeded 88.5% [1] and reached 89.7% two years ago [2], while the proposed method only achieves 86.9%. Therefore, it cannot be claimed that this method has achieved SOTA. 
- In Line 267, how can we ensure that the descriptions generated by the decompose-expand prompting are accurate? What would be the consequences if there are errors?
- Additionally, please include the Top-5 results in the experimental outcomes.

### Questions
- In lines 42-44, the author points out the "emphasis on capturing temporal information" and illustrates how this is a common phenomenon through the heatmap in Fig. 1(c). How does this demonstrate that the method proposed in this paper can address this issue, and what is the specific principle behind the solution?
- The description of the experimental results is quite imprecise. The performance of existing methods for Top-1 has exceeded 88.5% [1] and reached 89.7% two years ago [2], while the proposed method only achieves 86.9%. Therefore, it cannot be claimed that this method has achieved SOTA. 
- In Line 267, how can we ensure that the descriptions generated by the decompose-expand prompting are accurate? What would be the consequences if there are errors?
- Additionally, please include the Top-5 results in the experimental outcomes.


[1] Rethinking Image-to-Video Adaptation: An Object-centric Perspective
[2] Disentangling Spatial and Temporal Learning for Efficient Image-to-Video Transfer Learning

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes to leverage Vision Language Models (VLM) for cross-modal collaborative knowledge transfer to improve the spatial and semantic understanding for video data. The proposed approach aim to reduce the temporal gap between pre-training dataset and downstream tasks.

### Strengths
+ This work proposes a cross-modal collaborative knowledge transfer to adapt video pre-trained model for downstream tasks. Specifically, spatial knowledge is distill from VLM's image encoder via attentive spatial knowledge transfer. Then, textual knowledge transfer improve video representation via fine-grained text-video alignment.
+ A gating mechanism is proposed to guide the distillation process to focus more on the action relation region and less on broader content.
+ To improve the text-video alignment, a decompose-expand prompting method is proposed to improve the fine-grained and diverse description. This provide more training cue than a single description or class name. Then, a contrastive textual knowledge transfer learn the semantic knowledge.
+ The proposed method achieve consistent improvement over multiple baselines and datasets.

### Weaknesses
I don't see obvious weaknesses in this work. Please refer to the Questions Section for some clarification.

- On the ablation of negative text sampling, can the authors provide higher number of k (why is 1200 the current limit). In addition, It is no meaningful to stated that sampling 200 negative text yield the third-best Top-1 accuracy. Please provide a better explanation of the initial accuracy drop when k increase from 200 to 600, and subsequently improve again. How does the authors know the diminish was due to easy negatives? Is there a way to measure if easy negative was sampled in early stage?
- On the evaluation of gate mechanism, the improve with gate mechanism is relatively low (+0.24%). It would be to provide analysis on the class that is accurately classified with gate mechanism, and analyse if the corresponding attention map (with and without gate mechanism) match the hypothesis.
- What is the number of description generated for each category. Has the authors analyse the score of the positive text and observed cases where the scores are generally too low for some cases.

### Questions
- On the ablation of negative text sampling, can the authors provide higher number of k (why is 1200 the current limit). In addition, It is no meaningful to stated that sampling 200 negative text yield the third-best Top-1 accuracy. Please provide a better explanation of the initial accuracy drop when k increase from 200 to 600, and subsequently improve again. How does the authors know the diminish was due to easy negatives? Is there a way to measure if easy negative was sampled in early stage?
- On the evaluation of gate mechanism, the improve with gate mechanism is relatively low (+0.24%). It would be to provide analysis on the class that is accurately classified with gate mechanism, and analyse if the corresponding attention map (with and without gate mechanism) match the hypothesis.
- What is the number of description generated for each category. Has the authors analyse the score of the positive text and observed cases where the scores are generally too low for some cases.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a cross-modal collaborative knowledge transfer method for video action recognition. The framework consists of three key components: video adaptation, attentive spatial knowledge transfer and contrastive textual knowledge transfer. These three components correspond to three loss functions. Experiments on three datasets achieve state-of-the-art results.

### Strengths
+ Introducing VLMs and transfer learning for video understanding is reasonable.

+ The experimental results show slight improvements over previous methods.

### Weaknesses
 - The paper conducts experiments on video action recognition, but the title and abstract do not explicitly mention this task. Video understanding is a relatively broad concept.

- The three technical contributions result in only marginal improvements, especially as shown in Table 3. It is unclear which loss function serves as the main loss.

-  Why does the learning rate of the optimizer reported in the implementation details section differ from that in the appendix?

-  Why were experiments not conducted on the mainstream video dataset Something-Something V2 (SSV2) for action recognition?

-  How are the weight coefficients for the loss functions obtained?

-  Line 72 should be written as (e.g., CLIP). There are many similar issues throughout the manuscript.

-  Many equations are missing symbols, such as Equations (6) and (7). Additionally, the bold and italic formatting in the equations is inconsistent.

1. Line 238 is missing punctuation.

2. Line 313, 'Eq. equation 2' is so poor.

3. The capitalization of the first letters in the paper title is inconsistent.

### Questions
-  Why does the learning rate of the optimizer reported in the implementation details section differ from that in the appendix?

-  Why were experiments not conducted on the mainstream video dataset Something-Something V2 (SSV2) for action recognition?

-  How are the weight coefficients for the loss functions obtained?

-  Line 72 should be written as (e.g., CLIP). There are many similar issues throughout the manuscript.

-  Many equations are missing symbols, such as Equations (6) and (7). Additionally, the bold and italic formatting in the equations is inconsistent.

1. Line 238 is missing punctuation.

2. Line 313, 'Eq. equation 2' is so poor.

3. The capitalization of the first letters in the paper title is inconsistent.

### Soundness
2

### Presentation
2

### Contribution
2
