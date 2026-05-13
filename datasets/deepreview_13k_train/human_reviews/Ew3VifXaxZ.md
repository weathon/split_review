# Enhancing Outlier Knowledge for Few-Shot Out-of-Distribution Detection with Extensible Local Prompts

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
Out-of-Distribution~(OOD) detection, aiming to distinguish outliers from known categories, has gained prominence in practical scenarios. Recently, the advent of vision-language models~(VLM) has heightened interest in enhancing OOD detection for VLM through few-shot tuning. However, existing methods mainly focus on optimizing global prompts, ignoring refined utilization of local information with regard to outliers. Motivated by this, we freeze global prompts and introduce a novel coarse-to-fine tuning paradigm to emphasize regional enhancement with local prompts. Our method comprises two integral components: global prompt guided negative augmentation and local prompt enhanced regional regularization. The former utilizes frozen, coarse global prompts as guiding cues to incorporate negative augmentation, thereby leveraging local outlier knowledge. The latter employs trainable local prompts and a regional regularization to capture local information effectively, aiding in outlier identification. 
We also propose regional-related metric to empower the enrichment of OOD detection. Moreover, since our approach explores enhancing local prompts only, it can be seamlessly integrated with trained global prompts during inference to boost the performance. Comprehensive experiments demonstrate the effectiveness and potential of our method. Notably, our method reduces average FPR95 by 5.17\% against state-of-the-art method in 4-shot tuning on challenging ImageNet-1k dataset, even outperforming 16-shot results of previous methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The proposed work focuses on enhancing the model's ability to detect local features by training local feature prompts using localized image information. Furthermore, based on these local feature prompts, this paper introduce a new OOD score that integrates with MCM Score.

### Strengths
1.	Local image information is utilized to train local feature prompts, enhancing the model's ability to detect local features.

2.	Based on local feature prompts, an OOD metric combining MCM has been proposed, along with a new ID classification metric.

### Weaknesses
1.	In the latest works related to OOD detection, there are several studies similar to the method in this paper, such as "ID-like (ID-like Prompt Learning for Few-Shot Out-of-Distribution Detection)" and "NegLabel (NEGATIVE LABEL GUIDED OOD DETECTION WITH PRETRAINED VISION-LANGUAGE MODELS)." The structure of this paper is similar to that of ID-like, as it also employs random crop combined with CLIP to construct ID and OOD data, and utilizes positive prompts and negative prompts. However, the paper lacks a comparison and analysis of strengths and weaknesses with the ID-like paper. It is recommended that the authors add relevant discussions to enhance the depth and breadth of the paper.

2.	The OOD Score strategy proposed in this paper presents results for SMCM and SR-MCM but lacks results that only use the Regional OOD score and corresponding ablation experiments. This makes it difficult to effectively demonstrate that the SR-MCM outperforms the strategy that solely relies on the Regional OOD score. It is suggested that the authors include this part of the experiment to strengthen the paper's persuasiveness and the comparability of the results.

### Questions
Please refer to the weakness.

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
3

### Summary
The paper presents a novel approach to few-shot out-of-distribution (OOD) detection. The aim of this paper is at addressing a limitation of existing few-shot OOD detection methods, which predominantly rely on global prompts and struggle to identify challenging OOD images that differ only locally from in-distribution (ID) images. 

To enhance detection accuracy for these difficult cases, the proposed method introduces learnable local prompts. Specifically, the proposed method first picks out multiple randomly cropped regions from the original image and classifies them as positive or negative based on their similarity to the global text embedding. These regions are then used as tarining exampes to learn the positive and negative learnable local  prompts.

Experimental results on several popular benchmark datasets for few-shot OOD detection show that the proposed method can achieve better accuracy than several existing few-shot OOD detection methods.

### Strengths
- This paper proposes a novel idea of learning local prompts, which has not been well explored in the context of few-shot OOD detection.

- Experimental results reported in this paper show that the proposed method outperforms existing methods.

- This paper is well-organized and easy to follow.

### Weaknesses
My main concerns are about the experimental results.

**W1**. Some of the results, such as AUROC in Table 1, show very small performance differences (less than 1%) between the proposed method and the existing methods. Since the proposed method uses random cropping to learn local prompts, the standard deviation of accuracy should be reported to show the significance of the performance differences. It is crucial to determine if the observed improvements are statistically significant or merely due to random fluctuations in the cropping process. Without standard deviations, it's difficult to assess the robustness of the method.

**W2**. Looking at Fig. 4, the accuracy differences between Ours w/ LNP and Ours w/o LNP appear to be quite small. LNP is one of the core ideas of the proposed method. If the accuracy differences are small, the superiority of the proposed method would be questionable. The marginal improvement raises concerns about the actual contribution of the local negative prompts, and whether the added complexity is justified by the performance gain.

**W3**. As stated in the second paragraph of the introduction section, the aim of this paper is to detect hard OOD samples that are similar to the ID classes as a whole, but can be distinguished only by looking at subtle local differences. However, there is no support in this paper for whether the proposed method can actually detect such a hard OOD sample. It would be good to show some examples of OOD images that could not be detected with the global prompts alone, but could be detected with the introduction of the local prompts. The lack of such examples makes it difficult to validate the core claim of the paper.

**W4**. Based on the results in Table 9, the authors claim that the accuracy of the proposed method is not sensitive to the values of the two hyperparameters $\lambda_{\text{neg}}$ and $\lambda_{\text{reg}}$. However, this claim seems to contradict the effectiveness of the proposed method since the learning of the local prompt, which is the core of the proposed method, is controlled by these two hyperparameters (see Eq. 8). If the performance is insensitive to these parameters, it questions the importance of the local prompt learning mechanism itself.

**W5**. Table 8 shows that the FPR95 values change nonlinearly with the number of shots; the FPR95 values improve as the number of shots increases from 4-shot to 8-shot, but deteriorate as it increases to 16-shot. What is the reason for this? This non-monotonic behavior is unexpected and requires a clear explanation. It suggests that there might be an optimal number of shots for this method, and that simply increasing the number of shots does not necessarily lead to better performance.

### Questions
As noted in the Weaknesses section, I believe the experiments have several significant shortcomings. While all of these issues are important, I have listed them in descending order of priority. The first four points (**W1-W4**) directly concern the effectiveness of the proposed method and the motivation of this paper. I would like to encourage the authors to address these points in their response.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work proposes to enhance Out-of-Distribution (OOD) detection through local prompt learning. Specifically, the method involves randomly cropping training images and identifying hard negatives by comparing their similarity to global prompts, which are provided in textual format. These hard negatives, along with the associated object samples, are then used to train local negative prompts.

### Strengths
1. The paper is well-written overall, but it lacks some crucial symbol definitions and implementation details.
2. The method addresses a significant task aimed at detecting OOD images using only a few images from the ID data. Extensive experiments demonstrate the effectiveness of the method.

### Weaknesses
1. Some crucial symbol definitions, such as T_k and ​\hat{t}_i , are not clearly explained. Specifically, the paper does not define what the input to T_k is, nor does it clarify if it is a vector or a scalar. Additionally, the exact meaning of the subscript 'i' in \hat{t}_i is not specified, leaving ambiguity about the number and nature of these negative local prompts.
2. Apart from replacing the maximum process with an average in Equation 3, what distinguishes the proposed method from [Miyai et al. 2023b]? The paper does not provide a clear explanation of the fundamental differences in the underlying mechanisms or objectives, making it difficult to assess the novelty of the approach beyond a minor modification to the scoring function. The motivation for using an average instead of a maximum is also not well-justified in the context of OOD detection.
3. Although hard negative samples can serve as a form of OOD data, they primarily consist of cluttered backgrounds or parts of in-distribution (ID) objects lacking distinctive features. Essentially, they are quite different from true OOD classes. The work lacks an explanation of the underlying theories. It is unclear why training on these hard negatives, which are essentially noisy versions of ID data, would generalize to detecting true OOD samples. The paper needs to provide a theoretical justification for this approach.

### Questions
1.  How are the local prompts and negative local prompts initialized, and what are their dimensions?
2.  Moreover, from lines 270 and 237, it appears that global and local prompts t_k share the same format, "a photo of {class}." However, Figure 2 indicates that local prompts are trainable, which seems contradictory. Could the authors provide further clarification? Are the local prompts in Equation 4 simply using the same symbol t_k but representing different meanings? If so, using distinct symbols might be more appropriate.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors propose an approach to Out-of-Distribution (OOD) detection in Vision Language Models through few-shot fine-tuning. The paper uses random crops from the images to generate negative global prompts, which are used to guide the learning of learnable local prompts aimed at detecting local or regional outliers. They also propose a metric for quantifying the OOD scores that takes into account local or regional information.

### Strengths
I think the paper sheds light on an interesting perspective regarding the role of local or regional features in OOD detection. The idea of randomly cropping the image and creating negative global samples based on image-text similarity scores, while simple, is both effective and clever. The authors have empirically demonstrated the effectiveness of learning local prompts, achieving strong performance.

### Weaknesses
I am unsure about the justification for using few-shot fine-tuning. I do not understand what the authors meant in lines 46-48. Having access to the full dataset for a class can provide a better estimate of the outliers. Identifying outliers with only a few examples, while challenging, may be biased toward the examples of the class being used, especially if the number of shots is low and one of the examples is an outlier. The reason I am focusing on this is that the results in Table 1 seem counterintuitive to me. It appears that OOD detection worsens with 16 shots on the SUN and Places datasets, where we would expect the model to identify OODs better with more examples.

There also seems to be a lack of ablation studies regarding the model's performance without the learnable negative local prompts. I believe this ablation is important.

I have a comment about Figure 2. It mentions local features of augmented inputs, which I believe refers to the image patches from the randomly cropped images. However, from the figure, it appears that they are only taking patches from the entire image, which is confusing.

### Questions
I kindly request that the authors clarify the motivation behind few-shot tuning and address the discrepancy between few-shot and many-shot performance in Table 1, as highlighted in the weaknesses section. I believe an ablation study on the impact of additional negative local prompts is necessary to justify their use. Additionally, I would appreciate it if the authors could provide a clearer explanation of the image in Figure 2.

### Soundness
3

### Presentation
3

### Contribution
3
