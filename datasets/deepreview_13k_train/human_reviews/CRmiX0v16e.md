# Open-YOLO 3D: Towards Fast and Accurate Open-Vocabulary 3D Instance Segmentation

- Decision: Accept
- Scores: 8, 5, 8, 8, 10

## Abstract
Recent works on open-vocabulary 3D instance segmentation show strong promise, but at the cost of slow inference speed and high computation requirements. This high computation cost is typically due to their heavy reliance on 3D clip features, which require computationally expensive 2D foundation models like Segment Anything (SAM) and CLIP for multi-view aggregation into 3D. As a consequence, this hampers their applicability in many real-world applications that require both fast and accurate predictions. To this end, we propose a fast yet accurate open-vocabulary 3D instance segmentation approach, named Open-YOLO 3D, that effectively leverages only 2D object detection from multi-view RGB images for open-vocabulary 3D instance segmentation. 
 We address this task by generating class-agnostic 3D masks for objects in the scene and associating them with text prompts.
 We observe that the projection of class-agnostic 3D point cloud instances already holds instance information; thus, using SAM might only result in redundancy that unnecessarily increases the inference time.
We empirically find that a better performance of matching text prompts to 3D masks can be achieved in a faster fashion with a 2D object detector. 
 We validate our Open-YOLO 3D on two benchmarks, ScanNet200 and Replica, 
 under two scenarios: \textit{(i)} with ground truth masks, where labels are required for given object proposals, and \textit{(ii)} with class-agnostic 3D proposals generated from a 3D proposal network.
 Our Open-YOLO 3D achieves state-of-the-art performance on both datasets while obtaining up to $\sim$16$\times$ speedup compared to the best existing method in literature.  
 On ScanNet200 val. set, our Open-YOLO 3D achieves mean average precision (mAP) of 24.7\% while operating at 22 seconds per scene

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces an efficient 3D mask labeling method that leverages multi-view 2D label maps, referred to as Low Granularity (LG) Label Maps, created from 2D object bounding boxes to label 3D instances. The 3D instance (mask) proposals are generated using a pre-trained class-agnostic 3D segmentation method. To address object occlusion across different viewpoints, an Accelerated Visibility Computation (VACC) method is introduced, enabling rapid calculation of visibility matrices using intrinsic and extrinsic parameters.

### Strengths
1. The paper is well-organized, and the ideas are clearly illustrated.
2. This paper introduces a novel approach for efficient open-vocabulary 3D instance labeling by leveraging 2D bounding box priors from a fast 2D object detector, demonstrating superior performance and time efficiency in experimental results.
3. A fast visibility computation algorithm (VAcc) is proposed to accelerate the process of associating 2D label maps with 3D proposals that may be occluded in some views.  This algorithm demonstrates both efficiency and robustness to variations in label map granularity.

### Weaknesses
1. The foundation of the proposed method is built upon the class-agnostic 3D segmentation model, Mask3D, which is used to generate 3D mask proposals. However, this paper lacks sufficient evidence to demonstrate Mask3D's effectiveness and generalizability for open vocabulary instance proposals. Specifically, the paper does not adequately address how Mask3D, trained with category information, can effectively generate proposals for novel, unseen object categories. The reliance on a class-agnostic approach for proposal generation is not fully justified, given that the underlying model utilizes class information during training. The paper should provide a more thorough analysis of Mask3D's limitations in this context.
2. The experimental evaluation of the proposed method for open-vocabulary 3D instance segmentation is relatively limited (only Table 6). The evaluation primarily focuses on a single dataset split, and lacks a comprehensive analysis across diverse datasets or scenarios. The paper would benefit from a more extensive evaluation, including comparisons with a wider range of baselines and a more detailed analysis of the method's performance under varying conditions, such as different levels of occlusion or object complexity.

### Questions
1. In Table 1, does the class-agnostic Mask3D model have access to mask annotations for the same classes as those in the validation set? Do the other methods use the same class-agnostic segmentation model?

2. Since the proposed approach relies on a class-agnostic 3D instance generation model, what are the advantages of using only mask annotations, rather than both instance and label annotations, for training? I mean, are there practical scenarios where only mask annotations are available?

3. What does the tag "(Closed Vocab)" mean in Table 1? Does it indicate that the Mask3D method uses both mask annotations and object class annotations for training?

4. What is the performance of Mask3D (Closed Vocab.) on the Replica dataset?

Minor：

1. In line 092, a comma is missing after "multi-view information".

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
This paper primarily aims to achieve faster open-vocabulary 3D instance segmentation compared with existing methods like OpenMask3D. To realize this target, this work first uses a 3D instance segmentation network to generate segmentation proposals. Then, the output of an open-vocabulary 2D object detector as well as some designed 3D information is employed to derive the categories of these proposals.

### Strengths
1. **[Efficiency]** The experimental results suggest that the proposed method achieves high precision with a significantly better speed compared with most methods, and efficiency is important for practical deployment.

2. **[Clearness]** This paper explains its main contribution, how to assign class predictions to 3D proposals, with great clarity. The implementation details are elaborated sufficiently.

### Weaknesses
1. **[Insufficient Academic Contributions]**: This work just combines the output of a 3D segmentation network and a well-implemented open-vocabulary 2D object detector to realize open-vocabulary 3D object detection (similar to existing open-world segmentation method, just with a replacement of the post network to 2D object detector), which is trivial. It is much faster than previous methods because previous methods are developed based on models like SAM and CLIP. This work employs more efficient and suitable existing models. Therefore, although this work is sound in terms of engineering, its real academic contribution and new insights are plain. The core idea of leveraging 2D detections for 3D segmentation is not novel, and the paper fails to articulate any significant methodological advancements beyond this combination. The approach essentially repurposes existing tools without introducing any novel techniques for handling the inherent challenges of open-vocabulary 3D understanding, such as view inconsistencies or occlusions. The paper lacks a deep analysis of how the chosen 2D detector's limitations impact the overall 3D segmentation performance, which is a critical aspect for a thorough academic contribution.

2. **[Insufficient Ablation Study]** As the method is efficient because it makes good use of existing models, it is important to clearly analyze how these models contribute to the efficiency, which will guide future works on how to develop an efficient open-vocabulary pipeline. However, this work fails to do so. The ablation study should have included a systematic analysis of the impact of different 2D detectors, varying the number of views used for classification, and the effect of different 3D proposal generation methods. Without such analysis, it is difficult to understand the true contribution of each component and how they interact to achieve the reported performance. The current ablation study does not provide sufficient insight into the design choices and their impact on the final results.

3. **[Misleading title]** The method name OPEN-YOLO 3D seems to be unsuitable. YOLO is a 2D object detector while the task is about 3D point cloud segmentation. Although the method utilizes the output of YOLO-World to generate class predictions, the method name is still a little misleading. The title implies a direct adaptation of the YOLO architecture to 3D data, which is not the case. This discrepancy between the title and the actual method can lead to confusion and misinterpretation of the paper's contributions. A more accurate title would better reflect the method's reliance on a 2D detector for 3D segmentation.

### Questions
See weakness.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes Open-YOLO 3D, which is an open-vocabulary 3D instance segmentation framework that efficiently combines 2D object detection and 3D mask generation. The key idea of this paper is its reliance on bounding box predictions from a 2D open-vocabulary object detector and the subsequent use of these predictions for efficient 3D mask proposal and labeling. Unlike prior methods that use computationally intensive models such as SAM and CLIP for feature lifting from 2D to 3D, this paper uses a novel Multi-View Prompt Distribution (MVPDist) and Accelerated Visibility Computation (VAcc) methods to speed up the segmentation process. The framework this paper proposed achieves up to 16x faster inference while keeping competitive or better accuracy.

### Strengths
This paper proposed a novel framework, which uses 2D object detection for 3D instance segmentation. The model they presented reduced computational overhead significantly. The Accelerated Visibility Computation (VAcc) leverages tensor operations and GPU batch processing, enabling highly parallelized visibility computation. This contributes to the following speed improvements without compromising performance. By integrating a high-performing 2D open-vocabulary detector, the framework retains strong zero-shot performance, which is important for real-world applications that use new or unknown object types.

It also includes detailed experiments that showcase Open-YOLO 3D's speech and accuracy, and highlight its performance above state-of-the-art approaches like Open3DIS and OpenMask3D. The paper also includes comprehensive ablation studies to demonstrate the improvement of each component. 

The overall writing is clear and the framework will be beneficial for related research.

### Weaknesses
I like the overall framework this paper presents and appreciate its contribution to 3D instance segmentation by introducing an inference-efficient model, but I still have some concerns about it:

While the paper mentions that VAcc uses tensor operations, a deeper explanation or complexity analysis comparing it to conventional iterative methods would strengthen the understanding of its true computational advantage, and the reason why it can achieve faster inference speed. I believe the paper clearly demonstrates the operation of this proposed algorithm, however, more explanation about why it is efficient and how much computation cost it saves will better demonstrate the paper's contribution.

The method relies on the quality of the 2D object detector, and this might be an issue if the 2D views are suboptimal (for example poor lighting, and occlusions). A more extensive analysis or discussion on how 2D detection failures propagate through the pipeline would add value.

### Questions
Could you provide a more detailed theoretical analysis or complexity comparison of VAcc with the conventional method?
How does the method perform when the 2D object detector encounters difficult conditions, such as poor lighting or significant occlusion, if there's any evaluation of the robustness under such conditions?
What are the potential strategies for mitigating errors from misclassifications made by the 2D object detector, and how do they affect the 3D mask assignments?
I'm also particularly interested in the discussion in your limitation section, I was wondering would integrating fast 2D segmentation models, as mentioned, be feasible within your current framework? How might this affect both performance and speed?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors propose an efficient method for open-vocabulary 3D instance segmentation to enhance the real-time capability. Unlike existing methods that rely on obtaining 2D masks and category labels from 2D foundation models (like SAM and CLIP), the authors propose a novel approach, Open-YOLO3D, which only leverages bounding boxes generated by 2D object detectors. Moreover, the authors propose a Multi-View Prompt Distribution (MVPDist) method to endeavor promising performance in recognition. The experimental results demonstrate the promising real-time performance of the method proposed by the authors.

### Strengths
1.	The authors only utilize the bounding boxes from 2D object detectors to alleviate the redundancy brought by 2D masks, which demonstrates a significant improvement in inference speed compared to OpenMask3D.
2.	The authors propose a Multi-View Prompt Distribution to obtain reliable category labels form 3D masks, the experimental results evaluation on the ScanNet200 and Replica datasets prove the efficiency of the method proposed by the authors.
3.	The paper is well-structured, and the connection between the proposed method and the motivation is coincident.

### Weaknesses
1.	The improvements of the segmentation performance observed in Open-YOLO3D primarily arise from the enhanced category recognition, which is likely from the prior knowledge of the pre-trained YoloWorld model.
2.	The challenges inherent in Open-YOLO3D closely resemble those faced by Open3DIS, as both methods rely on pre-trained models for generating 3D proposals. As discussed in Open3DIS, the pre-trained 3D models have limited capabilities when it comes to detecting uncommon categories. The representation of 3D data for open vocabulary instance segmentation might be uncultivated and limited.
3.	Recent studies [1] have indicated that OpenMask3D performs poorly on certain outdoor datasets, such as NuScenes. Does Open-YOLO3D face similar challenges in effectively identifying sparse-diverse and less common categories in outdoor environments?

### Questions
Please see the weakness.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
10

### Rating Number
10

### Confidence
5

### Summary
This paper aims to deal with the open-vocabulary 3D instance segmentation task with a fast and cost-effective approach by utilizing a YOLO-style design. A Multi-View Prompt Distribution method is proposed to effectively fuse the multi-view information. The low granularity label maps are proposed to only use 2D detectors to predict prompt IDs for 3D instance masks. Experimental results demonstrate the state-of-the-art performance of the proposed method. The speed of the proposed method is about 16 times faster than that of existing methods.

### Strengths
1.	The proposed method is simple yet effective.
2.	The two proposed designs are helpful for 3D instance segmentation with meaningful designs.
3.	The experimental results show that the proposed method could achieve good performance while remaining very efficient.

### Weaknesses
1.	Is it possible to extend the proposed method on panoptic segmentation of 3D scenarios? Please present your design briefly for this.
2.	As shown in Table 1, the inference time of the proposed method is 21.8, which is slower than OpenScene (3D Distill). Please add the explanation for this phenomenon in the corresponding text (first paragraph of Section 5.1).
3.	In Line 405, it should be 4.29 but not 04.29 for OpenScene (3D Distill).

### Questions
Please draw my concerns listed in the Weaknesses part.

### Soundness
3

### Presentation
4

### Contribution
3
