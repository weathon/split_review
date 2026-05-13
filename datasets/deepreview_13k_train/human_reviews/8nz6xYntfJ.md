# AlignDiff: Aligning Diffusion Models for General Few-Shot Segmentation

- Decision: Reject
- Scores: 6, 5, 3, 5

## Abstract
Text-to-image diffusion models have shown remarkable success in synthesizing photo-realistic images. Apart from creative applications, can we use such models to synthesize samples that aid the few-shot training of discriminative models? In this work, we propose AlignDiff, a general framework for synthesizing training images and associated mask annotations for few-shot segmentation. We identify three levels of misalignments that arise when utilizing pre-trained diffusion models in segmentation tasks. These misalignments need to be addressed to create realistic training samples and align the synthetic data distribution with the real training distribution: 1) instance-level misalignment, where generated samples fail to be consistent with the target task (e.g., specific texture or out-of-distribution generation of rare categories); 2) scene-level misalignment, where synthetic samples are object-centric and fail to represent realistic scene layouts with multiple objects; and 3) annotation-level misalignment, where diffusion models are limited to generating images without pixel-level annotations. AlignDiff overcomes these challenges by leveraging a few real samples to guide the generation, thus improving novel IoU over baseline methods in generalized few-shot semantic segmentation on Pascal-5i and COCO-20i by up to 80%. In addition, AlignDiff is capable of augmenting the learning of out-of-distribution categories on FSS-1000, while naive diffusion model generates samples that hurt the training process. The code will be released.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
- The paper aims to synthesize training images and masks of novel categories to augment few-shot learning.

- They identify three issues with directly using text-conditioned stable diffusion model -- failure on OOD classes, object-centric bias of stable diffusion and coarse mask generation. These are referred to as instance, scene and annotation level misalignments.

- Failure on OOD is addressed using normalized masked textual inversion. Object-centric bias is mitigated using copy-paste augmentation, and coarse masks are refined by updating the segmenter using semi-supervised learning.

- Experiments in the GFSS (Pascal-5i, COCO-20i datasets) and FSS (FSS-100 dataset) settings show impressive results.

### Strengths
- The paper is well-written and well-organized 
- The identification of issues arising in applying text-to-image models for data scarce few-shot semantic segmentation setting is valuable 
- Even though the solutions provided to each of the issues are not novel, they are simple and well-proven methods 
- Extensive ablation study is provided in the appendix (both qualitative and quantitative)

### Weaknesses
 - Limited comparison on the FSS-1000 dataset
- Evidence of the finding that treating the learnable embedding as an adjective leads to a faster and more stable training convergence, is missing
- A clear discussion of time taken by each step (textual inversion, semi-supervised mask generation), and comparison of total time with Grounded Diffusion (which is the only alternate baseline) 
- The evaluation setup describes that DiffuMask without their prompt engineering is used, but it it missing from Table1 and Table2

### Questions
- Do the methods compared with in Table1 and Table2 also use base classes, or is it extra information used in this approach? (for copy-paste and semi-supervised learning parts) 
- An ablation on the amount of generated samples would be valuable in practice 
- See weaknesses

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes to use the pretrained diffusion models to augment the training set for few-shot semantic segmentation. Specifically, this paper provides an algorithm that generates novel instances from the diffusion model conditioned on a few available training data with annotated semantic segmentation masks and class names. Experiments on standard benchmarks such as FSS-1000 demonstrate the proposed data augmentation method improves the overall performance of existing few-shot segmentation methods.

### Strengths
1. It is technically sound and interesting to use pretrained image generative models for data augmentation. This paper pinpoints three major types of misalignment between the synthetic distribution and the target data distribution when a naive text-conditioned image generation method is applied and proposes a simple solution per aspect.
2. Experiments demonstrate that the proposed data augmentation can significantly improve the existing few-shot segmentation methods, especially on novel categories. 
3. This paper is well-written and easy to follow.

### Weaknesses
1. Even though the proposed data augmentation method improves the overall performance, the synthetic data can be harmful for many categories (see Fig. A.2). It is worth a more thorough analysis regarding this issue. For example, is that because the synthetic data misaligned with the target distribution, just like the text-conditioned image generation baseline? Specifically, are there identifiable patterns in the types of categories where the synthetic data hurts performance? For instance, are these categories characterized by specific visual attributes or complexities that the diffusion model struggles to capture accurately? A deeper investigation into the failure modes of the synthetic data generation is needed to understand the limitations of the proposed approach.
2. As stated in the limitation section, the proposed method degrades when the gap between the target distribution and the distribution covered by the generative model is large (e.g., medical images). However, I believe the few-shot semantic segmentation would be mostly useful for rare categories that are hard to collect enough instances for training a segmentation model. For common classes (e.g., chairs, sofa, boat) of which plenty of images can be found, it is hard to justify the necessity of using synthetic data. How is the performance of the proposed method on rare objects (e.g., the rare species from the iNaturalist dataset)? It would be beneficial to see a more detailed analysis of the performance on a spectrum of categories, ranging from common to rare, to better understand the practical applicability of the method. Furthermore, it would be useful to explore the relationship between the rarity of a category and the effectiveness of the proposed data augmentation technique.

### Questions
See the weakness section.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents a data augmentation approach for few-shot image segmentation. The aim is to synthesise training samples of the novel object categories that are segmented from the few-shot samples. The approach is based on proposing three modifications to the text-to-image stable diffusion for image generation. First, the image sample generation is based on creating a bank of banks of embeddings with the proposed mask and normalising the loss related to the textual inversion (Gal et al 2022). Second, more training samples are generated in a copy-paste manner by including objects generated with stable diffusion in the available training data. Third, a few-shot segmentation (FSS) model is trained with a set of appropriate image-segmentation pairs.  The FSS model is used to find more adequate pairs and is trained again with a larger pool of samples. The approach shows reasonable performance on several standard benchmarks for few-shot segmentation.

### Strengths
+ The paper is well written and easy to follow. In addition, the related work is complete and discussed in detail. The method is also well presented. 

+ The method provides solid results for almost all evaluations.

+ The ideas proposed are easy to implement in any latent diffusion model. 

+ The paper addresses an open problem for segmentation-like tasks. It is challenging to generate scenes with pixel-level masks using diffusion models.

### Weaknesses
- (Major) The three main contributions of the paper are extensions of existing approaches. This is not a problem, but in all cases the new approach is minor. For example, the copy-paste idea is used out of the box, without any adaptation to the specific problem of few-shot segmentation. Similarly, the iterative training of the few-shot segmentation model, while useful, does not contain any particular innovation in terms of the training procedure or loss function. The paper has limited novelty in terms of algorithmic contributions.

- (Major) The lack of 1-shot results is a significant omission, as this is a standard evaluation setting in few-shot segmentation and is common in previous work.  Furthermore, a more comprehensive comparison with recent state-of-the-art approaches is needed. For example, the paper should discuss the performance differences with methods like Xu, Qianxiong, et al. "Self-Calibrated Cross Attention Network for Few-Shot Segmentation". Proceedings of the IEEE/CVF International Conference on Computer Vision. 2023. It would be useful to provide a detailed analysis of when the paper does not achieve state-of-the-art results and why, including a discussion of the limitations of the proposed approach. Overall, the results presented do not demonstrate a substantial improvement over existing methods.

- The term "synthetic distribution" is a bit confusing because it is usually associated with the generation of data from a simulator, where the underlying data generation process is known. This is not the case for the problem under consideration, where the data is generated from a diffusion model. Generated or realistic data distribution would be more appropriate to describe the nature of the data.

- The term "out-of-distribution generation" is also confusing and not well-defined. There is no clear discussion of what constitutes in-distribution information in terms of prompts or generated images. The paper may be referring to the additional image variations given a prompt as OOD, but this is not clearly stated. This usage of OOD differs significantly from the common use of the term in the context of uncertainty estimation and robustness.

### Questions
- It would be interesting to discuss whether the method is limited to latent diffusion models or generalisable to more diffusion approaches.

### Soundness
3 good

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper aims to utilize pre-trained text-to-image diffusion models for few-shot segmentation. It points out three levels of misalignments that arise when utilizing pre-trained diffusion models in segmentation tasks: 1) text prompt may not generate desired instances; 2) may fail on multi-object scenes; 3) diffusion models cannot generate segmentation masks.

To solve 1), it binds an instance specific word embedding with the given real examples. To solve 2), it combines
synthesized instances with real images to generate training samples with more realistic layouts. To solve 3), it use semi-supervised learning (Wei et al., 2022) and condition the generative process on provided novel samples.

The experiments are done on Pascal-5, COCO-20, and FSS-1000. Compared to previous methods, the proposed method achieves the SoTA.

### Strengths
The proposed method seem robust as it achieves on-par performance even if it is combined with simple fune-tuning, while other methods suffer from significant decrease in performance.

### Weaknesses
1. As few-shot segmentation might refer to semi-supervised segmentation with very few annotated examples and lots of unannotated examples in some literature, different from the setting in this paper, I suggest to state the problem setting in the very beginning of the paper.
2. If I recall correctly, using a special adjective token for a specific instance was proposed in [A], but it seems claimed as one of the contribution of this paper.
3. This paper does not clearly explain the "copy-paste" process, but simply cites another paper. An example figure would be nice. The images in Figure 2 is too dark to see clearly. If the space is not enough, I suggest to remove the introduction of diffusion models as it is becoming a common sense in this area.
4. The proposed method sounds very expensive. For every category, users need to personalize Stable Diffusion with text-inversion first, and then train the segmentor over and over again to contain the new generated masks into training set. However, the paper seems to only compare the mask generation speed. I would suggest to compare the whole process speed to benefit the community.
5. The main performance gain seems to come from combining two papers: [B] and [C], which correspond to the contribution 2) and 3) in the introduction, respectively.

### Questions
1. Related to weakness 3), does the "copy-paste" process requires post-process harmonious method? If not, how to make sure the generated image make sense to the layout? Does it harm the performance?
2. Related to 1), with only a few examples of the new instance, how to obtain multi-object layout? Does the layout include the new instance?

### Soundness
3 good

### Presentation
1 poor

### Contribution
2 fair
