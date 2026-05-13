# R-MAE: Regions Meet Masked Autoencoders

- Decision: Accept
- Scores: 6, 6, 6

## Abstract
In this work, we explore \emph{regions} as a potential visual analogue of words for self-supervised image representation learning. Inspired by Masked Autoencoding (MAE), a generative pre-training baseline, we propose masked region autoencoding to learn from groups of pixels or regions. Specifically, we design an architecture which efficiently addresses the one-to-many mapping between images and regions, while being highly effective especially with high-quality regions. When integrated with MAE, our approach (\ours) demonstrates consistent improvements across various pre-training datasets and downstream detection and segmentation benchmarks, with negligible computational overheads. Beyond the quantitative evaluation, our analysis indicates the models pre-trained with masked region autoencoding unlock the potential for interactive segmentation.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors introduce a self-supervised image representation learning method called "masked region autoencoding" (RAE), treating regions as the visual equivalent of words. When integrated with the existing Masked Autoencoding (MAE) approach, the combined method (R-MAE) consistently improves performance in various vision tasks. RAE offers a more region-aware and instance-aware representation of images.

### Strengths
1. The paper is highly clear in its presentation, effectively conveying the proposed methodology with its motivation.
2. The paper extends the traditional Masked Autoencoding (MAE) approach by considering regions as visual analogs of words. The concept of using regions for interactive segmentation is also original.
3. The proposed method can consistently help downstream performance on localization-related tasks (e.g., detection and segmentation).

### Weaknesses
1. The paper could benefit from a more extensive comparison with existing methods in the field. While it highlights the strengths of R-MAE, a more in-depth quantitative comparison with other state-of-the-art self-supervised learning techniques (based on MAE) would strengthen the paper.

### Questions
1. Is the performance of R-MAE sensitive to the quality of region maps, and are there strategies to mitigate this sensitivity?
2. Could the authors provide a more extensive quantitative comparison with other state-of-the-art self-supervised learning methods in computer vision? This would help readers understand how R-MAE performs in relation to existing techniques.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a new pretext task called mask Region Autoencoding for self-supervised visual representation learning. Instead of considering pixels as the operated units, the authors conduct masking and reconstruction on the so-called region levels. By integrating RAE into MAE, the resulting R-MAE achieves impressive performance on various transfer learning settings.

### Strengths
- The paper is generally well-written with solid experimental results.
- The paper has a clear explanation of the proposed method with valid qualitative demonstration.
- Beside common transfer learning experiments, the authors also explore the usage of R-MAE for interactive segmentation.

### Weaknesses
- About the importance of regions:
  - As discussed in Sec. 2, the authors claim that there are many different sources to obtain regions. In other words, here regions do not have a specific definition, especially under the context of unsupervised learning. Or in another words, the best definition of regions might differ with respect to different downstream tasks, while just for object detection and semantic segmentation, SAM proposals might be the best.
  - One following question to explain is that why in SAM as the region source can even perform better than panoptic ground truth COCO annotations when pre-trained on COCO, as in Tab. 1(d)?
  - Also, as claimed in 3rd paragraph of Sec. 1, the authors claim that "regions" might perform similarly with "words" in language models to improve the scalability of MAE and pursue visual emergent properties. Unfortunately, both the qualitative and quantitative results can only demonstrate similar observation for the learned representation with MAE. Moreover, the authors only conduct experiments with ViT-B, without further exploration about the scalability of R-MAE.
  - Therefore, it is hard to convince me that this work has a different motivation with locality reconstruction works like LoMaR [1] and SemMAE.
- About the architecture:
  - Does the region encoder share weights with the pixel encoder? If not, which one would be transferred for downstream tasks in the context of RAE and R-MAE respectively?
  - Is there any advantage to conduct region reconstruction only for binary region masks, which totally throw the RGB information, while the latter should also be part of the semantics? This question is way more interesting if we consider that RAE with SAM performs better than MAE.
  - One following question would be what will happen if we transfer RAE and MAE weights to downstream color-sensitive tasks, like the the Flowers classification dataset.
  - Moreover, is there any advantage to maintain a separate branch of region encoder, since a simpler implementation might be similar with LoMaR, where for the visible part of each region, we can directly utilize them to reconstruct the RGB values of the masked part of this specific region, so that we can perform the two objectives of R-MAE at the same with without introducing a separate branch.
  - Just to make sure I have understood correctly, does RAE mean we only apply the upper part (=region encoder + region decoder) of Fig. 1?
- Overall, it is hard to convince me that region modeling is so important as the authors claim and it seems like there are much easier ways to implement this idea than the proposed R-MAE framework.

[1] Chen, Jun, et al. "Efficient self-supervised vision pretraining with local masked reconstruction." *arXiv preprint arXiv:2206.00790* (2022).

[2] Chen, Kai, et al. "Mixed autoencoder for self-supervised visual representation learning." *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition*. 2023.

[3] Liu, Jihao, et al. "Mixmim: Mixed and masked image modeling for efficient visual representation learning." *arXiv preprint arXiv:2205.13137* (2022).

### Questions
- About experiments:
  - R-MAE has been surpassed by earlier MAE-based framework targeting at detection and segmentation with local awareness (e.g., 800-epoch MixedAE [2] outperforms 1600-epoch R-MAE on ADE20K).
  - It would be better to also report quantitative comparison for interactive segmentation for better understanding in Fig. 6.

[1] Chen, Jun, et al. "Efficient self-supervised vision pretraining with local masked reconstruction." *arXiv preprint arXiv:2206.00790* (2022).

[2] Chen, Kai, et al. "Mixed autoencoder for self-supervised visual representation learning." *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition*. 2023.

[3] Liu, Jihao, et al. "Mixmim: Mixed and masked image modeling for efficient visual representation learning." *arXiv preprint arXiv:2205.13137* (2022).

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper studies regions in masked autoencoders. The idea is interesting although there has been a large amount of self-supervised learning introducing the concept of regions (These methods are generally called self-supervised object detection methods in the field). The resulting R-MAE shows better performance on COCO, ADE20K datasets compared with MAE baseline.

### Strengths
1. The overall paper is clear and easy to follow.
2. The analysis for different designs of regions is comprehensive.
3. This paper gives some suggestions when training with regions in MIM.
4. The authors will open the source code and models.

### Weaknesses
1.	Self-supervised contrastive learning needs to introduce the concept of region to focus local information due to its a priori assumption of image semantic consistency, but MAE does not have this problem. Moreover, I agree that the reconstruction of raw pixel values lacks a higher level of semantic information for image understanding compared to word reconstruction in NLP. However, I do not agree the introduction of binary regions adds high-level semantics. Therefore, I argue this paper is the same as previous self-supervised object detection learning. The effect comes from further learning of the local region, so it is effective in tasks such as detection and segmentation. At the same time, the performance of this type of method will be lower than the baseline on tasks such as ImageNet image classification. If high-level semantic understanding tasks such as image classification do not perform well, then it is difficult to say that R-MAE has a high-level understanding as mentioned in the introduction.
2.	Like question 1, the paper lacks ImageNet classification experiments.
3.	The calculation amount comparison is unfair. The paper only calculates the calculation amount of the architecture, but the results of the FH algorithm and SAM region generation are not included.
4.	From Table 3, more data show that the gain in segmentation results relative to MAE is weaker. Is there no difference between the results of MAE and R-MAE on a larger data set?

### Questions
Please refer to weaknesses.

### Soundness
2 fair

### Presentation
4 excellent

### Contribution
2 fair
