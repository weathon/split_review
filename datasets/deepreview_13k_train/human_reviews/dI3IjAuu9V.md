# Towards Cross-modal Backward-compatible Representation Learning for Vision-Language Models

- Decision: Reject
- Scores: 5, 6, 5, 6

## Abstract
Modern retrieval systems often struggle with upgrading to new and more powerful models due to the incompatibility of embeddings between the old and new models. This necessitates a costly process known as backfilling, which involves re-computing the embeddings for a large number of data samples. In vision, Backward-compatible Training (BT) has been proposed to ensure that the new model aligns with the old model's embeddings. This paper extends the concept of vision-only BT to the field of cross-modal retrieval, marking the first attempt to address Cross-modal BT (XBT). Our goal is to achieve backward-compatibility between Vision-Language Pretraining (VLP) models, such as CLIP, for the cross-modal retrieval task. To address XBT challenges, we propose an efficient solution: a projection module that maps the new model's embeddings to those of the old model. This module, pretrained solely with text data, significantly reduces the number of image-text pairs required for XBT learning, and, once it is pretrained, it avoids using the old model during training. Furthermore, we utilize parameter-efficient training strategies that improve efficiency and preserve the off-the-shelf new model's knowledge by avoiding any modifications. Experimental results on cross-modal retrieval datasets demonstrate the effectiveness of XBT and its potential to enable backfill-free upgrades when a new VLP model emerges.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces Cross-modal Backward-compatible Training (XBT), designed to address the challenges of upgrading vision-language models in cross-modal retrieval systems. Traditional methods require costly backfilling, where old embeddings must be re-computed with new models, but XBT aims to eliminate this necessity. The authors propose a text-only pretrained projection module that aligns new model embeddings with those of the old model, significantly reducing the need for extensive image-text pairs. This method enhances training efficiency and preserves the knowledge of the new model while allowing for effective fine-tuning. Experimental results demonstrate the effectiveness of XBT in various cross-modal benchmarks, offering a promising solution for backfill-free upgrades in retrieval systems.

### Strengths
- The motivation is meaningful. The paper seeks to avoid the time-consuming updating calculations on the embeddings of a cross-modal retrieval system when a new, improved model is introduced.

- The paper aims to develop a backfill-free cross-modal retrieval system and extends Backward-compatible Training from the vision domain to the cross-modal domain, potentially opening a new research direction.

- The effectiveness of the proposed method is supported by the experimental results.

### Weaknesses
 - Poor formulation of the paper: There are incorrect citations in the paper. For example, in Lines 116 and 117, “(BT) was first introduced in the study Shen et al. (2020)” should be “(BT) was first introduced in the study (Shen et al. 2020).” Additionally, in Fig. 2, the captions refer to the wrong figures: "text-only pretraining" is on the left side, while XBT is on the right side, but the paper states "above" and "below."
- The backward-compatible representation seems counterintuitive. If the old model creates a flawed representational space, forcibly mapping the new, more powerful model to the old model's representation space could compromise the new model's representation. Could the authors discuss this issue?
- The baseline only considers the old model. As I understand it, the upper bound of a retrieval system when introducing a new, improved model should be based on the new model, while the old model serves as the lower bound.
- The retrieval performances of CLIP-ViT-B32 on Flickr and COCO are extremely low. According to the original CLIP paper, CLIP-ViT-L14 can achieve 88% R@1 on Flickr's text retrieval, while the performance of CLIP-ViT-B32 reported in this paper is 40.35%, which is over 40% lower than CLIP-ViT-L14. This lead to the experimental results unconvincing.

### Questions
Please refer to the weaknesses to check out the questions.

### Soundness
2

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
4

### Summary
The paper presents an approach to address the challenge of model upgrades in cross-modal retrieval systems by introducing Cross-modal Backward-compatible Training (XBT). This approach aims to align the embeddings of new Vision-Language Pretraining (VLP) models with those of the old models, thereby reducing the need for costly re-embedding of data, known as backfilling.

### Strengths
1. The concept of XBT is innovative and addresses a significant practical issue in the deployment of new models in real-world applications. The idea of using a text-only pretrained projection module to align embeddings is interesting and shows potential for efficiency gains.
2. The methodology is well-explained and technically sound. The authors have provided a clear outline of the training process, including the text-only pretraining and the cross-modal backward-compatible training stages.
3. The paper is well-supported by empirical evidence, with experiments on multiple benchmarks demonstrating the effectiveness of XBT in cross-modal retrieval tasks.

### Weaknesses
1. While the paper claims that XBT reduces the need for image-text pairs, the scalability of the approach in very large-scale systems with real-world data distributions is not fully explored. The author only used a source dataset from BLIP (which is a sythetic dataset), a subset from LAION400M will be benificial for this work.
2. The paper briefly mentions the impact of data quality on XBT performance. A more detailed analysis on how noisy or biased training data might affect the embedding alignment could provide deeper insights.
3. The computational analysis is limited to a comparison of training times and memory loads. A more comprehensive analysis, including the trade-offs between accuracy and computational resources, would be valuable.

### Questions
Please see weaknesses.

### Soundness
3

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
4

### Summary
This paper presents a cross-modal backward-compatible training (XBT) method that enables the deployment of new multimodal encoders while maintaining compatibility with existing retrieval systems. The key innovation lies in its approach to align a single modality to potentially achieve cross-modal alignment, offering a practical solution for real-world system updates. The work addresses an important practical challenge in maintaining backward compatibility while upgrading multimodal systems.

### Strengths
1.	Comprehensive Experimentation: The paper demonstrates strong empirical validation through extensive experiments across multiple models and datasets. This thorough evaluation effectively showcases the method's generalization capability and robustness across different scenarios.
2.	Novel Perspective: The authors present an innovative approach by proposing that aligning a single modality can potentially lead to cross-modal alignment. This insight offers a fresh perspective on handling multimodal compatibility issues and could inspire new research directions in the field.
3.	Practical Relevance: The work addresses a real-world challenge in deploying updated multimodal systems while maintaining compatibility with existing infrastructure, making it valuable for practical applications.

### Weaknesses
1.	Some citation formats are incorrect.
2.	Most performance tables are confusing, making it difficult to clearly understand the performance of both old and new retrieval systems.
3.	Lack of several analytical experiments, which are detailed in questions.

### Questions
1.	Can you show the similarity between new and old representations after φ's transformation for both image and text? Is image similarity lower than text similarity? What is the relationship between similarity and performance? How does noise magnitude in φ affect similarity?
2.	In Table 1, B32 is used as an old encoder model in the original column. Why does B32 show better performance after XBT training compared to the original B32? Can XBT improve the performance of old retrieval systems?
3.	Could the tables be reorganized into three parts to show the retrieval performance of:
-	Old systems
-	New systems
-	Proposed backward-compatible new systems

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors propose a novel approach called Cross-modal Backward-compatible Training (XBT), which extends the concept of Backward-compatible Training (BT) from vision-only to cross-modal retrieval, specifically for aligning Vision-Language Pretraining (VLP) models like CLIP.   A text-only pre-trained projection module, ϕ, is proposed to map new model embeddings to old model embeddings. This module is trained solely with text data, reducing the need for image-text pairs. The paper utilizes parameter-efficient training strategies that improve efficiency and preserve the new model's knowledge by avoiding modifications to it. Experiments on cross-modal retrieval datasets show XBT's effectiveness and its potential to enable backfill-free upgrades when new VLP models emerge.

### Strengths
1. The targeting problem is interesting. And it is might be useful for the real applications.

2. The proposed method achieved expecting performance.

### Weaknesses
1. It seems that the motivation of the text-only pre-training stage is not very clear.

2. Why preventing overfitting in the text-only pre-training stage is needed ? Are there any explanations for that?

### Questions
1. Why is the text-only pre-training necessary?

2. Why preventing overfitting in the text-only pre-training stage is needed ? Are there any explanations for that?

### Soundness
3

### Presentation
3

### Contribution
3
