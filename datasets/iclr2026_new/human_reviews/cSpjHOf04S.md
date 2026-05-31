## Human Reviewer 1

### Summary
The paper introduces a novel fine-tuning approach that repurposes generative models such as Stable Diffusion and Masked Autoencoders  for category-agnostic instance segmentation. Despite being fine-tuned only on limited synthetic data (indoor furnishings and cars), these models exhibit strong zero-shot generalization, segmenting unseen object types and image styles -- often surpassing the heavily supervised Segment Anything Model.

### Strengths
- Demonstrates good performance on unseen object categories and visual domains despite fine-tuning on a very limited dataset.

- Shows that generative models (Stable Diffusion, MAE) encode transferable perceptual grouping abilities, enabling segmentation without large-scale supervision.

- Achieves competitive results to SAM with a lightweight fine-tuning procedure using fewer resources and annotated masks.

### Weaknesses
- Questionable evaluation protocols

Actually, there exists an established experimental protocol for evaluating click-based segmentation methods, that implies testing on GrabCut, Berkeley, DAVIS, SBD, PascalVOC benchmarks. E.g., SimpleClick referred in the proposed paper as a baseline, reports values obtained in this benchmark. But here, the proposed method is not tested in the same setup, instead, an entirely different experimental protocol is used. Namely, SimpleClick was trained on synthetic datasets with limited number of classes and scenarios, and tested far beyond classes used for training. In such an artificial scenario, its low accuracy, otherwise suspicious, can be indeed expected -- as well as superior performance of a generalist model. When tested in the normal evaluation protocol, SimpleClick yields decent performance, though.

- Using diffusion (and even SD!) for click-based segmentation is not novel 

This idea was exploited in the early Conditional Diffusion Network (CDNet) [1] that dates back to 2021. In CDNet, global similarity of features from clicks and potential target regions was used in a diffusion process that spreaded the predicted logits of clicks within locally connected regions. The most recent M2N2 [2] utilizes self-attention maps produced by Stable Diffusion for unsupervised and training-free approach to instance segmentation. None of these works is cited or discussed, which might make a reader to overestimate the novelty of the proposed approach. 
 
[1] Conditional Diffusion for Interactive Segmentation. Xi Chen et al. ICCV 2021.

[2] Repurposing Stable Diffusion Attention for Training-Free Unsupervised Interactive Segmentation. Markus Karmann and  Onay Urfalioglu. In CVPR 2025.

- Results are questionable

The method was evaluated against trainable SimpleClick, custom pipeline based on DINO and off-the-shelf SAM. SimpleClick were trained according to custom training procedure, which naturally inhibits concerns about whether there were properly trained -- or their potential was not unleashed due to suboptimal hyperparameters, shortened training schedule etc. DINO was again used as a part of a custom pipeline, so similar concerns are applicable. Results achieved with SD, are significantly inferior to those of SAM on medium-sized and small-sized objects in COCO, DRAM, EgoHOS and PIDRay, in other words, in almost all scenarios, which makes me doubt the practical value of the proposed approach. It seems that on real world applications, it barely could compete SAM.

### Questions
- Why not use the well known evaluation protocol for assessing quality of click (point-prompt) interactive segmentation? 

- Why not compare to pretrained SimpleClick but implement a custom training scheme on synthetic datasets?

- Why SAM and SimpleClick are selected as beaselines? I believe there are some more powerful methods that have been released since; at least SAM2, if not digging deeper [3]. 

[3] AdaptiveClick: Clicks-aware Transformer with Adaptive Focal Loss for Interactive Image Segmentation. Jiacheng Lin et al. In TNNLS, 2024.

### Soundness
2

### Presentation
3

### Contribution
2

### Rating
2

### Confidence
3

---

## Human Reviewer 2

### Summary
The paper explores how generative models pretrained for image synthesis can be repurposed for perceptual organization. By finetuning Stable Diffusion and MAE with an instance coloring loss on limited object types, the models achieve strong zero-shot generalization, segmenting unseen objects with high accuracy. Remarkably, they rival or even surpass SAM on fine structures, demonstrating that generative models inherently learn transferable object grouping mechanisms without large-scale supervision.

### Strengths
1. GenSeg demonstrates that simply finetuning generative models such as Stable Diffusion can yield strong performance in category-agnostic instance segmentation.

2. The paper is clearly written and easy to follow.

3. GenSeg achieves SAM-level performance in certain out-of-distribution segmentation scenarios.

### Weaknesses
1. The novelty of this work is limited. Previous studies [1][2][3] have already shown that generative models can exhibit open-set segmentation capabilities without task-specific training. This paper mainly extends those ideas to category-agnostic instance segmentation.

2. Methodologically, the paper lacks innovation. Finetuning generative models for segmentation is a well-established approach, and the proposed loss function is highly similar to existing techniques [4][5].

[1] Generative prompt model for weakly supervised object localization[C]//Proceedings of the IEEE/CVF International Conference on Computer Vision. 2023: 6351-6361.

[2] Diffumask: Synthesizing images with pixel-level annotations for semantic segmentation using diffusion models[C]//Proceedings of the IEEE/CVF International Conference on Computer Vision. 2023: 1206-1217.

[3] Open-vocabulary panoptic segmentation with text-to-image diffusion models[C]//Proceedings of the IEEE/CVF conference on computer vision and pattern recognition. 2023: 2955-2966.

[4] Recurrent pixel embedding for instance grouping[C]//Proceedings of the IEEE conference on computer vision and pattern recognition. 2018: 9018-9028.

[5] Efficient and accurate arbitrary-shaped text detection with pixel aggregation network[C]//Proceedings of the IEEE/CVF international conference on computer vision. 2019: 8440-8449

### Questions
The major weakness of the paper is limited novelty.

### Soundness
2

### Presentation
3

### Contribution
2

### Rating
4

### Confidence
4

---

## Human Reviewer 3

### Summary
This work demonstrates that generative models such as Stable Diffusion and Masked Autoencoders (MAE) can be fine-tuned on a small set of labeled object masks to achieve general-purpose instance segmentation.
Remarkably, the fine-tuned models exhibit strong zero-shot generalization, accurately segmenting objects of entirely unseen types and styles.
They also produce sharper boundaries and handle fine-grained structures with notable precision, behaviors that likely stem from their generative pretraining.
These results suggest that generative pretraining inherently encodes a grouping and compositional understanding of the visual world, enabling segmentation capabilities that are more generalizable and human-like across diverse domains.

### Strengths
### 1. Surprising zero-shot generalization and conceptual novelty:
It is impressive that the proposed generative models exhibit strong zero-shot generalization, accurately segmenting objects of entirely unseen types and styles.
This suggests that generative pretraining inherently encodes a grouping mechanism that transfers across categories and domains, supporting more generalizable and human-like perception.
This is arguably the first convincing demonstration of the potential of generative segmentation models to surpass traditional discriminative approaches in terms of generalization capability.

### 2. Robustness to visual perturbations:
The models show high robustness to variations in color, illumination, and texture, indicating that their segmentation ability does not rely merely on low-level visual cues.
This robustness highlights a deeper structural or semantic understanding learned through generative pretraining.

### 3. Strong qualitative performance:
Qualitative visualizations (see pages 7–9) show coherent reconstructions and smooth, well-aligned segmentation boundaries.
The results are visually compelling and provide strong evidence for the model’s superior perceptual grouping and boundary accuracy compared to discriminative baselines.

### Weaknesses
### 1. Limited performance on small objects:
As shown in Table 1, the proposed approach performs well on large objects but struggles significantly with small-object segmentation.
This limitation suggests that the model’s generative priors may bias it toward capturing dominant, large-scale structures, leaving fine-scale, small instances underrepresented.

### 2. Imprecise instance coloring and unclear mask extraction details:
The color-based instance representation occasionally produces noisy or “dirty” colors, which raises concerns about the consistency and robustness of the predicted masks.
The paper would benefit from a clearer explanation of how these colored outputs are converted into binary or instance masks, with more explicit technical detail in the Methods section.

### 3. Limited extensibility to semantic or text-guided segmentation:
Since the framework relies heavily on color-based encoding, its applicability to semantic or  text-guided segmentation appears constrained.
The authors may consider discussing how this approach could be extended to tasks requiring semantic consistency or text/image guidance, which could broaden the impact of the work in future research.

### Questions
The main concern lies in the model’s difficulty with small-object segmentation.
Generative segmentation models, while powerful, can be somewhat uncontrollable, as it is often unclear what structures or priors the model has actually learned.
This may explain why small or less prominent objects tend to be omitted in the predictions.

Could the authors elaborate on how controllability might be improved in such generative segmentation frameworks?
Additionally, what potential strategies do you envision for enhancing the detection and segmentation of small objects within this generative paradigm?

### Soundness
4

### Presentation
4

### Contribution
4

### Rating
8

### Confidence
3

---

## Human Reviewer 4

### Summary
The authors propose a method to adapt image generation models to perform instance segmentations across diverse classes including those unseen during training. Impressive improvements over strong baselines have been shown in the paper. Image generation models are adapted to output segmentation maps in a single step by training on various image segmentation datasets with novel loss functions. Ablations and analysis is also included.

### Strengths
The performance gains are good over baselines trained on the same data. The authors also test on unseen domains such as luggage X-ray images where they observe similar trends. Qualitative comparison is very helpful to understand these claims and quite impressive. The fact that the model performs so well on unseen domains makes the contribution of the novel losses and method design strong.

### Weaknesses
According to evaluation, the Stable Diffusion variant of their model is performing the best. However this a old model and it would be good to see how the performance scales when used with recent DiT based models such as SD3 and Flux.

The authors hint at part level understanding in Figure 3. It would good to perform evaluation on some part segmentation datasets [1,2] to check generalization of these models to finer granularity levels.

Training is conducted on a relatively small and limited diversity dataset. It would be good to explore the effect of expanding the dataset, eg. using SA-1B (or a subset). 


[1] Saha, O., Cheng, Z. and Maji, S., 2022, October. Improving few-shot part segmentation using coarse supervision. In European Conference on Computer Vision (pp. 283-299). Cham: Springer Nature Switzerland.

[2] Vedaldi, A., Mahendran, S., Tsogkas, S., Maji, S., Girshick, R., Kannala, J., Rahtu, E., Kokkinos, I., Blaschko, M.B., Weiss, D. and Taskar, B., 2014. Understanding objects in detail with fine-grained attributes. In Proceedings of the IEEE conference on computer vision and pattern recognition (pp. 3622-3629).

### Questions
Will the pretrained models also generalize to medical segmentation scenarios?

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
6

### Confidence
4