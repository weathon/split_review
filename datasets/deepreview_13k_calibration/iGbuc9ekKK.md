# Duoduo CLIP: Efficient 3D Understanding with Multi-View Images

- Decision: Accept
- Avg Score: 5.75
- Scores: 6, 5, 6, 6

## Abstract
We introduce \PROJECTNAME, a model for 3D representation learning that learns shape encodings from multi-view images instead of point-clouds.
    The choice of multi-view images allows us to leverage 2D priors from off-the-shelf CLIP models to facilitate fine-tuning with 3D data. Our approach not only shows better generalization compared to existing point cloud methods, but also reduces GPU requirements and training time. In addition, \REVTEXT{the model is modified} with cross-view attention to leverage information across multiple frames of the object which further boosts performance. \REVTEXT{Notably, our model is permutation invariant to the order of multi-view images while being pose-free.} Compared to the current SOTA point cloud method that requires 480 A100 hours to train 1 billion model parameters we only require 57 A5000 hours and 87 million parameters. \REVTEXT{Multi-view images also provide more flexibility including being able to encode objects with a variable number of images, and performance scales when more views are used. In contrast, point cloud based methods require an entire scan or model of the object. We showcase this flexibility with benchmarks from images of real-world objects.} Our model also achieves better performance in more fine-grained text to shape retrieval, demonstrating better text-and-shape alignment than point cloud based models.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces Duoduo CLIP, a model for 3D representation learning that captures object shapes from multi-view images instead of point clouds. By leveraging multi-view images, the model uses 2D priors from pre-trained CLIP models to fine-tune on 3D data. The proposed cross-view attention module aggregates information across different views, and the model is both permutation-invariant and pose-free. Compared to point cloud-based methods, this multi-view approach significantly reduces GPU training requirements and demonstrates improved performance on fine-grained text-to-shape retrieval tasks.

### Strengths
1. The paper is clearly written and easy to follow. Extensive experiments are conducted for point cloud classification and text-based retrieval.

2. The proposed method achieves state-of-the-art performance on these tasks while significantly reducing computational costs.

### Weaknesses
1. The zero-shot CLIP baseline is insufficient to demonstrate the proposed model’s advantages, as the test set is specific to 3D renderings, while the original CLIP model is primarily trained on natural images. To provide a fair comparison, the authors should fine-tune the original CLIP model using the same datasets and training strategies as the proposed model, and report the results.

2. Representing 3D shapes with multi-view images is one of the most straightforward approaches and has been used in previous works, such as ULIP2, to align the feature spaces of text, image, and point cloud representations. The purpose of such works is not solely to achieve high classification performance, but to deepen understanding of raw 3D representation beyond using just images. The original CLIP model, even without fine-tuning or special design, already serves as a strong baseline. This paper focuses on multi-view representation and achieves moderate improvements in basic classification and retrieval tasks by training on large-scale images, but this is quiet straight forward and it does not introduce new ideas or insights to the field. The work would be more compelling if the authors explored capabilities *beyond* the scope of those point cloud representations, such as scene-level multi-view data, to better demonstrate the necessity and potential upper bounds of the proposed approach.

3. Have the authors investigated the effect of different view sampling strategies? Unlike point cloud representations, which capture the entire shape, multi-view representations may be influenced by both the number and sampling strategy of views. While the impact of view count is examined in the paper, it would be beneficial if the authors also explored the impact of different sampling strategies, such as front versus back views, or uniformly sampled versus randomly sampled views. The lack of analysis on view sampling strategies could lead to suboptimal performance, as certain views might be more informative than others for specific object categories.

4. Environmental lighting can significantly affect the appearance of 3D renderings by introducing shading, reflections, and slight color variations. It would be useful to conduct experiments examining how these lighting conditions impact the model’s performance. The absence of such experiments raises concerns about the model's robustness to variations in lighting, which are common in real-world scenarios. For example, the model might perform poorly under strong directional lighting or in environments with complex reflections.

5. Maybe add some more downstream tasks like image based retrieval and the concept combination as in Figure 1 of OpenShape.

### Questions
1. In Figure 6, the second row describes "a brown chair with a round back and thin metal base," but the ground truth appears to show a dark green or gray chair. It’s unclear whether this discrepancy is due to color shifts introduced during the rendering process or if it reflects a lack of quality control in the dataset.

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
5

### Summary
The paper proposes a multi-view 3D understanding model based on contrastive learning. The model is a multiview image encoder encoding variable number of input frames and output a feature vector. The model is trained by constrasting against the corresponding clip and language embeddings.

### Strengths
- The paper is well-written. The figures and well-made and easy to understand. The overall presentation is good.
- The idea is simple and easy to understand. The architecture proposed might be reused for other multiview image tasks.
- The quantitative results are pretty strong and convincing.

### Weaknesses
 - It's unclear to me why this task is important. The proposed method seems pretty incremental and I don't see a clear insights or surprising findings reviewed by the paper

 - Can the model generalize outside of the training datasets? I didn't see any in-the-wild evaluation in the paper, which I feel is necessary as a metric for evaluation.

 - Isn't it a little cyclic to use features from a frozen CLIP to train a multiview image encoder? Would the encoder benefit from some inter-view and inter-object contrastive losses? Wouldn't that allow the model to discover novel semantic and geometric information which might not have been captured by CLIP and text encoder?

 - Can the learned multiview encoder be used for 3D reconstruction?

### Questions
- Why is this an important task? What are some example applications of the proposed model? The paper seems to indicate that there are some applications in robotics. I'd like to see some examples of how the proposed technique can be used in robotic tasks and how exactly can current robotics methods can benefit from it.
- Can the model generalize outside of the training datasets? I didn't see any in-the-wild evaluation in the paper, which I feel is necessary as a metric for evaluation.
- Isn't it a little cyclic to use features from a frozen CLIP to train a multiview image encoder? Would the encoder benefit from some inter-view and inter-object contrastive losses? Wouldn't that allow the model to discover novel semantic and geometric information which might not have been captured by CLIP and text encoder?
- Can the learned multiview encoder be used for 3D reconstruction?

### Soundness
4

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
This work presents Douduo CLIP, a technique for 3D representation learning for classification and retrieval that leverages multi-view input images rather than more explicit 3D representations like point clouds or meshes. The method is simple but effective approach to fine-tuning CLIP for 3D understanding, performing CLIP-style contrastive training between multi-view image encodings (a shape representation), single image encodings and text encodings. The multi-view image encoder is initialized from CLIP and fine-tuned with self-attention across all views for some layers of the ViT encoder, while the single image and text encoders are frozen (this allows for more efficient training).

The proposed Duoduo CLIP outperforms or is competitive with point cloud-based baselines for classification on Objaverse-LVIS and MVPNet, and outperforms CLIP applied zero-shot without any tuning. There are reasonable qualitative image-based retrieval and state-of-the-art zero-shot results (no specialized training for this task) for text-based retrieval.

### Strengths
### Originality
- It is reasonable to use pre-trained CLIP encoders and fine-tune them for 3D shape understanding from multiple-views. This allows for training on more data and taking advantage of the large-scale pre-trained representation.
- Attention implemented  across multiple views of a single object is reasonable, and ablation show that it helps.
### Quality
- The investigation into the effect of replacing the point-cloud encoder with a multi-view image encoder is thorough, including analysis about training/testing time inference costs, comparisons with non-fine tuned CLIP backbones, and comparisons with baselines on image-based retrieval, text-based retrieval and classification.
### Clarity
- The paper is mostly well written and easy to follow with the exception of the experiments section, which could be improved (see comments in weaknesses).
### Significance
- For tasks like retrieval and classification it is good to know that point-cloud representations are weaker than multi-view image representations, which is the main takeaway of this work. Point cloud representations find their main applications in robotics, often in object manipulation tasks that do not only require recognition and where real-time multi-view data collection is cumbersome (see comments further comments on significance in weaknesses)

### Weaknesses
### Originality
- The main technical novelty is replacing a point cloud encoder with a multi-view CLIP image encoder, and tuning this multi-view encoder. While effective, the novelty is minor. It would also be good to understand the significance of what pre-trained representation (CLIP vs. DINO for example) is used to initialize the multi-view encoder
### Quality
- Accuracy of evaluation: Both the Objaverse LVIS and the new MVPNet use somewhat automated procedures using off-the-shelf VLMs to create the object labels. Without additional filtering the Objaverse LVIS dataset is quite noisy and this is likely the case for BLIP (what was used for MVPNet) as well. This is also the case for techniques purpose-made for captioning like Luo et al. (NeurIPS 2023). What is the significance of the findings if the ground truth labels themselves are inaccurate and might contain similar mislabeling patters as the CLIP model that is used as the pre-trained representation in this work?
### Clarity
- The flow of the writing in the experiment section can be improved, the sentences don't flow into each other, but read as consecutive lists of facts (e.g.L301-314). It's possible to understand with some effort, but a revision would greatly improve the paper.
### Significance
- Point clouds are a data modality generally used for tasks that require fine-grained object shape understanding and real-time visual feedback in robotics, like object manipulation. The present work focuses on recognition related tasks, so the significance in robotics (emphasized by the authors) is not entirely clear.

### Questions
- Clarity: What is the difference between 5F and 12F as described in the tables (e.g. two bottom rows of Table 2)? This notation is not defined, although it's possible to conclude that this might mean number of views?
- What is the effect of the choice of pre-trained backbone for the multi-view encoder? How much worse would a DINO or randomly initialized model do? It would be good to understand the effect and significance of this choice. 
- What are specific applications in robotics for which multi-view images are available in real time and where improved recognition from multi-view images would have a positive and significant impact?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces a novel method named Duoduo Clip, which addresses limitations in 3D shape representation by using multi-view images over traditional point clouds, improving adaptability and efficiency in 3D shape retrieval. Unlike previous methods constrained by point cloud limitations and high computational demands (e.g., Uni3D), Duoduo CLIP leverages multi-view images to simplify training, generalize better to unseen shapes, and reduce the need for extensive compute resources. This approach allows direct input of images, enabling seamless integration with real-world datasets (e.g., ScanNet, ScanObjectNN) and enhancing real-time applicability in robotics.

### Strengths
Here is the strength of this paper:
- The authors propose to use rendered multiview images as shape representation instead of point cloud inputs for retrieval task.
- It proposes a training strategy that requires significantly less computation resources. 
- The author claims SoTA performance in comparison with baseline models.

### Weaknesses
Here is some concerns from me:

**Major:**

- **Novelty:** While this paper proposes a more efficient approach to leverage multiview image for 3D understanding. Using multi-view (MV) attention to establish connections between multiple views for fine-tuning is not a novel idea. This limits the technical contribution. The primary innovation appears to be shifting from single-view images to multi-view images for training, which is incremental rather than groundbreaking. Also, this paper is similar with: `Yipeng Gao et al. Sculpting Holistic 3D Representation in Contrastive Language-Image-3D Pre-training CVPR2024`. Which use point cloud, multi-view image and text to conduct contrastive learning for multi-modality alignment. Author should explain about it.


- **Experiment.** I am also concerned about the potential degradation in performance on natural single-view images. The training dataset is smaller compared to the original CLIP model, and some of the data are synthetic. Although the proposed method improves performance on multi-view images, I worry that it may compromise the model’s ability to handle single-view natural images, which could negatively impact its performance in downstream applications.

**Minor:**

1.Line 80:
A citation is missing for the reference to "previous methods..."

2. There is some confusing in Figure 3:
- So why the first image all focus on the plate when multiple object are present? What is the query?
- I also question the claim that this figure demonstrates "geometric correspondences of 3D shapes." It could be interpreted as a simple classification heatmap, which does not necessarily indicate the model is aware of 3D structure.

### Questions
As posted in weakness, I hope the author could solve these concerns in the rebuttal phase.

### Soundness
3

### Presentation
3

### Contribution
2
