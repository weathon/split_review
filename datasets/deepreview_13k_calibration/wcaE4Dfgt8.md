# Uni3D: Exploring Unified 3D Representation at Scale

- Decision: Accept
- Avg Score: 7.33
- Scores: 8, 8, 6

## Abstract
Scaling up representations for images or text has been extensively investigated in the past few years and has led to revolutions in learning vision and language.
However, scalable representation for 3D objects and scenes is relatively unexplored.
In this work, we present \Ours, a 3D foundation model to explore the unified 3D representation at scale.
\Ours uses a 2D initialized ViT end-to-end pretrained to align the 3D point cloud features with the image-text aligned features.
Via the simple architecture and pretext task, \Ours can leverage abundant 2D pretrained models as initialization and image-text aligned models as the target, unlocking the great potential of 2D models and scaling-up strategies to the 3D world.
We efficiently scale up \Ours to one billion parameters, and set new records on a broad range of 3D tasks, such as zero-shot classification, few-shot classification, open-world understanding and part segmentation. 
We show that the strong \Ours representation also enables applications such as 3D painting and retrieval in the wild.
We believe that \Ours provides a new direction for exploring both scaling up and efficiency of the representation in 3D domain.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
**Note: this is an emergency review**

This paper proposes Uni3D, a 3D point cloud foundation model for open-world understanding that achieves state-of-the-art performance on zero-shot shape classification. The Uni3D architecture, drawing inspirations from the scalability of ViT, is composed of a network that encodes local point cloud patches into features, akin to the image patch features in ViT. Subsequently, the transformer layers of ViT process these patch features and output a final global feature. These transformers can be loaded from pretrained 2D visual encoders such as the ones in DINO or EVA-CLIP. Besides demonstrating the superior open-world performance of Uni3D, the authors also showcase applications such as point cloud painting and cross-modal retrieval.

### Strengths
- The paper is generally well-written. 
- Authors plan to release all the code and pretrained models, which will greatly facilitate future research efforts.
- The proposed ViT-like architecture is intuitive and well-motivated. The architecture also achieves quite a significant performance gain over existing models in e.g., OpenShape.

### Weaknesses
 - Further exploration and analysis of Uni3D's behaviors could provide additional insights and understanding. Please refer to the "Questions" section below for more details.
- (New concern on Nov 22) Prior works like OpenShape have been trained on a much smaller batch size than Uni3D (OpenShape is trained using a batch size of 200 on a single A100-80G, while Uni3D is trained using a batch size of 1152 on 24x A100-40G). My question is, if authors train Uni3D using the same batch size as OpenShape, or train OpenShape using the same batch size as Uni3D, does Uni3D still outperform OpenShape (when both models have similar numbers of parameters)? This experiment will reveal whether the better training setting or the proposed architecture plays a bigger role in the superior performance of Uni3D. Though, regardless of the final findings from this experiment, it won't affect my positive view of the paper.

### Questions
- It would be helpful to include a comparison of the inference speed of Uni3D compared to prior work on open-world 3D understanding.
- The main source of performance gains of Uni3D over existing work seems to come from the proposed architecture, instead of how the architecture is initialized (according to authors' reply to Reviewer 1Xtq, whether to initialize the architecture from pretrained ViT only leads to about 1% performance difference). This observation might be attributed to the extensive size of the pretraining dataset, which encompasses 1 million 3D shapes. This raises a question: If a smaller pretraining dataset were used, would initializing with a pretrained ViT have a more significant impact on open-world generalization?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces a 3D foundation model, dubbed Uni3D, which uses a 3D point tokenizer and ViT to align 3D features with CLIP features (images and texts). Uni3D is trained with the triplet contrastive loss OpenShape used. By scaling up the model size of ViT as a point encoder to a billion-scale, Uni3D shows impressive performance on zero-shot and few-shot 3D perception tasks including classification and semantic segmentation. Although the experiment results are impressive, the technical novelty of the proposed is limited, and a few analyses (as described in the weakness section) seem necessary to strengthen the paper.

### Strengths
[Method] Training a 3D foundation model is a timely topic and the proposed method Uni3D showed impressive results on various benchmarks.

[Experiments] The paper provides not only common benchmarks for open-world understanding but also interesting analysis (e.g., point cloud painting). Especially, the point cloud coloring analysis shows that the trained 3D encoder can encode the color of a 3D point cloud, which is aligned with text features.

[Detailed explanation] The paper provides implementation details to help readers understand the proposed method well. For example, I could understand that Uni3D used a PointNet++-based upsampling strategy from the details related to part segmentation experiments, as shown in the Appendix.

### Weaknesses
[Novelty] The proposed method mainly follows the previous work, OpenShape, in terms of the training data construction (Sec 3.2) and the training objective (Eq. (1)). From my understanding, the only difference is that Uni3D uses PointBERT’s 3D tokenizer + ViT as a 3D encoder while OpenShape uses PointBERT. Although OpenShape is still in arXiv, I recommend the authors clarify what differentiates Uni3D from OpenShape since OpenShape is the most relevant baseline and high similarity to this work.

[Experiments] Although the paper provides text-to-3D retrieval and image-to-3D retrieval, I think 3D-to-text (captioning) and 3D-to-image (generation) experiments need to be included in the paper to show the good alignment of 3D, image, and text. The absence of these experiments limits the evaluation of the model's ability to generate content in other modalities, which is crucial for a foundation model.

[Analysis] As shown in Figure 1, scaling up OpenShape does not improve its zero-shot accuracy, unlike Uni3D. Why can Uni3D have such consistent improvement while it has a similar architecture to OpenShape? Does this improvement come from the initialization of the large pre-trained 2D ViT? I recommend the authors provide an analysis of this to make the paper stronger. Furthermore, the paper lacks a detailed analysis of the impact of different components of the 3D encoder, such as the point tokenizer and the ViT architecture, on the overall performance. It would be beneficial to understand how each component contributes to the final results.

### Questions
Please refer to the weakness section.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents Uni3D, a general 3D foundation model to explore the "unified" 3D representation at scale. Given the point cloud at input, it uses a 2D initialized ViT to align 3D / 2D features. It scales up to 1B (which is very large for 3D tasks) and achieves good performance on a broad range of tasks.

### Strengths
+ Simple and effective structure to scale up the model capacity to 1B. This is very impressive in the 3D point cloud domain.

+ Good performance in a wide span of tasks with detailed experimental results.

### Weaknesses
 - The exact insight as to why the proposed method succeeds in 3D domain is not fully stated or analyzed. Please see the questions below.

 - The successful scaling up to 1B parameters is a very key contribution from this work. It works well on multiple downstream tasks. Does the gain come from the 2D pretrained models? Table 7 seems to give some ablations and yet this is not clearly stated in the introduction. I was wondering this since it would tell people whether to focus more on 2D data/pretraining to resolve 3D problems, or 3D pretraining is essential. If I am getting this right, using none 2D initialized weights as shown in Table 7, the gain is not too much obvious (44.8 vs 45.8).

 - Uni3D is verified on a wide variety of tasks and benchmarks. This is motivating. Do you plan to try some challenging and realistic settings, eg. autonomous driving settings with point clouds? That would strength the proposed approach to great extent.

 - The last row in Table 1 shows the result of models separately trained on each benchmark. The unified approach of Uni3D is on par with them, demonstrating the generalization or universality. Does Uni3D potentially could surpass the performance of the model trained each on one particular benchmark? I was wondering the nessecity of training a universal model.

--- 
Minor:
- Typo in Figure 1, "ensambled"

### Questions
1. The successful scaling up to 1B parameters is a very key contribution from this work. It works well on multiple downstream tasks. Does the gain come from the 2D pretrained models? Table 7 seems to give some ablations and yet this is not clearly stated in the introduction. I was wondering this since it would tell people whether to focus more on 2D data/pretraining to resolve 3D problems, or 3D pretraining is essential. If I am getting this right, using none 2D initialized weights as shown in Table 7, the gain is not too much obvious (44.8 vs 45.8).

2. Uni3D is verified on a wide variety of tasks and benchmarks. This is motivating. Do you plan to try some challenging and realistic settings, eg. autonomous driving settings with point clouds? That would strength the proposed approach to great extent.

3. The last row in Table 1 shows the result of models separately trained on each benchmark. The unified approach of Uni3D is on par with them, demonstrating the generalization or universality. Does Uni3D potentially could surpass the performance of the model trained each on one particular benchmark? I was wondering the nessecity of training a universal model.

---
Minor:
- Typo in Figure 1, "ensambled"

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
