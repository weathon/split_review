# Depth-Guided Self-Supervised Learning: Seeing the World in 3D

- Decision: Reject
- Avg Score: 3.67
- Scores: 3, 3, 5

## Abstract
Self-Supervised Learning (SSL) methods operate on unlabeled data to learn robust representations useful for downstream tasks. Most SSL methods rely on augmentations obtained by transforming the 2D image pixel map. These augmentations ignore the fact that biological vision takes place in an immersive three-dimensional, temporally contiguous environment, and that low-level biological vision relies heavily on depth cues. Using a signal provided by a pretrained state-of-the-art monocular RGB-to-depth model (the Depth Prediction Transformer, Ranftl et al., 2021), we explore two distinct approaches to incorporating depth signals into the SSL framework. First, we evaluate self-supervised learning using an RGB+depth input representation. Second, we use the depth signal to generate novel views from slightly different camera positions, thereby producing a 3D augmentation for self-supervised learning. We also examine the combination of the two approaches. We evaluate the approaches on three different SSL methods---BYOL, SimSiam, and SwAV---using ImageNette (10 class subset of ImageNet), ImageNet-100 and ImageNet-1k datasets. We find that both approaches to incorporating depth signals improve the robustness and generalization of the baseline SSL methods, and the two approaches are complementary because the combination of depth and 3D views performs the best in most settings.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper provides a new representation learning method that utilizes an estimated depth map to learn a geometry-aware representation.
As mentioned in the abstract, the goal of SSL is to learn useful representation for "downstream tasks."
However, the scale of the conducted experiments is insufficient to claim the effectiveness of the proposed method. 
1) The proposed method is evaluated only in small-scale datasets (e.g., ImageNet-100, ImageNet-1k).
2) The proposed method is evaluated only in small-scale models (e.g., ResNet-18, 50). 
3) The proposed method is evaluated only in a classification task.

The proposed method must need to show its effectiveness and scalability in large-scale datasets, various backbone models (e.g., CNN, Transformer variant models), and diverse downstream tasks (e.g., 2D/3D detection, 2D/3D segmentation, 3D reconstruction, 3D view generation, etc)

### Strengths
This paper provides a new representation learning method that utilizes an estimated depth map to learn a geometry-aware representation.
To train an RGB-D backbone network, the method generates 3D views with an image and estimated depth map and utilizes them with the previous SSL method.

### Weaknesses
 [Quality & Significance]
As mentioned in the abstract, the goal of SSL is to learn useful representation for "downstream tasks."
However, the scale of the conducted experiments is insufficient to claim the effectiveness of the proposed method. 
1) The proposed method is evaluated only in small-scale datasets (e.g., ImageNet-100, ImageNet-1k).
2) The proposed method is evaluated only in small-scale models (e.g., ResNet-18, 50). 
3) The proposed method is evaluated only in a classification task.

The proposed method must need to show its effectiveness and scalability in large-scale datasets, various backbone models (e.g., CNN, Transformer variant models), and diverse downstream tasks (e.g., 2D/3D detection, 2D/3D segmentation, 3D reconstruction, 3D view generation, etc)

[Clarity]
I recommend the authors to narrow down the scope of the proposed method from general SSL to a specific SSL method.
The current backbone tasks RGB-Depth image as inputs, so targeting downstream tasks for RGB-D inputs (e.g., RGB-D segmentation, 3D recon, 3D view synthesis, human pose estimation) is a more reasonable choice to claim the effectiveness of the proposed method.
The current claim is too general and insufficient to support the claim.

### Questions
Please see the weakness part.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work proposes to incorporate depth signals into the self-supervised learning (SSL) framework. Specifically, two baselines are provided: the first baseline directly concatenates RGB and depth signals as the input of SSL, and the second baseline augments novel view generated according to the depth signal for SSL.

### Strengths
1. This work investigate the influence of including depth signals into the SSL framework.
2. The experiments show that with the introduction of depth signals, the existing SOTA SSL methods yield a better performance.

### Weaknesses
1. Using depth signals as augmentation is not new in SSL. Previous works, e.g., DepthContrast, have explored it thouroughly.
2. The proposed method lacks generalizbility. Though it can be adopted to any SSL frameworks, the adopted depth estimation model is supervised trained on several datasets. The performance of depth estimation can not gurantee in scenarios that have a huge domain gap compared to the trained datasets. 
3. Also, due to the utilization of the supervised depth-estimation model, it is questionable to claim the proposed method as a SSL framework.
4. Experiments are all conducted on the subset of Imagenet or the modification of Imagenet. Results on more datasets are expected.

### Questions
Please see Weaknesses.

### Soundness
2 fair

### Presentation
2 fair

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
This paper proposes a new self-supervised representation learning approach (SSL) incorporating novel view synthesis data augmentation and estimated depth maps as input. DPT and AdaMPI are used for depth and novel view synthesis estimation. By incorporating depths and novel views during training the authors found their method more accurate when learning from few data and more robust to noisy test inputs. The authors claim this is the first method to use estimated depth as inputs for self-supervised representation learning.

### Strengths
1. Biologically inspired and a corresponding well-written introduction.

2. Good correlation with biological elements in the visual system.

3. Interesting reasoning on why novel views should improve SSL: As the mutual information between depth and input images is high, the effect of depth is negligible on an infinite dataset. However, novel 3D views introduce new information.

4. Simple and clear method, seems reproducible.

5. Clear ablation studies.

### Weaknesses
1. Figure 1 lacks details. For instance, it is unclear what "2D  augmentation" is being performed in PixDepth. It would also be good to visually represent your SSL objective.

3. Depth is dropped from the input to encourage the network to not over-rely on it. However, depth is used to compute the error metrics in the results table. In this case, the comparison could be considered unfair, as the previous methods do not have depth as input. As depth is obtained from a supervised network, this method is not a pure SSL method.

3. Most improvements come from adding the depth channel, which I could not consider an important contribution.

4. What is the reason behind the statement of improvements of SwAV in Table 1 when no results for SwAV are provided?

5. For the results on imagenet-100 no improvement is achieved, it is actually the opposite. This is not clearly reflected in the text in a tricky way. Why are there no results with the combination method (depth + 3D)?

6. I am afraid that the added robustness to corruptions in ImageNet-C and ImageNet-3DCC comes from the robustness of the depth estimation network (trained with depth GTs over a considerable amount of data).

2. Some minor typos: "a approach", "an conceptually",

### Questions
1. Don't you think this is too casual language "we take seriously two insights" ?

2. Clear metrics comparing against SOTA would be helpful in the introduction.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
