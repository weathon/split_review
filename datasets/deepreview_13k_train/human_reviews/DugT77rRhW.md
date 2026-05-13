# Unposed Sparse Views Room Layout Reconstruction in the Age of Pretrain Model

- Decision: Accept
- Scores: 10, 6, 5, 6

## Abstract
Multiple-perspective images room layout reconstruction is poorly investigated due to the tedious and cumbersome steps that emerge from multi-view geometry, e.g camera intrinsic/extrinsic estimation, image matching, and triangulation. However, with the advancement of the current 3D foundation model DUSt3R, a paradigm shift has occurred in the 3D reconstruction realm, moving from a multi-step Structure-from-motion approach to an end-to-end single-step reconstruction without error accumulation and instability.
To this end, this paper employs the 3D foundation model DUSt3R in the room layout reconstruction task, naming it \ours{}. As the name suggests, \ours{} incorporates the DUSt3R framework and plane representation, then fine-tunes on a room layout dataset (Structure3D). With the uniform and parsimonious results of \ours{}, we can obtain the final room layout with only a single post-processing step and 2D detection results. Compared to previous room layout reconstruction methods, it relaxes the setting from a single perspective/panorama image to multiple perspective images. Moreover, \ours{} solves the task in an end-to-end paradigm without cumbersome steps and accumulated errors. Finally, experiments show that our \ours{} not only surpasses the state-of-the-art on the synthesis dataset Structure3D but also demonstrates the robustness and performs well in real-world cases.

## Human Reviews

## Human Reviewer 1

### Rating
10

### Rating Number
10

### Confidence
4

### Summary
The paper proposes an extension of DUSt3R to room layout reconstruction by retraining and using additional processing steps. Results demonstrate superior performance.

### Strengths
- The method is sound with great results outperforming other methods.
- This is the first method for unposed sparse view room layout reconstruction, especially when the views are not overlapping. 
- The whole idea is interesting, especially to use structural plane depth map and metric scale for DUSt3R. 
- The evaluation is great, especially the design of baselines.
- The paper is well-written and was a pleasure to read.

### Weaknesses
 - Evaluation on more datasets would be more interesting, e.g. CAD-Estate dataset with structural elements annotations.

### Questions
- Figures seem to have low resolution since they are most likely represented as jpg/png images. I recommend using vector graphics instead for better visualisations.

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this work authors propose sparse-view layout reconstruction pipeline that combines existing single view layout methods such as [1] and sparse view 3D reconstruction method Dust3R [2], to generate more accurate 3D layout from sparse images. 

Authors retrained [1] to more accurately detect 2D premitives. They also retrain Dust3R, to only predict layout-plane pointmaps, essentially ignoring foreground furniture. They call this new model Plane-Dust3R. Authors train their PlaneDust3R method on synthetic multi-view Structure3D dataset. And compare accuracy of multiple components of their pipeline, on this synthetic dataset. 

From 2D primitives and 3D plane pointmaps, authors design post-processing pipeline that converts them to 3D plane equations, and their relationships, resulting in full 3D layout representations. 


[1] Yang, Cheng, et al. "Learning to reconstruct 3d non-cuboid room layout from a single rgb image." Proceedings of the IEEE/CVF Winter Conference on Applications of Computer Vision. 2022.

[2] Wang, Shuzhe, et al. "Dust3r: Geometric 3d vision made easy." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2024.

### Strengths
Proposed sparse multi-view layout method is first of its kind. Authors make use of existing methods and retrain them to make them work for their task. 

Overall pipeline is shown to work better than naively combining existing methods such as NonCuboid + Mast3R / NonCuboid + GT Pose. 

Overall paper is well written, is easy to follow. There are many components in the pipeline, but authors explain them in an understandable manner.

### Weaknesses
The big limitation of method is that it is only shown to work on synthetic dataset. While availability of real multi-view layout dataset is scarse, there exists many multi-view 3D datasets (such as ScanNet, ARKit Scene) etc. These datasets have ground-truth depth maps and camera poses that can be used for pseudo ground-truth generation and the proposed method can be compared against other layout reconstruction methods on such dataset. Authors do provide qualitative results on some real-world data, but it is not enough to assess accuracy of method on the real data. If authors can show effectiveness of the method on real data this method can be promising.

Second, I am not convinced as to why PlaneDust3R is needed. If authors take regular Dust3R and use off-the-shelf semantic segmentation to segment walls, floors, and ceilings and use only those points to generate layout (by combining this with NonCuboids + f3 post-processing proposed in the paper), that might also be enough. Retraining method only on synthetic dataset such as Structure3D might reduce their accuracy on the real-world dataset.

### Questions
In Table-2, other datasets results are not useful since this method does not have numbers for those. I would suggest authors to keep results for only structure 3D.

3D precision and recall should be reported at different threshold. I think 15deg threshold is pretty high. Maybe authors should show results at 5deg, 15deg, and 30deg angular thresholds, and similar translation thresholds. This will give more comprehensive view of the methods performance.

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
3

### Summary
This paper introduces Plane-DUSt3R, a method that leverages the DUSt3R framework to estimate structural planes from multi-view images by finetuning on a room layout dataset (Structure3D). This approach allows for room layout estimation with just a single post-processing step and 2D detection results, handling multiple-perspective images. Experimental results show that Plane-DUSt3R outperforms existing methods on synthetic datasets and is robust across various real-world image styles, including cartoons.

### Strengths
1. The major strength of this paper is the first time addressing 3D room layout estimation from multi images by using large reconstruction model s (i.e., DUST3R). 
2. To support using DUST3R, this paper proposed Plane-DUSt3R to estimate structural planes from multi-view images by only require a single post-processing step.
3. Plane-DUSt3R achieves the best performance comparing with the baselines.

### Weaknesses
1. I think the major contribution of the performance boost should go to Dust3R architecture and its pretrained weight, as it is a strong prior model that gives stable and faithful 3D points and camera poses output for Plane-DUSt3R. The paper does not sufficiently analyze the impact of using different backbones or pre-trained models, which could further validate the contribution of the proposed post-processing step. It is unclear how much of the performance gain is due to the novel post-processing versus the inherent capabilities of the DUST3R model.

2. The key model of this paper is only the post-processing step of extracting layout planes, which is, technically speaking, quite incremental. The method essentially takes the point cloud and camera poses from DUST3R and fits planes to them. The novelty of this plane fitting process is not fully explored, and the paper lacks a detailed comparison with other plane fitting algorithms or a discussion on why the chosen method is superior for this specific task. The technical contribution of the post-processing step seems limited, and the paper could benefit from a more in-depth analysis of its design choices.

### Questions
None

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
This work propose Plane-DUSt3R to reconstruct room layout from sparse views with unknown poses. The DUSt3R is retrained to have the amodal perception to see through the occluder and predict floors, walls, ceilings pointmap. The unknown camera parameters can then be estimated from the predicted point map. The outcome from Plane-DUSt3R is then integrated with the other prediction from single-view layout model (e.g., plane instance masks), which is then formulated as a minimum cut problem to produce the final room layout.

### Strengths
+ This work introduce state-of-the-art geomety prediction model, DUSt3R, into the classical layout estimation task, solving an underexplored aspect with sparse views and unknown poses.
+ The problem formulation in Sec.3.1 is clear and fluent, which unifies previous room layout estimator in a single pipeline and help readers understand how the propose method augments the existing pipeline.
+ A new benchamrk with some reasonable baselines is constructed for this task.

### Weaknesses
 - In Table2, the performance by the proposed method on Co3Dv2 and RealEstate10K are missing. It's reasonable that DUSt3R and MASt3R perform worse as they didn't trained on the synthetic Structured3D dataset. What about the generalized performance of the proposed Plane-DUSt3R on the other real-world dataset?

- It's a pity that the proposed Plane-DUSt3R is only trained and mainly evaluated on the synthetic Structured3D dataset. There are many existing resource with multiview and room layout annotation on the 360 panorama domain, e.g., ZInD has multiview layout on unfurnished rooms, MP3DLayout has single-view layout annotation but the source Matterport3D also offer nearby views. Gather more data by projecting these 360 to perspective can make this work much stronger.
  - [1] Zillow Indoor Dataset: Annotated Floor Plans With 360º Panoramas and 3D Room Layouts
  - [2] Manhattan Room Layout Reconstruction from a Single 360° image: A Comparative Study of State-of-the-art Methods

- The qualitative comparison in Fig.6 and Fig.8 is unfair to the baseline. In the fourth column, the baseline "Noncuboid+MASt3R" is presented without texture. We can then easily spot one big issue that some of the walls are duplicated and misaligned. However, in the final column, the layout wireframe from the proposed method is hiding by the rgb point cloud, making it difficult to judge if the similar issue happend to the proposed method as well.

- Too few qualitative results. On the in-domain Structured3D dataset, only two are provided in Fig.6. The additional three in supp's Fig.9 also has two duplicated scenes from Fig.6. In application of room tour and room demo, the final visual outcome is what we really care about while the improvement on number is sometimes hard to interpret how it affect the final visual. In addition, some more visualization, espeically on the failure cases, may can provide some hint for future work to further improve.

### Questions
Seems that Sec3 only covers camera poses. Is the camera intrinsic also estimated as in DUSt3R or assumed to be known in this work?

How the accuracy vary with the number of input views? Is the performance scalable with more input views?

### Soundness
2

### Presentation
3

### Contribution
3
