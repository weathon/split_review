# Mind's Eye: Image Recognition by EEG via Multimodal Similarity-Keeping Contrastive Learning

- Decision: Reject
- Scores: 5, 3, 5, 8, 3

## Abstract
Decoding images from non-invasive electroencephalographic (EEG) signals has been a grand challenge in understanding how the human brain process visual information in real-world scenarios. To cope with the issues of signal-to-noise ratio and nonstationarity, this paper introduces a MUltimodal Similarity-keeping contrastivE learning (MUSE) framework for zero-shot EEG-based image classification. We develop a series of multivariate time-series encoders tailored for EEG signals and assess the efficacy of regularized contrastive EEG-Image pretraining using an extensive visual EEG dataset. Our method achieves state-of-the-art performance, with a top-1 accuracy of $19.3\%$ and a top-5 accuracy of $48.8\%$ in 200-way zero-shot image classification. Furthermore, we visualize neural patterns via model interpretation, shedding light on the visual processing dynamics in the human brain.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
- The paper presents the MUltimodal Similarity-keeping contrastive learning (MUSE) framework for zero-shot EEG-based image classification. The work proposes a new way of doing self-supervised learning in this context, as well as regularisation of contrastive learning.
- The study explores one dataset, THING'S EEG version 1.

### Strengths
- The results seem to show an increase in the results presented by Song, Y. et al (2023) at the same conference.

### Weaknesses
IMHO, The paper needs to be better summarized; the text, in general, is more verbose than necessary, and I think the overall presentation needs to be improved.

**Major:**
- The EEG-to-IMG field is heavily criticized in the literature mainly because of its many co-founders, with some authors saying that 'it does not seem possible to decode object class from EEG data recorded from subjects viewing image stimuli with randomized stimulus,' Kilgallen, J. A. et al. A. et al. (2024), Bharadwaj, H. M. (2023), Li, R. et al. (2020), Ahmed, H. et al. (2021), and there is no discussion in your paper on these points, which raises a flag in my mind about the generalisability of your work. How do you ensure that these co-founders don't also affect your work as well?
- In Figure 4, ST Conv looks equal to ST Conv from Song. et al. (2023) in Nice, can you clarify the difference for me?
- The use of GradCam in this context does not seem very appropriate since other models of interpretability are more refined for the task of eeg decoding; the temporal dynamics are best captured by methods like LIFT, see in Sujatha Ravindran, A., & Contreras-Vidal, J. (2023) and Cui, J. et al. (2023).

**Minor:**

- The figures and subfigures are super small (half of Fig 1, Fig 2, Fig 3, Fig 4, Fig 5, Fig 6, Fig 7, Fig 8, Fig 9, Fig 10, Fig 11, Fig 12, Fig 13 and Fig 14) that it's impossible to read them in the printed version, mainly because of the size of the fonts. This considerably restricted my revision process. I kindly request that this be corrected; please adjust the size of the fonts and the resolution with vectorization of the figures to make them larger and easier to read.
- The tables were also difficult to read.
- I couldn't understand figures 5 and 6 in the plots. Can you help me with what I should see in these plots?
- MUSE in EEG is usually associated with the company MUSE (https://choosemuse.com/)
- The training time, lines 338-339, without the machine specifications, is not very useful.

### Questions
- On lines 278-281: Can you clarify what inspiration you had based on the article by Bao et al. 2020 and She et al. (2024)?
- I am not sure I understood the NervFormer method details; I found the notation a bit confusing (Nerv, SK, GA); can you clarify this for me?
- Why didn't you compare it to the other aspects of NICE (Features Distribution, EEG Encoder Comparison, Semantic Similarity, Parameter Sensitivity In The Beta) ?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper presents a multimodal contrastive learning approach that aligns EEG and image data. 
A similarity-keeping term is added to the contrastive loss to force the preservation of inter-sample relationships.
Various EEG encoders are evaluated. 
Experiments are performed on the ThingsEEG dataset.
The experimental results show that the presented model can successfully perform zero-shot classification.

### Strengths
**Clarity** The content of the paper is written clearly. The flow of the text is easy to understand and follow.

### Weaknesses
 **Originality** The originality of the work is quite limited. Previous work has explored a similar approach for image recognition from EEG [1, 2] and fMRI [3]. Especially, [2] is very similar, which has already investigated the recognition of images from EEG on the same ThingsEEG dataset using the same contrastive loss.

**Significance** The paper introduces the similarity-keeping contrastive loss that achieves state-of-the-art results, as it is claimed in the paper. However, as shown in Table 1, the results are nearly the same whether the similarity-keeping contrastive loss is used or not. Here, a more detailed analysis of the impact of the similarity-keeping contrastive loss would be beneficial. Specifically, the reported improvements in top-1 and top-5 accuracy are marginal, and it is unclear if these differences are statistically significant. A statistical test should be performed to validate the claims of improved performance. Furthermore, the paper should provide a more in-depth analysis of the scenarios where the similarity-keeping loss provides a benefit, and where it does not. 

Another concerning factor is that the NICE model achieves lower performance than the models that do not use the similarity-keeping contrastive loss. However, the same dataset, the same GA encoder, and the same contrastive loss are used as in the paper that introduced the NICE model. What is different? The paper does not provide a detailed comparison of the implementation with the NICE model, which makes it difficult to understand the source of the performance discrepancy. A thorough comparison of the implementation details, including hyperparameters, training procedures, and any other factors that might explain the performance difference, is needed.

**Presentation of tables and figures** Table 2 and Table 3 contain the identical rows as in Table 1. It is very hard to read the text on the axes in Figure 7.

### Questions
1. What is the benefit of using the similarity-keeping loss term, as defined in Eq. (2). 
2. The NICE model uses the same contrastive loss, the same GA encoder and is evaluated on the same dataset. Why are the presented results in Table 1 higher than those produced by the NICE model? Could you provide a detailed comparison of your implementation versus the NICE model, including any differences in hyperparameters, training procedures, or other factors that might explain the performance difference?

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents MUSE, a framework for EEG-based image recognition that employs multivariate time-series encoders for EEG signals and an advanced image encoder. MUSE leverages a self-supervised learning approach to achieve state-of-the-art performance in zero-shot image classification, with top-1 and top-5 accuracies of 19.3% and 48.8%, respectively. The framework includes a novel similarity-keeping mechanism to enhance contrastive learning and provides insights into human visual processing through model interpretation.

### Strengths
This paper focuses on a novel brain-based image recognition. A new method has been proposed with new loss functions and EEG encoders. Comparative studies have been conducted, including performance comparison, ablation studies, spatial-temporal analysis.

### Weaknesses
The paper's contributions, particularly regarding the loss functions and EEG encoder, require further elucidation. While the improvements over prior work are mentioned, the specific advancements are not clearly articulated. The ablation studies, crucial for understanding the impact of the EEG modal's inner loss and the image model on performance, do not provide compelling evidence. Specifically, the role of the proposed Similarity-Keeping loss needs more rigorous justification, as the reported gains are marginal and lack a clear mechanistic explanation. The ablation study comparing different EEG encoders (STConv vs. NervFormer) is also inconclusive, as the NervFormer's performance is inconsistent and its purported advantages are not well-supported by the results. Additionally, the roles of attention mechanisms, spatial-temporal, and temporal-spatial approaches need to be more clearly defined, and their effects on the model's performance need to be explained. The paper lacks a detailed analysis of how these architectural choices impact the model's ability to learn meaningful representations from EEG signals. The sections attempting to interpret what the model has learned from EEG signals lack conviction. Enhanced clarity and depth in these interpretations would significantly strengthen the paper.

### Questions
1) The introduction should more prominently feature the paper's key contributions and their significance compared to previous work.

2) Figures must be legible, with larger legends to ensure clarity and comprehension.

3) There's a need for a clearer explanation of the benefits of upstream spatial convolution and the comparative advantages of ST and TS methods. The 'Nerv' approach's lack of superiority in Table 1 should be addressed.

4) It will be beneficial to compare the inner batch similarity and the multi-modal similarity. Has it used the label information? If so, it’s not self-supervised. How did the contrastive loss of image modal update the model? Has the image encoder been updated?

5) A comparison of model complexity would underscore the methods' advantages.

6) The equation needs claims. What is ‘S’ in (2)?

7) Can you explain the time-frequency maps in Fig. 9-14? Is there a clear conclusion?

[1] Liang She, Marcus K Benna, Yuelin Shi, Stefano Fusi, and Doris Y Tsao. Temporal multiplexing of perception and memory codes in it cortex. Nature, pp. 1–8, 2024. 

[2] Pinglei Bao, Liang She, Mason McGill, and Doris Y Tsao. A map of object space in primate inferotemporal cortex. Nature, 583(7814):103–108, 2020.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors propose a method to decode images from scalp electroencephalographic (EEG) signals. They combine an EEG encoder with a image encoder (CLIP), and introduce a MUltimodal Similarity-keeping contrastivE learning (MUSE) framework for zero-shot EEG-based image classification. Experiments on an extensive visual EEG dataset are presented. The results are significantly better than state-of-the-art methods. The authors also visualize neural patterns via model interpretation, shedding light on the visual processing dynamics in the human brain.

### Strengths
Detailed numerical results and benchmarks are proposed. The numerical results are encouraging, showing a clear improvement over SOTA. 

The method is well described, and it makes good sense.

### Weaknesses
One could argue that the proposed pipeline mainly consists of existing building blocks. However, the overall approach is creative, and the application is fascinating. 

Numerical results are only presented for one dataset. It would need to be verified whether good results can also be obtained for other experimental protocols.

The neuroscience interpretation of the results is limited. More links with the existing literature could be established.

### Questions
The EEG scalp maps are too small to be useful. Perhaps it's better to select some of them, and make them larger. I sugges to select the EEG scalp maps showing key temporal or spatial patterns.

How does this work relate to similar studies based on fMRI? Are similar accuracies obtained or better? It would be nice to include a brief comparison table or discussion section comparing the EEG-based results to recent fMRI-based image decoding studies. 

The text in Figure 4 is too small.

The EEG encoder is only briefly described. More details are needed. Moreover, the interpretation of the EEG dynamics is rather superficial. Discussing the EEG encoder in more depth, and interpreting this encoder from a neuroscientific perspectice would help to better understand the strength of the proposed approach. I recommend analyzing specific frequency bands (e.g., alpha, beta, gamma) or temporal windows (e.g., early vs. late responses) that are known to be relevant for visual processing, and/or comparing the learned features to known ERP components or oscillatory patterns associated with visual perception.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper presented a study about image recognition from EEG. The proposed method used a CLIP-based contrastive learning to align the EEG and images. The experiment was performed on a public dataset.

### Strengths
The topic was interesting and had broad audience.

### Weaknesses
The study was incremental given the main idea has been explored in the previous studies. The proposed method was mainly based on CLIP and the contributions to the field were limited. The work was not solid and technically sound. The experiments were weak.

The presentation of the paper should be largely improved. The Abstract did not include any descriptions about the model details or model features. Some figures had small texts, making hard to see.

The novelty of the proposed method was unclear. More analysis was needed to interpret the results. Currently only the performance comparisons were described. More insights from the decoding results would be helpful for readers. The current version needed more discussions and analysis, rather than simply showing the numbers.

### Questions
1. More experiments on more datasets should be included to strengthened the work. Some baseline methods were missing. In Table I, only two main baselines were used for comparison.  
2. The presentation of the paper should be largely improved. The Abstract did not include any descriptions about the model details or model features. Some figures had small texts, making hard to see. 
3. Were the model performance evaluated based on subject-dependent? What about the generalization to new subjects or even new images? 
4. The novelty of the proposed method was unclear. More analysis was needed to interpret the results. Currently only the performance comparisons were described. More insights from the decoding results would be helpful for readers. The current version needed more discussions and analysis, rather than simply showing the numbers. 
5. The source codes should be provided for readers to reproduce all the results in the paper.

### Soundness
2

### Presentation
1

### Contribution
2
