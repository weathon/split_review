# Data De-Duplication and Semantic Enhancement for Contrastive Language-Image Pre-training

- Decision: Reject
- Scores: 3, 5, 5, 5

## Abstract
Benefiting from the countless image-text pairs in the web data, vision-language pre-training models (e.g. CLIP) have emerged as an efficient alternative in learning representations that are transferable across a wide range of downstream tasks.
However, we reveal that the web data are noisy, with significant scene redundancy and misalignment in the image-text pairs, which increase the training expenses and computing resources.
To alleviate these problems, this paper proposes a novel training strategy that comprises two dedicated components, namely Data De-Duplication ($\text{D}^3$) and Semantic Enhancement (SE).
$\text{D}^3$ leverages the pre-clustered data prototypes to decrease the training cost without reducing the data diversity by uniformly sampling a portion of image-text pairs at each training epoch. 
SE utilizes a large language model (LLM) and a visual large language model (VLLM) to refine and augment the text caption, which can help to form a one-to-multiple mapping relation between image and text. 
Furthermore, we employ a Diverse Captions Training Mechanism (DCTM) and a Modality Self-enhancement Training Mechanism (MSTM) for effective training. 
Experimental results indicate that the proposed method achieves state-of-the-art performance on various tasks including image classification, image-text retrieval, object detection, and segmentation (performance improvements varying from 0.2\% to 23.9\% for all datasets) with only half of the training time compared with original CLIP. 
Our code and generated data will be publicly available.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposed DS-CLIP for vision-language pre-training, which contains several techniques to improve original CLIP. 1) Data De-Duplication (D^3) is used for data sampling. 2) Diverse Captions Training Mechanism (DCTM) and Modality Self-enhancement Training Mechanism (MSTM) for improving the quality of the original caption. They show the proposed techniques can improve the training efficiency and final performance of zero-shot evaluation.

### Strengths
1. The authors conducted extensive experiments with various setups. 
2. The overall performances on several benchmarks are stronger than the original CLIP.

### Weaknesses
1. I think the presentation is really bad and confusing. a) There are several abbreviations are introduced in the abstraction and introduction, e.g., D^3, SE, DS-CLIP, DCTM, and MSTM. Additionally, those abbreviations seem to have a hierarchical structure, DS-CLIP is for SE and D^3, SE is for DCTM and MSTM, which is really confusing. b) Some parts of the presentation are unclear. What's Image-to-Text
Multi-Positive Contrastive Loss and Text Multi-Positive Self-Supervised Loss in Fig. 2? What's the hyper-parameter choice for K, $\alpha$ and $\beta$? c) Some illustrations can be improved. In Fig. 2(a) the original image and the augmented image are reversed and the spacing between letters is different. d) Several dataset abbreviations are introduced in Sec. 4.1. However, those abbreviations are used in Sec. 4.3. You'd better define them when used. e) The ablation results in Tab. 1 are hard to read. What's your default setting and final setting for those experiments? 
2. While there are several techniques are introduced in this paper, many of them are already proposed in prior arts. DCTM has been proposed in LaCLIP (Fan et al.). MSTM was introduced in DeCLIP (Li et al.). I can't find the main contribution of this paper. If those techniques are not your contribution, do not claim it. What's your main point and how does your main contribution affect the final performance?

### Questions
See the weakness part.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces a new training framework for CLIP-like models, aiming to 1) reduce training costs and 2) mitigate the misalignment issues stemming from noisy image-text pairs. For this, the authors propose following components:

1. Data De-duplication (D3) enables fast training without losing the diversity of sampling by leveraging pre-clustered prototypes which enables.

2. Semantic Enhancement (SE) mitigates the noisy image-text correspondence issues by generating more descriptive captions with powerful pre-trained Large Language Models (LLMs) and Vision-Language Large Models (VLLMs) 

3. Diverse Captions Training Mechanism (DCTM) and a Modality Self-enhancement Training Mechanism (MSTM) : DCTM utilizes diverse captions, while MSTM employs a combination of uni-modal contrastive learning.

 As a result, it achieves state-of-the-art performance over various downstream tasks with half of the training time compared with original CLIP.

### Strengths
1. The paper is well-written and figures are easy to understand.
2. The motivation of paper (efficient pre-training by mitigating mis-alignment in image-text papers and scene redundancy) is solid.
3. The experimental results are strong.

### Weaknesses
Despite  strong experimental results and motivation, the novelty of the proposed methods appears to be limited:
    
   1) In SE: The effectiveness of synthetic captions from VLP models for mitigating noisy image-text alignment has already been demonstrated by BLIP.  Therefore, it is somewhat straightforward that more descriptive captions from recent LLaVA models would be effective. Furthermore, as the authors themselves pointed out, the concept of using LLM-generated captions has already been proposed in LaCLIP. Moreover, the effectiveness of using both LLaVA and LLaMA is unclear. See question 2.

   2) In DCTM: Previous works like OSCAR [1], ALBEF [2], and BLIP have empirically shown that diverse captions (one image with multiple captions) from sources like COCO and Flickr are effective in enhancing performance. These works treat each image-caption pair as unique; for instance, if one image comes with five captions as in the COCO setting, they construct five distinct pairs. The difference in the current approach is the use of diverse captions with a multi-positive contrastive loss. However, it remains unclear where the benefits of this approach specifically originate from. See question 1.

   3) In MSTM: The utility of uni-modal contrastive losses in improving performance has already been showcased by ERNIE-VIL 2.0 [3].

### Questions
1)  The benefits from DCTM comes from the data augmentations (use multiple captions) or from multi-positive contrastive loss? Moreover, what is the difference between multi-positive contrastive loss and supervised contrastive loss [4]? What is the advantage of using multi-positive contrastive loss? 

2)  Does it have to use both LLaVA and LLaMA? In table 2 (c), the gap between LLaVA only and LLaVA/LLaMA seems very marginal. Isn't it possible to use LLaVA only to generate diverse captions with proper prompts?

3) In Figure 3 and Figure5, it seems that the boundaries are still indistinguishable.

[4] Khosla, Prannay, et al. "Supervised contrastive learning." Advances in neural information processing systems 33 (2020): 18661-18673.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a novel training strategy called DS-CLIP to improve the traditional contrastive language-image pre-training (CLIP) model. It introduces two components - Data De-Duplication (D3) and Semantic Enhancement (SE) to reduce training costs and enhance dataset diversity. D3 employs data clustering and sampling to reduce scene redundancy without losing diversity. SE uses large language models to generate diverse, semantically enriched captions to address image-text misalignment. Furthermore, this paper proposes Diverse Captions Training and Modality Self-enhancement Training for effective learning. Extensive experiments show DS-CLIP achieves state-of-the-art on various downstream tasks, including classification, retrieval, detection and segmentation.

### Strengths
(1)	This paper addresses the efficiency problem of CLIP pre-training by proposing Data De-Duplication (D3) and Semantic Enhancement strategies, which first clusters and re-samples noisy multi-modal data to ensure a balanced semantic distribution without reducing the scene diversity, then employ powerful LLM and VLLM to enrich semantic information of text and mitigate the issue of text-image misalignment.

(2)	This paper presents a one-to-multiple mapping among image and text as the Diverse Captions Training Mechanism (DCTM) and Modality Self-enhancement Training Mechanism (MSTM), which effectively reduces training time and alleviates data redundancy and misalignment.

(3)	This paper is clearly written and easy to follow. The problems and limitations of previous CLIP training are clearly explained. The method section has explained technical details well. The related tables and figures also are presented clearly.

(4)	Extensive experiments have shown that the DS-CLIP significantly outperforms traditional CLIP on various vision-language tasks, especially fine-grained classification datasets, and various patch-level downstream tasks from 0.2% to 23.9%, with ONLY half of the training time.

### Weaknesses
(1)	The core contributions of this paper are the D3 and SE modules, which belong to the data augmentation and data cleaning essentially. The clustering, re-sampling, and text re-generation are all very common strategies in recent work, e.g., BLIP [1], and BLIP-2[2]. Hence the technical contribution is weak. Specifically, the paper does not adequately demonstrate how the proposed approach differs fundamentally from existing data augmentation techniques. The use of LLMs for text generation, while effective, is not a novel concept in itself, and the paper lacks a detailed analysis of how the specific implementation of LLM-based text augmentation provides a unique advantage over other methods. The clustering and re-sampling techniques, while useful for reducing redundancy, are not presented with sufficient novelty to justify a significant contribution.

(2)	The previous contrastive loss function can deal with the multi-positive image-text pairs during training. However the experiments lack ablation studies or theoretical justification, more analysis can help prove the effectiveness of the proposed loss function. The paper does not provide a clear explanation of why the proposed loss function is superior to existing contrastive loss functions when dealing with multiple positive text samples per image. The ablation study is insufficient to demonstrate the necessity of the proposed loss function, and the paper lacks a theoretical analysis of the properties of the loss function that justify its effectiveness.

(3)	The CLIP is a famous multi-modal pretraining model. However, this paper only contains pure vision-understanding tasks and lacks sufficient experiments on various multi-modal tasks and datasets, e.g., image-text matching, video-text retrieval, and image captioning.

### Questions
(1)	This paper has claimed that the DS-CLIP only needs half the training time compared with traditional CLIP. But the D3 and SE modules also need large computational costs, e.g., the clustering operation, and the inference process of LLM/VLLM. It is necessary to report related time costs since the extra data augment is an important part of the proposed method.

(2)	The Data De-Duplication (D3) relies on the clustering algorithm to converge unlabeled data. However, the K-means is not a good choice for large amounts of data, in which the runtime and memory cost are non-negligible with multiple iterations. Have you tried any other clustering algorithms, e.g., spectral clustering? Besides, why not cluster the texts?

### Soundness
2 fair

### Presentation
3 good

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
This paper explores several tricks to enhance the CLIP model.
These tricks include cluster-based data de-duplication, text augmentation with LLM and VLM, and image augmentation.
The pre-training is performed on the large-scale Laion400M dataset.
With the experimental results on a wide variety of downstream tasks, we can observe that the proposed method achieves improved performance over the plain CLIP model.

### Strengths
- The paper is well-written and well-organized.
Most parts of this paper are easy to follow and understand.

- The proposed method achieves consistent improvements on diverse downstream tasks and datasets when compared to the vanilla CLIP model.

- The authors conducted detailed ablation studies of the proposed method.

### Weaknesses
 - The biggest concern for this paper is the key intuition and motivation of the proposed method.
The data de-duplication is leveraged to reduce the training samples, which is useful for training efficiency.
However, the other three tricks mostly focus on augmentation, thus introducing more data for training.
This mix-up makes the readers follow the key contribution of this paper.

- The novelty of the proposed method is somewhat limited.
All these approaches look like tricks that have been well-explored by existing literature.

- The first approach, i.e., data de-duplication is also limited by the pre-trained vision model.
If we use another model rather than DINO, the sampled images could be different, which may lead to different conclusions.

- There are many notational errors (for example, N or B for the number of pairs?) in the descriptions of Sec. 3.1. Please carefully revise them.


### Questions
- Eqn.1 seems not right.
Normally the NCE contrastive loss only holds one positive label.
But for this approach, there could be at least three positive labels.
Maybe some theoretical analysis helps address this concern.

- Have the authors also considered generating images as augmentation?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
