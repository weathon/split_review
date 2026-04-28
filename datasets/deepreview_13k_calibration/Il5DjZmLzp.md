# Foundation Vision Models are Unsupervised Image Canonicalizers

- Decision: Reject
- Avg Score: 4.50
- Scores: 3, 6, 6, 3

## Abstract
One of the most significant and longstanding problems in computer vision is invariance - the ability to robustly handle changes in real-world transformations such as rotation, viewpoint, and lighting. Unfortunately, popular foundation models remain brittle under such transformations. While existing solutions towards invariance have shown promise, they all fundamentally require some model training, limiting their ability to adapt broadly to new tasks, transformations, and datasets. Our key insight is that foundation model priors can be used to reason about transformations. We thus propose Foundation Model Canonicalization (FMC), an approach that can undo nuisance transformations in images without any model training. With a single core approach, FMC can make models like CLIP and SAM invariant to different transformations without any training or fine-tuning. Our approach FMC flexibly adapts to new foundation models and tasks, making it significantly easier for newer and larger models to achieve invariance.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper propose a training-free adaptation approach for vision foundation models, e.g. CLIP and SAM, to adapt on unseen 2D image rotation. They conduct experiments on small datasets e.g. CIFAR and STL10 with C4/C8 rotations. Results show some improvement vs baseline w/o such adaptation.

### Strengths
Improvement for robustness of foundation models are useful.  Training free adaptation reduce the limitation of usage of those adaptation.

### Weaknesses
In the abstract the author talk about rotation, viewpoint, and lighting. However, in the experiment, they only conduct on 2D image rotation.  The 2D in-plane rotation is far too simple, and easy to solve. One can easy train a additional small estimation via self-supervision (data augmentation in training). Or use some existing approach to detect the rotation first [1]. Unless the author can show some results also for other type of perturbation, otherwise, it is hard to convince me the effectiveness of the approach. Additionally, CIFAR10 and STL10 is consider too small and far from realworld usage, I would command the author to conduct more experiment on larger dataset.

### Questions
See weakness

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper studies to what extent large pre-trained models can be used to canonicalize images with respect to transformations such as rotation and lighting. The proposed approach is to define an energy $E(I)$ for every image $I$ by combining pre-trained CLIP, stable diffusion and SAM and to use brute-force search or bayesian optimization to find the transformation $t$ that minimizes $E(t(I))$. The finding is that this works quite well, i.e. that the proposed energy can be used to canonize images to get improved downstream performance.

### Strengths
1. The approach is simple and novel.
2. The paper demonstrates that CLIP, Stable diffusion and SAM (at least when combined) have a strong knowledge of the distribution of internet images under common image transformations.

### Weaknesses
1. The approach needs to apply three large pre-trained models (including 500 steps of stable diffusion) to many transformations of the input image. It must be quite computationally expensive, but this is not commented on.
2. There is no comparison to test-time-augmentation, which would be the most common approach to get invariance/equivariance from a non-invariant/equivariant model. Since the proposed approach requires evaluating pre-trained models on several input transformations it seems not to have a computational advantage over test-time-augmentation, which previous work on canonicalization might have had.
3. The approach is claimed to be training-free, but the energy hyperparameters need to be tuned using bayesian optimization (Appendix A.3).

### Questions
1. How large is the computational cost? In particular compared to using test-time-augmentation.
2. Is the performance better than using test-time-augmentation?
3. How computationally expensive is the tuning of the energy hyperparameters?
4. What is the typical number of transformations used to find the canonical one? How much does the performance improve for, say, each doubling of the number of transformations?
5. What is the advantage of the proposed approach over using the downstream model for the task at hand for canonicalization? For instance, in image classification, the classification model itself could be used to define an energy similar to the CLIP-energy. (This, again, would be a sort of test-time-augmentation.)

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
FMC introduces a training-free approach to equip foundation models, like CLIP and SAM, with canonicalization-based invariance, enhancing their adaptability across various models and a wide range of downstream transformations.

### Strengths
1. This energy function-based training-free method is technically sound and novel. 
2. The experiments are convincing and sufficient, validating the proposed methods across multiple dimensions, such as datasets (Sec. 5.1), models (Sec. 5.2), and transforms (Sec. 5.3).
3. The paper is well-motivated (a training-free general-invariance method) and easy to understand.

### Weaknesses
Please see the "Questions" section.

For Takeaway #9,

1. The performance gains in Fig. 6 (a) and Fig. 6 (c) are not monotonous and I would like to see more analysis regarding it. 

2.  Zero123 is trained on Objaverse, how about the performance comparison on other datasets, such as OmniObject3D [1] and Co3D.

3.  How about changing the Zero123 baseline to the advanced image-to-3D methods, like One-2-3-45 [2] and Unique3D [3].

### Questions
For Takeaway #9, 

1. The performance gains in Fig. 6 (a) and Fig. 6 (c) are not monotonous and I would like to see more analysis regarding it. 

2.  Zero123 is trained on Objaverse, how about the performance comparison on other datasets, such as OmniObject3D [1] and Co3D.

3.  How about changing the Zero123 baseline to the advanced image-to-3D methods, like One-2-3-45 [2] and Unique3D [3].

[1] OmniObject3D: Large-Vocabulary 3D Object Dataset for Realistic Perception, Reconstruction and Generation. CVPR 2023

[2] One-2-3-45: Any Single Image to 3D Mesh in 45 Seconds without Per-Shape Optimization. NeurIPS 2024

[3] Unique3D: High-Quality and Efficient 3D Mesh Generation from a Single Image. NeurIPS 2024

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes a training-free method for image canonicalization based on pre-trained foundation models. The method is based on the hypothesis that the canonical image will have the minimal energy evaluated using the foundation models. The authors permute the possible augmentation and use the proposed method to evaluate their energy.

### Strengths
- This paper proposes a training-free method for image canonicalization using pre-trained foundation model, which is interesting.
- The paper is easy to follow and the idea is easy to understand.

### Weaknesses
 - This method formulates the image canonicalization problem as an optimization problem, which needs to permutes all possible augmentation/transformation, which is slow and is sample-inefficient.
- Moreover, the method is dependent on human-designed transformations, e.g. color, viewpoint, rotation, etc. It may have limited potential to generalize real-world transformation that are actually very complex.
- No reason or intuition on why picking the mentioned three vision foundation models. Why using them, not other foundation models?
- No ablation on figuring out which foundation model is useful for recovering which transformation. And no ablation on whether it is necessary to use all three foundation models.
- Besides, I am actually not sure whether this method can generalize to any vision foundation models. For example, DINO/DINOv2, which uses contrastive learning for representation learning might not suitable for this task, as they might not be sensitive to transformations/augmentations.
- The authors should provide a deeper understanding on how to choose these foundation models and how to balance the energy they contribute to the final energy function.

### Questions
Please see comments above.

### Soundness
2

### Presentation
3

### Contribution
2
