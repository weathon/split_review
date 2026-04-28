# Semantic Flow: Learning Semantic Fields of Dynamic Scenes from Monocular Videos

- Decision: Accept
- Avg Score: 6.33
- Scores: 6, 8, 5

## Abstract
In this work, we pioneer Semantic Flow, a neural semantic representation of dynamic scenes from monocular videos. 
In contrast to previous NeRF methods that reconstruct dynamic scenes from the colors and volume densities of individual points, 
Semantic Flow learns semantics from continuous flows that contain rich 3D motion information. 
As there is 2D-to-3D ambiguity problem in the viewing direction when extracting 3D flow features from 2D video frames,
we consider the volume densities as opacity priors that describe the contributions of flow features to the semantics on the frames. 
More specifically, we first learn a flow network to predict flows in the dynamic scene, and propose a flow feature aggregation module to extract flow features from video frames.
Then, we propose a flow attention module to extract motion information from flow features, which is followed by a semantic network to output semantic logits of flows. We integrate the logits with
volume densities in the viewing direction to supervise the flow features with semantic labels on video frames.
Experimental results show that our model is able to learn from multiple dynamic scenes and supports a series of new tasks such as instance-level scene editing, semantic completions, dynamic scene tracking and semantic adaption on novel scenes.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces learning a semantic field of the dynamic scene using NeRF given a monocular video. Given a sequence of input frames from a monocular video, precomputed optical flow, their Dynamic NeRF learns a semantic field so that it can render a semantic segmentation map at novel views. The method can be used for a couple of applications that output semantic field for unseen frames given partial frames.

### Strengths
- Better accuracy over baseline methods

  Compared to the two baselines, the method shows better accuracy on multiple tasks (scene completion, scene tracking, and semantic representation) in Table 1 and Table 2. Also it demonstrates better qualitative results in Fig. 3

- New applications

  The paper proposes interesting new applications, both dynamic scene tracking and completion that estimates semantic maps on unseen frames. (Fig. 1)

### Weaknesses
 - Outdated baselines

  The paper compares their method with a couple of baselines (DynNeRF and MonoNeRF) but those are a bit limited. There are many other baselines for the dynamic NeRF task such as D-NeRF, RoDynRF, NSFF (Neural Scene Flow Field), etc. It would have been great if the paper provided accuracy on more baseline methods to make the comparison much fairer.

- A bit difficult to follow the equations (from Eq. (4) to Eq. (8))

  I am wondering if it's possible to put the mathematic notation from Eq. (4) to Eq. (8) into Fig. 2 for better understanding.

- Clarity 

  Some parts of the paper have lack of clarity and make it hard to understand clearly. What is the meaning of '25%/50% semantic labels' in Fig. 3? I wonder if the paper can provide more details in the figure captions. How are the 25%/50% determined? 

- Marginal accuracy improvement in Fig. 4

  The choice of low displacement seems not so critical for the accuracy gain. Maybe it would be good to have a justification or discussion on the result.

### Questions
- How much does the accuracy of the method depend on the off-the-shelf optical flow methods? Can it be critical?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper looks to solve the problem related to generating a novel view 2D semantic map, for dynamic scenes using continuous flow. Paper leverages optical flow for the foreground part of the images and uses volume density as a prior to determining flow feature contribution towards semantics. Authors evaluate this on Dynamic scene dataset.

### Strengths
Strengths:
-The paper is well written with the objective clearly identified. It is structured well and has logically moving sub-section-wise explanations. 
-Tackles a well-known problem in terms of generating novel view synthesis for dynamic scenes, but for semantics.
- Proposes a novel idea, that leverages optical flow to predict semantic labels for dynamic foreground pixels/regions.
- Evaluate and compare the model on the Dynamic Scene Dataset.

### Weaknesses
Weakness:
- Paper leverages optical flow output as one of the intermediate steps, but fails to discuss its shortcomings and how exactly do they handle occlusion and disocclusion related to both dynamic and static regions of the frame. Specifically, the paper does not address how inaccuracies in optical flow, especially at object boundaries or in regions with significant depth discontinuities, affect the semantic prediction. The reliance on potentially noisy flow fields could introduce artifacts or inconsistencies in the generated semantic maps. Furthermore, the paper lacks a discussion on how the method handles cases where optical flow fails completely, such as with fast-moving objects or significant changes in lighting.
- For the most part of the paper, the authors only compare with two dynamic scene-based works, Considering other related works in dynamic scene reconstruction, Would be great to see comparative baseline results, with a few more of these models with semantic head. The limited comparison makes it difficult to assess the true performance and novelty of the proposed approach against a broader range of existing techniques. Including comparisons with methods that incorporate explicit 3D reasoning or those that use different forms of motion cues would provide a more comprehensive evaluation.

### Questions
- Could Authors share some of the shortcomings (a few qualitative results) which may be due to imperfect flow prediction, which results in bad performance during inference?
- In Section 3.4: while calculating Semantic Consistency Constraint; Do we generate some sort of valid mask here to enforce the semantic consistency or is it done for all pixels, irrespective of occlusion or uncertainty?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper the problem of novel view synthesis of semantic labels is studied. Rather than rendering colour, the segmentation is rendered with a NeRF model. The authors propose a model and training procedure that can learn scene flow fields and semantic renderings of a given video sequence. Furthermore, the proposed method allows for quick adaptation on novel video sequences. Since no earlier work studies this problem, the authors label the nvidia dynamic scenes dataset with pixel-wise semantic labels. The experiments show that the semantic labels can be rendered accurately, and furthermore that we do not need labels for all frames in a sequence, and that we can use the semantic labels to mask out specific parts of the video and render it without specific objects.

### Strengths
- There is no existing dataset for the problem setup, so authors annotated the nvidia dynamic scenes dataset with pixel-wise semantic segmentation labels.
- A strength of the method is that it allows for quick adaptation to new scenes, e.g. with just 500 iterations it can perform well given pre-training on other scenes. The reason is that the scene flow field is not learned from scratch, but rather from frame-wise video features, which does not need to be learned from scratch for each scene.
- Augmenting NeRF models with semantic segmentation has been done for static scenes (e.g. Zhi et al 2021) but to the best of my knowledge not for general dynamic scenes, so the paper tackles a new problem setup.
- The method is clearly described and ablations are provided for the main components.

### Weaknesses
 - There are some baselines that would be reasonable to try that are missing from the paper. For instance, if we just render the rgb images with any NeRF method (e.g. MonoNeRF) and apply some video object segmentation algorithm (e.g. any top-performing method on the DAVIS dataset) or semantic segmentation method (trained on some dataset with overlapping labels), how well would that perform?
- Since one of the applications mentioned in the paper is scene editing, i.e. removing some specific object, it is necessary to not just render semantics correctly but also rgb. There are no values provided for the standard novel view synthesis metrics (PSNR, SSIM, LPIPS) for rgb on the tested video sequences.
- It would have been interesting to somehow visualise or discuss the flow fields. Since the objective is semantic rendering rather than colour rendering it is not clear if we need the scene flow to map to the same specific part of an object, or if it is sufficient or even beneficial to just map to anywhere within the same object. For instance, the consistency loss L_consis only enforces that points along flow trajectories should have the same label.

Minor issues:
- Missing related work: “Panoptic neural fields: A semantic object-aware neural scene representation” (CVPR 2022) also considers novel view synthesis for semantic segmentation from a video, although their method is limited to non-deformable dynamic objects.
- Page 5: Does ground truth flow mean optical flow estimated from RAFT? If that is the case it should not be called ground truth.
- Page 5: The closing parenthesis in eq. (7) is probably incorrect.
- Page 8: “Boundray” typo
- Page 8: Table 2 caption: “qualitative” should be “quantitative”

### Questions
See everything under weaknesses.
- When training for semantic completion or tracking, only a subset of the frames are used for semantic supervision. Is the same true for RGB supervision or are all frames used for that? 
- In Fig. 3, what are the indices of the frames that are shown? How far are they from the frames with semantic labels?
- For the DynNeRF and MonoNeRF baselines, what exactly is the input to the semantic heads that are learned?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
