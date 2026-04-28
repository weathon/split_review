# View-Independent 3D Feature Distillation with Object-Centric Priors

- Decision: Reject
- Avg Score: 5.25
- Scores: 6, 5, 5, 5

## Abstract
Grounding natural language to the physical world is a ubiquitous topic with a wide
range of applications in computer vision and robotics. Recently, 2D vision-language
models such as CLIP have been widely popularized, due to their impressive capa-
bilities for open-vocabulary grounding in 2D images. Subsequent works aim to
elevate 2D CLIP features to 3D via feature distillation, but either learn neural fields
that are scene-specific and hence lack generalization, or focus on indoor room
scan data that require access to multiple camera views, which is not practical in
robot manipulation scenarios. Additionally, related methods typically fuse features
at pixel-level and assume that all camera views are equally informative. In this
work, we show that this approach leads to sub-optimal 3D features, both in terms
of grounding accuracy, as well as segmentation crispness. To alleviate this, we
propose a multi-view feature fusion strategy that employs object-centric priors to
eliminate uninformative views based on semantic information, and fuse features
at object-level via instance segmentation masks. To distill our object-centric 3D
features, we generate a large-scale synthetic multi-view dataset of cluttered tabletop
scenes, spawning 15k scenes from over 3300 unique object instances, which we
make publicly available. We show that our method reconstructs 3D CLIP features
with improved grounding capacity and spatial consistency, while doing so from
single-view RGB-D, thus departing from the assumption of multiple camera views
at test time. Finally, we show that our approach can generalize to novel tabletop
domains and be re-purposed for 3D instance segmentation without fine-tuning, and
demonstrate its utility for language-guided robotic grasping in clutter.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes a novel method for 2D->3D feature distillation using point cloud encoder, but focus on the multi-view fusion strategy. In particular, the paper is centered around the distillation of pretrained 2D CLIP models into 3D encoder, dubbed DROP-CLIP. Compared to existing multi-view fusion and per-scene optimization method, the proposed method does not require expensive optimization, and work with as few as a single RGB-D view. To facilitate the training of DROP-CLIP, the paper also uses blender to construct a large synthetic dataset termed MV-TOD for training the 3D encoder. Experiments show significant improvement of segmentation results on the MV-TOD dataset over existing baselines (OpenScene and OpenMask3D).

### Strengths
- **Technical contributions.** The paper proposes a series of techniques and datasets that are well-justified. To start with, viewpoint uncertainty is an important factor in 2D->3D distillation. Many existing methods suffer from inaccurate predictions caused by such uncertainty. The paper not only proposes a method to address this, but proposes an object-centric dataset that attempts to eliminate the bias of room-scale datasets. The individual components are also well-ablated in Tab. 2.
- **Good ablation and motivating applications.** The experiment sections ablate individual components well and show improvement over existing baselines on the proposed MV-TOD dataset. Though more real-world data experiments would be appreciated, the experiments seem to justify each component to some extent.

### Weaknesses
 - **Unclear performance on real-world data.** Though the paper demonstrates that DROP-CLIP outperforms recent methods (OpenScene and OpenMask3D), the results were obtained on the synthetic MV-TOD dataset. For the experiments with real-world data in Tab. 4, the paper compares with relatively outdated methods. So the improvement of DROP-CLIP on real-world data seems a bit inconclusive. Furthermore, the comparison in Table 4 is limited to single-view 2D segmentation methods, which does not fully validate the 3D feature distillation capabilities of the proposed method on real-world data. A comparison with more recent 2D zero-shot segmentation methods, such as GroundedSAM, would be beneficial to better highlight the contributions.
- **Efficiency is unreported.** The paper provides a motivating application that uses DROP-CLIP for robotics grasping, which is good. However, efficiency is crucial for robotics applications. The paper is unclear as to whether the proposed method is real-time. It would be important to report the inference time for generating the 3D feature clouds, especially considering the multi-view fusion step.
- **Unclear pipeline.** The paper does not seem to have a figure that shows how all components are connected. For example, L240-L242 mentions that sets of 2D segmentation masks are used. However, the method overview figure does not show how 2D masks are integrated, and there does not seem to be a description of how these masks are obtained (especially for real data) in the main paper. The lack of a clear pipeline diagram makes it difficult to understand the overall data flow and the role of each component.
- **Justification of the dataset contribution.** In the introduction, the paper discusses the necessity of constructing the MV-TOD dataset from synthetic data by comparing it to an existing room-level dataset. However, there is no quantitative evidence to support this. For example, how would the proposed component work if it is trained on an existing dataset and evaluated on the proposed dataset? Would joint-training improve the overall performance? The paper needs to provide more concrete evidence to justify the necessity and contribution of the proposed dataset.
- **Discussion of related work.** The paper compares with several 2D->3D distillation methods. However, there are several more recent methods that are closely related to the paper. Specifically, [A] and [B] also distill 3D features, and [B] also uses 2D input masks to improve 3D segmentation results. Citing and providing differentiation with these work would benefit the presentation.

### Questions
Reflecting on weaknesses above, my questions are

- Is it possible to include additional experiments on real-world data?
- What is the efficiency of the proposed method?
- Can the figures be improved to be more informative?
- Is it possible to do joint training on both MV-TOD and some other datasets to show possible improvement? If not, why?
- Discussion of related work.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a method for fusing 2D semantic features from foundation models into 3D representations, applying this approach to downstream tasks in robotics, such as manipulation. The focus is on leveraging information across different views to maximize useful insights, while also addressing the fusion of priors in an object-centric manner. Additionally, the paper introduces a new dataset designed to tackle the challenges posed by cluttered scenes in real-world environments.

### Strengths
Two areas that are less well addressed in the literature include:

Semantics-informed View Selection: This approach utilizes an informative matrix to balance information across different views while accounting for uncertainty.

Object-wise Fusion and Features: The emphasis on object-centric features is potential to enhance generalization in complex scenes.

Table 1 provides an informative summary of the datasets.

### Weaknesses
My primary concern lies in the fact that feature distillation has been a popular topic in recent research, making it difficult to identify the paper's key contributions in this context. While the dataset is certainly valuable for the community, the fundamental challenge of achieving multi-view consistency when fusing 2D features into 3D representations remains a critical issue that the paper does not fully address. Specifically, the method relies on a point cloud encoder trained on synthetic data, which raises concerns about its generalization to real-world scenarios, especially given the variability in object geometry and semantics. The object-centric prior, while motivated, is implemented through simple instance segmentation and independent feature fusion, lacking a more sophisticated prior distribution such as those derived from pre-trained text-to-3D models. Furthermore, the semantic informativeness metric, while incorporating text data, does not fully leverage the potential of large language models for richer object priors. The robotics experiments presented are interesting; however, they do not effectively demonstrate the performance of the proposed method. The research presented in this paper only finds the parts of interested objects. As noted in the discussion, the current manipulation pipeline appears to be limited to a two-stage open-loop demonstration.

### Questions
How can we ensure that the fused 3D features are consistent across multiple views?

### Soundness
2

### Presentation
2

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
This paper proposes a multi-view feature fusion strategy that employs object-centric priors to eliminate uninformative views based on semantic information, and fuse features at object-level via instance segmentation masks.

### Strengths
1. This paper addresses the issue of sub-optimal 3D feature distillation resulting from the assumption that all camera views are equally informative and presents view-independent feature distillation, allowing the extraction of 3D open-vocabulary features from a single view. 
2. This paper proposes DROP-CLIP, which utilizes an object-centric prior for weighted multi-view feature re-projection, enhancing the accuracy of feature extraction. 
3. A new dataset MV-TOD has been collected, which includes detailed 3D masks and 6DoF grasp pose annotations specifically designed for table-top scenes.
4. Experimental results validate the effectiveness, generalization and applicability of the proposed methods.

### Weaknesses
1. My main concern is the **novelty** of the proposed method. As far as the reviewer knows, the authors just replace the pixel-level features by object-level features through cropping the images. It seems that the contributions are mostly on the dataset and downstream applications, which is not enough for this venue. The core idea of using instance segmentation masks to isolate object features for multi-view fusion lacks significant novelty, as this is a relatively straightforward application of existing techniques. The paper does not present a novel theoretical framework or a fundamentally new approach to feature fusion; rather, it applies existing techniques to a new dataset.
2. It is beneficial to provide some comparisons with **more baselines** like sparsedff[1] or d3field[2]. The lack of comparison with these specific methods, which also address feature distillation without relying on NeRFs, makes it difficult to assess the relative performance and advantages of the proposed approach. These methods utilize depth information for feature projection and point pruning, which are relevant to the current work and should be included for a comprehensive evaluation.
3. The dataset was constructed in a simulated environment (Blender). Its **impact on real-world scenarios** is unknown. I suggest the authors provide clarification or experiments to demonstrate its generalization ability in real-world scenarios. The reliance on a synthetic dataset raises concerns about the practical applicability of the proposed method. The domain gap between simulated and real-world data could significantly affect the performance of the model, and the paper lacks sufficient evidence to demonstrate its robustness to such variations.

### Questions
1. The symbols in the paper are poorly represented. I suggest the author to simplify these symbols and remove some meaningless ones.
2. Some of the fonts in the tables and figures are too small to recognize, like Tab.1, Fig.2, Fig.3.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper addresses the limitations of 3D feature distillation in previous methods, which assumed all camera views are equally informative. To tackle this, it introduces MV-TOD, a synthetic dataset with detailed 3D masks and 6DoF grasp pose annotations for tabletop scenes. The paper then proposes DROP-CLIP, a method that employs object-centric priors for weighted multi-view feature re-projection. Additionally, to simplify the application for robotics, it introduces view-independent feature distillation, enabling the extraction of 3D open-vocabulary features from a single view. Experimental results demonstrate the method's effectiveness, including its utility in language-guided (open-vocabulary) robotic grasping.

### Strengths
1. The method demonstrates strong results in CLIP/DINO feature distillation and performs well on object-level segmentation.
2. The experiments are comprehensive, with sufficient ablation studies provided.
3. The paper is well-written and clearly communicates its ideas.

### Weaknesses
1. A broader set of baselines should be included in experiments, such as LERF [1], D3Field [2], and Semantic Gaussians [3]. The comparison in the updated submission is still not entirely fair, as the proposed method leverages RGBD input, while some baselines use only RGB. Specifically, the feature distillation part of GaussianGrasper, which also uses RGBD, should be included as a more appropriate baseline.
2. The MV-TOD dataset, while useful, is synthetic and introduces a sim-to-real gap when using modified CLIP/DINO for dense feature extraction, which limits its impact. The real-world experiments are limited to simple objects like books and boxes, which does not fully address the sim-to-real generalization concerns. Testing on more complex, open-vocabulary categories, such as specific colored objects (e.g., 'red apple', 'yellow toy'), would be more convincing.
3. For open-vocabulary grasping, comparing the proposed 3D representation to baselines like F3RM [4], LERF-TOGO [5], and GaussianGrasper [6] would help validate its advantages.
4. The novelty of the method may fall short for an ICLR submission, as it relies on projecting 2D CLIP or DINO features into 3D points via simple averaging, which is not a new approach. While the authors claim to use a semantic informativeness metric and object-wise fusion, the core mechanism still involves projecting 2D features to 3D, and the improvement over simple averaging needs to be more clearly demonstrated.
5. The results from real-world scenes (Fig. 7) are not particularly impressive; comparisons with recent methods, such as Semantic Gaussians [3] and GaussianGrasper [6], would strengthen the evaluation.

### Questions
See weaknesses

### Soundness
2

### Presentation
2

### Contribution
2
