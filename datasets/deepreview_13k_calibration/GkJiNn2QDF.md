# FeatUp: A Model-Agnostic Framework for Features at Any Resolution

- Decision: Accept
- Avg Score: 5.00
- Scores: 6, 6, 3

## Abstract
Deep features are a cornerstone of computer vision research, capturing image semantics and enabling the community to solve downstream tasks even in the zero- or few-shot regime. However, these features often lack the spatial resolution to directly perform dense prediction tasks like segmentation and depth prediction because models aggressively pool information over large areas. In this work, we introduce FeatUp, a task- and model-agnostic framework to restore lost spatial information in deep features. We introduce two variants of FeatUp: one that guides features with high-resolution signal in a single forward pass, and one that fits an implicit model to a single image to reconstruct features at any resolution. Both approaches use a multi-view consistency loss with deep analogies to NeRFs. Our features retain their original semantics and can be swapped into existing applications to yield resolution and performance gains even without re-training. We show that FeatUp significantly outperforms other feature upsampling and image super-resolution approaches in class activation map generation, transfer learning for segmentation and depth prediction, and end-to-end training for semantic segmentation.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Deep features are usually in a low resolution due to the usage of pooling operations. This paper introduces FeatUp to restore the lost spatial information in deep features. FeatUp has two variants: one that guides features with high-resolution signal in a single forward pass, and one that fits an implicit model to a single image to reconstruct features at any resolution. Both approaches use a novel multi-view consistency loss with deep analogies to NeRFs. FeatUp outperforms other feature upsampling approaches in class activation map generation, semantic segmentation, and depth prediction.

### Strengths
This paper is well motivated and quite novel. The writing is professional and convincing. The improvement over existing approaches is solid and nontrivial. The proposed method can be used as a drop-in replacement for deep feature upsampling, which could be useful for this community if the claimed improvement can be easily obtained.

### Weaknesses
The training details of the FeatUp model when used as a drop-in replacement for existing features are missing. How do you train it? What data do you use for the training? What is the objective and loss for the training?

The experimental details in Table 1 and Table 2 are unclear, making it difficult to reproduce the results. Which networks/models and backbones are used for various downstream tasks? How do you train these models? Are all upsampling approaches evaluated under the same setting?

There are no numeric results for ablation study in this paper, and this is no ablation study in the main part. This paper has many designs and components (Eq. (1) – Eq. (8)), and it is important and necessary to evaluate each of these designs and components. Recently, ablation study is also a necessary part of computer vision papers, especially for deep learning papers. This is the biggest weakness of this paper.

Will the code be released? This is not mentioned in the paper. If the claimed improvement can be easily obtained, the code and pretrained models would be valuable to this community.

### Questions
Many details are unclear in the paper. Please see the above weaknesses.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces a method FeatUp that learns to upsample a low-resolution feature map at any-resolution. The proposed method is supervised by multiview consistency, and has two variants, one with a single forward and one fits an implicit model per image. The authors compare the method to several prior baselines for feature upsampling.

### Strengths
1. Upsampling deep feature maps of neural networks is an important research topic and has wide applications.
2. The idea of connecting feature upsampling to implicit neural representations and using multiview consistency to supervise the upsampled results is interesting and intuitive.
3. The effectiveness of the proposed method is well visualized in several figures.

### Weaknesses
1. A main goal of upsampling the feature map is to use it for tasks that requires semantic understanding and dense prediction, e.g. semantic segmentation. How does the proposed method work for more standard semantic segmentation benchmarks (for both mIoU and computation cost) and what are the main advantages of the proposed method? For example, in the context of any-resolution upsampling of feature map, Learning implicit feature alignment function for semantic segmentation (ECCV 2022) seems to be related, does the proposed method show advantages over the prior work?
2. How does the computation cost (in FLOPS) compare to prior works in main tables? Since the proposed method is a new upsampler, it would better demonstrate the advantages of the proposed method by comparing the computation cost.
3. In practice, why the reconstruction of features at any-resolution is important? Typically, the encoder takes a fixed-resolution input, the task is more likely to be fixed-resolution rather than any-resolution. If any-resolution is not the key point, can the proposed method improve over state-of-the-art semantic segmentation methods on standard benchmarks?

### Questions
Why a predicted salience map is needed in attention downsampler?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper presents a model-agnostic framework for feature upsampling. The main contribution of the framework is a multi-view cycle consistency loss where low-res features are matched to its upsampled and downsampled ones. Two instantiations are presented. One is inspired by joint bilateral upsampling, and a fast CUDA implementation is provided. The other is inspired by NeRF where upsampled features are optimized per image. The authors have demonstrated good visualizations of the upsampled feature maps and show that the presented upsampling framework can preserve good semantic smoothness and boundary sharpness. The effectiveness of the framework is validated on a number of tasks.

### Strengths
+ Developing general-purpose feature upsampling operators is a recent emerging topic. The goal of designing model-agnostic framework is interesting and shows significantly better visualizations in terms of feature quality over prior art.
+ As far as I can tell, viewing feature upsampling as a rendering problem from multiple low-res views is novel.

### Weaknesses
While I generally like the idea of the cycle-consistent training, I have a number of major concerns on the specific operators used/proposed and the results presented.
- **The focus of the paper seems unclear**. Being a feature upsampling framework, the framework should be agnostic to the specific downsampling or upsampling operator chosen. Yet, the current approach leaves me an impression that the framework only works on the proposed learned downsamplers and upsamplers. If the framework matters, some additional existing downsampler-upsampler pairs should be demonstrated to demonstrate its generality; If the proposed operators matter, the contributions and the title may need to be revised.

- Following my previous comment, I think the problem is that the authors attempt to combine many seemingly related techniques together. For instance, the JBU and its fast CUDA implementation look standalone to me. It is unclear to me what the role of the JBU is in the framework, particularly when it is claimed as a contribution. Please explain why JBU is essential to the FeatUp framework. In addition, applying JBU to feature upsampling is not new. "Fast End to End Trainable Guided Filter" CVPR18 and "Superpixel Convolutional Networks using Bilateral Inceptions" ECCV16 are two example works, which is also missing in the related work.

- **The ablation study of the paper is poor**. It is unclear to me what exactly leads to the good feature quality. Aside from the loss, there are a number of tricky designs in the downsampler and upsampler used. For example, why a blur kernel must be used in downsampling? And why introducing the saliency map and how it works? Why a simple 1x1 convolution is sufficient to present the saliency map? Would it be precise enough? Also, the implicit FeatUp produces significantly better visualizations according to Fig. 5. Is it because of the per-image optimization. A thorough ablation study is required.

- **The method may be justified in an inappropriate setting**. According to Table 1, FeatUp (Implicit) has reported significant performance improvements on the transfer learning setting. Yet, this setting is rarely used in feature upsampling literature. Why choosing this setting? I wonder how the parameters of comparing upsamplers are updated in this setting. In addition, the comparison between the implicit variant and other upsamplers seems unfair, because other upsamplers do not optimize the per-image upsampling quality. This also leads to the next issue.

- **The practicality of the implicit FeatUp seems poor**. In reality, the per-image optimization of upsampling is unrealistic, it is not likely that the implicit variant is used as a plug-in in existing networks (the experimental setting in Table 2 also confirms my opinion). But I think this approach can somehow indicate an upper bound of upsampling quality.

- The performance of baseline approaches does not align with the number reported in the corresponding papers and is significantly lower. For example, SAPA reports 44.4 mIoU but the table in Table 2 only reports 41.6. Please check.

### Questions
Please see the weaknesses for my major concerns. I have also some other suggestions:

Is it appropriate to indicate augmented low-res features as different views? In 3D, different views often imply different view points.

In addition, the organization of related work does not make sense to me. 
- First, the paper does not conduct experiments on image super-resolution. This sub-section seems redundant. 
- Second, the references in general-purpose feature upsampling are weird. Both Amir et al. (2021) and Tumanyan et al. (2022) do not study feature upsampling at all. Why are the two papers cited? In my opinion, most references discussed in the section of image-adaptive feature upsampling should be discussed in this section. As far as I know, CARAFE is one of the first paper studying general-purpose feature upsampling. 
- In addition, some closely related approaches compared in experiments are not discussed/compared in related work such as FADE and SAPA.

Please address my major concerns in the rebuttal. I would re-evaluaute the paper conditioned on the response.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
